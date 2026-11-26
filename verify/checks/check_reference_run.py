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
    return out


if __name__ == "__main__":
    res = run_checks()
    bad = [r for r in res if not r["passed"]]
    for r in bad:
        print("FAIL", r["id"], r["detail"])
    print(f"{len(res) - len(bad)}/{len(res)} pass")
