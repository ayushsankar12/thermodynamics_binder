#!/usr/bin/env python3
"""
Independent Numerical & Structural Verification Suite for Group 1 (§§2–5):
  - src/sec02.tex: Thermodynamic Systems, State Variables, Equilibrium & Zeroth Law
  - src/sec03.tex: Foundations of Heat & Temperature, Scales, Expansion & 8 Scientists (5.c.v)
  - src/sec04.tex: Heat Capacity, Specific/Molar Heat, Dulong-Petit & Multi-Body Calorimetry
  - src/sec05.tex: Phases of Matter, Phase Diagrams (H2O, CO2, Binary Eutectic), Clausius-Clapeyron & Psychrometrics

Compatible with verify/verify_all.py (exposes run_checks() returning (name, passed, detail) tuples)
and runnable standalone: `python verify/checks/check_sec02_05.py`.
"""

import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC_DIR = ROOT / "src"
JSON_PATH = ROOT / "research" / "phase3_constants_tables.json"


def _close(val: float, target: float, rel_tol: float = 1e-3, abs_tol: float = 1e-6) -> bool:
    return math.isclose(val, target, rel_tol=rel_tol, abs_tol=abs_tol)


def check_sec02_examples() -> tuple[str, bool, str]:
    """Verify all 4 worked examples and unit identities in §2 (src/sec02.tex)."""
    # ex:02.1: Mixing Two Identical Subsystems (Intensive vs Extensive)
    V_A, V_B = 2.50, 2.50  # L
    n_A, n_B = 0.200, 0.200  # mol
    T_A, T_B = 300.0, 300.0  # K
    P_A, P_B = 199.5, 199.5  # kPa
    U_A, U_B = 748.3, 748.3  # J
    V_tot = V_A + V_B
    n_tot = n_A + n_B
    U_tot = U_A + U_B
    V_m = V_tot / n_tot
    ok_2_1 = (
        _close(V_tot, 5.00)
        and _close(n_tot, 0.400)
        and _close(U_tot, 1496.6)
        and _close(T_A, 300.0)
        and _close(P_A, 199.5)
        and _close(V_m, 12.50)
    )

    # ex:02.2: First Law Sign Translation (Physics W_by vs Chemistry w_on) & Pressure Conversion
    Q_in = 1.850e3  # J
    P_gauge_psi = 29.40
    P_atm_psi = 14.696
    P_abs_psi = P_gauge_psi + P_atm_psi  # 44.096 psia = 3.0005 atm
    P_abs_Pa = (P_abs_psi / P_atm_psi) * 101325.0  # ~303.98e3 Pa
    P_round_Pa = 304.0e3  # 3.000 atm * 101.325 kPa/atm = 303.975 kPa -> 304.0 kPa
    dV = (6.20 - 2.00) * 1e-3  # 4.20e-3 m^3
    W_by = P_round_Pa * dV  # 1276.8 J
    dU_phys = Q_in - W_by  # +573.2 J
    w_on = -W_by  # -1276.8 J
    dU_chem = Q_in + w_on
    ok_2_2 = (
        _close(P_abs_psi, 44.096, rel_tol=1e-3)
        and _close(W_by, 1276.8, rel_tol=1e-3)
        and _close(dU_phys, 573.2, rel_tol=1e-3)
        and _close(dU_phys, dU_chem, rel_tol=1e-9)
    )

    # ex:02.3: State Function vs Path Function Across Three P-V Paths
    P1, V1 = 300.0e3, 1.00e-3
    P2, V2 = 100.0e3, 3.00e-3
    W_A = P1 * (V2 - V1) + 0.0  # 600.0 J
    W_B = 0.0 + P2 * (V2 - V1)  # 200.0 J
    W_C = 0.5 * (P1 + P2) * (V2 - V1)  # 400.0 J
    Q_A = 600.0
    dU_12 = Q_A - W_A  # 0.0 J
    Q_B = dU_12 + W_B  # 200.0 J
    Q_C = dU_12 + W_C  # 400.0 J
    W_cycle = W_A - W_B  # +400.0 J enclosed rectangle area
    ok_2_3 = (
        _close(W_A, 600.0)
        and _close(W_B, 200.0)
        and _close(W_C, 400.0)
        and _close(Q_B, 200.0)
        and _close(Q_C, 400.0)
        and _close(W_cycle, 400.0)
    )

    # ex:02.4: Two-Point Linear Thermometric Calibration & Triple-Point Check
    X_0, X_100 = 108.40, 146.90  # Ohm
    alpha_X = (X_100 - X_0) / 100.0  # 0.3850 Ohm/C
    X_bath = 122.645
    T_C = (X_bath - X_0) / alpha_X  # 37.00 C
    T_K = T_C + 273.15  # 310.15 K
    P_tr_tp = 45.00
    P_tr = 50.98
    T_gas_K = 273.16 * (P_tr / P_tr_tp)  # 309.46 K
    discrepancy_K = T_K - T_gas_K  # 0.69 K
    ok_2_4 = (
        _close(alpha_X, 0.3850)
        and _close(T_C, 37.00)
        and _close(T_K, 310.15)
        and _close(T_gas_K, 309.46, rel_tol=1e-4)
        and _close(discrepancy_K, 0.69, abs_tol=0.01)
    )

    passed = ok_2_1 and ok_2_2 and ok_2_3 and ok_2_4
    return (
        "sec02_worked_examples",
        passed,
        f"ex02.1={ok_2_1}, ex02.2={ok_2_2} (dU={dU_phys:.1f} J), ex02.3={ok_2_3} (W_cyc={W_cycle:.1f} J), ex02.4={ok_2_4}",
    )


