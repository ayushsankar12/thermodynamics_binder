<!-- Source: src/sec04.tex | Tab: Tab 3: CAL/PHASE | Target: 12 pp -->
# §4: Heat Capacity, Specific/Molar Heat, Dulong–Petit & Multi-Body Calorimetry {#sec:04}

> **[SCOPE: REQUIRED | Rule 5.c.i–ii (Specific Heat, Heat Capacity & Calorimetry), 5.c.vi (Enthalpy & Phase Energy), 5.d.iv (Algebra/Geometry Only)]**

### [FORMULA & DECISION CARD: §4 Core Formula Card — Heat Capacity, Dulong–Petit & Multi-Body Calorimetry]

| **Formula** | **Variables (SI units)** | **Flags** | **Use when** |
| --- | --- | --- | --- |
| Sensible Heat & Heat Capacity | $\displaystyle Q = m c \Delta T = n C_m \Delta T = C \Delta T, \qquad C = mc = nC_m, \qquad C_m = M c$ | $J$ (`eq:04:sensible`) |  |
| Water Equivalent of Calorimeter | $\displaystyle m_{\mathrm{eq}} = \frac{C_{\mathrm{cal}}}{c_w}, \qquad Q_{\mathrm{cal}} = C_{\mathrm{cal}}\Delta T = m_{\mathrm{eq}} c_w \Delta T$ | $kg$ (`eq:04:watereq`) |  |
| Dulong–Petit Classical Solid Limit | $\displaystyle C_{V,m} \approx 3R = 24.943 J/mol/K, \qquad c \approx \frac{3R}{M}$ | $T \gtrsim \Theta_D$ (`eq:04:dulongpetit`) |  |
| Debye Low-$T$ Phonon $T^3$ Law | $\displaystyle C_{V,m}(T) = \frac{12\pi^4}{5} R \left(\frac{T}{\Theta_D}\right)^3 \approx 233.78\,R\left(\frac{T}{\Theta_D}\right)^3$ | $T \ll \Theta_D$ (`eq:04:debye`) |  |
| $N$-Body Sensible Equilibrium $T_f$ | $\displaystyle \sum_{i=1}^N Q_i = 0 \implies T_f = \frac{\sum_{i=1}^N m_i c_i T_i + C_{\mathrm{cal}} T_{\mathrm{cal}}}{\sum_{i=1}^N m_i c_i + C_{\mathrm{cal}}}$ | No phase change (`eq:04:nbody`) |  |
| Calorimeter Calibration ($C_{\mathrm{cal}}$) | $\displaystyle C_{\mathrm{cal}} = m_h c_w \frac{T_h - T_f}{T_f - T_c} - m_c c_w$ | Warm + cold water (`eq:04:ccal`) |  |
| Latent Heat of Fusion / Vaporization | $\displaystyle Q_{\mathrm{fus}} = \pm m L_f, \qquad Q_{\mathrm{vap}} = \pm m L_v, \qquad Q_{\mathrm{sub}} = \pm m L_{\mathrm{sub}}$ | Isothermal plateau (§`sec:04.3`) |  |
| Electrical Immersion Calorimetry | $\displaystyle E_{\mathrm{elec}} = V I t = I^2 R t = \frac{V^2}{R}t = (m c + C_{\mathrm{cal}})\Delta T + Q_{\mathrm{leak}}$ | $J$ (`eq:04:elec`) |  |
| Callendar–Barnes Continuous Flow | $\displaystyle V I = \dot{m} c_p (T_{\mathrm{out}} - T_{\mathrm{in}}) + \dot{Q}_{\mathrm{loss}}$ | Steady flow (`eq:04:flow`) |  |
| Regnault–Pfaundler Drift Correction | $\displaystyle \Delta T_{\mathrm{corr}} = (T_{\max} - T_0) - \frac{r_{\mathrm{pre}} + r_{\mathrm{post}}}{2}\,(t_{\max} - t_0)$ | Cooling correction (`eq:04:drift`) |  |
| Isobaric vs. Isochoric Calorimetry | $\displaystyle q_P = \Delta H, \qquad q_V = \Delta U = -C_{\mathrm{bomb}}\Delta T, \qquad \Delta H_{\mathrm{rxn}} = \Delta U_{\mathrm{rxn}} + \Delta n_{\mathrm{gas}} R T$ | $J/mol$ (`eq:04:bomb`) |  |

## Heat Capacity, Specific Heat, Molar Heat & Sourced Property Tables

When heat $Q$ enters or leaves a single-phase substance of mass $m$ and molar amount $n = m/M$ without triggering a phase transition or chemical reaction, its temperature changes by $\Delta T = T_f - T_i$. The proportionality defines three related capacity quantities  **[S04,S05]**:

$$
\begin{aligned}

  Q = C\,\Delta T = m c\,\Delta T = n C_m\,\Delta T, \qquad
  c = \frac{C}{m} = \frac{Q}{m\Delta T} \;\left[J/kg/K\right], \qquad
  C_m = M c = \frac{Q}{n\Delta T} \;\left[J/mol/K\right],
\end{aligned}
$$

where $C$ ($J/K$) is the **total (extensive) heat capacity** of the object, $c$ ($J/kg/K$ or $J/g/K$) is the **specific (mass-basis) heat capacity**, $C_m$ ($J/mol/K$) is the **molar heat capacity**, and $M$ ($kg/mol$) is the molar mass. In transient conduction and thermal-mass design (§`sec:13`), the **volumetric heat capacity** $\rho c_p$ ($J/m^3/K$) measures energy stored per unit volume.
- **Constant-Pressure ($c_p$) vs. Constant-Volume ($c_v$) Specific Heat:** By the First Law (§`sec:07.1`), heating at constant volume ($\Delta V = 0 \implies W_{\mathrm{by}} = 0$) gives $Q_V = \Delta U = m c_v \Delta T$, whereas heating at constant pressure gives $Q_P = \Delta U + P\Delta V = \Delta H = m c_p \Delta T$. Exact thermodynamics relates their molar difference to the volumetric expansion coefficient $\beta_V$ and isothermal compressibility $\kappa_T$:
  
$$
\begin{aligned}

    C_{P,m} - C_{V,m} = \frac{T V_m \beta_V^2}{\kappa_T}.
\end{aligned}
$$

  For dense solids and liquids near $298 K$, $\beta_V$ is small ($\sim 10^{-5}\text{--}10^{-4}\,/K$), so $C_{P,m} - C_{V,m}$ is only $1\%\text{--}5\%$ of $C_{P,m}$ (e.g., for copper at $298 K$, $C_{P,m} = 24.44 J/mol/K$ vs. $C_{V,m} = 23.7 J/mol/K$) and standard tables report $c \approx c_p$. For an ideal gas ($\beta_V = 1/T$, $\kappa_T = 1/P$), (`eq:04:cpcvsolid`) yields Mayer's exact relation $C_{P,m} - C_{V,m} = R$ (§`sec:06`).
- **Water Equivalent ($m_{\mathrm{eq}}$) & Fast Unit Conversions:** Older calorimetry problems express a vessel's heat capacity $C_{\mathrm{cal}}$ ($J/K$) as its **water equivalent**—the mass of liquid water having the same heat capacity:
  
$$
\begin{aligned}

    m_{\mathrm{eq}} = \frac{C_{\mathrm{cal}}}{c_w} \implies C_{\mathrm{cal}} = m_{\mathrm{eq}} c_w.
\end{aligned}
$$

  Because both the calorie and the BTU were historically defined using liquid water, specific heat has a **1-to-1 numerical identity** between CGS calories and Imperial units:
  
$$
\begin{aligned}

    1\,\mathrm{cal/(g\cdot°C)} = 1\,\mathrm{kcal/(kg\cdotK)} = 1\,\mathrm{BTU/(lb_m\cdot{}^\circ\mathrm{F})} = 4.184 J/g/K = 4184 J/kg/K.
\end{aligned}
$$

### [2027 OFFICIAL RULE / CLARIFICATION: Steam Specific Heat Reconciliation Across NIST, OpenStax & Ideal-Gas Limit  **[S04,S14,S16]**]

Water vapor specific heat $c_{p,\mathrm{steam}}$ appears with **three different values** across standard references depending on temperature and pressure:
- **NIST Real Saturated Steam at $100.0 °C, 101.325 kPa$  **[S16]**:** $c_p = \mathbf{2080.0 J/kg/K}$ ($C_{p,m} = 37.47 J/mol/K$), $c_v = 1555.6 J/kg/K$, $\gamma = 1.337$. Hydrogen-bond clustering near saturation elevates $c_p$ by $\sim 11\%$ above the ideal-gas value.
- **OpenStax *University Physics Vol. 2* Table 1.3  **[S04]**:** $c_p = \mathbf{2020 J/kg/K}$ ($0.482\,\mathrm{kcal/(kg\cdot°C)}$) and $c_v = 1520 J/kg/K$, representing slightly superheated steam at $1 atm$ averaged over $100–150 °C$ (Lienhard 6e gives $2034 J/kg/K$ at $110 °C$  **[S14]**).
- **Dilute Ideal-Gas Limit at $298.15 K$ ($f = 3\text{ trans} + 3\text{ rot} = 6$)  **[S16]**:** $C_{p,m}^\circ = 33.58 J/mol/K \implies c_p = \mathbf{1864 J/kg/K}$ (exact $4R/M = 1846 J/kg/K$), $c_v = 1403 J/kg/K$, $\gamma = 1.329$.

**Competition Rule:** If a problem does not give $c_{\mathrm{steam}}$, write down both the textbook value $2020 J/kg/K$ (or $2010 J/kg/K$) and the NIST saturation value $2080 J/kg/K$; they differ by only $3\%$ on the sensible superheat step and negligible amounts compared to $L_v = 2256.4 kJ/kg$.

**Table:** Sourced thermophysical and calorimetry properties of 28 common solids and liquids at $20 °C$–$25 °C$, $1 atm$, cross-reconciling Lienhard 6e  **[S14]**, NIST WebBook  **[S16,S17]**, and OpenStax UP2  **[S04]**.

