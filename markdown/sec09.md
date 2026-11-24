<!-- Source: src/sec09.tex | Tab: Tab 4: GASES/LAWS | Target: 12 pp -->
# §9: Heat Engines, Refrigerators, Heat Pumps, Carnot Bounds & Named Thermodynamic Cycles {#sec:09}

> **[SCOPE: REQUIRED | 2027 Rule 5.c.iv (All Tournament Levels) | Complete Power & Refrigeration Cycle Atlas]**

Thermodynamic cycles and cyclic devices (engines, refrigerators, and heat pumps) are core Rule `5.c.iv` topics tested at every competition level  **[S01,S25,S26,S30]**. Every cycle equation in this chapter follows the positive-magnitude convention ($Q_H > 0, Q_C > 0, W > 0$) and is solved using pure algebra and geometry under Rule `5.d.iii–iv`  **[S06,S13]**.

## Heat Engines ($\eta$), Refrigerators ($\mathrm{COP}_R$), Heat Pumps ($\mathrm{COP}_{\mathrm{HP}}$) & Cycle Orientation

Over one complete cycle of any closed-loop device, the working fluid returns to its initial state ($\Delta U_{\mathrm{cycle}} = 0, \Delta H_{\mathrm{cycle}} = 0, \Delta S_{\mathrm{fluid,cycle}} = 0$). Taking heat absorbed from the hot reservoir $Q_H = |Q_{\mathrm{in}}| > 0$ and heat rejected to the cold reservoir $Q_C = |Q_{\mathrm{out}}| > 0$ as **positive magnitudes**, the First Law enforces $\boxed{Q_H = Q_C + W}$ for both power and refrigeration cycles  **[S13,S14]**:

### [FORMULA & DECISION CARD: Master Efficiency & Coefficient of Performance (COP) Ledger  **[S08,S13,S33]**]

| **Cyclic Device** | **Loop Direction** | **Desired / Paid** | **Universal First-Law Formula** | **Reversible Carnot Limit ($T$ in $K$!)** |
| --- | --- | --- | --- | --- |
| **1. Heat Engine** | **Clockwise** | $\dfrac{\text{Net Work } W_{\mathrm{net}}}{\text{Heat Input } Q_H}$ | $\displaystyle \eta = \frac{W_{\mathrm{net}}}{Q_H} = \frac{Q_H - Q_C}{Q_H} = 1 - \frac{Q_C}{Q_H}$ | $\displaystyle \eta_{\mathrm{Carnot}} = 1 - \frac{T_C}{T_H} < 1$ |
| **2. Refrigerator / AC** | **Counterclockwise** | $\dfrac{\text{Cold Heat } Q_C}{\text{Work Input } W_{\mathrm{in}}}$ | $\displaystyle \mathrm{COP}_R = \frac{Q_C}{W_{\mathrm{in}}} = \frac{Q_C}{Q_H - Q_C}$ | $\displaystyle \mathrm{COP}_{R,\mathrm{Carnot}} = \frac{T_C}{T_H - T_C} \in (0,\infty)$ |
| **3. Heat Pump** | **Counterclockwise** | $\dfrac{\text{Hot Heat } Q_H}{\text{Work Input } W_{\mathrm{in}}}$ | $\displaystyle \mathrm{COP}_{\mathrm{HP}} = \frac{Q_H}{W_{\mathrm{in}}} = \frac{Q_H}{Q_H - Q_C}$ | $\displaystyle \mathrm{COP}_{\mathrm{HP,Carnot}} = \frac{T_H}{T_H - T_C} = \frac{1}{\eta_{\mathrm{Carnot}}} > 1$ |

- **Universal Exact Identity ($\mathrm{COP}_{\mathrm{HP}} = \mathrm{COP}_R + 1$):** Dividing the First Law $Q_H = Q_C + W_{\mathrm{in}}$ by $W_{\mathrm{in}}$ yields $\boxed{\mathrm{COP}_{\mathrm{HP}} = \mathrm{COP}_R + 1}$ for **every** real or ideal refrigerator/heat pump operating between the same two states! Because $Q_C \ge 0$, $\mathrm{COP}_{\mathrm{HP}}$ is **always $\ge 1$** (where $\mathrm{COP}_{\mathrm{HP}} = 1$ corresponds to an electric space heater converting $100\%$ of $W_{\mathrm{in}}$ directly into $Q_H$ with $Q_C = 0$).
- **Enclosed Loop Area Identity on $P$–$V$ and $T$–$S$ Diagrams:** For any internally reversible closed cycle, the net work output equals the enclosed area on **both** the $P$–$V$ plane and the $T$–$S$ plane:
  
$$
\begin{aligned}

    \boxed{W_{\mathrm{net,by}} = \mathrm{Area}_{P\text{--}V} = \mathrm{Area}_{T\text{--}S} = Q_{\mathrm{net}}} \quad (+\text{ for clockwise power loop; } -\text{ for counterclockwise refrigeration loop})
\end{aligned}
$$
- **HVAC Engineering Rating Conversions (NIST SP 811  **[S08]**):**
- **1 Ton of Refrigeration:** The heat rate required to melt $1\text{ short ton}$ ($2000 lbm$) of ice at $0 °C$ ($32 ° F$) in $24 h$: $\boxed{1 ton = 200 BTU _{ IT }/min = 12000 BTU _{ IT }/h = 3516.85 W \approx 3.517 kW}$.
- **Energy Efficiency Ratio ($\mathrm{EER}$):** Cooling capacity in $BTU _{ IT }/h$ divided by electrical power input in $W$: $\boxed{\mathrm{EER} = 3.41214\,\mathrm{COP}_R}$.
  

### Worked Example — Heat Pump vs. Electric Space Heater & Ton-of-Refrigeration Chiller Audit `[Regional/State Standard | Tier 1]`

(a) A residential heat pump maintains a house interior at $T_H = 22.00 °C$ ($295.15 K$) when the outdoor winter air is at $T_C = -5.00 °C$ ($268.15 K$). The heat-loss rate through the house envelope is $\dot{Q}_{\mathrm{loss}} = 18.00 kW$. If the heat pump achieves a Second-Law efficiency of $\eta_{\mathrm{II}} = 45.00\%$ of the Carnot limit, find its actual $\mathrm{COP}_{\mathrm{HP}}$, the required electrical power input $\dot{W}_{\mathrm{in}}$, the rate of heat extracted from the cold outdoor air $\dot{Q}_C$, and the electrical power saved compared to a $100\%$-efficient electric baseboard resistance heater.
(b) An industrial chiller rated at $15.00 tons of refrigeration$ has an $\mathrm{EER} = 11.94\,BTU/(·h···W·)$. Find its cooling rate $\dot{Q}_C$ in $kW$, its $\mathrm{COP}_R$, its compressor power $\dot{W}_{\mathrm{in}}$, and its condenser heat-rejection rate $\dot{Q}_H$.
**Solution.**
- **(a) Heat pump $\mathrm{COP}_{\mathrm{HP}}$, electrical power $\dot{W}_{\mathrm{in}}$, and cold-air heat extraction $\dot{Q}_C$:**
  
$$
\mathrm{COP}_{\mathrm{HP,Carnot}} = \frac{T_H}{T_H - T_C} = \frac{295.15}{295.15 - 268.15} = \frac{295.15}{27.00} = \mathbf{10.9315}, \qquad \mathrm{COP}_{\mathrm{HP,actual}} = 0.4500(10.9315) = \mathbf{4.9192}
$$

  
$$
\dot{W}_{\mathrm{in}} = \frac{\dot{Q}_H}{\mathrm{COP}_{\mathrm{HP,actual}}} = \frac{18.00 kW}{4.9192} = \mathbf{3.6592 kW}, \qquad \dot{Q}_C = \dot{Q}_H - \dot{W}_{\mathrm{in}} = 18.00 - 3.6592 = \mathbf{14.341 kW}
$$

  An electric resistance heater ($\mathrm{COP} = 1.00$) requires $18.00 kW$ of electricity, so the heat pump saves $\dot{W}_{\mathrm{saved}} = \dot{Q}_C = \mathbf{14.341 kW}$ ($79.67\%$) by pumping free thermal energy from the $-5 °C$ outdoor air!
- **(b) $15.00 ton$ chiller metrics:**
  
$$
\dot{Q}_C = 15.00 \times 3.51685 kW = \mathbf{52.753 kW}, \qquad \mathrm{COP}_R = \frac{\mathrm{EER}}{3.41214} = \frac{11.94}{3.41214} = \mathbf{3.4993}
$$

  
$$
\dot{W}_{\mathrm{in}} = \frac{\dot{Q}_C}{\mathrm{COP}_R} = \frac{52.753}{3.4993} = \mathbf{15.075 kW}, \qquad \dot{Q}_H = \dot{Q}_C + \dot{W}_{\mathrm{in}} = 52.753 + 15.075 = \mathbf{67.828 kW}
$$

**✓ Verified by:** Identity $\mathrm{COP}_{\mathrm{HP}} = \dot{Q}_H/\dot{W}_{\mathrm{in}} = 67.828/15.075 = 4.4993 = \mathrm{COP}_R + 1$ (`check_sec06_09.py::ex09_1`).

## The Carnot Cycle, Carnot's Theorem & Impossible-Machine Claim Diagnostics

