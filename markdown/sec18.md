<!-- Source: src/sec18.tex | Tab: Tab 7: LAB/DATA | Target: 8 pp -->
# §18: Graphs, Data & Experimental Analysis (Semi-Log Linearization, Residual Diagnostics, Interpolation & Numerical Table Extraction) {#sec:18}

> **[SCOPE: REQUIRED | 2027 Rules 5.I.b, 5.d.i–iv & 5.II (All Tournament Levels)]**

Across the $N = 8$ Division C tournament corpus (§`sec:22`), graph interpretation (`FMT-4`: $12.2\%$ of points) and experimental table/apparatus analysis (`FMT-5`: $20.2\%$ of the 2027 Cornell Invitational `E1`, including Tiebreaker `#1` worth $16.0\text{ pts}$!) carry decisive medal and tiebreaker weight  **[S25,S26,S28]**. Moreover, 2027 Rule `5.I.d.iv` strictly mandates that *“No questions may require trigonometry or calculus”*  **[S01,S06]**. This chapter equips competitors with zero-calculus algebraic tools to extract slopes, integrals, steam-table properties, linearized time constants ($\tau$), activation/vaporization enthalpies ($\Delta H_{\mathrm{vap}}$), ordinary least-squares (OLS) regression uncertainties, residual diagnostics, and Grubbs outlier tests in seconds.

## Systematic Reading of Thermodynamic Graphs & Coordinate Transformations

Whenever a graph appears on a written test, execute the **4-Step Axis Audit** before touching your calculator: (1) read the exact axis variable and **SI prefix/unit** (e.g., $P$ in $kPa$ vs. $MPa$ vs. $atm$; $V$ in $L$ vs. $cm^3$ vs. $m^3$; $1000/T$ in $/K$ vs. $T$ in $°C$); (2) check whether axes are **linear, semi-logarithmic ($\ln y$ or $\log_{10} y$), or log-log**; (3) check whether the origin $(0,0)$ is shown or suppressed; and (4) identify whether the physical quantity needed is a **point coordinate**, a **chord/tangent slope**, a **horizontal plateau width**, or a **signed enclosed area**.

**Table:** Master Guide to Extracting Physical Quantities from the Six Canonical Thermodynamic Graphs  **[S12,S13,S25,S26]**.

| **Graph Type** | **Axes $(x, y)$** | **What the Slope $\Delta y/\Delta x$ Means** | **What Plateau / Area Means** | **Classic Exam Trap & Unit Rule** |
| --- | --- | --- | --- | --- |
| **1. 5-Stage Heating / Cooling Curve** (§`sec:04`) | $x = Q$ $[J]$ or $t$ $[s]$ <br> $y = T$ $[°C\text{ or }K]$ | $\text{Slope} = \dfrac{\Delta T}{\Delta Q} = \dfrac{1}{m c_p}$ <br> (or $\dfrac{\Delta T}{\Delta t} = \dfrac{\dot{Q}_{\mathrm{net}}}{m c_p}$) | **Horizontal Plateau** ($\Delta T = 0$): <br> $L = \dfrac{\Delta Q_{\mathrm{plateau}}}{m} = \dfrac{\dot{Q}\,\Delta t_{\mathrm{plat}}}{m}$ | **Steeper slope $=$ LOWER specific heat $c_p$!** Ice slope ($2.10 J/g/K$) is $2\times$ steeper than liquid water ($4.184 J/g/K$). |
| **2. Unary $P$–$T$ Phase Diagram** (§`sec:05`) | $x = T$ $[K]$ <br> $y = P$ (or $\log_{10} P$) | Clapeyron co-existence slope: <br> $\dfrac{dP}{dT} = \dfrac{\Delta H_{\mathrm{trans}}}{T\,\Delta V_{\mathrm{trans}}}$ | Triple point $(T_{\mathrm{tp}}, P_{\mathrm{tp}})$: 3 phases coexist ($F=0$). Critical point $(T_c, P_c)$: L–V line ends. | $\mathrm{H_2O}$ solid–liquid line has **negative** slope ($v_{\mathrm{ice}} > v_{\mathrm{liq}}$); $\mathrm{CO_2}$ has positive S–L slope and $P_{\mathrm{tp}} = 5.11 atm > 1 atm$. |
| **3. Binary Alloy $T$–$w_B$ Phase Diagram** (§`sec:05`) | $x = w_B$ (wt% or mol%) <br> $y = T$ $[°C\text{ or }K]$ | Liquidus $T_L(w_B)$ (top boundary); Solidus $T_S(w_B)$ (bottom boundary). | **Horizontal Tie Line** in $L+\alpha$ zone: <br> $f_L = \dfrac{w_0 - w_\alpha}{w_L - w_\alpha},\ f_\alpha = \dfrac{w_L - w_0}{w_L - w_\alpha}$ | **Opposite-Arm Lever Rule:** Fraction of phase $L$ uses the segment length on the *opposite* ($\alpha$) side of overall composition $w_0$ (`E1 Q10–14, Q30` **[S25]**). |
| **4. $P$–$V$ Work & Cycle Diagram** (§`sec:07`, §`sec:09`) | $x = V$ $[m^3\text{ or }L]$ <br> $y = P$ $[Pa\text{ or }kPa]$ | Isotherm slope $= -\dfrac{P}{V}$; <br> Adiabat slope $= -\gamma\dfrac{P}{V}$ (steeper!). | **Area under path:** $W_{\mathrm{by}} = \int P\,dV$. <br> **Enclosed loop area:** $\|W_{\mathrm{net}}\|$. | $kPa\timesL = \mathbf{1 J}$! Clockwise loop: $W_{\mathrm{net,by}} > 0$ (engine); Counterclockwise: $W_{\mathrm{net,by}} < 0$ (refrigerator/pump). |
| **5. $T$–$S$ Entropy & Cycle Diagram** (§`sec:08`, §`sec:09`) | $x = S$ $[J/K]$ <br> $y = T$ $[K]$ | Isochoric slope $= \dfrac{T}{n C_{V,m}}$; <br> Isobaric slope $= \dfrac{T}{n C_{P,m}}$ (shallower!). | **Area under rev. path:** $Q_{\mathrm{rev}} = \int T\,dS$. <br> **Enclosed loop area:** $Q_{\mathrm{net}} = W_{\mathrm{net}}$. | $T$ **must be in Kelvin ($K$)** when computing area $\int T\,dS$! Carnot cycle is a rectangle: $W_{\mathrm{net}} = (T_H - T_C)\Delta S$. |
| **6. Transient Collector Curve $T(t)$** (§`sec:13`, §`sec:16`) | $x = t$ $[s\text{ or }min]$ <br> $y = T(t)$ $[°C]$ | Initial tangent slope at $t=0$: <br> $\left(\dfrac{dT}{dt}\right)_0 = \dfrac{P_{\mathrm{abs}}}{C_{\mathrm{eff}}} = \dfrac{T_{\mathrm{ss}} - T_i}{\tau}$ | Asymptote $T_{\mathrm{ss}} = T_{\mathrm{room}} + P_{\mathrm{abs}}R_{\mathrm{th}}$. <br> At $t = \tau$: $T(\tau) - T_i = 63.21%(T_{\mathrm{ss}} - T_i)$. | Initial tangent intersects horizontal asymptote $y = T_{\mathrm{ss}}$ at exactly $t = \mathbf{1\tau}$ (§`sec:13`, Fig. `fig:13:lumped-heating`)! |

