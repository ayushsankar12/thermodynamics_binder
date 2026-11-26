#!/usr/bin/env python3
"""Production Build Orchestrator for Science Olympiad 2026-2027 Division C Thermodynamics Binder.

Usage:
    python build/build.py                         # build main binder
    python build/build.py --target all            # build main + gray + quickref + device
    python build/build.py --all                   # alias for --target all
    python build/build.py --target main|gray|quickref|device
    python build/build.py --workdir build/smoke --tex test_style --job test_style

Pipeline per target:
  - Main / Gray: pdflatex -> makeindex (all 5 named .idx with binder.ist) -> pdflatex -> makeindex -> pdflatex (+ up to 2 settle passes)
  - Companion (quickref / device): generates booklet-ext.aux from main.aux, runs 3 pdflatex passes with \\def\\companionmode{1}
Appends structured summaries to build/build-log.txt and exits nonzero on hard LaTeX errors.
"""
import argparse, os, re, shutil, subprocess, sys, time
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

BUILD_DIR = Path(__file__).resolve().parent
ROOT = BUILD_DIR.parent
SRC = ROOT / "src"
OUT = ROOT / "output"
LOG = BUILD_DIR / "build-log.txt"

MIKTEX = Path(os.environ.get("LOCALAPPDATA", "")) / "Programs/MiKTeX/miktex/bin/x64"
if MIKTEX.exists():
    os.environ["PATH"] = str(MIKTEX) + os.pathsep + os.environ["PATH"]

# Target registry: target_key -> (tex_stem, jobname, output_pdf_name, pre_tex_hook, is_companion)
TARGETS = {
    "main":     ("main",            "main",            "Thermodynamics_DivC_Binder.pdf",                 None,                        False),
    "gray":     ("main",            "main-gray",       "Thermodynamics_DivC_Binder_GRAYSCALE_PROOF.pdf", r"\def\grayproof{1}",        False),
    "quickref": ("quickref_12pp",   "quickref_12pp",   "Thermodynamics_DivC_QuickRef_12pp.pdf",          r"\def\companionmode{1}",    True),
    "device":   ("device_handbook", "device_handbook", "Thermodynamics_DivC_Device_Handbook.pdf",        r"\def\companionmode{1}",    True),
}

NAMED_INDICES = ("topic", "formula", "figure", "error", "devfail")
NEWLABEL = re.compile(r"^\\newlabel\{([^}]*)\}")
MATH_MACRO_RE = re.compile(
    r"\\(?:mathrm|frac|sqrt|Delta|tau|kappa|lambda|alpha|beta|gamma|sigma|varepsilon|eta|mu|rho|pi|ln|exp|ge|le|to|cdot|times|pm|infty|partial|nabla|sum|prod|int|oint)\b"
)

def _sanitize_outside_math(seg: str) -> str:
    seg = seg.replace("##", r"\#")
    seg = re.sub(r"(?<!\\)#", r"\#", seg)
    seg = re.sub(r"(?<!\\)%", r"\%", seg)
    seg = re.sub(r"(?<!\\)&", r"\&", seg)
    if ": " in seg:
        pre, post = seg.split(": ", 1)
        if (MATH_MACRO_RE.search(post) or "_{" in post or "^{" in post) and "$" not in post:
            pre = _sanitize_outside_math(pre)
            return f"{pre}: ${post.strip()}$"
    if MATH_MACRO_RE.search(seg) or "_{" in seg or "^{" in seg:
        if seg.lstrip().startswith(("\\", "F_{", "V(", "T(", "C''")):
            return f"${seg.strip()}$"
    seg = re.sub(r"(?<!\\)_", r"\_", seg)
    seg = re.sub(r"(?<!\\)\^", r"\\textasciicircum{}", seg)
    return seg

def _sanitize_ind_line(ln: str) -> str:
    if not (ln.lstrip().startswith(r"\item") or ln.lstrip().startswith(r"\subitem")):
        return ln
    if r"\dotfill" in ln:
        head, tail = ln.split(r"\dotfill", 1)
        tail = r"\dotfill" + tail
    else:
        head, tail = ln, ""
    m_cmd = re.match(r"^(\s*\\(?:sub)*item\s+)(.*)$", head)
    if not m_cmd:
        return ln
    prefix, body = m_cmd.group(1), m_cmd.group(2)
    parts = re.split(r"(\$[^$]*\$)", body)
    new_parts = [p if p.startswith("$") else _sanitize_outside_math(p) for p in parts]
    return prefix + "".join(new_parts) + tail

