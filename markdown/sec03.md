<!-- Source: src/sec03.tex | Tab: Tab 2: FOUNDATIONS | Target: 8 pp -->
# §3: Thermal Foundations, Zeroth Law, Thermometry Scales, Thermal Expansion & The 8 Named Scientists {#sec:03}

> **[SCOPE: REQUIRED | 2027 Rules 5.c.i, 5.c.v (All Tournament Levels — Minimum 6 Written Questions Combined)]**

### [FORMULA & DECISION CARD: §3 Foundations, 8 Temperature Scales, Thermal Expansion & 8 Scientists Quick Card]

| **Formula** | **Variables (SI units)** | **Flags** | **Use when** |
| --- | --- | --- | --- |
| $\dfrac{T - T_1}{T_2 - T_1} = \dfrac{X - X_1}{X_2 - X_1}$ | $X$: linear thermometric property ($L, P_V, R$); $(X_1,T_1), (X_2,T_2)$: fixed points | **[2027-RULE]** | Universal two-point linear thermometer calibration; gas thermometer $T = 273.16 K(P/P_{\mathrm{tp}})$ **[S13]** |
| $\dfrac{T_C}{100} = \dfrac{T_F - 32}{180} = \dfrac{T_K - 273.15}{100}$ | $T_C$: Celsius; $T_F$: Fahrenheit; $T_K$: Kelvin; Rankine $T_R = 1.8\,T_K = T_F + 459.67$ | **[2027-RULE]** | Primary four-scale conversions; interval rule $\Delta T_K = \Delta T_C = \tfrac{5}{9}\Delta T_F = \tfrac{5}{9}\Delta T_R$ **[S08,S13]** |
| $T_{\mathrm{R\acute{e}}} = 0.8\,T_C;\quad T_{\mathrm{De}} = 150 - 1.5\,T_C$ | $T_{\mathrm{R\acute{e}}}$: R\'eaumur ($0^\circ/80^\circ$); $T_{\mathrm{De}}$: Delisle (**inverted** $150^\circ/0^\circ$); $T_N = 0.33\,T_C$; $T_{\mathrm{Rø}} = 0.525\,T_C + 7.5$ | **[2027-RULE]** | Four historical competition scales (R\'eaumur, Delisle, Newton, Rø mer) **[S25,S26]** |
| $\Delta L = \alpha_L L_0 \Delta T;\quad \Delta A \approx 2\alpha_L A_0 \Delta T$ | $\alpha_L$: linear expansion coeff. $(/K)$; $L_0, A_0$: initial length $(m)$, area $(m^2)$ | **[INCOMP]** | 1D rod/wire/hole/perimeter & 2D isotropic plate/circular aperture expansion **[S13,S14]** |
| $\Delta V = \beta_V V_0 \Delta T \approx 3\alpha_L V_0 \Delta T$ | $\beta_V$: volume expansion coeff. $(/K)$; $\Delta V_{\mathrm{over}} = (\beta_{\mathrm{liq}} - 3\alpha_{\mathrm{ves}})V_0\Delta T$ | **[INCOMP]** | 3D solid/cavity/liquid expansion & apparent liquid overflow from expanding vessel **[S13]** |
| $\sigma = \dfrac{F}{A} = -E\alpha_L\Delta T;\quad R_{\mathrm{curv}} \approx \dfrac{d}{(\alpha_2-\alpha_1)\Delta T}$ | $E$: Young's modulus $(Pa)$; $d$: layer center spacing $(m)$; $\alpha_2 > \alpha_1$ | **[INCOMP]** | Clamped-rod thermal stress & bimetallic strip radius of curvature **[S13,S26]** |

## Intensive vs. Extensive Properties, Equilibrium & The Zeroth Law

### The Duplication Test for Intensive vs. Extensive Properties

Consider combining two identical homogeneous systems, each in equilibrium state $(T, P, V, m, n, U, H, S, \rho, c_p)$, by removing a partition between them  **[S13,S16]**:
- **Extensive Properties (Scale with System Size, $Y \to 2Y$; Additive $Y_{\mathrm{tot}} = \sum Y_i$):** Mass $m$ $(kg)$, amount of substance $n$ $(mol)$, particle count $N$, volume $V$ $(m^3)$, internal energy $U$ $(J)$, enthalpy $H = U + PV$ $(J)$, Helmholtz free energy $F = U - TS$ $(J)$, Gibbs free energy $G = H - TS$ $(J)$, entropy $S$ $(J/K)$, total heat capacity $C = mc = nC_m$ $(J/K)$, and parallel thermal conductance $G_{\mathrm{th}} = 1/R_{\mathrm{th}}$ $(W/K)$.
- **Intensive Properties (Independent of System Size, $y \to y$; Spatially Uniform at Equilibrium):** Temperature $T$ $(K)$, pressure $P$ $(Pa)$, density $\rho = m/V$ $(kg/m^3)$, specific volume $v = V/m = 1/\rho$ $(m^3/kg)$, molar volume $V_m = V/n$ $(m^3/mol)$, specific heat capacity $c = C/m$ $(J/kg/K)$, molar heat capacity $C_m = C/n$ $(J/mol/K)$, specific internal energy $u = U/m$, specific enthalpy $h = H/m$, specific entropy $s = S/m$, chemical potential $\mu_i = (\partial G/\partial n_i)_{T,P,n_{j\neq i}}$ $(J/mol)$, thermal conductivity $k$ $(W/m/K)$, dynamic viscosity $\mu$ $(Pa s)$, emissivity $\varepsilon$, mole fraction $x_i = n_i/n_{\mathrm{tot}}$, and vapor quality $x = m_g/m_{\mathrm{tot}}$.
- **Universal Ratio Identity:** The ratio of *any two extensive properties* of a homogeneous single phase is **always intensive** (e.g., $\rho = m/V$, $M = m/n$, $c = C/m$, $P = \tfrac{2}{3}U_{\mathrm{trans}}/V$). Conversely, the product of an extensive property and an intensive property is extensive ($U = mu$, $H = nH_m$).

