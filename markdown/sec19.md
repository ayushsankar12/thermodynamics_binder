<!-- Source: src/sec19.tex | Tab: Tab 8: PROBLEMS | Target: 8 pp -->
# §19: Integrated Problem-Solving Playbook (Multi-Physics Coupling Templates & Step-by-Step Decision Trees) {#sec:19}

> **[SCOPE: REQUIRED | All 2027 Written Syllabus Clauses 5.c.i–vii & Math Rules 5.d.i–iv]**

On research-university invitational and national exams (§`sec:22`), multi-step quantitative derivations (`FMT-3`) carry $\mathbf{36.7\%}$ of all raw written points and dominate tiebreakers  **[S25,S26,S28]**. High-difficulty “separator” problems rarely test a single isolated equation; instead, they chain **three or four thermodynamic domains** together (e.g., an electrical heater inside a leaking cylinder melting ice and pushing a weighted piston, or a selective radiative collector driving a heat engine coupled to a heat pump). This chapter provides a systematic decomposition protocol, a verbal-cue process recognizer, a 5-check answer audit, Fermi estimation anchors, four canonical coupled-system templates (Fig. `fig:19:coupled-router`), and a Class III calculator speed playbook.

## The Universal 6-Step Problem-Solving Architecture

Execute these six steps in order on every free-response problem (even writing the symbolic setup earns $40\text{--}60\%$ partial credit on university rubrics  **[S25,S26,S28]**):

### [FORMULA & DECISION CARD: Step 1 (System Boundary) $\to$ Step 2 (State Ledger) $\to$ Step 3 (Conservation Accounting)]
- **Step 1 — System-Boundary & Wall-Constraint Checklist:**
  Draw an explicit dashed boundary around your chosen system and classify:
- *Mass transfer across boundary?* **Closed System / Control Mass** ($\Delta m = 0$: use $\Delta U = Q - W_{\mathrm{by}}$) vs. **Open Control Volume / Steady Flow** ($\dot{m}_{\mathrm{in}} = \dot{m}_{\mathrm{out}} = \dot{m}$: use enthalpy $\dot{Q} - \dot{W}_{\mathrm{sh}} = \dot{m}[\Delta h + \tfrac{1}{2}\Delta v^2 + g\Delta z]$) vs. **Isolated Composite System** ($Q_{\mathrm{ext}} = W_{\mathrm{ext}} = 0 \implies \sum \Delta U_i = 0$ and $\Delta S_{\mathrm{tot}} = S_{\mathrm{gen}} \ge 0$).
- *Mechanical boundary constraint?* **Rigid wall** ($\Delta V = 0 \implies W_{\mathrm{by}} = 0$) vs. **Freely floating weighted piston** ($P = P_{\mathrm{ext}} = P_{\mathrm{atm}} + \frac{m_p g}{A_p} = \text{const} \implies W_{\mathrm{by}} = P\Delta V$ and $Q_P = \Delta H$) vs. **Linear spring-loaded piston** ($P(V) = P_1 + \frac{k_s}{A_p^2}(V - V_1)$: straight chord on $P$–$V$, so $W_{\mathrm{by}} = \frac{P_1 + P_2}{2}(V_2 - V_1)$!) vs. **Vacuum free expansion** ($P_{\mathrm{ext}} = 0 \implies W_{\mathrm{by}} = 0$).
- *Thermal boundary constraint?* **Adiabatic / well-insulated** ($Q = 0$) vs. **Diathermal wall in contact with reservoir $T_R$** ($T_{\mathrm{final}} = T_R$) vs. **Conductive wall with finite resistance $R_{\mathrm{th}}$** ($\dot{Q}_{\mathrm{leak}} = \frac{T(t) - T_\infty}{R_{\mathrm{th}}}$).
- **Step 2 — Known/Unknown State-Variable Ledger & Phase-Gate Check:**
  Build a compact grid of states $1, 2, 3, \dots$ across columns $(P,\ V\text{ or }v,\ T\text{ in }K,\ U\text{ or }u,\ H\text{ or }h,\ S\text{ or }s,\ \text{phase/quality }x)$ and path columns $(Q_{ij},\ W_{\mathrm{by},ij},\ \Delta U_{ij},\ S_{\mathrm{gen},ij})$.
- **Step 3 — Coupled Energy, Mass & Entropy Accounting Workflow (§`sec:02`, §`sec:07`, §`sec:08`):**
  
$$
\begin{aligned}

    \underbrace{\Delta U = Q - W_{\mathrm{by}} = q + w_{\mathrm{on}}}_{\text{Closed System First Law}}, \qquad
    \underbrace{\dot{Q} - \dot{W}_{\mathrm{sh}} = \dot{m}\left[(h_2 - h_1) + \tfrac{1}{2}(v_2^2 - v_1^2) + g(z_2 - z_1)\right]}_{\text{Steady-Flow Open System (SFEE)}}, \qquad
    \underbrace{S_{\mathrm{gen}} = \Delta S_{\mathrm{sys}} - \sum_k \frac{Q_k}{T_{b,k}} \ge 0}_{\text{Second Law \& Gouy--Stodola } X_{\mathrm{dest}} = T_0 S_{\mathrm{gen}}}
\end{aligned}
$$

**Table:** Step 4 & Step 5 — Verbal Cue Process Recognizer & Heat-Transfer Mode Selector  **[S12,S13,S25,S26]**.

| **Problem Verbal Cue / Phrase** | **Thermodynamic Model** | **Exact Algebraic Constraint** | **Key Formula / Trap to Watch** |
| --- | --- | --- | --- |
| *“Rigid, sealed tank / bomb calorimeter”* | Isochoric closed system | $\Delta V = 0 \implies W_{\mathrm{by}} = 0$ | $Q_V = \Delta U = n C_{V,m}\Delta T$; on $P$–$T$: $\dfrac{P_2}{P_1} = \dfrac{T_2}{T_1}$. |
| *“Heavy frictionless piston / open to atmosphere / coffee cup”* | Isobaric closed system | $P = P_0 = \text{const}$ | $W_{\mathrm{by}} = P_0(V_2 - V_1) = nR\Delta T$; $Q_P = \Delta H = n C_{P,m}\Delta T$. |
| *“Slowly in thermal contact with a large constant-$T$ bath”* | Reversible isothermal | $\Delta T = 0 \implies \Delta U_{\mathrm{IG}} = \Delta H_{\mathrm{IG}} = 0$ | $Q = W_{\mathrm{by}} = nRT\ln\!\left(\dfrac{V_2}{V_1}\right) = nRT\ln\!\left(\dfrac{P_1}{P_2}\right)$. |
| *“Rapidly compressed/expanded in a well-insulated cylinder”* | Reversible adiabatic (isentropic if frictionless) | $Q = 0,\ \Delta S = 0$, <br> $P V^\gamma = \text{const},\ T V^{\gamma-1} = \text{const}$ | $\Delta U = -W_{\mathrm{by}} = n C_{V,m}(T_2 - T_1) = \dfrac{P_2 V_2 - P_1 V_1}{\gamma - 1}$. |
| *“Membrane bursts into an evacuated, insulated chamber”* | Adiabatic free expansion (Joule expansion) | $Q = 0,\ P_{\mathrm{ext}} = 0 \implies W_{\mathrm{by}} = 0$ <br> $\implies \Delta U = 0$ ($\Delta T_{\mathrm{IG}} = 0$) | **Irreversible!** $\Delta S = nR\ln\!\left(\dfrac{V_2}{V_1}\right) > 0$ even though $Q = 0$! |
| *“Flows steadily through a porous plug, capillary, or partially open valve”* | Steady-flow throttling (Joule–Thomson) | $\dot{Q} = 0,\ \dot{W}_{\mathrm{sh}} = 0 \implies \mathbf{h_2 = h_1}$ <br> (Isenthalpic, $\Delta H = 0$) | For ideal gas, $\Delta T = 0$; for wet steam/refrigerant, $h_1 = h_{f2} + x_2 h_{fg2}$ drops $T$! |
| *“Small metal sphere cools/warms in fluid ($h L_c / k_{\mathrm{solid}} < 0.1$)”* | Lumped-capacitance transient ($\mathrm{Bi} < 0.1$, §`sec:13`) | $T(t) = T_{\mathrm{ss}} - (T_{\mathrm{ss}} - T_i)e^{-t/\tau}$ | $\tau = R_{\mathrm{th}} C = \dfrac{m c_p}{h A}$; check $\mathrm{Bi} = \dfrac{h(V/A)}{k_{\mathrm{solid}}} < 0.1$ first! |
| *“Object in vacuum cavity / orbital satellite / tungsten filament”* | Pure radiative exchange ($h_{\mathrm{conv}} = 0$, §`sec:12`) | $\dot{Q}_{\mathrm{net}} = \varepsilon\sigma A\left(T^4 - T_{\mathrm{surr}}^4\right)$ | Vacuum cooling time ($T_{\mathrm{surr}} \to 0$): $\Delta t = \dfrac{m c}{3\varepsilon\sigma A}\!\left(\dfrac{1}{T_f^3} - \dfrac{1}{T_i^3}\right)$ (`E4 Q14d` **[S28]**). |

