<!-- Source: src/sec02.tex | Tab: Tab 2: FOUNDATIONS | Target: 6 pp -->
# §2: Notation, SI/Imperial Units, Sign Conventions, Significant Figures & Algebra-Only Math Toolkit {#sec:02}

> **[SCOPE: REQUIRED | 2027 Rules 5.I.b, 5.c.i, 5.d.i–iv (All Tournament Levels — Foundational Sign, Unit & Math Contract)]**

### [FORMULA & DECISION CARD: §2 Master Sign, Unit & Algebra-Only Math Quick Card]

| **Formula** | **Variables (SI units)** | **Flags** | **Use when** |
| --- | --- | --- | --- |
| $\Delta U = Q - W_{\mathrm{by}}$ | $\Delta U$: internal energy change $(J)$; $Q$: heat added **to** system $(J)$; $W_{\mathrm{by}}$: work done **by** system $(J)$ | **[CLOSED]** **[2027-RULE]** | **Primary Binder Convention** (Physics/Engineering) **[S12,S13]** |
| $\Delta U = q + w_{\mathrm{on}}$ | $w_{\mathrm{on}} = -W_{\mathrm{by}}$: work done **on** system $(J)$; $q = Q$: heat added **to** system $(J)$ | **[CLOSED]** | Chemistry / IUPAC convention translation ($w_{\mathrm{on}} = -P_{\mathrm{ext}}\Delta V$) **[S16]** |
| $W_{\mathrm{by}} = P_{\mathrm{ext}}(V_2 - V_1)$ | $P_{\mathrm{ext}}$: constant external pressure $(Pa)$; $V_1, V_2$: initial/final volume $(m^3)$ | **[CLOSED]** | Isobaric boundary work ($1\,Pa m^3 = 1\,J$; $1\,L kPa = 1\,J$) **[S13]** |
| $W_{\mathrm{by}} = \tfrac{1}{2}(P_1 + P_2)(V_2 - V_1)$ | $P_1, P_2$: endpoint pressures $(Pa)$; $V_1, V_2$: endpoint volumes $(m^3)$ | **[CLOSED]** **[REV]** | Straight-line chord on $P$–$V$ plane (trapezoid area under curve, Rule `5.d.iii`) **[S01]** |
| $(1 + \epsilon)^n \approx 1 + n\epsilon$ | $\epsilon$: small dimensionless ratio ($\|\epsilon\| \ll 1$); $n$: real exponent | **[2027-RULE]** | Algebraic binomial linear approximation (thermal expansion $n=2,3,-1,\tfrac{1}{2}$) **[S13]** |
| $y = y_1 + (y_2 - y_1)\dfrac{x - x_1}{x_2 - x_1}$ | $(x_1, y_1), (x_2, y_2)$: adjacent table rows; $x$: target state; $y$: interpolated property | **[2027-RULE]** | Linear table interpolation (steam tables, DOE bulb-height lookup) **[S09,S16]** |

## System Boundaries, Control Volumes & The Locked Sign Contract

Every thermodynamic calculation begins by drawing an explicit **system boundary** (real or imaginary surface) separating the **system** from its **surroundings** (Fig. `fig:02:boundaries`)  **[S12,S13,S16]**. Sign errors and missing energy terms in written exams almost always trace to an unstated or shifting boundary.

> **[Vector Figure: System classification and boundary ledger under the locked Physics sign convention ($\Delta U = Q - W_{\mathrm{by}}$). Choosing a closed vs. open boundary determines whether flow work $Pv$ is tracked separately or bundled into enthalpy $H = U + PV$  **[S12,S13,S16]**. | Label: `fig:02:boundaries`]**
> - **Diagram Annotations & Key Elements:** 1. CLOSED SYSTEM (Control Mass) • Fixed mass $m = \mathrm{const}$ ($\Delta m = 0$) / Impermeable boundary ($\dot{m}=0$) / $\Delta U = Q - W_{\mathrm{by}} = Q + W_{\mathrm{on}}$ • (heat in) • (work out) • Ex: Sealed piston–cylinder, sealed / gas tank, covered non-evaporating cup • 2. OPEN SYSTEM (Control Volume) • Mass crosses boundary ($\dot{m}_{\mathrm{in}}, \dot{m}_{\mathrm{out}} \neq 0$) / Carries enthalpy $h = u + Pv$ / Steady: $\dot{Q} - \dot{W}_s = \dot{m}(h_{\mathrm{out}} - h_{\mathrm{in}})$ • Ex: Uncovered evaporating 9 oz cup, / turbine, compressor, throttling valve • 3. ISOLATED SYSTEM • $\Delta m = 0, \quad Q = 0, \quad W = 0$ / $\Delta U_{\mathrm{iso}} = \sum \Delta U_i = 0$ / $\Delta S_{\mathrm{iso}} = S_{\mathrm{gen}} \geq 0$ • Ex: Ideal sealed calorimeter / (cup + contents), the Universe

### Boundary Constraint Pairs

