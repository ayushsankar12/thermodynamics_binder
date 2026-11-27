# Binder overhaul — status (paused 26 Nov 2026)

Branch `binder-overhaul`, based on `main` at `677e35f`. The full task is in [`docs/overhaul_master_prompt.md`](docs/overhaul_master_prompt.md). Every change is logged in [`CHANGELOG_OVERHAUL.md`](CHANGELOG_OVERHAUL.md); items that need the team's Rules Manual or a decision are in [`REVIEW_NEEDED.md`](REVIEW_NEEDED.md).

**State at the pause**
- `verify/verify_all.py`: **1419 / 1419 pass** (baseline was 274).
- A draft compile of every chapter and appendix (one pass) succeeds with **0 overfull boxes > 3 pt**. QuickRef (12 pp) and Device Handbook (49 pp; 46 at baseline) build with 0 errors and 0 undefined references.
- The full four-PDF build (`python build/build.py --target all`) has **not** been rerun since Phase 1. Everything in `output/`, `qa/renders/`, `build/build-log.txt` and `build/verification-report.md` is stale and deliberately not committed.

**Done so far**: Phases 1, 2 and 3 are complete. Phase 4 is about two-thirds done. Phases 5–11 have not started, apart from a few items done along the way, which are noted under each phase.

---

## Phase-by-phase

### Phase 1 — Baseline: **done** (`7f7d86c`)
- [x] Built all four PDFs. Page counts, warnings, overfull boxes, `pdfcheck.py` and `verify_all.py` results are recorded in the changelog.
- [x] `qa/audit_metrics.py` (PyMuPDF): words per page, minimum font, share of text under 8 pt, pages under 250 words, literal `**`, empty headings, captions without "How to read". The baseline is saved in `qa/metrics/baseline_*`.
- [x] Tooling fixes needed to build at all: the macOS `TEXINPUTS` separator and NumPy 2's removed `np.trapz`.

### Phase 2 — Accuracy: **done**
- **2a, worked examples** (`83c64f8`, `7b48b52`, `a2fe0bc`; follow-ups in `eca084c`, `522ce78`)
  - [x] Every flagged example fixed: 11.1, 12.3, 12.1, 09.3, 09.4, 07.6, 05.5, 04.1, 03.2, the §20 statistics, the p38 devicebox and the §8 tierbox claims.
  - [x] C_eff = 380 J/K decision: REVIEW A1.
  - [x] All 163 worked examples and 38 problems recomputed. Real errors fixed include P10.5, Ex 12.4, the Planck table, Ex 18.4, Ex 15.6b, Ex 15.1b, Ex 8.9, Ex 9.7–9.9, Ex 11.7, P13.11, Ex 14.1 and Ex 16.7.
  - [x] Checks went from 274 to 1020.
- **2b, figures** (each re-rendered and inspected after its fix)
  - [x] Fig 1.1 (`a2fe0bc`).
  - [x] Fig 16.2 and all §16 tables, generated from `verify/device_model.py` (`eca084c`).
  - [x] Figs 5.2, 5.3, 14.1, 18.2 (`f466f2e`).
  - [x] Figs 9.3a, 9.4a, 10.2 (`7aee441`).
  - [x] Fig 12.2 split into 12.2 and 12.3 (`31e6149`).
  - [x] Fig 13.2 (`2d7562c`).
  - [x] °Rø for Rømer (`523c57f`).
  - [x] Fig 6.3a (`2344274`).
  - [x] Fig 17.2 plus the §15 single reference-run model (`522ce78`).
  - [x] Fig 15.3, and one view-factor plane at z_ap = 30.0 cm (`2734019`).
  - [x] Invar 1.2×10⁻⁶ /K (2a).

### Phase 3 — Rules and FAQs: **done** (`1fde937`)
- [x] 189 invented "Clarification #n" citations → "FAQ mm/dd/2026 (topic)".
- [x] §0.1 ledger rebuilt as the 11 official FAQs. They were re-read on soinc.org (`/thermodynamics-div-c`) on 26 Nov 2026.
- [x] "9 clarifications" → "11 official FAQs (checked 26 Nov 2026)" everywhere, including both READMEs and `build/architecture-lock.md`.
- [x] Eye protection now reads "None required by the event header; Category C goggles if your device contains glass (FAQ)." on the cover, §0, App E, App F and the QuickRef.
- [x] Tongs, hot pads and gloves (FAQ) added to the §23.7, App F and QuickRef checklists.
- [x] Fixed two QuickRef statements that contradicted the FAQs: items *may* rest on or around the cup, and the 10/22 FAQs concern lids and inserting the cup.
- [x] REVIEW_NEEDED section B lists the rule items for the team to confirm, unchanged in the binder: B1 the TS formula conflict, B2 multipliers, B3 TG/PE, B4 tiebreak, B5 heights/times, B6 notes and calculators, B7 removing the cup cover, B8 the polystyrene consequence, B9 the prediction deadline.

