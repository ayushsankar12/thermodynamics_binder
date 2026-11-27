# Master Prompt: Overhaul the 2027 Div C Thermodynamics Binder

You are revising a Science Olympiad 2027 Division C Thermodynamics competition binder so that it is **correct, fast to use under time pressure, consistent, and lean**. Work through every phase below in order. Do not skip items. When an item needs a human decision or a source you cannot access, do not guess: add it to `REVIEW_NEEDED.md` and move on.

---

## 0. Context you must keep in mind

**Who uses it and how**
- Two partners use it at once during a 50-minute event: a timed written test (Part I) plus a pre-built heat-lamp collector device (Part II) whose final water temperature they must predict.
- It is printed, possibly in **grayscale**, and used as an open binder. Pages may be removed during the event (per the binder's reading of Rule 2.c; confirm in the manual).
- The pass bar for every common question: **under 30 seconds, one place, no flipping between sections**: formula, symbols with units, when it applies, and a worked example on the same page or spread.
- A wrong answer costs more than a missing one. Accuracy beats completeness, and completeness beats polish.

**Repo facts** (`ayushsankar12/thermodynamics_binder`, local clone at `/Users/ashrithrepaka/thermodynamics_binder`)
- LaTeX book class. Driver: `src/main.tex`. Content: `src/sec00.tex`–`src/sec23.tex`, `src/appA.tex`–`src/appH.tex`, `src/frontmatter.tex`. Style: `src/thermobinder.sty`, identical to `build/thermobinder.sty`; keep them identical or make one canonical.
- Companion PDFs: `src/quickref_12pp.tex` (12-page QuickRef) and `src/device_handbook.tex` (46-page Device Handbook, which reuses §14–§16 figures).
- Build: `python build/build.py --target all`. The README assumes MiKTeX on Windows, but this machine is macOS. Check for `latexmk`/`pdflatex`/`makeindex` first. If TeX is missing, stop and ask the user before installing anything.
- QA: `python qa/pdfcheck.py`, `python verify/verify_all.py` (274 numerical checks), `python build/export_markdown.py` (regenerates the `markdown/` mirror).
- Output: `output/Thermodynamics_DivC_Binder.pdf` (264 pp now), `..._GRAYSCALE_PROOF.pdf`, `..._QuickRef_12pp.pdf`, `..._Device_Handbook.pdf`.
- Box environments in the .sty: `formulacard`, `workedexample`, `trapbox`, `shortcut`, `devicebox`, `rulebox`, `tierbox`, `derivation`, `quicksheet`, `problem`/`solution`. Font macros: `\tabfont` (= `\footnotesize`), `\densefont` (9.5 pt), `\tiny` redefined to 7.0 pt, `\src`/`\flag` use `\scriptsize`.

**Git rules**
- Create a branch first: `git checkout -b binder-overhaul`. Never commit to `main`. Do not push, open PRs, comment or open issues unless the user asks.
- Commit after each phase with a clear message. Keep a running `CHANGELOG_OVERHAUL.md` listing every change with file, old → new, and reason.

**Hard rules**
- Never invent rules text, clarification text, test statistics or device data. The official 2027 rules are only in the purchased Rules Manual, not on soinc.org.
- Never fabricate calibration data. Leave blank tables for the team to fill in.
- Physics sign convention stays ΔU = Q − W_by (chemistry ΔU = q + w_on shown only as a translation).
- SI units throughout; every answer has units and sensible significant figures.
- After changing any number, recompute it and add or update a check in `verify/`. `verify/verify_all.py` must pass at the end.
- Don't add new deep content. The goal is a smaller, cleaner binder. The only new content allowed is what this prompt lists.

---

## Phase 1: Baseline

1. Build all four PDFs; record page counts, build warnings, overfull boxes, and `pdfcheck.py` and `verify_all.py` results in `CHANGELOG_OVERHAUL.md`.
2. Write `qa/audit_metrics.py` (use PyMuPDF; install into a venv if missing). For each page it reports word count, smallest font size, share of characters under 8 pt, and pages under 250 words. Across the PDF it also reports any literal `**`, empty section headings (a heading followed directly by another heading or by the page end), and figure captions without a "How to read" line. Run it now and save the baseline. Current baseline: median 694.5 words/page; 27% of all characters under 7.5 pt; 37 pages mostly under 8 pt; minimum font 5.2 pt.

---

## Phase 2: Accuracy (do first; a wrong page is worse than a missing one)

### 2a. Worked-example errors (recompute, fix text and verify checks)
| Example (page) | Fix |
|---|---|
| Ex 11.1 (§11, p119) | Churchill–Chu intermediates: 0.670·Ra^¼ = **51.15** (not 50.888), denominator [1+(0.492/0.711)^(9/16)]^(4/9) = **1.3027** (not 1.2768). Nu = **39.94**, h̄ = **3.53 W/(m²·K)**, Q̇ = **4.45 W** (remove the "4.51 W" bold answer). Doubled ΔT: Q̇ ≈ **10.5 W** (ratio 2.37 with the 0.68 term). |
| Ex 12.3 (§12, p129) | σ(T₁⁴−T₂⁴) = **150.64 W/m²**; q″_card = **128.3**; q″_foil = **3.074**; q″_2 shields = **1.025 W/m²**; single-shield **T_s = 307.30 K = 34.15 °C** (not 307.08 K / 33.93 °C). |
| Ex 12.1 (p128) | M_fil = **6.585×10⁵ W/m²**; L = **2.096×10⁵ W/(m²·sr)**; A = **1.898 cm²**. |
| Ex 09.3 (p96) | 9.5^0.4 = **2.46087**; T₂ = **738.26 K**; η = 0.59364. |
| Ex 09.4 (p98) | r_p,opt = (1470/300)^1.75 = **16.14**; W_net = **3457.9 J**; Q₁→₂ = **5186.8 J**. |
| Ex 07.6 (p75) | W₂→₃ = Q₂→₃ = **5186.8 J** (R = 8.314463, 900 K, ln 2). Re-check that leg's row and totals. |
| Ex 05.5 (p57) | m_a = **1135.1 kg**; m_cond = **6.125 kg**. |
| Ex 04.1 (p45) | Don't end with "Copper … or Zinc!". State that Dulong–Petit (M ≈ 65 g/mol) cannot separate Cu from Zn, then decide by c: 383 J/(kg·K) → **copper** (385) over zinc (388), or check density. |
| Ex 03.2 (p36) | Sig figs: the 0.010 cm gap has 2 s.f. → report **≈1.3×10² °C** and **≈3.1×10² °C** (show the full value in working). |
| Ex 13.2 / §16 (pp135, 175) | C_eff = 380 J/K is less than the 418 J/K of 100 mL of water alone. Either define it explicitly as an effective **top-layer** capacitance (and say why) or correct the model. Put the decision in `REVIEW_NEEDED.md` if unsure. |
| §20 intro & Ex 20.1 (pp212–213) | Delete unsourced statistics ("over 70% of lost points…", "What 65% of contestants write"), or cite a real source. Also check §8 tierbox claims like "8/8 exams tested ΔS, ΔH, ΔG" against `research/phase2_exam_corpus.md`. |
| p38 devicebox | Don't imply the ES cup can't be #6 PS. The polystyrene ban (FAQ 10/22/2026) applies to **the device**. The cup may be PS, PET or PP; PS softens near 100 °C. |

**Then recompute every remaining worked example and problem-bank item** (163 `workedexample` + 38 `problem`/`solution`). Already verified correct: 00.1, 01.3, 02.1, 02.2, 03.1, 04.2, 04.3, 05.2, 05.3, 05.4, 06.2, 06.3, 06.5, 07.1, 07.4, 08.1, 09.1, 10.1, 10.4, 10.9, 11.3, 12.2, 12.5, 13.3, 13.6, 15.3, 16.1, 16.3, 17.2, 20.1, 21.1, 23.1. Write a check for each one not already in `verify/checks/`. Log every discrepancy, even 4th-digit ones; fix anything that changes a reported answer.

### 2b. Figure errors (verify each by rendering the page after the fix)
| Figure (page, file) | Problem | Fix |
|---|---|---|
| Fig 1.1, QS-06 (p16, `sec01.tex` ~l.318 & ~l.338) | P–V and T–S panels are drawn on top of each other (titles, axis labels and ticks overprint). Unusable. | Replace with the clean QuickRef QR-07 figure (`quickref_12pp.tex`, QuickRef p7), or place the two panels side by side with separate axes. |
| Fig 16.2 nomogram (p177, `sec16.tex` ~l.288–340) | 11/12/14/15-min curves use multipliers 1.076/1.143/1.274/1.334. | Correct M_t = (1−e^(−60t/903))/(1−e^(−600/903)) = **1.068, 1.132, 1.192, 1.247, 1.300** for 11–15 min. Recompute all plotted coordinates from the 10-min base (24.8, 27.7, 21.3, 17.5, 13.6, 10.6 at 40…65 cm). E.g. 15 min @ 40 cm = **32.2** (not 33.1). Fix the legend text. |
| Fig 14.1 (p146, `sec14.tex` ~l.53) | Legend shifted by one: the dashed α=ε diagonal took the first legend entry, so every marker is mislabeled and white paint has no entry. | Add `forget plot` to the diagonal (or reorder); give white paint (red diamonds) an entry; move the legend off the Zone III label. |
| Fig 18.2 (p200, `sec18.tex` ~l.303) | Same shifted-legend bug: the flat curve is labeled "Pattern B", the inverted-U "Pattern C", the step curve unlabeled. | Fix the order; label curves directly on the plot. |
| Fig 5.2 P–v dome (p53, `sec05.tex`) | The dashed T = T_c isotherm passes above the critical point. | Draw it through the critical point with a horizontal inflection there. |
| Fig 5.3 Pb–Sn eutectic (p54, `sec05.tex` ~l.283) | The 250 °C tie line extends past the liquidus (w_L dot ≈ 41 wt%; drawn liquidus is at ≈ 33 wt%). The "Eutectic E" label covers "β + L"; ticks "97.8100" merge. | End the tie line and w_L on the liquidus; move labels; fix ticks. |
| Fig 9.3a Brayton (p97, `sec09.tex` ~l.434–470) | Expansion `308*x^(-1.4)` ends at ≈ 183 kPa at v = 1.45 while state 4 is drawn at 100 kPa; the cycle doesn't close. Labels "1", "4" clipped. | Domain 0.52 → **2.24** m³/kg; 4→1 isobar from 2.24 → 0.86; xmax ≈ 2.4; un-clip labels; fix "2→3: q_H in (P₂)" overlapping state markers. |
| Fig 9.4a Rankine T–s (p98, `sec09.tex` ~l.543) | Boiler line goes flat at s ≈ 2.0, left of the saturated-liquid line at that T; boiling can only start on the dome. | Follow the saturated-liquid line to the boiler T, then cross the dome horizontally. |
| Fig 10.2 critical radius (p107, `sec10.tex` ~l.335) | y-unit "K/(W m)" is wrong; the legend hides the R_tot minimum. | Label it "R_tot for ℓ = 1 m [K/W]" (or R′ [m·K/W]); move the legend outside. |
| Fig 12.2b (p128, `sec12.tex` ~l.250–275) | Labels z_ap = 29.5 cm but prints F = 0.665 (the 30.0 cm value; 29.5 cm gives 0.644). Panels (a) and (b) overlap. | Use z_ap = 30.0 cm to match Ex 12.2; split into two figures. Also reconcile §15.2's "43.65× at 29.5 cm". |
| Fig 13.2 (p136, `sec13.tex` ~l.169) | Straight sloped profiles start at an "insulated base", which needs zero slope. | Curved profiles flat at x = 0; explain what T_∞ means for the top-heated cup. |
| Fig 17.2 + its table (p191, `sec17.tex`) | Table titled "Measured Stratification Map" but values are modeled; contradicts §15 for the same run (T_top 45.2 vs 49.7 °C; T_bot ≈ 38 vs 29.3 °C; swirled 41.6 vs 39.8 °C). | Rename "Modeled"; make one device model the single source for §15/§16/§17 numbers (see Phase 4). |
| Table 3.1, Fig 3.1, QS-01, §23, App B, QuickRef | Rankine and Rømer both use "°R". | °R = Rankine, **°Rø** = Rømer everywhere. |
| Fig 6.3a (p65) | CO₂ at 300 K is subcritical (T_c = 304 K) and condenses near 67 bar; the smooth Z curve hides this. | Use 320 K, or break the curve and label "liquefies". |
| Fig 15.3 (p160) | Shading implies State = 50–55 cm and Nationals = 55–65 cm (actually State 40–55, Nationals 40–65). The 45 cm peak is unexplained. | Bracket bars for tier ranges; one sentence on why the tuned focus peaks at 45 cm. |
| Fig 3.2 vs QS-02 | Invar α 0.9×10⁻⁶ vs 1.2×10⁻⁶ /K. | Use 1.2×10⁻⁶ /K everywhere. |

---

## Phase 3: Rules and compliance

Official FAQs on soinc.org for Thermodynamics Div C (checked 25 Nov 2026; there are **11**, not 9). Cite each by date and topic; drop the binder's invented "#1–#9" numbering.
1. Glass allowed in the device (undated): "Yes, glass is allowed", **but teams using glass should wear Category C goggles when interacting with the device.**
2. Cup-handling tools (undated): tongs, hot pads, heat-resistant gloves and similar safety items are allowed.
3. 10/01/2026: no swirling the water before the temperature reading.
4. 10/21/2026: teams may place something on or around the cup (cling wrap/foil), but no adhesives, tape or fasteners (rubber bands, clips), and don't alter the cup's shape.
5. 10/22/2026: polystyrene (incl. Styrofoam, #6 plastics) is hazardous under the lamp and must not be used.
6. 10/28/2026: a device not impounded incurs one additional construction violation.
7. 10/22/2026: opening a lid to insert the cup counts as "inserting/removing the cup".
8. 10/22/2026: actions inherent to inserting the cup (open/close lid or door, change orientation/position) are not "modifying" the device.
9. 10/06/2026: water must not be swirled, shaken or stirred.
10. 10/06/2026: probe depth is the local ES's call; recommended: top layer near the cup center, probe only as deep as needed.
11. 09/30/2026: the water will not be stirred or swirled before measurement.
No Thermodynamics entries exist on the rules-corrections page.

Tasks:
- Replace "Eye Protection: None" (cover p1, §0 p6, App E pp260–261, App F p262, QuickRef p1) with "None required by the event header; **Category C goggles if your device contains glass** (FAQ)."
- Change "9 clarifications" to "11 official FAQs (checked [date])" on p1, App E, App F, App H, `markdown/README.md`, and anywhere else (`grep -rn "9 clarif\|#9\|Clarification \\\\#"`).
- Add tongs, hot pads and gloves to the event-day checklist, citing the FAQ.
- Put these into `REVIEW_NEEDED.md` for the team to check against their own Rules Manual (pp. C57–C59), and don't change them without confirmation:
  - **TS formula conflict:** QS-13 (p23) uses 30·TG_adj/TG_adj,max (normalized by the highest *penalized* TG); §0.2, §16.1, §23 and App E use 30·M_pen·TG/TG_max. Pick the one Rule 6.e–h and Scoresheet v2.0.0 use, then make all copies match.
  - The 0.7 (construction) / 0.9 (competition) multipliers and how they stack; TG = max(0, T_final − T_start); PE = max(0, 1 − |T_f − T_pred|/T_f) with T in °C; tiebreak order (TS, ES, preselected questions).
  - Bulb heights (Regional 40–50 cm in 5 cm steps; State 40–55; Nationals 40–65 in 1 cm), heating times (Regional 10 min; State/Nat 10–15 min), 3-min device setup, 1-min water setup.
  - The notes rule wording (any form, any size, pages may be removed) and the Class III calculator allowance.

---

## Phase 4: Consistency

**House constants** (one value everywhere; footnote "use the test's value if one is given"):
- L_f = **333.55 J/g** (currently 333.4 in QS-03/Ex 01.3, 333.43 in App A, 334.0 in Ex 08.1, 334 in §21, 333.5 in §10 problem p113)
- L_v (100 °C) = **2256.4 J/g** (2260 in §21, 2256 in §19)
- c_w = **4.184 J/(g·K)**; c_ice = **2.09 J/(g·K)** (2093/2090/2100/2.10 now); c_steam = **2.08 J/(g·K)**
- R = **8.314 J/(mol·K)** in examples; full CODATA digits only in App A.1
- σ = 5.670×10⁻⁸ W/(m²·K⁴); b = 2898 µm·K in examples (full digits in App A.1)

**Single prediction formula** (§16 boxed form). Use it verbatim in §0.4 (p9), §16, §21.2 (p221), §23 C39 and §23.7 (pp229, 235), the QuickRef and the Device Handbook:
`T_pred = T_start + TG_table(h, P, t) + k_room(t)·(T_room − T_start) − ΔT_cool`, all in °C, reported to 0.1 °C. C39 currently drops −ΔT_cool. The Device Handbook's "S₀ + k_start·T_start" and the QuickRef's "−ΔT_drift(T_i − T_room)" must go.

**Single prediction hand-in rule:** "Hand in at heating minute 3; hard deadline before heating ends (Rule 5.II.f)." It now reads t = 7 min (`sec00.tex` l.268), t = 8 min (l.296), "6:00–10:00" (§21.2), "heating minute 3" (§23.7) and "immediately" (Device Handbook).

**Single device model.** All §13/§15/§16/§17 numbers for the reference collector must come from one table (T_top, T_bot, mixed T, gains, view factors, stage angles). Today they conflict:
- stage angles 23.5°/29.7° (Fig 15.1), 23°/30°/15° (Fig 15.2), ≈22°/28°/15° (p160 text)
- gain over a bare cup: 45.1× (Ex 12.2), 43.65× (§15.2), 13.7–28.6× (p160), ≈11× (Fig 15.3)
- TG_100W(50 cm): 17.10 (Ex 16.3) vs 0.8 × 21.3 = 17.04 (calculator program p179)

Label all of it "Reference design (modeled), not our device."

**Notation:**
- Work: W_by (physics) and w_on (chemistry) only; fix capital W_on in `sec02.tex` (figure l.40 and table titles ~l.93–96).
- Exitance: always M_b or M_e, never bare M (bare M = molar mass only). Molarity → c (glossary Π = iMRT).
- Use α_L (expansion) and α_abs (absorptance), plus α (diffusivity) as App C defines. Use τ_opt for transmittance and τ for time constants.
- TG = max(0, T_final − T_start) everywhere (cover p1 and App C p245 lack the max).

**Sheet numbering:** the QuickRef uses QR-01–QR-12 and the binder QS-01–QS-14 for overlapping content (First Law = QR-07 vs QS-06; collector = QR-12 vs QS-13). Make the QuickRef reuse the binder's QS numbers and content, or retire the QuickRef.

**Box and layout house style:**
- `rulebox` only for rules and FAQs. Move the steam-c_p reconciliation (p40, `sec04.tex` ~l.50) into a `formulacard` or `shortcut`.
- Every section uses one skeleton, repeated per subsection: formula card → short explanation → worked example → trap box. Every section has ≥1 shortcut box.
- One example format. Convert §10–§13 `problem`/`solution` items to `workedexample`, or move them out (Phase 5).
- Example meta tag = level · time only ("Warm-up · 30 s", "Standard · 60 s", "Hard · 2 min"). Remove "Tier n", "Basic/Competition/National", and source codes (MIT E3 Q24, Lienhard Ex 2.6, Cornell E1 …) from title bars; put the source in a small line at the end of the example if wanted.
- Every example ends with a boxed **Answer:** line with units and correct sig figs.

**Render bugs:**
- Literal `**` on pp25, 26, 27, 32, 77, 126, 185, 212 (markdown leaking into LaTeX). Grep `\*\*` in `src/` and replace with `\textbf{}`.
- Backtick quotes in the §3.4 heading (p34).
- Doubled running heads ("§10 · §10", "§21 · §21"; check `\binderchapter` short titles).
- §20 intro says "six case studies"; there are 7.
- "Table A.4a/A.4b" printed under §A.2 (p238); renumber.

**Stale page counts:**
- `markdown/README.md` ("248 Pages", "250 pp", per-section targets)
- the cover's "Budget" column (p1)
- `src/main.tex` comments
- `build/architecture-lock.md` ("246–250")

Generate page ranges from the `.aux` at build time and delete hard-coded budgets.

---

## Phase 5: Cut and merge (do this before raising fonts)

Target: about 40 pages removed. Keep content only where it serves the test or the device.
| Remove or merge | Now | Keep in |
|---|---|---|
| 3-page TOC + near-empty p5 | pp2–5 | New one-page tab map (Phase 6) |
| Cover rules wall (735 words) | p1 | Cover = title + tab list; rules move to §0.1 |
| Partner timelines ×4 | p9, p221, pp235–236, Device Handbook | One event-day card in Tab 1 |
| Scoring copies ×6; scoring examples 00.1/16.1/21.1 | p7, pp173–174, p221 | §16.1 + QS-13, one example |
| FAQs on stirring/probe depth restated ×5 | §11.5 p122, §15.5 p163, §17.4 p191, §0, cover | §0.1 with pointers |
| §22 corpus statistics | pp225–228 | Half-page "what tests ask" table in Tab 1 |
| §21.4 MCQ guessing math, §21.5 online/satellite | pp223–224 | Delete |
| §19.4 calculator playbook | p211 | 3 lines in the event-day card |
| §23.1 Top-40, §23.2 constants, §23.4–23.5 flash cards | pp229–233 | Quick sheets; keep §23.6 traps and §23.7 checklist |
| §23.3 scientist matrix (3rd copy) | p231 | QS-14 + §3.4 |
| App C formula index (duplicates App B); error index; device index | pp251–257 | App B; error items → §20 / trap boxes; device items → §15.7 FMEA. Keep the topic index. |
| App H build pipeline; App G → top 10 sources | pp263–264 | Repo README |
| Table 4.1 (dup of App A.3); §5 steam table (dup of App A.2) | p40, §5.3 | App A |
| Problem banks §10.7, §11.6, §12.5, §13.6 | pp112–115, 122–124, 131–133, 140–144 | Keep 3 short problems each; move the rest to a separate `practice/` packet |
| Deep dives: exergy §8.6, Debye/residual entropy §8.7, cascades/dual/Ericsson §9.7–9.8, tank charging §7.7, ellipsoid funnels §15.3, GUM §17.6, Beer–Lambert §14.3 | pp89–92, 99–102, 77, 159–160, 193–194, 148 | ½ page each |
| Trap catalogs ×4 (§20.1–20.3, §23.6, App C error index, per-section trap sections) | pp212–216, 234 | Trap box per section + §20.4 lookup table |
| Example 19.4 (duplicate of 06.7) | §19 | Keep 06.7 |

Keep the 14 detachable quick sheets.

---

## Phase 6: Reorganize and rename

**One-page tab map** (replaces pp2–5), 9 tabs:
| Tab | Topics (plain words) | Sections |
|---|---|---|
| 1 START | This map · "Which page answers my question?" router · 14 quick sheets · event-day card (timeline + checklist + scoring) | §0, §1 |
| 2 TEMPERATURE & UNITS | Units & conversions · sign rules · sig figs · temperature scales · zeroth law · expansion · 8 scientists | §2, §3 |
| 3 HEAT & PHASES | Specific heat · calorimetry & mixing · latent heat · phase diagrams · lever rule · Clausius–Clapeyron · steam quality · humidity · ΔH vs ΔU | §4, §5 |
| 4 GASES | Ideal gas · partial pressure · kinetic theory & speeds · Cv, Cp, γ · real gases | §6 |
| 5 LAWS & ENGINES | First law · P–V work · process table · cycles · entropy · enthalpy & Hess · Gibbs · third law · engines/fridges/heat pumps · named cycles | §7, §8, §9 |
| 6 HEAT TRANSFER | Conduction & R-values · convection · radiation · heating & cooling curves · everyday examples | §10–§13 |
| 7 OUR DEVICE | Zero-score rules · build checklist · allowed/banned materials · OUR calibration table · prediction card · test log | §14–§16, App D, App E, App F |
| 8 LAB, DATA & TRAPS | Thermometers · reading graphs · linear fits · uncertainty · common wrong answers · multi-step problems | §17–§20 |
| 9 TABLES & INDEX | Constants · steam table · property table · find-a-variable list · symbols · glossary · topic index | App A, B, C |

Merge §21 (strategy) into the Tab 1 event-day card. Shrink §22 to a half page in Tab 1; trim §23 as in Phase 5. Move §20's case studies into their home sections as trap examples.

**Plain-language titles** (rename chapters and subsections; keep it short):
- §0 "Start Here: Rules, Scoring & Question Finder"
- §1 "Quick Sheets"
- §2 "Units, Sign Rules & Math"
- §3 "Temperature, Expansion & the 8 Scientists"
- §4 "Specific Heat & Calorimetry"
- §5 "Phase Changes, Phase Diagrams & Steam"
- §6 "Gases"
- §7 "First Law & Processes"
- §8 "Entropy, Enthalpy & Free Energy"
- §9 "Engines, Refrigerators & Cycles"
- §10 "Conduction"
- §11 "Convection"
- §12 "Radiation"
- §13 "Heating & Cooling Over Time"
- §14 "Device Materials"
- §15 "Building Our Collector"
- §16 "Calibration & Prediction"
- §17 "Thermometers & Measurement"
- §18 "Graphs & Data"
- §19 "Multi-Step Problems"
- §20 "Common Wrong Answers"
- App A "Tables", App B "Find a Variable", App C "Symbols, Glossary & Index", App D "Device Logs", App E "Rules Check", App F "Before the Tournament"

Subsections:
- "Paradigm-Shift Mandate" → "2027 Rules Summary"
- "Locked Sign Contract" → "Sign Rules"
- "Polytropic Process Star" → "Polytropic Processes (PVⁿ = const)"
- "Coordinate Transformation Atlas" → "Reading Cycles on P–V, P–T and V–T Graphs"
- "Five-Variable Physical–Empirical Heating-Curve Prediction Model" → "Prediction Formula"
- "Master 36-Condition DOE Matrix, Nomogram & 1-cm National Interpolation" → "Lookup Table & Chart"
- "Zone I…V" → plain descriptions ("all ice", "ice + water at 0 °C", …)
- Remove "Gouy–Stodola", "Paradigm", "Atlas", "Master", "Championship", "Locked", "Ultra-Fast" from titles.

**Formula homes:** each formula lives in full in ONE home section (equation · symbols with units · when it applies · don't use when · worked example), plus a short copy on its quick sheet with a page pointer. Generate both from one macro per formula (e.g. `\EqCarnot`) so they can't drift. App B becomes a "find a variable → page" list with **no equations**. The router (§0.3) lists questions → page only.
| Formula group | Home | Quick sheet |
|---|---|---|
| Temperature scales, ΔT intervals | §3.2 | QS-01 |
| Q = mcΔT, mixing, ice–water–steam rule | §4.3 | QS-03 |
| Clapeyron, lever rule, quality | §5.3–5.5 | QS-04 |
| Ideal gas, speeds, equipartition | §6.2–6.5 | QS-05 |
| First law & process table | §7.1, §7.3 | QS-06 |
| Entropy, ΔG | §8.2, §8.5 | QS-07 |
| η, COP, Otto/Diesel/Brayton/Rankine | §9.1–9.6 | QS-08 |
| Conduction resistances, r_crit | §10.2–10.3 | QS-09 |
| Convection, evaporation | §11.2 | QS-10 |
| Radiation (σT⁴, Wien, shields) | §12.1–12.2 | QS-11 |
| Lumped heating/cooling, 3-point τ | §13.1–13.2 | QS-12 |
| Scoring; T_pred | §16.1; §16.2 | QS-13 |
| Constants | App A.1 | QS-01 |

Steam: one App A table, saturation 0.01–200 °C (ideally to 374 °C) with P, v_f, v_g, h_f, h_fg, h_g, s_f, s_g, plus a short superheated block (0.1, 1, 3 MPa). Use IAPWS-95 / NIST values and cite them. Delete the §5 copy. (The Cornell 2026 test had a 66-point steam FRQ.) Also add a one-page "property lookup" table (c, k, ε, ρ, α_L for the ~20 most-tested materials) and an α_L table in §3.3.

---

## Phase 7: Speed — examples, warm-ups, text

**Move examples next to their concept** (§6–§9 and §14–§17 already do this):
- §2: 02.1→§2.1; 02.3→§2.3; 02.2, 02.4→§2.5
- §3: 03.1→§3.2; 03.2–03.4→§3.3; 03.5→§3.4
- §4: 04.11→§4.1; 04.1→§4.2/4.3; 04.2, 04.3, 04.4, 04.9, 04.10→§4.3; 04.5, 04.8→§4.4; 04.6, 04.7→§4.5
- §5: 05.1, 05.7→§5.2; 05.2, 05.8→§5.3; 05.3→§5.4; 05.4–05.6→§5.5
- §10: 10.6, 10.7→§10.1; 10.1, 10.2, 10.5, 10.8→§10.2; 10.3, 10.4→§10.3; 10.9, 10.10→§10.4
- §11: 11.1, 11.5, 11.6, 11.7→§11.2; 11.2, 11.3→§11.3; 11.4→§11.5
- §12: 12.1, 12.4, 12.5→§12.1; 12.2, 12.3, 12.6, 12.7→§12.2
- §13: 13.1→§13.1; 13.2, 13.3→§13.2; 13.4–13.6→§13.3; 13.7–13.9→§13.5
- §20 case studies → home sections (20.1→§4.3; 20.2→§9.2/§12.1; 20.4→§7.2; 20.5→§4.5/§8.2; 20.6→§9.2; 20.7→§10.3)

Cap each subsection at one spread.

**Add warm-ups** (1–2 steps, placed before the long examples; answers verified):
| Where | Given → Answer | Teaches |
|---|---|---|
| §2.3 | 5.00 L·atm → 506.6 J | 1 L·atm = 101.325 J |
| §2.3 | 2.50 kcal → 10.46 kJ | cal_th = 4.184 J |
| §2.3/§6.1 | 150 kPa gauge → 251.3 kPa abs | add P_atm |
| §3.2 | 98.6 °F → 37.0 °C, 310.15 K | point conversion |
| §3.2 | rise of 18 °F → 10 K | intervals take no offset |
| §3.3 | 1.000 m steel, α = 12×10⁻⁶/K, ΔT = 50 K → 0.60 mm | ΔL = αL₀ΔT |
| §4.1 | 250 g water, 20→80 °C → 62.8 kJ | Q = mcΔT |
| §4.3 | melt 100 g ice at 0 °C → 33.4 kJ | latent heat |
| §6.2 | 101.3 kPa, 24.0 L, 20 °C → n = 0.998 mol | Kelvin + SI |
| §6.2 | 2.00 L, 300 K, 1.00 atm → 400 K, 2.00 atm: V = 1.33 L | combined gas law |
| §6.4 | v_rms N₂ at 300 K → 517 m/s | M in kg/mol |
| §7.3 | 1.00 mol, 300 K, V doubles isothermally → W_by = 1.73 kJ | nRT ln(V₂/V₁) |
| §7.3 | diatomic, 300 K, V halved adiabatically → 396 K | TV^(γ−1) = const |
| §8.2 | 1.00 kg ice melts at 0 °C → ΔS = 1221 J/K | ΔS = Q/T |
| §8.2 | 2.00 kg water 20→80 °C → ΔS = 1558 J/K | mc ln(T₂/T₁) |
| §9.2 | Carnot 600 K/300 K → η = 0.500 | Kelvin only |
| §9.1 | fridge 2 °C in 27 °C room → COP_R = 11.0, COP_HP = 12.0 | COP_HP = COP_R + 1 |
| §11.2 | h = 10, A = 0.050 m², ΔT = 20 K → 10 W | Q = hAΔT |
| §11.2 | Nu = 40, k = 0.026, L = 0.30 m → h = 3.47 W/(m²·K) | h = Nu·k/L |
| §12.1 | blackbody 300 K → 459 W/m² | σT⁴ |
| §12.1 | Sun 5778 K → λ_max = 0.502 µm | Wien |
| §12.2 | ε = 0.90, A = 1.5 m², 310 K body in 295 K room → 127 W | T₁⁴ − T₂⁴ |
| §13.1 | τ = 600 s, 60→30 °C in 20 °C room → 832 s | t = τ ln(ΔT₀/ΔT) |

**Retitle jargon examples by skill:**
- 06.1 → "Gauge vs absolute pressure in a steam boiler"
- 06.4 → "Average vs rms speed; mean free path"
- 06.7 → "Two gases split by a sliding piston: final T and P"
- 07.3 → "Cheapest way to compress a gas"
- 07.4 → "Find γ from a measured adiabatic temperature rise"
- 07.9 → "Read a cycle drawn on P–T axes"
- 08.2 → "Entropy made when two gases equalize"
- 08.4 → "Build a steam-table entry; ΔH_vap at body temperature"
- 08.6 → "Useful work lost in a steam plant"
- 09.5 → "Steam power plant efficiency from steam tables"
- 09.7 → "Efficiency of a triangle cycle on P–V"
- 04.2 → "Ice + warm water: not all the ice melts"
- 04.9 → "Very cold ice freezes all the water"
- 11.2 → "Thickest air gap before convection starts"
- 12.6 → "View factor by the crossed-string rule"
- 15.2 → "Cut a cone reflector from a flat sheet"
- 19.x → drop "Template n:"; title by what's asked

Review every other example title the same way.

**Text to add:**
1. Under **every** figure, one bold "How to read this:" line (none exist now). Examples:
   - Fig 16.2: "Find h on the x-axis → go up to your heating-time curve → read TG → add the Table 16.4 offset → subtract ΔT_cool."
   - Fig 5.1: "Follow the 1 atm line: crossings are melting/boiling points."
   - Fig 8.3a: "Below zero = spontaneous."
   - Fig 10.2: "If the outer radius is below r_crit, more insulation increases heat loss."
   - Fig 13.1: "At t = τ, 63% of the way; at 5τ, 99%."
   - Fig 14.1: "Absorbers top-left, reflectors bottom-left."
   - Fig 17.1: "Wait 5τ before reading."
2. Top of each quick sheet: "Full explanation: §x p.y · Worked example: p.z · Traps: p.w" (auto-generated with `\pageref`).
3. Every formula card gets four columns, Equation | Symbols with SI units | Use when | **Don't use when**, modeled on the §10 card (p103). Examples of "Don't use when":
   - Q = mcΔT: not across a phase change
   - PV^γ: reversible adiabatic only
   - η_C: reversible engines only, T in K
   - Newton cooling: Bi < 0.1 only
   - σT⁴: T in K, use T₁⁴ − T₂⁴

   Turn bare equations in running text that matter on tests into cards.
4. Start of Tab 2: half-page "Definitions in one line each": heat, temperature, internal energy, work, open/closed/isolated systems, intensive vs extensive (10 examples each), equilibrium, zeroth law.
5. Tab 6: an "Everyday heat transfer" box, each item with its mode and a one-line reason:
   - sea/land breeze
   - why metal feels colder than wood (effusivity)
   - thermos/Dewar flask
   - double-pane window
   - wind chill
   - igloo
   - dark vs light clothing
   - greenhouse
   - radiator (mostly convection)
6. Beside the App A steam table: "how to use" (linear interpolation, y = y_f + x·y_fg, compressed liquid ≈ saturated liquid at the same T).
7. Top of Tab 7, a boxed "Zero-score list":
   - TS = PS = 0: hazardous material incl. polystyrene, any energy source, touching device/lamp during heating, no device
   - PS = 0: prediction not handed in before heating ends
8. A banner on §16 tables and Figs 15.3, 15.5, 16.2, 17.2: "Modeled for the reference collector. Replace with our measured runs."
9. QS-13: a fill-in prediction card (h, t, T_room, T_start, TG_table, offset, ΔT_cool, T_pred to 0.1 °C).

---

## Phase 8: Device packet (aimed at the 20-point prediction score)

Build a 2-page "Our Device" packet at the front of Tab 7:
- Page 1:
  - the single prediction formula
  - a **blank** lookup grid of TG [°C] vs bulb height 40–65 cm (rows every 5 cm, plus a 1 cm interpolation line) × heating time 10–15 min
  - a blank ΔT_cool box (seconds waited vs drop)
  - the fill-in prediction card
- Page 2:
  - the calibration protocol: 15–20 runs across heights and times; record h, t, T_room, T_start, T_final, probe depth, glazing on/off, wait time; three repeats at the most likely height
  - a blank calibration chart (TG [°C] 0–40 vs h_bulb [cm] 40–65, lines for 10/12/15 min, arrowed axes)
  - the build-day checklist (merge §15.7, §23.7, §0.5 and App D.2 into one list: dimensions ≤ 30.0 cm cube incl. cup, no polystyrene/fiberglass/mineral wool/asbestos, no energy sources, no commercial thermos/cooler/vacuum device, no thermometers/probes in the device, nothing touches the water, nothing attached to the cup, room temperature at impound, impound device + spare parts, tongs/hot pads, goggles if glass)

Do NOT fill any numbers; the team will. Keep the reference-design tables as an appendix example, clearly labeled.

---

## Phase 9: Figures — add, fix overlaps, axis style

**Axis style** (one global pgfplots style in the .sty): `axis lines=left`, arrowheads on both axes (`axis line style={-stealth}`), labels "quantity [unit]", legends outside the plot area or curves labeled directly, no meaning carried by color alone (vary line style and markers for grayscale). Add the V unit to the Otto/Diesel/Brayton P–V plots (`sec09.tex` ~l.295, 330, 466). Add direction arrows to every cycle (e.g. Fig 9.1).

**Un-pile labels** on all crowded figures (leader lines, move legends, split two-panel figures that collide):
- Unreadable, highest priority: 0.2 (p9), 2.1 (p25), 3.3 (p34), 10.1 (p106; split sketch and circuit), 12.2 (p128; split), 15.1 and 15.2 (pp157, 160), 19.1 (p206; 2×3 grid or cut), 21.1 (p222; replace with a simple 3-zone desk sketch)
- Crowded: 4.1 (clipped stage labels, merged "3092.13217" ticks), 4.3 ("V = cons" cut), 5.1 (titles hit the P axis; TP label on "VAPOR"), 6.1, 8.1 ("Q_C − Q_C = 0!" cut), 8.3 (right axis label on "1,000"), 9.1 (panels use different T_H/T_C; make them match), 9.2, 11.1, 12.1 ("Opaque" hidden behind the legend), 13.1 (garbled "0.693 (t½τ)(63.2%)"), 14.2, 14.3, 15.4 (C_top hidden), 15.5, 16.1 (slope label hidden), 16.3, 17.2

**Add figures** (vector TikZ/pgfplots, arrowed axes with units, grayscale-safe):
- §7.3 p72: a thumbnail P–V column in Table 7.1 for all 8 processes, with direction arrow and shaded W_by
- §9.1 p93: engine / refrigerator / heat pump reservoir diagrams with arrow widths proportional to Q_H, Q_C, W and the η/COP formula under each
- §6.4 p62: kinetic-theory box (L, v_x, Δp = 2mv_x, 2L/v_x → P = Nm⟨v²⟩/3V)
- §10.4 p107: pin fin sketch above T [°C] vs x [cm]
- §17.1 pp184–188: five thermometer types (LiG, thermocouple with cold junction, Pt100 RTD, thermistor bead, IR spot cone) with range, resolution and response time
- §8.2 p84: T–S diagram of the four basic processes with Q_rev areas
- §3.3 p33: ring/hole expansion and bimetal strip
- §11.1 p116: convection plume over a heated cup and wall
- §13.2 p135: heating curve with equally spaced T₀, T₁, T₂, T_ss asymptote and 63% at τ
- §20: four "trap vs fix" mini plots (ice plateau, Carnot in °C vs K, isothermal vs adiabatic, R_tot vs r with r_crit)
- §23 or Tab 1: one-page process & cycle map (P–V and T–S panels) + heat-transfer mode decision tree
- One 4×4 cm thumbnail on each quick sheet (only QS-06 and QS-13 have figures now):
  - QS-02: bimetal
  - QS-03: heating curve
  - QS-04: water vs CO₂ phase diagrams
  - QS-05: Maxwell curve with v_mp < v_avg < v_rms
  - QS-07: Carnot rectangle on T–S
  - QS-08: reservoir boxes
  - QS-09: R network
  - QS-10: plume
  - QS-11: Planck curves at 300 / 2400 / 5778 K
  - QS-12: exponential approach
  - QS-14: timeline 1760–1911
- §15.7: exploded build view with step numbers

After every figure change, render the page at ≥130 dpi and look at it. Confirm there are no overlaps or clipped text and that the physics is right. The Device Handbook reuses §14–§16 figures, so rebuild and check it too.

---

## Phase 10: Print and layout

- **8 pt floor** for all printed text (subscripts may go to 6 pt). Redefine `\tabfont` to `\small`; remove `\scriptsize`/`\tiny` from tables, `\src`, `\flag`, App C (the dictionary and glossary are set in `\scriptsize` at arraystretch 0.93), App A, App B, §23, the router (p8) and the quick sheets (QS-06, QS-08 and QS-14 are mostly sub-8 pt). Make room by dropping redundant columns (e.g. Table 4.1's second c_p and "OS UP2" columns, long note columns) rather than adding pages.
- **Floats:** fix §20 (`[h!]` floats leave §20.1–20.4 as empty headings on p212; use `[H]` or non-floating `\captionof`), the orphan Table 4.2 caption at the foot of p40, the near-empty p244 (App C dictionary pushed to p245), and short pages p5, p38, p68, p172, p224.
- **Grayscale:** keep trap boxes distinguishable by border weight; check the grayscale proof after the font change.
- Cover: title + tab list only.

---

## Phase 11: Rebuild, verify, report

1. Rebuild all four PDFs and the grayscale proof; regenerate `markdown/` with `export_markdown.py` (residual macros = 0).
2. Run `pdfcheck.py`, `verify_all.py` (all checks pass, including new ones for every changed or added number) and `qa/audit_metrics.py`. Done means:
   - 0 characters under 8 pt outside sub/superscripts
   - 0 literal `**`
   - 0 empty headings
   - 0 pages under 250 words except intentional blank forms
   - every figure has a "How to read this" line
   - every formula card has 4 columns
   - every quick sheet has page pointers
   - every example has an Answer line
3. Re-render every figure page and visually confirm: no overlaps, legends correct, physics right.
4. Repeat the 30-question speed trace below. For each type, confirm the formula + example are on one page or spread and reachable from the tab map + router in under 30 s; list failures.
5. Update `README.md`, `markdown/README.md` and App H's revision line with real page counts from the build.
6. Final deliverables:
   - `CHANGELOG_OVERHAUL.md` (every change)
   - `REVIEW_NEEDED.md` (rule items to confirm in the manual, the C_eff decision, anything you couldn't verify)
   - a short summary: page count before/after, % text under 8 pt before/after, examples recomputed, figures fixed/added, speed-trace pass count

**Speed-trace question types (30):**
1. temperature scale & ΔT conversion
2. the 8 scientists
3. heat/energy unit conversion
4. system types / intensive–extensive / zeroth law
5. thermal expansion & bimetal
6. Q = mcΔT with property lookup
7. ice/water/steam mixing
8. calorimeter constant
9. phase diagram reading
10. lever rule / eutectic
11. Clausius–Clapeyron
12. steam tables (quality, h, s)
13. ideal & combined gas law, gauge→absolute
14. Dalton / gas over water / Graham
15. molecular speeds & KE
16. f, Cv, Cp, γ
17. first-law sign problems
18. work as area under P–V
19. Q/W/ΔU for the four processes
20. net work & efficiency of a P–V cycle
21. Carnot limit / impossible engines
22. COP fridge / heat pump
23. Otto/Diesel/Brayton/Rankine
24. entropy change & ΔS_universe
25. enthalpy / Hess / bomb vs coffee cup
26. ΔG & 2nd/3rd law statements
27. layered wall / R-values
28. property lookup (k, ε, c)
29. Stefan–Boltzmann & Wien
30. Newton cooling / heating curve & τ

Baseline: 18 pass, 6 formula only, 6 fail. Target: 30/30.

---

## What you must not do

- Don't push, merge, open PRs, or touch `main`.
- Don't fill in device calibration numbers or invent rule text, FAQ text or statistics.
- Don't change the sign convention or the meaning of any rule.
- Don't add new advanced topics; this overhaul makes the binder smaller and clearer.
- Don't raise font sizes before doing the Phase 5 cuts.
- Don't leave any changed number without a matching check in `verify/`.
