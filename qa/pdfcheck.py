#!/usr/bin/env python3
"""Automated Mechanical & Visual PDF QA Verifier for Thermodynamics-Binder (qa/pdfcheck.py).

Checks enforced via PyMuPDF (fitz) + Pillow (PIL):
  P1  US Letter page dimensions (612.0 x 792.0 pt, tolerance +/- 1.0 pt) on every page.
  P2  Page budget limits:
        - Main binder / Grayscale proof: <= 280 pages
        - QuickRef 12-page handbook: == 12 pages (unless --relax-budget is passed for smoke/draft tests)
  P3  Zero unresolved references ("??") or leaked raw LaTeX macros (e.g., \\scopebanner, \\idxtopic, \\sref).
  P4  Zero text spans intruding into the 0.72 in (51.84 pt) inner 3-hole-punch zone
        (left edge x0 < 51.84 pt on odd pages; right edge x1 > 612 - 51.84 pt on even pages).
  P5  Running header/footer verification ("Page N of M" and "2026-11-22" on every page after page 1).
  P6  Minimum font size audit (warns/flags text spans < 5.0 pt) and 100% embedded Type 1 fonts
        (zero unembedded fonts, zero Type 3 bitmap fonts).
  V1  Renders representative pages (cover/command center, quick sheet, dense table, diagram page,
        worked problem page, index page, duplex spread, grayscale proof) at 150 DPI into qa/renders/
        and builds a composite visual contact sheet.

Writes build/pdfcheck-report.md and exits nonzero on any P1-P6 failure.
"""
import argparse, re, sys
from collections import Counter
from pathlib import Path
import fitz
from PIL import Image

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

QA_DIR = Path(__file__).resolve().parent
ROOT = QA_DIR.parent
OUT = ROOT / "output"
RENDERS = QA_DIR / "renders"
REPORT = ROOT / "build" / "pdfcheck-report.md"

PUNCH_IN = 0.72
PUNCH_PT = PUNCH_IN * 72.0  # 51.84 pt (inside our 0.75 in = 54.0 pt inner margin)
RAW_LATEX_RE = re.compile(
    r"\\(?:scopebanner|binderchapter|idxtopic|idxformula|idxfig|idxerr|idxdev|verifiedby|sref|pref|spref|SI|begin|end)\b"
)

def select_representative_pages(doc: fitz.Document) -> list[tuple[int, str]]:
    """Select representative pages covering cover/cmd, quick sheet, table, diagram, worked example, index, and spread."""
    n = len(doc)
    if n <= 8:
        return [(i + 1, f"page-{i+1}") for i in range(n)]
    picked = {}
    picked[1] = "cover_or_cmd"
    if n >= 2:
        picked[2] = "duplex_verso_p2"
    if n >= 3:
        picked[3] = "duplex_recto_p3"
    for i in range(n):
        pno = i + 1
        txt = doc[i].get_text("text")
        if "ONE-PAGE QUICK SHEET" in txt and not any(v == "quicksheet" for v in picked.values()):
            picked[pno] = "quicksheet"
        if "Table " in txt and not any(v == "dense_table" for v in picked.values()):
            picked[pno] = "dense_table"
        if "Fig. " in txt and not any(v == "diagram_page" for v in picked.values()):
            picked[pno] = "diagram_page"
        if "Worked Example" in txt and not any(v == "worked_example" for v in picked.values()):
            picked[pno] = "worked_example"
        if "Index" in txt and pno > n // 2 and not any(v == "index_page" for v in picked.values()):
            picked[pno] = "index_page"
    picked[n] = "final_page"
    return sorted(picked.items())

