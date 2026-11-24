#!/usr/bin/env python3
"""
build/export_markdown.py — Reproducible LaTeX-to-GitHub-Flavored-Markdown Mirror Generator
for the 2026-2027 Science Olympiad Division C Thermodynamics Competition Binder.

Converts all 33 modular LaTeX source files:
  - src/frontmatter.tex          -> markdown/frontmatter.md
  - src/sec00.tex .. sec23.tex   -> markdown/sec00.md .. markdown/sec23.md
  - src/appA.tex  .. appH.tex    -> markdown/appA.md  .. markdown/appH.md
Plus generates:
  - markdown/README.md (Clickable master TOC with section titles, 9-Tab directory & page targets)
  - markdown/Thermodynamics_DivC_Complete_Binder.md (Single unified searchable Markdown edition)
"""

from __future__ import annotations
import pathlib
import re
import sys
from typing import Callable, Dict, List, Optional, Tuple

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC_DIR = ROOT / "src"
MD_DIR = ROOT / "markdown"

# Page targets locked in build/architecture-lock.md (248 pages total)
SECTION_META: List[Tuple[str, str, int, str]] = [
    ("frontmatter", "Front Matter, Verified 2027 Rules Baseline & 9-Tab Directory", 2, "Front Matter"),
    ("sec00", "§0 Competition Command Center & 2027 Rules Snapshot", 5, "Tab 1: CMD/QUICK"),
    ("sec01", "§1 Standalone One-Page Quick Sheets (QS-01 to QS-14)", 14, "Tab 1: CMD/QUICK"),
    ("sec02", "§2 Thermodynamic Systems, State Variables, Zeroth Law & Mathematical Toolkit", 6, "Tab 2: FOUNDATIONS"),
    ("sec03", "§3 Foundations of Heat & Temperature, Scales, Expansion & 8 Scientists (5.c.v)", 8, "Tab 2: FOUNDATIONS"),
    ("sec04", "§4 Heat Capacity, Specific/Molar Heat, Dulong-Petit & Multi-Body Calorimetry", 12, "Tab 3: CAL/PHASE"),
    ("sec05", "§5 Phases of Matter, Phase Diagrams (H2O, CO2, Binary Eutectic) & Psychrometrics", 10, "Tab 3: CAL/PHASE"),
    ("sec06", "§6 Ideal & Real Gases, Kinetic Theory, Maxwell-Boltzmann & Equipartition", 10, "Tab 4: GASES/LAWS"),
    ("sec07", "§7 First Law of Thermodynamics, Work, Enthalpy & Closed/Open Process Atlas", 12, "Tab 4: GASES/LAWS"),
    ("sec08", "§8 Second & Third Laws, Entropy, Free Energy (Delta G), Exergy & Maxwell Relations", 10, "Tab 4: GASES/LAWS"),
    ("sec09", "§9 Thermodynamic Cycles, Heat Engines, Refrigerators, Heat Pumps & 7 Named Cycles", 12, "Tab 4: GASES/LAWS"),
    ("sec10", "§10 Heat Transfer I: Conduction, Thermal Resistance Networks, Fins & Critical Radius", 12, "Tab 5: TRANSFER"),
    ("sec11", "§11 Heat Transfer II: Natural & Forced Convection, Dimensionless Groups & Evaporation", 8, "Tab 5: TRANSFER"),
    ("sec12", "§12 Heat Transfer III: Blackbody Radiation, Planck/Wien/Stefan-Boltzmann & Shields", 8, "Tab 5: TRANSFER"),
    ("sec13", "§13 Transient & Coupled Multi-Mode Heat Transfer, Lumped Capacitance & Lamp Heating ODE", 10, "Tab 5: TRANSFER"),
    ("sec14", "§14 Materials, Optical & Thermal Properties Encyclopedia (2027 #6 PS Ban Compliant)", 10, "Tab 6: DEVICE"),
    ("sec15", "§15 2027 Heat-Lamp Collector Engineering Manual, Optics & Top-Layer Stratification", 18, "Tab 6: DEVICE"),
    ("sec16", "§16 Thermal Modeling, DOE Calibration & 15-Second Temperature Prediction (PE) System", 12, "Tab 6: DEVICE"),
    ("sec17", "§17 Laboratory & Measurement Handbook: Thermometers, 5-tau Lag, Immersion & GUM Uncertainty", 12, "Tab 7: LAB/DATA"),
    ("sec18", "§18 Graphs, Data & Experimental Analysis: Steam Interpolation, Linearization & Residuals", 8, "Tab 7: LAB/DATA"),
    ("sec19", "§19 Integrated Multi-Physics Problem-Solving Playbook", 8, "Tab 8: PROBLEMS"),
    ("sec20", "§20 High-Yield Misconceptions, Common Mistakes & Wrong-Answer Diagnostic Catalog", 8, "Tab 8: PROBLEMS"),
    ("sec21", "§21 Exam Strategy, Time Management & Two-Partner Competition Protocol", 5, "Tab 8: PROBLEMS"),
    ("sec22", "§22 Evidence-Based Tournament Intelligence (N=8 Corpus E1-E8, 328 Items, 1,120.0 Pts)", 4, "Tab 8: PROBLEMS"),
    ("sec23", "§23 Final Review & Last-Week Cram Layer (Top-40 Equations, Top-25 Constants, Top-15 Traps)", 8, "Tab 8: PROBLEMS"),
    ("appA", "Appendix A: Master Physical Constants, Conversions & Extended Property/Steam Tables", 4, "Tab 9: INDEX/APP"),
    ("appB", "Appendix B: Master Equation & Formula Chooser Index (Algebra-Only 5.d.iv Compliant)", 3, "Tab 9: INDEX/APP"),
    ("appC", "Appendix C: Five Multi-Indices (Topic, Formula, Diagram, Error & Collector Failure-Mode)", 4, "Tab 9: INDEX/APP"),
    ("appD", "Appendix D: Printable 2027 Heat-Lamp Collector Test Log & Calibration Forms", 2, "Tab 9: INDEX/APP"),
    ("appE", "Appendix E: 2027 Official Rules & Clarifications (#1-#9) Clause-by-Clause Compliance Matrix", 2, "Tab 9: INDEX/APP"),
    ("appF", "Appendix F: One-Page Pre-Tournament Rules & Host-Modifications Verification Checklist", 1, "Tab 9: INDEX/APP"),
    ("appG", "Appendix G: Sourced Primary & Authoritative References Summary ([S01]-[S35])", 1, "Tab 9: INDEX/APP"),
    ("appH", "Appendix H: Tournament-Specific Open Questions & Binder Maintenance Guide", 1, "Tab 9: INDEX/APP"),
]

