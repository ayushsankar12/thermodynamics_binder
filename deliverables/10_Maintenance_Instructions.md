# Deliverable 10: Binder Maintenance, Rules-Update, Selective Reprinting & Build/QA Guide

**Baseline Revision Date:** `2026-11-22`  
**Workspace Root:** `C:\science olympiad\Thermodynamics-Binder\`  
**Verified Build & QA Toolchain:**
- **LaTeX Engine:** Offline **MiKTeX 25.12** (`pdflatex.exe` + `makeindex.exe` in `%LOCALAPPDATA%\Programs\MiKTeX\miktex\bin\x64`, automatically prepended to `PATH` by `build/build.py`).
- **Python Interpreter:** **Python 3.10.4** — always invoke as `python` (do **not** invoke `py`, which points to a bare Python 3.13 install without `PyMuPDF` or `Pillow`).
- **Build Orchestrator:** `C:\science olympiad\Thermodynamics-Binder\build\build.py`
- **Style & Index Specifications:** `build/thermobinder.sty` and `build/binder.ist`
- **Automated Mechanical & Visual QA Verifier:** `C:\science olympiad\Thermodynamics-Binder\qa\pdfcheck.py`

---

## 1. Pre-Tournament Official Rules & Clarification Check Protocol

Under **General Rule 3** (`official-2027-C.pdf`, p. C1), all official policies, rule corrections, and rule clarifications posted on `www.soinc.org` must be treated as if they were printed in the Rules Manual. Seven (7) days and again twenty-four (24) hours before every Invitational, Regional, State, and National tournament, run the following 3-minute verification check against our `2026-11-22` baseline:

### 1.1 National Rules Corrections (`https://www.soinc.org/events/rules-corrections`)
- **Baseline as of `2026-11-22`:** **0 (zero)** official Rules Corrections for Thermodynamics B or Thermodynamics C.
- **Action if a new correction appears:**
  1. Log the correction date, affected rule clause, and exact replacement wording on **Appendix F (`App F`, Verify-Against-Current-Rules Checklist)**.
  2. Update the corresponding `rulebox` in `src/` (typically in the Rules & Scoring chapter and on the 1-page Command Center / Device Checklist quick sheet).
  3. Recompile and reprint the affected duplex leaf pair(s) using the workflow in Sections 4–5 below.

### 1.2 National Rules Clarifications (`https://www.soinc.org/division-c-events` → `Thermodynamics - Div C`)
- **Baseline as of `2026-11-22`:** **9 active official National Rules Clarifications** (dated `09/30/2026` through `10/28/2026`, all fully integrated into the binder):
  1. `09/30/2026` (`5.g` L4): Water will **not** be stirred or swirled before temperature measurement.
  2. `10/01/2026` (`5.g` L1): Students may **not** swish water around in the cup prior to temperature measurement.
  3. `10/06/2026` (`5.g` L2): Students may **not** swirl, shake, or stir the cup when removing it.
  4. `10/06/2026` (`5.g` L4): Local ES sets uniform thermometer protocol; National recommendation is to measure the **top layer of water near the center of the cup**, inserting a probe only far enough for an accurate reading and no farther.
  5. `10/21/2026` (`5.d` L2): Teams **may place something on or around the cup** (e.g., plastic cling wrap or foil) during Water Setup Time, provided **no adhesives, tapes, or fasteners (rubber bands, clips) are applied or attached to the cup**, cup shape/structural integrity is unaltered, and all wrap/components are completely removed before $T_{\text{final}}$ measurement (`5.II.g`).
  6. `10/22/2026` (`3.i` [`3.b.i`] L1): **Polystyrene (including Styrofoam and `#6 PS` plastics)** is classified as hazardous under a heat lamp and is **prohibited** (`3.b.i` violation bars the device from setup/testing: $\text{TS}=\text{PS}=0$).
  7. `10/22/2026` (`5.b` [`5.II.b`] L5.2): Lifting/opening a reflector or lid to insert the cup and returning the lid to its original position is allowed as part of `"inserting or removing the cup."`
  8. `10/22/2026` (`5.b` [`5.II.b`] L4): Opening/closing a lid or door or altering device orientation/position as needed to insert the cup is **not** considered an illegal post-setup modification.
  9. `10/28/2026` (`2.d` L1): Failure to impound the device incurs **one additional construction violation** ($\times 0.7$ multiplier to $\text{TS}$ and $\text{PS}$).
