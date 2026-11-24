<!-- Source: src/sec07.tex | Tab: Tab 4: GASES/LAWS | Target: 12 pp -->
# §7: First Law of Thermodynamics, Internal Energy, Boundary Work & Master Process Atlas {#sec:07}

> **[SCOPE: REQUIRED | 2027 Rule 5.c.iv (All Tournament Levels) | Closed-System Process Atlas & Open Steady-Flow First Law]**

The First Law of Thermodynamics and ideal-gas process analysis form the quantitative backbone of Rule `5.c.iv`, accounting for $20\text{--}30\%$ of written points across the 8-exam invitational corpus  **[S25,S26,S27,S28]**. Every process work and heat equation in this chapter is formulated in closed algebraic and geometric form under Rule `5.d.iii–iv`  **[S01,S06]**.

## Energy Accounting, The First Law & Physics-to-Chemistry Sign Convention Lock

The total energy $E_{\mathrm{tot}}$ of a thermodynamic system consists of macroscopic kinetic energy $K_{\mathrm{macro}} = \frac{1}{2}mv_{\mathrm{cm}}^2$, macroscopic potential energy $U_{\mathrm{grav}} = mg_n z$, and microscopic **internal energy $U$** (the sum of all molecular translational, rotational, vibrational kinetic energies and intermolecular/chemical potential energies in the center-of-mass frame)  **[S13,S16]**. For a stationary closed system ($\Delta K_{\mathrm{macro}} = 0, \Delta U_{\mathrm{grav}} = 0$), conservation of energy states:

$$
\begin{aligned}

  \boxed{\Delta U = U_2 - U_1 = Q - W_{\mathrm{by}}} \ \text{(Physics Locked)} \quad \Longleftrightarrow \quad \boxed{\Delta U = q + w_{\mathrm{on}}, \ w_{\mathrm{on}} = -W_{\mathrm{by}}} \ \text{(Chemistry / IUPAC)}
\end{aligned}
$$

### [FORMULA & DECISION CARD: Master First-Law Sign Convention & Physics-to-Chemistry Translation Matrix  **[S13,S16,S33]**]
- **Heat $Q$ (identical in BOTH Physics and Chemistry!):** $Q > 0$ when heat energy enters the system from the surroundings (**endothermic** / heating); $Q < 0$ when heat energy leaves the system to the surroundings (**exothermic** / cooling).
- **Work $W_{\mathrm{by}}$ vs. $w_{\mathrm{on}}$ (OPPOSITE SIGNS!):**
- **Expansion ($\Delta V = V_2 - V_1 > 0$):** Gas pushes piston outward $\implies W_{\mathrm{by}} > 0$ (Physics), $w_{\mathrm{on}} = -W_{\mathrm{by}} < 0$ (Chemistry).
- **Compression ($\Delta V = V_2 - V_1 < 0$):** Surroundings push piston inward $\implies W_{\mathrm{by}} < 0$ (Physics), $w_{\mathrm{on}} = -W_{\mathrm{by}} > 0$ (Chemistry).
  

| **Thermodynamic Process / Action** | $\Delta V$ | **Heat $Q$** | **Physics $W_{\mathrm{by}}$** | **Chem. $w_{\mathrm{on}}$** | **Internal Energy $\Delta U$ (Identical in Both!)** |
| --- | --- | --- | --- | --- | --- |
| **Isochoric Heating** (rigid tank) | $0$ | $>0$ | $0$ | $0$ | $\Delta U = +Q = nC_{V,m}\Delta T > 0$ ($\Delta T > 0$) |
| **Isochoric Cooling** (rigid tank) | $0$ | $<0$ | $0$ | $0$ | $\Delta U = Q = nC_{V,m}\Delta T < 0$ ($\Delta T < 0$) |
| **Isobaric Expansion** ($P=\mathrm{const}$) | $>0$ | $+nC_{P,m}\Delta T > 0$ | $+P\Delta V > 0$ | $-P\Delta V < 0$ | $\Delta U = Q - P\Delta V = +nC_{V,m}\Delta T > 0$ |
| **Isobaric Compression** ($P=\mathrm{const}$) | $<0$ | $nC_{P,m}\Delta T < 0$ | $P\Delta V < 0$ | $-P\Delta V > 0$ | $\Delta U = Q - P\Delta V = nC_{V,m}\Delta T < 0$ |
| **Isothermal Expansion** (ideal gas) | $>0$ | $+nRT\ln(V_2/V_1)$ | $+nRT\ln(V_2/V_1)$ | $-nRT\ln(V_2/V_1)$ | $\Delta U = 0 \implies Q = W_{\mathrm{by}} = -w_{\mathrm{on}} > 0$ |
| **Isothermal Compression** (ideal gas) | $<0$ | $nRT\ln(V_2/V_1)<0$ | $nRT\ln(V_2/V_1)<0$ | $-nRT\ln(V_2/V_1)>0$ | $\Delta U = 0 \implies Q = W_{\mathrm{by}} = -w_{\mathrm{on}} < 0$ |
| **Adiabatic Expansion** ($Q=0$) | $>0$ | $0$ | $+\dfrac{P_1V_1-P_2V_2}{\gamma-1}>0$ | $-\dfrac{P_1V_1-P_2V_2}{\gamma-1}<0$ | $\Delta U = -W_{\mathrm{by}} = +w_{\mathrm{on}} < 0$ (**gas cools!**) |
| **Adiabatic Compression** ($Q=0$) | $<0$ | $0$ | $\dfrac{P_1V_1-P_2V_2}{\gamma-1}<0$ | $-\dfrac{P_1V_1-P_2V_2}{\gamma-1}>0$ | $\Delta U = -W_{\mathrm{by}} = +w_{\mathrm{on}} > 0$ (**gas warms!**) |
| **Adiabatic Free Expansion** (vacuum) | $>0$ | $0$ | $0$ | $0$ | $\Delta U = 0$ ($\Delta T = 0$ ideal; $\Delta T < 0$ vdW real gas) |
| **Clockwise $P$–$V$ Cycle** (Engine) | $0$ | $Q_H - Q_C > 0$ | $+\mathrm{Area} > 0$ | $-\mathrm{Area} < 0$ | $\Delta U_{\mathrm{cycle}} = 0 \implies W_{\mathrm{net,by}} = Q_{\mathrm{net}} > 0$ |
| **Counterclockwise $P$–$V$ Cycle** (Refrig.) | $0$ | $Q_C - Q_H < 0$ | $-\mathrm{Area} < 0$ | $+\mathrm{Area} > 0$ | $\Delta U_{\mathrm{cycle}} = 0 \implies W_{\mathrm{in}} = w_{\mathrm{net,on}} = Q_H - Q_C > 0$ |

### [FORMULA & DECISION CARD: State vs. Path Functions & Joule Work Modes  **[S13,S23]**]
- **State Functions ($U, H, S, G, F, P, V, T, \rho$):** Depend *only* on equilibrium endpoints $(1, 2)$, never on the path taken:
  
$$
\begin{aligned}

    \Delta U_{1\to 2,\text{Path I}} = \Delta U_{1\to 2,\text{Path II}} = U_2 - U_1, \quad \Delta U_{\mathrm{cycle}} = 0
\end{aligned}
$$
- **Path Functions ($Q, W_{\mathrm{by}}, S_{\mathrm{gen}}$):** Boundary transfer interactions that depend on the specific trajectory on a $P$–$V$ or $T$–$S$ diagram. A system never “contains” heat or work; never write $\Delta Q$ or $\Delta W$!
- **Non-Boundary Shaft & Electrical Work Inputs ($W_{\mathrm{by}} < 0, w_{\mathrm{on}} > 0$):**
  
$$
\begin{aligned}

    w_{\mathrm{paddle,on}} = N_{\mathrm{drop}} m_{\mathrm{wt}} g_n h, \quad w_{\mathrm{elec,on}} = I^2 R_\Omega t = V_{\mathrm{rms}} I t
\end{aligned}
$$

  

### Worked Example — Paddle-Wheel + Expansion First-Law Ledger `[Regional/State | Tier 1]`

A cylinder with a movable piston holds a gas that absorbs $120.0 cal _{ th }$ of heat from a flame while a falling-weight paddle wheel (two $5.000 kg$ lead masses dropping $2.000 m$ each, $N_{\mathrm{drop}} = 5$ times, $g_n = 9.80665 m/s^2$) stirs the gas and the gas expands against the piston, performing $850.0 J$ of $PV$ boundary work on the external atmosphere. Find $Q$, total Physics work $W_{\mathrm{by}}$, Chemistry work $w_{\mathrm{on}}$, and $\Delta U$.
**Solution.**
- **Heat input in Joules:** $Q = (120.0\,cal _{ th })(4.184 J/cal·_{·th·}) = \mathbf{+502.08 J}$.
- **Paddle-wheel work done ON gas:**
  
$$
W_{\mathrm{paddle,on}} = 5 \times (2\times 5.000 kg)(9.80665)(2.000) = +980.67 J
$$
- **Net Physics work $W_{\mathrm{by}}$ vs. Chemistry work $w_{\mathrm{on}}$:**
  
$$
W_{\mathrm{by}} = 850.0 - 980.67 = \mathbf{-130.67 J}, \quad w_{\mathrm{on}} = \mathbf{+130.67 J}
$$
- **Internal energy change:**
  
$$
\Delta U = Q - W_{\mathrm{by}} = 502.08 - (-130.67) = \mathbf{+632.75 J}
$$

**✓ Verified by:** $\Delta U = q + w_{\mathrm{on}} = 502.08 + 130.67 = 632.75 J$ (`check_sec06_09.py::ex07_1`).

## Moving-Boundary $P$–$V$ Work, Geometric Area Rules & Multi-Stage Compression

When a gas expands or compresses against a piston of cross-sectional area $A$ through displacement $\Delta x = \Delta V / A$ against external pressure $P_{\mathrm{ext}}$, the mechanical work done **by** the gas is $W_{\mathrm{by}} = F_{\mathrm{ext}}\Delta x = (P_{\mathrm{ext}}A)(\Delta V/A) = P_{\mathrm{ext}}\Delta V$. For a **quasistatic** (infinitely slow, frictionless) process, the gas stays in internal mechanical equilibrium ($P_{\mathrm{ext}} = P_{\mathrm{gas}}(V)$ at every instant), so $W_{\mathrm{by}}$ equals the **signed geometric area** under the path $P(V)$ on a $P$–$V$ diagram  **[S06,S13]**:

### [FORMULA & DECISION CARD: Algebraic & Geometric $P$–$V$ Area Formulas (Rule 5.d.iii Zero-Calculus Toolkit)  **[S06,S13,S26]**]

| **Path / Cycle Geometry on $P$–$V$ Plane** | **Closed Algebraic Work Formula $W_{\mathrm{by}}$** | **Sign & Unit Rules ($1\,kPa\cdotL = 1 J$!)** |
| --- | --- | --- |
| **Isochoric Vertical Segment** ($V_1 = V_2$) | $W_{\mathrm{by}} = 0$ | Zero horizontal width $\implies$ zero area. |
| **Isobaric Horizontal Segment** ($P = P_0$) | $W_{\mathrm{by}} = P_0(V_2 - V_1)$ | Rectangle of height $P_0$ and signed base $\Delta V$. |
| **Straight-Line Chord** $(P_1,V_1)\to(P_2,V_2)$ | $W_{\mathrm{by}} = \frac{1}{2}(P_1 + P_2)(V_2 - V_1)$ | Trapezoid of mean height $\bar{P}=\frac{1}{2}(P_1+P_2)$ and base $\Delta V$. |
| **Rectangular Closed Cycle** ($\Delta P \times \Delta V$) | $W_{\mathrm{net,by}} = \pm(P_{\mathrm{high}} - P_{\mathrm{low}})(V_{\max} - V_{\min})$ | $+$ if **clockwise** (engine); $-$ if **counterclockwise**. |
| **Triangular Closed Cycle** (base $\Delta V$, height $\Delta P$) | $W_{\mathrm{net,by}} = \pm\frac{1}{2}(P_{\mathrm{high}} - P_{\mathrm{low}})(V_{\max} - V_{\min})$ | $\pm\frac{1}{2}\,\text{base}\times\text{height}$ (check loop orientation!). |
| **Circular / Elliptical Cycle** (diameters $\Delta P, \Delta V$) | $W_{\mathrm{net,by}} = \pm\pi a b = \pm\frac{\pi}{4}(P_{\mathrm{high}} - P_{\mathrm{low}})(V_{\max} - V_{\min})$ | Semi-axes $a = \Delta V/2$ and $b = \Delta P/2$. |
| **Single-Step Irreversible Jump** (fixed $P_{\mathrm{ext}}$) | $W_{\mathrm{by,irrev}} = P_{\mathrm{ext}}(V_2 - V_1)$ | Rectangle at constant height $P_{\mathrm{ext}}$ (NOT area under $nRT/V$!). |

> **[Vector Figure: Path dependence of boundary work $W_{\mathrm{by}}$ vs. path independence of $\Delta U = U_B - U_A$ between states $A(2.00 L, 400 kPa)$ and $B(6.00 L, 100 kPa)$  **[S13]**. Upper path $A\to C\to B$ performs $W_{\mathrm{I}} = 1600 J$; straight chord $A\to B$ performs trapezoid area $W_{\mathrm{II}} = 1000 J$; lower path $A\to D\to B$ performs $W_{\mathrm{III}} = 400 J$. | Label: `fig:07:pv-work-paths`]**
> - **Diagram Annotations & Key Elements:** **X-Axis:** Volume $V$ ($L$) • **Y-Axis:** Pressure $P$ ($kPa$)

### Worked Example — Three-Path $P$–$V$ Work & Heat Ledger Between Identical Endpoints `[Classic Invitational FRQ | Tier 2]`