### Phase 4 — Consistency: **partly done** (`9581da9`, `f778d17`, and the wrap-up commit that adds this file)
- House constants
  - [x] L_f = 333.55, c_ice = 2.09, L_v = 2256.4, c_steam = 2.08 everywhere, with each affected example recomputed and checked (`f778d17`).
  - [ ] **R = 8.314, σ = 5.670×10⁻⁸ and b = 2898 µm·K in examples**: deferred (see Deferred decisions).
- [x] **Single prediction formula**: the `\TpredFormula` macro, used in §0.4/§0.5, QS-13, §15, §16, §21.2, §23 C39/§23.7, App D and the Device Handbook (`9581da9`). *The QuickRef still has its own prediction box and device table* (see the QuickRef decision).
- [x] **Single hand-in rule**: `\HandInRule` in every timeline (`9581da9`).
- Single device model
  - [x] The "Reference collector (modeled), not our device" table (`tab:16:reference-collector`) is the one source. A check ties it to the code.
  - [x] Fixed in Phase 2b and in this part: the §15 stage-angle text and Table 15.3 (43.3°, not 15.2°), the τ line, the Table 15.4 ratio column, and Ex 17.4.
  - [ ] The Fig 15.1/15.2 angle labels are not yet fixed (see Deferred decisions).
  - [ ] Some "reference design (modeled)" labeling is still missing in §13 and the Device Handbook.
- Notation
  - [x] W_by / w_on, with §19 using W_in.
  - [x] α_L for expansion (QS-02, router, App B; §3 already used it).
  - [x] c for molarity.
  - [x] M_b / M_e for exitance.
  - [x] τ_opt in App A.
  - [x] TG = max(0, ·).
  - [ ] α_abs for absorptance: §12 and §14 still use α / α_NIR.
  - [ ] τ_opt everywhere else: τ_NIR / τ_MIR were left as they are.
- [ ] **Sheet numbering, QR vs QS**: decided (rebuild the QuickRef from QS-01–QS-14), not implemented.
- Box and layout house style
  - [x] The steam-c_p rulebox became a shortcut box.
  - [ ] Audit the remaining `rulebox` uses (rules and FAQs only).
  - [ ] One skeleton per section, and at least one shortcut box per section.
  - [ ] One example format: §10–§13 problem/solution converted, or moved out in Phase 5.
  - [ ] Meta tags "Warm-up · 30 s / Standard · 60 s / Hard · 2 min": deferred.
  - [ ] A boxed **Answer:** line on every example: deferred.
- [x] **Render bugs** (`9581da9`):
  - Literal `**` and `*( )*` leaks.
  - Backticks in the §3.4 heading.
  - Doubled running heads.
  - "six case studies".
  - Table A.4a/b renumbered.
- [ ] **Stale page counts**: `markdown/README.md` ("248 Pages", "250 pp" and per-section targets), the cover's "Budget" column, `src/main.tex` comments and `build/architecture-lock.md` ("246–250"). Generate page ranges from the `.aux` at build time and delete the hard-coded budgets.

### Phase 5 — Cut and merge (~40 pages): **not started**
Every row of the prompt's table is still open.
- [ ] TOC → tab map.
- [ ] Cover rules wall → §0.1.
- [ ] 4 partner timelines → 1 event-day card.
- [ ] 6 scoring copies and examples 00.1 / 16.1 / 21.1 → one.
- [ ] FAQ restatements → pointers.
- [ ] §22 → half page.
- [ ] Delete §21.4 and §21.5.
- [ ] §19.4 → 3 lines.
- [ ] §23.1/23.2/23.4–23.5 → quick sheets; §23.3 → QS-14 + §3.4.
- [ ] App C formula index, error index and device index.
- [ ] App H build pipeline; App G → top 10 sources.
- [ ] Table 4.1 and the §5 steam table → App A.
- [ ] Problem banks §10.7, §11.6, §12.5, §13.6 → 3 problems each, the rest to `practice/`.
- [ ] Deep dives (§8.6, §8.7, §9.7–9.8, §7.7, §15.3, §17.6, §14.3) → ½ page each.
- [ ] 4 trap catalogs → a trap box per section + §20.4.
- [ ] Delete Ex 19.4 (duplicate of 06.7).

Already done along the way: §15's 8-layer table and the 5- and 15-min profile curves were removed in Phase 2b because they conflicted with the lookup model.

