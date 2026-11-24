<!-- Source: src/sec12.tex | Tab: Tab 5: TRANSFER | Target: 8 pp -->
# §12: Thermal Radiation, Blackbody Laws, View Factors, Radiation Shields & Two-Band Selective Surfaces {#sec:12}

> **[SCOPE: TIER-DEPENDENT | 2027 Rule 5.c.iii (All Levels Core) & Rule 5.c.vi (States/Nationals: Radiant Exitance, Blackbody Radiation, Stefan–Boltzmann Law) | Sources:  **[S01]**,  **[S07]**,  **[S12]**,  **[S19]**,  **[S25]**]**

### [FORMULA & DECISION CARD: §12 Master Blackbody Radiation, View-Factor, Shield & Selective-Surface Decision Card  **[S07,S12,S25]**]

| **Formula** | **Variables (SI units)** | **Flags** | **Use when** |
| --- | --- | --- | --- |
| $\alpha + \rho + \tau = 1, \quad \alpha_\lambda + \rho_\lambda + \tau_\lambda = 1$ | $\alpha$: absorptance; $\rho$: reflectance; $\tau$: transmittance (all $\in [0, 1]$); for an **opaque** surface ($\tau=0$): $\alpha + \rho = 1$ | **[OPTICAL]** | Energy conservation for incident irradiance $G$ $(W/m^2)$ at any surface |
| $M_{\lambda,b}(\lambda, T) = \dfrac{c_1}{\lambda^5 \left[\exp\!\left(\dfrac{c_2}{\lambda T}\right) - 1\right]}$ | $M_{\lambda,b}$ (or $e_{b\lambda}$): spectral blackbody exitance $(W/m^2/µm)$; $c_1 = 2\pi h c_0^2 = 3.74177×10^{8} W µm^4/m^2$; $c_2 = \dfrac{h c_0}{k_B} = 14387.77 µm K$ | **[STATE/NAT]** | Planck distribution (1900); $T$ MUST be in $K$, $\lambda$ in $µm$ |
| $\lambda_{\max} T = b_{\mathrm{Wien}} = 2897.772 µm K$ | $\lambda_{\max}$: peak wavelength of $M_{\lambda,b}$ $(µm)$; $b_{\mathrm{Wien}} = c_2 / 4.965114$ $(µm K)$ [frequency peak: $\nu_{\max}/T = 5.8789×10^{10} Hz/K$] | **[STATE/NAT]** | Sun ($5778 K$): $0.502 µm$; 125 W Lamp ($2400 K$): $1.207 µm$; Water ($300 K$): $9.66 µm$ |
| $M_b(T) = \sigma T^4, \quad M(T) = \varepsilon \sigma T^4$ | $M$ (or $e$): hemispherical radiant exitance $(W/m^2)$; $\sigma = \dfrac{2\pi^5 k_B^4}{15 c_0^2 h^3} = 5.670374×10^{-8} W/m^2/K^4$; $\varepsilon \in [0, 1]$: total emittance | **[STATE/NAT]** | Stefan–Boltzmann law ($\dot{Q}_{\mathrm{emit}} = \varepsilon\sigma A T^4$); $T$ MUST be in absolute $K$! |
| $L = I = \dfrac{M}{\pi} = \dfrac{\varepsilon \sigma T^4}{\pi}$ | $L$ (or $I$): directional radiance / intensity $(W/m^2/sr)$ of a diffuse (Lambertian) emitter; factor is $\pi$ (NOT $2\pi$!) | **[STATE/NAT]** | 2027 Cornell Invitational **[S25]** & Lienhard Eq. (10.7b) p. 551 **[S12]** |
| $\varepsilon_\lambda(T,\theta,\phi) = \alpha_\lambda(T,\theta,\phi)$ | Exact Kirchhoff's law: holds at identical wavelength $\lambda$; total $\alpha_{\mathrm{lamp}} \ne \varepsilon_{\mathrm{MIR}}$ when $T_{\mathrm{lamp}} \approx 2400 K \gg T_{\mathrm{surf}} \approx 310 K$! | **[SELECTIVE]** | Two-band selective absorbers ($\alpha_{\mathrm{NIR}}/\varepsilon_{\mathrm{MIR}} \gg 1$) & greenhouse glazings |
| $\sum_{j=1}^N F_{i\to j} = 1, \quad A_i F_{i\to j} = A_j F_{j\to i}$ | $F_{i\to j}$: geometric view factor (fraction of diffuse radiation leaving $i$ that strikes $j$ directly); convex/flat surface has $F_{i\to i} = 0$ | **[GEOMETRY]** | Enclosure view-factor algebra & coaxial lamp-to-aperture interception |
| $\dot{Q}_{1\to 2} = A_1 \mathcal{F}_{1\to 2}\,\sigma\left(T_1^4 - T_2^4\right)$ | $\mathcal{F}_{1\to 2} = \varepsilon_1$ (small body $A_1 \ll A_2$); $\mathcal{F}_{1\to 2} = \left[\dfrac{1}{\varepsilon_1} + \dfrac{A_1}{A_2}\!\left(\dfrac{1}{\varepsilon_2}-1\right)\right]^{-1}$ (enclosed body, $F_{12}=1$) | **[GRAY-SURF]** | Two-body diffuse-gray exchange (Lienhard Eqs. 10.25–10.30 **[S12]**) |
| $\dot{Q}_{N\text{ shields}} = \dfrac{\sigma A\left(T_1^4 - T_2^4\right)}{(N+1)\left(\dfrac{2}{\varepsilon} - 1\right)} = \dfrac{\dot{Q}_0}{N+1}$ | $N$: number of parallel radiation shields between plates when all surfaces have emittance $\varepsilon$; for unequal $\varepsilon_k$, resistances add in series | **[SHIELDS]** | Multi-layer aluminum-foil insulation ($\varepsilon=0.04$ cuts $\dot{Q}_{\mathrm{rad}}$ by $41.7(N+1)\times$!) |
| $h_{\mathrm{rad}} = 4\sigma T_m^3 \mathcal{F}_{1\to 2}, \quad R_{\mathrm{rad}} = \dfrac{1}{h_{\mathrm{rad}}A_1}$ | $T_m = \frac{1}{2}(T_1 + T_2)$ $(K)$; valid within $<1\%$ when $\frac{1}{4}(\Delta T/T_m)^2 \ll 1$; at $T_m=300 K$, $4\sigma T_m^3 = 6.12 W/m^2/K$ | **[LINEARIZED]** | Parallel convection + radiation networks ($h_{\mathrm{eff}} = h_{\mathrm{conv}} + h_{\mathrm{rad}}$) |

## Blackbody Radiation, Spectral Separation & Two-Band Selectivity

### [TIER: STATE & NATIONALS (Rule 5.c.vi–vii): 2027 Rule `5.c.iii` (All Levels) vs. Rule `5.c.vi` (States & Nationals Only)  **[S01]**]

Qualitative radiation mechanisms, shiny low-emissivity barriers, and 2027 heat-lamp collection appear at **all competition levels** under Rule `5.c.iii` and Part II device testing. Quantitative calculations of **radiant exitance ($M$), Planck/Wien blackbody spectra, and the Stefan–Boltzmann law ($M = \varepsilon\sigma T^4$)** are explicitly listed under Rule `5.c.vi` (*State and National levels only*, though frequent at major invitationals such as the 2026–2027 Cornell Invitational  **[S25]**).

### Planck Distribution, Wien's Displacement Law, and Lambertian Radiance

Every body above $0 K$ continuously emits electromagnetic thermal radiation (0.1–1000 µm, Lienhard Table 1.2 p. 28  **[S12]**). An ideal **blackbody** (realized experimentally by a small aperture in an isothermal cavity or *hohlraum*, where multiple internal reflections trap all incident rays) absorbs $100\%$ of incident radiation at all wavelengths and directions ($\alpha_\lambda = 1,\; \rho_\lambda = \tau_\lambda = 0$) and emits the maximum possible spectral flux allowed by thermodynamic equilibrium:
- **Wien's Displacement Law (1893) and the Wavelength–Frequency Peak Trap:** Differentiating Planck's distribution $M_{\lambda,b}(\lambda,T)$ with respect to $\lambda$ yields the transcendental equation $(5 - x)e^x = 5$ where $x = h c_0 / (\lambda_{\max} k_B T) = 4.96511423$, giving $\lambda_{\max} T = b_{\mathrm{Wien}} = 2897.772 µm K$  **[S07,S12]**. As plotted in Fig. `fig:12:planck-spectra`, this creates a crisp **three-spectrum wavelength separation** critical to the 2027 collector:
- **Solar Spectrum ($T_\odot \approx 5772 K$–$5778 K$):** $\lambda_{\max} = \frac{2897.8}{5778} = 0.5015 µm$ ($502 nm$, visible green-yellow; $\sim 98\%$ of solar energy lies at $\lambda < 2.7 µm$).
- **2027 Incandescent 100–125 W Heat-Lamp Tungsten Filament ($T_{\mathrm{fil}} \approx 2400 K$):** $\lambda_{\max} = \frac{2897.8}{2400} = \mathbf{1.2074 µm}$ (**near-infrared**; for $T_{\mathrm{fil}} \in [2200 K, 2500 K]$, $\lambda_{\max} \in [1.159 µm, 1.317 µm]$). Exactly $25.0\%$ of total blackbody emission always lies at $\lambda < \lambda_{\max}$, and $75.0\%$ lies at $\lambda > \lambda_{\max}$.
- **Room-Temperature Water & Collector Walls ($T_w \approx 300 K$–$318 K$):** $\lambda_{\max} = \frac{2897.8}{300} = \mathbf{9.659 µm}$ ($9.11 µm$ at $45 °C$, **mid/thermal infrared**, spanning $4–40 µm$).
  

  *Caution on Frequency Peak $\nu_{\max}$:* Because $M_\nu = M_\lambda |d\lambda/d\nu| = (\lambda^2/c_0)M_\lambda$, the peak of Planck's distribution per unit frequency $M_{\nu,b}(\nu,T)$ occurs at $x_\nu = h\nu_{\max}/(k_B T) = 2.821439$, so $\nu_{\max}/T = 5.8789×10^{10} Hz/K$ and $\lambda_{\max}\nu_{\max} = \frac{2.8214}{4.9651}c_0 = 0.56825\,c_0 \ne c_0$!
