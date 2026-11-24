<!-- Source: src/sec08.tex | Tab: Tab 4: GASES/LAWS | Target: 10 pp -->
# §8: Second Law, Entropy ($\Delta S$), Enthalpy ($\Delta H$), Gibbs/Helmholtz Potentials, Exergy & Third Law {#sec:08}

> **[SCOPE: TIER-DEPENDENT | 2027 Rule 5.c.iv (Core 2nd Law: All Levels) | Rule 5.c.vi–vii (Third Law, Entropy $\Delta S$, Enthalpy $\Delta H$: States & Nationals — Tested on 8/8 Invitational Exams!)]**

### [TIER: STATE & NATIONALS (Rule 5.c.vi–vii): 2027 Rules Scope vs. Observed Invitational Tournament Reality (`8/8` Corpus Alert)]

Under the 2027 Division C Rules Manual  **[S01]**, the **Second Law of Thermodynamics, heat engines, and Carnot efficiency bounds** fall under Clause `5.c.iv` (**REQUIRED at ALL levels: Regionals, States, and Nationals**). The **Third Law of Thermodynamics** (`5.c.vi`) and quantitative **Entropy ($\Delta S$) and Enthalpy ($\Delta H$)** (`5.c.vii`) are formally designated for **State and National tournaments**. However, our 8-exam corpus audit (§`sec:22`) revealed that **$\mathbf{8/8}$ ($\mathbf{100\%}$) of invitational and regional exams** (`E1`–`E8`) tested $\Delta S$, $\Delta H$, and $\Delta G$ — including `2027 Cornell E1 Q28–Q29` (`TB #1` & `TB #8`, 37 points on steam-table $h, s$, Gouy–Stodola exergy destruction $X_{\mathrm{dest}} = T_0 S_{\mathrm{gen}}$, and Second-Law efficiency $\eta_{\mathrm{II}}$)  **[S25,S26,S27]**! Teams at *every* tournament level must keep this section in their active binder.

## The Second Law: Kelvin–Planck & Clausius Equivalence, Irreversibility & Arrow of Time

While the First Law requires total energy to be conserved ($\Delta U_{\mathrm{univ}} = 0$), the **Second Law of Thermodynamics** establishes the directional *arrow of time*, forbidding $100\%$ conversion of heat into work in a cycle and forbidding spontaneous heat flow from cold to hot  **[S13,S16,S23]**:
- **Kelvin–Planck Statement (Heat-Engine Formulation, 1851/1897):** *It is impossible to construct a device operating in a thermodynamic cycle whose sole effect is to absorb heat from a single thermal reservoir and deliver an equivalent amount of net mechanical work* ($Q_C > 0$ is mandatory $\implies \eta = W_{\mathrm{net}}/Q_H < 1$; forbids a **Perpetual Motion Machine of the Second Kind, PMM2**).
- **Clausius Statement (Refrigerator / Heat-Flow Formulation, 1850):** *It is impossible to construct a device operating in a thermodynamic cycle whose sole effect is to transfer heat from a colder body ($T_C$) to a hotter body ($T_H > T_C$) without external work input* ($W_{\mathrm{in}} > 0$ is mandatory $\implies \mathrm{COP}_R = Q_C/W_{\mathrm{in}} < \infty$).

> **[Vector Figure: Proof of logical equivalence between the Kelvin–Planck and Clausius statements via contrapositive coupling  **[S13,S33]**. (a) A hypothetical $100\%$-efficient engine ($W = Q_H$) driving a refrigerator pumps net heat $Q_C$ from $T_C$ to $T_H$ with zero external work (violating Clausius). (b) A hypothetical zero-work heat pump returning $Q_C$ from $T_C$ to $T_H$ leaves the cold reservoir unchanged while a standard engine converts $Q_H - Q_C$ from $T_H$ $100\%$ into work $W$ (violating Kelvin–Planck). | Label: `fig:08:carnot-clausius`]**
> - **Diagram Annotations & Key Elements:** (a) Kelvin–Planck Violator $\Longrightarrow$ Clausius Violator • (b) Clausius Violator $\Longrightarrow$ Kelvin–Planck Violator

### [FORMULA & DECISION CARD: Reversible vs. Irreversible Processes & The 6 Sources of Irreversibility  **[S13,S33]**]

A process is **reversible** ($\Delta S_{\mathrm{univ}} = S_{\mathrm{gen}} = 0$) if and only if both the system and its surroundings can be restored to their exact initial states without leaving any net change elsewhere. Every real process is **irreversible** ($S_{\mathrm{gen}} > 0$) due to one or more of the 6 dissipative mechanisms:
- **Heat transfer across a finite temperature difference** ($T_H > T_C \implies S_{\mathrm{gen}} = Q(1/T_C - 1/T_H) > 0$).
- **Unrestrained / free expansion or throttling across a finite pressure drop** ($P_1 > P_2$, e.g., Joule expansion or valve throttling).
- **Mechanical sliding friction or viscous fluid dissipation** (converts ordered work $W$ into disordered internal energy $\Delta U$).
- **Spontaneous mixing of distinct chemical species** at different concentrations or partial pressures ($\Delta S_{\mathrm{mix}} > 0$).
- **Ohmic electrical dissipation** ($Q_{\mathrm{Joule}} = I^2 R_\Omega t$ dissipated inside a resistor at temperature $T \implies S_{\mathrm{gen}} = I^2 R_\Omega t / T > 0$).
- **Spontaneous chemical reactions or phase transitions away from equilibrium** ($\Delta G < 0 \implies S_{\mathrm{gen}} = -\Delta G / T > 0$).

*Exam distinction (`2018 MIT E3 MC1–MC2`):* “Quasistatic” means infinitely slow (internal equilibrium); a process with dry sliding friction can be quasistatic yet **irreversible**! Only a *frictionless* quasistatic process is internally reversible.

## Macroscopic Entropy ($\Delta S = Q_{\mathrm{rev}}/T$), Clausius Inequality & Master $\Delta S$ Atlas

Rudolf Clausius (1865) proved from Carnot's theorem that for *any* closed thermodynamic cycle exchanging heats $Q_k$ with reservoirs at boundary temperatures $T_{b,k}$, the **Clausius Inequality** holds  **[S13,S23,S33]**:

$$
\begin{aligned}

  \boxed{\sum_{\mathrm{cycle}} \frac{Q_k}{T_{b,k}} \le 0} \quad (\text{with } = 0 \text{ iff the cycle is completely reversible})
\end{aligned}
$$

Because the cyclic sum of $Q_{\mathrm{rev}}/T$ vanishes for every reversible cycle, Clausius defined the **state function Entropy $S$** ($J/K$) such that between any two equilibrium states $1$ and $2$:

$$
\begin{aligned}

  \boxed{\Delta S_{\mathrm{sys}} = S_2 - S_1 = \left(\sum \frac{\delta Q_{\mathrm{rev}}}{T}\right)_{\text{along ANY reversible path } 1\to 2}}, \qquad \boxed{\Delta S_{\mathrm{univ}} = \Delta S_{\mathrm{sys}} + \Delta S_{\mathrm{surr}} = S_{\mathrm{gen}} \ge 0}
\end{aligned}
$$

*Golden Rule for Irreversible Processes:* Because $S$ is a **state function**, $\Delta S_{\mathrm{sys}} = S_2 - S_1$ for an *irreversible* process from State $1$ to State $2$ is calculated by inventing a convenient **reversible path** connecting the exact same endpoints $(1, 2)$!

### [FORMULA & DECISION CARD: Master Algebraic $\Delta S$ Formula Atlas (Rule 5.d.iv Zero-Calculus Toolkit)  **[S13,S16,S18]**]