UNIT_MAP: Dict[str, str] = {
    r"\ampere": "A",
    r"\atmosphere": "atm",
    r"\bar": "bar",
    r"\cdot": "·",
    r"\celsius": "°C",
    r"\centi": "c",
    r"\coulomb": "C",
    r"\cubed": "^3",
    r"\cubic": "cubic ",
    r"\degree": "°",
    r"\electronvolt": "eV",
    r"\fahrenheit": "°F",
    r"\giga": "G",
    r"\gram": "g",
    r"\hertz": "Hz",
    r"\hour": "h",
    r"\joule": "J",
    r"\kelvin": "K",
    r"\kilo": "k",
    r"\kilogram": "kg",
    r"\kilojoule": "kJ",
    r"\kilowatt": "kW",
    r"\liter": "L",
    r"\mega": "M",
    r"\meter": "m",
    r"\micro": "µ",
    r"\milli": "m",
    r"\minute": "min",
    r"\mole": "mol",
    r"\nano": "n",
    r"\newton": "N",
    r"\ohm": "Ω",
    r"\pascal": "Pa",
    r"\percent": "%",
    r"\radian": "rad",
    r"\rankine": "°R",
    r"\second": "s",
    r"\siemens": "S",
    r"\square": "sq ",
    r"\squared": "^2",
    r"\steradian": "sr",
    r"\volt": "V",
    r"\watt": "W",
}


def find_matching(text: str, pos: int, open_ch: str = "{", close_ch: str = "}") -> int:
    """Return index of matching close_ch starting from open_ch at text[pos], or -1."""
    if pos >= len(text) or text[pos] != open_ch:
        return -1
    depth = 0
    i = pos
    while i < len(text):
        ch = text[i]
        if ch == "\\":
            i += 2
            continue
        if ch == open_ch:
            depth += 1
        elif ch == close_ch:
            depth -= 1
            if depth == 0:
                return i
        i += 1
    return -1


def strip_comments(text: str) -> str:
    """Remove LaTeX % comments while preserving escaped \\%."""
    out_lines: List[str] = []
    for line in text.splitlines():
        if line.lstrip().startswith("%"):
            continue
        m = re.search(r"(?<!\\)%", line)
        if m:
            line = line[: m.start()].rstrip()
        out_lines.append(line)
    return "\n".join(out_lines)


def format_si_unit(u_raw: str) -> str:
    """Convert siunitx unit specification into clean human-readable unit string."""
    u = u_raw.strip()
    if not u:
        return ""
    u = re.sub(r"\\(?:text|mathrm)\{([^{}]*)\}", r" \1 ", u)
    u = u.replace(r"\textdegree", "°")
    u = re.sub(r"\\tothe\{([^{}]*)\}", r"^\1 ", u)
    u = re.sub(
        r"\\square\\(centi|milli|micro|nano|kilo)?\\?(meter|foot|inch|kelvin|second)",
        lambda m: " "
        + (UNIT_MAP.get("\\" + m.group(1), "") if m.group(1) else "")
        + (UNIT_MAP.get("\\" + m.group(2), m.group(2)))
        + "^2 ",
        u,
    )
    u = re.sub(
        r"\\cubic\\(centi|milli|micro|nano|kilo)?\\?(meter|foot|inch)",
        lambda m: " "
        + (UNIT_MAP.get("\\" + m.group(1), "") if m.group(1) else "")
        + (UNIT_MAP.get("\\" + m.group(2), m.group(2)))
        + "^3 ",
        u,
    )
    prefixes = ["giga", "mega", "kilo", "centi", "milli", "micro", "nano"]
    base_units = [
        "joule", "watt", "pascal", "meter", "gram", "liter", "second",
        "kelvin", "mole", "ampere", "volt", "ohm", "hertz", "newton",
        "coulomb", "bar", "electronvolt",
    ]
    for p in prefixes:
        p_sym = UNIT_MAP["\\" + p]
        for b in base_units:
            b_sym = UNIT_MAP.get("\\" + b, b)
            u = u.replace(f"\\{p}\\{b}", f" {p_sym}{b_sym} ")
    tokens = re.split(r"(\\per(?![A-Za-z]))", u)
    out_parts: List[str] = []
    next_is_denom = False
    for tok in tokens:
        if tok == r"\per":
            next_is_denom = True
            continue
        for k in sorted(UNIT_MAP.keys(), key=len, reverse=True):
            tok = re.sub(re.escape(k) + r"(?![A-Za-z])", " " + UNIT_MAP[k] + " ", tok)
        tok = re.sub(r"\s+", " ", tok).strip()
        if not tok:
            continue
        tok = re.sub(r"\s+\^", "^", tok)
        if next_is_denom:
            subtoks = tok.split(" ")
            out_parts.append("/" + subtoks[0])
            if len(subtoks) > 1:
                out_parts.extend(subtoks[1:])
            next_is_denom = False
        else:
            out_parts.append(tok)
    res = "·".join([p for p in out_parts if p]).replace("·/", "/")
    res = re.sub(r"\s+", " ", res).strip()
    return res


def format_si_num(n_raw: str) -> str:
    """Convert siunitx number string (e.g. 6.022e23 or 1.5+-0.2) into readable string."""
    n = n_raw.strip()
    n = n.replace("+-", "±").replace(r"\pm", "±")
    m = re.match(r"^([+-]?\d+(?:\.\d+)?)[eE]([+-]?\d+)$", n)
    if m:
        mant, exp = m.group(1), int(m.group(2))
        if mant in ("1", ""):
            return f"10^{{{exp}}}"
        return f"{mant}×10^{{{exp}}}"
    return n