### [SHORTCUT: Fast Cycle Coordinate Translator: $P$–$V \Longleftrightarrow T$–$S \Longleftrightarrow P$–$T \Longleftrightarrow V$–$T$ (`MIT E2 P2b, GGSO E4 Q12`  **[S26,S28]**)]

To translate any 4-step ideal-gas cycle across unfamiliar coordinate planes in $<15\text{ s}$, map each leg by its invariant equation:
- **Isochoric ($V = \text{const}$):** Vertical line on $P$–$V$; straight line through origin ($P = \frac{nR}{V}T$, slope $\propto 1/V$) on $P$–$T$; exponential curve $T = T_1 e^{(S-S_1)/(nC_{V,m})}$ (steeper than isobar by factor $\gamma = C_P/C_V$) on $T$–$S$.
- **Isobaric ($P = \text{const}$):** Horizontal line on $P$–$V$ and $P$–$T$; straight line through origin ($V = \frac{nR}{P}T$, slope $\propto 1/P$) on $V$–$T$; exponential curve $T = T_1 e^{(S-S_1)/(nC_{P,m})}$ (shallower than isochor) on $T$–$S$.
- **Isothermal ($T = \text{const}$):** Hyperbola $P = nRT/V$ on $P$–$V$; horizontal line on $T$–$S$; vertical line on $P$–$T$ and $V$–$T$.
- **Reversible Adiabatic / Isentropic ($S = \text{const}$):** Steep curve $PV^\gamma = \text{const}$ on $P$–$V$; **vertical line** on $T$–$S$; power curve $P \propto T^{\gamma/(\gamma-1)}$ on $P$–$T$.

## Steam Table & Property Table Extraction: 1D Linear, 2D Bilinear & Finite Differences

### 1. Pure-Substance State-Identification Protocol ($T, P, v, u, h, s, x$)

Given any two independent intensive properties of water/steam (Appendix A Table A.3  **[S09]**), compare against saturation values at the given $T$ or $P$:
- **Compressed (Subcooled) Liquid** ($T < T_{\mathrm{sat}}(P)$, or $P > P_{\mathrm{sat}}(T)$, or $y < y_f$ for $y \in \{v, u, h, s\}$): Approximate by saturated liquid at the **given temperature $T$**: $u(T,P) \approx u_f(T)$, $v(T,P) \approx v_f(T)$, $s(T,P) \approx s_f(T)$, and include the small pressure-work correction for enthalpy:
  
$$
\begin{aligned}

    h(T,P) \approx h_f(T) + v_f(T)\,\left[P - P_{\mathrm{sat}}(T)\right]
\end{aligned}
$$
- **Saturated Two-Phase Liquid–Vapor Mixture** ($T = T_{\mathrm{sat}}(P)$ and $y_f \le y \le y_g$): Compute **vapor quality** $x = \frac{m_{\mathrm{vapor}}}{m_{\mathrm{total}}} \in [0, 1]$ from the known property $y \in \{v, u, h, s\}$, then evaluate all other properties via the linear lever rule ($y_{fg} \equiv y_g - y_f$):
  
$$
\begin{aligned}

    x = \frac{y - y_f}{y_g - y_f} = \frac{y - y_f}{y_{fg}} \quad\Longrightarrow\quad h = h_f + x\,h_{fg},\quad s = s_f + x\,s_{fg},\quad u = u_f + x\,u_{fg},\quad v = v_f + x\,v_{fg}
\end{aligned}
$$
- **Superheated Vapor** ($T > T_{\mathrm{sat}}(P)$, or $P < P_{\mathrm{sat}}(T)$, or $y > y_g$): Use 1D linear or 2D bilinear interpolation in the Superheated Steam Table (or at low pressure $P \ll P_c$ where $Z \approx 1$, use ideal-gas relations $\Delta h \approx c_{p,\mathrm{steam}}\Delta T$ and $\Delta s \approx c_{p,\mathrm{steam}}\ln(T_2/T_1) - R_w\ln(P_2/P_1)$ with $R_w = R/M_{\mathrm{H_2O}} = 0.46152 kJ/kg/K$).

### 2. 1D Linear Interpolation, 2D Bilinear Interpolation & Central Finite Differences

### [FORMULA & DECISION CARD: Algebra-Only Table Interpolation & Finite-Difference Derivative Formulas (`Rule 5.d.iv`)]
- **1D Linear Interpolation & Inverse Interpolation between $(x_1, y_1)$ and $(x_2, y_2)$:**
  
$$
\begin{aligned}

    y(x) = y_1 + \left(\frac{x - x_1}{x_2 - x_1}\right)(y_2 - y_1) = (1 - f)\,y_1 + f\,y_2 \quad\text{where } f = \frac{x - x_1}{x_2 - x_1} \in [0, 1]; \qquad x(y) = x_1 + \left(\frac{y - y_1}{y_2 - y_1}\right)(x_2 - x_1)
\end{aligned}
$$
- **2D Bilinear Interpolation on a Rectangular $(T, P)$ Table Grid $[T_1, T_2] \times [P_1, P_2]$:**
  Given four corner table entries $h_{11} = h(T_1,P_1)$, $h_{21} = h(T_2,P_1)$, $h_{12} = h(T_1,P_2)$, and $h_{22} = h(T_2,P_2)$, define fractional coordinates $f_T = \frac{T - T_1}{T_2 - T_1}$ and $f_P = \frac{P - P_1}{P_2 - P_1}$. First interpolate along $T$ at each pressure, then interpolate along $P$:
  
$$
\begin{aligned}

    \begin{aligned}
      h(T, P_1) &= h_{11} + f_T(h_{21} - h_{11}), \qquad h(T, P_2) = h_{12} + f_T(h_{22} - h_{12}) \\
      h(T, P) &= h(T, P_1) + f_P\left[h(T, P_2) - h(T, P_1)\right] = (1-f_T)(1-f_P)h_{11} + f_T(1-f_P)h_{21} + (1-f_T)f_P h_{12} + f_T f_P h_{22}
    \end{aligned}
\end{aligned}
$$
- **Central, Forward & Backward Finite-Difference Derivatives from Discrete Table Rows (spacing $\Delta T$):**
  When a competition problem asks for $\frac{dP_{\mathrm{sat}}}{dT}$ in the Clapeyron equation $\frac{dP_{\mathrm{sat}}}{dT} = \frac{h_{fg}}{T v_{fg}}$ (`2027 Cornell E1 Q27–28`  **[S25]**) or heat capacity $C_P = \left(\frac{\partial H}{\partial T}\right)_P$ from a table of discrete temperatures $T - \Delta T, T, T + \Delta T$:
  
$$
\begin{aligned}

    \underbrace{\left(\frac{\Delta y}{\Delta T}\right)_{\mathrm{central}} = \frac{y(T + \Delta T) - y(T - \Delta T)}{2\,\Delta T}}_{\text{**Second-Order Accurate**} \mathcal{O}(\Delta T^2)\text{ --- **Always Prefer!**}}, \qquad
    \left(\frac{\Delta y}{\Delta T}\right)_{\mathrm{fwd}} = \frac{y(T + \Delta T) - y(T)}{\Delta T}, \qquad
    \left(\frac{\Delta y}{\Delta T}\right)_{\mathrm{bwd}} = \frac{y(T) - y(T - \Delta T)}{\Delta T}
\end{aligned}
$$

  *(Why central difference wins: The quadratic Taylor curvature terms $+\frac{1}{2}y''(T)\Delta T^2$ and $-\frac{1}{2}y''(T)\Delta T^2$ cancel identically when subtracting $y(T+\Delta T) - y(T-\Delta T)$, reducing table derivative error by $10\times\text{--}30\times$ compared to one-sided differences!)*