Every physical wall or interface in a competition problem enforces a mathematical constraint:
- **Adiabatic vs. Diathermal Boundary:** An *adiabatic* wall prevents heat transfer ($Q = 0$ or $\dot{Q} = 0$; realized by vacuum jacketing, thick low-$k$ insulation, or an acoustic/rapid process where $t_{\mathrm{proc}} \ll \tau_{\mathrm{th}}$). A *diathermal* wall conducts heat freely so separated subsystems equilibrate to a shared temperature $T_A = T_B$  **[S13,S16]**.
- **Rigid vs. Movable/Deformable Boundary:** A *rigid* vessel has fixed volume ($\Delta V = 0 \implies W_{\mathrm{by,boundary}} = \int P\,dV = 0$), though shaft/paddle-wheel or electrical work ($W_{\mathrm{elec}} = -VIt$) may still cross the wall. A *freely movable frictionless piston* of mass $m_p$ and area $A_p$ enforces constant internal pressure $P_{\mathrm{gas}} = P_{\mathrm{atm}} + m_p g / A_p$ (isobaric process)  **[S13]**.
- **Impermeable vs. Permeable/Open Boundary:** An uncovered 9 oz cup of warm water under the 2027 heat lamp is an *open system* because water vapor crosses the top free surface ($\dot{m}_{\mathrm{evap}} > 0$), carrying away latent enthalpy $\dot{Q}_{\mathrm{evap}} = \dot{m}_{\mathrm{evap}} L_v$  **[S01,S12]**. Placing an unattached clear BoPET film cap over the rim (`Clarification #5`) converts the cup into a *closed system* ($\dot{m}_{\mathrm{evap}} \approx 0$)  **[S02]**.

### First Law Sign Convention Lock & Physics-to-Chemistry Translation

In physics and mechanical engineering textbooks (OpenStax *University Physics Vol. 2*, Lienhard 6e, MIT 2.005/16.Unified)  **[S12,S13]**, thermodynamic engines are primary, so expansion work done **by** the gas is defined as positive ($W_{\mathrm{by}} > 0$) and subtracted from heat added ($\Delta U = Q - W_{\mathrm{by}}$). In chemistry textbooks (IUPAC, MIT 5.60)  **[S16]**, all energy entering the system is defined as positive, so compression work done **on** the gas is positive ($w_{\mathrm{on}} > 0$) and added to heat ($\Delta U = q + w_{\mathrm{on}}$). Both conventions yield the **exact same physical $\Delta U$** because $W_{\mathrm{on}} = -W_{\mathrm{by}}$ (Table `tab:02:signtrans`).

**Table:** Complete Physics ($\Delta U = Q - W_{\mathrm{by}}$) vs. Chemistry/IUPAC ($\Delta U = Q + W_{\mathrm{on}}$) sign translation across all 11 canonical processes  **[S13,S16]**.

| **Process / Physical Action** | $\boldsymbol{\Delta V}$ | **Heat $\boldsymbol{Q}$** | **Physics $\boldsymbol{W_{\mathrm{by}}}$** | **Chem $\boldsymbol{W_{\mathrm{on}}}$** | **Internal Energy Change $\boldsymbol{\Delta U}$ (Identical in Both!)** |
| --- | --- | --- | --- | --- | --- |
| 1. Isochoric heating (rigid tank) | $0$ | $>0$ | $0$ | $0$ | $\Delta U = +Q = +nC_{V,m}\Delta T > 0$ ($\Delta T > 0$) |
| 2. Isochoric cooling (rigid tank) | $0$ | $<0$ | $0$ | $0$ | $\Delta U = Q = nC_{V,m}\Delta T < 0$ ($\Delta T < 0$) |
| 3. Isobaric expansion ($P=\mathrm{const}$) | $>0$ | $+nC_{P,m}\Delta T > 0$ | $+P\Delta V > 0$ | $-P\Delta V < 0$ | $\Delta U = Q - P\Delta V = +nC_{V,m}\Delta T > 0$ |
| 4. Isobaric compression ($P=\mathrm{const}$) | $<0$ | $nC_{P,m}\Delta T < 0$ | $P\Delta V < 0$ | $-P\Delta V > 0$ | $\Delta U = Q - P\Delta V = nC_{V,m}\Delta T < 0$ |
| 5. Isothermal expansion (ideal gas) | $>0$ | $+nRT\ln(V_2/V_1) > 0$ | $+nRT\ln(V_2/V_1) > 0$ | $-nRT\ln(V_2/V_1) < 0$ | $\Delta U = 0 \implies Q = W_{\mathrm{by}} = -W_{\mathrm{on}} > 0$ |
| 6. Isothermal compression (ideal gas) | $<0$ | $nRT\ln(V_2/V_1) < 0$ | $nRT\ln(V_2/V_1) < 0$ | $-nRT\ln(V_2/V_1) > 0$ | $\Delta U = 0 \implies Q = W_{\mathrm{by}} = -W_{\mathrm{on}} < 0$ |
| 7. Adiabatic expansion ($Q=0$) | $>0$ | $0$ | $+\dfrac{P_1V_1-P_2V_2}{\gamma-1} > 0$ | $-\dfrac{P_1V_1-P_2V_2}{\gamma-1} < 0$ | $\Delta U = -W_{\mathrm{by}} = +W_{\mathrm{on}} < 0$ (gas cools, $\Delta T < 0$) |
| 8. Adiabatic compression ($Q=0$) | $<0$ | $0$ | $\dfrac{P_1V_1-P_2V_2}{\gamma-1} < 0$ | $-\dfrac{P_1V_1-P_2V_2}{\gamma-1} > 0$ | $\Delta U = -W_{\mathrm{by}} = +W_{\mathrm{on}} > 0$ (gas warms, $\Delta T > 0$) |
| 9. Free expansion into vacuum ($P_{\mathrm{ext}}=0$) | $>0$ | $0$ | $0$ | $0$ | $\Delta U = 0$ ($\Delta T = 0$ for ideal gas; $\Delta S = nR\ln(V_2/V_1) > 0$) |
| 10. Clockwise $P$–$V$ cycle (heat engine) | $0_{\mathrm{cyc}}$ | $Q_H - Q_C > 0$ | $+\mathrm{Area} > 0$ | $-\mathrm{Area} < 0$ | $\Delta U_{\mathrm{cycle}} = 0 \implies W_{\mathrm{net,by}} = Q_H - Q_C > 0$ |
| 11. Counterclockwise $P$–$V$ cycle (refrig.) | $0_{\mathrm{cyc}}$ | $Q_C - Q_H < 0$ | $-\mathrm{Area} < 0$ | $+\mathrm{Area} > 0$ | $\Delta U_{\mathrm{cycle}} = 0 \implies W_{\mathrm{in}} = W_{\mathrm{net,on}} = Q_H - Q_C > 0$ |

