<!-- Source: src/sec17.tex | Tab: Tab 7: LAB/DATA | Target: 12 pp -->
# §17: Laboratory & Measurement Handbook (Thermometer Physics, Probe Time Constant $5\tau$, Immersion Bias, Calibration & GUM Uncertainty Propagation) {#sec:17}

> **[SCOPE: REQUIRED | 2027 Rules 4.f, 5.I.b, 5.II.c,g & Clarifications #1–#4 (All Tournament Levels)]**

Accurate thermal metrology links Part I written laboratory analysis (§`sec:18`) to Part II 2027 Heat-Lamp Collector temperature prediction (§`sec:15`–§`sec:16`)  **[S01,S05]**. Under 2027 Rule `4.f`, the Event Supervisor (ES) provides a non-mercury thermometer reading to $0.1 °C$ (*liquid-in-glass spirit, electronic digital probe, or non-contact infrared*) and uses the **same thermometer** for a team's starting ($T_{\mathrm{start}}$) and final ($T_f$) water readings  **[S01,S02]**. This chapter covers the sensor physics of all five thermometer families, dynamic thermal lag ($\tau_p$ and the $5\tau_p$ settling rule), top-layer immersion and radial stratification bias under Official Clarifications `#1–`#4“, fixed-point ice/steam calibration, JCGM GUM / NIST TN 1297 uncertainty propagation  **[S21]**, and step-by-step classroom-safe calorimetry and heat-lamp collector validation protocols.

## Physics & Specifications of the Five Thermometer Technologies (`Rule 4.f`)

Every thermometer transduces temperature $T$ into a measurable thermometric property $X(T)$ (liquid column length $L$, electrical resistance $R$, thermoelectric voltage $\Delta V$, or mid-infrared radiant exitance $M_{\lambda}$)  **[S13,S22,S33]**. Table `tab:17:sensors` summarizes the physical laws, operating windows, dynamic time constants $\tau_p$, active sensing zones, and 2027 competition diagnostics across all five sensor technologies permitted under Rule `4.f`  **[S01,S05,S22]**.

**Table:** Comparison of the Five Thermometer Technologies Used in Science Olympiad Thermodynamics (`Rule 4.f`)  **[S01,S05,S12,S22]**.

| **Sensor Family** | **Governing Thermometric Equation** | **Range $[°C]$** | **Typical Accuracy** | **$\tau_p$ in Water ($5\tau_p$)** | **Sensing Zone $[mm]$** | **2027 Top-Layer Stratification & Exam Role** |
| --- | --- | --- | --- | --- | --- | --- |
| **1. Liquid-in-Glass (Spirit / Galinstan)** | $L(T) = L_0 + \dfrac{V_0}{A_c}(\beta_{\mathrm{liq}} - 3\alpha_g)(T - T_0)$ | $-20$ to $+110$ (spirit) | $\pm0.5–1.0 °C$ | $6–12 s$ ($30–60 s$) | $15$–$25$ bulb ($50$–$76$ imm.) | Long bulb averages across top & middle layers; stem-emergence & meniscus parallax bias. Mercury banned (`Rule 4.f`). |
| **2. NTC Thermistor Digital Probe** | $\dfrac{1}{T} = A + B\ln R + C(\ln R)^3$; <br> $R(T) = R_0 e^{\beta(1/T - 1/T_0)}$ | $-50$ to $+150$ | $\pm0.1–0.2 °C$ | $0.8–3.5 s$ ($4–18 s$) | $4$–$10$ (bead at tip) | **Most common ES probe.** High sensitivity ($\alpha_R \approx -4 %/K$) & small tip sample top $5–12 mm$ layer (`Clarif. #4`). |
| **3. Platinum RTD (`Pt100` / `Pt1000`)** | $R(t) = R_0(1 + A t + B t^2)$ ($t \ge 0 °C$, $R_0 = 100.00 Ω$) | $-200$ to $+600$ | Class A: $\pm(0.15 + 0.002\|t\|)$ | $3.0–8.0 s$ ($15–40 s$) | $15$–$30$ (wire/film element) | Reference metrology standard (IEC 60751). Longer sheath requires $\ge25 mm$ depth; use 3/4-wire bridge for lead resistance. |
| **4. Thermocouple (`Type K` / `Type T`)** | $\Delta V = \int_{T_{\mathrm{ref}}}^{T} S_{AB}(T')\,dT' \approx S_{AB}(T - T_{\mathrm{ref}})$ **[S22]** | $-200$ to $+1260$ (K); $+350$ (T) | $\pm1.1 °C$ (K); $\pm0.5 °C$ (T) | $0.05–0.3 s$ bare ($1.5–3 s$ sheath) | $1$–$5$ (point weld) | Fastest point sensor ($5\tau_p < 1.5 s$ bare bead) with negligible heat-capacity drain; requires cold-junction compensation (CJC). |
| **5. Non-Contact Infrared (IR) Gun** | $T_{\mathrm{read}} = \left[T_{\mathrm{amb}}^4 + \dfrac{\varepsilon_{\mathrm{true}}}{\varepsilon_{\mathrm{set}}}(T_{\mathrm{obj}}^4 - T_{\mathrm{amb}}^4)\right]^{1/4}$ | $-30$ to $+500$ | $\pm1.5–2.0 °C$ | $0.15–0.5 s$ ($1.0–2.5 s$) | $0.015$ (top $15 µm$ skin) | Water $\varepsilon_w = 0.96$ matches $\varepsilon_{\mathrm{set}} = 0.95$. **Never shoot through plastic wrap/cup wall or at shiny Al foil ($\varepsilon=0.04$)!** |

### 1. Non-Mercury Liquid-in-Glass Thermometers (Spirit & Galinstan)

Because mercury ($\mathrm{Hg}$) is prohibited for safety under Rule `4.f`  **[S01]**, competition liquid-in-glass thermometers use dyed organic spirits (ethanol, $\beta_{\mathrm{liq}} = 1.12×10^{-3} /K$; toluene, $\beta_{\mathrm{liq}} = 1.08×10^{-3} /K$; or kerosene, $\beta_{\mathrm{liq}} = 0.99×10^{-3} /K$) or non-toxic liquid metal alloy Galinstan ($\mathrm{Ga\text{--}In\text{--}Sn}$, $\beta_{\mathrm{liq}} \approx 1.83×10^{-4} /K$) enclosed in a thin borosilicate glass bulb ($\alpha_g = 3.3×10^{-6} /K$, volumetric $\beta_g = 3\alpha_g = 9.9×10^{-6} /K$) connected to a uniform capillary bore of diameter $d_c$ and cross-sectional area $A_c = \pi d_c^2/4$  **[S13]**.
- **Differential Volumetric Expansion Law:** When the bulb of initial internal volume $V_0$ warms by $\Delta T = T - T_0$, the liquid volume expands by $\Delta V_{\mathrm{liq}} = V_0 \beta_{\mathrm{liq}}\Delta T$ while the glass bulb cavity expands by $\Delta V_{\mathrm{glass}} = V_0 (3\alpha_g)\Delta T$. Only the *apparent* differential volume $\Delta V_{\mathrm{app}} = V_0(\beta_{\mathrm{liq}} - 3\alpha_g)\Delta T = V_0\beta_{\mathrm{app}}\Delta T$ is forced up the capillary stem of area $A_c$:
  
$$
\begin{aligned}

    \Delta L = L(T) - L_0 = \frac{V_0}{A_c}(\beta_{\mathrm{liq}} - 3\alpha_g)(T - T_0) = \frac{4 V_0 \beta_{\mathrm{app}}}{\pi d_c^2}(T - T_0) \implies S_L = \frac{\Delta L}{\Delta T} = \frac{4 V_0(\beta_{\mathrm{liq}} - 3\alpha_g)}{\pi d_c^2}
\end{aligned}
$$

  Maximizing linear sensitivity $S_L$ $[mm/K]$ requires a large bulb volume $V_0$, a high-expansion working fluid $\beta_{\mathrm{liq}}$, a low-expansion borosilicate glass $\alpha_g$, and a narrow capillary bore $d_c$ (though large $V_0$ increases thermal time constant $\tau_p$).
- **Total vs. Partial Immersion & Stem-Emergence Correction:**  A *partial-immersion* thermometer is calibrated with the bulb and lower stem immersed to an etched immersion ring (typically $50 mm$ or $76 mm$) while the upper stem sits in ambient air. A *total-immersion* thermometer is calibrated with the entire liquid column submerged to the top of the meniscus. If a total-immersion thermometer (or a partial-immersion thermometer immersed shallower than its line, as in a $38 mm$-deep $100 mL$ cup!) has $N$ degrees (in $°C$ scale length) of liquid column emerging into cooler ambient stem air at $T_{\mathrm{stem}}$ while the bulb is at $T_{\mathrm{read}}$, the emergent liquid column contracts and under-reads the true bath temperature $T_{\mathrm{true}}$ by:
  
$$
\begin{aligned}

    \Delta T_{\mathrm{stem}} = k_g\,N\,(T_{\mathrm{read}} - T_{\mathrm{stem}}), \qquad T_{\mathrm{true}} = T_{\mathrm{read}} + k_g\,N\,(T_{\mathrm{read}} - T_{\mathrm{stem}})
\end{aligned}
$$

  where $k_g = \beta_{\mathrm{app}} \approx 0.00104 /°C$ for organic spirit-in-glass thermometers and $k_g \approx 0.00016 /°C$ for mercury/Galinstan-in-borosilicate-glass thermometers  **[S21,S33]**.
- **Separated Spirit Column Diagnostic & Fix:**  Organic spirit columns easily separate during shipping, leaving a gas bubble in the bore or a droplet clinging to the top expansion chamber (causing the thermometer to read $1–5 °C$ too low!). Always inspect the entire bore before use; rejoin a separated column by cooling the bulb in an ice-salt bath so all liquid retreats into the bulb, or by gentle centrifugal swinging (never heat the bulb over an open flame, which shatters the glass expansion bulb).

### 2. Negative Temperature Coefficient (NTC) Thermistors

NTC thermistors are sintered metal-oxide semiconductor beads ($\mathrm{Mn_3O_4}$, $\mathrm{NiO}$, $\mathrm{Co_3O_4}$) whose charge-carrier density grows exponentially with thermal excitation across a semiconductor energy gap, causing resistance $R(T)$ to drop steeply as absolute temperature $T$ $[K]$ rises  **[S21,S33]**:

$$
\begin{aligned}

  \text{**Steinhart--Hart (3-Parameter Exact):**}\quad \frac{1}{T} = A + B\ln R + C(\ln R)^3 \quad (T\text{ in }K,\ R\text{ in }Ω)
\end{aligned}
$$

*(Note: The quadratic $(\ln R)^2$ term vanishes in the standard Steinhart–Hart representation, achieving $\pm0.005 °C$ fidelity across $0–100 °C$).* Over a narrower $50 K$ window around reference state $(T_0, R_0)$ (typically $R_0 = 10.00 kΩ$ at $T_0 = 298.15 K = 25.00 °C$), setting $C=0$ yields the **2-parameter $\beta$-equation**:

$$
\begin{aligned}

  R(T) = R_0\exp\!\left[\beta\!\left(\frac{1}{T} - \frac{1}{T_0}\right)\right] \Longleftrightarrow T = \left[\frac{1}{T_0} + \frac{1}{\beta}\ln\!\left(\frac{R}{R_0}\right)\right]^{-1}, \qquad \alpha_R = \frac{1}{R}\frac{dR}{dT} = -\frac{\beta}{T^2}
\end{aligned}
$$

With material constant $\beta \in 3400–4100 K$, the fractional temperature coefficient at $T = 300 K$ is $\alpha_R \approx -3892/300^2 = -0.0432 /K = -4.32 %/K$ — roughly **11 times more sensitive** than a platinum RTD ($\alpha_{\mathrm{Pt}} = +0.385 %/K$)!
- **Voltage-Divider Readout & Self-Heating Dissipation Error ($\Delta T_{\mathrm{SH}}$):**  In a microcontroller or digital probe readout, the thermistor $R(T)$ is placed in series with a fixed precision resistor $R_s$ across excitation voltage $V_{\mathrm{ref}}$, producing output voltage $V_{\mathrm{out}} = V_{\mathrm{ref}}\frac{R(T)}{R_s + R(T)}$ (which has maximum linearity $\frac{d^2 V_{\mathrm{out}}}{dT^2} = 0$ when $R_s = R(T_{\mathrm{mid}})\frac{\beta - 2T_{\mathrm{mid}}}{\beta + 2T_{\mathrm{mid}}} \approx 0.77\,R(T_{\mathrm{mid}})$). Because current $I = \frac{V_{\mathrm{ref}}}{R_s + R(T)}$ dissipates Joule power $P_{\mathrm{elec}} = I^2 R(T)$ inside the tiny bead, the bead warms above the surrounding fluid by:
  
$$
\begin{aligned}

    \Delta T_{\mathrm{SH}} = \frac{P_{\mathrm{elec}}}{\delta_{\mathrm{diss}}} = \frac{I^2 R(T)}{\delta_{\mathrm{diss}}} = \frac{V_{\mathrm{ref}}^2 R(T)}{\delta_{\mathrm{diss}}\left[R_s + R(T)\right]^2}
\end{aligned}
$$

  where $\delta_{\mathrm{diss}} = h_p A_p$ $[mW/K]$ is the probe's **dissipation constant**. Because convective transfer $h_p$ is $5\text{--}10\times$ smaller in still air than in water, $\delta_{\mathrm{diss}} \approx 0.8–1.5 mW/K$ in still air versus $5.0–10.0 mW/K$ in liquid water! An improperly designed thermistor circuit carrying $I = 1.0 mA$ at $R = 10 kΩ$ ($P_{\mathrm{elec}} = 10 mW$) self-heats by $+10 °C$ in air and $+1.5 °C$ in water. Always limit thermistor excitation current to $I \le 100 µA$ ($P_{\mathrm{elec}} \le 0.1 mW \implies \Delta T_{\mathrm{SH}} < 0.02 °C$).

### 3. Platinum Resistance Temperature Detectors (`Pt100` & `Pt1000` RTDs)

Pure platinum exhibits a repeatable, nearly linear positive resistance-temperature relation standardized by IEC 60751 (`Pt100`: $R_0 = 100.00 Ω$ at $t = 0.00 °C$; `Pt1000`: $R_0 = 1000.0 Ω$ at $0.00 °C$) via the **Callendar–Van Dusen Equation**:

$$
\begin{aligned}

  R(t) = \begin{cases}
    R_0\left(1 + A t + B t^2\right) & \text{for }0 °C \le t \le 661 °C \\[2pt]
    R_0\left[1 + A t + B t^2 + C(t - 100 °C)t^3\right] & \text{for }-200 °C \le t < 0 °C
  \end{cases}
\end{aligned}
$$

where $t$ is temperature in $°C$, $A = 3.9083×10^{-3} /°C$, $B = -5.775×10^{-7} /sq·°C$, and $C = -4.183×10^{-12} /°C^4$. Over $0–100 °C$, the mean linear temperature coefficient is $\alpha_{0\text{--}100} = \frac{R(100) - R(0)}{100\,R_0} = A + 100B = 0.00385055 /°C$ ($+0.385055 Ω/°C$ for `Pt100`).
- **IEC 60751 Accuracy Classes:** Class AA: $\Delta t_{\mathrm{tol}} = \pm(0.10 + 0.0017|t|)\,°C$; Class A: $\pm(0.15 + 0.002|t|)\,°C$; Class B: $\pm(0.30 + 0.005|t|)\,°C$.
- **2-Wire Lead-Resistance Trap vs. 3-Wire & 4-Wire Bridges:**  Because a `Pt100` changes by only $0.385 Ω/°C$, two copper extension leads each of resistance $R_{\mathrm{lead}}$ in a simple 2-wire ohmmeter circuit add $2R_{\mathrm{lead}}$ to $R(t)$, creating a large positive temperature bias:
  
$$
\begin{aligned}

    \Delta t_{\mathrm{lead,2-wire}} \approx \frac{2 R_{\mathrm{lead}}}{R_0 \alpha_{0\text{--}100}} = \frac{2 R_{\mathrm{lead}}}{0.385055 Ω/°C} \approx \left(5.194 °C/Ω\right) R_{\mathrm{lead}}
\end{aligned}
$$

  Just $0.35 Ω$ per wire produces a $+1.82 °C$ reading error! A **3-wire Wheatstone bridge** places one current-carrying lead in each adjacent bridge leg so matched lead resistances cancel to first order, while a **4-wire Kelvin measurement** uses two outer leads to supply excitation current $I$ and two separate high-impedance inner sense leads ($I_{\mathrm{sense}} \approx 0$) to measure voltage drop directly across the platinum element, eliminating lead-resistance error completely.

### 4. Thermocouples (`Type K`, `T`, `J`, `E` — NIST ITS-90 SRD 60  **[S22]**)

When two dissimilar conductors $A$ and $B$ are joined at a sensing junction at $T_{\mathrm{sense}}$ and their open ends are held at a reference junction temperature $T_{\mathrm{ref}}$, carrier diffusion along the thermal gradient generates an open-circuit **Seebeck thermoelectric EMF** $\Delta V_{AB}$  **[S22]**:

$$
\begin{aligned}

  \Delta V_{AB} = \int_{T_{\mathrm{ref}}}^{T_{\mathrm{sense}}} \left[S_A(T) - S_B(T)\right]dT = \int_{T_{\mathrm{ref}}}^{T_{\mathrm{sense}}} S_{AB}(T)\,dT \approx S_{AB}(\bar{T})\,(T_{\mathrm{sense}} - T_{\mathrm{ref}})
\end{aligned}
$$
- **Three Fundamental Thermoelectric Laws:**
    (1) *Law of Homogeneous Circuits:* Heating a single homogeneous wire cannot produce a net thermoelectric current; voltage depends only on junction temperatures $T_{\mathrm{sense}}$ and $T_{\mathrm{ref}}$, not the temperature profile along homogeneous leads.
    (2) *Law of Intermediate Metals:* Inserting a third metal $C$ (e.g., copper voltmeter terminals or solder) into the circuit adds zero net EMF if both junctions with metal $C$ are at the same temperature.
    (3) *Law of Intermediate Temperatures (Cold-Junction Compensation, CJC):* $\Delta V(T_1, T_3) = \Delta V(T_1, T_2) + \Delta V(T_2, T_3)$. Because a digital thermocouple meter's input jack sits at ambient room temperature $T_{\mathrm{ref}} \approx 22 °C$ rather than an ice bath at $0 °C$, an onboard thermistor/IC measures $T_{\mathrm{ref}}$ at the terminal block and adds the NIST ITS-90 table voltage $\Delta V(0 °C, T_{\mathrm{ref}})$ electronically  **[S22]**.
- **Standard NIST ITS-90 Thermocouple Types at $25 °C$  **[S22]**:**
    `Type K` ($\text{Chromel}^+$ [$\mathrm{Ni\text{--}Cr}$] / $\text{Alumel}^-$ [$\mathrm{Ni\text{--}Al}$]): $S_K = 40.6 µV/K$ ($39.5 µV/K$ at $0 °C$, $41.3 µV/K$ at $50 °C$); general-purpose probe.
    `Type T` ($\text{Copper}^+$ / $\text{Constantan}^-$ [$\mathrm{Cu\text{--}Ni}$]): $S_T = 40.9 µV/K$; highest stability and tightest special tolerance ($\pm0.5 °C$) in wet $0–100 °C$ calorimetry.
    `Type J` ($\text{Iron}^+$ / $\text{Constantan}^-$): $S_J = 51.7 µV/K$ (iron rusts in water; avoid in wet labs).
    `Type E` ($\text{Chromel}^+$ / $\text{Constantan}^-$): $S_E = 60.9 µV/K$ (highest Seebeck output and lowest thermal conductivity stem loss).

**Table:** Master Sensor Transduction Reference Table ($-20 °C$ to $120 °C$): `Pt100` RTD Resistance (IEC 60751), $10 kΩ$ NTC Thermistor ($\beta=3892 K$), and NIST ITS-90 Thermocouple EMF ($T_{\mathrm{ref}}=0.00 °C$)  **[S21,S22]**.

| **$t$ $[°C]$** | **$T$ $[K]$** | **`Pt100` $R(t)$ $[Ω]$** | **NTC $10 kΩ$ $R(T)$ $[Ω]$** | **`Type K` $E(0 °C,t)$ $[mV]$** | **`Type T` $E(0 °C,t)$ $[mV]$** | **Benchmark State / Calibration Note** |
| --- | --- | --- | --- | --- | --- | --- |
| $-20.0$ | $253.15$ | $92.16$ | $101{,}916$ | $-0.778$ | $-0.757$ | Freezer / ice-salt bath |
| $0.0$ | $273.15$ | $100.00$ | $33{,}024$ | $0.000$ | $0.000$ | **Ice-point reference ($\delta_0$ check)** |
| $10.0$ | $283.15$ | $103.90$ | $19{,}969$ | $+0.397$ | $+0.391$ | Chilled water supply |
| $20.0$ | $293.15$ | $107.79$ | $12{,}488$ | $+0.798$ | $+0.790$ | Standard room baseline |
| $25.0$ | $298.15$ | $109.73$ | $10{,}000$ | $+1.000$ | $+0.992$ | **NTC reference ($R_0 = 10.00 kΩ$)** |
| $30.0$ | $303.15$ | $111.67$ | $8{,}064$ | $+1.203$ | $+1.196$ | Mild collector warming |
| $40.0$ | $313.15$ | $115.54$ | $5{,}337$ | $+1.612$ | $+1.612$ | Typical 2027 collector $T_f$ ($h=50 cm$) |
| $50.0$ | $323.15$ | $119.40$ | $3{,}613$ | $+2.023$ | $+2.036$ | High-gain collector $T_f$ ($h=40 cm$) |
| $60.0$ | $333.15$ | $123.24$ | $2{,}496$ | $+2.436$ | $+2.468$ | Hot water calorimetry bath |
| $80.0$ | $353.15$ | $130.90$ | $1{,}264$ | $+3.267$ | $+3.358$ | `#1 PET` cup $T_g$ warning zone! |
| $100.0$ | $373.15$ | $138.51$ | $682.3$ | $+4.096$ | $+4.279$ | **Normal steam point ($101.325 kPa$)** |
| $120.0$ | $393.15$ | $146.07$ | $390.0$ | $+4.920$ | $+5.228$ | Autoclave / pressurized steam |

### 5. Non-Contact Infrared (IR) Thermometers & the Clear-Cup / Foil Emissivity Traps

A handheld IR thermometer uses a germanium or Fresnel silicon lens to focus mid-infrared thermal radiation in the atmospheric window $\lambda \in 8–14 µm$ onto a thermopile detector at ambient housing temperature $T_{\mathrm{amb}}$  **[S12]**. For an opaque gray target of true mid-IR emissivity $\varepsilon_{\mathrm{true}}$ and reflectance $\rho_{\mathrm{true}} = 1 - \varepsilon_{\mathrm{true}}$ at temperature $T_{\mathrm{obj}}$ surrounded by background walls at $T_{\mathrm{amb}}$, the total radiosity leaving the target is $J = \varepsilon_{\mathrm{true}}\sigma T_{\mathrm{obj}}^4 + (1 - \varepsilon_{\mathrm{true}})\sigma T_{\mathrm{amb}}^4$. A background-compensated IR thermometer configured with user emissivity setting $\varepsilon_{\mathrm{set}}$ (typically fixed at $\varepsilon_{\mathrm{set}} = 0.95$) solves $\varepsilon_{\mathrm{set}}\sigma T_{\mathrm{read}}^4 + (1 - \varepsilon_{\mathrm{set}})\sigma T_{\mathrm{amb}}^4 = J$, yielding the exact apparent temperature read by the IR gun:

$$
\begin{aligned}

  \boxed{T_{\mathrm{read}} = \left[T_{\mathrm{amb}}^4 + \frac{\varepsilon_{\mathrm{true}}}{\varepsilon_{\mathrm{set}}}\left(T_{\mathrm{obj}}^4 - T_{\mathrm{amb}}^4\right)\right]^{1/4} \quad (\text{all }T\text{ in }K)}
\end{aligned}
$$

### [TRAP & DIAGNOSTIC: Four Critical Infrared Thermometer Traps in 2027 Thermodynamics Testing]
- **Trap 1 — Shooting Through the Clear `#1 PET` / `#5 PP` Plastic Cup Sidewall or Cling-Wrap Glazing:** 
  Because water and plastics are visually transparent at $\lambda = 0.4–0.7 µm$, students falsely assume an IR thermometer can “see through” a clear $9 oz$ plastic cup wall or a plastic cling-wrap cover to read the water inside. In the $8–14 µm$ thermal-IR band, glass and clear plastics ($\ge0.3 mm$ PET/PP) are **virtually opaque** ($\tau_{\mathrm{MIR}} < 0.05\text{--}0.25$, $\varepsilon_{\mathrm{MIR}} \approx 0.90\text{--}0.94$)  **[S12]**! Shooting an IR gun at the cup sidewall or through an unremoved top plastic film measures the **cooler exterior plastic temperature**, not the water! Under Official Clarification `#5` and the ES Guide  **[S02,S05]**, any team-placed film or lid **must be completely removed from the cup** during the 1-minute Final Measurement window so the ES thermometer views or contacts the bare top water surface directly.
- **Trap 2 — Shooting at Bare Liquid Water Surface (Why Top-Down IR Works Well on Open Water):**
  In the $8–14 µm$ band, liquid water has an absorption coefficient $\mu_a > 600 /cm$ (penetration depth $\delta_p < 17 µm$) and a hemispherical emissivity of $\varepsilon_w = \mathbf{0.96}$ at $40 °C$ (normal-incidence $\varepsilon_{w,n} = 0.985$, Lienhard Table 10.1 p. 546  **[S12]**). Thus, an IR gun preset to $\varepsilon_{\mathrm{set}} = 0.95$ aimed vertically downward at bare water reads within $+0.2 °C$ of the true surface skin temperature (which is slightly cooled by evaporation once uncovered).
- **Trap 3 — Shooting at Polished Metals or Aluminum Foil ($\varepsilon_{\mathrm{true}} = 0.04$):**
  On shiny aluminum foil ($\varepsilon_{\mathrm{true}} = 0.04$, $\rho_{\mathrm{true}} = 0.96$), $96\%$ of the IR radiation entering the gun is reflected room background! By Eq. (`eq:17:ir`), a $44.0 °C$ aluminum cone liner in a $22.0 °C$ room reads only $23.0 °C$ on an IR gun with $\varepsilon_{\mathrm{set}} = 0.95$ — a $-21.0 °C$ error! To measure a shiny metal surface with an IR gun, apply a patch of matte black electrical tape or flat black paint ($\varepsilon = 0.95$) and target the patch.
- **Trap 4 — Distance-to-Spot Ratio ($D:S$) Field-of-View Spillover:** 
  An IR gun with optical ratio $D:S = 12:1$ held at distance $d$ views a circular spot of diameter $D_{\mathrm{spot}} = d / 12$. Because the $9 oz$ cup water surface has diameter $D_{\mathrm{water}} \approx 6.8 cm$, holding a $12:1$ IR gun farther than $d_{\max} = 12 \times (4.5 cm\text{ safe central zone}) = 54 cm$ causes the sensor spot to spill over onto the cooler cup rim and table, averaging down $T_f$! Always hold the IR gun at $d = 15–30 cm$ ($D_{\mathrm{spot}} = 1.3–2.5 cm$) centered directly over the cup.

### Worked Example — Liquid-in-Glass Capillary Design & Partial-Immersion Stem Correction `[Rule 4.f & 5.c.i]`

A spirit-in-glass laboratory thermometer uses ethanol ($\beta_{\mathrm{liq}} = 1.120×10^{-3} /K$) in a borosilicate glass bulb ($\alpha_g = 3.30×10^{-6} /K$) of internal volume $V_0 = 250.0 mm^3$ connected to a capillary bore of diameter $d_c = 0.400 mm$. (a) Calculate the linear scale sensitivity $S_L = \Delta L/\Delta T$ in $mm/K$. (b) During a hot-water bath check, the thermometer reads $T_{\mathrm{read}} = 65.00 °C$, but an emergent column of length equivalent to $N = 45.0 °C$ protrudes above the immersion line into ambient air at $T_{\mathrm{stem}} = 23.0 °C$ ($k_g = 0.00104 /°C$). Find the true bath temperature $T_{\mathrm{true}}$.
**Solution.**
(a) Apparent expansion coefficient: $\beta_{\mathrm{app}} = \beta_{\mathrm{liq}} - 3\alpha_g = 1.120×10^{-3} - 3(3.30×10^{-6}) = 1.1101×10^{-3} /K$. Capillary cross-sectional area: $A_c = \frac{\pi}{4}(0.400 mm)^2 = 0.125664 mm^2$. By Eq. (`eq:17:lig`):
$$S_L = \frac{\Delta L}{\Delta T} = \frac{V_0 \beta_{\mathrm{app}}}{A_c} = \frac{(250.0 mm^3)(1.1101×10^{-3} /K)}{0.125664 mm^2} = \mathbf{2.2085 mm/K}$$
(b) By Eq. (`eq:17:stem`), the emergent column correction is $\Delta T_{\mathrm{stem}} = k_g N (T_{\mathrm{read}} - T_{\mathrm{stem}}) = (0.00104)(45.0)(65.00 - 23.0) = +1.9656 °C$, so:
$$T_{\mathrm{true}} = 65.00 + 1.9656 = \mathbf{66.97 °C}$$

**✓ Verified by:** Independent volumetric balance $\Delta V_{\mathrm{app}}(1 K) = 0.277525 mm^3 = A_c(2.20847 mm)$ and Python check `sec17:ex17.1` ($\Delta T_{\mathrm{stem}} = +1.9656 °C$).

### Worked Example — NTC Thermistor $\beta$-Model Inversion, Sensitivity & Self-Heating Audit `[Rule 4.f]`

An Event Supervisor's digital probe uses a $10.00 kΩ$ NTC thermistor ($R_0 = 10000 Ω$ at $T_0 = 25.00 °C = 298.15 K$, $\beta = 3892 K$, dissipation constant in water $\delta_{\mathrm{diss}} = 6.50 mW/K$) connected in a voltage divider with $R_s = 10.00 kΩ$ and $V_{\mathrm{ref}} = 3.30 V$. When immersed in the heated cup, the thermistor resistance is $R = 4912.0 Ω$. Find: (a) the water temperature in $°C$, (b) the fractional sensitivity $\alpha_R$ and $\frac{dR}{dT}$ at that temperature, and (c) the Joule self-heating bias $\Delta T_{\mathrm{SH}}$.
**Solution.**
(a) From Eq. (`eq:17:beta`):
$$\frac{1}{T} = \frac{1}{298.15 K} + \frac{1}{3892 K}\ln\!\left(\frac{4912.0}{10000.0}\right) = 3.3540164×10^{-3} - 1.826699×10^{-4} = 3.1713465×10^{-3} /K \implies T = 315.3235 K = \mathbf{42.17 °C}$$
(b) Fractional sensitivity: $\alpha_R = -\frac{\beta}{T^2} = -\frac{3892}{(315.3235)^2} = \mathbf{-0.03914 /K} = \mathbf{-3.914 %/K}$, so $\frac{dR}{dT} = \alpha_R R = (-0.039144)(4912.0) = \mathbf{-192.3 Ω/K}$.
(c) Divider current: $I = \frac{3.30}{10000 + 4912.0} = 0.22130 mA$. Electrical dissipation: $P_{\mathrm{elec}} = I^2 R = (2.2130×10^{-4})^2(4912.0) = 0.24056 mW$. By Eq. (`eq:17:selfheat`), $\Delta T_{\mathrm{SH}} = \frac{0.24056 mW}{6.50 mW/K} = \mathbf{+0.0370 °C}$ (well below the $0.1 °C$ display resolution; however, in still air where $\delta_{\mathrm{diss}} \approx 1.0 mW/K$, $\Delta T_{\mathrm{SH}}$ rises to $+0.24 °C$!).

**✓ Verified by:** Forward substitution $R(315.3235 K) = 10000\exp[3892(1/315.3235 - 1/298.15)] = 4912.00 Ω$ and Python check `sec17:ex17.2`.

### Worked Example — `Pt100` RTD Lead-Resistance Bias & IR Pyrometer Emissivity Audit `[Rule 4.f]`

(a) A 2-wire `Pt100` RTD ($R_0 = 100.00 Ω$, $A = 3.9083×10^{-3} /°C$, $B = -5.775×10^{-7} /sq·°C$) has two extension leads of resistance $R_{\mathrm{lead}} = 0.350 Ω$ each. If the meter reads total loop resistance $R_{\mathrm{meas}} = 117.47 Ω$, find the true water temperature $t_{\mathrm{true}}$ vs. the uncorrected 2-wire reading $t_{\mathrm{app}}$.
(b) An IR thermometer ($\varepsilon_{\mathrm{set}} = 0.95$, ambient room $T_{\mathrm{amb}} = 22.00 °C = 295.15 K$) is aimed at bare water ($\varepsilon_w = 0.96$) at $T_{\mathrm{obj}} = 44.00 °C = 317.15 K$, and then at the collector's shiny aluminum-foil cone ($\varepsilon_{\mathrm{Al}} = 0.04$) also at $44.00 °C$. Compute both IR readings.
**Solution.**
(a) Subtracting the two-lead loop resistance $2R_{\mathrm{lead}} = 0.700 Ω$ gives true RTD resistance $R_{\mathrm{true}} = 117.47 - 0.700 = 116.77 Ω$. Solving the Callendar–Van Dusen quadratic Eq. (`eq:17:cvd`), $100.00(1 + 3.9083×10^{-3}t - 5.775×10^{-7}t^2) = R$:
$$t = \frac{-A + \sqrt{A^2 - 4B(1 - R/R_0)}}{2B} \implies t_{\mathrm{true}}(116.77 Ω) = \mathbf{43.18 °C}, \qquad t_{\mathrm{app}}(117.47 Ω) = \mathbf{45.00 °C}$$
The 2-wire lead bias is $t_{\mathrm{app}} - t_{\mathrm{true}} = \mathbf{+1.815 °C}$ (eliminated by a 3-wire or 4-wire Kelvin probe).
(b) Using the background-compensated IR radiometer equation Eq. (`eq:17:ir`) with $T_{\mathrm{amb}} = 295.15 K$ and $T_{\mathrm{obj}} = 317.15 K$:
$$T_{\mathrm{read,water}} = \left[295.15^4 + \frac{0.96}{0.95}\left(317.15^4 - 295.15^4\right)\right]^{1/4} - 273.15 = 317.358 - 273.15 = \mathbf{44.21 °C} \quad (+0.21 °C\text{ offset})$$
$$T_{\mathrm{read,foil}} = \left[295.15^4 + \frac{0.04}{0.95}\left(317.15^4 - 295.15^4\right)\right]^{1/4} - 273.15 = 296.180 - 273.15 = \mathbf{23.03 °C} \quad (-20.97 °C\text{ error!})$$

**✓ Verified by:** Quadratic verification $100(1 + 3.9083×10^{-3}(43.1842) - 5.775×10^{-7}(43.1842)^2) = 116.770 Ω$ and Python check `sec17:ex17.3`.

## Metrology Fundamentals, Parallax, Balances, Timers & Volumetric Repeatability

### 1. Resolution vs. Precision vs. Accuracy vs. Sensitivity
- **Resolution ($\Delta_{\mathrm{res}}$):** The smallest increment distinguishable on a display or scale (e.g., $\Delta_{\mathrm{res}} = 0.1 °C$ required by Rule `4.f`). On an analog scale with graduation spacing $\Delta_{\mathrm{grad}}$, human interpolation resolves $\Delta_{\mathrm{res}} \approx \Delta_{\mathrm{grad}}/5$ to $\Delta_{\mathrm{grad}}/2$, whereas a digital display has hard quantization $\Delta_{\mathrm{res}} = 1\text{ LSD}$ (least significant digit), creating a rectangular Type B rounding uncertainty $u_{B,\mathrm{res}} = \frac{\Delta_{\mathrm{res}}}{2\sqrt{3}} \approx 0.2887\,\Delta_{\mathrm{res}}$ (§`sec:17.6`)  **[S21]**.
- **Precision (Repeatability / Random Scatter):** Closeness of agreement among independent repeated measurements under identical conditions, quantified by sample standard deviation $s$ and Type A standard uncertainty of the mean $u_A = s/\sqrt{n}$. High precision means small random noise, even if all readings share a constant offset.
- **Accuracy (Trueness / Low Systematic Bias):** Closeness of agreement between the mean measured value and the true NIST/SI reference value. Systematic bias $\delta_{\mathrm{sys}} = \bar{T}_{\mathrm{meas}} - T_{\mathrm{true}}$ is reduced only by physical calibration (§`sec:17.5`) or differential cancellation.
- **Why Rule `4.f` (“Same Thermometer for Start & Final Reading”) Cancels Zero-Offset Bias in $\mathrm{TG}$:** 
  Suppose the ES thermometer has a constant additive zero-offset bias $\delta_{\mathrm{sys}}$ (e.g., reads $+0.6 °C$ high across $20–50 °C$): $T_{\mathrm{start,read}} = T_{\mathrm{start,true}} + \delta_{\mathrm{sys}}$ and $T_{f,\mathrm{read}} = T_{f,\mathrm{true}} + \delta_{\mathrm{sys}}$.
- In the **Temperature Score ($\mathrm{TS}$, 30 pts, Rule `6.e`)**, which depends on Temperature Gain $\mathrm{TG} = T_{f,\mathrm{read}} - T_{\mathrm{start,read}} = (T_{f,\mathrm{true}} + \delta_{\mathrm{sys}}) - (T_{\mathrm{start,true}} + \delta_{\mathrm{sys}}) = \mathrm{TG}_{\mathrm{true}}$, the additive zero offset $\delta_{\mathrm{sys}}$ **cancels identically**!
- In the **Prediction Score ($\mathrm{PS}$, 20 pts, Rule `6.f`)**, $\mathrm{PE} = 1 - \frac{|T_{f,\mathrm{read}} - T_{\mathrm{pred}}|}{T_{f,\mathrm{read}}}$. Because the ES announces $T_{\mathrm{start,read}}$ measured with that **same** offset thermometer (`Rule 5.II.c`) and your team computes $T_{\mathrm{pred}} = T_{\mathrm{start,read}} + \widehat{\mathrm{TG}}$, the numerator $|T_{f,\mathrm{read}} - T_{\mathrm{pred}}| = |(T_{f,\mathrm{true}} + \delta_{\mathrm{sys}}) - (T_{\mathrm{start,true}} + \delta_{\mathrm{sys}} + \widehat{\mathrm{TG}})| = |\mathrm{TG}_{\mathrm{true}} - \widehat{\mathrm{TG}}|$ **also cancels $\delta_{\mathrm{sys}}$ identically**! Always anchor your prediction equation directly to the ES-announced $T_{\mathrm{start}}$ (§`sec:16`).
  

### 2. Meniscus Parallax, Digital Balances, Timers & $100 mL$ Water Dispensing Repeatability

**Table:** Laboratory Metrology Standards for Volume, Mass, Time, and Meniscus Reading in Calibration Labs  **[S05,S09,S21]**.

| **Measurement / Instrument** | **Governing Physics & Systematic Bias Formula** | **Typical Uncertainty** | **Best-Practice Protocol for 2027 Device Calibration** |
| --- | --- | --- | --- |
| **Meniscus & Parallax** <br> (Graduated cylinder & spirit thermometer) | Line-of-sight angle $\theta$ off horizontal across bore-to-scale gap $d_g$ shifts reading by $\Delta y_{\mathrm{par}} = d_g \tan\theta \approx d_g(\Delta z_{\mathrm{eye}} / L_{\mathrm{eye}})$. | $\pm0.2–0.5 mL$ or $\pm0.3 °C$ if viewed at angle | Water & ethanol wet glass (adhesion $>$ cohesion $\implies$ **concave meniscus**: read **bottom** of trough at eye level). Mercury does not wet glass (**convex**: read top of dome). |
| **Volumetric $100 mL$ Dispensing** (`Rule 3.a, 5.II.c`) | Thermal capacity of water $C_w = \rho_w(T)\,V_w\,c_{p,w}$ scales linearly with volume: $\dfrac{\delta(\mathrm{TG})}{\mathrm{TG}} \approx -\dfrac{C_w}{C_{\mathrm{eff}}}\dfrac{\delta V_w}{V_w}$ ($\approx -0.20 °C$ per $+1.0 mL$ error at $\mathrm{TG}=20 °C$!). | Beaker: $\pm5 mL$ <br> Class B cyl: $\pm1.0 mL$ <br> Class A cyl: $\pm0.5 mL$ <br> Gravimetric: $\pm0.05 mL$ | During pre-tournament DOE calibration (§`sec:16`), always dispense the $100.0 mL$ water sample **gravimetrically on a $0.01 g$ digital balance** so volume scatter never corrupts your calibration curve! |
| **Gravimetric Mass-to-Volume & Air Buoyancy** **[S09,S21]** | True mass $m_{\mathrm{true}} = m_{\mathrm{bal}}\dfrac{1 - \rho_{\mathrm{air}}/\rho_{\mathrm{cal}}}{1 - \rho_{\mathrm{air}}/\rho_w} \approx m_{\mathrm{bal}}\left[1 + \rho_{\mathrm{air}}\!\left(\dfrac{1}{\rho_w} - \dfrac{1}{\rho_{\mathrm{cal}}}\right)\right] = 1.00106\,m_{\mathrm{bal}}$ ($\rho_{\mathrm{air}} = 1.20 kg/m^3$, steel calibration weight $\rho_{\mathrm{cal}} = 8000 kg/m^3$). | Balance: $\pm0.01 g$ <br> Buoyancy + $\rho_w(T)$ shift: $0.33 g$ at $22 °C$ | At $T = 22.0 °C$, $\rho_w = 0.99777 g/mL$ **[S09]**; accounting for air buoyancy ($1.00106$), $100.00 mL$ of water weighs exactly $m_{\mathrm{bal}} = \dfrac{99.777 g}{1.00106} = \mathbf{99.67 g}$ on a tared digital scale (at $20.0 °C$, $99.72 g$; at $25.0 °C$, $99.60 g$). |
| **Digital Stopwatch & AC Line Voltage** | Heating gain scales as $\dfrac{\partial T_f}{\partial t} \approx 1.5 °C/min = 0.025 °C/s$; incandescent lamp power scales with AC mains voltage as $P_{\mathrm{bulb}} \propto (V_{\mathrm{AC}}/V_0)^{1.54}$. | Human reaction: $\pm0.2 s$ ($\pm0.005 °C$) <br> Mains voltage: $\pm3%$ | Stopwatch reaction error is negligible, but a $3%$ building AC line voltage sag ($120 V \to 116.4 V$) reduces heat-lamp output by $1.54 \times 3% = 4.6%$. Log Kill-A-Watt power meter readings during calibration runs. |

## Dynamic Probe Response Time ($\tau_p$), First-Order Thermal Lag & the $5\tau_p$ Settling Rule

When a thermometer probe of sensing-tip mass $m_p$, specific heat $c_p$, wetted surface area $A_p$, and internal thermal conductivity $k_p$ (with probe Biot number $\mathrm{Bi}_p = \frac{h_p r_p}{2 k_p} < 0.1$) is transferred at $t = 0$ from ambient room air at $T_{p,0}$ into liquid water at temperature $T_w$, convective heat transfer across the probe boundary layer ($h_p$) governs the probe reading $T_p(t)$ via a first-order linear energy balance  **[S12]**:

$$
\begin{aligned}

  m_p c_p \frac{dT_p}{dt} = h_p A_p \left[T_w - T_p(t)\right] \implies \tau_p \frac{dT_p}{dt} + T_p(t) = T_w, \qquad \tau_p = \frac{m_p c_p}{h_p A_p} = R_{\mathrm{th},p}\,C_p
\end{aligned}
$$

### [FORMULA & DECISION CARD: First-Order Probe Step Response, $5\tau_p$ Settling Rule, Ramp Lag & Probe Thermal Drain]
- **Step-Immersion Response & Dynamic Fractional Lag Error:**
  
$$
\begin{aligned}

    T_p(t) = T_w - \left(T_w - T_{p,0}\right)e^{-t/\tau_p}, \qquad E_{\mathrm{frac}}(t) = \frac{T_w - T_p(t)}{T_w - T_{p,0}} = e^{-t/\tau_p}, \qquad f_{\mathrm{settled}}(t) = 1 - e^{-t/\tau_p}
\end{aligned}
$$

  
  
  
| **Elapsed Time $t/\tau_p$** | $1\tau_p$ | $2\tau_p$ | $3\tau_p$ | $4\tau_p$ | $\mathbf{5\tau_p}$ **(Rule)** | $6\tau_p$ |
| --- | --- | --- | --- | --- | --- | --- |
| **Fraction Settled $1 - e^{-t/\tau_p}$** | $63.21%$ | $86.47%$ | $95.02%$ | $98.17%$ | $\mathbf{99.326%}$ | $99.752%$ |
| **Remaining Error $e^{-t/\tau_p}$** | $36.79%$ | $13.53%$ | $4.98%$ | $1.83%$ | $\mathbf{0.674%}$ | $0.248%$ |
| **Lag Error for $\Delta T = 25.0 °C$ Step** | $-9.20 °C$ | $-3.38 °C$ | $-1.24 °C$ | $-0.46 °C$ | $\mathbf{-0.17 °C}$ | $-0.06 °C$ |
- **Two-Point Algebraic Extraction of Probe Time Constant $\tau_p$ (Zero Calculus Required):** 
  From any two probe readings $T_p(t_1)$ and $T_p(t_2)$ during step immersion into a constant-temperature bath $T_w$:
  
$$
\begin{aligned}

    \tau_p = \frac{t_2 - t_1}{\ln\!\left(\dfrac{T_w - T_p(t_1)}{T_w - T_p(t_2)}\right)}
\end{aligned}
$$
- **Dynamic Ramp Lag During Continuous Heating ($T_w(t) = T_{w,0} + r\,t$):** 
  If a thermometer probe remains immersed while water warms at rate $r = \frac{dT_w}{dt}$ $[°C/s]$, the exact steady-ramp solution to $\tau_p \frac{dT_p}{dt} + T_p = T_{w,0} + rt$ is:
  
$$
\begin{aligned}

    T_p(t) = T_w(t) - r\tau_p\left(1 - e^{-t/\tau_p}\right) \xrightarrow{t \ge 5\tau_p} T_p(t) - T_w(t) = -r\,\tau_p
\end{aligned}
$$

  *(During continuous heating at $r = 2.4 °C/min = 0.040 °C/s$, a slow spirit thermometer with $\tau_p = 10 s$ constantly trails the true water temperature by $-r\tau_p = -0.40 °C$!)*
- **Calorimetric Probe Heat-Capacity Perturbation ($\Delta T_{\mathrm{drain}}$):** 
  When a cold probe of effective submerged heat capacity $C_p = m_p c_p$ initially at room temperature $T_{p,0}$ is dipped into an unstirred top water layer of effective heat capacity $C_{\mathrm{top}}$ initially at $T_{w,0}$, thermal equilibration cools the local water layer to:
  
$$
\begin{aligned}

    T_{\mathrm{eq}} = \frac{C_{\mathrm{top}} T_{w,0} + C_p T_{p,0}}{C_{\mathrm{top}} + C_p} \implies \Delta T_{\mathrm{drain}} = T_{\mathrm{eq}} - T_{w,0} = -\frac{C_p}{C_{\mathrm{top}} + C_p}\left(T_{w,0} - T_{p,0}\right)
\end{aligned}
$$

> **[Vector Figure: First-order thermometer probe step response $1 - e^{-t/\tau_p}$ and fractional dynamic lag error $e^{-t/\tau_p}$ versus dimensionless immersion time $t/\tau_p$. A probe with $\tau_p = 4.0 s$ must remain immersed for $\ge 5\tau_p = 20.0 s$ to reduce dynamic lag below $0.67\%$ of $\Delta T$  **[S12,S21]**. | Label: `fig:17:thermometer-response`]**
> - **Diagram Annotations & Key Elements:** **X-Axis:** Dimensionless Immersion Time $t / \tau_p$ (for $\tau_p = 4.0 s$, $1\tau_p = 4 s$ and $5\tau_p = 20 s$) • **Y-Axis:** Normalized Response / Fractional Error • **Legend:** Probe Step Response $\dfrac{T_p(t) - T_{p,0}}{T_{\mathrm{true}} - T_{p,0}} = 1 - e^{-t/\tau_p}$ • **Legend:** Fractional Lag Error $E_{\mathrm{frac}}(t) = \dfrac{T_{\mathrm{true}} - T_p(t)}{\Delta T} = e^{-t/\tau_p}$ • **Legend:** Initial Slope Tangent at $t=0$: $(d\theta/dt)_0 = 1/\tau_p$ • $1\tau_p$: $63.2\%$ ($36.8\%$ err) • $3\tau_p$: $95.0\%$ ($5.0\%$ err) • $5\tau_p$ Settling Threshold: $99.33\%$ settled ($0.67\%$ err $< 0.17 °C$)

## Immersion Depth, Stem Conduction & Radial Stratification Bias (`Clarifications #1–#4`)

### [2027 OFFICIAL RULE / CLARIFICATION: 2027 Official National Clarifications `#1–#4`: Unstirred Stratified Cup & Top-Layer Measurement  **[S02,S05]**]
- **Clarifications `#1, #2, #3` (`09/30/2026–10/06/2026`):** *“No, the water must not be swirled, shaken or stirred before taking the temperature.”*
- **Clarification `#4` (`10/06/2026`, Sec. 5 / Par. II.g):** *“It is recommended that the ES should measure the temperature of the top layer of water near the center of the cup. If the thermometer has a probe, the ES should insert it far enough into the water to take an accurate measurement, but no farther.”*

Why does probe placement inside the $100 mL$ water column ($38 mm$ total fill depth in a standard $9 oz$ clear cup) shift the measured temperature $T_f$ by up to $4.0–8.5 °C$?
- **Vertical Optical Deposition & Hydrostatic Stability ($z$-Axis Bias):**
  As established by the Hale & Querry (1973) and Kou et al. (1993) liquid-water near-IR absorption spectra (§`sec:14`, §`sec:15.3`)  **[S19,S20]**, $>66\%$ of the $2400 K$ tungsten heat lamp's transmitted radiant energy is absorbed directly inside the **top $z = 5 mm$** of water ($>72\%$ in the top $10 mm$). Because liquid water above $4 °C$ expands when heated ($\partial\rho/\partial T < 0$), the hot top water layer is less dense than the cooler water beneath it ($\partial\rho/\partial z > 0$ downward). This gravitationally stable density profile completely suppresses vertical natural-convection overturning ($\mathrm{Ra} < 0$), trapping heat in the upper $5–15 mm$ stratum while heat trickles downward only via slow molecular conduction ($\alpha_w = 1.45×10^{-7} m^2/s$, diffusion depth $\delta_{\mathrm{th}} = \sqrt{4\alpha_w t} \approx 18.7 mm$ after $10 min$)  **[S12]**.
- **Uncovered Surface Evaporative Skin Cooling ($z = 0–1.5 mm$):**
  The instant the cup is uncovered at the end of Heating Time (`Rule 5.II.g`), evaporative latent heat loss ($\dot{Q}_{\mathrm{evap}} \approx 2.2–4.4 W$, §`sec:15.4`) cools the uppermost $1 mm$ free-surface skin by $0.4–0.9 °C$ within $15–30 s$. Consequently, the **peak water temperature** sits just below the evaporative surface boundary layer at depth $\mathbf{z_{\mathrm{opt}} = 5–12 mm}$ — the exact zone targeted by an electronic probe tip under Clarification `#4`!
- **Radial Sidewall Cooling Boundary Layer ($r$-Axis Bias):**
  Along the vertical plastic cup wall ($r = R_{\mathrm{water}} \approx 33.8 mm$), radial heat loss to the ambient room cools a $\delta_T \approx 3–5 mm$ natural-convection boundary layer, creating a downward-sinking wall plume that feeds cool water to the cup bottom while leaving the central core ($r < 12 mm$) $0.6–1.8 °C$ warmer than the perimeter wall (Fig. `fig:17:probe-depth-bias`).
- **Probe Stem Conduction Error at Ultra-Shallow Immersion ($z < 4 mm$):** 
  A stainless-steel probe sheath ($k_{\mathrm{ss}} \approx 15 W/m/K$, diameter $d_p = 3.2 mm$) acts as a conductive fin protruding into $22 °C$ room air. If immersed only $2 mm$ deep so part of the internal thermistor/RTD element sits above the waterline, axial stem conduction pulls the sensor reading down by $0.8–2.5 °C$. Immersing the tip to $z = 8–12 mm$ ($2.5\text{--}4$ sheath diameters) submerges the entire active thermistor/thermocouple bead inside the peak isothermal stratum while minimizing stem-fin cooling.

!{

> **[Vector Figure: Original Vector Technical Diagram | Label: `fig:diagram`]**
> - **Diagram Annotations & Key Elements:** CLARIF. #4 TARGET ZONE / [-1pt]$z=5–12 mm,\ r<10 mm$ / [-1pt]$\mathbf{T_{\mathrm{top}} = 45.2 °C}$ • Bottom Cold Layer ($z=24–38 mm$): $T_{\mathrm{bot}} = 37.8–39.2 °C$ / [-1pt](Bias if pushed to bottom: $\mathbf{-6.0–7.4 °C}$!) • Thermocline Transition ($z=12–24 mm$): $T = 40.5–43.8 °C$ • Wall Plume $-1.4 °C$ • Probe A (Correct Clarif. #4 Center Tip) • Probe B (Bottom/Wall Error) / [-1pt]Reads $38.4 °C$ ($-6.8 °C$ bias) • IR Gun Spot ($z=15 µm$ skin) / [-1pt]$\varepsilon_w=0.96,\ T_{\mathrm{skin}}\approx44.6 °C$ • Measured Stratification Map $T(z,r)$ ($t=10 min$, $h=45 cm$) • **Calibration Rule:** Clamp practice probe at $z=8± 2 mm,\ r=0 mm$!

**Figure:** Thermometer immersion depth ($z$) and radial placement ($r$) bias inside an unstirred, top-heated $9 oz$ cup containing $100 mL$ of water (`Official Clarifications #1–#4`). Top-down near-IR absorption creates a buoyantly stable hot upper stratum ($z = 5–12 mm$) that exceeds the swirled bulk average by $+3.6 °C$ and the bottom boundary by $+7.1 °C$  **[S02,S05,S19]**.

## Fixed-Point Thermometer Calibration: Ice Bath ($0.00 °C$) & Barometric Steam Point

To verify or calibrate team thermometers before building the 36-run DOE calibration table (§`sec:16.2`), perform a two-point fixed-temperature calibration against the **ice point ($0.00 °C = 273.15 K$)** and the **barometric-corrected steam boiling point ($T_{\mathrm{boil}}(P_{\mathrm{atm}})$)**  **[S09,S21,S22]**:
- **Ice-Point Reference Bath ($T_{\mathrm{ice}} = 0.00 °C$ at $1 atm$):** 
  Pack a clean Dewar or insulated foam cup **all the way to the bottom** with finely shaved or crushed ice made from distilled water, then add just enough chilled distilled water to fill the pore spaces between ice crystals ($75–80 %$ solid ice, $20–25 %$ liquid water; slush looks wet and translucent, with **zero free-floating ice gap at the bottom**).
  *Why bottom-packed ice is critical:* Because liquid water reaches maximum density $\rho_{\max} = 999.97 kg/m^3$ at $+3.984 °C$ (§`sec:03`)  **[S09]**, if ice cubes merely float at the top of a cup of water, dense $+4 °C$ water sinks to the bottom, causing a deep probe to read $+1.5–4.0 °C$ instead of $0.00 °C$! Wait $3 min$, insert the probe into the central slush zone without touching the container walls, wait $\ge 5\tau_p$, and record $T_{\mathrm{read,ice}}$. The zero-offset error is $\delta_0 = T_{\mathrm{read,ice}} - 0.00 °C$. *(Note: Dissolved air depresses the freezing point of air-saturated water by only $-0.0024 °C$ relative to the $0.0100 °C$ triple point, and barometric pressure shifts the ice point by $\frac{dT_m}{dP} = -0.00743 °C/atm$, which is negligible on a $0.1 °C$ probe  **[S11]**).*
- **Altitude / Barometric-Pressure Corrected Steam Boiling Point ($T_{\mathrm{boil}}(P_{\mathrm{atm}})$):**
  Water boils at exactly $100.00 °C$ ($T_{90} = 99.974 °C$ on ITS-90  **[S09]**) **only** at standard sea-level pressure $P_0 = 101.325 kPa = 760.00 mm Hg$. Because $P_{\mathrm{atm}}$ drops with elevation $z_{\mathrm{alt}}$ $[m]$ as $P_{\mathrm{atm}}(z_{\mathrm{alt}}) \approx 101.325 kPa\left(1 - 2.2558×10^{-5}\,z_{\mathrm{alt}}\right)^{5.2559}$ ($\approx -1.2 kPa$ or $-9.0 mm Hg$ per $+100 m$ elevation) and fluctuates by $\pm2.5 kPa$ with weather fronts, calibrating a thermometer in boiling water without correcting for local barometric pressure introduces a $0.5–3.0 °C$ systematic error! From the NIST IAPWS-95 saturation curve around $100 °C$ ($\frac{dT_{\mathrm{sat}}}{dP} = \frac{T v_{fg}}{h_{fg}} = 0.2765 K/kPa = 0.03686 K/mm·Hg$)  **[S09]**:
  
$$
\begin{aligned}

    T_{\mathrm{boil}}(P_{\mathrm{mmHg}}) &= 100.00 °C + 0.03686\left(P_{\mathrm{mmHg}} - 760.0\right) - 0.000020\left(P_{\mathrm{mmHg}} - 760.0\right)^2 \\[2pt]
    T_{\mathrm{boil}}(P_{\mathrm{kPa}})  &= 100.00 °C + 0.2765\left(P_{\mathrm{kPa}} - 101.325\right) - 0.00112\left(P_{\mathrm{kPa}} - 101.325\right)^2
\end{aligned}
$$

  *(Suspend the probe in the condensing saturated steam just above the boiling distilled water surface or in a vigorously rolling bath with boiling chips to avoid $+0.2–0.6 °C$ liquid superheating at the heated vessel bottom).*
- **Two-Point Linear Calibration Correction Equation:** 
  Given raw thermometer reading $T_{\mathrm{raw}}$, ice-bath reading $T_{\mathrm{read,ice}}$ (at true $0.00 °C$), and steam-point reading $T_{\mathrm{read,boil}}$ (at true $T_{\mathrm{boil}}(P_{\mathrm{atm}})$):
  
$$
\begin{aligned}

    \boxed{T_{\mathrm{true}} = T_{\mathrm{boil}}(P_{\mathrm{atm}}) \times \frac{T_{\mathrm{raw}} - T_{\mathrm{read,ice}}}{T_{\mathrm{read,boil}} - T_{\mathrm{read,ice}}}}
\end{aligned}
$$

### Worked Example — 5$\tau_p$ Premature-Reading Audit, Probe Heat Drain & Two-Point Barometric Calibration `[Rule 4.f & 5.II.g]`

(a) A stainless-sheathed digital probe ($\tau_p = 3.20 s$, effective tip heat capacity $C_p = 0.450 J/K$, initial room temperature $T_{p,0} = 21.50 °C$) is inserted into the top stratified water layer ($C_{\mathrm{top}} = 185.0 J/K$, initial temperature $T_{w,0} = 46.50 °C$). Compute the true equilibrium temperature $T_{\mathrm{eq}}$ after probe thermal drain, the premature reading if recorded at $t = 6.40 s$ ($2\tau_p$), and the settled reading at $t = 5\tau_p = 16.0 s$.
(b) During pre-tournament calibration on a day when local barometric pressure is $P_{\mathrm{atm}} = 742.0 mm Hg$, the probe reads $T_{\mathrm{read,ice}} = -0.30 °C$ in an ice bath and $T_{\mathrm{read,boil}} = 98.90 °C$ in saturated steam. If the probe reads $T_{\mathrm{raw}} = 44.20 °C$ in a trial cup, what is the true calibrated water temperature $T_{\mathrm{true}}$?
**Solution.**
(a) By Eq. (`eq:17:probedrain`), calorimetric equilibration between the $21.50 °C$ probe tip and the $46.50 °C$ top layer yields:
$$T_{\mathrm{eq}} = \frac{185.0(46.50) + 0.450(21.50)}{185.0 + 0.450} = \frac{8612.175}{185.450} = \mathbf{46.439 °C} \quad (\Delta T_{\mathrm{drain}} = -0.061 °C)$$
Using Eq. (`eq:17:probestep`) with $\Delta T_{\mathrm{step}} = 46.4393 - 21.50 = 24.9393 °C$:
$$T_p(2\tau_p = 6.40 s) = 46.4393 - 24.9393\,e^{-2} = \mathbf{43.06 °C} \quad (\text{premature reading loses }\mathbf{3.38 °C}\text{!})$$
$$T_p(5\tau_p = 16.0 s) = 46.4393 - 24.9393\,e^{-5} = \mathbf{46.27 °C} \quad (\text{within }0.17 °C\text{ of }T_{\mathrm{eq}})$$
(b) At $P_{\mathrm{atm}} = 742.0 mm Hg$ ($\Delta P = -18.0 mm Hg$), Eq. (`eq:17:tboil`) gives true steam temperature:
$$T_{\mathrm{boil}}(742.0 mm Hg) = 100.00 + 0.03686(-18.0) - 0.000020(-18.0)^2 = 100.00 - 0.66348 - 0.00648 = \mathbf{99.330 °C}$$
Applying the two-point linear calibration formula Eq. (`eq:17:2ptcal`):
$$T_{\mathrm{true}} = 99.330 °C \times \frac{44.20 - (-0.30)}{98.90 - (-0.30)} = 99.330 \times \frac{44.50}{99.20} = \mathbf{44.56 °C}$$

**✓ Verified by:** Direct linear slope/offset verification $T_{\mathrm{true}} = 1.00131(44.20 + 0.30) = 44.5583 °C$ and Python check `sec17:ex17.4`.

## JCGM GUM / NIST TN 1297 Uncertainty Propagation Framework  **[S21]**

Under the international BIPM/JCGM *Guide to the Expression of Uncertainty in Measurement* (GUM, JCGM 100:2008) and NIST Technical Note 1297  **[S21]**, every measurement uncertainty is expressed as a **standard uncertainty** $u(x_i)$ (equivalent to one standard deviation, $1\sigma$) classified by evaluation method:
- **Type A Standard Uncertainty ($u_A$ — Statistical Evaluation of Repeated Trials):**
  From $n$ independent repeated measurements $x_1, x_2, \dots, x_n$ with sample mean $\bar{x} = \frac{1}{n}\sum_{k=1}^n x_k$ and sample standard deviation $s = \sqrt{\frac{1}{n-1}\sum_{k=1}^n (x_k - \bar{x})^2}$ (with $\nu = n - 1$ degrees of freedom):
  
$$
\begin{aligned}

    u_A(\bar{x}) = \frac{s}{\sqrt{n}} = \sqrt{\frac{\sum_{k=1}^n (x_k - \bar{x})^2}{n(n - 1)}}
\end{aligned}
$$
- **Type B Standard Uncertainty ($u_B$ — Non-Statistical Prior / Specification Bounds):**
- *Manufacturer Tolerance $\pm a$ (Rectangular / Uniform Distribution on $[\bar{x}-a, \bar{x}+a]$):*
    
$$
\begin{aligned}

      u_{B,\mathrm{tol}} = \frac{a}{\sqrt{3}} \approx 0.57735\,a
\end{aligned}
$$
- *Digital Display Resolution $\Delta_{\mathrm{res}}$ (Uniform Rounding Within $\pm a = \pm\Delta_{\mathrm{res}}/2$):*
    
$$
\begin{aligned}

      u_{B,\mathrm{res}} = \frac{\Delta_{\mathrm{res}} / 2}{\sqrt{3}} = \frac{\Delta_{\mathrm{res}}}{2\sqrt{3}} \approx 0.28868\,\Delta_{\mathrm{res}} \quad (\text{for }\Delta_{\mathrm{res}} = 0.1 °C,\ u_{B,\mathrm{res}} = 0.0289 °C)
\end{aligned}
$$
- *Analog Meniscus / Scale Reading Bound $\pm a$ (Triangular Distribution Peaked at Center):* $u_{B,\mathrm{tri}} = \frac{a}{\sqrt{6}} \approx 0.40825\,a$.
- **Combined Standard Uncertainty $u_c(y)$ & Expanded Uncertainty $U = k\,u_c(y)$:**
  For a single measurand $x$ with independent Type A and Type B components, $u(x) = \sqrt{u_A^2 + u_{B,\mathrm{tol}}^2 + u_{B,\mathrm{res}}^2}$. For a derived quantity $y = f(x_1, x_2, \dots, x_N)$, the first-order Taylor expansion (Law of Propagation of Uncertainty) with sensitivity coefficients $c_i = \frac{\partial f}{\partial x_i}$ and covariance $u(x_i, x_j) = r_{ij}u(x_i)u(x_j)$ gives  **[S21]**:
  
$$
\begin{aligned}

    u_c^2(y) = \sum_{i=1}^N \left(\frac{\partial f}{\partial x_i}\right)^2 u^2(x_i) + 2\sum_{i=1}^{N-1}\sum_{j=i+1}^N \frac{\partial f}{\partial x_i}\frac{\partial f}{\partial x_j}\,r_{ij}u(x_i)u(x_j), \qquad U = k\,u_c(y)
\end{aligned}
$$

  where coverage factor $k = 2$ defines an approximately $95%$ confidence interval $y \pm U$ (or $k = t_{0.95,\nu_{\mathrm{eff}}}$ from the Student-$t$ distribution when effective degrees of freedom $\nu_{\mathrm{eff}}$ from the Welch–Satterthwaite formula $\nu_{\mathrm{eff}} = u_c^4(y)/\sum \frac{[c_i u(x_i)]^4}{\nu_i}$ are small, e.g., $\nu < 10$).

**Table:** Algebra-Only JCGM GUM Uncertainty Propagation Rules for Science Olympiad Thermodynamics (`Rule 5.d.iv` Compliant)  **[S06,S21]**.

| **Functional Relationship** | **Equation $y = f(x_1, x_2, \dots)$** | **Ready-to-Use Algebraic Uncertainty Rule** | **Thermodynamics Competition Application** |
| --- | --- | --- | --- |
| **1. Linear Sum / Difference** (Uncorrelated, $r_{ij}=0$) | $y = a x_1 + b x_2 - c x_3$ | $u_c(y) = \sqrt{a^2 u^2(x_1) + b^2 u^2(x_2) + c^2 u^2(x_3)}$ <br> *(Absolute uncertainties add in quadrature)* | $\Delta T = T_2 - T_1$ with two *different* sensors: $u(\Delta T) = \sqrt{u^2(T_2) + u^2(T_1)}$. |
| **2. Correlated Difference** (**Rule `4.f` Same Thermometer!**) | $\mathrm{TG} = T_f - T_s$ <br> ($r_{\mathrm{sys}} = +1$ for shared bias $u_{B,\mathrm{sys}}$) | $u_c(\mathrm{TG}) = \sqrt{u_{\mathrm{rand}}^2(T_f) + u_{\mathrm{rand}}^2(T_s)}$ <br> where $u_{\mathrm{rand}}^2 = u_A^2 + u_{B,\mathrm{res}}^2$ <br> *(Shared systematic tolerance $u_{B,\mathrm{sys}}$ cancels!)* | Under Rule `4.f`, the same thermometer measures $T_s$ and $T_f$: $u_{B,\mathrm{sys}}^2 + u_{B,\mathrm{sys}}^2 - 2(+1)u_{B,\mathrm{sys}}^2 = 0$! |
| **3. Product & Quotient** | $y = \dfrac{k\,x_1\,x_2}{x_3}$ | $\dfrac{u_c(y)}{\|y\|} = \sqrt{\left(\dfrac{u(x_1)}{x_1}\right)^2 + \left(\dfrac{u(x_2)}{x_2}\right)^2 + \left(\dfrac{u(x_3)}{x_3}\right)^2}$ <br> *(Fractional uncertainties add in quadrature)* | Calorimetry $Q = m c_p \Delta T$, ideal gas $P = nRT/V$, or thermal conductivity $k = \dfrac{\dot{Q} L}{A \Delta T}$. |
| **4. Power / Monomial Law** | $y = k\,x_1^a\,x_2^b\,x_3^{-c}$ | $\dfrac{u_c(y)}{\|y\|} = \sqrt{\left(a\dfrac{u(x_1)}{x_1}\right)^2 + \left(b\dfrac{u(x_2)}{x_2}\right)^2 + \left(c\dfrac{u(x_3)}{x_3}\right)^2}$ | Stefan–Boltzmann $\dot{Q} = \varepsilon\sigma A T^4 \implies \dfrac{u(\dot{Q})}{\dot{Q}} = \sqrt{\dots + \left(\mathbf{4}\dfrac{u(T)}{T}\right)^2}$; pipe area $A = \frac{\pi}{4}D^2 \implies 2\frac{u(D)}{D}$. |
| **5. Natural Logarithm & Exponential** | $y = a\ln(x)$ <br> or $z = a e^{b x}$ | $u_c(y) = \|a\|\dfrac{u(x)}{\|x\|}$ <br> $\dfrac{u_c(z)}{\|z\|} = \|b\|\,u(x)$ | Semi-log cooling plot $y = \ln(T - T_{\mathrm{ss}})$, entropy $\Delta S = mc\ln(T_2/T_1)$, or Boltzmann factor $e^{-E/(k_B T)}$. |
| **6. OLS Linear Regression Slope $m$ & Intercept $b$** | $y = m x + b$ across $N$ points $(x_i, y_i)$ | $s_{y\|x} = \sqrt{\dfrac{S_{yy} - m S_{xy}}{N - 2}}$,\quad $u(m) = \dfrac{s_{y\|x}}{\sqrt{S_{xx}}}$, <br> $u(b) = s_{y\|x}\sqrt{\dfrac{1}{N} + \dfrac{\bar{x}^2}{S_{xx}}}$ | Time constant $\tau = -1/m \implies u(\tau) = \dfrac{u(m)}{m^2} = \tau^2 u(m)$; Clausius–Clapeyron $\Delta H_{\mathrm{vap}} = -R m \implies u(\Delta H) = R\,u(m)$. |

### Worked Example — Complete JCGM GUM Uncertainty Budget for `Rule 4.f` $\mathrm{TG}$ & Specific-Heat Calorimetry `[Rules 4.f & 5.I.b]`

(a) An ES digital probe has manufacturer tolerance $\pm a_{\mathrm{sys}} = \pm0.40 °C$, display resolution $\Delta_{\mathrm{res}} = 0.10 °C$, and Type A random repeatability $u_A = 0.050 °C$. Calculate the combined standard uncertainty $u(T)$ of a single temperature reading, and compare $u_c(\mathrm{TG})$ for $\mathrm{TG} = T_f - T_{\mathrm{start}}$ when measured with two *different* probes ($r=0$) versus the *same* probe under Rule `4.f` ($r_{\mathrm{sys}} = +1$).
(b) In a calorimetry lab using that same thermometer, a metal sample of mass $m_x = 85.00 ± 0.05 g$ cooled by $\Delta T_x = 52.60 °C$ warms $m_w = 100.00 ± 0.15 g$ of water ($c_w = 4.184 J/g/K$, exact) by $\Delta T_w = 5.40 °C$ (where $u(\Delta T_w) = u(\Delta T_x) = u_{\mathrm{corr}}(\mathrm{TG}) = 0.08165 °C$). Compute $c_x$, its combined standard uncertainty $u_c(c_x)$, and the expanded uncertainty $U(c_x)$ ($k=2$).
**Solution.**
(a) From Eq. (`eq:17:typeBtol`)–Eq. (`eq:17:typeBres`): $u_{B,\mathrm{sys}} = \frac{0.40}{\sqrt{3}} = 0.23094 °C$ and $u_{B,\mathrm{res}} = \frac{0.10}{2\sqrt{3}} = 0.02887 °C$. For a single reading:
$$u(T) = \sqrt{u_{B,\mathrm{sys}}^2 + u_{B,\mathrm{res}}^2 + u_A^2} = \sqrt{0.23094^2 + 0.02887^2 + 0.050^2} = \mathbf{0.2380 °C}$$
If two independent thermometers were used ($r = 0$), $u_{\mathrm{uncorr}}(\mathrm{TG}) = \sqrt{2}\,u(T) = \mathbf{0.3366 °C}$. Under Rule `4.f` (same thermometer, $r_{\mathrm{sys}} = +1$), the correlated systematic variance cancels ($u_{B,\mathrm{sys}}^2 + u_{B,\mathrm{sys}}^2 - 2u_{B,\mathrm{sys}}^2 = 0$), leaving only random and resolution terms:
$$u_{\mathrm{corr}}(\mathrm{TG}) = \sqrt{2\left(u_{B,\mathrm{res}}^2 + u_A^2\right)} = \sqrt{2\left(0.02887^2 + 0.050^2\right)} = \mathbf{0.08165 °C} \quad (\mathbf{4.12\times\text{**lower uncertainty!**}})$$
(b) Specific heat of the metal: $c_x = \frac{m_w c_w \Delta T_w}{m_x \Delta T_x} = \frac{(100.00)(4.184)(5.40)}{(85.00)(52.60)} = \mathbf{0.50533 J/g/K}$. By Rule 3 in Table `tab:17:gumrules`:
$$\frac{u_c(c_x)}{c_x} = \sqrt{\left(\frac{0.15}{100.00}\right)^2 + \left(\frac{0.05}{85.00}\right)^2 + \left(\frac{0.08165}{5.40}\right)^2 + \left(\frac{0.08165}{52.60}\right)^2} = \mathbf{0.01528}\ (1.53%)$$
*(Notice that $\frac{u(\Delta T_w)}{\Delta T_w} = 1.51%$ contributes $>97\%$ of the total variance!)* Thus $u_c(c_x) = (0.50533)(0.01528) = \mathbf{0.00772 J/g/K}$ and expanded uncertainty ($k=2$) is $U = 2 u_c(c_x) = \mathbf{0.0154 J/g/K}$, reported as $c_x = \mathbf{0.505 ± 0.015 J/g/K}$.

**✓ Verified by:** Monte Carlo / finite-difference perturbation of $c_x(m_w, m_x, \Delta T_w, \Delta T_x)$ and Python check `sec17:ex17.5`.

### Worked Example — Thermocouple Cold-Junction Compensation (CJC) & Stefan–Boltzmann $T^4$ Power-Law Uncertainty `[Rules 4.f, 5.c.vi]`

(a) A `Type T` thermocouple has its sensing junction in warm water at $T_{\mathrm{sense}}$ and its voltmeter terminal block (reference junction) at ambient room temperature $T_{\mathrm{ref}} = 20.00 °C$. The uncompensated millivoltmeter reads $\Delta V(T_{\mathrm{ref}}, T_{\mathrm{sense}}) = +0.934 mV$. Using Table `tab:17:sensortable`, find the total ice-point referenced EMF $E(0 °C, T_{\mathrm{sense}})$ and determine $T_{\mathrm{sense}}$ by linear interpolation between $40.0 °C$ and $50.0 °C$.
(b) A blackbody cavity ($\varepsilon = 1.000$ exact) of aperture area $A = 50.00 ± 0.25 cm^2$ operates at $T = 500.0 ± 2.5 K$. Calculate the emitted radiant power $\dot{Q} = \sigma A T^4$ and its combined standard uncertainty $u_c(\dot{Q})$.
**Solution.**
(a) From Table `tab:17:sensortable`, a `Type T` junction at $T_{\mathrm{ref}} = 20.00 °C$ has $E(0 °C, 20.00 °C) = +0.790 mV$. By the Law of Intermediate Temperatures:
$$E(0 °C, T_{\mathrm{sense}}) = E(0 °C, 20.00 °C) + \Delta V(20.00 °C, T_{\mathrm{sense}}) = 0.790 + 0.934 = \mathbf{+1.724 mV}$$
Interpolating in Table `tab:17:sensortable` between $40.0 °C$ ($1.612 mV$) and $50.0 °C$ ($2.036 mV$):
$$T_{\mathrm{sense}} = 40.0 + (50.0 - 40.0)\frac{1.724 - 1.612}{2.036 - 1.612} = 40.0 + 10.0\left(\frac{0.112}{0.424}\right) = \mathbf{42.64 °C}$$
(b) Emitted radiant power ($\sigma = 5.670374×10^{-8} W/m^2/K^4$, $A = 5.000×10^{-3} m^2$):
$$\dot{Q} = \sigma A T^4 = (5.670374×10^{-8})(5.000×10^{-3})(500.0)^4 = \mathbf{17.720 W}$$
By the power-law GUM formula (Rule 4 in Table `tab:17:gumrules`), the exponent $4$ on $T$ multiplies its relative uncertainty by $4$:
$$\frac{u_c(\dot{Q})}{\dot{Q}} = \sqrt{\left(\frac{u(A)}{A}\right)^2 + \left(4\,\frac{u(T)}{T}\right)^2} = \sqrt{\left(\frac{0.25}{50.00}\right)^2 + \left(4\times\frac{2.5}{500.0}\right)^2} = \sqrt{0.0050^2 + 0.0200^2} = \mathbf{0.02062}\ (2.06%)$$
Thus $u_c(\dot{Q}) = (17.720 W)(0.020616) = \mathbf{0.365 W}$, so $\dot{Q} = \mathbf{17.72 ± 0.37 W}$ ($1\sigma$).

**✓ Verified by:** Exact differential $\delta\dot{Q} = \sqrt{(\sigma T^4 u_A)^2 + (4\sigma A T^3 u_T)^2} = \sqrt{0.0886^2 + 0.3544^2} = 0.3653 W$ and Python check `sec17:ex17.6`.

## Step-by-Step Classroom-Safe Calorimetry & 2027 Collector Validation Protocols

### [2027 HEAT-COLLECTOR DEVICE & LAB: Protocol A (Calorimeter Heat Capacity $C_{\mathrm{cal}}$) & Protocol B (2027 Heat-Lamp Collector DOE Validation)]

**Protocol A: Classroom Calorimeter Calibration & Specific Heat Determination (`Rule 5.c.iii`)**
- **Dry Tare & Cold Baseline:** Weigh dry inner calorimeter cup ($m_{\mathrm{cup}}$) on $0.01 g$ balance. Add $100.0 mL$ room-temperature water, re-weigh ($m_c = m_{\mathrm{total}} - m_{\mathrm{cup}}$), insert calibrated probe, stir gently, wait $\ge 5\tau_p$, and log $T_c$ every $15 s$ for $2 min$ to confirm zero drift.
- **Determine Calorimeter Constant $C_{\mathrm{cal}}$ $[J/K]$:** Heat a separate $100.0 mL$ water sample to $T_h \approx 55 °C$ (safe below scalding threshold). Record $T_h$ ($\ge 5\tau_p$) and exact mass $m_h$, pour rapidly into cold calorimeter, cover lid, and log $T(t)$ every $5 s$ through peak $T_{\mathrm{eq}}$ and for $3 min$ of post-peak cooling. Extrapolate the post-peak linear cooling line back to mixing time $t_{\mathrm{mix}}$ (Regnault–Pfaundler cooling correction, §`sec:04`) to get true $T_{\mathrm{eq}}$, then compute:
  $$C_{\mathrm{cal}} = \frac{m_h c_w (T_h - T_{\mathrm{eq}}) - m_c c_w (T_{\mathrm{eq}} - T_c)}{T_{\mathrm{eq}} - T_c}$$
- **Unknown Solid Specific Heat $c_x$:** Equilibrate dry metal cylinder ($m_x \approx 80 g$) in a boiling steam jacket ($T_{x,i} = T_{\mathrm{boil}}(P_{\mathrm{atm}})$ for $\ge10 min$), transfer rapidly ($<2 s$ in air) into fresh calorimeter water ($m_w, T_{w,i}$) without splashing, record $T_{\mathrm{eq}}$, and solve:
  $$c_x = \frac{\left(m_w c_w + C_{\mathrm{cal}}\right)(T_{\mathrm{eq}} - T_{w,i})}{m_x\left(T_{x,i} - T_{\mathrm{eq}}\right)}$$

**Protocol B: 2027 Heat-Lamp Collector Calibration & Stratification Validation (`Rule 5.II`)**
- **Station Geometry & Lamp Pre-Warm:** Mount clamp lamp with $125 W$ (or $100 W$) clear untinted incandescent heat-lamp bulb facing straight down (`Rule 4.a–d`). Set vertical height $h \in 40.0–65.0 cm$ from table surface to bottommost tip of bulb (`Rule 4.c`) using a rigid meterstick and plumb line. Turn lamp ON for $\ge3 min$ off to the side so filament and glass envelope reach thermal steady state.
- **3-Min Device Setup & 1-Min Water Setup Simulation:** Start master timer. Configure collector pedestal slot for height $h$ (`Rule 5.II.b`). Dispense $99.67 ± 0.05 g$ ($100.00 mL$ at $22 °C$) water from source bath into a fresh $9 oz$ clear cup, measure $T_{\mathrm{start}}$ at $z = 8 mm$ after $5\tau_p$, place non-attached clear BoPET film cap on cup rim (`Clarif. #5`), seat cup into collector cradle, and center under lamp at $t = 0$.
- **Heating Window & Unswirled Top-Layer Extraction:** Heat for exact target duration $t \in \{10, 12, 15\}\,min$. At lamp turn-off, lift upper reflector hood straight up (removing the clear film cap cleanly) and lift the $9 oz$ cup vertically onto the Testing Surface in $<8 s$ **with zero tilting, swirling, or vibration** (`Clarif. #1–#3`).
- **Clarification `#4` Probe Reading & Cool-Down Return:** Lower probe clamp into top water layer ($z = 8 ± 2 mm$, $r = 0 mm$), wait $5\tau_p$ ($10 s$), and log $T_f$ in Appendix D test log. Cool collector back to $T_{\mathrm{room}}$ with a fan before the next trial!

### [2027 OFFICIAL RULE / CLARIFICATION: Mandatory Laboratory Safety & Impound Compliance Checklist (Thermal, Electrical, Glass & Chemical)]
- **Thermal Burn & Fire Prevention:** A $125 W$ heat lamp glass face reaches $180–230 °C$; never touch the bulb or metal clamp shroud until cooled for $\ge15 min$. Keep all paper/cardboard/balsa collector surfaces $\ge10 cm$ below the bulb and faced with reflective aluminum foil ($\rho_{\mathrm{NIR}} = 0.96$) so structural temperatures stay $<45 °C$ (well below the $218 °C$ paper ignition point and $74 °C$ `#1 PET` cup softening point).
- **Zero-Tolerance Prohibited Materials Audit (`Rule 3.b.i` & `Clarification #6`):** Verify that **zero Polystyrene / Styrofoam / `#6 PS` plastic**, fiberglass, mineral wool, asbestos, or mercury thermometers are present anywhere in the device or lab kit (`Rule 3.b.iii` bars any device containing prohibited hazardous materials from testing: $\mathrm{TS}=0, \mathrm{PS}=0$!).
- **Electrical & Water-Spill Separation:** Plug the clamp lamp into a GFCI-protected $120 V$ outlet with a drip loop so water spills on the Testing Surface can never reach electrical cords. Never place or remove the water cup while looking directly into the incandescent filament.

—
**See also:** §`sec:00` (Command Center & Rules), §`sec:02` (Sig Figs & Units), §`sec:14` (Material Optical/Thermal Properties), §`sec:15`–§`sec:16` (2027 Collector Design & Calibration DOE), §`sec:18` (Graphs, Semi-Log OLS & Residuals), and §`app:D` (Printable Calibration Logs).