### Worked Example — Steam-Table Quality, 2D Bilinear Interpolation & Central-Difference Clapeyron Audit `[`2027 Cornell E1 Q27–29`  **[S09,S25]**]`

(a) From the NIST saturation table (§`app:A`), water at $T = 85.0 °C$ has $P_{\mathrm{sat}} = 57.868 kPa$, $h_f = 355.96 kJ/kg$, $h_g = 2651.7 kJ/kg$, $s_f = 1.1346 kJ/kg/K$, and $s_g = 7.5445 kJ/kg/K$. Find the vapor quality $x$ and specific enthalpy $h$ of wet steam at $85.0 °C$ having $s = 5.942025 kJ/kg/K$.
(b) In a superheated steam table grid, $h(160 °C, 0.30 MPa) = 2782.3 kJ/kg$, $h(180 °C, 0.30 MPa) = 2824.4 kJ/kg$, $h(160 °C, 0.40 MPa) = 2776.1 kJ/kg$, and $h(180 °C, 0.40 MPa) = 2819.5 kJ/kg$. Compute $h(172.0 °C, 0.350 MPa)$ via 2D bilinear interpolation.
(c) Using $P_{\mathrm{sat}}(95.0 °C) = 84.609 kPa$, $P_{\mathrm{sat}}(105.0 °C) = 120.90 kPa$, and at $100.0 °C$ ($373.15 K$): $v_f = 0.0010435 m^3/kg$, $v_g = 1.6718 m^3/kg$, estimate the latent heat of vaporization $h_{fg}(100.0 °C)$ via the central finite-difference Clapeyron equation and compare to the exact NIST value $2256.4 kJ/kg$.
**Solution.**
(a) Since $s_f < s < s_g$, the state is inside the two-phase dome. By Eq. (`eq:18:quality`):
$$x = \frac{s - s_f}{s_g - s_f} = \frac{5.942025 - 1.1346}{7.5445 - 1.1346} = \frac{4.807425}{6.4099} = \mathbf{0.75000} \implies h = 355.96 + 0.75000(2651.7 - 355.96) = \mathbf{2077.77 kJ/kg}$$
(b) Fractional coordinates: $f_T = \frac{172.0 - 160.0}{180.0 - 160.0} = 0.600$ and $f_P = \frac{0.350 - 0.300}{0.400 - 0.300} = 0.500$. By Eq. (`eq:18:bilinear`):

$$
\begin{aligned}
h(172 °C, 0.30 MPa) &= 2782.3 + 0.600(2824.4 - 2782.3) = 2807.56 kJ/kg \\
  h(172 °C, 0.40 MPa) &= 2776.1 + 0.600(2819.5 - 2776.1) = 2802.14 kJ/kg \\
  h(172.0 °C, 0.350 MPa) &= 2807.56 + 0.500(2802.14 - 2807.56) = \mathbf{2804.85 kJ/kg}
\end{aligned}
$$

(c) By Eq. (`eq:18:finitediff`) with $\Delta T = 5.0 K$, the central-difference saturation slope at $100.0 °C$ is $\left(\frac{\Delta P}{\Delta T}\right)_{\mathrm{central}} = \frac{120.90 - 84.609}{2(5.0)} = 3.6291 kPa/K$. With $v_{fg} = v_g - v_f = 1.6718 - 0.0010435 = 1.6707565 m^3/kg$, the Clapeyron equation yields:
$$h_{fg} = T\,v_{fg}\left(\frac{\Delta P}{\Delta T}\right)_{\mathrm{central}} = (373.15 K)(1.6707565 m^3/kg)(3.6291 kPa/K) = \mathbf{2262.5 kJ/kg} \quad (\text{only } \mathbf{+0.27\%}\text{ from NIST }2256.4 kJ/kg\text{!})$$
*(By contrast, a one-sided forward difference $\frac{120.90 - 101.42}{5.0} = 3.896 kPa/K$ gives $2429 kJ/kg$, a $+7.6\%$ error!)*

**✓ Verified by:** Lagrange 4-corner expansion $0.2(2782.3)+0.3(2824.4)+0.2(2776.1)+0.3(2819.5)=2804.85 kJ/kg$ and Python check `sec18:ex18.1`.

## Graphical Slope & Zero-Calculus Geometric / Trapezoidal Area Integration (`Rule 5.d.iii–iv`)

Under Rule `5.I.d.iii–iv`, every thermodynamic integral — boundary work $W_{\mathrm{by}} = \int_{V_1}^{V_2} P\,dV$, reversible heat transfer $Q_{\mathrm{rev}} = \int_{S_1}^{S_2} T\,dS$, enthalpy change $\Delta H = \int_{T_1}^{T_2} C_P(T)\,dT$, or total band radiance $L_{\mathrm{band}} = \int_{\lambda_1}^{\lambda_2} L_\lambda(\lambda,T)\,d\lambda$ (`2027 Cornell E1 Q36d`  **[S25]**) — can be evaluated without calculus by **geometric decomposition** or the **composite trapezoidal rule**:
- **Geometric Shape Decomposition on $P$–$V$ and $T$–$S$ Diagrams (`GGSO E4 Q12–13, Cornell E6 Sec IV`  **[S28,S30]**):**
- *Straight-Line Chord from $(V_1, P_1)$ to $(V_2, P_2)$:* The region under a straight chord down to $P=0$ is a **trapezoid** of mean height $P_{\mathrm{avg}} = \frac{1}{2}(P_1 + P_2)$:
    
$$
\begin{aligned}

      W_{\mathrm{by,chord}} = \frac{P_1 + P_2}{2}\,(V_2 - V_1)
\end{aligned}
$$
- *Closed Polygonal Cycle (Triangle, Rectangle, Parallelogram, Trapezoid):*
    $$\left|W_{\mathrm{net,triangle}}\right| = \frac{1}{2}\,\Delta V_{\mathrm{base}}\,\Delta P_{\mathrm{height}}, \qquad \left|W_{\mathrm{net,rect}}\right| = (V_{\max} - V_{\min})(P_{\max} - P_{\min})$$
- *Circular or Elliptical Cycle / Quarter-Circle Arc of Semi-Axes $a = \Delta V/2$ and $b = \Delta P/2$ (`GGSO E4 Q13a`):*
    $$\left|W_{\mathrm{net,ellipse}}\right| = \pi\,a\,b = \frac{\pi}{4}(V_{\max} - V_{\min})(P_{\max} - P_{\min}), \qquad A_{\mathrm{quarter\text{-}ellipse}} = \frac{\pi}{4}\,R_V\,R_P$$
- **Composite Trapezoidal Rule for Discrete Tabulated Data $(x_0, y_0), (x_1, y_1), \dots, (x_N, y_N)$:**
  
$$
\begin{aligned}

    \text{Area} \approx \sum_{k=1}^N \frac{y_{k-1} + y_k}{2}\,(x_k - x_{k-1}) \xrightarrow{\text{uniform spacing }\Delta x} \Delta x\left[\frac{1}{2}y_0 + y_1 + y_2 + \dots + y_{N-1} + \frac{1}{2}y_N\right]