def check_sec03_examples() -> tuple[str, bool, str]:
    """Verify all 5 worked examples, 8 temperature scales, and 8 Rule 5.c.v scientists in §3."""
    # ex:03.1: Historical Temperature Scales (Delisle 195.0 De & Reaumur -24.0 Re)
    T_De = 195.0
    T_C_1 = 100.0 - (2.0 / 3.0) * T_De  # -30.0 C
    T_K_1 = T_C_1 + 273.15  # 243.15 K
    T_F_1 = 1.8 * T_C_1 + 32.0  # -22.0 F
    T_Re = -24.0
    T_C_2 = 1.25 * T_Re  # -30.0 C
    ok_3_1 = _close(T_C_1, -30.0) and _close(T_K_1, 243.15) and _close(T_F_1, -22.0) and _close(T_C_1, T_C_2)

    # Verify all 8 temperature scales at -30.0 C
    T_R = 1.8 * T_K_1  # 437.67 R
    T_N = 0.33 * T_C_1  # -9.90 N
    T_Ro = (21.0 / 40.0) * T_C_1 + 7.5  # -8.25 Ro
    ok_scales = _close(T_R, 437.67) and _close(T_N, -9.90) and _close(T_Ro, -8.25)

    # ex:03.2: Shrink-Fit Interference Assembly (Brass collar on Steel shaft)
    T0 = 20.0
    a_brass, a_steel = 19.0e-6, 12.0e-6
    D_brass0, D_steel0 = 4.990, 5.000
    dT_a = (D_steel0 - D_brass0) / (a_brass * D_brass0)  # 105.474 C
    T_a = T0 + dT_a  # 125.474 C
    dT_b = (D_steel0 - D_brass0) / (a_brass * D_brass0 - a_steel * D_steel0)  # 287.274 C
    T_b = T0 + dT_b  # 307.274 C
    ok_3_2 = _close(T_a, 125.47, rel_tol=1e-3) and _close(T_b, 307.27, rel_tol=1e-3)

    # ex:03.3: Apparent Overflow of Ethanol in a Pyrex Beaker
    a_pyrex = 3.0e-6
    b_eth = 1100.0e-6
    V0 = 500.0  # mL
    dT = 30.0
    dV_over = (b_eth - 3.0 * a_pyrex) * V0 * dT  # 16.365 mL
    ok_3_3 = _close(dV_over, 16.365, rel_tol=1e-4)

    # ex:03.4: Bimetallic Strip Curvature & Tip Deflection (Brass-Invar)
    L0 = 0.0800  # m
    d = 5.00e-4  # m
    a2, a1 = 19.0e-6, 0.90e-6
    dT_bi = 100.0
    R_curv = d / ((a2 - a1) * dT_bi)  # 0.276243 m
    delta_tip = (L0**2) / (2.0 * R_curv)  # 0.011584 m
    ok_3_4 = _close(R_curv, 0.27624, rel_tol=1e-3) and _close(delta_tip, 0.01158, rel_tol=1e-3)

    # ex:03.5: Joule's Falling-Weight Paddle-Wheel Experiment (Rule 5.c.v)
    N = 20
    m_lead = 13.20
    g = 9.80665
    h = 1.60
    W_mech = 2 * N * m_lead * g * h  # 8284.6579 J
    C_tot = 5.50 * 4184.0 + 385.0  # 23397.0 J/K
    dT_joule = W_mech / C_tot  # 0.354091 K
    ok_3_5 = _close(W_mech, 8284.66, rel_tol=1e-4) and _close(dT_joule, 0.35409, rel_tol=1e-4)

    passed = ok_3_1 and ok_scales and ok_3_2 and ok_3_3 and ok_3_4 and ok_3_5
    return (
        "sec03_worked_examples",
        passed,
        f"ex03.1={ok_3_1}, ex03.2={ok_3_2}, ex03.3={ok_3_3}, ex03.4={ok_3_4}, ex03.5={ok_3_5} (dT={dT_joule:.4f} K)",
    )


