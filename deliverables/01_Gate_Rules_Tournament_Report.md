# Deliverable 01: Consolidated Gate 0, Official 2027 Rules & Tournament Reconnaissance Report

**Event:** Science Olympiad Division C — **Thermodynamics** (`2026–2027` Competition Season / `"2027 Rules"`)  
**Verification & Access Date:** `2026-11-22`  
**Gate 0 Verdict:** **`PASS` (100% Tier-1 Primary Verification Achieved)**  
**Contributing Research Modules:**
- **Gate 0 & Phase 1 Rules Verification (`@gate0-rules`):** `research/phase1_rules_extract.md`, `deliverables/02_Rules_Compliance_Matrix.md`
- **Gate 0 Workspace & Toolchain Audit (`@workspace-audit`):** `build/toolchain_smoke_spec.md`, `build/thermobinder.sty`, `build/build.py`, `qa/pdfcheck.py`
- **Phase 2 Tournament & Past-Exam Reconnaissance (`@exam-recon`):** `research/phase2_exam_corpus.md`, `deliverables/07_Tournament_Intelligence_Report.md`

---

## 1. Executive Summary & Gate 0 Verdict (`PASS`)

1. **Licensed 2027 Division C Rules Manual Verified in Workspace:**
   - Located at `C:\science olympiad\Circuit-Lab-Binder\research\official-2027-C.pdf` (`10,572,049 bytes`, `84 PDF pages`, created `2026-09-02` via Adobe InDesign 21.4, *Division C Rules Manual, Division C (Gr. 9–12), SCIENCE OLYMPIAD, INC. © 2027*).
   - **Thermodynamics C** occupies **Manual pp. C57–C59 (PDF pp. 62–64)**, supplemented by **General Rules (`p. C1`, PDF p. 6)**, **Event Type Descriptions (`p. C2`, PDF p. 7)**, **Div. C Chemistry Lab Equipment List (`p. C73`, PDF p. 78)**, **Calculator Class Descriptions (`p. C74`, PDF p. 79)**, **Eye Protection Guide (`p. C75`, PDF p. 80)**, and the **2027 National Tournament Division C Schedule (`p. C78`, PDF p. 83 — May 14–15, 2027 at The Ohio State University, Columbus, OH)**.
2. **Complete Live `soinc.org` Verification (`2026-11-22`):**
   - Directly fetched and verified **28 official `soinc.org` pages, national scoresheets, checklists, supervisor guides, and policy PDFs** (Section 2 below), confirming:
     - **0 Official 2027 Rules Corrections** for Thermodynamics B or C as of `2026-11-22` (`/events/rules-corrections`).
     - **9 Active Official 2027 National Rules Clarifications** for Thermodynamics Div C (`/division-c-events` → `/thermodynamics-div-c`, dated `09/30/2026` through `10/28/2026`).
     - **Official 2027 National Team Checklist (`2027ThermodynamicsBC_checklist.pdf`, updated `10/20/2026`)** and **Official v2.0.0 Excel Scoresheet (`2027ThermodynamicsBC_scoresheet.xlsx`, updated `11/06/2026`)**.
     - **Official 2027 Event Supervisor Device Testing Guide** (`1izXVwchASL-3TPaCihmZ_AB0AqRL8Bc13LT9bwJnLwA`) and **2027 Event Logistics Resource Sheet** (`1hEm1Edn2m_0c5-hAFRr8PufZR1N6PDGr`).
3. **Critical 2027 Device Paradigm Shift Confirmed:**
   - Unlike the historical `2018–2019` event (which tested a passive **insulating box holding a beaker of pre-heated hot water** and included a 10-point Plot Score for 4 cooling curves), **2027 Thermodynamics B/C** tests a pre-built **heat-collecting device** placed under an Event Supervisor-provided **100–125 W untinted incandescent/IR heat lamp bulb** (mounted facing down at **$40\text{–}65\text{ cm}$** height above the Testing Surface) for **$10\text{–}15\text{ minutes}$** to heat **$100\text{ mL}$ of room-temperature water** inside an ES-provided **9 oz clear plastic party cup** within a **$30.0\text{ cm} \times 30.0\text{ cm} \times 30.0\text{ cm}$** cubic envelope.
   - The 10-point Plot Score is **eliminated** in 2027: $\text{Final Score (100 pts)} = \text{Exam Score (ES, 50 pts)} + \text{Temperature Score (TS, 30 pts)} + \text{Prediction Score (PS, 20 pts)}$.