\end{aligned}
$$
- **Grid-Square Counting for Continuous Plotted Curves (`Cornell E1 Q36d` Planck Curve):**
  Compute the physical energy/work value of **one grid box** $A_{\mathrm{box}} = (\Delta x_{\mathrm{box}})(\Delta y_{\mathrm{box}})$, count the number of full boxes $N_{\mathrm{full}}$ plus half the number of boundary-intersected boxes $\frac{1}{2}N_{\mathrm{partial}}$ under the curve, and multiply: $\text{Area} \approx (N_{\mathrm{full}} + 0.5\,N_{\mathrm{partial}})A_{\mathrm{box}}$.

### Worked Example — Composite Trapezoidal $P$–$V$ Work Integration from Discrete Pressure Sensor Logs `[Rule 5.d.iii–iv]`

During a non-standard gas expansion in an insulated cylinder, a data logger records pressure $P$ at five volume stations: $(V_0, P_0) = (2.00 L, 420.0 kPa)$, $(V_1, P_1) = (3.00 L, 310.0 kPa)$, $(V_2, P_2) = (4.00 L, 240.0 kPa)$, $(V_3, P_3) = (5.00 L, 195.0 kPa)$, and $(V_4, P_4) = (6.00 L, 165.0 kPa)$. Calculate the boundary work $W_{\mathrm{by}}$ done by the gas using the composite trapezoidal rule.
**Solution.**
Note that $1 kPa\times1 L = (1000 Pa)(10^{-3} m^3) = 1.000 J$. Because the volume step is uniform at $\Delta V = 1.00 L$, Eq. (`eq:18:trap`) gives:
$$W_{\mathrm{by}} = (1.00 L)\left[\frac{420.0 + 310.0}{2} + \frac{310.0 + 240.0}{2} + \frac{240.0 + 195.0}{2} + \frac{195.0 + 165.0}{2}\right]kPa = 365.0 + 275.0 + 217.5 + 180.0 = \mathbf{1037.5 J}$$

**✓ Verified by:** Uniform-step end-weighted sum $\Delta V[0.5(420.0) + 310.0 + 240.0 + 195.0 + 0.5(165.0)] = 1037.5 J$ and Python check `sec18:ex18.2`.

## Algebraic Linearization Catalog: Semi-Log Transients, Arrhenius/Clapeyron & Power Laws

Converting a curved exponential or power-law relationship into a straight line $Y = m X + b$ lets you extract physical parameters directly from the slope $m$ and intercept $b$ using a ruler or your Class III calculator's linear regression mode (§`sec:19.4`):

**Table:** Algebraic Linearization Transformations for Science Olympiad Thermodynamics (`Rule 5.d.i–iv` Compliant)  **[S12,S16,S21]**.

| **Physical Model** | **Nonlinear Governing Equation** | **Linearized Axes $(X,\ Y)$** | **Slope $m$ & Intercept $b$** | **Parameter Extraction Formulas** |
| --- | --- | --- | --- | --- |
| **1. Lumped Heating / Cooling Transient** (§`sec:13.2`, §`sec:16`) | $T(t) = T_{\mathrm{ss}} - (T_{\mathrm{ss}} - T_i)e^{-t/\tau}$ <br> ($\theta(t) = \dfrac{T(t) - T_{\mathrm{ss}}}{T_i - T_{\mathrm{ss}}} = e^{-t/\tau}$) | $X = t$ $[s\text{ or }min]$ <br> $Y = \ln\!\left(\dfrac{T(t) - T_{\mathrm{ss}}}{T_i - T_{\mathrm{ss}}}\right)$ | $m = -\dfrac{1}{\tau}$ <br> $b = 0$ | $\tau = -\dfrac{1}{m} = R_{\mathrm{th}} C_{\mathrm{eff}}$ <br> *(If $Y = \ln\|T_{\mathrm{ss}} - T(t)\|$, then $b = \ln\|T_{\mathrm{ss}} - T_i\|$)* |
| **2. Clausius–Clapeyron Vapor Pressure** (§`sec:05`) | $P_{\mathrm{sat}}(T) = P_0 \exp\!\left[-\dfrac{\Delta H_{\mathrm{vap}}}{R}\!\left(\dfrac{1}{T} - \dfrac{1}{T_0}\right)\right]$ | $X = \dfrac{1}{T}$ $[/K]$ <br> $Y = \ln P_{\mathrm{sat}}$ | $m = -\dfrac{\Delta H_{\mathrm{vap}}}{R}$ <br> $b = \ln P_0 + \dfrac{\Delta H_{\mathrm{vap}}}{R T_0}$ | $\Delta H_{\mathrm{vap}} = -R\,m$ <br> *(If $Y = \log_{10} P$, then $\Delta H_{\mathrm{vap}} = -2.302585\,R\,m$!)* |
| **3. Van't Hoff / Arrhenius Rate & Equilibrium** (§`sec:08`) | $K_{\mathrm{eq}}(T) = \exp\!\left(-\dfrac{\Delta H^\circ}{R T} + \dfrac{\Delta S^\circ}{R}\right)$ <br> $k(T) = A e^{-E_a / (R T)}$ | $X = \dfrac{1}{T}$ $[/K]$ <br> $Y = \ln K_{\mathrm{eq}}$ (or $\ln k$) | $m = -\dfrac{\Delta H^\circ}{R}$ <br> $b = +\dfrac{\Delta S^\circ}{R}$ | $\Delta H^\circ = -R\,m$ <br> $\Delta S^\circ = +R\,b$ <br> $E_a = -R\,m$ |
| **4. Polytropic Gas Process** (§`sec:07`) | $P V^n = C_{\mathrm{poly}}$ | $X = \ln V$ <br> $Y = \ln P$ | $m = -n$ <br> $b = \ln C_{\mathrm{poly}}$ | Polytropic index $n = -m$ <br> ($n=0$ isobar, $n=1$ isotherm, $n=\gamma$ adiabat) |
| **5. Convection / Lamp Scaling Power Law** (§`sec:11`, §`sec:15`) | $\mathrm{Nu} = C\,\mathrm{Ra}^n$ <br> or $\mathrm{TG}(h) = A_0 (h - z_{\mathrm{eff}})^{-n}$ | $X = \ln\mathrm{Ra}$ (or $\ln(h-z_{\mathrm{eff}})$) <br> $Y = \ln\mathrm{Nu}$ (or $\ln\mathrm{TG}$) | $m = n$ (or $-n$) <br> $b = \ln C$ | Scaling exponent $n = m$; <br> prefactor $C = e^b$ |

### [SHORTCUT: Three-Point Equidistant Algebraic Formula for Unknown $T_{\mathrm{ss}}$ (Before Semi-Log Plotting!)]

To plot $Y = \ln[(T(t) - T_{\mathrm{ss}})/(T_i - T_{\mathrm{ss}})]$ during a 10-minute heat-lamp run, you need the asymptotic stagnation temperature $T_{\mathrm{ss}}$, which has *not yet been reached* at $t = 10 min$! Pick any **three equally spaced time points** $t_1$, $t_2 = t_1 + \Delta t$, and $t_3 = t_1 + 2\Delta t$ (e.g., $t = 0, 5, 10 min$ or $t = 0, 4, 8 min$) with measured temperatures $T_1, T_2, T_3$. Because $T_{\mathrm{ss}} - T_2 = (T_{\mathrm{ss}} - T_1)e^{-\Delta t/\tau}$ and $T_{\mathrm{ss}} - T_3 = (T_{\mathrm{ss}} - T_1)e^{-2\Delta t/\tau}$, the ratio $\frac{T_{\mathrm{ss}} - T_2}{T_{\mathrm{ss}} - T_1} = \frac{T_{\mathrm{ss}} - T_3}{T_{\mathrm{ss}} - T_2} = e^{-\Delta t/\tau}$ is identical! Cross-multiplying $(T_{\mathrm{ss}} - T_2)^2 = (T_{\mathrm{ss}} - T_1)(T_{\mathrm{ss}} - T_3)$ cancels $T_{\mathrm{ss}}^2$ and gives the exact closed-form algebraic solution for $T_{\mathrm{ss}}$ and $\tau$:

$$
\begin{aligned}

  \boxed{T_{\mathrm{ss}} = \frac{T_1 T_3 - T_2^2}{T_1 + T_3 - 2\,T_2}, \qquad \tau = \frac{\Delta t}{\ln\!\left(\dfrac{T_2 - T_1}{T_3 - T_2}\right)}}
\end{aligned}
$$

> **[Vector Figure: Linearized semi-log regression plot $Y = \ln[(T_{\mathrm{ss}} - T(t))/(T_{\mathrm{ss}} - T_i)] = -t/\tau$ for extracting the thermal time constant $\tau = R_{\mathrm{th}}C_{\mathrm{eff}}$ and verifying first-order lumped-capacitance behavior (Fig. `fig:13:lumped-heating`, Worked Example `ex:18.3`). Notice that propagating a constant temperature uncertainty $u(T)$ through $Y = \ln(T_{\mathrm{ss}} - T)$ yields slightly growing semi-log error bars $u(Y_k) = u(T)/(T_{\mathrm{ss}} - T_k)$ as $T_k$ approaches $T_{\mathrm{ss}}$  **[S12,S21]**. | Label: `fig:18:semilog-fit`]**
> - **Diagram Annotations & Key Elements:** **X-Axis:** Heating Time $t$ $[min]$ ($0 s$ to $600 s$ during 2027 Collector Calibration Run) • **Y-Axis:** Linearized Log Coordinate $Y = \ln\!\left(\dfrac{T_{\mathrm{ss}} - T(t)}{T_{\mathrm{ss}} - T_i}\right)$ • **Legend:** $95\%$ OLS Regression Confidence Band ($\pm 2 s_{y|t}$) • **Legend:** OLS Best-Fit Line: $Y = -\dfrac{1}{\tau}\,t = (-0.06619 /min)\,t$ ($R^2 = 0.999997$) • **Legend:** Transformed Data $Y_k = \ln[(T_{\mathrm{ss}}-T_k)/(T_{\mathrm{ss}}-T_i)] \pm u(Y_k)$ • Slope $m = -\dfrac{1}{\tau} = -0.066194 /min \implies \tau = \mathbf{15.110 ± 0.010 min} = \mathbf{906.6 ± 0.6 s}$

## Ordinary Least Squares (OLS), Residual Diagnostics, Error Metrics & Outlier Tests

### 1. Ordinary Least Squares (OLS) Algebraic Formulas & Residual Diagnostic Patterns

Given $N$ data pairs $(x_1, y_1), \dots, (x_N, y_N)$ ($N \ge 3$), compute sample means $\bar{x} = \frac{1}{N}\sum_{k=1}^N x_k$ and $\bar{y} = \frac{1}{N}\sum_{k=1}^N y_k$, and the three centered sums of squares $S_{xx}$, $S_{yy}$, and $S_{xy}$  **[S21]**:

$$
\begin{aligned}

  \begin{aligned}
    S_{xx} &= \sum_{k=1}^N (x_k - \bar{x})^2 = \sum x_k^2 - N\bar{x}^2, \qquad S_{yy} = \sum_{k=1}^N (y_k - \bar{y})^2 = \sum y_k^2 - N\bar{y}^2, \qquad S_{xy} = \sum_{k=1}^N (x_k - \bar{x})(y_k - \bar{y}) = \sum x_k y_k - N\bar{x}\bar{y} \\
    m &= \frac{S_{xy}}{S_{xx}}, \qquad b = \bar{y} - m\,\bar{x}, \qquad R^2 = r^2 = \frac{S_{xy}^2}{S_{xx} S_{yy}} \in [0, 1], \qquad s_{y|x} = \sqrt{\frac{\sum r_k^2}{N - 2}} = \sqrt{\frac{S_{yy} - m S_{xy}}{N - 2}} \\
    u(m) &= \frac{s_{y|x}}{\sqrt{S_{xx}}} = |m|\sqrt{\frac{1/R^2 - 1}{N - 2}}, \qquad u(b) = s_{y|x}\sqrt{\frac{1}{N} + \frac{\bar{x}^2}{S_{xx}}}, \qquad u\left(\hat{y}_{\mathrm{pred}}(x_0)\right) = s_{y|x}\sqrt{1 + \frac{1}{N} + \frac{(x_0 - \bar{x})^2}{S_{xx}}}
  \end{aligned}
\end{aligned}
$$

Never rely on $R^2 > 0.99$ alone to validate a physical model! Always inspect the **residuals** $r_k = y_{\mathrm{meas},k} - \hat{y}_{\mathrm{fit}}(x_k) = y_k - (m x_k + b)$ (which satisfy $\sum_{k=1}^N r_k = 0$ and $\sum_{k=1}^N x_k r_k = 0$ identically) plotted against $x_k$ (Fig. `fig:18:residuals`):
- **Pattern A — Random White-Noise Scatter Around $r_k = 0$:** Confirms that the functional model is physically well-specified and deviations are purely random measurement noise ($|r_k| \lesssim 2 s_{y|x}$, zero trend or curvature).
- **Pattern B — Systematic U-Shaped or Inverted-U Parabolic Curvature:** Proves an **unmodeled nonlinear physical mechanism**! For example, fitting a straight line $T(t) = T_i + m t$ to a collector heating curve without accounting for exponential parasitic heat loss $(T - T_{\mathrm{room}})/R_{\mathrm{th}}$ — or choosing too high a $T_{\mathrm{ss}}$ in a semi-log plot — produces a characteristic inverted-U or U-shaped residual curve.
- **Pattern C — Step Discontinuity / Regime Jump at $t = t^*$:** Exposes an abrupt experimental disturbance during the run: e.g., the clear plastic film cap slipped off at $t = 6 min$ (triggering sudden evaporative cooling), the thermometer probe slipped deeper across the thermocline, or a phase boundary was crossed.

> **[Vector Figure: Three diagnostic residual patterns $r_k = T_{\mathrm{meas},k} - T_{\mathrm{fit},k}$ versus time $t_k$. Pattern A (random scatter inside $\pm 2u_{\mathrm{rand}}$) confirms a physically valid model; Pattern B (arch curvature) reveals unmodeled heat loss or an erroneous asymptote $T_{\mathrm{ss}}$; Pattern C (abrupt step shift) flags a mid-run probe depth shift or vapor-cover failure  **[S21]**. | Label: `fig:18:residuals`]**
> - **Diagram Annotations & Key Elements:** **X-Axis:** Heating Time $t_k$ $[min]$ Across a 10-Minute Calibration Run • **Y-Axis:** Residual $r_k = T_{\mathrm{meas},k} - T_{\mathrm{fit},k}$ $[°C]$ • **Legend:** Pattern A (Random White Noise $|r_k|\le0.05 °C$): Valid First-Order Model • **Legend:** Pattern B (Inverted-U Curvature): Unmodeled Heat Loss / Wrong $T_{\mathrm{ss}}$ • **Legend:** Pattern C (Step Drop at $t=6 min$): Probe Slipped Deeper or Vapor Cap Dislodged • Discontinuity at $t^*=6 min$

### 2. Percent Error vs. Percent Difference vs. 2027 Prediction Estimate ($\mathrm{PE}$) & Defensible Outlier Tests

