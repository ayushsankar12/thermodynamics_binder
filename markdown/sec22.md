<!-- Source: src/sec22.tex | Tab: Tab 8: PROBLEMS | Target: 4 pp -->
# §22: Evidence-Based Tournament Intelligence {#sec:22}

> **[SCOPE: REQUIRED | Empirical Corpus E1–E8 (N=8 Exams, 328 Graded Items, 1,120.0 Raw Points)]**

This section synthesizes empirical tournament intelligence from **$N = 8$ legally public, unauthenticated Science Olympiad Division C Thermodynamics exams and official grading keys** (`217` numbered questions, `328` individually graded items/subparts, `1,120.0` total raw written points) accessed on `2026-11-22`  **[S25,S26,S27,S28,S29,S30,S31,S32]**. Every finding is tagged strictly as **[OBSERVED]** (directly counted from the accessed corpus), **[RECOMMENDED]** (actionable engineering/study priorities derived from observed frequencies + 2027 rules), or **[SPECULATIVE]** (falsifiable hypotheses regarding 2026–2027 test-writer adaptations).

## Corpus Inventory & Prominent Methodological Limitations

**Table:** **[OBSERVED]** Verified $N = 8$ Division C Thermodynamics Tournament Exam Corpus Inventory (`Accessed 2026-11-22`)  **[S25,S26,S27,S28,S29,S30,S31,S32]**.

| **ID** | **Tournament & Host Institution** | **Date** | **Rules Season** | **Qs** | **Items** | **Points** | **Format & Companion Artifacts Analyzed** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **`E1`** | **Cornell Univ. Invitational** (Div C) **[S25]** | `2026-11-14` | **2026–2027 (`2027`)** | 37 | 74 | **238.0** | 20 MC/Match/TF (44 pt) + 5 FRQs (194 pt); 31-p. key + $n=55$ team score histogram |
| **`E2`** | **MIT Invitational** (Div C) **[S26]** | `2019-01-12` | 2018–2019 (`2019`) | 30 | 68 | **220.0** | 5 multi-part Problems (145 pt) + 25 MC (75 pt); 12-p. rubric + top score $93.81 pts$ |
| **`E3`** | **MIT Invitational** (Div C) **[S27]** | `2018-01-20` | 2017–2018 (`2018`) | 24 | 37 | **168.0** | 16 MC (64 pt) + 8 multi-part Short Answer derivations (104 pt); 12-p. key |
| **`E4`** | **Golden Gate Inv. (UCB/Stanford)** **[S28]** | `2019-01-17` | 2018–2019 (`2019`) | 14 | 32 | **189.0** | 25-min station sprint; 14 multi-part FRQs; 5-p. partial-credit rubric |
| **`E5`** | **Golden Gate Inv. (UCB/Stanford)** **[S29]** | `2018-02-10` | 2017–2018 (`2018`) | 21 | 26 | **45.0** | 45-min written test (45 pts of 105 pts event total); DOCX key & scoresheet |
| **`E6`** | **Cornell Univ. Invitational** (Div C) **[S30]** | `2018-02-24` | 2017–2018 (`2018`) | 31 | 31 | **140.0** | Sec. I–V: 7 scale conv., 8 units, 3 heat exchangers, 7 Stirling cycle, 6 short calc |
| **`E7`** | **UT Austin (ATX) Invitational** (B/C) **[S31]** | `2018-10-27` | 2018–2019 (`2019`) | 30 | 30 | **60.0** | Standard Regional-style B/C packet: 4 conversions (8 pt) + 26 MC (52 pt) |
| **`E8`** | **UT Austin (ATX) Regional** (B/C) **[S32]** | `2019-03-02` | 2018–2019 (`2019`) | 30 | 30 | **60.0** | Official Spring Regional B/C packet: 4 conversions (8 pt) + 26 MC (52 pt) |
| **Sum** | **4 Hosts (`Cornell, MIT, GGSO, ATX`)** | `2018–2026` | **3 Seasons** | **217** | **328** | **1,120.0** | **6 Research-Univ. Exams ($1000.0 pts$) + 2 Standard B/C Exams ($120.0 pts$)** |