def check_sec04_examples() -> tuple[str, bool, str]:
    """Verify all 7 worked examples and 5-stage water heating curve in §4 (src/sec04.tex)."""
    c_w = 4.184  # J/(g K)
    c_ice = 2.09  # J/(g K) house value
    c_st = 2.080  # J/(g K)
    L_f = 333.55  # J/g
    L_v = 2256.4  # J/g
    R = 8.314462618

    # 5-stage water heating curve (-40 C to +160 C per kg)
    q1 = c_ice * 40.0  # 83.60 kJ/kg
    q2 = q1 + L_f  # 417.15 kJ/kg
    q3 = q2 + c_w * 100.0  # 835.55 kJ/kg
    q4 = q3 + L_v  # 3091.95 kJ/kg
    q5 = q4 + c_st * 60.0  # 3216.75 kJ/kg
    ok_curve = _close(q1, 83.60) and _close(q2, 417.15) and _close(q3, 835.55) and _close(q4, 3091.95) and _close(q5, 3216.75)

    # ex:04.1: Calorimeter Calibration & Unknown Metal ID via Dulong-Petit
    C_cal = 100.0 * c_w * (60.00 - 35.38) / (35.38 - 20.00) - 150.0 * c_w  # 42.166 J/K
    m_eq = C_cal / c_w  # 10.078 g
    c_m = (200.0 * c_w + C_cal) * (27.86 - 20.00) / (0.2500 * (100.00 - 27.86))  # 383.07 J/(kg K)
    M_est = (3.0 * R) / (c_m / 1000.0)  # 65.11 g/mol
    ok_4_1 = _close(C_cal, 42.17, rel_tol=1e-3) and _close(m_eq, 10.08, rel_tol=1e-3) and _close(c_m, 383.1, rel_tol=1e-3) and _close(M_est, 65.1, rel_tol=2e-3)

    # ex:04.2: Partial-Melting Ice-Water Equilibrium (Zone II Plateau at 0 C)
    E_avail_0 = (250.0 * c_w + 120.0 * 0.385) * 22.0  # 24028.4 J
    E_warm_ice = 110.0 * c_ice * 15.0  # 3453.45 J
    E_melt_ice = 110.0 * L_f  # 36690.50 J
    E_net_0 = E_avail_0 - (E_warm_ice + E_melt_ice)  # -16115.55 J
    m_ice_final = -E_net_0 / L_f  # 48.315 g
    m_liq_final = 360.0 - m_ice_final  # 311.685 g
    ok_4_2 = _close(E_net_0, -16110.60) and _close(m_ice_final, 48.30, rel_tol=1e-4) and _close(m_liq_final, 311.70, rel_tol=1e-4)

    # ex:04.3: Three-Phase Ice + Water + Steam Mixture in Copper Calorimeter (Zone III)
    E_avail_3 = 200.0 * c_w * 50.0 + 25.0 * (c_st * 30.0 + L_v + 100.0 * c_w) - 38.50 * 10.0  # 109885.0 J
    E_need_3 = 80.0 * (c_ice * 10.0 + L_f)  # 28358.4 J
    E_net_3 = E_avail_3 - E_need_3  # 81526.6 J
    C_tot_3 = 305.0 * c_w + 38.50  # 1314.62 J/K
    T_f_3 = E_net_3 / C_tot_3  # 62.0153 C
    ok_4_3 = _close(E_net_3, 81529.0) and _close(T_f_3, 62.02, rel_tol=1e-4)

    # ex:04.4: Partial Steam Condensation (Zone IV Plateau at 100 C)
    E_avail_4 = 200.0 * c_w * 50.0 + 60.0 * (c_st * 30.0 + L_v + 100.0 * c_w) - 38.50 * 10.0  # 205687.0 J
    E_net_4 = E_avail_4 - E_need_3  # 177328.6 J
    E_100_l = (340.0 * c_w + 38.50) * 100.0  # 146106.0 J
    m_st_final = (E_net_4 - E_100_l) / L_v  # 13.8374 g
    m_liq_4 = 340.0 - m_st_final  # 326.1626 g
    ok_4_4 = _close(E_net_4, 177331.0) and _close(m_st_final, 13.84, rel_tol=1e-3) and _close(m_liq_4, 326.16, rel_tol=1e-3)

    # ex:04.5: Electrical Calorimetry with Regnault-Pfaundler Drift Correction
    dT_obs = 28.340 - 21.200  # 7.140 K
    r_bar = 0.5 * (0.010 - 0.050)  # -0.020 K/min
    dT_corr = dT_obs - r_bar * 4.000  # 7.220 K
    E_elec = 12.00 * 2.500 * 240.0  # 7200.0 J
    c_liq = (E_elec / dT_corr - 55.0) / 0.4000  # 2355.57 J/(kg K)
    ok_4_5 = _close(dT_corr, 7.220) and _close(c_liq, 2355.6, rel_tol=1e-4)

    # ex:04.6: Isobaric Coffee-Cup Neutralization Enthalpy (HCl + NaOH)
    m_soln = 200.0 * 1.020  # 204.0 g
    q_soln = (m_soln * 4.050 + 18.0) * (28.12 - 21.50)  # 5588.604 J
    dH_neut = -(q_soln / 1000.0) / 0.1000  # -55.886 kJ/mol
    ok_4_6 = _close(q_soln, 5588.6, rel_tol=1e-4) and _close(dH_neut, -55.89, rel_tol=1e-3)

    # ex:04.7: Isochoric Bomb Calorimetry (Benzoic Acid Calibration & Octane dU -> dH)
    q_cal_1 = 1.2500 * 26434.0 + 48.0  # 33090.5 J
    C_bomb = q_cal_1 / 3.1850  # 10389.482 J/K
    n_oct = 0.8565 / 114.23  # 7.49803e-3 mol
    q_V_oct = C_bomb * 3.9410 - 48.0  # 40896.95 J
    dU_c = -(q_V_oct / 1000.0) / n_oct  # -5454.36 kJ/mol
    dn_gas = 8.0 - 12.5  # -4.5
    dH_c = dU_c + dn_gas * (R / 1000.0) * 298.15  # -5465.51 kJ/mol
    ok_4_7 = (
        _close(C_bomb, 10389.5, rel_tol=1e-4)
        and _close(dU_c, -5454.4, rel_tol=1e-4)
        and _close(dH_c, -5465.5, rel_tol=1e-4)
    )

    # ex:04.8: Callendar-Barnes Continuous-Flow Calorimeter with Heat-Leak Cancellation
    P1, P2 = 15.00 * 2.200, 20.00 * 2.850  # 33.00 W, 57.00 W
    dm1, dm2 = 1.800e-3, 3.300e-3
    dT_flow = 8.00
    cp_oil = (P2 - P1) / ((dm2 - dm1) * dT_flow)  # 2000.0 J/(kg K)
    Q_dot_loss = P1 - dm1 * cp_oil * dT_flow  # 4.20 W
    ok_4_8 = _close(cp_oil, 2000.0) and _close(Q_dot_loss, 4.20)

    # ex:04.9: Zone I Sub-Zero Equilibrium (Cryogenic Ice Freezing All Liquid Water)
    E_avail_9 = 50.0 * c_w * 20.0  # 4184.0 J
    E_need_9 = 600.0 * c_ice * 40.0 + 600.0 * L_f  # 250362.0 J
    E_net_9 = E_avail_9 - E_need_9  # -246178.0 J
    M_tot_9 = 650.0
    T_f_9 = (E_net_9 + M_tot_9 * L_f) / (M_tot_9 * c_ice)  # -21.5888 C
    ok_4_9 = _close(E_net_9, -246106.0) and _close(T_f_9, -21.57, rel_tol=2.4e-4)

    # ex:04.10: Four-Body Multi-Metal & Glycerol Mixture with Water Equivalent m_eq
    C_cal_10 = 15.0 * c_w  # 62.76 J/K
    C_gly_10 = 350.0 * 2.427  # 849.45 J/K
    C_Al_10 = 120.0 * 0.897  # 107.64 J/K
    C_Ag_10 = 200.0 * 0.235  # 47.00 J/K
    C_sum_10 = C_cal_10 + C_gly_10 + C_Al_10 + C_Ag_10  # 1066.85 J/K
    T_f_10 = ((C_cal_10 + C_gly_10) * 18.00 + C_Al_10 * 140.0 + C_Ag_10 * 180.0) / C_sum_10  # 37.4461 C
    ok_4_10 = _close(C_sum_10, 1066.85) and _close(T_f_10, 37.45, rel_tol=1e-3)

    # ex:04.11: Temperature-Dependent Gas Heating via NIST Shomate Midpoint Cp
    Q_const_11 = 5.000 * 37.13 * (1000.0 - 298.15) / 1000.0  # 130.298 kJ
    Q_mid_11 = 5.000 * (0.5 * (37.13 + 47.32) * (600.0 - 298.15) + 0.5 * (47.32 + 54.31) * 400.0) / 1000.0  # 165.363 kJ
    err_pct_11 = (Q_mid_11 - Q_const_11) / Q_mid_11 * 100.0  # 21.205%
    ok_4_11 = _close(Q_const_11, 130.30, rel_tol=1e-3) and _close(Q_mid_11, 165.36, rel_tol=1e-3) and _close(err_pct_11, 21.2, rel_tol=2e-3)

    passed = ok_curve and ok_4_1 and ok_4_2 and ok_4_3 and ok_4_4 and ok_4_5 and ok_4_6 and ok_4_7 and ok_4_8 and ok_4_9 and ok_4_10 and ok_4_11
    return (
        "sec04_worked_examples",
        passed,
        f"curve={ok_curve}, ex04.1..11={[ok_4_1, ok_4_2, ok_4_3, ok_4_4, ok_4_5, ok_4_6, ok_4_7, ok_4_8, ok_4_9, ok_4_10, ok_4_11]}",
    )