def replace_siunitx(text: str) -> str:
    """Replace all \SI{v}{u}, \SI[opt]{v}{u}, \SIrange{v1}{v2}{u}, \si{u}, \num{v}."""
    out: List[str] = []
    i = 0
    n = len(text)
    while i < n:
        if text[i] == "\\":
            m = re.match(r"\\(SIrange|SI|si|num)(?![A-Za-z])", text[i:])
            if m:
                cmd = m.group(1)
                cur = i + len(m.group(0))
                while cur < n and text[cur] in " \t":
                    cur += 1
                if cur < n and text[cur] == "[":
                    end_opt = find_matching(text, cur, "[", "]")
                    if end_opt != -1:
                        cur = end_opt + 1
                while cur < n and text[cur] in " \t":
                    cur += 1
                if cmd == "SIrange" and cur < n and text[cur] == "{":
                    e1 = find_matching(text, cur)
                    if e1 != -1:
                        v1 = text[cur + 1 : e1]
                        c2 = e1 + 1
                        while c2 < n and text[c2] in " \t":
                            c2 += 1
                        if c2 < n and text[c2] == "{":
                            e2 = find_matching(text, c2)
                            if e2 != -1:
                                v2 = text[c2 + 1 : e2]
                                c3 = e2 + 1
                                while c3 < n and text[c3] in " \t":
                                    c3 += 1
                                if c3 < n and text[c3] == "{":
                                    e3 = find_matching(text, c3)
                                    if e3 != -1:
                                        u = format_si_unit(text[c3 + 1 : e3])
                                        f1, f2 = format_si_num(v1), format_si_num(v2)
                                        rep = f"{f1}–{f2} {u}".strip()
                                        out.append(rep)
                                        i = e3 + 1
                                        continue
                elif cmd == "SI" and cur < n and text[cur] == "{":
                    e1 = find_matching(text, cur)
                    if e1 != -1:
                        v1 = text[cur + 1 : e1]
                        c2 = e1 + 1
                        while c2 < n and text[c2] in " \t":
                            c2 += 1
                        if c2 < n and text[c2] == "{":
                            e2 = find_matching(text, c2)
                            if e2 != -1:
                                u = format_si_unit(text[c2 + 1 : e2])
                                f1 = format_si_num(v1)
                                if u in ("%", "°"):
                                    rep = f"{f1}{u}"
                                else:
                                    rep = f"{f1} {u}".strip()
                                out.append(rep)
                                i = e2 + 1
                                continue
                elif cmd in ("si", "num") and cur < n and text[cur] == "{":
                    e1 = find_matching(text, cur)
                    if e1 != -1:
                        arg = text[cur + 1 : e1]
                        rep = format_si_unit(arg) if cmd == "si" else format_si_num(arg)
                        out.append(rep)
                        i = e1 + 1
                        continue
        out.append(text[i])
        i += 1
    return "".join(out)


def replace_cmd_1arg(text: str, cmd: str, fn: Callable[[str], str]) -> str:
    """Brace-balanced replacement for \cmd{arg} (ignoring optional [opt])."""
    if "\\" + cmd not in text:
        return text
    pat = re.compile(r"\\" + re.escape(cmd) + r"(?![A-Za-z])")
    out: List[str] = []
    i = 0
    n = len(text)
    while i < n:
        m = pat.search(text, i)
        if not m:
            out.append(text[i:])
            break
        out.append(text[i : m.start()])
        cur = m.end()
        while cur < n and text[cur] in " \t":
            cur += 1
        if cur < n and text[cur] == "[":
            eopt = find_matching(text, cur, "[", "]")
            if eopt != -1:
                cur = eopt + 1
        while cur < n and text[cur] in " \t":
            cur += 1
        if cur < n and text[cur] == "{":
            end = find_matching(text, cur)
            if end != -1:
                arg = text[cur + 1 : end]
                out.append(fn(arg))
                i = end + 1
                continue
        out.append(text[m.start() : m.end()])
        i = m.end()
    return "".join(out)


def replace_cmd_2arg(text: str, cmd: str, fn: Callable[[str, str], str]) -> str:
    """Brace-balanced replacement for \cmd{arg1}{arg2}."""
    if "\\" + cmd not in text:
        return text
    pat = re.compile(r"\\" + re.escape(cmd) + r"(?![A-Za-z])")
    out: List[str] = []
    i = 0
    n = len(text)
    while i < n:
        m = pat.search(text, i)
        if not m:
            out.append(text[i:])
            break
        out.append(text[i : m.start()])
        cur = m.end()
        while cur < n and text[cur] in " \t":
            cur += 1
        if cur < n and text[cur] == "{":
            e1 = find_matching(text, cur)
            if e1 != -1:
                a1 = text[cur + 1 : e1]
                c2 = e1 + 1
                while c2 < n and text[c2] in " \t":
                    c2 += 1
                if c2 < n and text[c2] == "{":
                    e2 = find_matching(text, c2)
                    if e2 != -1:
                        a2 = text[c2 + 1 : e2]
                        out.append(fn(a1, a2))
                        i = e2 + 1
                        continue
        out.append(text[m.start() : m.end()])
        i = m.end()
    return "".join(out)