| **Substance** | **$\rho$ ($kg/m^3$)** | **$c_p$ [NIST/L6e]** | **$c_p$ [OS UP2]** | **$C_m$ ($J/mol/K$)** | **$T_m$ ($°C$)** | **$L_f$ ($kJ/kg$)** | **$T_b$ ($°C$)** | **$L_v$ ($kJ/kg$) / Notes** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Metals & Alloys** ($c_p$ in $J/kg/K$; Dulong–Petit benchmark $3R = 24.94 J/mol/K$) |  |  |  |  |  |  |  |  |
| Aluminum ($\mathrm{Al}$, $M=26.98$) | 2700 | **897** | 900 | $24.20\;(2.91R)$ | 660.3 | 397 | 2519 | $L_v = 10500$; $\Theta_D = 428 K$ |
| Beryllium ($\mathrm{Be}$, $M=9.012$) | 1850 | **1825** | 1825 | $16.44\;(1.98R)$ | 1287 | 876 | 2469 | Quantum freeze-out ($\Theta_D = 1440 K$) |
| Brass ($70\mathrm{Cu}$–$30\mathrm{Zn}$) | 8530 | **380** | 380 | $\approx 24.4$ | 930 | 168 | — | Standard calorimeter weight alloy |
| Copper ($\mathrm{Cu}$, $M=63.55$) | 8960 | **385** | 390 | $24.44\;(2.94R)$ | 1084.6 | 207 | 2562 | $L_v = 4730$; $\Theta_D = 343 K$ |
| Gold ($\mathrm{Au}$, $M=196.97$) | 19300 | **129** | 129 | $25.42\;(3.06R)$ | 1064.2 | 63.7 | 2856 | $L_v = 1645$; $\Theta_D = 165 K$ |
| Iron ($\mathrm{Fe}$, $M=55.845$) | 7874 | **449** | 450 | $25.10\;(3.02R)$ | 1538 | 247 | 2861 | $L_v = 6090$; $\Theta_D = 470 K$ |
| Steel (Carbon, $1\%\,\mathrm{C}$) | 7850 | **470** | 452 | $\approx 26.2$ | 1450 | 250 | — | Stainless 304: $c_p = 500 J/kg/K$ |
| Lead ($\mathrm{Pb}$, $M=207.2$) | 11340 | **129** | 128 | $26.65\;(3.21R)$ | 327.5 | 23.0 | 1749 | $L_v = 859$; $\Theta_D = 105 K$ |
| Nickel ($\mathrm{Ni}$, $M=58.69$) | 8908 | **444** | 444 | $26.07\;(3.13R)$ | 1455 | 298 | 2913 | Ferromagnetic contribution near $T_C$ |
| Platinum ($\mathrm{Pt}$, $M=195.08$) | 21450 | **133** | 133 | $25.86\;(3.11R)$ | 1768.3 | 113.6 | 3825 | RTD sensor standard (§`sec:03.2`) |
| Silver ($\mathrm{Ag}$, $M=107.87$) | 10490 | **235** | 235 | $25.35\;(3.05R)$ | 961.8 | 104.8 | 2162 | $L_v = 2360$; $\Theta_D = 225 K$ |
| Tin ($\mathrm{Sn}$, $M=118.71$) | 7310 | **228** | 227 | $27.11\;(3.26R)$ | 231.9 | 59.2 | 2602 | White $\beta$-$\mathrm{Sn}$; eutectic solder component |
| Titanium ($\mathrm{Ti}$, $M=47.87$) | 4506 | **523** | 522 | $25.06\;(3.01R)$ | 1668 | 295 | 3287 | Low-$k$ structural metal ($k = 21.9 W/m/K$) |
| Tungsten ($\mathrm{W}$, $M=183.84$) | 19250 | **132** | 134 | $24.27\;(2.92R)$ | 3422 | 192 | 5555 | Highest $T_m$ of any pure metal |
| Zinc ($\mathrm{Zn}$, $M=65.38$) | 7140 | **388** | 390 | $25.39\;(3.05R)$ | 419.5 | 112 | 907 | $L_v = 1760$; $\Theta_D = 327 K$ |
| **Nonmetallic Solids, Minerals, Ice & Polymers** ($c_p$ in $J/kg/K$) |  |  |  |  |  |  |  |  |
| Diamond ($\mathrm{C}$, $M=12.011$) | 3515 | **509** | 509 | $6.12\;(0.74R)$ | 3550 | — | — | Strongest quantum freeze-out ($\Theta_D = 2230 K$) |
| Silicon ($\mathrm{Si}$, $M=28.085$) | 2329 | **705** | 705 | $19.79\;(2.38R)$ | 1414 | 1787 | 3265 | $\Theta_D = 645 K$; high latent fusion heat |
| Glass (Crown / Soda-Lime) | 2500 | **840** | 840 | — | $\sim 1400$ | — | — | Pyrex borosilicate: $c_p = 753 J/kg/K$ |
| Quartz Sand / Granite ($\mathrm{SiO_2}$) | 2650 | **790** | 840 | $44.4\;\text{(3-atom)}$ | 1670 | 142 | 2230 | Dry sand bulk $\rho \approx 1600 kg/m^3$, $c_p \approx 800 J/kg/K$ |
| Concrete / Brick (Dry) | 2300 | **880** | 840 | — | — | — | — | Gypsum drywall: $c_p = 1090 J/kg/K$ |
| Ice Ih ($\mathrm{H_2O(s)}$ at $0 °C$) | 916.7 | **2093** | 2090 | $37.7\;\text{(at }0 °C\text{)}$ | 0.00 | **333.55** | — | At $-20 °C$: $c_p = 1960 J/kg/K$; OS $L_f = 334 kJ/kg$ |
| Polymers (`#1 PET / #5 PP`) | 1380/905 | **1200/1920** | — | — | 255/165 | — | — | Wood (oak/pine): $c_p \approx 1700 J/kg/K$ |
| **Calorimetry Liquids at $20 °C$–$25 °C$, $1 atm$** ($c_p$ in $J/kg/K$) |  |  |  |  |  |  |  |  |
| Water ($\mathrm{H_2O(\ell)}$, $M=18.015$) | 998.2 | **4184** | 4186 | $75.33\;(9.06R)$ | 0.00 | **333.55** | 100.0 | $L_v(100 °C) = \mathbf{2256.4}$ (OS: $2256$); $L_v(25 °C) = 2441.7$ |
| Seawater ($3.5\%$ salinity) | 1025 | **3993** | 3990 | — | $-1.91$ | 315 | 100.6 | Colligative depression $\Delta T_f = -1.91 °C$ |
| Ethanol ($\mathrm{C_2H_5OH}$, $M=46.07$) | 789 | **2440** | 2430 | $112.4$ | $-114.1$ | 108 | 78.24 | $L_v = 846 kJ/kg$ (OS: $854$) |
| Methanol ($\mathrm{CH_3OH}$, $M=32.04$) | 792 | **2530** | 2549 | $81.1$ | $-97.6$ | 99.2 | 64.7 | $L_v = 1100 kJ/kg$ |
| Glycerol ($\mathrm{C_3H_8O_3}$, $M=92.09$) | 1261 | **2427** | 2410 | $223.5$ | 17.8 | 200.6 | 290 | High viscosity ($\mu = 1.41 Pa s$ at $20 °C$) |
| Ethylene Glycol ($\mathrm{C_2H_6O_2}$) | 1113 | **2415** | 2386 | $149.9$ | $-12.9$ | 181 | 197.3 | $50/50$ water antifreeze: $c_p \approx 3350 J/kg/K$, $T_f \approx -37 °C$ |
| Mercury ($\mathrm{Hg(\ell)}$, $M=200.59$) | 13546 | **139.5** | 139 | $27.98\;(3.37R)$ | $-38.83$ | 11.4 | 356.7 | $L_v = 295 kJ/kg$; liquid metal at $298 K$ |
| Vegetable / Olive Oil | 918 | **1970** | 1970 | — | $\sim -6$ | — | $\sim 300$ | Kerosene / Mineral oil: $c_p \approx 2010 J/kg/K$ |

**Table:** Temperature-dependent thermophysical properties of Ice Ih ($-50 °C$ to $0 °C$), Liquid Water ($0 °C$ to $100 °C$), and Superheated Steam ($100 °C$ to $200 °C$) at $P = 1 atm$ ($101.325 kPa$) from NIST IAPWS-95  **[S16]** and Lienhard 6e  **[S14]**.

| **$T$ ($°C$)** | **Phase** | **$\rho$ ($kg/m^3$)** | **$c_p$ ($J/kg/K$)** | **$k$ ($W/m/K$)** | **$\mu$ ($mPa s$)** | **$\nu$ ($e-6 m^2/s$)** | **$\alpha$ ($e-7 m^2/s$)** | **$\mathrm{Pr} = \nu/\alpha$** | **$\beta_V$ ($e-4 /K$) / Key Benchmark** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $-50.0$ | Ice Ih | $921.6$ | $1741$ | $2.76$ | — | — | $17.20$ | — | $\alpha_L = 45×10^{-6} /K$ ($\beta_V = 1.35×10^{-4} /K$) |
| $-30.0$ | Ice Ih | $919.6$ | $1882$ | $2.50$ | — | — | $14.45$ | — | $c_p$ rises linearly with $T$ in ice |
| $-20.0$ | Ice Ih | $918.7$ | $1960$ | $2.39$ | — | — | $13.27$ | — | Standard freezer ice benchmark |
| $-10.0$ | Ice Ih | $917.8$ | $2027$ | $2.30$ | — | — | $12.36$ | — | $\alpha_{\mathrm{ice}} \approx 9\times \alpha_{\mathrm{water}}$! |
| $0.0$ | Ice Ih | $916.7$ | $\mathbf{2093}$ | $2.22$ | — | — | $11.57$ | — | $L_f = 333.55 kJ/kg$ at $0.00 °C$ |
| $0.0$ | Liquid | $999.84$ | $4217.6$ | $0.5610$ | $1.792$ | $1.792$ | $1.330$ | $13.48$ | $\beta_V = \mathbf{-0.68}$ (contracts on warming!) |
| $3.984$ | Liquid | $\mathbf{999.97}$ | $4204.5$ | $0.5687$ | $1.568$ | $1.568$ | $1.353$ | $11.59$ | **Density maximum** ($\beta_V = 0.00$) |
| $10.0$ | Liquid | $999.70$ | $4192.1$ | $0.5800$ | $1.306$ | $1.306$ | $1.384$ | $9.44$ | $\beta_V = +0.88$ |
| $20.0$ | Liquid | $998.21$ | $\mathbf{4181.8}$ | $0.5984$ | $1.002$ | $1.004$ | $1.434$ | $7.00$ | $\beta_V = +2.07$ ($1\,\mathrm{cal}_{\mathrm{th}} = 4.184 J$) |
| $25.0$ | Liquid | $997.05$ | $4179.6$ | $0.6072$ | $0.890$ | $0.893$ | $1.458$ | $6.13$ | $\beta_V = +2.57$ (Standard $298.15 K$) |
| $35.0$ | Liquid | $994.03$ | $\mathbf{4178.0}$ | $0.6233$ | $0.719$ | $0.724$ | $1.501$ | $4.82$ | **Minimum $c_p$** of liquid water at $35 °C$ |
| $40.0$ | Liquid | $992.22$ | $4178.6$ | $0.6306$ | $0.653$ | $0.658$ | $1.521$ | $4.33$ | $\beta_V = +3.85$ (2027 cup mean $T$) |
| $50.0$ | Liquid | $988.03$ | $4180.6$ | $0.6435$ | $0.547$ | $0.554$ | $1.558$ | $3.55$ | $\beta_V = +4.58$ |
| $60.0$ | Liquid | $983.20$ | $4184.3$ | $0.6543$ | $0.466$ | $0.474$ | $1.591$ | $2.98$ | $\beta_V = +5.23$ |
| $80.0$ | Liquid | $971.79$ | $4196.3$ | $0.6700$ | $0.354$ | $0.365$ | $1.643$ | $2.22$ | $\beta_V = +6.41$ |
| $100.0$ | Sat. Liq | $958.35$ | $4215.7$ | $0.6791$ | $0.282$ | $0.294$ | $1.680$ | $1.75$ | $\beta_V = +7.50$; $L_v = 2256.4 kJ/kg$ |
| $100.0$ | Sat. Vap | $0.5977$ | $\mathbf{2080.0}$ | $0.0251$ | $0.0123$ | $20.53$ | $201.9$ | $1.017$ | NIST real sat. steam ($c_v = 1555.6 J/kg/K$) |
| $120.0$ | Steam | $0.5608$ | $2036.0$ | $0.0268$ | $0.0131$ | $23.32$ | $234.7$ | $0.994$ | OpenStax average $c_p = 2020 J/kg/K$ |
| $150.0$ | Steam | $0.5164$ | $2003.9$ | $0.0295$ | $0.0143$ | $27.67$ | $285.1$ | $0.971$ | Approaches ideal-gas behavior |
| $200.0$ | Steam | $0.4564$ | $1988.2$ | $0.0342$ | $0.0163$ | $35.67$ | $376.9$ | $0.946$ | $1 atm$ superheated steam |

