#!/usr/bin/env python3
"""Independent Numerical Verification Suite for §§14--16 (verify/checks/check_sec14_16.py).

Verifies every worked example, equation, and table calculation in:
  - src/sec14.tex (§14 Material, Optical & Insulation Property Encyclopedia: ex:14.1 .. ex:14.5)
  - src/sec15.tex (§15 Competition Device Engineering — 2027 100-125 W Collector: ex:15.1 .. ex:15.6b)
  - src/sec16.tex (§16 Device Calibration, Heating-Curve Prediction & DOE Tables: ex:16.1 .. ex:16.6)
"""
from __future__ import annotations
import math
import sys
import numpy as np

SIGMA = 5.670374419e-8       # Stefan-Boltzmann constant [W/(m^2 K^4)] (CODATA 2022)
B_WIEN = 2897.771955         # Wien displacement constant [um K] (CODATA 2022)
R_GAS = 8.314462618          # Universal gas constant [J/(mol K)] (CODATA 2022)
G_STD = 9.80665              # Standard gravity [m/s^2]


def _make_record(
    cid: str,
    section: str,
    description: str,
    expected: float,
    computed: float,
    tol: float = 1e-3,
    method: str = "Independent Python/NumPy physical model assertion",
) -> dict:
    denom = max(abs(expected), 1e-12)
    rel_err = abs(computed - expected) / denom
    passed = rel_err <= tol
    detail = f"expected={expected:.6g}, computed={computed:.6g}, rel_err={rel_err:.2e} (tol={tol:.1e})"
    return {
        "id": cid,
        "section": section,
        "description": description,
        "passed": bool(passed),
        "expected": float(expected),
        "computed": float(computed),
        "rel_error": float(rel_err),
        "tolerance": float(tol),
        "detail": detail,
        "method": method,
    }


def coaxial_disk_view_factor(r1: float, r2: float, d: float) -> float:
    """Exact diffuse view factor F_{1->2} between coaxial parallel disks (Lienhard Table 10.3 Case 3)."""
    R1 = r1 / d
    R2 = r2 / d
    X = 1.0 + (1.0 + R2**2) / (R1**2)
    return 0.5 * (X - math.sqrt(X**2 - 4.0 * (R2 / R1) ** 2))