def clean_inline_latex(text: str) -> str:
    """Convert inline LaTeX macros and typography into clean GitHub-Flavored Markdown."""
    s = replace_siunitx(text)

    # Strip index & header commands completely
    for idx_cmd in (
        "idxtopic", "idxformula", "idxfig", "idxerr", "idxdev", "idxterm",
        "ix", "fx", "sx", "dx", "erx", "px", "cx", "markright", "chaptermark", "sectionmark",
    ):
        s = replace_cmd_1arg(s, idx_cmd, lambda _: "")

    # Cross-references & citations
    s = replace_cmd_1arg(s, "sref", lambda a: f"§`{a.strip()}`")
    s = replace_cmd_1arg(s, "spref", lambda a: f"§`{a.strip()}`")
    s = replace_cmd_1arg(s, "pref", lambda a: f"(`{a.strip()}`)")
    s = replace_cmd_1arg(s, "fref", lambda a: f"Fig. `{a.strip()}`")
    s = replace_cmd_1arg(s, "tref", lambda a: f"Table `{a.strip()}`")
    s = replace_cmd_1arg(s, "eref", lambda a: f"Eq. (`{a.strip()}`)")
    s = replace_cmd_1arg(s, "ref", lambda a: f"`{a.strip()}`")
    s = replace_cmd_1arg(s, "seesec", lambda a: f"→ §`{a.strip()}`")
    s = replace_cmd_1arg(s, "label", lambda a: "")

    # Flags & epistemic badges
    flag_repls = {
        r"\IG": "**[IDEAL-GAS]**",
        r"\CLSD": "**[CLOSED]**",
        r"\SSFL": "**[STEADY-FLOW]**",
        r"\REV": "**[REV]**",
        r"\CONSTC": "**[CONST-c]**",
        r"\LUMP": "**[Bi<0.1]**",
        r"\GRAY": "**[GRAY-SURF]**",
        r"\INCOMP": "**[INCOMP]**",
        r"\TIERf": "**[STATE/NAT]**",
        r"\RULEf": "**[2027-RULE]**",
        r"\SUPPf": "**[SUPP]**",
        r"\OBS": "**[OBSERVED]**",
        r"\REC": "**[RECOMMENDED]**",
        r"\SPEC": "**[SPECULATIVE]**",
        r"\UNVER": "**[UNVERIFIED]**",
        r"\cmark": "✓",
        r"\xmark": "✗",
    }
    for k, v in flag_repls.items():
        if k in s:
            s = re.sub(re.escape(k) + r"\\?(?![A-Za-z])", v, s)

    s = replace_cmd_1arg(s, "flag", lambda a: f"**[{a.strip()}]**")
    s = replace_cmd_1arg(s, "VERIF", lambda a: f"**[VERIFIED: {a.strip()}]**")
    s = replace_cmd_1arg(s, "INFER", lambda a: f"**[INFERRED: {a.strip()}]**")
    s = replace_cmd_1arg(s, "verifiedby", lambda a: f"\n**✓ Verified by:** {clean_inline_latex(a)}")
    s = replace_cmd_1arg(s, "verified", lambda a: f"\n**✓ Verified by:** {clean_inline_latex(a)}")
    s = replace_cmd_2arg(s, "ifgot", lambda a, b: f"\n**If you got {clean_inline_latex(a)},** {clean_inline_latex(b)}")
    s = replace_cmd_1arg(s, "alsosee", lambda a: f"\n---\n**See also:** {clean_inline_latex(a)}\n")
    s = replace_cmd_2arg(s, "texorpdfstring", lambda a, _: a)
    s = replace_cmd_2arg(s, "textcolor", lambda _, b: b)
    s = replace_cmd_2arg(s, "colorbox", lambda _, b: b)
    s = replace_cmd_1arg(s, "fbox", lambda a: a)
    s = replace_cmd_2arg(s, "parbox", lambda _, b: b)
    s = replace_cmd_2arg(s, "resizebox", lambda _, b: b)

    # Dingbats
    ding_map = {"51": "✓", "55": "✗", "72": "★", "73": "☆", "110": "■", "111": "☐", "45": "✎", "228": "➤"}
    s = replace_cmd_1arg(s, "ding", lambda a: ding_map.get(a.strip(), "•"))

    # Accents (careful never to eat an unmatched closing brace!)
    s = re.sub(r"\\'\{e\}|\\'e(?![A-Za-z])", "é", s)
    s = re.sub(r"\\'\{E\}|\\'E(?![A-Za-z])", "É", s)
    s = re.sub(r"\\'\{a\}|\\'a(?![A-Za-z])", "á", s)
    s = re.sub(r"\\'\{o\}|\\'o(?![A-Za-z])", "ó", s)
    s = re.sub(r'\\"\{o\}|\\"o(?![A-Za-z])', "ö", s)
    s = re.sub(r'\\"\{u\}|\\"u(?![A-Za-z])', "ü", s)
    s = re.sub(r'\\"\{a\}|\\"a(?![A-Za-z])', "ä", s)
    s = re.sub(r"\\c\s*\{c\}", "ç", s)
    s = re.sub(r"\\o\s*\{\}|\\o(?![A-Za-z])", "ø", s)
    s = re.sub(r"\\O\s*\{\}|\\O(?![A-Za-z])", "Ø", s)
    s = re.sub(r"\\r\s*\{A\}|\\AA(?![A-Za-z])", "Å", s)

    # Repeatable nested text formatting (run before math split so \textbf{... $x$ ...} works!)
    for _ in range(4):
        s = replace_cmd_1arg(s, "hdr", lambda a: f"**{a.strip()}**")
        s = replace_cmd_1arg(s, "textbf", lambda a: f"**{a.strip()}**")
        s = replace_cmd_1arg(s, "textit", lambda a: f"*{a.strip()}*")
        s = replace_cmd_1arg(s, "emph", lambda a: f"*{a.strip()}*")
        s = replace_cmd_1arg(s, "texttt", lambda a: f"`{a.strip()}`")
        s = replace_cmd_1arg(s, "textsf", lambda a: a.strip())
        s = replace_cmd_1arg(s, "textrm", lambda a: a.strip())
        s = replace_cmd_1arg(s, "underline", lambda a: f"<u>{a.strip()}</u>")
        s = replace_cmd_1arg(s, "textsuperscript", lambda a: f"^{a.strip()}")
        s = replace_cmd_1arg(s, "src", lambda a: f" **[{a.strip()}]**")
        s = replace_cmd_1arg(s, "Source", lambda a: f" **[{a.strip()}]**")
        s = replace_cmd_1arg(s, "Sources", lambda a: f" **[{a.strip()}]**")

    # Split text outside math ($...$ and $$...$$) vs inside math so we only strip layout macros outside math
    parts = re.split(r"(\$\$[\s\S]*?\$\$|\$[^\$]+?\$)", s)
    for idx in range(0, len(parts), 2):
        p = parts[idx]
        p = p.replace("``", "“").replace("''", "”")
        p = p.replace("---", "—").replace("--", "–")
        p = p.replace(r"\textperiodcentered", "·").replace(r"\textbar", "|").replace(r"\textbullet", "•")
        p = p.replace(r"\textdegree", "°").replace(r"\textbackslash", "\\")
        p = p.replace(r"\&", "&").replace(r"\%", "%").replace(r"\#", "#").replace(r"\_", "_").replace(r"\$", "$")
        p = p.replace(r"\ ", " ").replace("~", " ").replace(r"\,", " ").replace(r"\!", "")
        p = p.replace(r"\newline", "<br>").replace(r"\hfill", " ").replace(r"\hrulefill", "________").replace(r"\dotfill", "........")
        p = re.sub(r"\\S(\d+)", r"§\1", p)
        p = re.sub(r"\\S(?![A-Za-z])", "§", p)
        p = re.sub(
            r"\\(?:footnotesize|scriptsize|tiny|small|normalsize|large|Large|LARGE|huge|Huge|sffamily|bfseries|itshape|rmfamily|ttfamily|normalfont|selectfont|noindent|centering|raggedright|vfill|clearpage|newpage|par|smallskip|medskip|bigskip|strut|makeatletter|makeatother|printallthermoindices)\b\s*",
            "",
            p,
        )
        p = replace_cmd_1arg(p, "vspace", lambda _: "")
        p = replace_cmd_1arg(p, "hspace", lambda _: " ")
        p = replace_cmd_1arg(p, "needspace", lambda _: "")
        p = replace_cmd_1arg(p, "Needspace", lambda _: "")
        p = replace_cmd_1arg(p, "thispagestyle", lambda _: "")
        p = replace_cmd_1arg(p, "color", lambda _: "")
        p = replace_cmd_1arg(p, "rowcolor", lambda _: "")
        p = replace_cmd_2arg(p, "setlength", lambda _, __: "")
        p = replace_cmd_2arg(p, "renewcommand", lambda _, __: "")
        p = replace_cmd_2arg(p, "setcounter", lambda _, __: "")
        p = replace_cmd_2arg(p, "fontsize", lambda _, __: "")
        p = replace_cmd_2arg(p, "rule", lambda _, __: "---")
        parts[idx] = p
    s = "".join(parts)
    return s


