#!/usr/bin/env python3
"""Checks that every reference-collector number printed in §16 comes from verify/device_model.py.

Parses the LaTeX source of src/sec16.tex (DOE table, 125 W and 100 W complete matrices,
1-cm National table, M_t / k weights, Fig. 16.2 nomogram coordinates and legend) and
compares each printed value with the model, rounded the way the binder prints it.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "verify"))
import device_model as dm  # noqa: E402

SRC = (ROOT / "src" / "sec16.tex").read_text(encoding="utf-8")


def rec(cid, desc, printed, model_str):
    ok = printed == model_str
    return {"id": cid, "section": "sec16", "description": desc, "passed": ok,
            "expected": model_str, "computed": printed,
            "detail": f"printed={printed} model={model_str}",
            "method": "parsed from src/sec16.tex; compared with verify/device_model.py"}


def block(label):
    i = SRC.index(label)
    return SRC[i:SRC.index(r"\bottomrule", i)]


def run_checks():
    out = []
    # DOE table
    b = block(r"\label{tab:16:doe-36}")
    for h in dm.ANCHORS:
        m = re.search(r"\$\\mathbf\{" + f"{h}.0" + r"\}\$ & \\textbf\{[A-C/]+\} & \$\\SI\{[0-9.]+\}\{\\watt\}\$ & (.*?) & [A-Za-z]", b)
        assert m, h
        cells = re.findall(r"\$\+?([0-9.]+)\$", m.group(1))
        model = [dm.tg_table(h, 125, 10), dm.tg_table(h, 125, 12), dm.tg_table(h, 125, 15),
                 dm.tg_table(h, 100, 10), dm.tg_table(h, 100, 12), dm.tg_table(h, 100, 15)]
        model += [22.0 + x for x in model[:3]]
        names = ["125W-10", "125W-12", "125W-15", "100W-10", "100W-12", "100W-15", "Tf-10", "Tf-12", "Tf-15"]
        for nm, c, x in zip(names, cells, model):
            out.append(rec(f"DOE-{h}-{nm}", f"DOE table h={h} {nm}", c, dm.r1(x)))
    for t in range(10, 16):
        m = re.search(r"\$M_\{" + str(t) + r"\}=\\mathbf\{([0-9.]+)\}\$, \$k_\{\\mathrm\{start\}\}=\\mathbf\{([0-9.]+)\}\$, \$k_\{\\mathrm\{room\}\}=\\mathbf\{([0-9.]+)\}\$", SRC)
        assert m, t
        out += [rec(f"DOE-M{t}", f"M_t({t} min)", m.group(1), f"{dm.m_t(t):.3f}"),
                rec(f"DOE-KS{t}", f"k_start({t} min)", m.group(2), f"{dm.k_start(t):.3f}"),
                rec(f"DOE-KR{t}", f"k_room({t} min)", m.group(3), f"{dm.k_room(t):.3f}")]
    # complete matrices
    for label, watts in ((r"\label{tab:16:direct-tfinal-125}", 125), (r"\label{tab:16:direct-tfinal-100}", 100)):
        b = block(label)
        for h in dm.ANCHORS:
            m = re.search(r"\$\\mathbf\{" + str(h) + r"\}\$ & [A-C] & (.*?) \\\\", b)
            cells = re.findall(r"([0-9]+\.[0-9])", m.group(1))
            model = [dm.tg_table(h, watts, t) for t in range(10, 16)] + [dm.dT_ss(h, watts)]
            for t, c, x in zip(list(range(10, 16)) + ["ss"], cells, model):
                out.append(rec(f"MAT{watts}-{h}-{t}", f"{watts} W matrix h={h} t={t}", c, dm.r1(x)))
    # 1-cm table (three column groups per row)
    b = block(r"\label{tab:16:natl-1cm}")
    for m in re.finditer(r"\$\\mathbf\{(\d\d)\}\$ & [A-C] & \$\\?(?:mathbf\{)?([0-9.]+)\}?\$ & \$\\?(?:mathbf\{)?([0-9.]+)\}?\$", b):
        h = int(m.group(1))
        out += [rec(f"NATL-{h}-125", f"1-cm table TG125 h={h}", m.group(2), dm.r1(dm.tg125_10(h))),
                rec(f"NATL-{h}-100", f"1-cm table TG100 h={h}", m.group(3), dm.r1(dm.ETA_100 * dm.tg125_10(h)))]
    # ambient-offset grid: k_room(t) * (T_room - T_start), printed to 0.01
    import math
    b = block(r"\label{tab:16:ambient-offset-grid}")
    for d in (4.0, 3.0, 2.0, 1.0, 0.5, -0.5, -1.0, -2.0, -3.0, -4.0):
        lab = f"{d:+.1f}"
        m = re.search(r"\$\\mathbf\{" + re.escape(lab) + r"\}\$ & (.*?) & [A-Z]", b)
        cells = re.findall(r"\$([+-][0-9.]+)\$", m.group(1))
        for t, c in zip(range(10, 16), cells):
            x = dm.k_room(t) * d
            model = f"{math.copysign(math.floor(abs(x) * 100 + 0.5 + 1e-9) / 100, x):+.2f}"
            out.append(rec(f"AMB-{lab}-{t}", f"ambient offset d={lab} t={t}", c, model))
    for name, fn in (("room", dm.k_room), ("start", dm.k_start)):
        m = re.search(r"\\textbf\{Weight \$k_\{\\mathrm\{" + name + r"\}\}\$\} & (.*?) & \$", b)
        for t, c in zip(range(10, 16), re.findall(r"\$([0-9.]+)\$", m.group(1))):
            out.append(rec(f"AMB-K{name}-{t}", f"ambient grid k_{name}({t})", c, f"{fn(t):.3f}"))
    # nomogram
    for t, tag in ((15, "15.0"), (14, "14.0"), (13, "13.0"), (12, "12.0"), (11, "11.0"), (10, "10.0")):
        m = re.search(r"coordinates \{\n    ([^\n]*)\n\};\n\\addlegendentry\{\$t = \\SI\{" + re.escape(tag) + r"\}\{\\minute\}\$([^\n]*)", SRC)
        assert m, t
        for hh, val in re.findall(r"\((\d+), ([0-9.]+)\)", m.group(1)):
            out.append(rec(f"NOMO-{t}-{hh}", f"nomogram t={t} h={hh}", val, dm.r1(dm.tg_table(int(hh), 125, t))))
        if t != 10:
            mm = re.search(r"M_t = ([0-9.]+)", m.group(2))
            out.append(rec(f"NOMO-LEG-{t}", f"nomogram legend M_t({t})", mm.group(1), f"{dm.m_t(t):.3f}"))
    return out


if __name__ == "__main__":
    res = run_checks()
    bad = [r for r in res if not r["passed"]]
    for r in bad:
        print("FAIL", r["id"], r["detail"])
    print(f"{len(res) - len(bad)}/{len(res)} pass")