def check_sec05_examples() -> tuple[str, bool, str]:
    """Verify all 6 worked examples and phase diagram / psychrometric benchmarks in §5 (src/sec05.tex)."""
    R = 8.314462618

    # ex:05.1: Pressure Melting (Regelation) of Ice via Exact Clapeyron Equation
    L_f = 333550.0  # J/kg
    T0 = 273.15
    dv_fus = (1.00016 - 1.0908) * 1e-3  # -9.064e-5 m^3/kg
    dP_dT_Pa = L_f / (T0 * dv_fus)  # -13.472e6 Pa/K
    dP_dT_atm = dP_dT_Pa / 101325.0  # -132.96 atm/K
    dT_m = 149.0 / dP_dT_atm  # -1.1206 K
    ok_5_1 = _close(dP_dT_Pa / 1e6, -13.47, rel_tol=1e-3) and _close(dP_dT_atm, -133.0, rel_tol=1e-3) and _close(dT_m, -1.121, rel_tol=2e-3)

    # ex:05.2: Two-Phase Saturation Dome Quality x, Enthalpy & Volume at 120 C
    v_f, v_g = 0.0010603, 0.8913
    h_f, h_fg = 503.81, 2202.1
    v_mix = 0.500 / 2.000  # 0.2500 m^3/kg
    x = (v_mix - v_f) / (v_g - v_f)  # 0.279633
    m_g = x * 2.000  # 0.55927 kg
    m_f = 2.000 - m_g  # 1.44073 kg
    H_tot = 2.000 * (h_f + x * h_fg)  # 2239.18 kJ
    ok_5_2 = _close(x, 0.27963, rel_tol=1e-4) and _close(m_g, 0.5593, rel_tol=1e-3) and _close(H_tot, 2239.2, rel_tol=1e-4)

    # ex:05.3: Binary Eutectic Alloy Lever Rule & Microconstituents (2027 Cornell E1)
    w0 = 35.0
    w_S, w_L = 14.0, 50.0
    f_L = (w0 - w_S) / (w_L - w_S)  # 21/36 = 0.583333
    f_S = (w_L - w0) / (w_L - w_S)  # 15/36 = 0.416667
    m_L = 500.0 * f_L  # 291.67 g
    m_S = 500.0 * f_S  # 208.33 g
    w_aE, w_E, w_bE = 18.3, 61.9, 97.8
    f_alpha_tot = (w_bE - w0) / (w_bE - w_aE)  # 62.8/79.5 = 0.789937
    f_beta_tot = (w0 - w_aE) / (w_bE - w_aE)  # 16.7/79.5 = 0.210063
    f_prim_alpha = (w_E - w0) / (w_E - w_aE)  # 26.9/43.6 = 0.616972
    f_eutectic = (w0 - w_aE) / (w_E - w_aE)  # 16.7/43.6 = 0.383028
    ok_5_3 = (
        _close(m_L, 291.7, rel_tol=1e-3)
        and _close(m_S, 208.3, rel_tol=1e-3)
        and _close(f_alpha_tot, 0.7899, rel_tol=1e-3)
        and _close(f_prim_alpha, 0.6170, rel_tol=1e-3)
        and _close(f_eutectic, 0.3830, rel_tol=1e-3)
    )

    # ex:05.4: High-Altitude Boiling Point via Algebraic Clausius-Clapeyron
    T1 = 373.15
    P1, P2 = 101.325, 58.60
    dH_vap = 40650.0
    inv_T2 = (1.0 / T1) - (R / dH_vap) * math.log(P2 / P1)
    T2_K = 1.0 / inv_T2  # 358.180 K
    T2_C = T2_K - 273.15  # 85.030 C
    ok_5_4 = _close(T2_K, 358.18, rel_tol=1e-4) and _close(T2_C, 85.03, rel_tol=1e-3)

    # ex:05.5: Psychrometrics (RH, Humidity Ratio, Dew Point & Condensation)
    P_tot = 101.325
    P_sat_30 = 4.2470
    P_v1 = 0.600 * P_sat_30  # 2.5482 kPa
    P_a1 = P_tot - P_v1  # 98.7768 kPa
    w1 = 0.62198 * P_v1 / P_a1  # 0.0160452
    T_dp_lin = 20.0 + 5.0 * (2.5482 - 2.3393) / (3.1699 - 2.3393)  # 21.2575 C
    m_a = (P_a1 * 1000.0) * 1000.0 * 0.028965 / (R * 303.15)  # 1134.90 kg
    P_v2 = 1.7057
    w2 = 0.62198 * P_v2 / (P_tot - P_v2)  # 0.0106492
    m_cond = m_a * (w1 - w2)  # 6.124 kg
    ok_5_5 = (
        _close(P_v1, 2.5482)
        and _close(w1, 0.016045, rel_tol=1e-3)
        and _close(T_dp_lin, 21.26, rel_tol=1e-3)
        and _close(m_cond, 6.124, rel_tol=1e-3)
    )

    # ex:05.6: Adiabatic Crystallization of Supercooled Water & Colligative Antifreeze Check
    f_frozen = (4.184 * 12.0) / 333.55  # 0.150526
    m_ice_6 = 200.0 * f_frozen  # 30.105 g
    molality = 12.0 / (3.0 * 1.853)  # 2.15866 mol/kg
    m_CaCl2 = 0.2000 * molality * 110.98  # 47.913 g
    ok_5_6 = _close(f_frozen, 0.15053, rel_tol=1e-4) and _close(m_ice_6, 30.11, rel_tol=1e-3) and _close(m_CaCl2, 47.91, rel_tol=1e-3)

    # ex:05.7: Dry Ice Sublimation Bath & Sealed-Vessel Triple-Point Liquefaction
    Q_eth_max = 500.0 * 2.440 * (22.00 - (-78.46))  # 122561.2 J
    Q_sub_all = 150.0 * 571.3  # 85695.0 J
    T_f_eth = 22.00 - Q_sub_all / (500.0 * 2.440)  # -48.2418 C
    n_co2 = 150.0 / 44.010
    P_id_tp = n_co2 * R * 216.59 / 1.200e-3  # 5.1147e6 Pa
    ok_5_7 = _close(Q_sub_all, 85695.0) and _close(T_f_eth, -48.24, rel_tol=1e-3) and _close(P_id_tp / 1e6, 5.115, rel_tol=1e-3)

    # ex:05.8: Isochoric Heating Across Saturation Dome & Steam-Table Interpolation
    P_sat_70 = 0.5 * (19.946 + 47.414)  # 33.68 kPa
    h_fg_70 = 0.5 * (2357.7 + 2308.0)  # 2332.85 kJ/kg
    v_g_70 = 0.5 * (7.667 + 3.405)  # 5.536 m^3/kg
    v_amp = 31.06e-6 / 0.01000  # 0.003106 m^3/kg == v_c
    x_1_amp = (v_amp - 0.0010030) / (43.34 - 0.0010030)  # 4.8524e-5
    ok_5_8 = _close(P_sat_70, 33.68) and _close(h_fg_70, 2332.85) and _close(v_g_70, 5.536) and _close(x_1_amp, 4.852e-5, rel_tol=1e-3)

    passed = ok_5_1 and ok_5_2 and ok_5_3 and ok_5_4 and ok_5_5 and ok_5_6 and ok_5_7 and ok_5_8
    return (
        "sec05_worked_examples",
        passed,
        f"ex05.1..8={[ok_5_1, ok_5_2, ok_5_3, ok_5_4, ok_5_5, ok_5_6, ok_5_7, ok_5_8]}",
    )