### [TRAP & DIAGNOSTIC: Prominent Corpus Limitations & Epistemic Boundary Conditions]
- **No Single Target Host Specified & $n=2$ Per-Host Sample Limit:** Each of the 4 host institutions in Table `tab:22:corpus` is represented by exactly $n=2$ exams (below the $N \ge 3$ threshold required to infer an idiosyncratic single-host habit). Rather than making unsupported “Host X always asks Y” claims, we separate the **Research-University Invitational profile (`E1–E6`, $n=6$, $1000.0 pts$)** from the **Standard Regional / B-C Packet profile (`E7–E8`, $n=2$, $120.0 pts$)**.
- **2018–2019 Historical Rotation Boundary vs. 2027 Heat-Lamp Collector Shift:** Seven of the 8 exams (`E2–E8`, $882.0 pts$) were written during the 2018–2019 cycle when Part II was an *insulating box holding a beaker of hot water* (with a 10-pt Plot Score). Only **1 exam (`E1`, Cornell Invitational, `2026-11-14`, $238.0 pts$)** comes from the active 2026–2027 season under the new **100–125 W heat-lamp collector** rules ($\mathrm{ES}=50, \mathrm{TS}=30, \mathrm{PS}=20$)  **[S01,S25]**.
- **Honest Non-Access of Gated / Anti-Bot / Paid Repositories:** Community test exchanges behind anti-bot proof-of-work challenges and forum checkout logins (`scioly.org/wiki/index.php/Test_Exchange`), authenticated client apps (`scio.ly`), and paid downloads (`store.soinc.org` \$12 Starter Pack) were not bypassed and are logged as inaccessible in §`app:G` and `deliverables/RESEARCH\_LOG.md`.

## `OBSERVED` Syllabus Clause Frequencies & Format/Difficulty Matrices

\centering

**Table:** **[OBSERVED]** Topic Distribution Mapped to 2027 Division C Syllabus Clauses `5.c.i–vii` Across All 8 Exams (`328` Items, `1,120.0` Points)  **[S01,S25,S26,S27,S28,S29,S30,S31,S32]**.

\footnotesize
\setlength{\tabcolsep}{3.0pt}
\renewcommand{\arraystretch}{1.13}

| **Clause** | **2027 Official Syllabus Scope (`Rule 5.I.c`)** | **Rule Tier** | **Items** | **Item %** | **Total Pts** | **Corpus %** | **2027 `E1` %** | **Reg. `E7–8` %** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **`5.c.i`** | Systems, intensive/extensive, Zeroth Law, 8 temp scales, heat units | All Levels | 62 | 18.9% | 154.0 | **13.8%** | 4.2% (10 pt) | **21.7%** (26 pt) |
| **`5.c.ii`** | Phases, phase diagrams, latent/sensible heat, Clapeyron, gas laws | All Levels | 78 | 23.8% | 259.0 | **23.1%** | **36.6%** (87 pt) | **23.3%** (28 pt) |
| **`5.c.iii`** | Heat transfer modes, conductivity $k$, specific/molar heat capacity | All Levels | 49 | 14.9% | 178.0 | **15.9%** | **20.6%** (49 pt) | 15.0% (18 pt) |
| **`5.c.iv`** | Processes (isochoric/isobaric/isothermal/adiabatic), cycles, 1st/2nd Laws | All Levels | 51 | 15.5% | 225.0 | **20.1%** | 9.2% (22 pt) | 10.0% (12 pt) |
| **`5.c.v`** | History of **8 named scientists** (`Kelvin..Maxwell`) + pioneers | All Levels | 28 | 8.5% | 69.0 | **6.2%** | 0.8% (2 pt) | 13.3% (16 pt) |
| **`5.c.vi`** | Radiant exitance, blackbody radiation, Stefan–Boltzmann, 3rd Law | State/Natl* | 18 | 5.5% | 74.0 | **6.6%** | 9.7% (23 pt) | 1.7% (2 pt) |
| **`5.c.vii`** | Entropy ($\Delta S, S_{\mathrm{gen}}$) & enthalpy ($\Delta H$), steam tables, $\Delta G$, exergy | State/Natl* | 42 | 12.8% | 161.0 | **14.4%** | **18.9%** (45 pt) | 15.0% (18 pt) |
| **Total** | **All 7 Clauses ($\ge 3$ questions/clause required by Rule `5.c`)** | — | **328** | **100.0%** | **1,120.0** | **100.0%** | **100%** (238 pt) | **100%** (120 pt) |