- **Action if a 10th+ clarification is posted:** Add it to the Clarifications Table in `src/` and record it by hand or reprint on `App F`.

### 1.3 Official National Scoresheet & Team Checklist (`https://www.soinc.org/scoresheets`)
- **Baseline as of `2026-11-22`:**
  - `2027ThermodynamicsBC_checklist.pdf` — updated `10/20/2026`
  - `2027ThermodynamicsBC_scoresheet.xlsx` — **v2.0.0**, updated `11/06/2026`
- Check `https://www.soinc.org/scoresheets` for any version bump beyond `v2.0.0`.

---

## 2. Handling Tournament Host Modifications & Tier Toggling

Under **General Rule 7** (`p. C1`) and **Event Type Descriptions** (`p. C2`), Tournament Directors may announce site-dependent parameters, tier elevations, or format modifications (ideally at least 30 days prior to the tournament). Configure the binder and device kit for each tournament as follows:

1. **Regional vs. State/National Written Syllabus Tier (`Rule 5.I.c.vi–vii`):**
   - In the binder, all sections covering **Radiant Exitance, Blackbody Radiation, Stefan–Boltzmann Law & Third Law (`5.c.vi`)** and **Entropy & Enthalpy (`5.c.vii`)** are clearly badged with `\scopebanner{TIER-DEPENDENT}[Rule 5.c.vi--vii (State/National Tier)]` and `tierbox` environments.
   - **Important Empirical Note (`Deliverable 07`):** Because **100% (8/8)** of public invitational/regional exams in our corpus tested `5.c.vii` (entropy/enthalpy) and **75% (6/8)** tested `5.c.vi` (radiation/Third Law) — including `28.6%` of total points on the `2026-11-14` Cornell Invitational — **never remove the State/National chapters from the physical binder**, even at a Regional tournament!
2. **Bulb Height, Heating Time & Wattage Calibration (`Rule 4.a,c` & `Rule 5.II.a`):**
   - **Bulb Height ($h_{\text{bulb}}$ from Testing Surface to bottommost point of bulb):**
     - Regionals: $40, 45,\text{ or } 50\text{ cm}$ ($5\text{ cm}$ increments)
     - States: $40, 45, 50,\text{ or } 55\text{ cm}$ ($5\text{ cm}$ increments)
     - Nationals (and many University Invitationals): $40\text{ to } 65\text{ cm}$ ($1\text{ cm}$ increments)
   - **Heating Time ($t_{\text{heat}}$):**
     - Regionals: $10\text{ min}$
     - States/Nationals: $10, 11, 12, 13, 14,\text{ or } 15\text{ min}$ ($1\text{ min}$ increments)
   - **Bulb Wattage ($P_{\text{bulb}}$):** $100\text{–}125\text{ W}$ untinted incandescent/IR heat lamp bulb (typically $100\text{ W}$ or $125\text{ W}$ clear R40/BR40).
   - **Action when the team recalibrates or builds a new device revision:** Update the empirical parameters $(P_{\text{abs}}, R_{\text{th}}, C_{\text{eff}}, \tau, \kappa_{\text{strat}})$ in the device prediction chapter in `src/`, run `python build/build.py --target all`, and reprint **only** the `Thermodynamics_DivC_Device_Handbook.pdf` and the corresponding prediction table pages in the main binder!
3. **Satellite / MiniSO / Written-Only Tournament Fallback (`Manual p. C2`):**
   - If a tournament runs in written-only mode (omitting live Part II lamp testing so $\text{FS} = \text{ES}$), leave the device and spare parts at home, bring **both partners**, **two Class III calculators**, and the **full Main Binder + 12-Page QuickRef Booklet**, and assign Partner B directly to the back half of the written test from minute 0:00.

---

## 3. Repository Layout & Editing Individual `.tex` Chapters in `src/`