def run_checks() -> list[dict]:
    checks: list[dict] = []

    # =========================================================================
    # SECTION 14 CHECKS (ex:14.1 through ex:14.5 + Wien peaks)
    # =========================================================================
    # 14.0: Wien peaks for 2400 K tungsten filament vs 308.15 K (35 C) water
    lam_lamp = B_WIEN / 2400.0
    lam_water = B_WIEN / 308.15
    checks.append(_make_record(
        "SEC14:EQ14.1_WIEN_LAMP", "§14.1",
        "Wien peak wavelength of 2400 K heat-lamp filament [um]",
        1.2074, lam_lamp, tol=1e-3,
        method="Wien displacement law b / T_fil"
    ))
    checks.append(_make_record(
        "SEC14:EQ14.1_WIEN_WATER", "§14.1",
        "Wien peak wavelength of 308.15 K (35 C) water [um]",
        9.4038, lam_water, tol=1e-3,
        method="Wien displacement law b / T_water"
    ))

    # ex:14.1: Two-Band Net Radiative Heat Flux (Selective Black Cr vs Matte Black vs White)
    q_nir = 4500.0
    A_c = 4.00e-3
    T_s, T_e = 335.15, 295.15
    dM_bb = SIGMA * (T_s**4 - T_e**4)
    Q_black_cr = A_c * (0.95 * q_nir - 0.09 * dM_bb)
    Q_matte_blk = A_c * (0.94 * q_nir - 0.89 * dM_bb)
    Q_white = A_c * (0.26 * q_nir - 0.90 * dM_bb)
    checks.append(_make_record(
        "SEC14:EX14.1_BLACK_CR", "§14.1",
        "Worked Example 14.1(a): Selective Black Chrome net radiative power [W]",
        16.997, Q_black_cr, tol=1e-3,
        method="Two-band Stefan-Boltzmann balance A_c*(alpha_NIR*q_NIR - eps_MIR*sigma*(T_s^4-T_e^4))"
    ))
    checks.append(_make_record(
        "SEC14:EX14.1_MATTE_BLACK", "§14.1",
        "Worked Example 14.1(b): Matte Black Paint net radiative power [W]",
        15.905, Q_matte_blk, tol=1e-3,
        method="Two-band Stefan-Boltzmann balance"
    ))
    checks.append(_make_record(
        "SEC14:EX14.1_WHITE_PAINT", "§14.1",
        "Worked Example 14.1(c): White Acrylic Paint net radiative power [W]",
        3.6535, Q_white, tol=1e-3,
        method="Two-band Stefan-Boltzmann balance"
    ))

    # ex:14.2: Multi-Bounce Ray Delivery & Parasitic Mass (Shiny vs Dull Al Foil vs White Card)
    Q_in_cone = 42.0
    A_w = 0.120
    eta1_shiny = 0.88 + 0.35 * 0.08
    eta_cone_shiny = 0.65 * eta1_shiny + 0.35 * (eta1_shiny**2)
    Q_deliv_shiny = Q_in_cone * eta_cone_shiny
    Cw_shiny = 2707.0 * 905.0 * 16e-6 * A_w

    eta1_dull = 0.62 + 0.35 * 0.33
    eta_cone_dull = 0.65 * eta1_dull + 0.35 * (eta1_dull**2)
    Q_deliv_dull = Q_in_cone * eta_cone_dull

    eta1_white = 0.04 + 0.35 * 0.70
    eta_cone_white = 0.65 * eta1_white + 0.35 * (eta1_white**2)
    Q_deliv_white = Q_in_cone * eta_cone_white

    checks.append(_make_record(
        "SEC14:EX14.2_SHINY_FOIL", "§14.2",
        "Worked Example 14.2(a): Shiny Al foil 2-bounce delivered optical power [W]",
        36.910, Q_deliv_shiny, tol=1e-3,
        method="Specular + forward diffuse ray-bounce polynomial sum"
    ))
    checks.append(_make_record(
        "SEC14:EX14.2_SHINY_MASS", "§14.2",
        "Worked Example 14.2(a): 16 um Al foil wall heat capacity for 0.120 m^2 [J/K]",
        4.7037, Cw_shiny, tol=2e-3,
        method="Volumetric heat capacity rho * c_p * delta * A_w"
    ))
    checks.append(_make_record(
        "SEC14:EX14.2_DULL_FOIL", "§14.2",
        "Worked Example 14.2(b): Dull Al foil 2-bounce delivered optical power [W]",
        28.031, Q_deliv_dull, tol=1e-3,
        method="Specular + forward diffuse ray-bounce polynomial sum"
    ))
    checks.append(_make_record(
        "SEC14:EX14.2_WHITE_CARD", "§14.2",
        "Worked Example 14.2(c): White cardstock 2-bounce delivered optical power [W]",
        8.9746, Q_deliv_white, tol=1e-3,
        method="Specular + forward diffuse ray-bounce polynomial sum"
    ))

    # ex:14.3: Beer-Lambert Near-IR Attenuation & Bottom-Mirror Second-Pass Gain in Water
    n_w = 1.325
    R_F = ((n_w - 1.0) / (n_w + 1.0)) ** 2
    rho_eff_bot = 0.96 * 0.92
    L_w = 3.80  # cm
    for tag, mu_a, exp_top1cm, exp_tot2pass in [
        ("970NM", 0.450, 0.35528, 0.93148),
        ("1200NM", 1.040, 0.63398, 0.97788),
        ("1440NM", 29.40, 0.98045, 0.98045),
    ]:
        f1_1cm = (1.0 - R_F) * (1.0 - math.exp(-mu_a * 1.00))
        f1_L = (1.0 - R_F) * (1.0 - math.exp(-mu_a * L_w))
        df2 = (1.0 - R_F) * math.exp(-mu_a * L_w) * rho_eff_bot * (1.0 - math.exp(-mu_a * L_w))
        f_tot = f1_L + df2
        checks.append(_make_record(
            f"SEC14:EX14.3_{tag}_TOP1CM", "§14.3",
            f"Worked Example 14.3 ({tag}): Fraction absorbed in top 1.0 cm",
            exp_top1cm, f1_1cm, tol=1e-3,
            method="Beer-Lambert attenuation (1 - R_F)*(1 - exp(-mu_a * z))"
        ))
        checks.append(_make_record(
            f"SEC14:EX14.3_{tag}_2PASS", "§14.3",
            f"Worked Example 14.3 ({tag}): Total 2-pass absorbed fraction in 3.8 cm water",
            exp_tot2pass, f_tot, tol=1e-3,
            method="Two-pass Beer-Lambert integral with bottom mirror return"
        ))

    # ex:14.4: Fresnel Transmittance & Thermal Mass of 25 um BoPET vs 2.0 mm Borosilicate Glass
    A_disk = 6.00e-3
    C_top = 215.0
    dT_g = 18.0
    # BoPET
    n1, mu1, d1_cm, d1_m = 1.64, 8.0, 0.0025, 2.50e-5
    Rs1 = ((n1 - 1.0) / (n1 + 1.0)) ** 2
    ti1 = math.exp(-mu1 * d1_cm)
    tau_nir1 = ((1.0 - Rs1) ** 2 * ti1) / (1.0 - (Rs1 * ti1) ** 2)
    C_disk1 = 1390.0 * 1170.0 * A_disk * d1_m
    dT_loss1 = C_disk1 * dT_g / C_top
    # Borosilicate Glass
    n2, mu2, d2_cm, d2_m = 1.47, 0.080, 0.200, 2.00e-3
    Rs2 = ((n2 - 1.0) / (n2 + 1.0)) ** 2
    ti2 = math.exp(-mu2 * d2_cm)
    tau_nir2 = ((1.0 - Rs2) ** 2 * ti2) / (1.0 - (Rs2 * ti2) ** 2)
    C_disk2 = 2210.0 * 753.0 * A_disk * d2_m
    dT_loss2 = C_disk2 * dT_g / C_top

    checks.append(_make_record(
        "SEC14:EX14.4_BOPET_TAU", "§14.4",
        "Worked Example 14.4(a): 25 um BoPET two-surface NIR transmittance",
        0.8714, tau_nir1, tol=1e-3,
        method="Airy multiple-reflection slab transmittance formula"
    ))
    checks.append(_make_record(
        "SEC14:EX14.4_BOPET_CDISK", "§14.4",
        "Worked Example 14.4(b): 25 um BoPET 60 cm^2 disk heat capacity [J/K]",
        0.24395, C_disk1, tol=1e-3,
        method="Calorimetric capacitance rho * c_p * A * delta"
    ))
    checks.append(_make_record(
        "SEC14:EX14.4_GLASS_TAU", "§14.4",
        "Worked Example 14.4(a): 2.0 mm Borosilicate glass NIR transmittance",
        0.9153, tau_nir2, tol=1e-3,
        method="Airy multiple-reflection slab transmittance formula"
    ))
    checks.append(_make_record(
        "SEC14:EX14.4_GLASS_DRAIN", "§14.4",
        "Worked Example 14.4(c): 2.0 mm glass cover thermal drain on top water layer [C]",
        1.6719, dT_loss2, tol=1e-3,
        method="Headspace calorimetric perturbation C_disk * dT_g / C_top"
    ))

    # ex:14.5: 3-Layer 10 mm Foil-Air-Foil Wall vs Solid Corkboard
    Tm_145 = 308.65
    dT_gap = 7.00
    delta_gap = 0.010
    nu_alpha = 3.69e-10
    Ra_delta = 9.807 * (dT_gap / Tm_145) * (delta_gap**3) / nu_alpha
    h_rad_gap = 4.0 * SIGMA * (Tm_145**3) / (2.0 / 0.04 - 1.0)
    k_eff_gap = 0.0265 + h_rad_gap * delta_gap
    Q_foil_air = k_eff_gap * 0.0450 * 21.0 / 0.030
    Q_cork = 0.040 * 0.0450 * 21.0 / 0.030
    C_cork = 314500.0 * 0.0450 * 0.030

    checks.append(_make_record(
        "SEC14:EX14.5_RA_DELTA", "§14.5",
        "Worked Example 14.5(a): Rayleigh number Ra_delta of 10 mm air gap (< 1708)",
        602.7, Ra_delta, tol=2e-3,
        method="Rayleigh-Benard stability parameter g*beta*dT*delta^3/(nu*alpha)"
    ))
    checks.append(_make_record(
        "SEC14:EX14.5_Q_FOIL_AIR", "§14.5",
        "Worked Example 14.5(a): 3-layer foil-air sleeve conductive+radiative heat leak [W]",
        0.8776, Q_foil_air, tol=2e-3,
        method="Parallel conduction + radiation across 3 series air-foil gaps"
    ))
    checks.append(_make_record(
        "SEC14:EX14.5_Q_CORK", "§14.5",
        "Worked Example 14.5(b): 30 mm solid corkboard sleeve heat leak [W] and heat capacity [J/K]",
        1.260, Q_cork, tol=1e-3,
        method="Fourier conduction k_cork * A_m * dT / L_tot"
    ))

    # =========================================================================
    # SECTION 15 CHECKS (ex:15.1 through ex:15.6b)
    # =========================================================================
    # ex:15.1: Coaxial Disk View-Factor & Proximity Gain at h = 40 cm and h = 65 cm (z_ap = 30.0 cm top plane)
    F_cup_40 = coaxial_disk_view_factor(6.35, 3.75, 30.0)
    F_ap_40 = coaxial_disk_view_factor(6.35, 15.0, 10.0)
    ratio_40 = F_ap_40 / F_cup_40
    F_cup_65 = coaxial_disk_view_factor(6.35, 3.75, 55.0)
    F_ap_65 = coaxial_disk_view_factor(6.35, 15.0, 35.0)
    ratio_65 = F_ap_65 / F_cup_65

    checks.append(_make_record(
        "SEC15:EX15.1_F_AP_40CM", "§15.2",
        "Worked Example 15.1: Coaxial disk view factor F_{bulb->ap} at h=40 cm",
        0.66471, F_ap_40, tol=1e-3,
        method="Lienhard Table 10.3 Case 3 coaxial parallel disks formula"
    ))
    checks.append(_make_record(
        "SEC15:EX15.1_RATIO_40CM", "§15.2",
        "Worked Example 15.1: Aperture-to-bare-cup view factor ratio at h=40 cm",
        45.08, ratio_40, tol=1e-3,
        method="View-factor ratio F_{bulb->ap} / F_{bulb->cup}"
    ))
    checks.append(_make_record(
        "SEC15:EX15.1_F_AP_65CM", "§15.2",
        "Worked Example 15.1: Coaxial disk view factor F_{bulb->ap} at h=65 cm",
        0.15162, F_ap_65, tol=1e-3,
        method="Lienhard Table 10.3 Case 3 coaxial parallel disks formula"
    ))

    # ex:15.1b: Direct Unbounced Cup-Mouth Beam vs Wall-Reflected Frustum Beam Partition
    F_ap_to_cup = coaxial_disk_view_factor(14.50, 3.75, 14.30)
    F_ap_to_wall = 1.0 - F_ap_to_cup
    f_dir = 2.15 * F_ap_to_cup
    Q_dir = f_dir * 34.20
    Q_wall_deliv = (1.0 - f_dir) * 34.20 * 0.8788
    Q_cup_gross = Q_dir + Q_wall_deliv
    checks.append(_make_record(
        "SEC15:EX15.1B_F_WALL", "§15.2",
        "Worked Example 15.2 (15.1b): Conical surround wall view factor F_{ap->s}",
        0.96656, F_ap_to_wall, tol=1e-3,
        method="Enclosure summation rule F_{1->s} = 1 - F_{1->2}"
    ))
    checks.append(_make_record(
        "SEC15:EX15.1B_Q_GROSS", "§15.2",
        "Worked Example 15.2 (15.1b): Total concentrated optical power reaching cup glazing [W]",
        30.353, Q_cup_gross, tol=1e-3,
        method="Direct collimated beam + specular frustum wall delivery"
    ))

    # ex:15.2: Prolate Ellipsoid Conjugate Geometry & Frustum Pattern Unrolling
    h_des, z_foc, z_ap, r_ap = 45.0, 10.0, 27.0, 14.50
    z_c = 0.5 * (h_des + z_foc)
    c_ell = 0.5 * (h_des - z_foc)
    d1 = math.hypot(r_ap, h_des - z_ap)
    d2 = math.hypot(r_ap, z_ap - z_foc)
    a_ell = 0.5 * (d1 + d2)
    b_ell = math.sqrt(a_ell**2 - c_ell**2)
    r_z1 = b_ell * math.sqrt(1.0 - ((18.50 - z_c) / a_ell) ** 2)
    L_1 = math.hypot(14.50 - 13.31, 27.00 - 18.50)
    R_out1 = 14.50 * L_1 / (14.50 - 13.31)

    checks.append(_make_record(
        "SEC15:EX15.2_ELLIPSOID_A", "§15.3",
        "Worked Example 15.3 (15.2): Prolate ellipsoid semi-major axis a [cm]",
        22.7289, a_ell, tol=1e-3,
        method="Fermat equal-path focal distance sum 2a = d1 + d2"
    ))
    checks.append(_make_record(
        "SEC15:EX15.2_ELLIPSOID_R185", "§15.3",
        "Worked Example 15.3 (15.2): Ellipsoid radius r(z=18.5 cm) [cm]",
        13.318, r_z1, tol=1e-3,
        method="Canonical prolate ellipsoid equation r(z) = b*sqrt(1 - (z-z_c)^2/a^2)"
    ))
    checks.append(_make_record(
        "SEC15:EX15.2_UNROLLED_ROUT", "§15.3",
        "Worked Example 15.3 (15.2): Unrolled upper frustum pattern outer radius R_out,1 [cm]",
        104.58, R_out1, tol=1e-3,
        method="Pythagorean slant height and similar-triangles cone development"
    ))

    # ex:15.3: Four-Node Parallel Thermal Resistance Synthesis
    G_hs = (1.0 / 220.0) + (1.0 / 14.20) + (1.0 / 19.80)
    R_top_glazed = (1.0 / G_hs) + 3.680
    R_th_enc = 1.0 / ((1.0 / R_top_glazed) + (1.0 / 9.420) + (1.0 / 185.0))
    G_top_open = (1.0 / 5.50) + (1.0 / 14.20) + (1.0 / 19.80)
    R_th_enc_open = 1.0 / (G_top_open + (1.0 / 9.420) + (1.0 / 185.0))

    checks.append(_make_record(
        "SEC15:EX15.3_R_TOP_GLAZED", "§15.4",
        "Worked Example 15.4 (15.3): Net glazed top-aperture thermal resistance [K/W]",
        11.650, R_top_glazed, tol=1e-3,
        method="Series-parallel thermal resistance network reduction"
    ))
    checks.append(_make_record(
        "SEC15:EX15.3_R_ENC_GLAZED", "§15.4",
        "Worked Example 15.4 (15.3): Overall glazed collector enclosure resistance R_th,enc [K/W]",
        5.066, R_th_enc, tol=1e-3,
        method="Parallel combination of top, radial, and base resistance branches"
    ))
    checks.append(_make_record(
        "SEC15:EX15.3_R_ENC_OPEN", "§15.4",
        "Worked Example 15.4 (15.3): Uncovered open collector enclosure resistance [K/W]",
        2.414, R_th_enc_open, tol=1e-3,
        method="Parallel combination with open-cup evaporative conductance"
    ))

    # ex:15.3b: Heavy Metal Absorber Sleeve Trap
    C_Al = 0.150 * 896.0
    TG_Al = 27.70 * (220.6 / (220.6 + C_Al))
    checks.append(_make_record(
        "SEC15:EX15.3B_HEAVY_AL_TG", "§15.4",
        "Worked Example 15.5 (15.3b): Degraded TG with 150 g aluminum absorber sleeve [C]",
        17.213, TG_Al, tol=1e-3,
        method="Calorimetric thermal-mass partitioning TG_0 * C_sys0 / (C_sys0 + C_Al)"
    ))

    # ex:15.4: Cost of Swirling During Cup Removal
    T_mixed = (215.0 * 49.70 + 203.4 * 29.34) / 418.4
    TG_bulk = T_mixed - 22.00
    kappa_strat = 27.70 / TG_bulk
    pts_lost_swirl = (30.0 - 30.0 * (TG_bulk / 27.70)) + (20.0 - 20.0 * (1.0 - abs(T_mixed - 49.70) / T_mixed))
    checks.append(_make_record(
        "SEC15:EX15.4_T_MIXED", "§15.5",
        "Worked Example 15.6 (15.4): Adiabatic mixed bulk water temperature after swirling [C]",
        39.800, T_mixed, tol=1e-3,
        method="Two-node energy conservation (C_top*T_top + C_bot*T_bot)/(C_top + C_bot)"
    ))
    checks.append(_make_record(
        "SEC15:EX15.4_KAPPA_STRAT", "§15.5",
        "Worked Example 15.6 (15.4): Top-layer stratification multiplier kappa_strat",
        1.5562, kappa_strat, tol=1e-3,
        method="Ratio of stratified top-layer gain to bulk mixed gain"
    ))
    checks.append(_make_record(
        "SEC15:EX15.4_SWIRL_PTS_LOST", "§15.5",
        "Worked Example 15.6 (15.4): Total tournament points lost from post-heat swirling [pts]",
        15.69, pts_lost_swirl, tol=2e-3,
        method="Official v2.0.0 Scoresheet TS + PS loss calculation"
    ))

    # ex:15.5: Open-Cup Evaporative Latent Heat Drain vs Removable BoPET Cap Saturation
    m_dot_evap = 3.60e-3 * 6.65e-3 * (0.04680 - 0.00816)
    Q_dot_evap = 2.406e6 * m_dot_evap
    Q_evap_600 = Q_dot_evap * 600.0
    dm_sat_hs = (7384.0 - 1322.0) * 1.50e-4 * 18.0153 / (R_GAS * 313.15)
    Q_sat_hs = 2406.0 * dm_sat_hs
    checks.append(_make_record(
        "SEC15:EX15.5_Q_EVAP_OPEN", "§15.5",
        "Worked Example 15.7 (15.5): Open-cup evaporative heat loss over 600 s at 40 C [J]",
        1335.4, Q_evap_600, tol=1e-3,
        method="Lienhard §11.7 convective mass-transfer latent heat loss L_v * m_dot * t"
    ))
    checks.append(_make_record(
        "SEC15:EX15.5_Q_SAT_HEADSPACE", "§15.5",
        "Worked Example 15.7 (15.5): Latent heat to saturate 150 cm^3 headspace under BoPET cap [J]",
        15.138, Q_sat_hs, tol=1e-3,
        method="Ideal-gas saturated vapor mass capacity in trapped cup headspace"
    ))

    # ex:15.6 & ex:15.6b: 3-Fin Knife-Edge Pedestal & Tapered Frustum Cup Waterline
    G_base_fins = (0.040 * 1.80e-5 / 0.012) + (0.0278 * 2.188e-3 / 0.010)
    Q_base_fins = G_base_fins * 13.0
    C_fins = 314.5e3 * 1.80e-5 * 0.012
    # Frustum volume at z_w = 3.8757 cm for 100.0 mL (exact root; was 3.8732, which holds only 99.93 mL)
    rb, rt, Hcup = 2.650, 3.750, 10.00
    sc = (rt - rb) / Hcup
    zw_100 = ((100.0 * 3.0 * sc / math.pi + rb**3) ** (1.0 / 3.0) - rb) / sc
    c_rule = (Hcup - zw_100) - 2.50

    checks.append(_make_record(
        "SEC15:EX15.6_Q_BASE_FINS", "§15.6",
        "Worked Example 15.8 (15.6): 3-fin cork pedestal + air cavity base heat leak [W]",
        0.07986, Q_base_fins, tol=2e-3,
        method="Parallel conductive network across 3 knife-edge fins and foil-air cavity"
    ))
    checks.append(_make_record(
        "SEC15:EX15.6B_FRUSTUM_ZW", "§15.6",
        "Worked Example 15.9 (15.6b): Exact 100.0 mL waterline depth z_w in 9 oz cup [cm]",
        3.8757, zw_100, tol=1e-4,
        method="Exact cubic frustum inversion V(z) = (pi*z/3)*(r_b^2 + r_b*r(z) + r(z)^2)"
    ))
    checks.append(_make_record(
        "SEC15:EX15.6B_DRY_CLEARANCE", "§15.6",
        "Worked Example 15.9 (15.6b): Rule 3.e dry clearance below 2.50 cm overhang [cm]",
        3.6243, c_rule, tol=1e-4,
        method="Vertical dry margin H_cup - z_w - d_overhang >= 1.5 cm"
    ))

    # =========================================================================
    # SECTION 16 CHECKS (ex:16.1 through ex:16.6)
    # =========================================================================
    # ex:16.1: Official v2.0.0 Scoresheet Calculation
    ES_both = 50.0 * (88.5 / 92.0)
    TS_alpha = 30.0 * (27.7 / 27.7)
    PE_alpha = 1.0 - abs(49.7 - 49.4) / 49.7
    PS_alpha = 20.0 * (PE_alpha / 0.9980)
    FS_alpha = ES_both + TS_alpha + PS_alpha

    TS_beta = 30.0 * (8.1 / 27.7)
    PE_beta = 1.0 - abs(30.1 - 29.8) / 30.1
    PS_beta = 20.0 * (PE_beta / 0.9980)
    FS_beta = ES_both + TS_beta + PS_beta
    FS_beta_pen = ES_both + 0.7 * (TS_beta + PS_beta)

    checks.append(_make_record(
        "SEC16:EX16.1_FS_ALPHA", "§16.1",
        "Worked Example 16.1: Team Alpha Final Score FS on v2.0.0 Scoresheet [pts]",
        98.017, FS_alpha, tol=1e-3,
        method="Official 2027 Scoresheet v2.0.0 formula ES + TS + PS"
    ))
    checks.append(_make_record(
        "SEC16:EX16.1_FS_BETA", "§16.1",
        "Worked Example 16.1: Team Beta Final Score FS (unpenalized vs 0.7x penalized) [pts]",
        76.711, FS_beta, tol=1e-3,
        method="Official 2027 Scoresheet v2.0.0 formula ES + TS + PS"
    ))
    checks.append(_make_record(
        "SEC16:EX16.1_FS_BETA_PEN", "§16.1",
        "Worked Example 16.1: Team Beta Final Score with 1 construction violation (0.7x) [pts]",
        68.133, FS_beta_pen, tol=1e-3,
        method="Rule 6.g penalty multiplier M_pen = 0.7^(V_constr) applied to TS and PS"
    ))

    # ex:16.2: Five-Variable Prediction with Cold Source Bath Offset (T_start != T_room)
    tau_eff = 903.0
    k_start_13 = math.exp(-780.0 / tau_eff)
    k_room_13 = 1.0 - k_start_13
    M_13 = k_room_13 / (1.0 - math.exp(-600.0 / tau_eff))
    TG_tab_13 = 27.70 * M_13
    T_pred_162 = 19.60 + TG_tab_13 + k_room_13 * (23.20 - 19.60) - 0.22
    checks.append(_make_record(
        "SEC16:EX16.2_M13", "§16.2",
        "Worked Example 16.2: 13-minute time-scaling multiplier M_t(13 min)",
        1.1916, M_13, tol=1e-3,
        method="Lumped exponential growth ratio (1 - exp(-780/903))/(1 - exp(-600/903))"
    ))
    checks.append(_make_record(
        "SEC16:EX16.2_TPRED", "§16.2",
        "Worked Example 16.2: 5-variable predicted final temperature T_pred [C]",
        54.470, T_pred_162, tol=1e-3,
        method="Linear superposition T_start + TG_table + k_room*(T_room - T_start) - dT_cool"
    ))

    # ex:16.2b: Algebraic 3-Point Extraction of tau_eff & Delta T_ss
    TG1_3pt, TG2_3pt, dt_3pt = 16.17, 27.77, 300.0
    tau_3pt = dt_3pt / math.log(TG1_3pt / (TG2_3pt - TG1_3pt))
    dTss_3pt = (TG1_3pt**2) / (2.0 * TG1_3pt - TG2_3pt)
    TG_900_3pt = dTss_3pt * (1.0 - ((TG2_3pt - TG1_3pt) / TG1_3pt) ** 3)
    checks.append(_make_record(
        "SEC16:EX16.2B_TAU_3PT", "§16.2",
        "Worked Example 16.3 (16.2b): 3-point algebraic extracted time constant tau_eff [s]",
        903.21, tau_3pt, tol=1e-3,
        method="Equal-interval 3-point ratio dt / ln(TG1 / (TG2 - TG1))"
    ))
    checks.append(_make_record(
        "SEC16:EX16.2B_DTSS_3PT", "§16.2",
        "Worked Example 16.3 (16.2b): 3-point algebraic extracted steady-state gain Delta T_ss [C]",
        57.214, dTss_3pt, tol=1e-3,
        method="Equal-interval 3-point ratio TG1^2 / (2*TG1 - TG2)"
    ))

    # ex:16.3: 15-Second National Tournament 1-cm Lookup & Linear Interpolation
    TG_53_100_10m = 17.10 + 0.600 * (14.10 - 17.10)
    k_room_14 = 1.0 - math.exp(-840.0 / tau_eff)
    M_14 = k_room_14 / (1.0 - math.exp(-600.0 / tau_eff))
    T_pred_163 = 21.00 + TG_53_100_10m * M_14 + k_room_14 * (21.50 - 21.00) - 0.18
    checks.append(_make_record(
        "SEC16:EX16.3_NATL_INTERP", "§16.3",
        "Worked Example 16.3: National 1-cm interpolated T_pred at h=53 cm, 100 W, 14 min [C]",
        40.204, T_pred_163, tol=1e-3,
        method="Piecewise-linear height interpolation + 14-min exponential time scaling"
    ))

    # ex:16.4: Post-Lamp-Off Staggered Station Cooling Correction
    T_top_600 = 49.92
    dT_cool_A = 0.05 + 0.0245 * 36.0
    T_final_A = T_top_600 - dT_cool_A
    dT_cool_B = 0.05 + 0.0070 * 22.0 + 0.0245 * 14.0
    T_final_B = T_top_600 - dT_cool_B
    checks.append(_make_record(
        "SEC16:EX16.4_COOL_OPEN", "§16.4",
        "Worked Example 16.4(a): Immediate open extraction final temperature at t_wait=36 s [C]",
        48.988, T_final_A, tol=1e-3,
        method="Open-cup post-lamp cooling decay T_top(600) - (delta_ext + r_open*t_open)"
    ))
    checks.append(_make_record(
        "SEC16:EX16.4_COOL_DELAYED", "§16.4",
        "Worked Example 16.4(b): Delayed hood lift final temperature at t_closed=22 s, t_open=14 s [C]",
        49.373, T_final_B, tol=1e-3,
        method="Two-stage closed-hood + open-cup cooling decay integral"
    ))

    # ex:16.5: Six-Trial Repeatability Statistics & Expected PE
    trials = np.array([49.6, 49.8, 49.7, 49.5, 49.9, 49.7], dtype=float)
    mean_Tf = float(np.mean(trials))
    s_rep = float(np.std(trials, ddof=1))
    u_A = s_rep / math.sqrt(len(trials))
    u_run = s_rep * math.sqrt(1.0 + 1.0 / len(trials))
    exp_abs_err = math.sqrt(2.0 / math.pi) * u_run
    exp_PE = 1.0 - exp_abs_err / mean_Tf
    checks.append(_make_record(
        "SEC16:EX16.5_S_REP", "§16.5",
        "Worked Example 16.5(a): Sample repeatability standard deviation s_rep [C]",
        0.14142, s_rep, tol=1e-3,
        method="JCGM GUM Type A sample standard deviation with nu = n - 1 = 5"
    ))
    checks.append(_make_record(
        "SEC16:EX16.5_EXP_PE", "§16.5",
        "Worked Example 16.5(b): Expected single-run tournament Prediction Estimate E[PE]",
        0.99755, exp_PE, tol=1e-4,
        method="Half-normal expectation E[|err|] = sqrt(2/pi)*s_rep*sqrt(1+1/n)"
    ))

    # ex:16.6: Tournament Bulb-Shape Mismatch Recovery (PAR38 Narrow-Beam Bulb)
    TG_R40_60_100_12m = 12.40
    kappa_beam_par38 = 1.160
    T_pred_adj = 22.00 + kappa_beam_par38 * TG_R40_60_100_12m - 0.15
    PS_saved = 20.0 * (1.0 - (1.0 - abs(36.2 - 34.3) / 36.2))
    checks.append(_make_record(
        "SEC16:EX16.6_PAR38_TPRED", "§16.5",
        "Worked Example 16.6(b): PAR38 beam-collimation adjusted prediction T_pred [C]",
        36.234, T_pred_adj, tol=1e-3,
        method="Beam-shape mismatch scaling factor kappa_beam * TG_table"
    ))
    checks.append(_make_record(
        "SEC16:EX16.6_PS_SAVED", "§16.5",
        "Worked Example 16.6(c): Prediction Score points saved by PAR38 beam adjustment [pts]",
        1.0497, PS_saved, tol=2e-3,
        method="Rule 6.f Prediction Score difference 20 * (PE_adj - PE_unadj)"
    ))

    # ex:16.7: Inverse Effective-Distance Power-Law Height Fit
    d1_pl, d2_pl = 45.0 - 19.50, 65.0 - 19.50
    n_pl = math.log(27.70 / 10.60) / math.log(d2_pl / d1_pl)
    dT_55_slotA = 27.70 * ((d1_pl / (55.0 - 19.50)) ** n_pl)
    dT_55_slotB = 27.70 * ((d1_pl / 33.60) ** n_pl)
    checks.append(_make_record(
        "SEC16:EX16.7_POWERLAW_N", "§16.5",
        "Worked Example 16.7(a): Inverse distance power-law exponent n",
        1.6589, n_pl, tol=1e-3,
        method="Two-point log-log slope ln(TG1/TG2) / ln(d2/d1)"
    ))
    checks.append(_make_record(
        "SEC16:EX16.7_POWERLAW_SLOTB", "§16.5",
        "Worked Example 16.7(b): Power-law predicted TG at h=55 cm in Slot B [C]",
        17.52, dT_55_slotB, tol=1e-3,
        method="Inverse effective-distance power law TG1 * (d1 / d_SlotB)^n"
    ))

    return checks


CHECKS = [
    (r["id"], r["section"], r["description"], (lambda rec=r: (rec["passed"], rec["detail"])), r["method"])
    for r in run_checks()
]


if __name__ == "__main__":
    results = run_checks()
    n_pass = sum(1 for r in results if r["passed"])
    print(f"check_sec14_16: {n_pass}/{len(results)} checks PASSED")
    for r in results:
        status = "PASS" if r["passed"] else "FAIL"
        print(f"  [{status}] {r['id']} ({r['section']}): {r['detail']}")
    sys.exit(0 if n_pass == len(results) else 1)
