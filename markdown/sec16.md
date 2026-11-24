<!-- Source: src/sec16.tex | Tab: Tab 6: DEVICE | Target: 12 pp -->
# §16: Device Calibration, Heating-Curve Prediction & Day-Of Lookup Tables {#sec:16}

> **[SCOPE: REQUIRED | 2027 Rules 5.II.a–i, 6.b–j & Official Scoresheet v2.0.0 (All Tournament Levels)]**

In the 2026–2027 Division C Thermodynamics event, Part II (Device Testing) accounts for **$50.0\text{ of the }100.0\text{ total points}$**: up to **$30.0\text{ points}$** for the Temperature Score ($\mathrm{TS}$) and up to **$20.0\text{ points}$** for the Prediction Score ($\mathrm{PS}$)  **[S01,S04]**. Moreover, under Rule `6.j` and Official Scoresheet v2.0.0, **Best $\mathrm{TS}$ is the First Overall Tiebreaker (`TB1`)** for the entire event  **[S01,S04]**! Because the Event Supervisor announces the exact bulb height $h_{\mathrm{bulb}} \in [40 cm, 65 cm]$, heating duration $t_{\mathrm{heat}} \in [10 min, 15 min]$, room temperature $T_{\mathrm{room}}$, source bath temperature $T_{\mathrm{bath}}$, and bulb specifications ($P_{\mathrm{bulb}} \in [100 W, 125 W]$) only at the start of the competition block (Rule `5.II.a`), and announces your individual cup starting temperature $T_{\mathrm{start}}$ only when handing you the water (Rule `5.II.c`), a championship team must compute its final water temperature prediction $T_{\mathrm{pred}}$ to within **$\pm0.15 °C$ in under 15 seconds**  **[S01,S05]**. This chapter provides the complete five-variable physical–empirical prediction suite, the 36-condition Design-of-Experiments (DOE) calibration matrix, the 26-row $1 cm$ National interpolation table, post-lamp cooling corrections, and tournament mismatch recovery protocols.

## Mathematical Structure of 2027 Scoring ($\mathrm{TS}, \mathrm{PS}, \mathrm{PE}$) & Error Sensitivity

Under Rule `6.b`, **all scoring calculations are performed strictly in degrees Celsius ($°C$)**—never in Kelvin or Fahrenheit  **[S01,S04]**. Understanding the exact functional form of the official v2.0.0 Scoresheet reveals a critical synergy between maximizing optical heating ($\mathrm{TG}$) and maximizing prediction accuracy ($\mathrm{PE}$).

### [FORMULA & DECISION CARD: Official 2027 v2.0.0 Scoresheet Equations, Penalty Multipliers & Marginal Point Loss]

| **Formula** | **Variables (SI units)** | **Flags** | **Use when** |
| --- | --- | --- | --- |
| $\mathrm{FS} = \mathrm{ES} + \mathrm{TS} + \mathrm{PS}$ <br> $M_{\mathrm{pen}} = (0.7)^{V_{\mathrm{constr}}}\times (0.9)^{V_{\mathrm{comp}}}$ | $\mathrm{ES} \in [0, 50]$: Exam Score; $\mathrm{TS} \in [0, 30]$: Temp Score; $\mathrm{PS} \in [0, 20]$: Prediction Score; $V_{\mathrm{constr}}$: construction + non-impound violations (`6.g`); $V_{\mathrm{comp}}$: competition violations (`6.h`). | **[2027-RULE]** | Master 100-point event sum (`6.c`). Note: $M_{\mathrm{pen}}$ multiplies $\mathrm{TS}$ and $\mathrm{PS}$ only, never $\mathrm{ES}$ **[S01,S04]**. |
| $\mathrm{TG} = \max\!\left(0,\; T_{\mathrm{final}} - T_{\mathrm{start}}\right)$ <br> $\mathrm{TS} = 30\,M_{\mathrm{pen}}\,\dfrac{\mathrm{TG}}{\mathrm{TG}_{\max}}$ | $T_{\mathrm{start}}, T_{\mathrm{final}}$: ES thermometer readings to $0.1 °C$; $\mathrm{TG}_{\max}$: highest $\mathrm{TG}$ among all teams in the tournament (if $\mathrm{TG}_{\max}=0$, ratio $=1$). | **[2027-RULE]** | Rule `6.e`: $\mathrm{TS}=0$ if hazardous material (`3.b.i`), energy source (`3.f`), touched during heating (`5.II.e`), or no device. |
| $\mathrm{PE} = \max\!\left(0,\; 1 - \dfrac{\|T_{\mathrm{final}} - T_{\mathrm{pred}}\|}{T_{\mathrm{final}}}\right)$ <br> $\mathrm{PS} = 20\,M_{\mathrm{pen}}\,\dfrac{\mathrm{PE}}{\mathrm{PE}_{\max}}$ | $T_{\mathrm{pred}}$: team's submitted prediction in $[°C]$ (`5.II.f`); **Crucial:** $T_{\mathrm{final}}$ in the denominator is in $\mathbf{°C}$ (`6.b`), NOT Kelvin and NOT $\mathrm{TG}$! | **[2027-RULE]** | Rule `6.f`: $\mathrm{PS}=0$ if $\mathrm{TS}=0$ disqualification or if $T_{\mathrm{pred}}$ is not submitted before Heating Time ends (`5.II.f`). |
| $\Delta\mathrm{PS}_{\mathrm{lost}} \approx \dfrac{20\,M_{\mathrm{pen}}}{\mathrm{PE}_{\max}}\,\dfrac{\|\Delta T_{\mathrm{err}}\|}{T_{\mathrm{final}}}$ <br> $\dfrac{\partial\mathrm{PS}}{\partial \|\Delta T_{\mathrm{err}}\|} \approx -\dfrac{20}{T_{\mathrm{final}}}\ \left[\dfrac{\text{pts}}{°C}\right]$ | $\|\Delta T_{\mathrm{err}}\| = \|T_{\mathrm{final}} - T_{\mathrm{pred}}\|$: absolute prediction error $[°C]$; evaluated assuming $\mathrm{PE}_{\max} \approx 1.000$ and $M_{\mathrm{pen}} = 1$. | **[2027-RULE]** | At $T_{\mathrm{final}} = 50.0 °C$, each $0.5 °C$ error costs $0.20 pts$; at $T_{\mathrm{final}} = 25.0 °C$, the same $0.5 °C$ error costs $0.40 pts$ ($2\times$ more!). |

> **[Vector Figure: Prediction Score $\mathrm{PS} = 20(1 - |\Delta T_{\mathrm{err}}|/T_{\mathrm{final}})$ versus prediction error $|\Delta T_{\mathrm{err}}|$ across final water temperatures $T_{\mathrm{final}} \in [24 °C, 50 °C]$  **[S01,S04]**. | Label: `fig:16:pe-sensitivity`]**
> - **Diagram Annotations & Key Elements:** **X-Axis:** Absolute Prediction Error $|\Delta T_{\mathrm{err}}| = |T_{\mathrm{final}} - T_{\mathrm{pred}}|$ $[°C]$ • **Y-Axis:** Prediction Score $\mathrm{PS}$ $[\text{pts / }20]$ ($\mathrm{PE}_{\max}\!=\!1$) • **Legend:** $T_{\mathrm{final}} = 50.0 °C$ ($\mathrm{TG}=28 °C$) • **Legend:** $T_{\mathrm{final}} = 40.0 °C$ ($\mathrm{TG}=18 °C$) • **Legend:** $T_{\mathrm{final}} = 30.0 °C$ ($\mathrm{TG}=8 °C$) • **Legend:** $T_{\mathrm{final}} = 24.0 °C$ ($\mathrm{TG}=2 °C$) • Target $\le0.3 °C$ • Slope $-0.40 pts/ °C$ • Slope $-0.83 pts/ °C$

### [TRAP & DIAGNOSTIC: Double Penalty of Under-Heating & Asymmetric Over- vs. Under-Prediction]

- **Why “Sandbagging” $\mathrm{TG}$ for Easy Prediction Fails:** Some teams consider blocking the lamp so $\mathrm{TG} \approx 0 °C$ and $T_{\mathrm{final}} \approx T_{\mathrm{start}}$ is trivial to predict ($\mathrm{PS} = 20.0\text{ pts}$). That strategy forfeits up to $\mathbf{30.0\text{ points}}$ on $\mathrm{TS}$, loses the **First Overall Tiebreaker (`TB1` = Best $\mathrm{TS}$, Rule `6.j`)**, and actually *doubles* the fractional error penalty $1/T_{\mathrm{final}}$ per degree of thermometer jitter!
- **Higher $T_{\mathrm{final}}$ Buffers $\mathrm{PE}$:** Because $T_{\mathrm{final}}$ sits in the denominator of $\mathrm{PE} = 1 - |\Delta T_{\mathrm{err}}|/T_{\mathrm{final}}$, achieving $T_{\mathrm{final}} = 50.0 °C$ instead of $25.0 °C$ cuts the point loss of any $\pm0.2 °C$ sensor fluctuation in half (from $0.16 pts$ to $0.08 pts$).
- **Conditional Expectation Optimal Estimator:** Since $T_{\mathrm{final}}$ is fixed by physics while you choose $T_{\mathrm{pred}}$, the expected score $\mathbb{E}[\mathrm{PE}]$ under symmetric Gaussian repeatability noise $\epsilon \sim \mathcal{N}(0, \sigma_{\mathrm{rep}}^2)$ is strictly maximized by submitting the **unbiased conditional mean** $T_{\mathrm{pred}} = \mathbb{E}[T_{\mathrm{final}}]$ rounded to the nearest $0.1 °C$.

### Worked Example — Official v2.0.0 Scoresheet Calculation & Marginal Prediction Sensitivity `[Rule 6.c–j / §16.1]`

At a State tournament ($h_{\mathrm{bulb}} = 45.0 cm$, $t_{\mathrm{heat}} = 10.0 min$, $125 W$ lamp), the tournament-high metrics are $\mathrm{ES}_{\mathrm{raw,max}} = 92.0\text{ pts}$, $\mathrm{TG}_{\max} = 27.7 °C$, and $\mathrm{PE}_{\max} = 0.9980$. Compare two teams that both earn raw written exam score $88.5\text{ pts}$ and have zero violations ($M_{\mathrm{pen}} = 1.0$):
- **Team Alpha (3-Stage Glazed CPC):** $T_{\mathrm{start}} = 22.0 °C$, $T_{\mathrm{final}} = 49.7 °C$, submitted $T_{\mathrm{pred}} = 49.4 °C$ ($|\Delta T_{\mathrm{err}}| = 0.3 °C$).
- **Team Beta (Open $30^\circ$ Straight Cone):** $T_{\mathrm{start}} = 22.0 °C$, $T_{\mathrm{final}} = 30.1 °C$, submitted $T_{\mathrm{pred}} = 29.8 °C$ (same $|\Delta T_{\mathrm{err}}| = 0.3 °C$).

