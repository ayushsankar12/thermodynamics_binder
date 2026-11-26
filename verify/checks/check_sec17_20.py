#!/usr/bin/env python3
"""Independent Numerical Verification Suite for Phase 6 Group 5 (Sections 17-20).

Verifies every worked example, sensor equation, calibration formula, JCGM GUM
uncertainty propagation rule, steam-table bilinear interpolation, Clapeyron
finite-difference check, trapezoidal integration, semi-log OLS regression,
Grubbs outlier test, multi-physics coupled problem template, and diagnostic
trap calculation across:
  - src/sec17.tex (Laboratory & Measurement Handbook)
  - src/sec18.tex (Graphs, Data & Experimental Analysis)
  - src/sec19.tex (Integrated Problem-Solving Playbook)
  - src/sec20.tex (Misconceptions, Classic Sign/Unit Traps & Wrong-Answer Catalog)
"""
from __future__ import annotations

import math
import sys
import numpy as np


def _rec(
    cid: str,
    sec: str,
    desc: str,
    expected: float,
    computed: float,
    tol: float = 1e-4,
    method: str = "Independent Python analytical/numerical verification",
) -> dict:
    denom = max(abs(expected), 1e-15)
    rel_err = abs(computed - expected) / denom
    passed = rel_err <= tol
    return {
        "id": cid,
        "section": sec,
        "description": desc,
        "passed": bool(passed),
        "expected": round(float(expected), 6),
        "computed": round(float(computed), 6),
        "rel_error": float(rel_err),
        "tolerance": float(tol),
        "detail": (
            f"expected={expected:.6g}, computed={computed:.6g}, "
            f"rel_err={rel_err:.2e} <= tol={tol:.1e}"
        ),
        "method": method,
    }