**Step 6 — The Diagram-First Protocol:** Before solving multi-equation algebra, sketch a $3\times 3\text{ cm}$ diagnostic plot on scratch paper: (a) for gas processes/cycles, sketch both $P$–$V$ and $T$–$S$ planes to verify clockwise ($W_{\mathrm{net}} > 0$) vs. counterclockwise loop orientation; (b) for ice/water/steam mixing, sketch the 5-stage temperature–enthalpy ladder ($-273 °C \to 0 °C\text{ ice} \to 0 °C\text{ water} \to 100 °C\text{ water} \to 100 °C\text{ steam}$) to locate the final phase plateau before writing a single temperature equation (§`sec:04`, Fig. `fig:04:ice-water-tree`); (c) for composite conduction/convection/radiation, draw the series-parallel resistor node diagram (§`sec:10`, Fig. `fig:10:composite-wall`).

## The 5-Check Answer Audit & Fermi Estimation / Reverse-Engineering Playbook

### [SHORTCUT: The 15-Second 5-Check Answer Audit]

Run every final numerical answer through these 5 gates:
- **Check 1 (Units & Prefixes):** Did $kJ$ vs. $J$, $g$ vs. $kg$ in $M$ ($\mathrm{N_2} = 0.02801 kg/mol$ in $v_{\mathrm{rms}} = \sqrt{3RT/M}$), and $K$ vs. $°C$ cancel cleanly?
- **Check 2 (Signs):** Expansion $\Delta V > 0 \implies W_{\mathrm{by}} > 0$ ($w_{\mathrm{on}} < 0$). Cooling $\Delta T < 0 \implies \Delta S < 0$ and $\Delta U < 0$.
- **Check 3 (Thermodynamic Bounds):**
- Engine: $0 < \eta = \dfrac{W_{\mathrm{net}}}{Q_H} \le \eta_C = 1 - \dfrac{T_C}{T_H} < 1$.
- Refrigerator/Pump: $\mathrm{COP}_{\mathrm{HP}} = \mathrm{COP}_R + 1 \le \dfrac{T_H}{T_H - T_C}$.
- Calorimetry mixture: $T_{\mathrm{cold,init}} \le T_{\mathrm{final}} \le T_{\mathrm{hot,init}}$.
- Wet-steam quality: $0 \le x \le 1$; relative humidity: $0 \le \phi \le 100%$.
- **Check 4 (Limiting Cases):** Does $t \to 0$ give $T = T_i$? Does $t \to \infty$ give $T = T_{\mathrm{ss}}$? Does $r_o \to r_i$ give $R_{\mathrm{cyl}} \to 0$?
- **Check 5 (Independent Conservation):** Does $\sum Q_{\mathrm{in}} = \sum Q_{\mathrm{out}} + W_{\mathrm{net}}$ hold globally across the outer boundary?

### [FORMULA & DECISION CARD: Fermi Anchor Benchmarks & Reverse-Engineering]

**Order-of-Magnitude Physical Anchors:**
- Room air ($300\text{ K}, 1\text{ atm}$): $\rho \approx 1.18 kg/m^3$, $c_p \approx 1.007 kJ/kg/K$, $k \approx 0.026 W/m/K$, $v_{\mathrm{rms}} \approx 508 m/s$, $\lambda_{\mathrm{mfp}} \approx 68 nm$.
- Liquid water ($25 °C$): $\rho \approx 997 kg/m^3$, $c_p = 4.184 kJ/kg/K$ ($\rho c_p \approx 4.17 MJ/m^3/K$), $k \approx 0.607 W/m/K$, $L_f = 333.55 kJ/kg$, $L_v = 2256.4 kJ/kg$ ($L_v/L_f = 6.76\times$).
- Blackbody at $300 K$: $M = \sigma T^4 \approx 459 W/m^2$, $\lambda_{\max} \approx 9.66 µm$. Solar constant at Earth: $G_{\mathrm{sc}} \approx 1361 W/m^2$. Resting human metabolic heat: $\dot{Q}_{\mathrm{human}} \approx 100 W$.

**Reverse-Engineering Back-Solve Protocol:**
When a problem specifies a *desired final temperature, efficiency, or survival time* and asks for an unknown initial mass $m_0$, insulation thickness $L_{\mathrm{ins}}$, or electrical resistance $R_e$:
- Write the forward conservation equation symbolically keeping the target parameter isolated.
- For logarithmic transients $T(t) = T_{\mathrm{ss}} - (T_{\mathrm{ss}}-T_i)e^{-t/\tau}$, invert directly: $\tau = R_{\mathrm{th}}C = \dfrac{-t}{\ln[(T_{\mathrm{ss}}-T(t))/(T_{\mathrm{ss}}-T_i)]}$.

## Multi-Physics Coupled Problem Decomposition & National-Tier Templates

Figure `fig:19:coupled-router` illustrates how to decouple a complex multi-subsystem problem into modular algebraic blocks linked by shared boundary fluxes ($\dot{Q}$, $\dot{W}$) and equilibrium interface conditions ($P_{\mathrm{eq}}, T_{\mathrm{eq}}, V_{\mathrm{tot}}$).