**Table:** Temperature-dependent ideal-gas molar heat capacity $C_{p,m}^\circ(T) = A + Bt + Ct^2 + Dt^3 + E/t^2$ ($t = T/1000 K$) from NIST Chemistry WebBook  **[S16]**, with pre-evaluated values ($J/mol/K$) for algebraic midpoint calorimetry $\Delta H = n\,C_{p,m}(\bar{T})\,\Delta T$.

| **Gas ($M$, $g/mol$)** | **$A$** | **$B$** | **$C$** | **$D$** | **$E$** | **$C_{p,m}(298 K)$** | **$C_{p,m}(400 K)$** | **$C_{p,m}(600 K)$** | **$C_{p,m}(800 K)$** | **$C_{p,m}(1000 K)$** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $\mathrm{N_2}$ ($28.013$) | $28.986$ | $1.854$ | $-9.647$ | $16.635$ | $0.0001$ | $29.12\;(3.50R)$ | $29.25$ | $30.11$ | $31.43$ | $32.70\;(3.93R)$ |
| $\mathrm{O_2}$ ($31.999$) | $31.322$ | $-20.235$ | $57.866$ | $-36.506$ | $-0.0074$ | $29.38\;(3.53R)$ | $30.11$ | $32.09$ | $33.73$ | $34.87\;(4.19R)$ |
| $\mathrm{H_2}$ ($2.016$) | $33.066$ | $-11.363$ | $11.433$ | $-2.773$ | $-0.1586$ | $28.84\;(3.47R)$ | $29.18$ | $29.33$ | $29.62$ | $30.20\;(3.63R)$ |
| $\mathrm{CO}$ ($28.010$) | $25.568$ | $6.096$ | $4.055$ | $-2.671$ | $0.1310$ | $29.14\;(3.51R)$ | $29.34$ | $30.44$ | $31.90$ | $33.18\;(3.99R)$ |
| $\mathrm{H_2O(g)}$ ($18.015$) | $30.092$ | $6.833$ | $6.793$ | $-2.534$ | $0.0821$ | $33.58\;(4.04R)$ | $34.26$ | $36.33$ | $38.72$ | $41.27\;(4.96R)$ |
| $\mathrm{CO_2}$ ($44.010$) | $24.997$ | $55.187$ | $-33.691$ | $7.948$ | $-0.1366$ | $37.13\;(4.47R)$ | $41.33$ | $47.32$ | $51.43$ | $54.31\;(6.53R)$ |
| $\mathrm{CH_4}$ ($16.043$) | $-0.703$ | $108.477$ | $-42.522$ | $5.863$ | $0.6786$ | $35.69\;(4.29R)$ | $40.63$ | $52.23$ | $62.93$ | $71.80\;(8.64R)$ |
| $\mathrm{NH_3}$ ($17.031$) | $19.996$ | $49.771$ | $-15.376$ | $1.921$ | $0.1892$ | $35.65\;(4.29R)$ | $38.72$ | $45.29$ | $51.24$ | $56.49\;(6.79R)$ |

## The Law of Dulong & Petit (1819) and Quantum Lattice Freeze-Out

In 1819, French physicists Pierre Louis Dulong and Alexis Th\'er\`ese Petit discovered empirically that the product of specific heat $c$ and atomic molar mass $M$ is nearly identical for most solid elements near room temperature  **[S04,S07]**:

$$
\begin{aligned}

  C_m = M c \approx 3R = 3(8.31446 J/mol/K) = \mathbf{24.94 J/mol/K} \approx 6.0\,\mathrm{cal/(mol\cdotK)} \implies c \approx \frac{3R}{M}.
\end{aligned}
$$

### [DERIVATION: Algebraic Equipartition Proof of the Dulong–Petit Law  **[S04,S07]**]

In a crystalline solid of $N$ atoms, each atom vibrates harmonically in $3$ orthogonal directions ($x,y,z$) about its lattice site. Each 1D harmonic oscillator possesses $2$ quadratic energy terms ($E_{1\mathrm{D}} = \frac{1}{2}mv_x^2 + \frac{1}{2}\kappa_s x^2$), so a 3D lattice atom has $f = 3\text{ (kinetic)} + 3\text{ (potential)} = 6$ quadratic degrees of freedom. By the classical equipartition theorem (§`sec:06.2`), each quadratic mode stores an average thermal energy of $\frac{1}{2}k_B T$:

$$
U = N \left(6 \times \frac{1}{2}k_B T\right) = 3 N k_B T = 3 n R T \implies C_{V,m} = \frac{\Delta U}{n\Delta T} = \mathbf{3R = 24.943 J/mol/K}.
$$

For a multi-atom ionic or covalent crystal whose formula unit contains $\nu_{\mathrm{atoms}}$ atoms (such as $\mathrm{NaCl}$ with $\nu_{\mathrm{atoms}} = 2$, or $\mathrm{SiO_2}$ with $\nu_{\mathrm{atoms}} = 3$), the classical Kopp–Neumann extension gives $C_{V,m} \approx 3\,\nu_{\mathrm{atoms}}\,R$ ($\approx 49.9 J/mol/K$ for $\mathrm{NaCl}$, actual $50.5 J/mol/K$ at $298 K$).
- **Competition Shortcut — Identifying an Unknown Metal from Calorimetry Data:** Because $M \approx \dfrac{24.94 J/mol/K}{c}$, specific heat $c$ ($J/kg/K$) scales **inversely** with atomic mass $M$: light metals have large specific heat ($\mathrm{Al}$: $M = 27.0 g/mol \implies c = 897 J/kg/K$), medium transition metals cluster near $385–450 J/kg/K$ ($\mathrm{Fe}, \mathrm{Ni}, \mathrm{Cu}, \mathrm{Zn}$), and heavy metals have tiny specific heat ($\mathrm{Ag}$: $235 J/kg/K$; $\mathrm{Au}, \mathrm{Pb}, \mathrm{Pt}, \mathrm{W}$: $128–133 J/kg/K$).
- **Why Light, Stiff Solids Fall Below $3R$ at Room Temperature (Einstein 1907 & Debye 1912):** Classical equipartition assumes $k_B T \gg \hbar\omega_{\max}$, where $\omega_{\max}$ is the maximum lattice vibration (phonon) frequency $\omega_{\max} \sim \sqrt{\kappa_s/m_{\mathrm{atom}}}$. Defining the **Debye temperature** $\Theta_D = \hbar\omega_{\max}/k_B \propto \sqrt{\kappa_s/M}$:
- **High-$T$ Classical Regime ($T \gtrsim \Theta_D$):** All phonon modes are thermally active and $C_{V,m} \to 3R$. Heavy, soft metals have low $\Theta_D$ ($\mathrm{Pb}$: $\Theta_D = 105 K$; $\mathrm{Au}$: $165 K$; $\mathrm{Ag}$: $225 K$; $\mathrm{Cu}$: $343 K$) and reach $3R$ at or below $298 K$.
- **Quantum Freeze-Out at Room Temperature ($T < \Theta_D$):** Light atoms bound by ultra-stiff covalent bonds have high $\Theta_D$, so high-frequency modes are “frozen out” at $298 K$: **diamond** ($\Theta_D = 2230 K \implies C_m(298 K) = 6.12 J/mol/K = 0.74R$), **beryllium** ($\Theta_D = 1440 K \implies 16.44 J/mol/K = 1.98R$), **silicon** ($\Theta_D = 645 K \implies 19.79 J/mol/K = 2.38R$).
- **Cryogenic Debye $T^3$ Limit ($T \ll \Theta_D$):** As $T \to 0 K$, the phonon heat capacity vanishes as $T^3$, satisfying the Third Law (§`sec:08.5`):
    
$$
\begin{aligned}

      C_{V,m}(T) = \frac{12\pi^4}{5}R\left(\frac{T}{\Theta_D}\right)^3 \approx 233.78\,R\left(\frac{T}{\Theta_D}\right)^3 \qquad (\text{plus electronic } C_{\mathrm{el}} = \gamma_{\mathrm{el}}T \text{ in metals}).
\end{aligned}
$$

  

## Method of Mixtures, Calorimeter Constant $C_{\mathrm{cal}}$ & Multi-Phase Ledger

In an adiabatically insulated calorimeter ($Q_{\mathrm{ext}} = 0$) at constant pressure, conservation of energy requires that the algebraic sum of all signed heat transfers into every sub-body $i$ (including the calorimeter cup/stirrer/thermometer assembly $C_{\mathrm{cal}}$) equals zero  **[S04,S05]**:

$$
\begin{aligned}

  \sum_{i} Q_i = 0 \quad\Longleftrightarrow\quad \sum_{\text{cold}} |Q_{\mathrm{gained}}| = \sum_{\text{hot}} |Q_{\mathrm{lost}}|.
\end{aligned}
$$

When no phase change occurs, every term is sensible ($Q_i = m_i c_i (T_f - T_i)$) and (`eq:04:nbody`) yields the linear weighted average:

$$
\begin{aligned}

  \sum_{i=1}^N m_i c_i (T_f - T_i) + C_{\mathrm{cal}}(T_f - T_{\mathrm{cal}}) = 0 \implies
  T_f = \frac{\sum_{i=1}^N m_i c_i T_i + C_{\mathrm{cal}} T_{\mathrm{cal}}}{\sum_{i=1}^N m_i c_i + C_{\mathrm{cal}}}.
\end{aligned}
$$

To measure $C_{\mathrm{cal}}$ experimentally before an unknown-sample run, pour a known mass $m_h$ of warm water at $T_h$ into a known mass $m_c$ of cold water equilibrated with the calorimeter at $T_c$, record the equilibrium temperature $T_f$, and solve (`eq:04:nbodytf`):

$$
\begin{aligned}

  m_h c_w (T_f - T_h) + (m_c c_w + C_{\mathrm{cal}})(T_f - T_c) = 0 \implies
  C_{\mathrm{cal}} = m_h c_w \frac{T_h - T_f}{T_f - T_c} - m_c c_w.
\end{aligned}
$$

> **[Vector Figure: Five-stage quantitative heating curve for $1.000 kg$ of $\mathrm{H_2O}$ at $1 atm$ from $-40 °C$ ice to $160 °C$ steam ($c_{\mathrm{ice}} = 2.093 kJ/kg/K$, $L_f = 333.55 kJ/kg$, $c_w = 4.184 kJ/kg/K$, $L_v = 2256.4 kJ/kg$, $c_{p,\mathrm{steam}} = 2.080 kJ/kg/K$)  **[S04,S16]**. Note that boiling ($L_v$) absorbs $5.4\times$ more energy than heating liquid water from $0 °C$ to $100 °C$ ($418.4 kJ/kg$) and $6.76\times$ more than melting ice ($L_f$). | Label: `fig:04:heating-curve`]**
> - **Diagram Annotations & Key Elements:** **X-Axis:** Cumulative Heat Added per Kilogram of $\mathrm{H_2O}$, $q = Q/m$ ($kJ/kg$) • **Y-Axis:** Temperature $T$ ($°C$) • 1. Ice: $c_{\mathrm{ice}}\Delta T$ • 2. Melt ($0\,^\circ\mathrm{C}$): $L_f = 333.55 kJ/kg$ • 3. Liquid Water: $c_w\Delta T$ • 4. Boil ($100\,^\circ\mathrm{C}$): $L_v = 2256.4 kJ/kg$ • 5. Steam: $c_{\mathrm{st}}\Delta T$