## Symbol Disambiguation & Dimensional Consistency

Thermodynamics reuses several Latin and Greek letters for unrelated physical quantities with different dimensions. Before substituting numbers into any formula, check the symbol's **subscript and SI unit** (Table `tab:02:symcollision`).

**Table:** High-risk symbol collisions in thermodynamics and heat transfer: how to disambiguate by context and SI units  **[S07,S12,S13]**.

| **Overloaded Letter** | **Distinct Symbols** | **SI Units** | **Physical Meaning & Disambiguation Rule** |
| --- | --- | --- | --- |
| \multirow{3}{*}{$Q,\ \dot{Q},\ q,\ q''$} | $Q$ | $J$ | Total thermal energy transferred across boundary during a finite time interval $\Delta t$ |
|  | $\dot{Q} = Q/t$ | $W = J/s$ | Heat transfer rate (thermal power); integrate/multiply by time $t$ $(s)$ to get $Q$ $(J)$ |
|  | $q = Q/m$ vs. $q'' = \dot{Q}/A$ | $J/kg$ vs. $W/m^2$ | Mass-specific heat transfer $q$ $(J/kg)$ vs. heat flux $q''$ (power per unit area, $W/m^2$) |
| \multirow{3}{*}{$c,\ C,\ C_m$} | $c,\ c_p,\ c_v$ | $J/kg/K$ (or $J/g/K$) | Mass-specific heat capacity (intensive; $1\,J/g/K = 1000 J/kg/K$) |
|  | $C = mc = nC_m$ | $J/K$ | Total heat capacity of an object or calorimeter $C_{\mathrm{cal}}$ (extensive!) |
|  | $C_m = Mc,\ C_{P,m},\ C_{V,m}$ | $J/mol/K$ | Molar heat capacity (intensive; $C_{P,m} - C_{V,m} = R = 8.31446 J/mol/K$ for ideal gas) |
| \multirow{3}{*}{$R,\ R_s,\ R_{\mathrm{th}},\ R_{\mathrm{val}}$} | $R = N_A k_B$ vs. $R_s = R/M$ | $J/mol/K$ vs. $J/kg/K$ | Universal molar gas constant ($8.31446 J/mol/K$) vs. specific gas constant ($R_{\mathrm{air}} = 287.05 J/kg/K$) |
|  | $R_{\mathrm{th}} = \Delta T / \dot{Q}$ | $K/W$ | Lumped thermal resistance ($L/(kA)$ for conduction, $1/(hA)$ for convection) |
|  | $R_{\mathrm{val}} = R'' = L/k$ | $m^2 K/W$ | Unit-area thermal insulance ($R$-value; $R_{\mathrm{th}} = R_{\mathrm{val}}/A$) |
| \multirow{3}{*}{$\alpha_L,\ \alpha_{\mathrm{diff}},\ \alpha_{\mathrm{rad}}$} | $\alpha_L = \frac{1}{L}\frac{\Delta L}{\Delta T}$ | $/K$ (or $/°C$) | Linear coefficient of thermal expansion ($\beta_V \approx 3\alpha_L$ for isotropic solids) |
|  | $\alpha = k/(\rho c_p)$ | $m^2/s$ | Thermal diffusivity (rate of transient thermal penetration; enters Fourier number $\mathrm{Fo} = \alpha t/L_c^2$) |
|  | $\alpha,\ \alpha_\lambda$ | dimensionless $\in [0,1]$ | Hemispherical radiative absorptivity ($\alpha + \rho + \tau = 1$; equals $\varepsilon_\lambda$ at equilibrium) |
| \multirow{2}{*}{$h,\ h_{\mathrm{conv}},\ h_{\mathrm{plank}}$} | $h = u + Pv$ vs. $h_{\mathrm{conv}}$ | $J/kg$ vs. $W/m^2/K$ | Specific enthalpy $h$ ($H/m$) vs. convective heat transfer coefficient $h$ ($\dot{Q} = hA\Delta T$) |
|  | $h$ (Planck) vs. $h_{\mathrm{bulb}}$ | $J s$ vs. $cm$ or $m$ | Planck constant ($6.62607015×10^{-34} J s$) vs. 2027 heat-lamp bulb height ($40–65 cm$) |
| \multirow{2}{*}{$k_B,\ k_{\mathrm{cond}},\ \gamma$} | $k_B$ vs. $k$ | $J/K$ vs. $W/m/K$ | Boltzmann constant ($1.380649×10^{-23} J/K$) vs. thermal conductivity ($\dot{Q} = kA\Delta T/L$) |
|  | $\gamma = C_P/C_V$ | dimensionless $>1$ | Adiabatic index / heat-capacity ratio ($\tfrac{5}{3}$ monatomic, $\tfrac{7}{5}$ diatomic, $\tfrac{4}{3}$ nonlinear polyatomic) |

## SI Base Units, Exact 2019 SI Definitions & Multi-Unit Conversion Matrix