def summarize_tikzpicture(tikz_code: str, caption: str = "", label: str = "") -> str:
    """Convert a tikzpicture / pgfplots block into a structured, human-readable Markdown figure card."""
    nodes: List[str] = []
    for key, title in [("title", "Title"), ("xlabel", "X-Axis"), ("ylabel", "Y-Axis")]:
        for m in re.finditer(key + r"\s*=\s*\{", tikz_code):
            end = find_matching(tikz_code, m.end() - 1)
            if end != -1:
                val = clean_inline_latex(tikz_code[m.end() : end]).replace("\n", " ").strip()
                if val:
                    nodes.append(f"**{title}:** {val}")
    for m in re.finditer(r"\\(?:legend|addlegendentry)\s*\{", tikz_code):
        end = find_matching(tikz_code, m.end() - 1)
        if end != -1:
            val = clean_inline_latex(tikz_code[m.end() : end]).replace("\n", " ").strip()
            if val:
                nodes.append(f"**Legend:** {val}")
    idx = 0
    while idx < len(tikz_code):
        m = re.search(r"\\node\b[^;]*?\{", tikz_code[idx:])
        if not m:
            break
        brace_pos = idx + m.end() - 1
        end = find_matching(tikz_code, brace_pos)
        if end != -1:
            raw_node = tikz_code[brace_pos + 1 : end]
            cleaned = clean_inline_latex(raw_node)
            cleaned = re.sub(r"\\\\", " / ", cleaned)
            cleaned = re.sub(r"\s+", " ", cleaned).strip()
            if len(cleaned) >= 3 and not cleaned.startswith("\\"):
                if cleaned not in nodes:
                    nodes.append(cleaned)
            idx = end + 1
        else:
            idx += m.end()

    cap_clean = clean_inline_latex(caption).replace("\n", " ").strip() if caption else "Original Vector Technical Diagram"
    lbl_clean = label.strip() if label else "fig:diagram"
    lines = [
        f"> **[Vector Figure: {cap_clean} | Label: `{lbl_clean}`]**",
    ]
    if nodes:
        lines.append("> - **Diagram Annotations & Key Elements:** " + " • ".join(nodes[:18]))
    return "\n".join(lines) + "\n"


def convert_tabular_to_md(tab_body: str, default_headers: Optional[List[str]] = None) -> str:
    """Convert the body of a tabular / tabularx / ftab / errtab / vartab into a GFM pipe table."""
    body = tab_body
    body = re.sub(r"\\(?:toprule|midrule|bottomrule|hline|cline\{[^{}]*\})\b", "", body)
    body = re.sub(r"\\cmidrule(?:\([lr0-9.]*\))?\{[^{}]*\}", "", body)
    body = replace_cmd_1arg(body, "rowcolor", lambda _: "")

    # Split rows on \\ outside braces AND outside $...$ math mode!
    rows_raw: List[str] = []
    cur: List[str] = []
    i = 0
    n = len(body)
    depth = 0
    in_math = False
    while i < n:
        if body[i] == "\\" and i + 1 < n and body[i + 1] == "\\":
            if depth == 0 and not in_math:
                rows_raw.append("".join(cur))
                cur = []
                i += 2
                while i < n and body[i] in " \t":
                    i += 1
                if i < n and body[i] == "[":
                    eopt = find_matching(body, i, "[", "]")
                    if eopt != -1:
                        i = eopt + 1
                continue
            else:
                cur.append(r"\\")
                i += 2
                continue
        elif body[i] == "\\":
            if i + 1 < n:
                cur.append(body[i : i + 2])
                i += 2
                continue
        elif body[i] == "$":
            in_math = not in_math
        elif body[i] == "{":
            depth += 1
        elif body[i] == "}":
            depth = max(0, depth - 1)
        cur.append(body[i])
        i += 1
    if "".join(cur).strip():
        rows_raw.append("".join(cur))

    parsed_rows: List[List[str]] = []
    for r in rows_raw:
        r_str = r.strip()
        if not r_str:
            continue
        while r"\multicolumn" in r_str:
            m = re.search(r"\\multicolumn\s*\{(\d+)\}\s*\{", r_str)
            if not m:
                break
            e_align = find_matching(r_str, m.end() - 1)
            if e_align == -1:
                break
            c_txt = e_align + 1
            while c_txt < len(r_str) and r_str[c_txt] in " \t":
                c_txt += 1
            if c_txt < len(r_str) and r_str[c_txt] == "{":
                e_txt = find_matching(r_str, c_txt)
                if e_txt != -1:
                    span = int(m.group(1))
                    txt = r_str[c_txt + 1 : e_txt]
                    rep_cells = [txt] + [""] * max(0, span - 1)
                    r_str = r_str[: m.start()] + " & ".join(rep_cells) + r_str[e_txt + 1 :]
                    continue
            break

        # Split cells on unescaped & at depth 0 and outside $...$ math mode!
        cells: List[str] = []
        c_buf: List[str] = []
        ci = 0
        cn = len(r_str)
        cdepth = 0
        cmath = False
        while ci < cn:
            if r_str[ci] == "\\":
                if ci + 1 < cn:
                    c_buf.append(r_str[ci : ci + 2])
                    ci += 2
                    continue
            elif r_str[ci] == "$":
                cmath = not cmath
            elif r_str[ci] == "{":
                cdepth += 1
            elif r_str[ci] == "}":
                cdepth = max(0, cdepth - 1)
            elif r_str[ci] == "&" and cdepth == 0 and not cmath:
                cells.append("".join(c_buf))
                c_buf = []
                ci += 1
                continue
            c_buf.append(r_str[ci])
            ci += 1
        cells.append("".join(c_buf))

        cleaned_cells = []
        for cell in cells:
            c_clean = clean_inline_latex(cell)
            c_clean = re.sub(r"\s+", " ", c_clean).strip()
            c_clean = c_clean.replace("|", "\\|")
            cleaned_cells.append(c_clean)
        if any(cleaned_cells):
            parsed_rows.append(cleaned_cells)

    if default_headers:
        parsed_rows.insert(0, default_headers)

    if not parsed_rows:
        return ""

    ncols = max(len(r) for r in parsed_rows)
    norm_rows = [r + [""] * (ncols - len(r)) for r in parsed_rows]
    md_lines = [
        "| " + " | ".join(norm_rows[0]) + " |",
        "| " + " | ".join(["@@GFM_SEP@@"] * ncols) + " |",
    ]
    for r in norm_rows[1:]:
        md_lines.append("| " + " | ".join(r) + " |")
    return "\n" + "\n".join(md_lines) + "\n\n"