### Deterministic 5-Zone Algebraic Algorithm for Ice–Water–Steam Mixtures

When subcooled ice ($m_{\mathrm{ice}}$ at $T_{\mathrm{ice},i} \leq 0 °C$), liquid water ($m_w$ at $0 °C \leq T_{w,i} \leq 100 °C$), superheated or saturated steam ($m_{\mathrm{st}}$ at $T_{\mathrm{st},i} \geq 100 °C$), and non-phase-changing solids/calorimeter ($m_{\mathrm{sol}}, c_{\mathrm{sol}}, T_{\mathrm{sol},i}$; $C_{\mathrm{cal}}, T_{\mathrm{cal},i}$) are mixed at $1 atm$, **never guess** $T_f$ blindly! guessing the wrong phase region produces nonsensical results such as $T_f < 0 °C$ after assuming all ice melted. Instead, use the **$0 °C$ Liquid-Water Reference State Method** (Fig. `fig:04:ice-water-tree`):
- **Step 1 — Compute Net Thermal Energy $E_{\mathrm{net},0}$ Relative to All-Liquid Water at $T_{\mathrm{ref}} = 0 °C$:**
  Bring every component algebraically to liquid water (or solid metal/calorimeter) at $0 °C$. Heat released by hot bodies cooling/condensing to $0 °C$ liquid water is positive; heat required to warm and melt cold ice to $0 °C$ liquid water is negative:
  
$$
\begin{aligned}

    E_{\mathrm{avail},0} &= m_w c_w (T_{w,i} - 0) + m_{\mathrm{st}}\!\left[c_{\mathrm{st}}(T_{\mathrm{st},i} - 100) + L_v + 100\,c_w\right] + \sum_k C_{\mathrm{solid},k}(T_{\mathrm{solid},k,i} - 0), \\
    E_{\mathrm{need,ice}\to 0\,\ell} &= m_{\mathrm{ice}} c_{\mathrm{ice}}(0 - T_{\mathrm{ice},i}) + m_{\mathrm{ice}} L_f = E_{\mathrm{warm,ice}} + E_{\mathrm{melt,ice}}, \\
    E_{\mathrm{net},0} &= E_{\mathrm{avail},0} - E_{\mathrm{need,ice}\to 0\,\ell}.
\end{aligned}
$$
- **Step 2 — Define Total Water Mass $M_{\mathrm{H_2O}}$ and Checkpoint Capacities:**
  Let $M_{\mathrm{H_2O}} = m_{\mathrm{ice}} + m_w + m_{\mathrm{st}}$ be the total $\mathrm{H_2O}$ mass and $C_{\mathrm{solids}} = \sum_k m_{\mathrm{sol},k} c_{\mathrm{sol},k} + C_{\mathrm{cal}}$ be the total heat capacity of all non-$\mathrm{H_2O}$ solids/vessels. Relative to the all-liquid $0 °C$ reference state ($E = 0$), the five phase zones are separated by exact energy checkpoints:
  
$$
\begin{aligned}

    E_{\mathrm{100,\ell}} = (M_{\mathrm{H_2O}} c_w + C_{\mathrm{solids}})(100 °C), \qquad
    E_{\mathrm{100,g}} = E_{\mathrm{100,\ell}} + M_{\mathrm{H_2O}} L_v.
\end{aligned}
$$
- **Step 3 — Locate $E_{\mathrm{net},0}$ in the 5-Zone Table (Table `tab:04:fivezones`) to Read Off the Exact Final State:**

**Table:** Deterministic 5-Zone Phase-Equilibrium Table for $\mathrm{H_2O}$ + Solids Calorimetry at $1 atm$ (using $E_{\mathrm{net},0}$ from Eq. `eq:04:enet0`).

| **Zone** | **Energy Condition on $E_{\mathrm{net},0}$** | **Final Phase State** | **Exact Algebraic Solution for $T_f$ or Mass Fractions** |
| --- | --- | --- | --- |
| **Zone I** | $E_{\mathrm{net},0} < -M_{\mathrm{H_2O}} L_f$ | All Subcooled Ice ($T_f < 0 °C$) | $\displaystyle T_f = \frac{E_{\mathrm{net},0} + M_{\mathrm{H_2O}} L_f}{M_{\mathrm{H_2O}} c_{\mathrm{ice}} + C_{\mathrm{solids}}} < 0 °C$ |
| **Zone II** | $-M_{\mathrm{H_2O}} L_f \leq E_{\mathrm{net},0} \leq 0$ | **Ice + Water at $T_f = 0.00 °C$** | $\displaystyle m_{\mathrm{ice,final}} = \frac{-E_{\mathrm{net},0}}{L_f}, \quad m_{\mathrm{liq,final}} = M_{\mathrm{H_2O}} - m_{\mathrm{ice,final}}$ |
| **Zone III** | $0 < E_{\mathrm{net},0} < E_{\mathrm{100,\ell}}$ | All Liquid Water ($0 °C < T_f < 100 °C$) | $\displaystyle T_f = \frac{E_{\mathrm{net},0}}{M_{\mathrm{H_2O}} c_w + C_{\mathrm{solids}}}$ |
| **Zone IV** | $E_{\mathrm{100,\ell}} \leq E_{\mathrm{net},0} \leq E_{\mathrm{100,g}}$ | **Water + Steam at $T_f = 100.0 °C$** | $\displaystyle m_{\mathrm{steam,final}} = \frac{E_{\mathrm{net},0} - E_{\mathrm{100,\ell}}}{L_v}, \quad m_{\mathrm{liq,final}} = M_{\mathrm{H_2O}} - m_{\mathrm{steam,final}}$ |
| **Zone V** | $E_{\mathrm{net},0} > E_{\mathrm{100,g}}$ | Superheated Steam ($T_f > 100 °C$) | $\displaystyle T_f = 100 °C + \frac{E_{\mathrm{net},0} - E_{\mathrm{100,g}}}{M_{\mathrm{H_2O}} c_{\mathrm{st}} + C_{\mathrm{solids}}}$ |

> **[Vector Figure: Deterministic 5-Zone decision tree for multi-phase $\mathrm{H_2O}$ calorimetry at $1 atm$, eliminating trial-and-error phase guessing. | Label: `fig:04:ice-water-tree`]**
> - **Diagram Annotations & Key Elements:** **START:** Compute $E_{\mathrm{net},0} = E_{\mathrm{avail},0} - (E_{\mathrm{warm,ice}} + E_{\mathrm{melt,ice}})$ relative to all-liquid $\mathrm{H_2O}$ at $0 °C$ (Eq. `eq:04:enet0`), total $\mathrm{H_2O}$ mass $M_{\mathrm{H_2O}} = m_{\mathrm{ice}}+m_w+m_{\mathrm{st}}$, and $E_{\mathrm{100,\ell}} = 100(M_{\mathrm{H_2O}}c_w + C_{\mathrm{solids}})$, $E_{\mathrm{100,g}} = E_{\mathrm{100,\ell}} + M_{\mathrm{H_2O}}L_v$. • **Zone I** / $E_{\mathrm{net},0} < -M_{\mathrm{H_2O}}L_f$ / **All Ice ($T_f < 0 °C$)** • **Zone II** / $-M_{\mathrm{H_2O}}L_f \le E_{\mathrm{net},0} \le 0$ / **Ice+Water ($0 °C$)** • **Zone III** / $0 < E_{\mathrm{net},0} < E_{\mathrm{100,\ell}}$ / **All Liquid ($0–100 °C$)** • **Zone IV** / $E_{\mathrm{100,\ell}} \le E_{\mathrm{net},0} \le E_{\mathrm{100,g}}$ / **Water+Steam ($100 °C$)** • **Zone V** / $E_{\mathrm{net},0} > E_{\mathrm{100,g}}$ / **All Steam ($T_f > 100 °C$)**

## Electrical, Continuous-Flow & Heat-Loss Corrected Calorimetry

High-precision specific-heat measurements replace hot-block dropping with controlled electrical Joule heating ($P_{\mathrm{elec}} = VI = I^2R = V^2/R$) and account for ambient heat exchange $Q_{\mathrm{leak}}$  **[S05,S14]**:
- **Batch Electrical Immersion Calorimetry & Two-Power Heat-Leak Elimination:**
  When an electric heater operates at voltage $V$ and current $I$ for duration $t$ inside a liquid of mass $m$ and calorimeter $C_{\mathrm{cal}}$:
  
$$
\begin{aligned}

    V I t = (m c + C_{\mathrm{cal}})\Delta T + Q_{\mathrm{leak}}.
\end{aligned}
$$

  If two runs of equal duration $t$ are performed across the *same* mean temperature window (so $Q_{\mathrm{leak},1} = Q_{\mathrm{leak},2} = \dot{Q}_{\mathrm{loss}}t$) at electrical powers $P_1 = V_1 I_1$ and $P_2 = V_2 I_2$, subtracting Run 1 from Run 2 cancels $Q_{\mathrm{leak}}$ identically:
  
$$
\begin{aligned}

    (P_2 - P_1)t = (m c + C_{\mathrm{cal}})(\Delta T_2 - \Delta T_1) \implies
    c = \frac{(P_2 - P_1)t - C_{\mathrm{cal}}(\Delta T_2 - \Delta T_1)}{m(\Delta T_2 - \Delta T_1)}.
\end{aligned}
$$
- **Callendar–Barnes Steady Continuous-Flow Calorimeter (1899):**
  Fluid flows steadily at mass flow rate $\dot{m} = \Delta m/\Delta t$ ($kg/s$) through a tube heated electrically at power $P = VI$, entering at $T_{\mathrm{in}}$ and exiting at steady $T_{\mathrm{out}}$:
  
$$
\begin{aligned}

    V I = \dot{m} c_p (T_{\mathrm{out}} - T_{\mathrm{in}}) + \dot{Q}_{\mathrm{loss}}.
\end{aligned}
$$

  Because the tube wall temperature profile is stationary in time, the heat capacity of the calorimeter apparatus $C_{\mathrm{cal}}$ drops out completely! Changing flow rate and power from $(\dot{m}_1, V_1 I_1)$ to $(\dot{m}_2, V_2 I_2)$ while maintaining the *exact same* $T_{\mathrm{in}}$ and $T_{\mathrm{out}}$ keeps $\dot{Q}_{\mathrm{loss}}$ identical, giving:
  
$$
\begin{aligned}

    c_p = \frac{V_2 I_2 - V_1 I_1}{(\dot{m}_2 - \dot{m}_1)(T_{\mathrm{out}} - T_{\mathrm{in}})}.
\end{aligned}
$$
- **Regnault–Pfaundler Linear Drift / Newton Cooling Correction:**
  In a batch calorimetry run where temperature is logged during a pre-period ($t < t_0$, slope $r_{\mathrm{pre}} = (dT/dt)_{\mathrm{pre}}$), a main reaction/heating period ($t_0 \leq t \leq t_{\max}$), and a post-period ($t > t_{\max}$, cooling slope $r_{\mathrm{post}} = (dT/dt)_{\mathrm{post}} < 0$), Newton's law of cooling $\dot{T}_{\mathrm{leak}} = -k_c(T - T_\infty)$ yields the midpoint-corrected adiabatic temperature rise:
  
$$
\begin{aligned}

    \Delta T_{\mathrm{corr}} = (T_{\max} - T_0) - \left(\frac{r_{\mathrm{pre}} + r_{\mathrm{post}}}{2}\right)(t_{\max} - t_0).