4. **Real-Season 2026–2027 Tournament Baseline Established:**
   - Anchored by the newly released **2026–2027 Cornell University Invitational Division C Thermodynamics Exam, Answer Key, Image Sheet, and 55-Team Raw Score Histogram (`E1`, held `2026-11-14`, histogram published `2026-11-19`)**, within an $N = 8$ Division C exam corpus (`217` numbered questions, `328` graded subparts, `1,120.0` total raw points).

---

## 2. Master Verification Table of Official Web Sources (`2026-11-22`)

| # | Source URL | Final Resolved URL | HTTP Status | Access Date | Tier | Distinctive Verbatim Datum Proving Direct Access |
|---|---|---|---|---|---|---|
| 1 | `https://www.soinc.org/thermodynamics-c` | `https://www.soinc.org/thermodynamics-c` | `200` | `2026-11-22` | **Tier 1** | `"Welcome to Thermodynamics! In this event, teams will construct a device prior to the tournament designed to collect heat and complete a written test on thermodynamic concepts."` |
| 2 | `https://www.soinc.org/thermodynamics-b` | `https://www.soinc.org/thermodynamics-b` | `200` | `2026-11-22` | **Tier 1** | `"Event Supervisor Resources ... New - Thermo Event Supervisor Resource ... New - Event Logistics Resource Sheet"` |
| 3 | `https://www.soinc.org/rules-2027` | `https://www.soinc.org/rules-2027` | `200` | `2026-11-22` | **Tier 1** | `"Starting Tuesday, September 8, 2026 at 9:00am Central Time, you can click the links below to enter your information to receive your PDF via a valid email."` |
| 4 | `https://www.soinc.org/events/2027-event-table` | `https://www.soinc.org/events/2027-event-table` | `200` | `2026-11-22` | **Tier 1** | Lists `"Thermodynamics"` under `"Physical Science & Chemistry"` in both `"2027 B Events"` and `"2027 C Events"`. |
| 5 | `https://www.soinc.org/events/2027-division-c-events` | `https://www.soinc.org/events/2027-division-c-events` | `200` | `2026-11-22` | **Tier 1** | `"2027 Division C Events ... Physical Science & Chemistry: Chemistry Lab, Circuit Lab, Forensics, Hovercraft, Protein Modeling, Thermodynamics"` |
| 6 | `https://www.soinc.org/learn/c-event-short-descriptions` | `https://www.soinc.org/learn/c-event-short-descriptions` | `200` | `2026-11-22` | **Tier 1** | `"Thermodynamics: Teams will construct a device prior to the tournament designed to collect heat and complete a written test on thermodynamic concepts."` |
| 7 | `https://www.soinc.org/rules-corrections-rules-clarifications` | `https://www.soinc.org/rules-corrections-rules-clarifications` | `200` | `2026-11-22` | **Tier 1** | `"Rules Clarifications provide additional explanation or interpretation of existing rules and are posted on the FAQ/Submit a Question page."` |
| 8 | `https://www.soinc.org/events/rules-corrections` | `https://www.soinc.org/events/rules-corrections` | `200` | `2026-11-22` | **Tier 1** | `"2027 Science Olympiad Official Rules Corrections"` — lists only 6 items (`Anatomy and Physiology B`, `Elastic Launched Glider B`, `Mission Possible C`, `Water Quality B`, `Water Quality C`, `Junkyard Challenge C`). **0 corrections for Thermodynamics B/C.** |
| 9 | `https://www.soinc.org/events/submit-question-and-rule-clarifications` | `https://www.soinc.org/events/submit-question-and-rule-clarifications` | `200` | `2026-11-22` | **Tier 1** | `"The Submit a Question System for the 2027 season is now OPEN! ... Division B Event Rule Clarifications | Division C Event Rule Clarifications"` |
| 10 | `https://www.soinc.org/division_c_events` | `https://www.soinc.org/division-c-events` | `200` | `2026-11-22` | **Tier 1** | Contains full Drupal `<nav class="booknav">` FAQ tree including `/thermodynamics-div-c` with **9 active 2027 official Rule Clarifications** (`09/30/2026` to `10/28/2026`). |
| 11 | `https://www.soinc.org/scoresheets` | `https://www.soinc.org/scoresheets` | `200` | `2026-11-22` | **Tier 1** | `"Thermodynamics (Divisions B and C): Scoresheet - updated 10/20/26 | Checklist - updated 10/20/26"` |
| 12 | `https://github.com/Southern-Califonia-Science-Olympiad/scoresheets/releases/latest/download/2027ThermodynamicsBC_checklist.pdf` | `https://release-assets.githubusercontent.com/.../2027ThermodynamicsBC_checklist.pdf` | `200` | `2026-11-22` | **Tier 1** | `"THERMODYNAMICS B/C Team Checklist – 2027 © SCIENCE OLYMPIAD INC. ... 3.c. A 9 oz disposable plastic party cup is able to be inserted and removed within the device."` |
| 13 | `https://github.com/Southern-Califonia-Science-Olympiad/scoresheets/releases/latest/download/2027ThermodynamicsBC_scoresheet.xlsx` | `https://release-assets.githubusercontent.com/.../2027ThermodynamicsBC_scoresheet.xlsx` | `200` | `2026-11-22` | **Tier 1** | `"Thermodynamics B/C Event Scoresheet - 2027 | Last Updated: 11/06/2026 (v2.0.0) Direct all questions to scoresheets@soinc.org."` |
| 14 | `https://drive.google.com/file/d/1hEm1Edn2m_0c5-hAFRr8PufZR1N6PDGr/view?usp=sharing` | `https://drive.usercontent.google.com/download?id=1hEm1Edn2m_0c5-hAFRr8PufZR1N6PDGr&export=download` | `200` | `2026-11-22` | **Tier 1** | `"100-125 watt heat lamp bulb (Not tinted and not LED, halogen, or ceramic) | 1 cup - 9 oz (For 100 mL of water from source water bath; 3.9-4 inches tall w/ 2.9-3.0 inch mouth)"` |
| 15 | `https://docs.google.com/document/d/1izXVwchASL-3TPaCihmZ_AB0AqRL8Bc13LT9bwJnLwA/edit?usp=drive_link` | `https://doc-0o-4o-docstext.googleusercontent.com/export/...` | `200` | `2026-11-22` | **Tier 1** | `"THERMODYNAMICS DEVICE TESTING 2027 SUGGESTED SESSION SCHEDULE ... Specifically ask about asbestos, mineral wool, fiberglass, and polystyrene (styrofoam or plastic with a triangle recycling symbol with the number 6 and the letters PS)."` |
| 16 | `https://www.soinc.org/general-rules` | `https://www.soinc.org/general-rules` | `404` | `2026-11-22` | **Dead URL** | Confirmed `HTTP 404 Not Found`; replaced by `/join/policies` and `/code-ethics-general-rules`. |
| 17 | `https://www.soinc.org/join/policies` | `https://www.soinc.org/join/policies` | `200` | `2026-11-22` | **Tier 1** | Hub page for `"Policies & Guidelines"` linking to `/ethics_rules`, `/scoring_guidelines`, `/eye_protection`, `/building-and-tools-policy`, and policy PDFs. |
| 18 | `https://www.soinc.org/ethics_rules` | `https://www.soinc.org/code-ethics-general-rules` | `200` | `2026-11-22` | **Tier 1** | `"All Science Olympiad content (e.g., policies, requirements, clarifications, FAQs, etc. on soinc.org) must be treated as if it were included in the printed rules."` |
| 19 | `https://www.soinc.org/scoring_guidelines` | `https://www.soinc.org/scoring-guidelines` | `200` | `2026-11-22` | **Tier 1** | `"Officials are encouraged to apply the least restrictive penalty for rules infractions"` |
| 20 | `https://www.soinc.org/eye_protection` | `https://www.soinc.org/eye-protection` | `200` | `2026-11-22` | **Tier 1** | `"Water is not a hazardous liquid and its use does not require protective eyewear unless it is under pressure or substances that create a hazard are added."` |
| 21 | `https://www.soinc.org/building-and-tools-policy` | `https://www.soinc.org/building-and-tools-policy` | `200` | `2026-11-22` | **Tier 1** | `"One or more of a 15-member team must have constructed all pre-built devices presented for judging."` |
| 22 | `https://www.soinc.org/sites/default/files/uploaded_files/Calculator_Class_Descriptions.pdf` | `https://www.soinc.org/sites/default/files/uploaded_files/Calculator_Class_Descriptions.pdf` | `200` | `2026-11-22` | **Tier 1** | `"©2025-C72 ... Class III- Stand-alone, programmable, graphing calculators and stand-alone non-graphing, programmable calculators"` |
| 23 | `https://www.soinc.org/sites/default/files/uploaded_files/SO%20SIGNIFICANT%20FIGURES%20FINAL12-5-12.pdf` | `https://www.soinc.org/sites/default/files/uploaded_files/SO%20SIGNIFICANT%20FIGURES%20FINAL12-5-12.pdf` | `200` | `2026-11-22` | **Tier 1** | `"Science Olympiad Policy for Measuring and Recording Significant Figures ... The last digit (and only the last one) of a measurement should be an estimate"` |
| 24 | `https://www.soinc.org/sites/default/files/uploaded_files/Battery_Policy_SO_26_27.pdf` | `https://www.soinc.org/sites/default/files/uploaded_files/Battery_Policy_SO_26_27.pdf` | `200` | `2026-11-22` | **Tier 1** | `"Science Olympiad Battery Policy Revised September 2, 2026 ... prohibit the use of lithium-batteries in all participant-built devices"` |
| 25 | `https://www.soinc.org/sites/default/files/uploaded_files/MathGuidelines2022.pdf` | `https://www.soinc.org/sites/default/files/uploaded_files/MathGuidelines2022.pdf` | `200` | `2026-11-22` | **Tier 1** | `"Guidelines for Division C Mathematics ... Algebra II: ... Exponential and logarithmic functions"` |

