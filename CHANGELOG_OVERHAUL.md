# Binder Overhaul — Change Log (branch `binder-overhaul`)

Every change made during the overhaul, by phase: file · old → new · reason.
Page numbers refer to the **baseline** build unless marked "new p.".

---

## Phase 1 — Baseline (2026-11-25)

### Toolchain on this machine
- macOS (Darwin 25.5), TeX Live 2026 **BasicTeX** (`/usr/local/texlive/2026basic`, root-owned, installed by Homebrew). `pdflatex` and `makeindex` present; `latexmk` absent (not needed: `build.py` drives pdflatex/makeindex directly).
- 25 missing LaTeX packages installed **in user mode** (`tlmgr --usermode`, into `~/Library/texmf`; nothing under `/usr/local` touched; user approved): newtx, bera, siunitx, pgfplots, tcolorbox, titlesec, tocloft, tocbibind, imakeidx, lastpage, enumitem, makecell, multirow, needspace, newunicodechar, environ, trimspaces, xstring, fontaxes, mweights, kastrup, pdfcol, tikzfill, listingsutf8, zref, ifoddpage. To undo: delete `~/Library/texmf`.
- Python venv `.venv/` (gitignored) with PyMuPDF 2.2, Pillow, NumPy 2.5, SciPy, SymPy.

### Tooling fixes needed to run the baseline (no content change)
| File | Old → New | Reason |
|---|---|---|
| `build/build.py` `run()` | `TEXINPUTS=f"{BUILD_DIR};{cwd};"` → `os.pathsep`-joined with trailing separator | `;` is the Windows separator. On macOS kpathsea read the whole string as one directory and dropped its default search path, so no package could be found. |
| `verify/checks/check_sec17_20.py` l.393 | `np.trapz(...)` → `np.trapezoid` (falls back to `np.trapz` on old NumPy) | NumPy 2.x removed `trapz`; the exception discarded all 49 checks in the module (225 instead of 274 ran). |

### New tool
- `qa/audit_metrics.py` — per page: word count (`get_text("words")`, same definition as the stated 694.5 baseline), smallest font, share of characters under 8 pt (all text, and excluding detected sub/superscripts), pages < 250 words; per PDF: literal `**`, empty headings (heading followed by another heading or the page end), figure captions with no "How to read" line. PDF points: TeX 8 pt prints as 7.97 pt, so "under 8 pt" = size < 7.9 pt. Output: `qa/metrics/<label>_*.json`, `qa/metrics/<label>_summary.md`.

### Baseline build (`python build/build.py --target all`, TeX Live 2026)
| PDF | Pages | Errors | Undefined refs | Overfull hbox (> 3 pt) | Overfull vbox | Underfull h / v | Float `[h]`→`[ht]` |
|---|---:|---:|---:|---:|---:|---:|---:|
| `Thermodynamics_DivC_Binder.pdf` | 264 | 0 | 0 | 28 (0; max 2.40 pt) | 0 | 72 / 99 | 10 |
| `..._GRAYSCALE_PROOF.pdf` | 264 | 0 | 0 | 28 (0) | 0 | 72 / 99 | 10 |
| `..._QuickRef_12pp.pdf` | 12 | 0 | 0 | 18 (0) | 0 | 20 / 0 | 0 |
| `..._Device_Handbook.pdf` | 46 | 0 | 0 | 7 (0) | 0 | 7 / 20 | 0 |

Main-binder package warnings: 155 hyperref (PDF-string tokens), 121 caption (`hypcap` ignored for `\captionof`), 8 newunicodechar, 5 imakeidx, 1 tcolorbox. Build time ≈ 270 s (main, 3 passes). One transient failure: the first Device Handbook run stopped mid-page 9 with no error (0-page PDF, copy raised `EIO`); an immediate rerun produced the normal 46 pp.

### Baseline QA
- `qa/pdfcheck.py`: **PASS** on all 4 PDFs (P1–P6, V1). Min font 5.08 pt (binder), 5.18 pt (QuickRef, Device Handbook).
- `verify/verify_all.py`: **274 / 274 pass** (after the `trapz` fix; 224/225 before).
- `qa/audit_metrics.py` (`qa/metrics/baseline_summary.md`):

| PDF | Median words/pg | Chars < 8 pt | < 8 pt excl. scripts | Chars < 7.5 pt | Pages mostly < 8 pt | Pages < 250 words | Min font | Pages with `**` | Empty headings | Figures without How-to-read |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Binder | 692.0 | 26.3% | 18.6% | 24.8% | 38 | 8 | 5.08 pt | 9 | 5 | 54 / 54 |
| QuickRef | 764.5 | 90.2% | 89.9% | 90.2% | 12 / 12 | 0 | 5.18 pt | 0 | 0 | 1 / 1 |
| Device Handbook | 672.5 | 25.2% | 17.2% | 23.3% | 4 | 2 | 5.18 pt | 0 | 0 | 12 / 12 |

Binder detail: pages mostly < 8 pt = 6, 8, 9, 10, 15, 16, 18, 24, 40, 41, 52, 72, 96, 229–247, 258, 260–264. Pages < 250 words = 5, 38, 68, 155, 172, 224, 244, 246. Literal `**` = 25, 26, 27, 32, 77, **105**, 126, 185, 212 (p105 is one more than the prompt listed). Empty headings = p95 §9.3 (→ §9.4), p212 §20.1, §20.2, §20.3 (each → next heading), p235 §23.7 (page end).

These agree with the prompt's stated baseline (median 694.5 words; 27% under 7.5 pt; 37 pages mostly under 8 pt; min 5.2 pt) to within differences in the PyMuPDF version and the TeX distribution.