def check_sec17() -> list[dict]:
    out = []

    # Ex 17.1: Spirit-in-glass capillary sensitivity & stem-emergence correction
    beta_eth = 1.12e-3      # K^-1
    alpha_glass = 3.3e-6    # K^-1
    beta_app = beta_eth - 3.0 * alpha_glass
    v_bulb = 250.0          # mm^3
    d_bore = 0.400          # mm
    a_bore = math.pi * (d_bore / 2.0) ** 2
    dL_dT = (v_bulb / a_bore) * beta_app
    out.append(
        _rec(
            "sec17:ex17.1:capillary_sensitivity",
            "sec17",
            "Spirit-in-glass capillary sensitivity dL/dT [mm/K]",
            2.208474,
            dL_dT,
            1e-4,
            "Volumetric expansion (beta_liq - 3*alpha_glass)*V_bulb/(pi*r^2)",
        )
    )
    k_g = 0.00104
    N_deg = 45.0
    T_bath_read = 65.0
    T_stem = 23.0
    dT_stem = k_g * N_deg * (T_bath_read - T_stem)
    T_true_stem = T_bath_read + dT_stem
    out.append(
        _rec(
            "sec17:ex17.1:stem_emergence",
            "sec17",
            "Partial-immersion stem-emergence corrected temperature [deg C]",
            66.9656,
            T_true_stem,
            1e-4,
            "Stem correction T_true = T_read + k_g * N * (T_read - T_stem)",
        )
    )

    # Ex 17.2: NTC thermistor beta model, sensitivity, and self-heating error
    R0 = 10000.0
    T0 = 298.15
    beta = 3892.0
    R_meas = 4912.0
    inv_T = (1.0 / T0) + (1.0 / beta) * math.log(R_meas / R0)
    T_K = 1.0 / inv_T
    T_C = T_K - 273.15
    alpha_R = -beta / (T_K ** 2)
    V_ref = 3.30
    R_s = 10000.0
    I_mA = (V_ref / (R_s + R_meas)) * 1e3
    P_mW = ((V_ref / (R_s + R_meas)) ** 2) * R_meas * 1e3
    delta_diss = 6.5  # mW/K in water
    dT_sh = P_mW / delta_diss
    out.append(
        _rec(
            "sec17:ex17.2:ntc_temp_C",
            "sec17",
            "NTC thermistor temperature from beta equation [deg C]",
            42.172264,
            T_C,
            1e-4,
            "Direct inversion of R(T) = R0*exp(beta*(1/T - 1/T0))",
        )
    )
    out.append(
        _rec(
            "sec17:ex17.2:ntc_alpha_R",
            "sec17",
            "NTC fractional resistance sensitivity alpha_R [K^-1]",
            -0.0391439,
            alpha_R,
            1e-4,
            "Analytical derivative (1/R)(dR/dT) = -beta/T^2",
        )
    )
    out.append(
        _rec(
            "sec17:ex17.2:ntc_self_heating",
            "sec17",
            "NTC self-heating bias dT_SH = I^2*R/delta_diss [deg C]",
            0.0370085,
            dT_sh,
            1e-3,
            "Voltage divider Joule power P = (V_ref/(R_s+R))^2 * R / delta_diss",
        )
    )

    # Ex 17.3: Pt100 RTD Callendar-Van Dusen & 2-wire lead error + IR emissivity trap
    R0_pt = 100.0
    A_pt = 3.9083e-3
    B_pt = -5.775e-7
    R_meas_2w = 117.47
    R_lead_loop = 2.0 * 0.35
    R_true_pt = R_meas_2w - R_lead_loop
    # Solve R0*(1 + A*t + B*t^2) = R
    roots_true = np.roots([R0_pt * B_pt, R0_pt * A_pt, R0_pt - R_true_pt])
    t_true_pt = float([r for r in roots_true if 0 <= r <= 200][0])
    roots_app = np.roots([R0_pt * B_pt, R0_pt * A_pt, R0_pt - R_meas_2w])
    t_app_pt = float([r for r in roots_app if 0 <= r <= 200][0])
    out.append(
        _rec(
            "sec17:ex17.3:pt100_true_temp",
            "sec17",
            "Pt100 Callendar-Van Dusen true temperature [deg C]",
            43.18423,
            t_true_pt,
            1e-4,
            "Quadratic root of R0*(1 + A*t + B*t^2) = 116.77 Ohm",
        )
    )
    out.append(
        _rec(
            "sec17:ex17.3:pt100_lead_error",
            "sec17",
            "Pt100 2-wire lead-resistance error t_app - t_true [deg C]",
            1.81471,
            t_app_pt - t_true_pt,
            1e-3,
            "Difference between 117.47 Ohm and 116.77 Ohm CVD solutions",
        )
    )

    # IR emissivity trap: background-compensated pyrometer
    # eps_set * (T_read^4 - T_amb^4) = eps_true * (T_obj^4 - T_amb^4)
    T_obj = 44.0 + 273.15
    T_amb = 22.0 + 273.15
    eps_set = 0.95
    T_ir_water = (T_amb**4 + (0.96 / eps_set) * (T_obj**4 - T_amb**4)) ** 0.25 - 273.15
    T_ir_foil = (T_amb**4 + (0.04 / eps_set) * (T_obj**4 - T_amb**4)) ** 0.25 - 273.15
    out.append(
        _rec(
            "sec17:ex17.3:ir_water_read",
            "sec17",
            "IR thermometer reading on water (eps=0.96, eps_set=0.95) [deg C]",
            44.20835,
            T_ir_water,
            1e-4,
            "Background-compensated radiometric balance (T_amb^4 + (eps/eps_set)*(T_obj^4 - T_amb^4))^(1/4)",
        )
    )
    out.append(
        _rec(
            "sec17:ex17.3:ir_foil_read",
            "sec17",
            "IR thermometer reading on shiny Al foil (eps=0.04, eps_set=0.95) [deg C]",
            23.02970,
            T_ir_foil,
            1e-4,
            "Background-compensated radiometric balance showing -20.97 C error on low-eps metal",
        )
    )

    # Ex 17.4: 5*tau_p settling, probe thermal drain, and 2-point barometric calibration
    tau_p = 3.20
    C_p = 0.45
    C_top = 215.0  # house top-layer capacitance (Ex 15.4)
    T_p0 = 21.50
    T_w0 = 49.70  # reference-run top layer (Ex 15.4)
    T_eq = (C_top * T_w0 + C_p * T_p0) / (C_top + C_p)
    T_2tau = T_eq - (T_eq - T_p0) * math.exp(-2.0)
    T_5tau = T_eq - (T_eq - T_p0) * math.exp(-5.0)
    out.append(
        _rec(
            "sec17:ex17.4:probe_eq_temp",
            "sec17",
            "Equilibrium temperature after probe heat-capacity drain [deg C]",
            49.64110,
            T_eq,
            1e-4,
            "Calorimetric energy balance (C_top*T_w0 + C_p*T_p0)/(C_top + C_p)",
        )
    )
    out.append(
        _rec(
            "sec17:ex17.4:probe_2tau_vs_5tau",
            "sec17",
            "Probe reading at 5*tau_p = 16.0 s [deg C]",
            49.45149,
            T_5tau,
            1e-4,
            "First-order step response T_eq - (T_eq - T_p0)*exp(-5)",
        )
    )

    P_mmHg = 742.0
    dP = P_mmHg - 760.0
    T_boil_true = 100.00 + 0.03686 * dP - 0.000020 * (dP ** 2)
    T_read_ice = -0.30
    T_read_boil = 98.90
    T_raw = 44.20
    T_cal = T_boil_true * (T_raw - T_read_ice) / (T_read_boil - T_read_ice)
    out.append(
        _rec(
            "sec17:ex17.4:two_point_calibration",
            "sec17",
            "Two-point ice and barometric boiling calibrated temperature [deg C]",
            44.55835,
            T_cal,
            1e-4,
            "ITS-90 steam point at 742 mmHg (99.330 C) + 2-point linear interpolation",
        )
    )

    # Ex 17.5: JCGM GUM Uncertainty propagation (Rule 4.f correlation & calorimetry)
    u_sys = 0.40 / math.sqrt(3.0)
    u_res = 0.10 / (2.0 * math.sqrt(3.0))
    u_A = 0.050
    u_single = math.sqrt(u_sys**2 + u_res**2 + u_A**2)
    u_TG_uncorr = math.sqrt(2.0) * u_single
    u_TG_corr = math.sqrt(2.0 * (u_res**2 + u_A**2))
    out.append(
        _rec(
            "sec17:ex17.5:gum_rule4f_corr_TG",
            "sec17",
            "Correlated same-thermometer standard uncertainty u(TG) [deg C]",
            0.081650,
            u_TG_corr,
            1e-4,
            "JCGM GUM correlated difference with r_sys = +1 cancelling u_B,sys",
        )
    )
    m_w, u_mw = 100.00, 0.15
    m_x, u_mx = 85.00, 0.05
    dT_w, u_dTw = 5.40, u_TG_corr
    dT_x, u_dTx = 52.60, u_TG_corr
    c_w = 4.184
    c_x = (m_w * c_w * dT_w) / (m_x * dT_x)
    rel_u_cx = math.sqrt(
        (u_mw / m_w) ** 2 + (u_mx / m_x) ** 2 + (u_dTw / dT_w) ** 2 + (u_dTx / dT_x) ** 2
    )
    u_cx = c_x * rel_u_cx
    out.append(
        _rec(
            "sec17:ex17.5:gum_calorimetry_uc",
            "sec17",
            "Calorimetry specific heat combined standard uncertainty u_c(c_x) [J/(g K)]",
            0.007723,
            u_cx,
            1e-3,
            "Quadrature propagation of relative uncertainties in c_x = m_w*c_w*dT_w/(m_x*dT_x)",
        )
    )

    # Ex 17.6: Type T thermocouple CJC & Stefan-Boltzmann T^4 power-law uncertainty
    E_ref = 0.790
    dV_meas = 0.934
    E_tot = E_ref + dV_meas
    T_sense = 40.0 + 10.0 * (E_tot - 1.612) / (2.036 - 1.612)
    out.append(
        _rec(
            "sec17:ex17.6:type_t_cjc_temp",
            "sec17",
            "Type T thermocouple CJC interpolated temperature [deg C]",
            42.64151,
            T_sense,
            1e-4,
            "Law of Intermediate Temperatures E(0,T) = E(0,20) + dV + linear ITS-90 interpolation",
        )
    )
    sigma = 5.670374419e-8
    A_m2 = 50.00e-4
    T_bb = 500.0
    Q_dot_bb = sigma * A_m2 * (T_bb ** 4)
    rel_u_Q = math.sqrt((0.25 / 50.00) ** 2 + (4.0 * 2.5 / 500.0) ** 2)
    u_Q_bb = Q_dot_bb * rel_u_Q
    out.append(
        _rec(
            "sec17:ex17.6:stefan_boltzmann_gum_uQ",
            "sec17",
            "Stefan-Boltzmann blackbody power standard uncertainty u_c(Q_dot) [W]",
            0.365308,
            u_Q_bb,
            1e-4,
            "Power-law GUM propagation Q_dot * sqrt((u_A/A)^2 + (4*u_T/T)^2)",
        )
    )
    return out


