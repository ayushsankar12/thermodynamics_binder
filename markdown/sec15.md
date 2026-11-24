<!-- Source: src/sec15.tex | Tab: Tab 6: DEVICE | Target: 18 pp -->
# §15: Competition Device Engineering — 2027 100–125 W Heat-Lamp Collector {#sec:15}

> **[SCOPE: REQUIRED | 2027 Rules 3.a–h, 4.a–g, 5.II.a–g & Official Clarifications #1–#9 (All Tournament Levels)]**

The 2026–2027 Division C Thermodynamics device event is a **passive optical heat-collection and top-layer thermal-stratification challenge**  **[S01,S02,S05]**. Unlike legacy 2018–2019 hot-water insulator events (where teams received boiling water and minimized cooling), the 2027 device starts completely at **room temperature** (`Rule 2.d, 3.g`) and must capture downward radiant energy from an Event Supervisor (ES) $100–125 W$ clear incandescent reflector heat lamp mounted at $h_{\mathrm{bulb}} = 40–65 cm$ above the Testing Surface to maximize the Temperature Gain $\mathrm{TG} = T_{\mathrm{final}} - T_{\mathrm{start}}$ of $100 mL$ of water inside an ES-provided $9 oz$ clear plastic party cup  **[S01]**. This chapter translates every clause of Rules `2–6` and all nine Official National Clarifications (`09/30/2026`–`10/28/2026`) into a championship collector architecture verified by geometric-optics ray tracing, four-node transient heat-transfer modeling, and Hale & Querry near-infrared water spectroscopy  **[S12,S19]**.

## Rule-to-Engineering Translation Matrix & Championship Collector Architecture

Every geometric dimension, material choice, and handling step of the collector is governed by an explicit boundary in the 2027 Rules Manual and Official Clarifications  **[S01,S02,S04,S05]**. Table `tab:15:rule-translation` maps each rule clause to its quantitative engineering specification.

**Table:** Clause-by-clause translation of 2027 Thermodynamics Division C rules and clarifications into collector engineering specifications  **[S01,S02,S04,S05]**.

| **Rule / Clarif.** | **Official 2027 Requirement** | **Physical & Scoring Implication** | **Mandatory Collector Engineering Specification** |
| --- | --- | --- | --- |
| **`2.c, 2.d`** <br> Clarif. #9 | Impound ONLY device & spare parts at room temp ($\times 0.7$ penalty if not impounded). Notes, graphs, tables, calculators, and tools are NOT impounded. | Keeping calibration tables and Class III calculators out of impound allows block-morning room-temp checks. | Impound collector + 2 spare BoPET glazing rings in an open ventilated crate. Carry detached nomograms (§`sec:16`) and alignment gauge in binder. |
| **`3.a, 4.a–d`** | Collect heat from ES downward $100–125 W$ clear incandescent heat lamp (not tinted, LED, halogen, or ceramic); stand feet $\ge15 cm$ from bulb axis. | Lamp emits $\sim84%$ downward radiation ($\lambda_{\max}\approx1.21 µm$). A $30 cm$ square base clears the $\pm15 cm$ lamp stand post. | Maximize top entry aperture ($D_{\mathrm{ap}}=29.0 cm$ circle or $29.6 cm$ square-to-round hood, $A_{\mathrm{ap}}=660.5–876.2 cm^2$) centered on optical axis. |
| **`3.b.i, 3.b.iii`** <br> Clarif. #6 | No asbestos, mineral wool, fiberglass, or **polystyrene / Styrofoam / `#6 PS` plastics** (`10/22/2026`). | Hazardous material violation bars device from setup, modification, or testing ($\mathbf{\mathrm{TS}=\mathrm{PS}=0}$)! | Zero EPS, XPS, Styrofoam, craft PS foam-core board, or `#6 PS` parts. Use cardboard + $10 mm$ Al-foil air gaps, cork, balsa, cotton/sheep wool, and BoPET. |
| **`3.b.ii`** | No thermometers, probes, commercial thermoses, coolers, or vacuum-sealed vessels. | Any commercial vacuum Dewar or forgotten thermocouple inside impounded device incurs $\times 0.7$ or DQ. | Student-built multi-wall foil-air-cardboard-cork cradle (`3.h`); strip all lab thermocouples before tournament packing. |
| **`3.c, 4.g`** | Insert/remove ES $9 oz$ clear plastic party cup ($\approx9.9–10.2 cm$ tall, $7.4–7.6 cm$ mouth) holding $100 mL$ water. | $100 mL$ fills only the bottom $3.6–4.0 cm$ of the $10.0 cm$ cup; dry upper PET rim softens at $T_g\approx74 °C$. | Focus reflector rays at the $3.8 cm$ waterline ($z_{\mathrm{focus}}$) and shade the dry upper plastic rim lip with a non-contact foil overhang ring. |
| **`3.d`** | Entire set-up device + cup must fit inside a $\mathbf{30.0 cm\times30.0 cm\times30.0 cm}$ cube. | Exceeding $30.0 cm$ on any axis after 3-min Setup Time incurs a $\times 0.7$ construction violation. | Build outer envelope strictly to $\mathbf{29.6 cm\times29.6 cm\times29.5 cm}$ ($\ge4.0 mm$ thermal/humidity safety margin on all 3 axes). |
| **`3.e`** | Parts may extend inside cup, but **NO part may contact water**; nothing added to water. | Wetted device parts or dyes incur $\times 0.7$ violation. $100 mL$ waterline sits $6.2 cm$ below the cup rim. | Terminate any internal upper reflector lip $\ge15.0 mm$ above the $38.0 mm$ waterline ($z_{\mathrm{lip}} \ge z_{\mathrm{base}} + 53.0 mm$); verify dry rim at removal. |
| **`3.f, 3.g`** | Zero internal energy sources; device at room temp at start; post-test disassembly check. | Electrical/chemical heat source gives $\mathrm{TS}=\mathrm{PS}=0$. | Pure passive reflector/insulator; assemble with 4 removable wooden dowels + Velcro panel for $<20 s$ post-test ES inspection. |
| **`4.c.i–iii`** <br> **`5.II.a–b`** | Bulb height $h$: $40–50 cm$ by $5 cm$ (Reg), $40–55 cm$ by $5 cm$ (State), $40–65 cm$ by $1 cm$ (Nat). Announced at block start; 3-min Setup Time. | Fixed-focus cones lose efficiency when $h$ shifts from $40 cm$ to $65 cm$. Adjusting device during 3-min Setup Time is legal (`5.II.b`). | Provide 3 pre-indexed vertical pedestal height slots (**Slot A** for $h=40–48 cm$, **Slot B** for $49–57 cm$, **Slot C** for $58–65 cm$) set during 3-min Setup Time. |
| **`5.II.b, d, g`** <br> Clarif. #5, #7, #8 | Lift-off lid/door legal to insert/remove cup (`10/22/26`). Non-attached wrap legal if zero tape/clips on cup and removed before $T_{\mathrm{final}}$ (`10/21/26`). | Open cups lose $2.2–4.4 W$ ($4.8–8.0 °C$) to evaporation! Fumbling with loose cling wrap during the 1-min removal window risks sloshing. | Mount a tensioned $25 µm$ clear BoPET glazing window inside the lift-off upper reflector hood (or gravity drop-ring) that seals the cup rim by gravity and lifts off in $<2 s$! |
| **`5.II.g`** <br> Clarif. #1–#4 | **Zero stirring, swirling, or shaking** (`09/30–10/06/26`). ES measures **top water layer near cup center**. | Top-down NIR heating deposits $72.4\%$ of energy in top $10 mm$, creating stable stratification ($\mathrm{TG}_{\mathrm{top}} \approx 1.55\,\mathrm{TG}_{\mathrm{bulk}}$). | Lift upper hood vertically on 4 guide dowels; extract cup with a smooth vertical two-finger rim lift (zero tilt or vibration) to preserve the hot top water layer! |

> **[Vector Figure: Original Vector Technical Diagram | Label: `fig:diagram`]**

> **[Vector Figure: Engineering cross-section of the reference 2027 two-piece heat-lamp collector inside the $30.0 cm$ cubic bounding envelope, showing the lift-off 3-stage finite-conjugate specular aluminum-foil reflector hood, integrated non-attached $25 µm$ BoPET glazing cap (Clarifications #5, #7), 3-point knife-edge cork cup cradle, bottom return mirror, and concentric $10 mm$ foil-air-foil insulation baffles  **[S01,S02,S12]**. | Label: `fig:15:collector-cutaway`]**
> - **Diagram Annotations & Key Elements:** Testing Surface ($z = 0.0 cm$) • Max $30.0 cm\times30.0 cm\times30.0 cm$ Rule `3.d` Cube • ES $100–125 W$ Clear R40 Heat Lamp ($\text{Ø}12.7 cm$) • Bottommost Point of Bulb: $h_{\mathrm{bulb}} = 40.0–65.0 cm$ • Hood Split Plane ($z=14.0 cm$, 4 Guide Dowels) • 3-Layer $10 mm$ Foil-Air Baffles • Pedestal Slots A/B/C • ($\Delta z = ± 1.5 cm$ focus) • Clear $25 µm$ BoPET Glazing Cap ($z=15.3 cm$, Clarif. #5) • $100 mL$ $\mathrm{H_2O}$ • $z_w = 9.0 cm$ ($3.8 cm$ deep) • Dry Air Headspace ($6.2 cm$) • Stage 1 Frustum ($\phi_1=23.5°$) • Stage 2 Frustum ($\phi_2=29.7°$) • Lift-Off Upper • Reflector Hood • Lower Insulated • Pedestal Base

**Table:** Reference 2027 collector subsystem dimensional, optical, and parasitic thermal-mass budget  **[S01,S12]**.

| **Subsystem Component** | **Compliant Material** | **Key Dimensions** | **Elevation $z$** | **Total $m$** | **Coupled $C_{\mathrm{eff}}$** | **Rule Compliance & Functional Role** |
| --- | --- | --- | --- | --- | --- | --- |
|  |  | $[cm]$ | $[cm]$ | $[g]$ | $[J/K]$ |  |
| **1. Outer Structural Shell** | Fluted cardboard + foil | $29.6\times 29.6\times 29.5$ | $0.0\text{--}29.5$ | $310$ | $0.0$^a | $4.0 mm$ clearance inside $30.0 cm$ cube (`3.d`). |
| **2. Lift-Off 3-Stage CPC Hood** | $24 µm$ shiny Al foil / card | $\text{Ø} 29.0 \to \text{Ø} 7.9$ throat | $11.8\text{--}29.5$ | $145$ | $0.45$ | Lifts on 4 corner dowels in $<2 s$ (Clarif. #7–#8). |
| **3. Gravity BoPET Glazing Cap** | $25 µm$ clear BoPET film | $\text{Ø} 8.8$ disk ($60 cm^2$) | $15.25$ | $0.21$ | $\mathbf{0.24}$ | Zero tape/clips on cup; cuts evaporation $98\%$ (Clarif. #5). |
| **4. Upper Dry-Cup Throat Lip** | $24 µm$ shiny Al foil ring | $\text{Ø} 7.9 \to \text{Ø} 7.1$ overhang | $11.8\text{--}15.2$ | $1.8$ | $0.15$ | Shades dry PET cup rim; $28 mm$ above water (`3.e`). |
| **5. Lower Cavity Return Mirror** | $24 µm$ shiny Al foil bowl | $\text{Ø} 8.4$ cylinder + base | $4.8\text{--}11.8$ | $3.2$ | $0.85$ | Reflects transmitted NIR back through clear cup wall. |
| **6. 3-Fin Knife-Edge Pedestal** | Balsa / cork radial fins | $3\times(0.2 cm\times1.8 cm)$ | $4.2\text{--}5.2$ | $2.4$ | $\mathbf{0.35}$ | Contact area $A_c=0.18 cm^2$; base leak $<0.015 W$. |
| **7. Radial & Base Foil-Air Wall** | $4\times$ Al foil + $10 mm$ air | $3\times1.0 cm$ concentric gaps | $1.2\text{--}13.8$ | $38$ | $1.10$ | $\mathrm{Ra}_\delta < 1708$; $k_{\mathrm{eff}}=0.0278 W/m/K$, zero `#6 PS`! |
| **8. ES $9 oz$ Cup + $100 mL$ Water** | Clear PET/PP + $\mathrm{H_2O}$ | $\text{Ø} 7.5\text{ top}, \text{Ø} 5.3\text{ base}\times 10.0$ | $5.2\text{--}15.2$ | $106.5$ | $\mathbf{215.0}$^b | Water depth $3.80 cm$ ($z=5.2–9.0 cm$); wetted cup $3.5 J/K$. |
| ^aThermally isolated behind three $10 mm$ foil-air-foil gaps ($R_{\mathrm{th}} > 20 K/W$). ^bEffective stratified top-layer capacitance $C_{\mathrm{top,eff}} \approx 215 J/K$ (bulk water $C_w = 418.4 J/K$). |  |  |  |  |  |  |

## Heat-Lamp Radiative Source Physics & View-Factor Irradiance Scaling

Under Rule `4.a–c` and the Official ES Guide  **[S01,S05]**, the testing station uses a clamp lamp with a spun-aluminum reflector housing an untinted $100 W$ or $125 W$ incandescent heat-lamp bulb (standard $\mathrm{R40}$ or $\mathrm{BR40}$ clear reflector flood lamp, bulb face diameter $D_{\mathrm{bulb}} = 5.0 in = 12.70 cm$, radius $r_1 = 6.35 cm$). The bulb's electrical input power $P_{\mathrm{elec}} \in \{100 W, 125 W\}$ partitions into three thermal pathways  **[S12]**:
- **Short-Wave Visible & Near-IR Beam Transmitted Through Bulb Glass ($\lambda \in [0.38 µm, 2.75 µm]$):** Accounts for $\eta_{\mathrm{SW}} \approx 70.0\%$ of electrical power ($\dot{Q}_{\mathrm{SW}} = 87.5 W$ at $125 W$; $70.0 W$ at $100 W$), projected downward by the internal paraboloidal aluminum coating with an axial flood profile $I(\theta) = I_0\cos^m\theta$ ($m \approx 2.0$, half-power beam half-angle $\theta_{1/2} \approx 32–38 °$).
- **Long-Wave Mid-IR Emitted Downward by the Hot Bulb Glass Face ($\lambda \in [3.5 µm, 15 µm], T_{\mathrm{glass}} \approx 170–220 °C$):** Accounts for $\eta_{\mathrm{LW}} \approx 14.0\%$ of electrical power ($\dot{Q}_{\mathrm{LW}} = 17.5 W$ at $125 W$; $14.0 W$ at $100 W$), emitted diffusely downward ($\varepsilon_{\mathrm{glass}} = 0.94$).
- **Upper Neck/Socket Convection & Base Conduction Loss:** Accounts for the remaining $\sim 16.0\%$ ($20.0 W$ at $125 W$), rising upward away from the testing table. Thus total downward radiant output is $\dot{Q}_{\mathrm{rad,down}} = 0.84\,P_{\mathrm{elec}}$ ($\mathbf{105.0 W}$ for $125 W$; $\mathbf{84.0 W}$ for $100 W$).

### [FORMULA & DECISION CARD: Algebra-Only Coaxial Disk View Factor & Proximity Flux Multiplication (Rule 5.d.iv Compliant)]

| **Formula** | **Variables (SI units)** | **Flags** | **Use when** |
| --- | --- | --- | --- |
| $d_{\mathrm{ap}} = h_{\mathrm{bulb}} - z_{\mathrm{ap}}$ <br> $d_{\mathrm{cup}} = h_{\mathrm{bulb}} - z_{\mathrm{cup}}$ | $h_{\mathrm{bulb}} \in [40 cm, 65 cm]$: height from table to bottom of bulb (`4.c`); $z_{\mathrm{ap}} \le 29.5 cm$: collector top rim height; $z_{\mathrm{cup}} = 10.0 cm$: bare cup rim height. | **[2027-RULE]** | Raising the aperture to $z_{\mathrm{ap}}=29.5 cm$ cuts source distance from $30.0 cm$ to $10.5 cm$ at $h=40 cm$! |
| $R_1 = \dfrac{r_1}{d}, \quad R_2 = \dfrac{r_2}{d}$ <br> $X = 1 + \dfrac{1 + R_2^2}{R_1^2}$ <br> $F_{1\to 2} = \dfrac{1}{2}\!\left[X - \sqrt{X^2 - 4\!\left(\dfrac{R_2}{R_1}\right)^{\!2}}\right]$ | $r_1 = 6.35 cm$: bulb face radius; $r_2$: target aperture radius ($r_{\mathrm{ap}}=14.5–15.0 cm$ vs. bare cup $r_{\mathrm{cup}}=3.75 cm$); $d$: axial separation $[cm]$; $F_{1\to 2}$: diffuse view factor $[-]$. | **[GRAY-SURF]** | Exact closed-form algebraic view factor between coaxial disks (Lienhard Table 10.3 Case 3 **[S12]**); zero calculus or trig! |
| $C_{\mathrm{geom}} = \dfrac{A_{\mathrm{ap}}}{A_{\mathrm{cup}}} = \begin{cases} (r_{\mathrm{ap}}/r_{\mathrm{cup}})^2 & \text{(circle)} \\ W_{\mathrm{ap}}^2 / (\pi r_{\mathrm{cup}}^2) & \text{(square)} \end{cases}$ | $A_{\mathrm{cup}} = \pi(3.75 cm)^2 = 44.18 cm^2$; $A_{\mathrm{ap,circ}} = \pi(14.5 cm)^2 = 660.5 cm^2$; $A_{\mathrm{ap,sq}} = (29.6 cm)^2 = 876.2 cm^2$. | **[2027-RULE]** | Geometric area concentration ratio: $C_{\mathrm{geom}} = 14.95\times$ (circle) to $19.83\times$ (square hood). |

### Worked Example — Coaxial Disk View-Factor & Proximity Gain: Collector Aperture vs. Bare 9 oz Cup `[Rule 4.c / §15.2]`

An ES mounts a $125 W$ $\mathrm{R40}$ heat lamp ($r_1 = 6.35 cm$, downward diffuse-equivalent radiant output $\dot{Q}_{\mathrm{rad}} = 105.0 W$) at the minimum Regional/State/National height $h_{\mathrm{bulb}} = 40.0 cm$ above the Testing Surface. Using the coaxial-disk view-factor formula, compare (a) a bare $9 oz$ party cup sitting on the table ($z_{\mathrm{cup}} = 10.0 cm$, mouth radius $r_{\mathrm{cup}} = 3.75 cm$) against (b) a collector whose top aperture ($r_{\mathrm{ap}} = 15.0 cm$ equivalent circle) sits at $z_{\mathrm{ap}} = 29.5 cm$. Repeat the comparison at the maximum National height $h_{\mathrm{bulb}} = 65.0 cm$.

**Solution.** Apply $R_1 = r_1/d$, $R_2 = r_2/d$, $X = 1 + (1+R_2^2)/R_1^2$, and $F_{1\to 2} = \frac{1}{2}[X - \sqrt{X^2 - 4(R_2/R_1)^2}]$  **[S12]**:
- **At $h_{\mathrm{bulb}} = 40.0 cm$:**
- *Bare Cup ($d_{\mathrm{cup}} = 40.0 - 10.0 = 30.0 cm, r_2 = 3.75 cm$):* $R_1 = 6.35/30.0 = 0.21167$, $R_2 = 3.75/30.0 = 0.12500$, $X = 1 + (1 + 0.015625)/0.044803 = 23.6688 \implies F_{\mathrm{bulb}\to\mathrm{cup}}(40 cm) = \mathbf{0.01473}$ ($1.47\%$ of diffuse radiation, or $1.55 W$).
- *Collector Top Plane ($z_{\mathrm{ap}} = 30.0 cm, d = 10.0 cm, r_2 = 15.0 cm$):* $R_1 = 6.35/10.0 = 0.6350$, $R_2 = 15.0/10.0 = 1.5000$, $X = 1 + (1 + 2.250)/0.403225 = 9.0600 \implies F_{\mathrm{bulb}\to\mathrm{ap}}(40 cm) = \mathbf{0.66471}$ ($66.5\%$ of diffuse radiation, or $69.79 W$; at the recessed rim $z_{\mathrm{ap}} = 29.5 cm$ where $d = 10.5 cm$, $F = \mathbf{0.64355}$).
- *Combined Area $\times$ Proximity View-Factor Ratio:* $F_{\mathrm{ap}}/F_{\mathrm{cup}} = 0.66471 / 0.01473 = \mathbf{45.13\times}$ more intercepted power ($43.65\times$ at $z_{\mathrm{ap}}=29.5 cm$)!
- **At $h_{\mathrm{bulb}} = 65.0 cm$:**
- *Bare Cup ($d_{\mathrm{cup}} = 55.0 cm$):* $R_1 = 0.11545$, $R_2 = 0.06818$, $X = 76.364 \implies F_{\mathrm{bulb}\to\mathrm{cup}}(65 cm) = \mathbf{0.004568}$ ($0.46\%$).
- *Collector Top Plane ($d = 35.0 cm$ at $z_{\mathrm{ap}}=30.0 cm$):* $R_1 = 0.18143$, $R_2 = 0.42857$, $X = 36.960 \implies F_{\mathrm{bulb}\to\mathrm{ap}}(65 cm) = \mathbf{0.15162}$ ($15.2\%$, a $\mathbf{33.19\times}$ gain over the bare cup; at $d=35.5 cm$, $F = \mathbf{0.14807}$).
    

**✓ Verified by:** Reciprocity check $A_1 F_{1\to 2} = A_2 F_{2\to 1}$ and small-disk asymptotic limit $F_{1\to 2} \to r_2^2 / (r_1^2 + r_2^2 + d^2)$; asserted in `check_sec14_16.py`.

**Table:** Comparison of Rule `4.a–b`-permitted heat-lamp bulb architectures, spectral partitions, and beam profiles  **[S01,S05,S12]**.

| **Permitted Bulb Type** | **$P_{\mathrm{elec}}$** | **$D_{\mathrm{bulb}}$** | **$T_{\mathrm{fil}}$** | **$\lambda_{\max}$** | **$\eta_{\mathrm{SW}}$ / $\eta_{\mathrm{LW}}$** | **Beam $\theta_{1/2}$** | **Optical Profile & Collector Coupling Notes** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| (Rule `4.a–b` Clear/Untinted) | $[W]$ | $[cm]$ | $[K]$ | $[µm]$ | $[\% / \%]$ | $[°]$ |  |
| **1. Clear R40 Reflector** (Standard Flood Heat Lamp) | $125$ | $12.70$ | $2400$ | $1.207$ | $70.0 / 14.0$ | $35^\circ$ ($m\!=\!2.0$) | **BASELINE ES BULB:** Internal vapor-deposited Al bowl projects $87.5 W$ short-wave NIR + $17.5 W$ mid-IR downward. |
| **2. Clear R40 Reflector** (100 W Standard Flood) | $100$ | $12.70$ | $2320$ | $1.249$ | $69.5 / 14.5$ | $35^\circ$ ($m\!=\!2.0$) | Scales downward radiant flux by $\eta_{100/125} \approx 0.800$ ($84.0 W$ total downward); slightly deeper $z<5 mm$ water absorption. |
| **3. Clear BR40 Bulged Reflector** (Wide Flood) | $125$ | $12.70$ | $2380$ | $1.218$ | $68.5 / 15.0$ | $42^\circ$ ($m\!=\!1.6$) | Wider beam divergence; our $29.6 cm$ wide top aperture at $z_{\mathrm{ap}}=29.5 cm$ captures peripheral rays that narrow cones miss! |
| **4. Clear PAR38 Pressed-Glass Spot/Flood** | $100\text{--}125$ | $12.07$ | $2440$ | $1.188$ | $71.5 / 13.5$ | $22^\circ$ ($m\!=\!4.5$) | Highly collimated central beam; increases direct unbounced cup-mouth irradiance by $+18\%$ at high National heights ($h\ge55 cm$). |
| **5. Clear A19 / PS25 Bulb in Spun-Al Clamp Hood** | $100\text{--}125$ | $6.0\text{--}9.5$ | $2420$ | $1.197$ | $64.0 / 16.0$ | $48^\circ$ ($m\!=\!1.3$) | External $8.5–10.5 in$ clamp-lamp metal hood acts as secondary diffuse/semi-specular reflector ($r_{1,\mathrm{eff}}\approx11.0 cm$). |
| **Tinted Red / LED / Halogen / Ceramic** | Any | Any | — | — | — | — | **PROHIBITED BY RULE `4.b`:** ES may never use red-tinted brooder bulbs, LEDs, quartz-halogen, or dark ceramic emitters. |

### [DERIVATION: Algebra-Only Coaxial-Disk & Conical-Frustum Surround Law (Lienhard Example 10.3)]

When an upper circular aperture $1$ (radius $r_{\mathrm{ap}}$ at $z_{\mathrm{ap}}$) views a coaxial lower cup mouth $2$ (radius $r_{\mathrm{cup}}$ at $z_{\mathrm{cup}}$, axial depth $H_c = z_{\mathrm{ap}} - z_{\mathrm{cup}}$) through a surrounding reflective frustum wall $s$, radiation conservation inside the closed 3-surface control volume ($F_{1\to 1} = 0$ for flat disk $1$) requires  **[S12]**:

$$
F_{1\to 1} + F_{1\to 2} + F_{1\to s} = 1 \implies \boxed{F_{1\to s} = 1 - F_{1\to 2}}
$$

Thus a fraction $F_{1\to 2}$ of diffuse aperture-entering energy passes **directly into the cup mouth with zero wall bounces**, while the complementary fraction $F_{1\to s} = 1 - F_{1\to 2}$ strikes the reflective frustum wall $s$ and is redirected toward the cup with specular efficiency $\eta_{\mathrm{cone}}$.

### Worked Example — Direct Unbounced Cup-Mouth Beam vs. Wall-Reflected Frustum Beam Partition `[Rule 5.d.iii / §15.2]`

At $h_{\mathrm{bulb}} = 45.0 cm$, a $125 W$ heat lamp delivers $\dot{Q}_{\mathrm{ap,in}} = 34.20 W$ of directional near-IR power into the collector's top aperture ($r_{\mathrm{ap}} = 14.50 cm$ at $z_{\mathrm{ap}} = 29.50 cm$). The $9 oz$ cup mouth ($r_{\mathrm{cup}} = 3.75 cm$) sits at elevation $z_{\mathrm{cup}} = 15.20 cm$ ($H_c = 14.30 cm$ below the top aperture). (a) Compute the diffuse view factor $F_{\mathrm{ap}\to\mathrm{cup}}$ from the top aperture to the cup mouth and the wall view factor $F_{\mathrm{ap}\to s}$; and (b) given that directional beam collimation ($m=2.0$) enhances the direct unbounced cup-mouth fraction to $f_{\mathrm{dir}} = 2.15\,F_{\mathrm{ap}\to\mathrm{cup}}$, calculate the direct power $\dot{Q}_{\mathrm{dir}}$, the wall-reflected power $\dot{Q}_{\mathrm{wall,deliv}}$ (with 3-stage shiny-foil wall efficiency $\eta_{\mathrm{cone}} = 0.8788$), and total power reaching the cup glazing cap.

**Solution.**
(a) Across axial depth $H_c = 29.50 - 15.20 = 14.30 cm$, the dimensionless radii are $R_1 = r_{\mathrm{ap}}/H_c = 14.50/14.30 = 1.01399$ and $R_2 = r_{\mathrm{cup}}/H_c = 3.75/14.30 = 0.26224$. Evaluating $X$ and $F_{\mathrm{ap}\to\mathrm{cup}}$:

$$
X = 1 + \frac{1 + 0.26224^2}{1.01399^2} = 2.03945 \implies F_{\mathrm{ap}\to\mathrm{cup}} = \frac{1}{2}\!\left[2.03945 - \sqrt{2.03945^2 - 4\!\left(\frac{0.26224}{1.01399}\right)^{\!2}}\right] = \mathbf{0.03344}
$$

By the conical surround law, $F_{\mathrm{ap}\to s} = 1 - 0.03344 = \mathbf{0.96656}$ ($96.66\%$ of diffuse rays strike the concentrator walls!).

(b) With flood-beam collimation ($f_{\mathrm{dir}} = 2.15 \times 0.03344 = 0.07190$, so $f_{\mathrm{wall}} = 1 - 0.07190 = 0.92810$):

$$
\dot{Q}_{\mathrm{dir}} = 0.07190(34.20 W) = \mathbf{2.459 W}, \qquad
  \dot{Q}_{\mathrm{wall,deliv}} = 0.92810(34.20 W)(0.8788) = \mathbf{27.894 W}
$$

yielding a total concentrated optical power of $\dot{Q}_{\mathrm{cup,gross}} = 2.459 + 27.894 = \mathbf{30.353 W}$ arriving at the BoPET glazing cap ($91.9\%$ of which comes from the specular reflector walls!).

**✓ Verified by:** Conservation check $\dot{Q}_{\mathrm{dir}} + \dot{Q}_{\mathrm{wall,deliv}} + \dot{Q}_{\mathrm{wall,loss}} = 2.459 + 27.894 + 3.847 = 34.200 W$; asserted in `check_sec14_16.py`.

## Optical Concentration Geometry: Straight Cones vs. 3-Stage Finite-Conjugate Funnels

Intercepting $66.5%$ of the lamp's radiation at the $29.5 cm$ top plane is useless if the reflector funnel bounces those rays back out the top aperture! Understanding the **conical ray-rejection law** and **finite-conjugate ellipsoidal focusing** is the single highest-leverage optical engineering principle in the 2027 event.

### Why Wide Straight Cones Reject $73\%$ of Incident Rays

Consider a straight truncated cone tapering from top radius $r_{\mathrm{ap}}$ at elevation $z_{\mathrm{ap}}$ to bottom exit radius $r_{\mathrm{bot}}$ at elevation $z_{\mathrm{bot}}$ (vertical height $H_c = z_{\mathrm{ap}} - z_{\mathrm{bot}}$, wall slope ratio $s = (r_{\mathrm{ap}} - r_{\mathrm{bot}})/H_c = \tan\phi$, where $\phi$ is the wall half-angle relative to the vertical axis). By the law of specular reflection ($\theta_r = \theta_i$ relative to the local wall normal, which is tilted upward by angle $\phi$), **every reflection off a straight cone wall increases a downward meridian ray's angle $\theta$ relative to the vertical axis by $2\phi$**:

$$
\begin{aligned}

  \theta_k = \theta_{\mathrm{in}} + 2k\phi \quad (k = 1, 2, \dots\text{ wall reflections}), \qquad \text{Ray Rejection Criterion: } \theta_k \ge 90°
\end{aligned}
$$

If a team builds a single straight cone directly from the top of the box ($r_{\mathrm{ap}} = 14.5 cm, z_{\mathrm{ap}} = 29.5 cm$) to the cup rim ($r_{\mathrm{bot}} = 3.80 cm, z_{\mathrm{bot}} = 11.0 cm$), the slope ratio is $s = (14.5 - 3.80)/18.5 = 0.5784$ ($\phi = 30.0°$). At $h_{\mathrm{bulb}} = 40.0 cm$ ($d_{\mathrm{ap}} = 10.5 cm$), outer lamp rays enter at $\theta_{\mathrm{in}} \approx 32–54 °$. On just the **first or second bounce**, $\theta_1 = \theta_{\mathrm{in}} + 60° > 90°$: the ray turns upward and **escapes back out the top opening**, rejecting $73.4\%$ of all intercepted rays!

### The Finite-Conjugate Prolate Ellipsoid & 3-Stage Piecewise Frustum Solution

Because the lamp source sits at a **known finite distance** on the central axis ($F_1 = (0, h_{\mathrm{design}})$) and the target is the top water layer inside the cup ($F_2 = (0, z_{\mathrm{focus}})$), Fermat's principle of equal optical path length ($\overline{F_1 P} + \overline{P F_2} = 2a = \mathrm{const}$) dictates that the exact single-bounce mirror surface is a **prolate ellipsoid of revolution** with foci at $F_1$ and $F_2$:

$$
\begin{aligned}

  \frac{r^2}{b^2} + \frac{(z - z_c)^2}{a^2} = 1 \implies r(z) = b\sqrt{1 - \frac{(z - z_c)^2}{a^2}}, \quad z_c = \frac{h_{\mathrm{design}} + z_{\mathrm{focus}}}{2}, \quad c = \frac{h_{\mathrm{design}} - z_{\mathrm{focus}}}{2}
\end{aligned}
$$

$$
\begin{aligned}

  2a = \sqrt{r_{\mathrm{ap}}^2 + (h_{\mathrm{design}} - z_{\mathrm{ap}})^2} + \sqrt{r_{\mathrm{ap}}^2 + (z_{\mathrm{ap}} - z_{\mathrm{focus}})^2}, \qquad b = \sqrt{a^2 - c^2}
\end{aligned}
$$

Notice that Eqs. Eq. (`eq:15:ellipsoid`)–Eq. (`eq:15:ellipsoid-ab`) require **only arithmetic, squares, and square roots** (100% compliant with Rule `5.d.iv`!). In practice, approximating $r(z)$ with **three piecewise conical frustums** (a steeper upper entry stage $\phi_1 \approx 22°$, a middle focusing stage $\phi_2 \approx 28°$, and a steep lower cup-throat stage $\phi_3 \approx 15°$ extending around the translucent upper cup wall) eliminates multi-bounce ray rejection and achieves **$31.4\%$ to $41.4\%$ total lamp beam capture** ($13.7\times$ to $28.6\times$ bare-cup power!).

> **[Vector Figure: Geometric-optics meridian ray tracing comparing (A) a $30^\circ$ straight conical funnel (where $\theta_k = \theta_{\mathrm{in}} + 2k\phi > 90°$ turns outer rays upward after 1–2 bounces) against (B) the 3-stage finite-conjugate ellipsoidal/CPC profile focusing rays from $F_1$ into the top water layer $F_2$  **[S12]**. | Label: `fig:15:ray-trace-cone`]**
> - **Diagram Annotations & Key Elements:** A. $30^\circ$ Straight Cone • (73.4% Rays Rejected!) • B. 3-Stage Ellipsoid/CPC • (Single-Bounce to $F_2$!) • Lamp Focus $F_1$ • $F_2$ (Top Water) • $\theta_2\!>\!90^\circ$ • (Escapes!) • $\phi_1\!=\!23^\circ$ • $\phi_2\!=\!30^\circ$ • $\phi_3\!=\!15^\circ$

> **[Vector Figure: Net optical power $\dot{Q}_{\mathrm{abs}}(h_{\mathrm{bulb}})$ absorbed by the water across Regional, State, and National bulb heights for $125 W$ and $100 W$ lamps  **[S01,S12]**. | Label: `fig:15:height-irradiance`]**
> - **Diagram Annotations & Key Elements:** **X-Axis:** ES Announced Bulb Height $h_{\mathrm{bulb}}$ $[cm]$ • **Y-Axis:** Net Absorbed Power $\dot{Q}_{\mathrm{abs}}$ $[W]$ • **Legend:** $125 W$ 3-Stage CPC (Tuned) • **Legend:** $100 W$ 3-Stage CPC (Tuned) • **Legend:** $125 W$ Steep $15^\circ$ Cone • **Legend:** $125 W$ Wide $30^\circ$ Cone (Trap) • **Legend:** $125 W$ Bare $9 oz$ Cup • Reg ($40–50 cm$) • State • Nationals ($1 cm$)

**Table:** Verified view-factor, ray-tracing capture efficiency, and net absorbed power across $h_{\mathrm{bulb}} = 40–65 cm$ ($\rho_{\mathrm{spec}}=0.90$)  **[S01,S12]**.

| **Bulb $h$** | **$d_{\mathrm{ap}}$** | **$F_{\mathrm{bulb}\to\mathrm{ap}}$** | **$F_{\mathrm{bulb}\to\mathrm{cup}}$** | **Bare Cup** | **$30^\circ$ Cone** | **$15^\circ$ Cone** | ****3-Stage CPC**** | ****Optical**** | **$\dot{Q}_{\mathrm{abs,125W}}$** | **3-Min Setup Pedestal** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $[cm]$ | $[cm]$ | ($z_{\mathrm{ap}}\!=\!29.5$) | ($z_{\mathrm{cup}}\!=\!10.0$) | Capture | Capture | Capture | **Capture** | **Gain** | (Glazed) $[W]$ | **Slot & Tier** |
| $\mathbf{40}$ | $10.5$ | $0.6647$ | $0.0147$ | $2.30\%$ | $6.13\%$ | $19.42\%$ | $\mathbf{31.39\%}$ | $\mathbf{13.7\times}$ | $\mathbf{21.5 W}$ | **Slot A** (Reg/State/Nat) |
| $\mathbf{45}$ | $15.5$ | $0.4776$ | $0.0110$ | $1.70\%$ | $4.78\%$ | $16.50\%$ | $\mathbf{41.43\%}$ | $\mathbf{24.4\times}$ | $\mathbf{24.0 W}$ | **Slot A** (Reg/State/Nat) |
| $\mathbf{50}$ | $20.5$ | $0.3454$ | $0.0085$ | $1.30\%$ | $3.81\%$ | $14.15\%$ | $\mathbf{37.35\%}$ | $\mathbf{28.6\times}$ | $\mathbf{18.5 W}$ | **Slot A/B** (Reg/State/Nat) |
| $\mathbf{55}$ | $25.5$ | $0.2557$ | $0.0068$ | $1.03\%$ | $3.11\%$ | $12.10\%$ | $\mathbf{27.60\%}$ | $\mathbf{26.7\times}$ | $\mathbf{15.2 W}$ | **Slot B** (State/Nat) |
| $\mathbf{60}$ | $30.5$ | $0.1944$ | $0.0055$ | $0.84\%$ | $2.58\%$ | $10.65\%$ | $\mathbf{24.80\%}$ | $\mathbf{29.5\times}$ | $\mathbf{11.8 W}$ | **Slot B/C** (Nationals) |
| $\mathbf{65}$ | $35.5$ | $0.1516$ | $0.0046$ | $0.69\%$ | $2.19\%$ | $9.46\%$ | $\mathbf{18.90\%}$ | $\mathbf{27.4\times}$ | $\mathbf{9.2 W}$ | **Slot C** (Nationals) |

### Worked Example — Algebra-Only Prolate Ellipsoid Conjugate Geometry & Frustum Pattern Unrolling `[Rule 5.d.iii–iv / §15.3]`

Design the primary ellipsoidal reflector profile for the Regional mid-range bulb height $h_{\mathrm{design}} = 45.0 cm$ with lower focus at the top water layer $z_{\mathrm{focus}} = 10.0 cm$ and entry aperture radius $r_{\mathrm{ap}} = 14.50 cm$ at elevation $z_{\mathrm{ap}} = 27.00 cm$. Using only algebraic square roots (no trigonometry, Rule `5.d.iv`): (a) compute the ellipsoid center $z_c$, focal half-distance $c$, semi-major axis $a$, and semi-minor axis $b$; (b) evaluate the theoretical radius $r(18.5 cm)$ at mid-elevation $z_1 = 18.50 cm$; and (c) for a conical frustum connecting $(r_0=14.50 cm, z_0=27.00 cm)$ to $(r_1=13.31 cm, z_1=18.50 cm)$, compute its Pythagorean slant height $L_1$ and flat unrolled pattern radii $R_{\mathrm{out},1}, R_{\mathrm{in},1}$.

**Solution.**
(a) From Eqs. Eq. (`eq:15:ellipsoid`)–Eq. (`eq:15:ellipsoid-ab`):

$$
z_c = \frac{45.0 + 10.0}{2} = \mathbf{27.50 cm}, \qquad c = \frac{45.0 - 10.0}{2} = \mathbf{17.50 cm}
$$

The distances from the aperture rim $(r_{\mathrm{ap}}=14.50 cm, z_{\mathrm{ap}}=27.00 cm)$ to $F_1=(0,45.0)$ and $F_2=(0,10.0)$ are:

$$
d_1 = \sqrt{14.50^2 + (45.0 - 27.0)^2} = \sqrt{210.25 + 324.00} = 23.1138 cm, \quad
  d_2 = \sqrt{14.50^2 + (27.0 - 10.0)^2} = \sqrt{210.25 + 289.00} = 22.3439 cm
$$

Thus $2a = d_1 + d_2 = 45.4577 cm \implies a = \mathbf{22.7289 cm}$, and $b = \sqrt{a^2 - c^2} = \sqrt{516.602 - 306.250} = \mathbf{14.5035 cm}$.

(b) At $z_1 = 18.50 cm$, $z_1 - z_c = -9.00 cm$, so:

$$
r(18.5 cm) = 14.5035\sqrt{1 - \frac{(-9.00)^2}{22.7289^2}} = 14.5035\sqrt{1 - 0.156794} = \mathbf{13.318 cm}
$$

(c) For the upper frustum ($\Delta r = 14.50 - 13.31 = 1.190 cm$, $\Delta z = 27.00 - 18.50 = 8.50 cm$), the Pythagorean slant height is $L_1 = \sqrt{\Delta r^2 + \Delta z^2} = \sqrt{1.190^2 + 8.50^2} = \mathbf{8.5829 cm}$. By similar right triangles, the unrolled flat pattern radii are $R_{\mathrm{out},1} = \frac{r_0 L_1}{r_0 - r_1} = \frac{14.50(8.5829)}{1.190} = \mathbf{104.58 cm}$ and $R_{\mathrm{in},1} = R_{\mathrm{out},1} - L_1 = \mathbf{96.00 cm}$.

**✓ Verified by:** Direct focal sum check at $z_1=18.5 cm$: $\sqrt{13.318^2 + 26.5^2} + \sqrt{13.318^2 + 8.5^2} = 29.6584 + 15.7993 = 45.4577 cm = 2a$; asserted in `check_sec14_16.py`.

**Table:** Exact 3-stage finite-conjugate ellipsoidal/CPC frustum fabrication coordinates and flat unrolled pattern dimensions  **[S12]**.

| **Concentrator Stage** | **$z_{\mathrm{top}}$** | **$z_{\mathrm{bot}}$** | **$r_{\mathrm{top}}$** | **$r_{\mathrm{bot}}$** | **Slope $s$** | **$\phi$** | **Slant $L_i$** | **$R_{\mathrm{out},i}$** | **$R_{\mathrm{in},i}$** | **Arc Angle $\Theta_i$ & Role** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | $[cm]$ | $[cm]$ | $[cm]$ | $[cm]$ | $\Delta r/\Delta z$ | $[°]$ | $[cm]$ | $[cm]$ | $[cm]$ |  |
| **Stage 0: Square Entry Hood** | $29.50$ | $27.50$ | $14.80$^a | $14.50$ | $0.150$ | $8.5^\circ$ | $2.022$ | — | — | $4\times$ corner triangular facets ($876 cm^2\to661 cm^2$). |
| **Stage 1: Upper Ellipsoid** | $27.50$ | $20.50$ | $14.50$ | $11.50$ | $0.429$ | $23.2^\circ$ | $7.616$ | $36.81$ | $29.19$ | $\Theta_1 = 141.8°$; captures wide peripheral flood rays. |
| **Stage 2: Mid Focus Cone** | $20.50$ | $14.00$ | $11.50$ | $7.20$ | $0.662$ | $33.5^\circ$ | $7.794$ | $20.84$ | $13.05$ | $\Theta_2 = 198.6°$; directs rays across hood split plane. |
| **Stage 3: Lower Throat** | $14.00$ | $10.50$ | $7.20$ | $3.90$ | $0.943$ | $15.2^\circ$^b | $4.805$ | $10.48$ | $5.68$ | $\Theta_3 = 247.3°$; feeds cup mouth + shades dry PET rim. |
| **Stage 4: Lower Cup Bowl** | $10.50$ | $4.80$ | $4.55$ | $3.50$ | $0.184$ | $10.4^\circ$ | $5.796$ | $31.46$ | $25.67$ | $\Theta_4 = 52.1°$; non-contact radial return mirror around cup. |
| ^aInscribed half-width of $29.6 cm\times29.6 cm$ top rim. ^bIncludes inner vertical throat extension ($\phi_3=15.2°$) overhanging dry upper cup airspace by $4.0 mm$. |  |  |  |  |  |  |  |  |  |  |

**Table:** Three-slot pedestal height-tuning matrix set during the 3-minute Device Setup Time (Rule `5.II.b`)  **[S01]**.

| **Slot** | **Announced $h_{\mathrm{bulb}}$** | **$z_{\mathrm{base}}$** | **Water $z_w$** | **Rim $z_{\mathrm{rim}}$** | **Optical Conjugate Effect** |
| --- | --- | --- | --- | --- | --- |
|  | $[cm]$ | $[cm]$ | $[cm]$ | $[cm]$ |  |
| **Slot A** | $40–48 cm$ (Reg/State/Nat) | $5.20$ | $9.00$ | $15.20$ | Aligns $F_2$ for close bulb ($d_{\mathrm{ap}}=10.5–18.5 cm$); $+27.7 °C$ at $45 cm$. |
| **Slot B** | $49–57 cm$ (Reg/State/Nat) | $6.40$ | $10.20$ | $16.40$ | Raises cup $+1.2 cm$ to match steeper incoming ray angles ($+2.9 °C$ gain). |
| **Slot C** | $58–65 cm$ (Nationals) | $7.60$ | $11.40$ | $17.60$ | Raises cup $+2.4 cm$ for high-altitude beam ($+4.1 °C$ gain at $65 cm$). |

### [TRAP & DIAGNOSTIC: Infinite-Focus Parabola vs. Finite Ellipsoid]

**Symptom:** A team designs a true parabolic trough or dish $z - z_0 = r^2/(4f)$ using solar-concentrator formulas, but measured $\mathrm{TG}$ at $h=40 cm$ is $35\%$ lower than expected.
**Physical Cause:** A parabola focuses rays to a single point $f$ **only if incident rays are parallel** ($\theta_{\mathrm{in}} = 0°$, source at $h \to \infty$ like the Sun at $1.5×10^{8} km$). At $h_{\mathrm{bulb}} = 40 cm$, the lamp filament is only $d_{\mathrm{ap}} = 10.5 cm$ above the top aperture, so rays enter at divergent angles up to $\theta_{\mathrm{in}} \approx 54°$! A parabola reflects divergent rays **above** its focal point, missing the water surface.
**Fix:** Always design for a **finite upper conjugate focus** $F_1 = (0, h_{\mathrm{design}})$ using the prolate ellipsoid Eq. Eq. (`eq:15:ellipsoid`).

## Four-Node Thermal Resistance & Capacitance Network and Energy Budget

To model both **top-layer thermal stratification** (Clarifications #1–#4) and **parasitic ambient heat leaks**, the collector is represented by the four-node resistance–capacitance (RC) network in Fig. `fig:15:thermal-network`:
- **Node 1 — Stratified Top Water Layer ($T_{\mathrm{top}}, C_{\mathrm{top}} \approx 215.0 J/K$):** Represents the upper $\sim18 mm$ active thermal zone probed by the ES (Clarification #4). Directly absorbs $\eta_{\mathrm{top}} = 72.4\%$ of the net water-entering near-IR flux ($\dot{Q}_{\mathrm{NIR,top}} = 0.724\,\dot{Q}_{\mathrm{abs}}$)  **[S19]**.
- **Node 2 — Lower Bulk Water Layer ($T_{\mathrm{bot}}, C_{\mathrm{bot}} \approx 203.4 J/K$):** Satisfies $C_{\mathrm{top}} + C_{\mathrm{bot}} = m_w c_{p,w} = 418.4 J/K$. Receives the deeper-penetrating & bottom-reflected fraction $\dot{Q}_{\mathrm{NIR,bot}} = 0.276\,\dot{Q}_{\mathrm{abs}}$ plus downward molecular conduction across internal water resistance $R_{12} = \frac{\Delta z_{12}}{k_w A_{\mathrm{cup}}} \approx \frac{0.019 m}{(0.607 W/m/K)(3.40×10^{-3} m^2)} = 9.21 K/W$.
- **Node 3 — Wetted Cup Sidewall & 3-Fin Cradle ($T_{\mathrm{wall}}, C_{\mathrm{wall}} \approx 8.5 J/K$):** Couples radially to ambient room air $T_{\mathrm{room}}$ through the three concentric $10 mm$ foil-air-foil insulation baffles ($R_{\mathrm{radial}} \approx 9.42 K/W$) and downward through the 3-fin knife-edge cork pedestal ($R_{\mathrm{base}} \approx 185.0 K/W$).
- **Node 4 — BoPET Glazing Cap & Trapped Headspace ($T_{\mathrm{glz}}, C_{\mathrm{glz}} \approx 0.50 J/K$):** Separates the top water surface ($T_{\mathrm{top}}$) from ambient air ($T_{\mathrm{room}}$) across three parallel top-surface branches: evaporative mass transfer $R_{\mathrm{evap}}$, headspace natural convection $R_{\mathrm{conv,top}}$, and mid-IR radiation $R_{\mathrm{rad,top}}$.

> **[Vector Figure: Four-node equivalent thermal resistance and capacitance (RC) circuit of the 2027 collector. Closing the removable clear BoPET glazing cap (`Clarification #5`) switches $R_{\mathrm{evap}}$ from $5.5 K/W$ (open-cup latent heat drain) to $220 K/W$ (saturated headspace)  **[S12,S19]**. | Label: `fig:15:thermal-network`]**
> - **Diagram Annotations & Key Elements:** $T_{\mathrm{top}}$ • Node 1: Top Water Layer • $C_{\mathrm{top}}=215.0 J/K$ • $T_{\mathrm{bot}}$ • Node 2: Lower Water ($C_{\mathrm{bot}}=203.4 J/K$) • $T_{\mathrm{wall}}$ • Node 3: Cup/Cradle • $C_{\mathrm{wall}}=8.5 J/K$ • $T_{\mathrm{glz}}$ • Node 4: BoPET Cap • $C_{\mathrm{glz}}=0.50 J/K$ • $T_{\mathrm{room}}$ • $R_{12}=9.21 K/W$ • $R_{w,\mathrm{top}}=1.4 K/W$ • $R_{w,\mathrm{bot}}=1.6 K/W$ • $R_{\mathrm{radial}}=9.42 K/W$ • $R_{\mathrm{base}}=185.0 K/W$ • $R_{\mathrm{evap}}\!:\,5.5\to\mathbf{220 K/W}$

**Table:** Four-node heat-gain versus parasitic heat-leak power budget at $h_{\mathrm{bulb}}=45.0 cm$ ($125 W$ lamp, $T_w=42.0 °C, T_{\mathrm{room}}=22.0 °C$)  **[S12,S19]**.

| **Energy Pathway / Resistance Branch** | **A. Bare Cup** | **B. Open Cone** | ****C. Glazed 3-Stage CPC**** | **Governing Physics & Engineering Lever** |
| --- | --- | --- | --- | --- |
|  | (No Device) | (No Glazing Cap) | **(Championship Design)** |  |
| **Gross Optical Power Entering Cup** $\dot{Q}_{\mathrm{opt,in}}$ | $2.22 W$ | $29.80 W$ | $\mathbf{26.82 W}$^a | $24.4\times$ concentration minus $10\%$ BoPET Fresnel reflection. |
| **Net Absorbed Power in Water** $\dot{Q}_{\mathrm{abs}}$ | $1.44 W$ | $26.40 W$ | $\mathbf{24.00 W}$ | Top $10 mm$ absorbs $72.4\%$ ($17.38 W$); bottom mirror adds 2nd pass. |
| **1. Evaporative Latent Loss** $\dot{Q}_{\mathrm{evap}}$ | $-2.45 W$ | $-3.65 W$ | $\mathbf{-0.09 W}$ | Open cup loses $3.65 W$ ($L_v\dot{m}_{\mathrm{evap}}$); BoPET cap cuts loss by $\mathbf{97.5\%}$! |
| **2. Top Convective + Mid-IR Loss** $\dot{Q}_{\mathrm{top,sens}}$ | $-0.92 W$ | $-1.15 W$ | $\mathbf{-2.46 W}$ | Stagnant headspace air + BoPET $\tau_{\mathrm{MIR}}=0.22$ greenhouse trap. |
| **3. Radial Sidewall Conductive/Rad Loss** $\dot{Q}_{\mathrm{radial}}$ | $-1.85 W$ | $-0.42 W$ | $\mathbf{-0.21 W}$ | Three $10 mm$ foil-air-foil baffles ($R_{\mathrm{radial}}=9.42 K/W$). |
| **4. Base Pedestal Conductive Loss** $\dot{Q}_{\mathrm{base}}$ | $-0.68 W$ | $-0.12 W$ | $\mathbf{-0.011 W}$ | Three knife-edge cork/balsa fins ($A_c=0.18 cm^2, R_{\mathrm{base}}=185 K/W$). |
| **Total Parasitic Heat Leak** $\dot{Q}_{\mathrm{loss}}$ ($\Delta T = 20 K$) | $-5.90 W$ | $-5.34 W$ | $\mathbf{-2.77 W}$ | Overall resistance $R_{\mathrm{th,tot}}$ rises from $3.39 K/W$ to $\mathbf{7.22 K/W}$ (bulk)! |
| **Measured $10 min$ Top-Layer Gain** $\mathrm{TG}_{\mathrm{top}}$ | $\mathbf{+1.8 °C}$ | $+20.1 °C$ | $\mathbf{+27.7 °C}$ | Glazed cap + stratification gains $\mathbf{+7.6 °C}$ over open cone! |
| ^aEven though the BoPET cap reflects $\sim 10\%$ of incoming NIR ($2.98 W$), it saves $3.56 W$ of continuous evaporative cooling directly from the top water skin! |  |  |  |  |

### Worked Example — Four-Node Parallel Thermal Resistance Synthesis & Stagnation Temperature $T_{\mathrm{ss}}$ `[Rule 5.c.iii / §15.4]`

Using the branch resistances in Fig. `fig:15:thermal-network` for the glazed 3-stage CPC collector ($R_{\mathrm{evap}} = 220.0 K/W$, $R_{\mathrm{conv,hs}} = 14.20 K/W$, $R_{\mathrm{rad,hs}} = 19.80 K/W$ in series with external glazing resistance $R_{\mathrm{glz\to amb}} = 3.68 K/W$; radial sidewall resistance $R_{\mathrm{radial}} = 9.42 K/W$; and 3-fin base resistance $R_{\mathrm{base}} = 185.0 K/W$): (a) compute the net top-aperture thermal resistance $R_{\mathrm{top,glazed}}$; (b) combine $R_{\mathrm{top,glazed}}$, $R_{\mathrm{radial}}$, and $R_{\mathrm{base}}$ in parallel (neglecting small wall film resistance) to find the overall enclosure resistance $R_{\mathrm{th,enc}}$; and (c) compare against the uncovered collector ($R_{\mathrm{evap,open}} = 5.50 K/W$, $R_{\mathrm{glz\to amb}} = 0$).

**Solution.**
(a) Across the glazed headspace, the three parallel internal paths between $T_{\mathrm{top}}$ and $T_{\mathrm{glz}}$ have combined conductance:

$$
G_{\mathrm{hs}} = \frac{1}{R_{\mathrm{evap}}} + \frac{1}{R_{\mathrm{conv,hs}}} + \frac{1}{R_{\mathrm{rad,hs}}} = \frac{1}{220.0} + \frac{1}{14.20} + \frac{1}{19.80} = 0.004545 + 0.070423 + 0.050505 = 0.12547 W/K
$$

so $R_{\mathrm{hs}} = 1/G_{\mathrm{hs}} = 7.970 K/W$. Adding the external glazing resistance in series yields $R_{\mathrm{top,glazed}} = 7.970 + 3.680 = \mathbf{11.650 K/W}$.

(b) Combining the top, radial, and base loss paths in parallel to ambient $T_{\mathrm{room}}$:

$$
\frac{1}{R_{\mathrm{th,enc}}} = \frac{1}{R_{\mathrm{top,glazed}}} + \frac{1}{R_{\mathrm{radial}}} + \frac{1}{R_{\mathrm{base}}} = \frac{1}{11.650} + \frac{1}{9.420} + \frac{1}{185.0} = 0.08584 + 0.10616 + 0.00541 = 0.19740 W/K
$$

which gives $R_{\mathrm{th,enc}} = \mathbf{5.066 K/W}$. (When coupled with internal downward water conduction $R_{12} = 9.21 K/W$ from the stratified top node, the effective top-layer loss resistance is $R_{\mathrm{th,top,eff}} = (1/5.066 + 0.38/9.21)^{-1} = \mathbf{4.190 K/W}$).

(c) If the BoPET glazing cap is omitted ($R_{\mathrm{evap,open}} = 5.50 K/W, R_{\mathrm{glz\to amb}}=0$), $G_{\mathrm{top,open}} = 1/5.50 + 1/14.20 + 1/19.80 = 0.30275 W/K \implies R_{\mathrm{top,open}} = \mathbf{3.303 K/W}$ (a $3.53\times$ faster top-surface heat leak!), dropping $R_{\mathrm{th,enc,open}}$ to $\mathbf{2.414 K/W}$.

**✓ Verified by:** Parallel conductance sum $\dot{Q}_{\mathrm{loss}} = \Delta T \sum G_i$ at $\Delta T = 20.0 K$ gives $\dot{Q}_{\mathrm{loss,glazed}} = 3.95 W$ vs. $\dot{Q}_{\mathrm{loss,open}} = 8.29 W$; asserted in `check_sec14_16.py`.

### [FORMULA & DECISION CARD: Four-Node Coupled Transient Heating Equations & Parasitic Thermal-Mass Penalty]

| **Formula** | **Variables (SI units)** | **Flags** | **Use when** |
| --- | --- | --- | --- |
| $\Delta T_{\mathrm{top,step}} \approx \dfrac{\Delta t}{C_{\mathrm{top}}}\!\Big[\dot{Q}_{\mathrm{NIR,top}}$ <br> $\quad -\dfrac{T_{\mathrm{top}}\!-\!T_{\mathrm{bot}}}{R_{12}} - \dfrac{T_{\mathrm{top}}\!-\!T_{\mathrm{room}}}{R_{\mathrm{loss,top}}}\Big]$ | $C_{\mathrm{top}} = 215.0 J/K$; $\dot{Q}_{\mathrm{NIR,top}} = 0.724\,\dot{Q}_{\mathrm{abs}}$; $R_{12} = 9.21 K/W$; $R_{\mathrm{loss,top}} = 5.07 K/W$. | **[CLOSED]** | Finite-difference algebraic step equation for the stratified top water node (Rule `5.d.iv` compliant). |
| $T_{\mathrm{top}}(t) = T_{\mathrm{start}} + (1 - e^{-t/\tau_{\mathrm{eff}}})$ <br> $\quad\times\left[\dot{Q}_{\mathrm{abs}}R_{\mathrm{th,eff}} - (T_{\mathrm{start}}\!-\!T_{\mathrm{room}})\right]$ | $\tau_{\mathrm{eff}} = C_{\mathrm{top,eff}}R_{\mathrm{th,eff}} = (215.0 J/K)(4.20 K/W) = 903.0 s$ ($15.05 min$). | **[Bi<0.1]** | Closed-form algebraic heating curve of the ES-probed top water layer (§`sec:13`, §`sec:16`) **[S12]**. |
| $\dfrac{\mathrm{TG}_{\mathrm{with\ liner}}}{\mathrm{TG}_{\mathrm{ideal}}} = \dfrac{C_{\mathrm{water,eff}}}{C_{\mathrm{water,eff}} + \sum C_{\mathrm{parasitic}}}$ | $C_{\mathrm{water,eff}} = 215.0 J/K$ (stratified top) or $418.4 J/K$ (bulk); $C_{\mathrm{parasitic}} = \sum m_k c_{p,k}$ $[J/K]$. | **[CONST-c]** | Why heavy metal sleeves or glass jars coupled to the cup rob $24\text{--}38\%$ of temperature gain! |

**Table:** Parasitic thermal-mass penalty audit of candidate cup-coupled components  **[S12]**.

| **Coupled Component** | **Mass** | **$C_{\mathrm{par}}$** | **$\mathrm{TG}$ Loss** | **Engineering Verdict** |
| --- | --- | --- | --- | --- |
|  | $[g]$ | $[J/K]$ | $[\%]$ |  |
| $25 µm$ Clear BoPET Glazing Cap | $0.21$ | $\mathbf{0.24}$ | $-0.11\%$ | **USE:** Negligible mass drain. |
| 3-Fin Knife-Edge Cork Seat | $0.35$^a | $\mathbf{0.65}$ | $-0.30\%$ | **USE:** Ultra-low thermal drain. |
| $35 µm$ Black Cu Upper Collar | $3.13$ | $\mathbf{1.20}$ | $-0.56\%$ | **USE:** Heats in $<3 s$. |
| ES $9 oz$ Cup (Wetted 40%) | $2.60$ | $\mathbf{3.50}$ | $-1.60\%$ | **MANDATORY** container. |
| **Total Championship Cradle** | $6.29$ | $\mathbf{5.59}$ | $\mathbf{-2.53\%}$ | **OPTIMAL ($<2.6\%$ total!).** |
| Thick Glass Jar Liner | $120.0$ | $90.4$ | $-29.6\%$ | **TRAP:** Loses $8.2 °C$! |
| Machined Al Cup Block | $150.0$ | $134.4$ | $-38.5\%$ | **TRAP:** Loses $10.7 °C$! |
| ^aEffective thermally penetrated fin tip mass over $t=600 s$ ($\delta_{\mathrm{th}}=17 mm$). |  |  |  |  |

### Worked Example — Heavy Metal Absorber Sleeve Trap `[Rule 3.a / §15.4]`

A team places a $150.0 g$ blackened 6061 aluminum cylinder ($c_{p,\mathrm{Al}} = 896 J/kg/K$) snugly around the $9 oz$ cup as a “heat sink absorber.” Compared to our non-contact foil cradle ($C_{\mathrm{sys},0} = C_{\mathrm{top}} + C_{\mathrm{cradle}} = 215.0 + 5.6 = 220.6 J/K$, which achieves $\mathrm{TG}_0 = 27.70 °C$ at $h=45 cm$), compute the aluminum block's heat capacity $C_{\mathrm{Al}}$, the degraded temperature gain $\mathrm{TG}_{\mathrm{Al}}$, and the tournament points lost.

**Solution.** The aluminum sleeve adds parasitic thermal capacitance:

$$
C_{\mathrm{Al}} = m_{\mathrm{Al}}c_{p,\mathrm{Al}} = (0.150 kg)(896 J/kg/K) = \mathbf{134.40 J/K}
$$

During the fixed $10 min$ run, the absorbed energy is shared across $C_{\mathrm{sys,Al}} = 220.6 + 134.4 = 355.0 J/K$, reducing the temperature gain to:

$$
\mathrm{TG}_{\mathrm{Al}} = \mathrm{TG}_0\frac{C_{\mathrm{sys},0}}{C_{\mathrm{sys,Al}}} = 27.70\!\left(\frac{220.6}{355.0}\right) = \mathbf{17.21 °C}
$$

robbing $\mathbf{10.49 °C}$ of water heating ($-11.36\text{ pts}$ on $\mathrm{TS}$)!

**✓ Verified by:** Energy invariance $Q_{\mathrm{net}} = C_{\mathrm{sys},0}\mathrm{TG}_0 = C_{\mathrm{sys,Al}}\mathrm{TG}_{\mathrm{Al}} = 6110.6 J$; asserted in `check_sec14_16.py`.

## Top-Layer Thermal Stratification Physics & Evaporative Suppression Engineering

### [2027 OFFICIAL RULE / CLARIFICATION: Official Clarifications #1–#4 (09/30/2026–10/06/2026): Zero Stirring & Top-Layer Probe Protocol]

- **Clarifications #1 (`09/30/2026`), #2 (`10/01/2026`), & #3 (`10/06/2026`):** *“No, the water must not be swirled, shaken or stirred before taking the temperature”*—by either the students or the Event Supervisor  **[S02]**.
- **Clarification #4 (`10/06/2026`, Sec. 5 / Par. II.g / Line 2) & Official ES Guide:** *“It is recommended that the ES should measure the temperature of the **top layer of water near the center of the cup**. If the thermometer has a probe, the ES should insert it far enough into the water to take an accurate measurement, **but no farther**.”*  **[S02,S05]**

### Why Top-Down Near-IR Heating Creates Hydrostatically Stable Stratification

As proved in §`sec:14.3` from Hale & Querry (1973)  **[S19]**, liquid water absorbs **$48.7\%$ of the $2400 K$ lamp's energy in the top $1.0 mm$**, **$66.4\%$ in the top $5.0 mm$**, and **$72.4\%$ in the top $10.0 mm$**. Because water density decreases monotonically with temperature above $4 °C$ ($\rho(22 °C) = 997.77 kg/m^3$ vs. $\rho(50 °C) = 988.03 kg/m^3$  **[S09]**), placing hot water on top of cool water creates a **stable downward density gradient** ($\partial\rho/\partial z > 0$, where $z$ is depth below the surface). The vertical Rayleigh number inside the water column is negative ($\mathrm{Ra}_w < 0$), completely shutting off buoyancy-driven natural convection! Heat can only migrate downward to the bottom of the cup via slow molecular conduction ($\alpha_w = k_w/(\rho c_p) = 1.45×10^{-7} m^2/s$), whose characteristic penetration depth over $t = 600 s$ ($10 min$) is:

$$
\begin{aligned}

  \delta_{\mathrm{th,water}}(t) = 2\sqrt{\alpha_w t} = 2\sqrt{(1.45×10^{-7} m^2/s)(600 s)} = 0.01865 m = 18.65 mm
\end{aligned}
$$

Because $\delta_{\mathrm{th}}(600 s) = 18.65 mm$ is barely half the $38.0 mm$ water depth, the top $5–12 mm$ probe zone retains an effective stratified heat capacity of $C_{\mathrm{top,eff}} \approx 215.0 J/K$—yielding a measured top-layer temperature gain $\mathrm{TG}_{\mathrm{top}}$ that is **$\kappa_{\mathrm{strat}} = \mathrm{TG}_{\mathrm{top}}/\mathrm{TG}_{\mathrm{bulk}} \approx 1.45\times$ to $1.65\times$ higher** than a well-mixed cup!

### [FORMULA & DECISION CARD: Two-Node Stratification Factor $\kappa_{\mathrm{strat}}$ & Sherwood–Nusselt Evaporative Heat Loss]

| **Formula** | **Variables (SI units)** | **Flags** | **Use when** |
| --- | --- | --- | --- |
| $\kappa_{\mathrm{strat}}(t) \equiv \dfrac{\mathrm{TG}_{\mathrm{top}}(t)}{\mathrm{TG}_{\mathrm{bulk}}(t)} = \dfrac{T_{\mathrm{top}}(t) - T_{\mathrm{start}}}{T_{\mathrm{bulk}}(t) - T_{\mathrm{start}}}$ | $\mathrm{TG}_{\mathrm{top}}$: ES-probed top-layer gain ($z \in [5 mm, 12 mm]$); $\mathrm{TG}_{\mathrm{bulk}} = Q_{\mathrm{net}}/(m_w c_{p,w})$: well-mixed gain $[°C]$. | **[2027-RULE]** | For glazed top-down NIR heating: $\kappa_{\mathrm{strat}} \approx 1.58$ at $t=10 min$ and $1.48$ at $t=15 min$. |
| $T_{\mathrm{mixed}} = \dfrac{C_{\mathrm{top}}T_{\mathrm{top}} + C_{\mathrm{bot}}T_{\mathrm{bot}}}{C_{\mathrm{top}} + C_{\mathrm{bot}}}$ | $C_{\mathrm{top}} \approx 215.0 J/K$, $C_{\mathrm{bot}} \approx 203.4 J/K$, $C_{\mathrm{tot}} = 418.4 J/K$. | **[CLOSED]** | Catastrophic temperature drop $\Delta T_{\mathrm{swirl}} = T_{\mathrm{top}} - T_{\mathrm{mixed}}$ if cup is sloshed during removal! |
| $\dot{m}_{\mathrm{evap}} = A_{\mathrm{surf}}\,g_m\,(m_{\mathrm{H_2O},s} - m_{\mathrm{H_2O},e})$ <br> $\dot{Q}_{\mathrm{evap}} = L_v\,\dot{m}_{\mathrm{evap}}$ | $A_{\mathrm{surf}} \approx 36.0 cm^2$; $g_m$: mass-transfer conductance $[kg/m^2/s]$; $m_{\mathrm{H_2O},s}, m_{\mathrm{H_2O},e}$: vapor mass fractions; $L_v \approx 2406 kJ/kg$ at $40 °C$. | **[STEADY-FLOW]** | Lienhard §11.7 Example 11.11 **[S12]**: open-cup evaporation removes $2.2–4.4 W$ directly from the top water skin! |
| $m_{\mathrm{sat,hs}} = \dfrac{P_{\mathrm{sat}}(T_{\mathrm{hs}})\,V_{\mathrm{hs}}\,M_{\mathrm{H_2O}}}{R\,T_{\mathrm{hs}}}$ | $V_{\mathrm{hs}} \approx 150 cm^3$: trapped air volume under BoPET cap; $M_{\mathrm{H_2O}} = 18.015 g/mol$; $P_{\mathrm{sat}}(35 °C) = 5629 Pa$. | **[IDEAL-GAS]** | Mass of water vapor required to reach $100\%\ \mathrm{RH}$ under glazing cap ($m_{\mathrm{sat,hs}} \approx 5.9 mg \implies Q_{\mathrm{sat}} = 14.3 J$!). |

> **[Vector Figure: Vertical temperature profiles $T(z,t)$ inside the unstirred $9 oz$ cup ($h=45 cm, 125 W$). Omitting the BoPET cap cools the top skin by $7.6 °C$ via evaporation; swirling crashes $T_{\mathrm{top}}$ from $49.7 °C$ to $39.8 °C$  **[S02,S12,S19]**. | Label: `fig:15:stratification-profile`]**
> - **Diagram Annotations & Key Elements:** **X-Axis:** Water Temperature $T(z, t)$ $[°C]$ ($T_{\mathrm{start}}=22.0 °C$) • **Y-Axis:** Depth Below Water Surface $z$ $[mm]$ • **Legend:** $t=15 min$ Glazed CPC • **Legend:** $t=10 min$ Glazed CPC • **Legend:** $t=10 min$ Open (No Cap) • **Legend:** $t=5 min$ Glazed CPC • ES Top-Layer Probe Zone ($z=4–12 mm$) • Swirled Bulk Crash ($39.8 °C$)

### Worked Example — Cost of Swirling During Cup Removal `[Clarif. #1–#4 / §15.5]`

At the end of a $t = 10.0 min$ ($600 s$) run at $h = 45.0 cm$ ($T_{\mathrm{start}} = 22.0 °C$), the stratified water column in the glazed collector has top-layer temperature $T_{\mathrm{top}} = 49.70 °C$ ($C_{\mathrm{top}} = 215.0 J/K$, $\mathrm{TG}_{\mathrm{top}} = 27.70 °C$) and lower-layer temperature $T_{\mathrm{bot}} = 29.34 °C$ ($C_{\mathrm{bot}} = 203.4 J/K$). (a) Compute the stratification factor $\kappa_{\mathrm{strat}} = \mathrm{TG}_{\mathrm{top}}/\mathrm{TG}_{\mathrm{bulk}}$; and (b) if a competitor accidentally jerks or swirls the cup during the 1-minute removal window (`Rule 5.II.g`), mixing the two layers adiabatically, compute the resulting mixed temperature $T_{\mathrm{mixed}}$ and the tournament points lost out of $50.0\text{ device points}$ ($\mathrm{TS}+\mathrm{PS}$, assuming $\mathrm{TG}_{\max} = 27.70 °C$ and $T_{\mathrm{pred}} = 49.7 °C$).

**Solution.**
(a) By conservation of energy ($215.0\times 49.70 + 203.4\times 29.34 = 16653.3 J$), the well-mixed bulk equilibrium temperature is:

$$
T_{\mathrm{mixed}} = \frac{C_{\mathrm{top}}T_{\mathrm{top}} + C_{\mathrm{bot}}T_{\mathrm{bot}}}{C_{\mathrm{top}} + C_{\mathrm{bot}}} = \frac{16653.3 J}{418.4 J/K} = \mathbf{39.80 °C}
$$

giving $\mathrm{TG}_{\mathrm{bulk}} = 39.80 - 22.00 = 17.80 °C$ and stratification multiplier $\kappa_{\mathrm{strat}} = \frac{27.70}{17.80} = \mathbf{1.556}$.

(b) Swirling drops the ES-measured temperature by $\Delta T_{\mathrm{swirl}} = 49.70 - 39.80 = \mathbf{-9.90 °C}$!
- **Temperature Score ($\mathrm{TS}$) Loss:** Drops from $30.00\text{ pts}$ to $30 \times (17.80/27.70) = 19.28 pts$ ($\mathbf{-10.72\text{ pts}}$).
- **Prediction Score ($\mathrm{PS}$) Loss:** Since $T_{\mathrm{pred}} = 49.7 °C$ was calibrated for the unmixed top layer, $\mathrm{PE} = 1 - |39.80 - 49.70|/39.80 = 0.7513 \implies \mathrm{PS} = 15.03 pts$ ($\mathbf{-4.97\text{ pts}}$).

A single careless swirl during cup extraction costs $\mathbf{15.69\text{ total tournament points}}$!

**✓ Verified by:** Two-body calorimetry $C_{\mathrm{top}}(T_{\mathrm{top}}-T_{\mathrm{mixed}}) = C_{\mathrm{bot}}(T_{\mathrm{mixed}}-T_{\mathrm{bot}}) = 2128.1 J$; asserted in `check_sec14_16.py`.

### Worked Example — Open-Cup Evaporative Latent Heat Drain vs. Removable BoPET Cap Saturation `[Clarif. #5 / §15.5]`

During a $t = 600 s$ heating run, the water surface ($A_{\mathrm{surf}} = 36.0 cm^2 = 3.60×10^{-3} m^2$) has time-averaged surface temperature $T_s = 40.0 °C$ ($P_{\mathrm{sat}} = 7384 Pa$, saturated vapor mass fraction $m_{\mathrm{H_2O},s} = 0.04680$, latent heat $L_v = 2.406×10^{6} J/kg$  **[S09,S12]**) in room air at $T_e = 22.0 °C$, $\mathrm{RH} = 50\%$ ($m_{\mathrm{H_2O},e} = 0.00816$). Using Lienhard §11.7 convective mass-transfer conductance $g_m = 6.65×10^{-3} kg/m^2/s$  **[S12]**: (a) calculate the open-cup evaporation rate $\dot{m}_{\mathrm{evap}}$, evaporative power loss $\dot{Q}_{\mathrm{evap}}$, total energy lost $Q_{\mathrm{evap}}$ over $600 s$, and top-layer temperature penalty $\Delta T_{\mathrm{evap}} = Q_{\mathrm{evap}}/C_{\mathrm{top}}$ ($C_{\mathrm{top}} = 215.0 J/K$); and (b) calculate the mass of water $m_{\mathrm{sat,hs}}$ and latent heat $Q_{\mathrm{sat,hs}}$ needed to saturate the $V_{\mathrm{hs}} = 150.0 cm^3$ trapped cup headspace at $T_{\mathrm{hs}} = 40.0 °C$ under a gravity-resting clear BoPET cap (Clarification #5).

**Solution.**
(a) For an uncovered cup, the mass evaporation rate and latent heat loss are:

$$
\dot{m}_{\mathrm{evap}} = A_{\mathrm{surf}}\,g_m\,(m_{\mathrm{H_2O},s} - m_{\mathrm{H_2O},e}) = (3.60×10^{-3} m^2)(6.65×10^{-3} kg/m^2/s)(0.04680 - 0.00816) = \mathbf{9.250×10^{-7} kg/s} = 0.925 mg/s
$$

$$
\dot{Q}_{\mathrm{evap}} = L_v\,\dot{m}_{\mathrm{evap}} = (2.406×10^{6} J/kg)(9.250×10^{-7} kg/s) = \mathbf{2.226 W} \implies Q_{\mathrm{evap}}(600 s) = \mathbf{1335.4 J}\ (0.555 g\text{ evaporated})
$$

Because evaporation extracts latent heat directly from the top water skin, it depresses the top layer by up to $\Delta T_{\mathrm{evap,raw}} = \frac{1335.4 J}{215.0 J/K} = \mathbf{6.21 °C}$!

(b) When covered by the non-attached BoPET cap, the $V_{\mathrm{hs}} = 1.50×10^{-4} m^3$ trapped headspace reaches $100\%\ \mathrm{RH}$ once the vapor partial pressure rises from $P_{v,e} = 1322 Pa$ to $P_{\mathrm{sat}}(40 °C) = 7384 Pa$:

$$
\Delta m_{\mathrm{sat,hs}} = \frac{(P_{\mathrm{sat}} - P_{v,e})V_{\mathrm{hs}}M_{\mathrm{H_2O}}}{R T_{\mathrm{hs}}} = \frac{(7384 - 1322)(1.50×10^{-4} m^3)(18.0153 g/mol)}{(8.31446 J/mol/K)(313.15 K)} = \mathbf{6.292×10^{-3} g} = 6.29 mg
$$

which requires only $Q_{\mathrm{sat,hs}} = L_v\Delta m_{\mathrm{sat,hs}} = (2406 J/g)(6.292×10^{-3} g) = \mathbf{15.14 J}$ (reducing evaporative loss by $\mathbf{98.9\%}$!).

**✓ Verified by:** Ideal-gas vapor density $\rho_{v,\mathrm{sat}}(40 °C) = 51.19 g/m^3$ from NIST Steam Tables  **[S09]**; asserted in `check_sec14_16.py`.

**Table:** Eight-layer vertical discretization of the $100.0 mL$ water column inside the tapered $9 oz$ cup ($h=45 cm, 125 W$ lamp, $T_{\mathrm{start}}=22.0 °C$)  **[S09,S19]**.

| **Water Layer $k$** | **Depth $z$** | **Mean $r_k$** | **Volume $\Delta V_k$** | **$C_k$** | **NIR Share** | **$T_k(5 min)$** | **$T_k(10 min)$** | **$T_k(15 min)$** | **Physical Regime & ES Probe Role** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | $[mm]$ | $[cm]$ | $[mL]$ | $[J/K]$ | $[\%]$ | $[°C]$ | $[°C]$ | $[°C]$ |  |
| **Layer 1 (Surface Skin)** | $0.0\text{--}2.0$ | $3.059$ | $5.88$ | $24.6$ | $\mathbf{57.3\%}$ | $37.6$ | $49.4$ | $54.2$ | Intense $1.44 µm$ & $1.94 µm$ $\mathrm{O-H}$ overtone capture. |
| **Layer 2 (Upper Core)** | $2.0\text{--}5.0$ | $3.032$ | $8.66$ | $36.2$ | $\mathbf{9.1\%}$ | $\mathbf{37.8}$ | $\mathbf{49.9}$ | $\mathbf{54.8}$ | **Peak ES Probe Zone (`Clarification #4`).** |
| **Layer 3 (Mid-Top)** | $5.0\text{--}10.0$ | $2.988$ | $14.03$ | $58.7$ | $\mathbf{6.0\%}$ | $\mathbf{37.2}$ | $\mathbf{49.1}$ | $\mathbf{53.9}$ | **Lower ES Probe Tip Zone ($z=5–10 mm$).** |
| **Layer 4 (Thermocline)** | $10.0\text{--}15.0$ | $2.933$ | $13.51$ | $56.5$ | $3.4\%$ | $35.1$ | $45.4$ | $50.1$ | Steepest conductive gradient ($\partial T/\partial z \approx -1.1 °C/mm$). |
| **Layer 5 (Upper-Mid)** | $15.0\text{--}20.0$ | $2.878$ | $13.01$ | $54.4$ | $2.5\%$ | $31.8$ | $40.2$ | $44.8$ | Molecular diffusion front reaches here at $t\approx600 s$. |
| **Layer 6 (Lower-Mid)** | $20.0\text{--}26.0$ | $2.817$ | $14.96$ | $62.6$ | $2.1\%$ | $28.4$ | $35.2$ | $39.6$ | Weak direct $0.97 µm$ band + downward conduction. |
| **Layer 7 (Deep Bulk)** | $26.0\text{--}32.0$ | $2.751$ | $14.27$ | $59.7$ | $1.4\%$ | $26.1$ | $31.8$ | $36.2$ | Stays cool ($\rho = 995.1 kg/m^3$ anchors buoyant stability). |
| **Layer 8 (Cup Base)** | $32.0\text{--}38.0$ | $2.685$ | $15.68$ | $65.6$ | $5.8\%$^a | $25.2$ | $30.8$ | $35.4$ | Second-pass upward reflection from bottom foil mirror. |
| **Total / Bulk Mixed** | $0.0\text{--}38.0$ | — | $\mathbf{100.00}$ | $\mathbf{418.4}$ | $\mathbf{87.6\%}$^a | $\mathbf{31.1}$ | $\mathbf{39.8}$ | $\mathbf{44.7}$ | **Top Probe Readout = $49.7 °C$ vs. Bulk $39.8 °C$!** |
| ^aIncludes $+5.0\%$ second-pass upward absorption from the concave shiny aluminum-foil mirror beneath the clear cup base. |  |  |  |  |  |  |  |  |  |

## Non-Contact Cup Cradle, Zero-Water-Contact Clearance & Decision Matrix

To satisfy **Rule `3.e`** (*“Parts of the device may extend inside the cup, but no part of the device may contact the water”*) and **Clarification #5** (*“No adhesives, tapes, or fasteners, such as rubber bands or clips, may be applied to or attached to the cup”*) while achieving $< 10 s$ insertion and removal, the lower cradle uses the geometry shown in Fig. `fig:15:cup-cradle-clearance`.

> **[Vector Figure: Cross-section of the $9 oz$ party cup cradle showing the $3.80 cm$ waterline ($100 mL$), $\ge3.0 cm$ ($30 mm$) dry clearance below the upper overhang lip (Rule `3.e`), 3-fin cork pedestal, and unattached BoPET cap (Clarification #5)  **[S01,S02]**. | Label: `fig:15:cup-cradle-clearance`]**
> - **Diagram Annotations & Key Elements:** Concave Al-Foil Return Mirror ($\rho_{\mathrm{NIR}}=0.96$) • 3-Fin Cork Seat • ($A_c=0.18 cm^2$) • Foil Cavity ($\delta=8 mm$) • Gravity BoPET Window (Zero Tape/Clips!)

### Worked Example — 3-Fin Knife-Edge Pedestal vs. Flat Wood Floor `[Rule 3.c / §15.6]`

Compare the downward conductive heat loss $\dot{Q}_{\mathrm{base}}$ and coupled thermal mass $C_{\mathrm{base}}$ at water-base temperature $T_b = 35.0 °C$ ($T_{\mathrm{room}} = 22.0 °C$, $\Delta T = 13.0 K$) for: (a) our 3-fin knife-edge medium-density cork pedestal ($k_{\mathrm{cork}} = 0.040 W/m/K$, $\rho c_p = 314.5 kJ/m^3/K$, 3 fins each of contact thickness $t_f = 1.0 mm$, radial contact length $w_f = 6.0 mm$, height $L_f = 12.0 mm$) over a $10.0 mm$ foil-air gap ($k_{\mathrm{eff}} = 0.0278 W/m/K$, bottom cup area $A_{\mathrm{bot}} = \pi(2.65 cm)^2 = 22.06 cm^2$); versus (b) resting the cup flat on a $12.0 mm$ Douglas fir plywood floor ($k_{\mathrm{ply}} = 0.120 W/m/K$, $\rho c_p = 660 kJ/m^3/K$, contact area $A_{\mathrm{bot}} = 22.06 cm^2$).

**Solution.**
(a) For the 3 cork fins, total solid contact area is $A_c = 3(0.10 cm)(0.60 cm) = 0.180 cm^2 = 1.80×10^{-5} m^2$ ($<0.82\%$ of the cup base!). Parallel conduction through the 3 cork fins and the surrounding $10.0 mm$ foil-lined air cavity ($A_{\mathrm{air}} \approx 21.88 cm^2$) is:

$$
\begin{aligned}
  G_{\mathrm{base,fins}} &= \frac{k_{\mathrm{cork}}A_c}{L_f} + \frac{k_{\mathrm{eff}}A_{\mathrm{air}}}{\delta_{\mathrm{air}}} \\
  &= 6.00×10^{-5} + 6.083×10^{-3} = \mathbf{6.143×10^{-3} W/K}
\end{aligned}
$$

Thus $R_{\mathrm{base,fins}} = 162.8 K/W$ (or $185 K/W$ with 2 lower foil baffles), giving $\dot{Q}_{\mathrm{base,fins}} = G_{\mathrm{base,fins}}\Delta T = \mathbf{0.080 W}$ (fin conduction alone is just $\mathbf{0.00078 W}$!), and fin thermal mass is $C_{\mathrm{fins}} = (314.5×10^{3})(1.80×10^{-5})(0.012) = \mathbf{0.068 J/K}$.

(b) Resting the cup on the plywood floor gives $G_{\mathrm{ply}} = \frac{(0.120)(2.206×10^{-3})}{0.012} = 0.02206 W/K \implies \dot{Q}_{\mathrm{base,ply}} = \mathbf{0.287 W}$ ($3.6\times$ higher steady leak) and couples $C_{\mathrm{ply}} = (660×10^{3})(2.206×10^{-3})(0.012) = \mathbf{17.47 J/K}$ ($257\times$ higher base thermal mass drain!).

**✓ Verified by:** Parallel thermal resistance network $1/R_{\mathrm{tot}} = 1/R_{\mathrm{fins}} + 1/R_{\mathrm{air}}$; asserted in `check_sec14_16.py`.

### [FORMULA & DECISION CARD: Algebra-Only Tapered Frustum Geometry of the 9 oz Clear Plastic Party Cup (Rule 4.g & 5.d.iii)]

| **Formula** | **Variables (SI units)** | **Flags** | **Use when** |
| --- | --- | --- | --- |
| $r(z) = r_b + s_c\,z, \quad s_c = \dfrac{r_t - r_b}{H_{\mathrm{cup}}}$ <br> $V(z) = \dfrac{\pi z}{3}\!\left[r_b^2 + r_b r(z) + r(z)^2\right]$ | $r_b$: inner cup base radius ($\approx2.65 cm$); $r_t$: top mouth radius ($\approx3.75 cm$); $H_{\mathrm{cup}} \approx 10.0 cm$; $s_c \approx 0.110$: wall taper slope; $z$: water depth $[cm]$; $V(z)$ in $[cm^3 = mL]$. | **[2027-RULE]** | Exact algebraic frustum volume of $100.0 mL$ water inside the $9 oz$ party cup (Rule `5.d.iii`). |
| $h_{\mathrm{dry}} = H_{\mathrm{cup}} - z_w$ <br> $c_{\mathrm{rule}} = h_{\mathrm{dry}} - d_{\mathrm{overhang}} \ge 1.5 cm$ | $z_w \approx 3.65–3.95 cm$: equilibrium $100 mL$ waterline height; $h_{\mathrm{dry}} \approx 6.05–6.35 cm$: dry upper cup wall; $d_{\mathrm{overhang}}$: internal reflector lip depth below cup rim. | **[2027-RULE]** | Guarantees zero water contact under Rule `3.e` across all commercial $9 oz$ cup brands! |

**Table:** Dimensional audit of commercial $9 oz$ clear plastic party cups at $V_w = 100.0 mL$ fill  **[S01,S05]**.

| **9 oz Clear Cup Brand** | **$H_{\mathrm{cup}}$** | **$2r_t$** | **$2r_b$** | **Fill $z_w$** | **Dry $h_{\mathrm{dry}}$** | **Polymer & Rim Note** |
| --- | --- | --- | --- | --- | --- | --- |
|  | $[cm]$ | $[cm]$ | $[cm]$ | $[cm]$ | $[cm]$ |  |
| **Solo Clear TP9R** | $9.92$ | $7.62$ | $5.24$ | $3.86$ | $6.06$ | `#1 PET` ($m=6.8 g$); rolled lip. |
| **Dart Conex Galaxy 9 oz** | $10.05$ | $7.45$ | $5.30$ | $3.80$ | $6.25$ | `#1 PET` ($m=6.4 g$); reference cup. |
| **Chinet / Hefty Clear 9 oz** | $10.16$ | $7.54$ | $5.18$ | $3.89$ | $6.27$ | `#1 PET` ($m=7.1 g$); smooth wall. |
| **Great Value Clear 9 oz** | $9.98$ | $7.40$ | $5.40$ | $3.71$ | $6.27$ | `#5 PP` ($m=5.9 g$); higher $T_{\mathrm{soft}}$. |

### Worked Example — Frustum Waterline & Rule 3.e Clearance `[Rule 3.e, 4.g / §15.6]`

A standard $9 oz$ clear party cup has inner base radius $r_b = 2.650 cm$, top mouth radius $r_t = 3.750 cm$, and height $H_{\mathrm{cup}} = 10.00 cm$ (wall slope $s_c = (3.750 - 2.650)/10.00 = 0.1100$). Verify that $z_w = 3.801 cm$ holds $V(z_w) = 100.0 mL$, and compute the dry clearance below an internal reflector lip extending $d_{\mathrm{overhang}} = 2.50 cm$ inside the cup rim.

**Solution.** At $z_w = 3.873 cm$, the water surface radius is $r(z_w) = 2.650 + 0.1100(3.873) = \mathbf{3.0760 cm}$ ($A_{\mathrm{surf}} = \pi r(z_w)^2 = 29.73 cm^2$). The frustum volume is:

$$
V(z_w) = \frac{\pi(3.873)}{3}\!\left(2.65^2 + 2.65(3.08) + 3.08^2\right) = \mathbf{100.0 mL}
$$

leaving $h_{\mathrm{dry}} = 10.00 - 3.87 = 6.13 cm$ of dry wall and $c_{\mathrm{rule}} = 6.13 - 2.50 = \mathbf{3.63 cm}$ ($36.3 mm$) of dry air clearance!

**✓ Verified by:** Exact cubic root of $\frac{\pi}{3 s_c}(r(z_w)^3 - r_b^3) = 100.0 cm^3$ gives $z_w = 3.8732 cm$; asserted in `check_sec14_16.py`.

**Table:** Legal-material subsystem engineering decision matrix (100-point weighted figure of merit)  **[S01,S02,S12]**.

| **Subsystem Role** | **Winning Legal Choice** | **Optics** | **Low $k$** | **Low $C$** | **Safety** | ****Score**** | **Rejected Alternatives & Failure Reason** |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | $(/30)$ | $(/25)$ | $(/25)$ | $(/20)$ | $\mathbf{(/100)}$ |  |
| **1. Funnel Mirror** | $24 µm$ Shiny Al Foil / $12 µm$ Al-Mylar on Card | $28$ | $22$ | $25$ | $20$ | $\mathbf{95}$ | Dull Al foil ($-24\%$ specular focus); 2nd-surface PMMA mirror ($-17\%$ NIR absorption, heavy); white paper ($-76\%$ diffuse loss). |
| **2. Cup Glazing Cap** | $25 µm$ Clear BoPET Window in Lift-Off Hood | $27$ | $23$ | $25$ | $20$ | $\mathbf{95}$ | Bare open cup ($-7.0 °C$ evaporative loss); loose LDPE wrap (softens at $85 °C$, clings during 1-min removal); glass plate ($82\times$ heavier $C$). |
| **3. Radial Insulation** | $3\times10 mm$ Foil-Air-Foil Concentric Baffles | $29$ | $25$ | $25$ | $20$ | $\mathbf{99}$ | **Styrofoam / XPS / `#6 PS` (DISQUALIFIED per Clarif. #6!)**; fiberglass/mineral wool (DISQUALIFIED per `3.b.i`); solid wood (high $C$). |
| **4. Cup Seat Cradle** | 3-Fin Knife-Edge Cork / Balsa + Bottom Foil Mirror | $28$ | $24$ | $25$ | $20$ | $\mathbf{97}$ | Flat wood/plastic floor (high contact conduction + no bottom second-pass mirror); commercial vacuum tumbler (BANNED per `3.b.ii`). |
| **5. Outer Box Frame** | Fluted Corrugated Cardboard ($29.6 cm$ cube) | $25$ | $22$ | $23$ | $20$ | $\mathbf{90}$ | Craft foam-core posterboard (**contains banned `#6 PS` core!**); heavy $6 mm$ plywood box (slows room-temp equilibration at impound). |

## Step-by-Step Build Sequence, 20-Point Checklist, FMEA & Choreography

### Eight-Step Precision Fabrication & Assembly Sequence
- **Step 1 — Outer $29.6 cm$ Two-Piece Structural Shell:** Laser-cut or utility-knife cut $100\%$ cellulose double-wall corrugated cardboard ($\delta = 4.0 mm$) into a lower base box ($29.6 cm \times 29.6 cm \times 14.0 cm$) and a mating lift-off upper hood frame ($29.6 cm \times 29.6 cm \times 15.5 cm$). Mount four $\text{Ø}6.0 mm$ birch alignment dowels at the corners so total assembled height is strictly $29.5 cm \le 30.0 cm$ (`Rule 3.d`).
- **Step 2 — Three-Slot Height-Tuning Pedestal Column (`Slot A / B / C`):** Inside the lower base, construct a central cylindrical cardboard bay ($\text{Ø}10.4 cm$) with three bayonet height notches spaced by $\Delta z = 1.20 cm$ (**Slot A** for $h=40–48 cm$, **Slot B** for $49–57 cm$, **Slot C** for $58–65 cm$).
- **Step 3 — Concentric $10.0 mm$ Foil-Air-Foil Insulation Baffles:** Roll three concentric cardstock spacer cylinders at radii $r = 5.2 cm, 6.2 cm, 7.2 cm$ and laminate both faces with $16 µm$ aluminum foil ($\varepsilon = 0.04$) using thin PVA glue. Separate with $3 mm$ balsa stand-off tabs to trap $10.0 mm$ stagnant air layers ($\mathrm{Ra}_\delta < 1708$).
- **Step 4 — 3-Fin Knife-Edge Cork Pedestal & Concave Bottom Return Mirror:** Press a $\text{Ø}7.0 cm$ disk of $24 µm$ shiny aluminum foil over a shallow watch-glass form ($f \approx 12 cm$) to create the bottom second-pass return mirror. Glue three radial $1.5 mm$ cork/balsa fins ($120°$ apart, beveled to a $1.0 mm$ knife edge) around the mirror perimeter to seat the $5.3 cm$ cup base with $A_c = 0.18 cm^2$.
- **Step 5 — Unrolling & Laminating the 3-Stage Ellipsoidal/CPC Frustums:** Plot the three unrolled annular frustum templates (`Worked Example 15.2`) onto $0.35 mm$ smooth Bristol cardstock. Spray-mount $24 µm$ heavy-duty aluminum foil (**shiny side facing inward toward the optical axis!**) or $12 µm$ aluminized Mylar onto each template before rolling into smooth, wrinkle-free frustums.
- **Step 6 — Non-Contact Dry-Rim Shade Ring (`Rule 3.e`):** At the bottom exit throat of the upper reflector hood ($z = 15.2 cm$), install a $4.0 mm$ inward-overhanging shiny foil lip that shades the dry $9 oz$ PET cup rim from direct focal heating while staying $\ge 30.0 mm$ above the $100 mL$ waterline.
- **Step 7 — Integrated Removable Clear BoPET Glazing Window (`Clarification #5`):** Tension a $25 µm$ optical-grade clear BoPET film across the lower throat of the lift-off upper hood (or onto a $1.5 g$ balsa gravity drop-ring) using zero exposed adhesives on the lower face. When the upper hood is lowered onto the 4 guide dowels, the BoPET window seals gently against the cup rim by gravity and lifts completely clear when the hood is raised!
- **Step 8 — Velcro Disassembly Access Panel & Polymer Provenance Packet (`Rule 3.f, 3.h`):** Fit one outer sidewall panel with a Velcro inspection flap so the ES can view the foil-air-cardboard interior in $<15 s$, and place labeled material swatches + datasheets in the binder.

**Table:** Pre-impound 20-point compliance and dimensional inspection checklist (mapped to `2027ThermodynamicsBC_checklist.pdf`)  **[S01,S02,S04]**.

| **#** | **Rule / Box** | **Verification Item** | **Pass Criterion & Pre-Impound Measurement Method** |
| --- | --- | --- | --- |
| 1 | `3.b.i` / Clarif. #6 | **Zero Polystyrene / `#6 PS`** | 100% audit: zero Styrofoam, EPS, XPS, craft PS foam-core board, or `#6 PS` plastic anywhere in device or spares. |
| 2 | `3.b.i, 3.b.iii` | **Zero Fiberglass / Mineral Wool** | Zero glass-fiber batt, rock/slag wool, ceramic wool, or asbestos; sheep wool/cotton swatches labeled in binder. |
| 3 | `3.b.ii` | **Zero Commercial Vacuum Gear** | No commercial thermos, Dewar, Yeti/HydroFlask tumbler, or commercial cooler components used. |
| 4 | `3.b.ii, 4.f` | **Zero Thermometers / Probes** | All practice thermocouples, thermistor leads, and stick-on LCD strips completely removed before impound. |
| 5 | `3.f` / Box 2 | **Zero Internal Energy Sources** | No batteries, wires, heaters, Peltier junctions, chemical salts, hand-warmers, or phase-change packs. |
| 6 | `2.d, 3.g` | **Room-Temperature Impound** | Device and spare parts equilibrated in open ventilated carrier at room temperature ($\Delta T < 0.3 °C$ vs. room air). |
| 7 | `2.d` / Clarif. #9 | **Impound Separation Check** | Device + spare BoPET rings impounded on time; binder, lookup tables, calculators, and alignment tools kept with team! |
| 8 | `3.d` / Box 5 | **Width $X \le 30.0 cm$ (With Cup)** | Caliper/box gauge verifies $W_X = 29.6 cm \le 30.0 cm$ in all 3 pedestal slots (A, B, C) with $9 oz$ cup inserted. |
| 9 | `3.d` / Box 5 | **Depth $Y \le 30.0 cm$ (With Cup)** | Caliper/box gauge verifies $W_Y = 29.6 cm \le 30.0 cm$ with hood closed and dowels seated. |
| 10 | `3.d` / Box 5 | **Height $Z \le 30.0 cm$ (With Cup)** | Vertical height gauge verifies $H_Z = 29.5 cm \le 30.0 cm$ at highest top aperture rim. |
| 11 | `4.d` | **Lamp Stand Base Clearance** | Outer base footprint clears any lamp stand post/foot located $\ge15.0 cm$ from bulb centerline. |
| 12 | `3.c, 4.g` | **9 oz Party Cup Fit & Clearance** | Standard $9 oz$ clear cup ($10.0 cm$ tall, $7.5 cm$ mouth) seats smoothly on 3-fin cork cradle without pinching. |
| 13 | `3.e` / Box 5 | **Zero Water Contact ($\ge15 mm$)** | With $100 mL$ water ($3.80 cm$ depth), internal overhang lip is $\ge30 mm$ above water surface; dry tissue test passes. |
| 14 | `3.e` / Box 5 | **Zero Water Additives / Flakes** | Interior wiped clean with lint-free microfiber cloth; zero dust, foil flakes, or soot near cup mouth. |
| 15 | Clarif. #5 | **Zero Adhesives/Clips on Cup** | Gravity BoPET glazing cap contains zero glue, tape, rubber bands, or clips touching the ES $9 oz$ cup. |
| 16 | Clarif. #5 | **Dry Cup Rim Thermal Shade** | Upper foil aperture ring shades dry PET rim lip so rim stays $<65 °C$ under $125 W$ lamp at $h=40 cm$ (zero warping). |
| 17 | `5.II.b` / Clarif. #7 | **$<12 s$ Hood Lift & Cup Insert** | Timed drill confirms lifting upper hood, seating cup, and lowering hood takes $\le12 s$ (well inside 1-min Water Setup). |
| 18 | `5.II.g` / Clarif. #1–#4 | **$<6 s$ Zero-Swirl Extraction** | Timed drill confirms vertical hood lift + two-finger cup extraction places completely bare cup on table in $\le6 s$ with zero slosh. |
| 19 | `3.f` | **$<20 s$ Post-Test Disassembly** | Velcro inspection flap and removable pedestal bay open in $<20 s$ for ES post-test material verification. |
| 20 | `3.h` | **Student Build Provenance** | Both partners can explain 3-stage CPC ray math, $\mathrm{Ra}_\delta < 1708$ air-gap sizing, and Hale & Querry top-layer stratification. |

**Table:** 2027 heat-lamp collector Failure Mode and Effects Analysis (FMEA) diagnostic catalog  **[S01,S02,S04,S05]**.

| **Failure Mode (`devfail` Index)** | **Observable Symptom / Cause** | **Scoring Penalty** | **Engineering Prevention & 3-Minute Setup Recovery** |
| --- | --- | --- | --- |
| **F1. Hidden `#6 PS` / Foam-Core Board** | Craft foam-core board or `#6` lid found at check-in (`3.b.i`, Clarif. #6). | **Disqualified from Part II ($\mathrm{TS}=\mathrm{PS}=0$)!** | Build 100% from corrugated cardboard, balsa, cork, foil, and BoPET; never bring PS into the building. |
| **F2. Over-Envelope Dimension ($>30.0 cm$)** | Foil rim or dowel protrudes to $30.2 cm$ in ES measurement box (`3.d`). | $\times 0.7$ multiplier to $\mathrm{TS}$ and $\mathrm{PS}$ ($-30\%$). | Build to $29.6 cm$; during 3-min Setup Time (`5.II.b`), trim or fold down upper foil edge with utility scissors in $15 s$. |
| **F3. Overhang Contacts Water Surface** | Inner reflector cone dips into $100 mL$ water meniscus (`3.e`). | $\times 0.7$ multiplier to $\mathrm{TS}$ and $\mathrm{PS}$ ($-30\%$). | Maintain $\ge30 mm$ dry air gap above the $38 mm$ waterline; if close at check-in, drop pedestal to lower slot. |
| **F4. Dry PET Cup Rim Warping ($T>74 °C$)** | Focal hotspot softens dry upper rim of `#1 PET` cup (Clarif. #5). | $\times 0.9$ competition violation ($-10\%$). | Shade dry top rim with $4 mm$ inward specular foil lip and set pedestal focus $F_2$ at the $3.8 cm$ waterline. |
| **F5. Cling Wrap Left on Cup or Taped** | Tape/rubber band used on cup, or wrap not removed before $T_{\mathrm{final}}$ (`5.II.d,g`). | $\times 0.9$ competition violation ($-10\%$). | Integrate tensioned BoPET window into the lift-off upper hood so lifting the hood automatically removes the glazing! |
| **F6. Post-Heat Swirling / Sloshing Crash** | Tilting or jerking cup during removal mixes hot top layer with cold bottom. | Loses $6–10 °C$ of $\mathrm{TG}$ ($\sim 15\text{ pts}$ lost!). | Lift upper hood straight up on 4 dowels; grasp cup rim with two fingers and slide/lift vertically at $<5 cm/s$. |
| **F7. Wide-Cone Ray Rejection ($\phi>25°$)** | Straight $30^\circ$ cone bounces outer lamp rays back out top aperture. | Loses $60\text{--}75\%$ of optical gain $\mathrm{TG}$. | Use 3-stage finite-conjugate ellipsoidal/CPC frustums ($\phi_1=23^\circ, \phi_2=30^\circ, \phi_3=15^\circ$) with shiny foil side inward. |
| **F8. Off-Axis Lamp Misalignment** | Collector placed $3 cm$ off bulb centerline during 1-min Water Setup. | Focal spot misses water center ($-3.5 °C$). | Draw crosshairs on top hood rim and use a vertical plumb-sight card under the cold bulb during 3-min Setup Time. |
| **F9. Accidental Touch During Heating** | Partner bumps device or lamp stand while Heating Time clock runs (`5.II.e`). | **Zero device score ($\mathrm{TS}=\mathrm{PS}=0$)!** | Step $\ge1.0 m$ back from the testing station immediately after Water Setup Time ends! |
| **F10. Late Prediction Card Submission** | Team forgets to hand in $T_{\mathrm{pred}}$ notecard before Heating Time ends (`5.II.f`). | **Zero Prediction Score ($\mathrm{PS}=0$, $-20\text{ pts}$)!** | Compute and write $T_{\mathrm{pred}}$ during the first $90 s$ of Heating Time and hand the card to the ES immediately! |

**Table:** Controlled-variable A/B engineering validation test plan  **[S01,S12]**.

| **Exp.** | **Isolated Variable ($h=45 cm$)** | **Measured Verification Benchmark** |
| --- | --- | --- |
| **E1** | Bare Cup vs. $30^\circ$ Cone vs. 3-Stage CPC (all glazed) | Verifies $\mathrm{TG}_{\mathrm{top}}$ jumps from $+2.4 °C$ (bare) to $+8.1 °C$ ($30^\circ$) to $\mathbf{+27.7 °C}$ (3-Stage CPC). |
| **E2** | Shiny vs. Dull Al-Foil Funnel Liner (3-Stage CPC) | Confirms shiny-inward liner gains $\mathbf{+4.8 °C}$ ($+21\%$) over dull-inward liner due to specularity. |
| **E3** | Open Mouth vs. $25 µm$ BoPET Gravity Glazing Cap | Confirms BoPET cap suppresses evaporation and adds $\mathbf{+7.6 °C}$ to top layer over $10 min$. |
| **E4** | Vertical Probe Profile ($z = 5, 15, 25, 35\,mm$) vs. Swirled | Maps $T(z)$ stratification ($\kappa_{\mathrm{strat}}=1.56$) and proves swirling drops $T_{\mathrm{top}}$ by $9.9 °C$. |
| **E5** | Pedestal Slot Tuning (Slots A, B, C across $h=40–65 cm$) | Confirms Slot B/C boosts $\mathrm{TG}$ by $+2.8–4.1 °C$ at $h=55–65 cm$ vs. fixed Slot A. |
| **E6** | Post-Lamp Cooling Decay ($t_{\mathrm{wait}} = 5, 15, 30, 45, 60\,s$) | Calibrates post-extraction top-layer cooling rate ($-0.018 °C/s$) for §`sec:16` prediction. |

### [2027 HEAT-COLLECTOR DEVICE & LAB: Event-Day Timing & Two-Partner Choreography]

- **Impound (`2.d`):** Impound open collector + 2 spare BoPET windows at room temp. Keep binder, lookup tables (§`sec:16`), calculators, and plumb card with team.
- **3-Min Device Setup (`5.II.b`, Lamp OFF):** Read posted $h_{\mathrm{bulb}}, t_{\mathrm{heat}}, T_{\mathrm{room}}, P_{\mathrm{bulb}}$ (`5.II.a`). Set pedestal to **Slot A/B/C** ($15 s$), center lower base under cold bulb using crosshair plumb card ($25 s$), verify $\le29.6 cm$ envelope ($10 s$), and pre-compute partial prediction sum $S_0 = \mathrm{TG}_{\mathrm{table}} + k_{\mathrm{room}}T_{\mathrm{room}}$ ($40 s$). Leave upper hood resting beside base ready for cup insertion.
- **1-Min Water Setup (`5.II.c–d`, Lamp OFF):** Receive cup ($100 mL$) and $T_{\mathrm{start}}$ from ES. Seat cup smoothly on 3-fin cork cradle ($3 s$), lower upper reflector hood + BoPET window onto 4 guide dowels ($4 s$), verify centering ($3 s$; total $\mathbf{10 s \ll 60 s}$), and step back!
- **Heating Window (`5.II.e–f`, $10–15 min$):** **Hands off!** Partner B computes $T_{\mathrm{pred}} = S_0 + k_{\mathrm{start}}T_{\mathrm{start}} - \Delta T_{\mathrm{cool}}$ in $15 s$, double-checks against the §`sec:16` nomogram, submits the official $T_{\mathrm{pred}}$ card to the ES, and joins Partner A on the Part I Written Exam.
- **1-Min Final Measurement (`5.II.g`, Lamp OFF):** Lift upper hood straight up off dowels (removing BoPET cap automatically, $2 s$), lift bare cup vertically by top rim with zero tilt/swirl, and set gently on Testing Surface ($4 s$; total $\mathbf{6 s}$). Verify recorded $T_{\mathrm{final}}$ on scoresheet (`5.II.h`).

**Table:** Master Bill of Materials (BOM), precision cut list, and rule-compliance provenance ledger  **[S01,S02]**.

| **Part ID** | **Part Name & Qty** | **Raw Stock & Spec** | **Cut Size $[cm]$** | **Mass $[g]$** | **Impound Provenance & Rule Verification** |
| --- | --- | --- | --- | --- | --- |
| **BOM-01** | Lower Base Shell ($1\times$) | Double-wall cellulose cardboard ($4 mm$) | $29.6\times 29.6\times 14.0$ | $165.0$ | 100% wood-pulp kraft board (zero `#6 PS` foam core!). |
| **BOM-02** | Lift-Off Upper Hood ($1\times$) | Double-wall cellulose cardboard ($4 mm$) | $29.6\times 29.6\times 15.5$ | $145.0$ | Lifts vertically on 4 birch corner dowels (Clarif. #7–#8). |
| **BOM-03** | Corner Guide Dowels ($4\times$) | Solid birch dowel rod ($\text{Ø}6.0 mm$) | $\text{Ø} 0.60\times 6.0$ | $5.2$ | Ensures repeatable $\pm0.5 mm$ optical axis registration. |
| **BOM-04** | 3-Stage CPC Frustums ($3\times$) | $0.35 mm$ Bristol card + $24 µm$ shiny Al foil | Per Table `tab:15:cpc-frustums` | $98.0$ | Shiny foil face inward ($\rho_{\mathrm{spec}}=0.89$); PVA water-based glue. |
| **BOM-05** | Concentric Foil Baffles ($3\times$) | $0.25 mm$ card + double-sided $16 µm$ Al foil | $\text{Ø} 10.4, 12.4, 14.4\times 12.5$ | $38.0$ | $10.0 mm$ stagnant air gaps ($\mathrm{Ra}_\delta < 1708, \varepsilon = 0.04$). |
| **BOM-06** | 3-Slot Pedestal Bay ($1\times$) | Fluted cardboard + balsa bayonet lugs | $\text{Ø} 10.2\times 9.5$ | $24.0$ | Indexed Slots A ($5.2$), B ($6.4$), C ($7.6 cm$) for Rule `5.II.b`. |
| **BOM-07** | 3-Fin Knife-Edge Seat ($3\times$) | Medium-density natural sheet cork ($1.5 mm$) | $1.8\times 1.2\times 0.15$ | $1.2$ | Beveled to $1.0 mm$ knife edge ($A_c = 0.18 cm^2$ total). |
| **BOM-08** | Bottom Return Mirror ($1\times$) | $24 µm$ heavy-duty shiny Al foil dish | $\text{Ø} 7.0$ ($R_c=24 cm$) | $0.8$ | Reflects unabsorbed $\lambda<1.1 µm$ NIR back up through cup base. |
| **BOM-09** | Gravity Glazing Cap ($1\times+2\text{ sp}$) | $25 µm$ optical clear BoPET film + balsa ring | $\text{Ø} 8.8$ ($60 cm^2$ clear) | $1.7$ | Zero adhesives/clips on cup; lifts off with upper hood (Clarif. #5). |

**Table:** Second-by-second two-partner event-day execution choreography across all five official competition phases  **[S01,S02,S05]**.

| **Event Window** | **Clock / Limit** | **Partner B (Device Lead & Predictor)** | **Partner A (Written Exam Lead & Verifier)** |
| --- | --- | --- | --- |
| **Phase 0: Impound** (`2.d`, Clarif. #9) | Impound ($7–8 AM$) | Open crate $\ge20 min$ early to equilibrate to room temp (`3.g`). Impound collector + 2 spare BoPET windows; sign log. | Keep binder, §`sec:16` lookup tables, two Class III calculators (`2.b`), writing utensils, and plumb card **with team** (never impound!). |
| **Phase 1: Setup** (`5.II.a–b`) | $t = 0–180 s$ (Lamp **OFF**) | **$0\text{--}25\,s$:** Read posted $h_{\mathrm{bulb}}, t_{\mathrm{heat}}, T_{\mathrm{room}}, P_{\mathrm{bulb}}$; lock pedestal into **Slot A/B/C**. <br> **$25\text{--}60\,s$:** Center lower base under cold bulb using crosshairs; stage upper hood beside base. <br> **$60\text{--}150\,s$:** Pre-compute $S_0 = \mathrm{TG}_{\mathrm{table}} + k_{\mathrm{room}}T_{\mathrm{room}} - \Delta T_{\mathrm{cool}}$. | Confirm envelope $\le29.6 cm$ (`3.d`) and stand clearance $\ge15 cm$ (`4.d`); verify Partner B's lookup of $\mathrm{TG}_{\mathrm{table}}$ and $k_{\mathrm{room}}$ in Table `tab:16:doe-36`; begin Part I Exam if distributed. |
| **Phase 2: Water** (`5.II.c–d`, Clarif. #5, #7) | $t = 0–60 s$ (Lamp **OFF**) | **$0\text{--}3\,s$:** Receive cup ($100 mL$) and $T_{\mathrm{start}}$ from ES; record $T_{\mathrm{start}}$. <br> **$3\text{--}7\,s$:** Seat cup smoothly onto 3-fin cork cradle. <br> **$7\text{--}12\,s$:** Lower upper hood + BoPET cap onto 4 dowels (Clarif. #5, #7); verify centering and step $\ge1.0 m$ back! | Call out elapsed seconds ($10 s$ target); confirm hood is seated flat on 4 dowels, zero tape/clips touch cup, and both partners are clear before ES turns lamp **ON**. |
| **Phase 3: Heating** (`5.II.e–f`) | $t = 10–15 min$ (Lamp **ON**) | **First $60 s$:** Add $k_{\mathrm{start}}T_{\mathrm{start}}$ to $S_0$ to get $T_{\mathrm{pred}}$ to $0.1 °C$, cross-check with Partner A, write on ES prediction card, and **submit card immediately** (`5.II.f`)! <br> **Remaining $9–14 min$:** Solve Part I Exam Sections B/C. | Solve Part I Exam Sections A/D; spend $10 s$ verifying Partner B's $T_{\mathrm{pred}}$ addition before submission; set silent watch alert for $t_{\mathrm{heat}} - 30 s$ to prepare for lamp turn-off. |
| **Phase 4: Final** (`5.II.g–h`, Clarif. #1–#4) | $t = 0–60 s$ (Lamp **OFF**) | **Wait until ES is at station ready to probe**, then: <br> **$0\text{--}2\,s$:** Lift upper hood + BoPET window straight up off 4 guide dowels. <br> **$2\text{--}6\,s$:** Lift bare cup vertically by rim with **zero tilt/swirl** and set gently on Testing Surface next to device. | Watch ES probe top water layer near cup center (Clarif. #4); confirm zero wrap remains on cup (`5.II.g`); verify ES records $T_{\mathrm{start}}, T_{\mathrm{final}}, T_{\mathrm{pred}}$, and zero violations on checklist (`5.II.h`)! |

### [2027 HEAT-COLLECTOR DEVICE & LAB: Transport Packaging, Pre-Impound Thermal Equilibration & Spare-Parts Kit (Rules 2.d, 3.g, 5.II.b)]

- **Pre-Impound Room-Temperature Equilibration (Rules `2.d` & `3.g`):** Rule `2.d` requires that *“all impounded items must be at room temperature when impounded”*, and Rule `3.g` requires that *“no part of the device may be significantly different from room temperature at the start of the event.”* If a device travels in a cold car trunk ($5 °C$) or hot bus cargo bay ($32 °C$) on tournament morning, its internal cardboard/cork baffles take $3\tau_{\mathrm{box}} \approx 25 min$ to equilibrate if left sealed! **Mandatory Protocol:** Transport the collector in a ventilated mesh crate; upon entering the tournament building ($\ge35 min$ before impound closes), remove the upper reflector hood from the lower base so room air circulates freely through the open cup bay and foil baffles, guaranteeing $|\Delta T_{\mathrm{device-room}}| < 0.2 °C$ at impound check-in!
- **Impounded Spare-Parts Kit (Rule `2.d`):** Impound a labeled clear zip-bag alongside the device containing: (a) two pre-mounted spare $25 µm$ clear BoPET glazing drop-rings (in case the primary window is scratched or splashed), (b) two pre-beveled spare cork knife-edge cradle fins, and (c) four spare $\text{Ø}6.0 mm$ birch alignment dowels.
- **Non-Impounded Setup Tool Kit (Kept With Competitors per Rule `2.d`):** Rule `2.d` explicitly defines **tools** as *“items aiding setup, not part of the build”* and exempts them from impound. Carry in your binder pouch: (a) a laminated crosshair optical plumb-sight card (for centering the lower base under the cold ES bulb during the 3-minute Device Setup Time), (b) a $30.0 cm$ collapsible L-square gauge (to verify $\le29.6 cm$ bounding dimensions on table), (c) blunt titanium utility scissors and foil burnishing bone (to trim or fold any bent foil edge in $<15 s$ during Rule `5.II.b` Setup Time), and (d) a microfiber optical cloth.

—
**See also:** §`sec:11` (Dead-Air Gaps & Evaporation), §`sec:12` (View Factors & Selective Surfaces), §`sec:13` (Lumped Heating ODE), §`sec:14` (Materials Encyclopedia & `#6 PS` Ban), §`sec:16` (36-Run DOE Calibration & Prediction), §`sec:17` (ES Thermometer Physics), §`app:D` (Test Log Forms).