---

## 3. Summary of Verified 2027 Division C Thermodynamics Rules & All 9 Official National Clarifications

### 3.1 Core 2027 Rule Parameters (`official-2027-C.pdf`, pp. C57–C59)
- **Format & Resources (`Section 1–2`):** Hybrid Event; up to **2 competitors**; **50 minutes**; **Impound: Yes** (only the device and spare parts are impounded, at room temperature); **up to two Class III calculators** usable during any part of the event; **unrestricted paper notes/resources of any size** from any source in binders/books/folders/sheet protectors/lamination with tabs/labels, and **pages may be separated or removed from containers** during the event (`2.c`); setup tools and prepared calculation graphs/tables are permitted and **not** impounded (`2.d`). **Eye Protection:** None required (`p. C57`).
- **Device Construction (`Section 3`):**
  - Collects heat from an ES-provided overhead heat lamp setup to raise the temperature of room-temperature water (`3.a`).
  - Must allow inserting and removing an ES-provided **9 oz clear plastic disposable party cup** ($\sim 3.9\text{–}4.0\text{ in}$ [$9.9\text{–}10.2\text{ cm}$] tall, $\sim 2.9\text{–}3.0\text{ in}$ [$7.4\text{–}7.6\text{ cm}$] mouth diameter) containing **$100\text{ mL}$ of room-temperature water** (`3.c`, `4.g`).
  - Device + cup of water must fit within a **$\mathbf{30.0\text{ cm} \times 30.0\text{ cm} \times 30.0\text{ cm}}$ cube** when set up for testing (`3.d`).
  - Device parts may extend inside the cup, but **no part of the device may contact the water**, and **nothing may be added to the water** (`3.e`).
  - **Prohibited Hazardous Materials (`3.b.i` & `3.b.iii`):** Asbestos, mineral wool, fiberglass, and **polystyrene (Styrofoam and `#6 PS` plastics)** per Official Clarification `10/22/2026`. Violation bars the device from setup/testing ($\text{TS} = \text{PS} = 0$; team competes in Part I only).
  - **Prohibited Components (`3.b.ii`):** Thermometers, probes, commercially available thermoses, coolers, or vacuum-sealed devices ($\times 0.7$ construction violation multiplier if unfixed).
  - **Prohibited Energy Sources (`3.f`):** No electrical components, battery-powered heaters, chemical reactions, or internal energy sources ($\text{TS} = \text{PS} = 0$; ES may require post-test disassembly).
