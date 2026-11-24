<!-- Source: src/sec21.tex | Tab: Tab 8: PROBLEMS | Target: 5 pp -->
# §21: Exam Strategy, 50-Minute Timeline, Two-Partner Split & Device Setup/Water-Insertion Choreography {#sec:21}

> **[SCOPE: REQUIRED | 2027 Rules 1, 2.a–d, 5.I–II, 6.a–j (All Tournament Levels)]**

In 2027 Division C Thermodynamics, two competitors have approximately **50 minutes** to execute a high-precision **Part II Heat-Lamp Collector run** (50 pts: Temperature Score $\mathrm{TS} = 30 pts$ + Prediction Score $\mathrm{PS} = 20 pts$) while simultaneously solving a marathon **Part I Written Exam** ($\mathrm{ES} = 50 pts$)  **[S01,S04]**. Because both parts are normalized to the tournament-leading raw score, championship execution is governed by **point-per-minute return on investment (ROI)**, zero-penalty device choreography, and ruthless partner division of labor.

## Two-Minute Triage & The Cornell 2027 Normalization Law

### [FORMULA & DECISION CARD: 2027 Official Score Normalization & Marginal Point Value (**[2027-RULE]**)]

Under 2027 Rule `6.c–i` and the Official National Scoresheet (`v2.0.0`)  **[S01,S04]**, final tournament score $\mathrm{FS}$ ($\le 100.0 pts$) is:

$$
\begin{aligned}

  \mathrm{FS} = \mathrm{ES} + M_{\mathrm{pen}}\left(\mathrm{TS}_{\mathrm{raw}} + \mathrm{PS}_{\mathrm{raw}}\right), \qquad M_{\mathrm{pen}} = (0.7)^{V_{\mathrm{const}}}\,(0.9)^{V_{\mathrm{comp}}}
\end{aligned}
$$

where each component is normalized to the field maximum across all competing teams:

$$
\begin{aligned}

  \mathrm{ES} = 50\left(\frac{R_{\mathrm{exam}}}{R_{\mathrm{exam,\max}}}\right), \quad
  \mathrm{TS}_{\mathrm{raw}} = 30\left(\frac{\mathrm{TG}}{\mathrm{TG}_{\max}}\right), \quad
  \mathrm{PS}_{\mathrm{raw}} = 20\left(\frac{\mathrm{PE}}{\mathrm{PE}_{\max}}\right), \quad
  \mathrm{PE} = \max\!\left(0,\,1 - \frac{|T_f - T_{\mathrm{pred}}|}{T_f}\right)
\end{aligned}
$$

**Marginal Tournament Value of 1 Raw Exam Point vs. $1.0 °C$ of Device Gain/Error:**

$$
\begin{aligned}

  \frac{\partial \mathrm{FS}}{\partial R_{\mathrm{exam}}} = \frac{50}{R_{\mathrm{exam,\max}}}, \qquad
  \frac{\partial \mathrm{FS}}{\partial \mathrm{TG}} = \frac{30\,M_{\mathrm{pen}}}{\mathrm{TG}_{\max}}, \qquad
  \frac{\partial \mathrm{FS}}{\partial |\Delta T_{\mathrm{err}}|} \approx -\frac{20\,M_{\mathrm{pen}}}{T_f\,\mathrm{PE}_{\max}}
\end{aligned}
$$

### The Cornell 2027 Empirical Triage Law

