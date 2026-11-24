<!-- Source: src/sec13.tex | Tab: Tab 5: TRANSFER | Target: 10 pp -->
# §13: Transient Thermal Systems — Lumped Capacitance, 2027 Radiative-Lamp Heating ODE, Newton Cooling & Semi-Infinite Penetration {#sec:13}

> **[SCOPE: REQUIRED | 2027 Rule 5.c.iii & Part II Device Heating-Curve Prediction (Biot/Fourier tagged **[SUPP]**) | Sources:  **[S01]**,  **[S12]**,  **[S17]**,  **[S25]**]**

### [FORMULA & DECISION CARD: §13 Master Lumped-Capacitance, 2027 Forced Heating, Sensor Lag & Penetration Card  **[S12,S25]**]

| **Formula** | **Variables (SI units)** | **Flags** | **Use when** |
| --- | --- | --- | --- |
| $L_c = \dfrac{V}{A_s}, \quad \mathrm{Bi} = \dfrac{h L_c}{k_{\mathrm{solid}}}$ | $L_c$: characteristic length $(m)$ [slab half-thickness $L$, cylinder $R/2$, sphere $R/3$, cube $a/6$]; $k_{\mathrm{solid}}$: **solid** conductivity $(W/m/K)$ | **[Bi<0.1]** **[SUPP]** | Lumped-capacitance validity: $\mathrm{Bi} < 0.1$ ensures internal $\Delta T_{\mathrm{body}} < 5\%$ |
| $\mathrm{Fo} = \dfrac{\alpha t}{L_c^2}, \quad \dfrac{t}{\tau} = \mathrm{Bi}\cdot\mathrm{Fo}$ | $\mathrm{Fo}$: Fourier dimensionless time; $\alpha = k_s/(\rho c_p)$ $(m^2/s)$; $\tau = \dfrac{\rho c_p V}{h A_s} = R_{\mathrm{th}}C$ $(s)$ | **[SUPP]** | Lienhard Eq. (5.7) p. 196 **[S12]**; relates diffusion time scale $L_c^2/\alpha$ to $\tau$ |
| $\dfrac{T(t) - T_\infty}{T_i - T_\infty} = e^{-t/\tau}, \quad \tau = R_{\mathrm{th}} C = \dfrac{m c_p}{h A_s}$ | $T_i = T(0)$: initial temperature; $T_\infty$: constant ambient temperature; $C = m c_p$ $(J/K)$; $R_{\mathrm{th}} = 1/(hA_s)$ $(K/W)$ | **[Bi<0.1]** | Unforced Newton cooling/warming ($\dot{Q}_{\mathrm{source}}=0$); $t_{1/2} = \tau\ln 2 = 0.6931\tau$ |
| $C_{\mathrm{eff}}\dfrac{dT}{dt} = P_{\mathrm{abs}} - \dfrac{T(t) - T_{\mathrm{room}}}{R_{\mathrm{th}}}$ | $P_{\mathrm{abs}}$: net absorbed lamp radiant power $(W)$; $R_{\mathrm{th}} = 1/(UA)_{\mathrm{loss}}$ $(K/W)$; $C_{\mathrm{eff}}$: effective thermal capacitance $(J/K)$ | **[2027-RULE]** | Governing energy-balance ODE of the 2027 Heat-Lamp Collector |
| $T(t) = T_{\mathrm{ss}} - \left(T_{\mathrm{ss}} - T_{\mathrm{start}}\right)e^{-t/\tau}$ | $T_{\mathrm{ss}} = T_{\mathrm{room}} + P_{\mathrm{abs}} R_{\mathrm{th}}$: asymptotic stagnation temp; $\tau = C_{\mathrm{eff}} R_{\mathrm{th}}$; initial slope $(dT/dt)_0 = \dfrac{P_{\mathrm{abs}}}{C_{\mathrm{eff}}} - \dfrac{T_{\mathrm{start}}-T_{\mathrm{room}}}{\tau}$ | **[2027-RULE]** | Exact closed-form algebraic solution for 2027 collector temperature $T(t)$ |
| $\mathrm{TG}(t) \approx \dfrac{P_{\mathrm{abs}} t}{C_{\mathrm{eff}}}\!\left(1 - \dfrac{t}{2 C_{\mathrm{eff}} R_{\mathrm{th}}}\right)$ | Second-order algebraic expansion of $\mathrm{TG}(t) = T(t) - T_{\mathrm{start}}$ when $T_{\mathrm{start}} \approx T_{\mathrm{room}}$ and $t \lesssim \tau$ | **[2027-RULE]** | Separates optical gain $P_{\mathrm{abs}}t/C_{\mathrm{eff}}$ from finite heat-loss curvature $t/(2\tau)$ |
| $T_{\mathrm{ss}} = \dfrac{T_1^2 - T_0 T_2}{2T_1 - T_0 - T_2}, \quad \tau = \dfrac{\Delta t}{\ln\!\left(\dfrac{T_1 - T_0}{T_2 - T_1}\right)}$ | $T_0 = T(0),\; T_1 = T(\Delta t),\; T_2 = T(2\Delta t)$: three temperatures measured at equal time intervals $\Delta t$ (e.g., $t = 0, 5, 10\,min$) | **[3-PT-FIT]** | Exact algebra-only extraction of $T_{\mathrm{ss}}$ and $\tau$ from 3 data points! |
| $T_p(t) = T_w - \left(T_w - T_{p,0}\right)e^{-t/\tau_p}$ | $\tau_p = m_p c_{p,p}/(h_p A_p)$: probe time constant $(s)$; at $t = 5\tau_p$, remaining error is $e^{-5} = 0.674\%$ ($99.33\%$ settled) | **[SENSOR]** | Thermometer dynamic immersion lag; ramp lag in bath $\dot{T}_w=b$ is $\Delta T_{\mathrm{lag}} = -b\tau_p$ |
| $\delta_t \approx 2\sqrt{\alpha t}, \quad T_{\mathrm{int}} = \dfrac{b_1 T_1 + b_2 T_2}{b_1 + b_2}$ | $\delta_t$: semi-infinite thermal diffusion depth $(m)$; $b_i = \sqrt{k_i\rho_i c_{p,i}}$: thermal effusivity; $T_{\mathrm{int}}$: instantaneous contact interface temp | **[SUPP]** | Downward heat diffusion in unstirred cup ($\delta_t \approx 18.8 mm$ in $600 s$) & touch warmth |
| $t_{\mathrm{rad,vac}} = \dfrac{m c_p}{3\varepsilon\sigma A}\!\left(\dfrac{1}{T_f^3} - \dfrac{1}{T_i^3}\right)$ | Exact cooling time of a lumped body ($C=mc_p$) radiating into deep space ($T_{\mathrm{env}}\to0 K$) via $C\,dT/dt = -\varepsilon\sigma A T^4$ | **[STATE/NAT]** | 2027 Cornell Invitational **[S25]** ($T$ in $K$) |

## Lumped-Capacitance Validity ($\mathrm{Bi} < 0.1$) & Electrical $RC$ Analogy

### Internal vs. External Thermal Resistance and the Biot Number Criterion

When a body of volume $V$, surface area $A_s$, density $\rho$, specific heat $c_p$, and thermal conductivity $k_{\mathrm{solid}}$ exchanges heat with a surrounding environment via surface heat transfer coefficient $h_{\mathrm{eff}} = h_{\mathrm{conv}} + h_{\mathrm{rad}}$, the ratio of internal conductive resistance inside the body ($R_{\mathrm{cond,int}} \sim L_c / (k_{\mathrm{solid}}A_s)$) to external boundary-layer resistance at the surface ($R_{\mathrm{conv,ext}} = 1/(h_{\mathrm{eff}}A_s)$) is the dimensionless **Biot number** (Lienhard §1.3 pp. 22–24 & §5.2 pp. 194–197  **[S12]**):

$$
\begin{aligned}
\mathrm{Bi} \equiv \frac{R_{\mathrm{cond,int}}}{R_{\mathrm{conv,ext}}} = \frac{h_{\mathrm{eff}} L_c}{k_{\mathrm{solid}}}, \qquad L_c \equiv \frac{V}{A_s} = \begin{cases} L & \text{(plane slab of half-thickness } L\text{ exposed on both faces)} \\ R/2 = D/4 & \text{(long cylinder of radius } R\text{)} \\ R/3 = D/6 & \text{(sphere of radius } R\text{ or cube of side } 2R\text{)} \end{cases}
  
\end{aligned}
$$

As shown in Fig. `fig:13:biot-regimes` (modeled on Lienhard Figs. 1.10–1.11 and 2.11  **[S12]**):
- **Lumped-Capacitance Regime ($\mathrm{Bi} < 0.1$):** Internal conduction resistance is negligible compared to surface resistance ($k_{\mathrm{solid}}$ is large or $L_c$ is small). Spatial temperature variations inside the body are $<5\%$ of $|T - T_\infty|$, so the entire object can be modeled at a single uniform temperature $T(t)$ with lumped thermal capacitance $C = \rho c_p V = m c_p$ $[J/K]$ and lumped boundary resistance $R_{\mathrm{th}} = 1/(h_{\mathrm{eff}}A_s)$ $[K/W]$.
- **Intermediate / Stratified Regime ($0.1 \le \mathrm{Bi} \le 10$ — The Unstirred 2027 Water Cup!):** For the $100 mL$ quiescent water column in the 9 oz cup ($L_w \approx 36 mm = 0.036 m$, $k_w = 0.613 W/m/K$) heated from above with top-surface loss coefficient $h_{\mathrm{top}} \approx 12 W/m^2/K$, the vertical Biot number is $\mathrm{Bi}_z = \frac{h_{\mathrm{top}}L_w}{k_w} = \frac{(12)(0.036)}{0.613} = \mathbf{0.71 > 0.1}$! Because $\mathrm{Bi}_z > 0.1$ and top-down heating is buoyantly stable ($\mathrm{Ra} < 0$), a significant vertical temperature gradient persists across the water column (Fig. `fig:13:biot-regimes`, middle curve), keeping the ES-measured top water layer warmer than the bottom layer!
- **Conduction-Limited / Semi-Infinite Regime ($\mathrm{Bi} > 20$):** External convection offers negligible resistance ($T_{\mathrm{surface}} \to T_\infty$ almost instantly), and transient response is governed by internal thermal diffusion $\mathrm{Fo} = \alpha t / L_c^2$.

### Electrical $RC$ Circuit Analogy and Why Thermal Systems Never Overshoot

In the lumped-capacitance regime ($\mathrm{Bi} < 0.1$), temperature difference $\theta(t) = T(t) - T_\infty$ $[K]$ is analogous to capacitor voltage $V(t)$, heat flow rate $\dot{Q}(t)$ $[W]$ is analogous to electric current $I(t)$, thermal resistance $R_{\mathrm{th}} = 1/(h_{\mathrm{eff}}A_s)$ $[K/W]$ is analogous to electrical resistance $R$, and thermal capacitance $C = m c_p$ $[J/K]$ is analogous to electrical capacitance $C_e$, giving the thermal time constant:

$$
\begin{aligned}
\tau = R_{\mathrm{th}} C = \frac{m c_p}{h_{\mathrm{eff}} A_s} = \frac{\rho c_p L_c}{h_{\mathrm{eff}}} \quad [s], \qquad \frac{t}{\tau} = \frac{h_{\mathrm{eff}} t}{\rho c_p L_c} = \left(\frac{h_{\mathrm{eff}} L_c}{k_s}\right)\!\left(\frac{\alpha t}{L_c^2}\right) = \mathrm{Bi}\cdot\mathrm{Fo}
  
\end{aligned}
$$

As emphasized by Lienhard §5.2 (Fig. 5.2–5.3, p. 197  **[S12]**), while mechanical spring-mass-damper systems have mass $m$ and electrical circuits have inductance $L_e$ that can cause underdamped oscillations past equilibrium, **the Second Law of Thermodynamics forbids any thermal element analogous to mass or inductance**: a passive thermal system's temperature approaches $T_{\mathrm{ss}}$ monotonically and can never spontaneously overshoot its equilibrium temperature!

> **[Vector Figure: Universal dimensionless lumped-capacitance forced heating curve $1 - e^{-t/\tau}$ and unforced Newton cooling curve $e^{-t/\tau}$, showing the zero-loss initial tangent $t/\tau$, the $1\tau$ ($63.2\%$), $3\tau$ ($95.0\%$), and $5\tau$ ($99.33\%$) landmarks, and the 2027 competition heating window ($t/\tau \approx 0.67\text{--}1.00$)  **[S12]**. | Label: `fig:13:lumped-heating`]**
> - **Diagram Annotations & Key Elements:** **X-Axis:** Dimensionless Time $t / \tau = t / (C_{\mathrm{eff}}R_{\mathrm{th}}) = \mathrm{Bi}\cdot\mathrm{Fo}$ (For 2027 Collector with $\tau \approx 900 s$, $t = 10–15 min$ is $t/\tau \in [0.67, 1.00]$) • **Y-Axis:** Normalized Response $\theta(t) / \theta_{\max}$ • **Legend:** Forced Heating: $\dfrac{T(t)-T_i}{T_{\mathrm{ss}}-T_i} = 1 - e^{-t/\tau}$ • **Legend:** Newton Cooling: $\dfrac{T(t)-T_\infty}{T_i-T_\infty} = e^{-t/\tau}$ • **Legend:** Zero-Loss Tangent: $\left(\dfrac{dT}{dt}\right)_0 t = \dfrac{P_{\mathrm{abs}}t}{C_{\mathrm{eff}}}$ • 2027 Run / [-1pt]$10\text{--}15\text{ min}$

## 2027 Collector Forced Heating ODE & Algebra-Only Parameter Extraction

### [DERIVATION: Algebra-Only (`5.d.iv` Compliant) Solution of the 2027 Forced Radiative-Heating Equation  **[S01,S12]**]

During the 2027 Heating Time ($t \in [600 s, 900 s]$), the collector water layer (effective thermal capacitance $C_{\mathrm{eff}}$ $[J/K]$) absorbs constant radiant lamp power $P_{\mathrm{abs}}(h, P_{\mathrm{bulb}})$ $[W]$ while losing heat to the ambient room at $T_{\mathrm{room}}$ through overall parasitic resistance $R_{\mathrm{th}} = 1/(UA)_{\mathrm{loss}}$ $[K/W]$:

$$
\begin{aligned}
C_{\mathrm{eff}}\frac{dT}{dt} = P_{\mathrm{abs}} - \frac{T(t) - T_{\mathrm{room}}}{R_{\mathrm{th}}} = -\frac{1}{R_{\mathrm{th}}}\Big[T(t) - \underbrace{\left(T_{\mathrm{room}} + P_{\mathrm{abs}} R_{\mathrm{th}}\right)}_{T_{\mathrm{ss}}}\Big]
  
\end{aligned}
$$

Notice that $T_{\mathrm{ss}} = T_{\mathrm{room}} + P_{\mathrm{abs}} R_{\mathrm{th}}$ is the constant **steady-state stagnation temperature** where heat loss would exactly balance absorbed power ($dT/dt = 0$). Shifting the temperature variable to the remaining deficit $\Phi(t) \equiv T_{\mathrm{ss}} - T(t)$ (since $T_{\mathrm{ss}}$ is constant, $d\Phi/dt = -dT/dt$) transforms Eq. Eq. (`eq:13:forced-ode`) into the standard exponential decay $\frac{d\Phi}{dt} = -\frac{\Phi}{\tau}$ with $\tau = C_{\mathrm{eff}}R_{\mathrm{th}}$ and initial deficit $\Phi(0) = T_{\mathrm{ss}} - T_{\mathrm{start}}$:

$$
\begin{aligned}
\boxed{T(t) = T_{\mathrm{ss}} - \left(T_{\mathrm{ss}} - T_{\mathrm{start}}\right)e^{-t/\tau} = T_{\mathrm{start}} + \left[P_{\mathrm{abs}}R_{\mathrm{th}} - \left(T_{\mathrm{start}} - T_{\mathrm{room}}\right)\right]\!\left(1 - e^{-t/(C_{\mathrm{eff}}R_{\mathrm{th}})}\right)}
  
\end{aligned}
$$

**Three-Point Equal-Interval Algebraic Parameter Extraction (Zero Calculus or Nonlinear Solver Needed!):**
Suppose you measure three temperatures $T_0 = T(0)$, $T_1 = T(\Delta t)$, and $T_2 = T(2\Delta t)$ at equal time spacing $\Delta t$ (e.g., $t = 0, 5, 10\,min$). From Eq. Eq. (`eq:13:forced-solution`), let $E \equiv e^{-\Delta t/\tau}$:

$$
T_1 - T_0 = \left(T_{\mathrm{ss}} - T_0\right)(1 - E), \qquad T_2 - T_1 = \left(T_{\mathrm{ss}} - T_0\right)E(1 - E)
$$

Dividing the two increments eliminates $T_{\mathrm{ss}}$ immediately to give $\tau$, and substituting $E = \frac{T_2 - T_1}{T_1 - T_0}$ solves for $T_{\mathrm{ss}}$ directly:

$$
\begin{aligned}
\boxed{E = e^{-\Delta t/\tau} = \frac{T_2 - T_1}{T_1 - T_0} \implies \tau = \frac{\Delta t}{\ln\!\left(\dfrac{T_1 - T_0}{T_2 - T_1}\right)}, \qquad T_{\mathrm{ss}} = \frac{T_1^2 - T_0 T_2}{2T_1 - T_0 - T_2}}
  
\end{aligned}
$$

> **[Vector Figure: Comparison of internal solid/liquid temperature profiles versus external boundary-layer drops across three Biot number regimes (Lienhard Figs. 1.10–1.11 & 2.11  **[S12]**): $\mathrm{Bi} = 0.05 < 0.1$ (uniform lumped body), $\mathrm{Bi}_z = 0.71$ (unstirred 2027 water cup exhibiting top-layer thermal stratification), and $\mathrm{Bi} = 20 \gg 1$ (internal conduction-dominated). | Label: `fig:13:biot-regimes`]**
> - **Diagram Annotations & Key Elements:** **X-Axis:** Normalized Spatial Coordinate $x/L$ Across Slab or Water Depth $z/L_w$ ($0 = \text{Insulated Base},\; 1 = \text{Top Boundary}$) • **Y-Axis:** Dimensionless Temperature $\Theta(x) = \dfrac{T(x)-T_{\mathrm{base}}}{T_\infty - T_{\mathrm{base}}}$ • **Legend:** $\mathrm{Bi} = 0.05 < 0.1$ (Lumped Metal: $T_{\mathrm{body}}$ Uniform) • **Legend:** $\mathrm{Bi}_z = 0.71$ (2027 Water Cup: Stratified Top Layer!) • **Legend:** $\mathrm{Bi} = 20 \gg 1$ (Thick Insulator: $T_{\mathrm{surf}} \approx T_\infty$) • External / [-1pt]Boundary / [-1pt]Layer ($1/h$)

## Thermometer Lag ($5\tau_p$), Semi-Infinite Penetration & Radiative Cooling

### Sensor Dynamic Step Lag ($5\tau_p$ Settling Rule) and Linear Ramp-Tracking Lag
- **Step Immersion Response:** When a thermometer probe of time constant $\tau_p = m_p c_{p,p}/(h_p A_p)$ initially at room temperature $T_{p,0}$ is inserted into water at $T_w$, its reading evolves as $T_p(t) = T_w - (T_w - T_{p,0})e^{-t/\tau_p}$. At $t = 1\tau_p, 2\tau_p, 3\tau_p, 5\tau_p$, the probe has completed $63.21\%, 86.47\%, 95.02\%, \mathbf{99.33\%}$ of the step change. Always wait at least $\mathbf{t \ge 5\tau_p}$ before recording a steady temperature!
- **Ramp-Tracking Lag (Lienhard §5.2 Eq. 5.12, p. 198  **[S12]**):** If a probe of time constant $\tau_p$ sits in a water bath whose temperature is rising linearly at rate $b = dT_w/dt$ $[K/s]$ ($T_w(t) = T_i + b t$), solving $\tau_p \frac{dT_p}{dt} + T_p = T_i + b t$ yields:
  
$$
\begin{aligned}
T_p(t) = T_w(t) - b \tau_p\left(1 - e^{-t/\tau_p}\right) \xrightarrow{t \gg \tau_p} T_p(t) - T_w(t) = -b \tau_p
    
\end{aligned}
$$

  In steady ramp heating, a probe always lags behind the true bath temperature by a constant offset $\Delta T_{\mathrm{lag}} = -b\tau_p$ (i.e., it displays the temperature the bath had $\tau_p$ seconds ago!).

### Semi-Infinite Diffusion Depth ($\delta_t \approx 2\sqrt{\alpha t}$), Effusivity ($b$), and $T^4$ Vacuum Cooling
- **Semi-Infinite Penetration Depth ($\delta_t$):** When a surface temperature or heat flux is suddenly applied at $z = 0$ to a thick medium of thermal diffusivity $\alpha = k/(\rho c_p)$ (Lienhard §5.6, pp. 220–230  **[S12]**), the thermal wave penetrates a characteristic depth $\delta_t \approx 2\sqrt{\alpha t}$ where $\mathrm{Fo}_{\delta} = \alpha t / \delta_t^2 = 1/4$ (at $z = 2\sqrt{\alpha t}$, $\mathrm{erfc}(1) = 0.1573$, so $84.3\%$ of the temperature change is confined within $z < 2\sqrt{\alpha t}$). For quiescent water ($\alpha_w = 1.48×10^{-7} m^2/s$ at $35 °C$) over a $10.0 min$ ($600 s$) run, $\delta_t = 2\sqrt{(1.48×10^{-7})(600)} = \mathbf{18.85 mm}$ — half the $36 mm$ water depth in the 9 oz cup!
- **Instantaneous Two-Body Contact Temperature via Thermal Effusivity ($b = \sqrt{k\rho c_p}$):** When semi-infinite body $1$ at initial temperature $T_1$ is pressed into sudden contact with semi-infinite body $2$ at initial temperature $T_2$ (Lienhard Eq. 5.51, p. 228  **[S12]**), heat flux continuity at the interface requires their contact plane to jump immediately to the time-invariant **effusivity-weighted mean temperature**:
  