> **[Vector Figure: **[OBSERVED]** Pareto distribution of written exam point weights across the seven 2027 syllabus clauses `5.c.i–vii`, comparing the full 8-exam corpus ($1{,}120.0\text{ pts}$) against the November 14, 2026 Cornell University Invitational (`E1`, $238.0\text{ pts}$). Clauses marked with $*$ (`5.c.vi` and `5.c.vii`) are nominal State/National topics that appear on $100%$ of invitational exams. | Label: `fig:22:corpus-pareto`]**
> - **Diagram Annotations & Key Elements:** **Y-Axis:** Share of Written Exam Points (%) • **Legend:** Full 8-Exam Corpus ($1{,}120.0\text{ pts}$), 2027 Season Cornell `E1` ($238.0\text{ pts}$)

### Three Critical `OBSERVED` Laws from the Corpus
- **[OBSERVED]** **The ``Big Four'' Quantitative Dominance (`5.c.ii` + `5.c.iv` + `5.c.iii` + `5.c.vii` $= 73.5%$ of All Points; $85.3%$ on 2027 Cornell `E1`):** Phases/latent heat/gas laws (`5.c.ii`: $23.1%$ overall, $36.6%$ on `E1`), cycles/processes (`5.c.iv`: $20.1%$), heat transfer/calorimetry (`5.c.iii`: $15.9%$ overall, $20.6%$ on `E1`), and entropy/enthalpy/steam tables (`5.c.vii`: $14.4%$ overall, $18.9%$ on `E1`) account for **$823.0$ of $1{,}120.0$ corpus points ($73.5%$)** and **$203.0$ of $238.0$ points ($85.3%$)** on the 2026--2027 Cornell Invitational!
- **[OBSERVED]** **State/National Clauses (`5.c.vi--vii`) Are Universally Tested at Invitationals \& Regionals:** Even though Rule `5.c.vi` (blackbody radiation, Stefan--Boltzmann, 3rd Law) and Rule `5.c.vii` (entropy \& enthalpy) carry a *State and National Levels Only* label  **[S01]**, **8 of 8 exams ($100%$) tested `5.c.vii`** and **6 of 8 exams ($75%$, including the UT Austin Regional `E8`!) tested `5.c.vi`**. Together they represent **$21.0%$ of all corpus points ($235.0 pts$)** and **$28.6%$ of 2027 Cornell `E1` ($68.0 pts$)**.
- **[OBSERVED]** **Bimodal Format \& Difficulty Split Between University Invitationals (`E1--E6`) and Regional Packets (`E7--E8`):** As documented in Table `tab:22:fmt-hist`, multi-step derivations (`FMT-3`: $36.7%$ of corpus points) and Tier 3 separators ($41.1%$ of points on `E1--E6`) dominate university invitationals, whereas MCQ/short-conversion Tier 1 items ($65.0%$ of points on `E7--E8`) dominate standard regional tests.

\centering

**Table:** **[OBSERVED]** Left: Question Format & Difficulty Tier Distributions ($328\text{ items}, 1{,}120.0\text{ pts}$). Right: 2026–2027 Cornell Invitational (`E1`, `2026-11-14`) 55-Team Raw Score Histogram  **[S25]**.

\footnotesize
\setlength{\tabcolsep}{2.6pt}
\renewcommand{\arraystretch}{1.11}

| **Code / Tier** | **Format / Difficulty Category** | **Items** | **Pts** | **Pt %** |
| --- | --- | --- | --- | --- |
| `FMT-1` | Multiple Choice & True/False | 106 | 266.0 | 23.8% |
| `FMT-2` | Short Calc, Scale & Unit Conv. | 35 | 116.0 | 10.4% |
| `FMT-3` | **Multi-Step Calorim./Cycle/Deriv.** | **78** | **411.0** | **36.7%** |
| `FMT-4` | $PV/TS$/Phase/Blackbody Graphs | 43 | 137.0 | 12.2% |
| `FMT-5` | Exp. Apparatus & Steam Tables | 13 | 48.0 | 4.3% |
| `FMT-6` | History & Concept Matching | 53 | 142.0 | 12.7% |
| **Tier 1** | Foundational (Univ 20% / Reg 65%) | 125 | 278.0 | **24.8%** |
| **Tier 2** | Intermediate (Univ 39% / Reg 32%) | 121 | 427.0 | **38.1%** |
| **Tier 3** | Advanced Separator (Univ 41%) | 82 | 415.0 | **37.1%** |

