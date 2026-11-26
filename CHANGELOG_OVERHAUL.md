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

---

## Phase 2 — Accuracy

Example numbers below are the **source labels** (`ex:NN.M`), which is how the overhaul prompt cites them. Where the printed number differs (all of §1, §8.6–8.8, §15 after 15.1, §16 after 16.2), the printed number is given in brackets. Every changed number has a check in `verify/checks/check_examples_recomputed.py`; its tolerance comes from the printed precision, so a check fails if the recomputed value does not round to the printed value.

### 2a. Flagged worked-example errors
| Example | File | Old → New | Reason |
|---|---|---|---|
| Ex 11.1 | `sec11.tex` | 0.670·Ra^¼ = 50.888 → **51.15**; denominator 1.2768 → **1.3027**; Nu 40.54 → **39.94**; h̄ 3.581 → **3.53** W/(m²·K); Q̇ "4.51 W (or 4.45)" → **4.45 W**; doubled ΔT "2.378×, 10.6 W" → **10.5 W, ratio 2.37** (power law 2.38 noted) | arithmetic errors; two conflicting answers |
| Ex 12.1 | `sec12.tex` | M_fil 6.581e5 → **6.585e5** W/m² (6.5814e5 → 6.5845e5 in working); L 2.095e5 → **2.096e5** W/(m²·sr); A 1.899e-4 m² / 1.90 cm² → **1.898e-4 m² / 1.898 cm²** | σT⁴ arithmetic |
| Ex 12.3 | `sec12.tex` | σ(T₁⁴−T₂⁴) 150.76 → **150.64**; card 128.4 → **128.3**; foil 3.077 → **3.074**; 2 shields 1.026 → **1.025** W/m²; T_s 307.08 K / 33.93 °C → **307.30 K / 34.15 °C** | arithmetic |
| Ex 09.3 | `sec09.tex` | 9.5^0.4 2.46078 → **2.46087**; η 0.59363 → **0.59364**; T₂ 738.24 → **738.26** K; P₂ 2337.7 → **2337.8** kPa; w_net 474.90 → **474.91**; MEP 616.35 → **616.37** kPa; η_Diesel(9.5) 0.52425 → **0.52426** (52.43%); T₄ 752.41 → **752.39** K; q_C 325.10 → **325.09** | one power slipped, everything downstream shifted |
| Ex 09.4 | `sec09.tex` | r_p,opt 16.120 → **16.14**; Stirling W 3457.4 → **3457.9**, Q₁→₂ 5186.1 → **5186.8** J; η(0.85) 48.99% → **49.00%**; Q_isochor/Q₁→₂ 2.405 → **2.404** | (2.21359)^3.5 = 16.138; Stirling values used R ≈ 8.3137 |
| Ex 07.6 | `sec07.tex` | W₂→₃ = Q₂→₃ 5186.1 → **5186.8**; W₄→₁ −1728.7 → **−1728.9**; net 3457.4 → **3457.9** J (table, sum and verified line) | R slip (8.31332 implied) |
| Ex 05.5 | `sec05.tex` | ω₁ 0.016045 → **0.016046**; m_a 1134.9 → **1135.1** kg; ω₂ 0.010649 → **0.010650**; m_cond 6.124 → **6.125** kg | arithmetic/truncation |
| Ex 04.1 | `sec04.tex` | "matches Copper … or Zinc!" → Dulong–Petit (65 g/mol) cannot separate Cu/Zn; c = 383 J/(kg·K) is closer to Cu (385) than Zn (388) → **copper**; density check (27.9 vs 35.0 cm³ for 250.0 g) | ambiguous answer |
| Ex 03.2 | `sec03.tex` | answers 125.5 °C / 307.3 °C → working kept, answers **≈1.3×10² °C / ≈3.1×10² °C** + sig-fig note | 0.010 cm gap has 2 s.f. |
| Ex 13.2 | `sec13.tex` | added "What C_eff means here" paragraph: fitted effective top-layer capacitance, why < 418.4 J/K, modeled value, fit your own | C_eff = 380 J/K < 418 J/K of the water alone; see `REVIEW_NEEDED.md` A1 |
| §20 intro | `sec20.tex` | "proves that over 70% of lost calculation points stem from 16 recurring … traps" → traps recur across keys and PER research; "We have no statistic for how many points each trap costs" | unsourced statistic (corpus lists 10 traps, no loss %) |
| Ex 20.1 | `sec20.tex` | "Naive Trap Path (What 65% of Contestants Write)" → "(the common wrong setup)" | unsourced statistic |
| §8 tierbox + banner | `sec08.tex` | "8/8 (100%) of invitational and regional exams tested ΔS, ΔH, and ΔG" → "every exam had at least one entropy/enthalpy (5.c.vii) item" (7 invitationals + 1 regional, 7 under 2018–19 rules); banner "Tested on 8/8 Invitational Exams!" → "on all 8 exams in our corpus" | corpus supports ≥1 5.c.vii item per exam, not ΔG on all 8 (ΔG items only in E2) |
| QuickRef QR banner | `quickref_12pp.tex` l.555 | same "8/8 Invitational" wording → "on all 8 exams in our corpus" | same |
| §1 banner | `sec01.tex` l.380 | "Tested on 100% of Corpus Exams" → "entropy/enthalpy items on all 8 corpus exams" | precision |
| §6 intro | `sec06.tex` l.10 | "Gas-law and kinetic-theory items appear on 100% of surveyed exams" → "Gas-law items appear on nearly every exam in our 8-exam corpus" | E6 has no clear gas-law item; no kinetic-theory evidence for all 8 |
| p38 devicebox | `sec03.tex` | "#1 PET or #5 PP — and #6 PS is banned" → cups may be PET, PP or **PS** (α_L ≈ 70e-6/K, softens near 100 °C); the PS ban (FAQ 10/22/2026) applies to the device | the ban is on device materials, not the ES cup |
| Table 14.x resin codes | `sec14.tex` | "#6 PS BANNED! DISQUALIFIED" → "BANNED in device … The ES's cup may itself be #6 PS; that is allowed." | same |
| Invar α | `sec03.tex` (Ex 03.4, Fig 3.2 label), `appA.tex`, `quickref_12pp.tex` | 0.9e-6 → **1.2e-6 /K** (matches QS-02). Ex 03.4 recomputed: R 0.2762 → **0.2809 m (28.1 cm)**; δ_tip 1.16 → **1.14 cm**; exact R 0.27652 → **0.28118 m**, δ 1.157 → **1.138 cm** | one value everywhere (prompt) |