\end{aligned}
$$

  Since $r_{\mathrm{post}} < 0$ when $T_{\max} > T_\infty$, subtracting a negative drift rate **adds back** the temperature lost to the room during the mixing interval $(t_{\max} - t_0)$.

## Isobaric Coffee-Cup ($q_P = \Delta H$) vs. Isochoric Bomb Calorimetry ($q_V = \Delta U$)

Chemical and phase-change calorimetry (`Rule 5.c.ii, 5.c.vi`) employs two distinct vessels (Fig. `fig:04:calorimeters`) corresponding to the two thermodynamic state functions $H = U + PV$ and $U$  **[S05,S19]**:

> **[Vector Figure: Side-by-side comparison of (a) an open-to-atmosphere isobaric solution calorimeter measuring enthalpy change $q_P = \Delta H$ and (b) a rigid steel isochoric oxygen bomb calorimeter measuring internal energy change $q_V = \Delta U$  **[S05,S19]**. | Label: `fig:04:calorimeters`]**
> - **Diagram Annotations & Key Elements:** (a) Isobaric Coffee-Cup Calorimeter ($P = \text{const} \implies q_P = \Delta H$) • Loose lid ($P = P_{\mathrm{atm}}$) • Nested cups • Aqueous solution $m_{\mathrm{soln}}$ • $q_{\mathrm{rxn}} = -(m_{\mathrm{soln}}c_{\mathrm{soln}}+C_{\mathrm{cal}})\Delta T$ • (b) Isochoric Oxygen Bomb Calorimeter ($V = \text{const} \implies q_V = \Delta U$) • Steel Bomb ($V=\text{const}$) • $\mathrm{O_2}$ at $30 atm$ • Water bath ($m_w$) + Bomb ($C_{\mathrm{bomb}}$)
- **Isobaric Solution (Coffee-Cup) Calorimetry ($P = P_{\mathrm{atm}} = \text{const} \implies q_P = \Delta H$):**
  When $n_{\mathrm{lim}}$ moles of limiting reactant undergo an aqueous neutralization, dissolution, or displacement reaction inside an open-pressure cup containing total solution mass $m_{\mathrm{soln}} = m_1 + m_2$:
  
$$
\begin{aligned}

    q_{\mathrm{soln}} = (m_{\mathrm{soln}} c_{\mathrm{soln}} + C_{\mathrm{cal}})(T_f - T_i), \qquad
    q_{\mathrm{rxn}} = -q_{\mathrm{soln}}, \qquad
    \Delta H_{\mathrm{rxn}} = \frac{q_{\mathrm{rxn}}}{n_{\mathrm{lim}}} = -\frac{(m_{\mathrm{soln}} c_{\mathrm{soln}} + C_{\mathrm{cal}})\Delta T}{n_{\mathrm{lim}}}.
\end{aligned}
$$

  **Sign Rule:** If temperature rises ($\Delta T > 0$), the solution gained heat ($q_{\mathrm{soln}} > 0$), so the reaction released heat (**exothermic**, $\Delta H_{\mathrm{rxn}} < 0$). If temperature drops ($\Delta T < 0$, e.g., dissolving $\mathrm{NH_4NO_3(s)}$ in water), the reaction absorbed heat (**endothermic**, $\Delta H_{\mathrm{rxn}} > 0$).
- **Isochoric Oxygen Bomb Calorimetry ($V = \text{const} \implies W_{\mathrm{by}} = 0 \implies q_V = \Delta U$):**
  A combustible sample of mass $m_s$ ($n_s = m_s/M_s$ moles) is burned inside a thick-walled steel bomb pressurized to $\sim30 atm$ pure $\mathrm{O_2}$ and submerged in a water bath. Because the rigid steel bomb enforces $\Delta V = 0$, zero $P\text{--}V$ work is done and the total heat released measures $\Delta U$:
  
$$
\begin{aligned}

    q_{\mathrm{cal}} = C_{\mathrm{tot}}\Delta T = (m_w c_w + C_{\mathrm{hardware}})\Delta T, \qquad
    \Delta U_{\mathrm{rxn}} = \frac{-q_{\mathrm{cal}} + q_{\mathrm{fuse}} + q_{\mathrm{acid}}}{n_s},
\end{aligned}
$$

  where $q_{\mathrm{fuse}} = m_{\mathrm{wire}}|\Delta_c u_{\mathrm{wire}}|$ (for iron fuse wire, $|\Delta_c u_{\mathrm{Fe}}| = 5.86 kJ/g$ or $9.6 J/cm$) and $q_{\mathrm{acid}}$ corrects for trace $\mathrm{HNO_3}$ formation. Standard calibration uses **NIST SRM 39j Benzoic Acid** ($\mathrm{C_6H_5COOH(s)}$, $M = 122.12 g/mol$), which has certified constant-volume specific energy of combustion $|\Delta_c u^\circ| = \mathbf{26.434 kJ/g}$ ($\Delta_c U_m^\circ = \mathbf{-3228.1 kJ/mol}$) at $298.15 K$  **[S16,S19]**.
- **Converting Bomb $\Delta U_{\mathrm{rxn}}$ to Standard Enthalpy $\Delta H_{\mathrm{rxn}}$:**
  Since $H = U + PV$, for any reaction at temperature $T$ where ideal gases appear or disappear while condensed-phase volume changes $\Delta V_{\mathrm{solid/liq}}$ are negligible:
  
$$
\begin{aligned}

    \Delta H_{\mathrm{rxn}} = \Delta U_{\mathrm{rxn}} + \Delta(PV) \approx \Delta U_{\mathrm{rxn}} + \Delta n_{\mathrm{gas}} R T, \qquad
    \Delta n_{\mathrm{gas}} = \sum_{\text{gas prod}} \nu_p - \sum_{\text{gas react}} \nu_r.
\end{aligned}
$$

  Always check physical states at $298.15 K$: product water in bomb calorimetry condenses to **liquid** $\mathrm{H_2O(\ell)}$, so $\mathrm{H_2O(\ell)}$ is **not** counted in $\Delta n_{\mathrm{gas}}$!

**Table:** Sourced bomb ($\Delta_c U_m^\circ$) vs. isobaric ($\Delta_c H_m^\circ$) heats of combustion, gas-mole shifts $\Delta n_{\mathrm{gas}}$, and specific combustion energies $|\Delta_c u^\circ|$ ($kJ/g$, forming $\mathrm{CO_2(g)}$ and $\mathrm{H_2O(\ell)}$ at $298.15 K, 1 bar$) from NIST Chemistry WebBook  **[S16,S19]**.

| **Fuel / Standard** | **Formula (State)** | **$M$ ($g/mol$)** | **$\Delta_f H_m^\circ$ ($kJ/mol$)** | **$\Delta n_{\mathrm{gas}}$** | **$\Delta_c U_m^\circ$ ($kJ/mol$)** | **$\Delta_c H_m^\circ$ ($kJ/mol$)** | **$\|\Delta_c u^\circ\|$ ($kJ/g$) / Notes** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Benzoic Acid (SRM 39j) | $\mathrm{C_6H_5COOH(s)}$ | $122.12$ | $-385.2$ | $-0.5$ | $\mathbf{-3225.7}$ | $-3226.9$ | $\mathbf{26.434}$ (NIST bomb standard) |
| Sucrose | $\mathrm{C_{12}H_{22}O_{11}(s)}$ | $342.30$ | $-2226.1$ | $0.0$ | $-5643.4$ | $-5643.4$ | $16.487$ ($\Delta H_c = \Delta U_c$ exactly!) |
| D-Glucose | $\mathrm{C_6H_{12}O_6(s)}$ | $180.16$ | $-1273.3$ | $0.0$ | $-2805.0$ | $-2805.0$ | $15.570$ ($\Delta n_{\mathrm{gas}} = 6 - 6 = 0$) |
| Graphite (Carbon) | $\mathrm{C(s,graphite)}$ | $12.011$ | $0.0$ | $0.0$ | $-393.51$ | $-393.51$ | $32.763$ ($\mathrm{C(s)+O_2(g)\to CO_2(g)}$) |
| Hydrogen | $\mathrm{H_2(g)}$ | $2.016$ | $0.0$ | $-1.5$ | $-282.12$ | $-285.83$ | $139.94$ (HHV; LHV $= 119.96 kJ/g$) |
| Carbon Monoxide | $\mathrm{CO(g)}$ | $28.010$ | $-110.53$ | $-0.5$ | $-281.74$ | $-282.98$ | $10.059$ |
| Methane | $\mathrm{CH_4(g)}$ | $16.043$ | $-74.87$ | $-2.0$ | $-885.4$ | $-890.36$ | $55.19$ (Natural gas main component) |
| Acetylene | $\mathrm{C_2H_2(g)}$ | $26.038$ | $+227.4$ | $-1.5$ | $-1296.0$ | $-1299.7$ | $49.77$ (Oxy-acetylene torch fuel) |
| Ethane | $\mathrm{C_2H_6(g)}$ | $30.070$ | $-84.0$ | $-2.5$ | $-1553.6$ | $-1559.8$ | $51.67$ |
| Propane | $\mathrm{C_3H_8(g)}$ | $44.097$ | $-103.85$ | $-3.0$ | $-2212.5$ | $-2219.9$ | $50.17$ (LPG cylinder fuel) |
| $n$-Butane | $\mathrm{C_4H_{10}(g)}$ | $58.123$ | $-125.6$ | $-3.5$ | $-2868.8$ | $-2877.5$ | $49.36$ |
| $n$-Octane | $\mathrm{C_8H_{18}(\ell)}$ | $114.23$ | $-250.1$ | $-4.5$ | $-5459.3$ | $-5470.5$ | $47.79$ (Gasoline primary benchmark) |
| Benzene | $\mathrm{C_6H_6(\ell)}$ | $78.114$ | $+49.0$ | $-1.5$ | $-3263.9$ | $-3267.6$ | $41.78$ |
| Methanol | $\mathrm{CH_3OH(\ell)}$ | $32.042$ | $-239.2$ | $-0.5$ | $-724.9$ | $-726.1$ | $22.62$ |
| Ethanol | $\mathrm{C_2H_5OH(\ell)}$ | $46.068$ | $-277.6$ | $-1.0$ | $-1364.3$ | $-1366.8$ | $29.62$ (Spirit burner fuel) |
| Naphthalene | $\mathrm{C_{10}H_8(s)}$ | $128.17$ | $+77.9$ | $-2.0$ | $-5151.4$ | $-5156.3$ | $40.19$ (Secondary bomb calibrant) |

## Layered Worked Examples & Diagnostics

### Worked Example — Calorimeter Calibration ($C_{\mathrm{cal}}$) & Unknown Metal Identification via Dulong–Petit `[Basic $\cdot$ Rule 5.c.i–ii]`

A team first calibrates an insulated aluminum calorimeter originally containing $m_c = 150.0 g$ of water at $T_c = 20.00 °C$ by pouring in $m_h = 100.0 g$ of hot water at $T_h = 60.00 °C$ ($c_w = 4.184 J/g/K$); the mixture equilibrates at $T_{f,1} = 35.38 °C$. Next, they empty and refill the calorimeter with $m_w = 200.0 g$ of water at $T_1 = 20.00 °C$, drop in a $m_m = 250.0 g$ pure metal cylinder heated in a boiling-water bath to $T_m = 100.00 °C$, and measure a final temperature $T_{f,2} = 27.86 °C$. Find (a) the calorimeter constant $C_{\mathrm{cal}}$ and water equivalent $m_{\mathrm{eq}}$, (b) the metal's specific heat $c_m$, and (c) the metal's approximate atomic mass $M$ via Dulong–Petit and its identity from Table `tab:04:calorimetry`.