def check_sec18() -> list[dict]:
    out = []

    # Ex 18.1: Steam table quality, 2D bilinear interpolation, and Clapeyron central difference
    h_f, h_g = 355.96, 2651.7
    s_f, s_g = 1.1346, 7.5445
    s_mix = 5.942025
    x_qual = (s_mix - s_f) / (s_g - s_f)
    h_mix = h_f + x_qual * (h_g - h_f)
    out.append(
        _rec(
            "sec18:ex18.1:wet_steam_enthalpy",
            "sec18",
            "Two-phase wet steam enthalpy at T=85 C, x=0.750 [kJ/kg]",
            2077.765,
            h_mix,
            1e-4,
            "Lever rule h = h_f + ((s - s_f)/(s_g - s_f))*(h_g - h_f)",
        )
    )

    # Bilinear interpolation at T=172 C between 160 C and 180 C, P=0.35 MPa between 0.30 and 0.40 MPa
    fT = (172.0 - 160.0) / (180.0 - 160.0)
    fP = (0.35 - 0.30) / (0.40 - 0.30)
    h11, h21 = 2782.3, 2824.4
    h12, h22 = 2776.1, 2819.5
    h_P1 = h11 + fT * (h21 - h11)
    h_P2 = h12 + fT * (h22 - h12)
    h_bilin = h_P1 + fP * (h_P2 - h_P1)
    out.append(
        _rec(
            "sec18:ex18.1:bilinear_superheated_h",
            "sec18",
            "Bilinearly interpolated superheated enthalpy h(172 C, 0.35 MPa) [kJ/kg]",
            2804.85,
            h_bilin,
            1e-5,
            "2D bilinear Lagrange interpolation across (T, P) steam grid",
        )
    )

    # Central finite-difference Clapeyron at T=100 C (373.15 K)
    P_95 = 84.609
    P_105 = 120.90
    dP_dT = (P_105 - P_95) / 10.0  # kPa/K
    v_fg = 1.6718 - 0.0010435
    h_fg_clap = 373.15 * v_fg * dP_dT
    out.append(
        _rec(
            "sec18:ex18.1:clapeyron_central_diff",
            "sec18",
            "Central finite-difference Clapeyron latent heat h_fg at 100 C [kJ/kg]",
            2262.55,
            h_fg_clap,
            1e-4,
            "Clapeyron h_fg = T * v_fg * (P(105)-P(95))/(2*5)",
        )
    )

    # Ex 18.2: Composite trapezoidal P-V work integration
    V_L = np.array([2.0, 3.0, 4.0, 5.0, 6.0])
    P_kPa = np.array([420.0, 310.0, 240.0, 195.0, 165.0])
    _trap = getattr(np, "trapezoid", None) or np.trapz  # NumPy 2.x renamed trapz -> trapezoid
    W_trap = float(_trap(P_kPa, V_L))
    out.append(
        _rec(
            "sec18:ex18.2:trapezoidal_pv_work",
            "sec18",
            "Composite trapezoidal boundary work W_by across 5 states [J]",
            1037.5,
            W_trap,
            1e-6,
            "numpy.trapz(P_kPa, V_L) over 4 equal 1.0 L subintervals",
        )
    )

    # Ex 18.3: Semi-log OLS regression, 3-point T_ss estimator, and Grubbs outlier check
    t_min = np.array([0.0, 2.0, 4.0, 6.0, 8.0, 10.0])
    T_meas = np.array([22.00, 26.95, 31.32, 35.10, 38.45, 41.36])
    T_ss = 62.00
    T_i = 22.00
    y_ln = np.log((T_ss - T_meas) / (T_ss - T_i))
    t_bar = float(np.mean(t_min))
    y_bar = float(np.mean(y_ln))
    S_tt = float(np.sum((t_min - t_bar) ** 2))
    S_ty = float(np.sum((t_min - t_bar) * (y_ln - y_bar)))
    S_yy = float(np.sum((y_ln - y_bar) ** 2))
    m_slope = S_ty / S_tt
    b_int = y_bar - m_slope * t_bar
    R2 = (S_ty ** 2) / (S_tt * S_yy)
    tau_min = -1.0 / m_slope
    s_yx = math.sqrt((S_yy - m_slope * S_ty) / (len(t_min) - 2))
    u_m = s_yx / math.sqrt(S_tt)
    u_tau_min = (tau_min ** 2) * u_m

    out.append(
        _rec(
            "sec18:ex18.3:semilog_tau_min",
            "sec18",
            "OLS semi-log extracted time constant tau [min]",
            15.11007,
            tau_min,
            1e-4,
            "Linear least squares of ln((T_ss-T)/(T_ss-T_i)) vs t",
        )
    )
    out.append(
        _rec(
            "sec18:ex18.3:semilog_u_tau",
            "sec18",
            "OLS standard uncertainty of time constant u(tau) [min]",
            0.0104962,
            u_tau_min,
            1e-3,
            "s_yx / sqrt(S_tt) * tau^2",
        )
    )

    T1, T2, T3 = 22.00, 31.32, 38.45
    T_ss_3pt = (T1 * T3 - T2**2) / (T1 + T3 - 2.0 * T2)
    out.append(
        _rec(
            "sec18:ex18.3:three_point_Tss",
            "sec18",
            "Three-point equidistant asymptotic temperature T_ss [deg C]",
            61.6632,
            T_ss_3pt,
            1e-4,
            "Exact algebraic relation (T1*T3 - T2^2)/(T1 + T3 - 2*T2)",
        )
    )

    trials = np.array([21.30, 21.45, 21.20, 21.35, 21.40, 18.90])
    mean_all = float(np.mean(trials))
    sd_all = float(np.std(trials, ddof=1))
    G_stat = float(np.max(np.abs(trials - mean_all)) / sd_all)
    out.append(
        _rec(
            "sec18:ex18.3:grubbs_statistic",
            "sec18",
            "Grubbs outlier test statistic G for N=6 trials",
            2.033673,
            G_stat,
            1e-4,
            "max|x_i - mean| / s_sample with ddof=1 (exceeds G_crit=1.887)",
        )
    )

    # Ex 18.4: Clausius-Clapeyron vapor pressure OLS regression & normal boiling point
    T_cc = np.array([313.15, 333.15, 353.15, 373.15])
    P_cc = np.array([7.384, 19.946, 47.414, 101.42])
    X_cc = 1000.0 / T_cc
    Y_cc = np.log(P_cc)
    m_cc, b_cc = np.polyfit(X_cc, Y_cc, 1)
    dH_vap_kJ = -m_cc * 8.314462618
    X_boil = (math.log(101.325) - b_cc) / m_cc
    T_boil_C = (1000.0 / X_boil) - 273.15
    out.append(
        _rec(
            "sec18:ex18.4:clausius_clapeyron_dHvap",
            "sec18",
            "OLS Clausius-Clapeyron molar enthalpy of vaporization [kJ/mol]",
            42.4337,
            float(dH_vap_kJ),
            1e-4,
            "NumPy polyfit slope of ln(P_sat) vs 1000/T multiplied by -R",
        )
    )
    out.append(
        _rec(
            "sec18:ex18.4:clausius_clapeyron_Tb",
            "sec18",
            "OLS Clausius-Clapeyron predicted normal boiling point [deg C]",
            99.769,
            float(T_boil_C),
            1e-3,
            "Inversion of OLS fit at P = 101.325 kPa",
        )
    )

    # Ex 18.5: Heating curve slope/plateau extraction & binary eutectic lever rule
    Q_dot_h = 250.0
    m_s = 0.400
    c_solid = (Q_dot_h * 112.0) / (m_s * 40.0)
    L_fus = (Q_dot_h * 288.0) / m_s
    c_liq = (Q_dot_h * 224.0) / (m_s * 50.0)
    f_L = (40.0 - 18.0) / (55.5 - 18.0)
    m_Sn_in_L = 0.555 * f_L * 500.0
    out.append(
        _rec(
            "sec18:ex18.5:heating_curve_Lf",
            "sec18",
            "Extracted latent heat of fusion L_f from plateau duration [kJ/kg]",
            180.0,
            L_fus / 1000.0,
            1e-5,
            "Q_dot * dt_fus / m",
        )
    )
    out.append(
        _rec(
            "sec18:ex18.5:eutectic_lever_Sn_mass",
            "sec18",
            "Mass of Sn dissolved in liquid phase via binary lever rule [g]",
            162.80,
            m_Sn_in_L,
            1e-4,
            "w_L * ((w_0 - w_alpha)/(w_L - w_alpha)) * m_tot",
        )
    )
    return out