Since May 20, 2019 (9th SI Brochure / NIST CODATA 2022)  **[S07,S08]**, all seven SI base units are defined by fixing exact numerical values of fundamental constants:
- **The Kelvin ($K$):** Defined by fixing the Boltzmann constant to **exactly** $k_B = 1.380649×10^{-23} J/K$ ($kg m^2/s^2/K$). A change of $1 K$ corresponds to a thermal energy scale shift $\Delta(k_B T) = 1.380649×10^{-23} J$. Consequently, the triple point of water ($T_{\mathrm{tp}} = 273.16 K = 0.01 °C$ at $P_{\mathrm{tp}} = 611.657 Pa$) is now an experimentally measured quantity with a relative standard uncertainty of $1.5×10^{-7}$ ($\pm0.0001 K$), whereas the Celsius offset $T(°C) = T(K) - 273.15$ remains exact  **[S07,S08]**.
- **The Mole ($mol$) & Universal Gas Constant ($R$):** Fixing Avogadro's constant to **exactly** $N_A = 6.02214076×10^{23} /mol$ makes the molar gas constant $R = N_A k_B$ an **exact 23-digit decimal**:
  
$$
\begin{aligned}

  \begin{aligned}
    R = N_A k_B &= 8.31446261815324 J/mol/K = 8.314462618 Pa m^3/mol/K = 8.314462618 L kPa/mol/K \\
      &= 0.08314462618 L bar/mol/K = 0.08205736608 L \,atm/mol/K = 62.36359822 L \,Torr/mol/K \\
      &= 1.987204259 cal_{ th }/mol/K = 8.314462618×10^{7} erg/mol/K = 1.985875\ \mathrm{BTU_{IT}/(lbmol\cdot{^\circ R})}.
  \end{aligned}
\end{aligned}
$$

**Table:** Verified NIST CODATA 2022 & NIST SP 811 conversion factors for competition calculations  **[S07,S08]**.

| **Dimension** | **Coherent SI Unit** | **Exact or NIST SP 811 Conversion Factors** |
| --- | --- | --- |
| **Energy / Heat / Work** | $1 J = 1 N m = 1 Pa m^3$ | $1\,\mathrm{cal_{th}} = 4.184 J$ (exact); $1\,\mathrm{cal_{IT}} = 4.1868 J$ (exact); $1\,\mathrm{Cal}$ (dietary) $= 1\,\mathrm{kcal_{th}} = 4184 J$; $1\,\mathrm{BTU_{IT}} = 1055.05585262 J = 251.9958 cal_{IT} = 778.16926 ft · lbf$; $1\,\mathrm{BTU_{th}} = 1054.3503 J$; $1 L \,atm = 101.325 J$ (exact); $1 L bar = 100 J$ (exact); $1 L kPa = 1 J$ (exact); $1 kW h = 3.6×10^{6} J$ (exact); $1\,\mathrm{therm\ (US)} = 10^5\,\mathrm{BTU} = 1.054804×10^{8} J$; $1\,\mathrm{erg} = 10^{-7} J$; $1 eV = 1.602176634×10^{-19} J$ |
| **Power / Heat Rate** | $1 W = 1 J/s$ | $1\,\mathrm{BTU_{IT}/h} = 0.29307107 W$; $1\,\mathrm{BTU_{IT}/s} = 1055.0559 W$; $1\,\mathrm{ton\ of\ refrigeration} = 200\,\mathrm{BTU_{IT}/min} = 12000 BTU_{IT}/h = 3516.8528 W \approx 3.517 kW$; $1\,\mathrm{hp\ (mech)} = 550 ft · lbf/s = 745.69987 W$ |
| **Pressure** | $1 Pa = 1 N/m^2 = 1 J/m^3$ | $1 atm = 101325 Pa = 101.325 kPa = 1.01325 bar = 760\,\mathrm{Torr} = 760 mmHg\ (0\,^\circ\mathrm{C}) = 14.6959488 psi = 29.92126 inHg = 10.33227 mH_2O\ (4\,^\circ\mathrm{C})$; $1 bar = 10^{5} Pa = 100 kPa = 0.98692327 atm = 14.5037738 psi$; $1\,\mathrm{Torr} = \frac{101325}{760}\,Pa = 133.3223684 Pa$; $1\,\mathrm{psi} = 6894.757293 Pa$; $1\,\mathrm{inH_2O}\ (4\,^\circ\mathrm{C}) = 249.0889 Pa$ |
| **Specific Heat Capacity** | $1 J/kg/K = 1 J/kg/°C$ | $1 J/g/K = 1 kJ/kg/K = 1000 J/kg/K$; $1\,\mathrm{cal_{th}/(g\cdot^\circ C)} = 4184 J/kg/K$; $1\,\mathrm{cal_{IT}/(g\cdot^\circ C)} = 1\,\mathrm{BTU_{IT}/(lbm\cdot^\circ F)} = 4186.8 J/kg/K$ (exact) |
| **Latent Heat / Enthalpy** | $1 J/kg$ | $1 kJ/kg = 1 J/g$; $1\,\mathrm{cal_{th}/g} = 4.184 kJ/kg$; $1\,\mathrm{cal_{IT}/g} = 4.1868 kJ/kg$; $1\,\mathrm{BTU_{IT}/lbm} = 2.326 kJ/kg = 2326 J/kg$ (exact) |
| **Thermal Conductivity** | $1 W/m/K$ | $1\,\mathrm{BTU_{IT}/(h\cdot ft\cdot^\circ F)} = 1.730735 W/m/K$; $1\,\mathrm{BTU_{IT}\cdot in/(h\cdot ft^2\cdot^\circ F)} = 0.1442279 W/m/K$; $1\,\mathrm{cal_{th}/(s\cdot cm\cdot^\circ C)} = 418.4 W/m/K$ |
| **Conductance / $R$-Value** | $h, U$: $W/m^2/K$; $R''$: $m^2 K/W$ | $1\,\mathrm{BTU_{IT}/(h\cdot ft^2\cdot^\circ F)} = 5.678263 W/m^2/K$; $1\,\text{R-value (US: }\mathrm{h\cdot ft^2\cdot^\circ F/BTU_{IT}}\text{)} = 0.17611018 m^2 K/W$ (RSI); $1\,\mathrm{RSI} = 5.678263\,\text{R-value (US)}$; $1\,\mathrm{clo} = 0.155 m^2 K/W$ |
| **Viscosity ($\mu$ and $\nu$)** | $\mu$: $Pa s$; $\nu$: $m^2/s$ | $1\,\mathrm{P\ (poise)} = 0.1 Pa s$; $1\,\mathrm{cP} = 1 mPa s = 1000 µPa s$; $1\,\mathrm{St\ (stokes)} = 10^{-4} m^2/s$; $1\,\mathrm{cSt} = 1 mm^2/s = 10^{-6} m^2/s$ |

