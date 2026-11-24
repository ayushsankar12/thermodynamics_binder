<!-- Source: src/appC.tex | Tab: Tab 9: INDEX/APP | Target: 4 pp -->
# Appendix C: Master Symbol Dictionary, Glossary & Printed 5-Index Suite {#app:C}

> **[SCOPE: REQUIRED | Locked Notation Contract (§2) + 5 Auto-Generated MakeIndex Retrieval Indices]**

## Master Thermodynamic, Heat-Transfer & 2027 Collector Symbol Dictionary

| **Symbol** | **Quantity Name** | **SI Unit** | **Critical Disambiguation & Sign / Context Rules** |
| --- | --- | --- | --- |
| $Q$ vs. $\dot{Q}$ vs. $q''$ | Heat energy vs. heat rate vs. heat flux | J; W; W/m^2 | $Q > 0$ enters system (J); $\dot{Q} = dQ/dt$ is power (W); $q'' = \dot{Q}/A$ is flux (W/m^2); $q = Q/m$ is specific heat transfer (J/kg). |
| $W_{\mathrm{by}}$ vs. $w_{\mathrm{on}}$ | Boundary work by vs. on system | J | Physics (locked): $\Delta U = Q - W_{\mathrm{by}}$ ($W_{\mathrm{by}} = +\int P\,dV > 0$ expansion). Chemistry: $\Delta U = q + w_{\mathrm{on}}$ ($w_{\mathrm{on}} = -W_{\mathrm{by}} > 0$ compression). |
| $U, H, F, G$ | Internal energy, enthalpy, Helmholtz, Gibbs | J | Extensive state functions ($H = U + PV$, $F = U - TS$, $G = H - TS$). Lowercase $u, h, f, g$ are mass-specific (J/kg); $U_m, H_m, G_m$ are molar (J/mol). |
| $S, s, S_m, S_{\mathrm{gen}}$ | Entropy (total, specific, molar, generated) | J/K; J/kg/K; J/mol/K | State function ($dS = \delta Q_{\mathrm{rev}}/T$); $S_{\mathrm{gen}} = \Delta S_{\mathrm{univ}} = \Delta S_{\mathrm{sys}} + \Delta S_{\mathrm{surr}} \ge 0$ ($=0$ iff reversible). |
| $c, c_p, c_v$ vs. $C$ vs. $C_m$ | Specific vs. total vs. molar heat capacity | J/kg/K; J/K; J/mol/K | $C = m c = n C_m$ (J/K) is extensive object/calorimeter capacity; $c$ is per unit mass; $C_{P,m}, C_{V,m}$ are per mole. |
| $L_f, L_v, L_s$ | Specific latent heats (fusion, vap., subl.) | J/kg (or kJ/kg) | Molar forms: $\Delta H_{\mathrm{fus},m} = M L_f$, $\Delta H_{\mathrm{vap},m} = M L_v$, $\Delta H_{\mathrm{sub},m} = M L_s$ (J/mol). |
| $R$ vs. $R_{\mathrm{sp}}$ vs. $R_{\mathrm{th}}$ vs. $R_{\mathrm{val}}$ | Gas const. vs. specific gas const. vs. thermal resistance vs. $R$-value | J/mol/K; J/kg/K; K/W; m^2 K/W | $R = 8.31446 J/mol/K$; $R_{\mathrm{sp}} = R/M$; $R_{\mathrm{th}} = \Delta T/\dot{Q} = L/(kA)$ (K/W); $R_{\mathrm{val}} = A R_{\mathrm{th}} = L/k$ (m^2 K/W). |
| $h$ vs. $h_{\mathrm{conv}}$ vs. $h_c$ vs. $h_{\mathrm{Planck}}$ | Specific enthalpy vs. convection coeff. vs. contact conductance vs. Planck const. | J/kg; W/m^2/K; W/m^2/K; J s | Check units: enthalpy $h = u + Pv$ (J/kg or kJ/kg); heat transfer $h, h_c, h_r$ (W/m^2/K); $h_{\mathrm{bulb}}$ is lamp bulb height ($40–65 cm$). |
| $k$ vs. $k_B$ | Thermal conductivity vs. Boltzmann const. | W/m/K; J/K | Always write Boltzmann constant with subscript $k_B = 1.380649×10^{-23} J/K$. |
| $\alpha$ vs. $\alpha_L$ vs. $\alpha_{\mathrm{NIR}}$ | Thermal diffusivity vs. linear expansion vs. radiative absorptance | m^2/s; /K; $1$ | $\alpha = k/(\rho c_p)$ (m^2/s); $\alpha_L = L_0^{-1}(dL/dT)$ (/K); $\alpha_\lambda \in [0,1]$ (dimensionless absorptance). |
| $\beta$ vs. $\kappa_T$ vs. $K_T$ | Volumetric expansion, isothermal compressibility, bulk modulus | /K; /Pa; Pa | $\beta = V^{-1}(\partial V/\partial T)_P$ ($\approx 3\alpha_L$ solid, $1/T$ ideal gas); $\kappa_T = -V^{-1}(\partial V/\partial P)_T = 1/K_T$; $C_P - C_V = TV\beta^2/\kappa_T$. |
| $\gamma$ vs. $n$ vs. $f$ | Heat capacity ratio, polytropic index, active DOF | $1$ (dimensionless) | Ideal gas: $\gamma = C_{P,m}/C_{V,m} = (f+2)/f$; polytropic $PV^n = \mathrm{const}$ ($n=0$ isobar, $1$ isotherm, $\gamma$ adiabat, $\infty$ isochore). |
| $\varepsilon, \rho_{\mathrm{opt}}, \tau_{\mathrm{opt}}$ | Emissivity, reflectance, transmittance | $1$ (dimensionless) | Radiation balance: $\alpha + \rho_{\mathrm{opt}} + \tau_{\mathrm{opt}} = 1$; Kirchhoff: $\varepsilon_\lambda(T) = \alpha_\lambda(T)$ at same $\lambda, T$. |
| $M_b, I_b, J, G, F_{ij}$ | Radiant exitance, radiance, radiosity, irradiation, view factor | W/m^2; W/m^2/sr; W/m^2; W/m^2; $1$ | $M_b = \sigma T^4 = \pi I_b$; radiosity $J_i = \varepsilon_i M_{b,i} + (1-\varepsilon_i)G_i$; reciprocity $A_i F_{ij} = A_j F_{ji}$; enclosure $\sum_j F_{ij} = 1$. |
| $\tau$ vs. $\tau_p$ vs. $b$ | Collector time const., probe time const., thermal effusivity | s; s; J/m^2/K/s^1/2 | Collector $\tau = R_{\mathrm{th}}C_{\mathrm{eff}} \approx 900–1400 s$; probe $\tau_p \approx 2–15 s$; effusivity $b = \sqrt{k\rho c_p}$ governs contact temp $T_i$. |
| $\mu_{\mathrm{JT}}$ vs. $Z$ vs. $\omega$ | Joule–Thomson coeff., compressibility factor, humidity ratio / acentric factor | K/Pa; $1$; $\mathrm{kg_v/kg_{da}}$ | $\mu_{\mathrm{JT}} = (\partial T/\partial P)_H = C_P^{-1}(T(\partial V/\partial T)_P - V)$; $Z = PV/(nRT)$; psychrometric $\omega = 0.62198 P_v/(P-P_v)$. |
| $x$ vs. $w_i$ vs. $x_i$ | Vapor quality vs. mass fraction vs. mole fraction | $1$ (dimensionless) | Two-phase quality $x = m_g/(m_f+m_g) \in [0,1]$; alloy mass fraction $w_i = m_i/m_{\mathrm{tot}}$; gas mole fraction $x_i = n_i/n_{\mathrm{tot}}$. |
| $\eta_{\mathrm{th}}, \eta_C, \eta_{\mathrm{II}}, \mathrm{COP}_R, \mathrm{COP}_{\mathrm{HP}}$ | Thermal, Carnot, 2nd-law efficiencies & coefficients of performance | $1$ (dimensionless) | $\eta_{\mathrm{th}} = W_{\mathrm{net}}/Q_H \le \eta_C = 1 - T_C/T_H$; $\eta_{\mathrm{II}} = \eta_{\mathrm{th}}/\eta_C = \mathrm{COP}/\mathrm{COP}_C$; $\mathrm{COP}_{\mathrm{HP}} = \mathrm{COP}_R + 1$. |
| $\mathrm{FS, ES, TS, PS, TG, PE}$ | 2027 Official Scoring Quantities (**[2027-RULE]** 6) | points or $^\circ\mathrm{C}$ | $\mathrm{FS} = \mathrm{ES}_{50} + \mathrm{TS}_{30} + \mathrm{PS}_{20}$; $\mathrm{TG} = T_f - T_i$ ($^\circ\mathrm{C}$); $\mathrm{PE} = 1 - \|T_f - T_{\mathrm{pred}}\|/T_f$ ($T_f$ in $^\circ\mathrm{C}$!). |

