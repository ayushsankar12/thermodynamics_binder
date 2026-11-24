# Phase 3C — Build & QA Pipeline Architecture and Toolchain Smoke Specification

**Target Workspace:** `C:\science olympiad\Thermodynamics-Binder\`
**Smoke Test Artifacts:** `C:\science olympiad\Thermodynamics-Binder\build\smoke\` (`smoke.tex`, `binder.ist`, `run_smoke.py`, `smoke.pdf`, `smoke-gray.pdf`, `smoke-p1..p4.png`, `smoke-contact.png`, `smoke-gray-contact.png`)
**Verification Date:** `2026-11-22`

---

## 1. Machine Toolchain Verification & Engine Selection

### 1.1 Verified Binaries & Python Environment

| Tool | Exact Verified Executable Path | Version | Role in Pipeline |
|---|---|---|---|
| **MiKTeX `pdflatex`** | `C:\Users\ayush\AppData\Local\Programs\MiKTeX\miktex\bin\x64\pdflatex.exe` | **MiKTeX-pdfTeX 4.23 (MiKTeX 25.12)** | **Primary LaTeX compiler** (fast offline compilation, native `-jobname` & macro pre-injection for grayscale proof and standalone booklets). |
| **MiKTeX `makeindex`** | `C:\Users\ayush\AppData\Local\Programs\MiKTeX\miktex\bin\x64\makeindex.exe` | **MiKTeX 25.12 `makeindex`** | **Primary index generator** (`makeindex -q -s binder.ist <name>.idx` across all 7 named `imakeidx` `.idx` files). |
| **Tectonic** | `C:\science olympiad\tools\tectonic\tectonic.exe` | **Tectonic 0.17.0** | **Backup compiler only** (useful only if testing an uncached CTAN package online; not used for primary build). |
| **Primary Python (`python`)** | `C:\Users\ayush\AppData\Local\Programs\Python\Python310\python.exe` | **Python 3.10.4** | **Mandatory Python interpreter (`python`, NEVER `py`)**. Includes `fitz` (**PyMuPDF 1.22.5**), `pypdf` **6.19.0**, `pdfplumber` **0.11.6**, `numpy` **1.26.4**, `scipy` **1.15.3**, `sympy` **1.14.0**, `matplotlib` **3.10.9**, `PIL` (**Pillow 11.1.0**), `reportlab` **4.4.4**. |
| **Secondary Python (`py`)** | `C:\Users\ayush\AppData\Local\Programs\Python\Python313\python.exe` | **Python 3.13.1** | **DO NOT USE.** Bare install with zero scientific or PDF packages. |

> **PATH Requirement for Build Scripts:** MiKTeX's `bin\x64` directory is in `%LOCALAPPDATA%\Programs\MiKTeX\miktex\bin\x64` and is not on the default shell `PATH`. Every Python build script must prepend it at startup:
> ```python
> MIKTEX = Path(os.environ.get("LOCALAPPDATA", "")) / "Programs/MiKTeX/miktex/bin/x64"
> if MIKTEX.exists():
>     os.environ["PATH"] = str(MIKTEX) + os.pathsep + os.environ["PATH"]
> ```

### 1.2 Why Offline MiKTeX `pdflatex` + `makeindex` is Strictly Superior to `tectonic.exe`

1. **Multi-Index Support (`imakeidx` + `makeindex -s binder.ist`):** Our binder uses up to 7 distinct named indices (`alpha`, `fname`, `fsolve`, `subst`, `diag`, `proc`, `err`) with a custom style file (`src/binder.ist`). `build.py` runs `makeindex -q -s binder.ist <idx>` directly on every `.idx` file between `pdflatex` passes in `< 0.3 s`.
2. **Command-Line Pre-Injection for Grayscale Proof & Booklets:** `pdflatex -interaction=nonstopmode -file-line-error -jobname=main-gray "\def\grayproof{1}\input{main}"` compiles the grayscale proof from the exact same `main.tex` without modifying or copying files, and `xr-hyper` resolves cross-references across the companion booklets (`QuickRef_Handbook.pdf`, `Device_Lab_Handbook.pdf`, `Problem_Bank.pdf`) via `booklet-ext.aux`.
3. **100% Type 1 Font Embedding (`newtxtext` + `newtxmath`):** Under `pdflatex` with `\usepackage[T1]{fontenc}`, every glyph in `TeXGyreTermesX`, `NewTXMI`, `NimbusSanL`, `BeraSansMono`, and `Dingbats` embeds as an offline Type 1 `.pfa` outline font with zero bitmap (`Type 3`) fallbacks and zero network calls.

---

## 2. Verified Offline LaTeX Package Matrix

### 2.1 Packages Verified Working Offline in MiKTeX 25.12 (0 Errors, 0 Warnings)

Load in this exact sequence in `src/preamble.tex`:

1. **Document Class & Grayscale Hook (in `src/main.tex`):**
   ```latex
   \providecommand{\grayproof}{0}
   \ifnum\grayproof=1 \PassOptionsToPackage{gray}{xcolor}\fi
   \documentclass[10pt,twoside,openany,letterpaper]{book}
   ```
2. **Page Geometry (`geometry`):**
   ```latex
   \usepackage[letterpaper,twoside,inner=0.75in,outer=0.50in,top=0.62in,bottom=0.58in,
               includehead,includefoot,headheight=13pt,headsep=6pt,footskip=16pt]{geometry}
   ```
3. **Encoding, Math & Type 1 Fonts (`fontenc`, `inputenc`, `amsmath`, `newtxtext`, `newtxmath`, `helvet`, `beramono`, `textcomp`, `pifont`, `newunicodechar`, `microtype`):**
   ```latex
   \usepackage[T1]{fontenc}
   \usepackage[utf8]{inputenc}
   \usepackage{amsmath}
   \usepackage{newtxtext,newtxmath}
   \usepackage[scaled=0.90]{helvet}
   \usepackage[scaled=0.88]{beramono}
   \usepackage{textcomp}
   \usepackage{pifont}
   \usepackage{newunicodechar}
   \usepackage{microtype}
   \usepackage{setspace}\setstretch{1.05}
   \setlength{\parindent}{0pt}\setlength{\parskip}{2.2pt plus 0.8pt minus 0.4pt}
   ```
4. **Colors, Tables & Layout (`xcolor`, `colortbl`, `graphicx`, `array`, `tabularx`, `booktabs`, `longtable`, `multirow`, `makecell`, `multicol`, `enumitem`, `needspace`):**
   ```latex
   \usepackage[dvipsnames,table]{xcolor}
   \usepackage{colortbl}
   \usepackage{graphicx}
   \usepackage{array,tabularx,booktabs,longtable,multirow,makecell}
   \usepackage{multicol}
   \usepackage{enumitem}
   \setlist{nosep,leftmargin=1.3em}
   \usepackage{needspace}
   ```
5. **SI Units (`siunitx` v3 with Type 1 upright `\muup`):**
   ```latex
   \usepackage{siunitx}
   \sisetup{per-mode=symbol,group-minimum-digits=5,detect-all,
            product-units=single,range-units=single,list-units=single,mode=math}
   \DeclareSIPrefix{\micro}{\muup}{-6} % Uses newtxmath \muup; avoids CM Type 3 bitmap fallback
   ```
6. **Vector Graphics & Plots (`tikz`, `pgfplots` 1.18, `tcolorbox` `[most]`):**
   ```latex
   \usepackage{tikz}
   \usepackage{pgfplots}\pgfplotsset{compat=1.18}
   \usetikzlibrary{arrows.meta,positioning,calc,shapes.geometric,shapes.misc,
                   decorations.pathreplacing,decorations.pathmorphing,patterns,backgrounds,fit}
   \usepackage[most]{tcolorbox}
   ```
7. **Captions, Headings, Headers/Footers, Background Overlay, TOC & Multi-Index (`caption`, `titlesec`, `fancyhdr`, `lastpage`, `eso-pic`, `ifthen`, `tocbibind`, `tocloft`, `imakeidx`):**
   ```latex
   \usepackage{caption}
   \captionsetup{font=footnotesize,labelfont={bf,sf},labelsep=period,skip=2pt}
   \captionsetup[figure]{name=Fig.}
   \captionsetup[table]{name=Table}
   \usepackage{titlesec}
   \usepackage{fancyhdr}
   \usepackage{lastpage}
   \usepackage{eso-pic}
   \usepackage{ifthen}
   \usepackage[nottoc]{tocbibind}
   \usepackage{tocloft}
   \usepackage[noautomatic]{imakeidx}
   ```
8. **Cross-References & Hyperlinks (`xr-hyper` in booklets; `hyperref` loaded LAST):**
   ```latex
   \usepackage[hidelinks,bookmarksnumbered,bookmarksopen=false,pdfpagelabels]{hyperref}
   ```

### 2.2 Packages & Idioms to AVOID (Verified Failure Modes)

| Package / Idiom | Why to Avoid | Proven Replacement |
|---|---|---|
| `\usepackage{mathtools}` | **NOT cached in local MiKTeX 25.12** (caused fatal abort in legacy `Thermodynamics_DivC_Full_75pp.log` line 106). | Use `\usepackage{amsmath}` + `\usepackage{newtxtext,newtxmath}`. |
| `\usepackage{amssymb}` after `newtxmath` | Conflicts with `newtxmath` (`\Bbbk already defined`). | Omit `amssymb`; `newtxmath` already provides all AMS symbols (`\mathbb`, `\mathcal`, `\lesssim`, `\gtrsim`, etc.). |
| Default `\textmu` in `siunitx` | Triggers a Computer Modern TS1 Type 3 bitmap font fallback in PDF. | Use `\DeclareSIPrefix{\micro}{\muup}{-6}` and `\newunicodechar{µ}{\ensuremath{\muup}}` from `newtxmath`. |
| `\tabularx` directly inside a `tcolorbox` that has `attach title to upper={\ \ }` | Places the `tabularx` box horizontally *beside* the inline title, causing a `~195 pt` Overfull `\hbox` (discovered & fixed during smoke test). | Either start the box body with `\par\smallskip\noindent` before `\begin{tabularx}`, or use a standard header title bar (`colbacktitle=...`) for table-wrapping boxes. |
| `\tiny` (`< 5.0 pt`) inside TikZ diagrams | Triggers `pdfcheck.py` P5 small-text warning (`4.48 pt`). | Set `\begin{tikzpicture}[font=\scriptsize]` (`7.0 pt` at `10 pt` body) as the minimum diagram font size. |
| `latexmk` or `makeglossaries` | Requires Perl (not installed). | Drive `pdflatex` + `makeindex` directly from `build/build.py` in Python. |

---

## 3. Verified Geometry, 3-Hole Punch Clearance & Outer-Edge Thumb Tabs

### 3.1 US Letter `twoside` Geometry Budget

* **Paper Size:** US Letter (`8.50 in × 11.00 in` = `612.0 pt × 792.0 pt`).
* **Inner (Binding / 3-Hole Punch) Margin:** **`0.75 in` (`54.0 pt`)**
  * On **Odd Pages (recto):** Left edge `x ∈ [0.00 in, 0.75 in]` (`0.0 pt` to `54.0 pt`) is 100% clear of body text, headers, footers, and boxes.
  * On **Even Pages (verso):** Right edge `x ∈ [7.75 in, 8.50 in]` (`558.0 pt` to `612.0 pt`) is 100% clear of body text, headers, footers, and boxes.
  * Standard 3-hole punch diameter (`5/16 in` centered `3/8 in` to `7/16 in` from binding edge, reaching at most `0.60 in`) has a **`0.15 in` (`10.8 pt`) safety buffer** before the text column starts at `0.75 in`.
* **Outer (Thumb-Tab) Margin:** **`0.50 in` (`36.0 pt`)**
  * Text body width: `8.50 - 0.75 - 0.50 = 7.25 in` (`522.0 pt`).
  * Outer thumb-tab strip occupies the outer **`0.34 in` (`24.5 pt`)** flush to the paper edge (`x ∈ [8.16 in, 8.50 in]` on odd pages; `x ∈ [0.00 in, 0.34 in]` on even pages), leaving a **`0.16 in` (`11.5 pt`) white gutter** between the outer edge of the text column (`8.00 in` odd / `0.50 in` even) and the inner edge of the thumb tab.
* **Vertical Margins:** `top=0.62in` (`44.6 pt`), `bottom=0.58in` (`41.8 pt`), `includehead`, `includefoot`, `headheight=13pt`, `headsep=6pt`, `footskip=16pt`.

### 3.2 Outer-Edge Thumb-Index Implementation (`src/thumbindex.tex`)

```latex
\newcounter{tabslot}
\newcommand{\tablabel}{}
\newcommand{\settab}[2]{\clearpage\setcounter{tabslot}{#1}\renewcommand{\tablabel}{#2}}
\newcommand{\settabnoclear}[2]{\setcounter{tabslot}{#1}\renewcommand{\tablabel}{#2}}
\newlength{\tabslotheight}
\setlength{\tabslotheight}{0.70in}   % 13 slots x 0.70 in = 9.10 in vertical span
\AddToShipoutPictureBG{%
  \ifnum\value{tabslot}>0
  \AtPageUpperLeft{%
    \ifodd\value{page}
      \put(\LenToUnit{\paperwidth-0.34in},\LenToUnit{-0.85in-\value{tabslot}\tabslotheight+\tabslotheight}){%
        \makebox(0,0)[tl]{\color{tabblack}\rule{0.34in}{\tabslotheight}}}%
      \put(\LenToUnit{\paperwidth-0.17in},\LenToUnit{-0.85in-\value{tabslot}\tabslotheight+0.5\tabslotheight}){%
        \makebox(0,0){\rotatebox{-90}{\color{white}\sffamily\bfseries\scriptsize\tablabel}}}%
    \else
      \put(\LenToUnit{0in},\LenToUnit{-0.85in-\value{tabslot}\tabslotheight+\tabslotheight}){%
        \makebox(0,0)[tl]{\color{tabblack}\rule{0.34in}{\tabslotheight}}}%
      \put(\LenToUnit{0.17in},\LenToUnit{-0.85in-\value{tabslot}\tabslotheight+0.5\tabslotheight}){%
        \makebox(0,0){\rotatebox{90}{\color{white}\sffamily\bfseries\scriptsize\tablabel}}}%
    \fi}%
  \fi}
```

---

## 4. Grayscale-Surviving Color Palette & Category Callout Boxes

Every color in the palette is engineered with explicit CIE relative luminance $Y = 0.2126 R + 0.7152 G + 0.0722 B$, and every callout box pairs color with a **non-color structural distinguisher** (border weight, dashed/dotted/double line pattern, left bar thickness, Dingbat icon, and uppercase title prefix) so that when `\PassOptionsToPackage{gray}{xcolor}` is active in the grayscale proof (`smoke-gray.pdf`), zero semantic distinction is lost.

| Token | Hex / Gray Spec | Grayscale Luminance $Y$ | Text Contrast vs. Background | Non-Color Structural Distinguisher |
|---|---|---|---|---|
| `tabblack` | `gray = 0.08` (`#141414`) | $Y = 0.08$ | White text ($Y=1.00$, $\Delta Y = 0.92$) | Outer-edge thumb tab & `\scope` banner fill |
| `navy` | `HTML = 142B44` | $Y = 0.16$ | White title text ($\Delta Y = 0.84$) | `QUICK REFERENCE` solid dark header bar; `2027 OFFICIAL RULE` double border (`borderline={0.5pt}{1.5pt}{navy}`) |
| `rust` | `HTML = 8C2D19` | $Y = 0.23$ | Black text on white ($Y=1.00$) | `TRAP` heavy `1.8 pt` solid border + `\ding{110}` square icon |
| `slate` | `HTML = 3B4652` | $Y = 0.27$ | Black text on white ($Y=1.00$) | `DEVICE & LAB` thick `4.0 pt` left rule (`leftrule=4pt`) + `\ding{45}` pencil/gauge icon |
| `teal` | `HTML = 125E63` | $Y = 0.28$ | Black text on `boxbglight` ($Y=0.97$) | `SHORTCUT` `0.6 pt` frame + `\ding{228}` arrow icon |
| `amber` | `HTML = 6E4B00` | $Y = 0.30$ | Black title on `boxbg` ($Y=0.94$) | `TIER: States/Nationals-only` inner dotted border (`borderline={0.6pt}{1.5pt}{amber,dotted}`) |
| `rule` | `gray = 0.32` (`#525252`) | $Y = 0.32$ | Black text on `boxbg` ($Y=0.94$) | Standard table/box divider rule |
| `midgray` | `gray = 0.52` (`#858585`) | $Y = 0.52$ | Black text on `boxbglight` ($Y=0.97$) | `DERIVATION` borderless box with `1.8 pt` left bar only (`boxrule=0pt,leftrule=1.8pt`) |
| `boxbg` | `gray = 0.94` (`#F0F0F0`) | $Y = 0.94$ | Black text ($Y=0.00$, $\Delta Y = 0.94$) | `FORMULA` & `Example` header shaded background |
| `rowalt` | `gray = 0.95` (`#F2F2F2`) | $Y = 0.95$ | Black text ($Y=0.00$, $\Delta Y = 0.95$) | Alternating table row shading (`\rowcolors{2}{rowalt}{white}`) |
| `boxbglight`| `gray = 0.97` (`#F7F7F7`) | $Y = 0.97$ | Black text ($Y=0.00$, $\Delta Y = 0.97$) | `SHORTCUT` & `DERIVATION` subtle fill |

*(Note: `ASSUMPTIONS & VALIDITY` uses a white fill with a `0.6 pt` dashed black border `borderline={0.6pt}{0pt}{black,dashed},frame hidden`.)*

---

## 5. Thermodynamics Assumption Flags, Template Macros & PGFPlots Preamble

### 5.1 Standardized Assumption Flags (`src/boxes.tex`)

```latex
\newcommand{\flag}[1]{\textsf{\scriptsize\bfseries[#1]}}
\newcommand{\IG}{\flag{IDEAL-GAS}}      % PV = nRT, u(T) and h(T) only
\newcommand{\CLSD}{\flag{CLOSED}}       % Fixed mass (no mass crossing boundary)
\newcommand{\SSFL}{\flag{STEADY-FLOW}}  % Steady-state control volume (dm_cv/dt = 0, dE_cv/dt = 0)
\newcommand{\REV}{\flag{REV}}           % Internally/externally reversible process
\newcommand{\CONSTC}{\flag{CONST-$c$}}  % Constant specific heat over [T1, T2]
\newcommand{\LUMP}{\flag{Bi$<$0.1}}     % Lumped thermal capacitance (Bi = h L_c / k < 0.1)
\newcommand{\GRAY}{\flag{GRAY-SURF}}    % Diffuse-gray surface (epsilon = alpha)
\newcommand{\INCOMP}{\flag{INCOMP}}     % Incompressible liquid/solid (dv = 0)
\newcommand{\TIERf}{\flag{STATE/NAT}}   % 2027 Rule 5.c.vi-vii State/National tier topic
\newcommand{\RULEf}{\flag{2027-RULE}}   % 2027 Official Rule / National Clarification parameter
\newcommand{\SUPPf}{\flag{SUPP}}        % Supplementary enrichment beyond core syllabus
\newcommand{\VERIF}[1]{\textsf{\scriptsize[VERIFIED: #1]}}
```

### 5.2 PGFPlots & TikZ Standard Style

* Always enforce `\pgfplotsset{compat=1.18}`.
* Minimum text size inside any TikZ/PGFPlots environment is `\scriptsize` (`7 pt`); never use `\tiny` (`4.48 pt`).
* Pair line colors (`navy`, `teal`, `rust`, `black`) with distinct line styles (`solid`, `dashed`, `dotted`, `dashdotted`) and arrow tips (`-{Latex[length=2mm]}`) so multi-curve plots remain unambiguous in `smoke-gray.pdf`.

---

## 6. 4-Page Smoke Compile Results & PyMuPDF QA Report

### 6.1 Compilation Performance (`build/smoke/run_smoke.py`)

* **Color Target (`smoke.pdf`, 3 `pdflatex` passes + 2 `makeindex` passes across 3 `.idx` files):**
  * Return codes: `rc = (0, 0, 0)`
  * Index return codes: `[('alpha.idx', 0), ('fname.idx', 0), ('fsolve.idx', 0)]`
  * Wall time: **`10.59 s`** (`~3.4 s` per `pdflatex` pass)
* **Grayscale Proof Target (`smoke-gray.pdf`, 2 `pdflatex` passes with `\def\grayproof{1}`):**
  * Return codes: `rc = (0, 0)`
  * Wall time: **`5.70 s`**

### 6.2 Log & Mechanical QA Audit (`qa_check_pdf`)

| Check ID | QA Criterion | `smoke.pdf` (Color) | `smoke-gray.pdf` (Grayscale) | Verdict |
|---|---|---|---|---|
| **L1** | LaTeX compilation errors | `0` | `0` | **PASS** |
| **L2** | Undefined references / citations | `0` (`[]`) | `0` (`[]`) | **PASS** |
| **L3** | Multiply-defined labels | `0` (`[]`) | `0` (`[]`) | **PASS** |
| **L4** | Overfull `\hbox` / Overfull `\vbox` | `0` (`[]`) / `0` (`[]`) | `0` (`[]`) / `0` (`[]`) | **PASS** |
| **P0** | Exact PDF page count | `4` pages | `4` pages | **PASS** |
| **P1** | US Letter dimensions (`612.0 × 792.0 pt`) | All 4 pages exact (`size_bad=[]`) | All 4 pages exact (`size_bad=[]`) | **PASS** |
| **P2** | Unresolved `"??"` strings in PDF text | `0` (`qq=[]`) | `0` (`qq=[]`) | **PASS** |
| **P3** | 3-hole punch inner margin clearance (`0.72 in` / `51.84 pt` inside `0.75 in` inner margin; left on odd pages, right on even pages) | `0` violations (`punch_violations=[]`) | `0` violations (`punch_violations=[]`) | **PASS** |
| **P4** | Running footer (`Page N of 4` + `Rev. 2026-11-22`) on every page | Present on all 4 pages (`footer_missing=[]`, `rev_missing=[]`) | Present on all 4 pages (`footer_missing=[]`) | **PASS** |
| **P5** | Minimum font size across all spans (including figure labels) | **`5.48 pt`** (`>= 5.0 pt` threshold) | **`5.48 pt`** (`>= 5.0 pt` threshold) | **PASS** |
| **P6** | Font embedding (100% embedded Type 1 `.pfa`, zero Type 3 bitmaps) | 15/15 fonts embedded (`unembedded=set()`) | 15/15 fonts embedded (`unembedded=set()`) | **PASS** |
| **V1** | Visual inspection of 150 DPI PNG renders (`smoke-contact.png` & `smoke-gray-contact.png`) | Crisp layout, outer thumb tabs in `0.34 in` outer strip with `0.16 in` gutter, all 3 indices populated on p. 4 | High contrast across all 9 box types, tables, and plots | **PASS** |

### 6.3 Verified Embedded Font Inventory (15 Type 1 `.pfa` Fonts)

`TeXGyreTermesX-Regular`, `TeXGyreTermesX-Bold`, `NewTXMI`, `NewTXMI5`, `NewTXMI7`, `NewTXBMI`, `txsys`, `txbsys`, `txexs`, `txmiaX`, `NimbusSanL-Regu`, `NimbusSanL-Bold`, `TeXGyreHeros-Regular`, `BeraSansMono-Roman`, `Dingbats`.

---

## 7. Production Build & QA Pipeline Blueprint (`Thermodynamics-Binder/`)

When assembling the full production binder in Phase 5–10, mirror the proven `Circuit-Lab-Binder` pipeline with our 2027 Thermodynamics geometry (`inner=0.75in, outer=0.50in, top=0.62in, bottom=0.58in`):

1. **`build/build.py`**:
   * Targets: `main` (`Thermodynamics_DivC_Binder.pdf`), `gray` (`Thermodynamics_DivC_Binder_GRAYSCALE_PROOF.pdf`), `quickref` (`Thermodynamics_QuickRef_Handbook.pdf`), `labbook` (`Thermodynamics_Device_Lab_Handbook.pdf`), `problembank` (`Thermodynamics_Problem_Bank.pdf`), or `--all`.
   * Prepends `%LOCALAPPDATA%\Programs\MiKTeX\miktex\bin\x64` to `PATH`.
   * Runs `pdflatex` $\to$ `makeindex -q -s binder.ist` (across all 7 `.idx` files) $\to$ `pdflatex` $\to$ `makeindex` $\to$ `pdflatex` (plus up to 2 settle passes if `"Rerun to get"` appears).
   * Writes `src/booklet-ext.aux` from `main.aux` so standalone booklets resolve `\sref{...}` and `\pref{...}` into the full binder via `xr-hyper`.
2. **`verify/run_all.py`**:
   * Executes independent numerical verification scripts (`verify/checks/secNN.py`) using `numpy`/`scipy`/`sympy` under `python` (Python 3.10.4) for every worked example, table calculation, collector heat-balance model, and problem-bank item, writing `build/verification-report.md`.
3. **`qa/pdfcheck.py`, `qa/lint.py`, `qa/contradictions.py`, `qa/coverage.py`**:
   * `qa/pdfcheck.py`: Enforces P1–P6 via PyMuPDF (`fitz`) with `PUNCH = 0.70 * 72` (`50.4 pt` inside our `0.75 in = 54.0 pt` inner margin) and renders contact sheets for visual inspection.
   * `qa/lint.py`: Verifies zero placeholders (`TODO`, `TBD`, `???`), `\verified{...}` on every worked example, `\scope{...}` and `\alsosee{...}` on every section, all 7 solution elements on every problem-bank solution, and `\label{fig:...}` on every captioned figure.
   * `qa/contradictions.py`: Scans all `.tex` files for numerical/historical consistency across sections (CODATA 2022 constants, water triple/critical points, 2027 rule parameters: `100-125 W`, `30.0 cm` cube, `40-50 / 40-55 / 40-65 cm` bulb heights, `10 / 10-15 min` heating times, `100 mL` water in `9 oz` cup, `50/30/20` point split, 8 scientists birth/death years).