- **Lambert's Cosine Law and Directional Radiance ($L = M/\pi$):** A blackbody or ideal diffuse surface emits with uniform **directional radiance** (intensity) $L = I$ $[W/m^2/sr]$ in all directions $(\theta, \phi)$, so the heat flux emitted per unit solid angle $d\Omega = \sin\theta\,d\theta\,d\phi$ at polar angle $\theta$ from the surface normal is $dM = L \cos\theta\,d\Omega$ (because the projected area seen from angle $\theta$ is $dA\cos\theta$). Integrating over the upper hemisphere ($\phi \in [0, 2\pi],\; \theta \in [0, \pi/2]$) gives $\int_0^{2\pi}d\phi \int_0^{\pi/2}\cos\theta\sin\theta\,d\theta = 2\pi\left(\frac{1}{2}\right) = \pi\ sr$ (Lienhard Eq. 10.7b, p. 551  **[S12]**):
  
$$
\begin{aligned}
M(T) = \pi L(T) = \varepsilon \sigma T^4 \implies L(T) = \frac{\varepsilon \sigma T^4}{\pi} \quad \left[W/m^2/sr\right]
    
\end{aligned}
$$

> **[Vector Figure: Planck blackbody spectral exitance $M_{\lambda,b}(\lambda,T)$ for the Sun ($5778 K$), the 2027 125 W tungsten heat lamp ($2400 K$, peaking at $\lambda_{\max} = 1.207 µm$ in the near-IR), and room-temperature water ($300 K$, peaking at $9.66 µm$ in the mid-IR), overlaid with the $2.7 µm$ selective transmission cutoff of glass and BoPET glazing (Lienhard §10.1 & §10.6  **[S12]**). | Label: `fig:12:planck-spectra`]**
> - **Diagram Annotations & Key Elements:** **X-Axis:** Wavelength $\lambda$ $(µm)$ — Showing Short-Wave Lamp Band ($\lambda < 2.7 µm$) vs. Long-Wave Thermal IR Band ($\lambda > 4 µm$) • **Y-Axis:** Spectral Exitance $M_{\lambda,b}(\lambda,T)$ $(W/m^2/µm)$ • **Legend:** Solar Blackbody ($T=5778 K,\; \lambda_{\max}=0.502 µm$) • **Legend:** 2027 Heat Lamp ($T=2400 K,\; \lambda_{\max}=1.207 µm$) • **Legend:** Cup Water ($T=300 K,\; \lambda_{\max}=9.659 µm$) • **Legend:** Wien Peak Locus ($\lambda_{\max} = 2897.8 µm K/T$) • Glass / BoPET Window / [-1pt]Transmits ($\tau_{\mathrm{NIR}} \approx 0.90$) • Glass / BoPET Opaque / [-1pt]Traps Mid-IR ($\tau_{\mathrm{MIR}} < 0.20$)

### Kirchhoff's Law and Two-Band Wavelength-Selective Surfaces (Lienhard Tables 10.1 & 10.5)

Kirchhoff's law states that at any given wavelength $\lambda$ and direction $(\theta,\phi)$, spectral directional emittance equals spectral directional absorptance: $\varepsilon_\lambda(T,\theta,\phi) = \alpha_\lambda(T,\theta,\phi)$ (Lienhard Eq. 10.8a, p. 551  **[S12]**). However, when an object at $T_{\mathrm{surf}} \approx 310 K$ is irradiated by a high-temperature source at $T_{\mathrm{source}} \approx 2400 K$ (or $5778 K$), the absorbed radiation is governed by the surface's short-wave near-IR absorptance $\alpha_{\mathrm{NIR}} \approx \varepsilon_\lambda(\lambda \approx 1.2 µm)$, whereas its emitted thermal loss is governed by its long-wave mid-IR emittance $\varepsilon_{\mathrm{MIR}} \approx \varepsilon_\lambda(\lambda \approx 9.5 µm)$:

$$
\begin{aligned}
q''_{\mathrm{net,absorbed}} = \alpha_{\mathrm{NIR}}\,G_{\mathrm{lamp}} - \varepsilon_{\mathrm{MIR}}\,\sigma\left(T_{\mathrm{surf}}^4 - T_{\mathrm{amb}}^4\right) - h_{\mathrm{conv}}\left(T_{\mathrm{surf}} - T_{\mathrm{amb}}\right)
  
\end{aligned}
$$

Table `tab:12:selective-emissivity` summarizes verified short-wave absorptances $\alpha_{\mathrm{SW/NIR}}$ and long-wave thermal emittances $\varepsilon_{\mathrm{MIR}}$ from Lienhard Tables 10.1 (p. 546) and 10.5 (p. 598)  **[S12]**:

**Table:** Verified Short-Wave (Solar/Near-IR) Absorptance $\alpha_{\mathrm{SW/NIR}}$, Reflectance $\rho_{\mathrm{SW/NIR}}$, and Long-Wave Mid-IR Emittance $\varepsilon_{\mathrm{MIR}}$ near $300–313 K$ (Lienhard Tables 10.1 p. 546 & 10.5 p. 598  **[S12]**).

| **Surface / Coating (Lienhard Tables 10.1 & 10.5)** | **$\alpha_{\mathrm{SW/NIR}}$** | **$\rho_{\mathrm{SW/NIR}}$** | **$\varepsilon_{\mathrm{MIR}}$** | **$\alpha_{\mathrm{SW}}/\varepsilon_{\mathrm{MIR}}$** | **Radiative Classification & 2027 Role** |
| --- | --- | --- | --- | --- | --- |
| **Black Chrome on Ni plate** (Table 10.5) | $0.95$ | $0.05$ | $0.09$ | $\mathbf{10.56}$ | Selective absorber: absorbs lamp, blocks MIR loss |
| **Sputtered cermet on steel** (Table 10.5) | $0.96$ | $0.04$ | $0.16$ | $\mathbf{6.00}$ | High-efficiency selective solar/NIR absorber |
| **$\mathrm{CuO}$ on copper (Ebanol C)** (Table 10.5) | $0.90$ | $0.10$ | $0.16$ | $\mathbf{5.63}$ | Selective black-oxide copper foil collar |
| **Nickel black on steel** (Table 10.5) | $0.81$ | $0.19$ | $0.17$ | $\mathbf{4.76}$ | Selective metallic absorber |
| **Copper, polished electrolytic** (Tables 10.1, 10.5) | $0.30$ | $0.70$ | $0.02\text{--}0.04$ | $7.50$ | Weak solar absorber, ultra-low MIR emitter |
| **Aluminum foil, bright polished** (Tables 10.1, 10.5) | $0.04\text{--}0.09$ | $0.91\text{--}0.96$ | $0.03\text{--}0.04$ | $1.0\text{--}2.2$ | Broadband mirror: ideal cone & radiation shield |
| **Aluminum sheet, heavily oxidized** (Table 10.1) | $0.25$ | $0.75$ | $0.20\text{--}0.33$ | $\sim 1.0$ | Oxide layer degrades both reflectance & shield $\varepsilon$ |
| **Carbon black in acrylic / Matte black paint** | $0.94$ | $0.06$ | $0.83\text{--}0.95$ | $1.0\text{--}1.13$ | Non-selective blackbody: needs glazing cover |
| **Carbon lampsoot / Candle soot** (Table 10.1) | $0.96$ | $0.04$ | $0.95$ | $1.01$ | Reference broadband blackbody ($\varepsilon = 0.95$) |
| **Liquid water layer (thickness $\ge0.1 mm$, 40 °C)** | $0.78\text{--}0.85^*$ | $0.02$ | $\mathbf{0.96}$ | $0.85$ | Direct NIR volume absorption; black in $8\text{--}14\,µm$! |
| **Smooth glass / Pyrex** (Table 10.1, §10.6 p. 599) | $\tau_{\mathrm{NIR}}=0.91$ | $0.08$ | $\mathbf{0.94}$ | Greenhouse | Transmits $\lambda<2.7 µm$, opaque in mid-IR ($\tau_{\mathrm{MIR}}<0.02$) |
| **White acrylic paint / White paper** (Tables 10.1, 10.5) | $0.26 / 0.22$ | $0.74 / 0.78$ | $\mathbf{0.90 / 0.96}$ | $\mathbf{0.23\text{--}0.29}$ | Selective *radiative cooler*: reflects visible, emits MIR! |
| **Zinc oxide ($\mathrm{ZnO}$) white coating** (Table 10.5) | $0.15$ | $0.85$ | $\mathbf{0.93}$ | $\mathbf{0.16}$ | Stays cooler than air under lamp; never use in cone! |
| $^*$Planck-integrated absorptance of a $35 mm$ deep water column in a 9 oz cup under a $2400 K$ glass-filtered heat lamp (Hale & Querry 1973 **[S19]**). |  |  |  |  |  |