def sanitize_ind_files(workdir: Path):
    for ind in sorted(workdir.glob("*.ind")):
        lines = ind.read_text(encoding="utf-8", errors="replace").splitlines()
        cleaned = [_sanitize_ind_line(ln) for ln in lines]
        ind.write_text("\n".join(cleaned) + "\n", encoding="utf-8")

def sync_style_files(workdir: Path):
    """Ensure thermobinder.sty and binder.ist are directly accessible in workdir."""
    workdir.mkdir(parents=True, exist_ok=True)
    for fname in ("thermobinder.sty", "binder.ist"):
        src_file = BUILD_DIR / fname
        dst_file = workdir / fname
        if src_file.exists() and src_file.resolve() != dst_file.resolve():
            shutil.copy2(src_file, dst_file)

def run(cmd, cwd: Path):
    env = os.environ.copy()
    # os.pathsep (';' on Windows, ':' on macOS/Linux); the trailing empty entry keeps kpathsea's default path.
    sep = os.pathsep
    env["TEXINPUTS"] = f"{BUILD_DIR}{sep}{cwd}{sep}" + env.get("TEXINPUTS", "")
    p = subprocess.run(cmd, cwd=cwd, env=env, capture_output=True, text=True, encoding="utf-8", errors="replace")
    return p.returncode, p.stdout + p.stderr

def pdflatex(workdir: Path, texname: str, jobname: str, pre: str | None = None):
    arg = (pre or "") + r"\input{" + texname + "}"
    return run(["pdflatex", "-interaction=nonstopmode", "-file-line-error", f"-jobname={jobname}", arg], workdir)

def makeindexes(workdir: Path):
    done = []
    ist = "binder.ist" if (workdir / "binder.ist").exists() else str(BUILD_DIR / "binder.ist")
    idx_files = sorted(workdir.glob("*.idx"))
    for idx in idx_files:
        rc, _ = run(["makeindex", "-q", "-s", ist, idx.name], workdir)
        done.append(f"{idx.stem}:{rc}")
    sanitize_ind_files(workdir)
    return done

def write_ext_aux(workdir: Path, exclude=frozenset()):
    """Write booklet-ext.aux from main.aux minus labels defined by the companion booklet itself."""
    main_aux = workdir / "main.aux"
    lines = []
    if main_aux.exists():
        for ln in main_aux.read_text(encoding="utf-8", errors="replace").splitlines():
            m = NEWLABEL.match(ln)
            if m and m.group(1) not in exclude and m.group(1) not in ("LastPage", "LastContentPage"):
                lines.append(ln)
    (workdir / "booklet-ext.aux").write_text("\\relax\n" + "\n".join(lines) + "\n", encoding="utf-8")
    return len(lines)

def own_labels(workdir: Path, jobname: str):
    aux = workdir / f"{jobname}.aux"
    if not aux.exists():
        return set()
    return {m.group(1) for ln in aux.read_text(encoding="utf-8", errors="replace").splitlines() if (m := NEWLABEL.match(ln))}

