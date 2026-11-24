<!-- Source: src/sec05.tex | Tab: Tab 3: CAL/PHASE | Target: 10 pp -->
# §5: Phases of Matter, Latent vs. Sensible Heat, Phase Diagrams ($\mathrm{H_2O}, \mathrm{CO_2}$, Binary Eutectic Lever Rule), Clausius–Clapeyron & Psychrometrics {#sec:05}

> **[SCOPE: REQUIRED | Rule 5.c.ii (Phases of Matter, Phase Transitions & Phase Diagrams), 5.c.vi (Enthalpy & Entropy of Phase Change), 5.d.iv (Algebra/Geometry Only)]**

### [FORMULA & DECISION CARD: §5 Core Formula Card — Phase Transitions, Lever Rules, Clausius–Clapeyron & Psychrometrics]

| **Formula** | **Variables (SI units)** | **Flags** | **Use when** |
| --- | --- | --- | --- |
| Latent Heat & Sublimation Cycle | $\displaystyle Q = \pm m L = \pm n \Delta_{\mathrm{trs}}H_m, \qquad \Delta_{\mathrm{sub}}H_m(T) = \Delta_{\mathrm{fus}}H_m(T) + \Delta_{\mathrm{vap}}H_m(T)$ | $J$ (`eq:05:sublimation`) |  |
| Phase-Transition Entropy & Trouton | $\displaystyle \Delta_{\mathrm{trs}}S_m = \frac{\Delta_{\mathrm{trs}}H_m}{T_{\mathrm{trs}}}, \qquad \Delta_{\mathrm{vap}}S_m^\circ = \frac{\Delta_{\mathrm{vap}}H_m^\circ}{T_b} \approx 10.5 R \approx 87 J/mol/K$ | $J/mol/K$ (`eq:05:trouton`) |  |
| Supercooled Adiabatic Freeze Jump | $\displaystyle f_{\mathrm{frozen}} = \frac{m_{\mathrm{ice}}}{m_{\mathrm{tot}}} = \frac{c_w(T_m - T_{\mathrm{sc}})}{L_f}$ | $T_{\mathrm{sc}} < T_m$ (`eq:05:supercool`) |  |
| Gibbs Phase Rule (Full / Isobaric) | $\displaystyle F = C - P + 2 \quad (\text{general } P,T), \qquad F_P = C - P + 1 \quad (P = \text{const})$ | Degrees of freedom (`eq:05:gibbs`) |  |
| Pure-Substance Quality & Lever Rule | $\displaystyle x = \frac{m_g}{m_f + m_g} = \frac{y - y_f}{y_g - y_f}, \qquad y = (1-x)y_f + x y_g = y_f + x y_{fg}$ | $y \in \{v,u,h,s\}$ (`eq:05:quality`) |  |
| Binary Eutectic Tie-Line Lever Rule | $\displaystyle f_L = \frac{w_0 - w_S}{w_L - w_S}, \qquad f_S = \frac{w_L - w_0}{w_L - w_S}, \qquad f_L + f_S = 1$ | Two-phase field (`eq:05:eutecticlever`) |  |
| Exact Clapeyron Slope (`SUPP`) | $\displaystyle \frac{\Delta P}{\Delta T} = \frac{L}{T(v_2 - v_1)} = \frac{\Delta_{\mathrm{trs}}S_m}{\Delta_{\mathrm{trs}}V_m}$ | Coexistence line (`eq:05:clapeyron`) |  |
| Algebraic Clausius–Clapeyron (`SUPP`) | $\displaystyle \ln\!\left(\frac{P_2}{P_1}\right) = -\frac{\Delta_{\mathrm{vap}}H_m}{R}\left(\frac{1}{T_2} - \frac{1}{T_1}\right) \implies T_2 = \left[\frac{1}{T_1} - \frac{R}{\Delta_{\mathrm{vap}}H_m}\ln\!\left(\frac{P_2}{P_1}\right)\right]^{-1}$ | Ideal vapor (`eq:05:cc`) |  |
| Antoine Vapor-Pressure Equation | $\displaystyle \log_{10} P_{\mathrm{sat}} = A - \frac{B}{T + C} \implies P_{\mathrm{sat}} = 10^{\,A - B/(T+C)}$ | NIST WebBook (`eq:05:antoine`) |  |
| Psychrometrics: $\mathrm{RH}$ & Humidity Ratio | $\displaystyle \mathrm{RH} = \frac{P_v}{P_{\mathrm{sat}}(T)}\times 100\%, \qquad \omega = \frac{m_v}{m_a} = 0.62198\,\frac{P_v}{P - P_v}$ | $kg/kg$ (`eq:05:psychro`) |  |
| Colligative Boiling/Freezing Shifts | $\displaystyle P_{\mathrm{soln}} = x_{\mathrm{solv}}P_{\mathrm{solv}}^\circ, \qquad \Delta T_b = +i K_b m, \qquad \Delta T_f = -i K_f m$ | Molality $m$ (`eq:05:colligative`) |  |

## Microscopic States of Matter, All 6 Phase Transitions & Metastable States

The macroscopic phase of a substance is governed by the competition between intermolecular attractive potential energy $|\epsilon_{\mathrm{attr}}|$ and thermal kinetic energy $k_B T$  **[S04,S05]**:
- **Crystalline Solid ($k_B T \ll |\epsilon_{\mathrm{attr}}|$):** Atoms vibrate harmonically about fixed 3D lattice sites (long-range translational and orientational order); definite shape and volume, low compressibility ($\kappa_T \sim 10^{-11}\,/Pa$).
- **Liquid ($k_B T \sim |\epsilon_{\mathrm{attr}}|$):** Molecules remain in close contact (short-range order within $2\text{--}3$ molecular diameters, $\rho_{\mathrm{liq}} \sim \rho_{\mathrm{solid}}$) but translate past one another; definite volume, takes container shape, exhibits a free meniscus and surface tension $\gamma_{\mathrm{surf}}$.
- **Gas / Vapor ($k_B T \gg |\epsilon_{\mathrm{attr}}|$):** Molecules move freely with mean separation $d \gg \sigma_{\mathrm{mol}}$; no fixed shape or volume, expands to fill any container, highly compressible ($\kappa_T \approx 1/P$). (Conventionally called a **vapor** when $T < T_c$ so isothermal compression alone can liquefy it, and a **permanent gas** when $T > T_c$.)
- **Supercritical Fluid ($T > T_c$ and $P > P_c$):** Above the critical point (Table `tab:05:h2oco2`), the liquid–vapor meniscus and latent heat $L_v$ **vanish identically** ($L_v(T_c) = 0$). A gas compressed above $T_c$ and $P_c$ transitions continuously into a dense fluid combining liquid-like solvent density ($\rho \sim 200–800 kg/m^3$) with gas-like diffusivity and zero surface tension (e.g., supercritical $\mathrm{CO_2}$ above $31.0 °C, 7.38 MPa$ used for caffeine extraction).
- **Plasma ($k_B T \gtrsim E_{\mathrm{ion}} \sim 1–10 eV$):** High-temperature quasi-neutral ionized gas of free electrons and positive ions exhibiting collective electromagnetic (Debye-shielded) behavior.

**Table:** Complete thermodynamics of the 6 first-order phase transitions at constant pressure $P$  **[S04,S05,S19]**.

| **Transition** | **Direction** | **$\Delta H = Q_P$** | **$\Delta S$** | **$\Delta G(T_{\mathrm{trs}})$** | **$\mathrm{H_2O}$ Benchmark Values & Physical Notes** |
| --- | --- | --- | --- | --- | --- |
| **1. Melting (Fusion)** | Solid $\to$ Liquid | $+m L_f > 0$ | $+ > 0$ | $0$ | $L_f(0 °C) = 333.55 kJ/kg = 6.009 kJ/mol$; $\Delta V < 0$ for $\mathrm{H_2O}, \mathrm{Bi}, \mathrm{Ga}, \mathrm{Si}$ |
| **2. Freezing (Fusion$^{-1}$)** | Liquid $\to$ Solid | $-m L_f < 0$ | $- < 0$ | $0$ | Exothermic; releases exact latent heat $L_f$ at $T_m$ |
| **3. Vaporization** | Liquid $\to$ Gas | $+m L_v > 0$ | $+ \gg 0$ | $0$ | $L_v(100 °C) = 2256.4 kJ/kg = 40.65 kJ/mol$; $L_v(25 °C) = 2441.7 kJ/kg$ |
| **4. Condensation** | Gas $\to$ Liquid | $-m L_v < 0$ | $- \ll 0$ | $0$ | Exothermic; makes $100 °C$ steam burns far worse than $100 °C$ water |
| **5. Sublimation** | Solid $\to$ Gas | $+m L_{\mathrm{sub}} > 0$ | $+ \gg 0$ | $0$ | $\mathrm{H_2O}(0 °C)$: $L_{\mathrm{sub}} = 2834.8 kJ/kg$; Dry ice $\mathrm{CO_2}(-78.5 °C)$: $571.3 kJ/kg$ |
| **6. Deposition** | Gas $\to$ Solid | $-m L_{\mathrm{sub}} < 0$ | $- \ll 0$ | $0$ | Frost formation at $T < 0 °C$ when $T_{\mathrm{dp}} < 0 °C$ (*frost point*) |
- **Hess's Law Sublimation Identity & Temperature Dependence of Latent Heat:** Because enthalpy $H$ is a state function, subliming a solid to vapor at the triple point (or any temperature $T$ where all three phases are referenced) equals melting plus vaporizing at that same temperature  **[S05,S19]**:
  