### State Functions vs. Path Functions, Equilibrium vs. Steady State & Quasistatic vs. Reversible
- **State Functions vs. Path Functions:** A *state function* ($P, T, V, U, H, S, G, F, \rho$) is an equilibrium property whose change $\Delta X = X_2 - X_1$ depends **only on the endpoints $(1, 2)$** and satisfies $\Delta X_{\mathrm{cycle}} = 0$ around any closed loop. A *path function* (heat $Q$, work $W_{\mathrm{by}}$, entropy generation $S_{\mathrm{gen}}$) describes an energy or entropy transfer *during a process* and depends on the specific path taken between states $1$ and $2$; around a cycle, $Q_{\mathrm{net}} = W_{\mathrm{net,by}} \neq 0$  **[S13,S16]**.
- **Four Pillars of Thermodynamic Equilibrium vs. Steady State:** True thermodynamic equilibrium requires simultaneous (1) *thermal equilibrium* ($\nabla T = 0$, no heat flux), (2) *mechanical equilibrium* ($\nabla P = 0$ except gravity), (3) *phase equilibrium* ($\mu_i^{(\alpha)} = \mu_i^{(\beta)}$ across phases), and (4) *chemical equilibrium* ($\Delta_r G = \sum \nu_i \mu_i = 0$). A metal bar held between a $100 °C$ boiling bath and a $0 °C$ ice bath has a time-independent temperature profile ($\partial T/\partial t = 0$), so it is in **steady state**, NOT thermal equilibrium (it conducts a steady heat rate $\dot{Q} > 0$ and continuously generates entropy $\dot{S}_{\mathrm{gen}} = \dot{Q}(1/T_C - 1/T_H) > 0$)  **[S12,S16]**.
- **Quasistatic vs. Reversible Trap:** A *quasistatic* process proceeds slowly enough ($t_{\mathrm{proc}} \gg t_{\mathrm{relax}}$) that the system passes through a locus of well-defined internal equilibrium states. A *reversible* process is quasistatic **and** free of all dissipative entropy generation ($S_{\mathrm{gen}} = 0$: no friction, no unrestrained expansion, no finite $\Delta T$ heat transfer, no mixing). Every reversible process is quasistatic, but a quasistatic process with friction (e.g., slowly pushing a rough piston) or across a finite temperature difference is **irreversible** ($S_{\mathrm{gen}} > 0$)  **[S13,S16]**.
- **Zeroth Law of Thermodynamics (formulated by R. H. Fowler, 1931):** *If body $A$ is in thermal equilibrium with body $C$, and body $B$ is separately in thermal equilibrium with body $C$, then $A$ and $B$ are in thermal equilibrium with each other* ($T_A = T_C \land T_B = T_C \implies T_A = T_B$)  **[S13]**. This transitive equivalence relation defines **temperature** as the unique intensive property shared by all systems in mutual thermal equilibrium and validates using body $C$ as a **thermometer**.

## Thermometry & Complete Eight-Scale Temperature Conversion System

### Operational Thermometry & Constant-Volume Ideal-Gas Thermometer

Any physical property $X$ that varies monotonically with hotness (mercury/alcohol column length $L$, gas pressure $P$ at fixed volume, platinum RTD resistance $R(T) = R_0(1 + \alpha_R T_C)$, thermocouple Seebeck voltage) defines an empirical temperature scale. Because real materials expand nonlinearly at high/low temperatures, different liquid-in-glass thermometers calibrated at $0 °C$ and $100 °C$ disagree slightly at $50 °C$. However, all low-density gases inside a **constant-volume gas thermometer** converge to the exact same absolute thermodynamic temperature as reference pressure $P_{\mathrm{tp}} \to 0$  **[S13]**:

$$
\begin{aligned}

  T(K) = (273.16 K) \lim_{P_{\mathrm{tp}}\to 0} \frac{P}{P_{\mathrm{tp}}},
\end{aligned}
$$

where $P_{\mathrm{tp}}$ is the gas pressure when the bulb is immersed in a triple-point cell of pure water ($T_{\mathrm{tp}} = 273.16 K = 0.01 °C$, $P_{\mathrm{tp,H_2O}} = 611.657 Pa$).

### Master Conversion Table & Alignment Ladder for All 8 Competition Scales