| **Physical Process / System** | **Closed Algebraic $\Delta S$ Formula ($T$ in $K$!)** | **Key Competition Rules & Shortcuts** |
| --- | --- | --- |
| **1. Thermal Reservoir** ($T_{\mathrm{res}} = \mathrm{const}$) | $\displaystyle \Delta S_{\mathrm{res}} = \frac{Q_{\mathrm{res}}}{T_{\mathrm{res}}} = \frac{-Q_{\mathrm{sys}}}{T_{\mathrm{res}}}$ | $Q_{\mathrm{res}} > 0$ if reservoir *absorbs* heat; $<0$ if it *supplies* heat. |
| **2. Isothermal Phase Change** ($T_{\mathrm{tr}}$) | $\displaystyle \Delta S_{\mathrm{phase}} = \frac{\pm m L}{T_{\mathrm{tr}}} = \frac{\pm n\Delta_{\mathrm{tr}}H_m}{T_{\mathrm{tr}}}$ | $+$ for melting/boiling/sublimation; $-$ for freezing/condensing. **Trouton's Rule:** $\Delta_{\mathrm{vap}}S_m^\circ \approx 10.5R \approx 87 J/mol/K$ ($\mathrm{H_2O}$: $108.9 J/mol/K$). |
| **3. Solid or Liquid Warming** (const $c$) | $\displaystyle \Delta S = mc\ln\left(\frac{T_2}{T_1}\right) = nC_m\ln\left(\frac{T_2}{T_1}\right)$ | Derived from geometric-mean steps; valid for any constant-$c$ condensed phase ($T_1, T_2$ in $K$!). |
| **4. Two Identical Blocks Mixing** ($m, c$ at $T_1, T_2 \to T_f = \frac{T_1+T_2}{2}$) | $\displaystyle \Delta S_{\mathrm{univ}} = mc\ln\left(\frac{T_f^2}{T_1 T_2}\right) = 2mc\ln\left(\frac{(T_1+T_2)/2}{\sqrt{T_1 T_2}}\right) > 0$ | By AM–GM inequality, $\frac{T_1+T_2}{2} > \sqrt{T_1 T_2}$ for $T_1 \ne T_2$. If a **reversible Carnot engine** runs between them, $\Delta S_{\mathrm{univ}}=0 \implies \boxed{T_{f,\mathrm{rev}} = \sqrt{T_1 T_2}}$ and $\boxed{W_{\max} = mc(\sqrt{T_1}-\sqrt{T_2})^2}$! |
| **5. Ideal Gas State Change** $(P_1,V_1,T_1)\to(P_2,V_2,T_2)$ | $\displaystyle \begin{aligned}\Delta S &= nC_{V,m}\ln\frac{T_2}{T_1} + nR\ln\frac{V_2}{V_1} \quad [(T,V)]\\ &= nC_{P,m}\ln\frac{T_2}{T_1} - nR\ln\frac{P_2}{P_1} \quad [(T,P)]\\ &= nC_{V,m}\ln\frac{P_2}{P_1} + nC_{P,m}\ln\frac{V_2}{V_1} \quad [(P,V)]\end{aligned}$ | Holds for **BOTH reversible and irreversible** paths between $(1)$ and $(2)$ (e.g., for adiabatic free expansion $T_2=T_1 \implies \Delta S_{\mathrm{gas}} = +nR\ln(V_2/V_1) > 0$ while $\Delta S_{\mathrm{surr}} = 0$). |
| **6. Mixing of $K$ Distinct Ideal Gases** (at constant $T, P$) | $\displaystyle \Delta S_{\mathrm{mix}} = -R\sum_{i=1}^K n_i\ln x_i = -n_{\mathrm{tot}}R\sum_{i=1}^K x_i\ln x_i > 0$ | For $1\,mol\ A + 1\,mol\ B$: $\Delta S_{\mathrm{mix}} = 2R\ln 2 = 11.526 J/K$. **Gibbs Paradox:** If gases $A$ and $B$ are **identical**, $\Delta S_{\mathrm{mix}} = \mathbf{0}$! |
| **7. Steady Conduction Bar** ($T_H \to T_C$) | $\displaystyle \dot{S}_{\mathrm{gen}} = \dot{Q}\left(\frac{1}{T_C} - \frac{1}{T_H}\right) = \dot{Q}\left(\frac{T_H - T_C}{T_H T_C}\right) > 0$ | Bar itself is in steady state ($\Delta S_{\mathrm{bar}} = 0$), while reservoirs gain net entropy $\dot{S}_{\mathrm{gen}} > 0$. |

> **[Vector Figure: Temperature–entropy ($T$–$s$) diagram of water showing the liquid–vapor saturation dome, the $1 atm$ isobar, a superheated isochore (which has steeper slope $(\Delta T/\Delta s)_v = T/c_v > (\Delta T/\Delta s)_P = T/c_p$), and the rectangular area $q_{\mathrm{rev}} = T_{\mathrm{sat}}s_{fg} = h_{fg}$ representing latent heat of vaporization  **[S09,S13,S33]**. | Label: `fig:08:ts-dome`]**
> - **Diagram Annotations & Key Elements:** **X-Axis:** Specific Entropy $s$ ($kJ/kg/K$) • **Y-Axis:** Absolute Temperature $T$ ($K$) • **Shaded Area** $= q_{\mathrm{rev}} = T_b(s_g - s_f) = h_{fg}$ / ($2256.4 kJ/kg$ at $373.15 K$) • Sat. Liquid ($x=0$) • Sat. Vapor ($x=1$) • Isobar $P = 1 atm$ ($T_{\mathrm{sat}}=373.15 K$) • Isochore $v=\mathrm{const}$ (steeper)

### Worked Example — Melting Ice in a Lake vs. Reversible Carnot Engine Between Finite Bodies `[State/National Standard | Tier 2]`

(a) A block of subcooled ice of mass $m = 2.000 kg$ at $T_1 = -20.00 °C$ ($253.15 K$, $c_{\mathrm{ice}} = 2090 J/kg/K, L_f = 334.0 kJ/kg$) is dropped into a large lake at $T_{\mathrm{lake}} = 20.00 °C$ ($293.15 K$, $c_w = 4184 J/kg/K$) and comes to thermal equilibrium with the lake. Calculate $\Delta S_{\mathrm{ice}}$, $\Delta S_{\mathrm{lake}}$, and $\Delta S_{\mathrm{univ}} = S_{\mathrm{gen}}$.
(b) Two identical copper blocks (each of mass $m_{\mathrm{Cu}} = 5.000 kg$ and $c_{\mathrm{Cu}} = 385.0 J/kg/K$) are initially at $T_H = 500.0 K$ and $T_C = 200.0 K$. Compare their final temperature and $\Delta S_{\mathrm{univ}}$ when placed in direct thermal contact versus when a reversible Carnot engine operates between them until they reach a common temperature $T_{f,\mathrm{rev}}$, and compute the maximum work $W_{\max}$ extracted.
**Solution.**
- **(a) Three-stage reversible path for the $2.000 kg$ ice block ($253.15 K\to273.15 K\text{ melt}\to293.15 K$):**
  
$$
Q_{\mathrm{tot}} = m c_{\mathrm{ice}}(20.00) + m L_f + m c_w(20.00) = 83.60 + 668.00 + 167.36 = \mathbf{+918.96 kJ}
$$

  
$$
\Delta S_{\mathrm{ice}} = (2.000)(2090)\ln\left(\frac{273.15}{253.15}\right) + \frac{668000 J}{273.15 K} + (2.000)(4184)\ln\left(\frac{293.15}{273.15}\right) = 317.80 + 2445.54 + 591.36 = \mathbf{+3354.70 J/K}
$$

  
$$
\Delta S_{\mathrm{lake}} = \frac{-Q_{\mathrm{tot}}}{T_{\mathrm{lake}}} = \frac{-918960 J}{293.15 K} = \mathbf{-3134.78 J/K} \implies \Delta S_{\mathrm{univ}} = 3354.70 - 3134.78 = \mathbf{+219.92 J/K} > 0
$$
- **(b) Direct contact vs. reversible Carnot engine between finite blocks ($C = m_{\mathrm{Cu}}c_{\mathrm{Cu}} = 1925.0 J/K$):**
- *Direct contact ($W = 0$):* $T_f = \frac{500.0 + 200.0}{2} = \mathbf{350.0 K}$, and $\Delta S_{\mathrm{univ}} = C\ln\left(\frac{350.0^2}{500.0\times 200.0}\right) = 1925.0\ln(1.2250) = \mathbf{+390.6 J/K}$.
- *Reversible Carnot engine ($\Delta S_{\mathrm{univ}} = 0$):*
    
$$
T_{f,\mathrm{rev}} = \sqrt{T_H T_C} = \sqrt{(500.0)(200.0)} = \mathbf{316.23 K}, \qquad W_{\max} = C(T_H + T_C - 2\sqrt{T_H T_C}) = 1925.0(700.0 - 632.46) = \mathbf{+130.02 kJ}
$$

  

**✓ Verified by:** Note that $W_{\max}$ is NOT equal to $T_{f,\mathrm{rev}}\Delta S_{\mathrm{direct}}$; direct check $Q_H = C(500-316.23)=353.76 kJ$, $Q_C = C(316.23-200)=223.74 kJ$, $Q_H - Q_C = 130.02 kJ$ (`check_sec06_09.py::ex08_1`).

### Worked Example — Two-Compartment Piston Entropy Generation & Gibbs Mixing Paradox `[2018 MIT E3 Q24e | Tier 3]`

(a) In Worked Example `ex:06.7`, an insulated rigid cylinder ($V_{\mathrm{tot}} = 30.00 L$) with a conducting piston held $n_1 = 2.000 mol$ of $\mathrm{He}$ ($C_{V,m,1} = 1.5R, V_{1i} = 10.00 L, T_{1i} = 600.0 K$) and $n_2 = 3.000 mol$ of $\mathrm{N_2}$ ($C_{V,m,2} = 2.5R, V_{2i} = 20.00 L, T_{2i} = 300.0 K$), equilibrating to $T_f = 385.714 K, V_{1f} = 12.00 L, V_{2f} = 18.00 L$. Compute the total entropy generated $\Delta S_{\mathrm{univ}} = \Delta S_1 + \Delta S_2$.
(b) If the piston at $(T_f, P_f)$ is now dissolved so the $2.000 mol$ of $\mathrm{He}$ and $3.000 mol$ of $\mathrm{N_2}$ mix isothermally throughout $V_{\mathrm{tot}} = 30.00 L$, calculate the additional entropy of mixing $\Delta S_{\mathrm{mix}}$. What would $\Delta S_{\mathrm{mix}}$ be if both compartments contained $\mathrm{N_2}$?
**Solution.**
- **(a) Piston equilibration entropy generation using the $(T, V)$ ideal-gas formula:**
  