| **`E1` Raw Bin ($/238$)** | **% Max** | **Teams** | **Cum. %** | **Scaled $\mathrm{ES}$ ($/50$)** |
| --- | --- | --- | --- | --- |
| $5.00\text{–}16.43$ | $2.1\text{–}6.9%$ | 5 | 9.1% | $2.9\text{–}9.7$ |
| $16.43\text{–}27.86$ | $6.9\text{–}11.7%$ | 3 | 14.5% | $9.7\text{–}16.4$ |
| **$27.86\text{–}39.29$ (Mode)** | $11.7\text{–}16.5%$ | **21** | **52.7%** | **$16.4\text{–}23.1$** |
| $39.29\text{–}50.71$ | $16.5\text{–}21.3%$ | 16 | 81.8% | $23.1\text{–}29.8$ |
| $50.71\text{–}62.14$ | $21.3\text{–}26.1%$ | 5 | 90.9% | $29.8\text{–}36.6$ |
| $62.14\text{–}73.57$ | $26.1\text{–}30.9%$ | 3 | 96.4% | $36.6\text{–}43.3$ |
| **$73.57\text{–}85.00$ (Top)** | $30.9\text{–}35.7%$ | **2** | **100.0%** | **$43.3\text{–}50.0$** |
| **Total Field:** $n=55\text{ teams}$ $\cdot$ **Median** $\approx 38.5 pts$ ($\mathrm{ES}=22.65 pts$) |  |  |  |  |
| **Tier 1 (25 pt) + Tier 2 (65 pt)** $= \mathbf{90.0 pts} > 85.00 pt$ Winning Score! |  |  |  |  |

### Worked Example — Cornell 2027 (`E1`) Histogram Normalization & Tier 1+2 Sufficiency Proof `[Empirical ROI]`

Using the official 2026--2027 Cornell Invitational score distribution (Table `tab:22:fmt-hist`, $N_{\mathrm{max}} = 238.0 pts$, winning raw score $R_{\max} = 85.00 pts$, median raw score $R_{\mathrm{med}} = 38.50 pts$)  **[S25]**:
**(a)** Verify the total competing team count $n$, the normalized Exam Score multiplier $(\text{ES pts per raw pt})$, and the normalized point deficit between the median team and 1st place.
**(b)** If a team skips all 34 Tier 3 items ($148.0 pts$) except for writing symbolic equations on 6 of them ($6 \times 1.5 pts = 9.0 pts$), and scores $88%$ on Tier 1 ($25.0 pts$) and Tier 2 ($65.0 pts$) items, what is their normalized Exam Score $\mathrm{ES}$?

**Solution.**
**(a) Team count, normalization factor, and median deficit:**

$$
n = 5 + 3 + 21 + 16 + 5 + 3 + 2 = \mathbf{55\text{ teams}}, \qquad
  \frac{\partial \mathrm{ES}}{\partial R} = \frac{50.0}{85.00} = \mathbf{0.58824 ES pts/raw pt}.
$$

The median team ($R_{\mathrm{med}} = 38.50 pts$) earns $\mathrm{ES}_{\mathrm{med}} = 50 \times (38.50 / 85.00) = 22.647 pts$, trailing the top written score ($50.00 pts$) by:

$$
\Delta\mathrm{ES}_{\mathrm{deficit}} = 50.000 - 22.647 = \mathbf{27.353 normalized tournament points}.
$$

**(b) Tier 1 + Tier 2 + Symbolic Partial-Credit Strategy:**
Scoring $88%$ on Tier 1 + Tier 2 ($0.88 \times 90.0 pts = 79.20 pts$) plus $9.0 pts$ of Tier 3 symbolic equations yields $R_{\mathrm{team}} = 79.20 + 9.00 = \mathbf{88.20 raw pts} > 85.00 pts$, setting the new tournament high score and earning **$\mathrm{ES} = 50.00 pts$**!

**✓ Verified by:** Independent Python script `check_sec21_23.py` (`SEC22_CORNELL2027_HISTOGRAM`): $n=55$, $\partial\mathrm{ES}/\partial R = 0.588235$, $\Delta\mathrm{ES}_{\mathrm{deficit}} = 27.35294\text{ pts}$.