{Table C.2: Dimensionless Groups, Characteristic Lengths & Locked Subscript Conventions  **[S12,S13]**}

| **Group** | **Definition** | **Characteristic Length $L$ or $L_c$** | **Physical Ratio & Competition Threshold Criterion** |
| --- | --- | --- | --- |
| Biot $\mathrm{Bi}$ | $h L_c / k_{\mathrm{solid}}$ | $L_c = V/A_s$ ($L$ half-slab, $R/2$ cyl., $R/3$ sph.) | Internal conduction resistance / external convection resistance; $\mathbf{\mathrm{Bi} < 0.10}$ validates lumped capacitance. |
| Fourier $\mathrm{Fo}$ | $\alpha_{\mathrm{solid}} t / L_c^2$ | Same $L_c$ as Biot ($V/A_s$ or half-thickness $L$) | Dimensionless time (heat penetration depth2 / body size2); $\mathrm{Bi}\cdot\mathrm{Fo} = h A_s t/(\rho c_p V) = t/\tau$. |
| Nusselt $\mathrm{Nu}_L$ | $h L / k_{\mathrm{fluid}}$ | Plate length $L$, pipe diameter $D$, gap $\delta$ | Total convective heat transfer / pure fluid conduction ($\mathrm{Nu}_\delta = 1$ in quiescent air gap $\mathrm{Ra}_\delta < 1708$). |
| Reynolds $\mathrm{Re}_L$ | $\rho u_\infty L / \mu = u_\infty L / \nu$ | Plate length $L$ or pipe hydraulic $D_h = 4A_c/P_w$ | Inertia / viscous forces (flat plate transition $\mathrm{Re}_x \approx 5×10^{5}$; internal pipe transition $\mathrm{Re}_D \approx 2300$). |
| Prandtl $\mathrm{Pr}$ | $\nu / \alpha_f = c_p \mu / k_{\mathrm{fluid}}$ | Fluid property (no length scale) | Momentum diffusivity / thermal diffusivity ($\mathrm{Pr}_{\mathrm{air}} \approx 0.71$; $\mathrm{Pr}_{\mathrm{water,25^\circ C}} \approx 6.14$; liquid metals $\ll 0.03$). |
| Grashof $\mathrm{Gr}_L$ | $g\beta\Delta T L^3 / \nu^2$ | Vertical height $L$, horizontal $L = A_s/P$, gap $\delta$ | Buoyancy force $\times$ inertia / $(\text{viscous force})^2$; for ideal gas, evaluate $\beta = 1/T_f$ in Kelvin at film temp $T_f$. |
| Rayleigh $\mathrm{Ra}_L$ | $\mathrm{Gr}_L \mathrm{Pr} = g\beta\Delta T L^3 / (\nu\alpha_f)$ | Vertical wall $L$, horizontal plate $A_s/P$, gap $\delta$ | Buoyancy-driven natural convection parameter (horizontal cavity onset $\mathrm{Ra}_\delta = 1708$; vertical turbulent $\mathrm{Ra}_L > 10^9$). |
| Lewis $\mathrm{Le}$ | $\alpha_f / D_{AB} = \mathrm{Sc}/\mathrm{Pr}$ | Fluid/vapor mixture property | Thermal diffusivity / mass diffusivity ($\mathrm{Le}_{\mathrm{H_2O\text{--}air}} \approx 0.85 \implies$ Chilton–Colburn evaporative analogy $h_m \approx h/(\rho c_p \mathrm{Le}^{2/3})$). |