$$
\Delta S_1 = n_1 C_{V,m,1}\ln\left(\frac{T_f}{T_{1i}}\right) + n_1 R\ln\left(\frac{V_{1f}}{V_{1i}}\right) = R\left[3.000\ln\left(\frac{385.714}{600.0}\right) + 2.000\ln\left(\frac{12.00}{10.00}\right)\right] = R(-1.32550 + 0.36464) = -7.9890 J/K
$$

  
$$
\Delta S_2 = n_2 C_{V,m,2}\ln\left(\frac{T_f}{T_{2i}}\right) + n_2 R\ln\left(\frac{V_{2f}}{V_{2i}}\right) = R\left[7.500\ln\left(\frac{385.714}{300.0}\right) + 3.000\ln\left(\frac{18.00}{20.00}\right)\right] = R(+1.88486 - 0.31608) = +13.0435 J/K
$$

  
$$
\Delta S_{\mathrm{univ}} = \Delta S_1 + \Delta S_2 = -7.9890 + 13.0435 = \mathbf{+5.0545 J/K} > 0
$$
- **(b) Isothermal mixing at $(T_f, P_f)$ with mole fractions $x_{\mathrm{He}} = 2/5 = 0.400$ and $x_{\mathrm{N_2}} = 3/5 = 0.600$:**
  
$$
\Delta S_{\mathrm{mix}} = -R\left(n_1\ln x_{\mathrm{He}} + n_2\ln x_{\mathrm{N_2}}\right) = -(8.314463)\left[2.000\ln(0.400) + 3.000\ln(0.600)\right] = \mathbf{+27.979 J/K}
$$

  If both sides contained $\mathrm{N_2}$ at identical $(T_f, P_f)$, removing the partition produces **zero macroscopic or quantum change** (Gibbs Paradox), so $\Delta S_{\mathrm{mix}} = \mathbf{0.000 J/K}$!

**✓ Verified by:** Volume-expansion check for mixing: $n_1R\ln(30/12) + n_2R\ln(30/18) = R(2\ln 2.5 + 3\ln(5/3)) = 27.979 J/K$ (`check_sec06_09.py::ex08_2`).

## Microscopic Statistical Entropy ($S = k_B\ln\Omega$), Einstein Solids & “Disorder” Traps

Ludwig Boltzmann (1877) and Max Planck (1900) connected macroscopic thermodynamics to statistical mechanics by proving that the entropy $S$ of a macrostate equals $k_B$ times the natural logarithm of its **multiplicity $\Omega$** (the number of distinct microscopic quantum states consistent with the macroscopic constraints $U, V, N$)  **[S13,S15,S18]**:

$$
\begin{aligned}

  \boxed{S = k_B \ln\Omega}, \qquad \Delta S = S_2 - S_1 = k_B\ln\left(\frac{\Omega_2}{\Omega_1}\right), \qquad \frac{\Omega_2}{\Omega_1} = \exp\left(\frac{\Delta S}{k_B}\right) = \exp\left(\frac{N_A\Delta S}{R}\right)
\end{aligned}
$$

### [FORMULA & DECISION CARD: Microstate Multiplicity ($\Omega$) Models  **[S15,S18]**]
- **$N$-Particle Spatial Volume Scaling:** For $N$ independent gas molecules expanding isothermally from $V_1$ to $V_2$:
  
$$
\frac{\Omega_2}{\Omega_1} = \left(\frac{V_2}{V_1}\right)^N \implies \Delta S = N k_B\ln\frac{V_2}{V_1} = nR\ln\frac{V_2}{V_1}
$$
- **Two-State Paramagnet / Coin Lattice ($N$ sites, $k$ “up”):**
  
$$
\begin{aligned}

    \Omega(N, k) = \binom{N}{k} = \frac{N!}{k!\,(N - k)!}, \qquad \Omega_{\mathrm{tot}} = \sum_{k=0}^N \binom{N}{k} = 2^N
\end{aligned}
$$
- **Einstein Solid ($N$ harmonic oscillators sharing $q$ quanta):**
  
$$
\begin{aligned}

    \Omega(N, q) = \binom{q + N - 1}{q} = \frac{(q + N - 1)!}{q!\,(N - 1)!}
\end{aligned}
$$

  
- **Boltzmann Factor & Partition Function $Z_{\mathrm{part}}$:** At thermal equilibrium with a reservoir at temperature $T$, the probability of occupying a single microstate $i$ of energy $E_i$ is $P_i = \frac{e^{-E_i/(k_BT)}}{Z_{\mathrm{part}}}$, so the population ratio of two levels with degeneracies $g_1, g_2$ is:
  
$$
\begin{aligned}

    \frac{N_2}{N_1} = \frac{g_2}{g_1}\exp\left(-\frac{E_2 - E_1}{k_B T}\right)
\end{aligned}
$$

### [TRAP & DIAGNOSTIC: Why “Entropy = Visual Disorder” Fails on Exams!]

Entropy is strictly a measure of **energy and spatial microstate multiplicity $\Omega$**, NOT human visual “messiness”  **[S18,S35]**:
- **Spontaneous Freezing of Supercooled Water at $-5 °C$:** Visually, liquid water freezes into an ordered hexagonal ice crystal ($\Delta S_{\mathrm{sys}} < 0$), yet the process is $100\%$ spontaneous because the latent heat released into the surroundings increases the surroundings' vibrational multiplicity by $\Delta S_{\mathrm{surr}} > |\Delta S_{\mathrm{sys}}| \implies \Delta S_{\mathrm{univ}} > 0$!
- **Hard-Sphere Colloidal Crystallization & Oil/Water Separation:** At high packing fraction ($\phi > 0.494$), hard spheres with *zero* potential energy spontaneously crystallize into an ordered FCC lattice because locking particles onto lattice sites gives each sphere more local “rattle” free volume than a jammed random fluid ($\Omega_{\mathrm{FCC}} > \Omega_{\mathrm{jammed}}$)!

### Worked Example — Einstein Solid & Spin Lattice $S$ `[Tier 2]`

Find the multiplicity $\Omega$ and entropy $S/k_B$ of (a) an Einstein solid of $N = 4$ oscillators sharing $q = 6$ energy quanta, and (b) the macrostate of $N = 100$ spin-$1/2$ dipoles with $k = 50$ spins up.
**Solution.**
(a) From Eq. (`eq:08:einstein-solid`): $\Omega(4,6) = \binom{6+4-1}{6} = \binom{9}{6} = \frac{9\times 8\times 7}{3\times 2\times 1} = \mathbf{84} \implies S/k_B = \ln(84) = \mathbf{4.4308}$ ($S = 6.117×10^{-23} J/K$).
(b) From Eq. (`eq:08:two-state-omega`): $\Omega(100,50) = \frac{100!}{(50!)^2} = \mathbf{1.0089\times 10^{29}} \implies S/k_B = \ln\Omega = \mathbf{66.7839}$ (vs. $\ln(2^{100}) = 69.3147$ for all microstates).

**✓ Verified by:** Exact factorial evaluation in Python `math.comb(9,6)=84`, `math.comb(100,50)=1.0089e29` (`check_sec06_09.py::ex08_3`).

## Enthalpy ($H = U + PV$), Hess's Law, Kirchhoff's Correction & Steam Table Construction

Defining **Enthalpy** as the state function $H \equiv U + PV$ ($\Delta H = \Delta U + \Delta(PV)$) simplifies any constant-pressure process with only $PV$ expansion work ($W_{\mathrm{by}} = P\Delta V$): by the First Law, $\Delta H = \Delta U + P\Delta V = (Q_P - P\Delta V) + P\Delta V = \mathbf{Q_P}$  **[S16]**.

### [FORMULA & DECISION CARD: Hess's Law, Kirchhoff's Temperature Shift & Saturation Steam-Table Construction  **[S09,S10,S16,S25]**]
- **Hess's Law of Constant Heat Summation ($\Delta_r H^\circ, \Delta_r S^\circ, \Delta_r G^\circ$ at $P^\circ = 1 bar, T = 298.15 K$):**
  For any balanced reaction $\sum \nu_r \mathrm{R} \to \sum \nu_p \mathrm{P}$:
  
$$
\begin{aligned}

    \boxed{\Delta_r H^\circ = \sum_p \nu_p \Delta_f H^\circ(\mathrm{products}) - \sum_r \nu_r \Delta_f H^\circ(\mathrm{reactants})}, \qquad \boxed{\Delta_r S^\circ = \sum_p \nu_p S^\circ(\mathrm{products}) - \sum_r \nu_r S^\circ(\mathrm{reactants})}