### 2a. Recompute sweep (all other examples and problems)
| Example | Old → New | Reason |
|---|---|---|
| Ex 01.9 [1.5] | loss increase 6.93× (+593%) → **6.92× (+592%)** | 1.3848/0.200 = 6.924 (its own verified line said 6.924) |
| Ex 04.4 | verified line: 46.1623 g / 104 160.6 J / 107 904.6 J → **46.1626 g / 104 161.4 J / 107 905.4 J** | rounding |
| Ex 04.5 | overestimate without drift correction 27.4 J/(kg·K) (1.16%) → **27.9 (1.19%)** | arithmetic |
| Ex 04.7 | C_tot 10.390 → **10.389** kJ/K; q₂ 40 945.0 → **40 944.9** J, q_V 40 897.0 → **40 896.9** J; ΔnRT −11.15 → **−11.16** kJ/mol (answer −5465.5 unchanged) | double rounding / truncation |
| Ex 04.10 | Q_gly +16 518.4 → **+16 518.5** J; Q_Ag −6699.9 → **−6700.0** J | rounding (ΣQ = 0 now exact) |
| Ex 05.6 | verified line 30.106 g → **30.105 g** | rounding |
| Ex 06.4 | v_mp 422.09 → **422.00**, v_avg 476.28 → **476.17**, v_rms 516.95 → **516.84** m/s; Z_coll 7.087e9 → **7.085e9** s⁻¹ | used M = 0.0280 instead of the stated 0.0280134 |
| Ex 06.6 | RT/(V_m−b) 6.3656e6 → **6.3658e6** Pa; P_vdW 49.024 → **49.026** bar; Z 0.8423 → **0.8424** | arithmetic |
| Ex 07.3 | w_min 3498.0 → **3498.1** J; pre-cooled staircase 4499.6 → **4499.7** J | rounding |
| Ex 07.7 | T_inv(N₂) 851.6 → **851.5** K | arithmetic |
| Ex 07.9 | ln(390/298) 0.269055 → **0.269053**; ratio 4.0832 → **4.0833**; Q_H 4494.6 → **4495.3**, W_net 1060.3 → **1060.4**, Q_C 3434.3 → **3434.8** J (and verified line) | R slip (8.31325 implied) |
| Ex 08.3 | ln Ω(100,50) 66.7839 → **66.7838** | arithmetic |
| Ex 08.4 | s_f(120 °C) 1.5355 → **1.5356**, s_g 7.1379 → **7.1380** kJ/(kg·K) | rounding (4.217 ln(393.15/273.16) = 1.535551) |
| Ex 08.5 | exponent e^11.5448 → **e^11.5447** | rounding |
| Ex 08.7 [8.8] | nR 46.1523 → **46.1522** | rounding |
| Ex 08.8 [8.6] | exponent e^5.9720 → **e^5.9719** | rounding |
| Ex 08.9 | Debye A = 12π⁴R/(5Θ³) 1.751e-7 → **1.753e-7**; C_V 1.751e-4 → **1.753e-4**; S 5.837e-5 → **5.843e-5**; ΔU 4.378e-4 → **4.382e-4** | arithmetic |
| Ex 09.2 | Q_H 6915.7 → **6915.8**; Q_C and W_net 3457.8 → **3457.9** J (and verified line) | rounding |
| Ex 09.5 | w_t,s 121.53 → **121.54**; η_I 5.378% → **5.379%**; w_net,a 97.09 → **97.10**; ṁ 0.5150 → **0.5149** kg/s | 2718.6 − 2597.058 = 121.542 |
| Ex 09.7 | Dual numerator 1.8962 → **1.8964**, bracket 1.0774 → **1.0775**; Diesel bracket 1.1066 → **1.1083**, η_Diesel 61.49% → **61.44%** | arithmetic |
| Ex 09.8 | r_p = 25: 25^(2/7) 2.5094 → **2.5085**; η_simple 60.15 → **60.14%**; η_regen 49.81 → **49.83%**; T₂ 752.8 → **752.5 K**; T₄ 597.8 → **598.0 K** | arithmetic |
| Ex 09.9 | Q₁→₂ 21 413.2 → **21 410.6**; Q₃→₄ and W_net 10 706.6 → **10 705.3** J | arithmetic |
| Ex 10.10 | ratio used 14.4115 (not the stated 14.41 K) → uses **14.41**; verified line 167.00 → **167.02** (answer 167.0 unchanged); `check_sec10_13.py` updated to the stated value | inconsistent input |
| P10.5 | T_mid 541.5 °C → **560.1 °C** | the text's own quadratic solves to 560.15 |
| Ex 11.2 | h_rad,foil 0.1312 → **0.1313** | rounding |
| Ex 11.4 | TG lost by swirling 4.19 → **4.20 °C** | 17.102 − 12.906 |
| Ex 11.6 | e^(−NTU) 0.28609 → **0.28611**; T_out 62.835 → **62.833**; ΔT_out 17.165 → **17.167** (answers unchanged) | intermediate values |
| Ex 11.7 | Ra_D 1.0695e7 → **1.0689e7**; Ra_L* 1.6711e5 → **1.6702e5**; numerator 11.332 → **11.321**; denominator 1.3045 → **1.3033** (Nu, h̄ unchanged: the two errors cancelled) | arithmetic |
| P11.6 | counterflow ΔT_lm 37.00 → **36.99** K | rounding (36.9946) |
| P11.7 | Pr^(2/3) 0.79750 → **0.79736**; St 0.002633 → **0.002634** (h̄ 37.42 unchanged) | arithmetic |
| P11.8 | Nu 6.1288 → **6.1287**; base 10.0632 → **10.0631**; Re_D 141.7 → **141.8** (u∞ 2.09 m/s unchanged) | rounding |
| Ex 12.4 | white paint T_p 312.01 K / 38.86 °C → **312.59 K / 39.44 °C**; "26.1 °C cooler" → **25.5 °C** | root of the stated energy balance |
| Ex 12.7 | Taylor remainder 0.003254 → **0.003257** | arithmetic |
| Table 12.x (Planck fractions) | F(1680) 0.02540 → **0.02661**; median row 4107.6 → **4107.2** µm·K; F(6480) 0.77635 → **0.77492** | the three problem-specific rows were wrong; the 21 standard rows agree with the series to ±5e-5 |
| P12.3 | flipped-shield T_s 310.7 → **310.6 K** | arithmetic |
| P12.4 | sin θ_s 0.3027 → **0.3026** | rounding |
| P12.5 | F(1680) 2.54% → **2.66%**; band fraction 0.53032 (53.03%) → **0.52889 (52.89%)**; λ_med 1.7115 → **1.7113 µm**; ratio 1.4175 → **1.4174** | follows the table fix |
| P12.6 | h_rad 7.688 → **7.692**; Q̇_tot,1 364.1 → **364.2 W** | arithmetic |