def check_sec02_05_structure_and_figures() -> tuple[str, bool, str]:
    """Verify all mandatory labels, figures, scientists (5.c.v), and environments in src/sec02..05.tex."""
    expected_figs = {
        "sec02.tex": ["fig:02:boundaries"],
        "sec03.tex": ["fig:03:scales", "fig:03:bimetallic", "fig:03:history"],
        "sec04.tex": ["fig:04:heating-curve", "fig:04:ice-water-tree", "fig:04:calorimeters"],
        "sec05.tex": ["fig:05:h2o-co2-phase", "fig:05:pv-dome", "fig:05:binary-eutectic"],
    }
    expected_examples = {
        "sec02.tex": ["ex:02.1", "ex:02.2", "ex:02.3", "ex:02.4"],
        "sec03.tex": ["ex:03.1", "ex:03.2", "ex:03.3", "ex:03.4", "ex:03.5"],
        "sec04.tex": ["ex:04.1", "ex:04.2", "ex:04.3", "ex:04.4", "ex:04.5", "ex:04.6", "ex:04.7", "ex:04.8", "ex:04.9", "ex:04.10", "ex:04.11"],
        "sec05.tex": ["ex:05.1", "ex:05.2", "ex:05.3", "ex:05.4", "ex:05.5", "ex:05.6", "ex:05.7", "ex:05.8"],
    }
    scientists_5cv = [
        "William Thomson (Lord Kelvin)",
        "Joseph Black",
        "James Prescott Joule",
        "Sadi Carnot",
        "Max Planck",
        "Rudolf Clausius",
        "Ludwig Boltzmann",
        "James Clerk Maxwell",
    ]
    missing = []
    for fname, figs in expected_figs.items():
        fpath = SRC_DIR / fname
        if not fpath.exists():
            missing.append(f"MISSING FILE: {fname}")
            continue
        text = fpath.read_text(encoding="utf-8")
        for req in [r"\binderchapter", r"\scopebanner", r"\begin{formulacard}", r"\begin{trapbox}", r"\begin{devicebox}", r"\verifiedby", r"\alsosee"]:
            if req not in text:
                missing.append(f"{fname}: missing {req}")
        for flabel in figs:
            if f"\\label{{{flabel}}}" not in text:
                missing.append(f"{fname}: missing figure label {flabel}")
        for exlabel in expected_examples[fname]:
            if f"{{{exlabel}}}" not in text:
                missing.append(f"{fname}: missing example {exlabel}")
        if fname == "sec03.tex":
            for sci in scientists_5cv:
                if sci not in text:
                    missing.append(f"sec03.tex: missing 5.c.v scientist {sci}")

    passed = len(missing) == 0
    detail = "All 4 chapters, 10 figure labels, 26 worked examples & 8 scientists verified" if passed else "; ".join(missing)
    return ("sec02_05_structure_and_figures", passed, detail)