**Solution.**
**(a)** From (`eq:04:ccal`), the heat lost by the $100.0 g$ hot water equals the heat gained by the $150.0 g$ cold water plus calorimeter:

$$
C_{\mathrm{cal}} = m_h c_w \frac{T_h - T_{f,1}}{T_{f,1} - T_c} - m_c c_w = (100.0)(4.184)\frac{60.00 - 35.38}{35.38 - 20.00} - (150.0)(4.184) = 669.77 - 627.60 = \mathbf{42.17 J/K},
$$

giving a water equivalent $m_{\mathrm{eq}} = C_{\mathrm{cal}}/c_w = 42.17/4.184 = \mathbf{10.08 g}$ of water.
**(b)** In the metal run, $(m_w c_w + C_{\mathrm{cal}}) = (200.0)(4.184) + 42.17 = 878.97 J/K$. Energy balance $\sum Q_i = 0$ gives:

$$
c_m = \frac{(m_w c_w + C_{\mathrm{cal}})(T_{f,2} - T_1)}{m_m(T_m - T_{f,2})} = \frac{(878.97 J/K)(27.86 - 20.00)}{(0.2500 kg)(100.00 - 27.86)} = \frac{6908.7 J}{18.035 kg · K} = \mathbf{383.1 J/kg/K}.
$$

**(c)** Applying Dulong–Petit (`eq:04:dulongpetit`):

$$
M \approx \frac{3R}{c_m} = \frac{24.943 J/mol/K}{0.3831 J/g/K} = \mathbf{65.1 g/mol},
$$

which matches **Copper** ($M = 63.55 g/mol, c_p = 385 J/kg/K$) or **Zinc** ($M = 65.38 g/mol, c_p = 388 J/kg/K$)!

**✓ Verified by:** Re-substituting $C_{\mathrm{cal}} = 42.17 J/K$ and $c_m = 383.07 J/kg/K$ yields $T_{f,1} = 35.380 °C$ and $T_{f,2} = 27.860 °C$ (`check_sec02_05.py`).

### Worked Example — Partial-Melting Ice–Water Equilibrium (Zone II Plateau at $0\,^\circ\mathrm{C}$) `[Competition $\cdot$ Rule 5.c.i–ii]`

An insulated copper calorimeter of mass $m_{\mathrm{Cu}} = 120.0 g$ ($c_{\mathrm{Cu}} = 385 J/kg/K$) contains $m_w = 250.0 g$ of liquid water at $T_{w,i} = 22.0 °C$ ($c_w = 4184 J/kg/K$). A block of subcooled ice of mass $m_{\mathrm{ice}} = 110.0 g$ at $T_{\mathrm{ice},i} = -15.0 °C$ ($c_{\mathrm{ice}} = 2093 J/kg/K$, $L_f = 333.55 kJ/kg$) is added. Determine the final equilibrium temperature $T_f$ and the exact final masses of liquid water and solid ice.

**Solution.**
Using the deterministic 5-Zone Algorithm (§`sec:04.3.1`) relative to $0 °C$ liquid water:

$$
\begin{aligned}
E_{\mathrm{avail},0} &= (m_w c_w + m_{\mathrm{Cu}} c_{\mathrm{Cu}})(22.0 - 0) = \left[(0.2500)(4184) + (0.1200)(385)\right](22.0) = (1092.2 J/K)(22.0) = 24028.4 J, \\
  E_{\mathrm{warm,ice}} &= m_{\mathrm{ice}} c_{\mathrm{ice}}(0 - (-15.0)) = (0.1100)(2093)(15.0) = 3453.45 J, \\
  E_{\mathrm{melt,ice}} &= m_{\mathrm{ice}} L_f = (0.1100)(333550 J/kg) = 36690.50 J, \\
  E_{\mathrm{net},0} &= E_{\mathrm{avail},0} - (E_{\mathrm{warm,ice}} + E_{\mathrm{melt,ice}}) = 24028.40 - (3453.45 + 36690.50) = \mathbf{-16115.55 J}.
\end{aligned}
$$

Since $-M_{\mathrm{H_2O}} L_f = -120078 J \leq E_{\mathrm{net},0} \leq 0$, the system lies squarely in **Zone II** (Table `tab:04:fivezones`): the final temperature is locked at the phase plateau $\mathbf{T_f = 0.00 °C}$! The mass of ice remaining unmelted and the mass melted are:

$$
m_{\mathrm{ice,final}} = \frac{-E_{\mathrm{net},0}}{L_f} = \frac{16115.55 J}{333.55 J/g} = \mathbf{48.32 g}, \qquad
  m_{\mathrm{melted}} = 110.0 - 48.32 = 61.68 g, \qquad
  m_{\mathrm{liq,final}} = 250.0 + 61.68 = \mathbf{311.68 g}.
$$

**✓ Verified by:** Heat balance at $0 °C$: $Q_{\mathrm{warm,ice}} (3453.45 J) + m_{\mathrm{melted}} L_f (20574.95 J) = 24028.40 J = E_{\mathrm{avail},0}$ (`check_sec02_05.py`).

### Worked Example — Three-Phase Ice + Water + Steam Mixture in a Copper Calorimeter `[National $\cdot$ Rule 5.c.i–ii]`

Inside an insulated copper calorimeter ($m_{\mathrm{Cu}} = 100.0 g, c_{\mathrm{Cu}} = 385 J/kg/K$) initially equilibrated with $m_{\mathrm{ice}} = 80.0 g$ of ice at $T_{\mathrm{ice},i} = -10.0 °C$ ($c_{\mathrm{ice}} = 2093 J/kg/K, L_f = 333.55 kJ/kg$), an experimenter simultaneously introduces $m_w = 200.0 g$ of warm liquid water at $T_{w,i} = 50.0 °C$ ($c_w = 4184 J/kg/K$) and bubbles in $m_{\mathrm{st}} = 25.0 g$ of superheated steam at $T_{\mathrm{st},i} = 130.0 °C$ ($c_{\mathrm{st}} = 2080 J/kg/K, L_v = 2256.4 kJ/kg$) at $1 atm$. Determine the final temperature $T_f$ and phase composition.

**Solution.**
Apply the 5-Zone Algorithm (§`sec:04.3.1`) relative to $T_{\mathrm{ref}} = 0 °C$ liquid water, with $M_{\mathrm{H_2O}} = 80.0 + 200.0 + 25.0 = 305.0 g = 0.3050 kg$ and $C_{\mathrm{solids}} = m_{\mathrm{Cu}}c_{\mathrm{Cu}} = (0.1000)(385) = 38.50 J/K$:

$$
\begin{aligned}
E_{\mathrm{avail},0} &= m_w c_w(50.0) + m_{\mathrm{st}}\!\left[c_{\mathrm{st}}(130.0 - 100.0) + L_v + 100.0\,c_w\right] + C_{\mathrm{solids}}(-10.0 - 0) \\
  &= (0.200)(4184)(50.0) + (0.025)\!\left[(2080)(30.0) + 2256400 + 418400\right] - (38.50)(10.0) \\
  &= 41840.0 + 68430.0 - 385.0 = 109885.0 J, \\
  E_{\mathrm{need,ice}\to 0\,\ell} &= m_{\mathrm{ice}}\!\left[c_{\mathrm{ice}}(10.0) + L_f\right] = (0.0800)\!\left[20930 + 333550\right] = 28358.4 J, \\
  E_{\mathrm{net},0} &= 109885.0 - 28358.4 = \mathbf{+81526.6 J}.
\end{aligned}
$$

Compare $E_{\mathrm{net},0}$ against the liquid-boiling checkpoint $E_{\mathrm{100,\ell}} = (M_{\mathrm{H_2O}}c_w + C_{\mathrm{solids}})(100.0) = \left[(0.3050)(4184) + 38.50\right](100.0) = (1314.62 J/K)(100.0) = 131462.0 J$. Since $0 < E_{\mathrm{net},0} < E_{\mathrm{100,\ell}}$, the mixture lands in **Zone III** (100% liquid water, $305.0 g$) at:

$$
T_f = \frac{E_{\mathrm{net},0}}{M_{\mathrm{H_2O}} c_w + C_{\mathrm{solids}}} = \frac{81526.6 J}{1314.62 J/K} = \mathbf{62.02 °C}.
$$

**✓ Verified by:** $\sum Q_i$ at $T_f = 62.0153 °C$ equals $0.00 J$ to machine precision (`check_sec02_05.py`).

### Worked Example — Partial Steam Condensation (Zone IV Plateau at $100\,^\circ\mathrm{C}$) `[National $\cdot$ Rule 5.c.i–ii]`

Suppose in Example `ex:04.3` the mass of $130.0 °C$ superheated steam injected into the same vessel ($m_{\mathrm{Cu}} = 100.0 g$, $m_{\mathrm{ice}} = 80.0 g$ at $-10.0 °C$, $m_w = 200.0 g$ at $50.0 °C$) is increased from $25.0 g$ to $m_{\mathrm{st}} = 60.0 g$. Find the new final temperature $T_f$ and the final masses of liquid water and uncondensed steam.

**Solution.**
Here $M_{\mathrm{H_2O}} = 80.0 + 200.0 + 60.0 = 340.0 g = 0.3400 kg$ and $C_{\mathrm{solids}} = 38.50 J/K$:

$$
\begin{aligned}
E_{\mathrm{avail},0} &= 41840.0 + (0.0600)(2737200) - 385.0 = 41840.0 + 164232.0 - 385.0 = 205687.0 J, \\
  E_{\mathrm{net},0} &= 205687.0 - 28358.4 = \mathbf{177328.6 J}.
\end{aligned}
$$

The checkpoint for all-liquid water at $100.0 °C$ is $E_{\mathrm{100,\ell}} = \left[(0.3400)(4184) + 38.50\right](100.0) = 146106.0 J$, while complete vaporization requires $E_{\mathrm{100,g}} = 146106.0 + (0.3400)(2256400) = 913282.0 J$. Because $E_{\mathrm{100,\ell}} \leq E_{\mathrm{net},0} \leq E_{\mathrm{100,g}}$, the system lands in **Zone IV** (Table `tab:04:fivezones`) at $\mathbf{T_f = 100.0 °C}$! The mass of steam remaining uncondensed in equilibrium with liquid water is:

$$
m_{\mathrm{steam,final}} = \frac{E_{\mathrm{net},0} - E_{\mathrm{100,\ell}}}{L_v} = \frac{177328.6 - 146106.0}{2256.4 J/g} = \frac{31222.6 J}{2256.4 J/g} = \mathbf{13.84 g},
$$

and the final liquid water mass is $m_{\mathrm{liq,final}} = 340.0 - 13.84 = \mathbf{326.16 g}$ (so $60.0 - 13.84 = 46.16 g$ of steam condensed).

**✓ Verified by:** Heat released by $60.0 g$ steam cooling to $100 °C$ ($3744.0 J$) + $46.1623 g$ condensing ($104160.6 J$) = $107904.6 J$ = heat needed to bring ice, water & Cu to $100 °C$ (`check_sec02_05.py`).

### Worked Example — Electrical Calorimetry with Drift-Rate Cooling Correction `[National $\cdot$ Rule 5.c.i–ii]`