\end{aligned}
$$

  
- *Zero vs. Non-Zero Reference Trap:* By convention, $\Delta_f H^\circ = 0$ and $\Delta_f G^\circ = 0$ for pure elements in their most stable reference state at $1 bar, 298.15 K$ (e.g., $\mathrm{O_2}(g), \mathrm{N_2}(g), \mathrm{H_2}(g), \mathrm{C(graphite)}, \mathrm{Fe}(s), \mathrm{Br_2}(l)$), **BUT their absolute standard entropies $S^\circ(298.15 K)$ are NEVER zero** ($S^\circ > 0$ by the Third Law)!
- *Bond Dissociation Estimate (Gas Phase Only — Opposite Order!):* $\Delta_r H_{\mathrm{gas}} \approx \sum D(\text{bonds **broken**}) - \sum D(\text{bonds **formed**})$.
- **Kirchhoff's Law of Thermochemistry (Temperature Correction from $T_0$ to $T$, `2019 MIT E2 P3e TB #3`):**
  With $\Delta_r C_P^\circ = \sum \nu_p C_{P,m}^\circ(\mathrm{prod}) - \sum \nu_r C_{P,m}^\circ(\mathrm{react})$ constant over $[T_0, T]$:
  
$$
\begin{aligned}

    \boxed{\Delta_r H^\circ(T) = \Delta_r H^\circ(T_0) + \Delta_r C_P^\circ (T - T_0)}, \qquad \boxed{\Delta_r S^\circ(T) = \Delta_r S^\circ(T_0) + \Delta_r C_P^\circ \ln\left(\frac{T}{T_0}\right)}
\end{aligned}
$$

  
- **Saturation Steam-Table Construction Identities (`2027 Cornell E1 Q28 TB #1`, Reference State $u_f = s_f = 0$ at $T_{\mathrm{tp}} = 273.16 K$):**
  
$$
\begin{aligned}

    h_f = u_f + P_{\mathrm{sat}}v_f \approx c_{p,f}(T - T_{\mathrm{tp}}), \quad h_g = h_f + h_{fg}, \quad \boxed{u_g = h_g - P_{\mathrm{sat}}v_g}, \quad \boxed{s_f = c_{p,f}\ln\left(\frac{T}{273.16 K}\right)}, \quad \boxed{s_g = s_f + \frac{h_{fg}}{T}}
\end{aligned}
$$

  
  *(Unit warning: when $P_{\mathrm{sat}}$ is in $kPa$ and $v_g$ is in $m^3/kg$, their product $P_{\mathrm{sat}}v_g$ is already in $\mathbf{kJ/kg}$!)*

**Table:** NIST Standard Thermochemical Reference Values at $T = 298.15 K$ ($25.0 °C$) and $P^\circ = 1.000 bar$ ($100 kPa$)  **[S09,S10]**.

| **Species** | **Phase** | $\Delta_f H^\circ$ | $S^\circ$ | $\Delta_f G^\circ$ | **Species** | **Phase** | $\Delta_f H^\circ$ | $S^\circ$ | $\Delta_f G^\circ$ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | ($kJ/mol$) | ($J/mol/K$) | ($kJ/mol$) |  |  | ($kJ/mol$) | ($J/mol/K$) | ($kJ/mol$) |
| $\mathrm{H_2O}$ | liquid ($l$) | $-285.83$ | $69.95$ | $-237.14$ | $\mathrm{CH_4}$ | gas ($g$) | $-74.87$ | $186.25$ | $-50.74$ |
| $\mathrm{H_2O}$ | gas ($g$) | $-241.83$ | $188.84$ | $-228.59$ | $\mathrm{C_2H_5OH}$ | liquid ($l$) | $-277.69$ | $159.86$ | $-174.78$ |
| $\mathrm{CO_2}$ | gas ($g$) | $-393.51$ | $213.79$ | $-394.39$ | $\mathrm{NH_3}$ | gas ($g$) | $-45.94$ | $192.77$ | $-16.41$ |
| $\mathrm{CO}$ | gas ($g$) | $-110.53$ | $197.66$ | $-137.17$ | $\mathrm{NO}$ | gas ($g$) | $+90.29$ | $210.76$ | $+86.58$ |
| $\mathrm{H_2}$ | gas ($g$) | $0.00$ | $130.68$ | $0.00$ | $\mathrm{NO_2}$ | gas ($g$) | $+33.10$ | $240.04$ | $+51.23$ |
| $\mathrm{O_2}$ | gas ($g$) | $0.00$ | $205.15$ | $0.00$ | $\mathrm{SO_2}$ | gas ($g$) | $-296.81$ | $248.22$ | $-300.13$ |
| $\mathrm{N_2}$ | gas ($g$) | $0.00$ | $191.61$ | $0.00$ | $\mathrm{HCl}$ | gas ($g$) | $-92.31$ | $186.90$ | $-95.30$ |
| $\mathrm{Cu}$ | solid ($s$) | $0.00$ | $33.15$ | $0.00$ | $\mathrm{Al_2O_3}$ | solid ($s$) | $-1675.70$ | $50.92$ | $-1582.30$ |
| $\mathrm{Al}$ | solid ($s$) | $0.00$ | $28.30$ | $0.00$ | $\mathrm{NaCl}$ | solid ($s$) | $-411.12$ | $72.11$ | $-384.04$ |

### Worked Example — Steam-Table Construction (`Cornell 2027 TB #1`) & Kirchhoff Sweat Cooling (`MIT 2019 TB #3`) `[2027 Cornell E1 Q28 & 2019 MIT E2 P3e | Tier 3]`

(a) In `2027 Cornell E1 Q28` (`TB #1`), experimental measurements on saturated water at $T = 120.0 °C$ ($393.15 K$) yield $P_{\mathrm{sat}} = 198.67 kPa$, $v_f = 0.001060 m^3/kg$, $v_g = 0.8919 m^3/kg$, and $h_{fg} = 2202.6 kJ/kg$ (using mean liquid specific heat $c_w = 4.217 kJ/kg/K$ above $T_{\mathrm{tp}} = 273.16 K$ where $u_f = s_f = 0$). Compute $h_f$, $u_f$, $h_g$, $u_g$, $s_f$, and $s_g$ at $120.0 °C$.
(b) In `2019 MIT E2 P3e` (`TB #3`), human sweat evaporates at body temperature $T_{\mathrm{body}} = 37.00 °C$ ($310.15 K$). Given $\Delta_{\mathrm{vap}}H_m^\circ(373.15 K) = 40.65 kJ/mol$, $C_{P,m}(\mathrm{H_2O},l) = 75.33 J/mol/K$, and $C_{P,m}(\mathrm{H_2O},g) = 33.58 J/mol/K$, apply Kirchhoff's law Eq. (`eq:08:kirchhoff`) to find $\Delta_{\mathrm{vap}}H_m^\circ(310.15 K)$ and the mass of sweat ($M = 18.0153 g/mol$) required to remove $5000.0 kJ$ of metabolic heat.
**Solution.**
- **(a) Constructing the $120.0 °C$ saturation steam table row from Eq. (`eq:08:steam-table-build`):**
  
$$
h_f = c_w(393.15 - 273.16) = (4.217)(119.99) = \mathbf{506.00 kJ/kg}, \qquad u_f = h_f - P_{\mathrm{sat}}v_f = 506.00 - (198.67)(0.001060) = \mathbf{505.79 kJ/kg}
$$

  
$$
h_g = h_f + h_{fg} = 506.00 + 2202.6 = \mathbf{2708.60 kJ/kg}, \quad u_g = h_g - P_{\mathrm{sat}}v_g = 2708.60 - 177.19 = \mathbf{2531.41 kJ/kg}
$$

  
$$
s_f = c_w\ln\left(\frac{393.15}{273.16}\right) = \mathbf{1.5355 kJ/kg/K}, \quad s_g = s_f + \frac{h_{fg}}{T} = 1.5355 + \frac{2202.6}{393.15} = \mathbf{7.1379 kJ/kg/K}
$$
- **(b) Kirchhoff temperature correction of $\Delta_{\mathrm{vap}}H_m^\circ$ from $T_0 = 373.15 K$ to $T = 310.15 K$:**
  For $\mathrm{H_2O}(l) \to \mathrm{H_2O}(g)$, $\Delta_{\mathrm{vap}}C_P^\circ = C_{P,m}(g) - C_{P,m}(l) = 33.58 - 75.33 = -41.75 J/mol/K = -0.04175 kJ/mol/K$:
  
$$
\Delta_{\mathrm{vap}}H_m^\circ(310.15 K) = 40.65 + (-0.04175)(310.15 - 373.15) = 40.65 + 2.630 = \mathbf{43.280 kJ/mol} \quad (L_v = 2402.4 kJ/kg)
$$

  
$$
m_{\mathrm{sweat}} = \frac{Q_{\mathrm{remove}}}{L_v(37 °C)} = \frac{5000.0 kJ}{2402.4 kJ/kg} = \mathbf{2.0813 kg}
$$