### Phase 6 — Reorganize and rename: **not started**
- [ ] One-page 9-tab map.
- [ ] Merge §21 into the Tab 1 event-day card.
- [ ] Plain-language chapter and subsection titles.
- [ ] Formula homes generated from one macro per formula (the prediction formula already is).
- [ ] App B → "find a variable → page" with no equations; the router → questions → page.
- [ ] A single IAPWS-95 steam table in App A (0.01–200 °C, ideally to 374 °C, plus a superheated block).
- [ ] Property lookup table.
- [ ] α_L table in §3.3.

### Phase 7 — Speed: **not started**
- [ ] Move examples next to their concepts; one spread per subsection.
- [ ] The 24 warm-ups (answers verified).
- [ ] Retitle the jargon example titles.
- [ ] "How to read this:" under every figure. Only Figs 15.3 and 17.2 have one so far.
- [ ] Page pointers on the quick sheets.
- [ ] 4-column formula cards.
- [ ] Definitions half-page.
- [ ] "Everyday heat transfer" box.
- [ ] Steam-table how-to.
- [ ] Zero-score list.
- [ ] "Modeled for the reference collector" banners: done on Fig 17.2 and the reference table; §16 tables and Figs 15.5/16.2 left.
- [ ] QS-13 fill-in prediction card.

### Phase 8 — Device packet: **not started**
- [ ] The 2-page "Our Device" packet: blank lookup grid, blank ΔT_cool box, fill-in card, calibration protocol, blank calibration chart, one merged build-day checklist.
- [ ] Move the reference-design tables, including the new `tab:16:reference-collector`, to an appendix example.

### Phase 9 — Figures: **not started as a phase**
- Done during Phase 2b: labels un-piled in Figs 1.1, 5.2, 5.3, 6.3, 9.3a, 9.4a, 10.2, 12.2/12.3, 13.2, 14.1, 15.3, 15.6, 17.2 and 18.2.
- [ ] Global pgfplots axis style (arrowed axes, "quantity [unit]", grayscale-safe).
- [ ] V unit on the cycle plots; direction arrows on every cycle.
- [ ] Highest-priority un-piling: 0.2, 2.1, 3.3, 10.1, 15.1, 15.2, 19.1, 21.1.
- [ ] The crowded list (4.1, 4.3, 5.1, …).
- [ ] All the new figures and the quick-sheet thumbnails.

### Phase 10 — Print and layout: **not started**
- [ ] 8 pt floor. Fonts must not be raised before the Phase 5 cuts.
- [ ] Floats: §20 empty headings; the orphan Table 4.2 caption; short pages.
- [ ] Grayscale check.
- [ ] Cover = title + tab list.

### Phase 11 — Rebuild, verify, report: **not started**
- [ ] Full build plus the grayscale proof.
- [ ] `export_markdown.py`, `pdfcheck.py`, `audit_metrics.py --label final`.
- [ ] Re-render every figure page.
- [ ] 30-question speed trace.
- [ ] READMEs and App H revision line with real page counts.
- [ ] Final summary.

---

## Deferred decisions

1. **R / σ / b sweep (Phase 4), deferred until after the Phase 5 cuts.**
   - **What is affected:** about 45 examples quote R = 8.3144626…, σ = 5.670374…×10⁻⁸ or b = 2897.77, and many print 5–6 digits, so their intermediates change.
     - R: Ex 04.7, 05.4, 05.5, 06.1–06.7, 07.4, 07.5, 07.6, 07.9, 07.10, 07.12, 08.2, 08.5, 08.7, 08.8, 09.2, 09.9, 15.5, 18.4, 19.6, the §19 examples at l.251/369, and 20.5.
     - σ: §12 examples and problems, 14.1, 14.5, 17.6, 19.2, §19 l.357, 20.2.
     - b: §12.
     - Non-example text: §0, §1 (QS-01), §2, §6 and §23. App A.1 keeps the full CODATA digits.
   - **Why wait:** several of these sit in content that Phase 5 cuts or moves (problem banks, §8.7, §9.7–9.8, Ex 19.4), so recomputing them first would be wasted.
   - **How to do it:** `check_examples_recomputed.py` already defines the house constants (`R_H`, `SIG_H`, `B_H`). Switch each example's check to them, let the failing checks list the printed numbers that move, then fix the text and any unchecked intermediates by hand.
