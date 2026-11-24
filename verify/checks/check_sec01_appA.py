#!/usr/bin/env python3
"""Independent numerical verification suite for §1 (14 Quick Sheets QS-01..QS-14)
and Appendices A, B, C (verify/checks/check_sec01_appA.py)."""
import json, math, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
CONST_JSON = ROOT / "research" / "phase3_constants_tables.json"
MAT_JSON = ROOT / "research" / "phase3_materials_optical.json"

def run_checks() -> list[dict]:
    d1 = json.loads(CONST_JSON.read_text(encoding="utf-8"))
    d2 = json.loads(MAT_JSON.read_text(encoding="utf-8"))
    cmap = {c["symbol"]: c["value"] for c in d1["fundamental_constants_CODATA2022"]}
    results = []

    def add(cid: str, sec: str, desc: str, expected: float, computed: float, tol: float, method: str):
        denom = max(abs(expected), 1e-30)
        rel_err = abs(computed - expected) / denom if expected != 0 else abs(computed)
        passed = rel_err <= tol
        results.append({
            "id": cid,
            "section": sec,
            "description": desc,
            "passed": passed,
            "expected": expected,
            "computed": computed,
            "rel_error": rel_err,
            "tolerance": tol,
            "detail": f"exp={expected:.6g}, comp={computed:.6g}, rel_err={rel_err:.2e} <= {tol:.1e}",
            "method": method,
        })

    # 1. CODATA 2022 exact derived constants
    k_B = cmap["k_B"]
    N_A = cmap["N_A"]
    R = cmap["R"]
    h = cmap["h"]
    c = cmap["c"]
    sigma = cmap["sigma"]
    b_wien = cmap["b"]
    c1 = cmap["c_1"]
    c2 = cmap["c_2"]
    e_chg = cmap["e"]
    F_const = cmap["F"]

    add("C01_R_NA_kB", "QS-01/AppA", "Molar gas constant R = N_A * k_B", R, N_A * k_B, 1e-12, "CODATA 2022 exact product N_A*k_B")
    sigma_calc = (2.0 * (math.pi ** 5) * (k_B ** 4)) / (15.0 * (h ** 3) * (c ** 2))
    add("C02_Stefan_Boltzmann", "QS-01/AppA", "Stefan-Boltzmann sigma = 2*pi^5*k_B^4/(15*h^3*c^2)", sigma, sigma_calc, 1e-9, "Exact Planck radiation integral")
    b_calc = (h * c) / (4.965114231744276 * k_B)
    add("C03_Wien_b", "QS-01/AppA", "Wien displacement b = h*c/(4.96511423*k_B)", b_wien, b_calc, 1e-9, "Transcendental Planck root x=4.96511423")
    add("C04_Radiation_c1", "AppA", "First radiation constant c_1 = 2*pi*h*c^2", c1, 2.0 * math.pi * h * (c ** 2), 1e-9, "CODATA 2022 definition")
    add("C05_Radiation_c2", "AppA", "Second radiation constant c_2 = h*c/k_B", c2, (h * c) / k_B, 1e-9, "CODATA 2022 definition")
    add("C06_Faraday_F", "AppA", "Faraday constant F = N_A * e", F_const, N_A * e_chg, 1e-9, "CODATA 2022 exact product")
    add("C07_Vm_STP_1bar", "QS-01/AppA", "Molar volume at IUPAC STP (273.15 K, 100 kPa)", cmap["V_m_STP_1bar"], R * 273.15 / 100000.0, 1e-8, "Ideal gas law V_m = R*T/P")
    add("C08_Vm_STP_1atm", "QS-01/AppA", "Molar volume at traditional STP (273.15 K, 101.325 kPa)", cmap["V_m_STP_1atm"], R * 273.15 / 101325.0, 1e-8, "Ideal gas law V_m = R*T/P")
    add("C09_Loschmidt_n0", "AppA", "Loschmidt constant n_0 = P_atm/(k_B*273.15)", cmap["n_0_1atm"], 101325.0 / (k_B * 273.15), 1e-8, "Number density P/(k_B*T)")

    # 2. Alternative forms of R
    add("C10_R_Latm", "QS-01/AppA", "R in L*atm/(mol*K)", 0.08205736608, R / 101.325, 1e-9, "R / 101.325 kPa/atm")
    add("C11_R_calth", "QS-01/AppA", "R in cal_th/(mol*K)", 1.9872042586, R / 4.184, 1e-9, "R / 4.184 J/cal_th")
    add("C12_R_LTorr", "QS-01/AppA", "R in L*Torr/(mol*K)", 62.36359822, R * 760.0 / 101.325, 1e-8, "R * 760 / 101.325")

    # 3. 8 Temperature scales & 6 exact intersections
    add("C13_Inter_C_F", "QS-01/AppA", "Celsius-Fahrenheit crossover (-40)", -40.0, (9.0 / 5.0) * (-40.0) + 32.0, 1e-12, "Linear intersection T = 1.8*T + 32")
    add("C14_Inter_K_F", "QS-01/AppA", "Kelvin-Fahrenheit crossover (574.5875)", 574.5875, (9.0 / 5.0) * (574.5875 - 273.15) + 32.0, 1e-10, "Linear intersection T = 1.8*(T-273.15)+32")
    add("C15_Inter_C_De", "QS-01/AppA", "Celsius-Delisle crossover (60)", 60.0, 150.0 - 1.5 * 60.0, 1e-12, "Linear intersection T = 150 - 1.5*T")
    add("C16_Inter_F_De", "QS-01/AppA", "Fahrenheit-Delisle crossover (1060/11 = 96.3636...)", 1060.0 / 11.0, 150.0 - 1.5 * ((1060.0 / 11.0 - 32.0) * 5.0 / 9.0), 1e-10, "Exact rational root T_C=1180/33, T_F=T_De=1060/11")
    add("C17_Inter_C_Ro", "QS-01/AppA", "Celsius-Romer crossover (+300/19 = +15.7895...)", 300.0 / 19.0, (21.0 / 40.0) * (300.0 / 19.0) + 7.5, 1e-10, "Exact rational root +300/19")

    # 4. NIST Saturation Water Table checks (0.01 C to 100 C)
    ws = d1["water_ice_steam_properties"]["liquid_water_saturation_0_to_100C"]
    for row in ws:
        tc = row["T_C"]
        if tc in (0.01, 4.0, 20.0, 25.0, 40.0, 60.0, 100.0):
            add(f"C18_Water_Lv_{tc}C", "AppA", f"Water Lv = h_v - h_l at {tc} C", row["L_v_kJ_kg"], row["h_v_kJ_kg"] - row["h_l_kJ_kg"], 1e-3, "NIST IAPWS-95 enthalpy difference")
            pr_calc = (row["cp_l_J_kgK"] * (row["mu_l_uPa_s"] * 1e-6)) / row["k_l_W_mK"]
            add(f"C19_Water_Pr_{tc}C", "AppA", f"Water Prandtl Pr = cp*mu/k at {tc} C", row["Pr_l"], pr_calc, 2e-3, "Dimensionless Prandtl identity")

    # 5. Ideal & Real Gas table checks
    for g in d1["ideal_and_real_gases"][:5]:
        sym = g["symbol"]
        f = g["f_ideal"]
        eq = g["ideal_equipartition"]
        add(f"C20_Gas_gamma_{sym}", "QS-05/AppA", f"Equipartition gamma = (f+2)/f for {sym}", eq["gamma_ideal"], (f + 2.0) / f, 5e-4, "Classical equipartition theorem")
        add(f"C21_Gas_Mayer_{sym}", "QS-05/AppA", f"Mayer relation Cp,m - Cv,m = R for {sym}", R, eq["Cp_m_J_molK"] - eq["Cv_m_J_molK"], 5e-4, "Mayer ideal gas identity")

    # 6. Quick-Sheet Reference Formula & Worked Verification Checks (QS-02..QS-14)
    # QS-02: Bimetallic strip radius of curvature R_curv = d / ((alpha_2 - alpha_1)*Delta_T) (thin equal-modulus limit)
    d_strip = 0.001  # 1.0 mm
    a_brass, a_steel = 19e-6, 12e-6
    dT = 50.0
    R_curv = d_strip / ((a_brass - a_steel) * dT)
    add("C22_QS02_Bimetallic", "QS-02", "Bimetallic strip radius R = d/((a2-a1)*dT)", 2.857142857, R_curv, 1e-6, "Small-angle arc length difference")

    # QS-03: Ice + Water mixing threshold check (50 g ice at 0 C + 200 g water at 30 C)
    m_ice, L_f = 0.050, 333400.0
    m_w, c_w = 0.200, 4184.0
    Q_melt = m_ice * L_f  # 16670 J
    Q_avail = m_w * c_w * 30.0  # 25104 J
    T_f_mix = (Q_avail - Q_melt) / ((m_ice + m_w) * c_w)
    add("C23_QS03_IceMix", "QS-03", "Ice-water calorimeter final temperature T_f (C)", 8.0630975, T_f_mix, 1e-5, "Enthalpy balance relative to 0 C liquid water")

    # QS-04: Binary eutectic lever rule (Al-Cu eutectic at 33.2 wt% Cu, alloy at 20.0 wt% Cu, alpha at 5.65 wt% Cu)
    w_0, w_alpha, w_E = 20.0, 5.65, 33.2
    f_eutectic = (w_0 - w_alpha) / (w_E - w_alpha)
    add("C24_QS04_LeverRule", "QS-04", "Binary eutectic constituent mass fraction", 0.52087114, f_eutectic, 1e-6, "Tie-line mass balance (w0-wa)/(wE-wa)")

    # QS-06: Adiabatic compression work W_by = (P1*V1 - P2*V2)/(gamma - 1)
    P1, V1, V2, gam = 100e3, 0.004, 0.001, 1.4
    P2 = P1 * ((V1 / V2) ** gam)
    W_by = (P1 * V1 - P2 * V2) / (gam - 1.0)
    add("C25_QS06_AdiabaticWork", "QS-06", "Adiabatic reversible compression work W_by (J)", 1000.0 * (1.0 - (4.0 ** 0.4)), W_by, 1e-10, "Closed-form polytropic integral")

    # QS-08: Otto cycle efficiency eta = 1 - r^(1 - gamma) for r=8, gamma=1.4
    eta_otto = 1.0 - (8.0 ** (1.0 - 1.4))
    add("C26_QS08_OttoEff", "QS-08", "Air-standard Otto cycle efficiency at r=8, gamma=1.4", 0.5647247, eta_otto, 1e-6, "1 - r^(1-gamma)")

    # QS-09: Critical radius of cylindrical insulation r_crit = k / h
    add("C27_QS09_CritRadius", "QS-09", "Critical radius r_crit = k/h for k=0.040 W/mK, h=10 W/m2K", 0.0040, 0.040 / 10.0, 1e-12, "dR_cyl/dr_o = 0 extremum")

    # QS-11: Radiation shield reduction factor with N=2 shields of emissivity eps=0.04 between plates of eps=0.04
    # Since all surfaces have identical eps, Q_N / Q_0 = 1 / (N + 1) = 1/3
    add("C28_QS11_RadShields", "QS-11", "Radiation shield factor Q_2/Q_0 for N=2 equal-eps shields", 1.0 / 3.0, 1.0 / (2.0 + 1.0), 1e-12, "Series radiative surface+space resistances")

    # QS-12 & QS-13: 2027 Collector Lumped Heating ODE & Prediction Estimate PE
    P_abs, G_loss, C_eff, T_i, T_inf, t_s = 18.5, 0.440, 440.0, 22.4, 22.0, 600.0
    tau = C_eff / G_loss
    T_ss = T_inf + P_abs / G_loss
    T_f = T_ss - (T_ss - T_i) * math.exp(-t_s / tau)
    add("C29_QS12_CollectorTf", "QS-12/QS-13", "2027 collector final water temperature T_f (C) at t=600 s", 41.18978, T_f, 1e-4, "Exact exponential ODE solution")
    T_f_round = round(T_f, 1)  # 41.2 C per Rule 5.II.g
    T_pred = 42.0
    PE = 1.0 - abs(T_f_round - T_pred) / T_f_round
    add("C30_QS13_Rule6f_PE", "QS-13", "2027 Official Rule 6.f Prediction Estimate PE in Celsius", 1.0 - 0.8 / 41.2, PE, 1e-9, "Rule 6.f PE = 1 - |Tf - Tpred|/Tf")

    return results

if __name__ == "__main__":
    res = run_checks()
    n_ok = sum(1 for r in res if r["passed"])
    print(f"check_sec01_appA: {n_ok}/{len(res)} checks passed.")
    for r in res:
        if not r["passed"]:
            print("FAIL:", r)
    sys.exit(0 if n_ok == len(res) else 1)