$$
\begin{aligned}
T_{\mathrm{int}} = \frac{b_1 T_1 + b_2 T_2}{b_1 + b_2}, \qquad b_i \equiv \sqrt{k_i \rho_i c_{p,i}} \quad \left[J/m^2/K/s^1/2\right]
    
\end{aligned}
$$
- **Pure Radiative $T^4$ Cooling in Vacuum (State/National Tier, 2027 Cornell Invitational  **[S25]**):** For a body of heat capacity $C = m c_p$, area $A$, and emittance $\varepsilon$ cooling by pure Stefan–Boltzmann radiation in a cryogenic vacuum ($T_{\mathrm{env}}^4 \ll T^4$), separating variables in $C\frac{dT}{dt} = -\varepsilon\sigma A T^4$ ($\int T^{-4}dT = -\frac{1}{3}T^{-3}$) yields the exact algebraic cooling time from $T_i$ to $T_f$:
  
$$
\begin{aligned}
t_{\mathrm{rad,vac}} = \frac{m c_p}{3\varepsilon\sigma A}\!\left(\frac{1}{T_f^3} - \frac{1}{T_i^3}\right), \qquad T(t) = \left(T_i^{-3} + \frac{3\varepsilon\sigma A}{m c_p}\,t\right)^{\!-1/3}
    
\end{aligned}
$$

### Two-Node Stratified Water Cup Model, One-Term $\mathrm{Bi} > 0.1$ Decay & Calorimetry Corrections

- **Coupled Two-Node Stratified Water Model for the 2027 9 oz Cup ($\mathrm{Bi}_z = 0.71 > 0.1$):**
  Because $66\text{--}72\%$ of the $2400 K$ lamp's near-IR energy is absorbed in the upper $5–10 mm$ of the water column while downward conduction is slow ($R_{w,\mathrm{int}} = \frac{L_{\mathrm{mid}}}{k_w A_{\mathrm{cup}}} \approx \frac{0.018}{(0.62)(0.0036)} = 8.06 K/W$), divide the $100 mL$ water into an upper measured layer $C_1 = m_1 c_p$ at $T_1(t) = T_{\mathrm{top}}(t)$ (absorbing power $P_1 = f_{\mathrm{top}}P_{\mathrm{abs}}$) and a lower layer $C_2 = m_2 c_p$ at $T_2(t) = T_{\mathrm{bot}}(t)$ (absorbing transmitted power $P_2 = (1 - f_{\mathrm{top}})P_{\mathrm{abs}}$):
  
$$
\begin{aligned}
C_1\frac{dT_1}{dt} = P_1 - \frac{T_1 - T_{\mathrm{room}}}{R_1} - \frac{T_1 - T_2}{R_{w,\mathrm{int}}}, \qquad
    C_2\frac{dT_2}{dt} = P_2 + \frac{T_1 - T_2}{R_{w,\mathrm{int}}} - \frac{T_2 - T_{\mathrm{room}}}{R_2}
    
\end{aligned}
$$

  Solving Eq. Eq. (`eq:13:two-node-strat`) yields a fast top-layer mode ($\tau_{\mathrm{fast}} \approx 420 s$) and a slow bulk mode ($\tau_{\mathrm{slow}} \approx 1150 s$), producing a top-to-bottom stratification differential $\Delta T_{\mathrm{strat}}(t) = T_1(t) - T_2(t) \approx +12–+20 °C$ at $t = 600 s$!
- **One-Term Spatial Transient Conduction Approximation ($\mathrm{Bi} > 0.1,\; \mathrm{Fo} > 0.2$, Lienhard §5.5 pp. 213–218  **[S12]**):**
  When $\mathrm{Bi} > 0.1$ and dimensionless time $\mathrm{Fo} = \alpha t / L^2 > 0.2$ (where $L$ is the slab half-thickness or cylinder/sphere radius $R$), higher spatial eigenmodes decay rapidly and the centerline temperature $T_{\mathrm{center}}(t)$ and surface temperature $T_{\mathrm{surf}}(t)$ follow a single exponential mode with lead amplitude $A_1$ and eigenvalue $\lambda_1$:
  
$$
\begin{aligned}
\Theta_{\mathrm{center}}(t) = \frac{T_{\mathrm{center}}(t) - T_\infty}{T_i - T_\infty} \approx A_1 \exp\!\left(-\lambda_1^2\,\mathrm{Fo}\right), \qquad \Theta_{\mathrm{surf}}(t) = \Theta_{\mathrm{center}}(t)\cdot \phi_1(\lambda_1)
    
\end{aligned}
$$

  For $\mathrm{Bi} \ll 1$, $\lambda_1^2 \approx \mathrm{Bi}$ (slab), $2\mathrm{Bi}$ (cylinder), or $3\mathrm{Bi}$ (sphere) and $A_1 \to 1$, recovering lumped capacitance $\lambda_1^2\mathrm{Fo} = (hL_c/k)(\alpha t/L_c^2) = t/\tau$!
- **Regnault–Pfaundler / Dickinson Linear-Drift Calorimetry Heat-Loss Correction:**
  In a laboratory calorimetry run spanning reaction interval $[t_0, t_f]$ ($\Delta t = t_f - t_0$) where the calorimeter exhibits a steady pre-reaction temperature drift rate $r_i = (dT/dt)_{\mathrm{pre}}$ (at $T_0$) and a steady post-reaction cooling drift rate $r_f = (dT/dt)_{\mathrm{post}}$ (at peak temperature $T_{\mathrm{obs}}$), the true adiabatic temperature rise $\Delta T_{\mathrm{corr}}$ corrected for Newton heat leakage to the surroundings is:
  
$$
\begin{aligned}
\boxed{\Delta T_{\mathrm{corr}} = \left(T_{\mathrm{obs}} - T_0\right) - r_i\,t_m - r_f\left(\Delta t - t_m\right) \approx \left(T_{\mathrm{obs}} - T_0\right) - \left(\frac{r_i + r_f}{2}\right)\Delta t\quad (\text{symmetric rise } t_m = \Delta t/2)}
    
\end{aligned}
$$

  where $t_m \in [0, \Delta t]$ is the Dickinson equal-area midpoint time at which $\int_{t_0}^{t_f}[T(t) - T_0]\,dt = (T_{\mathrm{obs}} - T_0)(\Delta t - t_m)$ (for an exponential calorimetry rise, $t_m \approx 0.35\text{--}0.45\,\Delta t$).

## Worked Competition Examples (§13)

### Worked Example — Biot Number Check & Lumped Cooling of a Cylindrical Resistor `[Lienhard Ex. 2.8  **[S12]**]`

A cylindrical electronic resistor of diameter $D = 3.60 mm$ ($r_o = 1.80 mm$) and length $\ell = 10.0 mm$ has density $\rho = 2000 kg/m^3$, specific heat $c_p = 700 J/kg/K$, and conductivity $k = 10.0 W/m/K$. When power is switched off at $T_i = 72.3 °C$, it cools in still cabinet air at $T_\infty = 35.0 °C$ by parallel natural convection ($h = 13.0 W/m^2/K$) and thermal radiation ($h_{\mathrm{rad}} = 7.17 W/m^2/K$). Verify $\mathrm{Bi} < 0.1$, find the thermal time constant $\tau$, and compute the time $t_{95}$ required to complete $95.0\%$ of its temperature drop.
\tcblower
**Solution.** Total surface area (sidewall + 2 circular ends) is $A_s = 2\pi r_o \ell + 2\pi r_o^2 = 1.3345×10^{-4} m^2$, and volume is $V = \pi r_o^2 \ell = 1.0179×10^{-7} m^2$, so $L_c = V/A_s = 7.627×10^{-4} m$. With $h_{\mathrm{eff}} = 13.0 + 7.17 = 20.17 W/m^2/K$:

$$
\mathrm{Bi} = \frac{h_{\mathrm{eff}} L_c}{k} = \frac{(20.17)(7.627×10^{-4})}{10.0} = \mathbf{0.00154 \ll 0.1} \quad (\text{or } \frac{h_{\mathrm{eff}} r_o}{k} = 0.00363 \ll 0.1 \implies \text{lumped model exact!})
$$

$$
\tau = \frac{\rho c_p V}{h_{\mathrm{eff}} A_s} = \frac{(2000)(700)(1.0179×10^{-7})}{(20.17)(1.3345×10^{-4})} = \mathbf{52.94 s}, \qquad
  t_{95} = -\tau\ln(0.05) = 3.00\,\tau = \mathbf{158.6 s}
$$

**✓ Verified by:** Checked in `check_sec10_13.py` (`EX-13.1-TAU`, `EX-13.1-T95`): $\tau = 52.940 s$, $t_{95} = 158.59 s$.

### Worked Example — 2027 Heat-Lamp Collector Transient Heating Curve at $t = 10\text{ min}$ vs. $15\text{ min}$ `[2027 Part II Prediction]`