### 3.1 Directory Structure
```text
C:\science olympiad\Thermodynamics-Binder\
├── build\
│   ├── thermobinder.sty       # Master LaTeX package (geometry, 9 thumb tabs, 7 boxes, 5 indices, grayscale hook)
│   ├── binder.ist             # MakeIndex formatting style (bold letter headers, dot leaders)
│   ├── build.py               # Multi-pass Python 3.10 build orchestrator (--target main|gray|quickref|device|all)
│   ├── build-log.txt          # Cumulative timestamped build & warning audit log
│   └── pdfcheck-report.md     # Latest automated PyMuPDF P1–P6 & V1 verification report
├── src\
│   ├── main.tex               # Master driver for Thermodynamics_DivC_Binder.pdf & GRAYSCALE_PROOF.pdf
│   ├── quickref.tex           # Companion driver for Thermodynamics_DivC_QuickRef_12pp.pdf
│   ├── device.tex             # Companion driver for Thermodynamics_DivC_Device_Handbook.pdf
│   └── ch*.tex / app*.tex     # Modular chapter and appendix source files
├── output\
│   ├── Thermodynamics_DivC_Binder.pdf
│   ├── Thermodynamics_DivC_Binder_GRAYSCALE_PROOF.pdf
│   ├── Thermodynamics_DivC_QuickRef_12pp.pdf
│   └── Thermodynamics_DivC_Device_Handbook.pdf
├── qa\
│   ├── pdfcheck.py            # Automated PyMuPDF (fitz) + Pillow mechanical & visual verifier
│   └── renders\               # 150 DPI PNG page renders & composite visual contact sheets
├── deliverables\              # Standalone Part J Markdown deliverables (01 through 10)
└── research\                  # Phase 1–4 verified primary research datasets & logs
```

### 3.2 Rules for Safe `.tex` Editing
1. **UTF-8 Direct File Writes Only:** Always edit `.tex` files in a UTF-8 text editor (e.g., VS Code) or via Python `Path.write_text(..., encoding="utf-8")`. Never write `.tex` files through shell heredocs that strip or collapse double backslashes (`\\`).
2. **Offline MiKTeX 25.12 Package Compatibility:**
   - Do **not** load `\usepackage{mathtools}` (not pre-cached in offline MiKTeX; `amsmath` is loaded by `thermobinder.sty`).
   - Do **not** load `\usepackage{amssymb}` (conflicts with `newtxmath` `\Bbbk`; `newtxmath` already provides all AMS symbols).
   - Never use `\tiny` (`< 5.0 pt`) anywhere in text or TikZ figures; use `\scriptsize` (`7.0 pt`) as the smallest figure label size so `qa/pdfcheck.py` check **P6** passes with margin.
   - Inside `tcolorbox` environments (`formulacard`, `workedexample`, `trapbox`, `devicebox`, `rulebox`, `tierbox`), always place `\par\smallskip\noindent` before starting a `\begin{tabularx}` or `\begin{longtable}`.
3. **Mandatory Verification & Indexing Macros:**
   - Every `workedexample` must end with `\verifiedby{<independent method, e.g., energy balance + Python sympy check>}`.
   - Tag new concepts, equations, figures, traps, and device failure modes with the 5 named index macros: `\idxtopic{...}`, `\idxformula{...}`, `\idxfig{...}`, `\idxerr{...}`, and `\idxdev{...}`.

---

## 4. Rebuilding the PDFs & Running Automated QA (`build.py` + `pdfcheck.py`)

Open PowerShell in `C:\science olympiad\Thermodynamics-Binder` and run:

### 4.1 Build Commands (`python build/build.py`)
```powershell
# Rebuild all 4 production PDFs (Main Binder, Grayscale Proof, 12-Page QuickRef, Device Handbook):
python build/build.py --target all

# Or rebuild a single target during rapid chapter editing:
python build/build.py --target main       # -> output/Thermodynamics_DivC_Binder.pdf
python build/build.py --target gray       # -> output/Thermodynamics_DivC_Binder_GRAYSCALE_PROOF.pdf
python build/build.py --target quickref   # -> output/Thermodynamics_DivC_QuickRef_12pp.pdf
python build/build.py --target device     # -> output/Thermodynamics_DivC_Device_Handbook.pdf
```
- **What `build.py` does automatically:**
  1. Prepends `%LOCALAPPDATA%\Programs\MiKTeX\miktex\bin\x64` to `PATH` and syncs `thermobinder.sty` + `binder.ist` into `src/`.
  2. For `main` and `gray`: runs `pdflatex` $\to$ `makeindex -q -s binder.ist` across all 5 named `.idx` files (`topic`, `formula`, `figure`, `error`, `devfail`) $\to$ `pdflatex` $\to$ `makeindex` $\to$ `pdflatex` (plus settle passes if labels shifted).
  3. For `quickref` and `device`: extracts `booklet-ext.aux` from `src/main.aux` so all `\ref{}` / `\pageref{}` pointers to the Main Binder resolve accurately via `xr-hyper`, and runs 3 `pdflatex` passes with `\def\companionmode{1}`.
  4. Audits `.log` files for LaTeX errors, undefined references, multiply-defined labels, overfull `\hbox > 3.0 pt`, and overfull `\vbox`, writing a full summary to `build/build-log.txt`.

