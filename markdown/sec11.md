<!-- Source: src/sec11.tex | Tab: Tab 5: TRANSFER | Target: 8 pp -->
# §11: Convective Heat Transfer, Dimensionless Groups, Dead-Air Gaps, Evaporative Coupling & Top-Layer Thermal Stratification {#sec:11}

> **[SCOPE: REQUIRED | 2027 Rule 5.c.iii (All Levels) & Official National Clarifications #1–#5 (Top-Layer Stratification & Wrap) | Sources:  **[S01]**,  **[S02]**,  **[S09]**,  **[S12]**,  **[S17]**]**

### [FORMULA & DECISION CARD: §11 Master Convection, Dimensionless Scaling, Air-Gap & Evaporative Loss Decision Card  **[S02,S12]**]

| **Formula** | **Variables (SI units)** | **Flags** | **Use when** |
| --- | --- | --- | --- |
| $\dot{Q}_{\mathrm{conv}} = h A \left(T_s - T_\infty\right) = \dfrac{T_s - T_\infty}{R_{\mathrm{conv}}}$ | $\dot{Q}_{\mathrm{conv}}$: convective rate $(W)$; $h$: convection coefficient $(W/m^2/K)$; $A$: wetted surface area $(m^2)$; $R_{\mathrm{conv}} = 1/(hA)$ $(K/W)$ | **[NEWTON]** | Any solid–fluid boundary; evaluate fluid properties at $T_f = \frac{1}{2}(T_s + T_\infty)$ |
| $\mathrm{Nu}_L = \dfrac{h L}{k_{\mathrm{fluid}}} \implies h = \dfrac{k_{\mathrm{fluid}}}{L}\,\mathrm{Nu}_L$ | $\mathrm{Nu}_L$: Nusselt number (dimensionless); $L$: characteristic length $(m)$; $k_{\mathrm{fluid}}$: **fluid** thermal conductivity $(W/m/K)$ | **[CONV-CORE]** | Ratio of convective heat transfer to pure fluid conduction ($\mathrm{Nu}=1$ stagnant slab; $\mathrm{Nu}_D=2$ sphere limit) |
| $\mathrm{Pr} = \dfrac{\nu}{\alpha} = \dfrac{\mu c_p}{k_{\mathrm{fluid}}} \approx \left(\dfrac{\delta_v}{\delta_T}\right)^{\!3}$ | $\nu = \mu/\rho$: kinematic viscosity $(m^2/s)$; $\alpha = k_f/(\rho c_p)$: thermal diffusivity $(m^2/s)$; $\delta_v, \delta_T$: velocity & thermal b.l. thicknesses | **[FLUID-PROP]** | Air ($300 K$): $\mathrm{Pr}=0.713$; liquid water ($27 °C$): $\mathrm{Pr}=5.83$; liquid metals: $\mathrm{Pr}\sim 0.01$ |
| $\mathrm{Re}_L = \dfrac{u_\infty L}{\nu} = \dfrac{\rho u_\infty L}{\mu}$ | $u_\infty$: free-stream flow speed $(m/s)$; $L$: length or pipe diameter $D$ $(m)$ | **[FORCED]** | Forced convection; laminar flat plate $\mathrm{Re}_x < 5×10^{5}$, pipe $\mathrm{Re}_D < 2300$ |
| $\mathrm{Gr}_L = \dfrac{g \beta \|T_s - T_\infty\| L^3}{\nu^2}$ | $g = 9.80665 m/s^2$; $\beta = -\frac{1}{\rho}(\frac{\partial\rho}{\partial T})_P$ $(/K)$ [for ideal gas, $\beta = 1/T_f$ with $T_f$ in $K$!] | **[BUOYANCY]** | Ratio of buoyancy to viscous forces; $\mathrm{Gr}_L / \mathrm{Re}_L^2 \sim 1$ indicates mixed convection |
| $\mathrm{Ra}_L = \mathrm{Gr}_L\,\mathrm{Pr} = \dfrac{g \beta \|T_s - T_\infty\| L^3}{\nu \alpha}$ | $\mathrm{Ra}_L$: Rayleigh number (dimensionless); laminar natural convection has $\mathrm{Nu}_L \propto \mathrm{Ra}_L^{1/4}$ ($h \propto (\Delta T/L)^{1/4}$, $\dot{Q} \propto \Delta T^{5/4}$) | **[NAT-CONV]** | Turbulent natural convection ($\mathrm{Ra}_L \gtrsim 10^9$): $\mathrm{Nu}_L \propto \mathrm{Ra}_L^{1/3}$ ($h$ independent of $L$, $\dot{Q} \propto \Delta T^{4/3}$) |
| $\mathrm{Ra}_\delta = \dfrac{g\beta\Delta T_{\mathrm{gap}}\delta^3}{\nu\alpha} < \mathrm{Ra}_c = 1708$ | $\delta$: enclosed air-gap thickness $(m)$; $\delta_c = \left(\dfrac{1708\,\nu\alpha}{g\beta\Delta T_{\mathrm{gap}}}\right)^{\!1/3} \approx 10–12 mm$ in room air | **[ENCLOSURE]** | Rayleigh–B\'enard criterion: for $\delta \le \delta_c$, air stays stagnant ($\mathrm{Nu}_\delta = 1$, pure conduction $k_{\mathrm{air}}$!) |
| $\dot{Q}_{\mathrm{evap}} = L_v \dot{m}_{\mathrm{evap}} = L_v A_{\mathrm{surf}} g_m \left(m_{\mathrm{H_2O},s} - m_{\mathrm{H_2O},e}\right)$ | $L_v \approx 2430 kJ/kg$ (30 °C); $g_m = \dfrac{\rho_f D_{\mathrm{H_2O,air}}\mathrm{Nu}_{m,D}}{D}$ $(kg/m^2/s)$; $m_{\mathrm{H_2O}} = \rho_{\mathrm{H_2O}}/\rho_{\mathrm{mix}}$ | **[MASS-XFER]** | Open-cup evaporative heat loss (Lienhard §11.7 Ex. 11.11 **[S12]**); suppressed $>95\%$ by BoPET film cap |

## Forced vs. Natural Convection & Boundary-Layer Structure

### Newton's Law of Cooling and Typical Regimes of $h$

Convection is energy transfer between a solid surface at $T_s$ and an adjacent moving fluid at bulk temperature $T_\infty$ through the combined action of molecular thermal conduction at the stationary wall interface ($u_{\mathrm{fluid}}(y=0) = 0$, no-slip boundary condition) and macroscopic fluid advection  **[S12]**. Consequently, the convective heat transfer coefficient $h$ $[W/m^2/K]$ in Newton's law of cooling, $\dot{Q}_{\mathrm{conv}} = h A (T_s - T_\infty)$, is **not a intrinsic thermophysical property of the fluid alone**: it depends on the surface temperature gradient inside the fluid boundary layer, $h = \frac{-k_{\mathrm{fluid}}(\partial T/\partial y)_{y=0}}{T_s - T_\infty} \sim \frac{k_{\mathrm{fluid}}}{\delta_T}$. Per Lienhard Table 1.1 (p. 21  **[S12]**), representative orders of magnitude for $h$ are:
- **Natural (Free) Convection in Air / Gases:** $h \approx 3–20 W/m^2/K$ (around the 2027 collector box and cup in still room air: $h \approx 4–9 W/m^2/K$, comparable to linearized thermal radiation $h_{\mathrm{rad}} = 4\varepsilon\sigma T_m^3 \approx 6 W/m^2/K$!).
- **Forced Convection in Air / Gases:** $h \approx 10–250 W/m^2/K$ (room HVAC draft or fan).
- **Natural Convection in Water / Liquids:** $h \approx 50–1000 W/m^2/K$ (bottom-heated water plume; suppressed when heated from above!).
- **Forced Convection in Water / Liquids:** $h \approx 100\text{--}15000 W/m^2/K$ (stirred probe in water: $h \approx 400\text{--}1200 W/m^2/K$).
- **Phase-Change Boiling or Condensation of Water:** $h \approx 2500–100000 W/m^2/K$.

### Velocity vs. Thermal Boundary Layers and the Role of Prandtl Number ($\mathrm{Pr}$)

As illustrated in Fig. `fig:11:boundary-layer`(a), when a fluid flows along a heated surface of distance $x$ from the leading edge, viscous shear retards the fluid within a **velocity (hydrodynamic) boundary layer** of thickness $\delta_v(x)$, while heat diffuses across a **thermal boundary layer** of thickness $\delta_T(x)$ (Lienhard §6.2–6.5, pp. 292–326  **[S12]**):

$$
\begin{aligned}
\frac{\delta_v(x)}{x} = \frac{4.92}{\sqrt{\mathrm{Re}_x}}, \quad \frac{\delta_T(x)}{\delta_v(x)} \approx \mathrm{Pr}^{-1/3}\ (\mathrm{Pr} \gtrsim 0.6), \quad \mathrm{Nu}_x = 0.332\,\mathrm{Re}_x^{1/2}\mathrm{Pr}^{1/3}, \quad \overline{\mathrm{Nu}}_L = 2\,\mathrm{Nu}_{x=L} = 0.664\,\mathrm{Re}_L^{1/2}\mathrm{Pr}^{1/3}
  
\end{aligned}
$$

Notice that for laminar forced flow over a flat plate, $h_x \propto x^{-1/2}$, so the **average heat transfer coefficient $\bar{h}_L$ over length $[0, L]$ is exactly twice the local coefficient $h_x(L)$ at the trailing edge**! Moreover, the Prandtl number $\mathrm{Pr} = \nu/\alpha$ directly sets the thickness ratio $\delta_v/\delta_T \approx \mathrm{Pr}^{1/3}$:
- **Gases ($\mathrm{Pr} \approx 0.71$):** $\delta_T \approx 1.12\,\delta_v$ (momentum and heat diffuse at nearly identical rates).
- **Liquid Water ($\mathrm{Pr} = 5.83$ at $27 °C$, $4.34$ at $40 °C$  **[S12]**) & Oils ($\mathrm{Pr} \sim 10^2\text{--}10^4$):** $\delta_T \approx 0.56\,\delta_v$ (water) to $0.05\,\delta_v$ (oils) — heat diffuses much more slowly than momentum ($\alpha \ll \nu$), creating a thin thermal boundary layer.
- **Liquid Metals ($\mathrm{Hg}, \mathrm{Na}, \mathrm{Pb\text{-}Bi}$: $\mathrm{Pr} \approx 0.004\text{--}0.025$):** $\delta_T \gg \delta_v$ (free electrons conduct heat far beyond the viscous layer; $\mathrm{Nu}_x = 0.565\,\mathrm{Pe}_x^{1/2}$ where P\'eclet number $\mathrm{Pe}_x = \mathrm{Re}_x\mathrm{Pr} = u_\infty x/\alpha$).

> **[Vector Figure: (a) Hydrodynamic ($\delta_v$) and thermal ($\delta_T$) boundary-layer development along a heated flat plate  **[S12]**. (b) Contrast between unstable bottom heating ($\mathrm{Ra}>0$, full convective mixing) and 2027 top-down near-IR lamp heating ($\mathrm{Ra}<0$, buoyantly stable hot top water layer measured by the ES under Clarifications #1–#4  **[S02]**). | Label: `fig:11:boundary-layer`]**
> - **Diagram Annotations & Key Elements:** (a) Forced Convection Boundary Layers ($\delta_v/\delta_T \approx \mathrm{Pr}^{1/3}$) • Heated Isothermal Flat Plate at $T_s > T_\infty$ ($x=0$ to $x=L$) • $\delta_v(x)$ (Velocity b.l.) • $\delta_T(x)$ (Air, $\mathrm{Pr}=0.71$) • $\delta_T(x)$ (Water, $\mathrm{Pr}=5.8$) • Laminar ($\mathrm{Re}_x < 5×10^{5}$) / [-1pt]$h_x \propto x^{-1/2}$ • Turbulent ($\mathrm{Re}_x > 5×10^{5}$) / [-1pt]$h_x \propto x^{-1/5}$ • (b) Unstable Bottom Heating vs. 2027 Stable Top-Down Lamp Heating • Bottom Hot ($\rho_{\mathrm{bot}} < \rho_{\mathrm{top}}$) • Unstable ($\mathrm{Ra}>0$) / [-1pt]Plumes mix entire cup • BoPET Cap (Clarif. #5: $\dot{Q}_{\mathrm{evap}}\to 0$) • Hot Top Layer ($T_{\mathrm{top}},\; \rho_{\mathrm{top}}$ low) • Cooler Bottom ($\rho_{\mathrm{bot}}$ high) • Buoyantly Stable ($\mathrm{Ra}<0$, Clarif. #1–#4)

## Verified Natural & Forced Convection Correlations (Lienhard Ch. 6–8)

**Table:** Verified Forced and Natural Convection Nusselt Correlations from Lienhard & Lienhard (6th ed., 2024, Chapters 6–8  **[S12]**). All fluid properties are evaluated at film temperature $T_f = (T_s + T_\infty)/2$ except internal pipe flows (evaluated at bulk mean $T_b$).

| **Geometry & Flow Regime** | **Length $L$** | **Verified Nusselt Correlation (Lienhard 6e **[S12]**)** | **Validity & Scaling** |
| --- | --- | --- | --- |
| **Forced Flat Plate** (Laminar, isothermal) | $L = \text{plate length}$ | $\overline{\mathrm{Nu}}_L = 0.664\,\mathrm{Re}_L^{1/2}\mathrm{Pr}^{1/3}$ \quad (Eq. 6.58, p. 319) | $\mathrm{Re}_L < 5×10^{5},\; \mathrm{Pr} \ge 0.6$; $\bar{h} \propto u_\infty^{1/2} L^{-1/2}$ |
| **Forced Flat Plate** (Turbulent, isothermal) | $L = \text{plate length}$ | $\overline{\mathrm{Nu}}_L = 0.037\,\mathrm{Re}_L^{4/5}\mathrm{Pr}^{1/3}$ \quad (Ch. 6, p. 344) | $5×10^{5} < \mathrm{Re}_L < 10^8$; $\bar{h} \propto u_\infty^{4/5} L^{-1/5}$ |
| **Internal Pipe Flow** (Laminar, fully developed) | $D = \text{tube ID}$ | $\mathrm{Nu}_D = 3.657$ (const $T_w$); $\mathrm{Nu}_D = 4.364$ (const $q''_w$) (pp. 371–373) | $\mathrm{Re}_D < 2300$; $h \propto k_f / D$ (independent of $u_m$!) |
| **Internal Pipe Flow** (Turbulent, Dittus–Boelter) | $D = \text{tube ID}$ | $\mathrm{Nu}_D = 0.023\,\mathrm{Re}_D^{0.8}\mathrm{Pr}^n$ ($n=0.4$ heating, $0.3$ cooling, p. 383) | $\mathrm{Re}_D > 10^4,\; 0.7 \le \mathrm{Pr} \le 160$; $h \propto u_m^{0.8} D^{-0.2}$ |
| **Vertical Plate / Cylinder** (Natural convection) | $L = \text{vertical height}$ | $\overline{\mathrm{Nu}}_L = 0.68 + \dfrac{0.670\,\mathrm{Ra}_L^{1/4}}{\left[1 + (0.492/\mathrm{Pr})^{9/16}\right]^{4/9}}$ (Churchill–Chu Eq. 8.13a, p. 422) | $0 < \mathrm{Ra}_L \le 10^9$ (laminar); $\bar{h} \propto (\Delta T/L)^{1/4}$, $\dot{Q} \propto \Delta T^{5/4}$ |
| **Horizontal Cylinder** (Natural convection) | $D = \text{outer diameter}$ | $\overline{\mathrm{Nu}}_D = 0.36 + \dfrac{0.518\,\mathrm{Ra}_D^{1/4}}{\left[1 + (0.559/\mathrm{Pr})^{9/16}\right]^{4/9}}$ (Churchill–Chu Eq. 8.28, p. 430) | $10^{-6} \le \mathrm{Ra}_D \le 10^9$; $\bar{h} \propto (\Delta T/D)^{1/4}$ |
| **Submerged Sphere** (Natural convection) | $D = \text{sphere diameter}$ | $\overline{\mathrm{Nu}}_D = 2 + \dfrac{0.589\,\mathrm{Ra}_D^{1/4}}{\left[1 + (0.492/\mathrm{Pr})^{9/16}\right]^{4/9}}$ (Churchill Eq. 8.33, p. 433) | $\mathrm{Ra}_D < 10^{12}$; pure conduction limit $\lim_{\mathrm{Ra}_D\to 0}\mathrm{Nu}_D = 2$ |
| **Horizontal Plate — Unstable** (Hot top OR cold bottom) | $L^* = \dfrac{A}{P}$ ($D/4$ disk) | $\overline{\mathrm{Nu}}_{L^*} = \dfrac{0.560\,\mathrm{Ra}_{L^*}^{1/4}}{\left[1 + (0.492/\mathrm{Pr})^{9/16}\right]^{4/9}}$ ($\mathrm{Ra}_{L^*} < 10^7$, Eq. 8.37a, p. 436); $\overline{\mathrm{Nu}}_{L^*} = 0.14\,\mathrm{Ra}_{L^*}^{1/3}$ ($\mathrm{Ra}_{L^*} \ge 10^7$, Eq. 8.35) | Buoyant plumes rise off hot surface; for $\mathrm{Ra}^{1/3}$, $\bar{h}$ is independent of $L^*$ ($\dot{Q} \propto \Delta T^{4/3}$) |
| **Horizontal Plate — Stable** (Hot bottom OR cold top) | $D = \text{disk diameter}$ | $\overline{\mathrm{Nu}}_D = 0.82\,\mathrm{Ra}_D^{1/5}\mathrm{Pr}^{0.034}$ (Kadambi–Drake Eq. 8.39, p. 437); 2D plate: $\overline{\mathrm{Nu}}_L = 0.58\,\mathrm{Ra}_L^{1/5}$ (Eq. 8.38) | Stable stratification pins fluid against surface ($\bar{h}$ is $3\text{--}5\times$ smaller than unstable case!) |

### Internal Pipe & Non-Circular Duct Convection, Hydraulic Diameter ($D_h$) and LMTD

For internal flow of mass flow rate $\dot{m} = \rho u_m A_c$ $[kg/s]$ through a duct of cross-sectional area $A_c$, wetted perimeter $P_w$, and heated length $L$ ($A_s = P_w L$, Lienhard Ch. 3 & Ch. 7, pp. 117–134, 366–399  **[S12]**):
- **Hydraulic Diameter ($D_h$):** Used as the characteristic length in $\mathrm{Re}_{D_h} = u_m D_h / \nu$ and $\mathrm{Nu}_{D_h} = h D_h / k_f$ for any non-circular cross-section:
  
$$
\begin{aligned}
D_h \equiv \frac{4 A_c}{P_w} = \begin{cases} D & \text{(circular tube of diameter } D\text{)} \\ a & \text{(square duct of side } a\text{: } 4a^2/(4a) = a\text{)} \\ \dfrac{2ab}{a + b} & \text{(rectangular duct } a\times b\text{; wide parallel plates } b \gg a \implies D_h = 2a\text{)} \\ D_o - D_i = 2(r_o - r_i) & \text{(concentric circular annulus of radii } r_i, r_o\text{)} \end{cases}
    
\end{aligned}
$$

  In fully developed laminar duct flow ($\mathrm{Re}_{D_h} < 2300$), $\mathrm{Nu}_{D_h}$ is a pure geometric constant independent of $\mathrm{Re}_{D_h}$ and $\mathrm{Pr}$ (Lienhard Table 7.1, p. 397  **[S12]**): circular tube $\mathrm{Nu}_D = 3.657$ (const $T_w$) or $4.364$ (const $q''_w$); square duct $\mathrm{Nu}_{D_h} = 2.976$ (const $T_w$) or $3.608$ (const $q''_w$); wide parallel plates $\mathrm{Nu}_{D_h} = 7.541$ (const $T_w$) or $8.235$ (const $q''_w$).
- **Constant Wall Heat Flux ($q''_w = \mathrm{const}$) vs. Constant Wall Temperature ($T_w = \mathrm{const}$) & Log-Mean Temperature Difference ($\mathrm{LMTD}$):**
- *Constant Wall Heat Flux ($q''_w = \mathrm{const}$, e.g., electrical resistance heating):* Both the bulk fluid temperature $T_b(x)$ and wall temperature $T_w(x)$ rise **linearly** at the exact same slope $dT_b/dx = (q''_w P_w)/(\dot{m} c_p)$ once thermally developed ($T_w(x) - T_b(x) = q''_w / h = \mathrm{const}$).
- *Constant Wall Temperature ($T_w = \mathrm{const}$, e.g., condensing steam jacket or isothermal bath):* The temperature difference $\Delta T(x) = T_w - T_b(x)$ decays **exponentially** along the pipe length as the fluid approaches $T_w$:
    
$$
\begin{aligned}
\frac{\Delta T_{\mathrm{out}}}{\Delta T_{\mathrm{in}}} = \frac{T_w - T_{b,\mathrm{out}}}{T_w - T_{b,\mathrm{in}}} = \exp\!\left(-\frac{\bar{h} A_s}{\dot{m} c_p}\right) = e^{-\mathrm{NTU}}, \qquad \dot{Q} = \dot{m} c_p\left(T_{b,\mathrm{out}} - T_{b,\mathrm{in}}\right) = \bar{h} A_s \Delta T_{\mathrm{lm}}
      
\end{aligned}
$$

    where $\mathrm{NTU} = \frac{\bar{h}A_s}{\dot{m}c_p}$ is the Number of Transfer Units and $\Delta T_{\mathrm{lm}}$ is the **Log-Mean Temperature Difference**:
    
$$
\begin{aligned}
\boxed{\Delta T_{\mathrm{lm}} \equiv \frac{\Delta T_{\mathrm{in}} - \Delta T_{\mathrm{out}}}{\ln\!\left(\Delta T_{\mathrm{in}} / \Delta T_{\mathrm{out}}\right)} = \frac{T_{b,\mathrm{out}} - T_{b,\mathrm{in}}}{\ln\!\left(\dfrac{T_w - T_{b,\mathrm{in}}}{T_w - T_{b,\mathrm{out}}}\right)} \le \Delta T_{\mathrm{arith}} = \frac{\Delta T_{\mathrm{in}} + \Delta T_{\mathrm{out}}}{2}}
      
\end{aligned}
$$

  

## Enclosed Dead-Air Gaps ($\delta_{\mathrm{opt}} = 10–12 mm$) & Open-Cup Evaporative Loss

### Why $10–12 mm$ Foil-Bounded Air Gaps Outperform Prohibited Styrofoam

Consider an air layer of thickness $\delta$ trapped between two surfaces at $T_1$ and $T_2$ ($\Delta T_{\mathrm{gap}} = T_1 - T_2$). Across this gap, heat is transferred by three parallel mechanisms: gas conduction, cellular natural convection, and surface-to-surface thermal radiation:

$$
\begin{aligned}
q''_{\mathrm{gap}}(\delta) = \mathrm{Nu}_\delta(\mathrm{Ra}_\delta)\,\frac{k_{\mathrm{air}}\Delta T_{\mathrm{gap}}}{\delta} + \frac{\sigma(T_1^4 - T_2^4)}{\frac{1}{\varepsilon_1} + \frac{1}{\varepsilon_2} - 1} \approx \underbrace{\left(\mathrm{Nu}_\delta\,k_{\mathrm{air}} + h_{\mathrm{rad}}\,\delta\right)}_{k_{\mathrm{eff}}(\delta)}\frac{\Delta T_{\mathrm{gap}}}{\delta}
  
\end{aligned}
$$
- **Rayleigh–B\'enard Convection Onset ($\mathrm{Ra}_c = 1708$):** When a horizontal fluid layer is heated from below, viscous shear prevents cellular overturning so long as $\mathrm{Ra}_\delta = \frac{g\beta\Delta T_{\mathrm{gap}}\delta^3}{\nu\alpha} < \mathrm{Ra}_c = 1708$ ($\mathrm{Nu}_\delta = 1.00$, pure stagnant conduction!). Once $\delta > \delta_c = \left(\frac{1708\,\nu\alpha}{g\beta\Delta T_{\mathrm{gap}}}\right)^{1/3}$, B\'enard convection rolls form ($\mathrm{Nu}_\delta \approx 0.069\,\mathrm{Ra}_\delta^{1/3}\mathrm{Pr}^{0.074} \propto \delta$), so making a single air gap wider than $\delta_c \approx 11 mm$ provides **zero additional convective resistance** (plotted in Fig. `fig:11:air-gap-evap`a)!
- **Foil Radiation Suppression:** In an unlined cardboard air gap ($\varepsilon_1 = \varepsilon_2 = 0.92$), $h_{\mathrm{rad}} \approx 5.4 W/m^2/K$, which is **double** the conductive conductance $k_{\mathrm{air}}/\delta = 2.62 W/m^2/K$ at $\delta = 10 mm$! Lining the gap walls with household aluminum foil ($\varepsilon = 0.04$) drops $h_{\mathrm{rad}}$ by $41.7\times$ to $0.13 W/m^2/K$, yielding an effective conductivity $k_{\mathrm{eff}} = 0.0265 + (0.131)(0.010) = \mathbf{0.0278 W/m/K}$ — lower than banned expanded polystyrene ($0.035 W/m/K$  **[S02,S12]**) with $20\times$ lower thermal mass!

### Open-Cup Evaporative Mass-Transfer Heat Loss (Lienhard §11.7 Example 11.11)

Per Lienhard §11.7 (pp. 662–664  **[S12]**), an uncovered cup of warm water at surface temperature $T_s$ in ambient room air at $T_e$ and relative humidity $\mathrm{RH}$ loses latent heat rapidly because saturated water vapor above the surface ($P_{\mathrm{H_2O},s} = P_{\mathrm{sat}}(T_s)$) has lower molar mass ($M_w = 18.015 kg/kmol$) than dry air ($M_a = 28.965 kg/kmol$), driving upward buoyant mass transfer:

$$
\begin{aligned}
\rho_{\mathrm{H_2O}} = \frac{P_{\mathrm{H_2O}} M_w}{R_u T}, \qquad \rho_{\mathrm{air}} = \frac{(P_{\mathrm{atm}} - P_{\mathrm{H_2O}}) M_a}{R_u T}, \qquad m_{\mathrm{H_2O}} = \frac{\rho_{\mathrm{H_2O}}}{\rho_{\mathrm{H_2O}} + \rho_{\mathrm{air}}}
  
\end{aligned}
$$

$$
\begin{aligned}
g_m = \frac{\rho_f D_{\mathrm{H_2O,air}}\,\mathrm{Nu}_{m,D}}{D_{\mathrm{surf}}}, \qquad \dot{m}_{\mathrm{evap}} = A_{\mathrm{surf}}\,g_m\left(m_{\mathrm{H_2O},s} - m_{\mathrm{H_2O},e}\right), \qquad \dot{Q}_{\mathrm{evap}} = L_v\,\dot{m}_{\mathrm{evap}}
  
\end{aligned}
$$

As shown in Fig. `fig:11:air-gap-evap`(b), for the 2027 9 oz cup ($A_{\mathrm{surf}} = 36.0 cm^2$) at $T_s = 40 °C$–$50 °C$, **evaporation accounts for $73\text{--}83\%$ of all top-surface heat loss** ($\dot{Q}_{\mathrm{evap}} = 2.22–4.45 W$ vs. $\dot{Q}_{\mathrm{conv}} \approx 0.42 W$ and $\dot{Q}_{\mathrm{rad}} \approx 0.40 W$), removing $1330–2670 J$ directly from the top water layer over a $10 min$ run!

> **[Vector Figure: (a) Heat flux across an enclosed air gap ($\Delta T = 15 K$) versus gap width $\delta$, showing the Rayleigh–B\'enard onset knee at $\delta_c = 10.9 mm$ ($\mathrm{Ra}_c = 1708$) and the $41.7\times$ radiation reduction of aluminum foil walls. (b) Uncovered 9 oz cup top-surface heat losses versus water surface temperature $T_s$ (Lienhard §11.7  **[S12]**), demonstrating why evaporation dominates and why a removable BoPET cap (Clarification #5  **[S02]**) saves $2–4 W$. | Label: `fig:11:air-gap-evap`]**
> - **Diagram Annotations & Key Elements:** **Title:** **(a) Dead-Air Gap Flux vs. Thickness $\delta$** • **Title:** **(b) Uncovered 9 oz Cup Top Losses vs. $T_s$** • **X-Axis:** Enclosed Air-Gap Thickness $\delta$ $(mm)$ ($\Delta T_{\mathrm{gap}} = 15 K$) • **X-Axis:** Top Water Surface Temperature $T_s$ $(^\circ\mathrm{C})$ ($T_{\mathrm{room}}=22 °C,\; 50\%\ \mathrm{RH}$) • **Y-Axis:** Gap Heat Flux $q''_{\mathrm{gap}}$ $(W/m^2)$ • **Y-Axis:** Top-Surface Heat Loss $\dot{Q}$ $(W)$ • **Legend:** Cardboard ($\varepsilon=0.92$) • **Legend:** Al-Foil Gap ($\varepsilon=0.04$) • **Legend:** $\dot{Q}_{\mathrm{evap}}$ (Uncovered) • **Legend:** $\dot{Q}_{\mathrm{conv,top}}$ • **Legend:** $\dot{Q}_{\mathrm{rad,top}}$ ($\varepsilon_w=0.96$) • **Legend:** $\dot{Q}_{\mathrm{tot}}$ w/ BoPET Cap • $\delta_c = 10.9 mm$ ($\mathrm{Ra}_c=1708$)

## Worked Competition Examples (§11)

### Worked Example — Natural Convection Loss from a Vertical Collector Wall (Churchill–Chu) `[Lienhard Eq. 8.13a  **[S12]**]`

A vertical side wall of a $30.0\times 30.0\times30.0 cm$ collector ($L = 0.300 m$, width $W = 0.300 m$, $A = 0.0900 m^2$) has outer surface temperature $T_s = 37.0 °C$ in still room air at $T_\infty = 23.0 °C$. At the film temperature $T_f = 30.0 °C$ ($303.15 K$), air has $\nu = 1.60×10^{-5} m^2/s$, $\alpha = 2.25×10^{-5} m^2/s$, $\mathrm{Pr} = 0.711$, and $k_f = 0.0265 W/m/K$. Compute (a) $\mathrm{Ra}_L$, (b) $\overline{\mathrm{Nu}}_L$ and $\bar{h}$, (c) convective heat loss $\dot{Q}_{\mathrm{conv}}$, and (d) the new heat loss if $\Delta T$ doubles to $28.0 K$.
\tcblower
**Solution.** (a) Treating air as an ideal gas at $T_f = 303.15 K$, $\beta = 1/T_f = 3.2987×10^{-3} /K$ and $\Delta T = 37.0 - 23.0 = 14.0 K$:

$$
\mathrm{Ra}_L = \frac{g\beta\Delta T L^3}{\nu\alpha} = \frac{(9.80665)(3.2987×10^{-3})(14.0)(0.300)^3}{(1.60×10^{-5})(2.25×10^{-5})} = \mathbf{3.397×10^{7}} < 10^9 \quad (\text{laminar})
$$

(b) By Churchill and Chu (Table `tab:11:correlations`):

$$
\overline{\mathrm{Nu}}_L = 0.68 + \frac{0.670(3.3967×10^{7})^{1/4}}{\left[1 + (0.492/0.711)^{9/16}\right]^{4/9}} = 0.68 + \frac{50.888}{1.2768} = \mathbf{40.54}, \qquad
  \bar{h} = \frac{k_f}{L}\overline{\mathrm{Nu}}_L = \frac{0.0265}{0.300}(40.54) = \mathbf{3.581 W/m^2/K}
$$

(c) Convective heat loss: $\dot{Q}_{\mathrm{conv}} = \bar{h} A \Delta T = (3.581)(0.0900)(14.0) = \mathbf{4.51 W}$ (or $4.45 W$ using exact unrounded $\mathrm{Nu}_L - 0.68$ scaling).\\
(d) Since laminar natural convection scales as $h \propto \Delta T^{1/4}$ ($\dot{Q} \propto \Delta T^{5/4}$), doubling $\Delta T$ increases $\dot{Q}$ by $2^{5/4} = \mathbf{2.378\times}$ (to $10.6 W$), *not* $2.0\times$!

**✓ Verified by:** Evaluated in `check_sec10_13.py` (`EX-11.1-RAL`, `EX-11.1-Q`): $\mathrm{Ra}_L = 3.3967×10^{7}$, $\dot{Q}_{\mathrm{conv}} = 4.446 W$.

### Worked Example — Rayleigh–B\'enard Critical Air-Gap Thickness & Foil Baffle Conductance `[2027 Device Insulation]`

An air space beneath the 9 oz cup cradle has mean air temperature $T_f = 305.0 K$ ($\beta = 1/305.0 = 3.2787×10^{-3} /K,\; \nu = 1.62×10^{-5} m^2/s,\; \alpha = 2.28×10^{-5} m^2/s,\; k_{\mathrm{air}} = 0.0265 W/m/K$) and temperature difference $\Delta T_{\mathrm{gap}} = 15.0 K$ across one gap. Find (a) the maximum gap thickness $\delta_c$ before Rayleigh–B\'enard cellular convection begins ($\mathrm{Ra}_c = 1708$), and (b) the effective thermal conductivity $k_{\mathrm{eff}}$ of a $\delta = 10.0 mm$ gap lined on both sides with household aluminum foil ($\varepsilon = 0.04$).
\tcblower
**Solution.** (a) Inverting $\mathrm{Ra}_\delta = \frac{g\beta\Delta T_{\mathrm{gap}}\delta_c^3}{\nu\alpha} = 1708$:

$$
\delta_c = \left(\frac{1708\,\nu\alpha}{g\beta\Delta T_{\mathrm{gap}}}\right)^{\!1/3} = \left(\frac{1708(1.62×10^{-5})(2.28×10^{-5})}{(9.80665)(1/305.0)(15.0)}\right)^{\!1/3} = \mathbf{10.94 mm}
$$

(b) At $\delta = 10.0 mm < \delta_c$, air is 100% stagnant ($\mathrm{Nu}_\delta = 1.00$). With foil boundaries ($\varepsilon_1 = \varepsilon_2 = 0.04$ at $T_m = 305 K$), the linearized radiative conductance across the gap is $h_{\mathrm{rad,foil}} = \frac{4\sigma T_m^3}{2/\varepsilon - 1} = \frac{4(5.6704×10^{-8})(305.0)^3}{49.0} = 0.1312 W/m^2/K$:

$$
k_{\mathrm{eff}} = k_{\mathrm{air}} + h_{\mathrm{rad,foil}}\,\delta = 0.0265 + (0.1312)(0.0100) = \mathbf{0.02781 W/m/K}
$$

**✓ Verified by:** Checked in `check_sec10_13.py` (`EX-11.2-DELTAC`, `EX-11.2-KEFF`): $\delta_c = 10.936 mm$, $k_{\mathrm{eff}} = 0.027813 W/m/K$.

### Worked Example — Open-Cup Evaporative Mass-Transfer Heat Loss vs. Removable Glazing Cap `[Lienhard Ex. 11.11 & Clarif. #5  **[S02,S12]**]`

During a 2027 collector test, the top water surface in an uncovered 9 oz cup ($D_{\mathrm{surf}} = 6.77 cm,\; A_{\mathrm{surf}} = 3.60×10^{-3} m^2$) reaches $T_s = 40.0 °C$ ($313.15 K$, saturation vapor pressure $P_{\mathrm{sat}} = 7384 Pa$, latent heat $L_v = 2406 kJ/kg$  **[S09]**) in ambient room air at $T_e = 22.0 °C$ ($295.15 K$), $50.0%\ \mathrm{RH}$ ($P_{\mathrm{H_2O},e} = 1322 Pa$), and $P_{\mathrm{atm}} = 101325 Pa$. Given convective mass transfer conductance $g_m = 6.65×10^{-3} kg/m^2/s$, calculate (a) the surface and ambient water-vapor mass fractions $m_{\mathrm{H_2O},s}$ and $m_{\mathrm{H_2O},e}$, (b) the evaporation rate $\dot{m}_{\mathrm{evap}}$ and evaporative heat loss $\dot{Q}_{\mathrm{evap}}$, and (c) the temperature penalty over a $10.0 min$ ($600 s$) run on the top stratified water layer ($C_{\mathrm{top}} = 215 J/K$).
\tcblower
**Solution.** (a) Using Eq. Eq. (`eq:11:mass-fraction`) with $R_u = 8314.46 J/kmol/K$, $M_w = 18.0153$, and $M_a = 28.965$:
{$$
\begin{aligned}
T_s = 313.15 K:\; \rho_{\mathrm{H_2O},s} &= \frac{(7384)(18.0153)}{(8314.46)(313.15)} = 0.05109 kg/m^3,\;
  \rho_{\mathrm{air},s} = \frac{(101325 - 7384)(28.965)}{(8314.46)(313.15)} = 1.0450 kg/m^3 \Rightarrow m_{\mathrm{H_2O},s} = \mathbf{0.04661} \\
  T_e = 295.15 K:\; \rho_{\mathrm{H_2O},e} &= \frac{(1322)(18.0153)}{(8314.46)(295.15)} = 0.009704 kg/m^3,\;
  \rho_{\mathrm{air},e} = \frac{(101325 - 1322)(28.965)}{(8314.46)(295.15)} = 1.1802 kg/m^3 \Rightarrow m_{\mathrm{H_2O},e} = \mathbf{0.008155}
\end{aligned}
$$

(b) By Eq. Eq. (`eq:11:qevap-full`), with $\Delta m_{\mathrm{H_2O}} = 0.04661 - 0.008155 = 0.03846$:

$$
\dot{m}_{\mathrm{evap}} = (3.60×10^{-3} m^2)(6.65×10^{-3} kg/m^2/s)(0.03846) = \mathbf{9.206×10^{-7} kg/s} = 0.921 mg/s \quad (0.552 g\text{ in }10 min)
$$

$$
\dot{Q}_{\mathrm{evap}} = L_v\,\dot{m}_{\mathrm{evap}} = (2.406×10^{6} J/kg)(9.206×10^{-7} kg/s) = \mathbf{2.215 W}
$$

(c) Over $600 s$, evaporation removes $E_{\mathrm{evap}} = (2.215 W)(600 s) = 1329 J$, depressing the top stratified layer ($C_{\mathrm{top}} = 215 J/K$) by $\Delta T_{\mathrm{loss}} = \frac{1329}{215} = \mathbf{6.18 °C}$! Resting a clear BoPET film cap over the cup mouth (`Clarification #5`) traps saturated vapor ($\Delta m_{\mathrm{H_2O}} \to 0$) and recovers this entire loss.

**✓ Verified by:** Checked in `check_sec10_13.py` (`EX-11.3-QEVAP`): $\dot{Q}_{\mathrm{evap}} = 2.2150 W$.

### Worked Example — Top-Down Stratified Heating Advantage Under Official Clarifications #1–#4 `[2027 Scoring Core  **[S02]**]`

During a $10.0 min$ heating run, a collector delivers $E_{\mathrm{net}} = 5400 J$ of net retained thermal energy to the $100.0 mL$ water ($m_{\mathrm{tot}} = 100.0 g,\; c_p = 4.184 J/g/K,\; C_{\mathrm{bulk}} = 418.4 J/K$) starting at $T_{\mathrm{start}} = 21.0 °C$. Because near-IR lamp radiation is absorbed from above ($\mathrm{Ra} < 0$, buoyantly stable), $72.4%$ of the energy ($3910 J$) is absorbed directly in the upper $45.0 mL$ layer ($C_{\mathrm{top}} = 188.28 J/K$) while $27.6%$ ($1490 J$) reaches the lower $55.0 mL$ layer ($C_{\mathrm{bot}} = 230.12 J/K$), and internal water conduction transfers $E_{\mathrm{cond,down}} = 690 J$ from top to bottom. Compare the ES-measured top-layer temperature gain $\mathrm{TG}_{\mathrm{top}}$ (unstirred per Clarifications #1–#4) against the bulk temperature gain $\mathrm{TG}_{\mathrm{bulk}}$ if a competitor accidentally swirls the cup while removing it!
\tcblower
**Solution.** Net energy retained in the top $45.0 mL$ layer is $E_{\mathrm{top}} = 3910 - 690 = 3220 J$, while the bottom $55.0 mL$ layer gains $E_{\mathrm{bot}} = 1490 + 690 = 2180 J$ ($E_{\mathrm{top}} + E_{\mathrm{bot}} = 5400 J$):

$$
\mathrm{TG}_{\mathrm{top}} = \frac{E_{\mathrm{top}}}{C_{\mathrm{top}}} = \frac{3220 J}{188.28 J/K} = \mathbf{+17.10 °C} \quad (T_{f,\mathrm{top}} = 38.10 °C), \qquad
  \mathrm{TG}_{\mathrm{bot}} = \frac{2180 J}{230.12 J/K} = +9.47 °C
$$

If the competitor accidentally swirls or shakes the cup during removal (violating Clarifications #1–#3 and mixing the layers), the water equalizes to $\mathrm{TG}_{\mathrm{bulk}} = \frac{5400}{418.4} = \mathbf{+12.91 °C}$ ($T_{f,\mathrm{bulk}} = 33.91 °C$) — **destroying $4.19 °C$ ($24.5%$) of their Temperature Score $\mathrm{TS}$ AND ruining their Prediction Score $\mathrm{PS}$!**

**✓ Verified by:** First-law enthalpy check in `check_sec10_13.py` (`EX-11.4-STRAT`, `EX-11.4-ECONS`): $C_{\mathrm{top}}\mathrm{TG}_{\mathrm{top}} + C_{\mathrm{bot}}\mathrm{TG}_{\mathrm{bot}} = 5400.00 J$.

### Worked Example — Mixed Convection Criterion ($\mathrm{Gr}_L/\mathrm{Re}_L^2$) Under Room HVAC Drafts `[Lienhard Eq. 8.45  **[S12]**]`

If a tournament testing table sits beneath a room air-conditioning vent producing a gentle horizontal draft $u_\infty = 0.250 m/s$ across the vertical wall of Worked Example `ex:11.1` ($L = 0.300 m,\; \nu = 1.60×10^{-5} m^2/s,\; \mathrm{Ra}_L = 3.397×10^{7},\; \mathrm{Pr} = 0.711$), evaluate $\mathrm{Gr}_L / \mathrm{Re}_L^2$ and determine whether forced convection can be neglected.
\tcblower
**Solution.** $\mathrm{Gr}_L = \frac{\mathrm{Ra}_L}{\mathrm{Pr}} = \frac{3.3967×10^{7}}{0.711} = 4.777×10^{7}$, and $\mathrm{Re}_L = \frac{u_\infty L}{\nu} = \frac{(0.250)(0.300)}{1.60×10^{-5}} = \mathbf{4687.5}$:

$$
\frac{\mathrm{Gr}_L}{\mathrm{Re}_L^2} = \frac{4.777×10^{7}}{(4687.5)^2} = \frac{4.777×10^{7}}{2.197×10^{7}} = \mathbf{2.174} \sim \mathcal{O}(1)
$$

Because $\mathrm{Gr}_L/\mathrm{Re}_L^2 = 2.17$ is of order unity ($0.1 < \mathrm{Gr}_L/\mathrm{Re}_L^2 < 10$), **neither natural nor forced convection can be neglected** (mixed convection applies: $\mathrm{Nu}_{\mathrm{mixed}}^3 \approx \mathrm{Nu}_{\mathrm{forced}}^3 + \mathrm{Nu}_{\mathrm{nat}}^3$). Enclosing the collector sides within the full $30.0 cm$ outer shell shields the internal cup completely from room HVAC drafts!

**✓ Verified by:** Checked in `check_sec10_13.py` (`EX-11.5-MIXED`): $\mathrm{Gr}_L/\mathrm{Re}_L^2 = 2.1742$.

### Worked Example — Internal Pipe Flow Exponential Approach & Log-Mean Temperature Difference (LMTD) `[Lienhard §7.4  **[S12]**]`

Water ($c_p = 4180 J/kg/K$) flows at $\dot{m} = 0.0200 kg/s$ through a circular tube of inner diameter $D = 15.0 mm$ and length $L = 1.20 m$ whose inner wall is maintained at constant temperature $T_w = 80.0 °C$ by condensing steam. If the water enters at $T_{b,\mathrm{in}} = 20.0 °C$ and the internal convection coefficient is $\bar{h} = 1850 W/m^2/K$, compute (a) the outlet water bulk temperature $T_{b,\mathrm{out}}$, (b) the total heat transfer rate $\dot{Q}$ via First-Law enthalpy balance, and (c) verify $\dot{Q} = \bar{h} A_s \Delta T_{\mathrm{lm}}$ and compare $\Delta T_{\mathrm{lm}}$ against the naive arithmetic mean $\Delta T_{\mathrm{arith}}$.
\tcblower
**Solution.** (a) Internal surface area is $A_s = \pi D L = \pi(0.0150)(1.20) = 0.056549 m^2$, and stream heat-capacity rate is $\dot{m}c_p = (0.0200)(4180) = 83.60 W/K$. Number of Transfer Units: $\mathrm{NTU} = \dfrac{\bar{h}A_s}{\dot{m}c_p} = \dfrac{(1850)(0.056549)}{83.60} = \mathbf{1.2514}$. By Eq. Eq. (`eq:11:pipe-lmtd`):

$$
T_{b,\mathrm{out}} = T_w - \left(T_w - T_{b,\mathrm{in}}\right)e^{-\mathrm{NTU}} = 80.0 - (80.0 - 20.0)e^{-1.25143} = 80.0 - 60.0(0.28609) = \mathbf{62.83 °C}
$$

(b) By the First Law: $\dot{Q} = \dot{m}c_p(T_{b,\mathrm{out}} - T_{b,\mathrm{in}}) = (83.60)(62.835 - 20.00) = \mathbf{3581 W}$.\\
(c) End temperature differences are $\Delta T_{\mathrm{in}} = 80.0 - 20.0 = 60.0 K$ and $\Delta T_{\mathrm{out}} = 80.0 - 62.835 = 17.165 K$. By Eq. Eq. (`eq:11:lmtd-boxed`):

$$
\Delta T_{\mathrm{lm}} = \frac{60.0 - 17.165}{\ln(60.0 / 17.165)} = \frac{42.835}{1.25143} = \mathbf{34.23 K} \quad \left(\text{vs.\ } \Delta T_{\mathrm{arith}} = \frac{60.0 + 17.165}{2} = 38.58 K,\ +12.7\%\text{ error!}\right)
$$

Multiplying $\bar{h}A_s\Delta T_{\mathrm{lm}} = (1850)(0.056549)(34.230) = \mathbf{3581 W}$, identical to the First-Law balance!

**✓ Verified by:** Checked in `check_sec10_13.py` (`EX-11.6-LMTD`): $\dot{Q} = 3580.87 W$ by both methods ($\text{rel\_err} = 0.00$).

### Worked Example — Horizontal Heated Disk: Unstable Upward-Facing vs. Stable Downward-Facing `[Lienhard §8.4  **[S12]**]`

A flat horizontal circular plate of diameter $D = 16.0 cm$ ($0.160 m$) is heated to $T_s = 57.0 °C$ in still room air at $T_\infty = 23.0 °C$ ($\Delta T = 34.0 K$; at $T_f = 40.0 °C = 313.15 K$, air has $\beta = 1/313.15 = 3.1934×10^{-3} /K$, $\nu = 1.70×10^{-5} m^2/s$, $\alpha = 2.40×10^{-5} m^2/s$, $\mathrm{Pr} = 0.708$, $k_f = 0.0272 W/m/K$). Compare the natural convection coefficient $\bar{h}_{\mathrm{up}}$ on the upward-facing hot surface (unstable plumes, Eq. 8.37a with $L^* = A/P = D/4 = 0.0400 m$) against $\bar{h}_{\mathrm{down}}$ on the downward-facing hot surface (stable stratification, Eq. 8.39 with $D = 0.160 m$).
\tcblower
**Solution.** Diameter-based Rayleigh number is $\mathrm{Ra}_D = \frac{(9.80665)(1/313.15)(34.0)(0.160)^3}{(1.70×10^{-5})(2.40×10^{-5})} = \mathbf{1.0695×10^{7}}$, and $L^*$-based Rayleigh number ($L^* = D/4$) is $\mathrm{Ra}_{L^*} = \mathrm{Ra}_D / 4^3 = \mathrm{Ra}_D / 64 = \mathbf{1.6711×10^{5}}$.
- **Upward-Facing Hot Surface (Unstable, Table `tab:11:correlations` Eq. 8.37a):**
  
$$
\overline{\mathrm{Nu}}_{L^*} = \frac{0.560(1.6711×10^{5})^{1/4}}{\left[1 + (0.492/0.708)^{9/16}\right]^{4/9}} = \frac{11.332}{1.3045} = \mathbf{8.686} \implies
    \bar{h}_{\mathrm{up}} = \frac{k_f}{L^*}\overline{\mathrm{Nu}}_{L^*} = \frac{0.0272}{0.0400}(8.686) = \mathbf{5.907 W/m^2/K}
$$
- **Downward-Facing Hot Surface (Stable, Table `tab:11:correlations` Eq. 8.39):**
  
$$
\overline{\mathrm{Nu}}_D = 0.82(1.0695×10^{7})^{1/5}(0.708)^{0.034} = \mathbf{20.630} \implies
    \bar{h}_{\mathrm{down}} = \frac{k_f}{D}\overline{\mathrm{Nu}}_D = \frac{0.0272}{0.160}(20.630) = \mathbf{3.507 W/m^2/K}
$$

Stable gravitational stratification reduces convective heat transfer on the downward-facing hot surface by $\mathbf{1.68\times}$!

**✓ Verified by:** Checked in `check_sec10_13.py` (`EX-11.7-H-UP`, `EX-11.7-H-DOWN`): $\bar{h}_{\mathrm{up}} = 5.9067 W/m^2/K$, $\bar{h}_{\mathrm{down}} = 3.5071 W/m^2/K$.

## Convection Traps, Diagnostics & 2027 Stratification Playbook

### [TRAP & DIAGNOSTIC: Top Convection & Mass-Transfer Traps on Science Olympiad Exams]

| **Wrong move / Symptom** | **What it produces / Why it fails** | **5-second diagnostic & fix** |
| --- | --- | --- |
| **1. Using solid conductivity $k_{\mathrm{solid}}$ inside $\mathrm{Nu} = hL/k_{\mathrm{fluid}}$ (or $k_{\mathrm{fluid}}$ inside $\mathrm{Bi} = hL_c/k_{\mathrm{solid}}$)** | Mixes up fluid boundary-layer convection ($\mathrm{Nu}$) with internal solid temperature uniformity ($\mathrm{Bi}$) (Lienhard p. 23 **[S12]**). | Memory lock: $\mathrm{Nu}$ = **N**ewton fluid ($k_{\mathrm{fluid}}$); $\mathrm{Bi}$ = **B**ody internal ($k_{\mathrm{body}}$). |
| **2. Plugging Celsius $T_f$ into ideal-gas expansion coefficient $\beta = 1/T_f$** | Overestimates $\beta$ and $\mathrm{Ra}_L$ by $\sim 10\times$ at $25 °C$! | Always convert $T_f$ to absolute Kelvin: $\beta_{\mathrm{gas}} = \frac{1}{T_f(K)}$. |
| **3. Assuming natural convection heat loss $\dot{Q}$ scales linearly with $\Delta T$** | Because $h_{\mathrm{nat}} \propto \Delta T^{1/4}$ (laminar) or $\Delta T^{1/3}$ (turbulent), $\dot{Q} = hA\Delta T$ scales as $\Delta T^{5/4}$ or $\Delta T^{4/3}$! | If $\Delta T$ doubles in laminar natural convection, $\dot{Q}$ multiplies by $2^{5/4} = 2.378\times$. |
| **4. Making a single insulation air gap wider than $15 mm$** | Triggers Rayleigh–B\'enard cellular convection ($\mathrm{Ra}_\delta > 1708$), circulating heat across the cavity. | Subdivide wide cavities with aluminum-foil baffles into $10–12 mm$ stagnant cells. |

### [2027 OFFICIAL RULE / CLARIFICATION: 2027 Official Clarifications #1–#5: Zero Stirring, Top-Layer Probe & Removable Glazing  **[S02,S05]**]

- **Clarifications #1–#3 (`09/30/2026`–`10/06/2026`):** *“No, the water will not be stirred or swirled before taking the temperature... No, the water must not be swirled, shaken or stirred before taking the temperature.”*
- **Clarification #4 (`10/06/2026`):** *“It is recommended that the ES should measure the temperature of the top layer of water near the center of the cup. If the thermometer has a probe, the ES should insert it far enough into the water to take an accurate measurement, but no farther.”*
- **Clarification #5 (`10/21/2026`) & Official ES Guide:** Teams may rest a transparent vapor barrier / glazing cover (such as a $25 µm$ clear BoPET disk or LDPE wrap mounted on an upper gravity ring) on or around the cup during Water Setup Time, provided **zero adhesives, tapes, rubber bands, or clips attach it to the cup**, cup shape is unaltered, and the cover is completely removed before final temperature measurement.

## Rapid Competition Problem & Solution Bank (§11)

#### Problem P11.1: Boundary-Layer Scaling Along a Laminar vs. Turbulent Flat Plate `[§11.1 | 5.c.iii | State / National | 60 s | Power-Law Ratio | Trap: assuming $\bar{h}_L = h_x(L)$ instead of $2 h_x(L)$]`

Air ($\mathrm{Pr} = 0.71$) flows at free-stream speed $u_\infty = 4.00 m/s$ over an isothermal flat plate of length $L = 0.400 m$ ($\nu = 1.60×10^{-5} m^2/s$, $k_f = 0.0265 W/m/K$). (a) Verify that the boundary layer is laminar over the entire plate and compute both the trailing-edge local convection coefficient $h_x(L)$ and the plate-averaged coefficient $\bar{h}_L$. (b) If the plate length is quadrupled to $4L$ while remaining laminar, by what factor does the total heat transfer rate $\dot{Q}$ change?

**Solution P11.1:** 
(a) At $x = L = 0.400 m$, $\mathrm{Re}_L = \dfrac{u_\infty L}{\nu} = \dfrac{(4.00)(0.400)}{1.60×10^{-5}} = \mathbf{1.00×10^{5} < 5×10^{5}}$ (100% laminar). By Eq. Eq. (`eq:11:blasius-pohlhausen`):

$$
\mathrm{Nu}_{x=L} = 0.332(1.00×10^{5})^{1/2}(0.71)^{1/3} = 0.332(316.23)(0.8921) = \mathbf{93.66} \implies
  h_x(L) = \frac{0.0265}{0.400}(93.66) = \mathbf{6.205 W/m^2/K}
$$

The plate-averaged coefficient is exactly twice the trailing-edge value: $\bar{h}_L = 2 h_x(L) = \mathbf{12.41 W/m^2/K}$ ($\overline{\mathrm{Nu}}_L = 187.3$).\\
(b) Since $\bar{h}_L \propto L^{-1/2}$ while surface area $A = W L \propto L^1$, total heat flow scales as $\dot{Q} = \bar{h}_L A \Delta T \propto L^{1/2}$: quadrupling $L$ multiplies total heat transfer by $4^{1/2} = \mathbf{2.00\times}$ (the upstream half $[0, 2L]$ transfers $\frac{1}{\sqrt{2}} = 70.7\%$ of the heat!).

#### Problem P11.2: Microgravity / Small-Sphere Conduction Limit ($\mathrm{Nu}_D \to 2$) `[§11.2 | 5.c.iii | National / MIT | 60 s | Asymptotic Limit | Trap: using cylinder correlation with lead constant 0.36 instead of 2]`

A spherical water droplet of diameter $D = 0.500 mm$ is suspended in still air ($k_{\mathrm{air}} = 0.0262 W/m/K$) under microgravity conditions ($g \to 0 \implies \mathrm{Ra}_D \to 0$, Lienhard §8.4 Eq. 8.31, p. 433  **[S12]**). What is the exact asymptotic Nusselt number $\mathrm{Nu}_D$ and convective/conductive heat transfer coefficient $h$ of the droplet?

**Solution P11.2:** 
As $\mathrm{Ra}_D \to 0$, buoyant motion vanishes and steady radial heat transfer into the infinite surrounding air medium occurs by pure 3-D spherical conduction ($R_{\mathrm{sph},\infty} = \lim_{r_o\to\infty}\frac{r_o - r_i}{4\pi k_{\mathrm{air}}r_i r_o} = \frac{1}{4\pi k_{\mathrm{air}}r_i} = \frac{1}{2\pi k_{\mathrm{air}}D}$). Equating $\dot{Q} = h(\pi D^2)\Delta T = 2\pi k_{\mathrm{air}}D\Delta T$ gives the exact lower bound for any sphere (Table `tab:11:correlations`):

$$
\lim_{\mathrm{Ra}_D \to 0} \mathrm{Nu}_D = \mathbf{2.000}, \qquad h = \frac{2 k_{\mathrm{air}}}{D} = \frac{2(0.0262 W/m/K)}{0.000500 m} = \mathbf{104.8 W/m^2/K}
$$

(Notice how small diameter $D = 0.5 mm$ creates a huge heat transfer coefficient $h = 104.8 W/m^2/K$ even with zero air flow!).

#### Problem P11.3: Dittus–Boelter Turbulent Pipe Flow Velocity & Diameter Scaling `[§11.2 | 5.c.iii | State / National | 60 s | Exponents | Trap: forgetting that mass flow $\dot{m}$ at fixed $D$ scales $u_m \propto \dot{m}$]`

Water flows turbulently ($\mathrm{Re}_D = 4.0×10^{4}$) through a heated circular tube of diameter $D$, giving internal heat transfer coefficient $h_1 = 2400 W/m^2/K$. Using the Dittus–Boelter correlation $\mathrm{Nu}_D = 0.023\,\mathrm{Re}_D^{0.8}\mathrm{Pr}^{0.4}$, find the new heat transfer coefficient $h_2$ if the same mass flow rate $\dot{m}$ is forced through a tube of half the diameter ($D_2 = D_1 / 2$).

**Solution P11.3:** 
At constant mass flow rate $\dot{m} = \rho u_m (\frac{\pi}{4}D^2)$, mean flow speed scales as $u_m \propto D^{-2}$, so $\mathrm{Re}_D = \frac{\rho u_m D}{\mu} = \frac{4\dot{m}}{\pi\mu D} \propto D^{-1}$. Therefore, $h = \frac{k_f}{D}\mathrm{Nu}_D \propto D^{-1}\left(\mathrm{Re}_D^{0.8}\right) \propto D^{-1}\left(D^{-0.8}\right) = \mathbf{D^{-1.8}}$! Halving the diameter at fixed mass flow rate multiplies $h$ by $2^{1.8} = \mathbf{3.482\times}$:

$$
h_2 = 2^{1.8}(2400 W/m^2/K) = (3.4822)(2400) = \mathbf{8357 W/m^2/K}
$$

#### Problem P11.4: Sling Psychrometer Wet-Bulb Adiabatic Evaporative Equilibrium `[§11.3 | 5.c.ii, 5.c.iii | National / Cornell E1 | 90 s | Coupled Heat-Mass Balance | Trap: forgetting Lewis/Chilton-Colburn factor or latent heat]`

In a sling psychrometer (Lienhard §11.7 Fig. 11.16, p. 665  **[S12]**), a wet-wick thermometer bulb reaches steady wet-bulb temperature $T_{\mathrm{wb}} = 18.0 °C$ when swung in dry desert air where the convective heat transfer coefficient is $h = 45.0 W/m^2/K$ and the mass-transfer evaporative cooling flux at the wick surface is $\dot{m}''_{\mathrm{evap}} = 0.370 g/m^2/s$ ($L_v(18 °C) = 2458 kJ/kg$, neglect radiation). Calculate the dry-bulb air temperature $T_{\mathrm{db}}$.

**Solution P11.4:** 
At steady wet-bulb equilibrium, the rate of convective sensible heat gain from the warmer dry-bulb air ($q''_{\mathrm{conv}} = h(T_{\mathrm{db}} - T_{\mathrm{wb}})$) exactly balances the rate of evaporative latent heat removal ($q''_{\mathrm{evap}} = L_v \dot{m}''_{\mathrm{evap}}$):

$$
h\left(T_{\mathrm{db}} - T_{\mathrm{wb}}\right) = L_v\,\dot{m}''_{\mathrm{evap}} = (2.458×10^{6} J/kg)(3.70×10^{-4} kg/m^2/s) = \mathbf{909.46 W/m^2}
$$

$$
T_{\mathrm{db}} = T_{\mathrm{wb}} + \frac{909.46}{h} = 18.0 + \frac{909.46}{45.0} = 18.0 + 20.21 = \mathbf{38.21 °C}
$$

#### Problem P11.5: Multi-Cell Foil Air-Gap Baffle Optimization Inside a 30 mm Wall `[§11.3 | 5.c.iii | 2027 Device / State | 75 s | Rayleigh Scaling $\mathrm{Ra} \propto \Delta T \delta^3$ | Trap: forgetting that $N$ cells divide both $\delta$ and $\Delta T_{\mathrm{cell}}$ by $N$]`

A single vertical air cavity of thickness $W = 30.0 mm$ across a temperature drop $\Delta T_{\mathrm{tot}} = 30.0 K$ has Rayleigh number $\mathrm{Ra}_W = 7.20×10^{4}$. If two thin parallel aluminum-foil sheets are inserted to subdivide the $30.0 mm$ space into $N = 3$ equal $10.0 mm$ series air cells, by what exact factor is the Rayleigh number $\mathrm{Ra}_\delta$ inside each individual cell reduced compared to $\mathrm{Ra}_W$?

**Solution P11.5:** 
Subdividing a gap of width $W$ into $N$ equal series cells divides the cell thickness by $N$ ($\delta = W/N$) **AND** divides the temperature drop across each cell by $N$ ($\Delta T_{\mathrm{cell}} = \Delta T_{\mathrm{tot}}/N$)! Because $\mathrm{Ra}_\delta \propto \Delta T_{\mathrm{cell}}\,\delta^3$, the Rayleigh number in each cell drops as $\mathbf{N^{-4}}$:

$$
\frac{\mathrm{Ra}_\delta}{\mathrm{Ra}_W} = \left(\frac{\Delta T_{\mathrm{tot}}/N}{\Delta T_{\mathrm{tot}}}\right)\!\left(\frac{W/N}{W}\right)^{\!3} = \frac{1}{N^4} = \frac{1}{3^4} = \mathbf{\frac{1}{81}} \implies \mathrm{Ra}_\delta = \frac{7.20×10^{4}}{81} = \mathbf{888.9 < \mathrm{Ra}_c = 1708}
$$

Two foil sheets reduce $\mathrm{Ra}$ by $\mathbf{81\times}$, completely quenching cellular natural convection!

**Table:** Thermophysical Properties of Dry Air ($1 atm$) and Saturated Liquid Water from $0 °C$ to $100 °C$, Including Pre-Computed Rayleigh Modulus $g\beta/(\nu\alpha)$ for Instant $\mathrm{Ra}_L = [g\beta/(\nu\alpha)]\Delta T L^3$ Lookup (Lienhard Tables A.3 & A.6, pp. 746, 756  **[S11,S12]**).

| $T$ $[°C]$ | $T$ $[K]$ | $\rho$ $[kg/m^3]$ | $c_p$ $[J/kg/K]$ | $k_f$ $[W/m/K]$ | $\nu$ $[m^2/s]$ | $\alpha$ $[m^2/s]$ | $\mathrm{Pr}$ $[1]$ | $g\beta/(\nu\alpha)$ $[/K/m^3]$ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Dry Air at $1.00 atm$ ($101.325 kPa$)** — Ideal-gas thermal expansion $\beta = 1/T(K)$ |  |  |  |  |  |  |  |  |
| $0$ | $273.15$ | $1.292$ | $1006$ | $0.0242$ | $1.33×10^{-5}$ | $1.86×10^{-5}$ | $0.715$ | $1.45×10^{8}$ |
| $20$ | $293.15$ | $1.204$ | $1006$ | $0.0257$ | $1.51×10^{-5}$ | $2.12×10^{-5}$ | $0.713$ | $1.04×10^{8}$ |
| $27$ | $300.00$ | $1.177$ | $1006$ | $0.0262$ | $1.57×10^{-5}$ | $2.21×10^{-5}$ | $0.712$ | $9.42×10^{7}$ |
| $40$ | $313.15$ | $1.127$ | $1007$ | $0.0272$ | $1.70×10^{-5}$ | $2.40×10^{-5}$ | $0.710$ | $7.68×10^{7}$ |
| $60$ | $333.15$ | $1.059$ | $1008$ | $0.0287$ | $1.90×10^{-5}$ | $2.69×10^{-5}$ | $0.708$ | $5.76×10^{7}$ |
| $80$ | $353.15$ | $0.999$ | $1010$ | $0.0302$ | $2.10×10^{-5}$ | $2.99×10^{-5}$ | $0.706$ | $4.42×10^{7}$ |
| $100$ | $373.15$ | $0.946$ | $1012$ | $0.0317$ | $2.31×10^{-5}$ | $3.31×10^{-5}$ | $0.704$ | $3.44×10^{7}$ |
| **Saturated Liquid Water ($\mathrm{H_2O}$)** — Note $\beta < 0$ for $T < 3.984 °C$ and $\beta = 0$ at $3.984 °C$ |  |  |  |  |  |  |  |  |
| $0$ | $273.15$ | $999.8$ | $4217$ | $0.561$ | $1.79×10^{-6}$ | $1.33×10^{-7}$ | $13.47$ | $-2.80×10^{9}$ |
| $20$ | $293.15$ | $998.2$ | $4182$ | $0.598$ | $1.00×10^{-6}$ | $1.43×10^{-7}$ | $7.01$ | $1.42×10^{10}$ |
| $30$ | $303.15$ | $995.6$ | $4179$ | $0.615$ | $8.01×10^{-7}$ | $1.48×10^{-7}$ | $5.42$ | $2.51×10^{10}$ |
| $40$ | $313.15$ | $992.2$ | $4179$ | $0.631$ | $6.58×10^{-7}$ | $1.52×10^{-7}$ | $4.33$ | $3.77×10^{10}$ |
| $60$ | $333.15$ | $983.2$ | $4185$ | $0.654$ | $4.74×10^{-7}$ | $1.59×10^{-7}$ | $2.98$ | $6.79×10^{10}$ |
| $80$ | $353.15$ | $971.8$ | $4197$ | $0.670$ | $3.65×10^{-7}$ | $1.64×10^{-7}$ | $2.22$ | $1.05×10^{11}$ |
| $100$ | $373.15$ | $958.4$ | $4216$ | $0.679$ | $2.94×10^{-7}$ | $1.68×10^{-7}$ | $1.75$ | $1.49×10^{11}$ |

#### Problem P11.6: Counterflow vs. Parallel-Flow Heat Exchanger LMTD Comparison `[§11.2 | 5.c.iii | National / Invitational | 75 s | LMTD Eq. (11.5) | Trap: using arithmetic mean $\Delta T$ or parallel-flow endpoint subtraction in counterflow]`

In a double-pipe heat exchanger, hot oil enters at $T_{h,\mathrm{in}} = 90.0 °C$ and exits at $T_{h,\mathrm{out}} = 50.0 °C$ while transferring $\dot{Q} = 12.00 kW$ to cooling water that enters at $T_{c,\mathrm{in}} = 20.0 °C$ and exits at $T_{c,\mathrm{out}} = 45.0 °C$ (overall heat transfer coefficient $U = 400.0 W/m^2/K$, Lienhard Ch. 3 pp. 117–128  **[S12]**). Compute the log-mean temperature difference $\Delta T_{\mathrm{lm}}$ and required heat-exchange surface area $A_s = \dot{Q}/(U\Delta T_{\mathrm{lm}})$ for (a) parallel flow, and (b) counterflow.

**Solution P11.6:** 
- **(a)** **Parallel Flow (both fluids enter at End A and exit at End B):** $\Delta T_A = T_{h,\mathrm{in}} - T_{c,\mathrm{in}} = 90.0 - 20.0 = 70.0 K$, and $\Delta T_B = T_{h,\mathrm{out}} - T_{c,\mathrm{out}} = 50.0 - 45.0 = 5.00 K$. By Eq. Eq. (`eq:11:lmtd-boxed`):
  
$$
\Delta T_{\mathrm{lm,par}} = \frac{70.0 - 5.00}{\ln(70.0/5.00)} = \frac{65.00}{\ln(14.00)} = \frac{65.00}{2.63906} = \mathbf{24.63 K} \implies A_{s,\mathrm{par}} = \frac{12000 W}{(400.0)(24.630)} = \mathbf{1.218 m^2}
$$
- **(b)** **Counterflow (hot enters End A where cold exits; hot exits End B where cold enters):** $\Delta T_A = T_{h,\mathrm{in}} - T_{c,\mathrm{out}} = 90.0 - 45.0 = 45.0 K$, and $\Delta T_B = T_{h,\mathrm{out}} - T_{c,\mathrm{in}} = 50.0 - 20.0 = 30.0 K$:
  
$$
\Delta T_{\mathrm{lm,cf}} = \frac{45.0 - 30.0}{\ln(45.0/30.0)} = \frac{15.00}{\ln(1.500)} = \frac{15.00}{0.40547} = \mathbf{37.00 K} \implies A_{s,\mathrm{cf}} = \frac{12000 W}{(400.0)(36.995)} = \mathbf{0.8109 m^2}
$$

  Counterflow provides a $+50.2%$ larger driving $\Delta T_{\mathrm{lm}}$ and requires $33.4%$ less surface area (and only counterflow allows $T_{c,\mathrm{out}} > T_{h,\mathrm{out}}$!).

#### Problem P11.7: Chilton–Colburn / Reynolds Heat-Momentum Analogy ($C_f \leftrightarrow \mathrm{St}$) `[§11.1 | 5.c.iii | National / MIT | 60 s | Chilton–Colburn Analogy | Trap: forgetting the $\mathrm{Pr}^{2/3}$ factor when $\mathrm{Pr} \ne 1$]`

Air ($\rho = 1.177 kg/m^3$, $c_p = 1006 J/kg/K$, $\mathrm{Pr} = 0.712$ at $300 K$, Table `tab:11:air-water-props`) flows at $u_\infty = 12.0 m/s$ over a flat surface where wind-tunnel drag measurements give a plate-averaged skin-friction coefficient $\bar{C}_f = \dfrac{\bar{\tau}_w}{\frac{1}{2}\rho u_\infty^2} = 0.00420$. Using the Chilton–Colburn Reynolds analogy $\overline{\mathrm{St}}\,\mathrm{Pr}^{2/3} = \dfrac{\bar{C}_f}{2}$ where the Stanton number is $\overline{\mathrm{St}} = \dfrac{\bar{h}}{\rho c_p u_\infty} = \dfrac{\overline{\mathrm{Nu}}_L}{\mathrm{Re}_L \mathrm{Pr}}$ (Lienhard §6.3 Eq. 6.48, p. 297  **[S12]**), compute the average convective heat transfer coefficient $\bar{h}$.

**Solution P11.7:** 
By the Chilton–Colburn analogy (valid for laminar and turbulent boundary layers with $0.6 \le \mathrm{Pr} \le 60$):

$$
\overline{\mathrm{St}} = \frac{\bar{h}}{\rho c_p u_\infty} = \frac{\bar{C}_f}{2\,\mathrm{Pr}^{2/3}} = \frac{0.00420}{2(0.712)^{2/3}} = \frac{0.002100}{0.79750} = \mathbf{0.002633}
$$

$$
\bar{h} = \rho c_p u_\infty\,\overline{\mathrm{St}} = (1.177 kg/m^3)(1006 J/kg/K)(12.0 m/s)(0.0026332) = \mathbf{37.42 W/m^2/K}
$$

#### Problem P11.8: Hot-Wire / Cylinder Crossflow Anemometer Speed Determination `[§11.2 | 5.c.iii | State / National | 75 s | Churchill–Bernstein / King's Law | Trap: forgetting that $\mathrm{Nu}_D \propto \mathrm{Re}_D^{1/2}$ at moderate $\mathrm{Re}_D$]`

A cylindrical platinum resistance probe of diameter $D = 1.20 mm$ and length $\ell = 25.0 mm$ ($A_s = \pi D\ell = 9.425×10^{-5} m^2$) is held at $T_w = 74.0 °C$ in an air stream at $T_\infty = 20.0 °C$ ($T_f = 47.0 °C \implies \nu = 1.77×10^{-5} m^2/s$, $k_f = 0.0277 W/m/K$, $\mathrm{Pr} = 0.709$). When electrical heating power $P = 0.720 W$ is dissipated in the probe at steady state, use the simplified Hilpert crossflow correlation $\overline{\mathrm{Nu}}_D = 0.683\,\mathrm{Re}_D^{0.466}\mathrm{Pr}^{1/3}$ ($40 < \mathrm{Re}_D < 4000$, Lienhard §8.4  **[S12]**) to determine the air speed $u_\infty$.

**Solution P11.8:** 
From the measured electrical power and temperature difference $\Delta T = 74.0 - 20.0 = 54.0 K$:

$$
\bar{h} = \frac{P}{A_s \Delta T} = \frac{0.720 W}{(9.4248×10^{-5} m^2)(54.0 K)} = \mathbf{141.47 W/m^2/K} \implies
  \overline{\mathrm{Nu}}_D = \frac{\bar{h} D}{k_f} = \frac{(141.47)(0.00120)}{0.0277} = \mathbf{6.1288}
$$

Invert $\overline{\mathrm{Nu}}_D = 0.683\,\mathrm{Re}_D^{0.466}\mathrm{Pr}^{1/3}$ with $\mathrm{Pr}^{1/3} = (0.709)^{1/3} = 0.8917$:

$$
\mathrm{Re}_D = \left(\frac{6.1288}{0.683 \times 0.8917}\right)^{\!1/0.466} = (10.0632)^{2.1459} = \mathbf{141.7} \implies
  u_\infty = \frac{\nu\,\mathrm{Re}_D}{D} = \frac{(1.77×10^{-5})(141.7)}{0.00120} = \mathbf{2.09 m/s}
$$

—
**See also:** §`sec:01.10` (`QS-10` Convection Fast Sheet), §`sec:10` (Conduction Networks), §`sec:12` (Thermal Radiation & View Factors), §`sec:13` (Transient Lumped Heating), §`sec:15` (2027 Collector Stratification & Glazing Design), §`sec:17` (ES Probe Immersion Depth).