## View-Factor Algebra, Gray-Body Networks & Radiation Shields

### Coaxial-Disk View Factor ($F_{1\to 2}$) for the 2027 Heat Lamp and Collector Aperture

For two coaxial parallel circular disks of radii $r_1$ (heat-lamp reflector face, $r_1 = 6.35 cm$ for a $5.0\ \text{in}$ R40 bulb) and $r_2$ (collector top aperture $r_2 = 15.0 cm$, or bare 9 oz cup mouth $r_{\mathrm{cup}} = 3.75 cm$) separated by vertical distance $d = h_{\mathrm{bulb}} - z_{\mathrm{opening}}$, Lienhard Table 10.3 Case 3 (p. 562  **[S12]**) gives the exact analytical view factor:

$$
\begin{aligned}
R_1 = \frac{r_1}{d}, \qquad R_2 = \frac{r_2}{d}, \qquad X = 1 + \frac{1 + R_2^2}{R_1^2}, \qquad F_{1\to 2} = \frac{1}{2}\!\left[X - \sqrt{X^2 - 4\left(\frac{R_2}{R_1}\right)^{\!2}}\right]
  
\end{aligned}
$$

Furthermore, by the enclosure summation rule (Lienhard Example 10.3, p. 565  **[S12]**), if disk $1$ (base radius $r_1$) and disk $2$ (top radius $r_2$) are connected by an enclosing conical frustum $s$, the fraction of diffuse radiation leaving disk $1$ that strikes the conical wall $s$ is simply $F_{1\to s} = 1 - F_{1\to 2}$.

### Hottel's Crossed-String Algebraic View-Factor Rule & Cavity Effective Absorptance

- **Hottel's 2-D Crossed-String Method (Zero Calculus or Trigonometry Required! Lienhard Table 10.2 Case 4, p. 561  **[S12]**):** For any two infinitely long (2-D) surfaces $A_1$ and $A_2$ (which may be curved, tilted, or partially obstructed), imagine stretching tight strings between their four outer endpoints $(a, b)$ on $A_1$ and $(c, d)$ on $A_2$. The exact view factor $F_{1\to 2}$ equals the sum of the two **crossed** diagonal string lengths minus the sum of the two **uncrossed** side string lengths, divided by $2 A_1$:
  
$$
\begin{aligned}
\boxed{F_{1\to 2} = \frac{\left(L_{\mathrm{crossed},ad} + L_{\mathrm{crossed},bc}\right) - \left(L_{\mathrm{uncrossed},ac} + L_{\mathrm{uncrossed},bd}\right)}{2 A_1}}
    
\end{aligned}
$$

  For two parallel directly opposed strips of equal width $w$ separated by distance $h$ ($L_{\mathrm{crossed}} = \sqrt{w^2 + h^2},\; L_{\mathrm{uncrossed}} = h$), Eq. Eq. (`eq:12:hottel-strings`) immediately yields Lienhard Table 10.2 Case 1: $F_{1\to 2} = \sqrt{1 + (h/w)^2} - (h/w)$.
- **Concentric Cylinders and Concentric Spheres ($r_1 < r_2$, Lienhard Tables 10.2–10.3  **[S12]**):** Because the inner convex surface $1$ cannot see itself ($F_{1\to 1} = 0$), all radiation leaving $1$ strikes $2$ ($F_{1\to 2} = 1$). By reciprocity ($A_1 F_{1\to 2} = A_2 F_{2\to 1}$) and summation on the concave outer surface $2$ ($F_{2\to 1} + F_{2\to 2} = 1$):
  
$$
\begin{aligned}
F_{1\to 2} = 1, \qquad F_{2\to 1} = \frac{A_1}{A_2} = \begin{cases} r_1 / r_2 & \text{(concentric cylinders)} \\ (r_1 / r_2)^2 & \text{(concentric spheres)} \end{cases}, \qquad F_{2\to 2} = 1 - \frac{A_1}{A_2}
    
\end{aligned}
$$
- **Cavity (*Hohlraum*) Effective Absorptance & Emittance Enhancement:** When a cavity of interior surface area $A_{\mathrm{cav}}$ and intrinsic wall absorptance $\alpha_s = \varepsilon_s$ opens to the outside through an aperture of area $A_{\mathrm{ap}} \le A_{\mathrm{cav}}$, any ray entering $A_{\mathrm{ap}}$ undergoes an average of $A_{\mathrm{cav}}/A_{\mathrm{ap}}$ internal bounces before escaping, boosting the effective aperture absorptance $\alpha_{\mathrm{cav}}$ to:
  
$$
\begin{aligned}
\boxed{\alpha_{\mathrm{cav}} = \varepsilon_{\mathrm{cav}} = \frac{\alpha_s}{\alpha_s + \left(1 - \alpha_s\right)\dfrac{A_{\mathrm{ap}}}{A_{\mathrm{cav}}}} \xrightarrow{A_{\mathrm{ap}} \ll A_{\mathrm{cav}}} 1.000 \quad (\text{ideal blackbody cavity})}
    
\end{aligned}
$$

### Oppenheim Radiosity-Space Resistance Network and $N$ Radiation Shields

In a diffuse-gray enclosure, each opaque surface $i$ (area $A_i$, temperature $T_i$, emittance $\varepsilon_i$, reflectance $\rho_i = 1 - \varepsilon_i$) has a surface resistance $R_{\mathrm{surf},i} = \frac{1-\varepsilon_i}{\varepsilon_i A_i}$ connecting its blackbody emissive potential $E_{b,i} = \sigma T_i^4$ to its outgoing **radiosity node** $J_i = \varepsilon_i\sigma T_i^4 + (1-\varepsilon_i)G_i$ (Lienhard §10.4, pp. 569–573  **[S12]**). Two radiosity nodes $J_1$ and $J_2$ are connected by the geometric space resistance $R_{\mathrm{space},12} = \frac{1}{A_1 F_{1\to 2}} = \frac{1}{A_2 F_{2\to 1}}$, as drawn in Fig. `fig:12:shields-viewfactor`(a).
When $N$ thin parallel reflective sheets (shields $s_1, \dots, s_N$, each with emittance $\varepsilon_s$ on both faces and $F=1$) are placed in series between parallel walls $1$ ($\varepsilon_1$) and $2$ ($\varepsilon_2$):

$$
\begin{aligned}
\dot{Q}_{\mathrm{net},1\to 2} = \frac{\sigma A\left(T_1^4 - T_2^4\right)}{\left(\dfrac{1}{\varepsilon_1} + \dfrac{1}{\varepsilon_2} - 1\right) + \sum_{k=1}^N \left(\dfrac{2}{\varepsilon_{s,k}} - 1\right)} \xrightarrow{\varepsilon_1=\varepsilon_2=\varepsilon_s=\varepsilon} \frac{\sigma A\left(T_1^4 - T_2^4\right)}{(N + 1)\left(\dfrac{2}{\varepsilon} - 1\right)} = \frac{\dot{Q}_{0\text{ shields}}}{N + 1}
  
\end{aligned}
$$

A single floating shield ($N=1$) with $\varepsilon_s = \varepsilon_1 = \varepsilon_2$ reaches steady radiative equilibrium at the fourth-power mean temperature $T_s = \left[\frac{1}{2}(T_1^4 + T_2^4)\right]^{1/4}$ and cuts radiative heat transfer in half; if the shield has much lower emissivity ($\varepsilon_s = 0.04$ aluminum foil) than cardboard walls ($\varepsilon_1 = \varepsilon_2 = 0.92$), a single foil sheet reduces radiative flux by $\frac{2/0.92 - 1 + 2/0.04 - 1}{2/0.92 - 1} = \mathbf{42.7\times}$!