def summarize(workdir: Path, jobname: str):
    logf = workdir / f"{jobname}.log"
    txt = logf.read_text(encoding="utf-8", errors="replace") if logf.exists() else ""
    errors = re.findall(r"^.*?:\d+: .*$", txt, flags=re.M)
    # LaTeX 2025-11 kernel sets \ignoreprimitiveerror on longtable \vsplit checks; filter harmless notes
    ignored = [e for e in errors if "ignored error: Infinite glue shrinkage" in e]
    errors = [e for e in errors if e not in ignored]
    fatal_bang = re.findall(r"^! (?:LaTeX Error|Emergency stop|Undefined control sequence).*$", txt, flags=re.M)
    for fb in fatal_bang:
        if not any(fb in e for e in errors):
            errors.append(fb)
    undef = re.findall(r"LaTeX Warning: (?:Reference|Citation) `([^']+)' .*undefined", txt)
    multi = re.findall(r"LaTeX Warning: Label `([^']+)' multiply defined", txt)
    overfull_h = [float(x) for x in re.findall(r"Overfull \\hbox \((\d+\.\d+)pt too wide\)", txt)]
    big_over_h = [x for x in overfull_h if x > 3.0]
    overfull_v = [float(x) for x in re.findall(r"Overfull \\vbox \((\d+\.\d+)pt too high\)", txt)]
    skipped = re.findall(r"BINDER-SKIPPED (\S+)", txt)
    pages = None
    m = re.search(r"Output written on .*?\((\d+) pages", txt)
    if m:
        pages = int(m.group(1))
    return {
        "errors": errors,
        "ignored": ignored,
        "undef": sorted(set(undef)),
        "multi": sorted(set(multi)),
        "overfull_h": len(overfull_h),
        "big_overfull_h": big_over_h,
        "overfull_v": overfull_v,
        "skipped": skipped,
        "pages": pages,
    }

def build_job(workdir: Path, target_label: str, texname: str, jobname: str, outname: str | None, pre: str | None, is_companion: bool, copy_to_output: bool = True):
    sync_style_files(workdir)
    tex_path = workdir / f"{texname}.tex"
    if not tex_path.exists():
        msg = f"=== {time.strftime('%Y-%m-%d %H:%M:%S')} target={target_label} SKIPPED ({tex_path} not found)"
        print(msg)
        return None
    t0 = time.time()
    idx_report = []
    if is_companion:
        had_aux = (workdir / f"{jobname}.aux").exists()
        prev_ext = (workdir / "booklet-ext.aux").read_text(encoding="utf-8", errors="replace") if (workdir / "booklet-ext.aux").exists() else ""
        write_ext_aux(workdir, own_labels(workdir, jobname))
        rc1, _ = pdflatex(workdir, texname, jobname, pre)
        write_ext_aux(workdir, own_labels(workdir, jobname))
        new_ext = (workdir / "booklet-ext.aux").read_text(encoding="utf-8", errors="replace")
        logf = workdir / f"{jobname}.log"
        logtxt = logf.read_text(encoding="utf-8", errors="replace") if logf.exists() else ""
        need_p2 = (not had_aux) or (new_ext != prev_ext) or ("Rerun to get" in logtxt) or ("Label(s) may have changed" in logtxt) or ("undefined" in logtxt)
        if need_p2:
            rc2, _ = pdflatex(workdir, texname, jobname, pre)
            logtxt = logf.read_text(encoding="utf-8", errors="replace") if logf.exists() else ""
            if "Rerun to get" in logtxt or "Label(s) may have changed" in logtxt:
                rc3, _ = pdflatex(workdir, texname, jobname, pre)
            else:
                rc3 = rc2
        else:
            rc2 = rc3 = rc1
    elif target_label == "gray" and (workdir / "main.aux").exists():
        for ext in (".aux", ".toc", ".out"):
            src_a = workdir / f"main{ext}"
            if src_a.exists():
                shutil.copy2(src_a, workdir / f"{jobname}{ext}")
        idx_report = makeindexes(workdir)
        rc1, _ = pdflatex(workdir, texname, jobname, pre)
        rc2 = rc3 = rc1
    else:
        had_aux = (workdir / f"{jobname}.aux").exists()
        prev_inds = {p.name: p.read_text(encoding="utf-8", errors="replace") for p in workdir.glob("*.ind")}
        rc1, _ = pdflatex(workdir, texname, jobname, pre)
        idx_report = makeindexes(workdir)
        new_inds = {p.name: p.read_text(encoding="utf-8", errors="replace") for p in workdir.glob("*.ind")}
        logf = workdir / f"{jobname}.log"
        logtxt = logf.read_text(encoding="utf-8", errors="replace") if logf.exists() else ""
        need_p2 = (not had_aux) or (new_inds != prev_inds) or ("Rerun to get" in logtxt) or ("Label(s) may have changed" in logtxt) or ("undefined" in logtxt)
        if need_p2:
            rc2, _ = pdflatex(workdir, texname, jobname, pre)
            idx_report = makeindexes(workdir)
            logtxt = logf.read_text(encoding="utf-8", errors="replace") if logf.exists() else ""
            if "Rerun to get" in logtxt or "Label(s) may have changed" in logtxt:
                rc3, _ = pdflatex(workdir, texname, jobname, pre)
                for _ in range(2):
                    logtxt = logf.read_text(encoding="utf-8", errors="replace") if logf.exists() else ""
                    if "Rerun to get" not in logtxt and "Label(s) may have changed" not in logtxt:
                        break
                    idx_report = makeindexes(workdir)
                    rc3, _ = pdflatex(workdir, texname, jobname, pre)
            else:
                rc3 = rc2
        else:
            rc2 = rc3 = rc1

    s = summarize(workdir, jobname)
    pdf = workdir / f"{jobname}.pdf"
    if copy_to_output and outname and pdf.exists():
        OUT.mkdir(parents=True, exist_ok=True)
        shutil.copy2(pdf, OUT / outname)
    dt = time.time() - t0
    lines = [
        f"=== {time.strftime('%Y-%m-%d %H:%M:%S')} target={target_label} job={jobname} rc=({rc1},{rc2},{rc3}) pages={s['pages']} time={dt:.2f}s",
        f"  errors={len(s['errors'])} undefined_refs={len(s['undef'])} multiply_defined={len(s['multi'])} "
        f"overfull_hbox={s['overfull_h']} (>3pt: {len(s['big_overfull_h'])}) overfull_vbox={len(s['overfull_v'])} "
        f"indices={idx_report} skipped_inputs={len(s['skipped'])} known_upstream_notes={len(s['ignored'])}"
    ]
    for e in s["errors"][:25]:
        lines.append("  ERR " + e)
    for u in s["undef"][:40]:
        lines.append("  UNDEF " + u)
    for u in s["multi"][:20]:
        lines.append("  MULTI " + u)
    if s["skipped"]:
        lines.append("  SKIPPED " + " ".join(s["skipped"]))
    msg = "\n".join(lines)
    LOG.parent.mkdir(parents=True, exist_ok=True)
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(msg + "\n")
    print(msg)
    return s