### STP vs. SATP Molar Volume Disambiguation

Never assume “STP” means $22.4 L/mol$ without checking the pressure standard  **[S07]**:
- **IUPAC / Modern NIST STP ($T = 273.15 K = 0 °C$, $P = 1 bar = 100 kPa$):** $V_m = RT/P = \mathbf{22.71095 L/mol}$ ($n_0 = 2.651646×10^{25} /m^3$).
- **Traditional / US Textbook STP ($T = 273.15 K = 0 °C$, $P = 1 atm = 101.325 kPa$):** $V_m = RT/P = \mathbf{22.41397 L/mol}$ ($n_0 = 2.686780×10^{25} /m^3$).
- **SATP (Standard Ambient $T = 298.15 K = 25 °C$, $P = 1 bar = 100 kPa$):** $V_m = \mathbf{24.78957 L/mol}$ (or $\mathbf{24.46540 L/mol}$ at $25 °C, 1 atm$).

## Science Olympiad Significant Figures & Rounding Policy

Rule `5.I.b` requires all written answers to be reported in **metric units with appropriate significant figures unless otherwise specified**  **[S01,S06]**:
- **Measurement Recording Rule:** Record all certain digits from instrument graduations plus **one (and only one) estimated digit** (typically $\pm 0.1$ of the smallest graduation for analog scales, or the last displayed digit on a digital thermometer)  **[S06]**. Under 2027 Rules `4.f` and `5.II.c,g`, the ES thermometer reads to $\mathbf{0.1 °C}$ (e.g., $21.4 °C$ has 3 sig figs and 1 decimal place)  **[S01]**.
- **Addition & Subtraction (Decimal-Place Rule):** Round the result to the **least precise decimal column** among the terms.
- *Critical Calorimetry & Temperature-Convert Trap:* Converting $T_C = 25.0 °C$ (1 decimal place, 3 sig figs) to kelvin via $T_K = 25.0 + 273.15 = 298.15 K \to \mathbf{298.2 K}$ limits the kelvin value to **1 decimal place (4 sig figs)**. Conversely, subtracting two close thermometer readings $T_f - T_i = 28.4\,°C - 22.7\,°C = \mathbf{5.7 °C}$ preserves 1 decimal place but drops from 3 sig figs to **2 sig figs** (limiting $Q = mc\Delta T$ to 2 sig figs!).
- **Multiplication, Division, Powers & Roots (Sig-Fig Count Rule):** Round the final answer to the **smallest number of significant figures** among any measured factor. Defined exact constants ($k_B, N_A, R, 4.184 J /cal_{th}, 101325 Pa /atm$, stoichiometric integers, $\tfrac{3}{2}, \tfrac{5}{2}$) have **infinite significant figures** and never limit precision  **[S06,S07]**.
- **Logarithms & Exponentials ($\ln x$, $\log_{10} x$, $e^x$):** In $y = \ln x$ or $\log_{10} x$, the number of digits after the decimal point in $y$ (the *mantissa*) equals the number of significant figures in $x$ (e.g., $\ln(2.50) = 0.91629\ldots \to \mathbf{0.916}$ has 3 decimal places because $2.50$ has 3 sig figs). In $x = e^y$ or $10^y$, the number of sig figs in $x$ equals the number of decimal places in $y$  **[S06]**.
- **Guard-Digit Rule:** Never round intermediate values during multi-step calculations! Store full floating-point precision in your Class III calculator memory (`STO`/`ANS`) and round **only the final reported number**  **[S06]**.

## Rule `5.d.i–iv` Algebra-Only & Geometry-Only Math Toolkit

### [2027 OFFICIAL RULE / CLARIFICATION: 2027 Rule 5.d.i–iv & National Physics Math Guidelines  **[S01,S06]**]
- **Permitted Mathematics (`5.d.i–iii`):** Arithmetic (ratios, scientific notation, exponents, roots, absolute values), algebraic manipulations (multi-step and multi-variable symbolic derivations, linear systems, quadratics, logarithms $\ln/\log_{10}$ and exponentials $e^x$ per `MathGuidelines2022.pdf` Division C Algebra II), and geometry (areas and volumes of rectangles, triangles, trapezoids, circles/ellipses, cylinders, spheres, cones, and cubes).
- **Strict Prohibition (`5.d.iv`):** *“No questions may require trigonometry or calculus.”* Every problem on a 2027 compliant exam can be solved without differentiation, integration, or trigonometric functions ($\sin, \cos, \tan$).