Sadi Carnot (1824) proved that the most efficient cycle operating between two reservoirs at $T_H$ and $T_C$ must transfer all heat **isothermally** (zero $\Delta T$ across reservoir boundaries) and change temperature **adiabatically**  **[S13,S23]**:
- **Leg $1\to 2$ (Reversible Isothermal Expansion at $T_H$):** Absorbs $Q_H = W_{1\to 2} = nRT_H\ln(V_2/V_1) > 0$; $\Delta S_{1\to 2} = +Q_H/T_H = +nR\ln(V_2/V_1)$.
- **Leg $2\to 3$ (Reversible Adiabatic Expansion $T_H \to T_C$):** $Q_{2\to 3} = 0$, $\Delta S_{2\to 3} = 0$, $W_{2\to 3} = +nC_{V,m}(T_H - T_C)$, and $T_H V_2^{\gamma-1} = T_C V_3^{\gamma-1}$.
- **Leg $3\to 4$ (Reversible Isothermal Compression at $T_C$):** Rejects $Q_C = |W_{3\to 4}| = nRT_C\ln(V_3/V_4) > 0$; $\Delta S_{3\to 4} = -Q_C/T_C = -nR\ln(V_3/V_4)$.
- **Leg $4\to 1$ (Reversible Adiabatic Compression $T_C \to T_H$):** $Q_{4\to 1} = 0$, $\Delta S_{4\to 1} = 0$, $W_{4\to 1} = -nC_{V,m}(T_H - T_C) = -W_{2\to 3}$, and $T_H V_1^{\gamma-1} = T_C V_4^{\gamma-1}$.

Dividing the two adiabatic volume relations $T_H V_2^{\gamma-1} = T_C V_3^{\gamma-1}$ and $T_H V_1^{\gamma-1} = T_C V_4^{\gamma-1}$ yields the exact **Carnot Volume-Ratio Symmetry** and **Kelvin Thermodynamic Temperature Ratio**:

$$
\begin{aligned}

  \boxed{\frac{V_2}{V_1} = \frac{V_3}{V_4}, \qquad \frac{P_1}{P_2} = \frac{P_4}{P_3}}, \qquad \implies \qquad \boxed{\left(\frac{Q_C}{Q_H}\right)_{\mathrm{rev}} = \frac{nRT_C\ln(V_3/V_4)}{nRT_H\ln(V_2/V_1)} = \frac{T_C}{T_H}}, \qquad \boxed{\eta_{\mathrm{Carnot}} = 1 - \frac{T_C}{T_H}}
\end{aligned}
$$

> **[Vector Figure: Paired (a) $P$–$V$ and (b) $T$–$S$ representations of the reversible Carnot heat engine cycle  **[S13]**. On the $T$–$S$ plane, the two isotherms are horizontal and the two isentropes are vertical, forming a rectangle of total heat height $T_H$, waste-heat base height $T_C$, and width $\Delta S = S_2 - S_1 = nR\ln(V_2/V_1)$. | Label: `fig:09:carnot-pv-ts`]**
> - **Diagram Annotations & Key Elements:** **Title:** **(a) Carnot Cycle on $P$–$V$ Plane (2 Isotherms + 2 Adiabats)** • **Title:** **(b) Carnot Cycle on $T$–$S$ Plane (Exact Rectangle!)** • **X-Axis:** Volume $V$ ($L$) • **X-Axis:** Entropy $S$ ($J/K$) • **Y-Axis:** Pressure $P$ ($kPa$) • **Y-Axis:** Absolute Temperature $T$ ($K$) • $T_H=\mathrm{const}$ ($Q_H$ in) • $T_C=\mathrm{const}$ ($Q_C$ out) • $Q=0$ • $W_{\mathrm{net}} = (T_H - T_C)\Delta S$ / $\eta_C = \dfrac{W_{\mathrm{net}}}{Q_H} = 1 - \dfrac{T_C}{T_H}$ • Rejected Heat Area / $Q_C = T_C(S_2 - S_1)$

### [FORMULA & DECISION CARD: Carnot Sensitivity Rule, 3-Way Machine Claim Audit & Curzon–Ahlborn Power Limit  **[S13,S33]**]
- **Lowering $T_C$ Beats Raising $T_H$ by the Same $\Delta T > 0$ (Algebraic Proof):**
  Compare decreasing the cold sink to $T_C - \Delta T$ versus increasing the hot source to $T_H + \Delta T$:
  
$$
\begin{aligned}

    \eta_{\mathrm{low\ }T_C} = 1 - \frac{T_C - \Delta T}{T_H} = \eta_C + \frac{\Delta T}{T_H} \quad > \quad \eta_{\mathrm{high\ }T_H} = 1 - \frac{T_C}{T_H + \Delta T} = \eta_C + \frac{T_C\,\Delta T}{T_H(T_H + \Delta T)}
\end{aligned}
$$

  
  Because $\frac{T_C}{T_H + \Delta T} < 1$, **lowering $T_C$ by $\Delta T$ ALWAYS produces a larger increase in Carnot efficiency than raising $T_H$ by $\Delta T$**!
- **Two-Step Inventor Claim Diagnostic Protocol (First-Law + Second-Law Audit):**
  Given claimed cyclic transfers $(Q_H, Q_C, W)$ between reservoirs at $(T_H, T_C)$:
- *Check 1 (First Law):* Does $Q_H = Q_C + W$? If $Q_H \ne Q_C + W$, the claim violates **Conservation of Energy (First Law / PMM1)**.
- *Check 2 (Second Law / Clausius Entropy Generation):* Compute universe entropy generation per cycle:
    {$$
\begin{aligned}

      S_{\mathrm{gen,cycle}} = \begin{cases} \dfrac{Q_C}{T_C} - \dfrac{Q_H}{T_H} & \text{(Engine: } \eta \le \eta_C\text{)}\\[5pt] \dfrac{Q_H}{T_H} - \dfrac{Q_C}{T_C} & \text{(Refrig/HP: } \mathrm{COP} \le \mathrm{COP}_C\text{)} \end{cases} \Rightarrow \begin{cases} S_{\mathrm{gen}} > 0: & \text{**Possible \& Irreversible** (real)}\\ S_{\mathrm{gen}} = 0: & \text{**Possible \& Reversible** (Carnot)}\\ S_{\mathrm{gen}} < 0: & \text{**IMPOSSIBLE** (violates 2nd Law)} \end{cases}
\end{aligned}
$$

- **Curzon–Ahlborn Efficiency at Maximum Power Output (`[SUPPLEMENTARY / NATIONALS]`):**
  An ideal Carnot engine requires zero temperature drop across its heat exchangers and therefore runs infinitely slowly ($\dot{W} \to 0$). For an endoreversible engine with finite heat-exchanger conductance maximizing power output $\dot{W}_{\max}$:
  
$$
\begin{aligned}

    \boxed{\eta_{\mathrm{CA}} = 1 - \sqrt{\frac{T_C}{T_H}}} \quad (\text{accurately predicts real nuclear/coal/geothermal plant efficiencies within } 2\text{--}4\%!)
\end{aligned}
$$

  

### Worked Example — 4-Vertex Carnot Gas Engine Ledger & Three-Inventor Claim Audit `[State/National Standard | Tier 2]`

(a) Two moles ($n = 2.000 mol$) of a diatomic ideal gas ($\gamma = 1.400, C_{V,m} = \frac{5}{2}R$) operate in a Carnot engine between $T_H = 600.0 K$ and $T_C = 300.0 K$. At the start of isothermal expansion, $P_1 = 1000.0 kPa$ ($V_1 = 9.9774 L$), and at the end of isothermal expansion $V_2 = 2.000\,V_1 = 19.955 L$. Calculate $V_3, V_4, Q_H, Q_C$, the adiabatic expansion work $W_{2\to 3}$, the net cycle work $W_{\mathrm{net}}$, and $\eta_C$.
(b) Audit three engine claims operating between $T_H = 600.0 K$ and $T_C = 300.0 K$ with $Q_H = 100.0 kJ$: Claim A ($W = 40.0 kJ, Q_C = 60.0 kJ$); Claim B ($W = 55.0 kJ, Q_C = 45.0 kJ$); Claim C ($W = 45.0 kJ, Q_C = 50.0 kJ$).
**Solution.**
- **(a) Carnot vertex volumes and work/heat transfers ($nR = 16.6289 J/K$):**
  Along adiabat $2\to 3$, $V_3/V_2 = (T_H/T_C)^{1/(\gamma-1)} = (600.0/300.0)^{1/0.400} = 2^{2.500} = 4\sqrt{2} = 5.65685$:
  
$$
V_3 = 5.65685(19.955 L) = \mathbf{112.88 L}, \qquad V_4 = \frac{V_1}{V_2}V_3 = 0.5000(112.88) = \mathbf{56.440 L}
$$

  
$$
Q_H = nRT_H\ln\left(\frac{V_2}{V_1}\right) = (16.6289)(600.0)\ln(2.000) = \mathbf{6915.7 J}, \quad Q_C = nRT_C\ln\left(\frac{V_3}{V_4}\right) = (16.6289)(300.0)\ln(2.000) = \mathbf{3457.8 J}
$$

  
$$
W_{2\to 3} = +nC_{V,m}(T_H - T_C) = (2.000)(2.5\times 8.314463)(300.0) = \mathbf{+12471.7 J} = -W_{4\to 1}
$$

  
$$
W_{\mathrm{net}} = Q_H - Q_C = 6915.7 - 3457.8 = \mathbf{3457.8 J}, \qquad \eta_C = 1 - \frac{300.0}{600.0} = \mathbf{0.5000} \quad (50.00\%)
$$
- **(b) Three-claim feasibility audit from Eq. (`eq:09:claim-audit`):**
- **Claim A:** $Q_H = 40+60 = 100 kJ$ (1st Law OK); $S_{\mathrm{gen}} = 60/300 - 100/600 = +0.0333\,kJ/K > 0$ ($\eta = 40\% < 50\% \implies$ **Valid irreversible engine**).
- **Claim B:** $Q_H = 55+45 = 100 kJ$ (1st Law OK); $S_{\mathrm{gen}} = 45/300 - 100/600 = -0.0167\,kJ/K < 0$ ($\eta = 55\% > 50\% \implies$ **Violates 2nd Law / PMM2**).
- **Claim C:** $W + Q_C = 45 + 50 = 95 kJ \ne Q_H = 100 kJ \implies$ **Violates 1st Law (energy not conserved!)**.
  

**✓ Verified by:** Total work sum $W_{1\to 2} + W_{2\to 3} + W_{3\to 4} + W_{4\to 1} = 6915.7 + 12471.7 - 3457.8 - 12471.7 = 3457.8 J = W_{\mathrm{net}}$ (`check_sec06_09.py::ex09_2`).

## Master Comparison Atlas of Named Power & Refrigeration Cycles

**Table:** Master Comparison Atlas of the 8 Named Thermodynamic Cycles (2027 Rule `5.c.iv`)  **[S13,S25,S30,S33]**.

| **Cycle Name** | **4 Constituent Legs** | **Heat In $Q_H$** | **Heat Out $Q_C$** | **Closed Algebraic $\eta$ or $\mathrm{COP}$** | **Defining Ratios & Competition Notes** |
| --- | --- | --- | --- | --- | --- |
| **(& Application)** | ($1\to 2\to 3\to 4\to 1$) | **Process** | **Process** | **Formula** |  |
| **1. Carnot** | $1\to 2$: Isothermal ($T_H$) | Isothermal | Isothermal | $\displaystyle \eta_C = 1 - \frac{T_C}{T_H}$ | Upper bound for all engines between $T_H, T_C$; |
| (Reversible Limit) | $2\to 3, 4\to 1$: Isentropic | ($T = T_H$) | ($T = T_C$) |  | rectangle on $T$–$S$ diagram. |
| **2. Otto** | $1\to 2, 3\to 4$: Isentropic | Isochoric | Isochoric | $\displaystyle \eta_{\mathrm{Otto}} = 1 - \frac{1}{r^{\gamma - 1}} = 1 - \frac{T_1}{T_2}$ | Compression ratio $r = V_1/V_2 = V_{\max}/V_{\min}$ |
| (Gasoline Spark-Ign.) | $2\to 3, 4\to 1$: Isochoric | ($V = V_2$) | ($V = V_1$) |  | (typical $r = 8\text{--}12$, limited by auto-ignition knock). |
| **3. Diesel** | $1\to 2, 3\to 4$: Isentropic | Isobaric | Isochoric | $\displaystyle \eta_{\mathrm{Diesel}} = 1 - \frac{1}{r^{\gamma - 1}}\left[\frac{r_c^\gamma - 1}{\gamma(r_c - 1)}\right]$ | $r = V_1/V_2$; cutoff ratio $r_c = V_3/V_2 = T_3/T_2 > 1$. |
| (Compression-Ign.) | $2\to 3$: Isobar; $4\to 1$: Isochor | ($P = P_2$) | ($V = V_1$) |  | At equal $r$, $\eta_{\mathrm{Otto}} > \eta_{\mathrm{Diesel}}$; actual $r = 15\text{--}22$. |
| **4. Brayton / Joule** | $1\to 2, 3\to 4$: Isentropic | Isobaric | Isobaric | $\displaystyle \eta_{\mathrm{Brayton}} = 1 - \frac{1}{r_p^{(\gamma - 1)/\gamma}} = 1 - \frac{T_1}{T_2}$ | Pressure ratio $r_p = P_2/P_1$. Max work per kg for |
| (Gas Turbine / Jet) | $2\to 3, 4\to 1$: Isobaric | ($P = P_2$) | ($P = P_1$) |  | fixed $T_1, T_3$ occurs at $T_2 = T_4 = \sqrt{T_1 T_3}$. |
| **5. Stirling** | $1\to 2, 3\to 4$: Isothermal | Isothermal $T_H$ | Isothermal $T_C$ | **100% Regen.:** $\displaystyle \eta = 1 - \frac{T_C}{T_H} = \eta_C$ | Internal regenerator exchanges $nC_{V,m}(T_H-T_C)$ |
| (Regen. External) | $2\to 3, 4\to 1$: Isochoric | (+Regen $4\to 1$) | (+Regen $2\to 3$) | **No Regen.:** $\frac{R(T_H-T_C)\ln(V_2/V_1)}{RT_H\ln(V_2/V_1)+C_{V,m}(T_H-T_C)}$ | between isochores $2\to 3$ and $4\to 1$. |
| **6. Ericsson** | $1\to 2, 3\to 4$: Isothermal | Isothermal $T_H$ | Isothermal $T_C$ | **100% Regen.:** $\displaystyle \eta = 1 - \frac{T_C}{T_H} = \eta_C$ | Internal regenerator exchanges $nC_{P,m}(T_H-T_C)$ |
| (Regen. Isobaric) | $2\to 3, 4\to 1$: Isobaric | (+Regen $4\to 1$) | (+Regen $2\to 3$) |  | between isobars $2\to 3$ and $4\to 1$. |
| **7. Rankine** | $1\to 2$: Pump; $2\to 3$: Boiler | Isobaric Boiler | Isobaric Cond. | $\displaystyle \eta_{\mathrm{Rank}} = \frac{(h_3 - h_4) - (h_2 - h_1)}{h_3 - h_2}$ | Liquid pump work $w_p = h_2-h_1 \approx v_{f,1}(P_2-P_1)$ |
| (Steam Power Plant) | $3\to 4$: Turbine; $4\to 1$: Cond. | $q_H = h_3 - h_2$ | $q_C = h_4 - h_1$ |  | is $<1\%$ of turbine output $w_t = h_3 - h_4$! |
| **8. Vapor-Compr.** | $1\to 2$: Compr.; $2\to 3$: Cond. | Evaporator | Condenser | $\displaystyle \mathrm{COP}_R = \frac{q_C}{w_{\mathrm{in}}} = \frac{h_1 - h_4}{h_2 - h_1}$ | Throttle valve ($3\to 4$) is strictly **isenthalpic** |
| **Refrigeration** | $3\to 4$: Throttle; $4\to 1$: Evap. | $q_C = h_1 - h_4$ | $q_H = h_2 - h_3$ |  | ($\mathbf{h_4 = h_3}$, irreversible $\Delta s > 0$). |

## Reciprocating Internal-Combustion Cycles: Air-Standard Otto vs. Diesel

In reciprocating piston engines, let $V_1 = V_{\max}$ be the cylinder volume at Bottom Dead Center (BDC) and $V_2 = V_{\min}$ be the clearance volume at Top Dead Center (TDC), defining the **compression ratio** $r \equiv V_1/V_2$ and **Mean Effective Pressure** $\mathrm{MEP} \equiv W_{\mathrm{net}}/(V_1 - V_2)$  **[S13,S33]**:

### [FORMULA & DECISION CARD: Algebra-Only Derivations of Otto & Diesel Cycle Efficiencies  **[S13,S33]**]
- **Air-Standard Otto Cycle (Gasoline Spark-Ignition — Isochoric Heat Addition $2\to 3$ at $V_2$):**
  Along isentropic compression $1\to 2$ ($V_1\to V_2$) and isentropic power stroke $3\to 4$ ($V_2\to V_1$):
  
$$
\frac{T_2}{T_1} = \left(\frac{V_1}{V_2}\right)^{\gamma - 1} = r^{\gamma - 1} = \frac{T_3}{T_4} \implies \frac{T_4 - T_1}{T_3 - T_2} = \frac{T_1}{T_2} = \frac{1}{r^{\gamma - 1}}
$$

  Since heat enters at constant volume $V_2$ ($Q_H = nC_{V,m}(T_3 - T_2)$) and exits at constant volume $V_1$ ($Q_C = nC_{V,m}(T_4 - T_1)$):
  
$$
\begin{aligned}

    \boxed{\eta_{\mathrm{Otto}} = 1 - \frac{Q_C}{Q_H} = 1 - \frac{T_4 - T_1}{T_3 - T_2} = 1 - \frac{1}{r^{\gamma - 1}}}
\end{aligned}
$$

  
- **Air-Standard Diesel Cycle (Compression-Ignition — Isobaric Heat Addition $2\to 3$ from $V_2$ to $V_3 = r_c V_2$):**
  Fuel is injected into hot compressed air at $P_2 = P_3$, expanding the volume by the **cutoff ratio** $r_c \equiv V_3/V_2 = T_3/T_2 > 1$ before isentropic expansion $3\to 4$ (expansion ratio $r_e = V_1/V_3 = r/r_c$). Using $T_2 = T_1 r^{\gamma-1}$, $T_3 = T_1 r^{\gamma-1} r_c$, and $T_4 = T_3(V_3/V_1)^{\gamma-1} = T_1 r_c^\gamma$, together with $Q_H = nC_{P,m}(T_3 - T_2)$ and $Q_C = nC_{V,m}(T_4 - T_1)$:
  
$$
\begin{aligned}

    \boxed{\eta_{\mathrm{Diesel}} = 1 - \frac{C_{V,m}(T_4 - T_1)}{C_{P,m}(T_3 - T_2)} = 1 - \frac{1}{r^{\gamma - 1}}\left[\frac{r_c^\gamma - 1}{\gamma(r_c - 1)}\right]}
\end{aligned}
$$

  
  *Otto vs. Diesel Exam Trap:* For any $r_c > 1$, the bracket factor $\frac{r_c^\gamma - 1}{\gamma(r_c - 1)} > 1$ (and approaches $1$ as $r_c \to 1$). Therefore:
- **At the SAME compression ratio $r$:** $\mathbf{\eta_{\mathrm{Otto}}(r) > \eta_{\mathrm{Diesel}}(r, r_c)}$ (and for a Dual cycle with mixed isochoric + isobaric combustion, $\eta_{\mathrm{Otto}} > \eta_{\mathrm{Dual}} > \eta_{\mathrm{Diesel}}$).
- **In REAL engines:** Diesel engines compress *only air* during $1\to 2$ (no fuel pre-ignition knock), allowing much higher compression ratios ($r_{\mathrm{Diesel}} \approx 16\text{--}22$ vs. $r_{\mathrm{Otto}} \approx 8\text{--}11$), so **actual Diesel engines are more efficient than actual Otto engines**!
  

> **[Vector Figure: Paired $P$–$V$ indicator diagrams of (a) the air-standard Otto cycle (isochoric heat addition $2\to 3$ at $V_2$) and (b) the air-standard Diesel cycle (isobaric fuel injection and combustion $2\to 3$ from $V_2$ to $V_3 = r_c V_2$)  **[S13,S33]**. | Label: `fig:09:otto-diesel`]**
> - **Diagram Annotations & Key Elements:** **Title:** **(a) Air-Standard Otto Cycle ($V=\mathrm{const}$ Heat Add)** • **Title:** **(b) Air-Standard Diesel Cycle ($P=\mathrm{const}$ Heat Add)** • **X-Axis:** Volume $V$ (showing $V_2 = V_{\min}$ and $V_1 = r V_2$) • **X-Axis:** Volume $V$ (showing $V_2$, $V_3 = r_c V_2$, $V_1 = r V_2$) • **Y-Axis:** Pressure $P$ ($kPa$) • **Y-Axis:** Pressure $P$ ($kPa$) • $PV^\gamma = \mathrm{const}$

### Worked Example — Otto vs. Diesel Cycle Efficiency, Peak Temperature & MEP Comparison `[Invitational/State Standard | Tier 2]`

(a) An air-standard Otto engine ($\gamma = 1.400, c_v = 718.6 J/kg/K, R_s = 287.05 J/kg/K$) operates with compression ratio $r = 9.500$. Air enters at State 1 ($P_1 = 100.0 kPa, T_1 = 300.0 K$) and absorbs $q_H = 800.0 kJ/kg$ during isochoric combustion $2\to 3$. Find $\eta_{\mathrm{Otto}}$, $T_2, P_2$, peak temperature $T_3$, peak pressure $P_3$, net specific work $w_{\mathrm{net}}$, and the Mean Effective Pressure ($\mathrm{MEP}$).
(b) Compare $\eta_{\mathrm{Otto}}$ at $r = 9.500$ with (i) a Diesel engine running at the same $r = 9.500$ and cutoff ratio $r_c = 2.000$, and (ii) a realistic Diesel engine running at $r = 18.00$ and $r_c = 2.000$.
**Solution.**
- **(a) Air-standard Otto cycle ($r = 9.500, r^{\gamma-1} = 9.500^{0.400} = 2.46078$):**
  
$$
\eta_{\mathrm{Otto}} = 1 - \frac{1}{9.500^{0.400}} = 1 - \frac{1}{2.46078} = \mathbf{0.59363} \quad (59.36\%)
$$

  
$$
T_2 = T_1 r^{\gamma-1} = (300.0)(2.46078) = \mathbf{738.24 K}, \qquad P_2 = P_1 r^\gamma = (100.0)(9.500^{1.400}) = \mathbf{2337.7 kPa}
$$

  
$$
T_3 = T_2 + \frac{q_H}{c_v} = 738.24 + \frac{800000 J/kg}{718.6 J/kg/K} = 738.24 + 1113.28 = \mathbf{1851.5 K}, \qquad P_3 = P_2\frac{T_3}{T_2} = \mathbf{5863.2 kPa}
$$

  
$$
w_{\mathrm{net}} = \eta_{\mathrm{Otto}} q_H = (0.59363)(800.0) = \mathbf{474.90 kJ/kg}
$$

  With specific volume $v_1 = R_s T_1 / P_1 = (287.05)(300.0)/100000 = 0.86115 m^3/kg$ and $v_2 = v_1 / 9.500 = 0.090647 m^3/kg$:
  
$$
\mathrm{MEP} = \frac{w_{\mathrm{net}}}{v_1 - v_2} = \frac{474.90 kJ/kg}{0.86115 - 0.090647\,m^3/kg} = \mathbf{616.35 kPa}
$$
- **(b) Diesel cycle comparison at $r_c = 2.000$ (bracket factor $\frac{2.000^{1.400} - 1}{1.400(2.000 - 1)} = \frac{1.63902}{1.400} = 1.17073 > 1$):**
  
$$
\eta_{\mathrm{Diesel}}(r=9.50) = 1 - \frac{1.17073}{2.46078} = \mathbf{0.52425} \ (52.42\% < \eta_{\mathrm{Otto}}), \quad \eta_{\mathrm{Diesel}}(r=18.0) = 1 - \frac{1.17073}{18.00^{0.400}} = \mathbf{0.63158} \ (63.16\% > \eta_{\mathrm{Otto}})
$$

**✓ Verified by:** Fourth Otto vertex check: $T_4 = T_3/r^{\gamma-1} = 752.41 K$, $q_C = c_v(T_4-T_1) = 325.10 kJ/kg$, $q_H - q_C = 474.90 kJ/kg$ (`check_sec06_09.py::ex09_3`).

## Gas-Turbine & Regenerative Cycles: Brayton, Stirling & Ericsson

### [FORMULA & DECISION CARD: Brayton Maximum-Work Theorem & Regenerative Stirling/Ericsson Cycles  **[S13,S30,S33]**]
- **Air-Standard Brayton / Joule Cycle (2 Isobars at $P_1, P_2$ + 2 Isentropes; Pressure Ratio $r_p \equiv P_2/P_1$):**
  Along isentropic compression $1\to 2$ and expansion $3\to 4$: $\frac{T_2}{T_1} = \frac{T_3}{T_4} = r_p^{(\gamma-1)/\gamma}$, yielding:
  
$$
\begin{aligned}

    \boxed{\eta_{\mathrm{Brayton}} = 1 - \frac{c_p(T_4 - T_1)}{c_p(T_3 - T_2)} = 1 - \frac{T_1}{T_2} = 1 - \frac{1}{r_p^{(\gamma - 1)/\gamma}}}, \qquad \mathrm{BWR} = \frac{w_{\mathrm{comp}}}{w_{\mathrm{turb}}} = \frac{T_2 - T_1}{T_3 - T_4} = \frac{T_2}{T_3} = \frac{T_1}{T_3}r_p^{(\gamma-1)/\gamma}
\end{aligned}
$$

  
- **Algebra-Only AM–GM Proof of Optimal Brayton Pressure Ratio for Maximum Net Work:**
  In a gas turbine with fixed ambient inlet temperature $T_1 = T_{\min}$ and metallurgical turbine-blade limit $T_3 = T_{\max}$, since $T_2 T_4 = T_1 T_3 = T_{\min}T_{\max}$, the specific net work $w_{\mathrm{net}} = c_p(T_3 - T_2 - T_4 + T_1) = c_p\left[T_{\max} + T_{\min} - (T_2 + T_{\min}T_{\max}/T_2)\right]$ is maximized when $T_2 + \frac{T_{\min}T_{\max}}{T_2}$ is minimized. By the AM–GM inequality, this occurs at the geometric mean:
  
$$
\begin{aligned}

    \boxed{T_2^* = T_4^* = \sqrt{T_1 T_3} = \sqrt{T_{\min}T_{\max}}}, \qquad \boxed{r_{p,\mathrm{opt}} = \left(\frac{T_{\max}}{T_{\min}}\right)^{\frac{\gamma}{2(\gamma - 1)}}}, \qquad \boxed{w_{\mathrm{net,\max}} = c_p\left(\sqrt{T_{\max}} - \sqrt{T_{\min}}\right)^2}
\end{aligned}
$$

  
  Notice that at maximum net work, the Brayton efficiency equals the Curzon–Ahlborn efficiency $\eta_{\mathrm{Brayton}}(r_{p,\mathrm{opt}}) = 1 - \sqrt{T_{\min}/T_{\max}}$!
- **Stirling Cycle ($2\text{ Isotherms} + 2\text{ Isochores}$) & Ericsson Cycle ($2\text{ Isotherms} + 2\text{ Isobars}$) with Regeneration:**
  In a Stirling engine (`2018 Cornell E6`), the heat released by the gas during isochoric cooling $2\to 3$ ($Q_{\mathrm{regen,max}} = nC_{V,m}(T_H - T_C)$) equals the heat required during isochoric warming $4\to 1$. With a porous-mesh regenerator of effectiveness $\varepsilon_{\mathrm{reg}} \in [0, 1]$ recycling fraction $\varepsilon_{\mathrm{reg}}$ internally:
  
$$
\begin{aligned}

    \boxed{\eta_{\mathrm{Stirling}}(\varepsilon_{\mathrm{reg}}) = \frac{W_{\mathrm{net}}}{Q_{H,\mathrm{ext}}} = \frac{R(T_H - T_C)\ln(V_{\max}/V_{\min})}{R T_H\ln(V_{\max}/V_{\min}) + (1 - \varepsilon_{\mathrm{reg}})C_{V,m}(T_H - T_C)}} \xrightarrow{\varepsilon_{\mathrm{reg}} = 1} \boxed{1 - \frac{T_C}{T_H} = \eta_{\mathrm{Carnot}}}
\end{aligned}
$$

  
  (For the Ericsson cycle with regeneration effectiveness $\varepsilon_{\mathrm{reg}}$, replace $C_{V,m}$ with $C_{P,m}$ and $\ln(V_{\max}/V_{\min})$ with $\ln(P_{\max}/P_{\min})$.)

> **[Vector Figure: Paired $P$–$V$ diagrams of (a) the Brayton gas-turbine cycle (2 isobars + 2 isentropes) and (b) the Stirling cycle (2 isotherms + 2 isochores), where an internal porous regenerator recycles $Q_{\mathrm{regen}} = nC_{V,m}(T_H - T_C)$ between legs $2\to 3$ and $4\to 1$ to attain full Carnot efficiency  **[S13,S30]**. | Label: `fig:09:brayton-stirling`]**
> - **Diagram Annotations & Key Elements:** **Title:** **(a) Air-Standard Brayton Cycle ($r_p = P_2/P_1$)** • **Title:** **(b) Regenerative Stirling Cycle ($2\text{ Isotherms} + 2\text{ Isochores}$)** • **X-Axis:** Specific Volume $v$ ($m^3/kg$) • **X-Axis:** Volume $V$ (between $V_1 = V_{\min}$ and $V_2 = V_{\max}$) • **Y-Axis:** Pressure $P$ ($kPa$) • **Y-Axis:** Pressure $P$ ($kPa$) • $T_H=\mathrm{const}$ ($Q_H$ in) • $T_C=\mathrm{const}$ ($Q_C$ out)

### Worked Example — Brayton Maximum-Work Design & Stirling Regenerator Effectiveness Audit `[2018 Cornell E6 Archetype | Tier 3]`

(a) An air-standard Brayton gas turbine ($\gamma = 1.400, c_p = 1.0062 kJ/kg/K$) operates between compressor inlet $T_1 = 300.0 K$ and turbine metallurgical limit $T_3 = 1470.0 K$. Find the optimal pressure ratio $r_{p,\mathrm{opt}}$ that maximizes net work per unit mass, the compressor/turbine exit temperatures $T_2^*, T_4^*$, the maximum net specific work $w_{\mathrm{net,\max}}$, the cycle efficiency $\eta_{\mathrm{Brayton}}(r_{p,\mathrm{opt}})$, and the back-work ratio $\mathrm{BWR}$.
(b) A Stirling engine using $n = 1.000 mol$ of diatomic nitrogen ($C_{V,m} = \frac{5}{2}R$) operates between $T_H = 900.0 K$ and $T_C = 300.0 K$ with volume compression ratio $V_{\max}/V_{\min} = 2.000$ (as in Worked Example `ex:07.6`). Compare its thermal efficiency $\eta$ for: (i) zero regeneration ($\varepsilon_{\mathrm{reg}} = 0$), (ii) $\varepsilon_{\mathrm{reg}} = 0.850$, and (iii) ideal regeneration ($\varepsilon_{\mathrm{reg}} = 1.000$).
**Solution.**
- **(a) Brayton maximum-work optimization from Eq. (`eq:09:brayton`)–Eq. (`eq:09:brayton-opt`):**
  
$$
T_2^* = T_4^* = \sqrt{T_1 T_3} = \sqrt{(300.0)(1470.0)} = \mathbf{664.08 K}, \qquad r_{p,\mathrm{opt}} = \left(\frac{T_2^*}{T_1}\right)^{\frac{\gamma}{\gamma - 1}} = \left(\frac{664.08}{300.0}\right)^{3.500} = (2.21359)^{3.500} = \mathbf{16.120}
$$

  
$$
w_{\mathrm{net,\max}} = c_p\left(\sqrt{T_3} - \sqrt{T_1}\right)^2 = (1.0062 kJ/kg/K)(1470.0 + 300.0 - 2\times 664.08) = 1.0062(441.84) = \mathbf{444.58 kJ/kg}
$$

  
$$
\eta_{\mathrm{Brayton}}(r_{p,\mathrm{opt}}) = 1 - \frac{T_1}{T_2^*} = 1 - \frac{300.0}{664.08} = \mathbf{0.54825} \ (54.82\%), \quad \mathrm{BWR} = \frac{T_2^*}{T_3} = \frac{664.08}{1470.0} = \mathbf{0.45175} \ (45.18\%)
$$
- **(b) Stirling cycle efficiency vs. regenerator effectiveness from Eq. (`eq:09:stirling`):**
  From Worked Example `ex:07.6`, $W_{\mathrm{net}} = nR(T_H - T_C)\ln 2 = 3457.4 J$, isothermal heat input is $Q_{1\to 2} = nRT_H\ln 2 = 5186.1 J$, and isochoric heat is $Q_{\mathrm{isochor}} = nC_{V,m}(T_H - T_C) = 12471.7 J$:
  
$$
\eta(0) = \frac{3457.4}{5186.1 + 12471.7} = \mathbf{19.58\%}, \quad \eta(0.850) = \frac{3457.4}{5186.1 + 0.150(12471.7)} = \mathbf{48.99\%}, \quad \eta(1) = \frac{3457.4}{5186.1} = \mathbf{66.67\%} = \eta_C
$$

**✓ Verified by:** Without a regenerator, the Stirling engine loses $47.1$ percentage points of efficiency because $Q_{\mathrm{isochor}} = 2.405\,Q_{1\to 2}$ (`check_sec06_09.py::ex09_4`).

## Vapor Power & Refrigeration Cycles: Rankine & Vapor-Compression (`2027 Cornell E1`)

> **[Vector Figure: Paired $T$–$s$ saturation-dome diagrams of (a) the Rankine vapor power cycle (clockwise, with liquid pump $1\to 2$ and steam turbine $3\to 4$) and (b) the vapor-compression refrigeration cycle (counterclockwise, replacing a wet expansion turbine with an irreversible isenthalpic throttle valve $3\to 4$ where $h_4 = h_3$ and $s_4 > s_3$)  **[S25,S33]**. | Label: `fig:09:rankine-refrigerator`]**
> - **Diagram Annotations & Key Elements:** **Title:** **(a) Rankine Steam Power Cycle (Clockwise on $T$–$s$)** • **Title:** **(b) Vapor-Compression Refrigerator (CCW on $T$–$s$)** • **X-Axis:** Specific Entropy $s$ ($kJ/kg/K$) • **X-Axis:** Specific Entropy $s$ ($kJ/kg/K$) • **Y-Axis:** Temperature $T$ ($K$) • **Y-Axis:** Temperature $T$ ($K$)

### Worked Example — Complete Rankine Steam Plant (`2027 Cornell E1 Q29`) & Vapor-Compression Chiller `[2027 Cornell E1 Q29a,d,f | Tier 3]`

(a) In `2027 Cornell E1 Q29`, a Rankine steam engine operates between a boiler at $T_{\mathrm{boil}} = 130.0 °C$ ($403.15 K, P_{\mathrm{boil}} = 270.28 kPa$) and a condenser at $T_{\mathrm{cond}} = 110.0 °C$ ($383.15 K, P_{\mathrm{cond}} = 143.38 kPa$). Dry saturated steam enters the turbine from the boiler ($h_{\mathrm{boil},g} = 2718.6 kJ/kg, s_{\mathrm{boil},g} = 6.9931 kJ/kg/K$). At $110.0 °C$, $v_f = 0.001052 m^3/kg, h_f = 461.29 kJ/kg, h_{fg} = 2229.6 kJ/kg, s_f = 1.4188 kJ/kg/K$, and $s_g = 7.2380 kJ/kg/K$ ($s_{fg} = 5.8192 kJ/kg/K$). Calculate: (i) the ideal isentropic turbine exit quality $x_{\mathrm{exit},s}$ and enthalpy $h_{\mathrm{exit},s}$, (ii) the pump work $w_p = v_f(P_{\mathrm{boil}} - P_{\mathrm{cond}})$, boiler heat $q_{\mathrm{in}}$, ideal turbine work $w_{t,s}$, and ideal First-Law efficiency $\eta_{\mathrm{I}}$, and (iii) the required steam mass flow rate $\dot{m}$ to deliver $\dot{W}_{\mathrm{actual}} = 50.00 kW$ if the turbine has isentropic efficiency $\eta_s = 0.8000$.
(b) An R134a vapor-compression refrigerator takes saturated vapor at $P_{\mathrm{evap}} = 200.0 kPa$ ($h_1 = 392.6 kJ/kg$), compresses it to $P_{\mathrm{cond}} = 800.0 kPa$ ($h_2 = 428.6 kJ/kg$), condenses it to saturated liquid ($h_3 = 243.6 kJ/kg$), and throttles it back to $200.0 kPa$ ($h_{f,\mathrm{evap}} = 186.6 kJ/kg, h_{fg,\mathrm{evap}} = 206.0 kJ/kg$). Find $h_4$, quality $x_4$, $q_C, w_{\mathrm{in}}, q_H$, and $\mathrm{COP}_R$.
**Solution.**
- **(a) Rankine cycle analysis (`2027 Cornell E1 Q29`):**
- *(i) Isentropic turbine exit quality ($s_{\mathrm{exit},s} = s_{\mathrm{boil},g} = 6.9931 kJ/kg/K$):*
    
$$
x_{\mathrm{exit},s} = \frac{s_{\mathrm{boil},g} - s_{f,110}}{s_{fg,110}} = \frac{6.9931 - 1.4188}{7.2380 - 1.4188} = \frac{5.5743}{5.8192} = \mathbf{0.95792}, \quad h_{\mathrm{exit},s} = 461.29 + 0.95792(2229.6) = \mathbf{2597.1 kJ/kg}
$$
- *(ii) Pump work, turbine work, and First-Law efficiency:*
    
$$
w_p = v_f(P_{\mathrm{boil}} - P_{\mathrm{cond}}) = (0.001052)(270.28 - 143.38) = \mathbf{0.1335 kJ/kg}, \quad h_{\mathrm{pump,out}} = 461.29 + 0.1335 = 461.42 kJ/kg
$$

    
$$
q_{\mathrm{in}} = 2718.6 - 461.42 = \mathbf{2257.2 kJ/kg}, \quad w_{t,s} = 2718.6 - 2597.1 = \mathbf{121.53 kJ/kg}, \quad \eta_{\mathrm{I}} = \frac{121.53 - 0.13}{2257.2} = \mathbf{5.378\%}
$$

    *(Note: Using Cornell E1's backup table value $h_{fg,110} = 2232 kJ/kg$ and $s_{g,110}=7.21 kJ/kg/K$ gave $x_{2s} = 0.9624, w_{t,s} = 109.92 kJ/kg, \eta_{\mathrm{I}} = 4.870\%$, as evaluated in Worked Example `ex:08.6`.)*
- *(iii) Steam mass flow rate for $\eta_s = 0.8000$ ($w_{t,a} = 0.8000\times 121.53 = 97.23 kJ/kg$, $w_{\mathrm{net},a} = 97.09 kJ/kg$):*
    
$$
\dot{m} = \frac{\dot{W}_{\mathrm{actual}}}{w_{\mathrm{net},a}} = \frac{50.00 kW}{97.09 kJ/kg} = \mathbf{0.5150 kg/s}
$$
- **(b) R134a vapor-compression chiller ($h_4 = h_3 = 243.6 kJ/kg$ across throttle):**
  
$$
x_4 = \frac{243.6 - 186.6}{206.0} = \mathbf{0.2767}, \quad q_C = h_1 - h_4 = 392.6 - 243.6 = \mathbf{149.0 kJ/kg}, \quad w_{\mathrm{in}} = h_2 - h_1 = 428.6 - 392.6 = \mathbf{36.0 kJ/kg}
$$

  
$$
q_H = h_2 - h_3 = 428.6 - 243.6 = \mathbf{185.0 kJ/kg} = q_C + w_{\mathrm{in}}, \qquad \mathrm{COP}_R = \frac{q_C}{w_{\mathrm{in}}} = \frac{149.0}{36.0} = \mathbf{4.139}
$$

**✓ Verified by:** Pump work is only $0.1335/121.53 = 0.11\%$ of turbine work; refrigeration energy balance $149.0 + 36.0 = 185.0\,kJ/kg$ (`check_sec06_09.py::ex09_5`).

## Compound, Cascaded & Combined Cycles (Series Engines & Engine-Driven Chillers)

### [FORMULA & DECISION CARD: Algebraic Formulas for Cascaded Engines, Cascaded Chillers & Coupled Systems  **[S13,S33]**]
- **Two Heat Engines in Series / Combined Cycle (Engine 1 rejects $Q_{C,1} = (1 - \eta_1)Q_H$ directly as heat input $Q_{H,2}$ to Engine 2):**
  Total work is $W_{\mathrm{tot}} = W_1 + W_2 = \eta_1 Q_H + \eta_2(1 - \eta_1)Q_H$, yielding the universal **Combined-Cycle Efficiency Identity**:
  
$$
\begin{aligned}

    \boxed{\eta_{\mathrm{combined}} = \eta_1 + \eta_2 - \eta_1\eta_2 = 1 - (1 - \eta_1)(1 - \eta_2)} \quad \xrightarrow{N\text{ stages}} \quad \eta_{1..N} = 1 - \prod_{k=1}^N (1 - \eta_k)
\end{aligned}
$$

  
  *Two Cascaded Carnot Engines ($T_H \to T_{\mathrm{mid}} \to T_C$):* Since $(1 - \eta_{C,1})(1 - \eta_{C,2}) = \frac{T_{\mathrm{mid}}}{T_H}\frac{T_C}{T_{\mathrm{mid}}} = \frac{T_C}{T_H}$, the combined Carnot efficiency is always $1 - T_C/T_H$ regardless of $T_{\mathrm{mid}}$! However, the intermediate temperature $T_{\mathrm{mid}}$ satisfies two classic tiebreaker conditions:
  
$$
\begin{aligned}

    W_1 = W_2 \iff \boxed{T_{\mathrm{mid}} = \frac{T_H + T_C}{2} \text{ (arith.\ mean)}}; \qquad \eta_1 = \eta_2 \iff \boxed{T_{\mathrm{mid}} = \sqrt{T_H T_C} \text{ (geom.\ mean)}}
\end{aligned}
$$

  
- **Two Refrigerators in Series / Cascade ($T_C \to T_{\mathrm{mid}} \to T_H$, where Condenser 1 feeds Evaporator 2, $Q_{H,1} = Q_{C,2}$):**
  
$$
\begin{aligned}

    \boxed{\mathrm{COP}_{R,\mathrm{cascade}} = \frac{\mathrm{COP}_{R,1}\,\mathrm{COP}_{R,2}}{1 + \mathrm{COP}_{R,1} + \mathrm{COP}_{R,2}}} \iff 1 + \frac{1}{\mathrm{COP}_{R,\mathrm{cascade}}} = \left(1 + \frac{1}{\mathrm{COP}_{R,1}}\right)\left(1 + \frac{1}{\mathrm{COP}_{R,2}}\right)
\end{aligned}
$$

  
- **Heat Engine ($T_H \to T_0$) Directly Driving a Refrigerator ($T_C \to T_0$) or Heat Pump ($T_0 \to T_{\mathrm{room}}$):**
  Setting $W_{\mathrm{eng}} = \eta_{\mathrm{eng}}Q_H$ equal to $W_{\mathrm{in}} = Q_C / \mathrm{COP}_R$ gives the overall heat ratio:
  
$$
\begin{aligned}

    \boxed{\frac{Q_C}{Q_H} = \eta_{\mathrm{eng}}\,\mathrm{COP}_R \le \left(1 - \frac{T_0}{T_H}\right)\left(\frac{T_C}{T_0 - T_C}\right)}, \qquad \frac{Q_{\mathrm{heating,tot}}}{Q_H} = 1 - \eta_{\mathrm{eng}} + \eta_{\mathrm{eng}}\,\mathrm{COP}_{\mathrm{HP}}
\end{aligned}
$$

### Worked Example — Brayton–Rankine Combined Cycle & Cascaded Carnot Equal-Work vs. Equal-$\eta$ Split `[National/Invitational | Tier 3]`

(a) A modern natural-gas combined-cycle power plant pairs a Brayton gas-turbine topping cycle ($\eta_1 = 38.00\%$) with a Rankine steam bottoming cycle ($\eta_2 = 32.00\%$) that recovers the gas turbine's exhaust heat. For a fuel heat input rate of $\dot{Q}_H = 500.0 MW$, find the overall combined efficiency $\eta_{\mathrm{combined}}$, the power output of each cycle ($\dot{W}_1, \dot{W}_2$), and the waste heat rejected to the river ($\dot{Q}_{C,2}$).
(b) Two reversible Carnot engines operate in series between $T_H = 900.0 K$ and $T_C = 100.0 K$. Compare the intermediate reservoir temperature $T_{\mathrm{mid}}$ and individual stage efficiencies $(\eta_1, \eta_2)$ when the engines produce (i) equal work ($W_1 = W_2$) versus (ii) equal thermal efficiency ($\eta_1 = \eta_2$).
**Solution.**
- **(a) Combined Brayton–Rankine plant from Eq. (`eq:09:cascade-engine`):**
  
$$
\eta_{\mathrm{combined}} = 0.3800 + 0.3200 - (0.3800)(0.3200) = 0.7000 - 0.1216 = \mathbf{0.5784} \quad (57.84\% \text{ — NOT } 38\%+32\%=70\%!)
$$

  
$$
\dot{W}_1 = 0.3800(500.0 MW) = \mathbf{190.0 MW}, \quad \dot{Q}_{C,1} = 310.0 MW \implies \dot{W}_2 = 0.3200(310.0 MW) = \mathbf{99.20 MW}, \quad \dot{Q}_{C,2} = \mathbf{210.8 MW}
$$
- **(b) Two cascaded Carnot engines between $T_H = 900.0 K$ and $T_C = 100.0 K$ ($\eta_{\mathrm{tot}} = 1 - 100/900 = 8/9 = 88.89\%$):**
- *(i) Equal work ($W_1 = W_2$):* $T_{\mathrm{mid}} = \frac{900.0 + 100.0}{2} = \mathbf{500.0 K} \implies \eta_1 = 1 - \frac{500}{900} = \mathbf{44.44\%}$, $\eta_2 = 1 - \frac{100}{500} = \mathbf{80.00\%}$.
- *(ii) Equal efficiency ($\eta_1 = \eta_2$):* $T_{\mathrm{mid}} = \sqrt{(900.0)(100.0)} = \mathbf{300.0 K} \implies \eta_1 = 1 - \frac{300}{900} = \mathbf{66.67\%}$, $\eta_2 = 1 - \frac{100}{300} = \mathbf{66.67\%}$.
  

**✓ Verified by:** Check (i) $1 - (1 - 4/9)(1 - 4/5) = 1 - (5/9)(1/5) = 8/9$; check (ii) $1 - (1 - 2/3)^2 = 8/9$ (`check_sec06_09.py::ex09_6`).

## Polygon $P$–$V$ Cycles, Dual Combustion, Regenerative Brayton & Ericsson Cycles

### [FORMULA & DECISION CARD: Polygon Cycle Positive-Heat Protocol, Dual Cycle & Regenerative Brayton Crossover  **[S13,S28,S33]**]
- **Polygon $P$–$V$ Cycle Efficiency Protocol (The $Q_H = \sum_{Q_k > 0} Q_k$ Positive-Leg Rule):**
  For a 3- or 4-sided polygon cycle (right triangle, rectangle, parallelogram) on a $P$–$V$ diagram:
- Compute $W_{\mathrm{net,by}}$ directly from the enclosed geometric area (e.g., $\frac{1}{2}\Delta P\Delta V$ for a triangle; $\Delta P\Delta V$ for a rectangle).
- Compute the heat transfer $Q_k = \Delta U_k + W_{\mathrm{by},k} = \frac{P_{\mathrm{end}}V_{\mathrm{end}} - P_{\mathrm{start}}V_{\mathrm{start}}}{\gamma - 1} + W_{\mathrm{by},k}$ along each leg $k$ individually.
- Sum **ONLY the positive heat inputs** to obtain $Q_H = \sum_{Q_k > 0} Q_k$, and evaluate $\boxed{\eta = \frac{W_{\mathrm{net,by}}}{\sum_{Q_k > 0} Q_k}}$ (never divide by $Q_{\mathrm{net}}$!).
- **Air-Standard Dual (Mixed Isochoric + Isobaric) Combustion Cycle:**
  Heat is added partly at constant volume $V_2$ (raising pressure by explosion ratio $r_p \equiv P_3/P_2 = T_3/T_2 > 1$) and partly at constant pressure $P_3$ (expanding volume by cutoff ratio $r_c \equiv V_4/V_3 = T_4/T_3 > 1$):
  
$$
\begin{aligned}

    \boxed{\eta_{\mathrm{Dual}} = 1 - \frac{1}{r^{\gamma - 1}}\left[\frac{r_p r_c^\gamma - 1}{(r_p - 1) + \gamma r_p(r_c - 1)}\right]} \quad (\text{reduces to Otto for } r_c=1 \text{ and Diesel for } r_p=1)
\end{aligned}
$$

  
- **Regenerative Brayton Gas-Turbine Cycle (Valid Only When $T_4 > T_2 \iff r_p < r_{p,\mathrm{opt}}$):**
  When turbine exhaust temperature $T_4$ exceeds compressor exit temperature $T_2$, an exhaust recuperator of effectiveness $\varepsilon_{\mathrm{reg}}=1$ preheats compressor air from $T_2$ to $T_4$, reducing combustor fuel heat to $q_H = c_p(T_3 - T_4)$ and exhaust waste heat to $q_C = c_p(T_2 - T_1)$:
  
$$
\begin{aligned}

    \boxed{\eta_{\mathrm{Brayton,regen}}(\varepsilon_{\mathrm{reg}}=1) = 1 - \frac{T_2 - T_1}{T_3 - T_4} = 1 - \left(\frac{T_1}{T_3}\right)r_p^{\frac{\gamma - 1}{\gamma}}} \quad (\text{crosses simple Brayton at } r_p = r_{p,\mathrm{opt}}!)
\end{aligned}
$$

  

### Worked Example — Right-Triangle $P$–$V$ Cycle Efficiency & Dual Combustion Cycle Ledger `[2019 GGSO E4 Archetype | Tier 3]`

(a) A monatomic ideal gas ($\gamma = 5/3, C_{V,m} = \frac{3}{2}R, C_{P,m} = \frac{5}{2}R$) executes a clockwise right-triangle cycle $A\to B\to C\to A$ on a $P$–$V$ diagram: State $A$ ($P_A = 100.0 kPa, V_A = 2.000 L$), State $B$ ($P_B = 400.0 kPa, V_B = 2.000 L$, isochoric rise $A\to B$), State $C$ ($P_C = 100.0 kPa, V_C = 6.000 L$, downward-sloping hypotenuse $B\to C$, followed by isobaric compression $C\to A$). Calculate $Q_{AB}, Q_{BC}, Q_{CA}$, net work $W_{\mathrm{net}}$, and the cycle thermal efficiency $\eta$ (assuming heat rejected during any sub-segment is not recovered).
(b) Compare the efficiency of a Dual cycle with compression ratio $r = 14.00$, $\gamma = 1.400$, isochoric pressure ratio $r_p = 1.500$, and isobaric cutoff ratio $r_c = 1.600$ against pure Otto ($r=14.00$) and pure Diesel ($r=14.00, r_c=1.600$) cycles.
**Solution.**
- **(a) Right-triangle cycle leg-by-leg energy audit ($P_A V_A = 200 J, P_B V_B = 800 J, P_C V_C = 600 J$):**
- *Enclosed triangle area:* $W_{\mathrm{net}} = +\frac{1}{2}(400.0 - 100.0)(6.000 - 2.000) = \mathbf{+600.0 J}$.
- *Leg $A\to B$ (Isochoric heating at $V=2.00 L$):* $W_{AB} = 0$, $Q_{AB} = \Delta U_{AB} = \frac{3}{2}(800.0 - 200.0) = \mathbf{+900.0 J} > 0$.
- *Leg $B\to C$ (Straight chord):* $W_{BC} = \frac{400.0+100.0}{2}(4.000) = +1000.0 J$, $\Delta U_{BC} = \frac{3}{2}(600.0 - 800.0) = -300.0 J \implies Q_{BC} = -300.0 + 1000.0 = \mathbf{+700.0 J} > 0$.
- *Leg $C\to A$ (Isobaric cooling at $P=100 kPa$):* $W_{CA} = 100.0(-4.000) = -400.0 J$, $\Delta U_{CA} = \frac{3}{2}(200.0 - 600.0) = -600.0 J \implies Q_{CA} = \mathbf{-1000.0 J} < 0$.
  

  Using the whole-leg positive-heat sum $Q_H = Q_{AB} + Q_{BC} = 900.0 + 700.0 = \mathbf{1600.0 J}$:
  
$$
\eta = \frac{W_{\mathrm{net}}}{Q_H} = \frac{600.0}{1600.0} = \mathbf{0.3750} \quad (37.50\%)
$$
- **(b) Dual cycle ($r=14.00, r^{\gamma-1} = 14.00^{0.400} = 2.8738, r_p = 1.500, r_c = 1.600$) from Eq. (`eq:09:dual-cycle`):**
  
$$
\eta_{\mathrm{Dual}} = 1 - \frac{1}{2.8738}\left[\frac{1.500(1.600^{1.400}) - 1}{(1.500 - 1) + 1.400(1.500)(1.600 - 1)}\right] = 1 - \frac{1}{2.8738}\left[\frac{1.8962}{1.7600}\right] = 1 - \frac{1.0774}{2.8738} = \mathbf{0.6251} \ (62.51\%)
$$

  Compared to $\eta_{\mathrm{Otto}}(14) = 1 - 1/2.8738 = \mathbf{65.20\%}$ and $\eta_{\mathrm{Diesel}}(14, 1.6) = 1 - 1.1066/2.8738 = \mathbf{61.49\%}$ ($\eta_{\mathrm{Otto}} > \eta_{\mathrm{Dual}} > \eta_{\mathrm{Diesel}}$!).

**✓ Verified by:** Heat sum on triangle cycle: $Q_{AB}+Q_{BC}+Q_{CA} = 900 + 700 - 1000 = 600.0 J = W_{\mathrm{net}}$ (`check_sec06_09.py::ex09_7`).

### Worked Example — Ericsson Cycle, Regenerative Brayton Crossover & Cascaded Cryo-Refrigerator `[National/Invitational | Tier 3]`

(a) In an air-standard Brayton gas turbine ($\gamma = 1.400$) with $T_1 = 300.0 K$ and $T_3 = 1500.0 K$, compare the simple Brayton efficiency Eq. (`eq:09:brayton`) and the ideal regenerative Brayton efficiency Eq. (`eq:09:brayton-regen`) at pressure ratio $r_p = 6.000$ versus $r_p = 25.00$, and find the exact crossover pressure ratio $r_p^*$ above which a regenerator becomes counterproductive!
(b) A two-stage cascaded cryogenic refrigerator uses Stage 1 ($\mathrm{COP}_{R,1} = 2.000$) between $T_C = 120.0 K$ and $T_{\mathrm{mid}} = 200.0 K$ and Stage 2 ($\mathrm{COP}_{R,2} = 3.000$) between $T_{\mathrm{mid}} = 200.0 K$ and room temperature $T_H = 300.0 K$. For a cold-box cooling load of $\dot{Q}_{C,1} = 12.00 kW$, find $\dot{W}_{\mathrm{in},1}, \dot{Q}_{H,1} = \dot{Q}_{C,2}, \dot{W}_{\mathrm{in},2}$, and the overall $\mathrm{COP}_{R,\mathrm{cascade}}$.
**Solution.**
- **(a) Simple vs. regenerative Brayton efficiencies ($T_1/T_3 = 300/1500 = 0.2000$):**
- *At $r_p = 6.000$ ($r_p^{2/7} = 1.6685$):* $\eta_{\mathrm{simple}} = 1 - \frac{1}{1.6685} = \mathbf{40.07\%}$, whereas $\eta_{\mathrm{regen}} = 1 - 0.2000(1.6685) = \mathbf{66.63\%}$ (regeneration boosts efficiency by $+26.56\%$ because $T_4 = 899.0 K \gg T_2 = 500.6 K$!).
- *At $r_p = 25.00$ ($r_p^{2/7} = 2.5094$):* $\eta_{\mathrm{simple}} = 1 - \frac{1}{2.5094} = \mathbf{60.15\%}$, whereas $\eta_{\mathrm{regen}} = 1 - 0.2000(2.5094) = \mathbf{49.81\%}$ (here $T_2 = 752.8 K > T_4 = 597.8 K$, so a regenerator would cool the compressed air!).
- *Crossover pressure ratio $r_p^* = r_{p,\mathrm{opt}}$ where $T_2 = T_4 = \sqrt{T_1 T_3} = 670.82 K$:*
    
$$
r_p^* = \left(\frac{T_3}{T_1}\right)^{\frac{\gamma}{2(\gamma - 1)}} = (5.000)^{1.750} = \mathbf{16.719} \quad (\text{where } \eta_{\mathrm{simple}} = \eta_{\mathrm{regen}} = 1 - 1/\sqrt{5} = \mathbf{55.28\%})
$$
- **(b) Two-stage cascaded cryo-chiller from Eq. (`eq:09:cascade-refrig`):**
  
$$
\dot{W}_{\mathrm{in},1} = \frac{\dot{Q}_{C,1}}{\mathrm{COP}_{R,1}} = \frac{12.00 kW}{2.000} = \mathbf{6.000 kW}, \qquad \dot{Q}_{H,1} = \dot{Q}_{C,2} = \dot{Q}_{C,1} + \dot{W}_{\mathrm{in},1} = 12.00 + 6.000 = \mathbf{18.00 kW}
$$

  
$$
\dot{W}_{\mathrm{in},2} = \frac{\dot{Q}_{C,2}}{\mathrm{COP}_{R,2}} = \frac{18.00 kW}{3.000} = \mathbf{6.000 kW} \implies \mathrm{COP}_{R,\mathrm{cascade}} = \frac{\dot{Q}_{C,1}}{\dot{W}_{\mathrm{in},1} + \dot{W}_{\mathrm{in},2}} = \frac{12.00}{6.000 + 6.000} = \mathbf{1.000}
$$

**✓ Verified by:** Formula Eq. (`eq:09:cascade-refrig`) check: $\mathrm{COP}_{R,\mathrm{cascade}} = (2.000\times 3.000)/(1 + 2.000 + 3.000) = 6.000/6.000 = 1.000$ (`check_sec06_09.py::ex09_8`).

### Worked Example — Ericsson Cycle Ledger & Engine-Driven Heat-Pump Heating Multiplier `[National/Invitational | Tier 3]`

(a) Two moles ($n = 2.000 mol$) of monatomic Helium ($\gamma = 5/3, C_{P,m} = \frac{5}{2}R = 20.786 J/mol/K$) execute a regenerative **Ericsson cycle** between $T_H = 800.0 K$ and $T_C = 400.0 K$, and between high pressure $P_{\max} = 500.0 kPa$ and low pressure $P_{\min} = 100.0 kPa$ ($P_{\max}/P_{\min} = 5.000$). Calculate the isothermal expansion heat $Q_{1\to 2}$, the isothermal compression heat rejected $Q_{3\to 4}$, the net cycle work $W_{\mathrm{net}}$, the isobaric regenerator heat load $Q_{\mathrm{regen}} = nC_{P,m}(T_H - T_C)$, and the cycle thermal efficiency with $\varepsilon_{\mathrm{reg}} = 1.000$ versus $\varepsilon_{\mathrm{reg}} = 0.000$.
(b) A reversible Carnot heat engine operates between a combustion furnace at $T_H = 1200.0 K$ and outdoor winter air at $T_0 = 270.0 K$. All of the engine's mechanical work $W$ drives a reversible Carnot heat pump that extracts heat from the outdoor air at $T_0 = 270.0 K$ and delivers heat $Q_{\mathrm{HP}}$ into a building at $T_{\mathrm{room}} = 300.0 K$. Meanwhile, the heat engine's waste heat $Q_{C,\mathrm{eng}}$ is also ducted directly into the building at $300.0 K$ (so the engine rejects heat at $T_{\mathrm{room}} = 300.0 K$). Find the total building heating multiplier $Q_{\mathrm{heating,tot}} / Q_H$ per unit of furnace fuel burned!
**Solution.**
- **(a) Ericsson cycle ($2\text{ isotherms} + 2\text{ isobars}$) ledger:**
  
$$
Q_{1\to 2} = nRT_H\ln\left(\frac{P_{\max}}{P_{\min}}\right) = (2.000)(8.314463)(800.0)\ln(5.000) = \mathbf{+21413.2 J}
$$

  
$$
Q_{3\to 4} = nRT_C\ln\left(\frac{P_{\max}}{P_{\min}}\right) = \mathbf{10706.6 J}, \qquad W_{\mathrm{net}} = Q_{1\to 2} - Q_{3\to 4} = \mathbf{+10706.6 J}
$$

  
$$
Q_{\mathrm{regen}} = nC_{P,m}(T_H - T_C) = (2.000)(2.5\times 8.314463)(800.0 - 400.0) = \mathbf{16628.9 J}
$$

  
$$
\eta_{\mathrm{Ericsson}}(\varepsilon_{\mathrm{reg}}=1) = \frac{10706.6}{21413.2} = \mathbf{50.00\%} = \eta_C, \qquad \eta_{\mathrm{Ericsson}}(\varepsilon_{\mathrm{reg}}=0) = \frac{10706.6}{21413.2 + 16628.9} = \mathbf{28.14\%}
$$
- **(b) Combined engine + heat-pump building heating multiplier from Eq. (`eq:09:engine-driven-chiller`):**
  With the engine operating between $T_H = 1200.0 K$ and $T_{\mathrm{room}} = 300.0 K$, its efficiency is $\eta_{\mathrm{eng}} = 1 - \frac{300.0}{1200.0} = \mathbf{0.7500}$, delivering work $W = 0.7500\,Q_H$ and direct exhaust heat $Q_{C,\mathrm{eng}} = 0.2500\,Q_H$ to the building. The heat pump operating between $T_0 = 270.0 K$ and $T_{\mathrm{room}} = 300.0 K$ has $\mathrm{COP}_{\mathrm{HP}} = \frac{300.0}{300.0 - 270.0} = \mathbf{10.00}$, delivering $Q_{\mathrm{HP}} = (10.00)(0.7500\,Q_H) = 7.500\,Q_H$. Total heat delivered to the building is:
  
$$
\frac{Q_{\mathrm{heating,tot}}}{Q_H} = \frac{Q_{C,\mathrm{eng}} + Q_{\mathrm{HP}}}{Q_H} = (1 - \eta_{\mathrm{eng}}) + \eta_{\mathrm{eng}}\,\mathrm{COP}_{\mathrm{HP}} = 0.2500 + 0.7500(10.00) = \mathbf{7.750}
$$

  Every $1.00 kJ$ of furnace heat delivers $7.75 kJ$ of space heating to the $300 K$ building (by pulling $6.75 kJ$ from the $270 K$ outdoor air)!

**✓ Verified by:** Universe entropy balance for reversible engine+HP system: $\Delta S_{\mathrm{univ}} = -Q_H/1200 - 6.75Q_H/270 + 7.75Q_H/300 = Q_H(-1/1200 - 1/40 + 31/1200) = 0$ (`check_sec06_09.py::ex09_9`).

### [TRAP & DIAGNOSTIC: Top 6 Heat-Engine, Refrigerator & Thermodynamic Cycle Traps (§9 Diagnostic Matrix)]

| **Wrong move / Symptom** | **What it produces / Why it fails** | **5-second diagnostic & fix** |
| --- | --- | --- |
| Substituting Celsius ($^\circ\mathrm{C}$) or Fahrenheit ($^\circ\mathrm{F}$) into $\eta_C = 1 - T_C/T_H$ or $\mathrm{COP}_C$ | Produces nonsense efficiencies (or division by zero at $0 °C$!). | Always convert $T_C$ and $T_H$ to **Kelvin** ($T_{\mathrm{K}} = T_{\mathrm{C}} + 273.15$) or Rankine ($T_{\mathrm{R}} = T_{\mathrm{F}} + 459.67$) before taking any ratio! |
| Confusing $\mathrm{COP}_R = Q_C/W_{\mathrm{in}}$ with $\mathrm{COP}_{\mathrm{HP}} = Q_H/W_{\mathrm{in}}$ | Off by exactly $1.00$ ($\mathrm{COP}_{\mathrm{HP}} = \mathrm{COP}_R + 1$). | Ask: *Which reservoir is the conditioned space?* Cooling a fridge ($Q_C$) $\to \mathrm{COP}_R$; warming a house ($Q_H$) $\to \mathrm{COP}_{\mathrm{HP}} = \mathrm{COP}_R + 1 \ge 1$. |
| Rejecting a refrigerator claim because $\mathrm{COP}_R > 1$ (e.g., $\mathrm{COP}_R = 4.2$) | Confuses $\mathrm{COP}$ with engine efficiency $\eta < 1$. | $\mathrm{COP}_R$ and $\mathrm{COP}_{\mathrm{HP}}$ routinely exceed $1$ ($3\text{--}6$); compare against $\mathrm{COP}_{\mathrm{Carnot}} = T_C/(T_H - T_C)$, NOT against $100\%$! |
| Adding efficiencies $\eta_1 + \eta_2$ for two engines in series | Violates energy conservation by double-counting the work extracted by Engine 1. | Engine 2 only receives $(1 - \eta_1)Q_H$, so $\eta_{\mathrm{combined}} = \eta_1 + \eta_2 - \eta_1\eta_2$. |
| Leaving an open refrigerator door in a sealed insulated room to “cool” the room | Actually **heats** the room at rate $\dot{W}_{\mathrm{in}} > 0$! | Taking the whole room as an adiabatic closed system, electrical work $W_{\mathrm{in}}$ enters from the wall outlet: $\Delta U_{\mathrm{room}} = +W_{\mathrm{in}} > 0$. |
| Using Otto efficiency $1 - r^{1-\gamma}$ for a Brayton cycle given pressure ratio $r_p$ | Uses volume ratio exponent $\gamma - 1$ instead of pressure ratio exponent $(\gamma - 1)/\gamma$. | Volume ratio $r = V_1/V_2 \to \eta_{\mathrm{Otto}} = 1 - r^{1-\gamma}$; pressure ratio $r_p = P_2/P_1 \to \eta_{\mathrm{Brayton}} = 1 - r_p^{-(\gamma-1)/\gamma}$. |

### [2027 HEAT-COLLECTOR DEVICE & LAB: First-Law Optical-to-Thermal Collector Efficiency ($\eta_{\mathrm{coll}}$) vs. Carnot Heat-Engine Efficiency]

Never confuse a **heat engine's thermal-to-work efficiency** ($\eta_{\mathrm{engine}} = W/Q_H \le 1 - T_C/T_H$) with the 2027 Heat-Lamp Collector's **First-Law optical-to-thermal capture efficiency** ($\eta_{\mathrm{coll}} \equiv \dot{Q}_{\mathrm{water,net}} / P_{\mathrm{lamp,elec}}$)! Because the 2027 collector converts electrical/radiative lamp power into *internal thermal energy* of the water rather than extracting mechanical work from a low-temperature heat reservoir, $\eta_{\mathrm{coll}}$ is governed by the First Law and view-factor optics (§`sec:15`), NOT by $1 - T_{\mathrm{room}}/T_{\mathrm{water}}$.(Indeed, the radiation source is the $2400 K$ tungsten filament, for which $1 - 300 K/2400 K = 87.5\%$!)

—
**See also:** Quick Sheet `QS-08` (§`sec:01.8`); 8 Named Scientists (§`sec:03`); Master Process Atlas (§`sec:07`); Entropy, Exergy & Steam Tables (§`sec:08`, §`app:A`); Multi-Physics Coupled Problems (§`sec:19`).