def check_sec19() -> list[dict]:
    out = []

    # Ex 19.1: Multi-stage heater + phase change + conductive leak + piston expansion
    m = 0.250
    c_ice = 2090.0  # house value
    c_w = 4184.0
    c_steam = 2080.0
    L_f = 333550.0
    L_v = 2256400.0
    P_elec = (48.0 ** 2) / 4.608  # 500.0 W
    R_wall = 2.50
    T_room = 20.0

    # Stage 1: ice -15 to 0 C (T_avg = -7.5 C)
    Q1 = m * c_ice * 15.0
    P_net1 = P_elec + (T_room - (-7.5)) / R_wall
    t1 = Q1 / P_net1
    # Stage 2: melt ice at 0 C
    Q2 = m * L_f
    P_net2 = P_elec + (T_room - 0.0) / R_wall
    t2 = Q2 / P_net2
    # Stage 3: heat water 0 to 100 C (T_avg = 50 C)
    Q3 = m * c_w * 100.0
    P_net3 = P_elec - (50.0 - T_room) / R_wall
    t3 = Q3 / P_net3
    # Stage 4: vaporize water at 100 C
    Q4 = m * L_v
    P_net4 = P_elec - (100.0 - T_room) / R_wall
    t4 = Q4 / P_net4
    t_used = t1 + t2 + t3 + t4
    t_rem = 1800.0 - t_used

    # Stage 5: superheat steam with exact lumped ODE C_steam * dT/dt = P_elec - (T - T_room)/R_wall
    C_steam = m * c_steam
    tau_s = C_steam * R_wall
    T_ss_s = T_room + P_elec * R_wall
    T_final = T_ss_s - (T_ss_s - 100.0) * math.exp(-t_rem / tau_s)

    out.append(
        _rec(
            "sec19:ex19.1:time_to_dry_steam",
            "sec19",
            "Total time to reach 100 C dry saturated steam t_1..4 [s]",
            1599.173,
            t_used,
            1e-4,
            "Piecewise energy balance across subcooled ice, fusion, liquid warming, and vaporization",
        )
    )
    out.append(
        _rec(
            "sec19:ex19.1:final_superheated_temp",
            "sec19",
            "Final superheated steam temperature at t=1800 s [deg C]",
            267.476,
            T_final,
            1e-4,
            "Exact first-order ODE T_ss - (T_ss - 100)*exp(-t_5/(m*c_p*R_wall))",
        )
    )

    # Isobaric expansion work from 0 C ice (rho=916.7 kg/m^3) to ideal steam at T_final (540.57 K) and P=101325 Pa
    n_mol = (m * 1000.0) / 18.01528
    R_gas = 8.314  # house value in examples
    V_init = m / 916.7
    V_final = n_mol * R_gas * (T_final + 273.15) / 101325.0
    W_by_kJ = 101325.0 * (V_final - V_init) / 1000.0
    out.append(
        _rec(
            "sec19:ex19.1:piston_boundary_work",
            "sec19",
            "Isobaric piston expansion work W_by [kJ]",
            62.3467,
            W_by_kJ,
            1e-4,
            "P*(V_final - V_ice) using ideal gas steam volume at 540.57 K",
        )
    )

    # Ex 19.2: Radiative collector + Carnot engine + reversible heat pump cascade
    sigma = 5.670374419e-8
    A_c = 2.00
    alpha_s = 0.92
    eps_ir = 0.10
    G_irr = 1000.0
    T_H = 450.0
    T_0 = 300.0
    Q_dot_H = A_c * (alpha_s * G_irr - eps_ir * sigma * (T_H**4 - T_0**4))
    eta_C = 1.0 - T_0 / T_H
    W_dot = eta_C * Q_dot_H
    COP_HP = 310.0 / (310.0 - 270.0)
    Q_dot_B = COP_HP * W_dot
    out.append(
        _rec(
            "sec19:ex19.2:cascade_building_heat",
            "sec19",
            "Building heating power delivered by radiative-Carnot-HP cascade [W]",
            3789.29,
            Q_dot_B,
            1e-4,
            "Coupled radiative balance * Carnot efficiency * Carnot heat-pump COP",
        )
    )

    # Ex 19.3: Steam Rankine turbine isentropic efficiency & Gouy-Stodola exergy destruction
    h1, s1 = 3116.1, 6.7450
    hf2, hfg2 = 191.81, 2392.1
    sf2, sfg2 = 0.6492, 7.4996
    x2s = (s1 - sf2) / sfg2
    h2s = hf2 + x2s * hfg2
    eta_t = 0.850
    w_t = eta_t * (h1 - h2s)
    h2a = h1 - w_t
    x2a = (h2a - hf2) / hfg2
    s2a = sf2 + x2a * sfg2
    T_dead = 298.15
    x_dest = T_dead * (s2a - s1)
    out.append(
        _rec(
            "sec19:ex19.3:rankine_actual_work",
            "sec19",
            "Actual Rankine turbine specific work w_t [kJ/kg]",
            832.957,
            w_t,
            1e-4,
            "eta_t * (h1 - (h_f + x_2s*h_fg))",
        )
    )
    out.append(
        _rec(
            "sec19:ex19.3:rankine_exergy_destruction",
            "sec19",
            "Gouy-Stodola turbine specific exergy destruction x_dest [kJ/kg]",
            137.402,
            x_dest,
            1e-4,
            "T_0 * (s_2a - s_1) = (1 - eta_t)*(h_1 - h_2s)*(T_0 / T_sat)",
        )
    )

    # Ex 19.4: Two-compartment diathermal piston equilibrium
    n_A, f_A = 1.00, 3
    n_B, f_B = 1.50, 5
    T_init = 300.0
    V_tot_m3 = 0.030
    Q_in = 12471.7
    C_V_tot = (n_A * 0.5 * f_A + n_B * 0.5 * f_B) * R_gas
    T_fin = T_init + Q_in / C_V_tot
    P_fin_kPa = ((n_A + n_B) * R_gas * T_fin / V_tot_m3) / 1000.0
    out.append(
        _rec(
            "sec19:ex19.4:two_compartment_P_final",
            "sec19",
            "Two-compartment diathermal piston final pressure P_f [kPa]",
            405.817,
            P_fin_kPa,
            1e-4,
            "Conservation of internal energy Delta_U = (n_A*C_VA + n_B*C_VB)*Delta_T = Q",
        )
    )

    # Ex 19.5: Pressurized glass-bulb liquid dilatometer
    V_l0 = 50.000 + 0.0200 * 5.00
    dV_app = V_l0 * ((9.50e-4 - 3.0 * 3.25e-6) * 50.00 - 8.20e-5 * 25.00)
    h1_cm = 5.00 + dV_app / 0.0200
    out.append(
        _rec(
            "sec19:ex19.5:dilatometer_meniscus_h1",
            "sec19",
            "Pressurized dilatometer final capillary reading h_1 [cm]",
            117.6311,
            h1_cm,
            1e-4,
            "h_0 + V_l0*((beta_l - 3*alpha_g)*dT - kappa_eff*dP)/A_c",
        )
    )

    # Ex 19.6: Linear spring-loaded piston expansion (k_s = 1.600 kN/m)
    P1_kPa, V1_L, V2_L = 120.0, 10.0, 20.0
    P2_kPa = P1_kPa + (1.600 / (0.0100 ** 2)) * (0.0200 - 0.0100)
    W_spring_J = 0.5 * (P1_kPa + P2_kPa) * (V2_L - V1_L)
    dU_spring_J = 2.5 * (P2_kPa * V2_L - P1_kPa * V1_L)
    Q_spring_kJ = (dU_spring_J + W_spring_J) / 1000.0
    out.append(
        _rec(
            "sec19:ex19.6:spring_piston_heat_Q",
            "sec19",
            "Total heat Q added to spring-loaded piston gas [kJ]",
            13.000,
            Q_spring_kJ,
            1e-5,
            "First Law Q = 2.5*(P2*V2 - P1*V1) + 0.5*(P1 + P2)*(V2 - V1)",
        )
    )

    # Ex 19.7: Planetary radiative equilibrium & vacuum T^4 cooling time
    T_eq_probe = ((0.800 * 1361.0) / (4.0 * 0.250 * sigma)) ** 0.25
    A_surf_probe = math.pi * (0.500 ** 2)
    dt_cool_s = (12500.0 / (3.0 * 0.250 * sigma * A_surf_probe)) * (
        (280.0 ** -3) - (T_eq_probe ** -3)
    )
    out.append(
        _rec(
            "sec19:ex19.7:vacuum_radiative_cooling_time",
            "sec19",
            "Vacuum T^4 radiative cooling duration Delta_t [s]",
            9793.03,
            dt_cool_s,
            1e-4,
            "Closed-form T^-4 integral C_p/(3*eps*sigma*A)*(T_f^-3 - T_i^-3)",
        )
    )

    # Ex 19.8: Two-stage intercooled adiabatic compression work savings
    Cp_m = 3.5 * R_gas
    T_1s = 300.0 * (9.0 ** (2.0 / 7.0))
    W_1s_kJ = 2.0 * Cp_m * (T_1s - 300.0) / 1000.0
    T_2s = 300.0 * (3.0 ** (2.0 / 7.0))
    W_2s_kJ = 2.0 * 2.0 * Cp_m * (T_2s - 300.0) / 1000.0
    out.append(
        _rec(
            "sec19:ex19.8:intercooled_work_saved",
            "sec19",
            "Compressor shaft work saved by 2-stage intercooling [kJ]",
            2.3740,
            W_1s_kJ - W_2s_kJ,
            1e-3,
            "Single-stage minus two-stage adiabatic enthalpy rise",
        )
    )
    return out