A monatomic ideal gas ($\gamma = 5/3, C_{V,m} = \frac{3}{2}R$) is taken from State $A$ ($P_A = 400.0 kPa, V_A = 2.000 L$) to State $B$ ($P_B = 100.0 kPa, V_B = 6.000 L$) along the three paths in Fig. `fig:07:pv-work-paths`: Path I ($A\to C\to B$), Path II (straight line $A\to B$), and Path III ($A\to D\to B$). (a) Compute $\Delta U_{A\to B}$ for all three paths. (b) Compute $W_{\mathrm{by}}$ and $Q$ for each path. (c) If the gas goes from $A\to C\to B$ and returns via $B\to D\to A$, find the net cycle work $W_{\mathrm{net,by}}$ and net heat $Q_{\mathrm{net}}$.
**Solution.**
- **(a) State-function internal energy change $\Delta U_{A\to B}$ (using $U = \frac{3}{2}PV$ and $1\,kPa L = 1 J$):**
  
$$
U_A = \frac{3}{2}P_A V_A = \frac{3}{2}(400.0)(2.000) = 1200.0 J, \qquad U_B = \frac{3}{2}P_B V_B = \frac{3}{2}(100.0)(6.000) = 900.0 J
$$

  
$$
\Delta U_{\mathrm{I}} = \Delta U_{\mathrm{II}} = \Delta U_{\mathrm{III}} = U_B - U_A = 900.0 - 1200.0 = \mathbf{-300.0 J} \quad (\text{identical for every path!})
$$
- **(b) Work $W_{\mathrm{by}}$ (geometric area) and Heat $Q = \Delta U + W_{\mathrm{by}}$ for each path:**
- **Path I ($A\to C\to B$):** $W_{\mathrm{I}} = P_A(V_B - V_A) + 0 = 400.0(6.000 - 2.000) = \mathbf{+1600.0 J} \implies Q_{\mathrm{I}} = -300.0 + 1600.0 = \mathbf{+1300.0 J}$.
- **Path II (Chord $A\to B$):** $W_{\mathrm{II}} = \frac{1}{2}(P_A + P_B)(V_B - V_A) = \frac{1}{2}(500.0)(4.000) = \mathbf{+1000.0 J} \implies Q_{\mathrm{II}} = -300.0 + 1000.0 = \mathbf{+700.0 J}$.
- **Path III ($A\to D\to B$):** $W_{\mathrm{III}} = 0 + P_B(V_B - V_A) = 100.0(4.000) = \mathbf{+400.0 J} \implies Q_{\mathrm{III}} = -300.0 + 400.0 = \mathbf{+100.0 J}$.
- **(c) Clockwise rectangular cycle $A\to C\to B\to D\to A$:**
  Returning from $B\to D\to A$ reverses Path III ($W_{B\to D\to A} = -400.0 J$), so the net work equals the enclosed rectangle area:
  
$$
W_{\mathrm{net,by}} = W_{\mathrm{I}} + W_{B\to D\to A} = 1600.0 - 400.0 = (400.0 - 100.0)(6.000 - 2.000) = \mathbf{+1200.0 J} = Q_{\mathrm{net}}
$$

**✓ Verified by:** Leg-by-leg heat sum on Path I: $Q_{A\to C} = \frac{5}{2}P_A\Delta V = +4000 J$ and $Q_{C\to B} = \frac{3}{2}V_B\Delta P = -2700 J \implies Q_{\mathrm{I}} = +1300 J$ (`check_sec06_09.py::ex07_2`).

### Worked Example — Isothermal vs. Adiabatic-Isobaric & $N$-Stage Intercooled Compression `[2019 MIT E2 P4 (TB #1 & #2) | Tier 3]`

One mole ($n = 1.000 mol$) of monatomic Helium ($\gamma = 5/3$, $C_{P,m} = \frac{5}{2}R$, $(\gamma-1)/\gamma = 2/5 = 0.400$) is compressed from State 1 ($P_1 = 1.000 bar, T_1 = 298.0 K$) to final State 2 ($P_2 = 8.000 bar, T_2 = 298.0 K$, so $P_2/P_1 = 8.000$). Compare the work input $w_{\mathrm{on}} = -W_{\mathrm{by}}$ required along four different compression strategies: (a) reversible isothermal compression at $T_1 = 298.0 K$; (b) **maximum-work** 2-leg path (adiabatic compression $1\to A$ to $P_2 = 8.000 bar$, followed by isobaric cooling $A\to 2$ at $P_2$ back to $T_1$); (c) **minimum-work** 2-leg path (isobaric cooling $1\to B$ at $P_1$, followed by adiabatic compression $B\to 2$ reaching $(P_2, T_1)$); and (d) a 3-stage intercooled compressor where each stage doubles the pressure ($1 bar\to2 bar\to4 bar\to8 bar$) via adiabatic compression followed by isobaric cooling back to $298.0 K$.
**Solution.**
- **(a) Reversible isothermal compression work input ($T = 298.0 K, nRT_1 = 2477.71 J$):**
  
$$
w_{\mathrm{on,iso}} = -W_{\mathrm{by,iso}} = nRT_1\ln\left(\frac{P_2}{P_1}\right) = (2477.71)\ln(8.000) = \mathbf{+5152.3 J} \quad (\text{MIT key rounds to } 5150 J)
$$
- **(b) Maximum-work 2-leg path (Adiabatic compression $1\to A$ to $8.00 bar$, then isobaric cooling $A\to 2$):**
  Along adiabat $1\to A$, $T_A = T_1(P_2/P_1)^{(\gamma-1)/\gamma} = T_1(8.000)^{2/5} = 2.29740\,T_1 = 684.62 K$. Since $\Delta U_{1\to 2} = 0$, the total work done on the gas across both legs equals the heat rejected during the isobaric cooling $A\to 2$, or directly:
  
$$
w_{\mathrm{on,\max}} = \underbrace{nC_{V,m}(T_A - T_1)}_{\text{adiabat } 1\to A} + \underbrace{nR(T_A - T_1)}_{\text{isobar } A\to 2} = nC_{P,m}T_1\left[\left(\frac{P_2}{P_1}\right)^{2/5} - 1\right] = \frac{5}{2}(2477.71)(2.29740 - 1) = \mathbf{+8036.4 J}
$$
- **(c) Minimum-work 2-leg path (Isobaric pre-cooling $1\to B$ at $1.00 bar$, then adiabatic compression $B\to 2$):**
  To land on $(P_2, T_1)$ after adiabatic compression $B\to 2$, the gas must first be pre-cooled at $P_1$ to $T_B = T_1(P_1/P_2)^{2/5} = T_1 / 2.29740 = 0.435275\,T_1 = 129.71 K$. Total work done on the gas is:
  
$$
w_{\mathrm{on,\min}} = nC_{P,m}(T_1 - T_B) = nC_{P,m}T_1\left[1 - \left(\frac{P_1}{P_2}\right)^{2/5}\right] = \frac{5}{2}(2477.71)(1 - 0.435275) = \mathbf{+3498.0 J}
$$
- **(d) $N=3$ intercooled adiabatic-isobaric stages (each stage has pressure ratio $r_s = (P_2/P_1)^{1/3} = 2.000$):**
  
$$
w_{\mathrm{on},N=3} = N\,nC_{P,m}T_1\left[\left(\frac{P_2}{P_1}\right)^{\frac{2}{5N}} - 1\right] = 3 \times \frac{5}{2}(2477.71)\left(2.000^{2/5} - 1\right) = 18582.8(1.319508 - 1) = \mathbf{+5937.4 J}
$$

  *(Note: In `2019 MIT E2 P4b(iv)`, the problem statement defined its multi-step path via pre-cooling steps $N\,nC_{P,m}T_1[1 - 2^{-2/5}] = 4499.6 J$; as $N\to\infty$, both upper and lower staircases converge to the isothermal limit $5152.3 J$!)*

**✓ Verified by:** Limit check as $N\to\infty$: $\lim_{N\to\infty} N\frac{5}{2}RT_1[8^{2/(5N)} - 1] = \frac{5}{2}RT_1\cdot\frac{2}{5}\ln 8 = RT_1\ln 8 = 5152.3 J$ (`check_sec06_09.py::ex07_3`).

## Master Closed-System Ideal-Gas Process Atlas (8 Canonical Processes)

For any closed system of $n$ moles of an ideal gas ($PV = nRT$) with constant heat capacities $C_{V,m} = \frac{f}{2}R = \frac{R}{\gamma - 1}$ and $C_{P,m} = \frac{f+2}{2}R = \frac{\gamma R}{\gamma - 1}$, two universal state-function identities hold across **every** process regardless of path  **[S13,S18]**:

$$
\begin{aligned}

  \boxed{\Delta U = nC_{V,m}(T_2 - T_1) = \frac{nR(T_2 - T_1)}{\gamma - 1} = \frac{P_2V_2 - P_1V_1}{\gamma - 1}}, \qquad \boxed{\Delta H = nC_{P,m}(T_2 - T_1) = \frac{\gamma(P_2V_2 - P_1V_1)}{\gamma - 1} = \gamma\,\Delta U}
\end{aligned}
$$

**Table:** Master Closed-System Ideal-Gas Process Atlas ($PV = nRT$, Physics Sign Convention $\Delta U = Q - W_{\mathrm{by}}$)  **[S13,S16,S18]**.