## `RECOMMENDED` Priorities & `SPECULATIVE` 2026–2027 Forecasts

\centering

**Table:** **[RECOMMENDED]** High-ROI Binder Prioritization & Top-10 Rubric Trap Forensics Derived from `E1–E8`  **[S25,S26,S27,S28,S29,S30,S31,S32]**.

\footnotesize
\setlength{\tabcolsep}{3.0pt}
\renewcommand{\arraystretch}{1.12}

| **Rank** | ****[RECOMMENDED]** Priority & Corpus Weight** | **Observed Rubric Trap in `E1–E8` Answer Keys** | **Binder Countermeasure Locator** |
| --- | --- | --- | --- |
| **1** | **Multiphase Calorimetry & Phase Diagrams (`5.c.ii`: $23.1%$ / $36.6%$ `E1`)** | Assuming all ice melts or all steam condenses without checking plateau bounds (`E1 Q30d, E4 Q9a, E6 III.2`); omitting $L_v(T)$ Kirchhoff shift at $T < 100 °C$ (`E2 P3e TB#3`); binary alloy lever-rule inversion (`E1 Q10–14, Q30c`). | §`sec:04` 5-Zone Ledger, §`sec:05` Binary Eutectic Lever Rule, `QS-03`, `QS-04` |
| **2** | **Processes, Cycles & Non-Standard Axes (`5.c.iv`: $20.1%$)** | Flipping work sign $W_{\mathrm{by}}$ vs. $w_{\mathrm{on}}$ (`E4 Q13`: $-2 pts$/part); failing to spot that extensive work $W$ is uncomputable on a $P$–$T$ Carnot plot without $n$ or $V$ (`E2 P2b TB#4`); using $C_V$ instead of $C_P$ in isobaric work (`E3 MC5`). | §`sec:07` Process Atlas, §`sec:09` Cycle Coordinate Translator, `QS-06`, `QS-08` |
| **3** | **Conduction, Convection, Newton Heating & $C_v$ (`5.c.iii`: $15.9%$ / $20.6%$ `E1`)** | Omitting calorimeter $C_{\mathrm{cal}}$ (`E7 Q16`) or glass-bulb thermal expansion $\beta_{\mathrm{glass}}V_0\Delta T$ (`E1 Q26d TB#9`); confusing Rayleigh number $\mathrm{Ra}$ with radiation (`E1 Q17e`); forgetting 2D lattice equipartition has $4$ quadratic modes ($C_v = 2Nk_B$, `E1 Q35a TB#3`). | §`sec:04`, §`sec:06`, §`sec:10`–§`sec:13`, `QS-09`, `QS-10`, `QS-12` |
| **4** | **Steam Tables, Entropy, Enthalpy & Exergy (`5.c.vii`: $14.4%$ / $18.9%$ `E1`)** | Plugging gauge pressure instead of $P_{\mathrm{abs}} = P_{\mathrm{gauge}} + P_{\mathrm{atm}}$ into $Pv=RT$ and steam tables (`E1 Q27c, Q28 TB#1`); forgetting $h = u + Pv$ when only $u, P, v$ are tabulated (`E1 Q29a`); confusing $\eta_1 = W/Q_{\mathrm{in}}$ with exergy efficiency $\eta_2 = \eta_1/\eta_{\mathrm{Carnot}}$ (`E1 Q29c TB#8`). | §`sec:05`, §`sec:08`, §`sec:09`, §`app:A` NIST Steam Table, `QS-07` |
| **5** | **8-Scale Temp & Energy Unit Conversions (`5.c.i`: $18.9%$ of items)** | Adding $+273.15$ or $+32$ to temperature *intervals* $\Delta T$ (`E7 Q5, E8 Q5`); using °C instead of K in gas-law ratios (`E8 Q26`); missing historical scales (`°R, °De, °N, °Ré, °Rø`) or units (`ft$\cdot$lbf, CHU, erg, foe`) (`E1 Q8,22b, E4 Q2,5, E6 I–II`). | §`sec:02`, §`sec:03`, `QS-01` 8-Scale & Unit Matrix |
| **6** | **Blackbody Radiation, $T^4$ Cooling & 3rd Law (`5.c.vi`: $6.6%$ / $9.7%$ `E1`)** | Confusing hemispherical exitance $M = \sigma T^4$ with Lambertian directional radiance $L = \sigma T^4/\pi$ (`E1 Q36e`); failing to link quantum vibrational freeze-out ($\hbar\omega \gg k_B T \implies C_v \to 0$) to convergence of $S(T) = \int_0^T (C_v/T') dT'$ under the Third Law (`E1 Q35c–d`). | §`sec:08`, §`sec:12`, §`sec:13`, `QS-11` |

### Five `SPECULATIVE` Forward-Looking Hypotheses for 2026–2027 Exams
- **[SPECULATIVE]** **Hypothesis S1 (Part I Written Questions Modeling the 2027 Heat-Lamp Apparatus --- `5.c.iii, vi`):** Just as `E3 Q23` tested inverse-square solar irradiance and radiative equilibrium, expect 2027 invitationals, regionals, and states to test (a) Wien's peak $\lambda_{\max} = b / T_{\mathrm{fil}} \approx 1.21 µm$ for a $2400 K$ tungsten heat lamp, (b) geometric concentration ratio $C_{\mathrm{geom}} = A_{\mathrm{ap}} / A_{\mathrm{cup}} = 900 cm^2 / 44.2 cm^2 \approx 20.4\times$, and (c) exponential lumped-capacitance heating $T(t) = T_{\mathrm{ss}} - (T_{\mathrm{ss}} - T_{\mathrm{start}})e^{-t/\tau}$ (§`sec:13`, §`sec:15`).
- **[SPECULATIVE]** **Hypothesis S2 (Near-IR Surface Absorption \& Stable Thermal Stratification --- `Clarifications \#1--\#4`):** Because Official Clarifications \#1--\#4  **[S02]** mandate **zero stirring/swirling** and top-layer temperature measurement, expect conceptual and quantitative questions asking why top-down near-IR heating of water above $4 °C$ creates a **buoyantly stable stratified hot surface layer** ($\partial\rho/\partial z > 0$, $\mathrm{Ra} < 0$, suppressing Rayleigh--Bénard convection) whereas bottom heating drives vigorous convective mixing (§`sec:11`, §`sec:15`).
- **[SPECULATIVE]** **Hypothesis S3 (Open-Cup Evaporative Cooling vs.\ Vapor-Barrier Glazing Calorimetry --- `Clarification \#5`):** Following Clarification \#5 (permitting an unattached cling-wrap/BoPET cover) and Lienhard Example 11.11  **[S02,S12]**, expect calorimetry problems calculating the temperature penalty when $0.5\text{–}2.0 g$ of water evaporates from a $100 mL$ cup ($L_v \approx 2420 J/g$ at $35 °C \implies 3–12 °C$ temperature loss!).
- **[SPECULATIVE]** **Hypothesis S4 (Polymer Thermal Softening \& `\#6 PS` Hazard Physics --- `Clarification \#6`):** Following the `10/22/2026` ban on polystyrene (`\#6 PS`/Styrofoam) under heat lamps  **[S02]**, expect material-comparison problems contrasting polymer glass-transition temperatures ($T_g \approx 95 °C$ for PS vs.\ $T_m = 254 °C$ for BoPET Mylar and char-resistant cork/balsa/cardboard) and specular vs.\ diffuse reflectance of shiny vs.\ dull aluminum foil (§`sec:14`).
- **[SPECULATIVE]** **Hypothesis S5 (Strict Alignment of `5.c.v` History Questions with the 2027 8-Scientist List):** Because Rule `5.c.v` mandates at least 3 questions from the exact 8 named scientists (**Kelvin, Joseph Black, Joule, Carnot, Planck, Clausius, Boltzmann, Maxwell**)  **[S01]**, expect Regional and State exams to feature direct matching across all 8 figures---with increased weight on **Joseph Black** (latent vs.\ sensible heat, ice calorimetry) and **Max Planck** (blackbody law, $E=h\nu$, 3rd Law crystal entropy) alongside **Carnot, Clausius, Kelvin, and Boltzmann** (§`sec:03`, `QS-14`).

—
**See also:** §`sec:00` (Command Center), §`sec:03` (8 Named Scientists `5.c.v`), §`sec:14`–§`sec:16` (2027 Heat-Lamp Collector Engineering & Calibration), §`sec:20` (Misconceptions & Error Catalog), §`sec:21` (Exam Strategy & Partner Protocol), and §`sec:23` (Final Review / Cram Layer).