Science Olympiad written exams regularly test not only the four modern scales ($K, °C, ^\circ\mathrm{F}, ^\circ\mathrm{R}$) but also the four classical historical scales (**R\'eaumur, Delisle, Newton, Rø mer**)  **[S25,S26]**. Every linear scale $S$ with water freezing point $S_{\mathrm{ice}}$ ($0 °C$) and normal boiling point $S_{\mathrm{boil}}$ ($100 °C$) obeys the universal algebraic ratio (Fig. `fig:03:scales`, Table `tab:03:scales`):

$$
\begin{aligned}

  \frac{T_S - S_{\mathrm{ice}}}{S_{\mathrm{boil}} - S_{\mathrm{ice}}} = \frac{T_C}{100} = \frac{T_K - 273.15}{100} = \frac{T_F - 32}{180} = \frac{T_R - 491.67}{180} = \frac{T_{\mathrm{R\acute{e}}}}{80} = \frac{150 - T_{\mathrm{De}}}{150} = \frac{T_N}{33} = \frac{T_{\mathrm{Rø}} - 7.5}{52.5}.
\end{aligned}
$$

**Table:** Complete conversion matrix, fixed points, and interval ratios ($\Delta T_S / \Delta T_C$) for all 8 competition temperature scales  **[S07,S08,S13]**.

| **Scale (Year)** | **Sym.** | **Abs. Zero** | **Ice Pt.** | **Triple Pt.** | **Body** | **Steam Pt.** | **From Celsius ($\boldsymbol{T_C}$)** | **To Celsius ($\boldsymbol{T_C}$)** | $\boldsymbol{\Delta T_S/\Delta T_C}$ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Kelvin** (1848) | $K$ | $0.00$ | $273.15$ | $273.16$ | $310.15$ | $373.15$ | $T_K = T_C + 273.15$ | $T_C = T_K - 273.15$ | $+1.000$ |
| **Celsius** (1742) | $°C$ | $-273.15$ | $0.00$ | $0.01$ | $37.00$ | $100.00$ | $T_C = T_C$ | $T_C = T_C$ | $+1.000$ |
| **Fahrenheit** (1724) | $^\circ\mathrm{F}$ | $-459.67$ | $32.00$ | $32.018$ | $98.60$ | $212.00$ | $T_F = \tfrac{9}{5}T_C + 32$ | $T_C = \tfrac{5}{9}(T_F - 32)$ | $+1.800$ |
| **Rankine** (1859) | $^\circ\mathrm{R}$ | $0.00$ | $491.67$ | $491.688$ | $558.27$ | $671.67$ | $T_R = \tfrac{9}{5}T_K = T_F + 459.67$ | $T_C = \tfrac{5}{9}T_R - 273.15$ | $+1.800$ |
| **R\'eaumur** (1730) | $^\circ\mathrm{R\acute{e}}$ | $-218.52$ | $0.00$ | $0.008$ | $29.60$ | $80.00$ | $T_{\mathrm{R\acute{e}}} = \tfrac{4}{5}T_C = 0.8\,T_C$ | $T_C = \tfrac{5}{4}T_{\mathrm{R\acute{e}}} = 1.25\,T_{\mathrm{R\acute{e}}}$ | $+0.800$ |
| **Delisle** (1732, *inv.*) | $^\circ\mathrm{De}$ | $+559.725$ | $150.00$ | $149.985$ | $94.50$ | $0.00$ | $T_{\mathrm{De}} = \tfrac{3}{2}(100 - T_C)$ | $T_C = 100 - \tfrac{2}{3}T_{\mathrm{De}}$ | $\mathbf{-1.500}$ |
| **Newton** (1701) | $^\circ\mathrm{N}$ | $-90.1395$ | $0.00$ | $0.0033$ | $12.21$ | $33.00$ | $T_N = \tfrac{33}{100}T_C = 0.33\,T_C$ | $T_C = \tfrac{100}{33}T_N$ | $+0.330$ |
| **Rø mer** (1701) | $^\circ\mathrm{Rø}$ | $-135.904$ | $7.50$ | $7.50525$ | $26.925$ | $60.00$ | $T_{\mathrm{Rø}} = \tfrac{21}{40}T_C + 7.5$ | $T_C = \tfrac{40}{21}(T_{\mathrm{Rø}} - 7.5)$ | $+0.525$ |

> **[Vector Figure: Eight-scale thermometric alignment ladder across absolute zero, key dual-scale intersection points ($-40^\circ$ and $+60^\circ$), and standard water fixed points. Note that Delisle ($^\circ\mathrm{De}$) increases *downward* from boiling ($0\,^\circ\mathrm{De}$) to freezing ($150\,^\circ\mathrm{De}$)  **[S08,S13]**. | Label: `fig:03:scales`]**

### [SHORTCUT: Six High-Yield Equal-Reading Crossover Temperatures]
- **Celsius $=$ Fahrenheit:** $x = 1.8x + 32 \implies \mathbf{-40.0\,^\circ\mathrm{C} = -40.0\,^\circ\mathrm{F}}$ ($233.15 K = 419.67\,^\circ\mathrm{R}$).
- **Kelvin $=$ Fahrenheit:** $T_C + 273.15 = 1.8T_C + 32 \implies T_C = 301.4375 °C \implies \mathbf{574.5875 K = 574.5875\,^\circ\mathrm{F}}$.
- **Celsius $=$ Delisle:** $x = 150 - 1.5x \implies 2.5x = 150 \implies \mathbf{+60.0\,^\circ\mathrm{C} = +60.0\,^\circ\mathrm{De}}$ ($333.15 K = 140.0\,^\circ\mathrm{F}$).
- **Fahrenheit $=$ Delisle:** $1.8T_C + 32 = 150 - 1.5T_C \implies T_C = 35.7576 °C \implies \mathbf{+96.3636\,^\circ\mathrm{F} = +96.3636\,^\circ\mathrm{De}}$.
- **Celsius $=$ Rø mer:** $x = 0.525x + 7.5 \implies 0.475x = 7.5 \implies \mathbf{-15.7895\,^\circ\mathrm{C} = -15.7895\,^\circ\mathrm{Rø}}$.
- **Celsius $=$ R\'eaumur $=$ Newton:** $\mathbf{0.0\,^\circ\mathrm{C} = 0.0\,^\circ\mathrm{R\acute{e}} = 0.0\,^\circ\mathrm{N}}$ (all three anchor zero at the ice point!).

## Thermal Expansion of Solids, Liquids & Gases

### Algebraic Binomial Derivations of 1D, 2D, and 3D Expansion

At constant pressure, warming a solid or liquid increases the anharmonic average interatomic spacing  **[S13]**:
- **Linear Expansion (1D rods, wires, perimeters, diameters):** $\Delta L = L - L_0 = \alpha_L L_0 \Delta T \implies L(T) = L_0(1 + \alpha_L\Delta T)$.
- **Superficial / Area Expansion (2D isotropic plates, circular holes, surface shells):** For an isotropic plate of dimensions $L_1 \times L_2$, each edge expands by $(1 + \alpha_L\Delta T)$:
    
$$
A(T) = A_0(1 + \alpha_L\Delta T)^2 = A_0\!\left[1 + 2\alpha_L\Delta T + (\alpha_L\Delta T)^2\right] \approx A_0(1 + 2\alpha_L\Delta T) \implies \boxed{\Delta A \approx 2\alpha_L A_0 \Delta T \quad (\alpha_A = 2\alpha_L)}.
$$
- **Volumetric Expansion (3D blocks, hollow cavities, liquids):** For an isotropic solid $V(T) = V_0(1 + \alpha_L\Delta T)^3$:
    
$$
V(T) = V_0\!\left[1 + 3\alpha_L\Delta T + 3(\alpha_L\Delta T)^2 + (\alpha_L\Delta T)^3\right] \approx V_0(1 + 3\alpha_L\Delta T) \implies \boxed{\Delta V = \beta_V V_0 \Delta T, \quad \beta_{V,\mathrm{isotropic}} \approx 3\alpha_L}.
$$

    For an *anisotropic crystal* with principal linear expansion coefficients $(\alpha_x, \alpha_y, \alpha_z)$, $\beta_V = \alpha_x + \alpha_y + \alpha_z$. For an *ideal gas* at constant pressure ($V = nRT/P$), $\beta_{V,\mathrm{ideal\ gas}} = \dfrac{1}{V}\dfrac{\Delta V}{\Delta T} = \dfrac{1}{T}$ (in kelvin: $\beta_V = 1/293.15 K = 3.411×10^{-3} /K$ at $20 °C$)  **[S13]**.
- **Holes, Annuli & Hollow Cavities (Photographic Enlargement Theorem):** Every linear dimension of a uniform body—including the inner diameter of a washer or the interior volume of a hollow glass flask—expands **at the exact same rate as if the cavity were filled with the solid material itself**: $\Delta D_{\mathrm{hole}} = \alpha_{L,\mathrm{solid}} D_0 \Delta T$ and $\Delta V_{\mathrm{flask}} = 3\alpha_{L,\mathrm{glass}} V_0 \Delta T$  **[S13]**.
- **Apparent Liquid Overflow & Density Variation:** When a vessel of volume $V_0$ and linear coefficient $\alpha_{\mathrm{ves}}$ is filled to the brim with a liquid of volumetric coefficient $\beta_{\mathrm{liq}}$ and heated by $\Delta T$:
    
$$
\begin{aligned}

      \Delta V_{\mathrm{overflow}} = \Delta V_{\mathrm{liq}} - \Delta V_{\mathrm{ves}} = \left(\beta_{\mathrm{liq}} - 3\alpha_{\mathrm{ves}}\right) V_0 \Delta T, \qquad
      \rho(T) = \frac{m}{V(T)} = \frac{\rho_0}{1 + \beta_V\Delta T} \approx \rho_0(1 - \beta_V\Delta T).
\end{aligned}
$$

### Bimetallic Strips, Thermal Stress, Clock/Ruler Errors & Water's $4 °C$ Anomaly
- **Bimetallic Strip Radius of Curvature ($R_{\mathrm{curv}}$):** Two metal strips of thickness $d$ (or center-to-center distance $d$) and expansion coefficients $\alpha_2 > \alpha_1$ are bonded at $T_0$ where both have length $L_0$ (Fig. `fig:03:bimetallic`b). When heated by $\Delta T > 0$, strip 2 stretches more than strip 1, forcing the composite beam to bend into a circular arc of subtended angle $\theta$ (in radians) with strip 2 on the **outer (convex)** arc ($R_{\mathrm{curv}} + d/2$) and strip 1 on the **inner (concave)** arc ($R_{\mathrm{curv}} - d/2$):
    
$$
L_1 = \left(R_{\mathrm{curv}} - \tfrac{d}{2}\right)\theta = L_0(1 + \alpha_1\Delta T), \qquad
      L_2 = \left(R_{\mathrm{curv}} + \tfrac{d}{2}\right)\theta = L_0(1 + \alpha_2\Delta T).
$$

    Subtracting gives $d\,\theta = L_0(\alpha_2 - \alpha_1)\Delta T$, while averaging gives $R_{\mathrm{curv}}\theta = L_0\left[1 + \tfrac{1}{2}(\alpha_1+\alpha_2)\Delta T\right] \approx L_0$. Dividing eliminates $\theta$ and $L_0$ by pure algebra  **[S26]**:
    
$$
\begin{aligned}

      \boxed{R_{\mathrm{curv}} = \frac{d\left[1 + \frac{1}{2}(\alpha_1 + \alpha_2)\Delta T\right]}{(\alpha_2 - \alpha_1)\Delta T} \approx \frac{d}{(\alpha_2 - \alpha_1)\Delta T}} \quad (\text{bends toward lower-}\alpha\text{ metal when heated, }\Delta T > 0).
\end{aligned}
$$
- **Thermal Stress in a Clamped Rod & Buckling:** If a rod of Young's modulus $E$ ($\sigma = E\,\Delta L_{\mathrm{mech}}/L_0$) is held between rigid walls so $\Delta L_{\mathrm{tot}} = \Delta L_{\mathrm{th}} + \Delta L_{\mathrm{mech}} = 0$, heating by $\Delta T$ induces compressive stress $\sigma = F/A = -E\alpha_L\Delta T$  **[S13]**.
- **Metal Scale / Tape-Measure & Pendulum Clock Corrections:** A metal ruler calibrated at $T_0$ has enlarged tick spacing at $T > T_0$, so it *under-reads* true length $L_{\mathrm{true}} = L_{\mathrm{read}}\left[1 + \alpha_{\mathrm{ruler}}(T - T_0)\right]$. A pendulum clock ($P_{\mathrm{pend}} = 2\pi\sqrt{L/g} \propto L^{1/2}$) has fractional period shift $\Delta P_{\mathrm{pend}}/P_{\mathrm{pend}} \approx +\tfrac{1}{2}\alpha_L\Delta T$: it runs **slow** when warm, losing $\Delta t \approx \tfrac{1}{2}\alpha_L\Delta T \times 86400 s /day$.
- **Water's $3.984 °C$ ($\approx4.0 °C$) Density Maximum Anomaly:** Between $0.00 °C$ ($\rho = 999.84 kg/m^3$) and $3.984 °C$ ($\rho_{\max} = 999.97 kg/m^3$), liquid water has a **negative** volumetric expansion coefficient ($\beta_V = -68×10^{-6} /K$ at $0.01 °C$, crossing zero at $3.984 °C$) because open tetrahedral hydrogen-bonded ice-like clusters collapse slightly upon warming (Fig. `fig:03:bimetallic`a)  **[S09,S13]**. In winter, cooling lake surface water sinks until the entire water column reaches $4 °C$; further cooling below $4 °C$ makes the surface water *lighter* ($\beta_V < 0$), so $0–4 °C$ water and $0 °C$ ice ($\rho_{\mathrm{ice}} = 916.7 kg/m^3$) stay stratified at the top, insulating aquatic life at $4 °C$ below!

> **[Vector Figure: (a) Anomalous density maximum of liquid water at $T = 3.984 °C$ ($\rho_{\max} = 999.97 kg/m^3$ at $1 atm$) where $\beta_V$ changes sign from negative to positive  **[S09]**. (b) Bimetallic strip bending toward the lower-expansion metal ($\alpha_1$) upon heating ($\Delta T > 0$) with radius $R_{\mathrm{curv}} \approx d/[(\alpha_2-\alpha_1)\Delta T]$  **[S13,S26]**. | Label: `fig:03:bimetallic`]**
> - **Diagram Annotations & Key Elements:** **Title:** **(a) NIST IAPWS-95 Water Density Maximum at $3.984 °C$** • **X-Axis:** Temperature $T$ ($°C$) • **Y-Axis:** Liquid Water Density $\rho$ ($kg/m^3$) • $\rho_{\max}=999.97 kg/m^3$ ($\beta_V=0$) • $\beta_V < 0$ ($0\text{--}4\,^\circ\mathrm{C}$) • (b) Bimetallic Strip Bending Geometry ($\alpha_2 > \alpha_1$) • Metal 2 ($\alpha_2$ higher, e.g., Brass $19×10^{-6}$) • Metal 1 ($\alpha_1$ lower, e.g., Invar $0.9×10^{-6}$) • At $T_0$ ($\Delta T = 0$): flat, $L_1 = L_2 = L_0$ • Heated ($\Delta T > 0$): outer arc = Metal 2 ($\alpha_2$)

## Historical Perspective of the Exact 8 Named Scientists (`2027 Rule 5.c.v`)

### [2027 OFFICIAL RULE / CLARIFICATION: 2027 Rule 5.c.v Mandatory Historical Syllabus  **[S01]**]

Rule `5.I.c` requires **at least 3 written questions** at every tournament level (Regionals, States, Nationals) from Clause `5.c.v`: *“Historical perspective of contributions of **Kelvin, Joseph Black, Joule, Carnot, Planck, Clausius, Boltzmann, and Maxwell**.”* The timeline (Fig. `fig:03:history`), deep profiles (Table `tab:03:scientists`), and decoy disambiguation matrix (Table `tab:03:historytraps`) cover every competition question pattern on these 8 scientists  **[S23,S25]**.

> **[Vector Figure: Chronological lifespan and discovery timeline of the exact 8 scientists specified in 2027 Rule `5.c.v` (1728–1947)  **[S01,S23]**. | Label: `fig:03:history`]**
> - **Diagram Annotations & Key Elements:** 1754 $\mathrm{CO_2}$; 1761 Latent & Specific Heat • 1840 $I^2R$; 1845–50 Paddle Wheel $J$ • 1850 1st/2nd Law; 1865 Coined *Entropy* $S$ • 1848 Abs. Scale; 1852 $\mu_{\mathrm{JT}}$ • 1860 $f(v)$; 1871 4 Relations & Demon • 1877 $S = k_B\ln\Omega$; 1884 $\sigma T^4$ • 1900 Blackbody $E=h\nu$; 1911 3rd Law $S(0)=0$

**Table:** Authoritative historical reference profiles for the exact 8 scientists in 2027 Rule `5.c.v`  **[S01,S23]**.

| **Scientist (`5.c.v`)** | **Key Experiments, Publications & Years** | **Laws, Equations & Units Named** | **Distinguishing Exam Traps** |
| --- | --- | --- | --- |
| **1. William Thomson (Lord Kelvin)** (1824–1907, Belfast / Glasgow, British) | **1848:** *On an Absolute Thermometric Scale* based on Carnot cycles. **1851:** *On the Dynamical Theory of Heat* reconciling Carnot with Joule. **1852–62:** Porous-plug throttling with Joule. **1854:** Thermoelectric Thomson effect & $\Pi = \alpha T$. | SI unit **kelvin** ($K$); Kelvin–Planck 2nd Law statement; Joule–Thomson $\mu_{\mathrm{JT}} = (\partial T/\partial P)_H$; Kelvin scale $T_C/T_H = Q_C/Q_H$. | Initially defended caloric theory at 1847 BAAS meeting before reconciling Carnot & Joule in 1851. Coined *“Maxwell's demon”* (1874). Title from River Kelvin at Univ. of Glasgow. |
| **2. Joseph Black** (1728–1799, Bordeaux / Glasgow / Edinburgh, Scottish) | **1754:** Isolated $\mathrm{CO_2}$ (*“fixed air”*) gravimetrically from $\mathrm{MgCO_3/CaCO_3}$. **1757–60:** Discovered **specific heat** (mercury vs. water mixing). **1761–62:** Discovered **latent heat** of fusion (ice melting) & vaporization; mentored/funded James Watt's separate condenser (1765). | Latent heat $Q = mL$ (coined *latent heat*, 1761); specific heat & method of mixtures $\sum m_i c_i \Delta T_i = 0$; heat vs. temperature distinction. | Taught discoveries in lectures (published posthumously 1803 by Robison). Do **not** confuse with Lavoisier & Laplace (who built the 1780 *ice calorimeter* using Black's $L_f$). |
| **3. James Prescott Joule** (1818–1889, Salford / Manchester, English) | **1840:** Ohmic heating $P = I^2R$. **1845:** Free expansion of air into vacuum in twin cylinders ($\Delta T = 0 \implies U_{\mathrm{ideal}} = U(T)$). **1845–50:** Falling-weight brass **paddle-wheel calorimeter** in water, mercury & sperm oil ($J = 772.69 ft · lbf/BTU$, $<0.7\%$ from $4.184 J /cal$). | SI energy unit **joule** ($J$); Mechanical equivalent of heat $W = JQ$; Joule's 1st Law $Q = I^2Rt$; Joule's 2nd Law $(\partial U/\partial V)_T = 0$; Joule–Thomson effect. | Distinguish Joule free expansion (closed rigid chambers into vacuum, $\Delta U = 0$) from Joule–Thomson throttling (steady porous-plug flow, $\Delta H = 0$). Mayer proposed conservation in 1842; Joule proved it quantitatively. |
| **4. Nicolas L\'eonard Sadi Carnot** (1796–1832, Paris, French military engineer) | **1824:** Published his sole book *R\'eflexions sur la puissance motrice du feu* (*Reflections on the Motive Power of Fire*) at age 28, introducing the 4-step reversible Carnot cycle (2 isotherms + 2 adiabats) and proving $\eta_{\max}$ depends only on $T_H, T_C$, independent of working fluid. | **Carnot cycle**; **Carnot efficiency** $\eta_C = 1 - T_C/T_H$; **Carnot's theorem**; Carnot $\mathrm{COP}_R = T_C/(T_H-T_C)$ & $\mathrm{COP}_{HP} = T_H/(T_H-T_C)$. | Used caloric waterfall analogy in 1824 ($Q_H = Q_C$), but his unpublished pre-1832 notes rejected caloric and estimated $J \approx 3.7 J /cal$. Clapeyron (1834) first drew Carnot's cycle on a $P$–$V$ diagram. |
| **5. Max Planck** (1858–1947, Kiel / Munich / Berlin, German; 1918 Nobel) | **1879/1897:** PhD & *Treatise on Thermodynamics* (2nd Law engine statement). **Oct/Dec 14, 1900:** Derived **Planck blackbody spectrum** by quantizing oscillator energy $E = h\nu$, resolving the Rayleigh–Jeans UV catastrophe, and evaluated $h$ and $k_B$. **1911:** Absolute Third Law ($S \to 0$ as $T \to 0$ for perfect crystal). | **Planck constant** $h = 6.62607015×10^{-34} J s$; **Planck's radiation law** $M_\lambda(\lambda,T)$; Kelvin–Planck 2nd Law; Planck 3rd Law ($\lim_{T\to 0}S_{\mathrm{cryst}} = 0$). | Planck first wrote Boltzmann's equation explicitly as $S = k\log W$ in Dec 1900 and named $k$ Boltzmann's constant! Walther Nernst discovered the Nernst Heat Theorem ($\Delta S \to 0$) in 1906; Planck set $S(0)=0$ in 1911. |
| **6. Rudolf Clausius** (1822–1888, K\"oslin / Zurich / Bonn, German) | **1850:** *On the Moving Force of Heat*—first joint mathematical formulation of 1st Law ($dQ = dU + P\,dV$) and 2nd Law (refrigerator statement). **1857–58:** Kinetic theory rotational/vibrational modes & **mean free path** $\lambda$. **1865:** Coined **Entropy** ($S$, $dS = \delta Q_{\mathrm{rev}}/T$) and $\oint \delta Q/T \leq 0$. | **Clausius statement** of 2nd Law; **Clausius inequality** $\oint \delta Q/T \leq 0$; macroscopic **entropy** $\Delta S = Q_{\mathrm{rev}}/T$; **Clausius–Clapeyron equation**; Virial theorem (1870). | Famous 1865 couplet: *“1. The energy of the universe is constant. 2. The entropy of the universe tends to a maximum.”* Clausius introduced $\lambda$ with factor $\tfrac{3}{4}$; Maxwell corrected it to $1/\sqrt{2}$ in 1860. |
| **7. Ludwig Boltzmann** (1844–1906, Vienna / Graz, Austrian) | **1868–71:** Generalized Maxwell speeds with **Boltzmann factor** $e^{-E/(k_B T)}$ and proved general equipartition ($\tfrac{1}{2}k_B T$). **1872:** Boltzmann transport equation & $H$-theorem ($dH/dt \leq 0$). **1877:** Statistical mechanics entropy $S = k_B\ln\Omega$. **1884:** Thermodynamic Carnot proof of Stefan's $M_e = \sigma T^4$ using radiation pressure $P = u/3$. | **Boltzmann constant** $k_B = 1.380649×10^{-23} J/K$; **Boltzmann entropy** $S = k\log W$ (on Vienna tombstone); **Stefan–Boltzmann law** $\sigma T^4$; Maxwell–Boltzmann distribution. | Josef Stefan (Boltzmann's PhD advisor) found $M_e \propto T^4$ *empirically* in 1879; Boltzmann proved it *theoretically* in 1884. J. W. Gibbs coined “statistical mechanics” (1902) and defined $G = H - TS$. |
| **8. James Clerk Maxwell** (1831–1879, Edinburgh / London / Cambridge, Scottish) | **1860:** Derived **Maxwell speed distribution** $f(v)$ and predicted dilute gas viscosity $\mu$ is independent of pressure/density (verified experimentally with Katherine Maxwell in 1866). **1867/1871:** *Theory of Heat*—derived the **Four Maxwell Relations** and invented the **Maxwell's Demon** thought experiment. | **Maxwell speed distribution** ($v_{\mathrm{mp}} < v_{\mathrm{avg}} < v_{\mathrm{rms}}$); **Four Maxwell Relations** from $dU, dH, dF, dG$; **Maxwell's Demon**; Maxwell equal-area rule (1875). | Maxwell's Demon proves the Second Law is *statistical* (resolved via Landauer/Szilard information erasure entropy $k_B\ln 2$ per bit). Gas viscosity $\mu \sim \rho \bar{v}\lambda$ is independent of $P$ because $\rho \propto P$ and $\lambda \propto 1/P$ cancel! |