def check_json_constants_consistency() -> tuple[str, bool, str]:
    """Cross-check research/phase3_constants_tables.json against §§2–5 fundamental constants."""
    if not JSON_PATH.exists():
        return ("sec02_05_json_consistency", False, f"Missing {JSON_PATH}")
    data = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    consts = {row["symbol"]: row for row in data.get("fundamental_constants_CODATA2022", [])}
    k_B = consts["k_B"]["value"]
    N_A = consts["N_A"]["value"]
    R_val = consts["R"]["value"]
    sci_list = data.get("historical_scientists_5cv", [])
    ok = (
        _close(k_B, 1.380649e-23, rel_tol=1e-9)
        and _close(N_A, 6.02214076e23, rel_tol=1e-9)
        and _close(k_B * N_A, R_val, rel_tol=1e-9)
        and len(sci_list) == 8
    )
    return (
        "sec02_05_json_consistency",
        ok,
        f"k_B*N_A={k_B*N_A:.7f} J/(mol K) == R={R_val:.7f}, scientists={len(sci_list)}",
    )


def run_checks() -> list[tuple[str, bool, str]]:
    return [
        check_sec02_examples(),
        check_sec03_examples(),
        check_sec04_examples(),
        check_sec05_examples(),
        check_sec02_05_structure_and_figures(),
        check_json_constants_consistency(),
    ]


if __name__ == "__main__":
    results = run_checks()
    all_ok = True
    for name, passed, detail in results:
        status = "PASS" if passed else "FAIL"
        print(f"[{status}] {name}: {detail}")
        if not passed:
            all_ok = False
    print(f"\nSummary: {sum(1 for _, p, _ in results if p)}/{len(results)} checks PASSED.")
    sys.exit(0 if all_ok else 1)
