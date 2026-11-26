# Review Needed — items for the team to confirm

Items here need a human decision or a source the overhaul could not access (chiefly the purchased 2027 Rules Manual). Nothing in this list was changed in the binder unless the entry says so.

---

## A. Device model

### A1. What C_eff = 380 J/K means (Ex 13.2, §16) — decision taken, please confirm
- **Problem:** Ex 13.2 and §16 use C_eff = 380 J/K with τ = 903 s. 100 mL of water alone is 100.0 g × 4.184 J/(g·K) = 418.4 J/K, plus a few J/K for the cup. A uniformly heated cup cannot have C_eff < 418 J/K.
- **Decision taken:** C_eff is now stated to be a **fitted, effective top-layer capacitance**: the value that makes the one-node model match the temperature the ES probes at the top center. Stratification makes that layer warm faster than the mixed average, so the fitted value can be below 418 J/K. The model's numbers (and the τ = 903 s behind the §16 nomogram multipliers) were kept, and are labeled as modeled values for the reference collector.
- **Still open:** §15 uses a different top-layer capacitance for the same reference cup (C_top,eff ≈ 215 J/K, κ_strat ≈ 1.56). 380 J/K implies much weaker stratification (418.4/380 ≈ 1.10). Phase 4's single device model has to pick one; the team's own calibration runs should replace both.
- **Why it matters:** if your device behaves well-mixed (e.g. no glazing, strong side heating), C ≈ 420–425 J/K and τ is ~11% longer than the reference model assumes, which shifts the 11–15 min multipliers.

### A2. Two-node stratification lump vs. the depth profile (§15, §17) — left as is
- **Single source now:** for the reference run (h = 45 cm, 125 W, 10 min, T_start = 22.0 °C) the binder uses T_top = 49.7 °C (the §16 lookup), the Ex 15.4 two-node lump (C_top = 215.0 J/K at 49.70 °C, C_bot = 203.4 J/K at 29.34 °C, mixed 39.80 °C) and the Fig 15.6 depth profile (49.7 °C at 6 mm … 30.8 °C at the base). `verify/checks/check_reference_run.py` ties §15, §16 and §17 to these numbers.
- **Remaining inconsistency (model limitation, not fixed):** the lump's lower-node mean (29.34 °C) is below the profile's coldest point (30.8 °C at the base), and the profile integrates to a mixed temperature near 40–41 °C rather than 39.80 °C. Both are idealizations of a run nobody measured; I did not invent a new profile to force agreement.
- **What would settle it:** one measured run of your device with a probe at 3–4 depths (top, middle, base) and a swirled reading afterwards (practice only; swirling is not allowed in competition).
- Removed during Phase 2b because they conflicted with the §16 lookup model: the §15 8-layer table and the 5- and 15-min profile curves (see CHANGELOG).

---

## B. Rules items to check against your own Rules Manual (pp. C57–C59)
The official 2027 rules are only in the purchased Rules Manual, which the overhaul could not read. The binder's statements below were **not changed** (except where noted), only listed here so the team can confirm or correct them.

