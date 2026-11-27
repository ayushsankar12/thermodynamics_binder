# Handoff: finish the 2027 Div C Thermodynamics binder overhaul

You are taking over a half-finished overhaul of a LaTeX competition binder. You have no prior context. This file, the files it names, and the git history are your context.

The theme of the whole job is **CLEAN, EASY TO FIND, EASY TO USE THE FIRST TIME.**
- **Correctness comes first.**
- **Right after it comes this test:** a student who has never opened this binder finds the right page and uses it within 30 seconds, under stress, while a partner is talking.
- **Every cut, merge, rename and layout decision is judged by that test.**

## 0. Read first, in this order

1. `docs/overhaul_master_prompt.md`. This is the full specification: Phases 1–11, the hard rules, the "Done means" list and the 30-question speed trace. It defines the scope. This handoff adds the current state, the decisions already taken, and the usability bar.
2. `OVERHAUL_STATUS.md`, `CHANGELOG_OVERHAUL.md` and `REVIEW_NEEDED.md`.
3. `git log --oneline main..binder-overhaul`.
4. `build/build.py`.
5. `build/thermobinder.sty`. Note the `\TpredFormula`, `\HandInRule` and `\TGFormula` macros.
6. `verify/verify_all.py`, `verify/device_model.py` and `verify/checks/*.py`.
7. `qa/audit_metrics.py`, `qa/pdfcheck.py` and `build/export_markdown.py`.

**State at handoff (27 Nov 2026)**
1. On `origin`, branch `binder-overhaul` is at `15dda0a`. This file is committed on top of it; that commit is on `origin` only if the user has pushed it. `main` is at `677e35f` and must stay untouched.
2. `python verify/verify_all.py` gives **1419 / 1419 checks pass in 11 modules**.
3. Phases 1–3 are done. Phase 4 is about two-thirds done. Phases 5–11 are open.
4. The full four-PDF build was last run in Phase 1.
   - Everything in `output/`, `qa/renders/`, `build/build-log.txt` and `build/verification-report.md` is stale.
   - On 26 Nov 2026 the QuickRef (12 pp) and Device Handbook (49 pp) were rebuilt cleanly, and a one-pass draft of every chapter compiled with 0 overfull boxes larger than 3 pt.
5. Baseline metrics for the "before" column of your final report are in `qa/metrics/baseline_summary.md` (Phase 1):
   - 264 pages.
   - 26.3% of characters under 8 pt (18.6% excluding sub/superscripts).
   - 38 pages mostly under 8 pt.
   - Minimum font 5.08 pt.
   - `**` on 9 pages.
   - 5 empty headings.
   - 54 of 54 figures without "How to read".
   - Speed trace: 18 pass, 6 formula only, 6 fail.

---

## 1. Goal and audience