2. **Meta tags and a boxed Answer line on every example (Phase 4), deferred until after the Phase 5 cuts.** Phase 7 also moves and retitles examples, so this pass is best done once, on the final set.
3. **QuickRef rebuilt from QS-01–QS-14 (Phase 4 sheet numbering). Decided, not implemented.**
   - **Why:** the QuickRef keeps its own copies of content that conflict with the binder.
     - Its own reference-device TG table.
     - κ_strat "1.28–1.42" (the model gives 1.556).
     - ">68% of the NIR in the top 10 mm" (§15 gives 72.4%).
     - The "−ΔT_drift(T_i − T_room)" prediction formula.
     - Its own QR-01…QR-12 numbering.
   - **Plan:** rebuild `quickref_12pp.tex` to `\input` the binder's quick sheets (cross-references via xr-hyper), so there is one source.
   - **Needs a decision:** the result is about 14 pages, so the output name `…_QuickRef_12pp.pdf` and the README references need a decision.
   - Until then, the QuickRef's Phase 3 FAQ fixes are in, but its prediction box and device table are stale.
4. **Fig 15.1 / 15.2 angle labels, deferred to the Phase 9 redraw.**
   - **Mismatch:** the drawings are labeled 23.5°/29.7° (Fig 15.1) and 23°/30°/15° (Fig 15.2), but the single source (Table 15.3) gives 23.2°/33.5°/43.3°.
   - **Why wait:** the drawn coordinates don't match Table 15.3 either, so the labels can't simply be changed; both figures are also on Phase 9's "unreadable" list.
   - **Fix:** redraw both from Table 15.3.
5. **Two-node lump vs. depth profile** (REVIEW A2): left as a documented model limitation. It needs a measured run, not invented numbers.
6. **Phase order.** Because of items 1–2, Phase 4 will finish after Phase 5. The end state is the same as the prompt's order.

## Gotchas hit so far

- **TeX on this Mac** is BasicTeX plus packages installed with `tlmgr --usermode` into `~/Library/texmf` (approved by the user). `build/build.py` needed `os.pathsep` in `TEXINPUTS`; macOS uses `:`, not `;`.
- **`build.py` copies `build/thermobinder.sty` over `src/`.** Edit the `build/` copy (canonical) and copy it to `src/`; they must stay identical.
- **The first Device Handbook build sometimes yields a 0-page PDF** with no error. Rerun it.
- **NumPy 2 removed `np.trapz`.** The checks use `getattr(np, "trapezoid", None) or np.trapz`.
- **PyMuPDF reports TeX's 8 pt as 7.97 pt**, so the audit's "under 8 pt" threshold is < 7.9 pt.
- **Example labels differ from printed numbers** in §1, §8.6–8.8, §15 after 15.1, and §16 after 16.2 (`ex:15.4` prints as Example 15.6). The changelog cites labels with the printed number in brackets.
- **Check tolerance:** a value passes only if it rounds to the printed digits. Displayed arithmetic on rounded intermediates is left as printed; those cases are noted in the changelog.
- **`\o` is text-only.** In math mode it is silently dropped, which is why Rømer printed as °R. Use `\text{R\o}`.
- **pgfplots helper lines steal legend entries** unless they have `forget plot`. This caused the shifted legends in Figs 14.1 and 18.2.
- **Long citations in non-wrapping `l` table columns** make tabularx collapse its X columns ("X Columns too narrow"), producing hundreds of overfull boxes. This happened in the Device Handbook after Phase 3. Keep table citations short ("FAQ 10/22"), and grep build logs for that warning.
- **Draft compiles of a few sections show `??` references.** That is expected; only the full build resolves cross-references and indices.
- **Shell quoting:**
  - zsh's `echo` mangles backslashes, so write generated `.tex` with `printf`.
  - Keep pdflatex's stdout out of the `.out` file, or hyperref loops.
  - `sed` and `grep` escaping of LaTeX is error-prone. Python replacements that assert an exact match count were reliable.
- **soinc.org:** the FAQ page is `https://www.soinc.org/thermodynamics-div-c`, with dates on the Division C events listing. The older event URLs return 404.

## How to resume

1. Read `docs/overhaul_master_prompt.md`, then this file, `CHANGELOG_OVERHAUL.md` and `REVIEW_NEEDED.md`.
2. Python tools run in `.venv` (`.venv/bin/python`: PyMuPDF, NumPy). Check with `.venv/bin/python verify/verify_all.py`.
3. To compile a few sections quickly, write a small driver and run pdflatex on it with `TEXINPUTS=src:build:`. The driver is:

   ```latex
   \documentclass[10pt,twoside,openany,letterpaper]{book}
   \usepackage{thermobinder}
   \begin{document}\mainmatter
   \input{sec15}
   \end{document}
   ```

   Put `\appendix` before the first appendix. Render pages with PyMuPDF (`page.get_pixmap(dpi=140)`) and look at them.
4. Suggested order:
   - The Phase 4 leftovers that don't depend on the cuts: stale page counts, the QuickRef rebuild, and the remaining `rulebox` audit.
   - **Phase 5 cuts.**
   - The deferred R/σ/b sweep, then meta tags and Answer lines.
   - Phases 6–11.
