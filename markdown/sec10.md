<!-- Source: src/sec10.tex | Tab: Tab 5: TRANSFER | Target: 12 pp -->
# §10: Steady-State Heat Conduction, Fourier's Law, Composite Walls, Cylinders/Spheres, Contact Resistance & Critical Radius {#sec:10}

> **[SCOPE: REQUIRED | 2027 Rule 5.c.iii (All Tournament Levels: Kinds of Heat Transfer, Thermal Conductivity) | Sources:  **[S01]**,  **[S12]**,  **[S13]**,  **[S17]**,  **[S25]**]**

### [FORMULA & DECISION CARD: §10 Master Conduction, Thermal Resistance, Fin & Wiedemann–Franz Decision Card  **[S12,S13,S25]**]

| **Formula** | **Variables (SI units)** | **Flags** | **Use when** |
| --- | --- | --- | --- |
| $\dot{Q} = k A \dfrac{T_1 - T_2}{L} = \dfrac{\Delta T}{R_{\mathrm{slab}}}$ | $\dot{Q}$: conduction rate $(W)$; $k$: thermal conductivity $(W/m/K)$; $A$: cross-sectional area $\perp$ heat flow $(m^2)$; $L$: thickness $(m)$; $\Delta T = T_1 - T_2 > 0$ $(K)$ | **[1D-STEADY]** | Plane slab/wall of constant area $A$ and homogeneous $k$ |
| $q'' = \dfrac{\dot{Q}}{A} = -k\dfrac{\Delta T}{\Delta x}$ | $q''$: heat flux $(W/m^2)$; minus sign indicates heat flows down the temperature gradient ($T_{\mathrm{hot}} \to T_{\mathrm{cold}}$) | **[1D-STEADY]** | Heat flow per unit area; constant across plane series layers |
| $\alpha = \dfrac{k}{\rho c_p}, \quad b = \sqrt{k\rho c_p}$ | $\alpha$: thermal diffusivity $(m^2/s)$; $b$: thermal effusivity $(J/m^2/K/s^1/2)$; $\rho c_p$: volumetric heat capacity $(J/m^3/K)$ | **[CONST-c]** | Speed of thermal penetration ($\delta_t \sim 2\sqrt{\alpha t}$) vs. contact heat sharing |
| $R_{\mathrm{slab}} = \dfrac{L}{k A}, \quad R_{\mathrm{val}} = \dfrac{L}{k}$ | $R_{\mathrm{slab}}$: lumped resistance $(K/W)$; $R_{\mathrm{val}} = A R_{\mathrm{slab}}$: unit-area $R$-value $(m^2 K/W)$ [$1\,\text{RSI} = 5.678\,\text{R}_{\text{US}}$] | **[1D-STEADY]** | Plane walls; series resistances add ($R_{\mathrm{tot}} = \sum R_i$) |
| $R_{\mathrm{cyl}} = \dfrac{\ln(r_o / r_i)}{2\pi k \ell} = \dfrac{r_o - r_i}{k A_{\mathrm{lm}}}$ | $r_i, r_o$: inner/outer radii $(m)$; $\ell$: axial length $(m)$; log-mean area $A_{\mathrm{lm}} = \dfrac{2\pi\ell(r_o - r_i)}{\ln(r_o/r_i)}$ $(m^2)$ | **[1D-RADIAL]** | Cylindrical pipe, tube, or 2027 cup sidewall ($\dot{Q} = \Delta T / R_{\mathrm{cyl}}$) |
| $R_{\mathrm{sph}} = \dfrac{r_o - r_i}{4\pi k r_i r_o} = \dfrac{r_o - r_i}{k A_{\mathrm{gm}}}$ | $r_i, r_o$: inner/outer radii $(m)$; geometric-mean area $A_{\mathrm{gm}} = \sqrt{A_i A_o} = 4\pi r_i r_o$ $(m^2)$ | **[1D-RADIAL]** | Spherical shells, Dewar bulbs, or quasi-spherical cavities |
| $R_{\mathrm{tot,ser}} = \sum_{i=1}^n R_i, \quad \dfrac{1}{R_{\mathrm{tot,par}}} = \sum_{j=1}^m \dfrac{1}{R_j}$ | Series: common $\dot{Q}$, $\Delta T = \dot{Q} R_{\mathrm{tot,ser}}$; Parallel: common $\Delta T$, $\dot{Q}_{\mathrm{tot}} = \sum \dot{Q}_j = \Delta T / R_{\mathrm{tot,par}}$ | **[NETWORK]** | Multi-layer walls, studs/bolts (thermal bridges), combined modes |
| $U A = \dfrac{1}{R_{\mathrm{tot}}}, \quad \dot{Q} = U A \Delta T_{\mathrm{overall}}$ | $U$: overall heat transfer coefficient $(W/m^2/K)$ referenced to chosen area $A$ ($U_i A_i = U_o A_o$) | **[COMPOSITE]** | Heat exchangers, walls with indoor/outdoor convection $h_{\mathrm{in}}, h_{\mathrm{out}}$ |
| $R_c = \dfrac{1}{h_c A}, \quad \Delta T_c = \dfrac{\dot{Q}}{h_c A} = \dfrac{q''}{h_c}$ | $h_c$: interfacial contact conductance $(W/m^2/K)$ (Lienhard Table 2.1 **[S12]**); $R_c'' = 1/h_c$ $(m^2 K/W)$ | **[INTERFACE]** | Finite temperature jump across rough solid–solid joints |
| $r_{\mathrm{crit,cyl}} = \dfrac{k_{\mathrm{ins}}}{h_{\mathrm{ext}}}, \quad r_{\mathrm{crit,sph}} = \dfrac{2k_{\mathrm{ins}}}{h_{\mathrm{ext}}}$ | $r_{\mathrm{crit}}$: outer insulation radius maximizing $\dot{Q}$ (minimizing $R_{\mathrm{tot}}$), where $\mathrm{Bi}_{r_{\mathrm{crit}}} = h_{\mathrm{ext}}r_{\mathrm{crit}}/k_{\mathrm{ins}} = 1$ (cyl) or $2$ (sph) | **[RADIAL-OPT]** | Thin wires/tubes ($r_i < r_{\mathrm{crit}}$); for 9 oz cup $r_i \gg r_{\mathrm{crit}}$ so insulation always helps |
| $m = \sqrt{\dfrac{h P}{k A_c}}, \quad \eta_f = \dfrac{\tanh(m L_c)}{m L_c}$ | $P$: fin perimeter $(m)$; $A_c$: fin cross-section $(m^2)$; $L_c = L + A_c/P$; $\dot{Q}_f = \eta_f h A_f \theta_b$; effectiveness $\varepsilon_f = \dot{Q}_f / (h A_c \theta_b)$ | **[1D-FIN]** | Extended surfaces / cooling pins ($\varepsilon_f \ge 2$ required to justify fins) |
| $\dfrac{k_e}{\sigma_e T} = k_e \dfrac{\rho_e}{T} = L_0 = \dfrac{\pi^2}{3}\!\left(\dfrac{k_B}{e}\right)^{\!2}$ | $k_e$: electronic thermal conductivity $(W/m/K)$; $\sigma_e = 1/\rho_e$: electrical conductivity $(S/m)$; $L_0 = 2.443×10^{-8} W Ω/K^2$ | **[METALS]** | Wiedemann–Franz law separating electronic $k_e$ from phonon $k_{\mathrm{ph}} = k - k_e$ **[S25]** |

## Fourier's Law, Thermal Conductivity Mechanisms & Diffusivity

### Macroscopic Law and Sign Convention

Heat conduction is the diffusive transfer of internal thermal energy from more energetic particles to adjacent less energetic particles without bulk macroscopic fluid motion  **[S12,S13]**. In 1822, Jean-Baptiste Joseph Fourier established that the local heat flux $q''$ $[W/m^2]$ is directly proportional to the negative temperature gradient. For steady one-dimensional conduction across a homogeneous plane slab of thickness $L$ $[m]$ and cross-sectional area $A$ $[m^2]$ held at uniform boundary temperatures $T_1$ (at $x=0$) and $T_2$ (at $x=L$):

$$
\begin{aligned}
\dot{Q}_{\mathrm{cond}} = A q'' = -k A \frac{T_2 - T_1}{L - 0} = \frac{k A (T_1 - T_2)}{L} = \frac{\Delta T}{R_{\mathrm{slab}}}, \qquad T(x) = T_1 - \frac{T_1 - T_2}{L}\,x
  
\end{aligned}
$$

where $k$ $[W/m/K]$ is the material's **thermal conductivity**. Because heat flows spontaneously from higher temperature to lower temperature ($T_1 > T_2 \implies \dot{Q}_{\mathrm{cond}} > 0$ in the $+x$ direction), the temperature profile $T(x)$ inside a homogeneous plane wall with constant $k$ and no internal heat generation ($\dot{q}_{\mathrm{gen}} = 0$) is strictly **linear**. If $k(T)$ varies linearly with temperature as $k(T) = k_0[1 + \beta_k(T - T_0)]$, the exact steady conduction rate is obtained simply by evaluating $k$ at the arithmetic mean temperature $T_m = (T_1 + T_2)/2$: $\dot{Q} = k(T_m) A (T_1 - T_2)/L$  **[S12]**.

### Microscopic Transport Carriers and the Wiedemann–Franz Law

In any condensed or gaseous medium, total thermal conductivity is the sum of contributions from mobile charge carriers (free electrons $k_e$) and quantized lattice vibrations or molecular collisions (phonons/molecules $k_{\mathrm{ph}}$):

$$
\begin{aligned}
k_{\mathrm{tot}} = k_e + k_{\mathrm{ph}}, \qquad k_{\mathrm{kinetic}} = \frac{1}{3} C_V v_{\mathrm{carrier}} \lambda_{\mathrm{mfp}}
  
\end{aligned}
$$

where $C_V$ $[J/m^3/K]$ is the carrier volumetric heat capacity, $v_{\mathrm{carrier}}$ is the carrier speed (Fermi velocity $v_F \sim e6 m/s$ for electrons; sound speed $c_s \sim 5×10^{3} m/s$ for phonons; mean thermal speed $\bar{v} = \sqrt{8RT/(\pi M)}$ for gases), and $\lambda_{\mathrm{mfp}}$ is the carrier mean free path  **[S12,S15]**.
- **Pure Metals & Alloys ($k \approx 10–427 W/m/K$):** Conduction is dominated by free conduction electrons ($k_e \gg k_{\mathrm{ph}}$). In 1853, Gustav Wiedemann and Rudolph Franz discovered that at a given absolute temperature $T$, the ratio of electronic thermal conductivity $k_e$ to electrical conductivity $\sigma_e = 1/\rho_e$ is nearly universal across metals. Sommerfeld's quantum free-electron theory yields the exact **Sommerfeld Lorenz number** $L_0$ (tested on the 2026–2027 Cornell Invitational  **[S25]**):
  
$$
\begin{aligned}
\frac{k_e}{\sigma_e T} = k_e \frac{\rho_e}{T} = L_0 = \frac{\pi^2}{3}\!\left(\frac{k_B}{e}\right)^{\!2} = 2.44300×10^{-8} W Ω/K^2
    
\end{aligned}
$$

  Alloying a pure metal (e.g., adding $4%\ \mathrm{Cu}$ to pure $\mathrm{Al}$ to make Duralumin, or $\mathrm{Cr/Ni}$ to iron to make AISI 304 stainless steel) introduces impurity scattering centers that sharply reduce $\lambda_{\mathrm{mfp}}$ for electrons, dropping $k$ from $237 W/m/K$ (pure $\mathrm{Al}$) to $164 W/m/K$ (Duralumin) and from $80 W/m/K$ (pure $\mathrm{Fe}$) to $13.8 W/m/K$ (AISI 304 stainless steel)  **[S12]**.