Under a $125 W$ heat lamp at $h = 45.0 cm$, a glazed 2027 collector delivers net absorbed power $P_{\mathrm{abs}} = 24.00 W$ into an effective thermal capacitance $C_{\mathrm{eff}} = 380.0 J/K$ with parasitic thermal resistance $R_{\mathrm{th}} = 2.3763 K/W$ ($\tau = C_{\mathrm{eff}}R_{\mathrm{th}} = 903.0 s = 15.05 min$). If $T_{\mathrm{start}} = T_{\mathrm{room}} = 22.00 °C$, calculate (a) the initial heating rate $(dT/dt)_0$ and stagnation temperature $T_{\mathrm{ss}}$, (b) the exact water temperature $T(t)$ at $t = 10.0 min$ ($600 s$) and $t = 15.0 min$ ($900 s$), and (c) the error if a team naively extrapolates the initial linear slope $(P_{\mathrm{abs}}/C_{\mathrm{eff}})t$ without accounting for heat loss!
\tcblower
**Solution.** (a) Initial heating rate: $\left(\dfrac{dT}{dt}\right)_0 = \dfrac{P_{\mathrm{abs}}}{C_{\mathrm{eff}}} = \dfrac{24.00}{380.0} = 0.063158 K/s = \mathbf{3.789 °C/min}$. Stagnation temperature: $T_{\mathrm{ss}} = T_{\mathrm{room}} + P_{\mathrm{abs}}R_{\mathrm{th}} = 22.00 + (24.00)(2.37632) = \mathbf{79.03 °C}$.\\
(b) By Eq. Eq. (`eq:13:forced-solution`):
{$$
\begin{aligned}
t = 600 s\ (10.0 min):\; T(600 s) &= 79.0316 - (79.0316 - 22.00)e^{-600/903.0} = 22.00 + 57.0316(0.48543) = \mathbf{49.69 °C}\ (\mathrm{TG} = +27.69 °C) \\
  t = 900 s\ (15.0 min):\; T(900 s) &= 79.0316 - (79.0316 - 22.00)e^{-900/903.0} = 22.00 + 57.0316(0.63090) = \mathbf{57.98 °C}\ (\mathrm{TG} = +35.98 °C)
\end{aligned}
$$

(c) Naive zero-loss linear extrapolation predicts $T_{\mathrm{lin}}(10 min) = 22.00 + 37.89 = 59.89 °C$ (an error of $+10.20 °C$!) and $T_{\mathrm{lin}}(15 min) = 22.00 + 56.84 = 78.84 °C$ (an error of $+20.86 °C$!).

**✓ Verified by:** Runge–Kutta `RK45` integration in `check_sec10_13.py` (`EX-13.2-T10M`, `EX-13.2-T15M`): $T(600 s) = 49.6857 °C$, $T(900 s) = 57.9810 °C$.

### Worked Example — Three-Point Equal-Interval Algebraic Extraction of $T_{\mathrm{ss}}$ and $\tau$ `[Calibration Lab Shortcut]`

During a pre-tournament calibration run, a team records water temperatures at $\Delta t = 300.0 s$ ($5.00 min$) intervals: $T_0 = T(0) = 20.00 °C$, $T_1 = T(300 s) = 32.00 °C$, and $T_2 = T(600 s) = 41.00 °C$. Using the exact three-point algebraic formulas in Eq. Eq. (`eq:13:three-point-exact`), determine the asymptotic stagnation temperature $T_{\mathrm{ss}}$, the system time constant $\tau$, and predict $T(900 s)$ at $t = 15.0 min$.
\tcblower
**Solution.** First temperature increment is $\Delta T_{01} = T_1 - T_0 = 12.00 K$, and second increment is $\Delta T_{12} = T_2 - T_1 = 9.00 K$ (ratio $E = e^{-\Delta t/\tau} = 9.00/12.00 = 0.7500$). Applying Eq. Eq. (`eq:13:three-point-exact`):

$$
T_{\mathrm{ss}} = \frac{T_1^2 - T_0 T_2}{2T_1 - T_0 - T_2} = \frac{32.00^2 - (20.00)(41.00)}{2(32.00) - 20.00 - 41.00} = \frac{1024.0 - 820.0}{64.0 - 61.0} = \frac{204.0}{3.0} = \mathbf{68.00 °C}
$$

$$
\tau = \frac{\Delta t}{\ln\!\left(\dfrac{T_1 - T_0}{T_2 - T_1}\right)} = \frac{300.0 s}{\ln(12.00 / 9.00)} = \frac{300.0}{\ln(4/3)} = \frac{300.0}{0.287682} = \mathbf{1042.8 s} = 17.38 min
$$

At $t = 900 s = 3\Delta t$, $e^{-3\Delta t/\tau} = E^3 = (0.7500)^3 = 0.421875$, so $T(900 s) = 68.00 - (68.00 - 20.00)(0.421875) = \mathbf{47.75 °C}$.

**✓ Verified by:** Forward substitution in `check_sec10_13.py` (`EX-13.3-TSS`, `EX-13.3-TAU`, `EX-13.3-FWD`): $T_{\mathrm{ss}} = 68.00 °C$, $\tau = 1042.82 s$, $T(600 s) = 41.0000 °C$.

### Worked Example — Thermometer Probe Step Lag ($2\tau_p$ vs. $5\tau_p$) & Ramp-Tracking Offset `[Lienhard Eq. 5.12  **[S12]**]`

An Event Supervisor's digital probe thermometer has time constant $\tau_p = 3.50 s$ in water and sits initially in room air at $T_{p,0} = 22.00 °C$. At the end of a run, the ES inserts the probe into the top layer of water at true temperature $T_w = 47.00 °C$. Find the displayed reading if the ES reads the thermometer prematurely at $t = 7.00 s$ ($2\tau_p$) versus waiting $t = 17.5 s$ ($5\tau_p$). Also find the steady tracking lag if the probe is left inside a calibration bath warming at $b = 2.70 °C/min$ ($0.0450 °C/s$).
\tcblower
**Solution.** Using $T_p(t) = T_w - (T_w - T_{p,0})e^{-t/\tau_p}$ with initial step $T_w - T_{p,0} = 25.00 °C$:

$$
T_p(7.00 s) = 47.00 - 25.00\,e^{-2.00} = 47.00 - 3.3834 = \mathbf{43.62 °C} \quad (\text{premature error } = \mathbf{-3.38 °C}!)
$$

$$
T_p(17.5 s) = 47.00 - 25.00\,e^{-5.00} = 47.00 - 0.1684 = \mathbf{46.83 °C} \quad (\text{residual lag } = -0.17 °C)
$$

In the warming bath ($b = 0.0450 °C/s$), Eq. Eq. (`eq:13:ramp-lag`) gives steady lag $\Delta T_{\mathrm{lag}} = -b\tau_p = -(0.0450)(3.50) = \mathbf{-0.16 °C}$.

**✓ Verified by:** Checked in `check_sec10_13.py` (`EX-13.4-STEP2TAU`, `EX-13.4-STEP5TAU`): $T_p(2\tau_p) = 43.617 °C$, $T_p(5\tau_p) = 46.832 °C$.

### Worked Example — Semi-Infinite Water Penetration Depth & Effusivity Contact Warmth `[Lienhard §5.6  **[S12]**]`

(a) Calculate the characteristic thermal diffusion penetration depth $\delta_t = 2\sqrt{\alpha_w t}$ downward from the top surface of quiescent water ($\alpha_w = 1.48×10^{-7} m^2/s$ at $35 °C$) over a $10.0 min$ ($600 s$) heating run. (b) Using Table `tab:10:k-hierarchy`, compare the instantaneous interfacial temperature $T_{\mathrm{int}}$ when a human fingertip ($T_1 = 34.0 °C$, effusivity $b_{\mathrm{skin}} = 1100 J/m^2/K/s^1/2$) touches an aluminum block ($b_{\mathrm{Al}} = 24095$) versus balsa wood ($b_{\mathrm{balsa}} = 89.44$), both initially at room temperature $T_2 = 20.0 °C$.
\tcblower
**Solution.** (a) Downward conductive penetration depth in $600 s$:

$$
\delta_t = 2\sqrt{(1.48×10^{-7} m^2/s)(600 s)} = 0.018847 m = \mathbf{18.85 mm} \quad (\approx 52\%\text{ of the }36 mm\text{ cup water depth!})
$$

(b) By Eq. Eq. (`eq:13:effusivity-contact`) (explaining why aluminum feels freezing while balsa feels warm):

$$
T_{\mathrm{int,Al}} = \frac{(1100)(34.0) + (24095.3)(20.0)}{1100 + 24095.3} = \mathbf{20.61 °C}, \qquad
  T_{\mathrm{int,balsa}} = \frac{(1100)(34.0) + (89.44)(20.0)}{1100 + 89.44} = \mathbf{32.95 °C}
$$

**✓ Verified by:** Checked in `check_sec10_13.py` (`EX-13.5-PENETRATION`, `EX-13.5-EFFUSIVITY-AL`, `EX-13.5-EFFUSIVITY-BALSA`): $\delta_t = 18.847 mm$, $T_{\mathrm{int,Al}} = 20.611 °C$, $T_{\mathrm{int,balsa}} = 32.947 °C$.

### Worked Example — Pure Radiative $T^4$ Cooling in Deep-Space Vacuum `[2027 Cornell Invitational E1  **[S25]**]`

A blackened copper sphere of mass $m = 0.500 kg$, specific heat $c_p = 384 J/kg/K$, surface area $A = 0.0150 m^2$, and emittance $\varepsilon = 0.800$ cools in deep space ($T_{\mathrm{env}} \approx 0 K$) from $T_i = 400.0 K$ to $T_f = 300.0 K$. Calculate the required cooling time $t_{\mathrm{rad,vac}}$.
\tcblower
**Solution.** Total heat capacity is $C = m c_p = (0.500)(384) = 192.0 J/K$. Applying Eq. Eq. (`eq:13:t4-vacuum`):

$$
t_{\mathrm{rad,vac}} = \frac{192.0}{3(0.800)(5.6704×10^{-8})(0.0150)}\!\left(\frac{1}{300.0^3} - \frac{1}{400.0^3}\right) = \mathbf{2013.9 s} = 33.57 min
$$

**✓ Verified by:** Independent `RK45` integration of $dT/dt = -(\varepsilon\sigma A/C)T^4$ in `check_sec10_13.py` (`EX-13.6-TVAC`, `EX-13.6-RKCHK`): $t = 2013.93 s$ gives $T(t) = 300.000 K$.

### Worked Example — Post-Lamp-Off Cup Extraction Cooling During the 1-Minute Window (`Rule 5.II.g`) `[2027 Execution Discipline  **[S01]**]`

At the end of a $10.0 min$ heating run, the ES turns off the heat lamp (`Rule 5.II.g`) when the top water layer in the 9 oz cup ($C_{\mathrm{top}} = 215.0 J/K$) is at $T_{\mathrm{off}} = 48.00 °C$ in a room at $T_{\mathrm{room}} = 22.00 °C$. Once the upper reflector hood and BoPET glazing cap are lifted off to remove the cup, the open cup loses heat to the room with total top+side conductance $G_{\mathrm{open}} = 1/R_{\mathrm{open}} = 0.14554 W/K$ ($\tau_{\mathrm{cool}} = C_{\mathrm{top}}/G_{\mathrm{open}} = 1477.3 s$). Compare the post-lamp cooling temperature drop $\Delta T_{\mathrm{cool}}$ for (a) a practiced team that removes the cup in $t_{\mathrm{fast}} = 6.0 s$, versus (b) an unpracticed team that fumbles for $t_{\mathrm{slow}} = 50.0 s$ inside the 1-minute window.
\tcblower
**Solution.** By Newton's cooling law, $\Delta T_{\mathrm{cool}}(t) = (T_{\mathrm{off}} - T_{\mathrm{room}})\left(1 - e^{-t/\tau_{\mathrm{cool}}}\right)$ with $T_{\mathrm{off}} - T_{\mathrm{room}} = 26.00 K$:

$$
\Delta T_{\mathrm{cool}}(6.0 s) = 26.00\left(1 - e^{-6.0 / 1477.26}\right) = \mathbf{0.105 °C} \quad (T_{\mathrm{meas}} = 47.89 °C)
$$

$$
\Delta T_{\mathrm{cool}}(50.0 s) = 26.00\left(1 - e^{-50.0 / 1477.26}\right) = \mathbf{0.865 °C} \quad (T_{\mathrm{meas}} = 47.13 °C)
$$

Delaying extraction from $6 s$ to $50 s$ throws away $\mathbf{0.76 °C}$ of Temperature Gain $\mathrm{TG}$ AND introduces a $0.76 °C$ prediction error!

**✓ Verified by:** Checked in `check_sec10_13.py` (`EX-13.7-COOL6S`, `EX-13.7-COOL50S`): $\Delta T_{\mathrm{cool}}(6 s) = 0.1054 °C$, $\Delta T_{\mathrm{cool}}(50 s) = 0.8653 °C$.

### Worked Example — Two-Node Stratified Water Cup Coupled ODE Simulation `[Clarifications #1–#4 Physics  **[S02]**]`

Model the $100.0 mL$ water in the 9 oz cup using the coupled two-node system Eq. Eq. (`eq:13:two-node-strat`): Node 1 (top $40.0 mL$ layer, $C_1 = 167.36 J/K$) absorbs $P_1 = 16.00 W$ of near-IR lamp radiation and loses heat to ambient ($T_{\mathrm{room}} = 22.00 °C$) through top glazing resistance $R_1 = 3.50 K/W$; Node 2 (bottom $60.0 mL$ layer, $C_2 = 251.04 J/K$) absorbs $P_2 = 4.00 W$ of transmitted visible/short-NIR radiation and loses heat through cradle resistance $R_2 = 8.00 K/W$; internal water conduction resistance between the layers ($L_{\mathrm{mid}} = 18.0 mm,\; k_w = 0.620 W/m/K,\; A_{\mathrm{cup}} = 36.0 cm^2$) is $R_{12} = \frac{0.0180}{(0.620)(0.00360)} = 8.0645 K/W$. Starting from $T_1(0) = T_2(0) = 22.00 °C$, determine $T_{\mathrm{top}}(600 s)$, $T_{\mathrm{bot}}(600 s)$, and the stratification differential $\Delta T_{\mathrm{strat}}(600 s)$ at $t = 10.0 min$.
\tcblower
**Solution.** Substituting into Eq. Eq. (`eq:13:two-node-strat`) gives the linear $2\times 2$ matrix system $\frac{d}{dt}\begin{bmatrix}\theta_1 \\ \theta_2\end{bmatrix} = \begin{bmatrix}-0.002448 & +0.0007409 \\ +0.0004940 & -0.0009919\end{bmatrix}\begin{bmatrix}\theta_1 \\ \theta_2\end{bmatrix} + \begin{bmatrix}0.09560 \\ 0.01593\end{bmatrix}$ where $\theta_i = T_i - 22.00$. Integrating to $t = 600.0 s$ yields:

$$
T_{\mathrm{top}}(600 s) = \mathbf{53.73 °C}\ (\mathrm{TG}_{\mathrm{top}} = +31.73 °C), \qquad
  T_{\mathrm{bot}}(600 s) = \mathbf{33.82 °C}\ (\mathrm{TG}_{\mathrm{bot}} = +11.82 °C)
$$

The top-to-bottom stratification differential is $\Delta T_{\mathrm{strat}} = 53.73 - 33.82 = \mathbf{+19.91 °C}$ (whereas a stirred cup would read only $0.40(53.73) + 0.60(33.82) = 41.79 °C$, losing $11.94 °C$!).

**✓ Verified by:** Exact `RK45` integration in `check_sec10_13.py` (`EX-13.8-2NODE-TOP`, `EX-13.8-2NODE-BOT`): $T_{\mathrm{top}} = 53.7346 °C$, $T_{\mathrm{bot}} = 33.8248 °C$.

### Worked Example — Regnault–Pfaundler / Dickinson Calorimetry Heat-Leak Correction `[Experimental Lab Analysis]`

In a coffee-cup dissolution calorimetry experiment, the thermometer records a pre-mixing linear drift rate $r_i = +0.020 °C/min$ leading up to mixing at $t_0 = 0.00 min$ ($T_0 = 21.000 °C$). The exothermic reaction reaches a peak observed temperature $T_{\mathrm{obs}} = 29.850 °C$ at $t_f = 4.00 min$ ($\Delta t = 4.00 min$), followed by a steady post-reaction Newton cooling drift $r_f = -0.140 °C/min$. If the Dickinson equal-area midpoint time is $t_m = 0.40\,\Delta t = 1.60 min$, compute the true adiabatic temperature rise $\Delta T_{\mathrm{corr}}$.
\tcblower
**Solution.** Observed uncorrected temperature rise is $\Delta T_{\mathrm{obs}} = 29.850 - 21.000 = 8.850 °C$. Applying Eq. Eq. (`eq:13:regnault-pfaundler`):

$$
\Delta T_{\mathrm{corr}} = 8.850 - (+0.020 °C/min)(1.60 min) - (-0.140 °C/min)(4.00 - 1.60)\,min = 8.850 - 0.032 + 0.336 = \mathbf{9.154 °C}
$$

Accounting for heat leakage recovers $+0.304 °C$ ($+3.44%$) of lost reaction enthalpy!

**✓ Verified by:** Checked in `check_sec10_13.py` (`EX-13.9-REGNAULT`): $\Delta T_{\mathrm{corr}} = 9.1540 °C$.

## Transient Thermal Traps & 2027 Post-Heating Extraction Discipline

### [TRAP & DIAGNOSTIC: Top Transient Conduction & Heating-Curve Traps]

| **Wrong move / Symptom** | **What it produces / Why it fails** | **5-second diagnostic & fix** |
| --- | --- | --- |
| **1. Using full diameter $D$ instead of $L_c = V/A_s$ ($D/4$ cylinder, $D/6$ sphere) in $\mathrm{Bi} = hL_c/k_s$** | Overestimates $\mathrm{Bi}$ by $4\times$ (cylinder) or $6\times$ (sphere). | Always compute $L_c = V/A_{\mathrm{exposed}}$ first. |
| **2. Linearly extrapolating initial heating slope $(P_{\mathrm{abs}}/C_{\mathrm{eff}})t$ to $t = 10\text{--}15\text{ min}$** | Ignores parasitic heat loss $(T - T_{\mathrm{room}})/R_{\mathrm{th}}$ and overpredicts $T_f$ by $8\text{--}20\,^\circ\mathrm{C}$! | Use $T_{\mathrm{ss}} - (T_{\mathrm{ss}} - T_{\mathrm{start}})e^{-t/\tau}$ or the 3-point fit Eq. Eq. (`eq:13:three-point-exact`). |
| **3. Confusing half-life $t_{1/2} = \tau\ln 2 = 0.6931\tau$ ($50\%$ change) with time constant $\tau$ ($63.21\%$ change)** | At $t = \tau$, remaining deficit is $1/e = 36.79\%$, NOT $50\%$! | $50\% \to 0.693\tau$; $63.2\% \to 1\tau$; $95.0\% \to 3\tau$; $99.3\% \to 5\tau$. |

### [2027 HEAT-COLLECTOR DEVICE & LAB: 2027 Collector Thermal-Mass Budget & Post-Lamp-Off Cup Extraction Timing  **[S01,S02,S05]**]

- **Parasitic Thermal-Mass Budget ($\sum C_{\mathrm{parasitic}} < 5 J/K$):** Because initial heating slope is $(dT/dt)_0 = P_{\mathrm{abs}}/C_{\mathrm{eff}}$, any heavy glass or thick metal structure thermally coupled to the cup drains energy during a short $10 min$ run. Keep all cup-adjacent elements foil-thin ($25 µm$ BoPET glazing cap: $C = 0.24 J/K$; $16 µm$ Al-foil mirror liner: $C = 1.18 J/K$; 3-point balsa knife-edge cradle tips: $C < 0.3 J/K$) so $>98\%$ of captured energy heats the water!
- **Post-Lamp-Off Extraction Window (`Rule 5.II.g` 1-Minute Window):** The instant the ES turns off the lamp, the uncovered water surface begins cooling at $(dT/dt)_{\mathrm{cool}} = -\frac{\dot{Q}_{\mathrm{evap}} + \dot{Q}_{\mathrm{conv}} + \dot{Q}_{\mathrm{rad}}}{C_{\mathrm{top}}} \approx -\frac{3.2 W}{215 J/K} \approx -0.015 °C/s$ ($-0.90 °C/min$). Complete the lift-off hood removal and gentle non-swirling cup placement onto the Testing Surface in a standardized $\mathbf{t_{\mathrm{extract}} = 6\text{--}8\text{ s}}$ (identical to your calibration runs!) so post-lamp cooling is $< 0.12 °C$ and 100% absorbed into your empirical calibration curve.

## Rapid Competition Problem & Solution Bank (§13)

#### Problem P13.1: Classic Coffee-and-Cream Mixing Paradox (Wait vs. Add Cream Immediately) `[§13.1 | 5.c.iii | All Levels / Classic Invitational | 75 s | Newton Cooling Linearity | Trap: assuming order of mixing and cooling commutes when $c_p\Delta T$ mixes at constant $hA$]`

Two students start with identical cups of black coffee of mass $m_c = 200.0 g$ at $T_{c,0} = 85.00 °C$ in a room at $T_\infty = 20.00 °C$ ($\tau = 1200 s = 20.0 min$). Student A immediately pours in $m_m = 25.0 g$ of cold cream at $T_m = 5.00 °C$ (assume equal $c_p$ and neglect change in $\tau$) and then waits $t = 10.0 min$ ($600 s$). Student B lets the hot black coffee cool for $t = 10.0 min$ first and then pours in the $25.0 g$ of $5.00 °C$ cream at the end. Which student has hotter coffee at $t = 10.0 min$, and by how many $^\circ\mathrm{C}$?

**Solution P13.1:** 
**Student A (adding cold cream immediately) ALWAYS ends up with hotter coffee!** Physically, cooling rate $\dot{Q}_{\mathrm{loss}} = hA(T - T_\infty)$ is proportional to temperature excess above the room; adding cold cream immediately drops the coffee's temperature, reducing heat loss to the room throughout the entire $10 min$ wait (and even more strongly when $h_{\mathrm{nat}}\propto\Delta T^{1/4}$, radiation $\propto T^4$, and evaporation $\propto P_{\mathrm{sat}}(T)$ are included!). Numerically, with $e^{-600/1200} = e^{-0.500} = 0.60653$:
- **Student A (Mix at $t=0$, then cool):** $T_{A,0} = \dfrac{200(85.0) + 25(5.0)}{225} = 76.111 °C \implies T_A(10 min) = 20.0 + (76.111 - 20.0)(0.60653) = \mathbf{54.03 °C}$.
- **Student B (Cool first, then mix at $t=10 min$):** $T_{B,\mathrm{pre}}(10 min) = 20.0 + (85.0 - 20.0)(0.60653) = 59.424 °C \implies T_B(10 min) = \dfrac{200(59.424) + 25(5.0)}{225} = \mathbf{53.38 °C}$.

Student A's coffee is warmer by $\Delta T = 54.033 - 53.377 = \mathbf{+0.66 °C}$! *(Note: Only if the cream were initially at room temperature $T_m = T_\infty = 20.0 °C$ and $\tau$ remained unchanged would the two temperatures tie; if $T_m < T_\infty$, adding immediately always wins!)*

#### Problem P13.2: Geometric Scaling of Cooling Time Across Sphere Radius ($\mathrm{Bi} \ll 1$ vs. $\mathrm{Bi} \gg 1$) `[§13.1 | 5.c.iii | State / National | 60 s | Dimensional Scaling | Trap: confusing lumped $\tau \propto R^1$ with diffusive $t \propto R^2$]`

Compare how the characteristic $95\%$ cooling time $t_{95}$ of a solid sphere of radius $R$ scales with $R$ when $R$ is doubled ($R_2 = 2R_1$) in two opposite regimes: (a) small high-conductivity copper spheres in still air where $\mathrm{Bi} \ll 0.1$ and $h$ is constant, versus (b) large low-conductivity rubber spheres quenched in agitated ice water where $\mathrm{Bi} \gg 20$.

**Solution P13.2:** 
- **(a)** **Lumped Regime ($\mathrm{Bi} \ll 0.1$):** $\tau = \dfrac{\rho c_p V}{h A_s} = \dfrac{\rho c_p (\frac{4}{3}\pi R^3)}{h (4\pi R^2)} = \dfrac{\rho c_p R}{3 h} \propto \mathbf{R^1}$. Doubling $R$ multiplies cooling time by $\mathbf{2.00\times}$ (or by $2^{5/4} = 2.38\times$ if laminar natural convection $h \propto R^{-1/4}$ applies).
- **(b)** **Internal Conduction-Limited Regime ($\mathrm{Bi} \gg 20$):** Surface temperature jumps immediately to $T_\infty$, and cooling is governed by the Fourier number $\mathrm{Fo} = \dfrac{\alpha t}{R^2} = \mathrm{const} \implies t_{95} \propto \dfrac{R^2}{\alpha} \propto \mathbf{R^2}$. Doubling $R$ multiplies cooling time by $\mathbf{4.00\times}$!

#### Problem P13.3: 2027 Collector Bulb-Wattage Switch ($125\text{ W} \to 100\text{ W}$) with $T_{\mathrm{start}} \ne T_{\mathrm{room}}$ `[§13.2 | 5.II.a–f | 2027 Part II Prediction | 75 s | Forced Heating Equation | Trap: scaling $T_{\mathrm{final}}$ by $100/125$ instead of scaling only $P_{\mathrm{abs}}$!]`

A team's collector has calibrated parameters $R_{\mathrm{th}} = 2.400 K/W$ and $\tau = C_{\mathrm{eff}}R_{\mathrm{th}} = 900.0 s$ ($15.00 min$). Under a $125.0 W$ bulb at $h = 50.0 cm$, absorbed radiant power is $P_{\mathrm{abs},125} = 18.50 W$. At the tournament, the ES announces $h = 50.0 cm$, a $\mathbf{100.0 W}$ bulb ($P_{\mathrm{abs},100} = 0.800\,P_{\mathrm{abs},125} = 14.80 W$), heating time $t = 12.00 min$ ($720.0 s$), room temperature $T_{\mathrm{room}} = 23.00 °C$, and starting water temperature $T_{\mathrm{start}} = 19.50 °C$. Calculate the exact predicted final temperature $T_{\mathrm{pred}}$.

**Solution P13.3:** 
Under the $100.0 W$ bulb, the asymptotic stagnation temperature is:

$$
T_{\mathrm{ss},100} = T_{\mathrm{room}} + P_{\mathrm{abs},100}R_{\mathrm{th}} = 23.00 + (14.80)(2.400) = 23.00 + 35.52 = \mathbf{58.52 °C}
$$

At $t = 720.0 s$, $e^{-t/\tau} = e^{-720.0/900.0} = e^{-0.8000} = 0.449329$, and $1 - e^{-t/\tau} = 0.550671$. By Eq. Eq. (`eq:13:forced-solution`):

$$
T_{\mathrm{pred}}(720 s) = T_{\mathrm{ss},100} - \left(T_{\mathrm{ss},100} - T_{\mathrm{start}}\right)e^{-t/\tau} = 58.52 - (58.52 - 19.50)(0.449329) = 58.52 - 17.5328 = \mathbf{40.99 °C} \longrightarrow \mathbf{41.0 °C}
$$

*Fatal Trap Check:* Simply multiplying the $125 W$ final temperature ($45.88 °C$) by $0.80$ would give $36.7 °C$ — an error of $-4.3 °C$! Only the absorbed power term $P_{\mathrm{abs}}R_{\mathrm{th}}$ scales with bulb wattage.

#### Problem P13.4: Two-Body Contact Effusivity Matching `[§13.3 | 5.c.iii | National / Cornell E1 | 60 s | Effusivity $b = \sqrt{k\rho c_p}$ | Trap: using conductivity $k$ ratio instead of effusivity $b$ ratio]`

A semi-infinite copper block ($T_{\mathrm{Cu}} = 100.0 °C$, effusivity $b_{\mathrm{Cu}} = 37000 J/m^2/K/s^1/2$ from Table `tab:10:k-hierarchy`) is brought into sudden perfect contact with a semi-infinite liquid water column ($T_w = 20.0 °C$, effusivity $b_w = 1598 J/m^2/K/s^1/2$). What is the instantaneous interface temperature $T_{\mathrm{int}}$ immediately after contact?

**Solution P13.4:** 
By Eq. Eq. (`eq:13:effusivity-contact`):

$$
T_{\mathrm{int}} = \frac{b_{\mathrm{Cu}} T_{\mathrm{Cu}} + b_w T_w}{b_{\mathrm{Cu}} + b_w} = \frac{(37000)(100.0) + (1598)(20.0)}{37000 + 1598} = \frac{3.73196×10^{6}}{38598} = \mathbf{96.69 °C}
$$

Because $b_{\mathrm{Cu}} / b_w = 23.15$, the interface stays within $3.31 °C$ of the copper's initial temperature!

#### Problem P13.5: Calorimetric Perturbation of the Top Water Layer by a Cold Metal Probe `[§13.3 | 4.f, 5.II.g | 2027 Lab / All Levels | 60 s | Thermal Equilibrium | Trap: ignoring thermal mass of thick metal probe tip]`

An Event Supervisor's heavy stainless-steel probe tip has active immersed mass $m_p = 2.20 g$ ($c_{p,\mathrm{SS}} = 460 J/kg/K = 0.460 J/g/K \implies C_p = 1.012 J/K$) and enters the top stratified water layer ($m_{\mathrm{top,local}} = 25.0 g,\; c_{p,w} = 4.184 J/g/K \implies C_{w,\mathrm{local}} = 104.6 J/K$) from an air-conditioned room at $T_{p,0} = 20.00 °C$. If the true water temperature before probe insertion is $T_{w,0} = 46.00 °C$, by how much does the probe's own thermal mass cool the local water zone at equilibrium?

**Solution P13.5:** 
By First-Law energy conservation between the probe tip and local water zone:

$$
\Delta T_{\mathrm{drain}} = T_{\mathrm{eq}} - T_{w,0} = -\frac{C_p}{C_{w,\mathrm{local}} + C_p}\left(T_{w,0} - T_{p,0}\right) = -\frac{1.012}{104.6 + 1.012}(46.00 - 20.00) = -(0.009582)(26.00) = \mathbf{-0.25 °C}
$$

#### Problem P13.6: Newton Cooling with Linearly Falling Room Temperature ($T_\infty(t) = T_i - b t$) `[§13.3 | 5.c.iii | National / Lienhard §5.2 | 75 s | Ramp Response Eq. (13.6) | Trap: assuming $T(t) = T_\infty(t)$ at long times instead of $T_\infty(t) + b\tau$]`

A well-stirred water vessel of thermal time constant $\tau = 600.0 s$ ($10.0 min$) starts in thermal equilibrium with a room at $T(0) = T_\infty(0) = 25.00 °C$. At $t = 0$, the room temperature begins dropping at a steady linear rate $b = 0.300 °C/min$ ($0.00500 °C/s$) so $T_\infty(t) = 25.00 - 0.00500\,t$. Find the vessel's temperature $T(t)$ and its temperature excess $T(t) - T_\infty(t)$ above the room at $t = 20.0 min$ ($1200 s$).

**Solution P13.6:** 
By Eq. Eq. (`eq:13:ramp-lag`) (with sign reversed for a falling bath, $T_\infty(t) = T_i - b t$), the vessel lags behind the falling room temperature by $+b\tau(1 - e^{-t/\tau})$:

$$
T(t) - T_\infty(t) = +b\tau\left(1 - e^{-t/\tau}\right) = (0.00500)(600.0)\left(1 - e^{-1200/600}\right) = 3.00(1 - e^{-2}) = 3.00(0.86466) = \mathbf{+2.594 °C}
$$

Since $T_\infty(1200 s) = 25.00 - (0.300)(20.0) = 19.00 °C$, the vessel temperature at $t = 20.0 min$ is $T(1200 s) = 19.00 + 2.594 = \mathbf{21.59 °C}$.

**Table:** Part A: Exact One-Term Heisler Eigenvalues ($\lambda_1$), Centerline Amplitudes ($A_1$), and Surface-to-Center Ratios ($\theta_{\mathrm{surf}}/\theta_{\mathrm{center}}$) for Plane Slab (Half-Thickness $L$), Infinite Cylinder (Radius $R$), and Sphere (Radius $R$) when $\mathrm{Fo} \ge 0.2$ (Lienhard §5.3 Tables 5.1–5.2, pp. 217–222  **[S12]**). Here $\mathrm{Bi} = hL/k$ (slab) or $hR/k$ (cylinder/sphere), and $\theta(0,t)/\theta_i = A_1 \exp(-\lambda_1^2 \mathrm{Fo})$. Part B: Gaussian Error Function $\mathrm{erf}(\eta)$ and $\mathrm{erfc}(\eta) = 1 - \mathrm{erf}(\eta)$ for Semi-Infinite Conduction $\eta = x/(2\sqrt{\alpha t})$ (Lienhard Table 5.3, p. 232  **[S12]**).

| $\mathrm{Bi}$ | **Plane Slab** ($\theta_s/\theta_c = \cos\lambda_1$) |  |  | **Infinite Cylinder** ($\theta_s/\theta_c = J_0(\lambda_1)$) |  |  | **Sphere** ($\theta_s/\theta_c = \frac{\sin\lambda_1}{\lambda_1}$) |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $[1]$ | $\lambda_1$ $[rad]$ | $A_1$ $[1]$ | $\theta_s/\theta_c$ | $\lambda_1$ $[rad]$ | $A_1$ $[1]$ | $\theta_s/\theta_c$ | $\lambda_1$ $[rad]$ | $A_1$ $[1]$ | $\theta_s/\theta_c$ |
| $0.02$ | $0.1410$ | $1.0033$ | $0.9901$ | $0.1995$ | $1.0050$ | $0.9901$ | $0.2445$ | $1.0060$ | $0.9901$ |
| $0.05$ | $0.2218$ | $1.0082$ | $0.9755$ | $0.3143$ | $1.0124$ | $0.9755$ | $0.3854$ | $1.0149$ | $0.9754$ |
| $0.10$ | $0.3111$ | $1.0161$ | $0.9518$ | $0.4417$ | $1.0246$ | $0.9518$ | $0.5423$ | $1.0298$ | $0.9516$ |
| $0.20$ | $0.4328$ | $1.0311$ | $0.9078$ | $0.6170$ | $1.0483$ | $0.9071$ | $0.7593$ | $1.0592$ | $0.9064$ |
| $0.50$ | $0.6533$ | $1.0701$ | $0.7940$ | $0.9408$ | $1.1143$ | $0.7900$ | $1.1656$ | $1.1441$ | $0.7885$ |
| $1.00$ | $0.8603$ | $1.1191$ | $0.6522$ | $1.2558$ | $1.2071$ | $0.6422$ | $1.5708$ | $1.2732$ | $0.6366$ |
| $2.00$ | $1.0769$ | $1.1785$ | $0.4741$ | $1.5994$ | $1.3384$ | $0.4557$ | $2.0288$ | $1.4793$ | $0.4421$ |
| $5.00$ | $1.3138$ | $1.2402$ | $0.2542$ | $1.9898$ | $1.5029$ | $0.2300$ | $2.5704$ | $1.7870$ | $0.2104$ |
| $10.0$ | $1.4289$ | $1.2620$ | $0.1415$ | $2.1795$ | $1.5677$ | $0.1220$ | $2.8363$ | $1.9249$ | $0.1058$ |
| $50.0$ | $1.5400$ | $1.2727$ | $0.0308$ | $2.3572$ | $1.5993$ | $0.0249$ | $3.0788$ | $1.9962$ | $0.0204$ |
| $\infty$ | $\pi/2=1.5708$ | $4/\pi=1.2732$ | $0.0000$ | $2.4048$ | $1.6020$ | $0.0000$ | $\pi=3.1416$ | $2.0000$ | $0.0000$ |
| **Part B: Semi-Infinite Error Function Lookup** ($\eta = \dfrac{x}{2\sqrt{\alpha t}}$; constant $T_s$: $\dfrac{T(x,t) - T_s}{T_i - T_s} = \mathrm{erf}(\eta)$, $\dfrac{T(x,t) - T_i}{T_s - T_i} = \mathrm{erfc}(\eta)$) |  |  |  |  |  |  |  |  |  |
| $\eta$: | $0.00$ | $0.10$ | $0.20$ | $0.30$ | $0.40$ | $0.50$ | $0.60$ | $0.70$ | $0.80$ |
| $\mathrm{erf}(\eta)$: | $0.0000$ | $0.1125$ | $0.2227$ | $0.3286$ | $0.4284$ | $0.5205$ | $0.6039$ | $0.6778$ | $0.7421$ |
| $\mathrm{erfc}(\eta)$: | $1.0000$ | $0.8875$ | $0.7773$ | $0.6714$ | $0.5716$ | $0.4795$ | $0.3961$ | $0.3222$ | $0.2579$ |
| $\eta$: | $0.90$ | $1.00$ | $1.10$ | $1.20$ | $1.40$ | $1.60$ | $1.80$ | $2.00$ | $2.50$ |
| $\mathrm{erf}(\eta)$: | $0.7969$ | $0.8427$ | $0.8802$ | $0.9103$ | $0.9523$ | $0.9763$ | $0.9891$ | $0.9953$ | $0.9996$ |
| $\mathrm{erfc}(\eta)$: | $0.2031$ | $0.1573$ | $0.1198$ | $0.0897$ | $0.0477$ | $0.0237$ | $0.0109$ | $0.0047$ | $0.0004$ |

**Table:** 2027 Heat-Lamp Collector Parametric Sensitivity Matrix for $T_f(t) = T_{\mathrm{room}} + P_{\mathrm{abs}}R_{\mathrm{th}}(1 - e^{-t/\tau}) + (T_{\mathrm{start}} - T_{\mathrm{room}})e^{-t/\tau}$ Evaluated at Baseline $P_{\mathrm{bulb}} = 125 W$, $h = 50.0 cm$, $t = 900 s$ ($15.0 min$), $\tau = 1200 s$, $R_{\mathrm{th}} = 2.40 K/W$, $P_{\mathrm{abs}} = 18.75 W$ ($T_{\mathrm{ss}} - T_{\mathrm{room}} = 45.00 K$, $e^{-t/\tau} = e^{-0.750} = 0.47237$, $1 - e^{-t/\tau} = 0.52763$, $\Delta T_f = +23.74 °C$ when $T_{\mathrm{start}} = T_{\mathrm{room}} = 21.00 °C$, $T_f = 44.74 °C$).

| **Tournament Input $x_i$** | **Exact Closed-Form Partial Derivative $\partial T_f / \partial x_i$** | **Baseline Sensitivity** | **Effect on Prediction $T_{\mathrm{pred}}$** |
| --- | --- | --- | --- |
| Starting water temp $T_{\mathrm{start}}$ | $\dfrac{\partial T_f}{\partial T_{\mathrm{start}}} = e^{-t/\tau}$ | $\mathbf{+0.472 °C/°C}$ | $+1.00 °C$ higher $T_{\mathrm{start}}$ raises $T_f$ by $+0.472 °C$ |
| Ambient room temp $T_{\mathrm{room}}$ | $\dfrac{\partial T_f}{\partial T_{\mathrm{room}}} = 1 - e^{-t/\tau}$ | $\mathbf{+0.528 °C/°C}$ | Notice $\frac{\partial T_f}{\partial T_{\mathrm{start}}} + \frac{\partial T_f}{\partial T_{\mathrm{room}}} \equiv 1.000$ |
| Heating duration $t$ | $\dfrac{\partial T_f}{\partial t} = \dfrac{T_{\mathrm{ss}} - T_{\mathrm{start}}}{\tau}\,e^{-t/\tau}$ | $\mathbf{+1.063 °C/min}$ ($+0.0177 °C/s$) | Going from $10 min$ to $15 min$ adds $+5.94 °C$ |
| Bulb wattage $P_{\mathrm{bulb}}$ ($100 W$ vs $125 W$) | $\dfrac{\partial T_f}{\partial P_{\mathrm{bulb}}} = \dfrac{P_{\mathrm{abs}} R_{\mathrm{th}}}{P_{\mathrm{bulb}}}\left(1 - e^{-t/\tau}\right)$ | $\mathbf{+0.190 °C/W}$ | Switching $125 W \to 100 W$ drops $T_f$ by $\mathbf{-4.75 °C}$! |
| Bulb height $h$ ($40–65 cm$, $P_{\mathrm{abs}} \propto d^{-n}$) | $\dfrac{\partial T_f}{\partial h} = -\dfrac{n}{h - z_{\mathrm{ap}}}\,P_{\mathrm{abs}}R_{\mathrm{th}}\left(1 - e^{-t/\tau}\right)$ | $\mathbf{-0.68 °C/cm}$ (at $h = 50 cm$) | Raising lamp by $+5.0 cm$ drops $T_f$ by $\sim\mathbf{-3.4 °C}$ |
| Evaporative glazing cover (`Clarif. #5`) | $\Delta T_{f,\mathrm{glaze}} \approx \Delta P_{\mathrm{evap}} R_{\mathrm{th}}\left(1 - e^{-t/\tau}\right)$ | $\mathbf{+2.8 °C\text{ to }+4.8 °C}$ | Removing $2.2–3.8 W$ latent loss raises $T_f$ by $2.8–4.8 °C$ |

#### Problem P13.7: Heisler One-Term Center, Surface, and Total Energy Calculation for a Quenched Sphere ($\mathrm{Bi} = 2.00$) `[§13.3 | 5.c.iii | National / MIT | 90 s | Table 13.1 Eigenvalues | Trap: using lumped formula when $\mathrm{Bi} = 2.00 \gg 0.1$]`

A solid glass sphere of radius $R = 20.0 mm$ ($k = 1.10 W/m/K$, $\alpha = 6.25×10^{-7} m^2/s$), initially at uniform temperature $T_i = 120.0 °C$, is plunged at $t = 0$ into a circulating bath at $T_\infty = 20.0 °C$ ($\theta_i = 100.0 K$) with convection coefficient $h = 110.0 W/m^2/K$. Using Table `tab:13:heisler-erf`, calculate at $t = 320.0 s$: (a) the Biot number $\mathrm{Bi}$ and Fourier number $\mathrm{Fo}$, (b) the exact sphere center temperature $T(0,t)$, and (c) the sphere outer surface temperature $T(R,t)$.

**Solution P13.7:** 
- **(a)** Using sphere radius $R = 0.0200 m$ in the Heisler convention of Table `tab:13:heisler-erf`:
  
$$
\mathrm{Bi}_R = \frac{h R}{k} = \frac{(110.0)(0.0200)}{1.10} = \mathbf{2.000}, \qquad
    \mathrm{Fo} = \frac{\alpha t}{R^2} = \frac{(6.25×10^{-7} m^2/s)(320.0 s)}{(0.0200)^2} = \frac{2.00×10^{-4}}{4.00×10^{-4}} = \mathbf{0.5000 \ge 0.2}
$$
- **(b)** From Table `tab:13:heisler-erf` (Sphere row at $\mathrm{Bi} = 2.00$), $\lambda_1 = 2.0288 rad$, $A_1 = 1.4793$, and $\theta_s/\theta_c = 0.4421$. The dimensionless center temperature excess is:
  
$$
\frac{\theta(0,t)}{\theta_i} = A_1 \exp\!\left(-\lambda_1^2 \mathrm{Fo}\right) = (1.4793)\exp\!\left(-(2.0288)^2(0.5000)\right) = 1.4793\,e^{-2.05801} = (1.4793)(0.12771) = \mathbf{0.18892}
$$

  
$$
T(0, 320 s) = T_\infty + 0.18892\,\theta_i = 20.0 + (0.18892)(100.0) = \mathbf{38.89 °C}
$$
- **(c)** At the outer surface $r = R$, $\theta(R,t) = (\theta_s/\theta_c)\,\theta(0,t) = (0.4421)(18.892 K) = 8.352 K$, so $T(R, 320 s) = 20.0 + 8.35 = \mathbf{28.35 °C}$ (a $10.54 °C$ radial temperature drop from center to surface!).

#### Problem P13.8: Diurnal & Annual Periodic Thermal Wave Penetration in Soil `[§13.3 | 5.c.iii | National / Invitational | 75 s | Damped Wave $\delta_{\mathrm{wave}} = \sqrt{2\alpha/\omega}$ | Trap: forgetting factor of $2\pi$ in angular frequency $\omega = 2\pi/P$]`

When the surface of a semi-infinite soil half-space ($\alpha_{\mathrm{soil}} = 5.40×10^{-7} m^2/s$, Table `tab:10:k-hierarchy`) experiences a sinusoidal temperature oscillation $T(0,t) - \bar{T} = \Delta T_0 \cos(\omega t)$ of period $P$ ($\omega = 2\pi/P$), the subsurface temperature wave decays exponentially and lags in phase according to Lienhard §5.6 Eq. (5.65), p. 244  **[S12]**:

$$
T(x,t) - \bar{T} = \Delta T_0 \exp\!\left(-\frac{x}{\delta_{\mathrm{wave}}}\right)\cos\!\left(\omega t - \frac{x}{\delta_{\mathrm{wave}}}\right), \qquad \delta_{\mathrm{wave}} = \sqrt{\frac{2\alpha}{\omega}} = \sqrt{\frac{\alpha P}{\pi}}
$$

Calculate the $1/e$ thermal-wave damping depth $\delta_{\mathrm{wave}}$ and the depth $x_{\pi} = \pi\delta_{\mathrm{wave}}$ where the subsurface temperature is exactly $180^\circ$ out of phase with the surface (warmest in winter, coolest in summer!) for (a) the diurnal 24-hour cycle ($P_{\mathrm{day}} = 86400 s$), and (b) the annual 365-day seasonal cycle ($P_{\mathrm{yr}} = 3.1536×10^{7} s$).

**Solution P13.8:** 
- **(a)** **Diurnal (24-Hour) Wave:**
  
$$
\delta_{\mathrm{day}} = \sqrt{\frac{(5.40×10^{-7} m^2/s)(86400 s)}{\pi}} = \sqrt{0.014851 m^2} = \mathbf{0.1219 m} = \mathbf{12.19 cm}, \qquad
    x_{\pi,\mathrm{day}} = \pi(0.1219 m) = \mathbf{0.3829 m}
$$
- **(b)** **Annual (365-Day) Seasonal Wave ($\sqrt{365} = 19.105\times$ deeper):**
  
$$
\delta_{\mathrm{yr}} = 19.105(0.12186 m) = \mathbf{2.328 m}, \qquad
    x_{\pi,\mathrm{yr}} = \pi(2.328 m) = \mathbf{7.314 m} \quad (\text{where amplitude is } e^{-\pi} = \mathbf{4.32\%}\text{ of }\Delta T_0)
$$

#### Problem P13.9: Two-Stage 2027 Collector Heating + Post-Lamp Extraction Cooldown Before ES Probe Reading `[§13.2 | 5.II.e–g | 2027 Part II Prediction | 75 s | Piecewise ODE Solution | Trap: forgetting the 30-to-45 s cooling drop between lamp shutoff and ES thermometer reading]`

At the end of an announced $t_1 = 720.0 s$ ($12.00 min$) heating period in a room at $T_{\mathrm{room}} = 21.00 °C$, a team's water cup reaches $T_1 = 47.80 °C$ inside the collector. At $t = t_1$, the heat lamp is turned off ($P_{\mathrm{abs}} = 0$). It takes $\Delta t_{\mathrm{in}} = 20.0 s$ inside the closed collector ($\tau_{\mathrm{in}} = 1200 s$) before the team opens the top and extracts the cup, followed by $\Delta t_{\mathrm{out}} = 25.0 s$ on the open table ($\tau_{\mathrm{out}} = 480.0 s$ due to exposed sidewall convection and uncovered evaporation) before the Event Supervisor's probe settles. Calculate the exact final measured temperature $T_f$ and the prediction error if the team forgets to subtract post-lamp extraction cooling.

**Solution P13.9:** 
During the $\Delta t_{\mathrm{in}} = 20.0 s$ dwell inside the collector with the lamp off:

$$
T_2 = T_{\mathrm{room}} + \left(T_1 - T_{\mathrm{room}}\right)e^{-\Delta t_{\mathrm{in}}/\tau_{\mathrm{in}}} = 21.00 + (47.80 - 21.00)e^{-20.0/1200} = 21.00 + 26.80(0.98347) = \mathbf{47.36 °C}
$$

During the $\Delta t_{\mathrm{out}} = 25.0 s$ open-table exposure before the probe reading settles:

$$
T_f = T_{\mathrm{room}} + \left(T_2 - T_{\mathrm{room}}\right)e^{-\Delta t_{\mathrm{out}}/\tau_{\mathrm{out}}} = 21.00 + (47.357 - 21.00)e^{-25.0/480.0} = 21.00 + 26.357(0.94925) = \mathbf{46.02 °C}
$$

Post-lamp wait and extraction cooling drops the measured temperature by $\Delta T_{\mathrm{cool}} = 47.80 - 46.02 = \mathbf{-1.78 °C}$! Including this two-stage decay factor in the team's prediction chart recovers $\frac{1.78}{46.02}\times 20 = \mathbf{+0.77 PS points}$ in final tournament score!

#### Problem P13.10: Semi-Infinite Wall Instantaneous Surface Heat Flux $q''_s(t)$ and Cumulative Absorbed Energy $Q''(t)$ `[§13.3 | 5.c.iii | National / Cornell E1 | 75 s | Effusivity Integral | Trap: forgetting factor of 2 when integrating $t^{-1/2}$ from $0$ to $t$]`

A thick concrete slab ($k = 1.30 W/m/K$, $\rho = 2300 kg/m^3$, $c_p = 880 J/kg/K$, effusivity $b = \sqrt{k\rho c_p} = 1622.1 J/m^2/K/s^1/2$, Lienhard §5.6 Eq. 5.53, p. 233  **[S12]**) is initially at uniform temperature $T_i = 18.0 °C$. At $t = 0$, its surface temperature is suddenly raised to $T_s = 58.0 °C$ ($\Delta T_s = 40.0 K$). Compute (a) the instantaneous surface heat flux $q''_s(t) = \frac{b\,\Delta T_s}{\sqrt{\pi t}}$ at $t = 100.0 s$, and (b) the total cumulative thermal energy per unit area $Q''(t) = \int_0^t q''_s(t')\,dt'$ absorbed during the first $100.0 s$.

**Solution P13.10:** 
- **(a)** Differentiating $\frac{T(x,t)-T_s}{T_i-T_s} = \mathrm{erf}\!\left(\frac{x}{2\sqrt{\alpha t}}\right)$ at $x = 0$ gives $q''_s(t) = -k\left.\frac{\partial T}{\partial x}\right|_{x=0} = \frac{k(T_s - T_i)}{\sqrt{\pi\alpha t}} = \frac{b\,\Delta T_s}{\sqrt{\pi t}}$:
  
$$
q''_s(100.0 s) = \frac{(1622.1)(40.0 K)}{\sqrt{\pi(100.0 s)}} = \frac{64884}{17.7245} = \mathbf{3661 W/m^2} = \mathbf{3.661 kW/m^2}
$$
- **(b)** Because $\int_0^t (t')^{-1/2}\,dt' = 2 t^{1/2}$, the cumulative energy absorbed per unit area from $0$ to $t$ is **exactly twice** the product $q''_s(t)\cdot t$:
  
$$
Q''(100.0 s) = \frac{2 b\,\Delta T_s \sqrt{t}}{\sqrt{\pi}} = 2\,q''_s(100.0 s)\,(100.0 s) = 2(3660.7 W/m^2)(100.0 s) = \mathbf{7.321×10^{5} J/m^2} = \mathbf{732.1 kJ/m^2}
$$

#### Problem P13.11: Optimal Parasitic Thermal-Mass Tradeoff of a Metallic Cup Sleeve in a 10-Minute Sprint `[§13.2 | 3.e, 5.II.e | 2027 Device Optimization | 75 s | Differentiating $T(t)$ wrt $C_{\mathrm{eff}}$ | Trap: adding a heavy metal cup holder that steals heat capacity from the 100 g water]`

In a $600.0 s$ ($10.00 min$) heating run at $T_{\mathrm{start}} = T_{\mathrm{room}} = 21.00 °C$, a bare $100.0 g$ water cup ($C_w = 420.5 J/K$, $R_{\mathrm{th}} = 2.400 K/W$) absorbs $P_{\mathrm{abs},0} = 16.50 W$. A student proposes adding a dry external black-anodized aluminum absorber collar around the cup sidewall that increases absorbed radiant power by $+\Delta P_{\mathrm{abs}} = +1.50 W$ (to $P_{\mathrm{abs},1} = 18.00 W$), but adds aluminum mass $m_{\mathrm{Al}} = 120.0 g$ ($c_{p,\mathrm{Al}} = 900 J/kg/K \implies \Delta C_{\mathrm{Al}} = 108.0 J/K$). Does the heavy aluminum collar increase or decrease the water temperature at $t = 600.0 s$, and what is the maximum allowable aluminum mass $m_{\mathrm{Al,max}}$ before the parasitic heat capacity outweighs the $+1.50 W$ optical gain?

**Solution P13.11:** 
- **(a)** **Baseline Bare Cup ($C_0 = 420.5 J/K$, $\tau_0 = C_0 R_{\mathrm{th}} = 1009.2 s$):**
  
$$
\Delta T_0(600 s) = P_{\mathrm{abs},0} R_{\mathrm{th}}\left(1 - e^{-600/1009.2}\right) = (16.50)(2.400)\left(1 - e^{-0.59453}\right) = 39.60(0.44818) = \mathbf{+17.75 °C}
$$
- **(b)** **With $120.0 g$ Aluminum Collar ($C_1 = 420.5 + 108.0 = 528.5 J/K$, $\tau_1 = C_1 R_{\mathrm{th}} = 1268.4 s$):**
  
$$
\Delta T_1(600 s) = (18.00)(2.400)\left(1 - e^{-600/1268.4}\right) = 43.20(0.37689) = \mathbf{+16.28 °C} \quad (\mathbf{-1.47 °C}\text{ WORSE!})
$$

  Even though the collar captures $+1.50 W$ more power, its $108 J/K$ parasitic heat capacity slows the initial heating rate $(dT/dt)_0 = P_{\mathrm{abs}}/C_{\mathrm{eff}}$ from $2.354 °C/min$ down to $2.044 °C/min$!
- **(c)** **Breakeven Mass Cutoff at $t = 600 s$:** Requiring $\Delta T_1(600 s) \ge 17.748 °C$ gives $1 - e^{-600/\tau_1} \ge \frac{17.748}{43.20} = 0.41083 \implies \tau_1 \le \frac{600}{-\ln(0.58917)} = 1134.1 s \implies C_1 \le \frac{1134.1}{2.400} = 472.5 J/K \implies \Delta C_{\mathrm{Al}} \le 52.0 J/K \implies m_{\mathrm{Al,max}} = \mathbf{57.8 g}$ (and for a $25 µm$ foil sleeve of mass $1.5 g$, $\Delta C = 1.35 J/K$, giving $\Delta T = \mathbf{+19.26 °C}$, a net gain of $+1.51 °C$!).

#### Problem P13.12: Multi-Stage Linearly Ramped Heating Followed by Isothermal Hold `[§13.3 | 5.c.iii | National / Invitational | 75 s | Superposition of Ramp + Step | Trap: failing to carry the end-of-ramp lag $-b\tau(1-e^{-t_1/\tau})$ into the hold stage]`

A sample of thermal time constant $\tau = 100.0 s$ starts in equilibrium with a programmable furnace at $T(0) = T_f(0) = 20.00 °C$. From $t = 0$ to $t_1 = 200.0 s$, the furnace ramps linearly upward at $b = 0.500 °C/s$ to $T_f(200 s) = 120.00 °C$, and then holds constant at $T_f = 120.00 °C$ for $t > 200.0 s$. Calculate the sample temperature $T(t)$ (a) at the end of the ramp ($t_1 = 200.0 s$), and (b) after $100.0 s$ of the isothermal hold ($t_2 = 300.0 s$).

**Solution P13.12:** 
- **(a)** At the end of the linear ramp ($t_1 = 200.0 s = 2.00\,\tau$), Eq. Eq. (`eq:13:ramp-lag`) gives:
  
$$
T(200 s) = T_f(200 s) - b\tau\left(1 - e^{-t_1/\tau}\right) = 120.00 - (0.500)(100.0)\left(1 - e^{-2.00}\right) = 120.00 - 50.00(0.86466) = \mathbf{76.77 °C}
$$
- **(b)** During the isothermal hold ($t \ge t_1$, furnace fixed at $T_f = 120.00 °C$), the remaining deficit $\Delta T_1 = 120.00 - 76.767 = 43.233 K$ decays exponentially over $\Delta t = t_2 - t_1 = 100.0 s = 1.00\,\tau$:
  
$$
T(300 s) = 120.00 - (43.233)e^{-100.0/100.0} = 120.00 - 43.233(0.36788) = 120.00 - 15.905 = \mathbf{104.10 °C}
$$

—
**See also:** §`sec:01.12` (`QS-12` Transient Fast Sheet), §`sec:10` (Conduction & Diffusivity), §`sec:11` (Convection & Stratification), §`sec:12` (Radiation Laws), §`sec:15` (4-Node Collector Circuit), §`sec:16` (36-Run DOE Calibration & $\mathrm{PE}$ Prediction), §`sec:17` (Thermometer $5\tau_p$ Lag), §`sec:18` (Semi-Log Regression).