**✓ Verified by:** Table 3.1 NIST IAPWS-95 exact value at $37.0 °C$ is $L_v = 2413.1 kJ/kg$ ($0.44\%$ agreement with linear Kirchhoff!) (`check_sec06_09.py::ex08_4`).

## Thermodynamic Potentials ($U, H, F, G$), 4-Quadrant Spontaneity & Van't Hoff Equilibrium

For a system in thermal and mechanical contact with an environment at constant temperature $T$ and pressure $P$, the surroundings' entropy change is $\Delta S_{\mathrm{surr}} = -\Delta H_{\mathrm{sys}}/T$. Multiplying the Second Law $\Delta S_{\mathrm{univ}} = \Delta S_{\mathrm{sys}} - \Delta H_{\mathrm{sys}}/T \ge 0$ by $-T$ defines the **Gibbs Free Energy $G \equiv H - TS$**  **[S15,S16]**:

$$
\begin{aligned}

  \boxed{\Delta G_{\mathrm{sys}} = \Delta H_{\mathrm{sys}} - T\Delta S_{\mathrm{sys}} = -T\Delta S_{\mathrm{univ}} \le 0} \quad (\text{at constant } T, P), \qquad \boxed{T^* = T_{\mathrm{eq}} = \frac{\Delta H}{\Delta S}} \quad (\text{where } \Delta G = 0)
\end{aligned}
$$

### [FORMULA & DECISION CARD: The 4 Thermodynamic Potentials, Maximum Work Bounds & Van't Hoff Equation  **[S15,S16,S18]**]

| **Potential Name** | **Definition** | **Natural Vars.** | **Maxwell Relation** | **Equilibrium & Maximum Work Meaning (`2019 MIT E2 MC10–11`)** |
| --- | --- | --- | --- | --- |
| **Internal Energy ($U$)** | $U$ | $(S, V)$ | $(\partial T/\partial V)_S = -(\partial P/\partial S)_V$ | Minimized at constant $(S, V)$; $\Delta U = Q_V$ in rigid bomb. |
| **Enthalpy ($H$)** | $U + PV$ | $(S, P)$ | $(\partial T/\partial P)_S = (\partial V/\partial S)_P$ | Minimized at constant $(S, P)$; $\Delta H = Q_P$ in open vessel. |
| **Helmholtz ($F$ or $A$)** | $U - TS$ | $(T, V)$ | $(\partial S/\partial V)_T = (\partial P/\partial T)_V$ | Minimized at constant $(T, V)$; $\mathbf{W_{\mathrm{tot,max,by}} = -\Delta F}$ (total isothermal work). |
| **Gibbs ($G$)** | $H - TS$ | $(T, P)$ | $-(\partial S/\partial P)_T = (\partial V/\partial T)_P$ | Minimized at constant $(T, P)$; $\mathbf{W_{\mathrm{non\text{-}PV,max,by}} = -\Delta G}$ (electrical/fuel-cell work). |

**Chemical Equilibrium Constant $K_{\mathrm{eq}}$ and Algebraic Two-Point Van't Hoff Equation:**

$$
\begin{aligned}

  \Delta_r G = \Delta_r G^\circ + RT\ln Q_r, \qquad \boxed{\Delta_r G^\circ = -RT\ln K_{\mathrm{eq}} \iff K_{\mathrm{eq}} = \exp\left(-\frac{\Delta_r G^\circ}{RT}\right)}, \qquad \boxed{\ln\left(\frac{K_2}{K_1}\right) = -\frac{\Delta_r H^\circ}{R}\left(\frac{1}{T_2} - \frac{1}{T_1}\right)}
\end{aligned}
$$