- **Competition Area & Testing Sequence (`Section 4` & `Section 5.II`):**
  - **Lamp Setup (`4.a–d`):** Clamp lamp with metal reflector and **100–125 W untinted heat lamp bulb** (not LED, halogen, or ceramic), mounted facing straight down above the Testing Surface; lamp stand protrusions $\ge 15\text{ cm}$ from bulb center.
  - **Bulb Height (`4.c`, Testing Surface to bottommost point of bulb):** Regionals: **$40\text{–}50\text{ cm}$** ($5\text{ cm}$ increments); States: **$40\text{–}55\text{ cm}$** ($5\text{ cm}$ increments); Nationals: **$40\text{–}65\text{ cm}$** ($1\text{ cm}$ increments).
  - **Heating Time (`5.II.a`):** Regionals: **$10\text{ min}$**; States/Nationals: **$10\text{–}15\text{ min}$** ($1\text{ min}$ increments).
  - **Timeline (`5.II.b–g`):** Up to **3 min Device Setup Time** (lamp OFF; fix construction violations; no modifications allowed afterward except inserting/removing cup) $\to$ ES dispenses $100\text{ mL}$ water and measures $T_{\text{start}}$ to **$0.1\ ^\circ\text{C}$** $\to$ Up to **1 min Water Setup Time** (lamp OFF; insert cup) $\to$ **10–15 min Heating Time** (lamp ON; touching device/lamp gives $\text{TS}=\text{PS}=0$; team must submit $T_{\text{predicted}}$ in $^\circ\text{C}$ before Heating Time ends or $\text{PS}=0$) $\to$ **1 min Final Measurement** (lamp OFF; team removes cup completely from device and all device components/wraps; ES measures $T_{\text{final}}$ to $0.1\ ^\circ\text{C}$ with the same thermometer used for $T_{\text{start}}$).