| Ex 13.1 | V = 1.0179e-7 **m²** → **m³** | units error |
| Ex 13.2 | 1 − e^(−600/903) 0.48543 → **0.48544** | arithmetic (same constant fixed in §16) |
| Ex 13.8 | matrix a₂₁ 0.0004940 → **0.0004939** | arithmetic |
| P13.11 | break-even C₁ 472.5 → **472.55**, ΔC 52.0 → **52.05** J/K (m_max 57.8 g unchanged); foil sleeve ΔT 19.26 → **19.32 °C**, net gain 1.51 → **1.57 °C** | arithmetic |
| Ex 14.1 | σT⁴ terms 715.49/430.35 → **715.43/430.31**, ΔM 285.14 → **285.12** W/m² (and the three q″ lines); verified line 4σT_m³ 7.122 → **7.099** W/(m²·K), 284.9 → **284.0** W/m², "0.09% agreement" → **0.40% below exact** | arithmetic |
| Ex 14.3 | R_F 0.01955 (1.96%) → **0.01954 (1.95%)**, (1−R_F) 0.98045 → **0.98046**; 80.32 → **80.31%**, 93.15 → **93.14%**, 63.40 → **63.39%** | arithmetic |
| Ex 14.4 | τ_NIR(BoPET) 0.8714 → **0.8713** | arithmetic |
| Ex 14.5 | Ra 602.7 → **602.8**; h_rad 0.1360 → **0.1361**; cork extra leak 43.5% → **43.6%** | arithmetic |
| Ex 15.1 | F_cup(40) 0.01473 → **0.01474**; F_ap(40) 0.66471 → **0.66465**; gain 45.13× → **45.08×**; X(65) 76.364 → **76.369**; F_cup(65) 0.004568 → **0.004567**; F_ap(65) 0.15162 → **0.15160** | arithmetic |
| Ex 12.2 | F_cup 0.01473 → **0.01474** (answer 45.1× unchanged; prompt listed 12.2 as verified — digit fixed for consistency with §15) | rounding (0.0147438) |
| Ex 15.1b [15.2] | X 2.03945 → **2.03949**; F_ap→cup 0.03344 → **0.03334**; F_ap→s 0.96656 → **0.96666**; f_dir 0.07190 → **0.07168**; Q̇_dir 2.459 → **2.451**, Q̇_wall 27.894 → **27.901**, total 30.353 → **30.352** W; conservation line closes at 34.200 W | digit error in F |
| Ex 15.4 [15.6] | verified line 2128.1 → **2128.0** J | arithmetic |
| Ex 15.5 [15.7] | verified line "ideal-gas ρ_v,sat = 51.19 g/m³ from NIST" → ideal gas **51.09** g/m³, NIST **51.24** g/m³ | the two sources were conflated |
| Ex 15.6b [15.9] | problem asked to verify z_w = 3.801 cm, solution used 3.873 cm, verified line 3.8732 — none holds 100.0 mL → "Find z_w": **3.876 cm**, r 3.0760 → **3.0764** cm, dry wall 6.13 → **6.12** cm, clearance 3.63 → **3.62** cm; `check_sec14_16.py` expected values updated (3.8757 / 3.6243) and tolerance tightened 1e-3 → 1e-4 | inconsistent; 3.8732 cm gives 99.93 mL |
| Ex 16.2 | denominator 0.48543 → **0.48544**; M_t(13) 1.19160 → **1.19156** (T_pred 54.47 unchanged); verified line 33.007 → **33.006**, 54.470 → **54.469** | arithmetic |
| Eq. 16.x (M_t) | 0.48543 → **0.48544** | arithmetic |
| Ex 16.2b [16.3] | TG(900 s) 36.10 → **36.09 °C**; verified e^(−600/903.2) 0.51461 → **0.51463** | arithmetic |
| Ex 16.3 [16.4] | k_start/k_room at 14 min 0.395/0.605 → **0.394/0.606**; verified line 0.6052 → **0.6055**, 40.204 → **40.208 °C** (answer 40.2 unchanged) | table weights were mis-rounded (see Phase 2b DOE table) |
| Ex 16.7 [16.8] | A₀ 5973.5 → **5968.1**; Slot B 17.52 → **17.53 °C**; "within 0.02 °C" → **0.03**; "+1.52 °C" → **+1.53** | arithmetic |
| Ex 17.2 | ln term −1.826699e-4 → **−1.826577e-4**; 1/T 3.1713465e-3 → **3.1713587e-3**; T 315.3235 → **315.3223 K** (42.17 °C unchanged) | arithmetic |
| Ex 17.5 | √2·u(T) 0.3366 → **0.3367**; c_x 0.50533 → **0.50534** | arithmetic |
| Ex 18.3 | S_tY −4.63274 → **−4.63268**; S_YY 0.3065976 → **0.3065967**; m −0.0661820 → **−0.0661811**; b −0.000010 → **−0.000014**; R² shown as 21.46228/21.46183 (a ratio > 1) → **21.461724/21.461766**; residual 4.89e-7 → **5.95e-7**; s_Y\|t 3.50e-4 → **3.86e-4**; u(m) 4.18e-5 → **4.61e-5** (u(τ) 0.0105 min unchanged); s_all 1.00003 → **0.99983** (G unchanged) | arithmetic |
| Ex 18.4 | Y₁ = ln(7.384) 2.00000 → **1.99932**; Ȳ 3.367805 → **3.367633**; S_XX 0.141913 → **0.146673**; S_XY −0.724014 → **−0.748562**; S_YY 3.693954 → **3.820578**; m −5.10182 → **−5.10360**; b 18.2990 → **18.3040**; R² 0.999954 → **0.999942**; ΔH_vap 42.42 → **42.43 kJ/mol**; X_b 2.68153 → **2.68158** (T_b 99.77 °C unchanged); two-point check 42.43 → **42.42** (the two had been swapped); `check_sec17_20.py` expected 42.4192 → 42.4337, tolerance 1e-3 → 1e-4 | wrong logarithm in the data table |
| Ex 19.1 | V_f 0.61555 → **0.61556** m³ (W 62.34 kJ unchanged) | rounding |
| Ex 19.4 | P_f 405 817 Pa / 405.82 kPa → **405 825 Pa / 405.83 kPa** (and verified line) | arithmetic |
| Ex 19.5 | verified line 117.631 → **117.634 cm** (absolute-volume check; 117.63 cm answer unchanged) | arithmetic |
| Ex 19.7 | prefactor 3.74232e11 → **3.74237e11**; 1/T_i³ 1.93855e-8 → **1.93864e-8**; Δt 9793.0 s / 163.22 min → **9792.9 s / 163.21 min** | arithmetic |
| Ex 20.2 | σT₁⁴ 1453.85 → **1453.79** W; back-radiation 460.28 → **460.22** W (net 993.57 W unchanged) | arithmetic |
| Ex 20.7 | ln-term 0.33648 → **0.33644**; R′ 0.76663 → **0.76659** m·K/W (−38.94% unchanged) | arithmetic |