def convert_tex_to_markdown(tex_content: str) -> str:
    """Convert a full modular .tex file into clean GitHub-Flavored Markdown."""
    s = strip_comments(tex_content)

    # 1. Extract and replace tikzpicture environments (with brace-balanced \captionof{figure}{...} and \label{...})
    def _replace_tikz(txt: str) -> str:
        out: List[str] = []
        i = 0
        n = len(txt)
        pat = re.compile(r"\\begin\{tikzpicture\}(?:\[[^\]]*\])?")
        end_tag = r"\end{tikzpicture}"
        while i < n:
            m = pat.search(txt, i)
            if not m:
                out.append(txt[i:])
                break
            out.append(txt[i : m.start()])
            end_pos = txt.find(end_tag, m.end())
            if end_pos == -1:
                out.append(txt[m.start() : m.end()])
                i = m.end()
                continue
            code = txt[m.end() : end_pos]
            cur = end_pos + len(end_tag)
            cap = ""
            lbl = ""
            # Check for trailing \par, \vspace, \captionof{figure}{...}, \label{...}, \idxfig{...}
            while cur < n:
                ws_m = re.match(r"[\s\n]*(?:\\par\b|\\vspace\{[^{}]*\})*[\s\n]*", txt[cur:])
                if ws_m:
                    cur += len(ws_m.group(0))
                cap_m = re.match(r"\\captionof\{figure\}\s*\{", txt[cur:])
                if cap_m:
                    brace_pos = cur + len(cap_m.group(0)) - 1
                    ecap = find_matching(txt, brace_pos)
                    if ecap != -1:
                        cap = txt[brace_pos + 1 : ecap]
                        cur = ecap + 1
                        continue
                lbl_m = re.match(r"\\label\s*\{", txt[cur:])
                if lbl_m:
                    brace_pos = cur + len(lbl_m.group(0)) - 1
                    elbl = find_matching(txt, brace_pos)
                    if elbl != -1:
                        lbl = txt[brace_pos + 1 : elbl]
                        cur = elbl + 1
                        continue
                idx_m = re.match(r"\\idxfig\s*\{", txt[cur:])
                if idx_m:
                    brace_pos = cur + len(idx_m.group(0)) - 1
                    eidx = find_matching(txt, brace_pos)
                    if eidx != -1:
                        cur = eidx + 1
                        continue
                break
            # Also check if \label{...} was inside \captionof{figure}{... \label{...}}
            if not lbl and r"\label{" in cap:
                lm = re.search(r"\\label\{([^{}]*)\}", cap)
                if lm:
                    lbl = lm.group(1)
                    cap = cap[: lm.start()] + cap[lm.end() :]
            out.append("\n" + summarize_tikzpicture(code, cap, lbl) + "\n")
            i = cur
        return "".join(out)

    s = _replace_tikz(s)

    # 2. Extract \captionof{table}{...} and \caption{...} before tables
    s = replace_cmd_2arg(
        s,
        "captionof",
        lambda kind, cap: f"\n**{kind.capitalize()}:** {clean_inline_latex(cap).strip()}\n",
    )
    s = replace_cmd_1arg(
        s,
        "caption",
        lambda cap: f"\n**Table:** {clean_inline_latex(cap).strip()}\n",
    )

    # 3. Convert custom table environments (ftab, vartab, errtab) and standard tabular/tabularx
    s = re.sub(
        r"\\begin\{ftab\}([\s\S]*?)\\end\{ftab\}",
        lambda m: convert_tabular_to_md(m.group(1), ["**Formula**", "**Variables (SI units)**", "**Flags**", "**Use when**"]),
        s,
    )
    s = re.sub(
        r"\\begin\{vartab\}([\s\S]*?)\\end\{vartab\}",
        lambda m: convert_tabular_to_md(m.group(1), ["**Symbol**", "**Meaning**", "**SI unit**", "**Typical range**"]),
        s,
    )
    s = re.sub(
        r"\\begin\{errtab\}([\s\S]*?)\\end\{errtab\}",
        lambda m: convert_tabular_to_md(m.group(1), ["**Wrong move / Symptom**", "**What it produces / Why it fails**", "**5-second diagnostic & fix**"]),
        s,
    )

    def _replace_tabulars(txt: str) -> str:
        out: List[str] = []
        i = 0
        n = len(txt)
        pat = re.compile(r"\\begin\{(tabularx|tabular)\}")
        while i < n:
            m = pat.search(txt, i)
            if not m:
                out.append(txt[i:])
                break
            out.append(txt[i : m.start()])
            env = m.group(1)
            cur = m.end()
            while cur < n and txt[cur] in " \t\n":
                cur += 1
            if env == "tabularx" and cur < n and txt[cur] == "{":
                ew = find_matching(txt, cur)
                if ew != -1:
                    cur = ew + 1
            while cur < n and txt[cur] in " \t\n":
                cur += 1
            if cur < n and txt[cur] == "{":
                ecol = find_matching(txt, cur)
                if ecol != -1:
                    cur = ecol + 1
            end_tag = f"\\end{{{env}}}"
            end_pos = txt.find(end_tag, cur)
            if end_pos != -1:
                body = txt[cur:end_pos]
                out.append(convert_tabular_to_md(body))
                i = end_pos + len(end_tag)
            else:
                out.append(txt[m.start() : m.end()])
                i = m.end()
        return "".join(out)

    s = _replace_tabulars(s)

    s = re.sub(r"\\rowcolors\{[^{}]*\}\{[^{}]*\}\{[^{}]*\}", "", s)
    s = re.sub(r"\\(?:begin|end)\{(?:table|center|multicols)\}(?:\[[^\]]*\])?(?:\{[^{}]*\})?", "", s)
    s = re.sub(r"\\begin\{twocol\}(?:\[[^\]]*\])?", "\n", s)
    s = re.sub(r"\\nextcol(?:\[[^\]]*\])?", "\n\n", s)
    s = re.sub(r"\\end\{twocol\}", "\n", s)
    s = re.sub(r"\\begin\{minipage\}(?:\[[^\]]*\])?\{[^{}]*\}", "\n", s)
    s = re.sub(r"\\end\{minipage\}", "\n", s)

    # 4. Convert \binderchapter and \binderapp
    def _repl_chapter(txt: str, cmd: str, prefix: str) -> str:
        pat = re.compile(r"\\" + cmd + r"\s*\{")
        out: List[str] = []
        i = 0
        while i < len(txt):
            m = pat.search(txt, i)
            if not m:
                out.append(txt[i:])
                break
            out.append(txt[i : m.start()])
            args: List[str] = []
            cur = m.end() - 1
            ok = True
            for _ in range(4):
                while cur < len(txt) and txt[cur] in " \t\n":
                    cur += 1
                if cur < len(txt) and txt[cur] == "{":
                    e = find_matching(txt, cur)
                    if e != -1:
                        args.append(txt[cur + 1 : e])
                        cur = e + 1
                    else:
                        ok = False
                        break
                else:
                    ok = False
                    break
            if ok and len(args) == 4:
                num, title, _, lbl = args
                out.append(f"# {prefix}{num}: {clean_inline_latex(title).strip()} {{#{lbl.strip()}}}\n")
                i = cur
            else:
                out.append(txt[m.start() : m.end()])
                i = m.end()
        return "".join(out)

    s = _repl_chapter(s, "binderchapter", "§")
    s = _repl_chapter(s, "binderapp", "Appendix ")

    # 5. Convert \scopebanner
    def _repl_scopebanner(txt: str) -> str:
        pat = re.compile(r"\\scopebanner\b")
        out: List[str] = []
        i = 0
        while i < len(txt):
            m = pat.search(txt, i)
            if not m:
                out.append(txt[i:])
                break
            out.append(txt[i : m.start()])
            cur = m.end()
            opt1, cat, opt2 = "", "", ""
            while cur < len(txt) and txt[cur] in " \t":
                cur += 1
            if cur < len(txt) and txt[cur] == "[":
                e = find_matching(txt, cur, "[", "]")
                if e != -1:
                    opt1 = txt[cur + 1 : e]
                    cur = e + 1
            while cur < len(txt) and txt[cur] in " \t":
                cur += 1
            if cur < len(txt) and txt[cur] == "{":
                e = find_matching(txt, cur)
                if e != -1:
                    cat = txt[cur + 1 : e]
                    cur = e + 1
            while cur < len(txt) and txt[cur] in " \t":
                cur += 1
            if cur < len(txt) and txt[cur] in "[{":
                och = txt[cur]
                cch = "]" if och == "[" else "}"
                e = find_matching(txt, cur, och, cch)
                if e != -1:
                    opt2 = txt[cur + 1 : e]
                    cur = e + 1
            sub = clean_inline_latex(opt1 or opt2).strip()
            cat_c = clean_inline_latex(cat).strip()
            banner = f"> **[SCOPE: {cat_c}" + (f" | {sub}]**\n" if sub else "]**\n")
            out.append(banner)
            i = cur
        return "".join(out)

    s = _repl_scopebanner(s)

    # 6. Convert section headings (\section, \subsection, \subsubsection)
    s = replace_cmd_1arg(s, "section", lambda a: f"\n## {clean_inline_latex(a).strip()}\n")
    s = replace_cmd_1arg(s, "subsection", lambda a: f"\n### {clean_inline_latex(a).strip()}\n")
    s = replace_cmd_1arg(s, "subsubsection", lambda a: f"\n#### {clean_inline_latex(a).strip()}\n")

    # 7. Convert pedagogical callout environments using brace/bracket-balanced title parser
    box_titles = {
        "formulacard": "FORMULA & DECISION CARD",
        "formula": "FORMULA",
        "quick": "QUICK REFERENCE",
        "trapbox": "TRAP & DIAGNOSTIC",
        "trap": "TRAP",
        "devicebox": "2027 HEAT-COLLECTOR DEVICE & LAB",
        "labbox": "DEVICE & LAB",
        "rulebox": "2027 OFFICIAL RULE / CLARIFICATION",
        "tierbox": "TIER: STATE & NATIONALS (Rule 5.c.vi–vii)",
        "quicksheet": "ONE-PAGE QUICK SHEET",
        "quicksheet*": "ONE-PAGE QUICK SHEET",
        "shortcut": "SHORTCUT",
        "derivation": "DERIVATION",
        "suppbox": "SUPPLEMENTARY",
    }
    for env_name, badge in box_titles.items():
        pat_b = re.compile(r"\\begin\{" + re.escape(env_name) + r"\}")
        out_b: List[str] = []
        bi = 0
        while bi < len(s):
            m = pat_b.search(s, bi)
            if not m:
                out_b.append(s[bi:])
                break
            out_b.append(s[bi : m.start()])
            cur = m.end()
            title_arg = ""
            while cur < len(s) and s[cur] in " \t":
                cur += 1
            if cur < len(s) and s[cur] in "[{":
                och = s[cur]
                cch = "]" if och == "[" else "}"
                e = find_matching(s, cur, och, cch)
                if e != -1:
                    title_arg = clean_inline_latex(s[cur + 1 : e]).strip()
                    cur = e + 1
            out_b.append(f"\n### [{badge}" + (f": {title_arg}]\n" if title_arg else "]\n"))
            bi = cur
        s = "".join(out_b).replace(f"\\end{{{env_name}}}", "\n")

    # workedexample environment (brace/bracket balanced)
    pat_we = re.compile(r"\\begin\{workedexample\}")
    out_we: List[str] = []
    wi = 0
    while wi < len(s):
        m = pat_we.search(s, wi)
        if not m:
            out_we.append(s[wi:])
            break
        out_we.append(s[wi : m.start()])
        cur = m.end()
        we_title, we_meta = "", ""
        while cur < len(s) and s[cur] in " \t":
            cur += 1
        if cur < len(s) and s[cur] == "[":
            e = find_matching(s, cur, "[", "]")
            if e != -1:
                we_title = clean_inline_latex(s[cur + 1 : e]).strip()
                cur = e + 1
        for slot in range(2):
            while cur < len(s) and s[cur] in " \t":
                cur += 1
            if cur < len(s) and s[cur] == "{":
                e = find_matching(s, cur)
                if e != -1:
                    val = clean_inline_latex(s[cur + 1 : e]).strip()
                    if slot == 0:
                        if not we_title:
                            we_title = val
                        else:
                            we_meta = val
                    cur = e + 1
        out_we.append(
            f"\n### Worked Example — {we_title}" + (f" `[{we_meta}]`" if we_meta else "") + "\n"
        )
        wi = cur
    s = "".join(out_we).replace(r"\end{workedexample}", "\n")

    # problem and solution environments (brace-balanced 8-argument parser)
    def _repl_problem(txt: str) -> str:
        pat = re.compile(r"\\begin\{problem\}")
        out: List[str] = []
        i = 0
        while i < len(txt):
            m = pat.search(txt, i)
            if not m:
                out.append(txt[i:])
                break
            out.append(txt[i : m.start()])
            cur = m.end()
            args: List[str] = []
            ok = True
            for _ in range(8):
                while cur < len(txt) and txt[cur] in " \t\n":
                    cur += 1
                if cur < len(txt) and txt[cur] == "{":
                    e = find_matching(txt, cur)
                    if e != -1:
                        args.append(txt[cur + 1 : e])
                        cur = e + 1
                    else:
                        ok = False
                        break
                else:
                    ok = False
                    break
            if ok and len(args) == 8:
                c_args = [clean_inline_latex(a).strip() for a in args]
                out.append(
                    f"\n#### Problem {c_args[0]}: {c_args[1]} "
                    f"`[§{c_args[2]} | {c_args[3]} | {c_args[4]} | {c_args[5]} | {c_args[6]} | Trap: {c_args[7]}]`\n"
                )
                i = cur
            else:
                out.append(txt[m.start() : m.end()])
                i = m.end()
        return "".join(out)

    s = _repl_problem(s)
    s = s.replace(r"\end{problem}", "\n")
    s = re.sub(r"\\begin\{solution\}\{([^{}]*)\}", lambda m: f"\n**Solution {m.group(1)}:** ", s)
    s = s.replace(r"\end{solution}", "\n")

    # 8. Display math environments (use (?<!\\)\\\[ so \\[6pt] linebreaks are never mistaken for \[!)
    for m_env in ("equation", "equation*", "align", "align*"):
        s = re.sub(
            r"\\begin\{" + re.escape(m_env) + r"\}([\s\S]*?)\\end\{" + re.escape(m_env) + r"\}",
            lambda m: "\n$$\n\\begin{aligned}\n" + replace_siunitx(m.group(1).strip()) + "\n\\end{aligned}\n$$\n",
            s,
        )
    s = re.sub(
        r"(?<!\\)\\\[([\s\S]*?)(?<!\\)\\\]",
        lambda m: "\n$$\n" + replace_siunitx(m.group(1).strip()) + "\n$$\n",
        s,
    )

    # 9. Lists (itemize, enumerate, description)
    s = re.sub(r"\\(?:begin|end)\{(?:itemize|enumerate|description)\}(?:\[[^\]]*\])?", "\n", s)
    s = re.sub(r"^\s*\\item\[([^\]]+)\]\s*", lambda m: f"- **{clean_inline_latex(m.group(1)).strip()}** ", s, flags=re.MULTILINE)
    s = re.sub(r"^\s*\\item\s+", "- ", s, flags=re.MULTILINE)

    # 10. Clean remaining inline LaTeX
    s = clean_inline_latex(s)

    # Restore GFM table separator hyphens and strip standalone scoping braces `{` or `}`
    s = s.replace("@@GFM_SEP@@", "---")
    s = re.sub(r"^\s*[{}]\s*$", "", s, flags=re.MULTILINE)
    s = re.sub(r"\n{3,}", "\n\n", s).strip() + "\n"
    return s