1. **Users.** Two Science Olympiad Division C partners use the binder at once during a 50-minute event: a timed written test (Part I) plus a pre-built heat-lamp collector whose final water temperature they must predict (Part II).
2. **Format.** The binder is printed, possibly in **grayscale**, and used open on a desk. Pages may be removed during the event (the binder's reading of Rule 2.c; to be confirmed in the manual, REVIEW_NEEDED B6).
3. **Priorities.** Correct beats complete. Complete beats polished. A wrong answer costs more than a missing one.
4. **The first-timer test** (the main quality bar after correctness):
   - A student who has never seen the binder starts at the cover.
   - Using only the tab map and the question router, they reach a page holding the formula (with symbols, units and when it applies) and a worked example on the same page or facing pages.
   - They do it in 30 seconds or less, without flipping between sections.
   - Every change you make must keep or improve this.

---

## 2. Setup

1. Clone and check out the branch. Do not create a new one.
   ```bash
   git clone https://github.com/ayushsankar12/thermodynamics_binder.git
   cd thermodynamics_binder
   git checkout binder-overhaul
   ```
2. Create the Python environment.
   ```bash
   python3 -m venv .venv
   .venv/bin/pip install pymupdf pillow numpy scipy
   ```
3. Check for TeX.
   ```bash
   which latexmk pdflatex makeindex
   kpsewhich tcolorbox.sty pgfplots.sty siunitx.sty imakeidx.sty xr-hyper.sty needspace.sty
   ```
   **If TeX or any package is missing, stop and ask the user before installing anything.**
4. Verify the starting point.
   ```bash
   .venv/bin/python verify/verify_all.py
   ```
   It must print `checks=1419 passed=1419 failed=0`. If it doesn't, stop and report.
5. Full build. It takes about 7 minutes and writes `output/*.pdf` and `build/build-log.txt`.
   ```bash
   .venv/bin/python build/build.py --target all
   ```
   Single targets are `--target main|gray|quickref|device`. The companions (QuickRef, Device Handbook) read `main.aux`, so build `main` first.
6. QA commands.
   ```bash
   .venv/bin/python verify/verify_all.py             # numeric checks; must end with failed=0
   .venv/bin/python qa/pdfcheck.py                   # P1–P6 page/ref/margin/font checks + V1 renders into qa/renders/
   .venv/bin/python qa/audit_metrics.py --label <phase-name>   # writes qa/metrics/<label>_summary.md
   .venv/bin/python build/export_markdown.py         # regenerates markdown/ (residual macros must be 0)
   ```
7. Quick draft compile of a few sections. Use it for fast checks. It shows `??` for cross-references outside the draft; that is expected. First create `scratch/` and add it to `.gitignore`.
   - Driver, `scratch/draft.tex`:
     ```latex
     \documentclass[10pt,twoside,openany,letterpaper]{book}
     \usepackage{thermobinder}
     \begin{document}\mainmatter
     \input{sec15}
     \end{document}
     ```
   - Put `\appendix` before the first appendix.
   - Compile it:
     ```bash
     cd scratch && TEXINPUTS="../src:../build:" pdflatex -interaction=nonstopmode -file-line-error draft.tex > draft.stdout 2>&1
     ```
   - Keep pdflatex's console output out of `draft.out`, because hyperref writes that file.
8. Render a page for inspection at 130 dpi or more.
   ```bash
   .venv/bin/python -c "import pymupdf,sys; d=pymupdf.open(sys.argv[1]); d[int(sys.argv[2])-1].get_pixmap(dpi=150).save(sys.argv[3])" output/Thermodynamics_DivC_Binder.pdf 42 scratch/p042.png
   ```

---

## 3. Hard rules

These are copied word for word from `docs/overhaul_master_prompt.md`. In them, "this prompt" means that file.

**Overall rule (master prompt, opening paragraph):**

> When an item needs a human decision or a source you cannot access, do not guess: add it to `REVIEW_NEEDED.md` and move on.

**Git rules**
- Create a branch first: `git checkout -b binder-overhaul`. Never commit to `main`. Do not push, open PRs, comment or open issues unless the user asks.
- Commit after each phase with a clear message. Keep a running `CHANGELOG_OVERHAUL.md` listing every change with file, old → new, and reason.

The branch already exists on `origin`. Run `git checkout binder-overhaul`; do not create it again.

**Hard rules**
- Never invent rules text, clarification text, test statistics or device data. The official 2027 rules are only in the purchased Rules Manual, not on soinc.org.
- Never fabricate calibration data. Leave blank tables for the team to fill in.
- Physics sign convention stays ΔU = Q − W_by (chemistry ΔU = q + w_on shown only as a translation).
- SI units throughout; every answer has units and sensible significant figures.
- After changing any number, recompute it and add or update a check in `verify/`. `verify/verify_all.py` must pass at the end.
- Don't add new deep content. The goal is a smaller, cleaner binder. The only new content allowed is what this prompt lists.

**What you must not do**
- Don't push, merge, open PRs, or touch `main`.
- Don't fill in device calibration numbers or invent rule text, FAQ text or statistics.
- Don't change the sign convention or the meaning of any rule.
- Don't add new advanced topics; this overhaul makes the binder smaller and clearer.
- Don't raise font sizes before doing the Phase 5 cuts.
- Don't leave any changed number without a matching check in `verify/`.

**Additional rules for this handoff (non-negotiable):**
1. Commit only to `binder-overhaul`. Never touch `main`. Push only when the user tells you to. Open no PRs.
2. Do not resolve any `REVIEW_NEEDED.md` item (A1–A2, B1–B9, C1–C2) by guessing. The 2027 Rules Manual is not available to you.
3. Do not commit `output/`, `qa/renders/`, `build/build-log.txt` or `build/verification-report.md` until the Phase 11 commit, and only after the final build passes. Before that they are stale.

---

## 4. Already done. Do not redo or undo.

| Phase | Commits | Done |
|---|---|---|
| 1 Baseline | `7f7d86c` | Baseline builds and metrics recorded in the changelog. Added `qa/audit_metrics.py`. Tooling fixes: macOS `TEXINPUTS` separator in `build.py`; NumPy 2 `trapz` fallback in the checks. |
| 2a Worked examples | `83c64f8`, `7b48b52`, `a2fe0bc` | Every flagged example fixed. **All 163 worked examples and 38 problems recomputed**; real errors fixed and logged. Checks went from 274 to 1020. |
| 2b Figures | `eca084c`, `f466f2e`, `7aee441`, `31e6149`, `2d7562c`, `523c57f`, `2344274`, `522ce78`, `2734019` | Fig 16.2 nomogram and all §16 tables generated from `verify/device_model.py`. Figs 1.1, 5.2, 5.3, 6.3a, 9.3a, 9.4a, 10.2, 12.2 (split into 12.2 and 12.3), 13.2, 14.1, 15.3, 15.5, 17.2 and 18.2 fixed and re-rendered. Rømer prints °Rø. Invar uses 1.2×10⁻⁶ /K. |
| 3 Rules/FAQs | `1fde937` | 189 "Clarification #n" citations replaced by dated FAQ citations. §0.1 FAQ table. Eye-protection wording. Tongs/hot pads/gloves on the checklists. REVIEW section B. |
| 4 (partial) | `9581da9`, `f778d17`, `15dda0a` | Single prediction formula, single hand-in rule, TG = max(0, ·). Render bugs fixed (`**`, backticks, doubled running heads, "six" case studies, Table A.4a/b). House constants L_f, c_ice, L_v, c_steam. Reference-collector table. Notation fixes. Layout regressions from Phase 3 fixed. |

**Decisions in force. Build on them; do not reverse them.**

1. **Single device model**
   1. `verify/device_model.py` is the only source for the reference collector's lookup numbers:
      - 10-minute, 125 W gains of 24.8, 27.7, 21.3, 17.5, 13.6 and 10.6 °C at 40, 45, 50, 55, 60 and 65 cm;
      - τ_eff = 903 s;
      - η(100 W) = 0.800;
      - M_t, k_start and k_room.
      
      `verify/checks/check_device_model.py` compares every §16 table cell and every nomogram point with it (311 checks).
   2. Table `tab:16:reference-collector` ("Reference collector (modeled), not our device", at the start of §16.3) is the single source for every reference-design number in §13, §15, §16 and §17:
      - **One-node fit at 45 cm:** P_abs 24.0 W, C_eff 380 J/K, R 2.376 K/W, giving 49.7 °C at 10 min and 58.0 °C at 15 min. It is used for heating curves and time scaling.
      - **Two-node lump:** C_top 215.0 J/K at 49.70 °C and C_bot 203.4 J/K at 29.34 °C, giving a mixed 39.80 °C and κ_strat 1.556. It is used only for mixing estimates.
      - **Depth profile:** 49.7 °C at 6 mm down to 30.8 °C at the base.
      - **Three different "gain" ratios at 40 cm:** 45.1× power intercepted, 13.6× beam delivered, 11.0× absorbed.
      - **Stage half-angles:** 23.2°, 33.5°, 43.3°.
      
      `verify/checks/check_reference_run.py` checks all of it (51 checks).
   3. The two models are kept **on purpose** and are documented in REVIEW_NEEDED A1/A2. Do not invent a new profile or new data to make them agree.
2. **The 11 official FAQs**
   1. They come from `https://www.soinc.org/thermodynamics-div-c` and were re-read on 26 Nov 2026. Cite them as "FAQ mm/dd/2026 (topic)". Inside narrow table cells use the short form "FAQ 10/22".
   2. The FAQs:
      - Undated: glass allowed, with Category C goggles.
      - Undated: tongs, hot pads and gloves allowed.
      - 09/30: water will not be stirred or swirled.
      - 10/01: no swirling.
      - 10/06: no swirling, shaking or stirring.
      - 10/06: probe depth is the local ES's call; top layer near the center is recommended.
      - 10/21: items may be placed on or around the cup; no adhesives, tape or fasteners; cup shape unchanged.
      - 10/22: polystyrene must not be used.
      - 10/22: opening a lid counts as inserting the cup.
      - 10/22: actions inherent to inserting the cup are not modifying.
      - 10/28: not impounding means one additional construction violation.
   3. Only three quotes were checked word for word against the page: the 10/06 no-swirl sentence, the 10/06 probe-depth recommendation, and the 10/21 "No adhesives…" sentence. All other FAQ text is paraphrase and is labeled as paraphrase.
3. **House constants** (one value everywhere, with "use the test's value if one is given"). Full CODATA digits appear only in App A.1.

   | Constant | Value | Status |
   |---|---|---|
   | L_f | 333.55 J/g | done |
   | L_v (100 °C) | 2256.4 J/g | done |
   | c_w | 4.184 J/(g·K) | done |
   | c_ice | 2.09 J/(g·K) | done |
   | c_steam | 2.08 J/(g·K) | done |
   | R | 8.314 J/(mol·K) in examples | **open (P4.1)** |
   | σ | 5.670×10⁻⁸ W/(m²·K⁴) in examples | **open (P4.1)** |
   | b | 2898 µm·K in examples | **open (P4.1)** |

   `verify/checks/check_examples_recomputed.py` defines `L_F, L_V, C_W, C_ICE, C_STEAM, R_H, SIG_H, B_H`. Use them.
4. **Macros in `build/thermobinder.sty`**
   1. `\TpredFormula` is math-mode content. Write `$\TpredFormula$`. It prints T_pred = T_start + TG_table(h, P, t) + k_room(t)·(T_room − T_start) − ΔT_cool, all in °C, reported to 0.1 °C.
   2. `\HandInRule` is text that ends with a period: "Hand in at heating minute 3; hard deadline before heating ends (Rule 5.II.f)."
   3. `\TGFormula` is math mode: TG = max(0, T_final − T_start).
   4. Use these macros. Never retype the formulas.
5. **Removed on purpose. Do not restore.**
   - The §15 eight-layer table (printed as Table 15.9 in the baseline PDF), and the 5- and 15-minute curves of Fig 15.5 (`fig:15:stratification-profile`). They conflicted with the lookup model.
   - The 29.5 cm hybrid view-factor asides (43.65×, F = 0.64355 / 0.14807). There is one plane, z_ap = 30.0 cm.
   - QS-13's old prediction model.
   - The Device Handbook's "S₀ + k_start·T_start".
   - All "Clarification #n" numbering.

---

## 5. What remains, in the master prompt's phase order

Each item lists its acceptance criteria. "Changelog" means a row in `CHANGELOG_OVERHAUL.md` (file, old → new, reason). "Checked" means verify_all passes and every changed or added number has a check in `verify/`.

### Phase 4 leftovers

These serve findability by giving one value, one formula and one place for each thing, so a first-timer never meets two conflicting numbers.

**P4.1 Set R = 8.314, σ = 5.670×10⁻⁸ and b = 2898 µm·K in the surviving examples.** Do this after the Phase 5 cuts.
1. **Scope:**
   - R: Ex 04.7, 05.4, 05.5, 06.1–06.7, 07.4, 07.5, 07.6, 07.9, 07.10, 07.12, 08.2, 08.5, 08.7, 08.8, 09.2, 09.9, 15.5, 18.4, 19.6, 19.8 and 20.5. (Ex 19.4 also uses R, but Phase 5 deletes it.)
   - σ: the §12 examples and problems, 14.1, 14.5, 17.6, 19.2, 19.7 and 20.2.
   - b: §12.
   - Non-example text in §0, QS-01, §2, §6 and §23.
   - These are `ex:` labels, not printed numbers. Skip anything Phase 5 removed.
2. **Method:**
   1. In the check modules (`check_examples_recomputed.py`, plus the hard-coded R and σ in `check_sec02_05.py`, `check_sec06_09.py`, `check_sec10_13.py`, `check_sec14_16.py` and `check_sec17_20.py`), switch that example's constants to `R_H`/`SIG_H`/`B_H`.
   2. Run verify_all. The failing checks list the printed numbers that change.
   3. Update the text, including unchecked intermediate values (recompute them by hand).
   4. Add checks for every number you change.
3. **Accept when:**
   - `grep -nE "8\.3144|8\.3145|5\.67037|5\.6704|2897\.7|2\.8978" src/sec*.tex src/app[B-H].tex src/device_handbook.tex src/quickref_12pp.tex` returns nothing.
   - App A.1 alone keeps the full digits.
   - verify_all passes.
   - Every old → new value is in the changelog.

**P4.2 Rebuild the QuickRef from the binder's QS-01–QS-14.**
1. **Change:**
   - Make `src/quickref_12pp.tex` `\input` the binder's quick sheets, so there is one source.
   - Delete the QuickRef-only content: the QR-01…QR-12 numbering, its own device TG table, "κ 1.28–1.42", ">68% in the top 10 mm" and the "−ΔT_drift" formula.
2. **Page count and file name:**
   - The page count becomes the number of quick sheets (14 unless Phase 5/6 changes it).
   - Update `qa/pdfcheck.py` P2, which currently requires exactly 12 pages.
   - Keep the output filename and add a REVIEW_NEEDED item asking the user whether to rename `…_QuickRef_12pp.pdf`.
3. **Accept when:**
   - The QuickRef pages' extracted text matches the binder's QS pages, apart from running heads.
   - There are 0 `??`.
   - `grep -rn "QR-[0-9]" src/*.tex` returns nothing.
   - pdfcheck passes.

**P4.3 Add a "level · time" tag and a boxed Answer line to every example.** Do one pass on the final set, after the Phase 5 cuts and the Phase 7 moves and retitles.
1. **Macros:** add these to `build/thermobinder.sty` and copy it to `src/`:
   - `\answer{…}`, which prints a boxed **Answer:** line;
   - `\TagWarmup`, `\TagStandard` and `\TagHard`, which print "Warm-up · 30 s", "Standard · 60 s" and "Hard · 2 min".
2. **Tag:**
   - Every `workedexample`'s second argument (the bracketed tag in the title bar) is exactly one of `\TagWarmup`, `\TagStandard` or `\TagHard`.
   - Choose by steps: 1–2 steps is Warm-up, 3–5 is Standard, 6 or more is Hard.
   - Remove "Tier n", "Basic/Competition/National" and source codes (MIT E3 Q24, Lienhard Ex 2.6, Cornell E1…) from title bars. A source may go in a small line at the end of the example.
3. **Answer line:**
   - Every example and every surviving problem ends with `\answer{…}`.
   - It holds the final result with SI units and correct significant figures, identical to the value already printed and checked.
4. **Accept when:** the source audit (T2) reports 0 examples without `\answer` and 0 tags other than the three tag macros, and verify_all passes.

**P4.4 Generate page counts from the `.aux` file.**
1. **Remove every hard-coded budget or page count:**
   - `markdown/README.md` ("248 Pages", "250 pp", the per-section targets);
   - the cover's "Budget" column (`\hdr{Budget}` in `src/frontmatter.tex`);
   - the "% Target Page Budget: N pages" / "% Target: N pages" comments at the top of the `src/sec*.tex` files;
   - comments in `src/main.tex`;
   - `build/architecture-lock.md` ("246–250" and its per-section page-budget column);
   - `SECTION_META` page targets and titles in `build/export_markdown.py`.
2. **Generate instead:**
   - Have `build.py` write a page-range table from the `main.aux` chapter labels on every build.
   - Regenerate the README section between marker comments from it.
   - In the binder itself, use `\pageref`.
3. **Accept when:**
   - `grep -rnE "248 Pages|250 pp|246–250|\\hdr\{Budget\}|Target( Page Budget)?: [0-9]+ pages" README.md markdown/README.md build/ src/*.tex` returns nothing. (Plain "budget" elsewhere, as in "Energy Budget", is fine.)
   - The per-section page-budget column in `build/architecture-lock.md` is gone.
   - The README page counts equal the built PDFs.

**P4.5 Match the Fig 15.1 and 15.2 stage angles to Table 15.5 (`tab:15:cpc-frustums`).** Do this together with the Phase 9 redraw. Earlier notes called this table "Table 15.3", which is wrong; Table 15.3 is the lamp table.
1. **The problem:**
   - The figures currently label 23.5°/29.7° and 23°/30°/15°.
   - The single source, Table 15.5, gives z/r coordinates and φ = 23.2°, 33.5°, 43.3°.
2. **Change:** redraw both figures from the Table 15.5 coordinates.
3. **Accept when:**
   - The labels print 23.2°, 33.5° and 43.3°.
   - The drawn slopes match within 0.5°.
   - A new check parses the figure coordinates.
   - The rendered figure shows no overlaps.

**P4.6 Remaining Phase 4 items.**
1. **Notation.** Use α_abs for absorptance in §12, §14 and App C; α_L for expansion is already done. Use τ_opt for transmittance; τ_NIR and τ_MIR become τ_opt,NIR and τ_opt,MIR. Define both in App C.
   - Accept when: there are no bare α or τ meaning absorptance or transmittance (grep, then review the hits).
2. **Rule boxes.** Audit every `rulebox`; it is for official rules and FAQs only. Move anything else to `shortcut` or `devicebox`.
   - Accept when: the T2 rule-box list holds only rules and FAQs.
3. **Section skeleton.** Each subsection follows: formula card → short explanation → worked example → trap box. Each section has at least one `shortcut`.
   - Accept when: the T2 source audit reports 0 sections missing a part.
4. **Problems.** Convert the §10–§13 `problem`/`solution` pairs that survive Phase 5 to `workedexample`, using one example format.
   - Accept when: 0 `problem` environments remain in the binder (the `practice/` packet may keep them).
5. **Labels.** Label every reference-collector number "Reference design (modeled), not our device", including §13 Ex 13.2 and the Device Handbook.
   - Accept when: each such example, table and figure carries the label or the banner.

### Phase 5. Cut and merge (about 40 pages)

This phase is where findability is won. The cut test for every block is: **"Does a first-timer need this during the event?"** If not, cut it, or move it to `practice/` or the repo README.

1. Do every row of the master prompt's Phase 5 table. Page numbers there refer to the 264-page baseline PDF.
   - The TOC becomes the tab map.
   - The cover rules wall moves to §0.1.
   - The four partner timelines become one event-day card.
   - The six scoring copies become §16.1 + QS-13 with one example.
   - The five FAQ restatements become pointers to §0.1.
   - §22 shrinks to a half-page "what tests ask" table.
   - Delete §21.4 and §21.5.
   - §19.4 shrinks to 3 lines.
   - §23.1, §23.2 and §23.4–23.5 go to the quick sheets; §23.3 goes to QS-14 + §3.4.
   - The App C formula, error and device indexes are cut (keep the topic index).
   - App H's build pipeline goes to the repo README; App G shrinks to the top 10 sources.
   - Table 4.1 and the §5 steam table move to App A.
   - The problem banks §10.7, §11.6, §12.5 and §13.6 keep 3 short problems each; move the rest to `practice/`.
   - The deep dives §8.6, §8.7, §9.7–9.8, §7.7, §15.3, §17.6 and §14.3 shrink to ½ page each.
   - The trap catalogs become one trap box per section + the §20.4 lookup.
   - Delete Ex 19.4.
   - Keep the 14 quick sheets.
2. Content moved to `practice/` keeps its checks. Delete a check only when its content is deleted, and log it.
3. Leave a `\pageref` pointer wherever a removed copy used to be. Never leave a dangling reference.
4. **Accept when:**
   - The binder is about 40 pages shorter than 264 (report the exact number).
   - 0 `??`.
   - 0 empty headings.
   - `practice/` compiles on its own.
   - verify_all passes.
   - Every cut is in the changelog.

### Phase 6. Reorganize and rename

This phase makes the binder findable: one tab map, plain words, and one home per formula.

1. Build the **one-page 9-tab map** at the front, using the master prompt's tab table, with the "How to use this binder" strip and box legend from F1 below.
2. Merge §21 into the Tab 1 event-day card. Move the §20 case studies to their home sections as trap examples.
3. Apply the **plain-language chapter and subsection titles** from the master prompt.
   - Accept when: the jargon audit (U1) reports 0.
4. **Formula homes**
   - Each formula group from the master prompt's table lives in full in one home section, with a short copy on its quick sheet.
   - Generate both from one macro per formula (e.g. `\EqCarnot`).
   - Accept when: F4 passes.
5. **App B** becomes a "find a variable → page" list with no equations. **The router (§0.3)** lists questions → page only (F2).
6. **Steam table.**
   - Make one App A table: saturation 0.01–200 °C (ideally to 374 °C) with P, v_f, v_g, h_f, h_fg, h_g, s_f, s_g, plus a superheated block at 0.1, 1 and 3 MPa.
   - Generate the values from an IAPWS-95 implementation (e.g. `pip install iapws` in the venv) and cite IAPWS-95/NIST.
   - Add a check that compares every printed value with the library.
   - Put the "how to use" box beside it.
   - Delete the §5 copy.
7. **Property lookup table** for about 20 materials: c, k, ε, ρ and α_L.
   - Take values only from tables already in the binder (App A, §4, §10, §12) or from a cited source.
   - Leave any unknown cell blank and log it in REVIEW_NEEDED.
   - Also add the α_L table in §3.3.
8. **Accept when:**
   - The tab map is one page.
   - Every chapter title matches the master prompt list.
   - Every formula group has exactly one home.
   - The steam-table checks pass.

### Phase 7. Speed

This phase puts the answer where the eye lands: the example sits next to its formula, warm-ups come first, and every figure says how to read it.

1. Move the examples next to their concept, following the master prompt lists for §2–§5, §10–§13 and §20. Cap each subsection at one spread.
2. Add the **24 warm-ups** from the master prompt table, placed before the long examples.
   - Each answer is recomputed and gets a check.
   - Accept when: all 24 are present with checks.
3. Retitle the listed jargon examples, and review every other title: it must say what is asked (U4).
4. Add the text items:
   - "How to read this:" under every figure (U5).
   - Quick-sheet pointer lines (U6).
   - 4-column formula cards (U3).
   - The "Definitions in one line each" half-page.
   - The "Everyday heat transfer" box.
   - The steam-table how-to.
   - The Zero-score list at the top of Tab 7.
   - The "Modeled for the reference collector. Replace with our measured runs." banner on the §16 tables and Figs 15.3, 15.5, 16.2 and 17.2. The banner already exists on Fig 17.2 and the reference table.
   - The QS-13 fill-in prediction card.
5. **Accept when:** the T2 counts for How-to-read, pointers and 4-column cards are all 0.

### Phase 8. Device packet

This phase gives one front door for the 20-point prediction, and every blank on it is a fill-in the team can use cold.

1. Build the **2-page "Our Device" packet** at the front of Tab 7. Its page contents are listed in the master prompt.
   - Page 1: `$\TpredFormula$`, the **blank** TG grid (40–65 cm × 10–15 min), the blank ΔT_cool box and the fill-in card.
   - Page 2: the calibration protocol, the blank calibration chart, and **one** merged build-day checklist. The checklist includes tongs/hot pads and goggles-if-glass.
2. Fill in no numbers.
3. Move the reference-design tables (including `tab:16:reference-collector`) to an appendix example, clearly labeled.
4. **Accept when:**
   - The packet is exactly 2 pages.
   - The grids are empty.
   - The other checklists are replaced by pointers.
   - The reference tables live only in the appendix.

### Phase 9. Figures

This phase makes every figure readable at a glance and in grayscale.

1. Add one global pgfplots style to `build/thermobinder.sty`:
   - `axis lines=left`, arrowheads (`axis line style={-stealth}`);
   - labels as "quantity [unit]";
   - legends outside the plot or direct labels;
   - line style and markers that differ (never color alone).
2. Add V units to the Otto, Diesel and Brayton P–V plots, and direction arrows to every cycle.
3. Un-pile labels.
   - Highest priority: Figs 0.2, 2.1, 3.3, 10.1, 15.1, 15.2, 19.1, 21.1.
   - Then the crowded list in the master prompt.
4. Add the listed figures and the 4×4 cm thumbnail on each quick sheet. Do P4.5 here.
5. **Accept when:**
   - Every figure page is rendered at 130 dpi or more (grayscale proof too) and inspected.
   - There are 0 overlapping or clipped labels and 0 color-only distinctions.
   - The Device Handbook is rebuilt and inspected after any §14–§16 figure change.

### Phase 10. Print and layout

This phase makes every page legible on paper without squinting.

1. **8 pt floor.**
   - Set `\tabfont` to `\small`.
   - Remove `\scriptsize`/`\tiny` from tables, `\src`, `\flag`, App A, B and C, §23, the router and the quick sheets.
   - Make room by dropping redundant and long note columns (e.g. Table 4.1's second c_p and "OS UP2" columns), not by adding pages.
2. **Floats.**
   - Fix §20 (`[H]` or `\captionof`), the orphan Table 4.2 caption, the near-empty pages, and short pages.
   - Accept when: 0 empty headings and 0 pages under 250 words except the listed blank forms.
3. **Grayscale.** Trap boxes stay distinguishable by border weight. Check the grayscale proof.
4. **Cover:** the title plus the tab list only.
5. **Accept when:** the audit shows 0% of characters under 7.9 pt outside sub/superscripts.

### Phase 11. Rebuild, verify, report

This phase proves the first-timer test with evidence.

1. Run the full build plus the grayscale proof, `export_markdown.py` (residual macros = 0), `pdfcheck.py`, `verify_all.py` and the extended `audit_metrics.py`.
2. Re-render every figure page and 20 random pages (T3).
3. Run the speed trace and first-timer test (T1). The target is 30/30.
4. Update `README.md`, `markdown/README.md` and App H's revision line with the real page counts.
5. Deliverables and the final report are in section 9.

---

## 6. Cleanliness and first-timer usability

Every rule below is checkable. "Audit" means the extended `qa/audit_metrics.py` (T2). "Render" means a page image at 130 dpi or more that you have looked at.

### 6.1 Findability

**F1. Tab map page.** It is one page, at the front, right after the cover.
1. It contains the 9-tab table: tab, topics in plain words, sections, and the first page via `\pageref`.
2. It contains the strip **"How to use this binder: 1 Find your question in the router (§0.3, p. X) → 2 Go to that page → 3 Read the formula card → 4 Follow the worked example → 5 Check the trap box."**
3. It contains a **box legend**: a small sample of each box plus its purpose, with the visual cue named in words so it works in grayscale.

   | Box | Looks like | Purpose |
   |---|---|---|
   | formula card | navy frame, gray fill | formulas |
   | worked example | thin black frame, gray title bar | worked examples |
   | trap box | thick rust frame | common mistakes |
   | shortcut | teal frame, light fill | fast methods |
   | device box | thick left bar | our device |
   | rule box | navy frame, white fill | official rules and FAQs only |
   | tier box | amber frame | State/National-only scope |
   | derivation | gray left bar, no frame | optional background |
   | quick sheet | full page | detachable summary |

4. Check: the legend lists every box environment that the audit finds in use.

**F2. Router (§0.3).**
1. It lists plain-language student questions → page numbers via `\pageref`, and no formulas. Example: "Ice and hot water are mixed — what is the final temperature?" → p. X.
2. It covers all 30 speed-trace types; tag each entry with its type number in a comment.
3. It is at most 2 pages.
4. Check: `qa/speed_trace.csv` maps each type to a router entry, and every entry resolves.

**F3. Running heads.**
1. Every page head shows the tab number and the plain-language section title, e.g. "Tab 3 · Heat & Phases · §4 Specific Heat & Calorimetry".
2. Add the tab number through `\binderchapter`/`\binderapp` (an extra argument or a `\bindertab{n}` setter). Keep both copies of the `.sty` identical.
3. Check: the audit reads the head text on every page and finds `Tab [1-9]`, and no doubled "§n · §n".

**F4. One place per topic.**
1. Each topic and formula group has exactly one home.
2. Its quick-sheet copy is generated from the same macro.
3. Everywhere else gets a pointer ("see §4.3, p. X"), never a copy.
4. Check: a script counts each formula macro's uses and allows only the home plus its QS. The Phase 5 duplicates are confirmed gone.

**F5. Page pointers.**
1. Every page pointer uses `\pageref`/`\sref`, never a hard-coded number.
2. Check: 0 `p.~123`- or `pp. 225–228`-style literals in `src/` outside `\pageref`.
3. Check: 0 `??` in all four PDFs (pdfcheck P3 and the audit).

**F6. Index.**
1. The topic index covers every formula name, every symbol in App C, and common student words such as "specific heat", "c", "calorimeter", "latent heat", "R-value", "COP", "efficiency", "steam table", "quality" and "lever rule".
2. Keep the list in `qa/index_terms.txt`: at least 150 terms, including the 30 speed-trace phrases.
3. Check: every term appears in the built topic index (`main-topic.ind` or the index pages).

### 6.2 Ease of use

**U1. Plain-language titles.**
1. Use the plain-language titles from the master prompt.
2. No heading, subsection or box title contains Paradigm, Atlas, Master, Championship, Locked or Ultra-Fast.
3. Check: the audit counts 0 in `src/` titles and in the PDF headings.

**U2. Symbols defined where used.**
1. Every symbol is defined, with SI units, where it is used: in the formula card's second column, and in each example's "Given" line.
2. Check: the review during T3 finds no undefined symbol on 20 random formula pages.

**U3. One skeleton.**
1. Every subsection follows: **4-column formula card** → a 2-line explanation → a worked example → a trap box.
2. The 4-column card is **Equation | Symbols with SI units | Use when | Don't use when**, modeled on the §10 card.
3. Redefine the `ftab` environment (currently Formula | Variables | Flags | Use when; 25 cards, 166 rows) to the new four columns, and convert the other 67 `formulacard` boxes to it.
4. "Don't use when" examples:
   - Q = mcΔT: not across a phase change.
   - PV^γ: reversible adiabatic only.
   - η_C: reversible engines only, T in K.
   - Newton cooling: Bi < 0.1 only.
   - σT⁴: T in K; use T₁⁴ − T₂⁴.
5. Check: the audit reports 0 formula cards that are not 4-column, and 0 subsections missing a part of the skeleton.

**U4. Examples.**
1. Every example has a title that says what is asked (for example "Ice + warm water: not all the ice melts"). No jargon, and no "Template n:".
2. It has a `level · time` tag (P4.3).
3. It has numbered steps (Step 1, 2, 3…).
4. It ends with a boxed `\answer{}` line with units and correct significant figures.
5. Check: the audit reports 0 examples without `\answer`, 0 non-standard tags, and 0 examples without numbered steps.

**U5. Figures.**
1. Every figure caption has a bold **"How to read this:"** line. The master prompt gives examples.
2. No overlapping labels.
3. Legends sit outside the plot, or curves are labeled directly.
4. Line style or markers differ, so the figure reads correctly in grayscale.
5. Axes are arrowed, with "quantity [unit]" labels.
6. Check: the audit reports 0 captions without "How to read", and T3 renders show 0 overlaps.

**U6. Quick sheets.**
1. Each of the 14 sheets is exactly one page.
2. Each starts with **"Full explanation: §x p.y · Example: p.z · Traps: p.w"**, printed by one macro (e.g. `\QSPointers{sec-label}{ex-label}{trap-label}`) with `\pageref`.
3. Check: the audit reports 0 sheets without the pointer line, and each sheet starts on a new page and ends on the same page.

**U7. Detached pages work alone.**
1. Quick sheets and the device packet must be usable when removed from the binder: no "see above" or "previous page".
2. Check: grep the QS and packet sources for "above", "below" and "previous"; there must be 0 hits that point across pages.

### 6.3 Cleanliness

**C1. One box style per purpose**, as in the F1 legend.
1. `rulebox` holds only official rules and FAQs.
2. `tierbox` holds only tier scope.
3. `devicebox` holds only the device.
4. Check: the audit lists every box title by environment; review the list, which must contain 0 misfiled boxes.

**C2. No shouting.**
1. No ALL-CAPS runs in body text. A run is 3 or more consecutive words of 3 or more letters each, all in capitals. Exclude a whitelist of acronyms and symbols: SI, NIST, IAPWS, CODATA, ES, TS, PS, PE, TG, FS, FAQ, COP, NIR, MIR, IR, PET, LDPE, HDPE, BoPET, RTD, DOE, CPC, and any you add, which must be listed in the audit.
2. No exclamation marks in body text. Exclude math, monospace calculator code, and headers and footers.
3. Check: the audit reports 0 for both.

**C3. Bold is reserved for answers and key terms.**
1. No bold whole sentences.
2. Check: the audit reports bold characters at no more than 10% of body text on every page. Headings, box titles, table header rows and Answer lines are excluded. List any page over the limit and fix it.

**C4. No clutter.**
1. 0 duplicate tables or formulas (F4).
2. 0 pages under 250 words, except a named list of intentional blank forms kept in `qa/blank_forms.txt`.
3. 0 empty or orphan headings.
4. 0 overprinted labels (T3).

**C5. Units and decimals.**
1. Every quantity with a unit uses siunitx (`\SI`, `\si`, `\num`). Define siunitx units for °F, °R, °Rø and the like if needed.
2. Within a table column, and between an example's statement and its answer, use the same number of decimals.
3. Check: the audit counts 0 raw `^\circ\mathrm{C}` or `$^\circ$` in body text outside unit macros. Review decimals during T3.

**C6. Cut, don't shrink.**
1. No printed text under 8 pt except sub- and superscripts. Use no `\resizebox` that pushes text below 7.9 pt.
2. When something doesn't fit, cut it or move it (Phase 5 rules). Never reduce the font size or the spacing.
3. Check: the audit shows 0% of characters under 7.9 pt outside scripts.

**C7. Scope guard.**
1. Usability work means layout, navigation and wording. It is not new deep content.
2. Anything beyond the master prompt goes into `REVIEW_NEEDED.md` as a proposal, not into the binder.

### 6.4 Acceptance tests (run all three and report them)

**T1. First-timer test.** Covers all 30 speed-trace types.
1. Create `qa/speed_trace.csv` with the columns `type_no, type_name, router_label, formula_label, example_label`.
2. Create `qa/speed_trace.py`. It reads the page numbers of those labels from `main.aux`. For each type it reports **PASS** when all of these hold:
   - the router has an entry for the type;
   - the router's `\pageref` target page is in the same spread as both the formula card and a worked example for that type. A spread is the same page, or an even page plus the odd page after it.
   - the path is at most 3 hops: tab map → router → page.
   Otherwise it reports FORMULA-ONLY or FAIL.
3. Then do a manual check of 10 randomly chosen types on the rendered PDF. Look only at the cover, the tab map and the router, and record what you looked at and in which order.
4. Fix the failures and rerun until the result is 30/30.
5. Report the baseline (18 pass, 6 formula only, 6 fail) and the final result.

**T2. Extended audit.** Extend `qa/audit_metrics.py`.
1. Add a **PDF pass** over all four PDFs. Each count has a target of 0:
   1. pages containing `??`;
   2. literal `**`;
   3. `!` in body text (C2);
   4. ALL-CAPS runs (C2);
   5. figure captions without "How to read";
   6. characters under 7.9 pt outside scripts;
   7. empty headings;
   8. pages under 250 words, excluding the blank forms;
   9. pages over the bold limit (C3).
2. Add a **source pass** over `src/*.tex`. Each count has a target of 0:
   1. examples or problems without `\answer`;
   2. tags other than `\TagWarmup`, `\TagStandard` or `\TagHard`;
   3. formula cards that are not 4-column;
   4. quick sheets without the pointer macro;
   5. jargon words in titles (U1);
   6. hard-coded page numbers (F5);
   7. raw degree signs (C5);
   8. formula macros used outside their home and QS (F4).
3. Have the source pass also list every box title by environment (C1).
4. The required counts, each with a target of 0, are:
   - `??`;
   - `**`;
   - exclamation marks;
   - ALL-CAPS runs;
   - figures without "How to read";
   - examples without an Answer line;
   - formula cards without 4 columns;
   - quick sheets without pointers.

**T3. Render review.**
1. Render every figure page, plus 20 random pages, at 130 dpi or more, from both the color and the grayscale PDFs. Choose the random pages with a fixed seed and list them.
2. Inspect them for clutter, overlapping or clipped labels, grayscale problems, undefined symbols and inconsistent decimals.
3. Fix what you find and re-render.

---

## 7. Gotchas

1. **The style file.** `build/thermobinder.sty` is the master copy. `build.py` (`sync_style_files`) copies it over `src/thermobinder.sty` on every build. Edit `build/`, copy to `src/`, and keep the two byte-identical.
2. **Printed numbers in the earlier notes.** `OVERHAUL_STATUS.md`, `CHANGELOG_OVERHAUL.md` and `REVIEW_NEEDED.md` sometimes give wrong printed numbers. Go by the labels:
   - the depth-profile figure is **Fig 15.5** (`fig:15:stratification-profile`), not 15.6;
   - the reflector fabrication table is **Table 15.5** (`tab:15:cpc-frustums`), not 15.3;
   - the removed eight-layer table was Table 15.9, not 15.6;
   - the reference-collector table is Table 16.5 (`tab:16:reference-collector`).
   Correct these notes when you next update them.
3. **Example numbering.** Example labels differ from the printed example numbers in §1, §8.6–8.8, §15 after 15.1 and §16 after 16.2; for example `ex:15.4` prints as Example 15.6. Always use `\ref`. The changelog cites labels, with the printed number in brackets.
4. **Check tolerance.** A check's tolerance is half a unit of the last printed digit. `chk(id, sec, desc, "printed-string", computed)` in `check_examples_recomputed.py` derives it from the string. Displayed arithmetic on rounded intermediate values is left as printed; those cases are noted in the changelog.
5. **Font sizes.** TeX's 8 pt prints as 7.97 pt in PyMuPDF, so the audit counts text under 7.9 pt.
6. **`\o` works only in text mode.** In math it is silently dropped (Rømer once printed as °R). Use `\text{R\o}`.
7. **The two device models are kept on purpose** (REVIEW_NEEDED A1/A2). Do not merge them by inventing data.
8. **Narrow table columns.** Long text in a non-wrapping `l` column makes tabularx collapse its X columns ("X Columns too narrow"), which produced hundreds of overfull boxes once. Keep table cells short ("FAQ 10/22"), and grep every build log for `X Columns too narrow`.
9. **pdfcheck hard-codes three things.** P5 expects the footer date `2026-11-22` (`\binderfooterlabel` in the `.sty`). P2 expects the QuickRef to have exactly 12 pages and the binder at most 280. If you change the footer date or the QuickRef page count, update `qa/pdfcheck.py` in the same commit.
10. **`build/export_markdown.py` hard-codes titles and page targets** in `SECTION_META`. Update it when you rename chapters (Phase 6) and when you remove budgets (P4.4).
11. **pgfplots helper lines need `forget plot`**, or they take the first legend entry and shift every label.
12. **The Device Handbook can build to a 0-page PDF on the first run**, with no error. Rerun it.
13. **Draft compiles of a few sections show `??`.** That is expected; only the full build resolves cross-references and indices.
14. **Edit LaTeX with Python string replacements that assert an exact match count**, not with `sed`, whose escaping of backslashes is error-prone. In zsh, `echo` mangles backslashes; use `printf`.
15. **soinc.org.** The FAQ page is `https://www.soinc.org/thermodynamics-div-c`; the older event URLs return 404. The Rules Manual is not online.
16. **`workedexample` arguments.** The signature is `\begin{workedexample}[Title]{tag}{label}`, and the tag prints in the title bar. A `problem` takes 8 arguments: id, title, section, rules, level, time, method, trap.

---

## 8. Working method

1. Work one phase at a time, in the order of section 5, and commit at the end of each phase on `binder-overhaul`. Use a clear message, and split large phases into numbered parts.
2. Log every change in `CHANGELOG_OVERHAUL.md` as file, old → new, reason. Put cuts, moves and renames in it too.
3. Run `verify/verify_all.py` after every number change. Never commit with `failed` above 0.
4. After any figure change, render its page at 130 dpi or more and look at it.
5. Rebuild the Device Handbook (`--target device`) whenever a §14–§16 figure or table changes, and look at it.
6. Run `qa/audit_metrics.py --label phaseN` at the end of each phase. Put the key counts in the commit message.
7. Update `OVERHAUL_STATUS.md` (done with commit hashes, left, gotchas) at the end of each phase, so the next person can resume.
8. When you are blocked on a human decision or an unreadable source, add an entry to `REVIEW_NEEDED.md` and move on.

---

## 9. Phase 11 deliverables and final report

1. Commit these on `binder-overhaul`:
   - the final `CHANGELOG_OVERHAUL.md` (every change);
   - the updated `REVIEW_NEEDED.md` (rule items to confirm in the manual, the C_eff decision, anything you could not verify, and the QuickRef filename question);
   - the updated `OVERHAUL_STATUS.md`;
   - the regenerated `output/`, `qa/renders/` and `markdown/`, in this final commit only.
2. Write the final report in `docs/OVERHAUL_REPORT.md` and show it to the user. It contains:
   1. Page count before and after, for each of the four PDFs (baseline 264 / 264 / 12 / 46).
   2. Share of text under 8 pt, before (26.3%; 18.6% excluding scripts) and after.
   3. The number of examples recomputed (Phase 2 recomputed 163 + 38; add the ones recomputed after it).
   4. Figures fixed and figures added, with lists.
   5. The speed-trace pass count (baseline 18/6/6) and the final result per type.
   6. The first-timer test (T1) results, including the manual spot-check notes.
   7. The new cleanliness audit counts (T2), each with its target of 0.
   8. The "Done means" checklist from the master prompt, each item marked pass or fail with evidence:
      - 0 characters under 8 pt outside sub/superscripts
      - 0 literal `**`
      - 0 empty headings
      - 0 pages under 250 words except intentional blank forms
      - every figure has a "How to read this" line
      - every formula card has 4 columns
      - every quick sheet has page pointers
      - every example has an Answer line

**Speed-trace question types (copied from the master prompt):**

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