### How Calculus-Origin Formulas Reduce to Pure Algebra & Geometry
- **$P$–$V$ Work as Geometric Area (`5.d.iii`):** Instead of evaluating $\int_{V_1}^{V_2} P(V)\,dV$, identify the geometric shape under the path on the $P$–$V$ plane (remembering $1 kPa\times1 L = 1 J$ and $1 MPa\times1 m^3 = 1 MJ$):
- *Isochoric vertical line ($V_2 = V_1$):* Base width is zero $\implies W_{\mathrm{by}} = 0$.
- *Isobaric horizontal line ($P = \mathrm{const}$):* Rectangle of height $P$ and width $(V_2 - V_1) \implies W_{\mathrm{by}} = P(V_2 - V_1)$.
- *Straight-line segment from $(V_1, P_1)$ to $(V_2, P_2)$:* Trapezoid of average height $\bar{P} = \tfrac{1}{2}(P_1 + P_2) \implies W_{\mathrm{by}} = \tfrac{1}{2}(P_1 + P_2)(V_2 - V_1)$.
- *Closed cycle (polygon or ellipse):* Net work per cycle is the **enclosed area** ($+\mathrm{Area}$ if clockwise, $-\mathrm{Area}$ if counterclockwise):
        
$$
\begin{aligned}

          W_{\mathrm{rect}} = \Delta P\,\Delta V, \qquad W_{\mathrm{triangle}} = \tfrac{1}{2}\,\Delta P\,\Delta V, \qquad W_{\mathrm{ellipse/circle}} = \pi a b = \frac{\pi}{4}(P_{\max} - P_{\min})(V_{\max} - V_{\min}).
\end{aligned}
$$
- **Zero-Calculus Proof of Reversible Adiabatic Work:** For an ideal gas, internal energy is a state function that always satisfies $\Delta U = nC_{V,m}(T_2 - T_1) = \frac{nR(T_2 - T_1)}{\gamma - 1} = \frac{P_2V_2 - P_1V_1}{\gamma - 1}$ regardless of path. Setting $Q = 0$ in the First Law $\Delta U = Q - W_{\mathrm{by}}$ immediately yields $W_{\mathrm{by}} = -\Delta U = \dfrac{P_1V_1 - P_2V_2}{\gamma - 1}$ by pure algebra without integrating $PV^\gamma$!
- **Closed-Form Logarithmic Formulas (Direct Calculator `LN` Key):** For reversible isothermal work $W_{\mathrm{by}} = nRT\ln(V_2/V_1)$, constant-$c$ warming entropy $\Delta S = mc\ln(T_2/T_1)$, ideal-gas entropy $\Delta S = nC_{V,m}\ln(T_2/T_1) + nR\ln(V_2/V_1)$, and cylindrical conduction resistance $R_{\mathrm{cyl}} = \frac{\ln(r_o/r_i)}{2\pi k L}$, substitute the dimensionless ratio directly into the $\ln(\cdot)$ key on your Class III calculator.
- **Logarithmic Mean Temperature Difference (LMTD) & Thin-Annulus Approximations:** When $r_o/r_i = 1 + \epsilon$ with $|\epsilon| \ll 1$, the algebraic Padé approximation $\ln\left(\frac{r_o}{r_i}\right) \approx \frac{r_o - r_i}{(r_o + r_i)/2} = \frac{\Delta r}{r_{\mathrm{avg}}}$ reduces cylindrical conduction to a flat slab of mean area $A_{\mathrm{avg}} = 2\pi r_{\mathrm{avg}} L$ to within $<0.1\%$ for $\epsilon < 0.05$.
- **Pythagorean Aspect-Ratio Replacement for Sloped Reflectors (Zero Trigonometry!):** For a truncated conical reflector of top radius $R_1$, bottom radius $R_2$, and vertical height $H$, never use $\sin\theta$ or $\cos\theta$; use the slant length $s = \sqrt{H^2 + (R_1 - R_2)^2}$, lateral surface area $A_{\mathrm{lat}} = \pi(R_1 + R_2)\sqrt{H^2 + (R_1 - R_2)^2}$, and frustum volume $V = \frac{1}{3}\pi H(R_1^2 + R_1 R_2 + R_2^2)$  **[S01]**.

## Layered Worked Examples & Diagnostics

### Worked Example — First Law Sign Translation & Multi-Unit Pressure-Volume Work `[Basic $\cdot$ Rule 5.c.i, 5.c.iv]`

A closed piston–cylinder assembly contains a gas that expands at a constant external pressure of $P = 2.50 atm$ from an initial volume of $V_1 = 1.20 L$ to a final volume of $V_2 = 4.80 L$ while absorbing $Q = 350.0 cal_{th}$ of heat from a heater. Find (a) the boundary work in joules under both the Physics ($W_{\mathrm{by}}$) and Chemistry ($w_{\mathrm{on}}$) conventions, and (b) the internal energy change $\Delta U$ in joules.

**Solution.**
**(a)** Convert heat and pressure–volume units to coherent SI ($J$):

$$
Q = 350.0 cal_{th} \times 4.184 J /cal_{th} = +1464.4 J, \qquad
  P\Delta V = (2.50 atm)(4.80 - 1.20 L) = 9.00 L \,atm.
$$

Using the exact conversion $1 L \,atm = 101.325 J$:

$$
W_{\mathrm{by}} = +P\Delta V = 9.00 \times 101.325 J = \mathbf{+911.925 J \approx +912 J}, \qquad
  w_{\mathrm{on}} = -W_{\mathrm{by}} = \mathbf{-911.925 J \approx -912 J}.
$$

**(b)** Internal energy change is identical under both conventions:

$$
\Delta U = Q - W_{\mathrm{by}} = 1464.4 - 911.925 = \mathbf{+552.475 J \approx +552 J} \quad (\text{or } \Delta U = q + w_{\mathrm{on}} = 1464.4 + (-911.925) = +552.475 J).
$$