An electrical immersion calorimeter ($C_{\mathrm{cal}} = 55.0 J/K$) holds $m = 400.0 g$ of an unknown organic liquid. Before heating ($t < 0$), the temperature drifts upward at $r_{\mathrm{pre}} = +0.010 °C/min$. At $t_0 = 0.0 min$ ($T_0 = 21.200 °C$), a $12.00 V$, $2.500 A$ DC heater is switched on for $\Delta t = 4.000 min$ ($240.0 s$), reaching a peak $T_{\max} = 28.340 °C$ at $t_{\max} = 4.000 min$. After the heater is turned off ($t > 4.0 min$), the vessel cools at $r_{\mathrm{post}} = -0.050 °C/min$. Compute (a) the Regnault–Pfaundler drift-corrected temperature rise $\Delta T_{\mathrm{corr}}$, and (b) the liquid's specific heat $c$ and identity from Table `tab:04:calorimetry`.

**Solution.**
**(a)** The observed temperature rise is $\Delta T_{\mathrm{obs}} = 28.340 - 21.200 = 7.140 °C$. Using (`eq:04:drift`), the mean drift rate during the $4.000 min$ heating window is $\bar{r} = \frac{1}{2}(+0.010 - 0.050) = -0.020 °C/min$, so the adiabatic corrected rise is:

$$
\Delta T_{\mathrm{corr}} = \Delta T_{\mathrm{obs}} - \bar{r}(t_{\max} - t_0) = 7.140 °C - (-0.020 °C/min)(4.000 min) = 7.140 + 0.080 = \mathbf{7.220 °C = 7.220 K}.
$$

**(b)** Electrical energy supplied is $E_{\mathrm{elec}} = V I t = (12.00 V)(2.500 A)(240.0 s) = 7200.0 J$. From $E_{\mathrm{elec}} = (m c + C_{\mathrm{cal}})\Delta T_{\mathrm{corr}}$:

$$
c = \frac{E_{\mathrm{elec}}/\Delta T_{\mathrm{corr}} - C_{\mathrm{cal}}}{m} = \frac{7200.0/7.220 - 55.0}{0.4000 kg} = \frac{997.23 - 55.0}{0.4000} = \mathbf{2355.6 J/kg/K \approx 2.36 kJ/kg/K},
$$

identifying the liquid as **Ethylene Glycol** (or **Ethanol/Glycerol** family) in Table `tab:04:calorimetry`.

**✓ Verified by:** Neglecting the $0.080 K$ cooling correction overestimates $c$ by $27.4 J/kg/K$ ($1.16\%$) (`check_sec02_05.py`).

### Worked Example — Isobaric Coffee-Cup Neutralization Enthalpy ($\mathrm{HCl + NaOH}$, $q_P = \Delta H$) `[Competition $\cdot$ Rules 5.c.ii, 5.c.vi]`

In a nested coffee-cup calorimeter ($C_{\mathrm{cal}} = 18.0 J/K$), $100.0 mL$ of $1.000 mol/L$ aqueous $\mathrm{HCl}$ at $21.50 °C$ is mixed with $100.0 mL$ of $1.000 mol/L$ aqueous $\mathrm{NaOH}$ at $21.50 °C$. The combined solution has density $\rho_{\mathrm{soln}} = 1.020 g/mL$ and specific heat $c_{\mathrm{soln}} = 4.050 J/g/K$, and reaches a peak temperature $T_f = 28.12 °C$. Compute the molar enthalpy of neutralization $\Delta H_{\mathrm{neut}}$.

**Solution.**
Total solution volume is $V_{\mathrm{soln}} = 200.0 mL$, so $m_{\mathrm{soln}} = (200.0)(1.020) = 204.0 g$, and $\Delta T = 28.12 - 21.50 = +6.62 K$. Moles reacted: $n_{\mathrm{lim}} = (0.1000 L)(1.000 mol/L) = 0.1000 mol$. From (`eq:04:coffeecup`):

$$
q_{\mathrm{soln}} = (m_{\mathrm{soln}} c_{\mathrm{soln}} + C_{\mathrm{cal}})\Delta T = \left[(204.0)(4.050) + 18.0\right](6.62) = (844.20 J/K)(6.62) = 5588.6 J,
$$

$$
\Delta H_{\mathrm{neut}} = -\frac{q_{\mathrm{soln}}}{n_{\mathrm{lim}}} = -\frac{5.5886 kJ}{0.1000 mol} = \mathbf{-55.89 kJ/mol} \quad (\text{standard infinite-dilution value: } -55.84 kJ/mol).
$$

**✓ Verified by:** Including $C_{\mathrm{cal}} = 18.0 J/K$ accounts for $1.19 kJ/mol$ ($2.1\%$) of $\Delta H_{\mathrm{neut}}$ (`check_sec02_05.py`).

### Worked Example — Isochoric Bomb Calorimetry: Benzoic Acid Calibration & Octane $\Delta U_c \to \Delta H_c$ `[National $\cdot$ Rules 5.c.ii, 5.c.vi]`

A constant-volume oxygen bomb calorimeter is calibrated by burning $m_{\mathrm{BA}} = 1.2500 g$ of NIST benzoic acid ($|\Delta_c u^\circ| = 26.434 kJ/g$) with $5.0 cm$ of iron fuse wire ($q_{\mathrm{fuse}} = 48.0 J$), producing a temperature rise $\Delta T_1 = 3.1850 K$. Next, $m_{\mathrm{oct}} = 0.8565 g$ of liquid $n$-octane ($\mathrm{C_8H_{18}(\ell)}$, $M = 114.23 g/mol$) is burned at $T = 298.15 K$ with the same fuse wire ($q_{\mathrm{fuse}} = 48.0 J$), yielding $\Delta T_2 = 3.9410 K$. Find (a) the total bomb heat capacity $C_{\mathrm{tot}}$, (b) the molar internal energy of combustion $\Delta_c U_m^\circ$ of $n$-octane, and (c) the molar enthalpy of combustion $\Delta_c H_m^\circ$ at $298.15 K$.

**Solution.**
**(a)** Calibration energy released inside the bomb is $q_{\mathrm{cal},1} = m_{\mathrm{BA}}|\Delta_c u^\circ| + q_{\mathrm{fuse}} = (1.2500)(26434.0) + 48.0 = 33042.5 + 48.0 = 33090.5 J$, so:

$$
C_{\mathrm{tot}} = \frac{q_{\mathrm{cal},1}}{\Delta T_1} = \frac{33090.5 J}{3.1850 K} = \mathbf{10389.5 J/K = 10.390 kJ/K}.
$$

**(b)** In the octane run ($n_{\mathrm{oct}} = 0.8565 / 114.23 = 7.4980×10^{-3} mol$), $q_{\mathrm{cal},2} = C_{\mathrm{tot}}\Delta T_2 = (10389.48)(3.9410) = 40945.0 J$. Subtracting the fuse wire gives the net octane combustion heat $q_{V,\mathrm{oct}} = 40945.0 - 48.0 = 40897.0 J$:

$$
\Delta_c U_m^\circ = -\frac{q_{V,\mathrm{oct}}}{n_{\mathrm{oct}}} = -\frac{40.8970 kJ}{7.4980×10^{-3} mol} = \mathbf{-5454.4 kJ/mol}.
$$

**(c)** For $\mathrm{C_8H_{18}(\ell)} + \frac{25}{2}\,\mathrm{O_2(g)} \longrightarrow 8\,\mathrm{CO_2(g)} + 9\,\mathrm{H_2O(\ell)}$, the gas-mole change per mole of octane is $\Delta n_{\mathrm{gas}} = 8 - 12.5 = \mathbf{-4.5}$. By (`eq:04:du2dh`):

$$
\Delta_c H_m^\circ = \Delta_c U_m^\circ + \Delta n_{\mathrm{gas}} R T = -5454.4 kJ/mol + (-4.5)(8.31446×10^{-3} kJ/mol/K)(298.15 K) = -5454.4 - 11.15 = \mathbf{-5465.5 kJ/mol}.
$$

**✓ Verified by:** NIST WebBook certified $\Delta_c H_m^\circ(\mathrm{C_8H_{18},\ell}) = -5470.5 kJ/mol$ ($0.09\%$ agreement; `check_sec02_05.py`).

### Worked Example — Callendar–Barnes Continuous-Flow Calorimeter with Heat-Leak Cancellation `[National $\cdot$ Rule 5.c.i–ii]`

In a Callendar–Barnes steady continuous-flow calorimeter (`eq:04:flow`), an unknown oil enters at $T_{\mathrm{in}} = 20.00 °C$ and exits at $T_{\mathrm{out}} = 28.00 °C$ ($\Delta T = 8.00 K$). In Run 1, at mass flow rate $\dot{m}_1 = 1.800 g/s$, an electrical heater input of $V_1 = 15.00 V$ and $I_1 = 2.200 A$ is required to hold $T_{\mathrm{out}} = 28.00 °C$. In Run 2, the flow rate is increased to $\dot{m}_2 = 3.300 g/s$ and the heater is adjusted to $V_2 = 20.00 V$ and $I_2 = 2.850 A$ so that the exact same $T_{\mathrm{in}} = 20.00 °C$ and $T_{\mathrm{out}} = 28.00 °C$ are maintained. Find (a) the oil's specific heat $c_p$ and (b) the steady ambient heat loss rate $\dot{Q}_{\mathrm{loss}}$.

**Solution.**
**(a)** Electrical powers are $P_1 = V_1 I_1 = (15.00)(2.200) = 33.00 W$ and $P_2 = V_2 I_2 = (20.00)(2.850) = 57.00 W$. Because $T_{\mathrm{in}}$ and $T_{\mathrm{out}}$ are unchanged, $\dot{Q}_{\mathrm{loss}}$ is identical in both runs. By (`eq:04:flowcancel`):

$$
c_p = \frac{P_2 - P_1}{(\dot{m}_2 - \dot{m}_1)(T_{\mathrm{out}} - T_{\mathrm{in}})} = \frac{57.00 - 33.00}{(3.300 - 1.800)\times 10^{-3}\,kg/s \times 8.00 K} = \frac{24.00 W}{0.01200 kg · K/s} = \mathbf{2000 J/kg/K}.
$$

**(b)** Substituting $c_p = 2000 J/kg/K$ back into Run 1 (`eq:04:flow`):

$$
\dot{Q}_{\mathrm{loss}} = P_1 - \dot{m}_1 c_p \Delta T = 33.00 W - (1.800×10^{-3} kg/s)(2000 J/kg/K)(8.00 K) = 33.00 - 28.80 = \mathbf{4.20 W}.
$$

**✓ Verified by:** Run 2 check: $\dot{m}_2 c_p \Delta T + \dot{Q}_{\mathrm{loss}} = (0.00330)(2000)(8.00) + 4.20 = 52.80 + 4.20 = 57.00 W = P_2$ (`check_sec02_05.py`).

### Worked Example — Zone I Sub-Zero Equilibrium: Cryogenic Ice Freezing All Liquid Water `[National $\cdot$ Rule 5.c.i–ii]`

A large block of deeply subcooled ice of mass $m_{\mathrm{ice}} = 600.0 g$ at $T_{\mathrm{ice},i} = -40.0 °C$ ($c_{\mathrm{ice}} = 2093 J/kg/K, L_f = 333.55 kJ/kg$) is placed inside a negligible-mass insulated pouch, and $m_w = 50.0 g$ of liquid water at $T_{w,i} = 20.0 °C$ ($c_w = 4184 J/kg/K$) is poured over it. Use the 5-Zone Algorithm (Table `tab:04:fivezones`) to determine the final equilibrium state and final temperature $T_f$.