**Table:** High-frequency historical attribution traps: 2027 Rule `5.c.v` scientists vs. related thermodynamic pioneers  **[S23,S25]**.

| **Discovery / Milestone Question Cue** | **Correct Scientist** | **Common Exam Trap / How to Distinguish** |
| --- | --- | --- |
| Coined *latent heat* (1761), discovered specific heat & isolated $\mathrm{CO_2}$ (*fixed air*) | **Joseph Black** (`5.c.v`) | **Lavoisier & Laplace** built the first *ice calorimeter* (1780–83) and coined *calorimeter* using Black's latent heat; Lavoisier named the *caloric* fluid theory (1783). |
| 1798 Munich cannon-boring demonstration that frictional heat is inexhaustible | **Count Rumford** (Benjamin Thompson) | Rumford attacked caloric *qualitatively* via brass cannon boring; **Joule** (`5.c.v`) measured the exact *quantitative* mechanical equivalent $J$ via paddle wheels (1845–50). |
| First philosophical conservation of energy & $C_P - C_V = R$ gas estimate of $J$ (1842) | **Julius Robert von Mayer** | Mayer (1842) published the first conceptual statement and gas-expansion calculation; **Joule** (`5.c.v`) provided the precision experimental proof; **Helmholtz** (1847) formalized potential + kinetic conservation. |
| First drew Carnot's cycle on a $P$–$V$ indicator diagram & derived $dP/dT = L/(T\Delta v)$ (1834) | **\'Emile Clapeyron** | **Carnot** (`5.c.v`, 1824) wrote verbally without $P$–$V$ graphs; Clapeyron (1834) graphed it; **Clausius** (`5.c.v`, 1850) corrected it for energy conservation and derived the ideal-vapor Clausius–Clapeyron form. |
| Empirical discovery of $M_e = \sigma T^4$ (1879) vs. thermodynamic Carnot derivation (1884) | **Josef Stefan** (1879 exp.) vs. **Ludwig Boltzmann** (`5.c.v`, 1884 theory) | Stefan deduced $T^4$ from Tyndall's platinum data (1879); his student **Boltzmann** (`5.c.v`) derived it theoretically from Maxwell's radiation pressure $P = u/3$ in 1884. |
| Wien displacement law $\lambda_{\max}T = b$ (1893) vs. quantum blackbody spectrum $E = h\nu$ (1900) | **Wilhelm Wien** (1893) vs. **Max Planck** (`5.c.v`, 1900) | Wien used classical Doppler/adiabatic cavity compression (1893); **Planck** (`5.c.v`) quantized oscillator energy $E=h\nu$ in 1900 (from which both Wien's $b$ and Stefan's $\sigma$ follow analytically). |
| Nernst Heat Theorem $\Delta S \to 0$ (1906) vs. perfect-crystal $S(0\,K) = 0$ (1911) | **Walther Nernst** (1906) vs. **Max Planck** (`5.c.v`, 1911) | Nernst formulated the Third Law in 1906 (1920 Chemistry Nobel); **Planck** (`5.c.v`) extended it in 1911 to fix the absolute entropy zero $S(0\,K) = 0$ for any pure perfect crystal. |