## Comprehensive Thermodynamics & 2027 Device Glossary (A–Z)

{- **Absolute zero ($0 K = -273.15 °C$):**  Lower bound of thermodynamic temperature where classical kinetic energy vanishes and crystal entropy reaches its Third-Law floor ($S \to 0$).
- **Acentric factor ($\omega$):**  Pitzer non-sphericity metric $\omega = -\log_{10}(P_{\mathrm{sat}}/P_c)_{T_r=0.7} - 1.0$ measuring departure from simple spherical-molecule corresponding states.
- **Adiabatic process / wall:**  Process or boundary with zero heat transfer ($Q = 0$); a reversible adiabatic process is *isentropic* ($\Delta S = 0$, $PV^\gamma = \mathrm{const}$ for ideal gas).
- **Amagat's law of additive volumes:**  Total volume of an ideal-gas mixture at $(T,P)$ equals the sum of component partial volumes $V_i = x_i V$.
- **Antoine equation:**  Empirical 3-parameter vapor-pressure correlation $\log_{10} P_{\mathrm{sat}} = A - B/(T + C)$ derived from Clausius–Clapeyron.
- **Available energy (Exergy, $X$):**  Maximum useful work obtainable as a system comes into equilibrium with the ambient dead state $(T_0, P_0)$; destroyed exergy is $X_{\mathrm{dest}} = T_0 S_{\mathrm{gen}} \ge 0$.
- **Avogadro's law:**  Equal volumes of all ideal gases at the same temperature and pressure contain equal numbers of molecules ($V/n = RT/P$).
- **Biot number ($\mathrm{Bi} = hL_c/k_s$):**  Ratio of internal solid conduction resistance to external boundary convection resistance; $\mathrm{Bi} < 0.1$ validates lumped-capacitance $T(t)$.
- **Blackbody:**  Idealized perfect absorber ($\alpha_\lambda = 1$) and emitter ($\varepsilon_\lambda = 1$) at all wavelengths and directions ($M_b = \sigma T^4$).
- **BoPET selective glazing (Mylar):**  Biaxially oriented polyethylene terephthalate film with high near-IR transmittance ($\tau_{\mathrm{NIR}} \approx 0.90$) used as an unattached cup vapor barrier (`Clarification #5`).
- **Boyle temperature ($T_B$):**  Temperature where the second virial coefficient vanishes ($B(T_B) = 0$, so $Z \approx 1$ as $P\to 0$; for a van der Waals gas, $T_B = a/(Rb) = \tfrac{27}{8}T_c$).
- **Calorimeter constant ($C_{\mathrm{cal}}$):**  Effective heat capacity ($J/K$) of the calorimeter cup, stirrer, and thermometer probe assembly ($Q_{\mathrm{cal}} = C_{\mathrm{cal}}\Delta T$).
- **Carnot theorem & efficiency:**  No heat engine operating between $T_H$ and $T_C$ can exceed $\eta_C = 1 - T_C/T_H$ (K), and all reversible engines between $T_H, T_C$ have $\eta = \eta_C$.
- **Choked / critical insulation radius ($r_{\mathrm{crit}}$):**  Outer insulation radius $r_{\mathrm{crit}} = k_{\mathrm{ins}}/h_{\mathrm{ext}}$ (cylinder) or $2k_{\mathrm{ins}}/h_{\mathrm{ext}}$ (sphere) that maximizes heat loss.
- **Clausius inequality:**  $\oint \delta Q/T_b \le 0$ for any cycle, with equality iff totally reversible; implies $dS \ge \delta Q/T$.
- **Clausius–Clapeyron equation:**  Phase-boundary slope $dP/dT = L/(T\Delta v) \approx P\Delta H_{\mathrm{vap},m}/(RT^2)$ when $v_g \gg v_f$ and vapor behaves as an ideal gas.
- **Coefficient of performance ($\mathrm{COP}$):**  Ratio of desired heat transfer to work input: $\mathrm{COP}_R = Q_C/W_{\mathrm{in}}$ (cooling) and $\mathrm{COP}_{\mathrm{HP}} = Q_H/W_{\mathrm{in}} = \mathrm{COP}_R + 1$ (heating).
- **Colligative properties:**  Solution properties ($\Delta T_b = i K_b m$, $\Delta T_f = -i K_f m$, osmotic pressure $\Pi = i M R T$) that depend on total solute particle concentration $i m$.
- **Compressibility factor ($Z = PV/nRT$):**  Measure of non-ideality ($Z=1$ ideal gas; $Z<1$ attractive forces dominate; $Z>1$ repulsive excluded volume $b$ dominates; $Z_c = 3/8 = 0.375$ for vdW gas).
- **Compound parabolic concentrator (CPC):**  Non-imaging reflector profile achieving the thermodynamic sine-law concentration limit $C_{\max} = 1/\sin^2\theta_a$ (3D) without tracking.
- **Contact conductance ($h_c$):**  Interfacial conductance $h_c = q''/\Delta T_{\mathrm{interface}}$ across micro-asperities between mating solids ($R_{\mathrm{contact}} = 1/(h_c A)$).
- **Critical point ($T_c, P_c, V_{m,c}$):**  Terminus of the liquid–vapor coexistence curve where liquid and vapor phases become indistinguishable ($\Delta H_{\mathrm{vap}} \to 0$).
- **Curzon–Ahlborn efficiency ($\eta_{\mathrm{CA}}$):**  Efficiency $\eta_{\mathrm{CA}} = 1 - \sqrt{T_C/T_H}$ of an endoreversible heat engine operating at maximum power output under finite-rate heat transfer.
- **Dalton's law of partial pressures:**  Total pressure of an ideal-gas mixture equals the sum of component partial pressures $P_i = x_i P$.
- **Dead-air gap ($\delta_c \approx 11 mm$):**  Enclosed air space thin enough ($\mathrm{Ra}_\delta < 1708$, $\delta \lesssim 11 mm$) that buoyancy cannot initiate convection cells, so $\mathrm{Nu}_\delta = 1$.
- **Debye $T^3$ law & Dulong–Petit limit:**  Lattice heat capacity approaches $C_{V,m} \to 3R = 24.94 J/mol/K$ per mole of atoms for $T \gtrsim \Theta_D$, and falls as $C_{V,m} \propto (T/\Theta_D)^3$ as $T \to 0\,K$.
- **Delisle scale ($^\circ\mathrm{De}$):**  Historical *inverted* scale ($0\,^\circ\mathrm{De}$ at $100 °C$ steam point, $150\,^\circ\mathrm{De}$ at $0 °C$ ice point): $T_{\mathrm{De}} = 150 - 1.5\,T_C$.
- **Dew-point temperature ($T_{\mathrm{dp}}$):**  Temperature at which moist air cooled at constant pressure and humidity ratio reaches saturation ($P_v = P_{\mathrm{sat}}(T_{\mathrm{dp}})$).
- **Diathermal wall:**  Boundary that permits heat transfer without mass transfer; two systems separated by a diathermal wall reach thermal equilibrium ($T_A = T_B$).
- **Eutectic point ($T_E, w_E$):**  Minimum-melting invariant point ($F=0$ at fixed $P$) in a binary system where liquid transforms isothermally into two solid phases ($L \rightleftharpoons \alpha + \beta$).
- **Extensive vs. intensive properties:**  Extensive quantities ($U, H, S, G, V, m, n, C$) scale linearly with system size; intensive quantities ($T, P, \rho, c, v, \mu_i$) are size-independent. The ratio of any two extensive properties is intensive!
- **Fin efficiency ($\eta_f$) & effectiveness ($\varepsilon_f$):**  $\eta_f = \dot{Q}_{\mathrm{fin}}/\dot{Q}_{\max} = \tanh(mL_c)/(mL_c)$ compares actual fin heat transfer to an isothermal fin at base temp $T_b$; $\varepsilon_f = \dot{Q}_{\mathrm{fin}}/(h A_c \Delta T_b)$ must exceed $2$ to justify fins.
- **Fourier's law of conduction:**  Conductive heat flux vector $\mathbf{q}'' = -k\nabla T$ (W/m^2) is proportional to the negative temperature gradient.
- **Gibbs phase rule ($F = C - P + 2$):**  Number of independent intensive variables $F$ for $C$ chemically independent components across $P$ coexisting phases in equilibrium ($F = C - P + 1$ at fixed pressure).
- **Gibbs paradox:**  Classical distinguishable-particle formula predicts $\Delta S = 2nR\ln 2 > 0$ when mixing two identical gases at $(T,P)$; resolved by quantum indistinguishability ($1/N!$), giving $\Delta S = 0$.
- **Gray vs. selective surface:**  A gray surface has wavelength-independent $\alpha = \varepsilon$; a selective absorber has high near-IR absorptance ($\alpha_{\mathrm{NIR}} \gtrsim 0.90$) and low thermal-IR emissivity ($\varepsilon_{\mathrm{MIR}} \lesssim 0.15$).
- **Heat-engine sign & orientation rule:**  Clockwise closed loop on $P$–$V$ or $T$–$S$ has $W_{\mathrm{net}} = \oint P\,dV = \oint T\,dS > 0$ (power cycle); counterclockwise loop has $W_{\mathrm{net}} < 0$ (refrigerator / heat pump).
- **Inversion temperature ($T_{\mathrm{inv}}$):**  Locus where $\mu_{\mathrm{JT}} = (\partial T/\partial P)_H = 0$ ($T_{\mathrm{inv,max}} = 2a/(Rb) = \tfrac{27}{4}T_c$ for vdW gas). Since $\mathrm{He}$ ($T_{\mathrm{inv}}\approx40 K$) and $\mathrm{H_2}$ ($\approx202 K$) have $T_{\mathrm{inv}} < 300 K$, throttling them at room temperature *warms* them!
- **Kirchhoff's radiation law:**  Spectral directional emissivity equals spectral directional absorptance at the same wavelength and temperature: $\varepsilon_\lambda(T) = \alpha_\lambda(T)$.
- **Lever rule:**  In any binary two-phase region $(\alpha + L)$, the mass fraction of each phase equals the opposite tie-line arm divided by the total tie-line length: $f_L = (w_0 - w_\alpha)/(w_L - w_\alpha)$.
- **Log-mean temperature difference ($\Delta T_{\mathrm{lm}}$):**  Exact mean driving temperature difference in a steady-flow heat exchanger: $\Delta T_{\mathrm{lm}} = (\Delta T_1 - \Delta T_2)/\ln(\Delta T_1/\Delta T_2)$.
- **Lumped-capacitance model:**  Exponential heating/cooling law $\theta(t)/\theta_i = \exp(-t/\tau)$ with $\tau = \rho c_p V/(h A_s) = R_{\mathrm{th}}C$, valid when $\mathrm{Bi} = hL_c/k_s < 0.10$.
- **Maxwell–Boltzmann speed ratios:**  For an ideal gas at temperature $T$, $v_{\mathrm{mp}} = \sqrt{2RT/M} < \bar{v} = \sqrt{8RT/(\pi M)} < v_{\mathrm{rms}} = \sqrt{3RT/M}$ in ratio $1 : 1.1284 : 1.2247$.
- **Polystyrene / #6 PS Disqualification Rule:**  Under 2027 Rule `3.b.i` and `Clarification #6`, ANY polystyrene (expanded EPS Styrofoam, extruded XPS board, or rigid `#6 PS` plastic cup/sheet) triggers immediate **Part II Disqualification**.
- **Prediction Score ($\mathrm{PS}$) Celsius Rule:**  Under 2027 Rule `6.b`, $\mathrm{PE} = 1 - |T_f - T_{\mathrm{pred}}|/T_f$ uses $T_f$ in **degrees Celsius** (never Kelvin!).
- **State vs. path functions:**  State functions ($P, T, V, U, H, S, F, G$) depend only on equilibrium state endpoints ($dU$ exact); path functions ($Q, W_{\mathrm{by}}, S_{\mathrm{gen}}$) depend on process trajectory ($\delta Q, \delta W$ inexact).
- **Thermal stratification in 9 oz cup:**  Stable hot-over-cold density profile formed under top-down lamp heating because near-IR radiation is absorbed in the top $10 mm$ of water while downward buoyancy convection is hydrostatically suppressed.
- **Triple point of water ($273.16 K, 611.657 Pa$):**  Unique invariant state ($F = 1 - 3 + 2 = 0$) where ice Ih, liquid water, and water vapor coexist in equilibrium ($T_{\mathrm{tp}} = 0.01 °C$).