### 4.2 Automated Mechanical & Visual QA (`python qa/pdfcheck.py`)
```powershell
# Verify all PDFs in output/ and generate 150 DPI visual contact sheets in qa/renders/:
python qa/pdfcheck.py

# Or check a specific PDF:
python qa/pdfcheck.py output/Thermodynamics_DivC_Binder.pdf
```
- **All 6 Mechanical Gates (`P1`–`P6`) + Visual Gate (`V1`) must report `PASS` in `build/pdfcheck-report.md` before printing:**
  - **P1:** Every page is exact US Letter (`612.0 x 792.0 pt`).
  - **P2:** Main Binder & Grayscale Proof $\le 280\text{ pages}$; QuickRef Handbook $== 12\text{ pages}$.
  - **P3:** Zero unresolved `"??"` references or leaked raw LaTeX macros.
  - **P4:** Zero text spans intruding into the `0.72 in` (`51.84 pt`) inner 3-hole-punch zone (`x0 < 51.84 pt` on odd pages; `x1 > 560.16 pt` on even pages).
  - **P5:** Every page $> 1$ displays `"Page N of M"` and revision date `"2026-11-22"`.
  - **P6:** Minimum font size $\ge 5.0\text{ pt}$ and 100% embedded Type 1 fonts (zero Type 3 bitmap fonts).
  - **V1:** Inspect the newly generated 150 DPI PNGs and `*_contact_sheet.png` in `qa/renders/` to confirm zero visual overlap, clipped boxes, or illegible grayscale shading.

---

## 5. Selective Duplex-Safe Page-Pair Replacement (No Full Reprint Needed)

Because `thermobinder.sty` uses `twoside` duplex geometry (`inner=0.75in` on the 3-hole punch edge, `outer=0.50in` with the `0.34 in` outer thumb-tab strip), **odd pages ($2k-1$, recto)** have their punch margin on the **left** and thumb tabs on the **right**, while **even pages ($2k$, verso)** have their punch margin on the **right** and thumb tabs on the **left**.

When you edit a table, calibration curve, or rule box in `src/`:
1. **Keep the Edit Page-Count-Neutral whenever possible:**
   - Since each major chapter and each `quicksheet` ends with a `\clearpage` boundary, adding or editing lines inside a chapter or quick sheet that does not push that chapter across an extra page break leaves **every subsequent page number in the entire binder unchanged**!
2. **Identify the Physical Duplex Leaf Pair $(2k-1,\; 2k)$:**
   - Every physical sheet in the 3-ring binder consists of **odd page $2k-1$ on the front** and **even page $2k$ on the back**:
     - If you edited **Page 17** (odd), its physical sheet is **Pages `17–18`**.
     - If you edited **Page 42** (even), its physical sheet is **Pages `41–42`**.
3. **Print Only the Changed Duplex Leaf Pair:**
   - In your PDF viewer (Adobe Acrobat / SumatraPDF / Edge), open `output/Thermodynamics_DivC_Binder.pdf` (or `Thermodynamics_DivC_Binder_GRAYSCALE_PROOF.pdf` if printing on a monochrome laser printer).
   - Set **Pages:** `2k-1 - 2k` (e.g., `41-42`).
   - Set **Page Sizing:** **Actual Size / 100%** (never "Fit to Printable Area", which shrinks margins and shifts outer thumb tabs!).
   - Set **Two-Sided / Duplex:** **Print on both sides — Flip on Long Edge**.
   - Punch (or print directly onto pre-punched 24 lb / 28 lb laser paper or matte top-loading sheet protectors) and swap the single leaf into the 3-ring binder.
4. **If an Edit Changes Total Page Count:**
   - Reprint the affected chapter from the edit point to its final `\clearpage`, plus the **Back-of-Book Indices (`App H`)** so index page pointers remain 100% exact.