Checked and correct (no change) in §8–§12: Ex 08.2, 08.6 [8.7]; 09.6; 10.2, 10.3, 10.5–10.8; P10.1–P10.4, P10.6–P10.10; 11.5; P11.1–P11.5; 12.6; P12.1, P12.2, P12.7, P12.8. Left as is: Ex 08.4 u_g = 2531.41 and m_sweat = 2.0813 kg (the displayed arithmetic on rounded intermediates gives these; unrounded gives 2531.40 / 2.0812).

Checked and correct (no change): Ex 00.2; 01.2, 01.4, 01.7, 01.11, 01.12; 02.3, 02.4; 03.3, 03.5; 04.6, 04.8, 04.9, 04.11; 05.1, 05.7, 05.8; 06.1, 06.7; 07.2, 07.5, 07.8, 07.10–07.14.

Checked and correct (no change) in §13–§23: Ex 13.4, 13.5, 13.7, 13.9; P13.1–P13.10, P13.12; 15.2 [15.3], 15.3 [15.4], 15.3b [15.5], 15.6 [15.8]; 16.1, 16.4 [16.5], 16.5 [16.6], 16.6 [16.7]; 17.1, 17.3, 17.4, 17.6; 18.1, 18.2, 18.5; 19.2, 19.3, 19.6, 19.8; 20.3–20.6; 21.1, 21.2; 22.1; 23.1–23.3. Left as is (displayed arithmetic on rounded intermediates, exact differs by 1 in the last digit): Ex 13.2(c) 10.20 °C (exact 10.21), Ex 13.8 "losing 11.94 °C" (exact 11.95), Ex 16.4 "+0.38 °C" (exact 0.385).

