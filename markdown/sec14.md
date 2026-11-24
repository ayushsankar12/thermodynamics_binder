<!-- Source: src/sec14.tex | Tab: Tab 6: DEVICE | Target: 10 pp -->
# §14: Material, Optical & Insulation Property Encyclopedia {#sec:14}

> **[SCOPE: REQUIRED | 2027 Rules 3.b.i–iii, 3.e, 5.c.iii & Official Clarifications #5, #6 (All Tournament Levels)]**

Selecting materials for the 2026–2027 Division C Thermodynamics heat-collecting device requires simultaneous optimization across **two distinct electromagnetic wavebands** and **three thermophysical transport regimes**  **[S01,S12]**. Under Rules `3.a`–`3.h` and `4.a`–`4.g`, an Event Supervisor (ES) downward-facing $100–125 W$ untinted incandescent reflector heat lamp suspended at $h_{\mathrm{bulb}} = 40–65 cm$ irradiates $100 mL$ of room-temperature water inside a $9 oz$ clear plastic party cup enclosed within a $30.0 cm \times 30.0 cm \times 30.0 cm$ bounding cube  **[S01,S05]**. Every material in the collector must satisfy four quantitative criteria: (1) **high near-infrared specular reflectance or transmittance** at the lamp's Wien peak ($\lambda_{\max,\mathrm{lamp}} \approx 1.21 µm$), (2) **strong mid-infrared radiative trapping** at the warm water's emission peak ($\lambda_{\max,\mathrm{water}} \approx 9.40 µm$), (3) **low parasitic thermal conductivity $k$ and volumetric heat capacity $\rho c_p$**, and (4) **absolute compliance with Rule `3.b.i–iii` and Official Clarification #6**, which strictly ban polystyrene/Styrofoam/`#6 PS`, fiberglass, mineral wool, and asbestos  **[S01,S02]**.

## Two-Band Radiative Selectivity & Thermophysical Selection Framework

Because the tungsten filament of a $100–125 W$ heat lamp operates at $T_{\mathrm{fil}} \approx 2300–2450 K$ (nominal $2400 K$) while the heated water and cup walls remain near $T_w \approx 295–330 K$ ($22–57 °C$), the incident and re-emitted radiation fields occupy non-overlapping spectral bands  **[S07,S12]**:

$$
\begin{aligned}

  \lambda_{\max,\mathrm{lamp}} = \frac{b}{T_{\mathrm{fil}}} = \frac{2897.772 µm K}{2400 K} = 1.207 µm\ (\text{Near-IR}), \qquad
  \lambda_{\max,\mathrm{water}} = \frac{b}{T_w} = \frac{2897.772 µm K}{308.15 K} = 9.404 µm\ (\text{Mid-IR})
\end{aligned}
$$

Over $96\%$ of the lamp's glass-transmitted optical power falls in the short-wave visible and near-infrared band ($\lambda \in [0.38 µm, 2.75 µm]$), whereas over $98\%$ of the thermal radiation emitted by the water, cup, and internal baffles falls in the long-wave mid-infrared band ($\lambda \in [4.5 µm, 30 µm]$)  **[S12]**.

### [FORMULA & DECISION CARD: Two-Band Optical Balance, Specularity & Parasitic Thermal Capacitance]

| **Formula** | **Variables (SI units)** | **Flags** | **Use when** |
| --- | --- | --- | --- |
| $\alpha_\lambda + \rho_\lambda + \tau_\lambda = 1$ | $\alpha_\lambda$: spectral absorptance; $\rho_\lambda$: reflectance; $\tau_\lambda$: transmittance $[-]$. For opaque solids ($\tau_\lambda = 0$), $\rho_\lambda = 1 - \alpha_\lambda$. | **[2027-RULE]** | Conservation of radiant energy at any interface **[S12]**. |
| $\rho_{\mathrm{NIR,tot}} = \rho_{\mathrm{NIR,spec}} + \rho_{\mathrm{NIR,diff}}$ | $\rho_{\mathrm{NIR,spec}}$: mirror-like specular reflectance ($\theta_r = \theta_i$); $\rho_{\mathrm{NIR,diff}}$: Lambertian diffuse scatter $[-]$. | **[2027-RULE]** | Concentrating cones require high $\rho_{\mathrm{NIR,spec}} \ge 0.85$; diffuse walls scatter rays out the top aperture. |
| $\varepsilon_\lambda(T) = \alpha_\lambda(T)$ <br> $\alpha_{\mathrm{NIR}} \neq \varepsilon_{\mathrm{MIR}}$ | $\alpha_{\mathrm{NIR}} \equiv \alpha(\lambda \approx 1.2 µm)$; $\varepsilon_{\mathrm{MIR}} \equiv \varepsilon(\lambda \approx 9.4 µm)$; selectivity ratio $S_{\alpha/\varepsilon} = \alpha_{\mathrm{NIR}}/\varepsilon_{\mathrm{MIR}}$ $[-]$. | **[STATE/NAT]** | Kirchhoff's law holds at each $\lambda$; non-gray surfaces decouple NIR capture from MIR loss **[S12]**. |
| $q''_{\mathrm{net}} = \alpha_{\mathrm{NIR}} q''_{\mathrm{NIR}} - \varepsilon_{\mathrm{MIR}}\sigma(T_s^4 - T_e^4)$ | $q''_{\mathrm{NIR}}$: incident lamp irradiance $[W/m^2]$; $\sigma = 5.6704×10^{-8} W/m^2/K^4$; $T_s, T_e$ in $[K]$. | **[STATE/NAT]** | Net radiative heat flux absorbed by an opaque collar or water surface **[S12]**. |
| $C'' = \rho c_p \delta = \dfrac{C_{\mathrm{comp}}}{A_{\mathrm{comp}}}$ <br> $\delta_{\mathrm{th}}(t) = 2\sqrt{\alpha t}, \quad \alpha = \dfrac{k}{\rho c_p}$ | $\rho$: density $[kg/m^3]$; $c_p$: specific heat $[J/kg/K]$; $\delta$: thickness $[m]$; $C''$: areal heat capacity $[J/m^2/K]$; $\alpha$: thermal diffusivity $[m^2/s]$. | **[CONST-c]** | Minimizing parasitic thermal mass ($C_{\mathrm{comp}} \ll C_w = 418.4 J/K$) and transient heat penetration **[S12]**. |

> **[Vector Figure: Two-band spectral selectivity map comparing near-infrared lamp absorptance $\alpha_{\mathrm{NIR}}$ ($\lambda \approx 1.2 µm$) against mid-infrared thermal emittance $\varepsilon_{\mathrm{MIR}}$ ($\lambda \approx 9.4 µm$) across reflectors, selective absorbers, liquid water, and diffuse white surfaces  **[S12,S24]**. | Label: `fig:14:two-band-optical`]**
> - **Diagram Annotations & Key Elements:** **X-Axis:** Mid-IR Thermal Emittance $\varepsilon_{\mathrm{MIR}}$ at $\lambda \approx 9.4 µm$ ($308 K$ Water Peak) $[-]$ • **Y-Axis:** Near-IR Lamp Absorptance $\alpha_{\mathrm{NIR}}$ at $\lambda \approx 1.2 µm$ $[-]$ • **Legend:** Metallic Reflectors (Al Foil, Mylar, Sheet) • **Legend:** Selective Solar/NIR Coatings (Cr, CuO, Cermet) • **Legend:** Broadband Absorbers & Liquid Water ($\ge35 mm$) • **Legend:** White Paint/Paper & 2nd-Surface PMMA Mirror • Zone I: Specular Reflectors & Shields ($\rho_{\mathrm{NIR}}\!\to\!1, \varepsilon_{\mathrm{MIR}}\!\to\!0$) • Zone II: Selective Absorbers ($\alpha_{\mathrm{NIR}}/\varepsilon_{\mathrm{MIR}} \gg 1$) • Zone III: Blackbody / Water Absorbers • Zone IV: Diffuse White Trap ($\varepsilon_{\mathrm{MIR}}\!\approx\!0.92$) • Gray-Body Locus ($\alpha_{\mathrm{NIR}} = \varepsilon_{\mathrm{MIR}}$) • Shiny Al Foil ($0.035, 0.04$) • Polished Al Sheet ($0.05, 0.07$) • Black Cr on Ni ($S=10.6$) • $\mathrm{CuO}$ on Cu ($S=5.6$) • Ni-Black ($S=4.8$) • Thin Anodized Al • Carbon Soot ($0.95, 0.96$)

### Worked Example — Two-Band Net Radiative Heat Flux: Selective vs. Non-Selective vs. White Collar `[Rule 5.c.vi / §14.1]`

A concentrating funnel delivers a near-IR lamp irradiance of $q''_{\mathrm{NIR}} = 4500 W/m^2$ onto a non-contact upper absorber collar of area $A_c = 40.0 cm^2 = 4.00×10^{-3} m^2$ operating at $T_s = 62.0 °C = 335.15 K$ inside a room-temperature surround at $T_e = 22.0 °C = 295.15 K$. Compare the net radiative power $\dot{Q}_{\mathrm{net}} = A_c[\alpha_{\mathrm{NIR}}q''_{\mathrm{NIR}} - \varepsilon_{\mathrm{MIR}}\sigma(T_s^4 - T_e^4)]$ captured by: (a) selective Black Chrome on Ni foil ($\alpha_{\mathrm{NIR}} = 0.95$, $\varepsilon_{\mathrm{MIR}} = 0.09$), (b) non-selective Matte Black Acrylic Paint ($\alpha_{\mathrm{NIR}} = 0.94$, $\varepsilon_{\mathrm{MIR}} = 0.89$), and (c) White Acrylic Paint ($\alpha_{\mathrm{NIR}} = 0.26$, $\varepsilon_{\mathrm{MIR}} = 0.90$)  **[S12]**.

**Solution.** The blackbody exitance difference between $T_s = 335.15 K$ and $T_e = 295.15 K$ is:

$$
\Delta M_{bb} = \sigma(T_s^4 - T_e^4) = (5.670374×10^{-8} W/m^2/K^4)\left(335.15^4 - 295.15^4\right) = 715.49 W/m^2 - 430.35 W/m^2 = 285.14 W/m^2
$$

Evaluating $q''_{\mathrm{net}} = \alpha_{\mathrm{NIR}}(4500 W/m^2) - \varepsilon_{\mathrm{MIR}}(285.14 W/m^2)$ and multiplying by $A_c = 4.00×10^{-3} m^2$:
- **Selective Black Chrome ($\alpha_{\mathrm{NIR}}=0.95, \varepsilon_{\mathrm{MIR}}=0.09$):** $q''_{\mathrm{net}} = 4275.00 - 25.66 = 4249.34 W/m^2 \implies \dot{Q}_{\mathrm{net}} = \mathbf{17.00 W}$ (re-radiation loss is only $0.103 W$, or $0.60\%$ of absorbed flux).
- **Matte Black Paint ($\alpha_{\mathrm{NIR}}=0.94, \varepsilon_{\mathrm{MIR}}=0.89$):** $q''_{\mathrm{net}} = 4230.00 - 253.78 = 3976.22 W/m^2 \implies \dot{Q}_{\mathrm{net}} = \mathbf{15.90 W}$ (unshielded mid-IR re-radiation loses $1.015 W$, or $9.9\times$ more than Black Chrome).
- **White Acrylic Paint ($\alpha_{\mathrm{NIR}}=0.26, \varepsilon_{\mathrm{MIR}}=0.90$):** $q''_{\mathrm{net}} = 1170.00 - 256.63 = 913.37 W/m^2 \implies \dot{Q}_{\mathrm{net}} = \mathbf{3.65 W}$ (loses $74\%$ by diffuse NIR reflection and radiates mid-IR at $\varepsilon_{\mathrm{MIR}}=0.90$ like a blackbody).

**✓ Verified by:** Direct Stefan–Boltzmann flux evaluation and linearized check $h_{\mathrm{rad,bb}} = 4\sigma T_m^3 = 7.122 W/m^2/K \implies h_{\mathrm{rad,bb}}(40\,K) = 284.9 W/m^2$ ($0.09\%$ agreement); asserted in `check_sec14_16.py`.

## Optical Reflector Encyclopedia & The Shiny vs. Dull Aluminum Foil Myth

In a 2027 heat-lamp collector, reflective surfaces perform two physically distinct duties: (1) **optical beam concentration** inside the upper funnel (redirecting downward lamp rays at $\lambda \approx 0.4–2.7 µm$ into the $7.5 cm$ cup mouth), and (2) **mid-infrared radiant barrier shielding** inside the lower insulation cradle (blocking $\lambda \approx 5–25 µm$ thermal radiation across stagnant air gaps). Table `tab:14:reflectors` compiles verified thermophysical and spectral properties for all candidate reflectors  **[S12,S24]**.

**Table:** Thermophysical and two-band optical properties of reflector and radiant-barrier materials at $T = 20–25 °C$  **[S01,S02,S12,S24]**.

| **Reflector Material** | **$\rho$** | **$c_p$** | **$k$** | **$C''$ ($\delta$)** | **$\rho_{\mathrm{NIR,tot}}$** | **$\rho_{\mathrm{NIR,spec}}$** | **$\varepsilon_{\mathrm{MIR}}$** | **$T_{\max}$** | **2027 Legality & Optical/Thermal Role** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | $[kg/m^3]$ | $[J/kg/K]$ | $[W/m/K]$ | $[J/m^2/K]$ | $1.2 µm$ | (Focus) | $9.4 µm$ | $[°C]$ |  |
| **Al Foil — Shiny Side** ($\delta=16 µm$ std) | $2707$ | $905$ | $237$ | $39.2$ | $0.96$ | $\mathbf{0.88}$ | $0.035$ | $600$ | **LEGAL.** Primary funnel liner; high specularity focuses beam; zero fire risk ($T_m=660 °C$) **[S12]**. |
| **Al Foil — Dull Side** ($\delta=16 µm$ std) | $2707$ | $905$ | $237$ | $39.2$ | $0.95$ | $0.62$ | $0.042$ | $600$ | **LEGAL.** Identical to shiny side as an internal MIR shield ($\varepsilon_{\mathrm{MIR}}\approx 0.04$), but $30\%$ lower specular focus. |
| **Heavy-Duty Al Foil** ($\delta=24 µm$ shiny) | $2707$ | $905$ | $237$ | $58.8$ | $0.96$ | $\mathbf{0.89}$ | $0.035$ | $600$ | **LEGAL.** Resists creasing during cone rolling while adding only $1.76 J/K$ per $300 cm^2$. |
| **Aluminized BoPET** (Mylar, $\delta=12 µm$) | $1390$ | $1170$ | $0.18$ | $\mathbf{19.5}$ | $0.96$ | $\mathbf{0.93}$ | $0.035$ | $150$ | **LEGAL.** Highest flexible mirror specularity ($\rho_{\mathrm{spec}}\ge 0.92$) and lowest thermal mass; orient Al face to lamp. |
| **Polished Al Sheet** (6061/1100, $0.30 mm$) | $2700$ | $896$ | $167$ | $725.8$ | $0.93$ | $0.87$ | $0.050$ | $500$ | **LEGAL.** Self-supporting rigid cone without wrinkles; isolate thermally from cup due to higher $C''$ **[S12]**. |
| **1st-Surface Al/Ag Mirror** (on $1.5 mm$ substrate) | $1180$ | $1460$ | $0.17$ | $2584$ | $0.97$ | $\mathbf{0.96}$ | $0.025$ | $85$ | **LEGAL.** Bare front metallic coating avoids substrate NIR absorption; ideal for planar faceted CPC funnels. |
| **2nd-Surface PMMA Mirror** (`#7` Acrylic, $2.0 mm$) | $1180$ | $1460$ | $0.17$ | $3446$ | $0.83$ | $0.82$ | $0.920$ | $85$ | **LEGAL (`#7` PMMA, NOT `#6` PS).** Double pass through PMMA absorbs $17\%$ of NIR $>1.6 µm$ **[S12]**. |
| **Silvered Glass Mirror** (Soda-lime, $2.0 mm$) | $2480$ | $750$ | $1.10$ | $3720$ | $0.87$ | $0.86$ | $0.940$ | $250$ | **LEGAL.** High optical flatness, but double glass pass absorbs NIR $>2.7 µm$ and adds high mass **[S12]**. |
| **White Cardstock / Acrylic Paint** ($0.30 mm$) | $790$ | $1340$ | $0.14$ | $317.6$ | $0.74$ | $\mathbf{0.04}$ | $\mathbf{0.930}$ | $120$ | **LEGAL — TRAP!** $96\%$ diffuse scatter bounces rays out top; emits mid-IR like a blackbody ($\varepsilon=0.90\text{--}0.98$) **[S12]**. |
| **Sintered White PTFE** (Teflon sheet, $1.0 mm$) | $2200$ | $1050$ | $0.25$ | $2310$ | $0.89$ | $0.05$ | $0.880$ | $260$ | **LEGAL.** Pure Lambertian diffuse reflector; poor directional concentrator **[S12]**. |

### [2027 HEAT-COLLECTOR DEVICE & LAB: Debunking the Shiny vs. Dull Aluminum Foil Myth: Hemispherical Shield vs. Specular Funnel]

A classic Science Olympiad question asks whether the **shiny (bright) side** or **dull (matte) side** of household aluminum foil performs better in a thermal device. The rigorous physical answer depends on whether the foil acts as a **flat insulation radiant barrier** or an **optical concentrating mirror**:
- **Manufacturing Origin (Pack-Rolling):** Household foil ($16–24 µm$) is rolled in two stacked sheets during the final finishing pass because thin single sheets tear under roll tension. The outer faces contacting the highly polished steel work rolls emerge **mirror-shiny** (root-mean-square roughness $\sigma_r \approx 0.03–0.06 µm \ll \lambda_{\mathrm{NIR}}$), while the inner faces pressing against each other undergo free grain deformation and emerge **satin-dull** ($\sigma_r \approx 0.25–0.45 µm$).
- **Why Both Sides Perform Identically in Insulation Air Gaps (Myth Debunked):** At mid-infrared thermal wavelengths ($\lambda \approx 9.4 µm \gg \sigma_r$), surface micro-roughness is sub-wavelength on both sides. Total hemispherical emissivity differs by less than $0.008$ ($\varepsilon_{\mathrm{MIR,shiny}} \approx 0.035$ vs. $\varepsilon_{\mathrm{MIR,dull}} \approx 0.042$), and total hemispherical NIR reflectance differs by $\le 1\%$ ($\rho_{\mathrm{NIR,tot}} = 0.96$ vs. $0.95$). Inside a flat $N$-shield insulation cavity, radiative transfer $\dot{Q}_{\mathrm{rad}} \propto (2/\varepsilon - 1)^{-1}$ changes by $< 0.3\%$ regardless of orientation!
- **Why the Shiny Side Wins Decisively Inside the Concentrating Funnel ($+26\%$ to $+47\%$ Gain):** At near-IR lamp wavelengths ($\lambda \approx 0.7–1.5 µm$), the dull side's $0.35 µm$ grain facets satisfy the Beckman–Spizzichino scattering criterion ($4\pi\sigma_r\cos\theta_i/\lambda \gtrsim 1$), converting $\sim 33\%$ of reflected energy into wide-angle **diffuse scatter** ($\rho_{\mathrm{NIR,spec}} \approx 0.62$, $\rho_{\mathrm{NIR,diff}} \approx 0.33$). Since roughly half of diffusely scattered rays travel upward and escape the top aperture, only $\rho_{\mathrm{eff,dull}} \approx \rho_{\mathrm{spec}} + 0.35\rho_{\mathrm{diff}} \approx 0.735$ reaches the cup per bounce, whereas the shiny side ($\rho_{\mathrm{NIR,spec}} \approx 0.88$, $\rho_{\mathrm{NIR,diff}} \approx 0.08$) delivers $\rho_{\mathrm{eff,shiny}} \approx 0.908$ per bounce ($+23.5\%$ more power on 1 bounce and $0.908^2/0.735^2 = \mathbf{1.526\times}$ more power on 2 bounces!). **Rule:** Always orient the **shiny side facing the lamp beam** inside the concentrating cone, and pull the foil taut over a smooth substrate so wrinkles do not create retro-reflecting facets.

### Worked Example — Multi-Bounce Ray Delivery & Parasitic Thermal Mass: Shiny Foil vs. Dull Foil vs. White Paper `[Rule 3.a / §14.2]`

An optical concentrator intercepts $\dot{Q}_{\mathrm{cone,in}} = 42.0 W$ of downward near-IR lamp rays on its reflective side walls (area $A_w = 0.120 m^2$). Due to the funnel geometry, $65\%$ of wall-incident rays undergo $k=1$ bounce and $35\%$ undergo $k=2$ bounces before entering the cup aperture. Using single-bounce forward delivery efficiency $\eta_1 = \rho_{\mathrm{NIR,spec}} + f_d\,\rho_{\mathrm{NIR,diff}}$ with forward diffuse view factor $f_d = 0.35$, compute the optical power $\dot{Q}_{\mathrm{deliv}} = \dot{Q}_{\mathrm{cone,in}}(0.65\,\eta_1 + 0.35\,\eta_1^2)$ delivered to the cup and the reflector wall heat capacity $C_w = C'' A_w$ for: (a) $16 µm$ Shiny Al Foil ($\rho_{\mathrm{spec}}=0.88, \rho_{\mathrm{diff}}=0.08$), (b) $16 µm$ Dull Al Foil ($\rho_{\mathrm{spec}}=0.62, \rho_{\mathrm{diff}}=0.33$), and (c) $0.30 mm$ White Cardstock ($\rho_{\mathrm{spec}}=0.04, \rho_{\mathrm{diff}}=0.70$).

**Solution.** First compute the single-bounce forward efficiency $\eta_1 = \rho_{\mathrm{spec}} + 0.35\,\rho_{\mathrm{diff}}$ and two-bounce weighted transmission $\eta_{\mathrm{cone}} = 0.65\,\eta_1 + 0.35\,\eta_1^2$:
- **Shiny Al Foil ($16 µm$):** $\eta_1 = 0.88 + 0.35(0.08) = 0.9080$. Weighted transmission: $\eta_{\mathrm{cone}} = 0.65(0.9080) + 0.35(0.9080)^2 = 0.5902 + 0.2886 = \mathbf{0.8788}$ ($87.9\%$). Delivered power: $\dot{Q}_{\mathrm{deliv}} = 42.0(0.8788) = \mathbf{36.91 W}$. Wall heat capacity: $C_w = (39.2 J/m^2/K)(0.120 m^2) = \mathbf{4.70 J/K}$.
- **Dull Al Foil ($16 µm$):** $\eta_1 = 0.62 + 0.35(0.33) = 0.7355$. Weighted transmission: $\eta_{\mathrm{cone}} = 0.65(0.7355) + 0.35(0.7355)^2 = 0.4781 + 0.1893 = \mathbf{0.6674}$ ($66.7\%$). Delivered power: $\dot{Q}_{\mathrm{deliv}} = 42.0(0.6674) = \mathbf{28.03 W}$ (loses $\mathbf{8.88 W}$, or $24.1\%$ of concentrated power, to upward diffuse scatter!).
- **White Cardstock ($0.30 mm$):** $\eta_1 = 0.04 + 0.35(0.70) = 0.2850$. Weighted transmission: $\eta_{\mathrm{cone}} = 0.65(0.2850) + 0.35(0.2850)^2 = 0.18525 + 0.02843 = \mathbf{0.2137}$ ($21.4\%$). Delivered power: $\dot{Q}_{\mathrm{deliv}} = 42.0(0.2137) = \mathbf{8.97 W}$ (a $75.7\%$ optical loss compared to shiny foil, plus $C_w = 38.1 J/K$ and $26\%$ wall heating!).

**✓ Verified by:** Ray-bounce polynomial identity $\dot{Q}_{\mathrm{deliv}}/\dot{Q}_{\mathrm{in}} = \sum p_k \eta_1^k$ and energy conservation $\alpha_{\mathrm{wall}} + \rho_{\mathrm{escape}} + \eta_{\mathrm{cone}} = 1$; asserted in `check_sec14_16.py`.

## Absorber Coatings, Selective Surfaces & Liquid Water Near-IR Spectroscopy

A widespread misconception transferred from legacy solar-oven builds is that the $9 oz$ clear plastic cup must be wrapped in thick black construction paper to absorb radiation. In reality, liquid water itself is a **highly selective near-infrared and mid-infrared absorber**  **[S12,S19,S20]**. While pure water is transparent to human vision ($\lambda = 0.40–0.70 µm$, penetration depth $\delta_p > 1.6 m$), a $2400 K$ tungsten heat lamp emits $91\%$ of its radiation at infrared wavelengths $\lambda > 0.70 µm$, where water's $\mathrm{O-H}$ stretching and bending vibrational overtones absorb intensely within the **top $1–10 mm$** of the water column! Table `tab:14:absorbers` catalogs solid absorber coatings alongside liquid water, and Fig. `fig:14:water-nir-depth` + Table `tab:14:water-bands` present the exact Hale & Querry (1973)  **[S19]** and Kou, Labrie & Chylek (1993)  **[S20]** spectral data.

**Table:** Thermophysical and spectral properties of broadband absorbers, wavelength-selective surfaces, and liquid water  **[S09,S12,S19,S24]**.

| **Absorber / Surface** | **$\rho$** | **$c_p$** | **$k$** | **$\alpha_{\mathrm{NIR}}$** | **$\varepsilon_{\mathrm{MIR}}$** | **$\dfrac{\alpha_{\mathrm{NIR}}}{\varepsilon_{\mathrm{MIR}}}$** | **$T_{\max}$** | **2027 Rule Legality & Engineering Assessment** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | $[kg/m^3]$ | $[J/kg/K]$ | $[W/m/K]$ | $1.2 µm$ | $9.4 µm$ | $[-]$ | $[°C]$ |  |
| **Liquid Water Layer** ($100 mL$, depth $L=38 mm$) | $997.8$ | $4181.3$ | $0.607$ | $\mathbf{0.83}$ | $\mathbf{0.96}$ | $0.86$ | $100$ | **TARGET FLUID.** Direct volumetric NIR absorption deposits $66.4\%$ in top $5 mm$ and $72.4\%$ in top $10 mm$ **[S09,S12,S19]**. |
| **Selective: Black Cr on Ni** (Solar foil on collar) | $8900$ | $445$ | $91$ | $\mathbf{0.95}$ | $\mathbf{0.09}$ | $\mathbf{10.56}$ | $350$ | **LEGAL** on device cradle (never glue to cup!). Absorbs $95\%$ of NIR while suppressing MIR loss by $10\times$ **[S12]**. |
| **Selective: Sputtered Cermet** (on thin steel/Al substrate) | $7850$ | $475$ | $55$ | $\mathbf{0.96}$ | $\mathbf{0.16}$ | $\mathbf{6.00}$ | $400$ | **LEGAL** commercial solar-absorber ribbon for non-contact upper cup radiation collar **[S12]**. |
| **Selective: $\mathrm{CuO}$ on Copper** (Ebanol C blackened Cu foil) | $8954$ | $384$ | $398$ | $\mathbf{0.90}$ | $\mathbf{0.16}$ | $\mathbf{5.63}$ | $300$ | **LEGAL.** Ultra-high conductivity ($k=398 W/m/K$) spreads heat around upper water zone **[S12]**. |
| **Selective: Nickel Black** (electroplated on foil) | $8900$ | $445$ | $91$ | $0.81$ | $0.17$ | $4.76$ | $300$ | **LEGAL.** Durable low-emittance absorber surface **[S12]**. |
| **Thin Black Anodized Al** ($0.10 mm$ collar sleeve) | $2700$ | $896$ | $167$ | $0.88$ | $0.24\text{--}0.82$ | $1.1\text{--}3.7$ | $400$ | **LEGAL.** Thin ($\le2 µm$) $\mathrm{Al_2O_3}$ pore layer is semi-selective; thick anodize has $\varepsilon_{\mathrm{MIR}}\approx 0.82$ **[S24]**. |
| **Matte Black High-Temp Paint** (Carbon black in acrylic) | $1200$ | $1400$ | $0.22$ | $\mathbf{0.94}$ | $0.83\text{--}0.92$ | $1.02\text{--}1.13$ | $150\text{--}650$ | **LEGAL** on device parts only. High $\alpha_{\mathrm{NIR}}$, but high $\varepsilon_{\mathrm{MIR}}$ requires outer glazing or foil shield **[S12]**. |
| **Carbon Soot / Lampblack** (deposited carbon layer) | $1700$ | $710$ | $0.10$ | $\mathbf{0.96}$ | $0.95$ | $1.01$ | $400$ | **CAUTION:** Must be sealed so zero soot flakes fall into water (Rule `3.e` zero-additive rule) **[S01,S12]**. |
| **Blackened $35 µm$ Cu / $24 µm$ Al Foil Collar** | $8954$ | $384$ | $398$ | $0.94$ | $0.04$ (back) | Tunable | $300$ | **LEGAL.** $100 cm^2$ collar has tiny mass ($C=0.86–1.20 J/K$, $<0.3\%$ of water) and bare $\varepsilon=0.04$ outer face! |
| **Matte Black Paper / Cardstock** ($0.25 mm$ sleeve) | $790$ | $1340$ | $\mathbf{0.14}$ | $0.92$ | $0.93$ | $0.99$ | $120$ | **DESIGN TRAP:** Blocks direct NIR from penetrating clear cup wall while conducting poorly ($k=0.14 W/m/K$) across air gap! |

> **[Vector Figure: Liquid water $1/e$ optical penetration depth $\delta_p(\lambda) = 1/\mu_a(\lambda)$ across the near-IR heat-lamp spectrum  **[S19,S20]**. | Label: `fig:14:water-nir-depth`]**
> - **Diagram Annotations & Key Elements:** **X-Axis:** Wavelength $\lambda$ $[µm]$ • **Y-Axis:** $1/e$ Penetration Depth $\delta_p(\lambda) = 1/\mu_a$ $[mm]$ • **Legend:** $\delta_p(\lambda)$ (Hale & Querry  **[S19]**) • Top $10 mm$ ES Probe Zone • Cup Water Depth ($38 mm$) • $2400 K$ Lamp Peak ($1.21 µm$) • $9.62 mm$ • $1.44 µm$ ($0.34 mm$) • $1.94 µm$ ($0.088 mm$)

**Table:** Liquid water spectral absorption $\mu_a(\lambda)$ and single-pass absorption fraction $1 - e^{-\mu_a z}$  **[S19,S20]**.

| **$\lambda$** | **$\mu_a(\lambda)$** | **$\delta_p$** | **Top $2 mm$** | **Top $10 mm$** | **Vibrational Band** |
| --- | --- | --- | --- | --- | --- |
| $[µm]$ | $[/cm]$ | $[mm]$ | $[\%]$ | $[\%]$ |  |
| $0.50$ | $0.00025$ | $40{,}000$ | $0.005$ | $0.025$ | Visible window |
| $0.70$ | $0.0060$ | $1667$ | $0.12$ | $0.60$ | Red edge |
| $0.97$ | $0.450$ | $22.2$ | $8.6$ | $36.2$ | $3\text{rd}$ $\mathrm{O-H}$ overtone |
| $\mathbf{1.20}$ | $\mathbf{1.040}$ | $\mathbf{9.62}$ | $\mathbf{18.8}$ | $\mathbf{64.7}$ | **$2400 K$ Wien peak** |
| $1.32$ | $1.380$ | $7.25$ | $24.1$ | $74.8$ | $2200 K$ Wien peak |
| $\mathbf{1.44}$ | $\mathbf{29.40}$ | $\mathbf{0.340}$ | $\mathbf{99.7}$ | $\mathbf{100.0}$ | **$1\text{st}$ $\mathrm{O-H}$ overtone** |
| $\mathbf{1.94}$ | $\mathbf{114.0}$ | $\mathbf{0.088}$ | $\mathbf{100.0}$ | $\mathbf{100.0}$ | **$\mathrm{O-H}$ stretch+bend** |
| $2.50$ | $90.48$ | $0.111$ | $100.0$ | $100.0$ | Near-IR upper band |
| $2.95$ | $12{,}694$ | $0.00079$ | $100.0$ | $100.0$ | Fund. $\mathrm{O-H}$ stretch |
| **Planck $2400 K$ Integrated:** |  |  | $\mathbf{57.3\%}$ | $\mathbf{72.4\%}$ | ($\mathbf{66.4\%}$ in top $5 mm$; $\mathbf{82.6\%}$ in $35 mm$) |

### Worked Example — Beer–Lambert Near-IR Attenuation & Bottom-Mirror Second-Pass Gain in Water `[Rule 5.c.vi / §14.3]`

Monochromatic rays enter a $100 mL$ water column of vertical depth $L = 3.80 cm$ ($38.0 mm$) at normal incidence. Air–water Fresnel reflection at the top surface is $R_F = [(n_w - 1)/(n_w + 1)]^2 = [(1.325 - 1)/(1.325 + 1)]^2 = 0.01955$ ($1.96\%$). An aluminum-foil mirror ($\rho_b = 0.96$) rests beneath the clear cup bottom (cup-base two-pass transmittance $\tau_b = 0.92$). For (a) $\lambda_1 = 0.97 µm$ ($\mu_a = 0.450 /cm$), (b) $\lambda_2 = 1.20 µm$ ($\mu_a = 1.040 /cm$), and (c) $\lambda_3 = 1.44 µm$ ($\mu_a = 29.40 /cm$), compute the fraction of incident power absorbed in the top $z_1 = 1.00 cm$ during the first downward pass, and the total fraction absorbed over the full column after the bottom-mirror second pass.

**Solution.** By Beer–Lambert's law  **[S19]**, the single-pass fraction absorbed between $z=0$ and depth $z$ is $f_1(z) = (1 - R_F)(1 - e^{-\mu_a z})$. The power reaching depth $L = 3.80 cm$ is $(1-R_F)e^{-\mu_a L}$, of which a fraction $\rho_{\mathrm{eff}} = \rho_b\tau_b = (0.96)(0.92) = 0.8832$ reflects back upward through thickness $L$, adding $\Delta f_2 = (1-R_F)e^{-\mu_a L}\,\rho_{\mathrm{eff}}(1 - e^{-\mu_a L})$:
- **At $\lambda_1 = 0.97 µm$ ($\mu_a = 0.450 /cm$):** Top $1.00 cm$: $f_1(1.0 cm) = 0.98045(1 - e^{-0.450}) = \mathbf{35.53\%}$. Full single pass ($L=3.80 cm$): $f_1(L) = 0.98045(1 - e^{-1.710}) = 80.32\%$. Second pass adds $\Delta f_2 = 0.98045(e^{-1.710})(0.8832)(1 - e^{-1.710}) = \mathbf{12.83\%}$, raising total absorption to $\mathbf{93.15\%}$.
- **At $\lambda_2 = 1.20 µm$ ($\mu_a = 1.040 /cm$, Wien peak):** Top $1.00 cm$: $f_1(1.0 cm) = 0.98045(1 - e^{-1.040}) = \mathbf{63.40\%}$. Full single pass: $f_1(L) = 0.98045(1 - e^{-3.952}) = 96.16\%$. Second pass adds $\Delta f_2 = \mathbf{1.63\%}$, yielding $\mathbf{97.79\%}$ total absorption.
- **At $\lambda_3 = 1.44 µm$ ($\mu_a = 29.40 /cm$, $\mathrm{O-H}$ overtone):** Top $1.00 cm$: $f_1(1.0 cm) = 0.98045(1 - e^{-29.40}) = \mathbf{98.05\%}$ (all $98.05\%$ is absorbed within the top $1.5 mm$!).

**✓ Verified by:** Exponential attenuation integral $\int_0^z \mu_a I_0 e^{-\mu_a z'}\,dz' = I_0(1 - e^{-\mu_a z})$; asserted in `check_sec14_16.py`.

## Transparent Glazings, Vapor Barriers & 9 oz Party Cup Polymer Physics

### [2027 OFFICIAL RULE / CLARIFICATION: Official Clarification #5 (10/21/2026) & ES Guide: Non-Attached Removable Glazing Cap]

**Clarification #5 (`10/21/2026`, Sec. 5 / Par. d / Line 2):** *“When putting the cup in the Device, teams may place something on or around the cup. No adhesives, tapes, or fasteners, such as rubber bands or clips, may be applied to or attached to the cup. The structural integrity and shape of the cup may not be altered in the process of placing the cup in the Device.”* Furthermore, per Rule `5.II.g` and the Official ES Guide  **[S02,S05]**, **all such wrap, foil, or covers must be completely removed/separated from the cup** during the 1-minute final measurement window before the ES measures $T_{\mathrm{final}}$.

**Table:** Optical transmittance, thermal capacitance, and softening limits of glazing films and $9 oz$ cup polymers  **[S01,S02,S12]**.

| **Glazing / Polymer** | **$\rho$** | **$c_p$** | **$k$** | **$C_{\mathrm{disk}}$^a** | **$\tau_{\mathrm{NIR}}$** | **$\tau_{\mathrm{MIR}}$** | **$T_g / T_{\mathrm{soft}}$** | **$T_m$** | **2027 Engineering Assessment & Legality** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | $[kg/m^3]$ | $[J/kg/K]$ | $[W/m/K]$ | $[J/K]$ | $0.4–2.5 µm$ | $5–15 µm$ | $[°C]$ | $[°C]$ |  |
| **Clear BoPET Film** (Mylar, $\delta=25 µm$) | $1390$ | $1170$ | $0.18$ | $\mathbf{0.244}$ | $\mathbf{0.90}$ | $\mathbf{0.22}$ | $75 / \mathbf{150}$ | $\mathbf{254}$ | **TOP RECOMMENDATION:** Zero sag at $150 °C$, blocks $78\%$ MIR, lifts off cup in $<0.5 s$ with zero cling **[S02]**. |
| **Clear BoPET Sheet** (Transparency, $75 µm$) | $1390$ | $1170$ | $0.18$ | $0.732$ | $0.89$ | $\mathbf{0.14}$ | $75 / \mathbf{150}$ | $254$ | **LEGAL.** Rigid flat gravity cap resting on cup rim or attached to upper reflector hood (Clarif. #5, #7). |
| **LDPE Cling Wrap** (Household, $\delta=12.5 µm$) | $920$ | $2100$ | $0.33$ | $\mathbf{0.145}$ | $\mathbf{0.92}$ | $0.76$ | $\mathbf{85\text{--}95}$ | $110$ | **LEGAL (Clarif. #5).** Cuts evaporation $99\%$, but softens at $85 °C$ and clings unless mounted on a drop-ring **[S12]**. |
| **PVDC Clear Wrap** (Saran formula, $13 µm$) | $1650$ | $1340$ | $0.13$ | $0.172$ | $0.90$ | $0.50$ | $135\text{--}145$ | $165$ | **LEGAL.** Stronger $\mathrm{C-Cl}$ mid-IR blocking and higher softening point than LDPE cling wrap. |
| **Polycarbonate Sheet** (Lexan, $\delta=0.75 mm$) | $1200$ | $1250$ | $0.29$ | $6.75$ | $0.86$ | $\mathbf{<0.05}$ | $147 / 120$ | $260$ | **LEGAL.** Rigid greenhouse window; blocks $>95\%$ of mid-IR re-radiation **[S12]**. |
| **Clear Acrylic Sheet** (`#7` PMMA, $\delta=1.5 mm$) | $1180$ | $1460$ | $0.17$ | $15.51$ | $0.85$ | $<0.05$ | $105 / 85$ | $160$ | **LEGAL (`#7` PMMA).** Rigid window; verify non-styrene `#7` stamp before impound **[S12]**. |
| **Borosilicate Glass** (Pyrex plate, $\delta=2.0 mm$) | $2210$ | $753$ | $1.30$ | $19.97$ | $\mathbf{0.91}$ | $\mathbf{<0.02}$ | $500+$ | $820$ | **LEGAL.** Classic selective window ($\tau>0.90$ for $\lambda<2.7 µm$, opaque $> 3.5 µm$); mount on frame **[S12]**. |
| **ES 9 oz Clear Cup: `#1 PET`** ($\delta\approx0.30 mm$, $m\approx6.5 g$) | $1385$ | $1170$ | $0.19$ | $7.61$^b | $0.88$ | $0.25$ | $\mathbf{72\text{--}78}$ | $254$ | **ES-PROVIDED CUP (Rule `4.g`).** Dry upper rim warps if heated above $T_g\approx74 °C$! Keep focus at waterline. |
| **ES 9 oz Clear Cup: `#5 PP`** ($\delta\approx0.32 mm$, $m\approx6.0 g$) | $905$ | $1900$ | $0.185$ | $11.40$^b | $0.88$ | $0.55$ | $125$ | $162$ | **ES-PROVIDED CUP (Rule `4.g`).** Higher softening resistance ($T_{\mathrm{soft}}\approx125 °C$); translucent to NIR. |
| ^a$C_{\mathrm{disk}} = \rho c_p A_{\mathrm{disk}}\delta$ evaluated for a $A_{\mathrm{disk}} = 60.0 cm^2$ ($D=8.74 cm$) cup-mouth cover. ^bFull cup heat capacity (wetted lower $40\%$ couples only $3.0–4.6 J/K$). |  |  |  |  |  |  |  |  |  |

### [TRAP & DIAGNOSTIC: The Clear PET Party Cup Dry-Rim Softening & Warping Trap ($T_g \approx 74 °C$)]

**Symptom:** After a $10 min$ run under a $125 W$ lamp at $h = 40 cm$, the top plastic rim of the ES-provided $9 oz$ cup visibly ovals or curls inward, triggering a Clarification #5 violation (*“structural integrity and shape of the cup may not be altered”*).
**Physical Cause:** Most clear $9 oz$ disposable party cups (e.g., Solo/Dart Clear) are thermoformed from **amorphous Polyethylene Terephthalate (`#1 PET`)**, whose glass-transition temperature is only $T_g \approx 72–78 °C$. Because $100 mL$ ($\approx 3.38 fl\,oz$) of water fills only the **bottom $3.6–4.0 cm$** of the $10.0 cm$ tall cup, the upper $6.0 cm$ of the plastic wall is **dry and air-backed**. Water-backed lower plastic cannot exceed $T_w \le 60 °C$, but dry upper PET exposed to concentrated focal rays rapidly exceeds $80 °C$ and relaxes its thermoforming stresses!
**Engineering Fix:** (1) Place the lower focal throat of the concentrating cone at the **water surface elevation** ($z_{\mathrm{focus}} = z_{\mathrm{base}} + 3.8 cm$), or (2) let an upper specular aluminum-foil aperture lip overhang the dry cup rim by $3 mm$ (explicitly legal under Rule `3.e` so long as nothing touches the water!) to shade the dry plastic lip while directing all rays into the water.

### Worked Example — Fresnel Transmittance, Greenhouse Trapping & Thermal Mass of BoPET vs. Glass Glazing `[Rule 5.c.iii / §14.4]`

A $60.0 cm^2$ transparent glazing cover is placed above the $9 oz$ cup mouth. Compare a $\delta_1 = 25.0 µm$ Clear BoPET film ($n_1 = 1.64$ in NIR, bulk NIR attenuation $\mu_{a,1} = 8.0 /cm$, $\tau_{\mathrm{MIR},1} = 0.22$) against a $\delta_2 = 2.00 mm$ Borosilicate Glass plate ($n_2 = 1.47$ in NIR, $\mu_{a,2} = 0.080 /cm$, $\tau_{\mathrm{MIR},2} = 0.015$). Compute for each: (a) normal-incidence single-surface Fresnel reflectance $R_s = [(n-1)/(n+1)]^2$ and two-surface NIR transmittance $\tau_{\mathrm{NIR}} = \frac{(1-R_s)^2 e^{-\mu_a\delta}}{1 - R_s^2 e^{-2\mu_a\delta}}$, (b) parasitic thermal capacitance $C_{\mathrm{disk}} = \rho c_p A\delta$, and (c) temperature penalty on the top water layer ($C_{\mathrm{top}} = 215.0 J/K$) if the glazing absorbs $\Delta T_g = 18.0 K$ from the cup headspace.

**Solution.** Using the exact multiple-reflection slab transmittance formula and data from Table `tab:14:glazings`:
- **Clear BoPET Film ($\delta_1 = 0.0025 cm, n_1 = 1.64$):** $R_{s,1} = (0.64/2.64)^2 = 0.05877$. Internal transmittance: $\tau_{i,1} = e^{-(8.0)(0.0025)} = 0.98020$. Total NIR transmittance: $\tau_{\mathrm{NIR},1} = \frac{(1-0.05877)^2(0.98020)}{1 - 0.05877^2(0.98020)^2} = \mathbf{0.8714}$ ($87.1\%$). Disk heat capacity: $C_{\mathrm{disk},1} = (1390)(1170)(6.00×10^{-3} m^2)(2.50×10^{-5} m) = \mathbf{0.2439 J/K}$. Headspace thermal drain: $\Delta T_{\mathrm{loss},1} = \frac{C_{\mathrm{disk},1}\Delta T_g}{C_{\mathrm{top}}} = \frac{0.2439(18.0)}{215.0} = \mathbf{0.020 °C}$ (completely negligible!).
- **Borosilicate Glass ($\delta_2 = 0.200 cm, n_2 = 1.47$):** $R_{s,2} = (0.47/2.47)^2 = 0.03621$. Internal transmittance: $\tau_{i,2} = e^{-(0.080)(0.200)} = 0.98413$. Total NIR transmittance: $\tau_{\mathrm{NIR},2} = \frac{(1-0.03621)^2(0.98413)}{1 - 0.03621^2(0.98413)^2} = \mathbf{0.9153}$ ($91.5\%$). Disk heat capacity: $C_{\mathrm{disk},2} = (2210)(753)(6.00×10^{-3} m^2)(2.00×10^{-3} m) = \mathbf{19.970 J/K}$ ($81.9\times$ heavier thermal mass!). If thermally coupled to the cup rim, glass drains $\Delta T_{\mathrm{loss},2} = \frac{19.970(18.0)}{215.0} = \mathbf{1.672 °C}$ from the top layer!

**✓ Verified by:** Airy slab summation $\tau = T_1 T_2 \tau_i \sum_{m=0}^\infty (R_s\tau_i)^{2m}$ and calorimetric energy balance; asserted in `check_sec14_16.py`.

## Rule-Compliant Insulators & Multi-Layer Foil-Air-Foil Baffles

In a transient $10–15 min$ heating run, an ideal insulator around and beneath the $9 oz$ cup must possess **both** low thermal conductivity $k$ $[W/m/K]$ (high steady-state resistance $R_{\mathrm{th}}$) **and** low volumetric heat capacity $\rho c_p$ $[kJ/m^3/K]$ (so the cradle itself does not soak up joules during warm-up). Table `tab:14:insulators` and Fig. `fig:14:insulator-k-chart` demonstrate why **$10–12 mm$ stagnant air gaps bounded by low-emissivity aluminum foil** outperform every solid foam—including banned Styrofoam—in both $k_{\mathrm{eff}}$ and $\rho c_p$  **[S12]**.

**Table:** Thermophysical and safety properties of Rule `3.b`-compliant insulators and structural framing materials  **[S01,S02,S12,S24]**.

| **Compliant Material** | **$\rho$** | **$c_p$** | **$\rho c_p$** | **$k$** | **$\alpha$** | **$\varepsilon_{\mathrm{MIR}}$** | **$T_{\max}$** | **Char / Ign.** | **2027 Engineering Role & Source** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | $[kg/m^3]$ | $[J/kg/K]$ | $[kJ/m^3/K]$ | $[W/m/K]$ | $[\times 10^{-7}m^2/s]$ | $[-]$ | $[°C]$ | $[°C]$ |  |
| **Stagnant Air + Al Foil Gap** ($\delta=10–12 mm$) | $\mathbf{1.18}$ | $1007$ | $\mathbf{1.18}$ | $\mathbf{0.0275}$^a | $221.3$ | $\mathbf{0.04}$ | $500+$ | Non-comb. | **BEST-IN-CLASS:** $\mathrm{Ra}_\delta < 1708$ (zero convection) + foil cuts $h_{\mathrm{rad}}$ $41.7\times$; near-zero mass **[S12]**! |
| **Closed-Cell PE Foam** (`#2/`#4` PE`, NOT `#6 PS`!) | $35$ | $2150$ | $75.3$ | $\mathbf{0.038}$ | $5.05$ | $0.90$ | $80$ | Soft. $85$ / Melt $115$ | **LEGAL (`#2/#4` Polyolefin).** Shield behind foil so $T<80 °C$; carry PE spec sheet at impound **[S12]**. |
| **Cotton / Denim Batting** (Cellulose fiber) | $45$ | $1340$ | $60.3$ | $\mathbf{0.039}$ | $6.47$ | $0.90$ | $120$ | Ign. $210$ ($400$ borate) | **LEGAL** natural plant fiber (distinct from banned fiberglass/mineral wool). Keep dry behind foil. |
| **Corkboard** (Medium density natural sheet) | $170$ | $1850$ | $314.5$ | $\mathbf{0.040}$ | $1.27$ | $0.88$ | $115$ | Char $200$ / Ign. $250$ | **LEGAL.** High compressive strength for 3-point knife-edge cup pedestal ($A_c < 0.25 cm^2$) **[S12]**. |
| **Balsa Wood** (Perpendicular to grain) | $\mathbf{100}$ | $1600$ | $160.0$ | $\mathbf{0.050}$ | $3.13$ | $0.85$ | $120$ | Char $190$ / Ign. $230$ | **LEGAL.** Ultra-light structural ribs, concentrator rings, and cup centering fins **[S12]**. |
| **Sheep Wool Batting / Felt** (Keratin fiber) | $145$ | $1500$ | $217.5$ | $0.050$ | $2.30$ | $0.88$ | $130$ | Self-ext. / Ign. $\mathbf{580}$ | **LEGAL** natural animal wool; highest fire-safety margin. Label clearly in binder for ES inspection **[S12]**. |
| **Dry Sawdust** (Loose cellulosic fill) | $128$ | $1400$ | $179.2$ | $0.050$ | $2.79$ | $0.88$ | $115$ | Char $190$ / Ign. $220$ | **LEGAL.** Traditional loose cavity fill; enclosed foil-air baffles are cleaner and lighter **[S12]**. |
| **Corrugated Cardboard** (Fluted air-core board) | $180$ | $1340$ | $241.2$ | $\mathbf{0.055}$ | $2.28$ | $0.92$ | $120$ | Brown $180$ / Ign. $\mathbf{232}$ | **LEGAL.** Primary structural shell and baffle spacer; face lamp-exposed walls with Al foil **[S12]**. |
| **Silicone Foam / Sheet** (Closed-cell elastomer) | $300$ | $1400$ | $420.0$ | $0.060$ | $1.43$ | $0.90$ | $\mathbf{220}$ | Decomp. $>300$ | **LEGAL.** High-temp soft centering bumpers and upper thermal seal gaskets around cup **[S12]**. |
| **Douglas Fir Plywood** (Structural base plate) | $550$ | $1200$ | $660.0$ | $0.120$ | $1.82$ | $0.85$ | $120$ | Char $200$ / Ign. $260$ | **LEGAL.** Rigid outer floor/frame; isolate from cup by foil-air gaps due to high $\rho c_p$ **[S12]**. |
| **Solid Paperboard / Oak** (Dense wood/card) | $790$ | $1340$ | $1059$ | $0.140$ | $1.32$ | $0.92$ | $120$ | Char $190$ / Ign. $240$ | **LEGAL.** Use thin cardstock ($\le0.4 mm$) as conical formers backed by stagnant air **[S12]**. |
| ^a$k_{\mathrm{eff}} = k_{\mathrm{air}} + h_{\mathrm{rad}}\delta = 0.02623 W/m/K + (0.125 W/m^2/K)(0.010 m) = 0.02748 W/m/K$ at $T_m = 305 K$ with $\varepsilon = 0.04$ foil walls. |  |  |  |  |  |  |  |  |  |

> **[Vector Figure: Thermal conductivity $k$ versus volumetric heat capacity $\rho c_p$ of Rule `3.b`-compliant insulators versus prohibited `#6 PS` and mineral/glass fibers  **[S01,S02,S12]**. | Label: `fig:14:insulator-k-chart`]**
> - **Diagram Annotations & Key Elements:** **X-Axis:** Volumetric Heat Capacity $\rho c_p$ $[kJ/m^3/K]$ • **Y-Axis:** Thermal Conductivity $k$ $[W/m/K]$ • Optimal Low-$k$, Low-Mass Zone • BANNED (`#6 PS`, Fiberglass) • $10 mm$ Foil-Air Gap ($k_{\mathrm{eff}}\!=\!0.0275$) • Cotton / `#4` PE Foam • Corkboard ($0.040$) • Balsa ($0.050$) • Sheep Wool • Fluted Cardboard • Plywood • Solid Card

### Worked Example — 3-Layer Foil-Air-Foil Wall vs. Corkboard `[Rule 5.c.iii / §14.5]`

A cylindrical insulation sleeve of total thickness $L_{\mathrm{tot}} = 30.0 mm$ and mean area $A_m = 0.0450 m^2$ separates the cup cavity at $T_1 = 46.0 °C$ from the outer casing at $T_2 = 25.0 °C$ ($\Delta T_{\mathrm{tot}} = 21.0 K$, $T_m = 308.65 K$). Compare (a) three $\delta = 10.0 mm$ stagnant air gaps separated by four $16 µm$ aluminum foil sheets ($\varepsilon = 0.04$, $k_{\mathrm{air}} = 0.0265 W/m/K$, $\nu\alpha = 3.69×10^{-10} m^4/s^2$, $\beta = 1/T_m$) against (b) $30.0 mm$ of solid corkboard ($k_{\mathrm{cork}} = 0.040 W/m/K$, $\rho c_p = 314.5 kJ/m^3/K$). Verify $\mathrm{Ra}_\delta < 1708$ and compute conductive+radiative heat leak $\dot{Q}$ and sleeve heat capacity $C_{\mathrm{sleeve}}$.

**Solution.**
(a) Across each $\delta = 10.0 mm$ air gap, $\Delta T_{\mathrm{gap}} = 21.0 K/3 = 7.00 K$. The Rayleigh number is:

$$
\mathrm{Ra}_\delta = \frac{g\beta\Delta T_{\mathrm{gap}}\delta^3}{\nu\alpha} = \frac{9.807(7.00/308.65)(0.01)^3}{3.69×10^{-10}} = \mathbf{602.7} < 1708
$$

so the air is $100\%$ stagnant ($\mathrm{Nu}_\delta = 1$). Across each foil-bounded gap, $h_{\mathrm{rad}} = \frac{4\sigma T_m^3}{2/\varepsilon - 1} = \frac{4(5.6704\times 10^{-8})(308.65)^3}{49} = 0.1360 W/m^2/K$, giving $k_{\mathrm{eff}} = k_{\mathrm{air}} + h_{\mathrm{rad}}\delta = 0.0265 + 0.00136 = \mathbf{0.02786 W/m/K}$. Thus $\dot{Q}_{\mathrm{foil-air}} = \frac{k_{\mathrm{eff}}A_m\Delta T_{\mathrm{tot}}}{L_{\mathrm{tot}}} = \frac{(0.02786)(0.0450)(21.0)}{0.030} = \mathbf{0.878 W}$, and total sleeve heat capacity (4 foil layers + air) is $C_{\mathrm{sleeve}} = 4(39.2)(0.0450) + (1180)(0.0450\times 0.030) = \mathbf{8.65 J/K}$.

(b) For solid corkboard: $\dot{Q}_{\mathrm{cork}} = \frac{(0.040)(0.0450)(21.0)}{0.030} = \mathbf{1.260 W}$ ($43.5\%$ higher heat leak), and $C_{\mathrm{cork}} = (314500 J/m^3/K)(0.0450\times 0.030) = \mathbf{424.6 J/K}$ ($49.1\times$ higher parasitic thermal mass!).

**✓ Verified by:** Series thermal resistance $R_{\mathrm{th}} = 3\delta/(k_{\mathrm{eff}}A_m) = 23.93 K/W$ vs. $R_{\mathrm{cork}} = 16.67 K/W$; asserted in `check_sec14_16.py`.

## Explicit Prohibited Materials Hazard Registry & Classroom/Tournament Safety Rules

### [2027 OFFICIAL RULE / CLARIFICATION: HARD SAFETY BAN: Polystyrene / Styrofoam / `#6 PS` Disqualification (Rule 3.b.i–iii & Official Clarification #6)]

- **Rule `3.b.i` (Hazardous Materials Prohibition):** Devices may be built from and contain anything **except**: *“Hazardous materials, including but not limited to asbestos, mineral wool, and fiberglass.”*  **[S01]**
- **Official National Clarification #6 (`10/22/2026`, Sec. 3 / Par. b / Sub-par. i, Line 1):** *“**Q:** Is polystyrene considered a safe material and allowed to be used in this event? **A:** **No. Polystyrene (which includes styrofoam and plastics with the recyclable symbol `6' and `PS' on them) is considered hazardous in high heat situations and should not be used in this event.**”*  **[S02]**
- **Mandatory Zero-Score Exclusion (Rule `3.b.iii`):** *“If a team uses hazardous materials (3.b.i.), **the device will not be allowed to be set up, modified, or tested**. Such teams will only be allowed to compete in Part I.”*  **[S01]** Unlike minor dimensional or non-hazardous construction violations (which can be fixed during the 3-minute Device Setup Time under Rule `5.II.b`), a Rule `3.b.i` hazardous material violation **cannot be cut out or modified at the tournament** because handling or heating hazardous materials in the testing room is prohibited—resulting in an automatic, unappealable $\mathbf{\mathrm{TS} = 0}$ and $\mathbf{\mathrm{PS} = 0}$ ($50.0\text{ points lost}$)!

**Table:** Complete 2027 prohibited materials, restricted components, and mandatory tournament penalties  **[S01,S02,S04,S05]**.

| **Prohibited Material / Item** | **Rule Authority** | **Exact Scope of Prohibition** | **Tournament Penalty** | **Approved Legal Replacement** |
| --- | --- | --- | --- | --- |
| **Polystyrene — ALL Forms** (Styrofoam, EPS bead foam, XPS blue/pink/green board, PS foam-core posterboard, rigid `#6 PS`) | `3.b.i`, `3.b.iii`, Clarif. #6 (`10/22/26`), ES Guide | All expanded, extruded, or rigid polystyrene polymers ($T_g\approx95–100 °C$; softens, outgasses styrene monomer, and melts under focused heat lamp). | **Barred from setup, modification, or testing ($\mathrm{TS}=0, \mathrm{PS}=0$)!** | Corrugated cardboard + multi-layer $10 mm$ Al-foil air gaps ($k_{\mathrm{eff}}=0.0275 W/m/K$), corkboard, balsa, cotton/wool. |
| **Fiberglass** (Glass-fiber batt, pipe wrap, loose glass wool, shedding fiberglass cloth/tape) | `3.b.i`, `3.b.iii`, Checklist Box 1 | All glass-fiber insulation or shedding glass textiles (skin, eye, and respiratory hazard). | **Barred from setup, modification, or testing ($\mathrm{TS}=0, \mathrm{PS}=0$)!** | Cotton/denim cellulose batting, sheep wool felt, corkboard, or foil-air baffles. |
| **Mineral Wool** (Rock wool, slag wool, ceramic refractory fiber wool) | `3.b.i`, `3.b.iii`, Checklist Box 1 | All mineral/rock/slag fibrous insulation (listed in textbook tables for written exam math only!). | **Barred from setup, modification, or testing ($\mathrm{TS}=0, \mathrm{PS}=0$)!** | Natural sheep wool felt (keratin protein, self-extinguishing at $580 °C$) or cotton batting. |
| **Asbestos** (Board, paper, loose fiber, or cloth) | `3.b.i`, `3.b.iii`, Checklist Box 1 | All asbestos-containing materials (regulated carcinogen). | **Barred from setup, modification, or testing ($\mathrm{TS}=0, \mathrm{PS}=0$)!** | Silicone elastomer sheet, corkboard, or borosilicate glass plate. |
| **Commercial Thermoses, Coolers, or Vacuum Vessels** | `3.b.ii`, `6.g`, Checklist Box 5 | Prefabricated Dewars, stainless vacuum tumblers (Yeti/Stanley/HydroFlask), commercial insulated coolers. | Construction violation ($\times 0.7$ to $\mathrm{TS},\mathrm{PS}$ if unfixed in 3-min Setup Time). | Scratch-built student-fabricated multi-wall foil-air-cardboard-cork cradle (`3.h`). |
| **Thermometers or Temperature Probes in Device/Spares** | `3.b.ii`, `4.f`, `6.g`, Checklist Box 5 | Digital probes, thermocouples, thermistors, RTDs, IR sensors, or stick-on LCD strips impounded or used on day of event. | Construction / Competition violation ($\times 0.7$ or $\times 0.9$ penalty). | Use team probes during pre-tournament lab calibration only; remove all sensors before impound! |
| **Electrical, Battery, or Chemical Energy Sources** | `3.f`, `6.e.iii`, `6.f.iii`, Checklist Box 2 | Batteries, heaters, Peltier modules, exothermic salts ($\mathrm{CaO}$, hand warmers, phase-change packs), pre-heated masses (`3.g`). | **Severe violation: $\mathrm{TS}=0$ and $\mathrm{PS}=0$** (post-test disassembly check per `3.f`). | Passive optical concentration of ES heat lamp only; impound ventilated at room temperature (`2.d`). |
| **Water-Contacting Parts or Water Additives** | `3.e`, `6.g`, Checklist Box 5 | Submerged metal fins/plates, dark dyes/ink, floating oil films, or overhanging cones dipping into water. | Construction violation ($\times 0.7$ multiplier to $\mathrm{TS}$ and $\mathrm{PS}$). | Maintain $\ge15 mm$ dry air clearance above the $38 mm$ waterline; rest glazing cap on top $100 mm$ cup rim. |
| **Adhesives, Tapes, Rubber Bands, or Clips on Cup** | `5.II.d`, Clarif. #5 (`10/21/26`), `6.h` | Any glue, tape, elastic band, clip, or fastener attached to the ES $9 oz$ cup, or wrap left on cup during $T_{\mathrm{final}}$ reading (`5.II.g`). | Competition violation ($\times 0.9$ multiplier to $\mathrm{TS}$ and $\mathrm{PS}$). | Gravity-resting clear BoPET cap or upper hood window that lifts off cleanly in $<2 s$. |

**Table:** Polymer Resin Identification Code (`#1`–`#7`) impound audit guide  **[S01,S02,S12]**.

| **Code** | **Polymer Name** | **$T_g / T_{\mathrm{soft}}$** | **$T_m$** | **2027 Status** | **Permitted Collector Use** |
| --- | --- | --- | --- | --- | --- |
|  |  | $[°C]$ | $[°C]$ |  |  |
| **`#1 PET`** | Polyethylene Terephthalate | $75 / 150$^a | $254$ | **LEGAL** | Clear BoPET (Mylar) glazing film & aluminized Mylar; ES $9 oz$ cup. |
| **`#2 HDPE`** | High-Density Polyethylene | $-120 / 115$ | $132$ | **LEGAL** | Lower structural base rings or unheated outer frame spacers. |
| **`#3 PVC`** | Polyvinyl Chloride | $82 / 75$ | $180$ | **AVOID** | Legal, but softens at $75 °C$ and dehydrochlorinates ($\mathrm{HCl}$) $> 140 °C$. |
| **`#4 LDPE`** | Low-Density Polyethylene | $-110 / 88$ | $110$ | **LEGAL** | Clear cling wrap (Clarif. #5) or foil-shielded closed-cell PE foam. |
| **`#5 PP`** | Polypropylene | $-10 / 125$ | $162$ | **LEGAL** | High-temp clear cups, corrugated plastic (*Coroplast*) outer shell. |
| **`#6 PS`** | **Polystyrene (EPS/XPS/PS)** | $95 / 90$ | $240$ | **BANNED!** | **DISQUALIFIED ($\mathrm{TS}=\mathrm{PS}=0$) per Rule `3.b.i` & Clarif. #6!** |
| **`#7 Other`** | Polycarbonate (PC) / PMMA | $147 / 105$ | $260$ | **LEGAL** | Rigid Lexan (PC) or acrylic (PMMA) glazing/mirrors (verify non-PS!). |
| ^aBiaxially oriented BoPET film is stable to $150 °C$. |  |  |  |  |  |

### [2027 HEAT-COLLECTOR DEVICE & LAB: Foam-Core Board Trap & Safety Protocol]

**Craft Foam-Core Posterboard Trap:** Standard craft-store “foam-core board” (e.g., Elmer's / Dollar Tree $5 mm$ paper-faced foam board) has an **extruded polystyrene (`#6 PS`) core**! Using it anywhere in your collector triggers immediate disqualification under Clarification #6. Use **100% cellulose corrugated cardboard** or **`#5 PP` corrugated plastic (*Coroplast*)** instead, and keep a cut cross-section sample + datasheet in your binder for ES verification.

**5 Mandatory Lab & Competition Safety Rules:**
- **Bulb Clearance ($\ge10.0 cm$):** At minimum bulb height $h = 40.0 cm$, a maximum-height $30.0 cm$ device sits $10.0 cm$ below the $220 °C$ bulb glass. Never exceed $29.6 cm$ device height.
- **Foil-Shield All Cellulosics:** Bare cardboard/balsa chars at $180–200 °C$ and ignites at $232 °C$. Facing all lamp-exposed surfaces with shiny Al foil ($\alpha_{\mathrm{NIR}}=0.04$) keeps wall temperatures $< 42 °C$.
- **Burn Protection:** Never touch the ES clamp-lamp metal hood or $\mathrm{R40}$ bulb during setup or cup removal.
- **Spill & Electrical Isolation:** Keep the $100 mL$ cup away from $120 V$ AC power cords and plug junctions.
- **Post-Test Disassembly Readiness (Rule `3.f`):** Use removable dowels or Velcro access panels so the ES can inspect internal insulation layers in $<30 s$ without destructive cutting.

—
**See also:** §`sec:10` (Conduction Networks), §`sec:11` (Air-Gap Convection & Evaporation), §`sec:12` (Thermal Radiation & Shields), §`sec:15` (2027 Collector Engineering), §`sec:16` (Calibration & Prediction), §`app:A` (Property Tables), §`app:E` (Compliance Matrix).