$$
\begin{aligned}

    \Delta_{\mathrm{sub}}H_m(T) = \Delta_{\mathrm{fus}}H_m(T) + \Delta_{\mathrm{vap}}H_m(T) \iff L_{\mathrm{sub}}(T) = L_f(T) + L_v(T).
\end{aligned}
$$

  For $\mathrm{H_2O}$ at the triple point $T_{\mathrm{tp}} = 0.01 °C$, $L_f(0.01 °C) = 333.55 kJ/kg$ and $L_v(0.01 °C) = 2501.3 kJ/kg$ sum to $L_{\mathrm{sub}}(0.01 °C) = 2834.8 kJ/kg$ ($51.07 kJ/mol$). Notice that $L_v$ decreases as $T$ rises toward $T_c$ ($\partial L_v/\partial T \approx c_{p,g} - c_{p,\ell} < 0$, Kirchhoff's equation) and vanishes at the critical point: $L_v(0 °C) = 2501.3 kJ/kg \to L_v(25 °C) = 2441.7 kJ/kg \to L_v(100 °C) = 2256.4 kJ/kg \to L_v(373.95 °C) = 0$.
- **Trouton's Rule (1884):** At any reversible phase transition, $\Delta G_{\mathrm{trs}} = \Delta H_{\mathrm{trs}} - T_{\mathrm{trs}}\Delta S_{\mathrm{trs}} = 0$, so:
  
$$
\begin{aligned}

    \Delta_{\mathrm{trs}}S_m = \frac{\Delta_{\mathrm{trs}}H_m}{T_{\mathrm{trs}}}, \qquad
    \Delta_{\mathrm{vap}}S_m^\circ = \frac{\Delta_{\mathrm{vap}}H_m^\circ}{T_b} \approx 10.5 R \approx \mathbf{85–88 J/mol/K} \quad (\text{non-polar liquids}).
\end{aligned}
$$

  Hydrogen-bonded liquids (water: $40650 J/mol/373.15 K = \mathbf{108.9 J/mol/K}$; ethanol: $109.7 J/mol/K$) exceed Trouton's rule because hydrogen bonds make the liquid unusually ordered (abnormally low $S_{\mathrm{liq}}$).
- **Metastable States (Supercooling, Superheating, Supersaturation) & Glass Transition ($T_g$):**
  First-order phase transitions require creating a new interface of surface energy $\gamma_{\mathrm{surf}}$, creating a nucleation barrier $\Delta G^* \propto \gamma_{\mathrm{surf}}^3 / (\Delta T_{\mathrm{undercool}})^2$:
- **Supercooled Liquid:** Ultra-pure dust-free liquid water at $1 atm$ can be cooled below $T_m = 0 °C$ down to the homogeneous nucleation limit $T_H \approx -40 °C$ while remaining liquid. When disturbed by a seed crystal at $T_{\mathrm{sc}} < T_m$, crystallization proceeds adiabatically ($Q = 0$), releasing latent heat that warms the mixture back up to the coexistence plateau $T_m = 0.00 °C$ and freezes the exact mass fraction:
    
$$
\begin{aligned}

      m_{\mathrm{ice}} L_f = m_{\mathrm{tot}} c_w (T_m - T_{\mathrm{sc}}) \implies
      f_{\mathrm{frozen}} = \frac{m_{\mathrm{ice}}}{m_{\mathrm{tot}}} = \frac{c_w(T_m - T_{\mathrm{sc}})}{L_f}.
\end{aligned}
$$

    (Example: liquid water supercooled to $T_{\mathrm{sc}} = -10.0 °C$ freezes a fraction $f_{\mathrm{frozen}} = (4.184)(10.0)/333.55 = \mathbf{12.54\%}$ upon nucleation, leaving $87.46\%$ liquid water at $0.00 °C$!)
- **Superheated Liquid & Bumping:** Smooth glass vessels lacking porous nucleation crevices allow liquid water to exceed $100 °C$ at $1 atm$ before flashing violently into vapor (*bumping*); prevented by porous boiling chips.
- **Amorphous Glass Transition ($T_g$):** If a viscous liquid (silica, glycerol, `#1 PET`) is cooled rapidly enough to bypass crystal nucleation below $T_m$, its viscosity exceeds $e12 Pa s$ at the **glass transition temperature** $T_g$, forming an amorphous solid (glass). Unlike true melting at $T_m$, the glass transition at $T_g$ exhibits **zero latent heat** ($L_f = 0$) and only a step decrease in $c_p$ and $\alpha_L$.
  

## Gibbs Phase Rule & Comparative $P$–$T$ Phase Diagrams ($\mathrm{H_2O}$ vs. $\mathrm{CO_2}$)

In 1876, J. Willard Gibbs proved that a thermodynamic system of $C$ chemically independent components distributed among $P$ coexisting phases in thermal, mechanical, and chemical equilibrium possesses $F$ intensive **degrees of freedom** (independent intensive variables such as $T, P$, or phase mole fractions that can be varied without changing the number of phases $P$)  **[S05,S19]**:

$$
\begin{aligned}

  F = C - P + 2 \qquad (\text{or } F_P = C - P + 1 \text{ when pressure } P \text{ is fixed externally, e.g., at } 1 atm).
\end{aligned}
$$

For a **pure substance ($C = 1$)**, $F = 3 - P$:
- **Single-Phase Area ($P = 1 \implies F = 2$, Bivariant):** Both $T$ and $P$ can be varied independently inside the solid, liquid, or gas region.
- **Two-Phase Coexistence Boundary Curve ($P = 2 \implies F = 1$, Univariant):** Along the fusion (melting), vaporization, or sublimation curve, choosing $T$ fixes $P_{\mathrm{sat}}(T)$ uniquely.
- **Three-Phase Triple Point ($P = 3 \implies F = 0$, Invariant):** Solid, liquid, and vapor coexist in equilibrium at **one unique point** $(T_{\mathrm{tp}}, P_{\mathrm{tp}})$ with zero degrees of freedom.

> **[Vector Figure: Side-by-side $P$–$T$ phase diagrams (not to scale) comparing (a) $\mathrm{H_2O}$, where $\rho_{\mathrm{ice}} < \rho_{\mathrm{liq}}$ gives an anomalous **negative** fusion slope $dP/dT = -133.2 atm/K$ and $P_{\mathrm{tp}} = 0.00604 atm < 1 atm$, against (b) $\mathrm{CO_2}$, where $\rho_{\mathrm{solid}} > \rho_{\mathrm{liq}}$ gives a normal **positive** fusion slope and $P_{\mathrm{tp}} = 5.112 atm > 1 atm$ (so dry ice sublimes directly at $1 atm, -78.46 °C$)  **[S04,S05,S16]**. | Label: `fig:05:h2o-co2-phase`]**
> - **Diagram Annotations & Key Elements:** (a) Water ($\mathrm{H_2O}$): Negative Fusion Slope ($dP/dT < 0$) • $\mathrm{TP}\;(0.01 °C,0.006 atm)$ • $\mathrm{CP}\;(374.0 °C,217.8 atm)$ • $0 °C$ • $100 °C$ • SOLID • (Ice Ih) • LIQUID • VAPOR (GAS) • SCF • (b) Carbon Dioxide ($\mathrm{CO_2}$): Positive Slope & $P_{\mathrm{tp}} > 1 atm$ • $\mathrm{TP}\;(-56.6 °C,5.11 atm)$ • $\mathrm{CP}\;(31.0 °C,72.8 atm)$ • $T_{\mathrm{sub}} = -78.5 °C$ • (Dry Ice)

**Table:** Quantitative side-by-side comparison of $\mathrm{H_2O}$ and $\mathrm{CO_2}$ phase diagram benchmarks  **[S04,S16,S17]**.

| **Phase Diagram Feature** | **Water ($\mathrm{H_2O}$, $M = 18.015 g/mol$)** | **Carbon Dioxide ($\mathrm{CO_2}$, $M = 44.010 g/mol$)** |
| --- | --- | --- |
| **Triple Point $(T_{\mathrm{tp}}, P_{\mathrm{tp}})$** | $T_{\mathrm{tp}} = 273.16 K = \mathbf{0.01 °C}$; $P_{\mathrm{tp}} = \mathbf{611.657 Pa} = 0.006037 atm$ | $T_{\mathrm{tp}} = 216.59 K = \mathbf{-56.56 °C}$; $P_{\mathrm{tp}} = \mathbf{517.96 kPa} = 5.112 atm$ |
| **Critical Point $(T_c, P_c, \rho_c)$** | $T_c = 647.10 K = \mathbf{373.95 °C}$; $P_c = \mathbf{22.064 MPa} = 217.75 atm$; $\rho_c = 322 kg/m^3$ | $T_c = 304.13 K = \mathbf{30.98 °C}$; $P_c = \mathbf{7.377 MPa} = 72.81 atm$; $\rho_c = 467.6 kg/m^3$ |
| **Phase Behavior at $1 atm$ ($101.325 kPa$)** | Since $P_{\mathrm{tp}} < 1 atm < P_c$, liquid water exists over $0.00 °C\text{--}100.00 °C$ | Since $1 atm < P_{\mathrm{tp}} = 5.112 atm$, **liquid $\mathrm{CO_2}$ cannot exist at $1 atm$**; sublimes at $\mathbf{-78.46 °C}$ ($194.69 K$) |
| **Solid vs. Liquid Density** | $\rho_{\mathrm{ice}} = 916.7 kg/m^3 < \rho_{\mathrm{liq}} = 999.84 kg/m^3$ ($\Delta v_{\mathrm{fus}} = \mathbf{-9.05×10^{-5} m^3/kg} < 0$; ice floats!) | $\rho_{\mathrm{solid}} = 1562 kg/m^3 > \rho_{\mathrm{liq}} = 1178 kg/m^3$ at $\mathrm{TP}$ ($\Delta v_{\mathrm{fus}} > 0$; solid $\mathrm{CO_2}$ sinks in liquid $\mathrm{CO_2}$) |
| **Fusion Curve Slope $dP/dT$** | **NEGATIVE:** $dP/dT = \mathbf{-13.50 MPa/K} = -133.2 atm/K$ ($dT_m/dP = -0.00751 K/atm$) | **POSITIVE:** $dP/dT \approx +4.4 MPa/K = +43 atm/K$ (raising $P$ raises $T_m$) |
| **High-Pressure / Regelation Note** | Isothermal compression of Ice Ih at $-1 °C$ above $13.5 MPa$ melts it to liquid (*regelation*). Above $209.9 MPa$ ($-22.0 °C$), Ice Ih converts to dense Ice III ($\rho > \rho_{\mathrm{liq}}$) and $dP/dT$ turns positive. | Fire extinguishers store saturated liquid + vapor $\mathrm{CO_2}$ at $20 °C$, where $P_{\mathrm{sat}}(20 °C) = 5.73 MPa = 56.5 atm$. |

**Table:** Sourced triple points $(T_{\mathrm{tp}}, P_{\mathrm{tp}})$, normal boiling points $T_b$ ($1 atm$), critical points $(T_c, P_c, \rho_c)$, and van der Waals constants $(a,b)$ for 15 common fluids from NIST Chemistry WebBook  **[S16,S17]**.

| **Substance** | **$M$ ($g/mol$)** | **$T_{\mathrm{tp}}$ ($K$)** | **$P_{\mathrm{tp}}$ ($kPa$)** | **$T_b$ ($K$)** | **$T_c$ ($K$)** | **$P_c$ ($MPa$)** | **$\rho_c$ ($kg/m^3$)** | **$a$ ($\mathrm{Pa\,m^6/mol^2}$)** | **$b$ ($e-5 m^3/mol$)** | **Key Phase Note at $1 atm$** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Helium-4 ($\mathrm{He}$) | $4.003$ | $2.177$ | $5.043$ | $4.222$ | $5.195$ | $0.2275$ | $69.6$ | $0.00346$ | $2.380$ | $\lambda$-superfluid transition at $2.177 K$; no solid at $1 atm$ |
| Hydrogen ($\mathrm{H_2}$) | $2.016$ | $13.803$ | $7.042$ | $20.271$ | $33.145$ | $1.296$ | $31.3$ | $0.02476$ | $2.661$ | Inversion $T_{\mathrm{inv}} \approx 202 K$ ($\mu_{\mathrm{JT}} < 0$ at $298 K$) |
| Neon ($\mathrm{Ne}$) | $20.180$ | $24.556$ | $43.38$ | $27.104$ | $44.492$ | $2.679$ | $481.9$ | $0.02135$ | $1.709$ | Monatomic noble gas ($\gamma = 5/3 = 1.667$) |
| Nitrogen ($\mathrm{N_2}$) | $28.013$ | $63.151$ | $12.52$ | $77.355$ | $126.19$ | $3.396$ | $313.3$ | $0.1370$ | $3.870$ | $\mathrm{LN_2}$ boils at $77.36 K = -195.79 °C$, $L_v = 199 kJ/kg$ |
| Carbon Monoxide ($\mathrm{CO}$) | $28.010$ | $68.15$ | $15.37$ | $81.64$ | $132.86$ | $3.494$ | $303.9$ | $0.1505$ | $3.985$ | Residual entropy $S_m(0) \approx R\ln 2 = 5.76 J/mol/K$ |
| Argon ($\mathrm{Ar}$) | $39.948$ | $83.806$ | $68.89$ | $87.302$ | $150.69$ | $4.863$ | $535.6$ | $0.1355$ | $3.201$ | ITS-90 fixed triple point ($83.8058 K$) |
| Oxygen ($\mathrm{O_2}$) | $31.999$ | $54.361$ | $0.1463$ | $90.188$ | $154.58$ | $5.043$ | $436.1$ | $0.1382$ | $3.186$ | Paramagnetic pale-blue liquid ($\mathrm{LOX}$, $L_v = 213 kJ/kg$) |
| Methane ($\mathrm{CH_4}$) | $16.043$ | $90.694$ | $11.70$ | $111.67$ | $190.56$ | $4.599$ | $162.7$ | $0.2283$ | $4.278$ | $\mathrm{LNG}$ carrier fuel ($L_v = 510 kJ/kg$) |
| Carbon Dioxide ($\mathrm{CO_2}$) | $44.010$ | $\mathbf{216.59}$ | $\mathbf{517.96}$ | $194.69^*$ | $304.13$ | $7.377$ | $467.6$ | $0.3640$ | $4.267$ | $*$Sublimes at $1 atm$ ($P_{\mathrm{tp}} = 5.112 atm > 1 atm$) |
| Nitrous Oxide ($\mathrm{N_2O}$) | $44.013$ | $182.33$ | $87.85$ | $184.67$ | $309.52$ | $7.245$ | $452.0$ | $0.3832$ | $4.415$ | Linear triatomic; residual entropy at $0 K$ |
| Ammonia ($\mathrm{NH_3}$) | $17.031$ | $195.48$ | $6.077$ | $239.82$ | $405.40$ | $11.33$ | $225.0$ | $0.4225$ | $3.713$ | Refrigerant R-717 ($T_b = -33.33 °C, L_v = 1371 kJ/kg$) |
| Sulfur Dioxide ($\mathrm{SO_2}$) | $64.064$ | $197.68$ | $1.674$ | $263.13$ | $430.64$ | $7.884$ | $525.0$ | $0.6803$ | $5.636$ | Historic compressor refrigerant |
| Ethanol ($\mathrm{C_2H_5OH}$) | $46.068$ | $159.0$ | $4.3×10^{-7}$ | $351.39$ | $514.71$ | $6.268$ | $276.0$ | $1.218$ | $8.407$ | Normal $T_b = 78.24 °C$, $L_v = 846 kJ/kg$ |
| Water ($\mathrm{H_2O}$) | $18.015$ | $\mathbf{273.16}$ | $\mathbf{0.6117}$ | $373.15$ | $647.10$ | $22.064$ | $322.0$ | $0.5536$ | $3.049$ | Highest $T_c, P_c$ of common hydrides (H-bonding) |
| Mercury ($\mathrm{Hg}$) | $200.59$ | $234.32$ | $1.65×10^{-7}$ | $629.88$ | $1750.0$ | $172.0$ | $5800$ | $0.8200$ | $1.696$ | ITS-90 triple point $-38.8344 °C$ |

## Pure-Substance $P$–$v$ Saturation Dome, Vapor Quality $x$ & Lever Rule

When a pure liquid–vapor mixture coexists inside the **saturation dome** on a pressure–specific volume ($P$–$v$) or temperature–specific volume ($T$–$v$) diagram (Fig. `fig:05:pv-dome`), $T$ and $P = P_{\mathrm{sat}}(T)$ are no longer independent ($F = 1 - 2 + 2 = 1$). To specify the state uniquely inside the wet region, define the **vapor quality (dryness fraction)** $x \in [0,1]$  **[S13,S16]**:

$$
\begin{aligned}

  x = \frac{m_g}{m_f + m_g}, \qquad 1 - x = \frac{m_f}{m_f + m_g},
\end{aligned}
$$

where subscript $f$ (*fluid*) denotes saturated liquid ($x = 0$), subscript $g$ (*gas*) denotes saturated vapor ($x = 1$), and $y_{fg} \equiv y_g - y_f$. Since total volume, internal energy, enthalpy, and entropy are extensive ($Y = m_f y_f + m_g y_g$), dividing by $m_{\mathrm{tot}} = m_f + m_g$ yields the **pure-substance two-phase lever rule**:

$$
\begin{aligned}

  y = (1 - x)y_f + x y_g = y_f + x\,y_{fg} \iff x = \frac{y - y_f}{y_g - y_f} = \frac{y - y_f}{y_{fg}} \qquad \text{for } y \in \{v, u, h, s\}.
\end{aligned}
$$

> **[Vector Figure: Pure-substance $P$–$v$ saturation dome showing the saturated liquid curve ($f, x=0$), saturated vapor curve ($g, x=1$), critical point $(v_c, P_c)$, horizontal isobaric–isothermal tie-line inside the dome, and lever-rule segments $x = (v - v_f)/(v_g - v_f)$  **[S13,S16]**. | Label: `fig:05:pv-dome`]**
> - **Diagram Annotations & Key Elements:** Isotherm $T_1 < T_c$ • Compressed / Liquid • Wet Liquid–Vapor Dome / $x = (v-v_f)/(v_g-v_f)$ • Superheated / Vapor

**Table:** Sourced NIST IAPWS-95 saturation properties of $\mathrm{H_2O}$ from the triple point ($0.01 °C$) to the critical point ($373.95 °C$)  **[S14,S16]**.

| **$T$ ($°C$)** | **$P_{\mathrm{sat}}$ ($kPa$)** | **$v_f$ ($m^3/kg$)** | **$v_g$ ($m^3/kg$)** | **$h_f$ ($kJ/kg$)** | **$h_{fg} = L_v$** | **$h_g$ ($kJ/kg$)** | **$s_f$ ($kJ/kg/K$)** | **$s_g$ ($kJ/kg/K$)** | **$\rho_f$ ($kg/m^3$) / Note** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $0.01$ | $0.6117$ | $0.0010002$ | $205.99$ | $0.00$ | $2500.9$ | $2500.9$ | $0.0000$ | $9.1555$ | $999.84$ (Triple Point) |
| $4.00$ | $0.8135$ | $0.0010000$ | $157.12$ | $16.81$ | $2491.4$ | $2508.2$ | $0.0611$ | $9.0505$ | $999.97$ ($\rho_{\max}$ at $3.984 °C$) |
| $10.00$ | $1.2282$ | $0.0010003$ | $106.30$ | $42.02$ | $2477.2$ | $2519.2$ | $0.1511$ | $8.8998$ | $999.70$ |
| $15.00$ | $1.7057$ | $0.0010009$ | $77.88$ | $62.98$ | $2465.4$ | $2528.3$ | $0.2245$ | $8.7803$ | $999.10$ |
| $20.00$ | $2.3393$ | $0.0010018$ | $57.76$ | $83.91$ | $2453.5$ | $2537.4$ | $0.2965$ | $8.6660$ | $998.21$ |
| $25.00$ | $3.1699$ | $0.0010030$ | $43.34$ | $104.83$ | $2441.7$ | $2546.5$ | $0.3672$ | $8.5567$ | $997.05$ (Standard $298.15 K$) |
| $30.00$ | $4.2470$ | $0.0010044$ | $32.88$ | $125.73$ | $2429.8$ | $2555.5$ | $0.4368$ | $8.4520$ | $995.65$ |
| $40.00$ | $7.3849$ | $0.0010079$ | $19.52$ | $167.53$ | $2406.0$ | $2573.5$ | $0.5724$ | $8.2556$ | $992.22$ |
| $50.00$ | $12.352$ | $0.0010121$ | $12.03$ | $209.34$ | $2382.0$ | $2591.3$ | $0.7038$ | $8.0748$ | $988.03$ |
| $60.00$ | $19.946$ | $0.0010171$ | $7.667$ | $251.18$ | $2357.7$ | $2608.8$ | $0.8313$ | $7.9082$ | $983.20$ |
| $80.00$ | $47.414$ | $0.0010291$ | $3.405$ | $335.01$ | $2308.0$ | $2643.0$ | $1.0756$ | $7.6111$ | $971.79$ |
| $100.00$ | $101.325$ | $0.0010435$ | $1.673$ | $419.06$ | **2256.4** | $2675.5$ | $1.3072$ | $7.3541$ | $958.35$ (Normal $T_b$, $1 atm$) |
| $120.00$ | $198.67$ | $0.0010603$ | $0.8913$ | $503.81$ | $2202.1$ | $2706.0$ | $1.5279$ | $7.1292$ | $943.11$ (Autoclave steam) |
| $150.00$ | $476.16$ | $0.0010905$ | $0.3925$ | $632.18$ | $2113.8$ | $2745.9$ | $1.8418$ | $6.8371$ | $917.01$ |
| $200.00$ | $1554.9$ | $0.0011565$ | $0.1272$ | $852.27$ | $1939.7$ | $2792.0$ | $2.3305$ | $6.4302$ | $864.66$ |
| $373.95$ | $22064.0$ | $0.003106$ | $0.003106$ | $2084.3$ | **0.0** | $2084.3$ | $4.4070$ | $4.4070$ | $322.00$ (Critical Point) |

## Binary Eutectic Alloy Phase Diagrams & Tie-Line Lever Rule (`2027 Cornell E1`)

Modern Division C Invitational and National exams (exemplified by the **2027 Cornell Invitational Section E1** phase-diagram problem  **[S31]**) test two-component ($C = 2$) temperature–composition ($T$ vs. mass fraction $w_B$) **binary eutectic phase diagrams** (Fig. `fig:05:binary-eutectic`) such as $\mathrm{Pb\text{--}Sn}$ solder, $\mathrm{Ag\text{--}Cu}$, or $\mathrm{NaCl\text{--}H_2O}$:

### [DERIVATION: Algebraic Mass-Conservation Proof of the Binary Tie-Line Lever Rule  **[S05,S31]**]

Consider an alloy of overall mass $m_{\mathrm{tot}}$ and overall component-$B$ weight fraction $w_0$ held at a temperature $T$ inside a two-phase coexistence field (such as $\alpha + L$ in Fig. `fig:05:binary-eutectic`). Draw a horizontal **isothermal tie-line** at temperature $T$: its intersection with the solidus curve gives the composition $w_S$ of the solid phase $\alpha$, and its intersection with the liquidus curve gives the composition $w_L$ of the liquid phase $L$. Let $f_S = m_S/m_{\mathrm{tot}}$ and $f_L = m_L/m_{\mathrm{tot}}$ be the mass fractions of solid and liquid phases present. Total mass conservation and component-$B$ mass conservation require:

$$
\begin{aligned}

  f_S + f_L = 1, \qquad w_S f_S + w_L f_L = w_0.
\end{aligned}
$$

Substituting $f_S = 1 - f_L$ into the second equation gives $w_S(1 - f_L) + w_L f_L = w_0 \implies (w_L - w_S)f_L = w_0 - w_S$:

$$
\begin{aligned}

  \mathbf{f_L = \frac{w_0 - w_S}{w_L - w_S} = \frac{\text{opposite arm (to solidus)}}{\text{total tie-line length}}}, \qquad
  \mathbf{f_S = \frac{w_L - w_0}{w_L - w_S} = \frac{\text{opposite arm (to liquidus)}}{\text{total tie-line length}}}.
\end{aligned}
$$

**Fulcrum Rule:** Think of $w_0$ as the fulcrum of a mechanical seesaw balanced between mass $f_S$ at $w_S$ and mass $f_L$ at $w_L$: $(w_0 - w_S)f_S = (w_L - w_0)f_L$. The fraction of either phase is always the **opposite** tie-line segment divided by the total tie-line length $(w_L - w_S)$!

> **[Vector Figure: Binary eutectic phase diagram modeled on the classic $\mathrm{Pb}$–$\mathrm{Sn}$ system ($T_{m,\mathrm{Pb}} = 327.5 °C$, $T_{m,\mathrm{Sn}} = 231.9 °C$, eutectic point $E$ at $w_E = 61.9\,\mathrm{wt\%\ Sn}, T_E = 183.0 °C$ with terminal solid solubility limits $w_{\alpha E} = 18.3\%$ and $w_{\beta E} = 97.8\%$), illustrating an isothermal tie-line $(w_S, w_0, w_L)$ inside the $\alpha + L$ field  **[S05,S31]**. | Label: `fig:05:binary-eutectic`]**
> - **Diagram Annotations & Key Elements:** **X-Axis:** Composition: Weight Percentage of Component $B$ ($\mathrm{Sn}$ in $\mathrm{Pb}$–$\mathrm{Sn}$), $w_B$ ($\mathrm{wt\%}$) • **Y-Axis:** Temperature $T$ ($°C$) • Eutectic $E\;(61.9\%, 183 °C)$ • Liquid ($L$) [$F_P = 2$] • $\alpha$ • $\alpha + L$ [$F_P = 1$] • $\beta + L$ • Two-Solid Field: $\alpha + \beta$ [$F_P = 1$]
- **Four Key Binary Eutectic Exam Rules (`2027 Cornell E1` Checklist):**
- **Liquidus vs. Solidus:** Above the **liquidus** curve, the alloy is $100\%$ homogeneous liquid $L$. Below the **solidus** line (and eutectic horizontal $T_E$), the alloy is $100\%$ solid ($\alpha$, $\beta$, or $\alpha + \beta$). Between the liquidus and solidus lies a **two-phase mushy zone** ($\alpha + L$ or $\beta + L$) where melting/freezing occurs over a temperature range rather than at a single temperature.
- **Invariant Eutectic Point $(w_E, T_E)$:** At constant atmospheric pressure ($F_P = C - P + 1$), the three-phase eutectic reaction $L(w_E) \rightleftharpoons \alpha(w_{\alpha E}) + \beta(w_{\beta E})$ has $C = 2, P = 3 \implies \mathbf{F_P = 0}$ (invariant isothermal arrest at $T_E$). An alloy of exact eutectic composition $w_0 = w_E$ melts and freezes **isothermally at $T_E$ like a pure element**, at a temperature lower than either pure component ($T_E < \min(T_{m,A}, T_{m,B})$).
- **Hypoeutectic ($w_{\alpha E} < w_0 < w_E$) vs. Hypereutectic ($w_E < w_0 < w_{\beta E}$) Cooling:** As a hypoeutectic liquid ($w_0 < w_E$) cools across the liquidus, **primary (proeutectic) $\alpha$ crystals** precipitate first while the remaining liquid enriches in $B$ along the liquidus curve until reaching $(w_E, T_E)$ at $T = T_E^+$, where the remaining liquid fraction $f_{\mathrm{eutectic}} = f_L(T_E^+) = \dfrac{w_0 - w_{\alpha E}}{w_E - w_{\alpha E}}$ freezes into fine alternating **eutectic $(\alpha + \beta)$ lamellae**.
- **Total Phase Fractions vs. Microconstituent Fractions Just Below $T_E$ ($T = T_E^-$):**
    
$$
\begin{aligned}

      f_{\alpha,\mathrm{total}}(T_E^-) = \frac{w_{\beta E} - w_0}{w_{\beta E} - w_{\alpha E}}, \qquad
      f_{\text{primary }\alpha}(T_E^+) = \frac{w_E - w_0}{w_E - w_{\alpha E}}, \qquad
      f_{\text{eutectic microconstituent}}(T_E^+) = \frac{w_0 - w_{\alpha E}}{w_E - w_{\alpha E}}.
\end{aligned}
$$

  

## Vapor Pressure, Psychrometrics, Colligative Shifts & Clausius–Clapeyron

- **Evaporation vs. Boiling & NIST Antoine Equation:**
  **Evaporation** is a surface phenomenon occurring at *any* temperature whenever the ambient partial pressure of water vapor $P_v$ is less than the equilibrium saturation vapor pressure $P_{\mathrm{sat}}(T)$ ($P_v < P_{\mathrm{sat}}(T)$); high-energy molecules in the Maxwell–Boltzmann tail escape the surface, cooling the remaining liquid. **Boiling** is a bulk phenomenon occurring when $P_{\mathrm{sat}}(T)$ equals or exceeds the external ambient pressure ($P_{\mathrm{sat}}(T_b) = P_{\mathrm{ext}}$), allowing vapor bubbles to nucleate and grow throughout the liquid volume (at high altitude where $P_{\mathrm{ext}} < 101.325 kPa$, $T_b < 100 °C$; inside a pressure cooker where $P_{\mathrm{ext}} \approx 2 atm$, $T_b \approx 120 °C$). NIST Chemistry WebBook parameterizes $P_{\mathrm{sat}}(T)$ ($bar$, $T$ in $K$) via the **Antoine equation**  **[S16]**:
  
$$
\begin{aligned}

    \log_{10}\!\left(\frac{P_{\mathrm{sat}}}{bar}\right) = A - \frac{B}{T + C}
    \quad\text{where } (A,B,C) = \begin{cases}
      (5.40221,\; 1838.675,\; -31.737) & 273 K \le T \le 303 K, \\
      (5.20389,\; 1733.926,\; -39.485) & 304 K \le T \le 333 K, \\
      (5.07680,\; 1659.793,\; -45.854) & 334 K \le T \le 363 K, \\
      (5.08354,\; 1663.125,\; -45.622) & 344 K \le T \le 373 K.
    \end{cases}
\end{aligned}
$$
- **Psychrometrics — Relative Humidity ($\mathrm{RH}$), Humidity Ratio ($\omega$), Dew Point ($T_{\mathrm{dp}}$) & Wet-Bulb ($T_{\mathrm{wb}}$):**
  Moist air at total barometric pressure $P$ is a Dalton ideal-gas mixture of dry air ($M_a = 28.965 g/mol$, partial pressure $P_a = P - P_v$) and water vapor ($M_v = 18.015 g/mol$, partial pressure $P_v$):
  
$$
\begin{aligned}

    \mathrm{RH} = \frac{P_v}{P_{\mathrm{sat}}(T)} \times 100\%, \qquad
    \omega = \frac{m_v}{m_a} = \frac{M_v}{M_a}\frac{P_v}{P - P_v} = \mathbf{0.62198\,\frac{P_v}{P - P_v}} \;\;\left[kg/kg\;(\mathrm{kg\,H_2O/kg\,dry\,air})\right].
\end{aligned}
$$
- **Dew Point ($T_{\mathrm{dp}}$):** The temperature to which moist air must be cooled at constant pressure $P$ (and constant $P_v$) for condensation to begin: $P_{\mathrm{sat}}(T_{\mathrm{dp}}) = P_v$.
- **Wet-Bulb Temperature ($T_{\mathrm{wb}}$):** The steady dynamic equilibrium temperature reached by a water-wetted thermometer bulb cooled by evaporation into moving air. Always satisfies $\mathbf{T_{\mathrm{dp}} \leq T_{\mathrm{wb}} \leq T_{\mathrm{dry\text{-}bulb}}}$, with equality $T_{\mathrm{dp}} = T_{\mathrm{wb}} = T_{\mathrm{db}}$ **if and only if** $\mathrm{RH} = 100\%$.
- **Colligative Phase Shifts (Raoult's Law, $\Delta T_b$, $\Delta T_f$):**
  Adding a non-volatile solute of molality $m$ ($mol solute/kg·solvent$) and van 't Hoff dissociation factor $i$ (e.g., $i=1$ for sucrose/urea/glycol, $i=2$ for $\mathrm{NaCl}$, $i=3$ for $\mathrm{CaCl_2}$) lowers solvent vapor pressure by Raoult's law ($P_{\mathrm{soln}} = x_{\mathrm{solv}}P_{\mathrm{solv}}^\circ$), which elevates the boiling point and depresses the freezing point  **[S05,S19]**:
  
$$
\begin{aligned}

    \Delta T_b = T_{b,\mathrm{soln}} - T_b^\circ = +i K_b m, \qquad
    \Delta T_f = T_{f,\mathrm{soln}} - T_f^\circ = -i K_f m,
\end{aligned}
$$

  where for water $K_b = \dfrac{R M_{\mathrm{H_2O}}(T_b^\circ)^2}{\Delta_{\mathrm{vap}}H_m^\circ} = \mathbf{0.512 K · kg/mol}$ and $K_f = \dfrac{R M_{\mathrm{H_2O}}(T_f^\circ)^2}{\Delta_{\mathrm{fus}}H_m^\circ} = \mathbf{1.853 K · kg/mol}$ (often rounded to $1.86 K · kg/mol$).

### [SUPPLEMENTARY: Exact Clapeyron & Algebraic Two-Point Clausius–Clapeyron Equations  **[S05,S19]**]

**`[SUPPLEMENTARY — ALGEBRAIC FORM, ZERO CALCULUS REQUIRED TO APPLY]`**\\
Equating the molar Gibbs free energies $G_{m,1}(T,P) = G_{m,2}(T,P)$ along any two-phase coexistence boundary yields the **exact Clapeyron equation** (valid for solid–liquid, liquid–vapor, and solid–vapor boundaries):

$$
\begin{aligned}

  \frac{\Delta P}{\Delta T} = \frac{\Delta_{\mathrm{trs}}S_m}{\Delta_{\mathrm{trs}}V_m} = \frac{\Delta_{\mathrm{trs}}H_m}{T\,\Delta_{\mathrm{trs}}V_m} = \frac{L}{T(v_2 - v_1)}.
\end{aligned}
$$

For vaporization or sublimation far below the critical point, $v_g \gg v_{\mathrm{cond}}$ so $\Delta_{\mathrm{vap}}V_m \approx V_{m,g} = RT/P$, which yields the **algebraic two-point Clausius–Clapeyron equation** (assuming constant $\Delta_{\mathrm{vap}}H_m$ over $[T_1, T_2]$):

$$
\begin{aligned}

  \ln\!\left(\frac{P_2}{P_1}\right) = -\frac{\Delta_{\mathrm{vap}}H_m}{R}\left(\frac{1}{T_2} - \frac{1}{T_1}\right) = \frac{\Delta_{\mathrm{vap}}H_m}{R}\left(\frac{T_2 - T_1}{T_1 T_2}\right).
\end{aligned}
$$

**Unit Warning:** In (`eq:05:cc`), $T_1, T_2$ **must be in kelvin ($K$)**, and $\Delta_{\mathrm{vap}}H_m$ ($J/mol$) must match $R = 8.31446 J/mol/K$ (convert $kJ/mol$ to $J/mol$ by multiplying by $1000$!).

## Layered Worked Examples & Diagnostics

### Worked Example — Pressure Melting (Regelation) of Ice Under High Compression `[Competition $\cdot$ Rule 5.c.ii]`

At $T_0 = 273.15 K$ ($0.00 °C$) and $1.00 atm$, ice has specific volume $v_{\mathrm{ice}} = 1.0908×10^{-3} m^3/kg$, liquid water has $v_w = 1.00016×10^{-3} m^3/kg$, and $L_f = 333.55 kJ/kg$. Using the exact Clapeyron equation (`eq:05:clapeyron`), compute (a) the slope $\Delta P/\Delta T$ of water's fusion line in $MPa/K$ and $atm/K$, and (b) the melting point of ice under an overburden pressure of $P = 150.0 atm$ ($15.20 MPa$).

**Solution.**
**(a)** The volume change upon melting is $\Delta v_{\mathrm{fus}} = v_w - v_{\mathrm{ice}} = (1.00016 - 1.0908)\times 10^{-3} = \mathbf{-9.064×10^{-5} m^3/kg} < 0$. By (`eq:05:clapeyron`):

$$
\frac{\Delta P}{\Delta T} = \frac{L_f}{T_0(v_w - v_{\mathrm{ice}})} = \frac{333550 J/kg}{(273.15 K)(-9.064×10^{-5} m^3/kg)} = \mathbf{-13.47 MPa/K = -133.0 atm/K}.
$$

**(b)** Inverting the slope gives $\Delta T_m / \Delta P = -0.007521 K/atm$. For $\Delta P = 150.0 - 1.0 = 149.0 atm$:

$$
\Delta T_m = (149.0 atm)(-0.007521 K/atm) = -1.121 K \implies T_m = \mathbf{-1.12 °C\;(272.03 K)}.
$$

**✓ Verified by:** Exact Clapeyron evaluation matches NIST IAPWS Ice Ih melting curve to $<0.3\%$ (`check_sec02_05.py`).

### Worked Example — Two-Phase Saturation Dome Quality $x$, Enthalpy & Volume `[Competition $\cdot$ Rules 5.c.ii, 5.c.vi]`

A rigid $0.500 m^3$ pressure vessel contains $m_{\mathrm{tot}} = 2.000 kg$ of a two-phase liquid–vapor water mixture in equilibrium at $T = 120.0 °C$ (Table `tab:05:steamtables`: $P_{\mathrm{sat}} = 198.67 kPa$, $v_f = 0.0010603 m^3/kg$, $v_g = 0.8913 m^3/kg$, $h_f = 503.81 kJ/kg$, $h_{fg} = 2202.1 kJ/kg$). Calculate (a) the mixture specific volume $v$ and vapor quality $x$, (b) the masses of saturated vapor $m_g$ and saturated liquid $m_f$, and (c) the total enthalpy $H$ of the vessel contents.

**Solution.**
**(a)** Specific volume of the mixture is $v = V/m_{\mathrm{tot}} = 0.500 m^3/2.000 kg = 0.2500 m^3/kg$. Since $v_f < v < v_g$, applying (`eq:05:purelever`):

$$
x = \frac{v - v_f}{v_g - v_f} = \frac{0.2500 - 0.0010603}{0.8913 - 0.0010603} = \frac{0.24894}{0.89024} = \mathbf{0.27963\;(27.96\%\text{ vapor by mass})}.
$$

**(b)** Vapor mass $m_g = x\,m_{\mathrm{tot}} = (0.27963)(2.000 kg) = \mathbf{0.5593 kg}$ and liquid mass $m_f = 2.000 - 0.5593 = \mathbf{1.4407 kg}$. (Notice that although liquid is $72.04\%$ of the mass, it occupies only $m_f v_f = 0.00153 m^3 = 0.31\%$ of the volume!)
**(c)** Specific enthalpy $h = h_f + x\,h_{fg} = 503.81 + (0.27963)(2202.1) = 1119.59 kJ/kg$, so total enthalpy is $H = m_{\mathrm{tot}}h = \mathbf{2239.2 kJ}$.

**✓ Verified by:** $m_f v_f + m_g v_g = (1.44073)(0.0010603) + (0.55927)(0.8913) = 0.50000 m^3$ (`check_sec02_05.py`).

### Worked Example — Binary Eutectic Alloy Lever Rule & Microconstituents (`2027 Cornell E1`) `[National $\cdot$ Rule 5.c.ii]`

A $m_{\mathrm{tot}} = 500.0 g$ lead–tin ($\mathrm{Pb\text{--}Sn}$) solder alloy of overall composition $w_0 = 35.0\,\mathrm{wt\%\ Sn}$ ($65.0\,\mathrm{wt\%\ Pb}$) is cooled slowly from the melt (Fig. `fig:05:binary-eutectic`: eutectic point $w_E = 61.9\,\mathrm{wt\%\ Sn}$ at $T_E = 183.0 °C$; maximum solid solubility limits at $183.0 °C$ are $w_{\alpha E} = 18.3\,\mathrm{wt\%\ Sn}$ in the $\alpha$-phase and $w_{\beta E} = 97.8\,\mathrm{wt\%\ Sn}$ in the $\beta$-phase).
(a) At $T = 220.0 °C$ inside the $(\alpha + L)$ field, the solidus and liquidus compositions are $w_S = 14.0\,\mathrm{wt\%\ Sn}$ and $w_L = 50.0\,\mathrm{wt\%\ Sn}$; calculate the mass of solid $\alpha$ and liquid $L$ present.
(b) At $T = 182.9 °C$ (just below the eutectic isotherm $T_E$), calculate the total mass fraction of $\alpha$-phase and $\beta$-phase, and distinguish the **primary (proeutectic) $\alpha$** mass fraction from the **eutectic microconstituent** mass fraction.

**Solution.**
**(a)** At $T = 220.0 °C$ ($w_S = 14.0\%, w_0 = 35.0\%, w_L = 50.0\%$), the tie-line lever rule (`eq:05:eutecticlever`) gives:

$$
f_L = \frac{w_0 - w_S}{w_L - w_S} = \frac{35.0 - 14.0}{50.0 - 14.0} = \frac{21.0}{36.0} = \mathbf{0.5833\;(58.33\%)}, \qquad
  f_S = \frac{w_L - w_0}{w_L - w_S} = \frac{50.0 - 35.0}{36.0} = \frac{15.0}{36.0} = \mathbf{0.4167\;(41.67\%)},
$$

so $m_L = (0.58333)(500.0 g) = \mathbf{291.7 g}$ of liquid (at $50.0\%\,\mathrm{Sn}$) and $m_\alpha = \mathbf{208.3 g}$ of solid $\alpha$ (at $14.0\%\,\mathrm{Sn}$).
**(b)** At $T = 182.9 °C$ ($T_E^-$), the tie-line spans the full two-solid $(\alpha + \beta)$ field from $w_{\alpha E} = 18.3\%$ to $w_{\beta E} = 97.8\%$:

$$
f_{\alpha,\mathrm{tot}} = \frac{w_{\beta E} - w_0}{w_{\beta E} - w_{\alpha E}} = \frac{97.8 - 35.0}{97.8 - 18.3} = \frac{62.8}{79.5} = \mathbf{0.7899\;(78.99\%)}, \qquad
  f_{\beta,\mathrm{tot}} = \frac{w_0 - w_{\alpha E}}{w_{\beta E} - w_{\alpha E}} = \frac{16.7}{79.5} = \mathbf{0.2101\;(21.01\%)}.
$$

Just above $T_E$ ($T = 183.1 °C, T_E^+$), the tie-line spans $w_{\alpha E} = 18.3\%$ to $w_E = 61.9\%$, so by (`eq:05:microconstituent`) the **primary proeutectic $\alpha$** fraction formed before reaching $T_E$ and the **eutectic lamellar microconstituent** fraction formed at $T_E$ are:

$$
f_{\text{primary }\alpha} = \frac{w_E - w_0}{w_E - w_{\alpha E}} = \frac{61.9 - 35.0}{61.9 - 18.3} = \frac{26.9}{43.6} = \mathbf{0.6170\;(61.70\%)}, \qquad
  f_{\text{eutectic}} = \frac{w_0 - w_{\alpha E}}{w_E - w_{\alpha E}} = \frac{16.7}{43.6} = \mathbf{0.3830\;(38.30\%)}.
$$

**✓ Verified by:** $\mathrm{Sn}$ mass check at $220 °C$: $0.58333(50.0) + 0.41667(14.0) = 29.167 + 5.833 = 35.00\% = w_0$ (`check_sec02_05.py`).

### Worked Example — High-Altitude Boiling Point via Algebraic Clausius–Clapeyron `[Competition $\cdot$ Rules 5.c.ii, 5.d.iv]`

At sea level ($P_1 = 101.325 kPa$), water boils at $T_1 = 100.00 °C = 373.15 K$ with $\Delta_{\mathrm{vap}}H_m = 40.65 kJ/mol$. Using the algebraic two-point Clausius–Clapeyron equation (`eq:05:cc`), compute the boiling point of water $T_2$ on the summit of Pike's Peak where barometric pressure is $P_2 = 58.60 kPa$.

**Solution.**
Directly substituting $P_2/P_1 = 58.60 / 101.325 = 0.57834$ and $\Delta_{\mathrm{vap}}H_m = 40650 J/mol$ into (`eq:05:cc`):

$$
\begin{aligned}
\frac{1}{T_2} &= \frac{1}{T_1} - \frac{R}{\Delta_{\mathrm{vap}}H_m}\ln\!\left(\frac{P_2}{P_1}\right) = \frac{1}{373.15 K} - \frac{8.31446 J/mol/K}{40650 J/mol}\ln(0.57834) = 2.79189×10^{-3} /K, \\
  T_2 &= \frac{1}{2.79189×10^{-3} /K} = \mathbf{358.18 K = 85.03 °C} \quad (\text{NIST steam-table interpolation gives } 85.32 °C).
\end{aligned}
$$

**✓ Verified by:** Re-substituting $T_2 = 358.180 K$ into (`eq:05:cc`) reproduces $P_2 = 58.600 kPa$ (`check_sec02_05.py`).

### Worked Example — Psychrometrics: Relative Humidity, Humidity Ratio $\omega$, Dew Point & Condensation `[Competition $\cdot$ Rule 5.c.ii]`

Air inside a testing gymnasium of volume $V = 1000 m^3$ is at $T_1 = 30.0 °C$ ($303.15 K$), total pressure $P = 101.325 kPa$, and relative humidity $\mathrm{RH}_1 = 60.0\%$. Using Table `tab:05:steamtables` ($P_{\mathrm{sat}}(30 °C) = 4.2470 kPa$, $P_{\mathrm{sat}}(20 °C) = 2.3393 kPa$, $P_{\mathrm{sat}}(15 °C) = 1.7057 kPa$), find (a) the water vapor partial pressure $P_{v,1}$ and humidity ratio $\omega_1$, (b) the approximate dew point $T_{\mathrm{dp}}$, and (c) the mass of liquid water that condenses out if the room air is cooled isobarically to $T_2 = 15.0 °C$.

**Solution.**
**(a)** From (`eq:05:psychro`), $P_{v,1} = \mathrm{RH}_1\,P_{\mathrm{sat}}(30 °C) = (0.600)(4.2470 kPa) = \mathbf{2.5482 kPa}$ and dry-air partial pressure is $P_{a,1} = 101.325 - 2.5482 = 98.7768 kPa$, giving humidity ratio:

$$
\omega_1 = 0.62198\,\frac{P_{v,1}}{P - P_{v,1}} = 0.62198\,\frac{2.5482}{98.7768} = \mathbf{0.016045 kg/kg\;(16.05 g/kg\text{ dry air})}.
$$

**(b)** At the dew point, $P_{\mathrm{sat}}(T_{\mathrm{dp}}) = P_{v,1} = 2.5482 kPa$, which lies between $20 °C$ ($2.3393 kPa$) and $25 °C$ ($3.1699 kPa$). Linear interpolation gives $T_{\mathrm{dp}} \approx 20.0 + 5.0\frac{2.5482 - 2.3393}{3.1699 - 2.3393} = \mathbf{21.26 °C}$ (exact Antoine solution: $21.39 °C$).
**(c)** Mass of dry air in the $1000 m^3$ room is $m_a = \dfrac{P_{a,1}V M_a}{RT_1} = \dfrac{(98776.8 Pa)(1000 m^3)(0.028965 kg/mol)}{(8.31446 J/mol/K)(303.15 K)} = 1134.9 kg$. Because $T_2 = 15.0 °C < T_{\mathrm{dp}}$, the air becomes saturated at $15.0 °C$ ($P_{v,2} = P_{\mathrm{sat}}(15 °C) = 1.7057 kPa$):

$$
\omega_2 = 0.62198\,\frac{1.7057}{101.325 - 1.7057} = 0.010649 kg/kg \implies
  m_{\mathrm{cond}} = m_a(\omega_1 - \omega_2) = (1134.9 kg)(0.016045 - 0.010649) = \mathbf{6.124 kg}.
$$

**✓ Verified by:** Ideal-gas vapor check: $\Delta m_v = m_a(\omega_1 - \omega_2) = 6.124 kg$ (`check_sec02_05.py`).

### Worked Example — Adiabatic Crystallization of Supercooled Water & Colligative Antifreeze Check `[Competition $\cdot$ Rule 5.c.ii]`

(a) A $200.0 g$ sample of ultra-pure liquid water is supercooled at $1 atm$ to $T_{\mathrm{sc}} = -12.0 °C$ ($c_w = 4.184 J/g/K, L_f = 333.55 J/g$) in an adiabatic container and then nucleated by a microscopic dust speck. What final temperature $T_f$ does the sample jump to, and how many grams of ice form?
(b) How many grams of calcium chloride ($\mathrm{CaCl_2}$, $M = 110.98 g/mol$, ideal van 't Hoff factor $i = 3$, $K_f = 1.853 K · kg/mol$) must be dissolved in $200.0 g$ of water to depress its equilibrium freezing point to $-12.0 °C$ so it never supercools?

**Solution.**
**(a)** Nucleation triggers rapid crystallization that releases $L_f$ until the remaining liquid + ice mixture reaches the equilibrium melting plateau $\mathbf{T_f = 0.00 °C}$. By (`eq:05:supercool`):

$$
f_{\mathrm{frozen}} = \frac{c_w(0 - T_{\mathrm{sc}})}{L_f} = \frac{(4.184)(12.0)}{333.55} = \mathbf{0.15053\;(15.05\%)} \implies
  m_{\mathrm{ice}} = (0.15053)(200.0 g) = \mathbf{30.11 g}.
$$

**(b)** From (`eq:05:colligative`), $\Delta T_f = -i K_f m = -12.0 K \implies \text{molality } m = \dfrac{12.0}{(3)(1.853)} = 2.1587 mol/kg$ of $\mathrm{H_2O}$. For $0.2000 kg$ of water:

$$
m_{\mathrm{CaCl_2}} = (0.2000 kg)(2.1587 mol/kg)(110.98 g/mol) = \mathbf{47.91 g}.
$$

**✓ Verified by:** Energy released by freezing $30.106 g$ ice ($10041.6 J$) equals sensible warming of $200.0 g$ water by $12.0 K$ (`check_sec02_05.py`).

### Worked Example — Dry Ice ($\mathrm{CO_2(s)}$) Sublimation Bath & Sealed-Vessel Triple-Point Liquefaction `[National $\cdot$ Rules 5.c.ii, 5.c.vi]`

(a) In an open insulated Dewar at $1.00 atm$, a chemist drops $m_{\mathrm{CO_2}} = 150.0 g$ of solid dry ice at its normal sublimation temperature $T_{\mathrm{sub}} = -78.46 °C$ ($L_{\mathrm{sub}} = 571.3 kJ/kg$, Table `tab:05:sixtransitions`) into $m_{\mathrm{eth}} = 500.0 g$ of liquid ethanol initially at $T_i = 22.00 °C$ ($c_{\mathrm{eth}} = 2.440 J/g/K$, freezing point $T_{m,\mathrm{eth}} = -114.1 °C$). Assuming the evolved $\mathrm{CO_2(g)}$ escapes immediately at $-78.46 °C$, does all the dry ice sublime, and what final temperature $T_f$ does the ethanol bath reach?
(b) If instead $m = 150.0 g$ of dry ice ($M = 44.010 g/mol$) is sealed inside an evacuated rigid steel cylinder of internal volume $V = 1.200 L$ and warmed slowly toward room temperature, at what temperature $T$ does **liquid $\mathrm{CO_2}$** first appear, and what is the ideal-gas pressure estimate inside the cylinder at that moment?

**Solution.**
**(a)** Maximum heat that the $500.0 g$ ethanol can release in cooling from $+22.00 °C$ down to $-78.46 °C$ ($\Delta T = 100.46 K$) is:

$$
Q_{\mathrm{eth,\max}} = m_{\mathrm{eth}} c_{\mathrm{eth}}(22.00 - (-78.46)) = (500.0 g)(2.440 J/g/K)(100.46 K) = 122561 J = 122.56 kJ.
$$

Complete sublimation of $150.0 g$ dry ice requires $Q_{\mathrm{sub,all}} = m_{\mathrm{CO_2}} L_{\mathrm{sub}} = (0.1500 kg)(571.3 kJ/kg) = \mathbf{85.695 kJ} < Q_{\mathrm{eth,\max}}$. Thus **100% of the dry ice sublimes**, and the ethanol cools to:

$$
T_f = T_i - \frac{Q_{\mathrm{sub,all}}}{m_{\mathrm{eth}} c_{\mathrm{eth}}} = 22.00 - \frac{85695 J}{1220.0 J/K} = 22.00 - 70.24 = \mathbf{-48.24 °C} \quad (\text{still liquid, since } T_f > -114.1 °C).
$$

**(b)** By Table `tab:05:h2oco2`, liquid $\mathrm{CO_2}$ cannot form below the triple point $(T_{\mathrm{tp}} = \mathbf{216.59 K = -56.56 °C}, P_{\mathrm{tp}} = \mathbf{517.96 kPa = 5.112 atm})$. Since $n = 150.0/44.010 = 3.4083 mol$ in $V = 1.200×10^{-3} m^3$ would generate an ideal-gas pressure $P_{\mathrm{id}}(T_{\mathrm{tp}}) = nRT_{\mathrm{tp}}/V = 5.115 MPa \gg P_{\mathrm{tp}}$, the vapor follows the solid–vapor sublimation curve up to $\mathbf{T_{\mathrm{tp}} = -56.56 °C}$, where liquid $\mathrm{CO_2}$ first melts at $\mathbf{P_{\mathrm{tp}} = 518.0 kPa}$!

**✓ Verified by:** To hold an ethanol bath at the $-78.46 °C$ dry-ice plateau requires at least $m_{\mathrm{CO_2}} \ge 122.56/571.3 = 214.5 g$ of dry ice (`check_sec02_05.py`).

### Worked Example — Isochoric Heating Across the Saturation Dome & Steam-Table Interpolation `[National $\cdot$ Rules 5.c.ii, 5.c.vi]`

Using Table `tab:05:steamtables`: (a) Estimate the saturation pressure $P_{\mathrm{sat}}$, latent heat $h_{fg}$, and saturated vapor specific volume $v_g$ of water at $T = 70.0 °C$ by linear interpolation between $60.0 °C$ and $80.0 °C$.
(b) A sealed rigid quartz ampoule of volume $V = 31.06 cm^3$ contains $m = 10.00 g$ of $\mathrm{H_2O}$ initially at $T_1 = 25.0 °C$. Determine its specific volume $v$, show that heating the sealed ampoule at constant volume causes it to pass directly through the **critical point** $(T_c = 373.95 °C, P_c = 22.064 MPa)$ without completely drying out or filling with liquid, and compute its initial vapor quality $x_1$ at $25.0 °C$.

**Solution.**
**(a)** Midpoint linear interpolation at $T = 70.0 °C$ ($\text{fraction } f = (70-60)/(80-60) = 0.500$) between $60.0 °C$ and $80.0 °C$ in Table `tab:05:steamtables` gives:

$$
P_{\mathrm{sat}}(70 °C) \approx \frac{19.946 + 47.414}{2} = \mathbf{33.68 kPa}\;\text{(NIST exact: }31.20 kPa\text{)}, \qquad
  h_{fg}(70 °C) \approx \frac{2357.7 + 2308.0}{2} = \mathbf{2332.85 kJ/kg},
$$

$$
v_g(70 °C) \approx \frac{7.667 + 3.405}{2} = \mathbf{5.536 m^3/kg}.
$$

**(b)** The constant specific volume of the sealed ampoule is:

$$
v = \frac{V}{m} = \frac{31.06×10^{-6} m^3}{0.01000 kg} = \mathbf{0.003106 m^3/kg} = v_c \quad \left(\rho = \frac{1}{v} = 322.0 kg/m^3 = \rho_c\right).
$$

Because $v = v_c$ identically (Table `tab:05:steamtables`, bottom row), the vertical isochoric path on the $P$–$v$ dome (Fig. `fig:05:pv-dome`) intersects the exact apex of the saturation dome at $(T_c = 373.95 °C, P_c = 22.064 MPa)$, where the meniscus fades out in mid-vessel! At $T_1 = 25.0 °C$ ($v_f = 0.0010030 m^3/kg, v_g = 43.34 m^3/kg$), the initial vapor quality is:

$$
x_1 = \frac{v - v_f}{v_g - v_f} = \frac{0.003106 - 0.0010030}{43.34 - 0.0010030} = \mathbf{4.852×10^{-5}\;(0.00485\%\text{ vapor by mass})}.
$$

**✓ Verified by:** If $v < v_c$, isochoric heating fills the tube with liquid below $T_c$; if $v > v_c$, all liquid evaporates below $T_c$; only $v = v_c = 0.003106 m^3/kg$ hits the critical point (`check_sec02_05.py`).

### [TRAP & DIAGNOSTIC: §5 Top 5 Phase Transitions, Phase Diagrams & Psychrometrics Traps]

| **Wrong move / Symptom** | **What it produces / Why it fails** | **5-second diagnostic & fix** |
| --- | --- | --- |
| Using the adjacent tie-line segment instead of the **opposite** tie-line segment in the binary eutectic lever rule | Swaps liquid fraction $f_L$ and solid fraction $f_S$ ($1 - f$ error on `Cornell E1` problems) | Fulcrum check: as $w_0 \to w_L$, $f_L$ must approach $1$, so the numerator of $f_L$ is $(w_0 - w_S)$ (opposite arm!). |
| Claiming liquid $\mathrm{CO_2}$ exists at $1 atm$ or that water's fusion slope $dP/dT$ is positive | Violates $P_{\mathrm{tp}}(\mathrm{CO_2}) = 5.11 atm > 1 atm$ and $\rho_{\mathrm{ice}} < \rho_{\mathrm{water}}$ | Check Table `tab:05:h2oco2`: $\mathrm{H_2O}$ has $dP/dT = -133.2 atm/K < 0$; $\mathrm{CO_2}$ sublimes at $1 atm, -78.5 °C$. |
| Plugging Celsius temperatures $T_C$ or $\Delta_{\mathrm{vap}}H_m$ in $kJ/mol$ directly into Clausius–Clapeyron with $R = 8.314 J/mol/K$ | Off by orders of magnitude in $P_2/P_1$ or $T_2$ | Always convert $T$ to $K$ and $\Delta_{\mathrm{vap}}H_m$ to $J/mol$ ($\times 1000$) before dividing by $R = 8.31446 J/mol/K$. |
| Confusing relative humidity $\mathrm{RH} = P_v/P_{\mathrm{sat}}(T)$ with humidity ratio $\omega = m_v/m_a = 0.622\,P_v/(P-P_v)$ | Warming air at constant moisture lowers $\mathrm{RH}$ even though $\omega$ and $P_v$ stay constant! | $\omega$ and dew point $T_{\mathrm{dp}}$ depend only on $P_v$; $\mathrm{RH}$ drops on warming because $P_{\mathrm{sat}}(T)$ grows exponentially. |
| Applying the ideal-vapor Clausius–Clapeyron equation (`eq:05:cc`) to a solid–liquid melting curve | Ideal-gas substitution $\Delta V_m \approx RT/P$ is completely invalid for solid–liquid melting! | Always use the exact Clapeyron slope $\Delta P/\Delta T = L_f/[T(v_\ell - v_s)]$ (`eq:05:clapeyron`) for melting curves. |

### [2027 HEAT-COLLECTOR DEVICE & LAB: Evaporative Latent-Heat Penalty & Removable BoPET Glazing Cap in the 2027 Collector]

Because water's latent heat of vaporization at $30–45 °C$ is huge ($L_v \approx 2420 kJ/kg = 2420 J/g$), the evaporation of just $\mathbf{1.00 g}$ of water from an open 9 oz cup strips away $2420 J$ of thermal energy—enough to cool $m_w = 50.0 g$ of water by $\Delta T_{\mathrm{loss}} = 2420 J/[(50.0 g)(4.184 J/g/K)] = \mathbf{11.57 °C}$! Under `2027 Official Clarification #5`, the $3.8 cm$ ($1.5 in$) top access hole (`Rule 4.f`) only needs to be open when inserting/removing the cup or inserting the ES thermometer at the end of the run: placing a removable optical-grade clear **BoPET (Mylar) or low-iron glass glazing window** over the aperture during the heating run traps the saturated headspace ($P_v \to P_{\mathrm{sat}}$), eliminating evaporative latent-heat loss while transmitting $\sim 90\%$ of the lamp's visible/near-IR beam (§`sec:14`)  **[S01,S02]**.

—
**See also:** §`sec:01.4` (`QS-04` Phase Diagrams), §`sec:01.5` (`QS-05` Lever Rule), §`sec:04.3` (5-Zone Calorimetry), §`sec:08.4` (Gibbs Free Energy $\Delta G$), and §`sec:14` (Evaporative Suppression in the 2027 Collector).