def build_readme() -> str:
    """Generate markdown/README.md with clickable TOC and exact page budget."""
    lines = [
        "# 2026–2027 Science Olympiad Division C Thermodynamics — Editable Markdown Source Mirror",
        "",
        "> **Verified Rules Baseline:** `official-2027-C.pdf` (pp. C57–C59) + **9 Official 2027 National Clarifications** (`09/30/2026`–`10/28/2026`) + **0 Rules Corrections** (`Accessed 2026-11-22`).",
        "> **Reproducible Generator:** `python build/export_markdown.py`",
        "> **Unified Searchable Single-File Edition:** [`Thermodynamics_DivC_Complete_Binder.md`](Thermodynamics_DivC_Complete_Binder.md)",
        "",
        "## Master Table of Contents (33 Modular Chapters & Appendices — 248 Pages Total)",
        "",
        "| # | 9-Tab Group | Markdown File | LaTeX Source | Section Title & Scope | Target Pages |",
        "|---:|---|---|---|---|---:|",
    ]
    total_pp = 0
    for idx, (stem, title, pp, tab) in enumerate(SECTION_META):
        total_pp += pp
        lines.append(f"| {idx} | **{tab}** | [`{stem}.md`]({stem}.md) | `src/{stem}.tex` | {title} | **{pp} pp** |")
    lines.append(f"| — | **Total** | [`Thermodynamics_DivC_Complete_Binder.md`](Thermodynamics_DivC_Complete_Binder.md) | `src/main.tex` | **Complete 9-Tab Competition Binder** | **{total_pp} pp** |")
    lines.append("")
    return "\n".join(lines)