!{

> **[Vector Figure: Original Vector Technical Diagram | Label: `fig:diagram`]**
> - **Diagram Annotations & Key Elements:** **SUBSYSTEM A: ENERGY SOURCE** / [2pt] $\bullet$ Joule Heater: $\dot{Q}_{\mathrm{elec}} = I V = \dfrac{V^2}{R_e} = I^2 R_e$ / [2pt] $\bullet$ Radiative Lamp/Sun: $\dot{Q}_{\mathrm{rad,in}} = \alpha_{\mathrm{NIR}} A G$ • **SUBSYSTEM B: WALL HEAT LEAK** / [2pt] $\bullet$ Composite Wall: $R_{\mathrm{th}} = \sum \dfrac{L_j}{k_j A} + \dfrac{1}{h A}$ / [2pt] $\bullet$ Net Power: $\dot{Q}_{\mathrm{net}}(T) = \dot{Q}_{\mathrm{in}} - \dfrac{T - T_\infty}{R_{\mathrm{th}}}$ • **SUBSYSTEM C: MULTI-PHASE WORKING FLUID** / [2pt] **5-Stage Energy & Time Budget ($\Delta t = \sum t_k$):** / [1pt] 1. Warm Solid ($T_1 \to T_m$): $Q_1 = m c_s(T_m - T_1)$ / 2. Melt Plateau ($T = T_m$): $Q_2 = m L_f$ / 3. Warm Liquid ($T_m \to T_b(P)$): $Q_3 = m c_\ell(T_b - T_m)$ / 4. Vaporize Plateau ($T = T_b(P)$): $Q_4 = m L_v$ / 5. Superheat Vapor ($T_b \to T_f$): / $C_p \dfrac{dT}{dt} = \dot{Q}_{\mathrm{in}} - \dfrac{T - T_\infty}{R_{\mathrm{th}}} \implies T_f = T_{\mathrm{ss}} - (T_{\mathrm{ss}}-T_b)e^{-t_5/\tau}$ • **SUBSYSTEM D: MECHANICAL BOUNDARY** / [2pt] $\bullet$ Weighted Piston ($P = P_0$): $W_{\mathrm{by}} = P_0(V_f - V_i)$ / [1pt] $\bullet$ Spring Piston: $W_{\mathrm{by}} = \tfrac{1}{2}(P_i + P_f)(V_f - V_i)$ / [1pt] $\bullet$ Internal Energy: $\Delta U = \Delta H - \Delta(PV)$ • **SUBSYSTEM E: 2ND LAW & GLOBAL AUDIT** / [2pt] $\bullet$ Global Energy: $E_{\mathrm{elec}} = \Delta H_{\mathrm{tot}} + Q_{\mathrm{leak,tot}}$ / [1pt] $\bullet$ Entropy Gen: $S_{\mathrm{gen}} = \Delta S_{\mathrm{fluid}} + \dfrac{Q_{\mathrm{leak}}}{T_\infty} \ge 0$ / [1pt] $\bullet$ Exergy Destroyed: $X_{\mathrm{dest}} = T_0 S_{\mathrm{gen}}$

**Figure:** Multi-physics coupled problem decomposition map showing how an electrical or radiative power source (Subsystem A), a conductive/convective wall heat leak (Subsystem B), a 5-stage phase-changing fluid (Subsystem C), and a moving piston boundary (Subsystem D) decouple into sequential algebraic energy balances verified by a global First/Second-Law audit (Subsystem E)  **[S12,S13,S25]**.

### Worked Example — Template 1: Coupled Joule Heater + 5-Stage Ice-to-Steam Phase Change + Conductive Leak + Piston `[Rules 5.c.ii–iv]`

A vertical cylinder insulated on its sides except for a sight window of thermal resistance $R_{\mathrm{wall}} = 2.50 K/W$ to a $T_{\mathrm{room}} = 20.0 °C$ room contains $m = 0.250 kg$ of ice initially at $T_1 = -15.0 °C$ under a frictionless piston maintaining constant absolute pressure $P_0 = 101.325 kPa$. An internal resistive heater ($V = 48.0 V$, $R_e = 4.608 Ω$) is switched on for $t_{\mathrm{tot}} = 1800.0 s$ ($30.0 min$). Using $c_{\mathrm{ice}} = 2100 J/kg/K$, $L_f = 333.55 kJ/kg$, $c_w = 4184 J/kg/K$, $L_v = 2256.4 kJ/kg$ at $100.0 °C$, $c_{p,\mathrm{steam}} = 2080 J/kg/K$, and $\rho_{\mathrm{ice}} = 916.7 kg/m^3$, find: (a) the time required to reach $100.0 °C$ dry saturated steam, (b) the final superheated steam temperature $T_f$ at $t = 1800.0 s$, and (c) the total boundary work $W_{\mathrm{by}}$ done by the piston.
**Solution.**
Electrical heating power: $P_{\mathrm{elec}} = \frac{V^2}{R_e} = \frac{48.0^2}{4.608} = \mathbf{500.0 W}$ (constant). Because $P_0 = \text{const}$, enthalpy changes satisfy $\frac{dH}{dt} = \dot{Q}_{\mathrm{net}}(T) = P_{\mathrm{elec}} - \frac{T - T_{\mathrm{room}}}{R_{\mathrm{wall}}}$.
(a) **Stages 1–4 Time Budget to Reach $100.0 °C$ Dry Saturated Vapor:**
- *Stage 1 (Warm ice $-15.0 °C \to 0.0 °C$, mean $T_{\mathrm{avg},1} = -7.5 °C < T_{\mathrm{room}}$, so room leaks heat **into** cylinder!):*
  $\Delta H_1 = m c_{\mathrm{ice}}\Delta T_1 = (0.250)(2100)(15.0) = 7875.0 J$; $\dot{Q}_{\mathrm{net},1} = 500.0 - \frac{-7.5 - 20.0}{2.50} = 500.0 + 11.0 = 511.0 W \implies t_1 = \frac{7875.0}{511.0} = \mathbf{15.411 s}$.
- *Stage 2 (Melt ice at $T_m = 0.0 °C$):*
  $\Delta H_2 = m L_f = (0.250)(333550) = 83387.5 J$; $\dot{Q}_{\mathrm{net},2} = 500.0 - \frac{0.0 - 20.0}{2.50} = 508.0 W \implies t_2 = \frac{83387.5}{508.0} = \mathbf{164.149 s}$.
- *Stage 3 (Warm liquid water $0.0 °C \to 100.0 °C$, mean $T_{\mathrm{avg},3} = 50.0 °C$):*
  $\Delta H_3 = m c_w \Delta T_3 = (0.250)(4184)(100.0) = 104600.0 J$; $\dot{Q}_{\mathrm{net},3} = 500.0 - \frac{50.0 - 20.0}{2.50} = 488.0 W \implies t_3 = \frac{104600.0}{488.0} = \mathbf{214.344 s}$.
- *Stage 4 (Vaporize water at $T_b = 100.0 °C$):*
  $\Delta H_4 = m L_v = (0.250)(2256400) = 564100.0 J$; $\dot{Q}_{\mathrm{net},4} = 500.0 - \frac{100.0 - 20.0}{2.50} = 468.0 W \implies t_4 = \frac{564100.0}{468.0} = \mathbf{1205.342 s}$.

Total elapsed time to reach dry saturated steam at $100.0 °C$: $t_{1\dots 4} = 15.411 + 164.149 + 214.344 + 1205.342 = \mathbf{1599.25 s}$ ($26.65 min$).
(b) **Stage 5 (Superheating Steam During Remaining $t_5 = 1800.0 - 1599.246 = 200.754 s$):**
For isobaric steam warming with $C_{p,\mathrm{steam}} = m c_{p,\mathrm{steam}} = (0.250)(2080) = 520.0 J/K$, the exact lumped ODE $C_{p,\mathrm{steam}}\frac{dT}{dt} = P_{\mathrm{elec}} - \frac{T - T_{\mathrm{room}}}{R_{\mathrm{wall}}}$ has time constant $\tau_s = C_{p,\mathrm{steam}}R_{\mathrm{wall}} = (520.0)(2.50) = 1300.0 s$ and asymptote $T_{\mathrm{ss}} = 20.0 + (500.0)(2.50) = 1270.0 °C$:
$$T_f = T_{\mathrm{ss}} - (T_{\mathrm{ss}} - 100.0 °C)e^{-t_5/\tau_s} = 1270.0 - (1170.0)e^{-200.754/1300.0} = 1270.0 - 1002.58 = \mathbf{267.42 °C}\ (540.57 K)$$
(c) **Total Isobaric Boundary Work $W_{\mathrm{by}} = P_0(V_f - V_i)$:**
Initial ice volume: $V_i = \frac{0.250 kg}{916.7 kg/m^3} = 2.727×10^{-4} m^3$. Final steam moles: $n = \frac{250.0 g}{18.01528 g/mol} = 13.8771 mol$, so ideal-gas steam volume at $T_f = 540.57 K$ is $V_f = \frac{n R T_f}{P_0} = \frac{(13.8771)(8.31446)(540.57)}{101325} = 0.61555 m^3$. Thus:
$$W_{\mathrm{by}} = P_0(V_f - V_i) = (101.325 kPa)(0.61555 m^3 - 0.00027 m^3) = \mathbf{62.34 kJ}$$

**✓ Verified by:** Global enthalpy balance $\sum_{k=1}^5 \Delta H_k = 7.875 + 83.388 + 104.600 + 564.100 + 87.058 = 847.02 kJ$ and Python check `sec19:ex19.1`.

### Worked Example — Template 2: Wavelength-Selective Radiative Collector Driving a Carnot Engine & Heat-Pump Cascade `[Rules 5.c.iii, 5.c.iv, 5.c.vi]`

A selective solar collector of area $A_c = 2.00 m^2$ ($\alpha_{\mathrm{sol}} = 0.92$, thermal-IR emittance $\varepsilon_{\mathrm{IR}} = 0.10$, insulated back) receives solar irradiance $G = 1000.0 W/m^2$ in an ambient environment at $T_0 = 300.0 K$ ($\sigma = 5.670374×10^{-8} W/m^2/K^4$). The collector operates at steady temperature $T_H = 450.0 K$ and supplies its net heat rate $\dot{Q}_H$ to a reversible Carnot heat engine rejecting heat at $T_0 = 300.0 K$. All shaft power $\dot{W}$ from the engine drives a reversible heat pump that extracts heat from outdoor winter air at $T_{\mathrm{out}} = 270.0 K$ to heat a building interior at $T_B = 310.0 K$. Calculate: (a) the net heat rate $\dot{Q}_H$ delivered to the engine, (b) the engine power output $\dot{W}$, and (c) the total heating power $\dot{Q}_B$ delivered to the building.
**Solution.**
(a) Collector radiative energy balance at $T_H = 450.0 K$:

$$
\begin{aligned}
\dot{Q}_H &= A_c\left[\alpha_{\mathrm{sol}} G - \varepsilon_{\mathrm{IR}}\sigma\left(T_H^4 - T_0^4\right)\right] = (2.00 m^2)\left[(0.92)(1000.0) - (0.10)(5.670374×10^{-8})\left(450.0^4 - 300.0^4\right)\right] \\
            &= 2.00\left(920.0 - 186.591\right) = \mathbf{1466.82 W}
\end{aligned}
$$

(b) Carnot engine efficiency between $T_H = 450.0 K$ and $T_0 = 300.0 K$ is $\eta_C = 1 - \frac{300.0}{450.0} = \frac{1}{3} = 0.33333$, so shaft power output is:
$$\dot{W} = \eta_C\,\dot{Q}_H = \frac{1}{3}(1466.82 W) = \mathbf{488.94 W}$$
(c) Reversible heat pump coefficient of performance between $T_{\mathrm{out}} = 270.0 K$ and $T_B = 310.0 K$ is $\mathrm{COP}_{\mathrm{HP}} = \frac{T_B}{T_B - T_{\mathrm{out}}} = \frac{310.0}{310.0 - 270.0} = \mathbf{7.750}$. Thus the total heating rate supplied to the building is:
$$\dot{Q}_B = \mathrm{COP}_{\mathrm{HP}}\,\dot{W} = (7.750)(488.94 W) = \mathbf{3789.3 W} \quad (\text{a }\mathbf{2.58\times\text{**thermal multiplier**}} \text{ over direct solar heating }\dot{Q}_H\text{!})$$

**✓ Verified by:** Reversible zero-entropy-generation check $\dot{Q}_H/T_H - (\dot{Q}_H-\dot{W})/T_0 = 0$ and $\dot{Q}_B/T_B - (\dot{Q}_B-\dot{W})/T_{\mathrm{out}} = 0$ in Python check `sec19:ex19.2`.

### Worked Example — Template 3: Steam-Table Rankine Turbine Efficiency $\eta_t$, Wet-Steam Quality & Gouy–Stodola Exergy `[`2027 Cornell E1 Q29`  **[S09,S25]**]`

In a steam Rankine cycle (`2027 Cornell E1 Q29`), superheated steam enters an adiabatic turbine at $P_1 = 3.00 MPa$, $T_1 = 350.0 °C$ ($h_1 = 3116.1 kJ/kg$, $s_1 = 6.7450 kJ/kg/K$) and expands to condenser pressure $P_2 = 10.0 kPa$ ($T_{\mathrm{sat}} = 45.81 °C = 318.96 K$, $h_f = 191.81 kJ/kg$, $h_{fg} = 2392.1 kJ/kg$, $s_f = 0.6492 kJ/kg/K$, $s_{fg} = 7.4996 kJ/kg/K$). If the turbine has an isentropic efficiency of $\eta_t = 85.0%$ and the dead-state environment is at $T_0 = 25.00 °C = 298.15 K$, compute: (a) the isentropic exit quality $x_{2s}$ and enthalpy $h_{2s}$, (b) the actual turbine work $w_t$, actual exit enthalpy $h_{2a}$, and actual exit quality $x_{2a}$, and (c) the specific entropy generation $s_{\mathrm{gen}}$ and Gouy–Stodola exergy destruction $x_{\mathrm{dest}} = T_0 s_{\mathrm{gen}}$.
**Solution.**
(a) For an ideal isentropic expansion ($s_{2s} = s_1 = 6.7450 kJ/kg/K$):
$$x_{2s} = \frac{s_1 - s_f}{s_{fg}} = \frac{6.7450 - 0.6492}{7.4996} = \mathbf{0.81282} \implies h_{2s} = h_f + x_{2s} h_{fg} = 191.81 + (0.81282)(2392.1) = \mathbf{2136.15 kJ/kg}$$
(b) Actual specific turbine work and exit state for $\eta_t = \frac{h_1 - h_{2a}}{h_1 - h_{2s}} = 0.850$:
$$w_t = \eta_t(h_1 - h_{2s}) = 0.850(3116.1 - 2136.15) = \mathbf{832.96 kJ/kg}, \qquad h_{2a} = h_1 - w_t = 3116.1 - 832.96 = \mathbf{2283.14 kJ/kg}$$
$$x_{2a} = \frac{h_{2a} - h_f}{h_{fg}} = \frac{2283.14 - 191.81}{2392.1} = \mathbf{0.87427} \quad (\text{irreversible friction }*increases*\text{ exit vapor quality from }81.3\%\text{ to }87.4\%\text{!})$$
(c) Actual exit entropy: $s_{2a} = s_f + x_{2a} s_{fg} = 0.6492 + (0.87427)(7.4996) = 7.20585 kJ/kg/K$. Because the turbine is adiabatic ($\dot{Q}=0$):
$$s_{\mathrm{gen}} = s_{2a} - s_1 = 7.20585 - 6.7450 = \mathbf{0.46085 kJ/kg/K}, \qquad x_{\mathrm{dest}} = T_0\,s_{\mathrm{gen}} = (298.15 K)(0.46085 kJ/kg/K) = \mathbf{137.40 kJ/kg}$$

**✓ Verified by:** Identity $s_{2a} - s_1 = (h_{2a} - h_{2s})/T_{\mathrm{sat}} = (1 - \eta_t)(h_1 - h_{2s})/T_{\mathrm{sat}} = 146.99/318.96 = 0.46085 kJ/kg/K$ and Python check `sec19:ex19.3`.

### Worked Example — Template 4: Two-Compartment Insulated Cylinder with Diathermal Frictionless Sliding Piston `[`MIT E3 Q24`  **[S26,S27]**]`

A rigid, well-insulated cylinder of total volume $V_{\mathrm{tot}} = 30.00 L$ is divided by a frictionless, thermally conducting (diathermal) piston of negligible heat capacity into Compartment A containing $n_A = 1.000 mol$ of monatomic helium ($\mathrm{He}$, $f_A = 3$) and Compartment B containing $n_B = 1.500 mol$ of diatomic nitrogen ($\mathrm{N_2}$, $f_B = 5$). Initially both gases are in equilibrium at $T_i = 300.0 K$. An electrical coil adds $Q = 12.4717 kJ$ of heat to the system. Find the final equilibrium temperature $T_f$, final volumes $V_{A,f}$ and $V_{B,f}$, and final pressure $P_f$.
**Solution.**
Choose the **combined gas A + B + piston** as our closed system. Because the outer cylinder is rigid ($W_{\mathrm{ext}} = 0$) and insulated except for the heater input $Q$, the First Law for the composite system is simply $\Delta U_{\mathrm{tot}} = \Delta U_A + \Delta U_B = Q$. Since the piston is diathermal, both gases reach a common final temperature $T_f$:
$$C_{V,\mathrm{tot}} = n_A C_{V,m,A} + n_B C_{V,m,B} = \left[(1.000)\!\left(\tfrac{3}{2}\right) + (1.500)\!\left(\tfrac{5}{2}\right)\right]R = 5.250\,R = (5.250)(8.3144626 J/mol/K) = \mathbf{43.6509 J/K}$$
$$T_f = T_i + \frac{Q}{C_{V,\mathrm{tot}}} = 300.0 + \frac{12471.7 J}{43.6509 J/K} = 300.0 + 285.714 = \mathbf{585.71 K}$$
Because the piston is frictionless and diathermal, mechanical and thermal equilibrium require $P_{A,f} = P_{B,f} = P_f$ and $T_{A,f} = T_{B,f} = T_f$, so $\frac{V_{A,f}}{V_{B,f}} = \frac{n_A R T_f / P_f}{n_B R T_f / P_f} = \frac{n_A}{n_B}$ (the piston does not move!). Thus $V_{A,f} = \frac{1.000}{2.500}(30.00 L) = \mathbf{12.00 L}$, $V_{B,f} = \mathbf{18.00 L}$, and:
$$P_f = \frac{(n_A + n_B) R T_f}{V_{\mathrm{tot}}} = \frac{(2.500 mol)(8.3144626 J/mol/K)(585.714 K)}{0.03000 m^3} = 405817 Pa = \mathbf{405.82 kPa}$$

**✓ Verified by:** Individual subsystem check $P_{A,f} = (1.000)(8.31446)(585.714)/0.0120 = 405.82 kPa = P_{B,f}$ and Python check `sec19:ex19.4`.

**Table:** Master Atlas of the 10 Canonical Multi-Physics Coupling Archetypes Across the Exam Corpus (`E1–E8`)  **[S12,S25,S26,S27,S28]**.

| **Coupling Archetype** | **Subsystems Linked** | **Bridging Algebraic Equations** | **Exam Precedent & Section Link** |
| --- | --- | --- | --- |
| **1. Container Dilatometer + Liquid Compressibility** | Glass bulb expansion ($3\alpha_g$) + liquid expansion ($\beta_\ell$) + pressure ($\kappa_T$) | $\Delta V_{\mathrm{app}} = V_0\left[(\beta_\ell - 3\alpha_g)\Delta T - \kappa_{T,\mathrm{eff}}\Delta P\right] = A_{\mathrm{cap}}\Delta h$ | `2027 Cornell E1 FRQ 1 (Q26)` **[S25]** (§`sec:03`, Ex. `ex:19.5`) |
| **2. Spring-Loaded Piston + Ideal-Gas or Phase Heating** | Hooke's law spring ($k_s$) + cylinder gas/steam ($P,V,T$) | $P(V) = P_1 + \dfrac{k_s}{A_p^2}(V - V_1)$;\quad $W_{\mathrm{by}} = \dfrac{P_1 + P_2}{2}(V_2 - V_1)$;\quad $\Delta U = Q - W_{\mathrm{by}}$ | `MIT E2/E3` & classic Olympiad piston-spring FRQ (§`sec:07`, Ex. `ex:19.6`) |
| **3. Planetary / Lamp Flux + Selective Gray Radiative Balance** | Inverse-square irradiance + two-band surface ($\alpha_{\mathrm{SW}}, \varepsilon_{\mathrm{LW}}$) | $I(D) = \dfrac{\sigma R_S^2 T_S^4}{D^2}$;\quad $T_{\mathrm{eq}} = \left(\dfrac{\alpha_{\mathrm{SW}}\,A_{\mathrm{proj}}\,I(D)}{\varepsilon_{\mathrm{LW}}\,A_{\mathrm{emit}}\,\sigma}\right)^{1/4}$ | `MIT E3 Q23`, `Cornell E1 Q36–37` **[S25,S27]** (§`sec:12`, Ex. `ex:19.7`) |
| **4. Vacuum $T^4$ Radiative Cooling Transient** | Sensible heat capacity ($mc$) + Stefan–Boltzmann radiation ($T_{\mathrm{surr}}\to 0$) | $m c\dfrac{dT}{dt} = -\varepsilon\sigma A T^4 \implies \Delta t = \dfrac{m c}{3\varepsilon\sigma A}\!\left(\dfrac{1}{T_f^3} - \dfrac{1}{T_i^3}\right)$ | `GGSO E4 Q14d` **[S28]** (§`sec:12`, §`sec:13`, Ex. `ex:19.7`) |
| **5. Intercooled Multi-Stage Gas Compression** | $N$-stage adiabatic compression + isobaric intercoolers back to $T_1$ | Optimal intermediate pressure: $P_{\mathrm{mid}} = \sqrt{P_1 P_2}$;\quad $W_{\mathrm{on,min}} = \dfrac{N\gamma}{\gamma-1}nRT_1\!\left[\left(\dfrac{P_2}{P_1}\right)^{\frac{\gamma-1}{N\gamma}} - 1\right]$ | `MIT E2 P4b` (`TB #1`) **[S26]** (§`sec:07`) |
| **6. Binary Eutectic Cooling + Phase-Fraction Calorimetry** | Lever-rule mass fractions ($f_L, f_\alpha$) + proeutectic & eutectic latent heats | $f_{\mathrm{eut}} = f_L(T_{\mathrm{eut}}^+) = \dfrac{w_0 - w_\alpha}{w_E - w_\alpha}$;\quad $Q_{\mathrm{eut}} = m_{\mathrm{tot}}\,f_{\mathrm{eut}}\,\Delta h_{\mathrm{eut}}$ | `2027 Cornell E1 Q10–14, Q30` (`TB #4`) **[S25]** (§`sec:05`, §`sec:18`) |
| **7. Drude Electron Gas + Wiedemann–Franz Conduction** | Kinetic theory of electrons + electrical ($\sigma_e$) & thermal ($\kappa$) conductivity | $\dfrac{\kappa}{\sigma_e T} = L = \dfrac{3}{2}\!\left(\dfrac{k_B}{e}\right)^2$ (Drude) or $\dfrac{\pi^2}{3}\!\left(\dfrac{k_B}{e}\right)^2 = 2.44×10^{-8} W Ω/K^2$ (Sommerfeld) | `2027 Cornell E1 FRQ 4 (Q32–34)` **[S25]** (§`sec:06`, §`sec:10`) |
| **8. Open-Cup Evaporative Mass Transfer + Convection/Radiation** | Vapor concentration boundary layer ($g_m$) + latent heat $L_v$ + sensible $h$ | $\dot{Q}_{\mathrm{tot}} = h A(T_s - T_e) + \varepsilon\sigma A(T_s^4 - T_e^4) + L_v A g_m(m_{\mathrm{H_2O},s} - m_{\mathrm{H_2O},e})$ | Lienhard Ex. 11.11 **[S12]** & 2027 Collector (§`sec:11`, §`sec:15.4`) |
| **9. Temperature-Dependent $\Delta H_{\mathrm{rxn}}(T)$ + Gibbs Crossover $T^*$** | Kirchhoff's enthalpy/entropy laws ($\Delta C_P$) + $\Delta G = \Delta H - T\Delta S$ | $\Delta H(T_2) = \Delta H(T_1) + \Delta C_P(T_2 - T_1)$;\quad $\Delta S(T_2) = \Delta S(T_1) + \Delta C_P\ln(T_2/T_1)$ | `MIT E2 P3b,e`, `GGSO E5 Q14–16`, `Cornell E6 Sec V` **[S26,S29,S30]** (§`sec:08`) |
| **10. Gravity Hydrostatic Atmosphere + Adiabatic Lapse Rate** | Hydrostatic balance ($dP/dz = -\rho g$) + ideal gas + adiabatic $T P^{(1-\gamma)/\gamma} = C$ | Dry adiabatic lapse rate: $\Gamma_d = -\dfrac{dT}{dz} = \dfrac{M_{\mathrm{air}} g}{C_{P,m}} = \dfrac{g}{c_{p,\mathrm{air}}} = 9.76 K/km$ | `MIT E2/E3` & atmospheric thermodynamics (§`sec:06`, §`sec:07`) |

### Worked Example — Template 5: Pressurized Glass-Bulb Liquid Dilatometer with Container Expansion Correction `[`2027 Cornell E1 Q26`  **[S25]**]`

A precision borosilicate glass dilatometer (`2027 Cornell E1 Q26`) has an internal bulb volume $V_0 = 50.000 cm^3$ attached to a vertical capillary tube of cross-sectional area $A_c = 0.0200 cm^2$ at $T_0 = 20.00 °C$ and $P_0 = 1.000 atm$. The borosilicate glass has linear thermal expansion coefficient $\alpha_g = 3.25×10^{-6} /K$, while the test liquid filling the bulb up to initial capillary height $h_0 = 5.00 cm$ has volumetric thermal expansion coefficient $\beta_\ell = 9.50×10^{-4} /K$ and effective isothermal compressibility (relative to glass) $\kappa_{T,\mathrm{eff}} = 8.20×10^{-5} /atm$. If the dilatometer is warmed to $T_1 = 70.00 °C$ ($\Delta T = 50.00 K$) while the overhead gas pressure in the capillary is raised to $P_1 = 26.00 atm$ ($\Delta P = 25.00 atm$), find: (a) the initial total liquid volume $V_{\ell,0}$, (b) the apparent volume change $\Delta V_{\mathrm{app}}$ measured against the glass capillary graduations, and (c) the new capillary meniscus reading $h_1$.
**Solution.**
(a) Initial total liquid volume occupying the bulb plus the first $5.00 cm$ of the capillary stem:
$$V_{\ell,0} = V_0 + A_c h_0 = 50.000 cm^3 + (0.0200 cm^2)(5.00 cm) = \mathbf{50.100 cm^3}$$
(b) As temperature increases by $\Delta T = 50.00 K$ and pressure increases by $\Delta P = 25.00 atm$, the liquid volume changes while the glass bulb and capillary container expand with volumetric coefficient $\beta_g = 3\alpha_g = 3(3.25×10^{-6}) = 9.75×10^{-6} /K$. By Archetype 1 in Table `tab:19:archetypes`:
$$\Delta V_{\mathrm{app}} = V_{\ell,0}\left[\left(\beta_\ell - 3\alpha_g\right)\Delta T - \kappa_{T,\mathrm{eff}}\,\Delta P\right] = (50.100 cm^3)\left[(9.50×10^{-4} - 9.75×10^{-6})(50.00) - (8.20×10^{-5})(25.00)\right]$$
$$\Delta V_{\mathrm{app}} = (50.100 cm^3)\left[0.0470125 - 0.0020500\right] = (50.100 cm^3)(0.0449625) = \mathbf{+2.2526 cm^3}$$
*(Notice that neglecting the glass bulb expansion $3\alpha_g\Delta T$ would overestimate $\Delta V_{\mathrm{app}}$ by $+0.0244 cm^3$ or $+1.22 cm$ of capillary height!)*
(c) New capillary column height reading (neglecting the tiny $2\alpha_g\Delta T = 0.03\%$ cross-sectional expansion of $A_c$):
$$h_1 = h_0 + \frac{\Delta V_{\mathrm{app}}}{A_c} = 5.00 cm + \frac{2.25262 cm^3}{0.0200 cm^2} = 5.00 + 112.631 = \mathbf{117.63 cm}$$

**✓ Verified by:** Absolute volume difference $[V_{\ell,0}(1 + \beta_\ell\Delta T - \kappa\Delta P) - V_0(1+3\alpha_g\Delta T)]/A_c = 117.631 cm$ and Python check `sec19:ex19.5`.

### Worked Example — Template 6: Linear Spring-Loaded Piston Expansion + Ideal-Gas First-Law Accounting `[Rules 5.c.ii, 5.c.iv]`

A vertical cylinder of cross-sectional area $A_p = 0.0100 m^2$ contains $n = 0.500 mol$ of a diatomic ideal gas ($C_{V,m} = \frac{5}{2}R$) initially at $P_1 = 120.0 kPa$ and $V_1 = 10.00 L$ ($0.0100 m^3$). The frictionless piston is restrained by a linear Hookean spring of spring constant $k_s = 1.600 kN/m$ ($1600 N/m$). Heat $Q$ is transferred slowly to the gas until its volume doubles to $V_2 = 20.00 L$ ($0.0200 m^3$). Find: (a) the initial and final gas temperatures $T_1, T_2$ and final pressure $P_2$, (b) the boundary work $W_{\mathrm{by}}$ done by the gas (separating work against the initial pressure force vs. elastic energy stored in the spring), and (c) the total heat $Q$ added.
**Solution.**
(a) Piston displacement: $\Delta x = \frac{V_2 - V_1}{A_p} = \frac{0.0100 m^3}{0.0100 m^2} = 1.000 m$. By mechanical force balance on the piston, gas pressure increases linearly with volume:
$$P_2 = P_1 + \frac{k_s\,\Delta x}{A_p} = P_1 + \frac{k_s}{A_p^2}(V_2 - V_1) = 120.0 kPa + \frac{1.600 kN/m}{0.0100 m^2}(1.000 m) = 120.0 + 160.0 = \mathbf{280.0 kPa}$$
By the ideal-gas law $T = \frac{P V}{n R}$:
$$T_1 = \frac{(120.0×10^{3} Pa)(0.0100 m^3)}{(0.500)(8.3144626 J/mol/K)} = \mathbf{288.65 K}, \qquad T_2 = \frac{(280.0×10^{3} Pa)(0.0200 m^3)}{(0.500)(8.3144626 J/mol/K)} = \mathbf{1347.05 K}$$
(b) Because $P(V)$ is a straight line from $(V_1, P_1)$ to $(V_2, P_2)$, the area under the $P$–$V$ path is a trapezoid Eq. (`eq:18:chordwork`):
$$W_{\mathrm{by}} = \frac{P_1 + P_2}{2}\,(V_2 - V_1) = \frac{120.0 + 280.0}{2}\,kPa\times(20.00 L - 10.00 L) = (200.0 kPa)(10.00 L) = \mathbf{2000.0 J} = \mathbf{2.000 kJ}$$
*(Physical Decomposition Check: Work against the constant baseline load $P_1$ is $P_1\Delta V = (120.0 kPa)(10.00 L) = 1200.0 J$, and elastic potential energy stored in the spring is $\Delta E_{\mathrm{spring}} = \frac{1}{2}k_s(\Delta x)^2 = \frac{1}{2}(1600 N/m)(1.000 m)^2 = 800.0 J$; total $W_{\mathrm{by}} = 1200.0 + 800.0 = 2000.0 J$!).*
(c) For a diatomic ideal gas, $\Delta U = n C_{V,m}(T_2 - T_1) = \frac{5}{2}nR(T_2 - T_1) = \frac{5}{2}(P_2 V_2 - P_1 V_1)$:
$$\Delta U = \frac{5}{2}\left[(280.0 kPa)(20.00 L) - (120.0 kPa)(10.00 L)\right] = 2.5\left(5600.0 - 1200.0\right) = \mathbf{11000.0 J} = \mathbf{11.000 kJ}$$
By the First Law $\Delta U = Q - W_{\mathrm{by}}$:
$$Q = \Delta U + W_{\mathrm{by}} = 11.000 kJ + 2.000 kJ = \mathbf{13.000 kJ}$$

**✓ Verified by:** Spring-energy + enthalpy/internal-energy conservation and Python check `sec19:ex19.6`.

### Worked Example — Template 7: Planetary Radiative Equilibrium & Deep-Space $T^4$ Vacuum Cooling Time `[`MIT E3 Q23 & GGSO E4 Q14d`  **[S27,S28]**]`

A spherical probe of diameter $D_p = 0.500 m$ (projected disk area $A_{\mathrm{proj}} = \frac{\pi}{4}D_p^2$, total spherical surface area $A_{\mathrm{surf}} = \pi D_p^2 = 4 A_{\mathrm{proj}}$), total thermal capacitance $C_p = m c = 12.50 kJ/K$, solar absorptance $\alpha_{\mathrm{sol}} = 0.800$, and thermal-IR emittance $\varepsilon_{\mathrm{IR}} = 0.250$ orbits in vacuum at a distance where solar irradiance is $I_0 = 1361.0 W/m^2$. (a) Find the probe's steady-state radiative equilibrium temperature $T_{\mathrm{eq}}$ in sunlight (assuming rapid rotation or high internal conductivity so $\mathrm{Bi} \ll 1$). (b) The probe then enters a total planetary eclipse (deep-space background $T_{\mathrm{space}} \approx 0 K$). Using the closed-form $T^4$ radiative cooling formula (Archetype 4 in Table `tab:19:archetypes`), calculate the elapsed time $\Delta t$ for the probe to cool from $T_i = T_{\mathrm{eq}}$ down to $T_f = 280.0 K$.
**Solution.**
(a) In steady radiative equilibrium, solar power absorbed over the projected cross-section $\alpha_{\mathrm{sol}} A_{\mathrm{proj}} I_0$ equals thermal-IR power emitted over the full spherical surface $\varepsilon_{\mathrm{IR}} A_{\mathrm{surf}} \sigma T_{\mathrm{eq}}^4$. Since $A_{\mathrm{proj}} / A_{\mathrm{surf}} = 1/4$:
$$T_{\mathrm{eq}} = \left(\frac{\alpha_{\mathrm{sol}}\,I_0}{4\,\varepsilon_{\mathrm{IR}}\,\sigma}\right)^{1/4} = \left(\frac{(0.800)(1361.0 W/m^2)}{4(0.250)(5.670374×10^{-8} W/m^2/K^4)}\right)^{1/4} = \left(1.920155×10^{10}\right)^{1/4} = \mathbf{372.25 K}\ (99.10 °C)$$
(b) Total spherical emitting area: $A_{\mathrm{surf}} = \pi(0.500 m)^2 = 0.785398 m^2$. During eclipse in vacuum ($T_{\mathrm{surr}} \to 0 K$), $C_p\frac{dT}{dt} = -\varepsilon_{\mathrm{IR}}\sigma A_{\mathrm{surf}} T^4$. Applying the pre-integrated algebraic formula from Table `tab:19:archetypes` (Row 4):
$$\Delta t = \frac{C_p}{3\,\varepsilon_{\mathrm{IR}}\,\sigma\,A_{\mathrm{surf}}}\left(\frac{1}{T_f^3} - \frac{1}{T_i^3}\right) = \frac{12500 J/K}{3(0.250)(5.670374×10^{-8})(0.785398 m^2)}\left(\frac{1}{280.0^3} - \frac{1}{372.251^3}\right)$$
$$\Delta t = (3.74232×10^{11})\left(4.55539×10^{-8} - 1.93855×10^{-8}\right) = (3.74232×10^{11})(2.61684×10^{-8}) = \mathbf{9793.0 s} = \mathbf{163.22 min}\ (2.720 h)$$

**✓ Verified by:** Direct ODE numerical quadrature $\int_{280}^{372.251} C_p(\varepsilon\sigma A T^4)^{-1}dT = 9793.0 s$ and Python check `sec19:ex19.7`.

### Worked Example — Template 8: Two-Stage Intercooled Adiabatic Gas Compression vs. Single-Stage Compression `[`MIT E2 P4b TB #1`  **[S26]**]`

An industrial compressor compresses $n = 2.000 mol$ of dry air (treated as a diatomic ideal gas with $\gamma = 1.400$, $C_{P,m} = \frac{7}{2}R = 29.1006 J/mol/K$) from intake state $P_1 = 100.0 kPa$, $T_1 = 300.0 K$ to final discharge pressure $P_3 = 900.0 kPa$. Compare: (a) the work input $W_{\mathrm{on,1\text{-}stage}}$ and final temperature $T_{f,1\text{-}stage}$ for a single reversible adiabatic compression from $P_1$ to $P_3$, versus (b) the total work input $W_{\mathrm{on,2\text{-}stage}}$ and intercooler heat rejected $Q_{\mathrm{ic}}$ when compressed in **two reversible adiabatic stages** through the optimal geometric-mean intermediate pressure $P_2 = \sqrt{P_1 P_3}$ with isobaric intercooling back to $T_1 = 300.0 K$ between stages, and (c) the isothermal lower bound $W_{\mathrm{on,iso}}$ at $T_1 = 300.0 K$.
**Solution.**
(a) **Single-Stage Reversible Adiabatic Compression ($P_1 = 100.0 kPa \to P_3 = 900.0 kPa$, pressure ratio $r_p = 9.000$):**
With $\frac{\gamma - 1}{\gamma} = \frac{0.400}{1.400} = \frac{2}{7} \approx 0.285714$:
$$T_{f,1\text{-}stage} = T_1\left(\frac{P_3}{P_1}\right)^{(\gamma-1)/\gamma} = (300.0 K)(9.000)^{2/7} = (300.0)(1.87344) = \mathbf{562.03 K}\ (288.88 °C)$$
For a steady-flow adiabatic compressor (shaft work $\dot{W}_{\mathrm{on,sh}} = \Delta H = n C_{P,m}\Delta T$, or closed-system adiabatic work $W_{\mathrm{on,closed}} = \Delta U = n C_{V,m}\Delta T = \frac{1}{\gamma}\Delta H$):
$$W_{\mathrm{on,sh,1\text{-}stage}} = n C_{P,m}(T_{f,1} - T_1) = (2.000)(29.1006 J/mol/K)(562.033 - 300.0) = \mathbf{15250.6 J} = \mathbf{15.251 kJ}$$
*(Closed-system piston work without flow work $\Delta(PV)$ is $W_{\mathrm{on,closed,1}} = \frac{15.2506}{1.400} = \mathbf{10.893 kJ}$).*
(b) **Two-Stage Intercooled Compression Through Optimal $P_2 = \sqrt{P_1 P_3} = \sqrt{(100.0)(900.0)} = \mathbf{300.0 kPa}$:**
Each stage has pressure ratio $\frac{P_2}{P_1} = \frac{P_3}{P_2} = 3.000$, so both stages exit at identical temperature $T_{\mathrm{exit}}$:
$$T_{\mathrm{exit}} = T_1(3.000)^{2/7} = (300.0 K)(1.36874) = \mathbf{410.62 K}\ (137.47 °C)$$
Total two-stage steady-flow shaft work input:
$$W_{\mathrm{on,sh,2\text{-}stage}} = 2\,n C_{P,m}(T_{\mathrm{exit}} - T_1) = 2(2.000)(29.1006 J/mol/K)(410.621 - 300.0) = \mathbf{12876.6 J} = \mathbf{12.877 kJ}$$
*(Closed-system piston work: $W_{\mathrm{on,closed,2}} = \frac{12.8766}{1.400} = \mathbf{9.198 kJ}$).* The isobaric intercooler at $P_2 = 300.0 kPa$ cools the gas from $410.62 K$ back to $300.0 K$, rejecting heat $Q_{\mathrm{out,ic}} = n C_{P,m}(410.621 - 300.0) = \mathbf{6.438 kJ}$ and saving $15.251 - 12.877 = \mathbf{2.374 kJ}$ ($\mathbf{15.6\%}$) of compressor shaft work!
(c) **Reversible Isothermal Compression Lower Bound ($N \to \infty$ stages at $T_1 = 300.0 K$):**
$$W_{\mathrm{on,iso}} = n R T_1 \ln\!\left(\frac{P_3}{P_1}\right) = (2.000)(8.3144626 J/mol/K)(300.0 K)\ln(9.000) = \mathbf{10961.2 J} = \mathbf{10.961 kJ}$$
*(Ordering Check: $W_{\mathrm{on,iso}} = 10.961 kJ < W_{\mathrm{on,sh,2\text{-}stage}} = 12.877 kJ < W_{\mathrm{on,sh,1\text{-}stage}} = 15.251 kJ$. Confirmed!)*

**✓ Verified by:** Exact equality of stage pressure ratios $P_2/P_1 = P_3/P_2 = 3.0$ and Python check `sec19:ex19.8`.

## Class III Scientific Calculator Speed Playbook (`Rule 2.b` — TI-36X Pro / Casio fx-991EX)

Under 2027 Rule `2.b` and the Science Olympiad Calculator Policy  **[S01]**, each competitor may bring a dedicated **Class III non-programmable, non-graphing scientific calculator** (two calculators per team). Storing the 8 fundamental CODATA 2022 constants  **[S07]** in non-volatile memory registers before the event block saves $3–5 min$ of keystroke entry and prevents transcription typos:

**Table:** Pre-Block Class III Calculator Memory Register Map & Built-In Solver Workflows (`TI-36X Pro` & `Casio fx-115ES/991EX`)  **[S01,S07]**.

| **Register** | **Constant Stored** | **Exact Value to Store** | **SI Units** | **Instant Competition Keystroke Macro** |
| --- | --- | --- | --- | --- |
| **`A`** | Universal gas constant $R$ | $8.314462618$ | $J/mol/K$ | $C_{V,m} = 1.5`A`$ (mono), $2.5`A`$ (di); $P = n`A`T/V$ |
| **`B`** | Stefan–Boltzmann $\sigma$ | $5.670374419×10^{-8}$ | $W/m^2/K^4$ | $\dot{Q}_{\mathrm{rad}} = \varepsilon`B`A(T^4 - T_0^4)$ |
| **`C`** | Boltzmann constant $k_B$ | $1.380649×10^{-23}$ | $J/K$ | $S = `C`\ln\Omega$;\quad $\bar{K}_{\mathrm{tr}} = 1.5`C`T$ |
| **`D`** | Avogadro constant $N_A$ | $6.02214076×10^{23}$ | $/mol$ | $N = n`D`$;\quad $m_{\mathrm{molecule}} = M/`D`$ |
| **`E`** | Specific heat of water $c_w$ | $4184$ | $J/kg/K$ | $Q_w = m`E`\Delta T$;\quad $1 cal _{ th } = `E`/1000\,J$ |
| **`F`** | Standard atmosphere $P_{\mathrm{atm}}$ | $101325$ | $Pa$ | $P_{\mathrm{abs}} = P_{\mathrm{gauge}} + `F`$;\quad $1 L · atm = `F`/1000\,J$ |
| **`X`** (or `M`) | Water fusion latent heat $L_f$ | $333550$ | $J/kg$ | $Q_{\mathrm{melt}} = m`X`$ ($333.55 J/g$) |
| **`Y`** | Water vaporization $L_v(100 °C)$ | $2256400$ | $J/kg$ | $Q_{\mathrm{boil}} = m`Y`$ ($2256.4 J/g$) |
- **30-Second 2-Variable Linear Regression (`data` / `stat-reg` $\to$ `2-Var Stats` $y = a + bx$):** Enter $X_k$ in `L1` and $Y_k$ in `L2` (you can type $\ln(62 - 26.95)$ or $1000/(60 + 273.15)$ directly into the list cell!). Select `LinReg(a+bx)` to read slope $b$ (or $m$), intercept $a$, and correlation $r$ to 9 digits in $5 s$.
- **Numerical Solver (`num-solv` / `SHIFT-SOLVE`) for Mixed Convection + $T^4$ Radiation (`2027 Cornell E1 Q16`):** To solve $h(T_s - T_\infty) + \varepsilon\sigma(T_s^4 - T_\infty^4) = q''_{\mathrm{abs}}$ for surface temperature $T_s$ without fourth-degree algebra, enter the equation with unknown $X$, seed $X_0 = 330 K$ (always seed a positive Kelvin temperature $T_0 \in 250–1000 K$ so Newton's method never locks onto the unphysical negative root $-T_s$!), and press `Solve`.

—
**See also:** §`sec:00` (`fig:00:router` 10-Second Router), §`sec:01` (`QS-01`..`QS-14`), §`sec:04`–§`sec:13` (Core Physics & Transfer), §`sec:17`–§`sec:18` (Lab & Data Analysis), §`sec:20` (Error Catalog), §`sec:21` (Partner Exam Strategy), and §`app:B` (Target-Variable Equation Chooser).