**✓ Verified by:** Direct SI conversion: $P = 2.50 \times 101325 Pa = 253312.5 Pa$, $\Delta V = 3.60×10^{-3} m^3 \implies W_{\mathrm{by}} = 911.925 J$, $\Delta U = 552.475 J$ (`check_sec02_05.py`).

### Worked Example — Geometric $P$–$V$ Cycle Area & Significant Figures Trap `[Competition $\cdot$ Rules 5.I.b, 5.d.iii]`

An ideal gas executes a clockwise right-triangular cycle $A \to B \to C \to A$ on a $P$–$V$ diagram with vertices $A(2.00 L, 100.0 kPa)$, $B(8.00 L, 400.0 kPa)$ along a straight chord, $C(8.00 L, 100.0 kPa)$ isochorically, and $C \to A$ isobarically. Compute (a) the work $W_{\mathrm{by}}$ along each leg $A\to B$, $B\to C$, and $C\to A$, and (b) the net work $W_{\mathrm{net}}$ and net heat $Q_{\mathrm{net}}$ over the complete cycle.

**Solution.**
**(a)** Recall $1 kPa\times1 L = 1 J$:
- Leg $A \to B$ (straight-line expansion from $V_A = 2.00 L$ to $V_B = 8.00 L$): Trapezoid area under segment $AB$:
    
$$
W_{A\to B} = \tfrac{1}{2}(P_A + P_B)(V_B - V_A) = \tfrac{1}{2}(100.0 + 400.0 kPa)(8.00 - 2.00 L) = (250.0 kPa)(6.00 L) = \mathbf{+1500 J = +1.50 kJ}.
$$
- Leg $B \to C$ (isochoric cooling at $V = 8.00 L$): $\Delta V = 0 \implies W_{B\to C} = \mathbf{0 J}$.
- Leg $C \to A$ (isobaric compression at $P = 100.0 kPa$ from $8.00 L$ to $2.00 L$): Rectangle area moving left:
    
$$
W_{C\to A} = P_C(V_A - V_C) = (100.0 kPa)(2.00 - 8.00 L) = \mathbf{-600 J = -0.600 kJ}.
$$

**(b)** Over the closed cycle, $\Delta U_{\mathrm{cycle}} = 0$, so $Q_{\mathrm{net}} = W_{\mathrm{net}} = W_{A\to B} + W_{B\to C} + W_{C\to A} = 1500 + 0 - 600 = \mathbf{+900 J = +0.900 kJ}$ (3 sig figs, limited by $\Delta V = 6.00 L$).

**✓ Verified by:** Right-triangle enclosed area formula: $W_{\mathrm{net}} = +\tfrac{1}{2}\Delta V\,\Delta P = \tfrac{1}{2}(6.00 L)(300.0 kPa) = +900.0 J$ (`check_sec02_05.py`).

### Worked Example — Compound Imperial-to-SI Conversion: Refrigeration Tonnage & Thermal Resistance `[Competition $\cdot$ Rule 5.c.i, 5.c.iii]`

A cold-storage room has walls of total area $A = 45.0 m^2$ insulated to a US rating of $\text{R-}19$ ($19.0 h · ft^2 ·^\circ F/BTU_{IT}$). When the outside air is $95.0 ^\circ F$ and the inside room is held at $23.0 ^\circ F$, find (a) the SI unit-area insulance $R_{\mathrm{val}}$ ($m^2 K/W$) and total thermal resistance $R_{\mathrm{th}}$ ($K/W$), and (b) the steady conductive heat leak $\dot{Q}$ in watts and in tons of refrigeration.

**Solution.**
**(a)** From Table `tab:02:conversions`, $1\,\text{R-value (US)} = 0.17611018 m^2 K/W$:

$$
R_{\mathrm{val}} = 19.0 \times 0.17611018 m^2 K/W = \mathbf{3.346 m^2 K/W}, \qquad
  R_{\mathrm{th}} = \frac{R_{\mathrm{val}}}{A} = \frac{3.3461 m^2 K/W}{45.0 m^2} = \mathbf{0.07436 K/W}.
$$

**(b)** Convert the temperature difference using the interval ratio $\Delta T_K = \Delta T_C = \frac{5}{9}\Delta T_F$ (do NOT subtract $32$ from $\Delta T_F$!):

$$
\Delta T_F = 95.0 - 23.0 = 72.0 ^\circ F \implies \Delta T_K = \frac{5}{9}(72.0) = 40.0 K.
$$

The steady heat leak is:

$$
\dot{Q} = \frac{\Delta T_K}{R_{\mathrm{th}}} = \frac{40.0 K}{0.074358 K/W} = \mathbf{537.9 W \approx 538 W}, \qquad
  \dot{Q}_{\mathrm{tons}} = \frac{537.94 W}{3516.85 W /ton} = \mathbf{0.153 tons\ of\ refrigeration}.
$$

**✓ Verified by:** Direct imperial flux calculation: $A = 45.0 m^2 / (0.3048 m /ft)^2 = 484.376 ft^2$, $\dot{Q} = 484.376 \times 72.0 / 19.0 = 1835.53 BTU_{IT}/h = 0.15296 tons = 537.94 W$ (`check_sec02_05.py`).

### Worked Example — Algebraic Binomial & Linear Interpolation Accuracy Check `[National $\cdot$ Rule 5.d.i–ii]`