## Layered Worked Examples & Diagnostics

### Worked Example — Historical Temperature Scale Conversion: Delisle & R\'eaumur to Kelvin `[Basic $\cdot$ Rule 5.c.i]`

In 1735, a Russian meteorological station recorded a winter air temperature of $T_{\mathrm{De}} = 195.0\,^\circ\mathrm{De}$ on a Delisle thermometer, while a French chemist recorded an alcohol bath at $T_{\mathrm{R\acute{e}}} = -24.0\,^\circ\mathrm{R\acute{e}}$. Convert both readings to $°C$, $K$, and $^\circ\mathrm{F}$, and determine which is colder.

**Solution.**
For the Delisle reading ($T_{\mathrm{De}} = 195.0\,^\circ\mathrm{De}$, inverted scale where $150\,^\circ\mathrm{De} = 0 °C$ and $0\,^\circ\mathrm{De} = 100 °C$):

$$
T_{C,1} = 100 - \frac{2}{3}T_{\mathrm{De}} = 100 - \frac{2}{3}(195.0) = 100 - 130.0 = \mathbf{-30.0 °C}, \qquad
  T_{K,1} = -30.0 + 273.15 = \mathbf{243.15 K \approx 243.2 K},
$$

$$
T_{F,1} = \frac{9}{5}(-30.0) + 32 = -54.0 + 32 = \mathbf{-22.0\,^\circ\mathrm{F}}.
$$

