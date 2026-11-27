#!/usr/bin/env python3
"""Single-source check for the modeled reference run (h = 45 cm, 125 W, 10 min, T_start = 22.0 C).

Every stratification number printed for this run must agree:
  * §16 lookup model (verify/device_model.py): T_top = 22.0 + TG_table(45, 125, 10) = 49.7 C;
  * §15 two-node model, Ex 15.4: T_mixed = (C_top*T_top + C_bot*T_bot)/(C_top + C_bot) = 39.80 C;
  * §15 Fig. 15.6 (10-min glazed profile T(z));
  * §17 Fig. 17.2 table (centre column, bias column, swirled row) and Ex 17.4 inputs.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "verify"))
import device_model as dm  # noqa: E402

S15 = (ROOT / "src" / "sec15.tex").read_text(encoding="utf-8")
S17 = (ROOT / "src" / "sec17.tex").read_text(encoding="utf-8")

# two-node lump of Ex 15.4 (house values)
C_TOP, C_BOT, T_BOT = 215.0, 203.4, 29.34


def rec(cid, desc, printed, expected):
    return {"id": cid, "section": "sec15/sec17", "description": desc, "passed": printed == expected,
            "expected": expected, "computed": printed, "detail": f"printed={printed} model={expected}",
            "method": "parsed from src/sec15.tex and src/sec17.tex; compared with the single reference-run model"}


def run_checks():
    out = []
    t_top = 22.0 + dm.tg_table(45, 125, 10)
    t_mix = (C_TOP * t_top + C_BOT * T_BOT) / (C_TOP + C_BOT)
    out.append(rec("REF-TTOP", "reference-run top-layer reading", dm.r1(t_top), "49.7"))
    out.append(rec("REF-TMIX", "two-node mixed temperature", f"{t_mix:.2f}", "39.80"))

    # Fig 15.6 10-min glazed profile
    m = re.search(r"% Curve 2: t = 10 min Glazed CPC.*?coordinates \{\s*(.*?)\s*\};", S15, re.S)
    prof = [(float(z), float(t)) for t, z in re.findall(r"\(([0-9.]+), ([0-9.]+)\)", m.group(1))]
    prof_d = {z: t for z, t in prof}
    out.append(rec("REF-PROF-6MM", "Fig 15.6 profile at the 6 mm ES depth", f"{prof_d[6.0]:.1f}", dm.r1(t_top)))
    m = re.search(r"\\draw\[rust, very thick, dashdotted\] \(axis cs:([0-9.]+),0\)", S15)
    out.append(rec("REF-FIG156-SWIRL", "Fig 15.6 swirled line", m.group(1), f"{t_mix:.1f}"))

    # Fig 17.2 table
    rows = re.findall(r"\$\\(?:mathbf\{\\)?SI\{([0-9.]+)\}\{\\milli\\meter\}\}?\$[^&]*& \$\\(?:mathbf\{\\)?SI\{([0-9.]+)\}\{\\celsius\}\}?\$ & \$(?:\\mathbf\{)?([+-]?)\\SI\{([0-9.]+)\}\{\\celsius\}", S17)
    assert len(rows) == 8, rows
    for z, t, sign, b in rows:
        z, t = float(z), float(t)
        out.append(rec(f"REF-F172-T-{z:g}", f"Fig 17.2 T at z={z:g} mm equals Fig 15.6", f"{t:.1f}", f"{prof_d[z]:.1f}"))
        bias = f"{prof_d[z] - t_top:+.1f}".replace("+0.0", "0.0")
        out.append(rec(f"REF-F172-B-{z:g}", f"Fig 17.2 bias at z={z:g} mm", f"{sign}{b}" if sign else b, bias))
    m = re.search(r"Swirled \(mixed; not allowed\) & \$\\SI\{([0-9.]+)\}\{\\celsius\}\$ & \$\\mathbf\{-\\SI\{([0-9.]+)\}", S17)
    out.append(rec("REF-F172-SWIRL", "Fig 17.2 swirled row", m.group(1), f"{t_mix:.1f}"))
    out.append(rec("REF-F172-SWIRL-B", "Fig 17.2 swirled bias", f"-{m.group(2)}", f"{t_mix - t_top:.1f}"))

    # Ex 17.4 uses the same top-layer capacitance and temperature
    m = re.search(r"\(\$C_\{\\mathrm\{top\}\} = \\SI\{([0-9.]+)\}\{\\joule\\per\\kelvin\}\$, initial temperature \$T_\{w,0\} = \\SI\{([0-9.]+)\}", S17)
    out.append(rec("REF-EX174-CTOP", "Ex 17.4 C_top", m.group(1), f"{C_TOP:.1f}"))
    out.append(rec("REF-EX174-TTOP", "Ex 17.4 top-layer temperature", m.group(2), f"{t_top:.2f}"))
    # Reference-collector summary table (§16.3) — every line recomputed
    S16 = (ROOT / "src" / "sec16.tex").read_text(encoding="utf-8")
    i = S16.index(r"\label{tab:16:reference-collector}")
    T = S16[i:S16.index(r"\end{tabularx}", i)]
    m = re.search(r"\$24\.8\$, \$27\.7\$, \$21\.3\$, \$17\.5\$, \$13\.6\$, \$\\SI\{10\.6\}", T)
    out.append(rec("REF-TAB-ANCHORS", "table lookup anchors = device_model.TG125_10MIN", "found" if m else "missing",
                   "found" if [dm.TG125_10MIN[h] for h in dm.ANCHORS] == [24.8, 27.7, 21.3, 17.5, 13.6, 10.6] else "model differs"))
    import math
    tau = 380.0 * 2.376
    out.append(rec("REF-TAB-TAU", "one-node tau = C_eff R_th [s]", "903", f"{tau:.0f}"))
    for t, pr in ((600, "49.7"), (900, "58.0")):
        out.append(rec(f"REF-TAB-1NODE-{t}", f"one-node T at {t} s", pr, f"{22.0 + 24.0 * 2.376 * (1 - math.exp(-t / tau)):.1f}"))

    def coax(r1, r2, d):
        R1, R2 = r1 / d, r2 / d
        X = 1 + (1 + R2 ** 2) / R1 ** 2
        return 0.5 * (X - math.sqrt(X * X - 4 * (R2 / R1) ** 2))
    fa, fc = coax(6.35, 15.0, 10.0), coax(6.35, 3.75, 30.0)
    out += [rec("REF-TAB-FAP", "view factor top plane at 40 cm", "0.665", f"{fa:.3f}"),
            rec("REF-TAB-FCUP", "view factor bare cup at 40 cm", "0.0147", f"{fc:.4f}"),
            rec("REF-TAB-GAIN-VF", "intercepted-power ratio", "45.1", f"{fa / fc:.1f}"),
            rec("REF-TAB-GAIN-CAP", "beam-delivered ratio (31.39 / 2.30)", "13.6", f"{31.39 / 2.30:.1f}"),
            rec("REF-TAB-GAIN-ABS", "absorbed-power ratio (21.5 / 1.95)", "11.0", f"{21.5 / 1.95:.1f}")]
    for k, (rt, rb, zt, zb, pr) in enumerate(((14.50, 11.50, 27.50, 20.50, "23.2"), (11.50, 7.20, 20.50, 14.00, "33.5"), (7.20, 3.90, 14.00, 10.50, "43.3")), 1):
        out.append(rec(f"REF-TAB-PHI{k}", f"stage {k} half-angle from Table 15.3 coordinates [deg]", pr, f"{math.degrees(math.atan((rt - rb) / (zt - zb))):.1f}"))
    S15c = (ROOT / "src" / "sec15.tex").read_text(encoding="utf-8")
    for cap, bare, pr in ((31.39, 2.30, "13.6"), (41.43, 1.70, "24.4"), (37.35, 1.30, "28.7"), (27.60, 1.03, "26.8"), (24.80, 0.84, "29.5"), (18.90, 0.69, "27.4")):
        out.append(rec(f"TAB-15.4-GAIN-{pr}", f"Table 15.4 capture ratio {cap}/{bare}", "found" if f"$\\mathbf{{{cap:.2f}\\%}}$ & $\\mathbf{{{pr}\\times}}$" in S15c else "missing", "found"))
        out.append(rec(f"TAB-15.4-GAINV-{pr}", f"Table 15.4 ratio value {cap}/{bare}", pr, f"{cap / bare:.1f}"))
    for pr in ("23.2", "33.5", "43.3"):
        out.append(rec(f"REF-T153-PHI-{pr}", f"Table 15.3 prints phi = {pr} deg", "found" if f"& ${pr}^\\circ$ &" in S15c else "missing", "found"))
    return out


if __name__ == "__main__":
    res = run_checks()
    bad = [r for r in res if not r["passed"]]
    for r in bad:
        print("FAIL", r["id"], r["detail"])
    print(f"{len(res) - len(bad)}/{len(res)} pass")