> **[Vector Figure: (a) Oppenheim surface-and-space radiation resistance network with an intermediate low-emissivity aluminum-foil radiation shield ($\varepsilon_s = 0.04$)  **[S12]**. (b) Coaxial-disk view-factor geometry between the $12.7 cm$ R40 heat lamp face at height $h$ and the $30.0 cm$ collector top aperture versus a bare 9 oz cup. | Label: `fig:12:shields-viewfactor`]**
> - **Diagram Annotations & Key Elements:** (a) Two-Body + Radiation Shield Resistance Network • Wall 1 ($T_1,\varepsilon_1$) • Foil Shield ($T_s,\varepsilon_s=0.04$) • Wall 2 ($T_2,\varepsilon_2$) • $E_{b1}=\sigma T_1^4 \;\xrightarrow{\;\frac{1-\varepsilon_1}{\varepsilon_1 A_1}\;}\; J_1 \;\xrightarrow{\;\frac{1}{A_1 F_{1s}}\;}\; J_{s,1} \;\xrightarrow{\;\frac{1-\varepsilon_s}{\varepsilon_s A_s}\;}\; E_{bs}=\sigma T_s^4 \;\xrightarrow{\;\frac{1-\varepsilon_s}{\varepsilon_s A_s}\;}\; J_{s,2} \;\xrightarrow{\;\frac{1}{A_s F_{s2}}\;}\; J_2 \;\xrightarrow{\;\frac{1-\varepsilon_2}{\varepsilon_2 A_2}\;}\; E_{b2}=\sigma T_2^4$ • Shield temperature ($F_{1s}=F_{s2}=1,\; \varepsilon_1=\varepsilon_2$): $T_s = \left[\frac{1}{2}\left(T_1^4 + T_2^4\right)\right]^{1/4}$ (always closer to the hotter temperature $T_1$!) • (b) 2027 Lamp-to-Aperture Coaxial Disk View Factor • R40 Lamp ($r_1=6.35 cm$ at $z=h$) • $z_{\mathrm{ap}}=29.5 cm$ ($r_2=15 cm$) • 9 oz Cup ($r_{\mathrm{cup}}=3.75 cm$) • $F_{\mathrm{bulb}\to\mathrm{ap}}(40\text{ cm}) = 0.665$ • $45.1\times$ bare-cup view factor!

### Planetary Radiative Equilibrium and Multi-Layer Atmospheric Greenhouse Model

A rapidly rotating spherical planet of radius $R_p$ and Bond albedo $A_{\mathrm{alb}}$ at solar constant irradiance $S_0$ $[W/m^2]$ intercepts solar power over its projected disk area $\pi R_p^2$ and radiates thermal IR over its full spherical surface area $4\pi R_p^2$ (tested on the 2026–2027 Cornell Invitational  **[S25]** and Lienhard §10.6 pp. 594–601  **[S12]**):

$$
\begin{aligned}
(1 - A_{\mathrm{alb}}) S_0 \left(\pi R_p^2\right) = 4\pi R_p^2 \sigma T_{\mathrm{eq}}^4 \implies T_{\mathrm{eq}} = \left[\frac{(1 - A_{\mathrm{alb}}) S_0}{4\sigma}\right]^{1/4}, \qquad T_{\mathrm{surf}, N\text{ IR-black layers}} = (N + 1)^{1/4}\,T_{\mathrm{eq}}
  
\end{aligned}
$$

If a single atmospheric layer ($N=1$) has solar transmittance $\tau_{\mathrm{SW}}$ and thermal-IR absorptance/emittance $\varepsilon_{\mathrm{LW}}$, solving the two-node radiative energy balance gives $T_{\mathrm{surf}} = \left[\frac{(1-A_{\mathrm{alb}})S_0}{4\sigma}\cdot\frac{1 + \tau_{\mathrm{SW}}(1 - \varepsilon_{\mathrm{LW}}/2)}{1 - \varepsilon_{\mathrm{LW}}/2}\right]^{1/4}$, which reduces to $2^{1/4}T_{\mathrm{eq}} = 1.1892\,T_{\mathrm{eq}}$ when $\tau_{\mathrm{SW}}=1$ and $\varepsilon_{\mathrm{LW}}=1$.

## Worked Competition Examples (§12)

### Worked Example — 2400 K Heat-Lamp Tungsten Filament: Wien Peak, Exitance & Lambertian Radiance `[2027 Cornell E1  **[S25]**]`

The tungsten filament of a $125.0 W$ R40 heat lamp operates at $T_{\mathrm{fil}} = 2400 K$ with total hemispherical emittance $\varepsilon_W = 0.350$ (Lienhard Table 10.1 p. 546  **[S12]**). Compute (a) the Wien peak wavelength $\lambda_{\max}$, (b) the hemispherical radiant exitance $M_{\mathrm{fil}}$, (c) the directional Lambertian radiance $L_{\mathrm{fil}}$, and (d) the effective radiating surface area $A_{\mathrm{fil}}$ of the filament assuming negligible base conduction.
\tcblower
**Solution.** (a) By Wien's displacement law: $\lambda_{\max} = \dfrac{b_{\mathrm{Wien}}}{T_{\mathrm{fil}}} = \dfrac{2897.772 µm K}{2400 K} = \mathbf{1.2074 µm}$ ($1207.4 nm$, near-IR).\\
(b) By the Stefan–Boltzmann law:

$$
M_{\mathrm{fil}} = \varepsilon_W \sigma T_{\mathrm{fil}}^4 = (0.350)(5.670374×10^{-8} W/m^2/K^4)(2400)^4 = \mathbf{6.581×10^{5} W/m^2}
$$

(c) By Eq. Eq. (`eq:12:lambert-radiance`), the Lambertian directional radiance is $L_{\mathrm{fil}} = \dfrac{M_{\mathrm{fil}}}{\pi} = \dfrac{6.5814×10^{5}}{\pi} = \mathbf{2.095×10^{5} W/m^2/sr}$.\\
(d) Required filament surface area: $A_{\mathrm{fil}} = \dfrac{125.0 W}{6.5814×10^{5} W/m^2} = 1.899×10^{-4} m^2 = \mathbf{1.90 cm^2}$.

**✓ Verified by:** Checked in `check_sec10_13.py` (`EX-12.1-WIEN`, `EX-12.1-RADIANCE`): $\lambda_{\max} = 1.2074 µm$, $L_{\mathrm{fil}} = 2.0948×10^{5} W/m^2/sr$.

### Worked Example — Coaxial-Disk View Factor: Top Collector Aperture vs. Bare 9 oz Cup `[Lienhard Table 10.3  **[S12]**]`

An R40 heat lamp of face diameter $D_1 = 12.70 cm$ ($r_1 = 6.35 cm$) is mounted at regional minimum height $h = 40.0 cm$ above the Testing Surface (Fig. `fig:12:shields-viewfactor`b). Compare the coaxial-disk view factor $F_{1\to 2}$ from the lamp face to: (a) a collector's inscribed circular top aperture of radius $r_2 = 15.0 cm$ elevated to $z_{\mathrm{ap}} = 30.0 cm$ ($d_{\mathrm{ap}} = 40.0 - 30.0 = 10.0 cm$), versus (b) a bare 9 oz cup of mouth radius $r_{\mathrm{cup}} = 3.75 cm$ resting on the Testing Surface with rim height $z_{\mathrm{cup}} = 10.0 cm$ ($d_{\mathrm{cup}} = 40.0 - 10.0 = 30.0 cm$).
\tcblower
**Solution.** Using Eq. Eq. (`eq:12:coaxial-disks`):\\
(a) For the elevated collector top aperture ($d_{\mathrm{ap}} = 10.0 cm$): $R_1 = \frac{6.35}{10.0} = 0.635$, $R_2 = \frac{15.0}{10.0} = 1.500$, so $X = 1 + \frac{1 + 1.500^2}{0.635^2} = 9.0600$, and:

$$
F_{\mathrm{bulb}\to\mathrm{ap}} = \frac{1}{2}\!\left[9.0600 - \sqrt{9.0600^2 - 4\left(\frac{1.500}{0.635}\right)^{\!2}}\right] = \frac{9.0600 - 7.7307}{2} = \mathbf{0.6647} \quad (66.5%\text{ intercepted!})
$$

(b) For the bare cup on the table ($d_{\mathrm{cup}} = 30.0 cm$): $R_1 = \frac{6.35}{30.0} = 0.21167$, $R_2 = \frac{3.75}{30.0} = 0.12500$, $X = 1 + \frac{1 + 0.125^2}{0.21167^2} = 23.669$, giving $F_{\mathrm{bulb}\to\mathrm{cup}} = \mathbf{0.01473}$ ($1.47%$). Raising and widening the aperture captures $\frac{0.6647}{0.01473} = \mathbf{45.1\times}$ more diffuse lamp flux!

**✓ Verified by:** Checked in `check_sec10_13.py` (`EX-12.2-F-AP40`, `EX-12.2-GAIN`): $F_{\mathrm{ap}} = 0.66465$, ratio $= 45.08\times$.