Compute $\mathrm{ES}, \mathrm{TG}, \mathrm{TS}, \mathrm{PE}, \mathrm{PS}$, and Final Score $\mathrm{FS}$ for both teams, and verify the point loss if Team Beta also forgot to impound its spare glazing ring ($V_{\mathrm{constr}} = 1$, Clarification #9).

**Solution.** Both teams earn Exam Score $\mathrm{ES} = 50 \times (88.5 / 92.0) = \mathbf{48.10 pts}$.
- **Team Alpha:** $\mathrm{TG}_\alpha = 49.7 - 22.0 = 27.7 °C \implies \mathrm{TS}_\alpha = 30 \times (27.7 / 27.7) = \mathbf{30.00 pts}$. Prediction Estimate: $\mathrm{PE}_\alpha = 1 - \frac{|49.7 - 49.4|}{49.7} = 1 - 0.006036 = \mathbf{0.99396} \implies \mathrm{PS}_\alpha = 20 \times \frac{0.99396}{0.9980} = \mathbf{19.92 pts}$. Total: $\mathrm{FS}_\alpha = 48.10 + 30.00 + 19.92 = \mathbf{98.02 pts}$.
- **Team Beta ($M_{\mathrm{pen}} = 1.0$):** $\mathrm{TG}_\beta = 30.1 - 22.0 = 8.1 °C \implies \mathrm{TS}_\beta = 30 \times (8.1 / 27.7) = \mathbf{8.77 pts}$. Because $T_{\mathrm{final},\beta} = 30.1 °C$ is lower, the exact same $0.3 °C$ prediction error gives a lower $\mathrm{PE}_\beta = 1 - \frac{0.3}{30.1} = \mathbf{0.99003} \implies \mathrm{PS}_\beta = 20 \times \frac{0.99003}{0.9980} = \mathbf{19.84 pts}$. Total: $\mathrm{FS}_\beta = 48.10 + 8.77 + 19.84 = \mathbf{76.71 pts}$ ($21.31 pts$ behind Team Alpha!).
- **If Team Beta Incurs $V_{\mathrm{constr}} = 1$ ($M_{\mathrm{pen}} = 0.7$):** $\mathrm{TS}_{\beta,\mathrm{pen}} = 0.7(8.77) = 6.14 pts$ and $\mathrm{PS}_{\beta,\mathrm{pen}} = 0.7(19.84) = 13.89 pts \implies \mathrm{FS}_{\beta,\mathrm{pen}} = \mathbf{68.13 pts}$ (losing an additional $8.58 pts$).

**✓ Verified by:** Exact cell-by-cell replication of `2027ThermodynamicsBC_scoresheet.xlsx` (v2.0.0) formulas; asserted in `check_sec14_16.py`.

**Table:** Exact Prediction Estimate $\mathrm{PE} = 1 - |\Delta T_{\mathrm{err}}|/T_f$ and Prediction Score $\mathrm{PS}$ ($\text{pts}/20$) lookup matrix  **[S01,S04]**.

| **$\|\Delta T_{\mathrm{err}}\|$** | **Prediction Estimate $\mathrm{PE}$ $[-]$** |  |  |  | **Score $\mathrm{PS}$ $[\text{pts}/20]$** |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $[°C]$ | $T_f\!=\!30^\circ$ | $40^\circ$ | $45^\circ$ | $50^\circ\mathrm{C}$ | $30^\circ$ | $40^\circ$ | $45^\circ$ | $50^\circ\mathrm{C}$ |
| $\mathbf{0.0}$ | $1.0000$ | $1.0000$ | $1.0000$ | $1.0000$ | $20.00$ | $20.00$ | $20.00$ | $\mathbf{20.00}$ |
| $\mathbf{0.1}$ | $0.9967$ | $0.9975$ | $0.9978$ | $0.9980$ | $19.93$ | $19.95$ | $19.96$ | $\mathbf{19.96}$ |
| $\mathbf{0.2}$ | $0.9933$ | $0.9950$ | $0.9956$ | $0.9960$ | $19.87$ | $19.90$ | $19.91$ | $\mathbf{19.92}$ |
| $\mathbf{0.3}$ | $0.9900$ | $0.9925$ | $0.9933$ | $0.9940$ | $19.80$ | $19.85$ | $19.87$ | $\mathbf{19.88}$ |
| $\mathbf{0.5}$ | $0.9833$ | $0.9875$ | $0.9889$ | $0.9900$ | $19.67$ | $19.75$ | $19.78$ | $\mathbf{19.80}$ |
| $\mathbf{1.0}$ | $0.9667$ | $0.9750$ | $0.9778$ | $0.9800$ | $19.33$ | $19.50$ | $19.56$ | $\mathbf{19.60}$ |
| $\mathbf{2.0}$ | $0.9333$ | $0.9500$ | $0.9556$ | $0.9600$ | $18.67$ | $19.00$ | $19.11$ | $19.20$ |
| $\mathbf{3.0}$ | $0.9000$ | $0.9250$ | $0.9333$ | $0.9400$ | $18.00$ | $18.50$ | $18.67$ | $18.80$ |
| $\mathbf{5.0}$ | $0.8333$ | $0.8750$ | $0.8889$ | $0.9000$ | $16.67$ | $17.50$ | $17.78$ | $18.00$ |

**Table:** Penalty multiplier $M_{\mathrm{pen}} = 0.7^{V_{\mathrm{constr}}} \times 0.9^{V_{\mathrm{comp}}}$ (Rules `6.g–h`)  **[S01,S04]**.

| **$V_{\mathrm{constr}}$** | **$V_{\mathrm{comp}}$** | **$M_{\mathrm{pen}}$** | **Max Pt II** | **Typical Cause** |
| --- | --- | --- | --- | --- |
| (`6.g`) | (`6.h`) | $[-]$ | $[\text{pts}/50]$ |  |
| $\mathbf{0}$ | $\mathbf{0}$ | $\mathbf{1.000}$ | $\mathbf{50.00}$ | **100% Compliant** |
| $0$ | $1$ | $0.900$ | $45.00$ | Wrap left on cup (`5.II.g`) |
| $0$ | $2$ | $0.810$ | $40.50$ | Tape on cup + late mod |
| $1$ | $0$ | $0.700$ | $35.00$ | Missed impound (`2.d`) |
| $1$ | $1$ | $0.630$ | $31.50$ | $>30\text{ cm}$ + wrap error |
| $2$ | $0$ | $0.490$ | $24.50$ | $>30\text{ cm}$ + water contact |
| **`3.b.i / 3.f / 5.II.e`** |  | $\mathbf{0.000}$ | $\mathbf{0.00}$ | **`#6 PS`, Battery, or Touch!** |

## Five-Variable Physical–Empirical Heating-Curve Prediction Model

Combining the forced lumped-capacitance heating ODE solution (§`sec:13.2`) with the stratified top-layer optical capture $\dot{Q}_{\mathrm{abs}}(h_{\mathrm{bulb}}, P_{\mathrm{bulb}})$ (§`sec:15.3`–§`sec:15.5`) yields a closed-form algebraic prediction model taking all **five day-of tournament variables** announced by the Event Supervisor under Rule `5.II.a,c`:

$$
\begin{aligned}

  \boxed{T_{\mathrm{pred}}(h, t, T_{\mathrm{start}}, T_{\mathrm{room}}, P_{\mathrm{bulb}}) = T_{\mathrm{start}} + \Delta T_{\mathrm{ref}}(h)\,\eta_P(P_{\mathrm{bulb}})\,\frac{1 - e^{-t/\tau_{\mathrm{eff}}}}{1 - e^{-600/\tau_{\mathrm{eff}}}} - \gamma_{\mathrm{loss}}(T_{\mathrm{start}} - T_{\mathrm{room}})\!\left(1 - e^{-t/\tau_{\mathrm{eff}}}\right) - \Delta T_{\mathrm{cool}}(t_{\mathrm{wait}})}
\end{aligned}
$$

where each parameter has a direct physical definition and pre-calibrated empirical value:
- **10-Minute Reference Gain $\Delta T_{\mathrm{ref}}(h)$ $[°C]$:** The calibrated top-layer temperature rise at $t_{\mathrm{ref}} = 600 s$ ($10.0 min$) under a $125 W$ clear $\mathrm{R40}$ heat lamp when $T_{\mathrm{start}} = T_{\mathrm{room}} = 22.0 °C$ (tabulated at $1 cm$ resolution across $h \in [40 cm, 65 cm]$ in Table `tab:16:natl-1cm`).
- **Bulb-Wattage Scaling Factor $\eta_P(P_{\mathrm{bulb}})$ $[-]$:** Scales absorbed radiant power relative to the $125 W$ baseline:
  
$$
\begin{aligned}

    \eta_P(P_{\mathrm{bulb}}) = \left(\frac{P_{\mathrm{bulb}}}{125 W}\right)^{\!\beta_P} = \begin{cases} 1.000 & \text{for } P_{\mathrm{bulb}} = 125 W \\ 0.800\ (\text{or empirical } 0.798\text{--}0.804) & \text{for } P_{\mathrm{bulb}} = 100 W \end{cases}
\end{aligned}
$$
- **Heating-Time Exponential Growth Ratio $M_t(t)$ $[-]$:** Scales from $t_{\mathrm{ref}} = 600 s$ to any State/National heating duration $t \in [600 s, 900 s]$ ($10–15 min$) using the collector's calibrated effective top-layer time constant $\tau_{\mathrm{eff}} = C_{\mathrm{top,eff}}R_{\mathrm{th,eff}} = 903.0 s$ ($15.05 min$):
  
$$
\begin{aligned}

    M_t(t) = \frac{1 - e^{-t/\tau_{\mathrm{eff}}}}{1 - e^{-600/\tau_{\mathrm{eff}}}} = \frac{1 - e^{-t/903.0 s}}{0.48543}
\end{aligned}
$$
- **Starting-Water vs. Ambient-Room Coupling Weights $k_{\mathrm{start}}(t)$ and $k_{\mathrm{room}}(t)$:** When the ES source water bath $T_{\mathrm{start}}$ differs from the ambient room temperature $T_{\mathrm{room}}$ (e.g., cold tap water filled that morning, $T_{\mathrm{start}} < T_{\mathrm{room}}$), setting $\gamma_{\mathrm{loss}} = 1.00$ rearranges Eq. Eq. (`eq:16:master-5var`) into the **10-Second Linear Superposition Formula**:
  
$$
\begin{aligned}

    \boxed{T_{\mathrm{pred}} = \mathrm{TG}_{\mathrm{table}}(h, P_{\mathrm{bulb}}, t) + k_{\mathrm{start}}(t)\,T_{\mathrm{start}} + k_{\mathrm{room}}(t)\,T_{\mathrm{room}} - \Delta T_{\mathrm{cool}}(t_{\mathrm{wait}}) = T_{\mathrm{start}} + \mathrm{TG}_{\mathrm{table}} + k_{\mathrm{room}}(t)\,(T_{\mathrm{room}} - T_{\mathrm{start}}) - \Delta T_{\mathrm{cool}}}
\end{aligned}
$$

  
  where $k_{\mathrm{start}}(t) = e^{-t/\tau_{\mathrm{eff}}}$ and $k_{\mathrm{room}}(t) = 1 - e^{-t/\tau_{\mathrm{eff}}}$ satisfy $k_{\mathrm{start}}(t) + k_{\mathrm{room}}(t) = 1$ identically!

**Table:** Analytical partial-derivative sensitivity matrix and GUM uncertainty propagation budget around nominal tournament operating point ($h=50.0 cm, P_{\mathrm{bulb}}=125 W, t=10.0 min=600 s, T_{\mathrm{start}}=T_{\mathrm{room}}=22.0 °C, \mathrm{TG}=21.30 °C, T_{\mathrm{final}}=43.30 °C, \tau_{\mathrm{eff}}=903 s$)  **[S01,S12,S21]**.

| **Input Variable $x_i$** | **Rule Source** | **Analytical Partial Derivative $\dfrac{\partial T_{\mathrm{final}}}{\partial x_i}$** | **Nominal** | **Day-Of** | **Propagated** | **Error If Variable Is Ignored** |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | **Slope** | **$u(x_i)$** | **$\|\frac{\partial T_f}{\partial x_i}\|u(x_i)$** | **Across Tournament Range** |
| **1. Starting Water Temp $T_{\mathrm{start}}$** $[°C]$ | `5.II.c` ($0.1 °C$) | $\dfrac{\partial T_f}{\partial T_{\mathrm{start}}} = k_{\mathrm{start}}(t) = e^{-t/\tau_{\mathrm{eff}}}$ | $+0.515 °C/°C$^a | $0.06 °C$ | $0.031 °C$ | $\pm1.5–3.5 °C$ across cold/warm tournament water baths! |
| **2. Ambient Room Temp $T_{\mathrm{room}}$** $[°C]$ | `5.II.a` (Board) | $\dfrac{\partial T_f}{\partial T_{\mathrm{room}}} = k_{\mathrm{room}}(t) = 1 - e^{-t/\tau_{\mathrm{eff}}}$ | $+0.485 °C/°C$ | $0.20 °C$ | $0.097 °C$ | $\pm0.8–2.0 °C$ between morning and afternoon blocks. |
| **3. Bulb Height $h_{\mathrm{bulb}}$** $[cm]$ | `4.c, 5.II.a` | $\dfrac{\partial T_f}{\partial h} = M_t\eta_P\dfrac{d(\Delta T_{\mathrm{ref}})}{dh}$ | $-1.03 °C/cm$ | $0.12 cm$ | $0.124 °C$ | **$17.1 °C$ swing across $h=40–65 cm$!** |
| **4. Heating Time $t_{\mathrm{heat}}$** $[min]$ | `5.II.a.i–ii` | $\dfrac{\partial T_f}{\partial t} = \dfrac{T_{\mathrm{ss}} - T_f}{\tau_{\mathrm{eff}}}$ ($[°C/min]$) | $+1.56 °C/min$ | $0.03 min$ | $0.047 °C$ | **$+7.2–9.2 °C$ swing from $10 min$ to $15 min$!** |
| **5. Bulb Wattage $P_{\mathrm{bulb}}$** $[W]$ | `4.a, 5.II.a` | $\dfrac{\partial T_f}{\partial P_{\mathrm{bulb}}} = \dfrac{\mathrm{TG}}{P_{\mathrm{bulb}}}$ | $+0.170 °C/W$ | $1.2 W$^b | $0.204 °C$ | **$-4.2–5.5 °C$ drop switching $125 W\to100 W$!** |
| **6. Extraction Wait $t_{\mathrm{wait}}$** $[s]$ | `5.II.g` ($\le60 s$) | $\dfrac{\partial T_f}{\partial t_{\mathrm{wait}}} = -r_{\mathrm{open}}$ | $-0.018 °C/s$ | $4.0 s$ | $0.072 °C$ | $-0.3–1.1 °C$ cooling during 1-min ES measurement window. |
| **Combined Quadrature Standard Uncertainty $u_c(T_{\mathrm{pred}}) = \sqrt{\sum (\partial T_f/\partial x_i)^2 u(x_i)^2}$:** |  |  |  | — | $\mathbf{0.273 °C}$ | **Expected $\mathbb{E}[\mathrm{PE}] = 1 - \frac{0.22}{43.3} = \mathbf{0.9950}$ ($19.90 pts$)!** |
| ^aAt fixed $T_{\mathrm{room}}$. When $T_{\mathrm{start}}$ and $T_{\mathrm{room}}$ shift together by $\Delta T$, $\partial T_f/\partial T_{\mathrm{start}} + \partial T_f/\partial T_{\mathrm{room}} = 0.515 + 0.485 = \mathbf{+1.000\,°C/°C}$. ^bLine-voltage fluctuation $\pm 1.0\%$. |  |  |  |  |  |  |

### Worked Example — Five-Variable Prediction with Cold Source Bath Offset ($T_{\mathrm{start}} \neq T_{\mathrm{room}}$) `[Rule 5.II.a,c,f / §16.2]`

At a State tournament, the ES announces at the start of the block (`Rule 5.II.a`): bulb height $h_{\mathrm{bulb}} = 45.0 cm$, heating time $t_{\mathrm{heat}} = 13.0 min$ ($780 s$), room temperature $T_{\mathrm{room}} = 23.2 °C$, and bulb wattage $P_{\mathrm{bulb}} = 125 W$ ($\eta_P = 1.000$). From calibration, the collector's 10-minute ($600 s$) reference gain at $h = 45.0 cm$ is $\Delta T_{\mathrm{ref}}(45 cm) = 27.70 °C$ with time constant $\tau_{\mathrm{eff}} = 903.0 s$. When the team receives its water cup (`Rule 5.II.c`), the ES measures $T_{\mathrm{start}} = 19.6 °C$ (the source water bath is $3.6 °C$ colder than the room!). Assuming a $12 s$ post-lamp extraction cooling correction $\Delta T_{\mathrm{cool}} = 0.22 °C$, compute $T_{\mathrm{pred}}$ using Eq. Eq. (`eq:16:master-5var`) and verify via the 10-second linear superposition formula Eq. Eq. (`eq:16:fast-superposition`).

**Solution.**
1. **Time-Scaling Multiplier at $t = 780 s$ ($13.0 min$):**

$$
e^{-780/903.0} = e^{-0.86379} = 0.42156 \implies 1 - e^{-t/\tau_{\mathrm{eff}}} = 0.57844, \qquad M_t(13 min) = \frac{0.57844}{1 - e^{-600/903.0}} = \frac{0.57844}{0.48543} = \mathbf{1.19160}
$$

Thus the isothermal ($T_{\mathrm{start}}=T_{\mathrm{room}}$) table gain at $13.0 min$ is $\mathrm{TG}_{\mathrm{table}}(45 cm, 125 W, 13 min) = 27.70 \times 1.19160 = \mathbf{33.01 °C}$.

2. **Ambient-to-Bath Offset Correction ($k_{\mathrm{start}} = 0.42156, k_{\mathrm{room}} = 0.57844$):**
Because the room ($T_{\mathrm{room}} = 23.2 °C$) is $3.6 °C$ warmer than the starting water ($T_{\mathrm{start}} = 19.6 °C$), parasitic heat loss to the room is reduced by:

$$
\Delta T_{\mathrm{ambient-boost}} = k_{\mathrm{room}}(13 min)\,(T_{\mathrm{room}} - T_{\mathrm{start}}) = 0.57844(23.2 - 19.6) = \mathbf{+2.082 °C}
$$

3. **Final Submitted Prediction $T_{\mathrm{pred}}$:**

$$
T_{\mathrm{pred}} = T_{\mathrm{start}} + \mathrm{TG}_{\mathrm{table}} + \Delta T_{\mathrm{ambient-boost}} - \Delta T_{\mathrm{cool}} = 19.60 + 33.01 + 2.08 - 0.22 = \mathbf{54.47 °C \longrightarrow \text{Submit }54.5 °C}
$$

**✓ Verified by:** Direct superposition check: $\mathrm{TG}_{\mathrm{table}} + k_{\mathrm{start}}T_{\mathrm{start}} + k_{\mathrm{room}}T_{\mathrm{room}} - \Delta T_{\mathrm{cool}} = 33.007 + 0.42156(19.6) + 0.57844(23.2) - 0.22 = 33.007 + 8.263 + 13.420 - 0.22 = 54.470 °C$; asserted in `check_sec14_16.py`.

### [DERIVATION: Algebra-Only Three-Point Equal-Interval Extraction of $\tau_{\mathrm{eff}}$ and $T_{\mathrm{ss}}$ (Rule 5.d.iv Compliant)]

During pre-tournament calibration when $T_{\mathrm{start}} = T_{\mathrm{room}}$, the temperature gain obeys $\mathrm{TG}(t) = \Delta T_{\mathrm{ss}}(1 - e^{-t/\tau_{\mathrm{eff}}})$, where $\Delta T_{\mathrm{ss}} = \dot{Q}_{\mathrm{abs}}R_{\mathrm{th,eff}}$. Measuring $\mathrm{TG}_1 \equiv \mathrm{TG}(\Delta t)$ at $t_1 = \Delta t$ (e.g., $5.0 min = 300 s$) and $\mathrm{TG}_2 \equiv \mathrm{TG}(2\Delta t)$ at $t_2 = 2\Delta t$ (e.g., $10.0 min = 600 s$) allows exact algebraic elimination of $\Delta T_{\mathrm{ss}}$ using the identity $1 - e^{-2\Delta t/\tau_{\mathrm{eff}}} = (1 - e^{-\Delta t/\tau_{\mathrm{eff}}})(1 + e^{-\Delta t/\tau_{\mathrm{eff}}})$:

$$
\frac{\mathrm{TG}_2}{\mathrm{TG}_1} = 1 + e^{-\Delta t/\tau_{\mathrm{eff}}} \implies e^{-\Delta t/\tau_{\mathrm{eff}}} = \frac{\mathrm{TG}_2 - \mathrm{TG}_1}{\mathrm{TG}_1} \implies
  \boxed{\tau_{\mathrm{eff}} = \frac{\Delta t}{\ln\!\left(\dfrac{\mathrm{TG}_1}{\mathrm{TG}_2 - \mathrm{TG}_1}\right)}, \qquad \Delta T_{\mathrm{ss}} = \frac{\mathrm{TG}_1^2}{2\,\mathrm{TG}_1 - \mathrm{TG}_2}}
$$

This closed-form algebraic solver extracts both $\tau_{\mathrm{eff}}$ and $\Delta T_{\mathrm{ss}}$ in 10 seconds on any scientific calculator without nonlinear regression!

### Worked Example — Algebraic 3-Point Extraction of $\tau_{\mathrm{eff}}$ & $\Delta T_{\mathrm{ss}}$ `[Rule 5.d.ii / §16.2]`

In a calibration run at $h = 45.0 cm$ ($125 W$ lamp, $T_{\mathrm{start}} = T_{\mathrm{room}} = 22.0 °C$), the top-layer temperature gain is $\mathrm{TG}_1 = 16.17 °C$ at $t_1 = 300 s$ ($5.0 min$) and $\mathrm{TG}_2 = 27.77 °C$ at $t_2 = 600 s$ ($10.0 min$). Using the three-point equal-interval formulas ($\Delta t = 300 s$), compute (a) the increment $\mathrm{TG}_2 - \mathrm{TG}_1$ and decay factor $e^{-\Delta t/\tau_{\mathrm{eff}}}$, (b) the effective time constant $\tau_{\mathrm{eff}}$, and (c) the asymptotic stagnation temperature rise $\Delta T_{\mathrm{ss}}$ and predicted $15.0 min$ gain $\mathrm{TG}(900 s)$.

**Solution.**
(a) Second-half gain increment: $\mathrm{TG}_2 - \mathrm{TG}_1 = 27.77 - 16.17 = 11.60 °C$, giving decay ratio:

$$
e^{-\Delta t/\tau_{\mathrm{eff}}} = \frac{\mathrm{TG}_2 - \mathrm{TG}_1}{\mathrm{TG}_1} = \frac{11.60}{16.17} = \mathbf{0.71738}
$$

(b) Solving for the effective thermal time constant $\tau_{\mathrm{eff}}$:

$$
\tau_{\mathrm{eff}} = \frac{300 s}{\ln(16.17 / 11.60)} = \frac{300}{0.33215} = \mathbf{903.2 s}\ (15.05 min)
$$

(c) The asymptotic steady-state gain and $15.0 min$ gain are:

$$
\Delta T_{\mathrm{ss}} = \frac{16.17^2}{2(16.17) - 27.77} = \frac{261.47}{4.57} = \mathbf{57.21 °C}
$$

$$
\mathrm{TG}(900 s) = \Delta T_{\mathrm{ss}}\!\left(1 - 0.71738^3\right) = \mathbf{36.10 °C}
$$

**✓ Verified by:** Direct check $\Delta T_{\mathrm{ss}}(1 - e^{-600/903.2}) = 57.214(1 - 0.51461) = 27.77 °C$; asserted in `check_sec14_16.py`.

**Table:** Pre-computed ambient-to-bath temperature offset correction $\Delta T_{\mathrm{amb}} = k_{\mathrm{room}}(t)(T_{\mathrm{room}} - T_{\mathrm{start}})$ $[°C]$  **[S01,S12]**.

| **$T_{\mathrm{room}}\!-\!T_{\mathrm{start}}$** | **Add $\Delta T_{\mathrm{amb}}$ $[°C]$ to $\mathrm{TG}_{\mathrm{table}}$** |  |  |  |  |  | **Physical** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| $[°C]$ | $10 min$ | $11 min$ | $12 min$ | $13 min$ | $14 min$ | $15 min$ | **Regime** |
| $\mathbf{+4.0}$ | $+1.94$ | $+2.07$ | $+2.20$ | $+2.31$ | $+2.42$ | $+2.52$ | Cold tap |
| $\mathbf{+3.0}$ | $+1.46$ | $+1.55$ | $+1.65$ | $+1.73$ | $+1.82$ | $+1.89$ | Cold bath |
| $\mathbf{+2.0}$ | $+0.97$ | $+1.04$ | $+1.10$ | $+1.16$ | $+1.21$ | $+1.26$ | Cool bath |
| $\mathbf{+1.0}$ | $+0.49$ | $+0.52$ | $+0.55$ | $+0.58$ | $+0.61$ | $+0.63$ | Slight cool |
| $\mathbf{+0.5}$ | $+0.24$ | $+0.26$ | $+0.28$ | $+0.29$ | $+0.30$ | $+0.32$ | Near eq. |
| $\mathbf{0.0}$ | $\mathbf{0.00}$ | $\mathbf{0.00}$ | $\mathbf{0.00}$ | $\mathbf{0.00}$ | $\mathbf{0.00}$ | $\mathbf{0.00}$ | **Isothermal** |
| $\mathbf{-0.5}$ | $-0.24$ | $-0.26$ | $-0.28$ | $-0.29$ | $-0.30$ | $-0.32$ | Near eq. |
| $\mathbf{-1.0}$ | $-0.49$ | $-0.52$ | $-0.55$ | $-0.58$ | $-0.61$ | $-0.63$ | Slight warm |
| $\mathbf{-2.0}$ | $-0.97$ | $-1.04$ | $-1.10$ | $-1.16$ | $-1.21$ | $-1.26$ | Warm bath |
| $\mathbf{-3.0}$ | $-1.46$ | $-1.55$ | $-1.65$ | $-1.73$ | $-1.82$ | $-1.89$ | Hot bath |
| $\mathbf{-4.0}$ | $-1.94$ | $-2.07$ | $-2.20$ | $-2.31$ | $-2.42$ | $-2.52$ | Cold room |
| **Weight $k_{\mathrm{room}}$** | $0.485$ | $0.518$ | $0.550$ | $0.578$ | $0.605$ | $0.631$ | $1-e^{-t/\tau}$ |
| **Weight $k_{\mathrm{start}}$** | $0.515$ | $0.482$ | $0.450$ | $0.422$ | $0.395$ | $0.369$ | $e^{-t/\tau}$ |

## Master 36-Condition DOE Matrix, Nomogram & 1-cm National Interpolation

To guarantee zero calculator-entry mistakes under tournament time pressure, Fig. `fig:16:calibration-nomogram` provides the **Master Graphical Temperature-Gain Nomogram**, Table `tab:16:doe-36` provides the **36-Condition Design-of-Experiments (DOE) Lookup Matrix** ($6\text{ heights} \times 2\text{ wattages} \times 3\text{ core durations}$, plus exact $1\text{-minute}$ time multipliers for $t = 10, 11, 12, 13, 14, 15\,min$), and Table `tab:16:natl-1cm` provides the **26-Row $1 cm$-Increment National Lookup Table** covering every integer centimeter from $h = 40 cm$ to $65 cm$ (`Rule 4.c.iii`).

> **[Vector Figure: Master 2027 Temperature-Gain Nomogram $\mathrm{TG}_{\mathrm{table}}(h_{\mathrm{bulb}}, t_{\mathrm{heat}})$ across $h_{\mathrm{bulb}} \in [40 cm, 65 cm]$ and $t_{\mathrm{heat}} \in [10 min, 15 min]$ for the glazed 3-stage CPC collector ($\tau_{\mathrm{eff}} = 903 s$)  **[S01,S12]**. | Label: `fig:16:calibration-nomogram`]**
> - **Diagram Annotations & Key Elements:** **X-Axis:** ES Announced Bulb Height Above Testing Surface $h_{\mathrm{bulb}}$ $[cm]$ (Rule `4.c`) • **Y-Axis:** Reference Top-Layer Gain $\mathrm{TG}_{\mathrm{table}}(h, t)$ $[°C]$ ($125 W$ Lamp) • **Legend:** $t = 15.0 min$ ($M_t = 1.334$) • **Legend:** $t = 14.0 min$ ($M_t = 1.274$) • **Legend:** $t = 13.0 min$ ($M_t = 1.192$) • **Legend:** $t = 12.0 min$ ($M_t = 1.143$) • **Legend:** $t = 11.0 min$ ($M_t = 1.076$) • **Legend:** $t = 10.0 min$ (Reg/State/Nat Base) • Pedestal Slot A ($z_{\mathrm{base}}=5.2 cm$) • Pedestal Slot B ($z_{\mathrm{base}}=6.4 cm$) • Pedestal Slot C ($z_{\mathrm{base}}=7.6 cm$) • **For $100 W$ Bulb:** Multiply $\mathrm{TG}_{125\mathrm{W}}$ by $\eta_P = \mathbf{0.800}$

**Table:** Master 36-Condition Design-of-Experiments (DOE) calibration lookup table ($T_{\mathrm{start}}=T_{\mathrm{room}}=22.0 °C$, $\tau_{\mathrm{eff}}=903.0 s$) and 1-minute time-scaling weights $M_t(t), k_{\mathrm{start}}(t), k_{\mathrm{room}}(t)$  **[S01,S12]**.

| **Height** | **Slot** | **$\dot{Q}_{\mathrm{abs}}$** | **$125 W$ Lamp $\mathrm{TG}_{\mathrm{table}}$ $[°C]$** |  |  | **$100 W$ Lamp $\mathrm{TG}_{\mathrm{table}}$ $[°C]$** |  |  | **$T_{\mathrm{final}}$ at $T_i\!=\!22.0 °C$ ($125 W$)** |  |  | **Tournament** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **$h$ $[cm]$** |  | $125 W$ | **$10 min$** | **$12 min$** | **$15 min$** | **$10 min$** | **$12 min$** | **$15 min$** | **$10 min$** | **$12 min$** | **$15 min$** | **Tier Scope** |
| $\mathbf{40.0}$ | **A** | $21.5 W$ | $+24.8$ | $+28.3$ | $+33.1$ | $+19.8$ | $+22.7$ | $+26.5$ | $46.8$ | $50.3$ | $55.1$ | Reg / State / Nat |
| $\mathbf{45.0}$ | **A** | $24.0 W$ | $+27.7$ | $+31.6$ | $+36.9$ | $+22.2$ | $+25.3$ | $+29.5$ | $49.7$ | $53.6$ | $58.9$ | Reg / State / Nat |
| $\mathbf{50.0}$ | **A/B** | $18.5 W$ | $+21.3$ | $+24.4$ | $+28.5$ | $+17.1$ | $+19.5$ | $+22.8$ | $43.3$ | $46.4$ | $50.5$ | Reg / State / Nat |
| $\mathbf{55.0}$ | **B** | $15.2 W$ | $+17.5$ | $+20.0$ | $+23.4$ | $+14.1$ | $+16.0$ | $+18.7$ | $39.5$ | $42.0$ | $45.4$ | State / Nationals |
| $\mathbf{60.0}$ | **B/C** | $11.8 W$ | $+13.6$ | $+15.6$ | $+18.2$ | $+10.9$ | $+12.4$ | $+14.5$ | $35.6$ | $37.6$ | $40.2$ | Nationals ($1 cm$) |
| $\mathbf{65.0}$ | **C** | $9.2 W$ | $+10.6$ | $+12.1$ | $+14.2$ | $+8.5$ | $+9.7$ | $+11.3$ | $32.6$ | $34.1$ | $36.2$ | Nationals ($1 cm$) |
| **Exact 1-Minute State/National Time-Scaling Factors ($\mathrm{TG}(h,t) = \mathrm{TG}(h,10 min)\times M_t(t)$) and Coupling Weights:** |  |  |  |  |  |  |  |  |  |  |  |  |
| $\bullet\ \mathbf{t=10 min}$ ($600 s$): $M_{10}=\mathbf{1.000}$, $k_{\mathrm{start}}=\mathbf{0.515}$, $k_{\mathrm{room}}=\mathbf{0.485}$ \quad $\bullet\ \mathbf{t=11 min}$ ($660 s$): $M_{11}=\mathbf{1.069}$, $k_{\mathrm{start}}=\mathbf{0.482}$, $k_{\mathrm{room}}=\mathbf{0.518}$ \quad $\bullet\ \mathbf{t=12 min}$ ($720 s$): $M_{12}=\mathbf{1.132}$, $k_{\mathrm{start}}=\mathbf{0.450}$, $k_{\mathrm{room}}=\mathbf{0.550}$ <br> $\bullet\ \mathbf{t=13 min}$ ($780 s$): $M_{13}=\mathbf{1.192}$, $k_{\mathrm{start}}=\mathbf{0.422}$, $k_{\mathrm{room}}=\mathbf{0.578}$ \quad $\bullet\ \mathbf{t=14 min}$ ($840 s$): $M_{14}=\mathbf{1.247}$, $k_{\mathrm{start}}=\mathbf{0.395}$, $k_{\mathrm{room}}=\mathbf{0.605}$ \quad $\bullet\ \mathbf{t=15 min}$ ($900 s$): $M_{15}=\mathbf{1.299}$, $k_{\mathrm{start}}=\mathbf{0.369}$, $k_{\mathrm{room}}=\mathbf{0.631}$ |  |  |  |  |  |  |  |  |  |  |  |  |

**Table:** National Tournament $1 cm$-Increment Reference Gain Lookup Table ($h_{\mathrm{bulb}} = 40–65 cm$, Rule `4.c.iii`, $t=10.0 min$)  **[S01]**.

| **$h$** | **Slot** | **$\mathrm{TG}_{125}$** | **$\mathrm{TG}_{100}$** | **Slope** | **$h$** | **Slot** | **$\mathrm{TG}_{125}$** | **$\mathrm{TG}_{100}$** | **Slope** | **$h$** | **Slot** | **$\mathrm{TG}_{125}$** | **$\mathrm{TG}_{100}$** | **Slope & Note** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $[cm]$ |  | $[°C]$ | $[°C]$ | $[°C/cm]$ | $[cm]$ |  | $[°C]$ | $[°C]$ | $[°C/cm]$ | $[cm]$ |  | $[°C]$ | $[°C]$ | $[°C/cm]$ |
| $\mathbf{40}$ | A | $24.8$ | $19.8$ | $+0.58$ | $\mathbf{49}$ | B | $22.6$ | $18.1$ | $-1.28$ | $\mathbf{58}$ | C | $15.2$ | $12.1$ | $-0.78$ (Slot C switch) |
| $\mathbf{41}$ | A | $25.4$ | $20.3$ | $+0.58$ | $\mathbf{50}$ | B | $21.3$ | $17.1$ | $-1.02$ | $\mathbf{59}$ | C | $14.4$ | $11.5$ | $-0.78$ |
| $\mathbf{42}$ | A | $26.0$ | $20.8$ | $+0.58$ | $\mathbf{51}$ | B | $20.5$ | $16.4$ | $-0.76$ | $\mathbf{60}$ | C | $13.6$ | $10.9$ | $-0.70$ |
| $\mathbf{43}$ | A | $26.5$ | $21.2$ | $+0.58$ | $\mathbf{52}$ | B | $19.8$ | $15.8$ | $-0.76$ | $\mathbf{61}$ | C | $13.0$ | $10.4$ | $-0.60$ |
| $\mathbf{44}$ | A | $27.1$ | $21.7$ | $+0.58$ | $\mathbf{53}$ | B | $19.0$ | $15.2$ | $-0.76$ | $\mathbf{62}$ | C | $12.4$ | $9.9$ | $-0.60$ |
| $\mathbf{45}$ | A | $\mathbf{27.7}$ | $\mathbf{22.2}$ | $0.00$^a | $\mathbf{54}$ | B | $18.3$ | $14.6$ | $-0.76$ | $\mathbf{63}$ | C | $11.8$ | $9.4$ | $-0.60$ |
| $\mathbf{46}$ | A | $26.4$ | $21.1$ | $-1.28$ | $\mathbf{55}$ | B | $17.5$ | $14.1$ | $-0.76$ | $\mathbf{64}$ | C | $11.2$ | $9.0$ | $-0.60$ |
| $\mathbf{47}$ | A | $25.1$ | $20.1$ | $-1.28$ | $\mathbf{56}$ | B | $16.7$ | $13.4$ | $-0.78$ | $\mathbf{65}$ | C | $10.6$ | $8.5$ | $-0.60$ (Natl Max $h$) |
| $\mathbf{48}$ | A | $23.9$ | $19.1$ | $-1.28$ | $\mathbf{57}$ | B | $15.9$ | $12.8$ | $-0.78$ | — | — | — | — | — |
| ^aPeak conjugate focus of Stage 1–2 ellipsoid occurs at $h=45.0 cm$ ($\mathrm{TG}_{125}=27.7 °C$); at $h=40–44 cm$, steep off-axis angles slightly reduce single-bounce capture. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

### Worked Example — 15-Second National Tournament 1-cm Lookup & Linear Interpolation `[Rule 4.c.iii / §16.3]`

At the 2027 National Tournament (`Rule 4.c.iii`), the ES announces $h_{\mathrm{bulb}} = 53.0 cm$, heating time $t_{\mathrm{heat}} = 14.0 min$ ($840 s$), room temperature $T_{\mathrm{room}} = 21.5 °C$, and a $100 W$ clear $\mathrm{R40}$ heat lamp. The team's starting water temperature is $T_{\mathrm{start}} = 21.0 °C$, and post-lamp extraction cooling is $\Delta T_{\mathrm{cool}} = 0.18 °C$. Compute $T_{\mathrm{pred}}$ both by direct lookup in Table `tab:16:natl-1cm` and by linear interpolation between the $h=50 cm$ and $h=55 cm$ rows of Table `tab:16:doe-36`.

**Solution.**
1. **From Table `tab:16:natl-1cm` (or Linear Interpolation between $50 cm$ and $55 cm$):**
At $h = 50.0 cm$, $\mathrm{TG}_{100}(10 min) = 17.10 °C$; at $h = 55.0 cm$, $\mathrm{TG}_{100}(10 min) = 14.10 °C$. Interpolating to $h = 53.0 cm$ (fraction $\xi = (53-50)/(55-50) = 0.600$):

$$
\mathrm{TG}_{100}(53 cm, 10 min) = 17.10 + 0.600(14.10 - 17.10) = \mathbf{15.30 °C} \quad (\text{matches Table `tab:16:natl-1cm` entry }15.2 °C\text{ within }0.1 °C)
$$

2. **Scale to $t = 14.0 min$ using $M_{14} = 1.247$ ($k_{\mathrm{start}} = 0.395, k_{\mathrm{room}} = 0.605$) from Table `tab:16:doe-36`:**

$$
\mathrm{TG}_{\mathrm{table}}(53 cm, 100 W, 14 min) = 15.30 \times 1.247 = \mathbf{19.08 °C}
$$

3. **Apply Superposition Eq. Eq. (`eq:16:fast-superposition`) for $T_{\mathrm{start}} = 21.0 °C, T_{\mathrm{room}} = 21.5 °C$:**

$$
T_{\mathrm{pred}} = 21.00 + 19.08 + 0.605(21.50 - 21.00) - 0.18 = 40.08 + 0.30 - 0.18 = \mathbf{40.20 °C \longrightarrow \text{Submit }40.2 °C}
$$

**✓ Verified by:** Exact formula evaluation $T_{\mathrm{pred}} = 21.0 + 15.30(1 - e^{-840/903})/(1 - e^{-600/903}) + 0.6052(0.50) - 0.18 = 40.204 °C$; asserted in `check_sec14_16.py`.

**Table:** Complete $125 W$ Lamp Temperature-Gain Matrix $\mathrm{TG}_{\mathrm{table}}(h, t)$ $[°C]$ across all 6 State/National heating durations ($t = 10–15 min$)  **[S01,S12]**.

| **$h$** | **Slot** | **$10 min$** | **$11 min$** | **$12 min$** | **$13 min$** | **$14 min$** | **$15 min$** | **$\Delta T_{\mathrm{ss}}$** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $[cm]$ |  | $[°C]$ | $[°C]$ | $[°C]$ | $[°C]$ | $[°C]$ | $[°C]$ | $[°C]$ |
| $\mathbf{40}$ | A | $24.8$ | $26.5$ | $28.1$ | $29.6$ | $30.9$ | $32.2$ | $51.1$ |
| $\mathbf{45}$ | A | $\mathbf{27.7}$ | $\mathbf{29.6}$ | $\mathbf{31.4}$ | $\mathbf{33.0}$ | $\mathbf{34.5}$ | $\mathbf{36.0}$ | $57.1$ |
| $\mathbf{50}$ | B | $21.3$ | $22.8$ | $24.1$ | $25.4$ | $26.6$ | $27.7$ | $43.9$ |
| $\mathbf{55}$ | B | $17.5$ | $18.7$ | $19.8$ | $20.9$ | $21.8$ | $22.7$ | $36.0$ |
| $\mathbf{60}$ | C | $13.6$ | $14.5$ | $15.4$ | $16.2$ | $17.0$ | $17.7$ | $28.0$ |
| $\mathbf{65}$ | C | $10.6$ | $11.3$ | $12.0$ | $12.6$ | $13.2$ | $13.8$ | $21.8$ |

**Table:** Complete $100 W$ Lamp Temperature-Gain Matrix $\mathrm{TG}_{\mathrm{table}}(h, t)$ $[°C]$ across all 6 State/National heating durations ($t = 10–15 min$)  **[S01,S12]**.

| **$h$** | **Slot** | **$10 min$** | **$11 min$** | **$12 min$** | **$13 min$** | **$14 min$** | **$15 min$** | **$\Delta T_{\mathrm{ss}}$** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $[cm]$ |  | $[°C]$ | $[°C]$ | $[°C]$ | $[°C]$ | $[°C]$ | $[°C]$ | $[°C]$ |
| $\mathbf{40}$ | A | $19.8$ | $21.2$ | $22.4$ | $23.6$ | $24.7$ | $25.7$ | $40.8$ |
| $\mathbf{45}$ | A | $\mathbf{22.2}$ | $\mathbf{23.7}$ | $\mathbf{25.1}$ | $\mathbf{26.5}$ | $\mathbf{27.7}$ | $\mathbf{28.8}$ | $45.7$ |
| $\mathbf{50}$ | B | $17.1$ | $18.3$ | $19.4$ | $20.4$ | $21.3$ | $22.2$ | $35.2$ |
| $\mathbf{55}$ | B | $14.1$ | $15.1$ | $16.0$ | $16.8$ | $17.6$ | $18.3$ | $29.0$ |
| $\mathbf{60}$ | C | $10.9$ | $11.6$ | $12.3$ | $13.0$ | $13.6$ | $14.2$ | $22.5$ |
| $\mathbf{65}$ | C | $8.5$ | $9.1$ | $9.6$ | $10.1$ | $10.6$ | $11.0$ | $17.5$ |

### [2027 HEAT-COLLECTOR DEVICE & LAB: Class III Programmable Calculator Solver (`THERMO27`, Permitted Under Rule 2.b)]

Because Rule `2.b` permits up to **two Class III programmable/graphing calculators** (TI-84 Plus CE, TI-Nspire CX II, HP Prime, Casio fx-9750GIII) during any part of the event  **[S01]**, pre-load the following 10-line TI-BASIC verification script `PRGM:THERMO27` on both calculators to cross-check your paper lookup in $5 s$:
`:Prompt H,P,T,S,R,W`   {*// Input Bulb $h$ (cm), Wattage $P$ (W), Time $t$ (min), $T_{\mathrm{start}}$ (C), $T_{\mathrm{room}}$ (C), Wait $W$ (s)*} \\
`:If H<=45:Then:24.8+0.58*(H-40)->G:Else:If H<=50:Then:27.7-1.28*(H-45)->G:` \\
`:Else:If H<=55:Then:21.3-0.76*(H-50)->G:Else:If H<=60:Then:17.5-0.78*(H-55)->G:` \\
`:Else:13.6-0.60*(H-60)->G:End:End:End:End`   {*// Piecewise $1 cm$ National Curve $\Delta T_{\mathrm{ref}}(h)$*} \\
`:G*(P/125)*(1-e\^{}(-60*T/903))/(1-e\^{}(-600/903))->D`   {*// Wattage & Exponential Time Scaling*} \\
`:(1-e\^{}(-60*T/903))*(R-S)->A : 0.05+0.018*W->C`   {*// Ambient Offset $\Delta T_{\mathrm{amb}}$ & Post-Lamp Cooling*} \\
`:Disp "TG=",round(D+A-C,2),"TPRED=",round(S+D+A-C,1)`   {*// Output $\mathrm{TG}$ and Rounded $T_{\mathrm{pred}}$ to $0.1 °C$*}

## Post-Lamp-Off 1-Minute Cooling Correction & ES Thermometer Alignment

Under **Rule `5.II.g`**, at the end of Heating Time the Event Supervisor turns **OFF** the heat lamp, the team completely removes the cup from the device (including removing all unattached wrap/glazing), and the ES measures $T_{\mathrm{final}}$ within a target window of **up to 1 minute ($0–60 s$)**  **[S01,S05]**. During this waiting window $t_{\mathrm{wait}}$, the newly exposed hot top water layer ($T_{\mathrm{top},0} \approx 35–55 °C$) loses heat simultaneously upward to room air (by unglazed evaporation $\dot{Q}_{\mathrm{evap}}$, convection $\dot{Q}_{\mathrm{conv}}$, and radiation $\dot{Q}_{\mathrm{rad}}$) and downward into the cooler bottom water layer ($\dot{Q}_{12} = (T_{\mathrm{top}} - T_{\mathrm{bot}})/R_{12}$).

### [FORMULA & DECISION CARD: Post-Lamp-Off Top-Layer Cooling Rate & Two-Stage Waiting-Window Correction]

| **Formula** | **Variables (SI units)** | **Flags** | **Use when** |
| --- | --- | --- | --- |
| $r_{\mathrm{open}}(T_{\mathrm{top}}) = -\!\left(\dfrac{dT_{\mathrm{top}}}{dt}\right)_{\!\mathrm{open}} = \dfrac{\dot{Q}_{\mathrm{evap}} + \dot{Q}_{\mathrm{conv}} + \dot{Q}_{\mathrm{rad}} + \dot{Q}_{12}}{C_{\mathrm{skin}}}$ | $C_{\mathrm{skin}} \approx 140 J/K$: upper $12 mm$ water layer; $r_{\mathrm{open}} \approx 0.012 °C/s$ at $35 °C$, $0.018 °C/s$ at $43 °C$, and $0.025 °C/s$ at $50 °C$. | **[CLOSED]** | Cooling rate of bare cup sitting on Testing Surface waiting for ES thermometer probe (`5.II.g`). |
| $r_{\mathrm{closed}}(T_{\mathrm{top}}) = -\!\left(\dfrac{dT_{\mathrm{top}}}{dt}\right)_{\!\mathrm{closed}} = \dfrac{\dot{Q}_{\mathrm{loss,glazed}} + \dot{Q}_{12}}{C_{\mathrm{top}}}$ | Inside closed glazed collector before hood removal: $r_{\mathrm{closed}} \approx 0.005–0.008 °C/s$ ($3\times$ slower than open cup!). | **[CLOSED]** | If ES is busy at another station when lamp turns off, wait until ES walks over before lifting hood (within $60 s$)! |
| $\Delta T_{\mathrm{cool}}(t_{\mathrm{closed}}, t_{\mathrm{open}}) = r_{\mathrm{closed}}\,t_{\mathrm{closed}} + r_{\mathrm{open}}\,t_{\mathrm{open}} + \delta_{\mathrm{probe}}$ | $t_{\mathrm{closed}}$: delay before lifting hood $[s]$; $t_{\mathrm{open}}$: open-cup exposure before peak probe reading $[s]$; $\delta_{\mathrm{probe}}$: probe heat-drain/depth offset $[°C]$. | **[2027-RULE]** | Subtract $\Delta T_{\mathrm{cool}}$ (typically $0.18–0.45 °C$) from end-of-heating $T_{\mathrm{top}}(t_{\mathrm{heat}})$ to match ES readout! |

> **[Vector Figure: Post-lamp-off top-layer temperature drop $-\Delta T_{\mathrm{cool}}(t_{\mathrm{wait}})$ during the Rule `5.II.g` 1-minute final measurement window  **[S01,S12]**. | Label: `fig:16:postheat-cooling`]**
> - **Diagram Annotations & Key Elements:** **X-Axis:** Post-Lamp-Off Measurement Delay $t_{\mathrm{wait}}$ $[s]$ (Rule `5.II.g`) • **Y-Axis:** Top-Layer Cooling Drop $-\Delta T_{\mathrm{cool}}$ $[°C]$ • **Legend:** Bare Cup Open at $50 °C$ ($-0.025 °C/s$) • **Legend:** Bare Cup Open at $43 °C$ ($-0.018 °C/s$) • **Legend:** Bare Cup Open at $35 °C$ ($-0.012 °C/s$) • **Legend:** Hood Closed Until $t=40 s$ ($50 °C$) • Fast Extraction ($6–15 s$)

**Table:** ES thermometer technology offsets $\delta_{\mathrm{probe}}$ relative to a $z=8 mm$ digital thermistor tip (Rule `4.f`, Clarif. #4)  **[S01,S02,S22]**.

| **ES Thermometer Type (`4.f`)** | **Depth $z_p$** | **$\tau_p$** | **Offset $\delta_{\mathrm{probe}}$** | **Stratification & Emissivity Mechanism** |
| --- | --- | --- | --- | --- |
|  | $[mm]$ | $[s]$ | $[°C]$ |  |
| **1. NTC Digital Thermistor** | $5\text{--}10$ | $1.8$ | $\mathbf{0.00}$ | **Reference ES Probe:** Tiny tip bead reads peak top layer in $9 s$. |
| **2. Bare Type-K Thermocouple** | $3\text{--}6$ | $0.2$ | $\mathbf{+0.15 °C}$ | Zero thermal drain; reads hotter upper $4 mm$ skin instantaneously. |
| **3. Non-Contact IR Pyrometer** | $0.015$ | $0.3$ | $\mathbf{-0.25 °C}$ | Reads $\varepsilon_w=0.96$ evaporative surface skin (**remove BoPET cap first!**). |
| **4. Sheathed Pt100 RTD** | $18\text{--}30$ | $5.0$ | $\mathbf{-1.40 °C}$ | Long $25 mm$ stem averages across upper thermocline + stem drain. |
| **5. Spirit Glass Thermometer** | $20\text{--}40$ | $8.5$ | $\mathbf{-2.10 °C}$ | Deep bulb immersion + slow $5\tau_p=42 s$ lag averages into middle water. |

### Worked Example — Post-Lamp-Off Staggered Station Cooling & ES Probe Offset Correction `[Rule 4.f, 5.II.g / §16.4]`

At the end of a $10.0 min$ run ($h=45.0 cm, 125 W$ lamp), the water in your collector reaches a true top-layer peak temperature of $T_{\mathrm{top}}(600 s) = 49.92 °C$ at lamp turn-off. Because four lamp stations are running simultaneously (`Rule 4.b`), you observe during check-in that your station will be measured third by the ES ($\approx28 s$ after lamp turn-off), and the ES is using a standard NTC digital thermistor probe ($\delta_{\mathrm{probe}} = 0.00 °C$, settling time $8 s$). Compare the final ES thermometer reading $T_{\mathrm{final}}$ if: (a) you immediately remove the cup at $t_{\mathrm{wait}}=0 s$ so it sits uncovered on the table for $t_{\mathrm{open}} = 28 + 8 = 36 s$ ($r_{\mathrm{open}} = 0.0245 °C/s$ plus initial extraction transient $\delta_{\mathrm{ext}} = 0.05 °C$); versus (b) you keep the insulated hood + BoPET cap closed for $t_{\mathrm{closed}} = 22 s$ ($r_{\mathrm{closed}} = 0.0070 °C/s$) and extract the cup in $6 s$ just as the ES arrives ($t_{\mathrm{open}} = 6 + 8 = 14 s$).

**Solution.**
(a) **Immediate Open Extraction ($t_{\mathrm{closed}}=0 s, t_{\mathrm{open}}=36 s$):**

$$
\Delta T_{\mathrm{cool,A}} = \delta_{\mathrm{ext}} + r_{\mathrm{open}}t_{\mathrm{open}} = 0.05 + (0.0245)(36) = \mathbf{0.932 °C} \implies T_{\mathrm{final,A}} = 49.92 - 0.932 = \mathbf{48.99 °C}
$$

(b) **Delayed Hood Lift Coordinated with ES Arrival ($t_{\mathrm{closed}}=22 s, t_{\mathrm{open}}=14 s$):**

$$
\Delta T_{\mathrm{cool,B}} = \delta_{\mathrm{ext}} + r_{\mathrm{closed}}t_{\mathrm{closed}} + r_{\mathrm{open}}t_{\mathrm{open}} = 0.05 + (0.0070)(22) + (0.0245)(14) = 0.05 + 0.154 + 0.343 = \mathbf{0.547 °C}
$$

giving $T_{\mathrm{final,B}} = 49.92 - 0.547 = \mathbf{49.37 °C}$ (preserving $+0.38 °C$ of extra Temperature Gain while completing extraction and measurement at $22 + 14 = 36 s \le 60 s$ per Rule `5.II.g`!).

**✓ Verified by:** Piecewise linear cooling integral $\int_0^{t_w} r(t)\,dt$; asserted in `check_sec14_16.py`.

**Table:** Combined post-lamp waiting-window and ES thermometer-type subtraction matrix $\Delta T_{\mathrm{cool,tot}} = \Delta T_{\mathrm{wait}} - \delta_{\mathrm{probe}}$ $[°C]$ ($T_{\mathrm{top}}\approx46 °C$)  **[S01,S02,S12]**.

| **ES Station Measurement Order** | **Thermistor** | **Bare TC** | **IR Gun** | **Pt100 RTD** | **Recommended Hood** |
| --- | --- | --- | --- | --- | --- |
| (Total Wait $t_{\mathrm{wait}}$ in `5.II.g`) | ($z\!=\!8 mm$) | ($z\!=\!4 mm$) | (Skin) | ($z\!=\!22 mm$) | **Lift Strategy** |
| **1st Station** ($t_{\mathrm{open}}=8 s$) | $-0.20 °C$ | $-0.05 °C$ | $-0.45 °C$ | $-1.60 °C$ | Lift hood immediately at $t=0$. |
| **2nd Station** ($t_{\mathrm{wait}}=20 s$) | $-0.31 °C$ | $-0.16 °C$ | $-0.56 °C$ | $-1.71 °C$ | Keep hood closed $12 s$, lift in $6 s$. |
| **3rd Station** ($t_{\mathrm{wait}}=35 s$) | $-0.46 °C$ | $-0.31 °C$ | $-0.71 °C$ | $-1.86 °C$ | Keep hood closed $25 s$, lift in $6 s$. |
| **4th Station** ($t_{\mathrm{wait}}=50 s$) | $-0.61 °C$ | $-0.46 °C$ | $-0.86 °C$ | $-2.01 °C$ | Keep hood closed $40 s$, lift in $6 s$. |
| **Uncovered 50 s Wait (Trap)** | $-1.18 °C$ | $-1.03 °C$ | $-1.43 °C$ | $-2.58 °C$ | Loses $0.57 °C$ to open air! |

### [TRAP & DIAGNOSTIC: IR Pyrometer Plastic-Wrap & $D\!:\!S$ Trap]

Under Rule `4.f`, the ES may use a **non-contact infrared (IR) thermometer** ($\lambda \in [8 µm, 14 µm]$, fixed preset $\varepsilon_{\mathrm{set}} = 0.95$). Liquid water has $\varepsilon_w = 0.96$ in this band  **[S12]**, so an IR gun reads bare water accurately within $0.2 °C$:

$$
T_{\mathrm{IR}} = \left[\frac{\varepsilon_w T_w^4 + (1-\varepsilon_w)T_{\mathrm{amb}}^4}{\varepsilon_{\mathrm{set}}}\right]^{1/4}
$$

**Two Fatal IR Pitfalls:** (1) If any BoPET or cling wrap is left over the cup mouth, the IR gun reads the **cooler plastic film temperature** ($-4–7 °C$ error + $\times 0.9$ Rule `5.II.g` violation!). (2) With a typical distance-to-spot ratio $D\!:\!S = 12\!:\!1$, the IR gun must be held $\le45 cm$ above the $7.5 cm$ cup mouth so the optical spot does not spill onto the table!

## Repeatability Statistics, Mismatch Recovery & Design Revision Log

### Pre-Tournament Repeatability Protocol & Bias–Variance Diagnostics

Before locking the binder's lookup tables, every collector must complete a **6-trial replicate repeatability block** at the primary reference condition ($h = 45.0 cm, P_{\mathrm{bulb}} = 125 W, t = 10.0 min$) alongside the 36-condition DOE grid. Using JCGM GUM (`[S21]`) and Ordinary Least Squares (OLS) residual diagnostics (§`sec:18`):

$$
\begin{aligned}

  \mathrm{MSE}(T_{\mathrm{pred}}) = \mathbb{E}\!\left[(T_{\mathrm{final}} - T_{\mathrm{pred}})^2\right] = \underbrace{\left(\bar{T}_{\mathrm{final}} - T_{\mathrm{pred}}\right)^2}_{\mathrm{Bias}^2\text{ (Systematic Model Error)}} + \underbrace{s_{\mathrm{rep}}^2\left(1 + \frac{1}{n}\right)}_{\text{Irreducible Run-to-Run Variance }\sigma_{\mathrm{run}}^2}
\end{aligned}
$$

Eliminating systematic model bias ($\mathrm{Bias} \to 0$) via residual diagnostics leaves only the irreducible run-to-run repeatability standard deviation $s_{\mathrm{rep}} \approx 0.12–0.18 °C$, corresponding to an expected absolute error $\mathbb{E}[|\Delta T_{\mathrm{err}}|] = \sqrt{2/\pi}\,s_{\mathrm{rep}} \approx 0.7979\,s_{\mathrm{rep}} \approx 0.11 °C$ ($\mathrm{PE} \ge 0.9975$!).

### Worked Example — Six-Trial Repeatability Statistics, $95\%$ Prediction Interval & Expected $\mathrm{PE}$ `[GUM / §16.5]`

In six replicate $10.0 min$ calibration trials at $h = 45.0 cm$ ($125 W$ lamp, normalized to $T_{\mathrm{start}} = T_{\mathrm{room}} = 22.0 °C$), our glazed 3-stage CPC collector produces measured final top-layer temperatures $T_{f,i} \in \{49.6, 49.8, 49.7, 49.5, 49.9, 49.7\}\,°C$. Compute: (a) the sample mean $\bar{T}_f = T_{\mathrm{pred}}$, sample standard deviation $s_{\mathrm{rep}}$, Type A standard uncertainty of the mean $u_A(\bar{T}_f) = s_{\mathrm{rep}}/\sqrt{n}$, and single-future-run prediction standard uncertainty $u_{\mathrm{run}} = s_{\mathrm{rep}}\sqrt{1 + 1/n}$; and (b) the expected tournament Prediction Estimate $\mathbb{E}[\mathrm{PE}] = 1 - \frac{\sqrt{2/\pi}\,u_{\mathrm{run}}}{\bar{T}_f}$.

**Solution.**
(a) The sample mean of the $n = 6$ trials is:

$$
\bar{T}_f = \frac{49.6 + 49.8 + 49.7 + 49.5 + 49.9 + 49.7}{6} = \mathbf{49.700 °C} \quad (\mathrm{TG}_{\mathrm{ref}} = \mathbf{27.700 °C})
$$

The residuals $r_i = T_{f,i} - \bar{T}_f$ are $\{-0.1, +0.1, 0.0, -0.2, +0.2, 0.0\}\,°C$, giving sum of squared residuals $\sum r_i^2 = 0.01 + 0.01 + 0 + 0.04 + 0.04 + 0 = 0.1000 °C^2$. With $\nu = n - 1 = 5$ degrees of freedom:

$$
s_{\mathrm{rep}} = \sqrt{\frac{0.1000}{5}} = \mathbf{0.1414 °C}, \qquad
  u_A(\bar{T}_f) = \frac{0.1414}{\sqrt{6}} = \mathbf{0.0577 °C}, \qquad
  u_{\mathrm{run}} = 0.1414\sqrt{1 + \frac{1}{6}} = \mathbf{0.1528 °C}
$$

(b) For a future tournament run under identical conditions, the expected absolute prediction error is $\mathbb{E}[|\Delta T_{\mathrm{err}}|] = \sqrt{2/\pi}\,u_{\mathrm{run}} = 0.79788(0.1528) = \mathbf{0.1219 °C}$, yielding an expected Prediction Estimate of:

$$
\mathbb{E}[\mathrm{PE}] = 1 - \frac{0.1219}{49.700} = \mathbf{0.99755} \quad (\text{earning }\mathbf{19.95 pts}\text{ out of }20.00 pts!)
$$

**✓ Verified by:** Student-$t$ $95\%$ prediction interval ($\pm t_{0.975,5}u_{\mathrm{run}} = \pm 2.571 \times 0.1528 = \pm0.393 °C$); asserted in `check_sec14_16.py`.

### Tournament-Condition Mismatch Recovery Protocol (Rule 5.II.a Bulb & Venue Variations)

At an invitational, Regional, State, or National tournament, the Event Supervisor announces the **bulb specifications (including wattage and physical measurements)** at the start of the block (`Rule 5.II.a.v`). If the tournament's heat-lamp bulb shape, external clamp-reflector diameter, or room airflow differs from your home lab's baseline $125 W$ $\mathrm{R40}$ flood lamp, multiply $\mathrm{TG}_{\mathrm{table}}(h, P_{\mathrm{bulb}}, t)$ by the **Bulb & Venue Mismatch Recovery Factor $\kappa_{\mathrm{mismatch}} = \kappa_{\mathrm{beam}}\times\kappa_{\mathrm{hood}}\times\kappa_{\mathrm{draft}}$** from Table `tab:16:mismatch-recovery`:

$$
\begin{aligned}

  \boxed{\mathrm{TG}_{\mathrm{adjusted}}(h, P_{\mathrm{bulb}}, t) = \kappa_{\mathrm{beam}}\,\kappa_{\mathrm{hood}}\,\kappa_{\mathrm{draft}}\,\left(\frac{P_{\mathrm{bulb,announced}}}{125.0 W}\right)\,\mathrm{TG}_{125\mathrm{W,table}}(h, t)}
\end{aligned}
$$

**Table:** Day-of tournament bulb-shape, clamp-reflector, and venue mismatch recovery multipliers (Rule `5.II.a.v`)  **[S01,S05,S12]**.

| **Announced ES Condition (`5.II.a.v`)** | **Physical Observation / Measure** | **Factor** | **Multiplier** | **Physical Mechanism & 3-Min Setup Action** |
| --- | --- | --- | --- | --- |
|  |  |  | ($h\!=\!45 cm / 60 cm$) |  |
| **1. Standard Clear R40 Flood** (Baseline Reference Bulb) | $\text{Ø}12.7 cm$ ($5.0 in$) flat/soft-crown reflector bulb, $\mathrm{MOL}=16.5 cm$ | $\kappa_{\mathrm{beam}}$ | $\mathbf{1.000 / 1.000}$ | Exact baseline of Table `tab:16:doe-36` and Table `tab:16:natl-1cm`; no beam correction needed. |
| **2. Clear BR40 Wide Flood** (Bulged Reflector Neck) | $\text{Ø}12.7 cm$ face with wider inner neck reflector contour ($\theta_{1/2}\approx 42^\circ$) | $\kappa_{\mathrm{beam}}$ | $\mathbf{0.955 / 0.920}$ | Slightly wider beam spill outside $29.6 cm$ aperture at high $h$; use Slot A/B. |
| **3. Clear PAR38 Pressed-Glass** (Collimated Flood/Spot) | Heavy fluted pressed-glass lens face, $\text{Ø}12.1 cm$ ($4.75 in$, $\theta_{1/2}\approx 22^\circ$) | $\kappa_{\mathrm{beam}}$ | $\mathbf{1.085 / 1.160}$ | Narrower beam concentrates more flux directly into central funnel & cup mouth! |
| **4. Non-Reflector Clear A19 / PS25 Bulb in Clamp Hood** | Small clear pear bulb ($\text{Ø}6.0–8.0 cm$) relying on external metal clamp hood | $\kappa_{\mathrm{beam}}$ | $\mathbf{0.780 / 0.710}$ | Isotropic filament relies on spun-Al clamp hood ($\rho_{\mathrm{spec}}\approx 0.55$); wide diffuse beam. |
| **5. Intermediate Wattage Bulb** (e.g., $110 W$ or $120 W$ rated) | Announced wattage $P_{\mathrm{bulb}} \notin \{100, 125\}\,W$ | $\eta_P$ | $\mathbf{P_{\mathrm{bulb}} / 125}$ | Linear power scaling $\eta_P = P_{\mathrm{bulb}}/125 W$ (e.g., $115 W \implies \eta_P = 0.920$). |
| **6. Deep $10.5 in$ vs. Shallow $8.5 in$ Clamp Hood** | ES clamp reflector lip extends below vs. behind R40 bulb face | $\kappa_{\mathrm{hood}}$ | $\mathbf{1.030 / 1.000}$ | Deep $10.5 in$ hood recaptures peripheral R40 side-spill at close height $h\le45 cm$. |
| **7. High-Velocity Lab Exhaust / AC Draft** | Noticeable cross-draft ($u_\infty > 0.5 m/s$) across testing table | $\kappa_{\mathrm{draft}}$ | $\mathbf{0.975 / 0.970}$ | Increases external glazing $h_{\mathrm{ext}}$ slightly; BoPET cap protects internal water! |

### Worked Example — Tournament Bulb-Shape Mismatch Recovery: PAR38 Narrow-Beam Bulb Announcement `[Rule 5.II.a.v / §16.5]`

At an Invitational tournament, the ES announces (`Rule 5.II.a`): $h_{\mathrm{bulb}} = 60.0 cm$, $t_{\mathrm{heat}} = 12.0 min$, $T_{\mathrm{room}} = 22.0 °C$, and a **$100 W$ clear $\mathrm{PAR38}$ pressed-glass flood heat lamp** ($\text{Ø}12.1 cm$, narrow $\theta_{1/2}=22°$ beam, $\kappa_{\mathrm{beam}}(60 cm) = 1.160$ from Table `tab:16:mismatch-recovery`, $\kappa_{\mathrm{hood}} = \kappa_{\mathrm{draft}} = 1.000$). When the water cup is dispensed (`Rule 5.II.c`), $T_{\mathrm{start}} = 22.0 °C$ and expected extraction cooling is $\Delta T_{\mathrm{cool}} = 0.15 °C$. Compute (a) the unadjusted $\mathrm{R40}$ table prediction, (b) the $\mathrm{PAR38}$ mismatch-corrected prediction $T_{\mathrm{pred}}$, and (c) the $\mathrm{PS}$ points saved by applying $\kappa_{\mathrm{beam}} = 1.160$.

**Solution.**
(a) From Table `tab:16:doe-36` at $h = 60.0 cm$, $P_{\mathrm{bulb}} = 100 W$, $t = 12.0 min$, the baseline $\mathrm{R40}$ temperature gain is $\mathrm{TG}_{\mathrm{R40}} = 12.40 °C$, which would predict $T_{\mathrm{pred,unadj}} = 22.00 + 12.40 - 0.15 = \mathbf{34.25 °C}$.

(b) Applying the $\mathrm{PAR38}$ collimation factor $\kappa_{\mathrm{beam}}(60 cm) = 1.160$ from Eq. Eq. (`eq:16:mismatch-recovery`):

$$
\mathrm{TG}_{\mathrm{adj}} = 1.160 \times 12.40 °C = \mathbf{14.384 °C} \implies T_{\mathrm{pred,adj}} = 22.00 + 14.384 - 0.15 = \mathbf{36.23 °C \longrightarrow \text{Submit }36.2 °C}
$$

(c) When the true final temperature measures $T_{\mathrm{final}} = 36.2 °C$, the mismatch-adjusted prediction earns $\mathrm{PE}_{\mathrm{adj}} = 1.0000$ ($\mathbf{20.00 pts}$), whereas the unadjusted $\mathrm{R40}$ prediction ($34.3 °C$, error $1.9 °C$) would earn $\mathrm{PE}_{\mathrm{unadj}} = 1 - 1.9/36.2 = 0.9475$ ($18.95 pts$)—saving $\mathbf{+1.05 pts}$ on $\mathrm{PS}$!

**✓ Verified by:** Ratio check $\Delta\mathrm{PS} = 20(\kappa_{\mathrm{beam}}-1)\mathrm{TG}_{\mathrm{R40}}/T_{\mathrm{final}} = 20(0.160)(12.40)/36.23 = 1.095 pts$; asserted in `check_sec14_16.py`.

**Table:** Physical collector design-iteration version-control ledger and 10-run blind validation summary  **[S01,S02,S04]**.

| **Build Rev.** | **Collector Configuration & Key Change** | **$\dot{Q}_{\mathrm{abs}}$^a** | **$R_{\mathrm{th,eff}}$** | **$\mathrm{TG}_{\mathrm{ref}}$^a** | **Blind $\mathrm{MAE}$** | **Experimental Finding & Action Taken** |
| --- | --- | --- | --- | --- | --- | --- |
|  |  | $[W]$ | $[K/W]$ | $[°C]$ | $[°C]$ |  |
| **Rev v0.0** | Bare $9 oz$ Clear Cup on Table (Control) | $1.44$ | $1.15$ | $+1.8$ | $0.18$ | Baseline control; $98.3\%$ of lamp rays miss cup mouth; high evaporation. |
| **Rev v1.0** | Open $30^\circ$ Straight Cone (Dull Al Foil) | $4.80$ | $1.85$ | $+8.1$ | $0.45$ | $\theta_k = \theta_{\mathrm{in}}+60^\circ > 90^\circ$ rejected $73\%$ of rays; evaporative cooling lost $5 °C$. |
| **Rev v2.0** | Steep $15^\circ$ Cone (Shiny Foil) + Cork Base | $14.80$ | $2.41$ | $+18.4$ | $0.32$ | Shiny foil + steeper wall tripled ray capture; uncovered mouth still steamed. |
| **Rev v3.0** | 3-Stage Finite Ellipsoid/CPC + $3\times$ Foil-Air | $26.40$ | $2.45$ | $+20.1$ | $0.26$ | $F_1\to F_2$ conjugate focus achieved $41.4\%$ beam capture; top skin cooled by air. |
| **Rev v4.0** | **Championship Glazed 3-Stage CPC + 3-Slot Bay + Lift-Off BoPET Hood** | $\mathbf{24.00}$ | $\mathbf{4.20}$ | $\mathbf{+27.7}$ | $\mathbf{0.13}$ | **FINAL PRODUCTION BUILD:** BoPET cap cut evaporation $98\%$ ($+7.6 °C$ boost); 10 blind runs across $h=40–65 cm$ achieved $\overline{\mathrm{PE}}=\mathbf{0.9971}$ ($19.94 /20 pts$)! |
| ^aEvaluated at reference benchmark $h_{\mathrm{bulb}}=45.0 cm, P_{\mathrm{bulb}}=125 W, t_{\mathrm{heat}}=10.0 min, T_{\mathrm{start}}=T_{\mathrm{room}}=22.0 °C$. |  |  |  |  |  |  |

**Table:** Ten-run randomized blind validation log for **Rev v4.0** across Regional, State, and National conditions  **[S01,S04]**.

| **Run** | **$h$** | **$P$** | **$t$** | **$T_{\mathrm{start}}$** | **$T_{\mathrm{room}}$** | **$T_{\mathrm{pred}}$** | **$T_{\mathrm{final}}$** | **Residual & $\mathrm{PE}$** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | $[cm]$ | $[W]$ | $[min]$ | $[°C]$ | $[°C]$ | $[°C]$ | $[°C]$ | $r_k$ $[°C]$ / $\mathrm{PE}$ |
| **B01** | $40$ | $125$ | $10$ | $21.8$ | $22.0$ | $46.5$ | $46.6$ | $+0.1 °C$ / $0.9979$ |
| **B02** | $45$ | $125$ | $10$ | $22.2$ | $22.2$ | $49.7$ | $49.7$ | $\mathbf{0.0 °C}$ / $\mathbf{1.0000}$ |
| **B03** | $50$ | $125$ | $10$ | $19.5$ | $22.4$ | $42.0$ | $41.8$ | $-0.2 °C$ / $0.9952$ |
| **B04** | $45$ | $100$ | $10$ | $21.0$ | $21.2$ | $43.1$ | $43.2$ | $+0.1 °C$ / $0.9977$ |
| **B05** | $55$ | $125$ | $12$ | $22.5$ | $22.0$ | $41.9$ | $42.1$ | $+0.2 °C$ / $0.9952$ |
| **B06** | $42$ | $125$ | $15$ | $20.4$ | $21.8$ | $54.8$ | $54.7$ | $-0.1 °C$ / $0.9982$ |
| **B07** | $53$ | $100$ | $14$ | $21.0$ | $21.5$ | $40.2$ | $40.1$ | $-0.1 °C$ / $0.9975$ |
| **B08** | $58$ | $125$ | $13$ | $23.0$ | $22.6$ | $40.7$ | $40.9$ | $+0.2 °C$ / $0.9951$ |
| **B09** | $62$ | $125$ | $15$ | $21.6$ | $22.0$ | $37.7$ | $37.6$ | $-0.1 °C$ / $0.9973$ |
| **B10** | $65$ | $100$ | $11$ | $22.0$ | $22.0$ | $30.9$ | $31.0$ | $+0.1 °C$ / $0.9968$ |
| **10-Run Blind Validation Summary:** |  |  |  |  |  | $\mathrm{Bias}\!=\!+0.02^\circ$ | $\mathrm{MAE}\!=\!\mathbf{0.13^\circ}$ | $\overline{\mathrm{PE}}=\mathbf{0.9971}$ |

**Table:** Calibration residual diagnostic & troubleshooting matrix (§`sec:18`)  **[S21]**.

| **Residual Pattern ($r = T_f - T_{\mathrm{pred}}$)** | **Physical Cause & Parameter Fix** |
| --- | --- |
| **1. Concave-down curvature vs. $t_{\mathrm{heat}}$** ($r < 0$ at $15\text{ m}$) | $\tau_{\mathrm{eff}}$ set too large (under-estimating heat loss). Re-extract $\tau_{\mathrm{eff}}$ via 3-point formula (`ex:16.2b`). |
| **2. Positive jump across Consecutive Runs** | Device cradle still warm from previous trial (violates Rule `3.g` room-temp start!). Cool cradle $\ge15 min$ between trials. |
| **3. Negative drop at $h \ge 55 cm$** | Pedestal left in Slot A instead of raising to Slot B/C for high bulb height. |
| **4. High scatter ($s_{\mathrm{rep}} > 0.35 °C$)** | Inconsistent cup extraction swirling or variable probe depth $z_p$; standardize 2-finger vertical lift and $8 mm$ probe stop. |

### Fast 12-Run Calibration Protocol & Inverse Power-Law Height Curve Fit

When a team builds a new collector revision or replaces a reflector liner during the week before a tournament, re-running all 36 DOE cells is unnecessary. Because the 5-variable physical model Eq. Eq. (`eq:16:master-5var`) factors cleanly into **spatial optical capture** $\Delta T_{\mathrm{ref}}(h)$, **wattage ratio** $\eta_P(P_{\mathrm{bulb}})$, and **first-order temporal approach** $M_t(t; \tau_{\mathrm{eff}})$, the entire 36-cell matrix and 26-row National $1 cm$ table can be regenerated from a **12-Run Fast Calibration Block** ($\sim2.5 h$ of lab time using two alternating cup cradles so each cradle cools completely to room temperature between runs):
- **Runs 1–6 (Six-Height $125 W$ Spatial Anchor Curve at $t = 10.0 min$):** Measure $\mathrm{TG}_{125}$ at $h \in \{40, 45, 50, 55, 60, 65\}\,cm$ (recording $t_1 = 5.0 min$ and $t_2 = 10.0 min$ gains to extract $\tau_{\mathrm{eff}}$ via Worked Example `ex:16.2b`). Beyond the $h_{\mathrm{peak}} = 45.0 cm$ conjugate focal peak ($h \in [45 cm, 65 cm]$), the reference gain follows the closed-form **Inverse Effective-Distance Power Law**:
  
$$
\begin{aligned}

    \Delta T_{\mathrm{ref}}(h) = \Delta T_{\mathrm{ref}}(h_0)\!\left(\frac{h_0 - z_{\mathrm{eff}}}{h - z_{\mathrm{eff}}}\right)^{\!n} \implies \ln\Delta T_{\mathrm{ref}}(h) = \ln A_0 - n\ln(h - z_{\mathrm{eff}})
\end{aligned}
$$

  
  where $z_{\mathrm{eff}} \approx 19.5 cm$ is the effective optical centroid elevation of the 3-stage funnel and $n \approx 1.66$ is the distance exponent.
- **Runs 7–9 (Three-Height $100 W$ Wattage Ratio Verification at $h \in \{45, 50, 60\}\,cm$):** Verify $\eta_P = \overline{\mathrm{TG}_{100} / \mathrm{TG}_{125}} \approx 0.800 \pm 0.005$.
- **Runs 10–12 (Long-Duration $15.0 min$ Time-Constant & Post-Lamp Cooling Check at $h \in \{45, 55\}\,cm$):** Verify $M_{15} = \mathrm{TG}(15 min)/\mathrm{TG}(10 min) = 1.299$ and measure the post-lamp cooling slope $r_{\mathrm{open}}$ across $t_{\mathrm{wait}} \in [5 s, 60 s]$.

### Worked Example — Inverse Effective-Distance Power-Law Height Fit & National 1-cm Prediction `[Rule 4.c.iii, 5.d.i / §16.5]`

Using the calibrated $10.0 min$, $125 W$ anchor points at $h_1 = 45.0 cm$ ($\Delta T_{\mathrm{ref},1} = 27.70 °C$) and $h_2 = 65.0 cm$ ($\Delta T_{\mathrm{ref},2} = 10.60 °C$) with effective optical centroid elevation $z_{\mathrm{eff}} = 19.50 cm$: (a) solve algebraically for the power-law exponent $n$ and amplitude $A_0$ in $\Delta T_{\mathrm{ref}}(h) = A_0 / (h - z_{\mathrm{eff}})^n$; and (b) evaluate the power-law prediction at $h = 55.0 cm$ and compare against the measured DOE value $17.50 °C$ in Table `tab:16:doe-36`.

**Solution.**
(a) At $h_1 = 45.0 cm$ and $h_2 = 65.0 cm$, the effective distances above $z_{\mathrm{eff}} = 19.50 cm$ are $d_1 = 45.0 - 19.50 = 25.50 cm$ and $d_2 = 65.0 - 19.50 = 45.50 cm$. Taking the natural logarithm of the ratio $\Delta T_{\mathrm{ref},1} / \Delta T_{\mathrm{ref},2} = (d_2 / d_1)^n$:

$$
n = \frac{\ln(\Delta T_{\mathrm{ref},1} / \Delta T_{\mathrm{ref},2})}{\ln(d_2 / d_1)} = \frac{\ln(27.70 / 10.60)}{\ln(45.50 / 25.50)} = \frac{\ln(2.61321)}{\ln(1.78431)} = \frac{0.96058}{0.57903} = \mathbf{1.6589}, \qquad
  A_0 = \Delta T_{\mathrm{ref},1}\,d_1^n = \mathbf{5973.5}
$$

(b) Evaluating at $h = 55.0 cm$ in fixed Slot A ($d = 55.0 - 19.50 = 35.50 cm$) vs. raised **Slot B** ($d_{\mathrm{Slot\,B}} = 33.60 cm$):

$$
\Delta T_{\mathrm{ref,Slot\,A}}(55 cm) = 27.70\!\left(\frac{25.50}{35.50}\right)^{\!1.6589} = \mathbf{16.00 °C}, \qquad
  \Delta T_{\mathrm{ref,Slot\,B}}(55 cm) = 27.70\!\left(\frac{25.50}{33.60}\right)^{\!1.6589} = \mathbf{17.52 °C}
$$

matching the Slot B DOE table entry ($17.5 °C$) to within $\mathbf{0.02 °C}$ and proving why raising the pedestal to Slot B adds $+1.52 °C$!

**✓ Verified by:** Log-log slope identity $\ln(17.52/27.70)/\ln(33.60/25.50) = -1.6589 = -n$; asserted in `check_sec14_16.py`.

### [2027 HEAT-COLLECTOR DEVICE & LAB: 30-Second Day-Of Prediction Worksheet & Double-Check Protocol (Copy onto Prediction Scratchpad)]

Execute these five steps in sequence during the **3-Minute Device Setup Time** (`Steps 1–3`) and **first 60 seconds of Heating Time** (`Steps 4–5`):
- **Record ES Board Parameters (`5.II.a`):** $h_{\mathrm{bulb}} = <u>\hspace{1.1cm}</u>\,cm$, \quad $t_{\mathrm{heat}} = <u>\hspace{1.0cm}</u>\,min$, \quad $T_{\mathrm{room}} = <u>\hspace{1.1cm}</u>\,°C$, \quad $P_{\mathrm{bulb}} = <u>\hspace{1.1cm}</u>\,W$.
- **Set Pedestal Slot (`5.II.b`):** **Slot A** ($40–48 cm$) | **Slot B** ($49–57 cm$) | **Slot C** ($58–65 cm$). Center device crosshairs under cold bulb!
- **Lookup Base Gain & Weights (Table `tab:16:doe-36` / Table `tab:16:natl-1cm`):** $\mathrm{TG}_{10\mathrm{m}}(h, P_{\mathrm{bulb}}) = <u>\hspace{1.1cm}</u>\,°C \times M_t(t) <u>\hspace{1.0cm}</u> \times \kappa_{\mathrm{beam}} <u>\hspace{1.0cm}</u> = \mathbf{\mathrm{TG}_{\mathrm{table}}} = <u>\hspace{1.2cm}</u>\,°C$. Record $k_{\mathrm{room}}(t) = <u>\hspace{1.0cm}</u>$.
- **Insert Cup & Record $T_{\mathrm{start}}$ (`5.II.c–d`):** $T_{\mathrm{start}} = <u>\hspace{1.1cm}</u>\,°C$. Compute ambient offset $\Delta T_{\mathrm{amb}} = k_{\mathrm{room}}(T_{\mathrm{room}} - T_{\mathrm{start}}) = <u>\hspace{1.1cm}</u>\,°C$.
- **Compute & Submit $T_{\mathrm{pred}}$ (`5.II.f`):** $T_{\mathrm{pred}} = T_{\mathrm{start}} + \mathrm{TG}_{\mathrm{table}} + \Delta T_{\mathrm{amb}} - \Delta T_{\mathrm{cool}}(0.20 °C) = \mathbf{<u>\hspace{1.4cm}</u>\,°C}$. (*Sanity check:* Verify $T_{\mathrm{start}} < T_{\mathrm{pred}} < 65 °C$ and compare against Fig. `fig:16:calibration-nomogram`; hand signed card to ES with $\ge8 min$ to spare!)

**Table:** Day-of emergency anomaly recovery and prediction adjustment matrix during 3-minute Setup / 1-minute Water Setup  **[S01,S02,S05]**.

| **Event-Day Anomaly** | **Detection Cue (`5.II.a–d`)** | **Immediate Physical Action** | **Quantitative Adjustment to $T_{\mathrm{pred}}$** |
| --- | --- | --- | --- |
| **1. Primary BoPET Window Splashed or Torn** | Water droplet or crease on underside of glazing film during Water Setup. | Swap in impounded spare BoPET drop-ring from clear zip-bag in $<8 s$ (`2.d`). | $\mathbf{0.0 °C}$ (spare BoPET ring is optically and thermally identical to primary window). |
| **2. ES Forbids All Removable Cup Covers** (Local Host Rule) | ES announces no loose cover may rest over cup mouth (despite Clarif. #5). | Remove BoPET drop-ring during 3-min Setup Time so zero violation occurs (`6.h`). | Multiply $\mathrm{TG}_{\mathrm{table}}$ by $\mathbf{0.726}$ (or subtract $\Delta T_{\mathrm{evap}} = 4.8–7.6 °C$ per Table `tab:15:heat-budget`). |
| **3. Off-Center Lamp Clamp Stand Post** | Lamp stand base foot prevents centering outer $29.6 cm$ square box (`4.d`). | Rotate square collector base $45°$ so corner notch straddles lamp post while cup stays centered! | $\mathbf{0.0 °C}$ once cup crosshair is aligned directly beneath bulb tip. |
| **4. Cold Morning Source Water Bath** ($T_{\mathrm{start}} < 18.0 °C$) | ES announces ice-chilled or cold tap bath ($T_{\mathrm{room}} - T_{\mathrm{start}} > +4.0 °C$). | Wipe outer cup wall dry before seating on cork fins; add $\Delta T_{\mathrm{amb}}$ from Table `tab:16:ambient-offset-grid`. | Add $+k_{\mathrm{room}}(t)(T_{\mathrm{room}} - T_{\mathrm{start}}) + 0.15 °C$ (suppressed evaporation at lower $T_{\mathrm{final}}$). |
| **5. ES Uses Deep-Stem Glass or RTD Thermometer** | Observe long glass spirit bulb or $25 mm$ stainless RTD probe at check-in (`4.f`). | Keep extraction ultra-smooth; apply probe-depth offset $\delta_{\mathrm{probe}}$ from Table `tab:16:probe-offsets`. | Subtract $\mathbf{1.4 °C}$ (Pt100 RTD) or $\mathbf{2.1 °C}$ (spirit glass thermometer) from thermistor baseline. |

—
**See also:** §`sec:00` (Scoring Calculator), §`sec:01.13` (`QS-13` Collector Fast Sheet), §`sec:13` (Lumped-Capacitance Heating ODE), §`sec:14` (Materials Encyclopedia), §`sec:15` (2027 Collector Engineering), §`sec:17` (Thermometer Physics & $5\tau_p$), §`sec:18` (Semilog Regression & Residuals), §`app:D` (Printable Test Logs).