- **Written Test Syllabus & Math Rules (`Section 5.I`):**
  - Metric units with appropriate significant figures unless requested otherwise (`5.I.b`).
  - At least **3 questions** from each area: `5.c.i` (systems, intensive/extensive, temperature, Zeroth Law, scales/conversions, heat units), `5.c.ii` (phases, phase transitions, phase diagrams, latent/sensible heat, ideal gas law), `5.c.iii` (heat transfer modes, thermal conductivity, heat capacity, specific heat), `5.c.iv` (processes: adiabatic/isothermal/isochoric/isobaric, cycles, engines, efficiency, First & Second Laws), `5.c.v` (contributions of **Kelvin, Joseph Black, Joule, Carnot, Planck, Clausius, Boltzmann, Maxwell**), plus State/National areas `5.c.vi` (radiant exitance, blackbody radiation, Stefan–Boltzmann law, Third Law) and `5.c.vii` (entropy and enthalpy).
  - **Math Constraint (`5.I.d`):** Arithmetic, ratios, exponents, absolute value (`5.d.i`), multi-step algebraic derivations (`5.d.ii`), geometry of common shapes (`5.d.iii`), and **"No questions may require the use of trigonometry or calculus"** (`5.d.iv`). Per `MathGuidelines2022.pdf` (p. 2), standard algebraic exponential and logarithmic functions ($\ln, \exp, x^\gamma$) are permitted in Division C.
- **Official Scoring (`Section 6` & `2027ThermodynamicsBC_scoresheet.xlsx` v2.0.0):**
  - All calculations in **$^\circ\text{C}$** (`6.b`). High score wins ($\max 100\text{ pts}$):
    $$\text{FS} = \text{ES} + \text{TS} + \text{PS}$$
    $$\text{ES} = 50 \times \frac{\text{Part I Score}}{\max \text{Part I Score}}, \quad \text{TS} = 30 \times M_{\text{pen}} \times \frac{\text{TG}}{\max \text{TG}}, \quad \text{PS} = 20 \times M_{\text{pen}} \times \frac{\text{PE}}{\max \text{PE}}$$
    where $\text{TG} = \max(0,\, T_{\text{final}} - T_{\text{start}})$, $\text{PE} = \max\!\left(0,\, 1 - \dfrac{|T_{\text{final}} - T_{\text{pred}}|}{T_{\text{final}}}\right)$, and $M_{\text{pen}} = (0.7)^{V_{\text{constr}}} \times (0.9)^{V_{\text{comp}}}$.
  - **Tiebreakers (`6.j`):** **1st: Best $\text{TS}$**; **2nd: Best $\text{ES}$**; **3rd: Preselected written test questions**.