def main():
    ap = argparse.ArgumentParser(description="Build Thermodynamics Div C Binder & Companion PDFs.")
    ap.add_argument("--target", default="main", choices=[*TARGETS.keys(), "all"])
    ap.add_argument("--all", action="store_true", help="Build all 4 targets (main, gray, quickref, device)")
    ap.add_argument("--workdir", default=None, help="Override LaTeX working directory (defaults to src/)")
    ap.add_argument("--tex", default=None, help="Compile a specific .tex stem inside --workdir")
    ap.add_argument("--job", default=None, help="Override jobname when --tex is specified")
    ap.add_argument("--gray", action="store_true", help="Pass \\def\\grayproof{1} when using --tex")
    ap.add_argument("--companion", action="store_true", help="Pass \\def\\companionmode{1} when using --tex")
    args = ap.parse_args()

    workdir = Path(args.workdir).resolve() if args.workdir else SRC

    if args.tex:
        tex_stem = args.tex[:-4] if args.tex.endswith(".tex") else args.tex
        job = args.job or (f"{tex_stem}-gray" if args.gray else tex_stem)
        pre = ""
        if args.gray:
            pre += r"\def\grayproof{1}"
        if args.companion:
            pre += r"\def\companionmode{1}"
        s = build_job(workdir, job, tex_stem, job, None, pre or None, args.companion, copy_to_output=False)
        sys.exit(1 if (s is None or s["errors"]) else 0)

    target_list = list(TARGETS.keys()) if (args.all or args.target == "all") else [args.target]
    bad = False
    ran_any = False
    for t in target_list:
        texname, jobname, outname, pre, is_comp = TARGETS[t]
        s = build_job(workdir, t, texname, jobname, outname, pre, is_comp, copy_to_output=True)
        if s is None:
            if len(target_list) == 1:
                bad = True
            continue
        ran_any = True
        bad |= bool(s["errors"])
    sys.exit(1 if (bad or not ran_any) else 0)

if __name__ == "__main__":
    main()