At the November 14, 2026 Cornell University Invitational (`E1`, $n=55$ Division C teams, maximum possible raw written score $= 238.0 pts$)  **[S25]**, the **highest raw exam score in the entire 55-team field was $85.00 pts$ ($35.7\%$)**, while the median team scored only $\approx 38.5 pts$ ($16.2\%$, scaling to $\mathrm{ES} = 22.65 pts$). Crucially, the exam contained $25.0 pts$ of **Tier 1** (foundational 1-step) items and $65.0 pts$ of **Tier 2** (standard 2–3 step) items—totaling **$90.0 raw pts > 85.00 pts$**!
- **Strategic Corollary 1 (Never Get Trapped in a Tier 3 Tar Pit Early):** Any team that sweeps $90\%$ of Tier 1 and Tier 2 items ($\approx 81 raw pts$) plus partial-credit equations on Tier 3 items wins $\mathrm{ES} = 50.0 pts$, whereas a team that spends 25 minutes grinding through a single 40-point Tier 3 derivation (such as Drude transport or a 24-cell steam table) while leaving Tier 1–2 pages blank loses $15\text{--}25 normalized pts$.
- **Strategic Corollary 2 (Four-Pass Packet Sweep):** Execute every written exam in four disciplined passes:
- **Pass 0 ($t = 0\text{--}2 min$ — Packet Audit, Unstaple & Split):** Check total pages, total raw points, designated Tiebreaker (`TB`) questions, significant-figure instructions, and MCQ guessing rules. If the Event Supervisor permits unstapling (explicitly recommended on Cornell exams  **[S30]**), unstaple the test booklet and divide sheets between Partner A and Partner B by topic domain.
- **Pass 1 ($t = 2\text{--}14 min$ — Fast Tier 1 Harvest):** Sweep all 1-step multiple-choice (`FMT-1`), temperature/unit conversions (`FMT-2`), intensive/extensive classifications, process matchings, and 8-scientist (`5.c.v`) attributions using the detached §`sec:01` Quick Sheets (`QS-01`, `QS-06`, `QS-14`). Target throughput: $\ge 3.5 raw pts/min$.
- **Pass 2 ($t = 14\text{--}38 min$ — Tier 2 Core & Tiebreaker Priority Sweep):** Solve all designated **Tiebreaker (`TB`)** problems first, followed by standard calorimetry ledgers (`5.c.ii`), phase diagram / lever-rule readings (`5.c.ii`), 1D conduction / Newton heating / Stefan–Boltzmann radiation (`5.c.iii, vi`), Carnot/Stirling/Rankine cycle legs (`5.c.iv`), and $\Delta S / \Delta H / \Delta G$ calculations (`5.c.vii`).
- **Pass 3 ($t = 38\text{--}47 min$ — Tier 3 Symbolic Equation Harvest):** On remaining multi-part Tier 3 problems, write the **symbolic governing equation, variable definitions, and algebraic setup** on every blank subpart before computing numbers. University grading rubrics (`E1, E2, E4`) award **$40\%\text{--}60\%$ of subpart points for the symbolic equation alone**  **[S25,S26,S28]**.
  

## Synchronized 50-Minute Two-Partner Choreography & Device Transitions