For the R\'eaumur reading ($T_{\mathrm{R\acute{e}}} = -24.0\,^\circ\mathrm{R\acute{e}}$, where $80\,^\circ\mathrm{R\acute{e}} = 100 °C$):

$$
T_{C,2} = \frac{5}{4}T_{\mathrm{R\acute{e}}} = 1.25(-24.0) = \mathbf{-30.0 °C}, \qquad
  T_{K,2} = \mathbf{243.15 K}, \qquad T_{F,2} = \mathbf{-22.0\,^\circ\mathrm{F}}.
$$

Both readings represent the **exact same temperature** ($-30.0 °C = 243.15 K = -22.0\,^\circ\mathrm{F}$)!

**✓ Verified by:** Universal ratio check (`eq:03:universalscale`): $(150 - 195.0)/150 = -0.300$ and $-24.0/80 = -0.300 = T_C/100$ (`check_sec02_05.py`).

### Worked Example — Shrink-Fit Interference Assembly of a Brass Ring onto a Steel Shaft `[Competition $\cdot$ Rule 5.c.i]`

At $T_0 = 20.0 °C$, a circular brass collar ($\alpha_{\mathrm{brass}} = 19.0×10^{-6} /°C$) has an inner hole diameter of $D_{\mathrm{brass},0} = 4.990 cm$, while a cylindrical steel shaft ($\alpha_{\mathrm{steel}} = 12.0×10^{-6} /°C$) has an outer diameter of $D_{\mathrm{steel},0} = 5.000 cm$. Find (a) the minimum temperature to which ONLY the brass collar must be heated so it slips over the $20.0 °C$ steel shaft, and (b) the common temperature to which BOTH the brass collar and steel shaft must be heated together so the collar slips onto the shaft.