def check_sec20() -> list[dict]:
    out = []

    # Ex 20.1: Ice-water mixing two-phase plateau trap vs naive linear solve
    m_ice, T_ice, c_ice, L_f = 80.0, -15.0, 2.09, 333.55
    m_w, T_w, c_w = 120.0, 25.0, 4.184
    Q_avail = m_w * c_w * (T_w - 0.0)
    Q_warm_ice = m_ice * c_ice * (0.0 - T_ice)
    Q_rem = Q_avail - Q_warm_ice
    m_melted = Q_rem / L_f
    T_naive = (Q_avail - Q_warm_ice - m_ice * L_f) / ((m_ice + m_w) * c_w)
    out.append(
        _rec(
            "sec20:ex20.1:naive_impossible_Tf",
            "sec20",
            "Naive un-gated equation false temperature T_f [deg C]",
            -19.8853,
            T_naive,
            1e-4,
            "Demonstrates false T_f < -15 C when skipping plateau inequality check",
        )
    )
    out.append(
        _rec(
            "sec20:ex20.1:true_melted_ice_mass",
            "sec20",
            "True mass of ice melted at 0.00 C two-phase plateau [g]",
            30.11243,
            m_melted,
            1e-4,
            "(m_w*c_w*T_w - m_ice*c_ice*|T_ice|) / L_f",
        )
    )

    # Ex 20.2: Celsius vs Kelvin trap in Carnot and Stefan-Boltzmann
    T_H_K, T_C_K = 227.0 + 273.15, 27.0 + 273.15
    eta_true = 1.0 - T_C_K / T_H_K
    sigma = 5.670374419e-8
    Q_rad_true = sigma * ((127.0 + 273.15) ** 4 - (27.0 + 273.15) ** 4)
    out.append(
        _rec(
            "sec20:ex20.2:carnot_kelvin_efficiency",
            "sec20",
            "True Kelvin Carnot efficiency between 227 C and 27 C",
            0.399880,
            eta_true,
            1e-4,
            "1 - 300.15/500.15 (vs false 0.8811 in Celsius)",
        )
    )
    out.append(
        _rec(
            "sec20:ex20.2:stefan_boltzmann_kelvin",
            "sec20",
            "True net blackbody radiation flux between 127 C and 27 C [W/m^2]",
            993.5746,
            Q_rad_true,
            1e-4,
            "sigma * (400.15^4 - 300.15^4) (vs false 5.67 W/m^2 for (Delta_T)^4)",
        )
    )

    # Ex 20.3: 2027 Device Prediction Estimate (PE) & evaporation/swirling loss audit
    T_pred = 45.0
    T_final = 36.0
    PE_true = 1.0 - abs(T_final - T_pred) / T_final
    pts_lost_PS = 20.0 * (1.0 - PE_true)
    pts_lost_TS = 30.0 * (1.0 - (36.0 - 21.0) / (45.0 - 21.0))
    out.append(
        _rec(
            "sec20:ex20.3:device_pe_true",
            "sec20",
            "2027 Rule 6.f Prediction Estimate PE = 1 - |36.0 - 45.0|/36.0",
            0.750000,
            PE_true,
            1e-5,
            "Official 2027 Rule 6.f formula with T_final in Celsius in denominator",
        )
    )
    out.append(
        _rec(
            "sec20:ex20.3:device_total_points_lost",
            "sec20",
            "Combined TS + PS tournament points lost from evaporation + swirling",
            16.2500,
            pts_lost_PS + pts_lost_TS,
            1e-5,
            "5.00 pts lost on PS + 11.25 pts lost on TS",
        )
    )

    # Ex 20.4: Isobaric compression with gauge pressure & C_V vs C_P
    P_abs_kPa = 150.0 + 101.325
    W_by_J = P_abs_kPa * (8.00 - 12.00)
    dU_J = 2.5 * W_by_J
    Q_J = dU_J + W_by_J
    out.append(
        _rec(
            "sec20:ex20.4:isobaric_compression_Q",
            "sec20",
            "Isobaric compression heat transfer Q with gauge pressure correction [J]",
            -3518.55,
            Q_J,
            1e-5,
            "Q = 3.5 * (P_gauge + P_atm) * (V2 - V1)",
        )
    )

    # Ex 20.5: Bomb calorimeter Delta_U to Delta_H & freezing water entropy
    dU_c_kJ = -(10.500 * 7.780) / 0.0250
    dH_c_kJ = dU_c_kJ + (-1.500) * 8.314462618e-3 * 298.15
    dS_univ_freeze = -333550.0 / 273.15 + 333550.0 / 263.15
    out.append(
        _rec(
            "sec20:ex20.5:bomb_calorimeter_dHc",
            "sec20",
            "Molar enthalpy of combustion from bomb calorimeter [kJ/mol]",
            -3271.318,
            dH_c_kJ,
            1e-4,
            "dU_c + dn_gas * R * T",
        )
    )
    out.append(
        _rec(
            "sec20:ex20.5:freezing_universe_entropy",
            "sec20",
            "Universe entropy generation during freezing at -10 C [J/K]",
            46.4041,
            dS_univ_freeze,
            1e-4,
            "L_f * (1/T_surr - 1/T_m) > 0",
        )
    )

    # Ex 20.6 & 20.7: Critical radius wire vs cup & parasitic thermal mass
    R_wire_bare = 1.0 / (2.0 * math.pi * 0.00100 * 10.0)
    R_wire_ins = math.log(4.0) / (2.0 * math.pi * 0.0400) + 1.0 / (2.0 * math.pi * 0.00400 * 10.0)
    pct_wire_increase = (R_wire_bare / R_wire_ins - 1.0) * 100.0
    TG_loss_Al = (9200.0 / 418.4) - (9200.0 / (418.4 + 0.140 * 900.0))
    out.append(
        _rec(
            "sec20:ex20.7:wire_rcrit_heat_increase_pct",
            "sec20",
            "Percentage heat loss increase on 1 mm wire insulated to r_crit=4 mm [%]",
            67.6232,
            pct_wire_increase,
            1e-4,
            "(R_bare / R_ins - 1) * 100%",
        )
    )
    out.append(
        _rec(
            "sec20:ex20.7:parasitic_sleeve_TG_loss",
            "sec20",
            "Temperature gain lost to 140 g parasitic aluminum sleeve [deg C]",
            5.0888,
            TG_loss_Al,
            1e-4,
            "E_net/C_w - E_net/(C_w + C_Al)",
        )
    )
    return out


def run_checks() -> list[dict]:
    records = []
    records.extend(check_sec17())
    records.extend(check_sec18())
    records.extend(check_sec19())
    records.extend(check_sec20())
    return records


if __name__ == "__main__":
    res = run_checks()
    n_pass = sum(1 for r in res if r["passed"])
    print(f"check_sec17_20: {n_pass}/{len(res)} checks passed.")
    for r in res:
        status = "PASS" if r["passed"] else "FAIL"
        print(f"  [{status}] {r['id']}: {r['detail']}")
    sys.exit(0 if n_pass == len(res) else 1)
