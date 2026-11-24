<!-- Source: src/sec06.tex | Tab: Tab 4: GASES/LAWS | Target: 10 pp -->
# §6: Ideal & Real Gases, Kinetic Theory, Maxwell–Boltzmann Speeds, Equipartition & Van der Waals {#sec:06}

> **[SCOPE: REQUIRED | 2027 Rule 5.c.ii & 5.c.iii (All Tournament Levels) | Real-Gas & Quantum Freeze-Out Extensions]**

Gas-law and kinetic-theory items appear on $100\%$ of surveyed Division C exams  **[S25,S26,S27,S28]**, spanning foundational pressure/temperature unit traps through multi-compartment piston equilibrium and quantum heat-capacity freeze-out. Every governing relation in this chapter is presented in closed algebraic form under Rule `5.d.iv`  **[S01,S06]**.

## Macroscopic Gas Variables: Absolute vs. Gauge Pressure, Manometry & STP Standards

Gas equations of state respond strictly to **absolute pressure** $P_{\mathrm{abs}}$ and **absolute temperature** $T$ (in $K$ or $^\circ\mathrm{R}$). Most mechanical pressure gauges (Bourdon tubes, tire gauges, boiler dials) measure pressure relative to the local ambient atmosphere $P_{\mathrm{atm}}$  **[S13,S25]**:

$$
\begin{aligned}

  P_{\mathrm{abs}} = P_{\mathrm{atm}} + P_{\mathrm{gauge}}, \qquad P_{\mathrm{abs}} = P_{\mathrm{atm}} - P_{\mathrm{vac}}
\end{aligned}
$$

where $P_{\mathrm{atm}} = 101325 Pa = 101.325 kPa = 1.01325 bar = 760 Torr = 14.6959 psi$ is the standard sea-level atmosphere  **[S07,S08]**.

### [FORMULA & DECISION CARD: Hydrostatic Manometry, Barometry & Reference Conditions  **[S07,S08,S13]**]
- **Hydrostatic Column Pressure Difference:** For an incompressible manometer fluid of density $\rho_f$ in gravitational field $g_n = 9.80665 m/s^2$ with vertical height difference $h$:
  
$$
\begin{aligned}

    \Delta P = \rho_f g_n h, \qquad P_{\mathrm{gas}} = \begin{cases} \rho_f g_n h & \text{(closed-end vacuum manometer, } P_{\mathrm{ref}}\approx 0\text{)}\\ P_{\mathrm{atm}} \pm \rho_f g_n h & \text{(open-end U-tube: $+$ if open limb is higher; $-$ if gas limb is higher)} \end{cases}
\end{aligned}
$$

  
- **Fluid-Column Equivalence ($h_1\rho_1 = h_2\rho_2$):** Using $\rho_{\mathrm{Hg}}(0 °C) = 13595.1 kg/m^3$ and $\rho_{\mathrm{H_2O}}(4 °C) = 999.97 kg/m^3$, a column of mercury of height $h_{\mathrm{Hg}}$ corresponds to an equivalent water column $h_{\mathrm{H_2O}} = (\rho_{\mathrm{Hg}}/\rho_{\mathrm{H_2O}})h_{\mathrm{Hg}} = 13.595\,h_{\mathrm{Hg}}$ ($1 atm = 760 mm Hg = 10.332 m H _2 O$).

| **Standard Label** | **Temperature $T$** | **Pressure $P$** | **Ideal $V_m = RT/P$** | **Authority & Competition Usage** |
| --- | --- | --- | --- | --- |
| **IUPAC STP (Current)** | $0 °C = 273.15 K$ | $100 kPa = 1.000 bar$ | $22.71095 L/mol$ | IUPAC since 1982; NIST CODATA 2022 **[S07]** |
| **Traditional STP** | $0 °C = 273.15 K$ | $101.325 kPa = 1.000 atm$ | $22.41397 L/mol$ | Classic high-school textbooks & invitational MCQs **[S13,S29]** |
| **SATP (Thermochem.)** | $25 °C = 298.15 K$ | $100 kPa = 1.000 bar$ | $24.78957 L/mol$ | Standard ambient tables ($\Delta_f H^\circ, S^\circ, \Delta_f G^\circ$) **[S10,S16]** |
| **NTP (Engineering)** | $20 °C = 293.15 K$ | $101.325 kPa = 1.000 atm$ | $24.05485 L/mol$ | NIST / industrial compressed-gas metering |

### Worked Example — Marcet Boiler Gauge-to-Absolute Specific Volume & Compressibility Audit `[2027 Cornell E1 Q27c | Tier 2]`

In a Regnault/Marcet steam-boiler experiment at $T = 120.0 °C$ ($393.15 K$), the boiler pressure gauge reads $P_{\mathrm{gauge}} = 97.35 kPa$ when the local barometric pressure is $P_{\mathrm{atm}} = 101.325 kPa$. The measured specific volume of saturated water vapor from Clapeyron slope analysis is $v_{g,\mathrm{meas}} = 0.8919 m^3/kg$  **[S09,S25]**. (a) Calculate the ideal-gas specific volume $v_{g,\mathrm{ideal}}$ of steam ($M = 18.0153 g/mol$) at this state. (b) Determine the fractional error incurred if a competitor forgets to add $P_{\mathrm{atm}}$. (c) Compute the real-gas compressibility factor $Z = P_{\mathrm{abs}}v_{g,\mathrm{meas}}/(R_s T)$ and explain why $Z < 1$.
**Solution.**
- **Absolute pressure and specific gas constant:**
  
$$
P_{\mathrm{abs}} = P_{\mathrm{atm}} + P_{\mathrm{gauge}} = 101.325 + 97.35 = 198.675 kPa = 1.98675×10^{5} Pa, \qquad R_s = \frac{R}{M} = \frac{8.3144626 J/mol/K}{0.0180153 kg/mol} = 461.522 J/kg/K
$$
- **(a) Ideal-gas specific volume at $393.15 K$:**
  
$$
v_{g,\mathrm{ideal}} = \frac{R_s T}{P_{\mathrm{abs}}} = \frac{461.522 \times 393.15}{1.98675\times 10^5} = \mathbf{0.91329 m^3/kg}
$$
- **(b) Gauge-pressure trap error:** Using $P_{\mathrm{gauge}} = 97.35 kPa$ gives $v_{\mathrm{wrong}} = \frac{461.522\times 393.15}{9.735\times 10^4} = 1.8639 m^3/kg$, an overestimate of $+104.1\%$ (more than double the true volume!).
- **(c) Compressibility factor $Z$:**
  
$$
Z = \frac{v_{g,\mathrm{meas}}}{v_{g,\mathrm{ideal}}} = \frac{0.8919}{0.91329} = \mathbf{0.9766} < 1
$$

  At saturation near $2 bar$, polar $\mathrm{H_2O}$ molecules experience strong attractive dipole and hydrogen-bonding forces ($a$ term), pulling molecules closer together than an ideal gas and reducing $v_g$ by $2.34\%$.

**✓ Verified by:** Direct evaluation from $P_{\mathrm{abs}}V_m = ZRT$ with $V_{m,\mathrm{meas}} = 0.016068 m^3/mol$ gives $Z = (198675\times 0.016068)/(8.31446\times 393.15) = 0.9766$ (`check_sec06_09.py::ex06_1`).

## The Ideal Gas Equation of State, Classical Limit Laws & Multi-Bulb Mass Ledgers

In the dilute limit ($P \ll P_c$ and $T \gtrsim 2T_b$), all gases obey the universal **Ideal Gas Equation of State**  **[S07,S13]**:

$$
\begin{aligned}

  PV = nRT = N k_B T = m R_s T, \qquad \rho = \frac{m}{V} = \frac{PM}{RT} = \frac{P}{R_s T}, \qquad n_{\#}=\frac{N}{V}=\frac{P}{k_B T}
\end{aligned}
$$

where $n = m/M = N/N_A$ is the amount of substance ($mol$), $M$ is molar mass ($kg/mol$ in SI formulas!), $R = N_A k_B = 8.314462618 J/mol/K$, $R_s = R/M$ is the specific gas constant ($J/kg/K$), and $n_{\#} = N/V$ is number density ($/m^3$; at $1\text{ atm}, 273.15 K$, Loschmidt's constant is $n_0 = 2.68678×10^{25} /m^3$  **[S07]**).

### [FORMULA & DECISION CARD: Classical Gas Laws & Valve/Leak Ledgers  **[S13]**]

| **Law / Invariant** | **Held Fixed** | **Algebraic Ratio Form** |
| --- | --- | --- |
| **Combined Gas Law** | — | $\dfrac{P_1 V_1}{n_1 T_1} = \dfrac{P_2 V_2}{n_2 T_2} = R$ |
| **Boyle's Law** (1662) | $n, T$ | $P_1 V_1 = P_2 V_2$ (hyperbola) |
| **Charles's Law** (1787) | $n, P$ | $V_1/T_1 = V_2/T_2$ ($\beta_V = 1/T$) |
| **Amontons / Gay-Lussac** | $n, V$ | $P_1/T_1 = P_2/T_2$ |
| **Avogadro's Law** (1811) | $P, T$ | $V_1/n_1 = V_2/n_2 = V_m$ |
| **Density-State Ratio** | Gas $M$ | $\dfrac{P_1}{\rho_1 T_1} = \dfrac{P_2}{\rho_2 T_2} = R_s$ |

**Connected Rigid Bulbs at Different Temperatures ($T_A, T_B$):** When a valve opens between bulbs of volumes $V_A$ (held at $T_A$) and $V_B$ (held at $T_B$), mechanical equilibrium enforces a **uniform final pressure $P_f$** across the capillary while total moles are conserved ($n_{\mathrm{tot}} = n_{A,i} + n_{B,i} = n_{A,f} + n_{B,f}$):

$$
\begin{aligned}

  \frac{P_{A,i}V_A}{T_{A,i}} + \frac{P_{B,i}V_B}{T_{B,i}} = P_f\left(\frac{V_A}{T_{A,f}} + \frac{V_B}{T_{B,f}}\right)
\end{aligned}
$$

### [SHORTCUT: 7 Competition Forms of $R$  **[S07,S08]**]

Pick the value of $R$ matching the problem's pressure and volume units to avoid conversion errors:
| **Numerical Value of $R$** | **Exact Unit Combination** |
| --- | --- |
| $\mathbf{8.314463}$ | $J/mol/K = Pa m^3/mol/K$ |
| $\mathbf{8.314463}$ | $L kPa/mol/K$ ($1\,L kPa = 1 J$) |
| $\mathbf{0.0831446}$ | $L bar/mol/K$ ($1\,L bar = 100 J$) |
| $\mathbf{0.0820574}$ | $L atm/mol/K$ ($1\,L atm = 101.325 J$) |
| $\mathbf{62.36360}$ | $L Torr/mol/K$ (or $L mm Hg/mol/K$) |
| $\mathbf{1.987204}$ | $cal _{ th }/mol/K$ ($\approx 2.0 cal/mol/K$) |
| $\mathbf{8.31446\times 10^7}$ | $erg/mol/K$ ($1\,J = 10^7\,erg$) |

### [TRAP & DIAGNOSTIC: Open-Room Heating: Internal Energy Does NOT Increase!]

For an open room or vented attic of fixed volume $V$ exposed to constant atmospheric pressure $P_{\mathrm{atm}}$ (as in `2019 MIT E2 P1b`), heating the air from $T_1$ to $T_2$ causes warm air to escape so that $n(T) = P_{\mathrm{atm}}V/(RT)$. Consequently, the total internal energy of the air remaining inside the room is $U_{\mathrm{room}} = \frac{f}{2}nRT = \frac{f}{2}P_{\mathrm{atm}}V = \mathbf{\text{constant}}$!

### Worked Example — Two-Bulb Capillary Equilibrium & Fractional Mass Redistribution `[Invitational Archetype | Tier 2]`

Two rigid glass bulbs of volumes $V_A = 2.00 L$ and $V_B = 3.00 L$ are connected by a negligible-volume stopcock. Initially, the stopcock is closed: Bulb $A$ contains dry nitrogen ($\mathrm{N_2}$, $M = 28.0134 g/mol$) at $P_{A,i} = 250.0 kPa$ and $T_{A,i} = 300.0 K$, while Bulb $B$ contains $\mathrm{N_2}$ at $P_{B,i} = 100.0 kPa$ and $T_{B,i} = 400.0 K$. The stopcock is opened while Bulb $A$ is maintained in a water bath at $T_{A,f} = 300.0 K$ and Bulb $B$ is heated to $T_{B,f} = 500.0 K$. Find (a) the total moles $n_{\mathrm{tot}}$, (b) the final uniform pressure $P_f$, and (c) the net mass of $\mathrm{N_2}$ ($\Delta m_A$) that flows into or out of Bulb $A$.
**Solution.**
- **(a) Initial and total moles (using $R = 8.314463 L kPa/mol/K$):**
  
$$
n_{A,i} = \frac{P_{A,i}V_A}{RT_{A,i}} = \frac{250.0\times 2.00}{8.314463\times 300.0} = 0.200454 mol, \quad n_{B,i} = \frac{P_{B,i}V_B}{RT_{B,i}} = \frac{100.0\times 3.00}{8.314463\times 400.0} = 0.090204 mol
$$

  
$$
n_{\mathrm{tot}} = n_{A,i} + n_{B,i} = \mathbf{0.290658 mol} \quad (m_{\mathrm{tot}} = n_{\mathrm{tot}}M = 8.1423 g)
$$
- **(b) Final pressure $P_f$ from Eq. (`eq:06:two-bulbs`):**
  
$$
P_f = \frac{n_{\mathrm{tot}}R}{\dfrac{V_A}{T_{A,f}} + \dfrac{V_B}{T_{B,f}}} = \frac{250.0(2.00)/300.0 + 100.0(3.00)/400.0}{2.00/300.0 + 3.00/500.0} = \frac{1.66667 + 0.75000}{0.0066667 + 0.0060000} = \frac{2.41667}{0.0126667} = \mathbf{190.789 kPa}
$$
- **(c) Final moles in Bulb $A$ and net mass transfer:**
  
$$
n_{A,f} = \frac{P_f V_A}{RT_{A,f}} = \frac{190.789\times 2.00}{8.314463\times 300.0} = 0.152978 mol, \qquad \Delta m_A = (n_{A,f} - n_{A,i})M = (-0.047476\,mol)(28.0134 g/mol) = \mathbf{-1.3300 g}
$$

  Thus $1.330 g$ of $\mathrm{N_2}$ flows from Bulb $A$ into Bulb $B$.

**✓ Verified by:** Conservation check: $n_{B,f} = P_f V_B/(RT_{B,f}) = 0.137680 mol$ and $n_{A,f} + n_{B,f} = 0.152978 + 0.137680 = 0.290658 mol = n_{\mathrm{tot}}$ (`check_sec06_09.py::ex06_2`).

## Dalton's Law of Partial Pressures, Wet Gases & Graham's Law of Effusion

For a non-reacting mixture of $K$ ideal gases occupying volume $V$ at temperature $T$, each species $i$ behaves as if it alone occupied the entire volume  **[S13,S16]**:

$$
\begin{aligned}

  P_{\mathrm{tot}} = \sum_{i=1}^K P_i = \left(\sum_{i=1}^K n_i\right)\frac{RT}{V} = n_{\mathrm{tot}}\frac{RT}{V}, \qquad P_i = x_i P_{\mathrm{tot}}, \qquad x_i = \frac{n_i}{n_{\mathrm{tot}}} = \frac{P_i}{P_{\mathrm{tot}}} = \frac{V_i}{V_{\mathrm{tot}}}
\end{aligned}
$$

where $V_i = x_i V_{\mathrm{tot}}$ is the **Amagat partial volume** (the volume species $i$ would occupy alone at $P_{\mathrm{tot}}$ and $T$). The mixture's apparent molar mass $M_{\mathrm{mix}}$ and specific gas constant $R_{s,\mathrm{mix}}$ are:

$$
\begin{aligned}

  M_{\mathrm{mix}} = \frac{m_{\mathrm{tot}}}{n_{\mathrm{tot}}} = \sum_{i=1}^K x_i M_i = \left(\sum_{i=1}^K \frac{w_i}{M_i}\right)^{-1}, \qquad R_{s,\mathrm{mix}} = \frac{R}{M_{\mathrm{mix}}} = \sum_{i=1}^K w_i R_{s,i}
\end{aligned}
$$

where $w_i = m_i/m_{\mathrm{tot}} = x_i M_i / M_{\mathrm{mix}}$ is the mass fraction of species $i$.

### [FORMULA & DECISION CARD: Wet-Gas Eudiometry & Graham's Law of Pinhole Effusion  **[S09,S13]**]
- **Gas Collected Over Water (Eudiometer Tube Correction):** When a gas is bubbled through liquid water at temperature $T$ into an inverted graduated tube where the internal water level stands a height $h$ *above* the outer reservoir level, the partial pressure of the dry gas is:
  
$$
\begin{aligned}

    P_{\mathrm{tot}} = P_{\mathrm{atm}} - \rho_{\mathrm{H_2O}} g_n h = P_{\mathrm{dry}} + P_{\mathrm{sat,H_2O}}(T) \implies \boxed{P_{\mathrm{dry}} = P_{\mathrm{atm}} - \rho_{\mathrm{H_2O}} g_n h - P_{\mathrm{sat,H_2O}}(T)}
\end{aligned}
$$

  
- **Graham's Law of Effusion (1848):** The molecular flux escaping through a pinhole of area $A_h$ (diameter $\ll$ mean free path $\lambda$) into vacuum is $\dot{N} = \frac{1}{4}(N/V)v_{\mathrm{avg}}A_h = \frac{P A_h}{\sqrt{2\pi m_0 k_B T}}$. Comparing two gases at identical $T$ and $P$:
  
$$
\begin{aligned}

    \boxed{\frac{\dot{n}_1}{\dot{n}_2} = \frac{\dot{V}_1}{\dot{V}_2} = \frac{v_{\mathrm{avg},1}}{v_{\mathrm{avg},2}} = \sqrt{\frac{M_2}{M_1}}}, \qquad \frac{t_{\mathrm{eff},1}}{t_{\mathrm{eff},2}} = \sqrt{\frac{M_1}{M_2}}, \qquad \boxed{\frac{\dot{m}_1}{\dot{m}_2} = \frac{M_1\dot{n}_1}{M_2\dot{n}_2} = \sqrt{\frac{M_1}{M_2}}}
\end{aligned}
$$

  
- **Multi-Stage Cascade Enrichment ($N_{\mathrm{stage}}$ porous-barrier stages):** If a binary mixture of initial molar ratio $(n_1/n_2)_0$ effuses sequentially through $N_{\mathrm{stage}}$ ideal vacuum stages, the enriched molar ratio is:
  
$$
\begin{aligned}

    \left(\frac{n_1}{n_2}\right)_{N_{\mathrm{stage}}} = \left(\frac{n_1}{n_2}\right)_0 \left(\frac{M_2}{M_1}\right)^{N_{\mathrm{stage}}/2} \implies N_{\mathrm{stage}} = \frac{2\ln\left[\dfrac{(n_1/n_2)_{N_{\mathrm{stage}}}}{(n_1/n_2)_0}\right]}{\ln(M_2/M_1)}
\end{aligned}
$$

### Worked Example — Wet Oxygen Eudiometry & Graham Effusion Mass-vs-Mole Trap `[Regional/State Standard | Tier 2]`

A $500.0 mL$ eudiometer tube collects oxygen gas ($\mathrm{O_2}$, $M = 31.9988 g/mol$) over water at $T = 25.0 °C$ ($298.15 K$, where $P_{\mathrm{sat,H_2O}} = 3.1699 kPa$ from NIST Table 3.1  **[S09]**). The water level inside the tube is $h = 13.60 cm$ *above* the outer dish ($\rho_{\mathrm{H_2O}} = 997.0 kg/m^3$), and the barometer reads $P_{\mathrm{atm}} = 101.325 kPa$. (a) Find the dry mass of $\mathrm{O_2}$ collected. (b) If an equimolar mixture of $\mathrm{He}$ ($M_{\mathrm{He}} = 4.0026 g/mol$) and $\mathrm{O_2}$ at $298.15 K$ effuses through a pinhole into vacuum, compute both the **molar** effusion ratio $\dot{n}_{\mathrm{He}}/\dot{n}_{\mathrm{O_2}}$ and the **mass** effusion ratio $\dot{m}_{\mathrm{He}}/\dot{m}_{\mathrm{O_2}}$.
**Solution.**
- **(a) Hydrostatic and vapor-pressure corrections from Eq. (`eq:06:wet-gas`):**
  
$$
\Delta P_{\mathrm{hydro}} = \rho_{\mathrm{H_2O}}g_n h = (997.0)(9.80665)(0.1360) = 1329.7 Pa = 1.3297 kPa
$$

  
$$
P_{\mathrm{dry,O_2}} = 101.325 - 1.3297 - 3.1699 = 96.8254 kPa
$$

  
$$
n_{\mathrm{O_2}} = \frac{P_{\mathrm{dry,O_2}}V}{RT} = \frac{(96.8254)(0.5000)}{(8.314463)(298.15)} = 0.0195295 mol \implies m_{\mathrm{O_2}} = n_{\mathrm{O_2}}M_{\mathrm{O_2}} = \mathbf{0.62492 g}
$$
- **(b) Molar vs. mass effusion rate ratios from Eq. (`eq:06:graham`):**
  
$$
\frac{\dot{n}_{\mathrm{He}}}{\dot{n}_{\mathrm{O_2}}} = \sqrt{\frac{M_{\mathrm{O_2}}}{M_{\mathrm{He}}}} = \sqrt{\frac{31.9988}{4.0026}} = \mathbf{2.8275}, \qquad \frac{\dot{m}_{\mathrm{He}}}{\dot{m}_{\mathrm{O_2}}} = \sqrt{\frac{M_{\mathrm{He}}}{M_{\mathrm{O_2}}}} = \sqrt{\frac{4.0026}{31.9988}} = \mathbf{0.35367}
$$

  
  *Trap check:* Helium effuses $2.83\times$ faster in *moles per second*, but oxygen effuses $2.83\times$ faster in *grams per second*!

**✓ Verified by:** Identity $(\dot{n}_{\mathrm{He}}/\dot{n}_{\mathrm{O_2}})(\dot{m}_{\mathrm{He}}/\dot{m}_{\mathrm{O_2}}) = 2.82746 \times 0.353674 = 1.00000$ (`check_sec06_09.py::ex06_3`).

## Microscopic Kinetic Theory, Maxwell–Boltzmann Speeds & Mean Free Path

### [DERIVATION: Algebra-Only Cubic-Box Collision Proof of Kinetic Theory Pressure  **[S13,S15]**]

Consider $N$ point molecules of mass $m_0 = M/N_A$ moving without intermolecular forces inside a rigid cube of side $L$ and volume $V = L^3$:
- **Single-wall elastic impulse:** A molecule with velocity components $(v_x, v_y, v_z)$ strikes the right wall ($x = L$, area $A = L^2$) and rebounds elastically with $(-v_x, v_y, v_z)$, transferring momentum $\Delta p_x = +2m_0 v_x$ to the wall.
- **Round-trip collision interval:** The molecule travels distance $2L$ across the box and back before hitting the same wall again, requiring time $\Delta t = 2L/v_x$, so its time-averaged force on the wall is $f_x = \Delta p_x / \Delta t = m_0 v_x^2 / L$.
- **3D isotropy & Pythagorean theorem:** Summing over all $N$ molecules and dividing by area $A = L^2$ gives $P = \frac{N m_0 \langle v_x^2\rangle}{V}$. Because thermal motion has no preferred axis, $\langle v_x^2\rangle = \langle v_y^2\rangle = \langle v_z^2\rangle = \frac{1}{3}\langle v_x^2 + v_y^2 + v_z^2\rangle = \frac{1}{3}\langle v^2\rangle = \frac{1}{3}v_{\mathrm{rms}}^2$, yielding:
  
$$
\begin{aligned}

    \boxed{P = \frac{1}{3}\frac{N}{V}m_0 v_{\mathrm{rms}}^2 = \frac{1}{3}\rho v_{\mathrm{rms}}^2 = \frac{2}{3}\left(\frac{N}{V}\right)K_{\mathrm{trans,avg}}}, \qquad \boxed{K_{\mathrm{trans,avg}} = \frac{1}{2}m_0 v_{\mathrm{rms}}^2 = \frac{3}{2}k_B T}
\end{aligned}
$$

  

In thermal equilibrium at temperature $T$, James Clerk Maxwell (1860) and Ludwig Boltzmann (1868) showed that the fraction of molecules with speeds in $[v, v+\Delta v]$ follows the **Maxwell–Boltzmann speed distribution**  **[S13,S15,S23]**:

$$
\begin{aligned}

  f(v) = 4\pi\left(\frac{m_0}{2\pi k_B T}\right)^{3/2} v^2 \exp\left(-\frac{m_0 v^2}{2k_B T}\right) = 4\pi\left(\frac{M}{2\pi R T}\right)^{3/2} v^2 \exp\left(-\frac{M v^2}{2 R T}\right)
\end{aligned}
$$

### [FORMULA & DECISION CARD: Characteristic Molecular Speeds, Sound Speed & Mean Free Path  **[S13,S15,S18]**]

| **Characteristic Speed** | **Molar Form ($M$ in $kg/mol$!)** | **Molecular Form ($m_0$ in $kg$)** | **Physical Meaning & Ratio to $v_{\mathrm{mp}}$** |
| --- | --- | --- | --- |
| **Most Probable ($v_{\mathrm{mp}}$)** | $\displaystyle v_{\mathrm{mp}} = \sqrt{\frac{2RT}{M}}$ | $\displaystyle \sqrt{\frac{2k_B T}{m_0}}$ | Peak of $f(v)$ curve; $\mathbf{1.0000\,v_{\mathrm{mp}}}$ ($\sqrt{2} \approx 1.4142$) |
| **Average ($v_{\mathrm{avg}} = \langle v\rangle$)** | $\displaystyle v_{\mathrm{avg}} = \sqrt{\frac{8RT}{\pi M}}$ | $\displaystyle \sqrt{\frac{8k_B T}{\pi m_0}}$ | Controls collision rate & effusion; $\mathbf{1.1284\,v_{\mathrm{mp}}}$ ($\sqrt{8/\pi} \approx 1.5958$) |
| **Root-Mean-Square ($v_{\mathrm{rms}}$)** | $\displaystyle v_{\mathrm{rms}} = \sqrt{\frac{3RT}{M}} = \sqrt{\frac{3P}{\rho}}$ | $\displaystyle \sqrt{\frac{3k_B T}{m_0}}$ | Controls $K_{\mathrm{trans}}$ & pressure $P$; $\mathbf{1.2247\,v_{\mathrm{mp}}}$ ($\sqrt{3} \approx 1.7321$) |
| **Adiabatic Sound ($c_s$)** | $\displaystyle c_s = \sqrt{\frac{\gamma RT}{M}} = \sqrt{\frac{\gamma P}{\rho}}$ | $\displaystyle \sqrt{\frac{\gamma k_B T}{m_0}} = \sqrt{\frac{\gamma}{3}}\,v_{\mathrm{rms}}$ | Acoustic wave speed ($\gamma = C_P/C_V$); for air ($\gamma=1.4$), $c_s = 0.6831\,v_{\mathrm{rms}}$ |

- **Clausius–Maxwell Hard-Sphere Mean Free Path ($\lambda$) and Collision Frequency ($Z_{\mathrm{coll}}$):** For molecules of effective collision diameter $d$ (typical $d \approx 2.2×10^{-10}–4.0×10^{-10} m$; for $\mathrm{N_2}$, $d \approx 3.70×10^{-10} m$):
  
$$
\begin{aligned}

    \boxed{\lambda = \frac{1}{\sqrt{2}\,\pi d^2 (N/V)} = \frac{k_B T}{\sqrt{2}\,\pi d^2 P}}, \qquad Z_{\mathrm{coll}} = \frac{v_{\mathrm{avg}}}{\lambda} = \sqrt{2}\,\pi d^2 \left(\frac{P}{k_B T}\right)\sqrt{\frac{8RT}{\pi M}} = \frac{4\pi d^2 P}{\sqrt{\pi m_0 k_B T}}
\end{aligned}
$$

  
- **Maxwell's Pressure-Independent Transport Law (1860/1866):** Because dynamic viscosity scales as $\mu \approx \frac{1}{3}\rho v_{\mathrm{avg}}\lambda$ and thermal conductivity scales as $k \approx \frac{1}{3}\rho c_v v_{\mathrm{avg}}\lambda$, the density $\rho \propto P$ and mean free path $\lambda \propto 1/P$ **cancel out exactly**! Thus dilute-gas $\mu$ and $k$ are **independent of pressure $P$** at fixed $T$ and scale as $\mu \propto \sqrt{T}$ and $k \propto \sqrt{T}$  **[S12,S23]**.

> **[Vector Figure: Maxwell–Boltzmann molecular speed distribution $f(v)$ for $\mathrm{N_2}$ at $T = 300 K$ and $T = 900 K$  **[S13,S15]**. Tripling $T$ shifts all three characteristic speeds ($v_{\mathrm{mp}} < v_{\mathrm{avg}} < v_{\mathrm{rms}}$) upward by $\sqrt{3} \approx 1.732$ and lowers the peak height $f(v_{\mathrm{mp}}) \propto 1/\sqrt{T}$ by $\sqrt{3}$ so total probability area remains unity. | Label: `fig:06:maxwell-boltzmann`]**
> - **Diagram Annotations & Key Elements:** **X-Axis:** Molecular speed $v$ ($m/s$) • **Y-Axis:** Probability density $f(v)$ ($10^{-3}\,s/m$) • **Legend:** $\mathrm{N_2}$ at $T=300 K$ ($M=28.0 g/mol$) • **Legend:** $\mathrm{N_2}$ at $T=900 K$ (broadened, peak $\div\sqrt{3}$) • $v_{\mathrm{avg}}=476 m/s$ • $v_{\mathrm{rms}}=517 m/s$

### Worked Example — Discrete Two-Speed Ensemble Trap vs. Mean Free Path in Dry Air `[2018 MIT E3 Q21 | Tier 2]`

(a) In a hypothetical ideal gas of $N$ particles (each of mass $m_0$), exactly half the particles move at speed $v_0$ and half move at speed $2v_0$. Express the kinetic temperature $T_{\mathrm{actual}}$ in terms of $m_0, v_0, k_B$, and compare it with the false temperature $T_{\mathrm{false}}$ obtained by substituting the mean speed $\langle v\rangle = 1.5v_0$ into $\frac{1}{2}m_0\langle v\rangle^2 = \frac{3}{2}k_B T$. (b) For dry nitrogen ($\mathrm{N_2}$, $M = 0.0280134 kg/mol$, collision diameter $d = 3.70×10^{-10} m$) at $T = 300.0 K$ and $P = 101.325 kPa$, compute $v_{\mathrm{mp}}, v_{\mathrm{avg}}, v_{\mathrm{rms}}$, the mean free path $\lambda$, and the single-molecule collision frequency $Z_{\mathrm{coll}}$.
**Solution.**
- **(a) Discrete speed ensemble ($\langle v^2\rangle$ vs. $\langle v\rangle^2$ trap):**
  
$$
\langle v^2\rangle = \frac{1}{2}v_0^2 + \frac{1}{2}(2v_0)^2 = 2.50\,v_0^2 \implies T_{\mathrm{actual}} = \frac{m_0\langle v^2\rangle}{3k_B} = \mathbf{\frac{5m_0 v_0^2}{6k_B} = 0.8333\,\frac{m_0 v_0^2}{k_B}}
$$

  Using $\langle v\rangle^2 = (1.5v_0)^2 = 2.25\,v_0^2$ yields $T_{\mathrm{false}} = \frac{2.25m_0 v_0^2}{3k_B} = \frac{3m_0 v_0^2}{4k_B} = 0.7500\,\frac{m_0 v_0^2}{k_B}$, underestimating $T_{\mathrm{actual}}$ by $10.0\%$ because $\mathrm{Var}(v) = \langle v^2\rangle - \langle v\rangle^2 = 0.25\,v_0^2 > 0$!
- **(b) Characteristic speeds and mean free path for $\mathrm{N_2}$ at $300.0 K, 101.325 kPa$:**
  
$$
v_{\mathrm{mp}} = \sqrt{\frac{2RT}{M}} = \mathbf{422.09 m/s}, \qquad v_{\mathrm{avg}} = \sqrt{\frac{8RT}{\pi M}} = \mathbf{476.28 m/s}, \qquad v_{\mathrm{rms}} = \sqrt{\frac{3(8.314463)(300.0)}{0.0280134}} = \mathbf{516.95 m/s}
$$

  
$$
\lambda = \frac{k_B T}{\sqrt{2}\,\pi d^2 P} = \frac{(1.380649\times 10^{-23})(300.0)}{\sqrt{2}\,\pi (3.70\times 10^{-10})^2 (101325)} = \mathbf{6.721×10^{-8} m} = 67.21 nm, \qquad Z_{\mathrm{coll}} = \frac{v_{\mathrm{avg}}}{\lambda} = \mathbf{7.087×10^{9} /s}
$$

**✓ Verified by:** Number density $n_{\#} = P/(k_BT) = 2.446×10^{25} /m^3$ gives $\lambda = 1/(\sqrt{2}\pi d^2 n_{\#}) = 67.21 nm$ (`check_sec06_09.py::ex06_4`).

## Equipartition of Energy, Mayer's Relation, Quantum Freeze-Out & Gas Mixtures

By the classical **Equipartition Theorem**  **[S13,S15]**, every independent quadratic term ($\frac{1}{2}mv_i^2$, $\frac{1}{2}I_j\omega_j^2$, or $\frac{1}{2}k_s q_k^2$) in a molecule's Hamiltonian contributes $\frac{1}{2}k_B T$ to the average molecular energy ($\frac{1}{2}RT$ per mole). Notice that a 1D harmonic vibrational mode has **two** quadratic terms (kinetic + potential), contributing $2\times\frac{1}{2}RT = RT$ per mole when fully excited! For a molecule of $N_{\mathrm{atom}}$ atoms, total modes are $3N_{\mathrm{atom}} = 3_{\mathrm{trans}} + f_{\mathrm{rot}} + f_{\mathrm{vib,modes}}$, where $f_{\mathrm{rot}} = 2$ (linear molecule, since moment of inertia about the internuclear axis is negligible) or $f_{\mathrm{rot}} = 3$ (nonlinear molecule).

### [FORMULA & DECISION CARD: Equipartition Relations, Mayer's Identity & Quantum Mode Freeze-Out  **[S10,S13,S15]**]

$$
\begin{aligned}

  \boxed{U = \frac{f}{2}nRT = \frac{f}{2}PV}, \qquad \boxed{C_{V,m} = \frac{f}{2}R = \frac{R}{\gamma - 1}}, \qquad \boxed{C_{P,m} = C_{V,m} + R = \frac{f+2}{2}R = \frac{\gamma R}{\gamma - 1}}, \qquad \boxed{\gamma = \frac{C_P}{C_V} = 1 + \frac{2}{f}}
\end{aligned}
$$

**Algebra-Only Proof of Mayer's Relation ($C_{P,m} - C_{V,m} = R$):** By definition $H = U + PV$. For an ideal gas, $PV = nRT$ and $U = U(T)$ only (Joule's Second Law), so over any temperature change $\Delta T$: $\Delta H = \Delta U + \Delta(PV) \implies nC_{P,m}\Delta T = nC_{V,m}\Delta T + nR\Delta T \implies C_{P,m} - C_{V,m} = R$ (and $c_p - c_v = R_s = R/M$).
**Quantum Rotational & Vibrational Freeze-Out (`2018 MIT E3 MC4` & `2027 Cornell E1 Q35`):** A quantum mode of spacing $\Delta E = k_B\Theta$ is thermally active only when $T \gtrsim \Theta$. For $\mathrm{H_2}$, $\Theta_{\mathrm{rot}} = \frac{\hbar^2}{2I k_B} \approx 85.4 K$ and $\Theta_{\mathrm{vib}} = \frac{\hbar\omega}{k_B} \approx 6100 K$ (for $\mathrm{N_2}$, $\Theta_{\mathrm{rot}} \approx 2.88 K$ and $\Theta_{\mathrm{vib}} \approx 3374 K$):
- **Cryogenic ($T \ll \Theta_{\mathrm{rot}}$, e.g. $\mathrm{H_2}$ below $50 K$):** Rotational and vibrational modes are frozen out $\implies f = 3$ ($C_{V,m} = \frac{3}{2}R, \gamma = \frac{5}{3}$).
- **Room Temperature ($\Theta_{\mathrm{rot}} \ll T \ll \Theta_{\mathrm{vib}}$, $300 K$):** Translation + rotation active, vibration frozen out $\implies f = 5$ ($C_{V,m} = \frac{5}{2}R, \gamma = \frac{7}{5} = 1.40$).
- **High Temperature ($T \gtrsim \Theta_{\mathrm{vib}}$, $\gtrsim 3000 K$):** Translation + rotation + vibration (2 quadratic terms!) active $\implies f = 7$ ($C_{V,m} = \frac{7}{2}R, \gamma = \frac{9}{7} \approx 1.286$).

> **[Vector Figure: Molar heat capacity $C_{V,m}/R$ of diatomic hydrogen ($\mathrm{H_2}$) vs. $\log_{10}(T/K)$ showing quantum freeze-out of vibrational modes below $\sim1000 K$ and rotational modes below $\sim85 K$  **[S10,S13,S15]**. | Label: `fig:06:equipartition`]**
> - **Diagram Annotations & Key Elements:** **X-Axis:** $\log_{10}(T/K)$ [Temperature $T$ from $10 K$ to $10000 K$] • **Y-Axis:** Dimensionless Molar Heat Capacity $C_{V,m}/R$ • **Trans. only** ($f=3$) • **Trans. + 2 Rot.** ($f=5$ at $300 K$) • **+ 1 Vib. (KE+PE)** ($f=7$) • Dissociation $\gtrsim 4500 K$

**Table:** Equipartition Ideal Limits vs. NIST Measured Gas Properties at $T = 298.15 K$ ($25 °C$) and $P = 1 atm$ ($101.325 kPa$)  **[S10,S12,S13]**.

| **Gas** | **Formula** | $M$ | $R_s$ | $f_{\mathrm{id}}$ | $C_{V,\mathrm{id}}/R$ | $\gamma_{\mathrm{id}}$ | **NIST** | **NIST** $C_{V,m}$ | **NIST** $C_{P,m}$ | **NIST** $c_v$ | **NIST** $c_p$ | **NIST** $\gamma$ | $c_s$ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | ($g/mol$) | ($J/kg/K$) |  |  |  | $C_{V,m}/R$ | ($J/mol/K$) | ($J/mol/K$) | ($J/kg/K$) | ($J/kg/K$) | ($25 °C$) | ($m/s$) |
| Helium | $\mathrm{He}$ | $4.0026$ | $2077.26$ | $3$ | $1.50$ | $5/3$ | $1.500$ | $12.47$ | $20.79$ | $3116.2$ | $5193.1$ | $1.6665$ | $1016.4$ |
| Neon | $\mathrm{Ne}$ | $20.1797$ | $412.02$ | $3$ | $1.50$ | $5/3$ | $1.500$ | $12.47$ | $20.79$ | $618.1$ | $1030.3$ | $1.6670$ | $452.7$ |
| Argon | $\mathrm{Ar}$ | $39.9480$ | $208.13$ | $3$ | $1.50$ | $5/3$ | $1.501$ | $12.48$ | $20.84$ | $312.4$ | $521.6$ | $1.6696$ | $321.7$ |
| Hydrogen | $\mathrm{H_2}$ | $2.0159$ | $4124.48$ | $5$ | $2.50$ | $7/5$ | $2.468$ | $20.52$ | $28.84$ | $10179.7$ | $14306.4$ | $1.4054$ | $1315.4$ |
| Nitrogen | $\mathrm{N_2}$ | $28.0134$ | $296.80$ | $5$ | $2.50$ | $7/5$ | $2.504$ | $20.82$ | $29.17$ | $743.1$ | $1041.4$ | $1.4013$ | $352.1$ |
| Oxygen | $\mathrm{O_2}$ | $31.9988$ | $259.84$ | $5$ | $2.50$ | $7/5$ | $2.534$ | $21.07$ | $29.43$ | $658.5$ | $919.6$ | $1.3966$ | $328.7$ |
| Dry Air | $\mathrm{Air}$ | $28.9655$ | $287.05$ | $5$ | $2.50$ | $7/5$ | $2.503$ | $20.82$ | $29.14$ | $718.6$ | $1006.2$ | $1.4002$ | $346.1$ |
| Carbon monoxide | $\mathrm{CO}$ | $28.0101$ | $296.84$ | $5$ | $2.50$ | $7/5$ | $2.505$ | $20.83$ | $29.19$ | $743.7$ | $1042.2$ | $1.4013$ | $352.0$ |
| Carbon dioxide$^*$ | $\mathrm{CO_2}$ | $44.0095$ | $188.92$ | $5$ | $2.50$ | $7/5$ | $\mathbf{3.480}$ | $28.94$ | $37.45$ | $657.5$ | $850.9$ | $1.2941$ | $268.6$ |
| Water vapor ($100 °C$) | $\mathrm{H_2O}(g)$ | $18.0153$ | $461.52$ | $6$ | $3.00$ | $4/3$ | $3.371$ | $28.02$ | $37.47$ | $1555.6$ | $2079.8$ | $1.3370$ | $472.2$ |
| Methane | $\mathrm{CH_4}$ | $16.0425$ | $518.28$ | $6$ | $3.00$ | $4/3$ | $3.297$ | $27.41$ | $35.80$ | $1708.6$ | $2231.7$ | $1.3062$ | $448.5$ |
| Ammonia | $\mathrm{NH_3}$ | $17.0305$ | $488.21$ | $6$ | $3.00$ | $4/3$ | $3.366$ | $27.98$ | $36.84$ | $1643.2$ | $2163.2$ | $1.3165$ | $433.1$ |
| Sulfur dioxide | $\mathrm{SO_2}$ | $64.0638$ | $129.78$ | $6$ | $3.00$ | $4/3$ | $3.905$ | $32.47$ | $41.60$ | $506.8$ | $649.4$ | $1.2813$ | $218.9$ |
| Sulfur hexafluoride | $\mathrm{SF_6}$ | $146.0554$ | $56.93$ | $6$ | $3.00$ | $4/3$ | $\mathbf{10.699}$ | $88.96$ | $97.71$ | $609.1$ | $669.0$ | $1.0984$ | $135.0$ |

{$^*$Linear triatomic $\mathrm{CO_2}$ has two degenerate low-frequency bending modes ($\Theta_{\mathrm{bend}} = 960 K$) partially excited at $298 K$, elevating $C_{V,m}/R$ from $2.50$ to $3.48$ (`2019 MIT E2 MC13`)  **[S13,S26]**.}

### Worked Example — Adiabatic Index & Sound Speed of a Multi-Component Gas Mixture `[State/National Standard | Tier 2]`

A $\mathrm{CO_2}$ gas-laser cavity at $T = 300.0 K$ contains a mixture of $n_1 = 0.700 mol$ Helium ($\mathrm{He}$, monatomic $f_1=3$, $M_1 = 4.0026 g/mol$), $n_2 = 0.200 mol$ Nitrogen ($\mathrm{N_2}$, rigid diatomic $f_2=5$, $M_2 = 28.0134 g/mol$), and $n_3 = 0.100 mol$ Carbon Dioxide ($\mathrm{CO_2}$, using NIST $C_{V,m,3} = 3.480\,R$, $M_3 = 44.0095 g/mol$). Find (a) the mixture molar heat capacities $C_{V,m,\mathrm{mix}}$ and $C_{P,m,\mathrm{mix}}$, (b) the true mixture adiabatic index $\gamma_{\mathrm{mix}}$ (and compare with the wrong mole-weighted average of $\gamma_i$), and (c) the speed of sound $c_{s,\mathrm{mix}}$ at $300.0 K$.
**Solution.**
- **(a) Mole-weighted extensive heat capacity average (NEVER average $\gamma_i$ directly!):**
  With $n_{\mathrm{tot}} = 1.000\,mol$, $x_1 = 0.700, x_2 = 0.200, x_3 = 0.100$:
  
$$
\frac{C_{V,m,\mathrm{mix}}}{R} = 0.700(1.500) + 0.200(2.500) + 0.100(3.480) = 1.050 + 0.500 + 0.348 = \mathbf{1.8980} \implies C_{V,m,\mathrm{mix}} = \mathbf{15.781 J/mol/K}
$$

  
$$
C_{P,m,\mathrm{mix}} = C_{V,m,\mathrm{mix}} + R = 2.8980\,R = \mathbf{24.095 J/mol/K}
$$
- **(b) Mixture adiabatic index $\gamma_{\mathrm{mix}}$:**
  
$$
\gamma_{\mathrm{mix}} = \frac{C_{P,m,\mathrm{mix}}}{C_{V,m,\mathrm{mix}}} = \frac{2.8980}{1.8980} = \mathbf{1.5269}
$$

  (Averaging $\gamma_i$ directly gives $0.70(1.6667) + 0.20(1.4000) + 0.10(1.2874) = 1.5754$, an error of $+3.18\%$!)
- **(c) Mixture molar mass and speed of sound:**
  
$$
M_{\mathrm{mix}} = 0.700(4.0026) + 0.200(28.0134) + 0.100(44.0095) = 12.8055 g/mol = 0.0128055 kg/mol
$$

  
$$
c_{s,\mathrm{mix}} = \sqrt{\frac{\gamma_{\mathrm{mix}} R T}{M_{\mathrm{mix}}}} = \sqrt{\frac{(1.52687)(8.314463)(300.0)}{0.0128055}} = \mathbf{545.36 m/s}
$$

**✓ Verified by:** Direct check $C_{P,m,\mathrm{mix}} - C_{V,m,\mathrm{mix}} = 24.0953 - 15.7809 = 8.3145 J/mol/K = R$ (`check_sec06_09.py::ex06_5`).

## Real-Gas Deviations: Compressibility Factor $Z$ & Van der Waals Equation

Real gases deviate from $PV = nRT$ at high pressures (small intermolecular spacing) and low temperatures (near condensation)  **[S10,S13,S16]**. The deviation is quantified by the dimensionless **compressibility factor $Z$** and the **virial expansion**:

$$
\begin{aligned}

  Z \equiv \frac{PV}{nRT} = \frac{P V_m}{RT} = 1 + \frac{B(T)}{V_m} + \frac{C(T)}{V_m^2} + \cdots \approx 1 + \frac{1}{RT}\left(b - \frac{a}{RT}\right)P
\end{aligned}
$$

- **Moderate Pressure ($Z < 1$, Attractive Regime):** Long-range intermolecular attractions ($a > 0$: London dispersion, dipole–dipole, hydrogen bonding) reduce the impact momentum of molecules hitting container walls, lowering $P < P_{\mathrm{ideal}}$ and making the gas *more compressible* than an ideal gas ($B(T) < 0$ for $T < T_B$).
- **Very High Pressure or High Temperature ($Z > 1$, Repulsive Excluded-Volume Regime):** Short-range hard-core repulsion ($b \approx 4N_A V_{\mathrm{molecule}} > 0$) reduces the free volume available for translation to $V - nb$, raising $P > P_{\mathrm{ideal}}$. For light gases with tiny $a$ ($\mathrm{He}, \mathrm{H_2}, \mathrm{Ne}$), $T_B < 130 K$, so $Z > 1$ at all pressures at room temperature ($300 K$)!

### [FORMULA & DECISION CARD: Van der Waals Equation of State (1873), Critical Parameters & Internal Energy  **[S10,S13,S16]**]

$$
\begin{aligned}

  \boxed{\left(P + \frac{a n^2}{V^2}\right)(V - nb) = nRT} \iff \boxed{P = \frac{RT}{V_m - b} - \frac{a}{V_m^2}}, \qquad Z_{\mathrm{vdW}} = \frac{V_m}{V_m - b} - \frac{a}{RTV_m}
\end{aligned}
$$

- **Critical Point Inflection Identity:** At the critical point $(T_c, P_c, V_{c,m})$, the isotherm has a horizontal inflection point, yielding the exact algebraic relations between $(a, b)$ and $(T_c, P_c, V_{c,m})$:
  
$$
\begin{aligned}

    V_{c,m} = 3b, \quad P_c = \frac{a}{27b^2}, \quad T_c = \frac{8a}{27Rb} \iff \boxed{a = \frac{27 R^2 T_c^2}{64 P_c}, \quad b = \frac{R T_c}{8 P_c}, \quad Z_{c,\mathrm{vdW}} = \frac{P_c V_{c,m}}{R T_c} = \frac{3}{8} = 0.375}
\end{aligned}
$$

  
- **Boyle Temperature ($T_B$, where $B(T_B) = 0$) & Max Joule–Thomson Inversion Temperature ($T_{\mathrm{inv,max}}$):**
  
$$
\begin{aligned}

    T_B = \frac{a}{Rb} = \frac{27}{8}T_c = 3.375\,T_c, \qquad T_{\mathrm{inv,max}} = \frac{2a}{Rb} = 2T_B = \frac{27}{4}T_c = 6.75\,T_c
\end{aligned}
$$
- **Law of Corresponding States:** Defining reduced variables $P_r = P/P_c$, $T_r = T/T_c$, and $V_r = V_m/V_{c,m}$ eliminates $(a,b)$ completely:
  
$$
\begin{aligned}

    \left(P_r + \frac{3}{V_r^2}\right)(3V_r - 1) = 8T_r
\end{aligned}
$$
- **Van der Waals Internal Energy & Free-Expansion Cooling:** Because work must be done against attractive forces $a n^2/V^2$ when separating molecules, the internal energy of a Van der Waals gas depends on volume $V$ as well as $T$:
  
$$
\begin{aligned}

    \boxed{U_{\mathrm{vdW}}(T,V) = nC_{V,m}T - \frac{a n^2}{V}} \implies \Delta T_{\text{free exp }(\Delta U = 0)} = -\frac{an}{C_{V,m}}\left(\frac{1}{V_1} - \frac{1}{V_2}\right) < 0 \quad (\text{always cools!})
\end{aligned}
$$

  

> **[Vector Figure: (a) Real-gas compressibility factor $Z = PV/(nRT)$ at $300 K$ showing attractive depression ($Z<1$) at moderate pressure and excluded-volume rise ($Z>1$) at high pressure. (b) Reduced Van der Waals isotherms Eq. (`eq:06:reduced-vdw`) showing the critical inflection point $(V_r, P_r)=(1,1)$ and Maxwell's equal-area vapor–liquid tie-line for $T_r < 1$  **[S13,S16]**. | Label: `fig:06:vdw-z`]**
> - **Diagram Annotations & Key Elements:** **Title:** **(a) Real-Gas Compressibility $Z(P)$ at $300 K$** • **Title:** **(b) Van der Waals Reduced Isotherms $P_r(V_r)$** • **X-Axis:** Pressure $P$ ($bar$) • **X-Axis:** Reduced molar volume $V_r = V_m/V_{c,m}$ • **Y-Axis:** Compressibility $Z = PV/(nRT)$ • **Y-Axis:** Reduced pressure $P_r = P/P_c$ • **Legend:** $\mathrm{H_2}$ ($T > T_B$) • **Legend:** $\mathrm{N_2}$ • **Legend:** $\mathrm{CH_4}$ • **Legend:** $\mathrm{CO_2}$ • **Legend:** $T_r = 1.15 > 1$ • **Legend:** $T_r = 1.00$ (Critical) • **Legend:** $T_r = 0.88 < 1$ • $Z<1$: Attraction ($a$) • $Z>1$: Core ($b$)

**Table:** Triple Points, Normal Boiling Points, Critical Constants & Van der Waals Parameters ($a, b$)  **[S09,S10]**.

| **Gas** | $T_{\mathrm{tp}}$ | $P_{\mathrm{tp}}$ | $T_b$ ($1 atm$) | $T_c$ | $P_c$ | $\rho_c$ | $Z_{c,\mathrm{exp}}$ | $a_{\mathrm{crit}}$ | $b_{\mathrm{crit}}$ | $a_{\mathrm{CRC}}$ | $b_{\mathrm{CRC}}$ | $T_{B,\mathrm{vdW}}$ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | ($K$) | ($kPa$) | ($K$) | ($K$) | ($kPa$) | ($kg/m^3$) |  | ($Pa m^6/mol^2$) | ($10^{-5}m^3/mol$) | ($L^2 bar/mol^2$) | ($L/mol$) | ($K$) |
| $\mathrm{He}$ | $2.18$ | $5.04$ | $4.22$ | $5.20$ | $228.3$ | $69.58$ | $0.304$ | $0.0034$ | $2.365$ | $0.0346$ | $0.0238$ | $17.5$ |
| $\mathrm{Ne}$ | $24.56$ | $43.36$ | $27.10$ | $44.40$ | $2661.6$ | $486.00$ | $0.299$ | $0.0216$ | $1.734$ | $0.2135$ | $0.0171$ | $149.9$ |
| $\mathrm{Ar}$ | $83.81$ | $68.89$ | $87.30$ | $150.69$ | $4863.0$ | $535.60$ | $0.290$ | $0.1362$ | $3.220$ | $1.3550$ | $0.0320$ | $508.6$ |
| $\mathrm{H_2}$ | $13.96$ | $7.36$ | $20.37$ | $33.15$ | $1296.4$ | $31.26$ | $0.303$ | $0.0247$ | $2.657$ | $0.2476$ | $0.0266$ | $111.9$ |
| $\mathrm{N_2}$ | $63.15$ | $12.52$ | $77.36$ | $126.19$ | $3395.8$ | $313.30$ | $0.289$ | $0.1368$ | $3.862$ | $1.3700$ | $0.0387$ | $425.9$ |
| $\mathrm{O_2}$ | $54.36$ | $0.15$ | $90.19$ | $154.58$ | $5043.0$ | $436.10$ | $0.288$ | $0.1382$ | $3.186$ | $1.3820$ | $0.0319$ | $521.7$ |
| $\mathrm{Air}$ | $59.75$ | $5.27$ | $78.90$ | $132.53$ | $3786.0$ | $342.68$ | $0.289$ | $0.1353$ | $3.638$ | $1.3580$ | $0.0364$ | $447.3$ |
| $\mathrm{CO}$ | $68.16$ | $15.54$ | $81.64$ | $132.86$ | $3494.0$ | $303.90$ | $0.292$ | $0.1473$ | $3.952$ | $1.4720$ | $0.0395$ | $448.4$ |
| $\mathrm{CO_2}$ | $216.59$ | $517.96$ | $194.69^*$ | $304.13$ | $7377.3$ | $467.60$ | $0.275$ | $0.3656$ | $4.285$ | $3.6580$ | $0.0429$ | $1026.4$ |
| $\mathrm{H_2O}$ | $273.16$ | $0.6117$ | $373.12$ | $647.10$ | $22064.0$ | $322.00$ | $0.229$ | $0.5535$ | $3.048$ | $5.5370$ | $0.0305$ | $2184.0$ |
| $\mathrm{CH_4}$ | $90.69$ | $11.70$ | $111.67$ | $190.56$ | $4599.2$ | $162.66$ | $0.286$ | $0.2303$ | $4.306$ | $2.3000$ | $0.0430$ | $643.1$ |
| $\mathrm{NH_3}$ | $195.49$ | $6.05$ | $239.83$ | $405.56$ | $11363.4$ | $233.25$ | $0.246$ | $0.4221$ | $3.709$ | $4.2250$ | $0.0371$ | $1368.8$ |
| $\mathrm{SO_2}$ | $197.70$ | $1.67$ | $263.14$ | $430.64$ | $7886.6$ | $517.50$ | $0.273$ | $0.6858$ | $5.675$ | $6.8650$ | $0.0568$ | $1453.4$ |
| $\mathrm{SF_6}$ | $223.56$ | $231.42$ | $204.90^*$ | $318.72$ | $3755.0$ | $742.30$ | $0.279$ | $0.7890$ | $8.822$ | $7.8570$ | $0.0879$ | $1075.7$ |
| $\mathrm{R134a}$ | $169.85$ | $0.39$ | $247.08$ | $374.21$ | $4059.3$ | $511.90$ | $0.260$ | $1.0061$ | $9.581$ | $10.090$ | $0.0957$ | $1263.0$ |

{$^*$At $1 atm$, $\mathrm{CO_2}$ and $\mathrm{SF_6}$ sublime directly from solid to gas ($P_{\mathrm{tp}} > 101.325 kPa$). Note unit conversion: $a[L^2 bar/mol^2] = 10\,a[Pa m^6/mol^2]$; $1\,L^2 atm/mol^2 = 1.01325\,L^2 bar/mol^2$.}

### Worked Example — Van der Waals Pressure, Compressibility $Z$ & Free-Expansion Cooling of $\mathrm{CO_2}$ `[National/Invitational Standard | Tier 3]`

Consider $n = 10.00 mol$ of carbon dioxide ($\mathrm{CO_2}$, $a = 0.3658 Pa m^6/mol^2 = 3.658 L^2 bar/mol^2$, $b = 4.286×10^{-5} m^3/mol = 0.04286 L/mol$, $C_{V,m} = 28.94 J/mol/K$) compressed into a rigid vessel of volume $V_1 = 5.000 L$ ($5.000×10^{-3} m^3$) at $T_1 = 350.0 K$. (a) Compare the ideal-gas pressure $P_{\mathrm{ideal}}$ with the Van der Waals pressure $P_{\mathrm{vdW}}$ and find $Z_{\mathrm{vdW}}$. (b) If a partition ruptures and the gas undergoes an adiabatic free expansion into an evacuated chamber to final total volume $V_2 = 50.00 L$, calculate the temperature drop $\Delta T$ from Eq. (`eq:06:vdw-u`).
**Solution.**
- **(a) Ideal vs. Van der Waals pressure at $V_m = V_1/n = 0.5000 L/mol = 5.000×10^{-4} m^3/mol$:**
  
$$
P_{\mathrm{ideal}} = \frac{RT_1}{V_m} = \frac{(8.314463)(350.0)}{5.000\times 10^{-4}} = 5.8201×10^{6} Pa = \mathbf{58.201 bar}
$$

  
$$
P_{\mathrm{vdW}} = \frac{RT_1}{V_m - b} - \frac{a}{V_m^2} = \frac{(8.314463)(350.0)}{(5.000 - 0.4286)\times 10^{-4}} - \frac{0.3658}{(5.000\times 10^{-4})^2} = 6.3656\times 10^6 - 1.4632\times 10^6 = 4.9024×10^{6} Pa = \mathbf{49.024 bar}
$$

  
$$
Z_{\mathrm{vdW}} = \frac{P_{\mathrm{vdW}}}{P_{\mathrm{ideal}}} = \frac{49.024}{58.201} = \mathbf{0.8423} < 1 \quad (\text{attractions reduce } P \text{ by } 9.18 bar \text{ or } 15.8\%!)
$$
- **(b) Adiabatic free-expansion cooling ($Q = 0, W_{\mathrm{by}} = 0 \implies \Delta U_{\mathrm{vdW}} = 0$):**
  
$$
\Delta T = -\frac{an}{C_{V,m}}\left(\frac{1}{V_1} - \frac{1}{V_2}\right) = -\frac{(0.3658)(10.00)}{28.94}\left(\frac{1}{5.000\times 10^{-3}} - \frac{1}{5.000\times 10^{-2}}\right) = -(0.12640)(200.0 - 20.0) = \mathbf{-22.75 K}
$$

  Thus the $\mathrm{CO_2}$ cools to $T_2 = 350.0 - 22.75 = \mathbf{327.25 K}$ (whereas an ideal gas would have $\Delta T = 0$).

**✓ Verified by:** Total internal energy conservation: $\Delta U_T = nC_{V,m}\Delta T = -6584.4 J$ balances potential energy gain $\Delta U_V = an^2(1/V_1 - 1/V_2) = +6584.4 J$ (`check_sec06_09.py::ex06_6`).

## Multi-Compartment Piston-Cylinder Equilibrium & Coupled Gas Mechanics

Multi-compartment piston problems (`2018 MIT E3 Q24`, `2019 GGSO E4`) are premier tiebreakers at invitationals and Nationals  **[S25,S27,S28]**. Solving them without calculus requires matching the mechanical and thermal constraints of the dividing piston.

### [FORMULA & DECISION CARD: Master Ledger for Coupled Piston-Cylinder Systems  **[S13,S27,S33]**]
- **Case A — Free, Frictionless, *Thermal-Conducting* (Diathermal) Piston Inside an Insulated Rigid Cylinder of Total Volume $V_{\mathrm{tot}} = V_1 + V_2$ (`2018 MIT E3 Q24`):**
- *Equilibrium conditions:* Thermal equilibrium enforces $T_{1f} = T_{2f} = T_f$; mechanical equilibrium enforces $P_{1f} = P_{2f} = P_f$.
- *Total internal energy conservation ($Q_{\mathrm{tot}}=0, W_{\mathrm{tot}}=0$):*
    
$$
\begin{aligned}

      \Delta U_1 + \Delta U_2 = n_1 C_{V,m,1}(T_f - T_{1i}) + n_2 C_{V,m,2}(T_f - T_{2i}) = 0 \implies \boxed{T_f = \frac{n_1 C_{V,m,1} T_{1i} + n_2 C_{V,m,2} T_{2i}}{n_1 C_{V,m,1} + n_2 C_{V,m,2}}}
\end{aligned}
$$

    
- *Final volumes and pressure:* Since $P_f = n_1 R T_f / V_{1f} = n_2 R T_f / V_{2f}$, the volume ratio equals the mole ratio:
    
$$
\begin{aligned}

      \boxed{V_{1f} = \frac{n_1}{n_1 + n_2}V_{\mathrm{tot}}, \qquad V_{2f} = \frac{n_2}{n_1 + n_2}V_{\mathrm{tot}}, \qquad P_f = \frac{(n_1 + n_2)R T_f}{V_{\mathrm{tot}}}}
\end{aligned}
$$
- *Equal-$\gamma$ Constant-Pressure Theorem:* Using $n_k C_{V,m,k} T_{ki} = \frac{P_{ki}V_{ki}}{\gamma_k - 1}$, if both gases have the **same adiabatic index** ($\gamma_1 = \gamma_2 = \gamma$) and start in mechanical equilibrium ($P_{1i} = P_{2i} = P_i$), then:
    
$$
\begin{aligned}

      U_{\mathrm{tot}} = \frac{P_{1i}V_{1i} + P_{2i}V_{2i}}{\gamma - 1} = \frac{P_i V_{\mathrm{tot}}}{\gamma - 1} = \frac{P_f V_{\mathrm{tot}}}{\gamma - 1} \implies \boxed{P_f = P_i \quad (\text{pressure never changes!})}
\end{aligned}
$$
- **Case B — Free, Frictionless, *Adiabatic* (Insulating) Piston with Heat $Q_{\mathrm{in}}$ Added to Side 1:**
  Side 2 undergoes a **reversible adiabatic compression** ($Q_2 = 0$), while mechanical equilibrium enforces $P_{1f} = P_{2f} = P_f$:
  
$$
\begin{aligned}

    P_{2i}V_{2i}^{\gamma_2} = P_f V_{2f}^{\gamma_2}, \qquad T_{2f} = T_{2i}\left(\frac{V_{2i}}{V_{2f}}\right)^{\gamma_2 - 1}, \qquad V_{1f} = V_{\mathrm{tot}} - V_{2f}, \qquad Q_{\mathrm{in}} = \Delta U_1 + \Delta U_2 = \frac{P_f V_{1f} - P_{1i}V_{1i}}{\gamma_1 - 1} + \frac{P_f V_{2f} - P_{2i}V_{2i}}{\gamma_2 - 1}
\end{aligned}
$$
- **Case C — Vertical Heavy Piston (Mass $m_p$, Area $A$) and Linear Spring (Stiffness $k_{\mathrm{sp}}$):**
  
$$
\begin{aligned}

    P_{\mathrm{gas}}(V) = P_{\mathrm{atm}} + \frac{m_p g_n}{A} + \frac{k_{\mathrm{sp}}(V - V_0)}{A^2} \quad (\text{straight line on } P\text{--}V \text{ plot} \implies W_{\mathrm{by}} = \frac{P_1 + P_2}{2}(V_2 - V_1))
\end{aligned}
$$

  

### Worked Example — Two-Compartment Cylinder with Conducting Piston: Helium vs. Nitrogen `[2018 MIT E3 Q24 Archetype | Tier 3]`

A rigid, perfectly insulated horizontal cylinder of total internal volume $V_{\mathrm{tot}} = 30.00 L$ is divided into two compartments by a thin, frictionless, thermally conducting (diathermal) piston. Initially, the piston is pinned in place: Compartment 1 ($V_{1i} = 10.00 L$) holds $n_1 = 2.000 mol$ of monatomic Helium ($\gamma_1 = 5/3$, $C_{V,m,1} = \frac{3}{2}R$) at $T_{1i} = 600.0 K$, while Compartment 2 ($V_{2i} = 20.00 L$) holds $n_2 = 3.000 mol$ of diatomic Nitrogen ($\gamma_2 = 7/5$, $C_{V,m,2} = \frac{5}{2}R$) at $T_{2i} = 300.0 K$. The pin is released and the system reaches full mechanical and thermal equilibrium. Find (a) the initial pressures $P_{1i}$ and $P_{2i}$, (b) the final temperature $T_f$, (c) the final compartment volumes $V_{1f}, V_{2f}$ and final pressure $P_f$, and (d) the work done and heat transferred between the two compartments.
**Solution.**
- **(a) Initial compartment pressures ($R = 8.314463 L kPa/mol/K$):**
  
$$
P_{1i} = \frac{n_1 R T_{1i}}{V_{1i}} = \frac{(2.000)(8.314463)(600.0)}{10.00} = \mathbf{997.74 kPa}, \qquad P_{2i} = \frac{n_2 R T_{2i}}{V_{2i}} = \frac{(3.000)(8.314463)(300.0)}{20.00} = \mathbf{374.15 kPa}
$$
- **(b) Final equilibrium temperature $T_f$ from Eq. (`eq:06:piston-diathermal-T`):**
  With $n_1 C_{V,m,1} = 2.000(1.5R) = 3.000\,R$ and $n_2 C_{V,m,2} = 3.000(2.5R) = 7.500\,R$:
  
$$
T_f = \frac{(3.000\,R)(600.0) + (7.500\,R)(300.0)}{3.000\,R + 7.500\,R} = \frac{1800.0 + 2250.0}{10.500} = \frac{4050.0}{10.500} = \mathbf{385.714 K}
$$
- **(c) Final volumes and final pressure $P_f$ from Eq. (`eq:06:piston-diathermal-V`):**
  
$$
V_{1f} = \frac{2.000}{2.000 + 3.000}(30.00 L) = \mathbf{12.00 L}, \qquad V_{2f} = \frac{3.000}{5.000}(30.00 L) = \mathbf{18.00 L}
$$

  
$$
P_f = \frac{(n_1 + n_2)R T_f}{V_{\mathrm{tot}}} = \frac{(5.000)(8.314463)(385.714)}{30.00} = \mathbf{534.50 kPa}
$$
- **(d) Internal energy transfer ($\Delta U_1 = -\Delta U_2$):**
  
$$
\Delta U_1 = n_1 C_{V,m,1}(T_f - T_{1i}) = (3.000)(8.314463)(385.714 - 600.0) = \mathbf{-5.3450 kJ}, \qquad \Delta U_2 = +\mathbf{5.3450 kJ}
$$

  Helium transfers $5.345 kJ$ of total energy (combined expansion work + conducted heat) to the Nitrogen compartment.

**✓ Verified by:** Pressure balance check: $P_{1f} = n_1 R T_f / V_{1f} = 2(8.314463)(385.714)/12.00 = 534.50 kPa = P_{2f}$ (`check_sec06_09.py::ex06_7`).

### [TRAP & DIAGNOSTIC: Top 6 Gas-Law & Kinetic-Theory Exam Traps (§6 Diagnostic Matrix)]

| **Wrong move / Symptom** | **What it produces / Why it fails** | **5-second diagnostic & fix** |
| --- | --- | --- |
| Using $M = 28.0 g/mol$ in $v_{\mathrm{rms}} = \sqrt{3RT/M}$ | Off by a factor of $\sqrt{1000} = 31.62$ (gives $16.3 m/s$ instead of $517 m/s$!). | Always convert $M$ to $kg/mol$ ($\mathrm{N_2}: 0.02801 kg/mol$); room-$T$ gas speeds are $250–1900 m/s$. |
| Substituting $P_{\mathrm{gauge}}$ into $PV = nRT$ | Underestimates $P_{\mathrm{abs}}$ by $101.325 kPa$, corrupting $n, V, T$ by $50\text{--}100\%$. | Add $P_{\mathrm{atm}} = 101.325 kPa$ ($14.7 psi$) whenever the problem states “gauge” or “manometer height.” |
| Forgetting $P_{\mathrm{sat,H_2O}}(T)$ in eudiometry | Overestimates dry gas moles by $2\text{--}5\%$ at room $T$ (and $>10\%$ above $45 °C$). | Subtract $P_{\mathrm{sat,H_2O}}(T)$ (Table `tab:06:vdw-constants` / App. A) and any liquid-column $\rho g h$ before using $PV=nRT$. |
| Averaging $\gamma_{\mathrm{mix}} = \sum x_i \gamma_i$ for a mixture | Violates energy additivity because $\gamma = C_P/C_V$ is a nonlinear ratio. | Compute $C_{V,m,\mathrm{mix}} = \sum x_i C_{V,m,i}$ and $C_{P,m,\mathrm{mix}} = C_{V,m,\mathrm{mix}} + R$ first, then take the ratio. |
| Confusing $K_{\mathrm{trans,avg}} = \frac{3}{2}k_B T$ with $U = \frac{f}{2}nRT$ | Gives $\frac{5}{2}k_B T$ for the *translational* kinetic energy of $\mathrm{N_2}$ instead of $\frac{3}{2}k_B T$. | Translational kinetic energy is **always** $\frac{3}{2}k_B T$ per molecule regardless of whether the gas is monatomic or polyatomic! |
| Inverting Graham's law for *mass* effusion rate | Predicts $\dot{m}_{\mathrm{He}} > \dot{m}_{\mathrm{O_2}}$ instead of $\dot{m}_1/\dot{m}_2 = \sqrt{M_1/M_2}$. | Molar rate $\dot{n} \propto 1/\sqrt{M}$, so mass rate $\dot{m} = M\dot{n} \propto \sqrt{M}$ (heavier gas has higher mass flux!). |

### [2027 HEAT-COLLECTOR DEVICE & LAB: 2027 Collector Air-Pocket Thermal Expansion, Buoyancy & Dead-Air Mean Free Path]

In the 2027 Heat-Lamp Collector (§`sec:15`), trapped air pockets heated from $20 °C$ ($293.15 K$) to $65 °C$ ($338.15 K$) possess volumetric expansion coefficient $\beta_{V,\mathrm{air}} = 1/T \approx 3.17×10^{-3} /K$, decreasing air density by $\Delta\rho/\rho \approx -13.3\%$ (from $1.204 kg/m^3$ to $1.044 kg/m^3$). If an insulation cavity is sealed hermetically, constant-volume heating raises internal pressure by $\Delta P = P_{\mathrm{atm}}(\Delta T/T_1) \approx +15.6 kPa$ ($2.26 psi$), which can bow or pop off an unvented BoPET glazing lid (`Clarification #5`)! Always leave a pinhole pressure-equalization vent in structural air baffles while keeping dead-air layer thickness $\delta \le 11 mm$ to suppress Rayleigh–B\'enard buoyancy plumes (§`sec:11`).

—
**See also:** Quick Sheet `QS-05` (§`sec:01.5`); First Law & Polytropic Processes (§`sec:07`); Ideal-Gas Entropy & Mixing (§`sec:08`); Gas Power Cycles (§`sec:09`); Dead-Air Convection (§`sec:11`); Master Gas Tables (§`app:A`).