### Worked Example — Multi-Layer Aluminum Foil Radiation Shields vs. Cardboard Walls `[Lienhard Eq. 10.31  **[S12]**]`

The inner cup cradle wall at $T_1 = 45.0 °C$ ($318.15 K$) faces the outer collector box wall at $T_2 = 22.0 °C$ ($295.15 K$). Compute the radiative heat flux $q''_{\mathrm{rad}}$ between the walls for: (a) bare corrugated cardboard walls ($\varepsilon_1 = \varepsilon_2 = 0.92$), (b) lining both walls with household aluminum foil ($\varepsilon_1 = \varepsilon_2 = 0.04,\; N = 0$ intermediate shields), and (c) inserting $N = 2$ floating double-sided aluminum-foil radiation shields ($\varepsilon_s = 0.04$) between the foil-lined walls. Also find the equilibrium temperature $T_s$ of a single floating shield ($N=1$).
\tcblower
**Solution.** Blackbody potential difference is $\sigma(T_1^4 - T_2^4) = (5.670374×10^{-8})(318.15^4 - 295.15^4) = 150.76 W/m^2$. By Eq. Eq. (`eq:12:n-shields`):
{$$
\begin{aligned}
\text{(a) Bare cardboard ($\varepsilon=0.92,\; N=0$):}\ \mathcal{F}_{12} &= \frac{1}{2/0.92 - 1} = 0.85185 \implies q''_{\mathrm{card}} = (0.85185)(150.76) = \mathbf{128.4 W/m^2} \\
  \text{(b) Foil-lined walls ($\varepsilon=0.04,\; N=0$):}\ \mathcal{F}_{12} &= \frac{1}{2/0.04 - 1} = \frac{1}{49} = 0.02041 \implies q''_{\mathrm{foil},0} = \frac{150.76}{49} = \mathbf{3.077 W/m^2}\ (41.7\times\text{ drop}) \\
  \text{(c) Foil walls + $N=2$ shields:}\ \mathcal{F}_{12} &= \frac{1}{(2+1)(49)} = \frac{1}{147} \implies q''_{\mathrm{foil},2} = \frac{150.76}{147} = \mathbf{1.026 W/m^2}\ (\mathbf{125.2\times}\text{ drop!})
\end{aligned}
$$

For $N=1$ equal-$\varepsilon$ shield, $T_s = \left[\frac{1}{2}(318.15^4 + 295.15^4)\right]^{1/4} = 307.08 K = \mathbf{33.93 °C}$.

**✓ Verified by:** Checked in `check_sec10_13.py` (`EX-12.3-Q-CARD`, `EX-12.3-Q-SHIELD`): $q''_{\mathrm{card}} = 128.32 W/m^2$, $q''_{\mathrm{foil},2} = 1.025 W/m^2$.

### Worked Example — Two-Band Selective Absorber vs. Non-Selective Black and White Paint `[Lienhard Ex. 10.12  **[S12]**]`

An insulated flat collector plate receives short-wave irradiance $G = 600.0 W/m^2$ in ambient air at $T_{\mathrm{air}} = 35.0 °C$ ($308.15 K$) with $h_{\mathrm{conv}} = 8.00 W/m^2/K$ and effective radiative surround temperature $T_{\mathrm{sky}} = 18.0 °C$ ($291.15 K$). Using Eq. Eq. (`eq:12:selective-balance`) and Table `tab:12:selective-emissivity`, find the steady equilibrium plate temperature $T_{\mathrm{plate}}$ for: (a) non-selective black paint ($\alpha_{\mathrm{SW}} = 0.90,\; \varepsilon_{\mathrm{MIR}} = 0.90$), (b) white acrylic paint ($\alpha_{\mathrm{SW}} = 0.26,\; \varepsilon_{\mathrm{MIR}} = 0.90$), and (c) a selective Black-Chrome-on-Nickel absorber ($\alpha_{\mathrm{SW}} = 0.95,\; \varepsilon_{\mathrm{MIR}} = 0.09$).
\tcblower
**Solution.** Setting $q''_{\mathrm{net}} = 0$ in Eq. Eq. (`eq:12:selective-balance`): $8.00(T_p - 308.15) + \varepsilon_{\mathrm{MIR}}(5.6704×10^{-8})(T_p^4 - 291.15^4) = 600.0\,\alpha_{\mathrm{SW}}$.\\
(a) Non-selective black ($\alpha=\varepsilon=0.90$, absorbed flux $540 W/m^2$): $T_p = 338.12 K = \mathbf{64.97 °C}$ ($\approx65 °C$ in Lienhard Ex. 10.12).\\
(b) White acrylic paint ($\alpha=0.26,\; \varepsilon=0.90$, absorbed flux $156 W/m^2$): $T_p = 312.01 K = \mathbf{38.86 °C}$ ($26.1 °C$ cooler than black!).\\
(c) Selective Black Chrome ($\alpha=0.95,\; \varepsilon=0.09$, absorbed flux $570 W/m^2$ with $10\times$ lower mid-IR re-radiation!):

$$
8.00(T_p - 308.15) + (0.09)(5.6704×10^{-8})(T_p^4 - 291.15^4) = 570.0 \implies T_p = 371.79 K = \mathbf{98.64 °C}
$$

Suppressing $\varepsilon_{\mathrm{MIR}}$ from $0.90$ to $0.09$ boosts the stagnation temperature by $+33.7 °C$!

**✓ Verified by:** Brent root-finding in `check_sec10_13.py` (`EX-12.4-BLACK`, `EX-12.4-SELECTIVE`): $T_{\mathrm{black}} = 64.966 °C$, $T_{\mathrm{sel}} = 98.645 °C$.

### Worked Example — Planetary Radiative Equilibrium & Single-Layer Greenhouse Sheet `[2027 Cornell E1  **[S25]**]`

Earth receives top-of-atmosphere solar irradiance $S_0 = 1361 W/m^2$ (Lienhard §10.6 p. 594  **[S12]**) with global Bond albedo $A_{\mathrm{alb}} = 0.300$. Compute (a) Earth's bare blackbody radiative equilibrium temperature $T_{\mathrm{eq}}$ without an atmosphere, and (b) the surface temperature $T_s$ under an idealized 1-layer greenhouse atmosphere that is transparent to solar radiation ($\tau_{\mathrm{SW}}=1$) and black to thermal infrared ($\varepsilon_{\mathrm{LW}}=1$).
\tcblower
**Solution.** (a) By Eq. Eq. (`eq:12:planetary-eq`), the globally averaged absorbed solar flux is $q''_{\mathrm{abs}} = \frac{1}{4}(1 - 0.300)(1361) = 238.175 W/m^2$:

$$
T_{\mathrm{eq}} = \left(\frac{238.175}{5.670374×10^{-8}}\right)^{\!1/4} = \mathbf{254.58 K} = -18.57 °C
$$

(b) With $N=1$ IR-absorbing atmospheric sheet radiating $\sigma T_{\mathrm{atm}}^4 = \sigma T_{\mathrm{eq}}^4$ both upward to space and downward to the ground, the ground absorbs $2\sigma T_{\mathrm{eq}}^4$, giving $T_s = 2^{1/4}T_{\mathrm{eq}} = (1.18921)(254.58) = \mathbf{302.75 K} = +29.60 °C$.

**✓ Verified by:** Checked in `check_sec10_13.py` (`EX-12.5-TEQ`, `EX-12.5-TGH`): $T_{\mathrm{eq}} = 254.578 K$, $T_s = 302.746 K$.

### Worked Example — Hottel Crossed-String View Factor & Cavity Effective Absorptance `[Lienhard Table 10.2  **[S12]**]`

(a) Use Hottel's crossed-string rule Eq. Eq. (`eq:12:hottel-strings`) to find the view factor $F_{1\to 2}$ between two parallel, directly opposed long strips of width $w = 10.0 cm$ separated by distance $h = 10.0 cm$. (b) A 2027 cup-cradle cavity has top aperture area $A_{\mathrm{ap}} = 44.18 cm^2$ (matching the 9 oz cup mouth) and interior absorbing surface area $A_{\mathrm{cav}} = 220.9 cm^2$ ($A_{\mathrm{ap}}/A_{\mathrm{cav}} = 0.200$). If the interior surface has intrinsic single-bounce absorptance $\alpha_s = 0.750$, compute the effective cavity absorptance $\alpha_{\mathrm{cav}}$.
\tcblower
**Solution.** (a) Uncrossed side strings have length $L_{u1} = L_{u2} = h = 0.100 m$, while crossed diagonal strings have Pythagorean length $L_{c1} = L_{c2} = \sqrt{w^2 + h^2} = \sqrt{0.100^2 + 0.100^2} = 0.141421 m$. By Eq. Eq. (`eq:12:hottel-strings`):

$$
F_{1\to 2} = \frac{2(0.141421) - 2(0.100)}{2(0.100)} = \sqrt{2} - 1 = \mathbf{0.4142}
$$

(b) By Eq. Eq. (`eq:12:cavity-hohlraum`), cavity multiple-reflection trapping elevates $\alpha_{\mathrm{cav}}$ from $0.750$ to:

$$
\alpha_{\mathrm{cav}} = \frac{0.750}{0.750 + (1 - 0.750)(0.200)} = \frac{0.750}{0.800} = \mathbf{0.9375} \quad (+18.75%\text{ cavity trapping gain!})
$$

**✓ Verified by:** Checked in `check_sec10_13.py` (`EX-12.6-CAV`, `EX-12.6-HOTTEL`): $\alpha_{\mathrm{cav}} = 0.9375$, $F_{1\to 2} = 0.414214$.

### Worked Example — Linearized Radiation Coefficient $h_{\mathrm{rad}}$ vs. Exact Stefan–Boltzmann Power `[Lienhard Ex. 2.7  **[S12]**]`

A small electronic component of surface area $A = 1.3345×10^{-4} m^2$ and emittance $\varepsilon = 0.900$ at $T_1 = 72.30 °C$ ($345.45 K$) radiates inside a large cabinet at $T_2 = 35.00 °C$ ($308.15 K$). Compute (a) the mean temperature $T_m$ and linearized radiation coefficient $h_{\mathrm{rad}} = 4\varepsilon\sigma T_m^3$, (b) the linearized radiative heat loss $\dot{Q}_{\mathrm{rad,lin}} = h_{\mathrm{rad}}A(T_1 - T_2)$ versus exact $\dot{Q}_{\mathrm{rad,ex}} = \varepsilon\sigma A(T_1^4 - T_2^4)$, and (c) verify that the fractional discrepancy matches the Taylor remainder $\frac{1}{4}(\Delta T/T_m)^2$ (Lienhard Eq. 2.28, p. 72  **[S12]**).
\tcblower
**Solution.** (a) $T_m = \frac{1}{2}(345.45 + 308.15) = 326.80 K$, and $\Delta T = 37.30 K$:

$$
h_{\mathrm{rad}} = 4(0.900)(5.670374×10^{-8})(326.80)^3 = \mathbf{7.125 W/m^2/K}
$$

(b) Linearized power: $\dot{Q}_{\mathrm{rad,lin}} = (7.1246)(1.3345×10^{-4})(37.30) = \mathbf{0.03546 W}$, compared to exact $\dot{Q}_{\mathrm{rad,ex}} = (0.900)(5.670374×10^{-8})(1.3345×10^{-4})(345.45^4 - 308.15^4) = \mathbf{0.03558 W}$.\\
(c) Fractional difference is $\frac{0.035580 - 0.035464}{0.035580} = \mathbf{0.00325} = 0.325%$, matching $\frac{1}{4}\!\left(\frac{37.30}{326.80}\right)^{\!2} = \mathbf{0.003254}$!

**✓ Verified by:** Checked in `check_sec10_13.py` (`EX-12.7-HRAD`, `EX-12.7-EXACT`): $h_{\mathrm{rad}} = 7.1246 W/m^2/K$.

## Radiation Traps, Diagnostics & 2027 Optical Concentrator Rules

### [TRAP & DIAGNOSTIC: Top Thermal Radiation Traps on Science Olympiad Exams]

| **Wrong move / Symptom** | **What it produces / Why it fails** | **5-second diagnostic & fix** |
| --- | --- | --- |
| **1. Writing $(T_1 - T_2)^4$ instead of $(T_1^4 - T_2^4)$, or leaving $T$ in Celsius** | $318.15^4 - 295.15^4 = 2.659×10^{9}\ K^4$, whereas $(45 - 22)^4 = 2.798×10^{5}$ (off by $\mathbf{9500\times}$!). | Convert $T_1, T_2$ to Kelvin first, raise each to the 4th power, then subtract. |
| **2. Dividing hemispherical exitance $M = \sigma T^4$ by $2\pi\ sr$ instead of $\pi\ sr$ to get radiance $L$** | Off by a factor of $2\times$; forgets the Lambertian $\cos\theta$ projected-area factor in $\int_0^{\pi/2}\cos\theta\sin\theta\,d\theta = 1/2$. | Diffuse radiance is always $L = M/\pi = \varepsilon\sigma T^4/\pi$ **[S12,S25]**. |
| **3. Assuming visually white surfaces (white paper/paint) have low mid-IR emissivity $\varepsilon_{\mathrm{MIR}}$** | White paper and white acrylic paint have $\varepsilon_{\mathrm{MIR}} = \mathbf{0.90\text{--}0.96}$ at $\lambda \approx 9.6 µm$ — they radiate thermal IR like a blackbody! | Only polished metals ($\mathrm{Al}, \mathrm{Ag}, \mathrm{Cu}, \mathrm{Au}$) have low $\varepsilon_{\mathrm{MIR}} \approx 0.02\text{--}0.05$. |
| **4. Assuming view factor reciprocity is $F_{1\to 2} = F_{2\to 1}$ when $A_1 \ne A_2$** | Violates Second Law! Reciprocity includes areas: $A_1 F_{1\to 2} = A_2 F_{2\to 1}$, so $F_{1\to 2} = F_{2\to 1}$ *only* when $A_1 = A_2$. | Small body $1$ enclosed by large body $2$ has $F_{1\to 2} = 1$, while $F_{2\to 1} = A_1/A_2 \ll 1$. |

### [2027 HEAT-COLLECTOR DEVICE & LAB: 2027 Heat-Lamp Collector Optical & Radiative Design Rules  **[S01,S02,S12,S19]**]

- **Shiny vs. Dull Aluminum Foil — Specular Concentrator vs. Radiant Shield:** Both faces of household aluminum foil have virtually identical total hemispherical IR reflectance ($\rho_{\mathrm{NIR,tot}} = 0.95\text{--}0.97$) and ultra-low mid-IR emittance ($\varepsilon_{\mathrm{MIR}} = 0.030\text{--}0.045$), performing identically inside insulation air gaps. However, inside the upper concentrating funnel, **always orient the SHINY side toward the heat lamp** because its specular (mirror-like) reflectance is $\rho_{\mathrm{spec}} \approx 0.88\text{--}0.91$ (versus $\sim 0.62$ on the micro-matte dull side), focusing directional rays straight into the 9 oz cup rather than scattering rays back out the top aperture!
- **Two-Band Greenhouse Trapping with Removable Clear BoPET Film (`Clarification #5`):** The $2400 K$ tungsten heat lamp emits $>80\%$ of its glass-transmitted power at $\lambda \in [0.4 µm, 2.7 µm]$, whereas the $310 K$ water emits at $\lambda \in [5 µm, 25 µm]$. A $25 µm$ clear BoPET film resting on the cup rim transmits $\tau_{\mathrm{NIR}} \approx 0.90$ of the incoming lamp beam while blocking mid-IR re-radiation ($\tau_{\mathrm{MIR}} \approx 0.20$) AND halting evaporative heat loss!

## Rapid Competition Problem & Solution Bank (§12)

#### Problem P12.1: Concentric Spherical Dewar View Factors & Self-View Factor $F_{2\to 2}$ `[§12.2 | 5.c.iii, 5.c.vi | State / National | 60 s | Reciprocity + Summation | Trap: setting $F_{2\to 2} = 0$ on a concave outer sphere]`

A spherical inner vessel of radius $r_1 = 6.00 cm$ ($\varepsilon_1 = 0.050$) is enclosed concentrically inside an outer spherical shell of inner radius $r_2 = 12.0 cm$ ($\varepsilon_2 = 0.050$) across an evacuated vacuum gap. Compute (a) all four view factors $F_{1\to 1}, F_{1\to 2}, F_{2\to 1}, F_{2\to 2}$, and (b) the gray transfer factor $\mathcal{F}_{1\to 2}$.

**Solution P12.1:** 
(a) Because sphere $1$ is convex, $F_{1\to 1} = \mathbf{0}$ and $F_{1\to 2} = \mathbf{1.000}$. By reciprocity Eq. Eq. (`eq:12:concentric-vf`), $F_{2\to 1} = \dfrac{A_1}{A_2} = \left(\dfrac{r_1}{r_2}\right)^{\!2} = \left(\dfrac{6.00}{12.0}\right)^{\!2} = \mathbf{0.2500}$. By summation on the concave outer sphere $2$, $F_{2\to 2} = 1 - F_{2\to 1} = \mathbf{0.7500}$ ($75\%$ of diffuse rays leaving the outer sphere strike the outer sphere directly!).\\
(b) By Lienhard Eq. (10.27): $\mathcal{F}_{1\to 2} = \left[\dfrac{1}{\varepsilon_1} + \dfrac{A_1}{A_2}\!\left(\dfrac{1}{\varepsilon_2} - 1\right)\right]^{-1} = \left[\dfrac{1}{0.050} + 0.250(19.0)\right]^{-1} = \dfrac{1}{24.75} = \mathbf{0.04040}$.

#### Problem P12.2: Wien Peak Shift & Stefan–Boltzmann Scaling Between 100 W and 125 W Lamps `[§12.1 | 5.c.vi | State / National | 60 s | Fourth-Power Scaling | Trap: confusing $\lambda_{\max} \propto T^{-1}$ with $P_{\mathrm{rad}} \propto T^4$]`

When an incandescent tungsten filament of constant surface area $A_{\mathrm{fil}}$ and constant emittance $\varepsilon_W$ has its electrical power reduced from $P_1 = 125.0 W$ (at filament temperature $T_1 = 2400 K$) to $P_2 = 100.0 W$ (neglecting stem conduction), find the new filament temperature $T_2$ and the new Wien peak wavelength $\lambda_{\max,2}$.

**Solution P12.2:** 
Since $P_{\mathrm{rad}} = \varepsilon_W \sigma A_{\mathrm{fil}} T^4 \propto T^4$, the new filament temperature is:

$$
T_2 = T_1\left(\frac{P_2}{P_1}\right)^{\!1/4} = (2400 K)\left(\frac{100.0}{125.0}\right)^{\!1/4} = 2400(0.8000)^{1/4} = 2400(0.94574) = \mathbf{2270 K}
$$

The Wien peak shifts to a slightly longer near-IR wavelength: $\lambda_{\max,2} = \dfrac{2897.77 µm K}{2269.8 K} = \mathbf{1.277 µm}$ (up from $1.207 µm$, increasing direct top-millimeter water absorption by $+2.3\%$!).

#### Problem P12.3: Asymmetric Radiation Shield Between High-Emissivity and Low-Emissivity Walls `[§12.2 | 5.c.iii, 5.c.vi | National / MIT | 75 s | Oppenheim Network | Trap: assuming shield temperature $T_s^4 = (T_1^4+T_2^4)/2$ when $\varepsilon_1 \ne \varepsilon_2$]`

Two large parallel plates at $T_1 = 400.0 K$ ($\varepsilon_1 = 0.800$) and $T_2 = 300.0 K$ ($\varepsilon_2 = 0.800$) are separated by a thin floating sheet that is painted black on Side A facing Plate 1 ($\varepsilon_{s,A} = 0.800$) and polished aluminum on Side B facing Plate 2 ($\varepsilon_{s,B} = 0.050$). Find (a) the steady temperature $T_s$ of the asymmetric shield, and (b) does flipping the shield ($180^\circ$) change the net heat flux $q''_{1\to 2}$ or the shield temperature $T_s$?

**Solution P12.3:** 
(a) The resistance between Plate 1 and Shield Side A is $R_{1s}'' = \frac{1}{0.80} + \frac{1}{0.80} - 1 = \mathbf{1.500}$, while the resistance between Shield Side B and Plate 2 is $R_{s2}'' = \frac{1}{0.050} + \frac{1}{0.80} - 1 = \mathbf{20.250}$ ($13.5\times$ larger!). At steady state, $q''_{1\to s} = q''_{s\to 2} \implies \frac{\sigma(T_1^4 - T_s^4)}{1.500} = \frac{\sigma(T_s^4 - T_2^4)}{20.250}$:

$$
T_s^4 = \frac{20.250\,T_1^4 + 1.500\,T_2^4}{20.250 + 1.500} = \frac{20.250(400^4) + 1.500(300^4)}{21.750} = 2.4393×10^{10}\ K^4 \implies T_s = \mathbf{395.2 K}
$$

(b) Flipping the shield leaves the **total series resistance** $R_{\mathrm{tot}}'' = 1.500 + 20.250 = 21.750$ and **net heat flux $q''_{1\to 2}$ completely unchanged**, but shifts the shield temperature $T_s$ from $395.2 K$ (close to $T_1$) to $310.7 K$ (close to $T_2$)!

#### Problem P12.4: Thermodynamic Second-Law Limit on Optical Concentration Ratio $C_{\max}$ `[§12.2 | 5.c.iv, 5.c.vi | National | 60 s | Second Law + Reciprocity | Trap: exceeding $1/\sin^2\theta_s$ or $T_{\mathrm{target}} > T_{\mathrm{source}}$]`

An R40 heat lamp of radiating disk radius $r_{\mathrm{source}} = 6.35 cm$ at temperature $T_{\mathrm{source}} = 2400 K$ sits at distance $d = 20.0 cm$ above a collector aperture ($\sin\theta_s = r_{\mathrm{source}}/\sqrt{r_{\mathrm{source}}^2 + d^2} = 0.3027$). According to the Second Law of Thermodynamics (conservation of optical \'etendue / view-factor reciprocity $A_1 F_{1\to 2} = A_2 F_{2\to 1}$ with $F_{2\to 1} \le 1$), what is the maximum theoretical geometric concentration ratio $C_{\max} = A_{\mathrm{ap}}/A_{\mathrm{receiver}}$ achievable by any passive 3-D ideal concentrator?

**Solution P12.4:** 
For a 3-D axisymmetric source subtending half-angle $\theta_s$ at the aperture, view-factor reciprocity requires $A_{\mathrm{ap}} F_{\mathrm{ap}\to\mathrm{source}} = A_{\mathrm{ap}}\sin^2\theta_s \le A_{\mathrm{rec}} F_{\mathrm{rec}\to\mathrm{ap}} \le A_{\mathrm{rec}}(1)$. If $C_{\mathrm{geom}} > 1/\sin^2\theta_s$, an isolated receiver could reach a steady temperature $T_{\mathrm{rec}} > T_{\mathrm{source}}$, violating the Clausius statement of the Second Law! Thus:

$$
C_{\max,\mathrm{3D}} = \frac{1}{\sin^2\theta_s} = \frac{r_{\mathrm{source}}^2 + d^2}{r_{\mathrm{source}}^2} = 1 + \left(\frac{20.0}{6.35}\right)^{\!2} = \mathbf{10.92\times} \quad (\text{and at } d = 35.0 cm,\ C_{\max,\mathrm{3D}} = \mathbf{31.38\times})
$$

**Table:** Universal Planck Blackbody Fractional Function $F_{0\to\lambda T} \equiv \frac{1}{\sigma T^4}\int_0^{\lambda} M_{\lambda,b}(\lambda',T)\,d\lambda'$ as a Function of $\lambda T$ $[µm K]$ (Lienhard Table 10.2, p. 556  **[S12,S25]**). Fraction of total blackbody power emitted in band $[\lambda_1, \lambda_2]$ is $\Delta F = F_{0\to\lambda_2 T} - F_{0\to\lambda_1 T}$.

| $\lambda T$ $[µm K]$ | $F_{0\to\lambda T}$ | $\lambda T$ $[µm K]$ | $F_{0\to\lambda T}$ | $\lambda T$ $[µm K]$ | $F_{0\to\lambda T}$ | $\lambda T$ $[µm K]$ | $F_{0\to\lambda T}$ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| $1000$ | $0.00032$ | $2400$ | $0.14026$ | $3800$ | $0.44338$ | $6480$ | $0.77635$ |
| $1400$ | $0.00779$ | $2600$ | $0.18312$ | $4000$ | $0.48088$ | $7000$ | $0.80811$ |
| $1680$ | $0.02540$ | $2880$ | $0.24603$ | $4107.6$ | $0.50000$ | $8000$ | $0.85629$ |
| $1800$ | $0.03934$ | $2897.8$ | $0.25006$ | $4600$ | $0.57928$ | $10000$ | $0.91420$ |
| $2000$ | $0.06673$ | $3200$ | $0.31810$ | $5000$ | $0.63375$ | $15000$ | $0.96898$ |
| $2200$ | $0.10089$ | $3600$ | $0.40361$ | $6000$ | $0.73782$ | $25000$ | $0.99222$ |

#### Problem P12.5: Planck Band-Fraction Split of a $2400 K$ Heat Lamp Across Visible, Water-Penetrating Near-IR, and Glass Cutoff `[§12.1 | 5.c.vi | National / MIT | 75 s | Table 12.2 Band Lookup | Trap: integrating Planck law by hand instead of subtracting $F_{0\to\lambda T}$]`

Using Table `tab:12:blackbody-fraction`, determine for a $2400 K$ blackbody filament: (a) the fraction of power emitted at $\lambda \le 0.700 µm$ ($\lambda T = 1680 µm K$, visible + UV), (b) the fraction emitted in the water-surface-absorbed near-IR window $\lambda \in [1.200 µm, 2.700 µm]$ ($\lambda T \in [2880, 6480 µm K]$), and (c) the median wavelength $\lambda_{\mathrm{med}}$ that divides the emitted power into two equal $50\%$ halves.

**Solution P12.5:** 
- **(a)** At $\lambda_1 = 0.700 µm$, $\lambda_1 T = (0.700)(2400) = 1680 µm K \implies F_{0\to 1680} = \mathbf{0.02540}$ ($\mathbf{2.54%}$ visible/UV).
- **(b)** At $\lambda_2 = 1.200 µm$, $\lambda_2 T = 2880 µm K \implies F_{0\to 2880} = 0.24603$. At $\lambda_3 = 2.700 µm$ (bulb glass cutoff), $\lambda_3 T = 6480 µm K \implies F_{0\to 6480} = 0.77635$. The power fraction in $[1.20 µm, 2.70 µm]$ is:
  
$$
\Delta F_{1.2\to 2.7\,\mu\mathrm{m}} = F_{0\to 6480} - F_{0\to 2880} = 0.77635 - 0.24603 = \mathbf{0.53032} \quad (\mathbf{53.03%}\text{ of total filament emission!})
$$
- **(c)** From Table `tab:12:blackbody-fraction`, $F_{0\to\lambda_{\mathrm{med}} T} = 0.50000$ occurs at $\lambda_{\mathrm{med}} T = 4107.6 µm K \implies \lambda_{\mathrm{med}} = \dfrac{4107.6}{2400} = \mathbf{1.7115 µm}$ (notice that $\lambda_{\mathrm{med}} = 1.4175\,\lambda_{\max}$ because the Planck tail is skewed toward long wavelengths, while $25.0\%$ of power lies below $\lambda_{\max}$ and $75.0\%$ lies above $\lambda_{\max}$!).

#### Problem P12.6: Combined Multimode Convection + Radiation From an Uninsulated vs. Foil-Wrapped Pipe `[§12.3 | 5.c.iii, 5.c.vi | State / National | 75 s | Parallel Conductances $h_{\mathrm{tot}} = h_{\mathrm{conv}} + h_{\mathrm{rad}}$ | Trap: forgetting radiation equals or exceeds natural convection in still air]`

A horizontal oxidized steel steam pipe of outer diameter $D = 50.0 mm$, length $\ell = 2.00 m$ ($A_s = \pi D\ell = 0.31416 m^2$), and surface temperature $T_s = 107.0 °C$ ($380.15 K$) passes through a large room with still air and walls at $T_\infty = T_{\mathrm{surr}} = 27.0 °C$ ($300.15 K$), where the natural-convection heat transfer coefficient is $h_{\mathrm{conv}} = 6.80 W/m^2/K$. Calculate (a) the linearized radiative coefficient $h_{\mathrm{rad}}$ and total heat loss $\dot{Q}_{\mathrm{tot}}$ when the bare oxidized steel has $\varepsilon_1 = 0.850$, and (b) the percentage reduction in total heat loss if a thin layer of shiny aluminum foil tape ($\varepsilon_2 = 0.040$) is wrapped tightly over the pipe without adding any foam thickness.

**Solution P12.6:** 
- **(a)** Using the linearized radiation coefficient at $T_s = 380.15 K$ and $T_{\mathrm{surr}} = 300.15 K$ ($\Delta T = 80.0 K$):
  
$$
h_{\mathrm{rad},1} = \varepsilon_1 \sigma\left(T_s^2 + T_{\mathrm{surr}}^2\right)\left(T_s + T_{\mathrm{surr}}\right) = (0.850)(5.670374×10^{-8})\left(380.15^2 + 300.15^2\right)(680.30) = \mathbf{7.688 W/m^2/K}
$$

  Notice that in still air, $h_{\mathrm{rad},1} = 7.69 W/m^2/K > h_{\mathrm{conv}} = 6.80 W/m^2/K$! Total parallel loss is:
  
$$
\dot{Q}_{\mathrm{tot},1} = \left(h_{\mathrm{conv}} + h_{\mathrm{rad},1}\right)A_s\Delta T = (6.80 + 7.688)(0.31416)(80.0) = \mathbf{364.1 W}
$$
- **(b)** Wrapping shiny aluminum foil tape reduces $\varepsilon$ from $0.850$ to $0.040$:
  
$$
h_{\mathrm{rad},2} = \frac{0.040}{0.850}(7.688 W/m^2/K) = \mathbf{0.362 W/m^2/K}, \qquad
    \dot{Q}_{\mathrm{tot},2} = (6.80 + 0.362)(0.31416)(80.0) = \mathbf{180.0 W}
$$

  This achieves a $\mathbf{50.6%}$ reduction in total heat loss with zero foam thickness!

#### Problem P12.7: Thermocouple Bead Radiative Error inside a Cool-Wall Hot-Gas Duct `[§12.3 | 5.c.iii, 5.c.vi | National / MIT | 75 s | Convection = Radiation Balance | Trap: forgetting that thermocouple reads its own bead temperature $T_{tc}$, not gas $T_g$]`

An unshielded spherical thermocouple junction ($\varepsilon_{tc} = 0.850$) is inserted into a hot air stream flowing through a large sheet-metal duct whose walls are at $T_w = 350.0 K$ ($76.85 °C$). The convective heat transfer coefficient on the small thermocouple bead is $h_{\mathrm{conv}} = 65.0 W/m^2/K$, and the thermocouple reads a steady temperature $T_{tc} = 450.0 K$ ($176.85 °C$). Calculate (a) the true hot-gas temperature $T_g$, and (b) the new thermocouple reading if a polished cylindrical silver radiation shield ($\varepsilon_s = 0.030$) is placed around the bead.

**Solution P12.7:** 
- **(a)** At steady state, convective heat transfer from the gas to the thermocouple bead equals radiative heat loss from the small bead to the large enclosing duct walls ($F_{tc\to w} = 1$, $A_{tc}/A_w \to 0$):
  
$$
h_{\mathrm{conv}}\left(T_g - T_{tc}\right) = \varepsilon_{tc}\sigma\left(T_{tc}^4 - T_w^4\right) = (0.850)(5.670374×10^{-8})\left(450.0^4 - 350.0^4\right) = (4.8198\times 10^{-8})(2.6000×10^{10}) = \mathbf{1253.2 W/m^2}
$$

  
$$
T_g = T_{tc} + \frac{1253.2 W/m^2}{65.0 W/m^2/K} = 450.0 + 19.28 = \mathbf{469.28 K} = \mathbf{196.13 °C}
$$

  The unshielded thermocouple under-reads the true gas temperature by $\mathbf{-19.28 K}$!
- **(b)** Surrounding the bead with a polished radiation shield reduces the radiative loss by $>90\%$, cutting the radiation error from $-19.3 K$ to $<1.2 K$ ($T_{tc,\mathrm{shielded}} \approx 468.1 K$).

#### Problem P12.8: Two-Surface Gray Enclosure vs. Blackbody Exchange Between Unequal Cylinders `[§12.2 | 5.c.vi | State / National | 60 s | Oppenheim 3-Resistor Formula | Trap: applying parallel-plate $\frac{1}{\varepsilon_1}+\frac{1}{\varepsilon_2}-1$ without area ratio $A_1/A_2$]`

A hot inner cylinder of diameter $D_1 = 60.0 mm$ ($T_1 = 360.0 K$, $\varepsilon_1 = 0.200$) is surrounded concentrically by a cold outer cylinder of diameter $D_2 = 180.0 mm$ ($T_2 = 300.0 K$, $\varepsilon_2 = 0.100$) across an evacuated gap of length $\ell = 0.500 m$. Calculate (a) the exact radiative heat transfer rate $\dot{Q}_{1\to 2}$, and (b) the percentage error committed if a student uses the flat parallel-plate denominator $\frac{1}{\varepsilon_1} + \frac{1}{\varepsilon_2} - 1$ instead of weighting the outer surface resistance by $A_1/A_2 = D_1/D_2$.

**Solution P12.8:** 
- **(a)** Inner surface area is $A_1 = \pi D_1 \ell = \pi(0.0600)(0.500) = 0.094248 m^2$, and the area ratio is $A_1 / A_2 = D_1 / D_2 = 60.0 / 180.0 = 1/3$. By Lienhard Eq. (10.27) (Eq. `eq:12:concentric-vf`):
  
$$
\frac{1}{\mathcal{F}_{1\to 2}} = \frac{1}{\varepsilon_1} + \frac{A_1}{A_2}\!\left(\frac{1}{\varepsilon_2} - 1\right) = \frac{1}{0.200} + \frac{1}{3}(10.0 - 1) = 5.00 + 3.00 = \mathbf{8.000}
$$

  
$$
\dot{Q}_{1\to 2} = \frac{A_1 \sigma\left(T_1^4 - T_2^4\right)}{8.000} = \frac{(0.094248)(5.670374×10^{-8})\left(360.0^4 - 300.0^4\right)}{8.000} = \frac{(0.094248)(493.10)}{8.000} = \mathbf{5.809 W}
$$
- **(b)** Using the flat-plate denominator $\frac{1}{0.200} + \frac{1}{0.100} - 1 = 14.00$ would predict $\dot{Q}_{\mathrm{flat}} = \frac{8.00}{14.00}(5.809) = 3.320 W$ — an error of $\mathbf{-42.9%}$!

—
**See also:** §`sec:01.11` (`QS-11` Radiation Fast Sheet), §`sec:10` (Conduction Networks), §`sec:11` (Convection & Evaporation), §`sec:13` (Transient Lumped Heating & $T^4$ Vacuum Cooling), §`sec:14` (Optical Materials Table), §`sec:15` (Ray-Traced Ellipsoidal/CPC Concentrator).