**Solution.**
Here $M_{\mathrm{H_2O}} = 600.0 + 50.0 = 650.0 g = 0.6500 kg$ and $C_{\mathrm{solids}} = 0$. Relative to all-liquid water at $T_{\mathrm{ref}} = 0 °C$ (`eq:04:enet0`):

$$
\begin{aligned}
E_{\mathrm{avail},0} &= m_w c_w(20.0 - 0) = (0.0500)(4184)(20.0) = 4184.0 J, \\
  E_{\mathrm{need,ice}\to 0\,\ell} &= m_{\mathrm{ice}} c_{\mathrm{ice}}(40.0) + m_{\mathrm{ice}} L_f = (0.6000)(2093)(40.0) + (0.6000)(333550) = 50232.0 + 200130.0 = 250362.0 J, \\
  E_{\mathrm{net},0} &= 4184.0 - 250362.0 = \mathbf{-246178.0 J}.
\end{aligned}
$$

Compare $E_{\mathrm{net},0}$ against the Zone I boundary $-M_{\mathrm{H_2O}}L_f = -(0.6500)(333550) = -216807.5 J$. Since $E_{\mathrm{net},0} < -M_{\mathrm{H_2O}}L_f$, the mixture lies in **Zone I** (Table `tab:04:fivezones`): all $50.0 g$ of liquid water cools to $0 °C$, freezes solid into ice, and the entire $650.0 g$ ice block equilibrates below $0 °C$ at:

$$
T_f = \frac{E_{\mathrm{net},0} + M_{\mathrm{H_2O}}L_f}{M_{\mathrm{H_2O}}c_{\mathrm{ice}}} = \frac{-246178.0 + 216807.5}{(0.6500)(2093)} = \frac{-29370.5 J}{1360.45 J/K} = \mathbf{-21.59 °C}.
$$

**✓ Verified by:** Direct check from $0 °C$ ice: warming $600 g$ ice from $-40 °C$ to $0 °C$ absorbs $50232 J$, while cooling & freezing $50 g$ water releases $4184 + 16677.5 = 20861.5 J$ (deficit $-29370.5 J$) (`check_sec02_05.py`).

### Worked Example — Four-Body Multi-Metal & Glycerol Mixture with Water Equivalent $m_{\mathrm{eq}}$ `[Competition $\cdot$ Rule 5.c.i–ii]`

A brass calorimeter with water equivalent $m_{\mathrm{eq}} = 15.0 g$ ($c_w = 4.184 J/g/K$) contains $m_{\mathrm{gly}} = 350.0 g$ of liquid glycerol ($c_{\mathrm{gly}} = 2.427 J/g/K$, Table `tab:04:calorimetry`) at $T_0 = 18.00 °C$. Two hot metal blocks—an aluminum block of mass $m_{\mathrm{Al}} = 120.0 g$ at $T_{\mathrm{Al},i} = 140.0 °C$ ($c_{\mathrm{Al}} = 0.897 J/g/K$) and a silver block of mass $m_{\mathrm{Ag}} = 200.0 g$ at $T_{\mathrm{Ag},i} = 180.0 °C$ ($c_{\mathrm{Ag}} = 0.235 J/g/K$)—are dropped simultaneously into the glycerol. Compute (a) the final equilibrium temperature $T_f$, and (b) the net heat transferred into or out of each of the four sub-systems.

**Solution.**
**(a)** The individual heat capacities $C_i = m_i c_i$ are $C_{\mathrm{cal}} = m_{\mathrm{eq}} c_w = (15.0)(4.184) = 62.76 J/K$, $C_{\mathrm{gly}} = (350.0)(2.427) = 849.45 J/K$, $C_{\mathrm{Al}} = (120.0)(0.897) = 107.64 J/K$, and $C_{\mathrm{Ag}} = (200.0)(0.235) = 47.00 J/K$.
Total heat capacity is $\sum C_i = 62.76 + 849.45 + 107.64 + 47.00 = 1066.85 J/K$. From (`eq:04:nbodytf`):

$$
T_f = \frac{(912.21)(18.00) + (107.64)(140.0) + (47.00)(180.0)}{1066.85} = \frac{39949.38 J}{1066.85 J/K} = \mathbf{37.45 °C}.
$$

**(b)** Individual signed heat transfers $Q_i = C_i(T_f - T_i)$:

$$
Q_{\mathrm{gly}} = +16518.4 J, \quad
  Q_{\mathrm{cal}} = +1220.4 J, \quad
  Q_{\mathrm{Al}} = -11038.9 J, \quad
  Q_{\mathrm{Ag}} = -6699.9 J \implies \sum Q_i = \mathbf{0.0 J}.
$$

**✓ Verified by:** $(16518.4 + 1220.4) - (11038.9 + 6699.9) = 0.0 J$ (`check_sec02_05.py`).

### Worked Example — Temperature-Dependent Gas Heating via NIST Shomate Midpoint $\bar{C}_{p,m}$ `[National $\cdot$ Rules 5.c.i, 5.c.vi, 5.d.iv]`

A steady industrial heat exchanger heats $n = 5.000 mol$ of carbon dioxide gas ($\mathrm{CO_2(g)}$) at constant pressure $P = 1.00 bar$ from $T_1 = 298.15 K$ to $T_2 = 1000.0 K$ ($\Delta T = 701.85 K$). Using Table `tab:04:shomate`, compute (a) the heat required $Q_{\mathrm{const}}$ if room-temperature $C_{p,m}(298 K) = 37.13 J/mol/K$ were naively assumed constant, and (b) the heat required $Q_{\mathrm{mid}}$ using the 3-point Simpson/midpoint average across $298 K$, $600 K$, and $1000 K$ (where vibrational modes of $\mathrm{CO_2}$ become thermally active), and find the percentage error of the constant-$C_p$ assumption.

**Solution.**
**(a)** Assuming constant room-temperature heat capacity:

$$
Q_{\mathrm{const}} = n\,C_{p,m}(298 K)\,\Delta T = (5.000 mol)(37.13 J/mol/K)(701.85 K) = \mathbf{130.30 kJ}.
$$

**(b)** From Table `tab:04:shomate`, $\mathrm{CO_2}$ vibrational bending and stretching modes elevate $C_{p,m}$ from $37.13 J/mol/K$ at $298 K$ to $47.32 J/mol/K$ at $600 K$ and $54.31 J/mol/K$ at $1000 K$. Splitting into two algebraic intervals $[298.15 K, 600 K]$ ($\bar{C}_{p,1} = \frac{1}{2}(37.13+47.32) = 42.225 J/mol/K$) and $[600 K, 1000 K]$ ($\bar{C}_{p,2} = \frac{1}{2}(47.32+54.31) = 50.815 J/mol/K$):

$$
Q_{\mathrm{mid}} = n\!\left[\bar{C}_{p,1}(600.0 - 298.15) + \bar{C}_{p,2}(1000.0 - 600.0)\right] = 5.000\!\left[(42.225)(301.85) + (50.815)(400.0)\right] = \mathbf{165.36 kJ}.
$$

Neglecting vibrational activation underestimates the heat requirement by $(165.36 - 130.30)/165.36 = \mathbf{21.2\%}$!

**✓ Verified by:** Exact NIST WebBook enthalpy difference $5[H^\circ(1000 K) - H^\circ(298.15 K)] = 5(33.405 kJ/mol) = 167.0 kJ$ ($0.98\%$ agreement without calculus; `check_sec02_05.py`).

### [TRAP & DIAGNOSTIC: §4 Top 5 Heat Capacity & Calorimetry Traps]

| **Wrong move / Symptom** | **What it produces / Why it fails** | **5-second diagnostic & fix** |
| --- | --- | --- |
| Writing $\sum m_i c_i (T_f - T_i) = 0$ across a phase boundary without checking if all ice melts or steam condenses | Predicts non-physical temperatures (e.g., $T_f = -18 °C$ after assuming all ice melted to liquid!) | Always compute $E_{\mathrm{net},0}$ (`eq:04:enet0`) and check the 5-Zone inequalities (Table `tab:04:fivezones`) before solving for $T_f$. |
| Mixing $J/g/K$ ($c_w = 4.184$) with latent heat in $kJ/kg$ ($L_f = 333.55$) in the same equation | Factor-of-$1000$ error between sensible and latent terms | Use either $(g, J/g/K, J/g)$ with $L_f = 333.55 J/g$ or $(kg, J/kg/K, J/kg)$ with $L_f = 333550 J/kg$. |
| Applying Dulong–Petit ($C_m \approx 3R$) blindly to diamond, beryllium, or multi-atom compounds like $\mathrm{NaCl}$ | Overestimates diamond's $c_p$ by $4\times$ and underestimates $\mathrm{NaCl}$ by $2\times$ | Light stiff solids ($\Theta_D > 300 K$) have quantum freeze-out; multi-atom ionic solids have $C_m \approx 3\,\nu_{\mathrm{atoms}} R$. |
| Forgetting to add the calorimeter's heat capacity $C_{\mathrm{cal}} = m_{\mathrm{eq}} c_w$ (or the metal cup mass $m_{\mathrm{cup}} c_{\mathrm{cup}}$) | Systematic $3\%\text{--}10\%$ error in $T_f$ or measured specific heat | Always include $C_{\mathrm{cal}}(T_f - T_{\mathrm{cal},i})$ at the same initial temperature as the fluid initially inside the vessel. |
| Counting liquid product water $\mathrm{H_2O(\ell)}$ in $\Delta n_{\mathrm{gas}}$ when converting bomb $\Delta U_c$ to $\Delta H_c$ at $298 K$ | Wrong sign/magnitude on $\Delta n_{\mathrm{gas}}RT$ (e.g., $+4.5$ instead of $-4.5$ for octane) | At $298.15 K$, combustion water condenses to $\mathrm{H_2O(\ell)}$ ($\nu_{\mathrm{gas}} = 0$); only count gaseous species ($\mathrm{O_2, CO_2, N_2}$). |

### [2027 HEAT-COLLECTOR DEVICE & LAB: 2027 Heat-Lamp Collector Calorimetry: Cup Thermal Mass, Stratification & Stirring]

In the 2027 heat-lamp collector event (`Rule 4.g, 5.II`), the Event Supervisor dispenses $m_w = 50–150 g$ ($50–150 mL$) of room-temperature water ($C_w = m_w c_w = 209.2–627.6 J/K$) into a 9 oz clear plastic party cup ($m_{\mathrm{cup}} \approx 5–10 g$, $c_{\mathrm{cup}} \approx 1200–1920 J/kg/K \implies C_{\mathrm{cup}} \approx 8–15 J/K$, only $1.5\%\text{--}6\%$ of $C_w$). Because infrared lamp radiation is absorbed within the **top $1–3 mm$ skin layer** of water and warm water is less dense than cool water ($\beta_V > 0$ for $T > 4 °C$), buoyancy **suppresses natural convection**, creating a stable thermal stratification where the top $1.3 cm$ ($0.5 in$) thermometer measurement zone (`Rule 5.II.g`) can sit $3–8 °C$ warmer than the cup bottom! See §`sec:14` for how to preserve this top-layer stratification during the 1-minute cup extraction window  **[S01,S02]**.

—
**See also:** §`sec:01.3` (`QS-03` Calorimetry), §`sec:01.4` (`QS-04` Ice/Steam Checkpoints), §`sec:05` (Phase Transitions & Latent Heat), §`sec:06.2` (Equipartition), §`sec:08.3` (Enthalpy & Hess's Law), and §`sec:14` (2027 Collector Thermal Budget).