- **Three Distinct Comparison Metrics (Never Confuse Their Denominators!):**
  
$$
\begin{aligned}

    \text{**\% Error**} = \frac{|x_{\mathrm{exp}} - x_{\mathrm{true}}|}{|x_{\mathrm{true}}|}\times 100\%, \quad
    \text{**\% Diff**} = \frac{|x_1 - x_2|}{\tfrac{1}{2}(x_1 + x_2)}\times 100\%, \quad
    \text{**Rule 6.f**}\mathrm{PE} = 1 - \frac{|T_f - T_{\mathrm{pred}}|}{T_f}\ (^\circ\mathrm{C})
\end{aligned}
$$

  *(Use **Percent Error** when comparing an experimental value $x_{\mathrm{exp}}$ against an authoritative NIST reference $x_{\mathrm{true}}$; use **Percent Difference** when comparing two experimental trials $x_1, x_2$ of equal standing where neither is “true”; use **Rule `6.f` $\mathrm{PE}$** with measured $T_f$ in $°C$ in the denominator for 2027 Part II scoring  **[S01]**).*
- **Defensible Outlier Identification Without Cherry-Picking (Grubbs' Test & Tukey IQR Fence)  **[S21]**:**
  Never delete a data point merely because it lowers $R^2$! An outlier $x_{\mathrm{suspect}}$ in $N$ replicate trials ($s = \sqrt{\frac{1}{N-1}\sum (x_i - \bar{x})^2}$) may be excluded **only** if (1) a physical anomaly was logged during the run (e.g., power flicker, spilled water, dislodged lid) **OR** (2) it exceeds the two-sided **Grubbs' Test critical value $G_{\mathrm{crit}}(\alpha=0.05, N)$** (or lies outside the non-parametric **Tukey Fence** $[Q_1 - 1.5\,\mathrm{IQR},\ Q_3 + 1.5\,\mathrm{IQR}]$ where $\mathrm{IQR} = Q_3 - Q_1$), and both the raw and filtered fits are reported:
  
$$
\begin{aligned}

    G = \frac{\max_{1\le i\le N}|x_i - \bar{x}|}{s} > G_{\mathrm{crit}}(\alpha=0.05, N) = \frac{N - 1}{\sqrt{N}}\sqrt{\frac{t_{\alpha/(2N),\,N-2}^2}{N - 2 + t_{\alpha/(2N),\,N-2}^2}}
\end{aligned}
$$

  
  
  
| **Sample Size $N$** | $3$ | $4$ | $5$ | $\mathbf{6}$ | $7$ | $8$ | $9$ | $10$ | $12$ | $15$ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Grubbs $G_{\mathrm{crit}}$ ($\alpha=0.05$, $95\%$)** | $1.155$ | $1.481$ | $1.715$ | $\mathbf{1.887}$ | $2.020$ | $2.126$ | $2.215$ | $2.290$ | $2.412$ | $2.549$ |
| **Grubbs $G_{\mathrm{crit}}$ ($\alpha=0.01$, $99\%$)** | $1.155$ | $1.496$ | $1.764$ | $\mathbf{1.973}$ | $2.139$ | $2.274$ | $2.387$ | $2.482$ | $2.636$ | $2.806$ |

  

## Complete End-to-End Worked Experimental Data-Analysis Set

### Worked Example — End-to-End Collector Transient Dataset: 3-Point $T_{\mathrm{ss}}$, Semi-Log OLS $\tau$, Uncertainty & Grubbs Test `[Rules 5.I.b, 5.d.i–iv, 5.II]`

A team logs water temperature $T(t)$ inside their 2027 collector ($h = 50.0 cm$, $125 W$ lamp, $T_i = T_{\mathrm{room}} = 22.00 °C$) every $2.00 min$ for $10.00 min$:

| **Time $t_k$ $[min]$** | $0.00$ | $2.00$ | $4.00$ | $6.00$ | $8.00$ | $10.00$ |
| --- | --- | --- | --- | --- | --- | --- |
| **Measured $T_k$ $[°C]$** | $22.00$ | $26.95$ | $31.32$ | $35.10$ | $38.45$ | $41.36$ |
| **Linearized $Y_k = \ln[(62.00 - T_k)/40.00]$** | $0.00000$ | $-0.13210$ | $-0.26527$ | $-0.39675$ | $-0.52975$ | $-0.66165$ |

(a) Without assuming $T_{\mathrm{ss}}$ is known, apply the 3-point equidistant formula Eq. (`eq:18:3ptTss`) to the readings at $t_1 = 0 min$, $t_2 = 4 min$, and $t_3 = 8 min$ to estimate $T_{\mathrm{ss}}$.
(b) Using the exact steady-state asymptote $T_{\mathrm{ss}} = 62.00 °C$, perform an OLS linear regression Eq. (`eq:18:ols`) of $Y_k = \ln[(T_{\mathrm{ss}} - T_k)/(T_{\mathrm{ss}} - T_i)]$ versus $t_k$ $[min]$ to determine the slope $m$, intercept $b$, $R^2$, time constant $\tau$, and standard uncertainty $u(\tau)$.
(c) Six replicate 10-minute runs at $h = 50.0 cm$ yield temperature gains $\mathrm{TG} = \{21.30,\ 21.45,\ 21.20,\ 21.35,\ 21.40,\ 18.90\}\,°C$ (where the operator noted that the BoPET film cap slipped slightly on run #6). Apply Grubbs' test at $\alpha = 0.05$ to determine whether run #6 may be rejected, and compute the clean mean $\overline{\mathrm{TG}}$ and Type A uncertainty $u_A$.
**Solution.**
(a) **Three-Point Equidistant $T_{\mathrm{ss}}$ Estimate ($t = 0, 4, 8 min \implies T_1 = 22.00,\ T_2 = 31.32,\ T_3 = 38.45\,°C$):**
By Eq. (`eq:18:3ptTss`):
$$T_{\mathrm{ss,3pt}} = \frac{T_1 T_3 - T_2^2}{T_1 + T_3 - 2 T_2} = \frac{(22.00)(38.45) - (31.32)^2}{22.00 + 38.45 - 2(31.32)} = \frac{845.9000 - 980.9424}{-2.1900} = \frac{-135.0424}{-2.1900} = \mathbf{61.663 °C}$$
*(Remarkably within $0.34 °C$ of the true $62.00 °C$ asymptote using only three points from the first 8 minutes!)*
(b) **Semi-Log OLS Regression ($N = 6$ points):**
From the table above, $\bar{t} = 5.000 min$ and $\bar{Y} = \frac{-1.98552}{6} = -0.330920$. Evaluating the sums of squares Eq. (`eq:18:ols`):
$$S_{tt} = (-5)^2 + (-3)^2 + (-1)^2 + 1^2 + 3^2 + 5^2 = \mathbf{70.000\,sq min}, \qquad S_{tY} = \sum_{k=1}^6 (t_k - \bar{t})(Y_k - \bar{Y}) = \mathbf{-4.63274\,min}, \qquad S_{YY} = \mathbf{0.3065976}$$
$$m = \frac{S_{tY}}{S_{tt}} = \frac{-4.63274}{70.000} = \mathbf{-0.0661820 /min}, \qquad b = \bar{Y} - m\bar{t} = -0.330920 - (-0.0661820)(5.000) = \mathbf{-0.000010} \approx 0$$
$$R^2 = \frac{S_{tY}^2}{S_{tt} S_{YY}} = \frac{21.46228}{21.46183} = \mathbf{0.999998}, \qquad s_{Y|t} = \sqrt{\frac{S_{YY} - m S_{tY}}{N - 2}} = \sqrt{\frac{4.89×10^{-7}}{4}} = \mathbf{3.50×10^{-4}}$$
$$u(m) = \frac{s_{Y|t}}{\sqrt{S_{tt}}} = \frac{3.50×10^{-4}}{\sqrt{70.0}} = \mathbf{4.18×10^{-5} /min} \quad\Longrightarrow\quad \tau = -\frac{1}{m} = \mathbf{15.110 min} = \mathbf{906.6 s}, \qquad u(\tau) = \tau^2 u(m) = \mathbf{0.0105 min} = \mathbf{0.63 s}$$
(c) **Grubbs' Outlier Test on the $N = 6$ Replicate $\mathrm{TG}$ Trials:**
Including all 6 trials: $\bar{x}_{\mathrm{all}} = 20.9333 °C$ and sample standard deviation $s_{\mathrm{all}} = 1.00003 °C$. Testing run #6 ($x_6 = 18.90 °C$) via Eq. (`eq:18:grubbs`):
$$G = \frac{|18.90 - 20.9333|}{1.00003} = \mathbf{2.0337} > G_{\mathrm{crit}}(\alpha=0.05, N=6) = \mathbf{1.887} \quad (\text{and } > G_{\mathrm{crit}}(\alpha=0.01, N=6) = 1.973!)$$
Because $G > G_{\mathrm{crit}}$ **and** a physical cause (slipped BoPET vapor cap) was logged, run #6 is legitimately excluded. The remaining $n = 5$ valid runs yield $\overline{\mathrm{TG}}_{\mathrm{clean}} = \mathbf{21.340 °C}$, $s_{\mathrm{clean}} = \mathbf{0.0962 °C}$, and Type A standard uncertainty $u_A = s_{\mathrm{clean}}/\sqrt{5} = \mathbf{0.0430 °C}$.

**✓ Verified by:** NumPy `polyfit` / `std(ddof=1)` exact match ($\tau = 15.1101 min$, $G = 2.03367 > 1.887$) in Python check `sec18:ex18.3`.

### Worked Example — Clausius–Clapeyron Vapor-Pressure Linear Regression & Normal Boiling Point Extraction `[`Cornell E1 FRQ 2 & GGSO E4 Q8`  **[S09,S25,S28]**]`

In a Marcet high-pressure saturation boiler experiment (`2027 Cornell E1 FRQ 2`), a student measures the vapor pressure $P_{\mathrm{sat}}$ of a volatile liquid at four temperatures:

| **Temperature $t_k$ $[°C]$ ($T_k$ $[K]$)** | $40.0\ (313.15 K)$ | $60.0\ (333.15 K)$ | $80.0\ (353.15 K)$ | $100.0\ (373.15 K)$ |
| --- | --- | --- | --- | --- |
| **Measured $P_{\mathrm{sat},k}$ $[kPa]$** | $7.384$ | $19.946$ | $47.414$ | $101.42$ |
| **Reciprocal $X_k = 1000/T_k$ $[/K]$** | $3.19336$ | $3.00165$ | $2.83166$ | $2.67989$ |
| **Log Pressure $Y_k = \ln(P_{\mathrm{sat},k}/kPa)$** | $2.00000$ | $2.99303$ | $3.85892$ | $4.61927$ |

(a) Perform an OLS linear regression of $Y = \ln(P_{\mathrm{sat}}/kPa)$ against $X = 1000/T$ $[/K]$ to determine the slope $m$, intercept $b$, and coefficient of determination $R^2$.
(b) Extract the mean molar enthalpy of vaporization $\Delta H_{\mathrm{vap}}$ $[kJ/mol]$ across $40–100 °C$ ($R = 8.3144626 J/mol/K$) and the predicted normal boiling point $T_b$ at $P_0 = 101.325 kPa$.
**Solution.**
(a) Means across $N = 4$ points: $\bar{X} = 2.926640\,/K$ and $\bar{Y} = 3.367805$. Centered sums of squares Eq. (`eq:18:ols`):
$$S_{XX} = \mathbf{0.141913}, \qquad S_{XY} = \mathbf{-0.724014}, \qquad S_{YY} = \mathbf{3.693954}$$
$$m = \frac{S_{XY}}{S_{XX}} = \frac{-0.724014}{0.141913} = \mathbf{-5.10182 K}, \qquad b = \bar{Y} - m\bar{X} = 3.367805 - (-5.10182)(2.926640) = \mathbf{18.2990}$$
$$R^2 = \frac{S_{XY}^2}{S_{XX} S_{YY}} = \frac{0.524196}{0.524220} = \mathbf{0.999954}$$
(b) Because the horizontal variable was scaled as $X = 1000/T$, the Clausius–Clapeyron relation $\ln P = -\frac{\Delta H_{\mathrm{vap}}}{1000\,R}\left(\frac{1000}{T}\right) + b$ gives slope $m = -\frac{\Delta H_{\mathrm{vap}}}{1000\,R}$, so:
$$\Delta H_{\mathrm{vap}} = -1000\,R\,m = -(1000)(8.3144626 J/mol/K)(-5.10182) = 42419 J/mol = \mathbf{42.42 kJ/mol}$$
*(Matching the arithmetic mean of NIST water $\Delta H_{\mathrm{vap}}(40 °C) = 43.35 kJ/mol$ and $\Delta H_{\mathrm{vap}}(100 °C) = 40.65 kJ/mol$, which is $42.00 kJ/mol$, within $1.0\%$!).* Setting $P_{\mathrm{sat}} = 101.325 kPa$ ($Y_0 = \ln(101.325) = 4.61833$):
$$X_b = \frac{1000}{T_b} = \frac{Y_0 - b}{m} = \frac{4.61833 - 18.2990}{-5.10182} = 2.68153\,/K \implies T_b = \frac{1000}{2.68153} = \mathbf{372.92 K} = \mathbf{99.77 °C}$$

**✓ Verified by:** Two-point check $\Delta H_{\mathrm{vap}} = R\ln(101.42/7.384)/(1/313.15 - 1/373.15) = 42.43 kJ/mol$ and Python check `sec18:ex18.4`.

### Worked Example — 5-Stage Heating-Curve Slope/Plateau Extraction & Binary Eutectic Tie-Line Lever Rule `[`Cornell E1 Q10–14, Q30 & GGSO E4 Q9`  **[S25,S28]**]`

(a) A constant-power electric heater ($\dot{Q}_{\mathrm{in}} = 250.0 W$) warms an insulated sample of mass $m = 0.400 kg$ initially solid at $T_0 = -25.0 °C$. On the plotted temperature-versus-time curve $T(t)$, the solid warms linearly from $-25.0 °C$ to the melting plateau $T_m = 15.0 °C$ over $\Delta t_{\mathrm{solid}} = 112.0 s$, remains flat at $T_m = 15.0 °C$ for $\Delta t_{\mathrm{fus}} = 288.0 s$, and then the liquid warms linearly from $15.0 °C$ to $65.0 °C$ over $\Delta t_{\mathrm{liq}} = 224.0 s$. Extract the solid specific heat $c_{\mathrm{solid}}$, latent heat of fusion $L_f$, and liquid specific heat $c_{\mathrm{liq}}$.
(b) On a binary $\mathrm{Pb\text{--}Sn}$ eutectic phase diagram at $T = 200.0 °C$ (above the $183.0 °C$ eutectic horizontal), an alloy of overall composition $w_0 = 40.0 wt\%\ Sn$ lies inside the two-phase $(\alpha + L)$ region. The horizontal tie line at $200.0 °C$ intersects the $\alpha$-solidus boundary at $w_\alpha = 18.0 wt\%\ Sn$ and the liquidus boundary at $w_L = 55.5 wt\%\ Sn$. Calculate the mass fraction of liquid phase $f_L$, mass fraction of solid $\alpha$-phase $f_\alpha$, and the mass of tin ($\mathrm{Sn}$) dissolved inside the liquid phase for a $500.0 g$ total alloy charge.
**Solution.**
(a) From Row 1 of Table `tab:18:graphs`, the heating slope of each single-phase segment is $\frac{\Delta T}{\Delta t} = \frac{\dot{Q}_{\mathrm{in}}}{m c_p} \implies c_p = \frac{\dot{Q}_{\mathrm{in}}\,\Delta t}{m\,\Delta T}$:
$$c_{\mathrm{solid}} = \frac{(250.0 W)(112.0 s)}{(0.400 kg)(15.0 - (-25.0))\,K} = \frac{28000 J}{16.0 kg · K} = \mathbf{1750 J/kg/K} = \mathbf{1.750 kJ/kg/K}$$
$$L_f = \frac{\dot{Q}_{\mathrm{in}}\,\Delta t_{\mathrm{fus}}}{m} = \frac{(250.0 W)(288.0 s)}{0.400 kg} = \frac{72000 J}{0.400 kg} = \mathbf{180000 J/kg} = \mathbf{180.0 kJ/kg}$$
$$c_{\mathrm{liq}} = \frac{(250.0 W)(224.0 s)}{(0.400 kg)(65.0 - 15.0)\,K} = \frac{56000 J}{20.0 kg · K} = \mathbf{2800 J/kg/K} = \mathbf{2.800 kJ/kg/K}$$
*(Sanity check: The liquid warming slope $\frac{50.0}{224.0} = 0.2232 °C/s$ is shallower than the solid warming slope $\frac{40.0}{112.0} = 0.3571 °C/s$ by the exact inverse ratio $\frac{c_{\mathrm{solid}}}{c_{\mathrm{liq}}} = \frac{1750}{2800} = 0.6250$!).*
(b) Applying the opposite-arm tie-line lever rule (Row 3 of Table `tab:18:graphs`) across $[w_\alpha, w_L] = [18.0, 55.5]\,\text{wt\%}$ with $w_0 = 40.0\,\text{wt\%}$:
$$f_L = \frac{w_0 - w_\alpha}{w_L - w_\alpha} = \frac{40.0 - 18.0}{55.5 - 18.0} = \frac{22.0}{37.5} = \mathbf{0.58667}\ (58.67%), \qquad f_\alpha = \frac{w_L - w_0}{w_L - w_\alpha} = \frac{55.5 - 40.0}{37.5} = \frac{15.5}{37.5} = \mathbf{0.41333}\ (41.33%)$$
For a $m_{\mathrm{tot}} = 500.0 g$ alloy sample, the total liquid phase mass is $m_L = f_L m_{\mathrm{tot}} = 0.58667(500.0 g) = 293.33 g$ (and $m_\alpha = 206.67 g$). Because the liquid phase has composition $w_L = 55.5 wt\%\ Sn$, the mass of $\mathrm{Sn}$ inside the liquid phase is:
$$m_{\mathrm{Sn,in\text{ }L}} = w_L\,m_L = (0.555)(293.333 g) = \mathbf{162.80 g}$$
*(Global Tin Conservation Audit: Tin in solid $\alpha$ is $m_{\mathrm{Sn,in\text{ }\alpha}} = w_\alpha m_\alpha = (0.180)(206.667 g) = 37.20 g$; total tin is $162.80 + 37.20 = 200.00 g = 0.400 \times 500.0 g$. Exact match!)*

**✓ Verified by:** Global energy audit $Q_{\mathrm{tot}} = 28.0 + 72.0 + 56.0 = 156.0 kJ = (250 W)(624 s)$ and tin mass balance in Python check `sec18:ex18.5`.

### [TRAP & DIAGNOSTIC: Ten High-Frequency Graph-Reading & Table-Extraction Traps on Division C Exams  **[S25,S26,S28]**]

| **Graph / Table Trap** | **Why Students Lose Points** | **5-Second Diagnostic & Fix** |
| --- | --- | --- |
| **1. $\log_{10} y$ vs. $\ln y$ Semi-Log Slope** | Reading slope $m_{10} = \Delta(\log_{10} P)/\Delta(1/T)$ and plugging directly into $\Delta H = -R m$ (off by $\ln 10 = 2.302585\times$!). | Since $\ln y = (\ln 10)\log_{10} y = 2.302585\log_{10} y$, always multiply a base-10 semi-log slope by $\mathbf{2.302585}$! |
| **2. Scaled Reciprocal Axis $1000/T$** | Plot horizontal axis is labeled $10^3/T$ $[/K]$; student forgets the $10^3$ factor and gets $\Delta H = 42.4 J/mol$ instead of $kJ/mol$. | If $X = 1000/T$, $\frac{d(\ln P)}{d(1/T)} = 1000\frac{d(\ln P)}{dX}$, so slope $m_X$ gives $\Delta H_{\mathrm{vap}}$ directly in $kJ/mol$ when multiplied by $R = 8.3145$! |
| **3. Suppressed Zero Origin $(V_0, P_0) \ne (0,0)$** | Computing area under a $P$–$V$ path down to the bottom border of the plot box when the bottom axis sits at $P_{\min} = 100 kPa > 0$! | Single-path work $W_{\mathrm{by}} = \int P\,dV$ **must integrate all the way down to absolute zero pressure $P = 0$** (add rectangle $P_{\min}\Delta V$!). |
| **4. Celsius on a $T$–$S$ Diagram** | Computing single-path reversible heat $Q_{\mathrm{rev}} = \int T\,dS$ using $T$ in $°C$ instead of $K$. | While enclosed loop area $\oint T_C\,dS = \oint T_K\,dS$ cancels the $+273.15$ offset, single-leg heat $Q_{12}$ **requires absolute Kelvin $T_K$**! |
| **5. $P$–$V$ Unit Prefix Product Trap** | Multiplying $kPa\timescm^3$ and writing $J$ (off by $10^3\times$). | Memorize: $Pa\cdotm^3 = J$;\quad $kPa\cdotL = J$;\quad $MPa\cdotL = kJ$;\quad $kPa\cdotcm^3 = 10^{-3} J$;\quad $bar\cdotL = 100 J$;\quad $atm\cdotL = 101.325 J$. |
| **6. Blind Linear Extrapolation Outside Two-Phase Dome** | Applying $x = (h - h_f)/h_{fg}$ when $h > h_g$ (getting $x = 1.18 > 1$) or $h < h_f$ (getting $x = -0.12 < 0$). | Quality $x$ is physically defined **only** for $0 \le x \le 1$! If $h > h_g$, switch to the Superheated Vapor Table; if $h < h_f$, use Subcooled Liquid Eq. (`eq:18:subcooled`). |

—
**See also:** §`sec:04`–§`sec:05` (Heating Curves, Phase Diagrams & Lever Rule), §`sec:07`–§`sec:09` ($P$–$V$ & $T$–$S$ Cycles), §`sec:13` (Lumped Transients), §`sec:16` (DOE Prediction Matrix), §`sec:17` (GUM Uncertainty Propagation), §`sec:19` (Calculator Regression Playbook), and §`app:A` (NIST Steam Tables).