(a) Use the NIST saturation water table (Table `tab:02:conversions` / App. A) at $T_1 = 30.0 °C$ ($P_{\mathrm{sat},1} = 4.2470 kPa, L_{v,1} = 2429.8 kJ/kg$) and $T_2 = 35.0 °C$ ($P_{\mathrm{sat},2} = 5.6290 kPa, L_{v,2} = 2417.9 kJ/kg$) to linearly interpolate $P_{\mathrm{sat}}$ and $L_v$ at $T = 32.0 °C$. (b) A copper sphere increases in radius by $\epsilon = \Delta R / R_0 = 1.70×10^{-3}$. Compare the exact fractional volume increase $(1+\epsilon)^3 - 1$ against the binomial linear approximation $3\epsilon$.

**Solution.**
**(a)** The interpolation fraction is $f = (32.0 - 30.0)/(35.0 - 30.0) = 2.0/5.0 = 0.400$:

$$
P_{\mathrm{sat}}(32.0 °C) \approx 4.2470 + 0.400(5.6290 - 4.2470) = \mathbf{4.800 kPa}, \qquad
  L_v(32.0 °C) \approx 2429.8 + 0.400(2417.9 - 2429.8) = \mathbf{2425.0 kJ/kg}.
$$

**(b)** For $\epsilon = 1.70×10^{-3}$:

$$
\left(\frac{\Delta V}{V_0}\right)_{\mathrm{linear}} = 3\epsilon = \mathbf{5.1000×10^{-3}}, \qquad
  \left(\frac{\Delta V}{V_0}\right)_{\mathrm{exact}} = (1.00170)^3 - 1 = \mathbf{5.10867×10^{-3}} \quad (\text{relative error } 0.17\%).
$$

**✓ Verified by:** NIST IAPWS-95 exact evaluation at $32.0 °C$ gives $L_v = 2425.1 kJ/kg$ ($0.004\%$ error) and $P_{\mathrm{sat}} = 4.759 kPa$ ($0.85\%$ secant error) (`check_sec02_05.py`).

### [TRAP & DIAGNOSTIC: §2 Top 5 Sign, Unit & Sig-Fig Traps Diagnosis Table]

| **Wrong move / Symptom** | **What it produces / Why it fails** | **5-second diagnostic & fix** |
| --- | --- | --- |
| Using $R = 8.314 J/mol/K$ when $P$ is in $atm$ and $V$ is in $L$ | Off by a factor of $101.325\times$! ($1 L \,atm = 101.325 J$, whereas $1 L kPa = 1 J$) | Either convert $P$ to $kPa$ and $V$ to $L$ (with $R=8.31446$) OR use $R = 0.082057 L \,atm/mol/K$. |
| Using molar mass $M$ in $g/mol$ inside $v_{\mathrm{rms}} = \sqrt{3RT/M}$ or $c_s = \sqrt{\gamma RT/M}$ | Speed is too large by $\sqrt{1000} = 31.62\times$ ($\mathrm{N_2}$ at $300 K$ gives $16340 m/s$ instead of $517 m/s$) | Always convert $M$ to $kg/mol$ ($\mathrm{N_2}: 0.028013 kg/mol$) because $1 J = 1 kg m^2/s^2$. |
| Adding $273.15$ or $32$ when converting a temperature **difference** $\Delta T$ | $\Delta T = 10 °C$ falsely converted to $283.15 K$ or $50 ^\circ F$ | Offset constants cancel in differences: $\Delta T_K = \Delta T_C = \frac{5}{9}\Delta T_F = \frac{5}{4}\Delta T_{\mathrm{R\acute{e}}} = -\frac{2}{3}\Delta T_{\mathrm{De}}$. |
| Mixing Physics $W_{\mathrm{by}}$ and Chemistry $w_{\mathrm{on}}$ in $\Delta U = Q \pm W$ | Sign of work flips, turning $\Delta U = 100 - 40 = 60 J$ into $140 J$ | Ask physically: *Did the gas expand?* Expansion work leaves the gas ($\Delta U$ decreases by $\|W\|$). |
| Using gauge pressure $P_{\mathrm{gauge}}$ instead of $P_{\mathrm{abs}} = P_{\mathrm{gauge}} + P_{\mathrm{atm}}$ in $PV = nRT$ | Fails completely ($P_{\mathrm{gauge}} = 0$ would imply $n=0$ or $T=0$) | Add ambient pressure ($P_{\mathrm{atm}} = 101.325 kPa = 14.696 psi$) before using any gas law or $PV^\gamma$. |

### [2027 HEAT-COLLECTOR DEVICE & LAB: 2027 Heat-Lamp Collector Scoring & Unit Discipline (`Rule 6.a–f`)]

Under 2027 Rule `6.b`, **all Part II device scoring calculations are performed in degrees Celsius ($°C$), NOT kelvin!** Specifically, Temperature Gain is $\mathrm{TG} = T_{\mathrm{final}} - T_{\mathrm{start}}$ (in $°C$) and Prediction Efficiency is:

$$
\mathrm{PE} = \max\!\left(0,\ 1 - \frac{|T_{\mathrm{final}} - T_{\mathrm{pred}}|}{T_{\mathrm{final}}}\right) \quad \text{with } T_{\mathrm{final}} \text{ and } T_{\mathrm{pred}} \text{ in } \mathbf{°C\text{ ( to }0.1 °C\text{)}}  **[S01,S04]**.
$$

Never convert $T_{\mathrm{final}}$ to kelvin inside the denominator of $\mathrm{PE}$, and always submit $T_{\mathrm{pred}}$ in $°C$ rounded to $0.1 °C$ before the end of Heating Time (`Rule 5.II.f`).

—
**See also:** §`sec:00` (Scoring & Router), §`sec:01.1` (`QS-01` Constants & Scales), §`sec:03` (Temperature Scales & 8 Scientists), §`sec:07` (First Law & Work Paths), and §`app:A` (CODATA 2022 Constants Table).