- **Crystalline vs. Amorphous Nonmetals ($k \approx 0.02–2000 W/m/K$):** In stiff, low-atomic-mass crystals with few defects, long phonon mean free paths produce extraordinary thermal conductivity without free electrons: Type IIb diamond has $k = 1350 W/m/K$ (and pyrolytic graphite $\parallel$ layer planes has $k = 2000 W/m/K$ at $20 °C$, exceeding silver's $427 W/m/K$ by $>4.6\times$!), silicon has $k = 153 W/m/K$, and sapphire ($\mathrm{Al_2O_3}$) has $k = 46 W/m/K$  **[S12]**. Conversely, in amorphous glasses ($k_{\mathrm{Pyrex}} = 1.3 W/m/K$, $k_{\mathrm{soda\text{-}lime}} = 1.1 W/m/K$) and polymers ($k = 0.15–0.35 W/m/K$), structural disorder restricts $\lambda_{\mathrm{mfp}}$ to a single interatomic bond spacing ($\sim 0.5 nm$).
- **Liquids ($k \approx 0.10–0.68 W/m/K$ for nonmetallic liquids) and Gases ($k \approx 0.006–0.18 W/m/K$):** Liquid water ($k = 0.598 W/m/K$ at $20 °C$, rising to $0.631 W/m/K$ at $40 °C$  **[S09,S12]**) is the most conductive common nonmetallic liquid because of its low molar mass and hydrogen-bonded network, yet it is still $\sim 650\times$ less conductive than copper. In ideal gases, kinetic theory gives $k_{\mathrm{gas}} \approx \frac{1}{3}\rho c_v \bar{v}\lambda_{\mathrm{mfp}} \propto \frac{\sqrt{T/M}}{d_{\mathrm{mol}}^2}$, so gas conductivity **increases with temperature** ($\propto \sqrt{T}$), is **independent of pressure** down to the Knudsen vacuum regime ($\lambda_{\mathrm{mfp}} \sim L$), and is highest for light gases ($\mathrm{H_2}$: $0.182 W/m/K$; $\mathrm{He}$: $0.151 W/m/K$ vs. stagnant air: $0.02623 W/m/K$ and $\mathrm{CO_2}$: $0.0166 W/m/K$ at $300 K$  **[S10,S12]**).

**Table:** Verified Thermal Conductivity $k$, Density $\rho$, Specific Heat $c_p$, Diffusivity $\alpha$, and Effusivity $b$ at $20 °C$–$27 °C$ (Lienhard Tables A.1, A.2, A.3, A.6  **[S12]**).

| **Material (20 °C unless noted)** | **$\rho$ $(kg/m^3)$** | **$c_p$ $(J/kg/K)$** | **$k$ $(W/m/K)$** | **$\alpha$ $(m^2/s)$** | **$b = \sqrt{k\rho c_p}$** | **Carrier / 2027 Role** |
| --- | --- | --- | --- | --- | --- | --- |
| Pyrolytic graphite ($\parallel$ planes, 27 °C) | $2200$ | $710$ | $2000$ | $1.28\times 10^{-3}$ | $55\,890$ | Anisotropic phonons ($\perp$: $k=9.5 W/m/K$) |
| Diamond (Type IIb) | $3250$ | $510$ | $1350$ | $8.14\times 10^{-4}$ | $47\,300$ | Sp$^3$ covalent phonon crystal |
| Silver ($99.99+\%$ pure) | $10\,524$ | $236$ | $427$ | $1.719\times 10^{-4}$ | $32\,570$ | Highest-$k$ pure metal |
| Copper (pure) | $8954$ | $384$ | $398$ | $1.157\times 10^{-4}$ | $37\,000$ | Thin non-contact absorber foil |
| Gold (pure) | $19\,320$ | $129$ | $318$ | $1.276\times 10^{-4}$ | $28\,150$ | Non-oxidizing IR reflector |
| Aluminum (pure / household foil) | $2707$ | $905$ | $237$ | $9.61\times 10^{-5}$ | $24\,100$ | Primary 2027 reflector ($\varepsilon \approx 0.035$) |
| Aluminum alloy 6061-T6 | $2700$ | $896$ | $167$ | $6.90\times 10^{-5}$ | $20\,100$ | Structural flashing/sheet |
| Brass ($70\%\ \mathrm{Cu}, 30\%\ \mathrm{Zn}$) | $8522$ | $385$ | $109$ | $3.32\times 10^{-5}$ | $18\,910$ | Calorimetry cylinder standard |
| Iron (pure) / Carbon steel ($0.5\%\ \mathrm{C}$) | $7833$ | $465$ | $54.0$ | $1.47\times 10^{-5}$ | $14\,030$ | Fastener thermal-bridge hazard! |
| Lead (pure) | $11\,373$ | $130$ | $35.0$ | $2.34\times 10^{-5}$ | $7193$ | Low-$c_p$ calorimetry weight |
| Stainless steel (AISI 304) | $8000$ | $400$ | $13.8$ | $4.31\times 10^{-6}$ | $6645$ | Low-$k$ probe sheath stem |
| Ice Ih (0 °C) | $917$ | $2100$ | $2.215$ | $1.15\times 10^{-6}$ | $2065$ | $3.7\times$ higher $k$ than liquid water! |
| Borosilicate glass (Pyrex, 60 °C) | $2210$ | $753$ | $1.30$ | $7.81\times 10^{-7}$ | $1471$ | Selective greenhouse glazing |
| Liquid water (27 °C / 300 K) | $996.6$ | $4179$ | $0.613$ | $1.47\times 10^{-7}$ | $1598$ | Target working fluid ($\mathrm{Bi}_z > 0.1$) |
| Polyethylene (LDPE film / HDPE) | $920$ | $2100$ | $0.330$ | $1.71\times 10^{-7}$ | $798$ | Legal evaporation cling wrap |
| Polycarbonate (Lexan, 23 °C) | $1200$ | $1250$ | $0.290$ | $1.93\times 10^{-7}$ | $660$ | Rigid glazing window |
| Polypropylene (`#5 PP` clear cup) | $905$ | $1900$ | $0.185$ | $1.08\times 10^{-7}$ | $564$ | ES 9 oz party cup wall |
| Cardboard (solid sheet / fluted) | $790 / 180$ | $1340$ | $0.14 / 0.055$ | $1.32\times 10^{-7}$ | $385 / 115$ | Legal structural box & baffles |
| Plywood (Douglas fir, 24 °C) | $550$ | $1200$ | $0.120$ | $1.82\times 10^{-7}$ | $281$ | Outer framing baseplate |
| Balsa wood ($\perp$ grain, 15 °C) | $100$ | $1600$ | $0.050$ | $3.13\times 10^{-7}$ | $89.4$ | Knife-edge 3-point cup support |
| Sheep wool / Cotton batting | $145 / 45$ | $1500 / 1340$ | $0.050 / 0.039$ | $2.30\times 10^{-7}$ | $104 / 48.5$ | Legal fibrous cavity fill |
| Corkboard (medium $\rho$, 30 °C) | $170$ | $1850$ | $0.040$ | $1.27\times 10^{-7}$ | $112$ | High-strength base insulator |
| Stagnant air (27 °C, $1\,\mathrm{atm}$) | $1.176$ | $1007$ | $0.02623$ | $2.213\times 10^{-5}$ | $5.57$ | Optimal $10\text{--}12\text{ mm}$ foil air gap |

## One-Dimensional Geometries, Composite Networks & Thermal Bridges

### [DERIVATION: Algebra-Only (`5.d.iv` Compliant) Derivation of Cylindrical and Spherical Shell Resistances  **[S06,S12]**]

For radial steady-state conduction without internal heat generation across a spherical shell ($A(r) = 4\pi r^2$) or cylindrical shell ($A(r) = 2\pi r \ell$), energy conservation requires the total radial heat transfer rate $\dot{Q}$ $[W]$ crossing any radius $r \in [r_i, r_o]$ to be independent of $r$.
- **Spherical Shell via Discrete Concentric Sub-Shells:** Subdivide $[r_i, r_o]$ into $N$ thin concentric shells with radii $r_0 = r_i < r_1 < \dots < r_N = r_o$. For a thin shell $m$ of thickness $\Delta r_m = r_m - r_{m-1}$ and geometric-mean surface area $A_{\mathrm{gm},m} = 4\pi r_{m-1}r_m$, the plane-slab resistance is $\Delta R_m = \frac{r_m - r_{m-1}}{4\pi k r_{m-1}r_m} = \frac{1}{4\pi k}\!\left(\frac{1}{r_{m-1}} - \frac{1}{r_m}\right)$. Summing the $N$ series shells telescopes algebraically without calculus:
  
$$
\begin{aligned}
R_{\mathrm{sph}} = \sum_{m=1}^N \Delta R_m = \frac{1}{4\pi k}\sum_{m=1}^N \left(\frac{1}{r_{m-1}} - \frac{1}{r_m}\right) = \frac{1}{4\pi k}\!\left(\frac{1}{r_i} - \frac{1}{r_o}\right) = \frac{r_o - r_i}{4\pi k r_i r_o} = \frac{L}{k A_{\mathrm{gm}}}
    
\end{aligned}
$$

  where $L = r_o - r_i$ and $A_{\mathrm{gm}} = \sqrt{A_i A_o} = 4\pi r_i r_o$ is the exact **geometric mean** of inner and outer surface areas.
- **Cylindrical Shell via Log-Mean Area ($A_{\mathrm{lm}}$):** Subdivide $[r_i, r_o]$ into $N$ geometric ratio shells with $r_m / r_{m-1} = (r_o/r_i)^{1/N} = 1 + \epsilon$. Each thin shell has $\Delta r_m / r_m \approx \epsilon = \frac{1}{N}\ln(r_o/r_i)$, so summing $N$ series shells yields Lienhard Eq. (2.22)  **[S12]**:
  
$$
\begin{aligned}
R_{\mathrm{cyl}} = \frac{\ln(r_o / r_i)}{2\pi k \ell} = \frac{r_o - r_i}{k A_{\mathrm{lm}}}, \qquad A_{\mathrm{lm}} = \frac{A_o - A_i}{\ln(A_o / A_i)} = \frac{2\pi\ell(r_o - r_i)}{\ln(r_o / r_i)}
    
\end{aligned}
$$

  When the wall is thin ($\delta = r_o - r_i \ll r_i$), the algebraic series $\ln(1 + \delta/r_i) \approx \frac{\delta}{r_i} - \frac{\delta^2}{2r_i^2}$ reduces Eq. Eq. (`eq:10:rcyl`) directly to the flat-slab formula $R_{\mathrm{cyl}} \approx \frac{\delta}{k (2\pi r_m \ell)}$ with arithmetic mean radius $r_m = (r_i + r_o)/2$ (error $<1\%$ for $r_o/r_i < 1.2$).

### Series–Parallel Composite Walls, Wiener Bounds and Fastener Thermal Bridges

When heat flows through a composite structure containing both series layers and parallel paths (such as wood studs or metal screws penetrating an insulation wall, shown in Fig. `fig:10:composite-wall`):
- **Series Layers (1-D Isothermal Planes $\perp$ Heat Flow):** Every layer carries the same heat flow $\dot{Q}$. For $n$ plane layers of thicknesses $L_i$ and conductivities $k_i$ exposed to fluid temperatures $T_{\infty,\mathrm{in}}$ (with $h_{\mathrm{in}}$) and $T_{\infty,\mathrm{out}}$ (with $h_{\mathrm{out}}$):
  
$$
\begin{aligned}
R_{\mathrm{tot,ser}} = \frac{1}{h_{\mathrm{in}}A} + \sum_{i=1}^n \frac{L_i}{k_i A} + \sum R_{c,i} + \frac{1}{h_{\mathrm{out}}A}, \qquad k_{\mathrm{eff,ser}} = \frac{\sum_{i=1}^n L_i}{\sum_{i=1}^n (L_i / k_i)} \quad \text{(Weighted Harmonic Mean)}
    
\end{aligned}
$$

  The interface temperature $T_m$ after resistance $R_m$ is found by the voltage-divider ratio:
  
$$
\begin{aligned}
T_m = T_{\infty,\mathrm{in}} - \dot{Q}\!\left(R_{\mathrm{in}} + \sum_{i=1}^m R_i\right) = T_{\infty,\mathrm{in}} - \left(T_{\infty,\mathrm{in}} - T_{\infty,\mathrm{out}}\right)\frac{R_{\mathrm{in}} + \sum_{i=1}^m R_i}{R_{\mathrm{tot,ser}}}
    
\end{aligned}
$$
- **Parallel Paths / Thermal Bridges (Heat Flow $\parallel$ Layer Interfaces):** Parallel paths of cross-sectional areas $A_j$ and thickness $L$ share the same temperature drop $\Delta T$, so thermal conductances $G_j = 1/R_j = k_j A_j / L$ add directly:
  
$$
\begin{aligned}
\frac{1}{R_{\mathrm{tot,par}}} = \sum_{j=1}^m \frac{1}{R_j} = \frac{1}{L}\sum_{j=1}^m k_j A_j, \qquad k_{\mathrm{eff,par}} = \frac{\sum_{j=1}^m k_j A_j}{\sum_{j=1}^m A_j} \quad \text{(Area-Weighted Arithmetic Mean)}
    
\end{aligned}
$$

  By the Cauchy–Schwarz inequality, for any heterogeneous composite with volume fractions $f_j = A_j/A_{\mathrm{tot}}$, the true 3-D effective conductivity is bounded by the **Wiener bounds**: $k_{\mathrm{eff,ser}} \le k_{\mathrm{eff,3D}} \le k_{\mathrm{eff,par}}$. Because $k_{\mathrm{steel}} / k_{\mathrm{cork}} = 54.0 / 0.040 = 1350$, a steel screw occupying just $0.17%$ of a wall's area conducts **$2.26\times$ more heat than the remaining $99.83%$ of cork insulation combined**!

> **[Vector Figure: Series–parallel composite wall with interfacial contact resistance $R_c = 1/(h_c A)$ and a high-conductivity fastener thermal bridge $R_{2b}$ in parallel with insulation $R_{2a}$, paired with its exact thermal resistance circuit  **[S12]**. | Label: `fig:10:composite-wall`]**
> - **Diagram Annotations & Key Elements:** (a) Physical Composite Wall with Fastener Bridge • Layer 1: Cork / [-1pt]$L_1, k_1$ • Layer 2a: Insulation / ($A_{2a}, L_2, k_{2a}$ low) • 2b: Bolt/Stud Bridge / [-1pt]($A_{2b}, L_2, k_{2b} \gg k_{2a}$) • Layer 3: Shell / [-1pt]$L_3, k_3$ • $R_c = \frac{1}{h_c A}$ • (b) Equivalent Series–Parallel Thermal Resistance Circuit • $R_{\mathrm{in}}$ • $R_1=\frac{L_1}{k_1 A}$ • $R_c=\frac{1}{h_c A}$ • $R_{2a} = \frac{L_2}{k_{2a}A_{2a}}$ • $R_{2b} = \frac{L_2}{k_{2b}A_{2b}}$ • $\dot{Q}_{\mathrm{bridge}} = \frac{\Delta T_2}{R_{2b}} \gg \dot{Q}_{\mathrm{ins}}$ • $R_3$ • $R_{\mathrm{out}}$ • $\dot{Q}_{\mathrm{tot}} = \dfrac{T_{\infty,\mathrm{in}} - T_{\infty,\mathrm{out}}}{R_{\mathrm{in}} + R_1 + R_c + \left(R_{2a}^{-1} + R_{2b}^{-1}\right)^{-1} + R_3 + R_{\mathrm{out}}} = U A \left(T_{\infty,\mathrm{in}} - T_{\infty,\mathrm{out}}\right)$

## Interfacial Contact Resistance & Critical Radius of Insulation

### Interfacial Contact Conductance ($h_c$)

Even optically smooth solid surfaces touch only at discrete microscopic asperities ($1\text{--}2\%$ of nominal area $A$ under moderate pressure); the remaining $98\text{--}99\%$ gap is filled with trapped air ($k_{\mathrm{air}} = 0.0262 W/m/K$) or vacuum. Heat crosses the interface by parallel solid-spot constriction conduction and interstitial fluid conduction, producing a discrete temperature jump $\Delta T_c = T_{1^-} - T_{1^+} = \dot{Q} R_c = \dot{Q}/(h_c A)$  **[S12]**. Table `tab:10:contact-hc` compiles verified contact conductances $h_c$ from Lienhard Table 2.1 (p. 76  **[S12]**):

**Table:** Verified Interfacial Contact Conductances $h_c$ and Unit-Area Contact Resistances $R_c'' = 1/h_c$ for Normal Surface Finishes at Moderate Contact Pressure ($1\text{--}10\ \text{atm}$ unless noted; Lienhard Table 2.1, p. 76  **[S12]**).

| **Contacting Interface Pair & Interstitial Condition** | **$h_c$ $(W/m^2/K)$** | **$R_c'' = 1/h_c$ $(m^2 K/W)$** | **Physical & Device Implication** |
| --- | --- | --- | --- |
| Iron / aluminum ($70\ \text{atm}$ high contact pressure, air) | $45\,000$ | $2.22\times 10^{-5}$ | Plastic deformation flattens asperities at high $P$ |
| Copper / copper ($1\text{--}10\ \text{atm}$, air interstices) | $10\,000\text{--}25\,000$ | $(0.40\text{--}1.00)\times 10^{-4}$ | Soft ductile metal yields low contact resistance |
| Aluminum / aluminum ($1\text{--}10\ \text{atm}$, air interstices) | $2200\text{--}12\,000$ | $(0.83\text{--}4.55)\times 10^{-4}$ | Native $\mathrm{Al_2O_3}$ film adds constriction resistance |
| Graphite / metals ($1\text{--}10\ \text{atm}$, air interstices) | $3000\text{--}6000$ | $(1.67\text{--}3.33)\times 10^{-4}$ | Conformable dry thermal interface pad |
| Stainless steel / stainless steel ($1\text{--}10\ \text{atm}$, air) | $2000\text{--}3700$ | $(2.70\text{--}5.00)\times 10^{-4}$ | Hard asperities; negligible only if slab $L \gg 3 mm$ |
| Ceramic / metals ($1\text{--}10\ \text{atm}$, air interstices) | $1500\text{--}8500$ | $(1.18\text{--}6.67)\times 10^{-4}$ | Ceramic heater / metal heat-sink interface |
| Ceramic / ceramic ($1\text{--}10\ \text{atm}$, air interstices) | $500\text{--}3000$ | $(0.33\text{--}2.00)\times 10^{-3}$ | Brittle point contacts with wide air pockets |
| Stainless steel / stainless steel (evacuated interstices) | $200\text{--}1100$ | $(0.91\text{--}5.00)\times 10^{-3}$ | Removing interstitial gas drops $h_c$ by $3\text{--}10\times$! |
| Aluminum / aluminum (low pressure, evacuated interstices) | $100\text{--}400$ | $(0.25\text{--}1.00)\times 10^{-2}$ | Vacuum multi-layer insulation (MLI) contact blocker |
| Unclamped plastic cup on knife-edge balsa/cork cradle ($\sim 0.01\ \text{atm}$) | $15\text{--}50$ | $(2.0\text{--}6.7)\times 10^{-2}$ | 2027 cup cradle: tiny contact $A_c < 0.25 cm^2$ blocks leak! |

### Critical Radius of Insulation ($r_{\mathrm{crit}}$) — Theory and 2027 9 oz Cup Immunity

When a cylinder of outer solid radius $r_i$ (at temperature $T_i$) is wrapped with an insulation layer of conductivity $k_{\mathrm{ins}}$ up to outer radius $r_o$ exposed to ambient air at $T_\infty$ with combined convection + radiation coefficient $h_{\mathrm{ext}} = h_{\mathrm{conv}} + h_{\mathrm{rad}}$, the total thermal resistance is:

$$
\begin{aligned}
R_{\mathrm{tot,cyl}}(r_o) = R_{\mathrm{cond}}(r_o) + R_{\mathrm{conv}}(r_o) = \frac{\ln(r_o / r_i)}{2\pi k_{\mathrm{ins}} \ell} + \frac{1}{2\pi r_o \ell h_{\mathrm{ext}}}
  
\end{aligned}
$$

Increasing $r_o$ **increases** $R_{\mathrm{cond}}$ logarithmically, but **decreases** $R_{\mathrm{conv}}$ as $1/r_o$ because the outer heat-loss surface area $2\pi r_o \ell$ expands! Setting the rate of change of $R_{\mathrm{tot,cyl}}(r_o)$ with respect to $r_o$ to zero ($\frac{1}{r_o k_{\mathrm{ins}}} - \frac{1}{r_o^2 h_{\mathrm{ext}}} = 0$, Lienhard Example 2.6 & Eq. 2.27, p. 70  **[S12]**) gives the exact **critical radius of insulation** where $R_{\mathrm{tot}}$ is a **minimum** and heat loss $\dot{Q}$ is a **maximum**:

$$
\begin{aligned}
\boxed{r_{\mathrm{crit,cyl}} = \frac{k_{\mathrm{ins}}}{h_{\mathrm{ext}}} \quad (\mathrm{Bi}_{r_{\mathrm{crit}}} = 1), \qquad r_{\mathrm{crit,sph}} = \frac{2k_{\mathrm{ins}}}{h_{\mathrm{ext}}} \quad (\mathrm{Bi}_{r_{\mathrm{crit}}} = 2)}
  
\end{aligned}
$$
- **Case 1 ($r_i < r_{\mathrm{crit}}$ — Thin Wire / Capillary Paradox):** Adding insulation initially **increases** heat dissipation until $r_o = r_{\mathrm{crit}}$ (useful for cooling current-carrying electrical wires!), and does not reduce heat loss below the bare-tube value until $r_o > r_{\mathrm{cross}}$ where $R_{\mathrm{tot}}(r_{\mathrm{cross}}) = R_{\mathrm{tot}}(r_i)$ (plotted in Fig. `fig:10:cylindrical-rcrit`).
- **Case 2 ($r_i > r_{\mathrm{crit}}$ — 2027 9 oz Cup & Standard Pipes):** For the ES-provided 9 oz party cup ($r_i \approx 30–37.5 mm$) surrounded by compliant insulation ($k_{\mathrm{ins}} \approx 0.040 W/m/K$) in room air ($h_{\mathrm{ext}} \approx 10 W/m^2/K$), $r_{\mathrm{crit}} = \frac{0.040}{10} = 0.0040 m = 4.0 mm$. Because $r_i = 37.5 mm = 9.4\,r_{\mathrm{crit}} \gg r_{\mathrm{crit}}$, we are far to the right of the minimum in Fig. `fig:10:cylindrical-rcrit`: **every millimeter of insulation added around the 9 oz cup monotonically increases $R_{\mathrm{tot}}$ and reduces heat loss!**

> **[Vector Figure: Total cylindrical thermal resistance $R_{\mathrm{tot}}(r_o) = R_{\mathrm{cond}} + R_{\mathrm{conv}}$ versus radius ratio $r_o/r_i$ for Lienhard Example 2.6  **[S12]**. When $r_i < r_{\mathrm{crit}} = k/h$, resistance passes through a minimum at $r_o = r_{\mathrm{crit}}$ ($\mathrm{Bi}=1$) before crossing the bare-pipe resistance at $r_o/r_i = 2.323$. | Label: `fig:10:cylindrical-rcrit`]**
> - **Diagram Annotations & Key Elements:** **X-Axis:** Normalized Outer Insulation Radius $r_o / r_i$ (Lienhard Example 2.6: $r_i = 2.5 mm,\; k = 0.074 W/m/K,\; h = 20 W/m^2/K$) • **Y-Axis:** Thermal Resistance $R_t$ $(K/W/m)$ • **Legend:** $R_{\mathrm{cond}}(r_o) = \dfrac{\ln(r_o/r_i)}{2\pi k \ell}$ • **Legend:** $R_{\mathrm{conv}}(r_o) = \dfrac{1}{2\pi r_o \ell h}$ • **Legend:** $R_{\mathrm{tot}}(r_o) = R_{\mathrm{cond}} + R_{\mathrm{conv}}$ • **2027 9 oz Cup Regime:** / $r_{\mathrm{cup}}=37.5 mm \gg r_{\mathrm{crit}}=4.0 mm$ / ($\mathrm{Bi}_{\mathrm{cup}} \approx 9.4 > 1 \implies$ insulation / always increases $R_{\mathrm{tot}}$!)

## Extended Surfaces (Fins) & Experimental Conductivity Determination

### Algebraic Fin Design Equations (When Convection Limits Heat Transfer)

When $R_{\mathrm{conv}} = 1/(hA)$ is much larger than internal solid conduction resistance, extended surfaces (**fins**) of cross-sectional area $A_c$, perimeter $P$, length $L$, and conductivity $k$ are attached to a base at excess temperature $\theta_b = T_b - T_\infty$ (Lienhard §4.5, pp. 177–196  **[S12]**). Define the **fin parameter** $m$ $[/m]$ and corrected tip length $L_c = L + A_c/P$ ($L_c = L + t/2$ for a rectangular plate fin of thickness $t$; $L_c = L + D/4$ for a cylindrical pin fin of diameter $D$):

$$
\begin{aligned}
m = \sqrt{\frac{h P}{k A_c}}, \qquad m L_c = \sqrt{\mathrm{Bi}_{\mathrm{fin}}}\,\frac{L_c}{\sqrt{A_c/P}}, \qquad \dot{Q}_{\mathrm{fin}} = \sqrt{h P k A_c}\,\theta_b \tanh(m L_c) = \eta_f h A_f \theta_b
  
\end{aligned}
$$
- **Fin Efficiency ($\eta_f$) and Overall Finned-Array Efficiency ($\eta_o$):**
  
$$
\begin{aligned}
\eta_f = \frac{\dot{Q}_{\mathrm{fin}}}{h A_f \theta_b} = \frac{\tanh(m L_c)}{m L_c} \in (0, 1], \qquad \eta_o = 1 - \frac{A_{\mathrm{fins}}}{A_{\mathrm{total}}}\left(1 - \eta_f\right), \qquad R_{\mathrm{th,array}} = \frac{1}{\eta_o h A_{\mathrm{total}}}
    
\end{aligned}
$$
- **Fin Effectiveness ($\varepsilon_f$):** Ratio of fin heat transfer rate to the heat transfer rate from the bare footprint area $A_c$ without the fin:
  
$$
\begin{aligned}
\varepsilon_f = \frac{\dot{Q}_{\mathrm{fin}}}{h A_c \theta_b} = \sqrt{\frac{k P}{h A_c}}\,\tanh(m L_c) \xrightarrow{m L_c \gtrsim 2.65\ (\text{long fin})} \varepsilon_{f,\infty} = \sqrt{\frac{k P}{h A_c}}
    
\end{aligned}
$$

  **Engineering Rules:** (1) Practical fins require $\varepsilon_f \ge 2$ ($k P \ge 4 h A_c$); (2) place fins on the **low-$h$ gas side**, never on a boiling/condensing side where $h$ is huge; (3) choose thin, closely spaced high-$k$ copper/aluminum fins to maximize perimeter-to-area ratio $P/A_c = 2/t$; (4) beyond $mL_c \approx 2.65$, $\tanh(mL_c) > 0.99$, so making a fin longer adds mass without adding heat transfer!

### Experimental Determination of Thermal Conductivity ($k$)
- **Symmetrical Guarded Hot-Plate Apparatus (ASTM C177 — Standard for Low-$k$ Insulators):** An electrical main heater of area $A$ dissipating measured DC power $P_{\mathrm{elec}} = V I$ is sandwiched symmetrically between two identical flat specimen slabs of thickness $L$, backed by water-cooled cold plates at $T_c$. A coplanar concentric **guard ring heater** around the main heater's perimeter is servo-controlled to the exact main-heater temperature $T_h$ ($T_{\mathrm{guard}} - T_h = 0$), forcing zero radial edge heat leak! Because half of $P_{\mathrm{elec}}$ flows through each identical specimen slab:
  
$$
\begin{aligned}
\dot{Q}_{\mathrm{one\,slab}} = \frac{P_{\mathrm{elec}}}{2} = \frac{V I}{2} \implies k = \frac{(V I / 2)\,L}{A\,(T_h - T_c)} = \frac{V I L}{2 A \Delta T}
    
\end{aligned}
$$
- **Comparative Cut-Bar Method (Axial Series Stack):** An unknown disk of thickness $L_x$ and conductivity $k_x$ is clamped in series between two calibrated reference cylinders of known conductivity $k_{\mathrm{ref}}$ and thickness $L_{\mathrm{ref}}$ inside an insulated guard shell. By series heat-flux continuity ($q''_{\mathrm{ref}} = q''_x$):
  
$$
\begin{aligned}
k_{\mathrm{ref}}\frac{\Delta T_{\mathrm{ref}}}{L_{\mathrm{ref}}} = k_x \frac{\Delta T_x}{L_x} \implies k_x = k_{\mathrm{ref}}\,\frac{L_x}{L_{\mathrm{ref}}}\,\frac{\Delta T_{\mathrm{ref}}}{\Delta T_x}
    
\end{aligned}
$$
- **Searle's Bar Method (High-$k$ Metal Rod with Flowing Water Calorimeter):** One end of an insulated metal bar (area $A$, thermocouple spacing $L$, temperatures $T_1, T_2$) is steam-heated while the cold end is cooled by steady water flow $\dot{m}_w$ warming from $T_{w,\mathrm{in}}$ to $T_{w,\mathrm{out}}$:
  
$$
\begin{aligned}
\dot{Q} = \dot{m}_w c_{p,w}\left(T_{w,\mathrm{out}} - T_{w,\mathrm{in}}\right) = k A \frac{T_1 - T_2}{L} \implies k = \frac{\dot{m}_w c_{p,w}(T_{w,\mathrm{out}} - T_{w,\mathrm{in}}) L}{A(T_1 - T_2)}
    
\end{aligned}
$$

### Multi-Dimensional Conduction Shape Factors ($S$) & Temperature-Dependent Conductivity $k(T)$

When steady conduction occurs through two- or three-dimensional geometries (such as a buried spherical/cylindrical tank or the 12 edges and 8 corners of a thick-walled cubic collector enclosure), the total heat flow between isothermal surfaces $T_1$ and $T_2$ is expressed via the **conduction shape factor** $S$ $[m]$ (Lienhard §5.7 Table 5.4, p. 242  **[S12]**):

$$
\begin{aligned}
\dot{Q} = S k \left(T_1 - T_2\right), \qquad R_{\mathrm{th,3D}} = \frac{1}{S k} \quad [K/W]
  
\end{aligned}
$$
- **Langmuir / Lienhard 3-D Thick-Walled Box Shape Factor (Walls + 12 Edges + 8 Corners):** For a closed rectangular box of uniform wall thickness $L_w \le a_{\mathrm{in}}/5$ with inner surface area $A_{\mathrm{in}}$ and 12 inner edge lengths $\ell_{\mathrm{edge},k}$:
  
$$
\begin{aligned}
S_{\mathrm{box,3D}} = \underbrace{\frac{A_{\mathrm{in}}}{L_w}}_{\text{6 plane walls}} + \underbrace{0.54\sum_{k=1}^{12} \ell_{\mathrm{edge},k}}_{\text{12 edges }(>13%\text{ boost!})} + \underbrace{0.15\times 8\,L_w}_{\text{8 corners}}
    
\end{aligned}
$$
- **Canonical Buried & Concentric Shape Factors (Lienhard Table 5.4, p. 242  **[S12]**):**
- *Isothermal sphere of radius $r$ buried at depth $z$ below an isothermal ground plane:* $S = \dfrac{4\pi r}{1 - r/(2z)} \xrightarrow{z \to \infty} 4\pi r$ ($\mathrm{Nu}_D \to 2$).
- *Horizontal cylinder of radius $r$ and length $\ell \gg r$ buried at depth $z$:* $S = \dfrac{2\pi\ell}{\operatorname{arccosh}(z/r)} \approx \dfrac{2\pi\ell}{\ln(2z/r)}$ (for $z > 3r$).
- *Concentric spheres of radii $r_i, r_o$:* $S = \dfrac{4\pi r_i r_o}{r_o - r_i}$; *Concentric cylinders of length $\ell$:* $S = \dfrac{2\pi\ell}{\ln(r_o/r_i)}$.
- **Temperature-Dependent Thermal Conductivity $k(T)$ (Kirchhoff Transform & Mean-Conductivity Theorem):** When $k(T)$ varies with temperature across $[T_2, T_1]$, separating variables in $\dot{Q} = -k(T)A\,\frac{dT}{dx}$ shows that $\dot{Q}$ equals the exact conduction rate computed with the **integral-average thermal conductivity** $\bar{k}$:
  
$$
\begin{aligned}
\dot{Q} = \frac{A}{L}\int_{T_2}^{T_1} k(T)\,dT = \bar{k}\,\frac{A(T_1 - T_2)}{L}, \qquad \text{For linear } k(T) = k_0\left[1 + \beta_k(T - T_0)\right]:\quad \bar{k} = k\!\left(\frac{T_1 + T_2}{2}\right)
    
\end{aligned}
$$

**Table:** Temperature Dependence of Metallic Thermal Conductivities $k(T)$ $[W/m/K]$ from $-170 °C$ to $800 °C$ (Lienhard Table A.1, pp. 739–740  **[S12]**).

| **Metal / Alloy** | **$-170 °C$** | **$-100 °C$** | **$0 °C$** | **$20 °C$** | **$100 °C$** | **$200 °C$** | **$400 °C$** | **$600 °C$** | **Trend $dk/dT$ & Mechanism** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Aluminum (pure) | $302$ | $242$ | $236$ | $237$ | $240$ | $238$ | $228$ | $215$ | Flat plateau $0–200 °C$ |
| Aluminum 6061-T6 | — | — | $166$ | $167$ | $172$ | $177$ | $180^*$ | — | Alloy: $k$ rises slightly with $T$ ($^*$300 °C) |
| Copper (pure) | $483$ | $420$ | $401$ | $398$ | $391$ | $389$ | $378$ | $366$ | Decreases slowly ($\beta_k \approx -2.3×10^{-4} /K$) |
| Brass ($70\mathrm{Cu}$–$30\mathrm{Zn}$) | $73$ | $89$ | $106$ | $109$ | $133$ | $143$ | $147$ | — | Strong positive slope ($+24\%$ by $100 °C$) |
| Iron (pure) | $132$ | $98$ | $84$ | $80$ | $72$ | $63$ | $50$ | $39$ | Phonon+magnon scattering drops $k$ |
| Carbon steel ($0.5\%\ \mathrm{C}$) | — | — | $55$ | $54$ | $52$ | $48$ | $42$ | $35$ | Monotonic decrease with $T$ |
| Stainless AISI 304 | — | — | $13.8$ | $13.8$ | $15.0$ | $17.2$ | $21.0$ | $25.0$ | Austenitic alloy: $k$ increases $+81\%$! |
| Silver ($99.99+\%$ pure) | $449$ | $431$ | $428$ | $427$ | $422$ | $417$ | $401$ | $386$ | Highest metallic $k$ across all $T$ |
| Tungsten (filament) | $235$ | $223$ | $182$ | $178$ | $166$ | $153$ | $134$ | $125$ | Drops to $\sim105 W/m/K$ at $2400 K$ |

## Worked Competition Examples (§10)

### Worked Example — Multi-Layer Collector Wall & Interface Temperature Profiling `[2027 Device Cradle / Regional–National]`

A flat side panel of a 2027 heat-collector enclosure has cross-sectional area $A = 0.0400 m^2$ and separates warm internal cavity air at $T_{\infty,\mathrm{in}} = 46.0 °C$ ($h_{\mathrm{in}} = 12.0 W/m^2/K$) from room air at $T_{\infty,\mathrm{out}} = 21.0 °C$ ($h_{\mathrm{out}} = 8.00 W/m^2/K$). From inside to outside, the wall consists of: (1) a corkboard liner ($L_1 = 4.00 mm,\; k_1 = 0.0400 W/m/K$), (2) a stagnant foil-bounded dead-air gap ($L_2 = 10.0 mm,\; k_{\mathrm{eff},2} = 0.0275 W/m/K$), and (3) an outer fluted corrugated cardboard shell ($L_3 = 4.00 mm,\; k_3 = 0.0550 W/m/K$). Find (a) the total thermal resistance $R_{\mathrm{tot}}$ and overall heat transfer coefficient $U$, (b) the steady heat loss $\dot{Q}$, and (c) the temperature $T_{12}$ at the cork–air gap interface.
\tcblower
**Solution.** All 5 thermal resistances act in series across $A = 0.0400 m^2$:

$$
\begin{aligned}
R_{\mathrm{in}} &= \frac{1}{h_{\mathrm{in}}A} = \frac{1}{(12.0)(0.0400)} = 2.0833 K/W, &
  R_1 &= \frac{L_1}{k_1 A} = \frac{0.00400}{(0.0400)(0.0400)} = 2.5000 K/W \\
  R_2 &= \frac{L_2}{k_{\mathrm{eff},2}A} = \frac{0.0100}{(0.0275)(0.0400)} = 9.0909 K/W, &
  R_3 &= \frac{L_3}{k_3 A} = \frac{0.00400}{(0.0550)(0.0400)} = 1.8182 K/W \\
  R_{\mathrm{out}} &= \frac{1}{h_{\mathrm{out}}A} = \frac{1}{(8.00)(0.0400)} = 3.1250 K/W
\end{aligned}
$$

(a) Summing in series: $R_{\mathrm{tot}} = 2.0833 + 2.5000 + 9.0909 + 1.8182 + 3.1250 = \mathbf{18.617 K/W}$, and $U = \frac{1}{R_{\mathrm{tot}}A} = \frac{1}{(18.6174)(0.0400)} = \mathbf{1.343 W/m^2/K}$ ($R_{\mathrm{val,tot}} = 1/U = 0.7447 m^2 K/W$).\\
(b) Steady heat transfer rate: $\dot{Q} = \dfrac{T_{\infty,\mathrm{in}} - T_{\infty,\mathrm{out}}}{R_{\mathrm{tot}}} = \dfrac{46.0 - 21.0}{18.6174} = \mathbf{1.343 W}$.\\
(c) By Eq. Eq. (`eq:10:node-temp`), the cork–air gap interface temperature is:

$$
T_{12} = T_{\infty,\mathrm{in}} - \dot{Q}\left(R_{\mathrm{in}} + R_1\right) = 46.0 - (1.34283)(2.0833 + 2.5000) = 46.0 - 6.1546 = \mathbf{39.85 °C}
$$

**✓ Verified by:** Independent $5\times 5$ nodal temperature matrix solve in `check_sec10_13.py` (`EX-10.1-Q`, `EX-10.1-T12`): $\dot{Q} = 1.34283 W$, $T_{12} = 39.8454 °C$ ($\text{rel\_err} = 0.00$).

### Worked Example — Fastener Thermal Bridge Short-Circuit in an Insulated Box `[Parallel Resistance Trap]`

A cork insulation wall of total area $A_{\mathrm{tot}} = 0.0300 m^2$ and thickness $L = 15.0 mm$ ($k_{\mathrm{cork}} = 0.0400 W/m/K$) is fastened using four carbon-steel M4 bolts (each of diameter $d = 4.00 mm$, $k_{\mathrm{steel}} = 54.0 W/m/K$) passing completely through the $15.0 mm$ thickness. Compare the wall's pure-cork thermal resistance $R_{\mathrm{pure}}$ against its actual parallel thermal resistance $R_{\mathrm{eq}}$ with the 4 bolts, and find the percentage of heat that leaks through the bolts.
\tcblower
**Solution.** Pure cork resistance: $R_{\mathrm{pure}} = \dfrac{L}{k_{\mathrm{cork}}A_{\mathrm{tot}}} = \dfrac{0.0150}{(0.0400)(0.0300)} = \mathbf{12.50 K/W}$.\\
With 4 bolts, total bolt cross-sectional area is $A_{\mathrm{bolts}} = 4\left(\frac{\pi}{4}d^2\right) = \pi(0.00400 m)^2 = 5.0265×10^{-5} m^2$ (just $0.1676%$ of $A_{\mathrm{tot}}$!), leaving $A_{\mathrm{cork}} = 0.0300 - 0.00005027 = 0.029950 m^2$. The parallel conductances $G = 1/R = kA/L$ are:

$$
G_{\mathrm{cork}} = \frac{(0.0400)(0.029950)}{0.0150} = 0.07987 W/K, \qquad
  G_{\mathrm{bolts}} = \frac{(54.0)(5.0265×10^{-5})}{0.0150} = 0.18096 W/K
$$

$$
R_{\mathrm{eq}} = \frac{1}{G_{\mathrm{cork}} + G_{\mathrm{bolts}}} = \frac{1}{0.07987 + 0.18096} = \frac{1}{0.26082} = \mathbf{3.834 K/W}, \qquad
  f_{\mathrm{bolts}} = \frac{G_{\mathrm{bolts}}}{G_{\mathrm{tot}}} = \frac{0.18096}{0.26082} = \mathbf{69.38%}
$$

Four tiny steel screws occupying $0.17%$ of the wall area destroy $69.3%$ of the wall's thermal resistance! Replacing steel bolts with balsa dowels ($k = 0.050 W/m/K$) or glue keeps $R_{\mathrm{eq}} = 12.49 K/W$.

**✓ Verified by:** Parallel conductance sum in `check_sec10_13.py` (`EX-10.2-R-STEEL`, `EX-10.2-FRAC`): $R_{\mathrm{eq}} = 3.83404 K/W$, $f_{\mathrm{bolts}} = 0.69379$.

### Worked Example — Interfacial Contact Resistance Between Pressed Stainless Steel Plates `[Lienhard Ex. 2.9 Extension  **[S12]**]`

Two AISI 304 stainless steel plates, each of thickness $L = 15.0 mm$, area $A = 0.0200 m^2$, and conductivity $k = 15.0 W/m/K$, are pressed together in air with interfacial contact conductance $h_c = 2500 W/m^2/K$ (Table `tab:10:contact-hc`). An overall temperature drop $\Delta T_{\mathrm{tot}} = 40.0 K$ is maintained across the outer faces. Find the steady heat transfer rate $\dot{Q}$ and the interfacial temperature jump $\Delta T_c$.
\tcblower
**Solution.** Each stainless plate has bulk conductive resistance $R_{\mathrm{plate}} = \frac{L}{kA} = \frac{0.0150}{(15.0)(0.0200)} = 0.0500 K/W$. The contact interface adds series resistance $R_c = \frac{1}{h_c A} = \frac{1}{(2500)(0.0200)} = 0.0200 K/W$:

$$
R_{\mathrm{tot}} = 2 R_{\mathrm{plate}} + R_c = 2(0.0500) + 0.0200 = 0.1200 K/W \implies
  \dot{Q} = \frac{\Delta T_{\mathrm{tot}}}{R_{\mathrm{tot}}} = \frac{40.0}{0.1200} = \mathbf{333.3 W}
$$

The temperature jump across the microscopic contact plane is $\Delta T_c = \dot{Q} R_c = (333.33)(0.0200) = \mathbf{6.67 K}$ ($16.7%$ of $\Delta T_{\mathrm{tot}}$).

**✓ Verified by:** Series resistance check in `check_sec10_13.py` (`EX-10.3-Q`, `EX-10.3-DT-INT`): $\dot{Q} = 333.333 W$, $\Delta T_c = 6.6667 K$.

### Worked Example — Critical Radius of Insulation & Crossover Radius vs. 9 oz Cup Cradle `[Lienhard Ex. 2.6  **[S12]**]`

A small tube of outer diameter $D_i = 5.00 mm$ ($r_i = 2.50 mm$) is insulated with $85\%$ magnesia ($k = 0.0740 W/m/K$) in ambient air with $h_{\mathrm{ext}} = 20.0 W/m^2/K$ (Fig. `fig:10:cylindrical-rcrit`). Find (a) the critical radius $r_{\mathrm{crit}}$ and minimum total resistance per unit length, (b) the crossover outer radius $r_{\mathrm{cross}}$ required before insulation begins reducing heat loss below the bare tube, and (c) compare against the 2027 9 oz cup ($r_{\mathrm{cup}} = 37.5 mm,\; k_{\mathrm{cork}} = 0.040 W/m/K,\; h_{\mathrm{ext}} = 10.0 W/m^2/K$).
\tcblower
**Solution.** (a) By Eq. Eq. (`eq:10:rcrit-boxed`), $r_{\mathrm{crit}} = \frac{k}{h_{\mathrm{ext}}} = \frac{0.0740}{20.0} = \mathbf{3.70 mm}$ ($r_{\mathrm{crit}}/r_i = 1.480$). For $\ell = 1.00 m$, the bare tube resistance is $R_{\mathrm{bare}} = \frac{1}{2\pi r_i \ell h_{\mathrm{ext}}} = \frac{1}{2\pi(0.00250)(1.00)(20.0)} = \mathbf{3.183 K/W}$, whereas at $r_o = r_{\mathrm{crit}} = 3.70 mm$, $R_{\min} = \frac{\ln(1.480)}{2\pi(0.0740)} + \frac{1}{2\pi(0.00370)(20.0)} = 0.8432 + 2.1508 = \mathbf{2.994 K/W}$ ($6.3%$ higher heat loss than bare!).\\
(b) Setting $R_{\mathrm{tot}}(r_{\mathrm{cross}}) = R_{\mathrm{bare}} = 3.1831 K/W$ gives $2.15076\ln(r_{\mathrm{cross}}/r_i) + \frac{3.18310}{r_{\mathrm{cross}}/r_i} = 3.18310 \implies \frac{r_{\mathrm{cross}}}{r_i} = \mathbf{2.323}$, so $r_{\mathrm{cross}} = \mathbf{5.81 mm}$.\\
(c) For the 2027 9 oz cup: $r_{\mathrm{crit,cup}} = \frac{0.040}{10.0} = 4.00 mm \ll r_{\mathrm{cup}} = 37.5 mm$ ($r_{\mathrm{cup}}/r_{\mathrm{crit}} = 9.375$), so adding cork/foil insulation around the cup **always reduces heat loss**.

**✓ Verified by:** Brent root-finding in `check_sec10_13.py` (`EX-10.4-RCRIT`): $r_{\mathrm{cross}}/r_i = 2.32321$ ($r_{\mathrm{cross}} = 5.808 mm$).

### Worked Example — Spherical Shell Conduction & Geometric-Mean Area $A_{\mathrm{gm}}$ `[All Levels]`

A spherical vessel of inner radius $r_i = 8.00 cm$ and outer radius $r_o = 12.0 cm$ is insulated with cork ($k = 0.0400 W/m/K$). If the inner wall is at $T_i = 80.0 °C$ and the outer wall is at $T_o = 20.0 °C$, calculate the steady heat loss $\dot{Q}$ and verify using the geometric-mean area $A_{\mathrm{gm}} = \sqrt{A_i A_o}$.
\tcblower
**Solution.** Using Eq. Eq. (`eq:10:rsph`):

$$
R_{\mathrm{sph}} = \frac{r_o - r_i}{4\pi k r_i r_o} = \frac{0.120 - 0.080}{4\pi(0.0400)(0.080)(0.120)} = 8.2893 K/W \implies
  \dot{Q} = \frac{80.0 - 20.0}{8.2893} = \mathbf{7.238 W}
$$

**✓ Verified by:** Geometric-mean area check in `check_sec10_13.py` (`EX-10.5-SPH`): $A_i = 0.080425 m^2$, $A_o = 0.180956 m^2$, $A_{\mathrm{gm}} = \sqrt{A_i A_o} = 0.120637 m^2 \implies \dot{Q} = k A_{\mathrm{gm}}\Delta T/(r_o - r_i) = 7.23823 W$.

### Worked Example — Wiedemann–Franz Law: Electronic vs. Alloy Thermal Conductivity `[2027 Cornell Invitational E1  **[S25]**]`

At $T = 20.0 °C$ ($293.15 K$), pure copper has electrical resistivity $\rho_{e,\mathrm{Cu}} = 1.68×10^{-8} Ω m$, while structural aluminum alloy 6061-T6 has $\rho_{e,\mathrm{6061}} = 3.99×10^{-8} Ω m$. Using the Sommerfeld Lorenz number $L_0 = \frac{\pi^2}{3}(k_B/e)^2 = 2.443×10^{-8} W Ω/K^2$, compute the theoretical free-electron thermal conductivity $k_e$ of each metal and compare against experimental values ($k_{\mathrm{Cu}} = 398 W/m/K$, $k_{\mathrm{6061}} = 167 W/m/K$, Table `tab:10:k-hierarchy`).
\tcblower
**Solution.** Applying Eq. Eq. (`eq:10:wiedemann-franz`), $k_e = L_0 T / \rho_e$:

$$
k_{e,\mathrm{Cu}} = \frac{(2.4430×10^{-8} W Ω/K^2)(293.15 K)}{1.68×10^{-8} Ω m} = \mathbf{426.3 W/m/K}, \qquad
  k_{e,\mathrm{6061}} = \frac{(2.4430×10^{-8})(293.15)}{3.99×10^{-8}} = \mathbf{179.5 W/m/K}
$$

Both predictions agree with experiment within $\sim 7%$ (at room temperature, inelastic electron–phonon scattering slightly reduces the effective Lorenz ratio below $L_0$ to $L_{\mathrm{eff}} \approx 2.28×10^{-8} W Ω/K^2$).

**✓ Verified by:** Exact CODATA evaluation in `check_sec10_13.py` (`EX-10.6-WF-CU`, `EX-10.6-WF-6061`): $k_{e,\mathrm{Cu}} = 426.29 W/m/K$, $k_{e,\mathrm{6061}} = 179.49 W/m/K$.

### Worked Example — Guarded Hot-Plate Experimental Determination of Cork Conductivity `[Lab & Data Analysis]`

In a symmetrical ASTM C177 guarded hot-plate test, two identical corkboard disks of thickness $L = 12.0 mm$ and metered main-heater area $A = 0.0250 m^2$ sandwich a central DC heater powered at $V = 12.00 V$ and $I = 0.350 A$. When the guard ring is balanced ($T_{\mathrm{guard}} = T_h$), steady plate temperatures are $T_h = 54.5 °C$ and $T_c = 29.3 °C$. Calculate $k_{\mathrm{cork}}$ and state the error if the student forgets the factor of $1/2$ for bidirectional heat split.
\tcblower
**Solution.** Total electrical heater power is $P_{\mathrm{elec}} = V I = (12.00)(0.350) = 4.200 W$. Because heat exits symmetrically through both cork specimens, each slab carries $\dot{Q}_1 = P_{\mathrm{elec}}/2 = 2.100 W$ across $\Delta T = 54.5 - 29.3 = 25.2 K$:

$$
k_{\mathrm{cork}} = \frac{\dot{Q}_1 L}{A \Delta T} = \frac{(2.100)(0.0120)}{(0.0250)(25.2)} = \frac{0.0252}{0.630} = \mathbf{0.0400 W/m/K}
$$

**If you got $0.0800 W/m/K$,** you used full $P_{\mathrm{elec}} = 4.20 W$ instead of $P_{\mathrm{elec}}/2 = 2.10 W$ for a two-sided symmetrical guarded hot plate!

**✓ Verified by:** Checked in `check_sec10_13.py` (`EX-10.7-GHP`): $k = 0.0400 W/m/K$, matching Lienhard Table A.2 p. 742  **[S12]**.

### Worked Example — 3-D Shape-Factor Conduction Loss of a Cubic Collector Box (Walls + Edges + Corners) `[Lienhard §5.7  **[S12]**]`

A closed cubic test enclosure of outer side $a_{\mathrm{out}} = 30.0 cm$ ($0.300 m$) and uniform wall thickness $L_w = 3.00 cm$ ($0.0300 m$, inner side $a_{\mathrm{in}} = a_{\mathrm{out}} - 2L_w = 0.240 m$) is constructed of corkboard ($k = 0.0400 W/m/K$). When the inner wall surfaces are at $T_1 = 45.0 °C$ and the outer wall surfaces are at $T_2 = 21.0 °C$ ($\Delta T = 24.0 K$), calculate (a) the naive 1-D plane-wall heat loss based on the inner surface area $A_{\mathrm{in}} = 6 a_{\mathrm{in}}^2$, and (b) the true 3-D heat loss $\dot{Q}_{\mathrm{3D}}$ including all 12 edges and 8 corners via Eq. Eq. (`eq:10:langmuir-box`).
\tcblower
**Solution.** (a) The 6 inner faces have area $A_{\mathrm{in}} = 6(0.240)^2 = 0.3456 m^2$, giving $S_{\mathrm{1D}} = \frac{A_{\mathrm{in}}}{L_w} = \frac{0.3456}{0.0300} = 11.520 m$ and naive 1-D loss $\dot{Q}_{\mathrm{1D}} = S_{\mathrm{1D}}k\Delta T = (11.520)(0.0400)(24.0) = \mathbf{11.06 W}$.\\
(b) Including the 12 inner edges (each of length $\ell_{\mathrm{edge}} = 0.240 m$) and 8 three-dimensional corners via Eq. Eq. (`eq:10:langmuir-box`):

$$
S_{\mathrm{edges}} = 0.54\left(12 \times 0.240 m\right) = 1.5552 m, \qquad
  S_{\mathrm{corners}} = 0.15\left(8 \times 0.0300 m\right) = 0.0360 m
$$

$$
S_{\mathrm{box,3D}} = 11.520 + 1.5552 + 0.0360 = \mathbf{13.1112 m} \implies
  \dot{Q}_{\mathrm{3D}} = (13.1112)(0.0400)(24.0) = \mathbf{12.59 W}
$$

Edge and corner 3-D flaring increases conductive heat leak by $+13.8%$ ($+1.53 W$) over the naive inner-area formula!

**✓ Verified by:** Checked in `check_sec10_13.py` (`EX-10.8-3DBOX`): $S_{\mathrm{box,3D}} = 13.1112 m$, $\dot{Q}_{\mathrm{3D}} = 12.5868 W$.

### Worked Example — Pin-Fin Efficiency $\eta_f$ and Fin Effectiveness $\varepsilon_f$ `[Lienhard §4.5  **[S12]**]`

A cylindrical aluminum alloy 6061-T6 pin fin ($k = 167 W/m/K$) of diameter $D = 4.00 mm$ and protruding length $L = 30.0 mm$ is attached to a base at $T_b = 65.0 °C$ in forced air at $T_\infty = 25.0 °C$ ($\theta_b = 40.0 K$) with $h = 25.0 W/m^2/K$. Compute (a) the fin parameter $m$ and corrected length $L_c = L + D/4$, (b) the fin efficiency $\eta_f$, (c) the heat dissipation rate $\dot{Q}_{\mathrm{fin}}$, and (d) the fin effectiveness $\varepsilon_f$.
\tcblower
**Solution.** Cross-sectional area is $A_c = \frac{\pi}{4}(0.00400 m)^2 = 1.2566×10^{-5} m^2$ and perimeter is $P = \pi(0.00400 m) = 1.2566×10^{-2} m$ ($P/A_c = 4/D = 1000 /m$).\\
(a) Corrected tip length: $L_c = 30.0 + 4.00/4 = 31.0 mm = 0.0310 m$. Fin parameter:

$$
m = \sqrt{\frac{h P}{k A_c}} = \sqrt{\frac{(25.0)(1000)}{167}} = \mathbf{12.235 /m} \implies m L_c = (12.235)(0.0310) = \mathbf{0.3793}
$$

(b) Fin efficiency: $\eta_f = \dfrac{\tanh(0.37929)}{0.37929} = \dfrac{0.36210}{0.37929} = \mathbf{0.9547}$ ($95.5%$).\\
(c) Total effective fin surface area is $A_f = P L_c = (1.2566×10^{-2})(0.0310) = 3.8956×10^{-4} m^2$, so:

$$
\dot{Q}_{\mathrm{fin}} = \eta_f h A_f \theta_b = (0.95465)(25.0)(3.8956×10^{-4})(40.0) = \mathbf{0.3719 W}
$$

(d) Without the fin, the bare base footprint $A_c$ dissipates $\dot{Q}_{\mathrm{base}} = h A_c \theta_b = (25.0)(1.2566×10^{-5})(40.0) = 0.012566 W$, giving effectiveness $\varepsilon_f = \dfrac{\dot{Q}_{\mathrm{fin}}}{\dot{Q}_{\mathrm{base}}} = \dfrac{0.3719}{0.012566} = \mathbf{29.59 \gg 2}$.

**✓ Verified by:** Checked in `check_sec10_13.py` (`EX-10.9-FIN-ETA`, `EX-10.9-FIN-EPS`): $\eta_f = 0.95465$, $\varepsilon_f = 29.594$.

### Worked Example — Comparative Cut-Bar Identification of an Unknown Structural Alloy `[Experimental Metrology]`

In an insulated comparative cut-bar stack, an unknown aluminum alloy cylinder of length $L_x = 30.0 mm$ is placed in axial series with a calibrated $70$–$30$ brass reference cylinder ($k_{\mathrm{ref}} = 109.0 W/m/K$, length $L_{\mathrm{ref}} = 25.0 mm$) of identical diameter. At steady state, thermocouples record axial temperature drops $\Delta T_{\mathrm{ref}} = 18.40 K$ across the brass reference and $\Delta T_x = 14.41 K$ across the unknown specimen. Determine $k_x$ and identify the alloy from Table `tab:10:k-hierarchy`.
\tcblower
**Solution.** By Eq. Eq. (`eq:10:comparative-bar`), series heat-flux continuity $q''_{\mathrm{ref}} = q''_x$ gives:

$$
k_x = k_{\mathrm{ref}}\,\frac{L_x}{L_{\mathrm{ref}}}\,\frac{\Delta T_{\mathrm{ref}}}{\Delta T_x} = (109.0)\!\left(\frac{30.0}{25.0}\right)\!\left(\frac{18.40}{14.4115}\right) = \mathbf{167.0 W/m/K} \longrightarrow **Aluminum Alloy 6061-T6**
$$

**✓ Verified by:** Checked in `check_sec10_13.py` (`EX-10.10-CUTBAR`): $k_x = 167.00 W/m/K$.

## Conduction Traps, Diagnostics & 2027 Collector Cradle Engineering

### [TRAP & DIAGNOSTIC: Top Conduction & Thermal Resistance Traps on Science Olympiad Exams]

| **Wrong move / Symptom** | **What it produces / Why it fails** | **5-second diagnostic & fix** |
| --- | --- | --- |
| **1. Using total wall area $A_{\mathrm{tot}}$ inside parallel branch $R_j = L/(k_j A_j)$** | Gives completely wrong parallel conductance; each parallel path $j$ MUST use its own cross-sectional area $A_j$ ($\sum A_j = A_{\mathrm{tot}}$). | Check $\sum f_j = 1$ in $k_{\mathrm{eff,par}} = \sum f_j k_j$. |
| **2. Adding parallel resistances ($R_1 + R_2$) instead of conductances ($1/R_1 + 1/R_2$)** | Predicts that a metal bolt *increases* resistance instead of short-circuiting it! | $R_{\mathrm{eq,par}} = \frac{R_1 R_2}{R_1 + R_2}$ is ALWAYS smaller than $\min(R_1, R_2)$. |
| **3. Confusing US Imperial $R$-value ($\text{ft}^2\cdot^\circ\text{F}\cdot\text{h/BTU}$) with SI $R_{\mathrm{val}}$ ($m^2 K/W$)** | Off by a factor of $5.6783\times$ (e.g., fiberglass R-13 in US units is $R_{\mathrm{SI}} = 13 / 5.6783 = 2.29 m^2 K/W$). | Convert first: $R_{\mathrm{SI}} = 0.17611 \times R_{\mathrm{US}}$. |
| **4. Using flat-slab $R = (r_o - r_i)/(2\pi r_i \ell k)$ on a thick cylindrical wall ($r_o/r_i > 1.2$)** | Overestimates area (if using $r_o$) or underestimates area (if using $r_i$). | Always use $\ln(r_o/r_i)/(2\pi k \ell)$ (log-mean area $A_{\mathrm{lm}}$). |
| **5. Forgetting the factor of $1/2$ in a symmetrical guarded hot-plate apparatus** | Doubles the calculated thermal conductivity $k$. | Check whether the heater is sandwiched between two identical slabs ($\dot{Q}_{\mathrm{slab}} = V I / 2$). |
| **6. Confusing thermal conductivity $k$ with thermal diffusivity $\alpha = k/(\rho c_p)$** | Stagnant air has very low $k = 0.0262 W/m/K$, yet its thermal diffusivity $\alpha_{\mathrm{air}} = 2.21×10^{-5} m^2/s$ is **$150\times$ larger than liquid water's** ($1.47×10^{-7} m^2/s$) because $\rho_{\mathrm{air}}$ is tiny! | Steady flux uses $k$; transient penetration $\delta_t \sim 2\sqrt{\alpha t}$ uses $\alpha$. |

### [2027 HEAT-COLLECTOR DEVICE & LAB: 2027 Heat-Lamp Collector Conduction & Cup-Cradle Playbook  **[S01,S02,S12]**]

- **Three-Point Knife-Edge Cup Seat ($\dot{Q}_{\mathrm{base}} < 0.02 W$):** Never rest the 9 oz cup flat on a solid table or thick wooden floor ($A_{\mathrm{base}} \approx 22 cm^2$ conducts heat downward into the cold floor). Support the cup base on **three radial balsa or cork knife-edge fins** ($k = 0.04–0.05 W/m/K$, contact footprint $A_c < 0.25 cm^2$, height $L = 35 mm$): $R_{\mathrm{support}} = \frac{0.035}{(0.045)(2.5×10^{-5})} = 31100 K/W$, reducing conductive base heat loss to $<0.001 W$!
- **Why Wrapping Black Paper Around the Outside of the Clear Cup Fails:** Matte black construction paper has low thermal conductivity ($k = 0.14 W/m/K$) and poor contact conductance ($h_c \approx 30 W/m^2/K$) against the tapered plastic cup wall. Wrapping black paper around the clear cup **blocks direct near-IR radiation from passing through the transparent cup wall into the water**, while dissipating absorbed heat outward to the air! Instead, surround the cup with a non-contact specular aluminum-foil cavity ($\varepsilon = 0.04$) or a foil-thin ($\le35 µm$) high-$k$ copper/aluminum sleeve backed by concentric $10 mm$ foil-air-foil insulation rings.
- **Rule `3.e` Zero-Water-Contact Constraint:** Although metallic fins have high fin efficiency $\eta_f$, **Rule `3.e` strictly prohibits any part of the device from contacting the water**  **[S01]**. All conductive/radiative collection elements must remain outside the cup or in the dry upper air space above the $100 mL$ waterline ($\ge15 mm$ clearance).

## Rapid Competition Problem & Solution Bank (§10)

#### Problem P10.1: Conduction + Phase Change (Stefan Ice-Layer Growth) `[§10.2 | 5.c.ii, 5.c.iii | National / Invitational | 90 s | Algebra + Energy Balance | Trap: forgetting average thickness $L/2$ or using water $k$ instead of ice $k$]`

A calm freshwater lake is at uniform temperature $T_w = 0.00 °C$ when cold winter air suddenly drops the upper ice surface temperature to a constant $T_{\mathrm{air}} = -15.0 °C$ ($\Delta T = 15.0 K$). Ice Ih has thermal conductivity $k_{\mathrm{ice}} = 2.215 W/m/K$ (Table `tab:10:k-hierarchy`), density $\rho_{\mathrm{ice}} = 917.0 kg/m^3$, and latent heat of fusion $L_f = 333.5 kJ/kg$  **[S11,S12]**. Neglecting sensible subcooling of the ice ($c_p\Delta T \ll L_f$), derive the algebraic Stefan law for ice thickness $y(t)$ at time $t$ by equating conductive heat flux across average thickness to latent heat release, and compute the time required to freeze an ice sheet from $y_1 = 2.00 cm$ to $y_2 = 8.00 cm$.

**Solution P10.1:** 
When the ice layer has thickness $y$ and grows by thickness $\Delta y$ over area $A$, the latent heat released at the $y$ interface ($0 °C$) is $\Delta Q = \rho_{\mathrm{ice}} A L_f\,\Delta y$, which must be conducted upward through the ice layer to the $-15.0 °C$ top surface at rate $\dot{Q} = k_{\mathrm{ice}} A \Delta T / y$. Writing $\rho_{\mathrm{ice}} L_f \frac{\Delta y}{\Delta t} = \frac{k_{\mathrm{ice}}\Delta T}{y_{\mathrm{avg}}}$ where the arithmetic mean thickness between $y_1$ and $y_2$ is $y_{\mathrm{avg}} = \frac{y_1 + y_2}{2}$ gives $y_{\mathrm{avg}}(y_2 - y_1) = \frac{1}{2}(y_2^2 - y_1^2) = \frac{k_{\mathrm{ice}}\Delta T}{\rho_{\mathrm{ice}} L_f}\,\Delta t$:

$$
\Delta t = \frac{\rho_{\mathrm{ice}} L_f \left(y_2^2 - y_1^2\right)}{2 k_{\mathrm{ice}} \Delta T} = \frac{(917.0)(3.335×10^{5} J/kg)\left(0.0800^2 - 0.0200^2\right)}{2(2.215)(15.0)} = \frac{1.8349×10^{6}}{66.45} = \mathbf{27613 s} = \mathbf{7.670 h}
$$

*Quick Check:* Notice $t \propto y^2$: growing from $0 cm$ to $8 cm$ takes $16\times$ as long as growing from $0 cm$ to $2 cm$, so the increment from $2$ to $8 cm$ takes $16 - 1 = 15$ units of the first $2 cm$ freeze time ($1840.9 s \times 15 = 27613 s$).

#### Problem P10.2: Series-Parallel Wiener Bounds & Anisotropic Laminate `[§10.2 | 5.c.iii | State / National | 75 s | Harmonic vs. Arithmetic Mean | Trap: swapping series and parallel conductivity formulas]`

A composite heat-spreader laminate is made by alternating $50$ thin sheets of pure copper ($k_{\mathrm{Cu}} = 398 W/m/K$, thickness $t_{\mathrm{Cu}} = 0.200 mm$) with $50$ thin sheets of polyimide film ($k_{\mathrm{PI}} = 0.350 W/m/K$, thickness $t_{\mathrm{PI}} = 0.100 mm$, Lienhard Table A.2 p. 743  **[S12]**). Assuming perfect bonding ($R_c \to 0$), calculate (a) the in-plane thermal conductivity $k_{\parallel}$ (heat flow parallel to the sheets), (b) the through-thickness thermal conductivity $k_{\perp}$ (heat flow perpendicular to the sheets), and (c) the anisotropy ratio $k_{\parallel} / k_{\perp}$.

**Solution P10.2:** 
Volume fractions are $f_{\mathrm{Cu}} = \frac{0.200}{0.200 + 0.100} = \frac{2}{3}$ and $f_{\mathrm{PI}} = \frac{0.100}{0.300} = \frac{1}{3}$.
- **(a)** **In-Plane (Parallel Paths, Eq. `eq:10:parallel-keff`):** $k_{\parallel} = f_{\mathrm{Cu}} k_{\mathrm{Cu}} + f_{\mathrm{PI}} k_{\mathrm{PI}} = \frac{2}{3}(398) + \frac{1}{3}(0.350) = 265.33 + 0.12 = \mathbf{265.5 W/m/K}$.
- **(b)** **Through-Thickness (Series Layers, Eq. `eq:10:series-keff`):** $k_{\perp} = \left(\frac{f_{\mathrm{Cu}}}{k_{\mathrm{Cu}}} + \frac{f_{\mathrm{PI}}}{k_{\mathrm{PI}}}\right)^{-1} = \left(\frac{2/3}{398} + \frac{1/3}{0.350}\right)^{-1} = \left(0.001675 + 0.952381\right)^{-1} = \mathbf{1.048 W/m/K}$.
- **(c)** **Anisotropy Ratio:** $\dfrac{k_{\parallel}}{k_{\perp}} = \dfrac{265.45}{1.0482} = \mathbf{253.3}$. (In-plane heat spreading is dominated by copper; through-plane insulation is dominated by polyimide!).

#### Problem P10.3: Spherical vs. Cylindrical Critical Radius Paradox `[§10.3 | 5.c.iii | Regional / State | 60 s | Direct Ratio | Trap: forgetting factor of 2 in spherical $r_{\mathrm{crit}} = 2k/h$]`

A small spherical thermistor bead of bare diameter $D_i = 2.00 mm$ ($r_i = 1.00 mm$) is coated with an epoxy shell of thermal conductivity $k_{\mathrm{ep}} = 0.220 W/m/K$ (Lienhard Table A.2 p. 743  **[S12]**) and placed in an airflow with $h_{\mathrm{ext}} = 110 W/m^2/K$. (a) Find the outer epoxy radius $r_{\mathrm{crit,sph}}$ that maximizes heat transfer from the bead. (b) At $r_o = r_{\mathrm{crit,sph}}$, by what percentage does the heat dissipation rate exceed that of the bare $1.00 mm$-radius bead?

**Solution P10.3:** 
(a) For a sphere (Eq. `eq:10:rcrit-boxed`), $r_{\mathrm{crit,sph}} = \dfrac{2 k_{\mathrm{ep}}}{h_{\mathrm{ext}}} = \dfrac{2(0.220)}{110} = 0.00400 m = \mathbf{4.00 mm}$ ($r_{\mathrm{crit}}/r_i = 4.00$).\\
(b) Bare sphere resistance is $R_{\mathrm{bare}} = \dfrac{1}{4\pi r_i^2 h_{\mathrm{ext}}} = \dfrac{1}{4\pi(0.00100)^2(110)} = \mathbf{723.43 K/W}$. At $r_o = r_{\mathrm{crit,sph}} = 4.00 mm$:

$$
R_{\min} = \frac{r_o - r_i}{4\pi k_{\mathrm{ep}} r_i r_o} + \frac{1}{4\pi r_o^2 h_{\mathrm{ext}}} = \frac{0.00300}{4\pi(0.220)(0.00100)(0.00400)} + \frac{723.43}{16} = 271.29 + 45.21 = \mathbf{316.50 K/W}
$$

Heat transfer increases by $\dfrac{\dot{Q}_{\max}}{\dot{Q}_{\mathrm{bare}}} = \dfrac{R_{\mathrm{bare}}}{R_{\min}} = \dfrac{723.43}{316.50} = 2.2857 \implies \mathbf{+128.6%}$!

#### Problem P10.4: Searle's Bar Calorimetric Conductivity Measurement `[§10.4 | 5.c.iii | All Levels | 75 s | Energy Balance | Trap: forgetting radius-to-area $\pi r^2$ or gram-to-kg conversion]`

In a Searle's bar experiment, a well-insulated cylindrical brass rod of diameter $D = 3.00 cm$ has two thermocouples spaced $L = 15.0 cm$ apart along its length reading $T_1 = 92.0 °C$ and $T_2 = 34.0 °C$. Cooling water flows through the cold-end copper coil at steady mass flow rate $\dot{m}_w = 1.45 g/s$ ($c_{p,w} = 4.184 J/g/K$), entering at $T_{w,\mathrm{in}} = 18.20 °C$ and exiting at $T_{w,\mathrm{out}} = 22.85 °C$. Calculate the measured thermal conductivity $k$ of the brass rod.

**Solution P10.4:** 
Cross-sectional area of the rod is $A = \frac{\pi}{4}(0.0300 m)^2 = 7.0686×10^{-4} m^2$. Steady heat rate absorbed by the cooling water is:

$$
\dot{Q} = \dot{m}_w c_{p,w}\left(T_{w,\mathrm{out}} - T_{w,\mathrm{in}}\right) = (1.45 g/s)(4.184 J/g/K)(22.85 - 18.20) = \mathbf{28.211 W}
$$

By Eq. Eq. (`eq:10:searles-bar`), $k = \dfrac{\dot{Q} L}{A(T_1 - T_2)} = \dfrac{(28.211)(0.150)}{(7.0686×10^{-4})(92.0 - 34.0)} = \dfrac{4.2316}{0.04100} = \mathbf{103.2 W/m/K}$ (matching $70$–$30$ brass at $0 °C$–$20 °C$, Table `tab:10:k-vs-temp`).

#### Problem P10.5: Temperature-Dependent Conductivity $k(T) = k_0(1 + \beta_k T)$ in a Refractory Wall `[§10.4 | 5.c.iii | National / Cornell E1 | 75 s | Mean-Conductivity Theorem | Trap: evaluating $k$ at only one boundary instead of $T_m$]`

An insulating firebrick wall of thickness $L = 0.200 m$ and area $A = 1.50 m^2$ has thermal conductivity that varies linearly with temperature as $k(T) = 0.100 + 1.25×10^{-4}\,T$ $[W/m/K]$, where $T$ is in $^\circ\mathrm{C}$ (Lienhard Table A.2 p. 741  **[S12]**). If the inner furnace face is held at $T_1 = 900.0 °C$ and the outer face is at $T_2 = 100.0 °C$, calculate (a) the steady heat transfer rate $\dot{Q}$, and (b) the exact temperature $T_{\mathrm{mid}}$ at the geometric midplane $x = L/2 = 0.100 m$.

**Solution P10.5:** 
(a) By Eq. Eq. (`eq:10:kt-average`), for linear $k(T)$ the integral average $\bar{k}$ equals $k(T_m)$ at the arithmetic mean temperature $T_m = \frac{1}{2}(900.0 + 100.0) = 500.0 °C$:

$$
\bar{k} = 0.100 + (1.25×10^{-4})(500.0) = \mathbf{0.1625 W/m/K} \implies
  \dot{Q} = \bar{k}\,\frac{A(T_1 - T_2)}{L} = \frac{(0.1625)(1.50)(800.0)}{0.200} = \mathbf{975.0 W}
$$

(b) At the midplane $x = L/2$, half of the integrated conductivity potential has elapsed: $\int_{T_{\mathrm{mid}}}^{T_1} k(T)\,dT = \int_{T_2}^{T_{\mathrm{mid}}} k(T)\,dT$. Since $k(T)$ increases with $T$, the hotter half ($x < L/2$) has higher conductivity and therefore a *smaller* temperature drop than the colder half! Solving $0.100(T_{\mathrm{mid}} - 100) + \frac{1.25×10^{-4}}{2}(T_{\mathrm{mid}}^2 - 100^2) = \frac{1}{2}(0.1625)(800) = 65.00$ gives $6.25×10^{-5}T_{\mathrm{mid}}^2 + 0.100 T_{\mathrm{mid}} - 75.625 = 0 \implies T_{\mathrm{mid}} = \mathbf{541.5 °C} > 500.0 °C$.

#### Problem P10.6: Coaxial Two-Layer Pipe Insulation & Optimal Layer Ordering `[§10.2 | 5.c.iii | National | 90 s | Logarithmic Radial Area | Trap: putting low-k layer on the outside instead of the inside]`

A hot pipe of outer radius $r_1 = 20.0 mm$ is to be insulated with two concentric $10.0 mm$-thick cylindrical sleeves (so intermediate radius is $r_2 = 30.0 mm$ and outer radius is $r_3 = 40.0 mm$): Material A ($k_A = 0.0250 W/m/K$) and Material B ($k_B = 0.0500 W/m/K$). Should Material A (the better insulator) be placed on the inner shell ($[r_1, r_2]$) or the outer shell ($[r_2, r_3]$) to maximize total thermal resistance, and by what percentage do the two arrangements differ?

**Solution P10.6:** 
In cylindrical or spherical geometry, heat flux $q''(r) = \dot{Q}/(2\pi r \ell)$ is highest at the smallest radius $r_1$, so the **lowest-conductivity material ($k_A$) must ALWAYS be placed on the innermost layer ($[r_1, r_2]$)** where cross-sectional area is smallest and $\ln(r_2/r_1) = \ln(1.50) = 0.40547 > \ln(r_3/r_2) = \ln(4/3) = 0.28768$! For $\ell = 1.00 m$:

$$
\begin{aligned}
R_{\mathrm{A\text{-}inner}} &= \frac{1}{2\pi}\!\left[\frac{\ln(30/20)}{0.0250} + \frac{\ln(40/30)}{0.0500}\right] = \frac{16.2186 + 5.7536}{2\pi} = \mathbf{3.4970 K/W} \\
  R_{\mathrm{B\text{-}inner}} &= \frac{1}{2\pi}\!\left[\frac{\ln(30/20)}{0.0500} + \frac{\ln(40/30)}{0.0250}\right] = \frac{8.1093 + 11.5073}{2\pi} = \mathbf{3.1221 K/W}
\end{aligned}
$$

Placing the superior insulator on the inside increases conductive resistance by $+12.01%$! (In a flat plane wall, order does not change $R_{\mathrm{tot}}$, but in radial geometry inner placement always wins).

**Table:** Conduction Shape Factors $S$ ($\dot{Q} = S k \Delta T$), Internal Volumetric Heating Profiles ($\dot{q}$ $[W/m^3]$), and Porous/Dispersed Composite Conductivity Laws (Lienhard §2.3 & Table 5.4, pp. 62–66, 253  **[S12]**).

| **Geometry / Physical System** | **Exact Closed-Form Expression ($S$, $\Delta T_{\max}$, or $k_{\mathrm{eff}}$)** | **Conditions & Notes** |
| --- | --- | --- |
| Isothermal sphere (radius $r_1$) buried at depth $z$ below isothermal surface | $S = \dfrac{4\pi r_1}{1 - r_1/(2z)} \xrightarrow{z \gg r_1} 4\pi r_1$ | Semi-infinite medium ($k$); exact image-source solution |
| Horizontal cylinder (radius $r_1$, length $\ell$) buried at axis depth $z$ | $S = \dfrac{2\pi \ell}{\operatorname{arcosh}(z/r_1)} \approx \dfrac{2\pi \ell}{\ln(2z/r_1)}$ \quad ($z > 3r_1$) | Requires $\ell \gg r_1$; for $z/r_1 = 5$, $\ln(10) = 2.3026$ |
| Two parallel cylinders (radii $r_1, r_2$, length $\ell$) at center spacing $w$ | $S = \dfrac{2\pi \ell}{\operatorname{arcosh}\!\left(\frac{w^2 - r_1^2 - r_2^2}{2r_1 r_2}\right)} \approx \dfrac{2\pi \ell}{\ln\!\left(\frac{w^2}{r_1 r_2}\right)}$ ($w \gg r_1,r_2$) | Infinite medium ($k$) between $T_1$ and $T_2$ |
| Eccentric circular cylinders (radii $r_1 < r_2$, length $\ell$, axis offset $e$) | $S = \dfrac{2\pi \ell}{\operatorname{arcosh}\!\left(\frac{r_1^2 + r_2^2 - e^2}{2r_1 r_2}\right)}$ | Reduces to $\frac{2\pi\ell}{\ln(r_2/r_1)}$ when concentric ($e = 0$) |
| Conduction from thin circular disk (radius $r_0$) on semi-infinite half-space | $S = 4 r_0$ \quad (isothermal disk on adiabatic surface); $S = 8 r_0$ (deeply buried) | Basis of constriction resistance $R_c = 1/(2 k r_0)$ |
| Uniform volumetric heating $\dot{q}$ $[W/m^3]$ in plane slab ($x \in [-L, +L]$) | $T(x) - T_s = \dfrac{\dot{q} L^2}{2 k}\!\left(1 - \dfrac{x^2}{L^2}\right) \implies \Delta T_{\max} = \dfrac{\dot{q} L^2}{2 k}$ | Symmetrical cooling at $x = \pm L$ (or insulated at $x=0$) |
| Uniform volumetric heating $\dot{q}$ in solid cylinder (outer radius $R$) | $T(r) - T_s = \dfrac{\dot{q} R^2}{4 k}\!\left(1 - \dfrac{r^2}{R^2}\right) \implies \Delta T_{\max} = \dfrac{\dot{q} R^2}{4 k}$ | Surface flux $q''(R) = \frac{\dot{q}(\pi R^2\ell)}{2\pi R\ell} = \frac{\dot{q} R}{2}$ |
| Uniform volumetric heating $\dot{q}$ in solid sphere (outer radius $R$) | $T(r) - T_s = \dfrac{\dot{q} R^2}{6 k}\!\left(1 - \dfrac{r^2}{R^2}\right) \implies \Delta T_{\max} = \dfrac{\dot{q} R^2}{6 k}$ | Ratio of $\Delta T_{\max}$ (slab : cyl : sph) $= \frac{1}{2} : \frac{1}{4} : \frac{1}{6} = \mathbf{6 : 3 : 2}$ |
| Maxwell–Eucken dispersed spheres (matrix $k_m$, dispersed pores/particles $k_p$, volume fraction $\phi$) | $k_{\mathrm{eff}} = k_m\,\dfrac{2k_m + k_p - 2\phi(k_m - k_p)}{2k_m + k_p + \phi(k_m - k_p)} \xrightarrow{k_p \ll k_m} k_m\,\dfrac{2(1-\phi)}{2+\phi}$ | Exact dilute-limit 3-D effective medium between Wiener bounds |

#### Problem P10.7: Internal Volumetric Joule Heating in Slab vs. Cylinder vs. Sphere `[§10.2 | 5.c.iii | National / MIT | 75 s | 1-D Poisson Equation | Trap: using slab divisor $2k$ instead of cylinder $4k$ or sphere $6k$]`

A cylindrical nuclear fuel pin of radius $R = 6.00 mm$ and thermal conductivity $k = 3.00 W/m/K$ generates uniform volumetric thermal power $\dot{q} = 1.50×10^{8} W/m^3$. If the outer cladding interface at $r = R$ is maintained at $T_s = 340.0 °C$, calculate (a) the outgoing surface heat flux $q''(R)$, (b) the centerline temperature $T(0)$, and (c) what the centerline temperature excess $T(0) - T_s$ would be in a sphere of the same radius $R$, conductivity $k$, and volumetric heating $\dot{q}$.

**Solution P10.7:** 
- **(a)** By steady energy conservation on a cylinder of length $\ell$, all heat generated inside radius $R$ crosses the perimeter $2\pi R \ell$:
  
$$
q''(R) = \frac{\dot{q}\left(\pi R^2 \ell\right)}{2\pi R \ell} = \frac{\dot{q} R}{2} = \frac{(1.50×10^{8} W/m^3)(0.00600 m)}{2} = \mathbf{4.50×10^{5} W/m^2} = \mathbf{450.0 kW/m^2}
$$
- **(b)** By Table `tab:10:shape-factors` (cylindrical Poisson equation $\frac{1}{r}\frac{d}{dr}(r\frac{dT}{dr}) = -\frac{\dot{q}}{k}$), the centerline temperature excess is:
  
$$
\Delta T_{\max,\mathrm{cyl}} = T(0) - T_s = \frac{\dot{q} R^2}{4 k} = \frac{(1.50×10^{8})(0.00600)^2}{4(3.00)} = \frac{5400}{12.0} = \mathbf{450.0 K} \implies T(0) = 340.0 + 450.0 = \mathbf{790.0 °C}
$$
- **(c)** In a sphere of radius $R$, the surface-to-volume ratio is $3/R$ instead of $2/R$, so the divisor is $6k$ instead of $4k$: $\Delta T_{\max,\mathrm{sph}} = \dfrac{\dot{q}R^2}{6k} = \dfrac{2}{3}(450.0 K) = \mathbf{300.0 K}$ ($T(0) = 640.0 °C$).

#### Problem P10.8: Buried Hot-Water Pipe Conduction Shape Factor in Soil `[§10.4 | 5.c.iii | State / National | 60 s | Shape Factor $S$ | Trap: using $\ln(z/r)$ instead of $\ln(2z/r)$]`

A district-heating pipe of outer diameter $D = 10.0 cm$ ($r_1 = 0.0500 m$) and length $\ell = 25.0 m$ is buried horizontally with its centerline at depth $z = 0.750 m$ ($z/r_1 = 15.0$) below a soil surface at $T_{\mathrm{soil}} = 8.0 °C$. The soil has thermal conductivity $k_{\mathrm{soil}} = 0.950 W/m/K$ (Table `tab:10:k-hierarchy`) and the pipe outer surface is at $T_p = 78.0 °C$. Calculate the steady conductive heat loss $\dot{Q}$ to the ground surface.

**Solution P10.8:** 
From Table `tab:10:shape-factors`, for a buried horizontal cylinder with $z/r_1 = 15.0 > 3$:

$$
S = \frac{2\pi \ell}{\ln(2z/r_1)} = \frac{2\pi(25.0 m)}{\ln(30.00)} = \frac{157.080}{3.40120} = \mathbf{46.184 m} \implies
  \dot{Q} = S k_{\mathrm{soil}}\left(T_p - T_{\mathrm{soil}}\right) = (46.184)(0.950)(78.0 - 8.0) = \mathbf{3071 W} = \mathbf{3.071 kW}
$$

#### Problem P10.9: Maxwell–Eucken Effective Conductivity of Cellular Cork Insulation `[§10.2 | 5.c.iii | National / Invitational | 75 s | Effective Medium Theory | Trap: using arithmetic parallel average on closed-cell foam]`

Closed-cell natural cork consists of a solid suberin cell-wall matrix ($k_m = 0.190 W/m/K$, volume fraction $1 - \phi = 0.220$) enclosing isolated spherical stagnant-air cells ($k_p = 0.0262 W/m/K$, porosity $\phi = 0.780$). Compare (a) the Wiener series lower bound $k_{\mathrm{ser}}$, (b) the Wiener parallel upper bound $k_{\mathrm{par}}$, and (c) the 3-D Maxwell–Eucken dispersed-pore conductivity $k_{\mathrm{ME}}$ against the measured value $k_{\mathrm{cork}} = 0.045 W/m/K$.

**Solution P10.9:** 
- **(a)** **Wiener Series Lower Bound:** $k_{\mathrm{ser}} = \left(\dfrac{0.220}{0.190} + \dfrac{0.780}{0.0262}\right)^{-1} = (1.1579 + 29.7710)^{-1} = \mathbf{0.0323 W/m/K}$.
- **(b)** **Wiener Parallel Upper Bound:** $k_{\mathrm{par}} = (0.220)(0.190) + (0.780)(0.0262) = 0.04180 + 0.02044 = \mathbf{0.0622 W/m/K}$.
- **(c)** **Maxwell–Eucken 3-D Closed-Cell Formula (Table `tab:10:shape-factors`):**
  
$$
k_{\mathrm{ME}} = (0.190)\,\frac{2(0.190) + 0.0262 - 2(0.780)(0.190 - 0.0262)}{2(0.190) + 0.0262 + (0.780)(0.190 - 0.0262)} = (0.190)\,\frac{0.4062 - 0.25553}{0.4062 + 0.12776} = (0.190)\,\frac{0.15067}{0.53396} = \mathbf{0.0536 W/m/K}
$$

  All three satisfy the rigorous theorem $k_{\mathrm{ser}} (0.0323) < k_{\mathrm{exp}} (0.0450) < k_{\mathrm{ME}} (0.0536) < k_{\mathrm{par}} (0.0622)$!

#### Problem P10.10: 2027 Collector Multi-Wall Conduction Budget & Fastener Bridge Audit `[§10.2 | 3.a–h, 5.c.iii | 2027 Device / All Levels | 75 s | Parallel Conductance Network | Trap: ignoring aluminum corner brackets or floor conduction]`

A team's cubic collector enclosure has outer dimensions $30.0 cm\times30.0 cm\times30.0 cm$ with four vertical sidewalls and a bottom floor made of $35.0 mm$-thick corkboard ($k_{\mathrm{cork}} = 0.0420 W/m/K$, total active conduction area $A_{\mathrm{walls+floor}} = 0.280 m^2$). The inner cavity air is at $T_{\mathrm{cav}} = 53.0 °C$ and the room is at $T_{\mathrm{room}} = 21.0 °C$ ($\Delta T = 32.0 K$). (a) Calculate the steady conductive heat loss $\dot{Q}_{\mathrm{cork}}$ through the corkboard walls and floor. (b) If a student secures the box with $8$ through-wall aluminum machine screws (Alloy 6061-T6, $k_{\mathrm{Al}} = 167 W/m/K$, screw shank diameter $d = 4.00 mm$, length $L = 35.0 mm$), how much extra heat $\dot{Q}_{\mathrm{screws}}$ leaks through the $8$ screws, and what percentage of the total wall conduction do the screws carry?

**Solution P10.10:** 
- **(a)** Through the $35.0 mm$-thick corkboard enclosure ($A_c = 0.280 m^2$):
  
$$
G_{\mathrm{cork}} = \frac{k_{\mathrm{cork}} A_c}{L} = \frac{(0.0420)(0.280)}{0.0350} = \mathbf{0.3360 W/K} \implies
    \dot{Q}_{\mathrm{cork}} = G_{\mathrm{cork}}\Delta T = (0.3360)(32.0) = \mathbf{10.75 W}
$$
- **(b)** Each $4.00 mm$-diameter screw has cross-sectional area $A_1 = \frac{\pi}{4}(0.00400)^2 = 1.2566×10^{-5} m^2$, so all $8$ screws have total area $A_{\mathrm{screws}} = 8 A_1 = 1.0053×10^{-4} m^2$ (just $0.0359%$ of the wall area!):
  
$$
G_{\mathrm{screws}} = \frac{k_{\mathrm{Al}} A_{\mathrm{screws}}}{L} = \frac{(167)(1.0053×10^{-4})}{0.0350} = \mathbf{0.4797 W/K} \implies
    \dot{Q}_{\mathrm{screws}} = (0.4797)(32.0) = \mathbf{15.35 W}
$$

  Eight small screws occupying $0.036%$ of the wall area conduct $\mathbf{15.35 W}$ — **more than the entire corkboard enclosure ($58.8%$ of the combined $26.10 W$ leak)**! Always assemble collector walls with non-metallic PVA wood glue, paper tape, or balsa dowels.

—
**See also:** §`sec:01.9` (`QS-09` Conduction Fast Sheet), §`sec:11` (Convection & Dead-Air Gaps), §`sec:12` (Radiation Shields), §`sec:13` (Transient Lumped Heating & Biot Number), §`sec:14` (Materials Encyclopedia & `#6 PS` Ban), §`sec:15` (2027 Collector Cradle Design).