### 3.2 All 9 Active Official 2027 National Rules Clarifications (`soinc.org/thermodynamics-div-c`)
1. **`09/30/2026` (`5.g`, L4):** Water **will not be stirred or swirled** before taking the temperature.
2. **`10/01/2026` (`5.g`, L1):** Students are **not allowed to swish the water around** in the cup prior to temperature measurement.
3. **`10/06/2026` (`5.g`, L2):** When removing the cup, the team **must not swirl, shake, or stir the cup** to equalize water temperatures.
4. **`10/06/2026` (`5.g`, L4):** While the local ES determines the uniform measuring protocol, it is officially recommended that the ES **measure the temperature of the top layer of water near the center of the cup**, inserting a probe only far enough to take an accurate measurement and no farther.
5. **`10/21/2026` (`5.d`, L2):** When placing the cup in the device, teams **may place something on or around the cup** (e.g., plastic cling wrap or foil), provided **no adhesives, tapes, or fasteners (rubber bands, clips) are applied or attached to the cup**, the cup's shape and structural integrity are not altered, and all wrap/components are completely removed from the cup before $T_{\text{final}}$ is measured (`5.II.g`).
6. **`10/22/2026` (`3.i` [`3.b.i`], L1):** **Polystyrene (including Styrofoam and plastics with recycling symbol `#6` and `PS`) is considered hazardous in high-heat situations and must not be used** (`3.b.i` violation $\implies$ device barred from setup/testing, $\text{TS}=\text{PS}=0$).
7. **`10/22/2026` (`5.b` [`5.II.b`], L5.2):** **Opening a reflector/lid to insert the cup and returning the lid to its original position** is part of the allowed `"inserting or removing the cup."`
8. **`10/22/2026` (`5.b` [`5.II.b`], L4):** Actions inherent to inserting the cup — such as **opening/closing a lid or door or altering the orientation/position of the device** — are **not considered `'modifying'` the device**.
9. **`10/28/2026` (`2.d`, L1):** **Devices not impounded incur one additional construction violation** ($\times 0.7$ multiplier to $\text{TS}$ and $\text{PS}$).

---

## 4. Phase 2 Tournament Reconnaissance Summary ($N = 8$ Division C Exams, `1,120.0` Points)

*(Full empirical tables and three-tier `OBSERVED` / `RECOMMENDED` / `SPECULATIVE` separation are detailed in `deliverables/07_Tournament_Intelligence_Report.md` and `research/phase2_exam_corpus.md`.)*

1. **Real-Season 2026–2027 Cornell Invitational Baseline (`E1`, `2026-11-14`, $n=55$ Teams, `238.0` Raw Points):**
   - **Topic Distribution on `E1`:** `5.c.ii` Phases/Phase Diagrams/Calorimetry/Gas Laws (**36.6%** of points, including `Al-Cu` and `Fe-C` binary phase diagrams, Ice III Clapeyron slope, and Regnault steam calorimetry), `5.c.iii` Heat Transfer & Transport (**20.6%**), `5.c.vii` Entropy/Enthalpy/Steam Tables (**18.9%**, including a 16-pt saturation steam-table construction problem designated `TB #1`), `5.c.vi` Blackbody Radiation & Third Law (**9.7%**), `5.c.iv` Processes & Cycles (**9.2%**), `5.c.i` Foundations (**4.2%**), `5.c.v` Scientists (**0.8%**).
   - **Score Normalization Reality on `E1` ($n=55$ teams):** Winning raw score was **`85.00 / 238.0` (`35.7%`)** $\to \text{ES} = 50.0\text{ pts}$ ($0.5882\text{ ES pts per raw point}$); median raw score was **`~38.5 / 238.0` (`16.2%`)** $\to \text{ES} \approx 22.6\text{ pts}$. Foundational `Tier 1` (`25.0 pts`) + Intermediate `Tier 2` (`65.0 pts`) items on `E1` summed to **`90.0` raw points**, exceeding the tournament-winning score (`85.00 pts`).
2. **Whole-Corpus Topic Weightings ($N=8$ Exams: `E1` Cornell 2027, `E2–E3` MIT 2019/2018, `E4–E5` Golden Gate 2019/2018, `E6` Cornell 2018, `E7–E8` UT Austin 2018/2019; `328` Items, `1,120.0` Points):**
   - `5.c.ii` (`23.1%` of points), `5.c.iv` (`20.1%`), `5.c.iii` (`15.9%`), `5.c.vii` (`14.4%` — tested on **8/8 [100%]** of exams), `5.c.i` (`13.8%`), `5.c.vi` (`6.6%` — tested on **6/8 [75%]** of exams), and `5.c.v` (`6.2%`).
   - **Prominent Limitation Note:** Because 7 of the 8 public exams (`E2–E8`) date from the 2018–2019 insulating-beaker rotation and each of the 4 host institutions (`Cornell`, `MIT`, `GGSO`, `UT Austin`) has $n=2$ exams ($<3$), all host tendencies are bounded by sample size and contrasted across the Research-University Invitational profile (`E1–E6`, $1,000.0\text{ pts}$) vs. the Standard Regional B/C profile (`E7–E8`, $120.0\text{ pts}$).