> **[Vector Figure: (a) Four-quadrant spontaneity plot of $\Delta G(T) = \Delta H - T\Delta S$ showing temperature-independent regimes (I and II) and crossover temperature $T^* = \Delta H/\Delta S$ for enthalpy-driven (III) vs. entropy-driven (IV) reactions. (b) Van't Hoff plot of $\ln K_{\mathrm{eq}}$ vs. $1/T$ with slope $-\Delta_r H^\circ/R$ and intercept $\Delta_r S^\circ/R$  **[S16]**. | Label: `fig:08:gibbs-spontaneity`]**
> - **Diagram Annotations & Key Elements:** **Title:** **(a) Four-Quadrant $\Delta G(T) = \Delta H - T\Delta S$ Lines** • **Title:** **(b) Linearized Van't Hoff Plot ($\ln K_{\mathrm{eq}}$ vs. $1/T$)** • **X-Axis:** Absolute Temperature $T$ ($K$) • **X-Axis:** Reciprocal Temperature $1000/T$ ($/K$) • **Y-Axis:** Gibbs Free Energy $\Delta G(T)$ ($kJ/mol$) • **Y-Axis:** $\ln K_{\mathrm{eq}} = -\dfrac{\Delta_r H^\circ}{R}\left(\dfrac{1}{T}\right) + \dfrac{\Delta_r S^\circ}{R}$ • **I:** $\Delta H<0, \Delta S>0$ (Always spont.) • **II:** $\Delta H>0, \Delta S<0$ (Never spont.) • **III:** $\Delta H<0, \Delta S<0$ ($T < T^*$) • **IV:** $\Delta H>0, \Delta S>0$ ($T > T^*$) • **Exothermic ($\Delta_r H^\circ < 0$)** / Slope $= -\Delta_r H^\circ/R > 0$ / ($K_{\mathrm{eq}}$ drops at high $T$) • **Endothermic ($\Delta_r H^\circ > 0$)** / Slope $= -\Delta_r H^\circ/R < 0$ / ($K_{\mathrm{eq}}$ rises at high $T$)

### Worked Example — Water-Gas Shift Hess's Law, Crossover Temperature $T^*$ & Van't Hoff $K_{\mathrm{eq}}$ `[State/National Standard | Tier 3]`

Using the NIST data in Table `tab:08:thermochem`, analyze the industrial water-gas shift reaction $\mathrm{CO}(g) + \mathrm{H_2O}(g) \rightleftharpoons \mathrm{CO_2}(g) + \mathrm{H_2}(g)$: (a) Calculate $\Delta_r H^\circ$, $\Delta_r S^\circ$, and $\Delta_r G^\circ$ at $T_1 = 298.15 K$. (b) Find the equilibrium constant $K_{\mathrm{eq}}(298.15 K)$ and the crossover temperature $T^*$ above which $\Delta_r G^\circ > 0$ ($K_{\mathrm{eq}} < 1$). (c) Assuming $\Delta_r H^\circ$ and $\Delta_r S^\circ$ are approximately constant, use the Van't Hoff equation Eq. (`eq:08:vant-hoff`) to compute $K_{\mathrm{eq}}$ at $T_2 = 800.0 K$.
**Solution.**
- **(a) Hess's Law at $298.15 K$ from Table `tab:08:thermochem`:**
  
$$
\Delta_r H^\circ = \left[-393.51 + 0.00\right] - \left[-110.53 + (-241.83)\right] = -393.51 - (-352.36) = \mathbf{-41.15 kJ/mol} \quad (\text{exothermic})
$$

  
$$
\Delta_r S^\circ = \left[213.79 + 130.68\right] - \left[197.66 + 188.84\right] = 344.47 - 386.50 = \mathbf{-42.03 J/mol/K} \quad (\text{Quad.\ III: } \Delta H < 0, \Delta S < 0)
$$

  
$$
\Delta_r G^\circ(298.15 K) = \Delta_r H^\circ - T_1\Delta_r S^\circ = -41.15 - (298.15)(-0.04203) = -41.15 + 12.53 = \mathbf{-28.62 kJ/mol} < 0
$$
- **(b) Equilibrium constant $K_{\mathrm{eq}}(298.15 K)$ and crossover temperature $T^*$:**
  
$$
K_{\mathrm{eq}}(298.15 K) = \exp\left(\frac{-\Delta_r G^\circ}{RT_1}\right) = \exp\left(\frac{+28619}{(8.314463)(298.15)}\right) = e^{11.5448} = \mathbf{1.032\times 10^5}, \quad T^* = \frac{\Delta_r H^\circ}{\Delta_r S^\circ} = \frac{-41150 J/mol}{-42.03 J/mol/K} = \mathbf{979.06 K}
$$
- **(c) Van't Hoff equilibrium constant at $T_2 = 800.0 K$:**
  
$$
\ln K_{\mathrm{eq}}(800.0 K) = \ln K_{\mathrm{eq}}(T_1) - \frac{\Delta_r H^\circ}{R}\left(\frac{1}{T_2} - \frac{1}{T_1}\right) = 11.5447 - \frac{-41150}{8.314463}\left(\frac{1}{800.0} - \frac{1}{298.15}\right) = 11.5447 - 10.4132 = \mathbf{1.1315}
$$

  
$$
\implies K_{\mathrm{eq}}(800.0 K) = e^{1.1315} = \mathbf{3.100}
$$

**✓ Verified by:** Direct check $\Delta_r G^\circ(800 K) = -41150 - 800(-42.03) = -7526 J/mol \implies e^{7526/(8.314463\times 800)} = 3.100$ (`check_sec06_09.py::ex08_5`).

### Worked Example — Coupled Biochemical ATP Spontaneity (`MIT 2019`) & Fuel-Cell Maximum Electrical Work `[2019 MIT E2 P3b & MC10–11 | Tier 2]`

(a) In cellular metabolism at $T = 310.15 K$ ($37.0 °C$), the synthesis of Acetyl-CoA from acetate and CoA-SH is endergonic with $\Delta G_1 = +31.50 kJ/mol > 0$. Compare coupling this reaction to: (i) ATP hydrolysis to $\mathrm{ADP} + \mathrm{P_i}$ ($\Delta G_2 = -30.50 kJ/mol$), versus (ii) ATP pyrophosphate cleavage to $\mathrm{AMP} + \mathrm{PP_i}$ ($\Delta G_3 = -45.90 kJ/mol$). Determine which pathway drives Acetyl-CoA synthesis spontaneously and compute the equilibrium ratio $K_{\mathrm{coupled},2}/K_{\mathrm{coupled},1}$.
(b) A hydrogen–oxygen PEM fuel cell ($\mathrm{H_2}(g) + \frac{1}{2}\mathrm{O_2}(g) \to \mathrm{H_2O}(l)$) operates isothermally and isobarically at $T = 298.15 K$ and $P = 1.000 bar$. Using Table `tab:08:thermochem`, compute $\Delta_r H^\circ$, $\Delta_r S^\circ$, $\Delta_r G^\circ$, the maximum electrical work $W_{\mathrm{elec,\max}}$ per mole of $\mathrm{H_2}$, the reversible cell voltage $E_{\mathrm{cell}}^\circ = -\Delta_r G^\circ / (n_e F)$ ($n_e = 2$ electrons per $\mathrm{H_2}$, Faraday constant $F = 96485.33 C/mol$), and the reversible heat $Q_{\mathrm{rev}} = T\Delta_r S^\circ$ rejected by the cell.
**Solution.**
- **(a) Coupled reaction Gibbs additivity (`2019 MIT E2 P3b`):**
- *Pathway (i) ($\mathrm{ATP}\to\mathrm{ADP}+\mathrm{P_i}$):* $\Delta G_{\mathrm{net,i}} = \Delta G_1 + \Delta G_2 = +31.50 - 30.50 = \mathbf{+1.00 kJ/mol} > 0$ (**non-spontaneous!**).
- *Pathway (ii) ($\mathrm{ATP}\to\mathrm{AMP}+\mathrm{PP_i}$):* $\Delta G_{\mathrm{net,ii}} = \Delta G_1 + \Delta G_3 = +31.50 - 45.90 = \mathbf{-14.40 kJ/mol} < 0$ (**spontaneous!**).
- *Equilibrium constant enhancement at $310.15 K$:*
    
$$
\frac{K_{\mathrm{coupled,ii}}}{K_{\mathrm{coupled,i}}} = \exp\left(\frac{-(\Delta G_{\mathrm{net,ii}} - \Delta G_{\mathrm{net,i}})}{RT}\right) = \exp\left(\frac{+15400}{(8.314463)(310.15)}\right) = e^{5.9720} = \mathbf{392.3}
$$
- **(b) $\mathrm{H_2/O_2}$ fuel-cell thermodynamics from Table `tab:08:thermochem`:**
  
$$
\Delta_r H^\circ = \Delta_f H^\circ(\mathrm{H_2O},l) = \mathbf{-285.83 kJ/mol}, \qquad \Delta_r S^\circ = 69.95 - \left[130.68 + \frac{1}{2}(205.15)\right] = \mathbf{-163.305 J/mol/K}
$$

  
$$
\Delta_r G^\circ = \Delta_r H^\circ - T\Delta_r S^\circ = -285.83 - (298.15)(-0.163305) = -285.83 + 48.69 = \mathbf{-237.14 kJ/mol}
$$

  
$$
W_{\mathrm{elec,\max}} = -\Delta_r G^\circ = \mathbf{237.14 kJ/mol}, \quad E_{\mathrm{cell}}^\circ = \frac{-\Delta_r G^\circ}{2F} = \frac{237140 J/mol}{2(96485.33 C/mol)} = \mathbf{1.2289 V}, \quad Q_{\mathrm{rev}} = T\Delta_r S^\circ = \mathbf{-48.69 kJ/mol}
$$

  Even an ideal $100\%$-reversible fuel cell must reject $48.69 kJ/mol$ of heat to the surroundings because $1.5\,mol$ of gas condenses into $1\,mol$ of liquid water ($\Delta_r S^\circ < 0$)!

**✓ Verified by:** First-Law check on fuel cell: $\Delta_r H^\circ = Q_{\mathrm{rev}} - W_{\mathrm{elec,\max}} = -48.69 - 237.14 = -285.83 kJ/mol$ (`check_sec06_09.py::ex08_8`).

## Exergy (Availability), Gouy–Stodola Destruction ($X_{\mathrm{dest}} = T_0 S_{\mathrm{gen}}$) & Second-Law Efficiency

In `2027 Cornell E1 Q29b–e` (`TB #8`), competitors were required to compute **exergy supplied**, **Gouy–Stodola exergy destruction**, and **Second-Law efficiency $\eta_{\mathrm{II}}$**  **[S25]**. Relative to a surrounding “dead-state” environment at temperature $T_0$ (typically $298.15 K$ or $300.0 K$) and pressure $P_0$, **Exergy $X$** is the *maximum useful work* obtainable as a system or heat stream is brought reversibly to equilibrium with $(T_0, P_0)$  **[S33]**:

### [FORMULA & DECISION CARD: Exergy Ledger, Gouy–Stodola Theorem & Second-Law Efficiency ($\eta_{\mathrm{II}}$)  **[S25,S33]**]
- **Exergy of a Heat Transfer $Q_{\mathrm{in}}$ from a Source at Temperature $T_{\mathrm{source}}$:**
  
$$
\begin{aligned}

    \boxed{X_{Q,\mathrm{in}} = W_{\mathrm{rev,max}} = Q_{\mathrm{in}}\left(1 - \frac{T_0}{T_{\mathrm{source}}}\right)}, \qquad x_{q,\mathrm{in}} = q_{\mathrm{in}}\left(1 - \frac{T_0}{T_{\mathrm{source}}}\right)
\end{aligned}
$$

  
- **Gouy–Stodola Exergy Destruction Theorem (Lost Work $W_{\mathrm{lost}} = X_{\mathrm{dest}}$):**
  Every real irreversible process generates entropy $S_{\mathrm{gen}} = \Delta S_{\mathrm{univ}} > 0$ and permanently destroys exergy equal to:
  
$$
\begin{aligned}

    \boxed{X_{\mathrm{dest}} = W_{\mathrm{lost}} = W_{\mathrm{rev,max}} - W_{\mathrm{actual}} = T_0 S_{\mathrm{gen}} \ge 0}, \qquad \boxed{x_{\mathrm{dest}} = T_0 s_{\mathrm{gen}}}
\end{aligned}
$$

  
- *Boiler / Heat Exchanger receiving $q_{\mathrm{in}}$ from source at $T_{\mathrm{source}}$:* $s_{\mathrm{gen,boiler}} = (s_{\mathrm{out}} - s_{\mathrm{in}}) - \dfrac{q_{\mathrm{in}}}{T_{\mathrm{source}}} \ge 0$.
- *Adiabatic Turbine or Compressor ($q = 0$):* $s_{\mathrm{gen,turb}} = s_{\mathrm{out},a} - s_{\mathrm{in}} \ge 0 \implies x_{\mathrm{dest,turb}} = T_0(s_{\mathrm{out},a} - s_{\mathrm{in}})$.
- **Second-Law Efficiency ($\eta_{\mathrm{II}}$ or $\eta_2$):** Measures how closely a real device approaches the reversible Second-Law limit ($\eta_{\mathrm{II}} \in [0, 1]$):
  
$$
\begin{aligned}

    \boxed{\eta_{\mathrm{II,engine}} = \frac{W_{\mathrm{net,actual}}}{X_{Q,\mathrm{in}}} = \frac{\eta_{\mathrm{I}}}{\eta_{\mathrm{Carnot}}} = 1 - \frac{X_{\mathrm{dest,cycle}}}{X_{Q,\mathrm{in}}}}, \qquad \boxed{\eta_{\mathrm{II,refrig}} = \frac{\mathrm{COP}_{R,\mathrm{actual}}}{\mathrm{COP}_{R,\mathrm{Carnot}}}}, \qquad \boxed{\eta_{\mathrm{II,HP}} = \frac{\mathrm{COP}_{\mathrm{HP,actual}}}{\mathrm{COP}_{\mathrm{HP,Carnot}}}}
\end{aligned}
$$

  

### Worked Example — Gouy–Stodola Exergy Destruction & Second-Law Efficiency of a Steam Plant `[2027 Cornell E1 Q29b–e (TB #8) | Tier 3]`

In `2027 Cornell E1 Q29`, a Rankine steam cycle operates in an environment at dead-state temperature $T_0 = 300.0 K$. In the boiler, water enters at State 4 ($h_4 = 461.42 kJ/kg, s_4 = 1.4188 kJ/kg/K$) and exits as dry saturated steam at State 1 ($T_1 = 130.0 °C = 403.15 K, h_1 = 2718.6 kJ/kg, s_1 = 6.9931 kJ/kg/K$) by absorbing heat $q_{\mathrm{in}} = h_1 - h_4 = 2257.2 kJ/kg$ from a furnace reservoir at $T_{\mathrm{source}} = 600.0 K$. Ideal isentropic expansion in the turbine to the $110.0 °C$ ($383.15 K$) condenser produces work $w_{t,s} = 109.92 kJ/kg$ (neglecting tiny pump work, so $\eta_{\mathrm{I,ideal}} = w_{t,s}/q_{\mathrm{in}} = 4.870\%$). (a) Calculate the specific exergy supplied by the furnace $x_{\mathrm{in}}$, the boiler entropy generation $s_{\mathrm{gen,boiler}}$, the exergy destroyed in the boiler $x_{\mathrm{dest,boiler}}$, and the cycle's Second-Law efficiency $\eta_{\mathrm{II}}$. (b) If the real adiabatic turbine has isentropic efficiency $\eta_s = 0.8000$, find the actual turbine work $w_{t,a}$, the turbine entropy generation $s_{\mathrm{gen,turb}}$, and the turbine exergy destruction $x_{\mathrm{dest,turb}}$.
**Solution.**
- **(a) Furnace exergy input, boiler exergy destruction, and Second-Law efficiency from Eq. (`eq:08:exergy-heat`)–Eq. (`eq:08:eta-ii`):**
  
$$
x_{\mathrm{in}} = q_{\mathrm{in}}\left(1 - \frac{T_0}{T_{\mathrm{source}}}\right) = (2257.2 kJ/kg)\left(1 - \frac{300.0}{600.0}\right) = \mathbf{1128.6 kJ/kg}
$$

  
$$
s_{\mathrm{gen,boiler}} = (s_1 - s_4) - \frac{q_{\mathrm{in}}}{T_{\mathrm{source}}} = (6.9931 - 1.4188) - \frac{2257.2}{600.0} = 5.5743 - 3.7620 = \mathbf{1.8123 kJ/kg/K}
$$

  
$$
x_{\mathrm{dest,boiler}} = T_0 s_{\mathrm{gen,boiler}} = (300.0 K)(1.8123 kJ/kg/K) = \mathbf{543.69 kJ/kg} \quad (48.2\%\text{ of } x_{\mathrm{in}}\text{ destroyed by finite }\Delta T\text{ in boiler!})
$$

  
$$
\eta_{\mathrm{II}} = \frac{w_{t,s}}{x_{\mathrm{in}}} = \frac{109.92}{1128.6} = \frac{\eta_{\mathrm{I}}}{1 - T_0/T_{\mathrm{source}}} = \frac{4.870\%}{0.5000} = \mathbf{9.740\%}
$$
- **(b) Real turbine ($\eta_s = 0.8000$) entropy generation and Gouy–Stodola exergy destruction:**
  
$$
w_{t,a} = \eta_s w_{t,s} = 0.8000(109.92) = \mathbf{87.936 kJ/kg}
$$

  The lost work inside the turbine is dissipated into the condensing steam at $T_{\mathrm{cond}} = 110.0 °C = 383.15 K$ ($\Delta h_{2a-2s} = w_{t,s} - w_{t,a} = 21.984 kJ/kg$ inside the two-phase dome at constant $T_{\mathrm{cond}}$):
  
$$
s_{\mathrm{gen,turb}} = s_{2a} - s_1 = s_{2a} - s_{2s} = \frac{h_{2a} - h_{2s}}{T_{\mathrm{cond}}} = \frac{21.984 kJ/kg}{383.15 K} = \mathbf{0.05738 kJ/kg/K}
$$

  
$$
x_{\mathrm{dest,turb}} = T_0 s_{\mathrm{gen,turb}} = (300.0 K)(0.05738) = \mathbf{17.213 kJ/kg}
$$

**✓ Verified by:** Note $x_{\mathrm{dest,turb}} = (T_0/T_{\mathrm{cond}})(w_{t,s}-w_{t,a}) = (300/383.15)(21.984) = 17.213 kJ/kg$ (`check_sec06_09.py::ex08_6`).

## The Third Law of Thermodynamics, Quantum $C_V \to 0$ Freeze-Out & Residual Entropy

### [FORMULA & DECISION CARD: Three Equivalent Formulations of the Third Law & Residual Entropy ($T \to 0 K$)  **[S11,S15,S25]**]
- **Nernst–Simon Heat Theorem (1906):** For any isothermal reversible process between internal equilibrium states of condensed phases, $\lim_{T\to0 K} \Delta S = 0$.
- **Planck Absolute-Zero Entropy Statement (1911):** The entropy of any pure, perfectly crystalline substance with a unique non-degenerate ground state ($\Omega_0 = 1$) vanishes identically at absolute zero:
  
$$
\begin{aligned}

    \boxed{\lim_{T\to0 K} S_{\text{perfect crystal}} = k_B\ln(1) = 0}
\end{aligned}
$$

  
- **Nernst Unattainability Principle (1912):** It is impossible to cool any system to $T = 0 K$ in a finite number of cyclic or adiabatic steps.
- **Why Heat Capacity MUST Vanish as $T \to 0 K$ (`2027 Cornell E1 Q35c–d`):**
  Integrating $C_V/T$ from $0 K$ to $T$ gives absolute entropy $S(T) = S_0 + \sum \frac{C_V\,\Delta T'}{T'}$. If $C_V$ remained positive at $0 K$ (as classical Dulong–Petit $C_{V,m} = 3R$ predicts), $S(T)$ would diverge as $\ln T \to -\infty$! Quantum phonon freeze-out ($\hbar\omega \gg k_B T$) forces $C_{V,\mathrm{Debye}} \propto T^3 \to 0$ (and electronic $C_{V,\mathrm{elec}} \propto T \to 0$), keeping $S(0 K) = 0$ finite.
- **Residual Entropy of Frustrated / Disordered Crystals ($S_{0,m} = R\ln w > 0$):**
  When a crystal freezes into $w > 1$ nearly degenerate orientations per molecule across $N = n N_A$ sites ($\Omega_0 = w^N$):
  
$$
\begin{aligned}

    \boxed{S_0 = k_B\ln(w^N) = N k_B\ln w = n R\ln w}, \qquad S_{0,m} = R\ln w = \begin{cases} R\ln 2 = \mathbf{5.763 J/mol/K} & (\mathrm{CO, N_2O, NO}: w = 2)\\ R\ln 4 = \mathbf{11.526 J/mol/K} & (\mathrm{FClO_3}: w = 4)\\ R\ln(3/2) = \mathbf{3.371 J/mol/K} & (\text{Pauling Ice Ih}: w = 3/2) \end{cases}
\end{aligned}
$$

  

### Worked Example — Pauling Residual Entropy of Hexagonal Ice Ih & Disordered $\mathrm{CO}$ Crystal `[National/Invitational | Tier 3]`

(a) In hexagonal Ice Ih, each oxygen atom is tetrahedrally surrounded by 4 hydrogen-bond positions; the Bernal–Fowler ice rules require 2 hydrogens close ($\mathrm{O-H}$ covalent bonds) and 2 hydrogens far ($\mathrm{O\cdots H}$ hydrogen bonds) among the $\binom{4}{2} = 6$ ways around each oxygen, while each of the $2N$ hydrogen bonds is independently shared with probability $1/2$, giving $\Omega_0 = \left(6 \times (1/2)^2\right)^N = (3/2)^N$ (Linus Pauling, 1935). Calculate the residual entropy of $m = 100.0 g$ of Ice Ih ($M = 18.0153 g/mol$) at $T \to 0 K$.
(b) How many moles of solid carbon monoxide ($\mathrm{CO}$, random head-to-tail dipole orientation $w = 2$) have the exact same theoretical residual entropy as $100.0 g$ of Ice Ih?
**Solution.**
- **(a) Residual entropy of $n_{\mathrm{ice}} = 100.0 / 18.0153 = 5.55084 mol$ of Ice Ih:**
  
$$
S_{0,\mathrm{ice}} = n_{\mathrm{ice}} R \ln\left(\frac{3}{2}\right) = (5.55084)(8.314463)\ln(1.500) = (46.1523)(0.405465) = \mathbf{18.713 J/K}
$$
- **(b) Equivalent moles of solid $\mathrm{CO}$ ($S_{0,m,\mathrm{CO}} = R\ln 2 = 5.7631 J/mol/K$):**
  
$$
n_{\mathrm{CO}} = n_{\mathrm{ice}}\,\frac{\ln(3/2)}{\ln 2} = (5.55084)\left(\frac{0.405465}{0.693147}\right) = \mathbf{3.2470 mol}
$$

**✓ Verified by:** Measured calorimetric vs. spectroscopic residual entropy of Ice Ih is $3.4± 0.2 J/mol/K$, matching $R\ln(3/2) = 3.371 J/mol/K$ within $1\%$ (`check_sec06_09.py::ex08_7`).

### Worked Example — Debye $T^3$ Cryogenic Entropy, Steady-Conduction $\dot{S}_{\mathrm{gen}}$ & Ohmic Exergy Loss `[National/Invitational | Tier 3]`

(a) At cryogenic temperatures ($T \ll \Theta_D$), the molar heat capacity of a non-metallic insulating crystal obeys Debye's $T^3$ law: $C_{V,m}(T) = A T^3$. Given that dividing $C_{V,m}(T)/T = A T^2$ and accumulating from $0 K$ to $T$ yields $S_m(T) = \frac{1}{3}A T^3 = \frac{1}{3}C_{V,m}(T)$, calculate the absolute molar entropy $S_m(10.00 K)$ and internal energy $U_m(10.00 K) - U_m(0 K) = \frac{1}{4}A T^4 = \frac{1}{4}T C_{V,m}(T)$ of diamond ($\Theta_D = 2230 K$, $A = \frac{12\pi^4 R}{5\Theta_D^3} = 1.751×10^{-7} J/mol/K^4$) at $T = 10.00 K$.
(b) A cylindrical copper rod ($k = 398.0 W/m/K, A = 5.000×10^{-4} m^2, L = 0.2500 m$) with insulated sides connects a hot reservoir at $T_H = 500.0 K$ to a cold reservoir at $T_C = 300.0 K$ in an environment at $T_0 = 300.0 K$. In steady state, find the heat conduction rate $\dot{Q}$, the entropy change rate of the copper rod itself $\dot{S}_{\mathrm{rod}}$, the universe entropy generation rate $\dot{S}_{\mathrm{gen}}$, and the Gouy–Stodola rate of exergy destruction $\dot{X}_{\mathrm{dest}}$.
**Solution.**
- **(a) Debye cryogenic heat capacity, absolute entropy, and thermal energy of diamond at $T = 10.00 K$:**
  
$$
C_{V,m}(10.00 K) = A T^3 = (1.751×10^{-7} J/mol/K^4)(10.00\,K)^3 = \mathbf{1.751×10^{-4} J/mol/K}
$$

  
$$
S_m(10.00 K) = \frac{1}{3}C_{V,m}(10.00 K) = \mathbf{5.837×10^{-5} J/mol/K}, \qquad \Delta U_m(0 K\to10.00 K) = \frac{1}{4}T C_{V,m}(T) = \mathbf{4.378×10^{-4} J/mol}
$$
- **(b) Steady-state conduction bar entropy generation and exergy destruction (`2027 Cornell E1 Q7` trap):**
  
$$
\dot{Q} = k A\,\frac{T_H - T_C}{L} = \frac{(398.0)(5.000\times 10^{-4})(500.0 - 300.0)}{0.2500} = \mathbf{159.20 W}
$$

  Because the copper rod's temperature profile $T(x)$ is time-independent in steady state, its own state function entropy is constant ($\mathbf{\dot{S}_{\mathrm{rod}} = 0.000 W/K}$!). All entropy is generated at the reservoir boundaries:
  
$$
\dot{S}_{\mathrm{gen}} = \dot{S}_{\mathrm{univ}} = -\frac{\dot{Q}}{T_H} + \frac{\dot{Q}}{T_C} = (159.20)\left(\frac{1}{300.0} - \frac{1}{500.0}\right) = \mathbf{+0.21227 W/K}, \qquad \dot{X}_{\mathrm{dest}} = T_0\dot{S}_{\mathrm{gen}} = (300.0 K)(0.21227) = \mathbf{63.68 W}
$$

  Notice that $\dot{X}_{\mathrm{dest}} = \dot{Q}(1 - T_0/T_H) = 159.20(1 - 300/500) = 63.68 W$ is the exact Carnot power that could have been generated had $\dot{Q}$ driven a reversible engine between $T_H$ and $T_C$ instead of conducting directly!

**✓ Verified by:** Carnot lost-work identity $\dot{W}_{\mathrm{Carnot,lost}} = \dot{Q}(1 - T_C/T_H) = 159.20(0.400) = 63.68 W = T_C\dot{S}_{\mathrm{gen}}$ (`check_sec06_09.py::ex08_9`).

### [TRAP & DIAGNOSTIC: Top 5 Second-Law, Entropy, Enthalpy & Gibbs Exam Traps (§8 Diagnostic Matrix)]

| **Wrong move / Symptom** | **What it produces / Why it fails** | **5-second diagnostic & fix** |
| --- | --- | --- |
| Claiming $\Delta S_{\mathrm{sys}} \ge 0$ for every spontaneous process | Falsely rejects spontaneous freezing, condensation, or exothermic gas-consuming reactions where $\Delta S_{\mathrm{sys}} < 0$. | Only $\mathbf{\Delta S_{\mathrm{univ}} = \Delta S_{\mathrm{sys}} + \Delta S_{\mathrm{surr}} \ge 0}$ is required! A non-isolated system can decrease its entropy whenever $\Delta S_{\mathrm{surr}} \ge \|\Delta S_{\mathrm{sys}}\|$. |
| Unit mismatch between $\Delta H$ ($kJ/mol$) and $T\Delta S$ ($J/mol$) in $\Delta G = \Delta H - T\Delta S$ | Off by $1000\times$ on the entropy term, destroying $\Delta G$ and $T^*$. | Always divide $\Delta S[J/mol/K]$ by $\mathbf{1000}$ to convert to $kJ/mol/K$ before subtracting $T\Delta S$ from $\Delta H[kJ/mol]$! |
| Setting $S^\circ(298.15 K) = 0$ for pure elements ($\mathrm{O_2}, \mathrm{H_2}, \mathrm{C}$) in $\Delta_r S^\circ$ | Confuses the formation convention $\Delta_f H^\circ = 0$ with absolute Third-Law entropy $S^\circ > 0$. | Only at $T = 0 K$ is $S = 0$; at $298.15 K$, look up every element's positive $S^\circ$ in Table `tab:08:thermochem`! |
| Using arithmetic mean $T_f = (T_1+T_2)/2$ for a reversible engine between finite blocks | Violates $\Delta S_{\mathrm{univ}} = 0$, overestimating $T_f$ and miscalculating $W_{\max}$. | Direct contact $\to T_f = (T_1+T_2)/2$; reversible Carnot engine $\to T_{f,\mathrm{rev}} = \sqrt{T_1 T_2}$ and $W_{\max} = mc(\sqrt{T_1}-\sqrt{T_2})^2$. |
| Using $\Delta S = Q_{\mathrm{actual}}/T$ for an irreversible adiabatic process ($Q=0$) | Concludes $\Delta S = 0$ for free expansion, throttling, or real adiabatic turbines! | $Q = 0$ implies $\Delta S = 0$ **only if the process is also reversible**! Irreversible adiabatic processes always have $\Delta S = S_{\mathrm{gen}} > 0$. |

### [2027 HEAT-COLLECTOR DEVICE & LAB: Second-Law Exergy Budget & Why Post-Heating Swirling Destroys Stratification Score]

In the 2027 Heat-Lamp Collector (§`sec:15`), near-IR lamp radiation ($\sim2400 K$) absorbed mostly in the top $10 mm$ of the water column creates a warm, buoyant top layer at $T_{\mathrm{top}} \approx 52 °C$ over a cooler bottom layer at $T_{\mathrm{bot}} \approx 42 °C$. Under Official Clarifications `#1–#4`  **[S02]**, the Event Supervisor measures $T_f$ near the top center without stirring. If a competitor accidentally swirls the cup while extracting it during the 1-minute post-heating window (`Rule 5.II.g`), irreversible internal mixing generates entropy $S_{\mathrm{gen,mix}} \approx \frac{1}{2}m_w c_w \frac{(T_{\mathrm{top}} - T_{\mathrm{bot}})^2}{4\bar{T}^2} > 0$ and collapses the top-layer temperature down to the bulk mean $\bar{T} \approx 47 °C$ — costing $\mathbf{5 °C}$ of Temperature Gain ($\mathrm{TG}$) and ruining the team's Prediction Estimate ($\mathrm{PE}$)!

—
**See also:** Quick Sheet `QS-07` (§`sec:01.7`); Phase Transitions & Quality (§`sec:05`); First Law & Throttling (§`sec:07`); Heat Engines, Carnot & Rankine Cycles (§`sec:09`); Blackbody Radiation (§`sec:12`); Steam Tables (§`app:A`).