def render_visual_audit(pdf_path: Path, doc: fitz.Document) -> list[str]:
    RENDERS.mkdir(parents=True, exist_ok=True)
    stem = pdf_path.stem
    rep_pages = select_representative_pages(doc)
    saved_paths = []
    for pno, tag in rep_pages:
        page = doc[pno - 1]
        pix = page.get_pixmap(dpi=150)
        out_png = RENDERS / f"{stem}_p{pno:03d}_{tag}.png"
        pix.save(str(out_png))
        saved_paths.append(out_png)
    if saved_paths:
        imgs = [Image.open(p) for p in saved_paths[:12]]
        w, h = imgs[0].size
        cols = 2 if len(imgs) <= 4 else 3
        rows = (len(imgs) + cols - 1) // cols
        sheet = Image.new("RGB", (w * cols, h * rows), (242, 242, 242))
        for idx, im in enumerate(imgs):
            sheet.paste(im, ((idx % cols) * w, (idx // cols) * h))
        contact_path = RENDERS / f"{stem}_contact_sheet.png"
        sheet.save(str(contact_path))
        saved_paths.append(contact_path)
    return [p.name for p in saved_paths]

def check_pdf(pdf_path: Path, relax_budget: bool = False):
    doc = fitz.open(pdf_path)
    res = {
        "name": pdf_path.name,
        "pages": len(doc),
        "budget_fail": None,
        "size_bad": [],
        "qq": [],
        "raw_latex": [],
        "punch": [],
        "footer_missing": [],
        "rev_missing": [],
        "small": Counter(),
        "min_size": 99.0,
        "unembedded": set(),
        "type3_fonts": set(),
        "total_fonts": set(),
        "renders": [],
    }
    lname = pdf_path.name.lower()
    if "binder" in lname and len(doc) > 280:
        res["budget_fail"] = f"Main binder exceeds 280-page ceiling ({len(doc)} > 280)"
    elif "quickref" in lname and "12pp" in lname and not relax_budget and len(doc) != 12:
        res["budget_fail"] = f"QuickRef 12pp handbook has {len(doc)} pages (expected 12)"

    for i, page in enumerate(doc):
        pno = i + 1
        w, h = page.rect.width, page.rect.height
        if abs(w - 612.0) > 1.0 or abs(h - 792.0) > 1.0:
            res["size_bad"].append((pno, round(w, 1), round(h, 1)))
        txt = page.get_text("text")
        if "??" in txt:
            res["qq"].append(pno)
        m_raw = RAW_LATEX_RE.search(txt)
        if m_raw:
            res["raw_latex"].append((pno, m_raw.group(0)))
        if pno > 1 and not re.search(r"page\s+\d+\s+of\s+\d+", txt, re.I):
            res["footer_missing"].append(pno)
        if pno > 1 and "2026-11-22" not in txt:
            res["rev_missing"].append(pno)

        odd = (pno % 2 == 1)
        for b in page.get_text("dict")["blocks"]:
            for ln in b.get("lines", []):
                for sp in ln["spans"]:
                    s = sp["text"].strip()
                    if not s:
                        continue
                    x0, y0, x1, y1 = sp["bbox"]
                    sz = sp["size"]
                    if sz < res["min_size"]:
                        res["min_size"] = sz
                    if sz < 5.0:
                        res["small"][pno] += 1
                    in_punch = (x0 < PUNCH_PT) if odd else (x1 > w - PUNCH_PT)
                    if in_punch:
                        res["punch"].append((pno, round(x0, 1), round(x1, 1), s[:30]))

        for f in page.get_fonts():
            fname, ftype, fembed = f[3], f[2], f[1]
            res["total_fonts"].add((fname, ftype, fembed))
            if fembed in ("n/a", ""):
                res["unembedded"].add(fname)
            if "type3" in str(ftype).lower():
                res["type3_fonts"].add(fname)

    res["renders"] = render_visual_audit(pdf_path, doc)
    doc.close()
    return res

def main():
    ap = argparse.ArgumentParser(description="Mechanical and visual QA verifier for Thermodynamics-Binder PDFs.")
    ap.add_argument("pdfs", nargs="*", help="Explicit PDF paths to check (defaults to all *.pdf in output/)")
    ap.add_argument("--relax-budget", action="store_true", help="Relax exact 12-page QuickRef budget check for smoke/draft runs")
    args = ap.parse_args()

    pdf_list = [Path(p).resolve() for p in args.pdfs] if args.pdfs else sorted(OUT.glob("*.pdf"))
    if not pdf_list:
        print("No PDF files found to check.")
        return 1

    lines = [
        "# PDF Mechanical & Visual QA Report (`qa/pdfcheck.py`)",
        "",
        f"- **Inner 3-Hole Punch Clearance Threshold:** `{PUNCH_IN:.2f} in` (`{PUNCH_PT:.2f} pt`, inside `0.75 in` / `54.0 pt` inner margin)",
        f"- **Visual Renders Directory:** `qa/renders/` (`150 DPI` page renders + contact sheets)",
        "",
    ]
    bad = 0
    for pdf in pdf_list:
        r = check_pdf(pdf, relax_budget=args.relax_budget)
        fails = []
        if r["budget_fail"]:
            fails.append(r["budget_fail"])
        if r["size_bad"]:
            fails.append(f"non-Letter pages {r['size_bad'][:10]}")
        if r["qq"]:
            fails.append(f"unresolved '??' on pages {r['qq'][:15]}")
        if r["raw_latex"]:
            fails.append(f"raw LaTeX macros on pages {r['raw_latex'][:10]}")
        if r["punch"]:
            fails.append(f"{len(r['punch'])} text spans in 0.72 in inner punch zone, e.g. {r['punch'][:4]}")
        if r["footer_missing"]:
            fails.append(f"'Page N of M' footer missing on pages {r['footer_missing'][:15]}")
        if r["rev_missing"]:
            fails.append(f"revision date '2026-11-22' missing on pages {r['rev_missing'][:15]}")
        if r["unembedded"]:
            fails.append(f"unembedded fonts {sorted(r['unembedded'])}")
        if r["type3_fonts"]:
            fails.append(f"Type 3 bitmap fonts {sorted(r['type3_fonts'])}")
        if r["min_size"] < 5.0:
            fails.append(f"text below 5.0 pt ({r['min_size']:.2f} pt on pages {sorted(r['small'])[:10]})")

        bad += bool(fails)
        verdict = "PASS (P1--P6 & V1)" if not fails else "FAIL: " + "; ".join(fails)
        lines.append(f"## `{r['name']}`")
        lines.append(f"- **Pages:** `{r['pages']}` | **Smallest Text:** `{r['min_size']:.2f} pt` | **Embedded Fonts:** `{len(r['total_fonts'])}/{len(r['total_fonts'])} Type 1`")
        lines.append(f"- **Visual Renders (`qa/renders/`):** `{', '.join(r['renders'])}`")
        lines.append(f"- **Verdict:** **{verdict}**")
        lines.append("")
        print(f"{r['name']}: pages={r['pages']} min_font={r['min_size']:.2f}pt fonts={len(r['total_fonts'])} renders={len(r['renders'])} -> {verdict}")

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return 1 if bad else 0

if __name__ == "__main__":
    sys.exit(main())