| # | Item | What the binder says now | Where | Check against |
|---|---|---|---|---|
| B1 | **TS formula conflict** | QS-13 (§1): TS = 30·TG_adj/TG_adj,max with TG_adj = TG·0.7^N_constr·0.9^N_comp, i.e. normalized by the highest **penalized** TG (same form for PS with PE_adj). §0.2, §16.1, §23 and App E: TS = 30·M_pen·TG/TG_max (normalized by the highest raw TG). The two differ whenever the top team has a violation. | `sec01.tex` ~l.696–701; `sec00.tex` ~l.83–89; `sec16.tex` ~l.19–30; `sec23.tex`; `appE.tex` ~l.57 | Rule 6.e–h and Scoresheet v2.0.0; then make every copy match |
| B2 | **Penalty multipliers** | 0.7 per construction violation, 0.9 per competition violation, multiplied together (M_pen = 0.7^V_c·0.9^V_p), applied to TS and PS only, never ES. FAQ 10/28/2026 says a device not impounded incurs one additional construction violation; the binder reads this as one more factor of 0.7. | `sec00.tex`, `sec16.tex` Table "penalty multiplier", cover | Rule 6.g–h; Scoresheet v2.0.0 |
| B3 | **TG and PE formulas** | TG = max(0, T_final − T_start) (§16.1); cover and App C print TG = T_f − T_i without the max (Phase 4 will add it). PE = max(0, 1 − \|T_f − T_pred\|/T_f) with temperatures in °C. | `sec16.tex`, cover, `appC.tex` | Rule 6.c–f |
| B4 | **Tiebreak order** | 1st best TS, 2nd best ES, 3rd preselected written-test questions. | cover; `sec00.tex` | Rule 6.j |
| B5 | **Bulb heights, times, setup windows** | Bulb height (bottom of bulb): Regional 40–50 cm in 5 cm steps; State 40–55 cm in 5 cm steps; Nationals 40–65 cm in 1 cm steps. Heating time: Regional 10 min; State/Nationals 10–15 min in 1 min steps. Device setup 3 min; water setup 1 min; cup out within 1 min after lamp-off. | `sec00.tex` tier box; cover; §15/§16 | Rules 4.c, 5.II.a–g |
| B6 | **Notes rule and calculators** | Paper notes of any form and any size from any source; pages may be separated/removed during any part of the event (Rule 2.c). Up to two Class III calculators (Rule 2.b). Prepared graphs/tables and setup tools are not impounded (Rule 2.d). | cover; `sec00.tex` §0.1 | Rules 2.a–2.d; Calculator Classes page |
| B7 | **Cup cover removal before the reading** | Several places say any film/cap on the cup must be **removed before T_f** (reading of Rule 5.II.g, "cup completely separated from all device components"). FAQ 10/21/2026 allows placing something on or around the cup but does not say whether it must come off before the reading. | `sec00.tex` timeline; `sec15.tex`; `device_handbook.tex` l.47; QuickRef | Rule 5.II.d, 5.II.g |
| B8 | **Polystyrene consequence** | A device containing polystyrene is barred from testing (TS = PS = 0) under Rule 3.b.iii. The FAQ (10/22/2026) says only that polystyrene is hazardous and should not be used. | `sec00.tex`; `sec14.tex`; §23.7 checklist | Rule 3.b.i–iii |
| B9 | **Prediction deadline** | Late prediction (after Heating Time ends) gives PS = 0 (Rules 5.II.f, 6.f.iv). Phase 4 sets one hand-in rule: "Hand in at heating minute 3; hard deadline before heating ends (Rule 5.II.f)". | `sec00.tex`, `sec16.tex`, `sec21.tex`, `sec23.tex` | Rules 5.II.f, 6.f |

**Changed in Phase 3 because they contradicted the official FAQ page (soinc.org/thermodynamics-div-c, read 26 Nov 2026):**
- QuickRef QR-01 said nothing may rest on the cup rim. FAQ 10/21/2026 allows placing something **on or around** the cup (no adhesives, tape or fasteners; cup shape unchanged). Corrected.
- QuickRef QR-01 cited "#7, #8" as "glazing cap must come completely off". FAQs 10/22/2026 are about opening a lid and the actions inherent to inserting the cup. Corrected; the removal question is B7.
- "Eye Protection: None" (cover, §0, App E, App F, QuickRef) → "None required by the event header; Category C goggles if your device contains glass (FAQ)".

---

## C. Things the overhaul could not verify
- **C1. FAQ wording.** The FAQ page was read on 26 Nov 2026: 11 entries, dates and topics as cited in the binder. The binder's quoted sentences from the 10/06/2026 FAQs ("No, the water must not be swirled, shaken or stirred before taking the temperature."; the probe-depth recommendation) and the 10/21/2026 FAQ ("No adhesives, tapes, or fasteners…") match the page; all other FAQ mentions are paraphrases and say so (§0.1). Re-check the page before each tournament for new entries.
- **C2. Exam-corpus statistics.** Percentages in tier boxes (e.g. §0 "100% of invitationals tested 5.c.vii … 28.6% of points on the Cornell Invitational") come from `research/phase2_exam_corpus.md`; they are rechecked or cut in Phase 5.