Because Part II Device Testing occurs on a staggered supervisor schedule while Part I is underway (`Rule 5.II.f`: *“Teams may work on Part I during the Heating Time at the Event Supervisor's discretion”*)  **[S01,S05]**, the team must operate as an asymmetric two-core processor. **Partner A (Lead Theorist)** stays anchored to the written exam for all 50 minutes, while **Partner B (Lead Device Engineer)** handles the $\approx 6 min$ of active hands-on device operations and devotes the remaining **$\approx 44 min$** to written test sections `5.c.i, iii, v, vi`.

**Table:** Synchronized 50-Minute Partner A / Partner B Master Execution Timeline  **[S01,S02,S05]**.

| **Clock Window** | **Event Phase (**[2027-RULE]**)** | **Partner A (Lead Theorist: `5.c.ii, iv, vii`)** | **Partner B (Device Lead + `5.c.i, iii, v, vi`)** |
| --- | --- | --- | --- |
| **Pre-Block** (Impound) | Impound (`Rule 2.d, 3.g`) | Verifies both Class III calculators (`2.b`), pencils, erasers, and binder tabs; keeps binder & nomograms (not impounded!). | Impounds device & spare parts at room temp (`2.d`); verifies cube clearance ($\le 29.6 cm$) and zero `#6 PS` (`3.b.i`). |
| **$0{:}00\text{--}2{:}00$** | Block Start & Packet Triage (`5.II.a`) | Audits written test pages/rubric; marks all `TB` items; separates packet into Pile A (`5.c.ii, iv, vii`) and Pile B (`5.c.i, iii, v, vi`). | Records ES-announced bulb height $h$ ($40–65 cm$), Heating Time $t_{\mathrm{heat}}$ ($10–15 min$), $T_{\mathrm{room}}$, $T_{\mathrm{bath}}$, and wattage $P_{\mathrm{bulb}}$ ($100–125 W$). |
| **$2{:}00\text{--}5{:}00$** | **3-Min Device Setup** (`Rule 5.II.b`) | Solves Pile A Pass-1 items (phase diagram reading, gas law ratios, process identification, $\Delta H/\Delta S$ signs). | Sets device internal cradle to slot for height $h$; passes inspection; pre-computes $T_{\mathrm{pred}}$ base terms from §`sec:16` DOE table. |
| **$5{:}00\text{--}6{:}00$** | **1-Min Water Setup** (`Rule 5.II.c–d`) | Continues Pile A written solving uninterrupted; double-checks Partner B's $T_{\mathrm{pred}}$ addition if called. | Receives 9 oz cup w/ 100 mL water; logs $T_{\mathrm{start}}$ (to 0.1 °C); seats cup on 3-fin cradle ($\le 12 s$); lowers hood w/ unattached BoPET cap (`Clarif. #5,7,8`). |
| **$6{:}00\text{--}10{:}00$** | **Heating Window Pt. 1** (`Rule 5.II.e–f`) | Finishes Pile A Pass 1; begins high-point FRQs (steam tables, Rankine/Carnot cycles, multiphase calorimetry). | Computes $T_{\mathrm{pred}} = \mathrm{TG}_{\mathrm{tab}} + k_s T_{\mathrm{start}} + k_r T_{\mathrm{room}}$; cross-checks w/ Partner A; **submits $T_{\mathrm{pred}}$ (in °C) to ES at $t_{\mathrm{heat}} = 3 min$!** |
| **$10{:}00\text{--}15{:}30$** | **Heating Window Pt. 2** (`Rule 5.II.e–f`) | Deep FRQ solving on Pile A (`5.c.ii, iv, vii`); calls out 15-min checkpoint status. | Sweeps Pile B Pass 1: 8-scale temperature conversions (`QS-01`), energy units, intensive/extensive, and 8 scientists (`QS-14`). |
| **$15{:}30\text{--}17{:}00$** | **1-Min Final Measurement** (`Rule 5.II.g–i`) | Continues Pile A FRQs without pause (zero distraction during cup extraction). | At lamp-off, lifts hood straight up (removing BoPET cap), sets cup smoothly on Testing Surface **with zero swirl/tilt (`Clarif. #1–4`)** in $\le 8 s$; signs Part II data sheet. |
| **$17{:}00\text{--}30{:}00$** | Written Exam Core Sprint (Checkpoint 2) | Solves remaining Pile A Tier 2/3 problems (Clapeyron slope, binary eutectic lever rule, exergy destruction). | Solves Pile B Tier 2 problems: Fourier conduction networks (`QS-09`), Newton heating/cooling (`QS-12`), Stefan–Boltzmann (`QS-11`). |
| **$30{:}00\text{--}42{:}00$** | Joint FRQ & Tiebreaker Convergence (Checkpoint 3) | Partners swap unsolved subparts; Partner A attacks highest-weight remaining calculation tiebreakers (`TB #1–#5`). | Partner B writes symbolic governing equations on all remaining Tier 3 subparts and verifies unit conversions on Partner A's FRQs. |
| **$42{:}00\text{--}47{:}00$** | Partial-Credit & Carry-Forward Sweep (Checkpoint 4) | Fills in backup-table or assumed-value carry-forward steps on any incomplete multi-part chain. | Checks every MCQ bubble / answer box against the blank-vs-guessing rule; eliminates decoys on remaining MCQs. |
| **$47{:}00\text{--}50{:}00$** | Final Audit & Re-Assembly | Audits every numerical box on Pages 1–5 for **units, sig figs, and Kelvin vs. °C ratios**. | Audits Pages 6–10 for units/sig figs; verifies Team # and Name on every sheet; re-orders answer packet cleanly. |

### [2027 HEAT-COLLECTOR DEVICE & LAB: Critical 60-Second Cup Extraction Choreography (`Rule 5.II.g` & `Clarifications #1–#8`)]

- **T-Minus 30 s Before Heating Time Ends:** Partner B caps their pen, moves to the testing station (keeping hands $\ge 30 cm$ clear of the device and clamp lamp while the lamp is still on so `Rule 5.II.e` is never violated), and visually locates the corner lift grips of the upper reflector hood.
- **T-Plus 0 s (ES Turns Lamp Off):** Partner B lifts the upper reflector hood straight upward off its alignment dowels ($\approx 2 s$). Because the non-attached clear BoPET vapor-barrier film rests inside the upper hood throat (`Clarification #5`), lifting the hood automatically separates the vapor cover from the cup. *(If a separate gravity-resting film disc was placed on the cup rim, lift it off the cup first and set it inside the device!)*
- **T-Plus 3 s to 8 s (Vertical Lift Without Swirling):** Grasp the 9 oz clear plastic cup gently near its dry top rim with two fingers and lift it straight up and onto the Testing Surface beside the device in one smooth motion. **NEVER swirl, swish, shake, tilt, or tap the cup!** Under `Clarifications #1, #2, #3, and #4`  **[S02]**, the ES measures the **top water layer near the center of the cup** without stirring; preserving the hot near-IR stratified surface layer yields $1.3\times\text{--}1.8\times$ higher measured temperature gain $\mathrm{TG}$ than a mixed cup (§`sec:15`).

### Worked Example — Tournament Score Normalization & Penalty Cost Analysis `[2027 Rule 6.c–i]`

At a 55-team invitational modeled on Cornell 2027 (`E1`)  **[S25]**, the tournament maxima are $R_{\mathrm{exam,\max}} = 85.00 pts$ (out of $238$), $\mathrm{TG}_{\max} = 24.0 °C$, and $\mathrm{PE}_{\max} = 0.9960$. Team Alpha earns raw Part I score $R_{\mathrm{exam}} = 68.00 pts$, heats water from $T_{\mathrm{start}} = 22.0 °C$ to $T_f = 43.6 °C$, and submits prediction $T_{\mathrm{pred}} = 43.2 °C$ at $t_{\mathrm{heat}} = 3 min$.
**(a)** Compute Team Alpha's normalized scores $\mathrm{ES}, \mathrm{TS}, \mathrm{PS}$, and $\mathrm{FS}$ with zero violations.
**(b)** How many tournament points would Team Alpha lose if they forgot to impound their device (`Clarification #9`: $V_{\mathrm{const}} = 1 \implies M_{\mathrm{pen}} = 0.7$), and how many raw written exam points on `E1` would be required to make up that penalty?

**Solution.**
**(a) Zero-violation normalized scores:**

$$
\begin{aligned}
\mathrm{ES} &= 50 \times \frac{68.00}{85.00} = 40.000 pts, \qquad
  \mathrm{TG} = T_f - T_{\mathrm{start}} = 43.6 - 22.0 = 21.6 °C \implies \mathrm{TS} = 30 \times \frac{21.6}{24.0} = 27.000 pts \\
  \mathrm{PE} &= 1 - \frac{|43.6 - 43.2|}{43.6} = 1 - \frac{0.4}{43.6} = 0.990826 \implies \mathrm{PS} = 20 \times \frac{0.990826}{0.9960} = 19.8961 pts
\end{aligned}
$$

Summing via Eq. (`eq:21:fs`) with $M_{\mathrm{pen}} = 1.0$:

$$
\mathrm{FS}_{\mathrm{clean}} = 40.000 + 27.000 + 19.8961 = \mathbf{86.896 pts} \quad (\text{rounded to } 86.90 pts).
$$

**(b) Cost of 1 construction/impound violation ($M_{\mathrm{pen}} = 0.7$):**
Under Rule `6.h` and Clarification #9  **[S01,S02,S04]**, both $\mathrm{TS}$ and $\mathrm{PS}$ are multiplied by $0.7$:

$$
\mathrm{FS}_{\mathrm{pen}} = 40.000 + 0.7\left(27.000 + 19.8961\right) = 40.000 + 32.8273 = 72.827 pts \implies \Delta\mathrm{FS}_{\mathrm{lost}} = 86.8961 - 72.8273 = \mathbf{14.069 pts}.
$$

Because each raw written point on `E1` is worth $50/85.00 = 0.58824 ES pts$, recovering $14.069 pts$ on the written exam would require:

$$
\Delta R_{\mathrm{exam}} = \frac{14.0688}{50 / 85.00} = \mathbf{23.92 raw exam points} \quad (\text{more than an entire 20-point FRQ!}).
$$

**✓ Verified by:** Independent Python script `check_sec21_23.py` (`SEC21_SCORING_PENALTY_EXAMPLE`): $\mathrm{FS}_{\mathrm{clean}} = 86.89610$, $\Delta\mathrm{FS}_{\mathrm{lost}} = 14.06883\text{ pts}$.

## Tabletop Ergonomics, Detached Quick Sheets (Rule 2.c) & Dual Calculator Discipline

### [2027 OFFICIAL RULE / CLARIFICATION: Exploiting 2027 Rule 2.c (Removable Pages) & Rule 2.b (Two Class III Calculators)]
- **Rule `2.c` (Unrestricted Removable Notes):** *“Participants are responsible for organizing and containing their notes efficiently and may separate or remove pages from containers for use during any part of the event.”*  **[S01]** Unlike events that mandate keeping all pages locked inside closed binder rings, Thermodynamics competitors may place detached laminated Quick Sheets (`QS-01`..`QS-14`) and the §`sec:16` Calibration Nomogram flat across the table for zero-flip, $<3$-second visual lookup.
- **Rule `2.b` (Two Stand-Alone Class III Calculators):** Each team may bring **up to two Class III calculators** (programmable graphing or scientific calculators; no laptops/phones/tablets per `p. C74`) for use during **any part of the event**  **[S01,S06]**. Both partners must hold a dedicated calculator at all times.

> **[Vector Figure: Optimal two-partner tabletop layout exploiting 2027 Rule `2.c` (detachable quick sheets and nomograms) and Rule `2.b` (dual Class III calculators) to achieve $<5\text{-second}$ formula retrieval without ring-flipping congestion. | Label: `fig:21:workspace-layout`]**
> - **Diagram Annotations & Key Elements:** COMPETITION TABLETOP ERGONOMIC MAP (60 in $\times$ 30 in Desk — 2027 Rule 2.b & 2.c Detached-Sheet Configuration) • PARTNER A ZONE (Lead Theorist: 5.c.ii, iv, vii) • **Detached QS-03, 04** / Calorimetry, Phase / Diagrams & Lever Rule • **Detached QS-06, 07, 08** / Processes, Cycles, / $\Delta S, \Delta H, \Delta G$ & Steam • **Active Exam Pile A** / (FRQs on Phases, Gases, / Cycles, Steam Tables, Exergy) / + Scratch Work Sheet • **Calc #1** / (Class III) / Consts in / Regs `A–H` • **Main Binder Ring Spine (Tabs 3, 4, 8, 9 Open)** / Fast Backup Access to §4–§9 & App. A NIST Steam Tables • SHARED CENTER BRIDGE (Triage, Timer & Conversion Hub) • **Wristwatch / Timer + Master Answer Sheet & TB Checklist** / Checkpoints at $t = 15, 30, 42, 47\text{ min}$ $\cdot$ **$T_{\mathrm{pred}}$ Submitted by $t_{\mathrm{heat}}=3 min$!** • **Detached QS-01 & 05** / CODATA Constants, 8 Temp / Scales, Energy Units, $R$ • **Detached QS-14 & §0** / 8 Named Scientists (`5.c.v`) / + 10-Sec Equation Router • **Completed & Audited Exam PagesTray** / Stacked in Numerical Order $\cdot$ Checked for Units ($kJ/kg$ vs. $J/g$), / Significant Figures (3 vs. 4 digits), and Kelvin Ratios • PARTNER B ZONE (Device Lead + 5.c.i, iii, v, vi) • **Detached QS-13 & §16** / 2027 Collector DOE Table / & $T_{\mathrm{pred}}$ Nomogram (`2.d`) • **Detached QS-09..12** / Conduction, Convection, / Radiation & Transient $\tau$ • **Calc #2** / (Class III) / DOE Fit & / $\sigma, k_B, h$ • **Active Exam Pile B** / (Scales, Units, History, / Heat Transfer, Blackbody) / + Part II Prediction Sheet • **Device Setup Tools (`Rule 2.d`) & Secondary Binder** / Metric Ruler/Height Gauge (for 3-min Setup) + Tabs 5, 6, 7

### Dual Class III Calculator Pre-Load & Cross-Check Discipline (`Rule 2.b`)

Before entering the competition room, verify that both Class III calculators have fresh batteries, are set to **floating-point / scientific display** (never fixed-decimal truncation!), and have identical fundamental constants stored in memory registers  **[S01,S07]**:
- **Standard Register Map:** `R` $= 8.3144626$ ($J/mol/K$); `K` $= 1.380649×10^{-23}$ ($J/K$); `N` $= 6.02214076×10^{23}$ ($/mol$); `S` $= 5.6703744×10^{-8}$ ($\sigma$, $W/m^2/K^4$); `H` $= 6.62607015×10^{-34}$ ($J s$); `C` $= 2.99792458×10^{8}$ ($m/s$); `W` $= 4184.0$ ($c_w$, $J/kg/K$); `F` $= 333550$ ($L_f$, $J/kg$); `V` $= 2256400$ ($L_v$, $J/kg$); `P` $= 101325$ ($Pa$).
- **Mandatory Two-Calculator Verification on Critical Values:** Two numbers must **always** be punched independently on both calculators before submission: (1) the Part II Final Temperature Prediction $T_{\mathrm{pred}}$ (worth $20 pts$), and (2) the #1 Written Tiebreaker calculation (`TB #1`, worth $10–16 pts$ on university exams).

## Partial-Credit Harvesting, MCQ Guessing Mathematics & Tiebreaker Protocol

### Anatomy of University Invitational Grading Rubrics (`E1–E6`)

Direct forensic analysis of the official grading rubrics from Cornell (`E1, E6`), MIT (`E2, E3`), and Golden Gate (`E4, E5`)  **[S25,S26,S27,S28,S29,S30]** reveals four universal scoring laws:
- **Symbolic Formula Credit ($40\%\text{--}60\%$ of Subpart Points):** On `E1` (Cornell 2027), `E2` (MIT 2019), and `E4` (GGSO 2019), writing the symbolic governing equation (e.g., $Q_{\mathrm{steam}} = m_s h_{fg} + m_s c_p(120 - T_f) = m_w c_p(T_f - 20)$, or $P = \varepsilon\sigma A T^4$, or $\Delta S = m c\ln(T_f/T_i)$) earns **1 to 4 points immediately**, even if no final number is computed.
- **Carry-Forward (Error-Propagation) Protection ($100\%$ Credit on Downstream Parts):** Both `E1` (p. 1: *“Apply carry-forward credit when a student uses an earlier incorrect numerical value consistently with a valid later method”*) and `E4` (p. 1: *“Do not deduct any points for cascading errors”*) award **full credit** on parts (b)–(f) if you clearly state your carried-forward value from part (a) and show the symbolic equation! If you cannot solve part (a), **declare a physically reasonable placeholder value** (or use the exam's backup table, as in `E1 Q29`) and solve parts (b)–(f) for full credit.
- **Explicit Unit & Significant-Figure Deductions ($10\%\text{--}33\%$ Penalty):** On `E2` (MIT 2019), every 2-point final answer block awards $1.0 pt$ for the numerical value, $0.5 pt$ for exact significant figures (3 sig figs), and $0.5 pt$ for explicit units—meaning omitting units or writing 2 sig figs instead of 3 forfeits **$25\%\text{--}50\%$ of the answer points**!
- **MCQ Blank-Credit vs. All-or-Nothing Multi-Select Traps:** Always read the section header before guessing on multiple choice:

### Worked Example — Optimal MCQ Guessing Threshold Under Blank-Credit vs. All-or-Nothing Rules `[Game Theory]`

Compare two actual Multiple-Choice scoring rules from our corpus:
**(a) MIT 2019 (`E2`) Blank-Credit Rule:** 4 choices (`a–d`); $+3 pts$ correct, $+1 pt$ left blank, $0 pts$ wrong  **[S26]**. How many distractors must you eliminate before guessing beats leaving the question blank?
**(b) Cornell 2027 (`E1 Q8–Q9`) Select-All-That-Apply Rule:** 6 options (`A–F`); $+2 pts$ awarded *only* if every correct option and zero incorrect options are selected ($0 pts$ otherwise)  **[S25]**. If you verify 4 options with certainty and are $50/50$ uncertain on the remaining 2 options, what is your expected value?

**Solution.**
**(a) MIT 2019 ($+3 / +1 / 0$) Elimination Threshold:**
If $m \in \{0, 1, 2\}$ distractors are eliminated out of $4$ choices, $k = 4 - m$ equally likely choices remain, so the probability of guessing correctly is $p = 1/k$ and the expected value of guessing is $\mathbb{E}[\text{guess}] = 3/k$, compared against the guaranteed $\mathbb{E}[\text{blank}] = 1.00 pt$:
- $m = 0$ eliminated ($k = 4$ choices left): $\mathbb{E}[\text{guess}] = 3/4 = 0.75 pts < 1.00 pt \implies$ **LEAVE BLANK** (guessing loses $0.25 pts/question$!).
- $m = 1$ eliminated ($k = 3$ choices left): $\mathbb{E}[\text{guess}] = 3/3 = 1.00 pt = \mathbb{E}[\text{blank}] \implies$ **Break-even** (leave blank to minimize variance, or guess if trailing on tiebreakers).
- $m \ge 2$ eliminated ($k = 2$ choices left): $\mathbb{E}[\text{guess}] = 3/2 = \mathbf{1.50 pts} > 1.00 pt \implies$ **ALWAYS GUESS** ($+0.50 pt$ expected gain).

**(b) Cornell 2027 All-or-Nothing Multi-Select ($+2 / 0 / 0$):**
Because leaving the question blank gives $0 pts$, any positive probability of hitting the exact combination has $\mathbb{E}[\text{guess}] > 0$. With 2 independent $50/50$ binary options remaining ($2^2 = 4$ combinations), $p = 1/4 = 0.25$ and $\mathbb{E}[\text{guess}] = 2 \times 0.25 = \mathbf{0.50 pts} > 0 \implies$ **NEVER LEAVE BLANK when blank credit is zero**.

**✓ Verified by:** Independent Python script `check_sec21_23.py` (`SEC21_MCQ_EV_BLANK_RULE`): $\mathbb{E}_{k=4}=0.75$, $\mathbb{E}_{k=3}=1.00$, $\mathbb{E}_{k=2}=1.50\text{ pts}$.

### [TRAP & DIAGNOSTIC: Tiebreaker Hierarchy (`Rule 6.j`) & Designated `TB` Question Strategy]

Under 2027 Rule `6.j`  **[S01,S04]**, overall event ties are broken in strict sequence:
**1st Tiebreaker:** Best Temperature Score ($\mathrm{TS}$) $\longrightarrow$ **2nd Tiebreaker:** Best Exam Score ($\mathrm{ES}$) $\longrightarrow$ **3rd Tiebreaker:** Preselected test questions (`TB #1, TB #2, ...`).
However, **ties in raw Part I Exam Score ($R_{\mathrm{exam}}$)** occur frequently among teams clustered in the modal score bin (`E1`: 21 of 55 teams scored between $27.86 pts$ and $39.29 pts$  **[S25]**)! Whenever an exam labels specific items as `(TB #1)`, `(TB #2)`, etc. (as on `E1` and `E2`), **those items must be attempted during Pass 2**, even if only to record the governing equation and partial setup.

## Handling Ambiguous Questions & Online / Satellite / MiniSO Adaptations

- **Defensive Convention Declaration on Ambiguous Problems:**
  If a written question asks for “the work $W$ during compression” without specifying whether $W$ means work done *by* the gas ($W_{\mathrm{by}} < 0$) or work done *on* the gas ($w_{\mathrm{on}} > 0$), **write both labeled values in the answer box**:
  
$$
\text{``}W_{\mathrm{by\ gas}} = -5.15 kJ \quad (\text{or } w_{\mathrm{on\ gas}} = +5.15 kJ)\text{''}
$$

  This takes 3 extra seconds and guarantees full credit regardless of whether the supervisor used a physics key (`E1, E3, E4, E6`) or a chemistry key (`E7, E8`)  **[S25,S28,S31]**. Similarly, if water properties are not given in the problem header, state the standard value used (e.g., $c_w = 4.184 kJ/kg/K$, $L_f = 334 kJ/kg$, $L_v = 2260 kJ/kg$, $P_{\mathrm{atm}} = 101.325 kPa$).
- **Online / Satellite / MiniSO Platform Protocol (Scilympiad / Avogadro):**
  When an invitational runs in online or satellite mode (§`app:F` Host Verification Checklist):
- **Rule `2.c` Paper-Notes Baseline vs. Digital PDF Rules:** Under national Rule `2.c`, notes must be printed on paper and Class IV devices (laptops/tablets) are prohibited for calculation (`p. C74`)  **[S01]**. **Always use physical printed binder pages and stand-alone Class III calculators** even during online testing unless the tournament host's written modification document explicitly authorizes searching a local PDF.
- **Zero-Collision Partner Question Split on Digital Platforms:** On Scilympiad/Avogadro, two partners typing in the same question box simultaneously can overwrite each other's buffer. Enforce a strict **Odd/Even or Section-Block Split**: Partner A claims even-numbered / Phase-Cycle-Entropy blocks; Partner B claims odd-numbered / Foundations-Transfer-History blocks, announcing “Saving Q#” aloud before clicking Next.
- **Auto-Graded Numeric Box Formatting:** Online platforms often parse numeric boxes via string/float matching before manual human re-grading. Unless the box explicitly includes units outside the text field, enter the **exact floating-point number to the requested significant figures** in the numeric box and type the full equation, units, and sign-convention note in the adjacent free-response work box.
  

—
**See also:** §`sec:00` (Command Center & 10-Second Router), §`sec:01` (14 Removable Quick Sheets `QS-01`..`QS-14`), §`sec:16` (2027 Collector Prediction Nomogram), §`sec:20` (Misconceptions & Error Catalog), §`sec:22` (Evidence-Based Tournament Intelligence), and §`app:F` (One-Page Rules & Host-Modifications Checklist).