| **Process** | **Constraint /** | **State Law** | **Work BY Gas** | **Internal Energy** | **Heat TO Gas** | **Enthalpy** | **Entropy Change** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Name** | **Exponent $n$** | ($1 \to 2$) | $W_{\mathrm{by}} = -w_{\mathrm{on}}$ | $\Delta U = U_2 - U_1$ | $Q = \Delta U + W_{\mathrm{by}}$ | $\Delta H = H_2 - H_1$ | $\Delta S = S_2 - S_1$ |
| **1. Isochoric** | $V = \mathrm{const}$ | $\dfrac{P_1}{T_1} = \dfrac{P_2}{T_2}$ | $\mathbf{0}$ | $nC_{V,m}\Delta T$ | $nC_{V,m}\Delta T = \Delta U$ | $nC_{P,m}\Delta T = \gamma Q_V$ | $nC_{V,m}\ln(T_2/T_1)$ |
| (Isometric) | ($n = \pm\infty$) |  |  | $= \dfrac{V\Delta P}{\gamma - 1}$ | $= \dfrac{V\Delta P}{\gamma - 1}$ | $= \dfrac{\gamma V\Delta P}{\gamma - 1}$ | $= nC_{V,m}\ln(P_2/P_1)$ |
| **2. Isobaric** | $P = \mathrm{const}$ | $\dfrac{V_1}{T_1} = \dfrac{V_2}{T_2}$ | $P(V_2 - V_1)$ | $nC_{V,m}\Delta T$ | $nC_{P,m}\Delta T = \Delta H$ | $nC_{P,m}\Delta T = Q_P$ | $nC_{P,m}\ln(T_2/T_1)$ |
|  | ($n = 0$) |  | $= nR\Delta T$ | $= \dfrac{P\Delta V}{\gamma - 1}$ | $= \dfrac{\gamma P\Delta V}{\gamma - 1}$ | $= \dfrac{\gamma P\Delta V}{\gamma - 1}$ | $= nC_{P,m}\ln(V_2/V_1)$ |
| **3. Isothermal** | $T = \mathrm{const}$ | $P_1 V_1 = P_2 V_2$ | $nRT\ln(V_2/V_1)$ | $\mathbf{0}$ | $nRT\ln(V_2/V_1)$ | $\mathbf{0}$ | $nR\ln(V_2/V_1)$ |
| (Reversible) | ($n = 1$) |  | $= P_1V_1\ln(P_1/P_2)$ |  | $= P_1V_1\ln(P_1/P_2)$ |  | $= nR\ln(P_1/P_2)$ |
| **4. Adiabatic** | $Q = 0$ | $P_1V_1^\gamma = P_2V_2^\gamma$ | $nC_{V,m}(T_1-T_2)$ | $nC_{V,m}(T_2 - T_1)$ | $\mathbf{0}$ | $nC_{P,m}(T_2 - T_1)$ | $\mathbf{0}$ (reversible) |
| (Isentropic) | ($n = \gamma$) | $T_1V_1^{\gamma-1} = T_2V_2^{\gamma-1}$ | $= \dfrac{P_1V_1 - P_2V_2}{\gamma - 1}$ | $= \dfrac{P_2V_2 - P_1V_1}{\gamma - 1}$ |  | $= \dfrac{\gamma(P_2V_2 - P_1V_1)}{\gamma - 1}$ | ($>0$ if irrev.) |
| **5. Polytropic** | $PV^n = \mathrm{const}$ | $T_1V_1^{n-1} = T_2V_2^{n-1}$ | $\dfrac{P_1V_1 - P_2V_2}{n - 1}$ | $nC_{V,m}(T_2 - T_1)$ | $nC_{n,m}(T_2 - T_1)$ | $nC_{P,m}(T_2 - T_1)$ | $nC_{n,m}\ln(T_2/T_1)$ |
| ($n \ne 1$) | ($C_{n,m}=\mathrm{const}$) | $T_1^n P_1^{1-n} = T_2^n P_2^{1-n}$ | $= \dfrac{nR(T_1 - T_2)}{n - 1}$ | $= \dfrac{P_2V_2 - P_1V_1}{\gamma - 1}$ | $C_{n,m} = C_{V,m}\dfrac{n-\gamma}{n-1}$ |  |  |
| **6. Linear $PV$** | $P(V)$ chord | $T = \dfrac{PV}{nR}$ | $\dfrac{P_1 + P_2}{2}\Delta V$ | $\dfrac{P_2V_2 - P_1V_1}{\gamma - 1}$ | $\Delta U + \dfrac{P_1+P_2}{2}\Delta V$ | $\dfrac{\gamma(P_2V_2 - P_1V_1)}{\gamma - 1}$ | $nC_{V,m}\ln\dfrac{P_2}{P_1} + nC_{P,m}\ln\dfrac{V_2}{V_1}$ |
| **7. Free Exp.** | Into vacuum | $T_1 = T_2$ | $\mathbf{0}$ ($P_{\mathrm{ext}} = 0$) | $\mathbf{0}$ | $\mathbf{0}$ | $\mathbf{0}$ | $+nR\ln(V_2/V_1) > 0$ |
| (Joule) | ($Q=0, W=0$) | $P_1V_1 = P_2V_2$ |  |  |  |  | (**irreversible!**) |
| **8. Throttling** | Porous plug | $H_1 = H_2$ | Flow work | $\mathbf{0}$ (ideal gas) | $\mathbf{0}$ | $\mathbf{0}$ (**isenthalpic**) | $+nR\ln(P_1/P_2) > 0$ |
| (Joule–Thomson) | ($\dot{Q}=0, \dot{W}_s=0$) | $T_1 = T_2$ (ideal) | $\Delta(PV) = 0$ |  |  | ($h_1 = h_2$ always!) | (**irreversible!**) |

### [DERIVATION: Zero-Calculus Proofs of Adiabatic Work, Isothermal Work & Isobaric Energy Partition  **[S06,S13]**]
- **Zero-Calculus Proof of Adiabatic Work ($W_{\mathrm{by}} = \frac{P_1V_1 - P_2V_2}{\gamma - 1}$):**
  By Eq. (`eq:07:universal-u-h`), $\Delta U = \frac{P_2V_2 - P_1V_1}{\gamma - 1}$ for *any* ideal-gas process. In an adiabatic process, $Q = 0$, so the First Law $\Delta U = Q - W_{\mathrm{by}}$ gives $W_{\mathrm{by}} = -\Delta U = \frac{P_1V_1 - P_2V_2}{\gamma - 1} = \frac{nR(T_1 - T_2)}{\gamma - 1}$ immediately without a single integral!
- **Three Equivalent Adiabatic State Forms ($PV^\gamma = \mathrm{const}$):** Substituting $P = nRT/V$ or $V = nRT/P$ into $P_1V_1^\gamma = P_2V_2^\gamma$ yields:
  
$$
\begin{aligned}

    \boxed{P_1 V_1^\gamma = P_2 V_2^\gamma}, \qquad \boxed{T_1 V_1^{\gamma - 1} = T_2 V_2^{\gamma - 1}}, \qquad \boxed{T_1^\gamma P_1^{1 - \gamma} = T_2^\gamma P_2^{1 - \gamma} \iff \frac{T_2}{T_1} = \left(\frac{P_2}{P_1}\right)^{\frac{\gamma - 1}{\gamma}}}
\end{aligned}
$$

  
- **Geometric-Mean Stepping Justification of Isothermal Work $W_{\mathrm{by}} = nRT\ln(V_2/V_1)$:**
  Divide the isothermal expansion $[V_1, V_2]$ into $M$ equal-ratio steps of multiplier $r = (V_2/V_1)^{1/M}$. Across step $k$, $P_k V_k = nRT$, so the fractional work is $\Delta W_k = P_k \Delta V_k = nRT(\Delta V_k / V_k) = nRT(r - 1)$. Summing $M$ identical steps and using the natural logarithm compound-interest limit $\lim_{M\to\infty} M[(V_2/V_1)^{1/M} - 1] = \ln(V_2/V_1)$ gives $W_{\mathrm{by}} = nRT\ln(V_2/V_1) = P_1V_1\ln(P_1/P_2)$.
- **Universal Isobaric Energy-Partition Ratios:** In any isobaric heating/expansion ($P = \mathrm{const}$), the fractions of added heat $Q_P = nC_{P,m}\Delta T$ converted into boundary work $W_{\mathrm{by}} = nR\Delta T$ versus stored as internal energy $\Delta U = nC_{V,m}\Delta T$ depend *only* on $\gamma$ (or $f$):
  
$$
\begin{aligned}

    \boxed{\frac{W_{\mathrm{by}}}{Q_P} = \frac{R}{C_{P,m}} = 1 - \frac{1}{\gamma} = \frac{2}{f + 2}}, \qquad \boxed{\frac{\Delta U}{Q_P} = \frac{C_{V,m}}{C_{P,m}} = \frac{1}{\gamma} = \frac{f}{f + 2}}
\end{aligned}
$$

  
  (**Monatomic $f=3$:** $40\%$ work, $60\%$ $\Delta U$; **Diatomic $f=5$:** $2/7 = 28.57\%$ work, $5/7 = 71.43\%$ $\Delta U$; **Polyatomic $f=6$:** $25\%$ work, $75\%$ $\Delta U$.)

### Worked Example — Adiabatic Scaling & Heat Capacity Extraction Without Solving for $n$ or $V$ `[2018 MIT E3 Q20 | Tier 2]`

Five moles ($n = 5.000 mol$) of an unknown ideal gas are compressed reversibly and adiabatically from $P_1 = 500.0 kPa$ and $T_1 = 300.0 K$ to $P_2 = 1000.0 kPa$, where its temperature is measured to be $T_2 = 378.0 K$ (note that $2^{1/3} = \sqrt[3]{2} \approx 1.25992 \approx 1.260$). (a) Without calculating $\gamma$ or $V$, determine the temperature $T_3$ if the gas is instead expanded reversibly and adiabatically from $(P_1, T_1) = (500.0 kPa, 300.0 K)$ to $P_3 = 250.0 kPa$. (b) Extract $\gamma$, $f$, $C_{V,m}$, and $C_{P,m}$ of the gas. (c) Compute the work done $W_{\mathrm{by},1\to 2}$ during the compression $1\to 2$, and the heat required to warm $5.000 mol$ of this gas by $\Delta T = 10.00 K$ at constant volume ($Q_V$) versus constant pressure ($Q_P$).
**Solution.**
- **(a) Direct ratio scaling from Eq. (`eq:07:adiabatic-laws`):**
  Since $T \propto P^{(\gamma-1)/\gamma}$, doubling the pressure ($500 kPa\to1000 kPa$) multiplies $T$ by the factor $2^{(\gamma-1)/\gamma} = \frac{378.0}{300.0} = 1.260$. Therefore, halving the pressure ($500 kPa\to250 kPa$) divides $T_1$ by the exact same factor $1.260$:
  
$$
T_3 = \frac{T_1}{1.260} = \frac{300.0 K}{1.260} = \mathbf{238.10 K} \quad (\text{exact } 300/2^{1/3} = 238.11 K)
$$
- **(b) Extracting $\gamma, f, C_{V,m}, C_{P,m}$:**
  
$$
2^{(\gamma-1)/\gamma} = 1.260 \approx 2^{1/3} \implies \frac{\gamma - 1}{\gamma} = \frac{1}{3} \implies \boxed{\gamma = \frac{3}{2} = 1.500}, \qquad f = \frac{2}{\gamma - 1} = \mathbf{4}
$$

  
$$
C_{V,m} = \frac{R}{\gamma - 1} = 2R = \mathbf{16.629 J/mol/K}, \qquad C_{P,m} = \frac{\gamma R}{\gamma - 1} = 3R = \mathbf{24.943 J/mol/K}
$$
- **(c) Adiabatic work $W_{\mathrm{by},1\to 2}$ and isochoric/isobaric heats for $\Delta T = 10.00 K$:**
  
$$
W_{\mathrm{by},1\to 2} = -\Delta U_{1\to 2} = -nC_{V,m}(T_2 - T_1) = -(5.000)(2\times 8.314463)(378.0 - 300.0) = \mathbf{-6.4853 kJ}
$$

  
$$
Q_V = nC_{V,m}\Delta T = (5.000)(16.6289)(10.00) = \mathbf{+831.45 J}, \qquad Q_P = nC_{P,m}\Delta T = (5.000)(24.9434)(10.00) = \mathbf{+1247.17 J}
$$

**✓ Verified by:** Isobaric partition check Eq. (`eq:07:isobaric-partition`): $\Delta U / Q_P = Q_V / Q_P = 831.45/1247.17 = 2/3 = 1/\gamma$ (`check_sec06_09.py::ex07_4`).

## The Polytropic Process Star ($PV^n = \mathrm{const}$), Slope Theorem & Linear-Chord $T_{\max}$

Every standard ideal-gas process is a special case of the **polytropic process** $P V^n = C = \mathrm{const}$, where $n \in (-\infty, \infty)$ is the **polytropic exponent**  **[S16,S33]**:
- $n = 0 \implies P = \mathrm{const}$ (**isobaric**, horizontal slope $\Delta P/\Delta V = 0$, $C_{0,m} = C_{P,m}$).
- $n = 1 \implies PV = \mathrm{const}$ (**isothermal**, slope $\Delta P/\Delta V = -P/V$, $C_{1,m} = \pm\infty$).
- $n = \gamma \implies PV^\gamma = \mathrm{const}$ (**reversible adiabatic / isentropic**, slope $\Delta P/\Delta V = -\gamma P/V$, $C_{\gamma,m} = 0$).
- $n \to \pm\infty \implies V = \mathrm{const}$ (**isochoric**, vertical slope $\Delta P/\Delta V = -\infty$, $C_{\infty,m} = C_{V,m}$).

### [FORMULA & DECISION CARD: Polytropic Slope Theorem, Negative Heat Capacity Regime & Linear-Chord $T_{\max}$  **[S13,S33]**]
- **Algebra-Only Proof That an Adiabat Is $\gamma$ Times Steeper Than an Isotherm:**
  For a small fractional volume change $\varepsilon = \Delta V / V_0 \ll 1$, the binomial expansion $(1 + \varepsilon)^{-n} \approx 1 - n\varepsilon$ gives $P/P_0 = (V/V_0)^{-n} \approx 1 - n(\Delta V/V_0)$, or:
  
$$
\begin{aligned}

    \left(\frac{\Delta P}{\Delta V}\right)_{\text{polytropic } n} = -n\,\frac{P}{V} \implies \boxed{\left(\frac{\Delta P}{\Delta V}\right)_{\text{adiabat } (n=\gamma)} = -\gamma\,\frac{P}{V} = \gamma\left(\frac{\Delta P}{\Delta V}\right)_{\text{isotherm } (n=1)}}
\end{aligned}
$$

  
  Because $\gamma > 1$, the adiabat is **always steeper** than the isotherm passing through the same state $(P_0, V_0)$!
- **Polytropic Molar Heat Capacity ($C_{n,m}$) and the Paradoxical Regime $1 < n < \gamma$:**
  Combining $\Delta U = n_{\mathrm{mol}}C_{V,m}(T_2 - T_1) = \frac{P_2V_2 - P_1V_1}{\gamma - 1}$ with $W_{\mathrm{by}} = \frac{P_1V_1 - P_2V_2}{n - 1} = \frac{-n_{\mathrm{mol}}R(T_2 - T_1)}{n - 1}$ yields:
  
$$
\begin{aligned}

    Q = \Delta U + W_{\mathrm{by}} = n_{\mathrm{mol}}\left(C_{V,m} - \frac{R}{n - 1}\right)(T_2 - T_1) = n_{\mathrm{mol}} C_{n,m}(T_2 - T_1), \qquad \boxed{C_{n,m} = C_{V,m}\left(\frac{n - \gamma}{n - 1}\right) = \frac{(n - \gamma)R}{(n - 1)(\gamma - 1)}}
\end{aligned}
$$

  
  *Crucial Exam Consequence:* Whenever $\mathbf{1 < n < \gamma}$, the polytropic heat capacity is **strictly negative ($C_{n,m} < 0$)**!
- During a polytropic **expansion** with $1 < n < \gamma$: the gas absorbs heat ($Q > 0$), yet its temperature **drops** ($\Delta T < 0$) because it performs more boundary work than the heat added ($W_{\mathrm{by}} > Q > 0$)!
- During a polytropic **compression** with $1 < n < \gamma$: work is done on the gas ($W_{\mathrm{by}} < 0$), heat leaks **out** ($Q < 0$), yet the gas temperature **rises** ($\Delta T > 0$)!
- **Peak Temperature $T_{\max}$ Along a Negatively Sloped Straight-Line $P$–$V$ Chord (Completing the Square):**
  Any downward-sloping straight line through $(P_1, V_1)$ and $(P_2, V_2)$ can be extended to its axis intercepts $(0, P_{\mathrm{int}})$ and $(V_{\mathrm{int}}, 0)$ as $\frac{P}{P_{\mathrm{int}}} + \frac{V}{V_{\mathrm{int}}} = 1 \iff P(V) = P_{\mathrm{int}}\left(1 - \frac{V}{V_{\mathrm{int}}}\right)$. The ideal-gas temperature $T(V) = \frac{P(V)V}{nR}$ is a downward-opening parabola:
  
$$
\begin{aligned}

    T(V) = \frac{P_{\mathrm{int}}V_{\mathrm{int}}}{nR}\left(\frac{V}{V_{\mathrm{int}}}\right)\left(1 - \frac{V}{V_{\mathrm{int}}}\right) = \frac{P_{\mathrm{int}}V_{\mathrm{int}}}{4nR}\left[1 - \left(\frac{2V}{V_{\mathrm{int}}} - 1\right)^2\right] \implies \boxed{T_{\max} = \frac{P_{\mathrm{int}}V_{\mathrm{int}}}{4nR} \text{ at } \left(V^*, P^*\right) = \left(\frac{V_{\mathrm{int}}}{2},\, \frac{P_{\mathrm{int}}}{2}\right)}
\end{aligned}
$$

  

> **[Vector Figure: The Polytropic Process Star $P/P_0 = (V/V_0)^{-n}$ passing through a common reference state $(V_0, P_0)$  **[S13,S33]**. In expansion ($V > V_0$), the adiabat ($n=\gamma$) drops below the isotherm ($n=1$) because $\Delta T < 0$; in compression ($V < V_0$), the adiabat rises above the isotherm because $\Delta T > 0$. Between the two curves ($1 < n < \gamma$), the effective heat capacity $C_{n,m}$ is negative. | Label: `fig:07:polytropic-star`]**
> - **Diagram Annotations & Key Elements:** **X-Axis:** Dimensionless Volume Ratio $V/V_0$ • **Y-Axis:** Dimensionless Pressure Ratio $P/P_0$ • **Legend:** $n = 1$: Isotherm ($PV = \mathrm{const}, \Delta T = 0$) • **Legend:** $n = \gamma = 1.4$: Adiabat ($PV^\gamma = \mathrm{const}, Q = 0$) • **Legend:** $n = 1.25 \in (1,\gamma)$: Polytropic ($C_{n,m} < 0$) • Isotherm: slope $-P_0/V_0$ • Adiabat: steeper slope $-\gamma P_0/V_0$

### Worked Example — Polytropic Compression with Negative Heat Capacity & Linear-Chord $T_{\max}$ `[National/Invitational | Tier 3]`

(a) Two moles ($n_{\mathrm{mol}} = 2.000 mol$) of dry air ($\gamma = 1.400, C_{V,m} = \frac{5}{2}R = 20.786 J/mol/K$) are compressed polytropically along $PV^{1.250} = \mathrm{const}$ ($n = 1.250$) inside a water-cooled cylinder from $T_1 = 300.0 K$ and $V_1 = 20.00 L$ to $V_2 = 5.000 L$. Find the final temperature $T_2$, the boundary work $W_{\mathrm{by}}$, the polytropic molar heat capacity $C_{n,m}$, and the heat transfer $Q$. (b) If the same $2.000\,mol$ of air instead expands along the straight-line chord from State $A$ ($P_A = 400.0 kPa, V_A = 2.000 L$) to State $B$ ($P_B = 100.0 kPa, V_B = 8.000 L$), find the maximum temperature $T_{\max}$ reached along the chord and the volume $V_{\mathrm{turn}}$ at which the gas switches from absorbing heat to rejecting heat!
**Solution.**
- **(a) Polytropic compression ($n = 1.250, V_1/V_2 = 4.000$):**
  
$$
T_2 = T_1\left(\frac{V_1}{V_2}\right)^{n - 1} = (300.0 K)(4.000)^{0.250} = 300.0 \times \sqrt{2} = \mathbf{424.264 K} \quad (\Delta T = +124.264 K)
$$

  
$$
W_{\mathrm{by}} = \frac{n_{\mathrm{mol}}R(T_1 - T_2)}{n - 1} = \frac{(2.000)(8.314463)(-124.264)}{0.250} = \mathbf{-8.2655 kJ}, \quad \Delta U = n_{\mathrm{mol}}C_{V,m}\Delta T = \mathbf{+5.1659 kJ}
$$

  
$$
C_{n,m} = C_{V,m}\left(\frac{n - \gamma}{n - 1}\right) = (20.786)\left(\frac{1.250 - 1.400}{1.250 - 1.000}\right) = -0.600\,C_{V,m} = \mathbf{-12.472 J/mol/K}
$$

  
$$
Q = \Delta U + W_{\mathrm{by}} = 5.1659 - 8.2655 = n_{\mathrm{mol}}C_{n,m}\Delta T = \mathbf{-3.0996 kJ}
$$

  Even though $3.100 kJ$ of heat escapes into the cooling jacket ($Q < 0$), the gas temperature rises by $124.3 K$ because $8.266 kJ$ of compression work is done on it!
- **(b) Peak temperature $T_{\max}$ and heat-reversal point $V_{\mathrm{turn}}$ along chord $A(2 L,400 kPa)\to B(8 L,100 kPa)$:**
  The chord slope is $\frac{\Delta P}{\Delta V} = \frac{100 - 400}{8 - 2} = -50.0 kPa/L$, giving $P(V) = 500.0 - 50.0\,V$ (intercepts $P_{\mathrm{int}} = 500.0 kPa, V_{\mathrm{int}} = 10.00 L$). From Eq. (`eq:07:chord-tmax`), $T_{\max}$ occurs at the midpoint $(V^*, P^*) = (5.000 L, 250.0 kPa) \in [2, 8]\,L$:
  
$$
T_{\max} = \frac{P^* V^*}{n_{\mathrm{mol}}R} = \frac{(250.0)(5.000)}{(2.000)(8.314463)} = \mathbf{75.170 K} \quad (\text{vs.\ } T_A = T_B = 48.109 K)
$$

  *Bonus National Trap — Where does $\delta Q = 0$?* Heat transfer switches sign where the straight chord is **tangent to an adiabat**, i.e., where the chord slope equals the adiabatic slope $-\gamma P/V$:
  
$$
\frac{\Delta P}{\Delta V} = -\frac{P_{\mathrm{int}}}{V_{\mathrm{int}}} = -\gamma\,\frac{P_{\mathrm{int}}(1 - V_{\mathrm{turn}}/V_{\mathrm{int}})}{V_{\mathrm{turn}}} \implies \boxed{V_{\mathrm{turn}} = \frac{\gamma}{\gamma + 1}\,V_{\mathrm{int}}} = \frac{1.400}{2.400}(10.00 L) = \mathbf{5.833 L}
$$

  Thus the gas absorbs heat on $[2.00, 5.833]\,L$ (even after passing $T_{\max}$ at $5.00 L$!) and rejects heat on $[5.833, 8.00]\,L$.

**✓ Verified by:** Quadratic energy differential $\delta Q = \frac{5}{2}d(PV) + P\,dV = P_{\mathrm{int}}[3.5 - 6(V/V_{\mathrm{int}})]dV = 0$ at $V/V_{\mathrm{int}} = 3.5/6 = 7/12 = 5.8333 L$ (`check_sec06_09.py::ex07_5`).

## Multi-Leg Closed-Cycle Ledgers ($P, V, T, \Delta U, Q, W_{\mathrm{by}}, \Delta H, \Delta S$ Protocol)

When an exam presents a 3- or 4-leg thermodynamic cycle and asks for a complete table of state properties $(P_k, V_k, T_k)$ and process transfers $(\Delta U, Q, W_{\mathrm{by}}, \Delta H, \Delta S)$, follow this fail-safe 4-step protocol:
- **Step 1 — Solve All Vertex States $(P_k, V_k, T_k)$ First:** Apply $PV = nRT$ at every vertex before computing any work or heat. Check that $P_k V_k / T_k = nR$ is identical at all vertices.
- **Step 2 — Fill the $\Delta U$ and $\Delta H$ Columns Using Only Vertex Temperatures:** Compute $\Delta U_{j\to k} = nC_{V,m}(T_k - T_j)$ and $\Delta H_{j\to k} = \gamma\,\Delta U_{j\to k}$ for every leg. Verify immediately that $\sum_{\mathrm{cycle}} \Delta U = 0$ and $\sum_{\mathrm{cycle}} \Delta H = 0$.
- **Step 3 — Fill the $W_{\mathrm{by}}$ Column from Each Leg's Process Type:** Isochoric $\to 0$; Isobaric $\to P\Delta V = nR\Delta T$; Isothermal $\to nRT\ln(V_k/V_j)$; Adiabatic $\to -\Delta U_{j\to k}$.
- **Step 4 — Fill the $Q$ Column via $Q = \Delta U + W_{\mathrm{by}}$ and Cross-Check $\sum Q = \sum W_{\mathrm{by}}$:** Never compute $Q$ and $W_{\mathrm{by}}$ with contradictory sign conventions; enforce $Q - W_{\mathrm{by}} = \Delta U$ row by row.

### Worked Example — Complete 4-Leg Ideal-Gas Cycle Ledger & Consistency Audit `[Invitational Multi-Part FRQ | Tier 2]`

One mole ($n = 1.000 mol$) of a diatomic ideal gas ($\gamma = 7/5 = 1.400, C_{V,m} = \frac{5}{2}R, C_{P,m} = \frac{7}{2}R$) executes a 4-step closed cycle starting at State 1 ($P_1 = 100.0 kPa, T_1 = 300.0 K, V_1 = 24.943 L$):
- **Leg $1\to 2$ (Isochoric heating):** Pressure triples at constant volume $V_1$ to $P_2 = 300.0 kPa$ ($T_2 = 900.0 K$).
- **Leg $2\to 3$ (Isothermal expansion):** Gas expands reversibly at $T_3 = T_2 = 900.0 K$ until $V_3 = 2V_1 = 49.887 L$ ($P_3 = 150.0 kPa$).
- **Leg $3\to 4$ (Isochoric cooling):** Gas cools at constant volume $V_4 = V_3 = 2V_1$ back to $T_4 = T_1 = 300.0 K$ ($P_4 = 50.00 kPa$).
- **Leg $4\to 1$ (Isothermal compression):** Gas is compressed reversibly at $T_1 = 300.0 K$ from $V_4 = 2V_1$ back to $V_1$.

Construct the complete cycle ledger for $\Delta U, W_{\mathrm{by}}, Q, \Delta H, \Delta S$ across all 4 legs and determine the cycle's net work output $W_{\mathrm{net,by}}$.
**Solution.** Using $R = 8.314463 J/mol/K$, $C_{V,m} = 20.7862 J/mol/K$, and $C_{P,m} = 29.1006 J/mol/K$:

| **Leg** | **Process Type & Endpoints** | $\Delta U$ ($J$) | $W_{\mathrm{by}}$ ($J$) | $Q = \Delta U + W_{\mathrm{by}}$ ($J$) | $\Delta H$ ($J$) | $\Delta S$ ($J/K$) |
| --- | --- | --- | --- | --- | --- | --- |
| $1\to 2$ | Isochoric ($V=V_1, 300 K\to900 K$) | $+12471.7$ | $0.0$ | $+12471.7$ | $+17460.4$ | $+22.836$ |
| $2\to 3$ | Isothermal ($T=900 K, V_1\to 2V_1$) | $0.0$ | $+5186.1$ | $+5186.1$ | $0.0$ | $+5.763$ |
| $3\to 4$ | Isochoric ($V=2V_1, 900 K\to300 K$) | $-12471.7$ | $0.0$ | $-12471.7$ | $-17460.4$ | $-22.836$ |
| $4\to 1$ | Isothermal ($T=300 K, 2V_1\to V_1$) | $0.0$ | $-1728.7$ | $-1728.7$ | $0.0$ | $-5.763$ |
| **Cycle Sum** | **Closed Loop ($1\to 2\to 3\to 4\to 1$)** | $\mathbf{0.0}$ | $\mathbf{+3457.4}$ | $\mathbf{+3457.4}$ | $\mathbf{0.0}$ | $\mathbf{0.000}$ |

Notice that this cycle is a **Stirling cycle** with volume ratio $V_{\max}/V_{\min} = 2$: its net work is $W_{\mathrm{net,by}} = nR(T_H - T_C)\ln 2 = (1.000)(8.314463)(600.0)(0.693147) = \mathbf{+3457.4 J}$.

**✓ Verified by:** State-function sums $\sum\Delta U = \sum\Delta H = \sum\Delta S = 0$ and $\sum Q - \sum W_{\mathrm{by}} = 3457.40 - 3457.40 = 0.00 J$ (`check_sec06_09.py::ex07_6`).

## Joule Free Expansion ($U = \mathrm{const}$) vs. Joule–Thomson Throttling ($H = \mathrm{const}$)

One of the highest-frequency conceptual and quantitative traps on Division C exams (`2019 MIT E2 MC6–MC7`) is confusing **Joule free expansion** (an unrestrained closed-system expansion into vacuum where $\mathbf{\Delta U = 0}$) with **Joule–Thomson throttling** (a continuous steady-flow expansion across a porous plug, capillary tube, or partially opened valve where $\mathbf{\Delta H = 0}$)  **[S13,S16,S26]**.

### [FORMULA & DECISION CARD: Joule Free Expansion vs. Joule–Thomson Throttling & Inversion Criterion  **[S13,S16,S33]**]
- **Joule Adiabatic Free Expansion (1845 — Closed Double-Chamber Vessel Into Vacuum):**
- *System & First Law:* Rigid insulated outer boundary ($Q = 0$) containing Gas in Chamber 1 ($V_1$) and Vacuum in Chamber 2. Opening the internal stopcock performs zero boundary work against the rigid walls ($W_{\mathrm{by}} = 0$), so $\boxed{\Delta U = Q - W_{\mathrm{by}} = 0 \implies U_2 = U_1}$.
- *Temperature response:* For an **ideal gas**, $U = U(T)$ only $\implies \Delta T = 0$ (and $\Delta H = \Delta U + \Delta(nRT) = 0$). For a **Van der Waals real gas**, $U_{\mathrm{vdW}} = nC_{V,m}T - an^2/V$, so doing internal work against attractive forces **always cools** the gas: $\Delta T_{\mathrm{free}} = -\frac{an}{C_{V,m}}\left(\frac{1}{V_1} - \frac{1}{V_2}\right) < 0$.
- **Joule–Thomson Adiabatic Throttling (1852 — Steady Flow Across Porous Plug / Expansion Valve):**
- *Algebra-Only Flow-Work Proof That $H_1 = H_2$:* Follow a fixed mass $m$ (or $n$ moles) pushed through an insulated porous plug ($\dot{Q} = 0$, no shaft work $\dot{W}_s = 0$) from upstream pressure $P_1$ (volume $V_1$) to downstream pressure $P_2 < P_1$ (volume $V_2$). The upstream fluid pushes the packet in with work $W_{\mathrm{in,on}} = +P_1 V_1$, while the packet pushes the downstream fluid out with work $W_{\mathrm{out,by}} = +P_2 V_2$. Net work done *by* the packet is $W_{\mathrm{by}} = P_2 V_2 - P_1 V_1$. Applying the First Law $U_2 - U_1 = Q - W_{\mathrm{by}} = 0 - (P_2 V_2 - P_1 V_1)$ gives:
    
$$
\begin{aligned}

      \boxed{U_1 + P_1 V_1 = U_2 + P_2 V_2 \iff H_1 = H_2 \quad (\Delta H = 0, \text{ strictly ISENTHALPIC!})}
\end{aligned}
$$

    
- *Joule–Thomson Coefficient $\mu_{\mathrm{JT}}$ and Inversion Temperature $T_{\mathrm{inv}}$:*
    The rate of temperature change with pressure at constant enthalpy is $\mu_{\mathrm{JT}} \equiv \left(\frac{\Delta T}{\Delta P}\right)_H$. For a dilute Van der Waals gas:
    
$$
\begin{aligned}

      \boxed{\mu_{\mathrm{JT}} = \left(\frac{\Delta T}{\Delta P}\right)_H \approx \frac{1}{C_{P,m}}\left(\frac{2a}{RT} - b\right)}, \qquad T_{\mathrm{inv,max}} = \frac{2a}{Rb} = \frac{27}{4}T_c = 6.75\,T_c
\end{aligned}
$$

    
    Since throttling always has $\mathbf{\Delta P = P_2 - P_1 < 0}$, the sign of $\Delta T = \mu_{\mathrm{JT}}\Delta P$ is **opposite** to the sign of $\mu_{\mathrm{JT}}$:
- **Below Inversion Temperature ($T < T_{\mathrm{inv}} \implies \mu_{\mathrm{JT}} > 0$):** $\Delta P < 0$ and $\mu_{\mathrm{JT}} > 0 \implies \mathbf{\Delta T < 0}$ (**COOLING!**). Includes $\mathrm{N_2}, \mathrm{O_2}, \mathrm{Ar}, \mathrm{CO_2}, \mathrm{CH_4}, \mathrm{NH_3}, \mathrm{R134a}$ at $300 K$.
- **Above Inversion Temperature ($T > T_{\mathrm{inv}} \implies \mu_{\mathrm{JT}} < 0$):** Excluded-volume repulsion $b$ dominates ($P_1V_1 > P_2V_2$), so $\Delta P < 0$ and $\mu_{\mathrm{JT}} < 0 \implies \mathbf{\Delta T > 0}$ (**HEATING!**). Includes $\mathbf{\mathrm{He}}$ ($T_{\mathrm{inv,max}} \approx 40 K$) and $\mathbf{\mathrm{H_2}}$ ($T_{\mathrm{inv,max}} \approx 202 K$) at room temperature ($300 K$)!
- **Ideal Gas ($a = b = 0$):** $\mu_{\mathrm{JT}} = 0 \implies \Delta T = 0$ at all pressures.
    

  

> **[Vector Figure: (a) Physical boundary distinction between closed-system Joule free expansion ($\Delta U = 0$) and steady-flow Joule–Thomson throttling ($\Delta H = 0$). (b) Joule–Thomson $T$–$P$ inversion locus (solid curve, where $\mu_{\mathrm{JT}} = 0$ and isenthalps $H=\mathrm{const}$ reach their peak temperature): throttling ($\Delta P < 0$, moving left along an isenthalp) cools the gas inside the dome ($\mu_{\mathrm{JT}} > 0$) but warms the gas outside the dome ($\mu_{\mathrm{JT}} < 0$)  **[S16,S33]**. | Label: `fig:07:joule-thomson`]**
> - **Diagram Annotations & Key Elements:** **Title:** **(b) J–T Inversion Curve & Isenthalps ($H=\mathrm{const}$)** • **X-Axis:** Pressure $P$ ($bar$) • **Y-Axis:** Temperature $T$ ($K$) • (a) Closed Free Expansion vs. Open Steady Throttling • **Gas** ($P_1, V_1, T_1$) / $\Delta U = 0$ • **Vacuum** ($P_{\mathrm{ext}}=0$) / $Q=0,\ W_{\mathrm{by}}=0$ • Joule Free Expansion: $U_1 = U_2$ (Closed Rigid Boundary) • Porous Plug • Joule–Thomson Throttling: $h_1 = u_1+P_1v_1 = u_2+P_2v_2 = h_2$ • **Cooling Dome** / $\mu_{\mathrm{JT}} > 0$ ($\Delta T < 0$) • **Heating Zone** / $\mu_{\mathrm{JT}} < 0$ ($\Delta T > 0$) • Isenthalps $H=\mathrm{const}$

### Worked Example — Joule–Thomson Throttling of $\mathrm{N_2}$ vs. $\mathrm{He}$ at $300 K$ & Wet-Steam Throttle Quality `[Invitational / National | Tier 3]`

(a) Using the Van der Waals parameters from Table `tab:06:vdw-constants` and $C_{P,m}$ from Table `tab:06:gas-properties`, compute the low-pressure Joule–Thomson coefficient $\mu_{\mathrm{JT}}$ at $T = 300.0 K$ for Nitrogen ($\mathrm{N_2}$: $a = 0.1370 Pa m^6/mol^2, b = 3.870×10^{-5} m^3/mol, C_{P,m} = 29.17 J/mol/K$) and Helium ($\mathrm{He}$: $a = 0.00346 Pa m^6/mol^2, b = 2.380×10^{-5} m^3/mol, C_{P,m} = 20.79 J/mol/K$), and find the temperature change $\Delta T$ when each gas is throttled from $P_1 = 101.0 bar$ to $P_2 = 1.000 bar$ ($\Delta P = -100.0 bar = -1.000×10^{7} Pa$). (b) Saturated liquid water at $T_1 = 150.0 °C$ ($h_1 = h_{f,150 °C} = 632.18 kJ/kg$) is throttled through an expansion valve to atmospheric pressure $P_2 = 101.325 kPa$ ($T_{\mathrm{sat}} = 100.0 °C$, where $h_f = 419.06 kJ/kg$ and $L_v = h_{fg} = 2256.4 kJ/kg$ from NIST Table 3.3  **[S09]**). Find the exit vapor quality $x_2$.
**Solution.**
- **(a) Joule–Thomson coefficients at $T = 300.0 K$ ($RT = 2494.34 J/mol$) from Eq. (`eq:07:mu-jt`):**
- **Nitrogen ($\mathrm{N_2}$):**
    
$$
\mu_{\mathrm{JT,N_2}} = \frac{1}{29.17}\left(\frac{2(0.1370)}{2494.34} - 3.870\times 10^{-5}\right) = \frac{1.0985\times 10^{-4} - 3.870\times 10^{-5}}{29.17} = \mathbf{+2.439×10^{-6} K/Pa} = \mathbf{+0.2439 K/bar}
$$

    
$$
\Delta T_{\mathrm{N_2}} = \mu_{\mathrm{JT,N_2}}\Delta P = (+0.2439\,K/bar)(-100.0\,bar) = \mathbf{-24.39 K} \quad (\mathrm{N_2}\text{ **cools** to } 275.6 K!)
$$
- **Helium ($\mathrm{He}$):**
    
$$
\mu_{\mathrm{JT,He}} = \frac{1}{20.79}\left(\frac{2(0.00346)}{2494.34} - 2.380\times 10^{-5}\right) = \frac{2.774\times 10^{-6} - 2.380\times 10^{-5}}{20.79} = \mathbf{-1.011×10^{-6} K/Pa} = \mathbf{-0.1011 K/bar}
$$

    
$$
\Delta T_{\mathrm{He}} = \mu_{\mathrm{JT,He}}\Delta P = (-0.1011\,K/bar)(-100.0\,bar) = \mathbf{+10.11 K} \quad (\mathrm{He}\text{ **warms** to } 310.1 K!)
$$
- **(b) Isenthalpic flash-evaporation quality of throttled water ($h_2 = h_1 = 632.18 kJ/kg$):**
  
$$
h_2 = h_{f,100 °C} + x_2 h_{fg,100 °C} = h_1 \implies x_2 = \frac{h_1 - h_{f,100 °C}}{h_{fg,100 °C}} = \frac{632.18 - 419.06}{2256.4} = \frac{213.12}{2256.4} = \mathbf{0.09445} \quad (9.45\%\text{ flashes to steam!})
$$

**✓ Verified by:** Max inversion temperatures Eq. (`eq:07:mu-jt`): $T_{\mathrm{inv,N_2}} = 2a/(Rb) = 851.6 K > 300 K$, whereas $T_{\mathrm{inv,He}} = 34.97 K < 300 K$ (`check_sec06_09.py::ex07_7`).

## Open-System Steady-Flow First Law (SFEE) & Tank-Charging Transients

For an open control volume operating in steady state ($\Delta m_{\mathrm{cv}}/\Delta t = 0$ and $\Delta E_{\mathrm{cv}}/\Delta t = 0$), mass conservation requires $\dot{m}_{\mathrm{in}} = \dot{m}_{\mathrm{out}} = \dot{m} = \rho A v_{\mathrm{flow}} = A v_{\mathrm{flow}}/v$ ($kg/s$). Because the entering fluid brings internal energy $u_1$ plus flow work $P_1 v_1$ ($u_1 + P_1 v_1 = h_1$), the **Steady-Flow Energy Equation (SFEE)** automatically replaces $u$ with specific enthalpy $h = u + Pv$  **[S12,S16,S33]**:

$$
\begin{aligned}

  \boxed{\dot{Q}_{\mathrm{cv}} - \dot{W}_{s,\mathrm{by}} = \dot{m}\left[(h_2 - h_1) + \frac{v_{\mathrm{flow},2}^2 - v_{\mathrm{flow},1}^2}{2} + g_n(z_2 - z_1)\right]}, \qquad q_{\mathrm{cv}} - w_{s,\mathrm{by}} = (h_2 - h_1) + \frac{v_{\mathrm{flow},2}^2 - v_{\mathrm{flow},1}^2}{2} + g_n(z_2 - z_1)
\end{aligned}
$$

### [FORMULA & DECISION CARD: Master Steady-Flow Engineering Device & Unsteady Tank-Charging Table  **[S12,S16,S33]**]

| **Open-System Device** | **Negligible Terms** | **Governing Algebraic First-Law Relation** | **Crucial Unit & Physics Notes** |
| --- | --- | --- | --- |
| **1. Adiabatic Nozzle** | $\dot{Q}=0, \dot{W}_s=0, \Delta z=0$ | $v_{\mathrm{flow},2} = \sqrt{v_{\mathrm{flow},1}^2 + 2(h_1 - h_2)}$ | Convert $\Delta h$ from $kJ/kg$ to $\mathbf{J/kg}$ ($\times 1000$)! |
| **2. Adiabatic Turbine** | $\dot{Q}=0, \Delta\mathrm{KE}\approx 0$ | $\dot{W}_{t,\mathrm{by}} = \dot{m}(h_1 - h_2) > 0$ | Isentropic efficiency: $\eta_t = \dfrac{h_1 - h_{2a}}{h_1 - h_{2s}} \le 1$. |
| **3. Compressor / Pump** | $\dot{Q}=0, \Delta\mathrm{KE}\approx 0$ | $\dot{W}_{\mathrm{in,on}} = -\dot{W}_{s,\mathrm{by}} = \dot{m}(h_2 - h_1) > 0$ | Liquid pump: $w_{p,\mathrm{in}} \approx v_f(P_2 - P_1)$; $\eta_c = \dfrac{h_{2s}-h_1}{h_{2a}-h_1}$. |
| **4. Throttling Valve** | $\dot{Q}=0, \dot{W}_s=0, \Delta\mathrm{KE}\approx 0$ | $h_2 = h_1$ ($u_2 + P_2 v_2 = u_1 + P_1 v_1$) | Strictly isenthalpic; pressure drops ($P_2 < P_1$). |
| **5. Heat Exchanger** | $\dot{W}_s=0, \dot{Q}_{\mathrm{ext}}=0$ | $\dot{m}_{\mathrm{hot}}(h_{h,\mathrm{in}} - h_{h,\mathrm{out}}) = \dot{m}_{\mathrm{cold}}(h_{c,\mathrm{out}} - h_{c,\mathrm{in}})$ | Each stream stays at constant pressure ($\Delta h = c_p\Delta T$). |
| **6. Evacuated Tank Fill** | Insulated rigid tank | $u_{\mathrm{tank},2} = h_{\mathrm{line}} \implies C_{V,m}T_{\mathrm{tank},2} = C_{P,m}T_{\mathrm{line}}$ | $\boxed{T_{\mathrm{tank},2} = \gamma\,T_{\mathrm{line}}}$ (flow work heats tank gas by $\gamma\times$!). |

### Worked Example — Adiabatic Steam Nozzle Velocity & Insulated Evacuated Tank Filling Paradox `[National/Invitational | Tier 3]`

(a) Superheated steam enters an insulated horizontal converging–diverging nozzle at $P_1 = 1.000 MPa, T_1 = 300.0 °C$ with specific enthalpy $h_1 = 3051.6 kJ/kg$ and inlet speed $v_{\mathrm{flow},1} = 50.00 m/s$, and exits at $P_2 = 101.325 kPa$ with specific enthalpy $h_2 = 2675.6 kJ/kg$. Calculate the exit speed $v_{\mathrm{flow},2}$. (b) An insulated, rigid, initially evacuated tank ($n_1 = 0$) is connected via a valve to a large supply pipeline carrying dry air ($\gamma = 1.400$) at $T_{\mathrm{line}} = 300.0 K$ and $P_{\mathrm{line}} = 500.0 kPa$. The valve is opened until the tank pressure reaches $P_{\mathrm{line}}$ and is then closed. Find the final temperature $T_{\mathrm{tank},2}$ of the air inside the tank!
**Solution.**
- **(a) Adiabatic nozzle exit speed (converting $\Delta h = 3051.6 - 2675.6 = 376.0 kJ/kg = 3.760×10^{5} J/kg$!):**
  
$$
v_{\mathrm{flow},2} = \sqrt{v_{\mathrm{flow},1}^2 + 2(h_1 - h_2)} = \sqrt{(50.00)^2 + 2(3.760\times 10^5)} = \sqrt{2500 + 752000} = \mathbf{868.62 m/s}
$$
- **(b) Unsteady tank-filling First-Law ledger:**
  When $n_2$ moles enter the rigid evacuated tank ($Q = 0, W_{\mathrm{tank,by}} = 0$) from the supply line, the pipeline performs flow work $W_{\mathrm{flow,on}} = P_{\mathrm{line}}V_{\mathrm{line}} = n_2 R T_{\mathrm{line}}$ pushing those $n_2$ moles across the valve, in addition to their internal energy $U_{\mathrm{in}} = n_2 C_{V,m} T_{\mathrm{line}}$. Thus the final internal energy of the tank gas is:
  
$$
U_{\mathrm{tank},2} = n_2 C_{V,m} T_{\mathrm{tank},2} = U_{\mathrm{in}} + W_{\mathrm{flow,on}} = n_2(C_{V,m} + R)T_{\mathrm{line}} = n_2 C_{P,m} T_{\mathrm{line}} \implies T_{\mathrm{tank},2} = \gamma T_{\mathrm{line}} = 1.400(300.0 K) = \mathbf{420.0 K}
$$

  The air inside the tank warms by $+120.0 K$ ($146.9 °C$) solely from the pipeline's $PV$ push work!

**✓ Verified by:** Nozzle kinetic energy check: $\frac{1}{2}(868.62^2 - 50^2) = 376000 J/kg = 376.0 kJ/kg$ (`check_sec06_09.py::ex07_8`).

## Coordinate Transformation Atlas ($P$–$V \leftrightarrow P$–$T \leftrightarrow V$–$T$) & Compound Spring/Stop Cylinders

Invitational and National exams frequently plot ideal-gas cycles on **$P$–$T$** or **$V$–$T$** axes (`2019 MIT E2 P2b TB #4`) or couple a gas to mechanical stops and linear springs  **[S26,S28,S33]**. Use the conversion matrix below to translate any path across all three thermodynamic planes before calculating work or heat.

### [FORMULA & DECISION CARD: Master $P$–$V \leftrightarrow P$–$T \leftrightarrow V$–$T$ Coordinate Transformation & Slope Rules  **[S13,S26,S33]**]

| **Process Type** | **On $P$–$V$ Plane** | **On $P$–$T$ Plane** | **On $V$–$T$ Plane** | **Slope & Ray-Through-Origin Comparison Rules** |
| --- | --- | --- | --- | --- |
| **Isochoric** ($V=\mathrm{const}$) | Vertical line | **Ray through origin** | Horizontal line | On $P$–$T$: $P = \left(\dfrac{nR}{V}\right)T \implies$ **larger $V$ = shallower ray slope**! |
| **Isobaric** ($P=\mathrm{const}$) | Horizontal line | Horizontal line | **Ray through origin** | On $V$–$T$: $V = \left(\dfrac{nR}{P}\right)T \implies$ **larger $P$ = shallower ray slope**! |
| **Isothermal** ($T=\mathrm{const}$) | Hyperbola $P \propto 1/V$ | Vertical line | Vertical line | Moving up on $P$–$T$ at fixed $T$ is compression ($V$ decreases). |
| **Adiabatic** ($PV^\gamma=\mathrm{const}$) | Steep curve $P \propto V^{-\gamma}$ | Curve $P \propto T^{\frac{\gamma}{\gamma-1}}$ | Curve $V \propto T^{-\frac{1}{\gamma-1}}$ | On $P$–$T$: slope $\dfrac{\Delta P}{\Delta T} = \dfrac{\gamma}{\gamma - 1}\dfrac{P}{T}$ is $\mathbf{\dfrac{\gamma}{\gamma - 1}\times}$ steeper than isochor ray! |

- **The `2019 MIT E2 P2b(i)` $P$–$T$ Extensive Work Trap:** A $P$–$T$ diagram specifies intensive variables $(P, T)$ only. Although cycle efficiency $\eta = W_{\mathrm{net}}/Q_H$ and molar heat capacities $C_{V,m}, C_{P,m}$ can be found directly from pressure and temperature ratios on a $P$–$T$ plot, total extensive work $W_{\mathrm{by}}$ ($J$) **cannot be determined** unless the mole number $n$ (or volume $V$ at one state) is also given!
- **Extracting $C_{V,m}$ and Molecular Geometry from an Adiabat on a $P$–$T$ Plot (`2019 MIT E2 P2b(iii)`):**
  Given two points $(T_1, P_1)$ and $(T_2, P_2)$ along a reversible adiabat on a $P$–$T$ graph, taking natural logarithms of $P_2/P_1 = (T_2/T_1)^{\gamma/(\gamma-1)} = (T_2/T_1)^{(C_{V,m}+R)/R}$ yields:
  
$$
\begin{aligned}

    \frac{\gamma}{\gamma - 1} = \frac{C_{P,m}}{R} = 1 + \frac{C_{V,m}}{R} = \frac{\ln(P_2/P_1)}{\ln(T_2/T_1)} \implies \boxed{\frac{C_{V,m}}{R} = \frac{\ln(P_2/P_1)}{\ln(T_2/T_1)} - 1, \qquad f = 2\left[\frac{\ln(P_2/P_1)}{\ln(T_2/T_1)} - 1\right]}
\end{aligned}
$$

  

### Worked Example — Decoding a Cycle Plotted on $P$–$T$ Axes & Extracting Molecular Structure `[2019 MIT E2 P2b | Tier 3]`

An ideal gas undergoes a reversible Carnot cycle plotted on a $P$–$T$ diagram between cold reservoir $T_C = 298.0 K$ and hot reservoir $T_H = 390.0 K$. Along the adiabatic compression leg ($1\to 2$) from $T_1 = T_C = 298.0 K$ to $T_2 = T_H = 390.0 K$, the pressure triples ($P_2/P_1 = 3.000$). (a) Calculate the Carnot thermal efficiency $\eta$. (b) Use Eq. (`eq:07:pt-adiabat-cv`) to determine $C_{V,m}/R$, $C_{P,m}/R$, $\gamma$, the active degrees of freedom $f$, and the molecular geometry of the gas. (c) If $n = 2.000 mol$ and the isothermal expansion leg ($2\to 3$) at $T_H = 390.0 K$ drops the pressure from $P_2 = 600.0 kPa$ to $P_3 = 300.0 kPa$, find $Q_H, W_{\mathrm{net,by}}$, and $Q_C$ for the cycle.
**Solution.**
- **(a) Carnot efficiency:**
  
$$
\eta = 1 - \frac{T_C}{T_H} = 1 - \frac{298.0}{390.0} = \frac{92.0}{390.0} = \mathbf{0.23590} \quad (23.59\%)
$$
- **(b) Extracting heat capacity and molecular geometry from the $P$–$T$ adiabat Eq. (`eq:07:pt-adiabat-cv`):**
  
$$
1 + \frac{C_{V,m}}{R} = \frac{\ln(P_2/P_1)}{\ln(T_2/T_1)} = \frac{\ln(3.000)}{\ln(390.0/298.0)} = \frac{1.098612}{0.269055} = \mathbf{4.0832 \approx 4.00}
$$

  
$$
\implies \boxed{C_{V,m} \approx 3R = 24.94 J/mol/K}, \qquad C_{P,m} \approx 4R = 33.26 J/mol/K, \qquad \gamma = \frac{4}{3} \approx 1.333, \qquad f = 6
$$

  Since $f = 6$ ($3$ translational $+ 3$ rotational degrees of freedom), the gas is a **nonlinear polyatomic molecule with $\ge 3$ atoms** (such as $\mathrm{H_2O}(g), \mathrm{NH_3}$, or $\mathrm{CH_4}$).
- **(c) Cycle heat and net work for $n = 2.000 mol$ with $P_2/P_3 = 600.0/300.0 = 2.000$:**
  
$$
Q_H = nRT_H\ln\left(\frac{P_2}{P_3}\right) = (2.000)(8.314463)(390.0)\ln(2.000) = \mathbf{+4494.6 J}
$$

  
$$
W_{\mathrm{net,by}} = \eta Q_H = \left(\frac{92.0}{390.0}\right)(4494.6) = \mathbf{+1060.3 J}, \qquad Q_C = Q_H - W_{\mathrm{net,by}} = \mathbf{3434.3 J}
$$

**✓ Verified by:** Direct cold-isotherm check: $Q_C = nRT_C\ln 2 = 2(8.314463)(298.0)\ln 2 = 3434.3 J$ and $Q_H - Q_C = 1060.3 J$ (`check_sec06_09.py::ex07_9`).

### [FORMULA & DECISION CARD: Three-Stage Stop-Pin & Spring-Loaded Piston-Cylinder Heating Protocol  **[S16,S33]**]

Consider a vertical cylinder of cross-sectional area $A$ holding $n$ moles of gas beneath a piston of mass $m_p$ resting on lower mechanical stops at volume $V_1$, with a linear spring of stiffness $k_{\mathrm{sp}}$ positioned above the piston so that it first touches at volume $V_2 \ge V_1$:
- **Stage 1 — Piston Seated on Bottom Stops ($V = V_1$, for $P_1 \le P \le P_{\mathrm{lift}}$):**
  The piston cannot rise until the internal gas pressure balances atmospheric pressure plus the piston's weight:
  
$$
\begin{aligned}

    \boxed{P_{\mathrm{lift}} = P_{\mathrm{atm}} + \frac{m_p g_n}{A}}, \qquad T_{\mathrm{lift}} = \frac{P_{\mathrm{lift}}V_1}{nR}, \qquad W_{\mathrm{by},1\to\mathrm{lift}} = 0, \qquad Q_{1\to\mathrm{lift}} = \Delta U_{1\to\mathrm{lift}} = \frac{V_1(P_{\mathrm{lift}} - P_1)}{\gamma - 1}
\end{aligned}
$$

  
- **Stage 2 — Free Isobaric Rise Before Spring Contact ($P = P_{\mathrm{lift}}$, for $V_1 \le V \le V_2$):**
  
$$
\begin{aligned}

    T_2 = \frac{P_{\mathrm{lift}}V_2}{nR}, \qquad W_{\mathrm{by},\mathrm{lift}\to 2} = P_{\mathrm{lift}}(V_2 - V_1), \qquad Q_{\mathrm{lift}\to 2} = \Delta H_{\mathrm{lift}\to 2} = \frac{\gamma P_{\mathrm{lift}}(V_2 - V_1)}{\gamma - 1}
\end{aligned}
$$
- **Stage 3 — Linear Spring Compression ($V_2 \le V \le V_3$, spring compressed by $\Delta x = (V - V_2)/A$):**
  
$$
\begin{aligned}

    P_3 = P_{\mathrm{lift}} + \frac{k_{\mathrm{sp}}(V_3 - V_2)}{A^2}, \qquad W_{\mathrm{by},2\to 3} = \frac{P_{\mathrm{lift}} + P_3}{2}(V_3 - V_2) = \underbrace{P_{\mathrm{lift}}(V_3 - V_2)}_{\text{atm + piston lift work}} + \underbrace{\frac{1}{2}k_{\mathrm{sp}}(\Delta x_3)^2}_{\text{elastic energy stored in spring}}
\end{aligned}
$$

  

### Worked Example — Three-Stage Stop-Pin + Free-Rise + Spring-Loaded Cylinder Heating Ledger `[National/Invitational FRQ | Tier 3]`

A vertical cylinder of cross-sectional area $A = 0.01000 m^2$ ($100.0 cm^2$) contains $n = 0.5000 mol$ of monatomic Argon ($\gamma = 5/3, C_{V,m} = \frac{3}{2}R$) initially at $P_1 = 100.0 kPa$ and $V_1 = 10.00 L$ ($0.01000 m^3$), with a frictionless piston of mass $m_p = 50.986 kg$ resting on lower stops ($P_{\mathrm{atm}} = 100.0 kPa, g_n = 9.80665 m/s^2$). At a height corresponding to $V_2 = 15.00 L$ ($0.01500 m^3$), the top of the piston contacts an unstretched linear spring of stiffness $k_{\mathrm{sp}} = 20.00 kN/m$ ($2.000×10^{4} N/m$). Heat is slowly added to the Argon until the volume reaches $V_3 = 20.00 L$ ($0.02000 m^3$). Find (a) the lift-off pressure $P_{\mathrm{lift}}$ and initial/final temperatures $T_1, T_3$, (b) the total boundary work $W_{\mathrm{by},1\to 3}$ and the elastic potential energy $E_{\mathrm{spring}}$ stored in the spring, and (c) the total heat $Q_{1\to 3}$ added to the gas.
**Solution.**
- **(a) Lift-off pressure $P_{\mathrm{lift}}$, final pressure $P_3$, and temperatures $T_1, T_3$:**
  
$$
P_{\mathrm{lift}} = P_{\mathrm{atm}} + \frac{m_p g_n}{A} = 100.0×10^{3} Pa + \frac{(50.986)(9.80665)}{0.01000} = 100.0\times 10^3 + 50.00\times 10^3 = \mathbf{150.0 kPa}
$$

  From $V_2 = 15.00 L$ to $V_3 = 20.00 L$, the piston rises by $\Delta x_3 = \frac{V_3 - V_2}{A} = \frac{0.00500 m^3}{0.01000 m^2} = 0.5000 m$, compressing the spring:
  
$$
P_3 = P_{\mathrm{lift}} + \frac{k_{\mathrm{sp}}\Delta x_3}{A} = 150.0 kPa + \frac{(20.00 kN/m)(0.5000 m)}{0.01000 m^2} = 150.0 + 1000.0 = \mathbf{1150.0 kPa}
$$

  
$$
T_1 = \frac{P_1 V_1}{nR} = \frac{(100.0)(10.00)}{(0.5000)(8.314463)} = \mathbf{240.54 K}, \qquad T_3 = \frac{P_3 V_3}{nR} = \frac{(1150.0)(20.00)}{(0.5000)(8.314463)} = \mathbf{5532.5 K}
$$
- **(b) Stage-by-stage boundary work $W_{\mathrm{by},1\to 3}$ and spring energy $E_{\mathrm{spring}}$:**
- Stage 1 (Isochoric at $V_1 = 10.00 L$, $P: 100\to150 kPa$): $W_1 = 0.00 J$.
- Stage 2 (Isobaric at $P_{\mathrm{lift}} = 150.0 kPa$, $V: 10.00\to15.00 L$): $W_2 = (150.0)(15.00 - 10.00) = +750.0 J$.
- Stage 3 (Linear spring, $V: 15.00\to20.00 L$, $P: 150.0\to1150.0 kPa$):
    
$$
W_3 = \frac{150.0 + 1150.0}{2}(20.00 - 15.00) = +3250.0 J, \qquad E_{\mathrm{spring}} = \frac{1}{2}k_{\mathrm{sp}}(\Delta x_3)^2 = \frac{1}{2}(20000)(0.5000)^2 = \mathbf{2500.0 J}
$$

  

  
$$
W_{\mathrm{by},1\to 3} = W_1 + W_2 + W_3 = 0 + 750.0 + 3250.0 = \mathbf{+4000.0 J} = \mathbf{+4.000 kJ}
$$
- **(c) Internal energy change $\Delta U_{1\to 3}$ and total heat input $Q_{1\to 3}$:**
  
$$
\Delta U_{1\to 3} = \frac{P_3 V_3 - P_1 V_1}{\gamma - 1} = \frac{3}{2}\left[(1150.0)(20.00) - (100.0)(10.00)\right] = \frac{3}{2}(23000 - 1000) = \mathbf{+33000.0 J} = \mathbf{+33.00 kJ}
$$

  
$$
Q_{1\to 3} = \Delta U_{1\to 3} + W_{\mathrm{by},1\to 3} = 33.00 + 4.000 = \mathbf{+37.00 kJ}
$$

**✓ Verified by:** Work partition check Eq. (`eq:07:piston-spring-stage`): $P_{\mathrm{lift}}(V_3 - V_1) + E_{\mathrm{spring}} = 150.0(10.00) + 2500.0 = 1500.0 + 2500.0 = 4000.0 J$ (`check_sec06_09.py::ex07_10`).

### [FORMULA & DECISION CARD: General Partial Tank Charging, Adiabatic Blowdown & Steady-Flow Mixing Chambers  **[S16,S33]**]
- **Partial Adiabatic Tank Charging ($n_1 > 0 \to n_2$):**
  An insulated rigid tank of volume $V$ initially holding $n_1$ moles of ideal gas at $(P_1, T_1)$ is charged from a supply manifold at temperature $T_{\mathrm{line}}$ until the tank pressure reaches $P_2$. Energy conservation $U_2 - U_1 = (n_2 - n_1)H_{m,\mathrm{line}}$ implies $n_2 T_2 - n_1 T_1 = \gamma(n_2 - n_1)T_{\mathrm{line}}$. Substituting $n_k = P_k V/(R T_k)$ gives the closed algebraic formula for $T_2$:
  
$$
\begin{aligned}

    \boxed{T_2 = \frac{\gamma P_2 T_1 T_{\mathrm{line}}}{\gamma P_1 T_{\mathrm{line}} + (P_2 - P_1)T_1}}
\end{aligned}
$$

  
  (Note: Setting $P_1 = 0$ immediately recovers the evacuated-tank limit $T_2 = \gamma T_{\mathrm{line}}$!)
- **Adiabatic Tank Venting / Blowdown ($P_1 \to P_2 < P_1$):**
  When an insulated tank vents gas rapidly through a valve from $P_1$ down to $P_2$, the gas *remaining inside the tank* expands reversibly and adiabatically against the escaping gas, cooling to:
  
$$
\begin{aligned}

    \boxed{T_{\mathrm{rem},2} = T_1\left(\frac{P_2}{P_1}\right)^{\frac{\gamma - 1}{\gamma}}}, \qquad \frac{n_2}{n_1} = \left(\frac{P_2}{P_1}\right)^{\frac{1}{\gamma}}
\end{aligned}
$$

  
- **Steady-Flow Adiabatic Mixing Chamber ($\dot{Q}=0, \dot{W}_s=0$ at Common Pressure $P$):**
  When $K$ fluid streams with mass flow rates $\dot{m}_i$ and specific enthalpies $h_i$ mix steadily inside an insulated T-junction or feedwater heater to form a single exit stream $\dot{m}_{\mathrm{out}} = \sum_{i=1}^K \dot{m}_i$:
  
$$
\begin{aligned}

    \boxed{h_{\mathrm{out}} = \frac{\sum_{i=1}^K \dot{m}_i h_i}{\sum_{i=1}^K \dot{m}_i}}, \qquad \frac{\dot{m}_1}{\dot{m}_2} = \frac{h_{\mathrm{out}} - h_2}{h_1 - h_{\mathrm{out}}} \quad (\text{two-stream enthalpy lever rule})
\end{aligned}
$$

  

### Worked Example — Partial Tank Charging, Adiabatic Blowdown & Direct-Contact Steam Mixing `[National Tier | Tier 3]`

(a) An insulated rigid SCUBA cylinder ($V = 12.00 L$) initially contains dry air ($\gamma = 1.400$) at $P_1 = 2.000 MPa$ and $T_1 = 300.0 K$. It is rapidly topped off from a compressor manifold at $T_{\mathrm{line}} = 300.0 K$ until the tank pressure reaches $P_2 = 10.00 MPa$. Find the final air temperature $T_2$ inside the cylinder. (b) If the cylinder at $(10.00 MPa, 388.89 K)$ is later vented adiabatically back down to $P_3 = 2.000 MPa$, find the temperature $T_3$ of the remaining air. (c) In a power-plant open feedwater heater operating at $P = 101.325 kPa$, subcooled liquid water at $T_{w,\mathrm{in}} = 20.00 °C$ ($h_w = 84.05 kJ/kg$, $\dot{m}_w = 10.00 kg/s$) mixes directly with superheated steam at $T_{s,\mathrm{in}} = 150.0 °C$ ($h_s = 2776.5 kJ/kg$, NIST Table 3.3  **[S09]**) to produce saturated liquid water at $T_{\mathrm{out}} = 99.97 °C$ ($h_{\mathrm{out}} = h_f = 419.06 kJ/kg$). Calculate the required steam mass flow rate $\dot{m}_s$.
**Solution.**
- **(a) Partial adiabatic charging ($T_1 = T_{\mathrm{line}} = 300.0 K, P_2/P_1 = 5.000$):**
  Evaluating Eq. (`eq:07:partial-tank-charge`) for $P_1 = 2.000 MPa, P_2 = 10.00 MPa, \gamma = 1.400, T_1 = T_{\mathrm{line}} = 300.0 K$:
  
$$
T_2 = \frac{1.400(10.00)}{1.400(2.000) + (10.00 - 2.000)}(300.0 K) = \frac{14.00}{10.80}(300.0 K) = \mathbf{388.89 K}
$$
- **(b) Adiabatic blowdown from $(10.00 MPa, 388.89 K)$ to $2.000 MPa$:**
  
$$
T_3 = (388.89 K)\left(\frac{2.000}{10.00}\right)^{0.400/1.400} = 388.89(0.2000)^{2/7} = \mathbf{245.54 K}
$$
- **(c) Direct-contact steam feedwater heater mass flow rate from Eq. (`eq:07:mixing-chamber`):**
  
$$
\dot{m}_s = \dot{m}_w\,\frac{h_{\mathrm{out}} - h_w}{h_s - h_{\mathrm{out}}} = (10.00 kg/s)\left(\frac{419.06 - 84.05}{2776.5 - 419.06}\right) = 10.00\left(\frac{335.01}{2357.44}\right) = \mathbf{1.4211 kg/s}
$$

**✓ Verified by:** Mole & energy balance: $n_1 = 9.622 mol$, $n_2 = P_2V/(RT_2) = 37.113 mol$, and $\dot{m}_s h_s + \dot{m}_w h_w = (\dot{m}_s+\dot{m}_w)h_{\mathrm{out}} = 4786.1 kW$ (`check_sec06_09.py::ex07_11`).

## Rapid-Solve Tournament First-Law & Process Drill Set

### Worked Example — Elliptical $P$–$V$ Cycle Net Work & Bomb-to-Isobaric Reaction $\Delta H_{\mathrm{rxn}}$ `[Invitational Rapid Drill | Tier 2]`

(a) An ideal gas executes a **clockwise elliptical cycle** on a $P$–$V$ diagram centered at $(V_0, P_0) = (5.000 L, 300.0 kPa)$, oscillating between minimum volume $V_{\min} = 2.000 L$ and maximum volume $V_{\max} = 8.000 L$ and between minimum pressure $P_{\min} = 100.0 kPa$ and maximum pressure $P_{\max} = 500.0 kPa$ (`2018 MIT E3 MC9` archetype). If the gas rejects $|Q_{\mathrm{out}}| = 1500.0 J$ of heat during the cooling half of the ellipse, find the net cycle work $W_{\mathrm{net,by}}$ and the heat absorbed $Q_{\mathrm{in}}$ during the heating half.
(b) Complete combustion of $1.000 mol$ of liquid benzene ($\mathrm{C_6H_6}(l) + \frac{15}{2}\mathrm{O_2}(g) \to 6\mathrm{CO_2}(g) + 3\mathrm{H_2O}(l)$) inside a rigid constant-volume bomb calorimeter at $T = 298.15 K$ releases $|q_V| = 3263.9 kJ/mol$ ($\Delta U_{\mathrm{rxn}} = -3263.9 kJ/mol$). Calculate the constant-pressure molar enthalpy of combustion $\Delta H_{\mathrm{rxn}}$ at $298.15 K$.
**Solution.**
- **(a) Elliptical cycle semi-axes $a = (V_{\max}-V_{\min})/2 = 3.000 L$ and $b = (P_{\max}-P_{\min})/2 = 200.0 kPa$:**
  
$$
W_{\mathrm{net,by}} = +\pi a b = \pi(3.000 L)(200.0 kPa) = 600.0\pi\,J = \mathbf{+1884.96 J}
$$

  Since $\Delta U_{\mathrm{cycle}} = 0$, $Q_{\mathrm{net}} = Q_{\mathrm{in}} - |Q_{\mathrm{out}}| = W_{\mathrm{net,by}} \implies Q_{\mathrm{in}} = 1884.96 + 1500.0 = \mathbf{+3384.96 J}$.
- **(b) Bomb-to-isobaric $\Delta H_{\mathrm{rxn}} = \Delta U_{\mathrm{rxn}} + (\Delta n_{\mathrm{gas}})RT$ conversion:**
  Counting only **gaseous** species ($\mathrm{C_6H_6}(l)$ and $\mathrm{H_2O}(l)$ have negligible molar volume compared to gases):
  
$$
\Delta n_{\mathrm{gas}} = \nu_{\mathrm{CO_2}(g)} - \nu_{\mathrm{O_2}(g)} = 6 - 7.5 = \mathbf{-1.500\,mol gas per mole rxn}
$$

  
$$
\Delta H_{\mathrm{rxn}} = \Delta U_{\mathrm{rxn}} + (\Delta n_{\mathrm{gas}})RT = -3263.9 kJ/mol + (-1.500)(8.314463×10^{-3} kJ/mol/K)(298.15 K) = -3263.9 - 3.718 = \mathbf{-3267.62 kJ/mol}
$$

**✓ Verified by:** Atmosphere does compression work $+3.718 kJ/mol$ as $1.5\,mol$ of gas is consumed, increasing heat released at constant pressure to $3267.62 kJ/mol$ (`check_sec06_09.py::ex07_12`).

### Worked Example — Single-Step vs. Two-Step Irreversible Isothermal Expansion & Non-Ideal Cycle Closure `[Invitational Rapid Drill | Tier 2]`

(a) Two moles ($n = 2.000 mol$) of an ideal gas immersed in a constant-temperature bath at $T = 300.0 K$ expand from $P_1 = 10.00 bar$ ($V_1 = 4.9887 L$) to $P_2 = 1.000 bar$ ($V_2 = 49.887 L$). Compare the boundary work $W_{\mathrm{by}}$ performed by the gas in: (i) a reversible isothermal expansion, (ii) a single-step irreversible expansion against fixed external pressure $P_{\mathrm{ext}} = P_2 = 1.000 bar$, and (iii) a two-step irreversible expansion where $P_{\mathrm{ext}}$ is first dropped to intermediate pressure $P_{\mathrm{mid}} = 3.1623 bar = \sqrt{P_1 P_2}$ until equilibrium is reached at $V_{\mathrm{mid}}$, and then dropped to $P_2 = 1.000 bar$. Prove algebraically that choosing the geometric mean $P_{\mathrm{mid}} = \sqrt{P_1 P_2}$ maximizes two-step irreversible expansion work!
(b) A real fluid executes a 3-leg closed cycle $A\to B\to C\to A$. Along $A\to B$, $Q_{AB} = +50.0 kJ$ and $W_{\mathrm{by},AB} = +20.0 kJ$. Along $B\to C$, $\Delta U_{BC} = -15.0 kJ$ and $W_{\mathrm{by},BC} = -10.0 kJ$. Along $C\to A$, $Q_{CA} = -25.0 kJ$. Find $\Delta U_{AB}$, $Q_{BC}$, $\Delta U_{CA}$, $W_{\mathrm{by},CA}$, and $W_{\mathrm{net,by}}$ for the cycle.
**Solution.**
- **(a) Reversible vs. single-step vs. optimal two-step irreversible expansion ($nRT = 4988.68 J$):**
- **(i) Reversible isothermal:** $W_{\mathrm{rev}} = nRT\ln(P_1/P_2) = (4988.68)\ln(10.00) = \mathbf{+11486.9 J}$.
- **(ii) Single-step irreversible at $P_{\mathrm{ext}} = P_2 = 1.000 bar$:**
    
$$
W_{\text{1-step}} = P_2(V_2 - V_1) = nRT\left(1 - \frac{P_2}{P_1}\right) = 4988.68(1 - 0.1000) = \mathbf{+4489.8 J} \quad (39.1\%\text{ of } W_{\mathrm{rev}})
$$
- **(iii) Two-step irreversible via $P_{\mathrm{mid}}$:**
    
$$
W_{\text{2-step}} = P_{\mathrm{mid}}(V_{\mathrm{mid}} - V_1) + P_2(V_2 - V_{\mathrm{mid}}) = nRT\left[\left(1 - \frac{P_{\mathrm{mid}}}{P_1}\right) + \left(1 - \frac{P_2}{P_{\mathrm{mid}}}\right)\right] = nRT\left[2 - \left(\frac{P_{\mathrm{mid}}}{P_1} + \frac{P_2}{P_{\mathrm{mid}}}\right)\right]
$$

    By the AM–GM inequality, $\frac{P_{\mathrm{mid}}}{P_1} + \frac{P_2}{P_{\mathrm{mid}}} \ge 2\sqrt{\frac{P_2}{P_1}}$ with equality iff $\frac{P_{\mathrm{mid}}}{P_1} = \frac{P_2}{P_{\mathrm{mid}}} \iff \boxed{P_{\mathrm{mid}}^* = \sqrt{P_1 P_2}} = 3.1623 bar$, giving:
    
$$
W_{\text{2-step,max}} = 2nRT\left(1 - \sqrt{\frac{P_2}{P_1}}\right) = 2(4988.68)(1 - 10^{-0.5}) = \mathbf{+6822.2 J} \quad (59.4\%\text{ of } W_{\mathrm{rev}})
$$
- **(b) Real-fluid closed-cycle state-function closure ($\Delta U_{AB} + \Delta U_{BC} + \Delta U_{CA} = 0$):**
- Leg $A\to B$: $\Delta U_{AB} = Q_{AB} - W_{\mathrm{by},AB} = 50.0 - 20.0 = \mathbf{+30.0 kJ}$.
- Leg $B\to C$: $Q_{BC} = \Delta U_{BC} + W_{\mathrm{by},BC} = -15.0 + (-10.0) = \mathbf{-25.0 kJ}$.
- Leg $C\to A$: $\Delta U_{CA} = -(\Delta U_{AB} + \Delta U_{BC}) = -(30.0 - 15.0) = \mathbf{-15.0 kJ} \implies W_{\mathrm{by},CA} = Q_{CA} - \Delta U_{CA} = -25.0 - (-15.0) = \mathbf{-10.0 kJ}$.
- Cycle net work: $W_{\mathrm{net,by}} = 20.0 - 10.0 - 10.0 = Q_{\mathrm{net}} = 50.0 - 25.0 - 25.0 = \mathbf{0.0 kJ}$ (a figure-eight loop with equal clockwise and counterclockwise lobes!).
  

**✓ Verified by:** $N$-step optimal irreversible expansion work $W_N = N nRT[1 - (P_2/P_1)^{1/N}]$ converges to $nRT\ln(P_1/P_2) = 11486.9 J$ as $N\to\infty$ (`check_sec06_09.py::ex07_13`).

### Worked Example — Steady-Flow Adiabatic Turbine + Heat Exchanger Network & Polytropic Shaft Work `[National/Invitational FRQ | Tier 3]`

Dry air ($M = 28.9655 g/mol, R_s = 287.05 J/kg/K, c_p = 1006.2 J/kg/K, \gamma = 1.400$) flows steadily at mass flow rate $\dot{m} = 2.500 kg/s$ through a two-component power module:
- **Component 1 (Adiabatic Gas Turbine, $1\to 2$):** Air enters at $P_1 = 800.0 kPa, T_1 = 1100.0 K$, and inlet speed $v_{\mathrm{flow},1} = 40.00 m/s$, and expands to $P_2 = 100.0 kPa$ with exit speed $v_{\mathrm{flow},2} = 160.0 m/s$. The turbine's isentropic efficiency is $\eta_t = 0.8500$.
- **Component 2 (Exhaust Recuperator Heat Exchanger, $2\to 3$):** The turbine exhaust at $T_{2a}$ passes at constant pressure $P_2 = 100.0 kPa$ (with negligible kinetic energy change) through a counterflow heat exchanger that cools the air to $T_3 = 400.0 K$ while heating a separate liquid water stream ($\dot{m}_w = 4.000 kg/s, c_{p,w} = 4184.0 J/kg/K$) entering at $T_{w,\mathrm{in}} = 295.0 K$.

Find (a) the ideal isentropic turbine exit temperature $T_{2s}$, (b) the actual turbine exit temperature $T_{2a}$ and shaft power output $\dot{W}_{t,\mathrm{by}}$ (including the kinetic energy change!), and (c) the heat transfer rate $\dot{Q}_{\mathrm{HX}}$ and water exit temperature $T_{w,\mathrm{out}}$ in the recuperator.
**Solution.**
- **(a) Ideal isentropic turbine exit temperature $T_{2s}$ ($P_2/P_1 = 100.0/800.0 = 1/8 = 0.1250$):**
  
$$
T_{2s} = T_1\left(\frac{P_2}{P_1}\right)^{\frac{\gamma - 1}{\gamma}} = (1100.0 K)(0.1250)^{0.400/1.400} = 1100.0(0.552045) = \mathbf{607.25 K}
$$
- **(b) Actual turbine exit temperature $T_{2a}$ and shaft power output $\dot{W}_{t,\mathrm{by}}$ from Eq. (`eq:07:sfee`):**
  By the definition of isentropic turbine enthalpy drop $\Delta h_a = \eta_t \Delta h_s$:
  
$$
T_1 - T_{2a} = \eta_t(T_1 - T_{2s}) = 0.8500(1100.0 - 607.25) = 418.84 K \implies T_{2a} = 1100.0 - 418.84 = \mathbf{681.16 K}
$$

  Specific kinetic energy change across the turbine is $\Delta\mathrm{ke} = \frac{1}{2}(v_{\mathrm{flow},2}^2 - v_{\mathrm{flow},1}^2) = \frac{1}{2}(160.0^2 - 40.00^2) = +12000 J/kg = \mathbf{+12.00 kJ/kg}$. Applying the SFEE Eq. (`eq:07:sfee`) with $\dot{Q}_{\mathrm{cv}} = 0$:
  
$$
w_{t,\mathrm{by}} = c_p(T_1 - T_{2a}) - \frac{v_{\mathrm{flow},2}^2 - v_{\mathrm{flow},1}^2}{2} = (1.0062 kJ/kg/K)(418.84\,K) - 12.00 kJ/kg = 421.43 - 12.00 = \mathbf{409.43 kJ/kg}
$$

  
$$
\dot{W}_{t,\mathrm{by}} = \dot{m}\,w_{t,\mathrm{by}} = (2.500 kg/s)(409.43 kJ/kg) = \mathbf{1023.6 kW} = \mathbf{1.0236 MW}
$$
- **(c) Recuperator heat transfer rate $\dot{Q}_{\mathrm{HX}}$ and water exit temperature $T_{w,\mathrm{out}}$:**
  
$$
\dot{Q}_{\mathrm{HX}} = \dot{m} c_p (T_{2a} - T_3) = (2.500 kg/s)(1.0062 kJ/kg/K)(681.16 - 400.0\,K) = \mathbf{707.26 kW}
$$

  
$$
T_{w,\mathrm{out}} = T_{w,\mathrm{in}} + \frac{\dot{Q}_{\mathrm{HX}}}{\dot{m}_w c_{p,w}} = 295.0 K + \frac{707263 W}{(4.000 kg/s)(4184.0 J/kg/K)} = 295.0 + 42.26 = \mathbf{337.26 K} \quad (64.11 °C)
$$

**✓ Verified by:** Total steady-flow enthalpy drop from $T_1=1100 K$ to $T_3=400 K$: $\dot{m}c_p(T_1-T_3) = 1760.85 kW = \dot{W}_{t,\mathrm{by}} + \dot{m}\Delta\mathrm{ke} + \dot{Q}_{\mathrm{HX}} = 1023.59 + 30.00 + 707.26\,kW$ (`check_sec06_09.py::ex07_14`).

### [TRAP & DIAGNOSTIC: Top 6 First-Law & Thermodynamic Process Exam Traps (§7 Diagnostic Matrix)]

| **Wrong move / Symptom** | **What it produces / Why it fails** | **5-second diagnostic & fix** |
| --- | --- | --- |
| Sign flip between Physics $\Delta U = Q - W_{\mathrm{by}}$ and Chemistry $\Delta U = q + w_{\mathrm{on}}$ | Subtracts a negative compression work twice, flipping the sign of $\Delta U$ or $Q$. | Check physical direction first: **expansion** lowers $U$ unless heat enters; **compression** raises $U$ unless heat leaves. |
| Using $W_{\mathrm{by}} = nRT\ln(V_2/V_1)$ for an *irreversible* or *free* expansion | Overestimates work when gas expands into vacuum ($W=0$) or against constant $P_{\mathrm{ext}} = P_2$. | Use $nRT\ln(V_2/V_1)$ **only** for a reversible isothermal path; for constant $P_{\mathrm{ext}}$, $W_{\mathrm{by}} = P_{\mathrm{ext}}(V_2 - V_1)$; for vacuum, $W_{\mathrm{by}} = 0$. |
| Using $Q = nC_{V,m}\Delta T$ for an isobaric process (as in `2018 MIT E3 MC5`) | Omits the boundary expansion work $W_{\mathrm{by}} = nR\Delta T$, underestimating $Q_P$ by factor $1/\gamma$. | At constant $P$, $Q_P = \Delta H = nC_{P,m}\Delta T$; $nC_{V,m}\Delta T$ is $\Delta U$, NOT $Q_P$! |
| Assuming $Q = 0$ means $\Delta T = 0$ (confusing adiabatic with isothermal) | Sets $\Delta U = 0$ in an adiabatic compression/expansion. | Adiabatic means $Q = 0 \implies \Delta U = -W_{\mathrm{by}} \ne 0$: adiabatic expansion **cools** ($\Delta T < 0$), compression **heats** ($\Delta T > 0$). |
| Confusing Joule free expansion ($\Delta U = 0$) with throttling ($\Delta H = 0$) | Claims enthalpy is not conserved in a throttle valve or that real gases do not cool in free expansion. | Rigid sealed chamber into vacuum $\to \Delta U = 0$; steady flow across valve/plug $\to \Delta H = 0$. |
| Forgetting $\times 1000$ when converting $\Delta h$ ($kJ/kg$) in nozzle velocity $v = \sqrt{2\Delta h}$ | Underestimates exit velocity by $\sqrt{1000} = 31.62\times$ (gives $27.5 m/s$ instead of $869 m/s$!). | $1\,kJ/kg = 1000 m^2/s^2$; always multiply $\Delta h[kJ/kg]$ by $1000$ inside the square root! |

### [2027 HEAT-COLLECTOR DEVICE & LAB: First-Law Control-Volume Ledger of the 2027 Heat-Lamp Water Cup (§15 Coupling)]

The $100.0 mL$ water sample inside the 9 oz cup (`2027 Rule 5.II.c`) is an **open control volume** at constant atmospheric pressure $P_{\mathrm{atm}} = 101.325 kPa$ ($W_{\mathrm{shaft}} = 0$). Its First-Law enthalpy balance over the heating interval $t_{\mathrm{heat}} \in [10, 15]\,min$ is:

$$
\begin{aligned}

  (m_w c_{p,w} + C_{\mathrm{cup,eff}})\Delta T_w = Q_{\mathrm{opt,abs}} - Q_{\mathrm{cond/conv,loss}} - Q_{\mathrm{rad,IR,loss}} - (\Delta m_{\mathrm{evap}}) L_v
\end{aligned}
$$

Because water's latent heat of vaporization at $45 °C$ is enormous ($L_v = 2394 kJ/kg = 2394 J/g$, NIST Table 3.1), evaporating just $\Delta m_{\mathrm{evap}} = 0.50 g$ of water ($0.5\%$ of the $100 g$ sample) steals $1197 J$ of enthalpy — erasing $\mathbf{2.86 °C}$ of temperature gain $\mathrm{TG}$! Placing an unattached clear BoPET glazing lid above the cup (`Clarification #5`) suppresses $\Delta m_{\mathrm{evap}} \to 0$ and preserves that $2.86 °C$ gain (§`sec:15`).

—
**See also:** Quick Sheet `QS-06` (§`sec:01.6`); Sign Conventions (§`sec:02`); Ideal & Real Gases (§`sec:06`); Entropy, Enthalpy & Exergy (§`sec:08`); Thermodynamic Cycles (§`sec:09`); Transient Collector Heating (§`sec:13`, §`sec:15`).