**Solution.**
**(a)** Heating only the brass collar until $D_{\mathrm{brass}}(T) = D_{\mathrm{brass},0}(1 + \alpha_{\mathrm{brass}}\Delta T) = D_{\mathrm{steel},0} = 5.000 cm$:

$$
\Delta T = \frac{D_{\mathrm{steel},0} - D_{\mathrm{brass},0}}{\alpha_{\mathrm{brass}}\,D_{\mathrm{brass},0}} = \frac{0.010 cm}{(19.0×10^{-6} /°C)(4.990 cm)} = 105.47 °C \implies T = 20.0 + 105.5 = \mathbf{125.5 °C}.
$$

**(b)** Heating both together to $T = T_0 + \Delta T$ requires $D_{\mathrm{brass},0}(1 + \alpha_{\mathrm{brass}}\Delta T) = D_{\mathrm{steel},0}(1 + \alpha_{\mathrm{steel}}\Delta T)$:

$$
\Delta T = \frac{D_{\mathrm{steel},0} - D_{\mathrm{brass},0}}{\alpha_{\mathrm{brass}} D_{\mathrm{brass},0} - \alpha_{\mathrm{steel}} D_{\mathrm{steel},0}} = \frac{0.010}{19.0\times 10^{-6}(4.990) - 12.0\times 10^{-6}(5.000)} = \frac{0.010}{3.481×10^{-5}} = 287.27 °C \implies T = \mathbf{307.3 °C}.
$$

**✓ Verified by:** At $T = 307.27 °C$, $D_{\mathrm{brass}} = 4.990(1 + 19\times 10^{-6}\times 287.274) = 5.01723 cm = D_{\mathrm{steel}}$ (`check_sec02_05.py`).

### Worked Example — Apparent Overflow of Ethanol in a Pyrex Beaker `[Competition $\cdot$ Rule 5.c.i]`

A Pyrex glass beaker ($\alpha_{L,\mathrm{Pyrex}} = 3.0×10^{-6} /°C$) has an interior volume of exactly $V_0 = 500.0 mL$ at $T_1 = 15.0 °C$ and is filled to the brim with liquid ethanol ($\beta_{\mathrm{ethanol}} = 1100×10^{-6} /°C$). When the assembly is warmed uniformly to $T_2 = 45.0 °C$ ($\Delta T = 30.0 °C$), how many milliliters of ethanol overflow?

**Solution.**
The volumetric expansion coefficient of isotropic Pyrex glass is $\beta_{\mathrm{Pyrex}} = 3\alpha_{L,\mathrm{Pyrex}} = 3(3.0×10^{-6} /°C) = 9.0×10^{-6} /°C$. By (`eq:03:overflow`):

$$
\Delta V_{\mathrm{overflow}} = (\beta_{\mathrm{ethanol}} - 3\alpha_{L,\mathrm{Pyrex}}) V_0 \Delta T = (1100 - 9.0)\times 10^{-6}\,/°C \times (500.0 mL)(30.0 °C) = \mathbf{16.365 mL \approx 16.4 mL}.
$$

**✓ Verified by:** $\Delta V_{\mathrm{liq}} = 16.500 mL$ minus $\Delta V_{\mathrm{glass}} = 0.135 mL = 16.365 mL$ (`check_sec02_05.py`).

### Worked Example — Bimetallic Strip Curvature & Tip Deflection (Brass–Invar) `[National $\cdot$ Rule 5.c.i]`

A bimetallic thermostat cantilever of length $L_0 = 8.00 cm$ is fabricated by bonding a $0.50 mm$-thick brass strip ($\alpha_2 = 19.0×10^{-6} /°C$) to a $0.50 mm$-thick Invar strip ($\alpha_1 = 0.90×10^{-6} /°C$) at $20.0 °C$. When heated to $120.0 °C$ ($\Delta T = 100.0 °C$), compute (a) the center-to-center spacing $d$ and radius of curvature $R_{\mathrm{curv}}$, and (b) the transverse tip deflection $\delta_{\mathrm{tip}} \approx L_0^2 / (2R_{\mathrm{curv}})$ using the small-sagitta chord geometry $L_0^2 \approx 2R_{\mathrm{curv}}\delta_{\mathrm{tip}}$.