def audit_markdown(md_text: str, filename: str) -> List[str]:
    """Check for any leaked non-math LaTeX formatting/structural macros outside $...$ and $$...$$."""
    without_math = re.sub(r"\$\$[\s\S]*?\$\$|\$[^\$]+?\$", "", md_text)
    forbidden = re.findall(
        r"\\(?:textbf|textit|texttt|emph|SIrange|SI|si|num|binderchapter|binderapp|scopebanner|begin|end|toprule|midrule|bottomrule|rowcolor|idx\w*|sref|fref|tref|eref|src)\b",
        without_math,
    )
    return forbidden


def main() -> int:
    MD_DIR.mkdir(parents=True, exist_ok=True)
    readme_md = build_readme()
    (MD_DIR / "README.md").write_text(readme_md, encoding="utf-8")

    unified_parts: List[str] = [readme_md, "\n---\n"]
    total_bytes = len(readme_md.encode("utf-8"))
    leaked_total = 0

    for stem, title, pp, tab in SECTION_META:
        tex_path = SRC_DIR / f"{stem}.tex"
        if not tex_path.exists():
            print(f"[ERROR] Missing source file: {tex_path}", file=sys.stderr)
            return 1
        raw_tex = tex_path.read_text(encoding="utf-8")
        md_body = convert_tex_to_markdown(raw_tex)
        header = f"<!-- Source: src/{stem}.tex | Tab: {tab} | Target: {pp} pp -->\n"
        if not md_body.lstrip().startswith("# "):
            header += f"# {title}\n\n"
        full_md = header + md_body
        out_path = MD_DIR / f"{stem}.md"
        out_path.write_text(full_md, encoding="utf-8")
        b_len = len(full_md.encode("utf-8"))
        total_bytes += b_len

        leaks = audit_markdown(full_md, out_path.name)
        if leaks:
            print(f"[WARN] {out_path.name} has {len(leaks)} residual macros: {leaks[:5]}")
            leaked_total += len(leaks)
        unified_parts.append(full_md)
        unified_parts.append("\n---\n")

    complete_path = MD_DIR / "Thermodynamics_DivC_Complete_Binder.md"
    complete_md = "\n".join(unified_parts)
    complete_path.write_text(complete_md, encoding="utf-8")

    print(
        f"[OK] Exported {len(SECTION_META)} chapter/appendix Markdown files + README.md + "
        f"Thermodynamics_DivC_Complete_Binder.md ({len(complete_md.encode('utf-8')):,} bytes, "
        f"residual_macros={leaked_total})."
    )
    return 0 if leaked_total == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