**Sweep coverage:** all 163 worked examples and all 38 problem-bank items recomputed. Ex 01.3 had no check anywhere; one was added. Total checks: 274 → **1020** (all pass).

### 2b. Figure errors (each page re-rendered at ≥130 dpi and inspected after the fix)
| Figure | File | Old → New | Reason |
|---|---|---|---|
| Fig 1.1 (QS-06) | `sec01.tex` | P–V and T–S panels overprinted → two named pgfplots axes side by side, arrowed axes, caption "Arrowheads mark one direction of travel along each path"; trap box moved below | unusable overlap |
| Fig 16.2 nomogram + §16 tables | `sec16.tex` | 11–15 min multipliers 1.076/1.143/1.274/1.334 → **M_t = 1.068/1.132/1.192/1.247/1.300** (τ_eff = 903 s); every plotted coordinate and every DOE/matrix/1-cm/ambient-offset cell regenerated from the 10-min base (e.g. 15 min @ 40 cm 33.1 → **32.2**); legend M_t values; 100 W cells follow the stated 0.800 rule (50 cm 17.1 → **17.0**, 55 cm 14.1 → **14.0**); k_start/k_room 0.482/0.450/0.395 → **0.481/0.451/0.394**; Ex 16.3 T_pred 40.2 → **40.1 °C**, Ex 16.6 TG 12.40 → **12.32 °C** | wrong multipliers; new `verify/device_model.py` is the single source and `check_device_model.py` compares all 311 printed cells with it |
| Fig 14.1 | `sec14.tex` | α=ε diagonal took the first legend entry → `forget plot`; white paint gets its entry; legend moved below the axes; point labels un-piled with leader lines | every marker was mislabeled |
| Fig 18.2 | `sec18.tex` | same shifted-legend bug (zero baseline) → `forget plot`; legend replaced by direct curve labels | flat curve was labeled "Pattern B" etc. |
| Fig 5.2 | `sec05.tex` | critical isotherm passed above C → drawn through C with a horizontal inflection; labels moved off lines | physics |
| Fig 5.3 | `sec05.tex` | 250 °C tie line ended at 42.5 wt% → ends on the drawn solidus (9.8 wt%) and liquidus (33.2 wt%); "Eutectic E" no longer covers β+L; merged "97.8100" ticks → on-plot labels | physics + overlap |
| Fig 9.3a Brayton | `sec09.tex` | expansion stopped at v = 1.45 m³/kg (≈183 kPa) → runs to **v₄ = 2.235 m³/kg** where P = 100 kPa; 4→1 isobar 2.235 → 0.86; xmax 2.45; labels un-clipped and moved off markers | cycle did not close |
| Fig 9.4a Rankine T–s | `sec09.tex` | state 1 inside the dome, boiler line flat left of the liquid line → state 1 on the saturated-liquid line; heating follows the liquid line to the boiler T, then crosses the dome horizontally | physics |
| Fig 10.2 | `sec10.tex` | y-unit "K/(W m)" → **"R for ℓ = 1 m [K/W]"**; legend moved below so the R_tot minimum is visible | wrong unit; hidden minimum |
| Fig 12.2 | `sec12.tex` | one two-panel figure → **Fig 12.2** (shield network) and **Fig 12.3** (lamp view factor, new label `fig:12:lamp-viewfactor`); panel (b) z_ap 29.5 cm with F = 0.665 → **z_ap = 30.0 cm** (d_ap = h − 30.0), matching Ex 12.2 (F = 0.665, 45.1×) | overlap; label/value mismatch |
| Ex 15.1, Table 15.4 | `sec15.tex` | "43.65× at z_ap = 29.5 cm" and "F = 0.64355 / 0.14807" asides (r = 15.0 cm at 29.5 cm, a hybrid of the 30.0 cm top plane and the 29.5 cm/14.5 cm rim) → removed; one view-factor plane, **z_ap = 30.0 cm, r = 15.0 cm**; Table 15.4 d_ap column 10.5…35.5 → **10.0…35.0** and header z_ap 29.5 → **30.0** (its F column was already the 30.0 cm values); formula-card line "29.5 cm … 10.5 cm" → "30.0 cm … 10.0 cm" | reconcile §15.2 with Ex 12.2; new checks `TAB-15.4-FAP-*`, `TAB-15.4-FCUP-*` |
| Fig 13.2 | `sec13.tex` | straight sloped profiles starting at an "insulated base" → one-term transient profiles Θ = 1 − cos(λ₁x/L) for Bi = 0.05, 0.71, 20 (λ₁ = 0.2218, 0.7548, 1.4961), flat at x = 0; caption explains T_∞ for the top-heated cup | insulated base needs zero slope |
| Fig 17.2 + table | `sec17.tex` | "Measured Stratification Map" (T_top 45.2, T_bot ≈ 38, swirled 41.6 °C) → **"Modeled Profile T(z)"** generated from the §15 reference-run model: ES reading **49.7 °C** at 6 mm, base **30.8 °C** (−18.9), swirled **39.8 °C** (−9.9); radial columns dropped (wall plume ≈ −1.4 °C kept as a note); banner "Modeled for the reference collector. Replace with our measured runs."; "How to read this" line; §17.4 text numbers follow (up to ≈19 °C bias; z_opt ≈ 3–6 mm; immerse ≈ 6–8 mm); labels un-piled (IR cone removed — the table has the skin row) | contradicted §15 for the same run; new `check_reference_run.py` |
| Ex 17.4 | `sec17.tex` | C_top 185.0 J/K, T_w0 46.50 °C → **215.0 J/K, 49.70 °C** (house values); T_eq 46.439 → **49.641 °C**, drain −0.061 → **−0.059**, 2τ reading 43.06 → **45.83 °C** (loss 3.38 → **3.81**), 5τ 46.27 → **49.45 °C** (within 0.17 → **0.19**) | single device model |
| Table 15.6 (8-layer) + Fig 15.6 | `sec15.tex` | 8-layer table removed: its own rows give a 10-min bulk of **40.1 °C** (printed 39.8) and 5-min **31.5 °C** (printed 31.1), and its 15-min column (≈54.8 °C at the probe) disagrees with the §16 lookup (58.0 °C); Fig 15.6 keeps only the 10-min glazed and open-cup curves (5- and 15-min curves removed for the same conflict); probe-zone shading 3–12 → 4–12 mm to match its label; legend moved below; swirl label moved off the open-cup curve; caption says "Modeled … same model as Ex 15.4 and Fig 17.2" | internal arithmetic + single device model |
| κ_strat text and card | `sec15.tex` | "≈1.58 at 10 min, 1.48 at 15 min", "1.45× to 1.65×" → **1.556 at 10 min (Ex 15.4)** | match the single model |
| Fig 6.3a | `sec06.tex` | smooth Z(P) curves at 300 K (CO₂ subcritical, T_c = 304 K, would liquefy near 67 bar) → **Peng–Robinson Z(P) at 320 K** for H₂, N₂, CH₄, CO₂ (CO₂ dips to ≈0.34 near 120 bar); caption explains the choice; Ideal/attraction/Maxwell labels un-piled; panel gap widened | physics |
| Fig 15.3 | `sec15.tex` | tier shading implied State = 50–55 cm, Nationals = 55–65 cm → **bracket bars** Regional 40–50 (5 cm steps), State 40–55, Nationals 40–65 (1 cm steps); legend moved below; caption adds why the tuned curves peak at 45 cm (reflector upper focus h_design = 45.0 cm, Ex 15.3) and "How to read this" | wrong tier ranges; unexplained peak |
| Table 3.1, Fig 3.1, p33 list, §23, App B | `sec03.tex`, `sec23.tex`, `appB.tex` | Rømer printed as "°R" (`\o` dropped in math mode, 13 warnings) → **°Rø** via `\text{R\o}`; Rankine keeps °R | two scales shared a symbol |
| Fig 3.2 vs QS-02 | `sec03.tex`, `sec01.tex`, `quickref_12pp.tex`, `appA.tex` | Invar α 0.9×10⁻⁶ → **1.2×10⁻⁶ /K** everywhere (Fig 3.2 label, Ex 03.4, App A, QuickRef) | consistency |

Checks after Phase 2: **1374**, all pass (`verify_all.py`).
