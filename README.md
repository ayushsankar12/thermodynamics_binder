# 2026–2027 Science Olympiad Division C — Thermodynamics Competition Binder

A comprehensive, competition-ready reference binder for the 2027 Science Olympiad Division C Thermodynamics event. Built entirely in LaTeX with original TikZ/PGFPlots vector figures, independently verified numerical content, and automated QA infrastructure.

## Output PDFs

| PDF | Pages | Description |
|---|---:|---|
| `Thermodynamics_DivC_Binder.pdf` | 264 | Full color competition binder with 9 thumb tabs, 14 quick sheets, 54 vector figures, and 5 printed indices |
| `Thermodynamics_DivC_Binder_GRAYSCALE_PROOF.pdf` | 264 | Grayscale print proof (identical content, verified legibility) |
| `Thermodynamics_DivC_QuickRef_12pp.pdf` | 12 | Standalone 12-page quick reference handbook |
| `Thermodynamics_DivC_Device_Handbook.pdf` | 46 | Standalone device engineering handbook (§14–§16, App D–F) |

## Quick Start

### Build All 4 PDFs

```bash
python build/build.py --target all
```

Requires offline MiKTeX 25.12 with cached packages. Build output goes to `output/`.

### Run Automated QA

```bash
python qa/pdfcheck.py                # Mechanical & visual QA (P1–P6 & V1) on all PDFs in output/
python verify/verify_all.py          # 274 independent numerical verification checks
python build/export_markdown.py      # Export LaTeX → Markdown mirror (residual_macros=0)
```

### Prerequisites

- **Python:** 3.10+ with `numpy`, `scipy`, `sympy`, `PyMuPDF`, `Pillow`
- **LaTeX:** MiKTeX 25.12 (offline, `%LOCALAPPDATA%\Programs\MiKTeX\miktex\bin\x64`)
- **Important:** Use `python` (not `py`) to invoke Python 3.10.4

## Binder Structure (264 pages)

| Tab | Sections | Pages | Topics |
|---|---|---:|---|
| **1 CMD/QUICK** | §0–§1 | 6–24 | Competition Command Center, 14 One-Page Quick Sheets |
| **2 FOUNDATIONS** | §2–§3 | 25–38 | Notation, SI/Imperial, Sign Conventions, Zeroth Law, 8 Scientists |
| **3 CAL/PHASE** | §4–§5 | 39–58 | Calorimetry, Dulong–Petit, Phase Diagrams, Clausius–Clapeyron |
| **4 GASES/LAWS** | §6–§9 | 59–102 | Ideal/Real Gases, 1st Law, 2nd Law, Engines & Cycles |
| **5 TRANSFER** | §10–§13 | 103–144 | Conduction, Convection, Radiation, Transient Systems |
| **6 DEVICE** | §14–§16 | 145–183 | Materials, Collector Engineering, Calibration & Prediction |
| **7 LAB/DATA** | §17–§18 | 184–203 | Thermometry, Uncertainty (GUM), Data Analysis |
| **8 PROBLEMS** | §19–§23 | 204–236 | Problem Solving, Misconceptions, Exam Strategy, Corpus Analysis |
| **9 INDEX/APP** | App A–H | 237–264 | Constants, Formula Index, 5 Indices, Test Log, Compliance, References |

## Key Features

- **163 worked examples** — every one independently verified (`\verifiedby{}`)
- **54 original vector figures** — TikZ/PGFPlots, no raster images
- **274 numerical verification checks** — CODATA 2022, NIST IAPWS-95, scoring formulas
- **14 detachable Quick Sheets** (QS-01..QS-14) — each exactly 1 printed page
- **5 printed indices** — Topic (650), Formula (253), Figure (66), Error (114), Device (81) = **1,164 entries**
- **10-second question router** — symptom → equation in < 10 s via flowchart + tabs + indices
- **2027 rules compliant** — Clause-by-clause matrix (App E), 11 official FAQs (checked 26 Nov 2026), 0 corrections
- **Sign convention locked** — Physics primary (ΔU = Q − W_by), Chemistry cross-referenced

## Sources

35 sources (`[S01]`–`[S35]`) documented in App G (p. 263) and `deliverables/RESEARCH_LOG.md`:
- **Tier 1 (30):** 2027 Rules Manual, CODATA 2022, NIST Chemistry WebBook, Lienhard 6th ed., OpenStax, MIT OCW, 8 exam corpus
- **Tier 2 (3):** Schroeder, Zemansky & Dittman / Callen, ASHRAE
- **Tier 3 (2):** Engineering ToolBox (cross-checked)

## Deliverables

| # | Deliverable | File |
|---:|---|---|
| 1 | Gate 0 Rules & Tournament Report | `deliverables/01_Gate_Rules_Tournament_Report.md` |
| 2 | Rules Compliance Matrix | `deliverables/02_Rules_Compliance_Matrix.md` |
| 3 | Architecture Lock | `build/architecture-lock.md` |
| 5 | 12-Page QuickRef Handbook | `output/Thermodynamics_DivC_QuickRef_12pp.pdf` |
| 6 | Research Log | `deliverables/RESEARCH_LOG.md` |
| 7 | Tournament Intelligence Report | `deliverables/07_Tournament_Intelligence_Report.md` |
| 8 | Audit Coverage & Defect Report | `deliverables/08_Audit_Coverage_Defect_Report.md` |
| 9 | Study & Device Testing Plan | `deliverables/09_Study_and_Device_Testing_Plan.md` |
| 10 | Maintenance Instructions | `deliverables/10_Maintenance_Instructions.md` |

## QA Infrastructure

- **`qa/pdfcheck.py`** — Automated mechanical QA: page count, font sizes (≥ 5.0 pt), Type 1 embedding, punch margins, overfull boxes, visual renders
- **`verify/verify_all.py`** — 274 independent numerical checks across 8 modules
- **`build/export_markdown.py`** — LaTeX → Markdown mirror with residual macro validation
- **`build/build.py`** — Multi-target build orchestrator with MakeIndex, settle passes, and speed optimization

## Audit Results (2026-11-22)

- **15/15 Quality Audits:** PASS
- **7/7 Reviewer Passes:** PASS
- **274/274 Numerical Checks:** PASS
- **4/4 PDFs:** PASS (P1–P6 & V1)
- **25-Prompt Retrieval Speed:** median 4.5 s, max 5 s (< 10 s target)
- **0 residual defects**