**Solution.**
**(a)** Center-to-center spacing of two $0.50 mm$ layers is $d = 0.50 mm = 5.00×10^{-4} m$. From (`eq:03:bimetallic`):

$$
R_{\mathrm{curv}} \approx \frac{d}{(\alpha_2 - \alpha_1)\Delta T} = \frac{5.00×10^{-4} m}{(19.0 - 0.90)\times 10^{-6}\,/°C \times 100.0 °C} = \frac{5.00×10^{-4} m}{1.810×10^{-3}} = \mathbf{0.2762 m = 27.6 cm}.
$$

**(b)** By the Pythagorean circle-chord relation $(R_{\mathrm{curv}} - \delta_{\mathrm{tip}})^2 + L_0^2 \approx R_{\mathrm{curv}}^2 \implies \delta_{\mathrm{tip}} \approx \dfrac{L_0^2}{2R_{\mathrm{curv}}}$ (zero trigonometry required!):

$$
\delta_{\mathrm{tip}} \approx \frac{(0.0800 m)^2}{2(0.27624 m)} = \mathbf{0.01158 m = 1.16 cm} \quad (\text{bending toward the Invar side}).
$$

**✓ Verified by:** Exact formula (`eq:03:bimetallic`) gives $R_{\mathrm{curv}} = 0.27652 m$, $\delta_{\mathrm{tip}} = 1.157 cm$ (`check_sec02_05.py`).

### Worked Example — Joule's Falling-Weight Paddle-Wheel Experiment (`Rule 5.c.v`) `[Competition $\cdot$ Rules 5.c.i, 5.c.v]`

In a reproduction of James Prescott Joule's 1845–1850 paddle-wheel calorimeter experiment, two lead masses of $m = 13.20 kg$ each fall through a vertical height of $h = 1.60 m$ a total of $N = 20$ times ($g = 9.80665 m/s^2$), churning $5.50 kg$ of water ($c_w = 4184 J/kg/K$) inside an insulated copper vessel of heat capacity $C_{\mathrm{cal}} = 385 J/K$. Assuming $100\%$ of the mechanical potential energy is dissipated into the water and vessel, calculate the expected temperature rise $\Delta T$ to $0.001 °C$ (explaining why Joule needed custom thermometers readable to $\frac{1}{200}\,^\circ\mathrm{F}$!).

**Solution.**
Total mechanical work delivered by the two falling masses over $N = 20$ drops is:

$$
W_{\mathrm{mech}} = 2 N m g h = 2(20)(13.20 kg)(9.80665 m/s^2)(1.60 m) = \mathbf{8284.66 J}.
$$

Total heat capacity of the water plus copper calorimeter is $C_{\mathrm{tot}} = m_w c_w + C_{\mathrm{cal}} = (5.50)(4184) + 385 = 23012 + 385 = 23397 J/K$. Thus:

$$
\Delta T = \frac{W_{\mathrm{mech}}}{C_{\mathrm{tot}}} = \frac{8284.66 J}{23397 J/K} = \mathbf{0.35409 K \approx 0.354 °C} \quad (\text{or } 0.637\,^\circ\mathrm{F}).
$$

**✓ Verified by:** $W_{\mathrm{mech}} / C_{\mathrm{tot}} = 8284.6579 / 23397.0 = 0.354091 K$ (`check_sec02_05.py`).

### [TRAP & DIAGNOSTIC: §3 Top 5 Foundations, Thermometry & Expansion Traps]

| **Wrong move / Symptom** | **What it produces / Why it fails** | **5-second diagnostic & fix** |
| --- | --- | --- |
| Claiming a hole in a heated metal plate *shrinks* as the metal expands inward | Sign of $\Delta D_{\mathrm{hole}}$ is inverted; a shrink-fit collar would jam instead of slipping on | Photographic enlargement rule: every linear distance (including cavities/holes) expands by $(1 + \alpha_L\Delta T)$. |
| Forgetting that the Delisle scale ($^\circ\mathrm{De}$) is **inverted** ($0\,^\circ\mathrm{De}$ boil, $150\,^\circ\mathrm{De}$ freeze) | Using $+1.5\,T_C$ instead of $150 - 1.5\,T_C$ gives the wrong sign and offset | Check fixed points: higher $^\circ\mathrm{De}$ means **colder** temperature ($\Delta T_{\mathrm{De}} = -1.5\,\Delta T_C$). |
| Confusing thermal expansion $\alpha_L$ ($/K$) with thermal diffusivity $\alpha = k/(\rho c_p)$ ($m^2/s$) | Substitution of $25×10^{-6}$ where $9.6×10^{-5}$ belongs in transient conduction | Always check units: expansion is $/K$; diffusivity is $m^2/s$. |
| Using $\beta_V = 3\alpha_L$ for liquid water between $0 °C$ and $4 °C$ | Predicts water expands upon warming from $0 °C$ to $4 °C$, when it actually **contracts** | Water has $\beta_V < 0$ for $0 °C < T < 3.984 °C$ ($\rho_{\max} = 999.97 kg/m^3$ at $3.984 °C$). |
| Attributing the 1780 ice calorimeter to Joseph Black or the $T^4$ theoretical proof to Stefan | Loses historical matching points under Rule `5.c.v` | Black discovered latent/specific heat (1761); Lavoisier & Laplace built the ice calorimeter (1780). Stefan found $T^4$ empirically (1879); Boltzmann proved it theoretically (1884). |

### [2027 HEAT-COLLECTOR DEVICE & LAB: Thermal Expansion & Softening Limits Inside the 2027 Heat-Lamp Collector]

Under a $100–125 W$ heat lamp at $40 cm$ height, dry upper rim sections of the ES-provided 9 oz clear plastic party cup (`Rule 3.c, 4.g`) can reach $65–80 °C$, while the water-wetted lower wall stays near $T_{\mathrm{water}} \approx 30–48 °C$. Because disposable clear cups are thermoformed from `#1 PET` ($T_g \approx 74 °C$, $\alpha_L \approx 65×10^{-6} /K$) or `#5 PP` ($\alpha_L \approx 100×10^{-6} /K$)—and `#6 PS` is banned under `Clarification #6`—your cup cradle (§`sec:15`) must leave a $\ge1.5 mm$ radial clearance so thermal expansion never binds the cup during the 1-minute extraction window (`Rule 5.II.g`)  **[S01,S02]**.

—
**See also:** §`sec:01.1` (`QS-01` Scales), §`sec:01.2` (`QS-02` Expansion), §`sec:01.14` (`QS-14` 8 Scientists), §`sec:04` (Calorimetry), §`sec:08` (Entropy & 3rd Law), and §`sec:12` (Planck/Stefan–Boltzmann Radiation).
