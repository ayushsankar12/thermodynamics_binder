#!/usr/bin/env python3
"""Recomputation checks for worked examples and problem-bank items (binder overhaul).

Every check recomputes a reported value from the example's givens and compares it with
the number PRINTED in the binder. The tolerance comes from the printed precision: a value
printed as "4.45" passes only if the recomputed value rounds to 4.45 (|x - 4.45| <= 0.005).
So a check fails on 4th-digit drift, not just on gross errors.

Constants are the ones each example states (most examples quote R = 8.314463 or
sigma = 5.670374e-8); house constants are applied where the example uses them.

Runnable standalone or through verify/verify_all.py (exposes run_checks()).
"""
import math
import re

R_FULL = 8.314462618          # J/(mol K), CODATA 2018 (exact)
SIG_FULL = 5.670374419e-8     # W/(m^2 K^4)
G0 = 9.80665                  # m/s^2


def _ptol(printed: str):
    """Value and rounding tolerance implied by a printed number such as '6.585e5' or '-1728.9'."""
    s = printed.strip().replace("−", "-").replace(" ", "")
    m = re.fullmatch(r"([+-]?)(\d+)(?:\.(\d*))?(?:[eE]([+-]?\d+))?", s)
    if not m:
        raise ValueError(f"cannot parse printed value {printed!r}")
    dec = len(m.group(3) or "")
    exp = int(m.group(4) or 0)
    return float(s), 0.5 * 10.0 ** (exp - dec)


def chk(cid, sec, desc, printed, computed, method="recomputed from the example's givens", slack=1.0):
    """Pass iff `computed` rounds to `printed` (slack scales the half-unit tolerance)."""
    val, tol = _ptol(printed)
    tol = tol * slack * (1 + 1e-9) + 1e-12
    err = abs(computed - val)
    return {
        "id": cid,
        "section": sec,
        "description": desc,
        "passed": err <= tol,
        "expected": val,
        "computed": computed,
        "tolerance": tol,
        "detail": f"printed={printed} recomputed={computed:.6g} |diff|={err:.3g} (tol {tol:.3g})",
        "method": method,
    }


# --------------------------------------------------------------------------------------
# §0
# --------------------------------------------------------------------------------------
def sec00():
    out = []
    dPE = 0.40 / 32.0
    out += [
        chk("EX-00.2-DPE", "sec00", "PE lost for a 0.40 C miss at Tf = 32.0 C", "0.01250", dPE),
        chk("EX-00.2-DPS", "sec00", "PS points lost [pts]", "0.250", 20 * dPE),
        chk("EX-00.2-DPEK", "sec00", "PE lost if Kelvin denominator were used", "0.001311", 0.40 / 305.15),
        chk("EX-00.2-FACTOR", "sec00", "Kelvin underestimate factor", "9.536", 305.15 / 32.0),
    ]
    return out


# --------------------------------------------------------------------------------------
# §1 (quick-sheet examples; labels ex:01.x print as Worked Example 1.1-1.7)
# --------------------------------------------------------------------------------------
def sec01():
    out = []
    b_app = 181e-6 - 3 * 3.2e-6
    exact = 500.0 * ((1 + 181e-6 * 60.0) - (1 + 3.2e-6 * 60.0) ** 3)
    out += [
        chk("EX-01.2-BAPP", "sec01", "apparent expansion coefficient [1/K]", "171.4e-6", b_app),
        chk("EX-01.2-DV", "sec01", "mercury overflow [mL]", "5.14", b_app * 500.0 * 60.0),
        chk("EX-01.2-EXACT", "sec01", "exact overflow [mL]", "5.142", exact),
    ]
    out += [
        chk("EX-01.4-FA", "sec01", "total alpha fraction", "0.6937", (52.5 - 20.0) / (52.5 - 5.65)),
        chk("EX-01.4-FT", "sec01", "total theta fraction", "0.3063", 1 - (52.5 - 20.0) / (52.5 - 5.65)),
        chk("EX-01.4-FPRIM", "sec01", "primary alpha fraction", "0.4791", (33.2 - 20.0) / (33.2 - 5.65)),
        chk("EX-01.4-FEUT", "sec01", "eutectic microconstituent fraction", "0.5209", (20.0 - 5.65) / (33.2 - 5.65)),
    ]
    Tfp = math.sqrt(400 * 200)
    out += [
        chk("EX-01.7-DS", "sec01", "Delta S_univ for direct contact [J/K]", "117.78", 1000 * math.log(9 / 8)),
        chk("EX-01.7-TF", "sec01", "reversible-engine final T [K]", "282.84", Tfp),
        chk("EX-01.7-W", "sec01", "maximum work [kJ]", "34.31", 1000 * (600 - 2 * Tfp) / 1e3),
    ]
    Gi = 0.040 * 0.0999 / 0.020
    Gb = 237 * 1.00e-4 / 0.020
    out += [
        chk("EX-01.9-GI", "sec01", "insulation conductance [W/K]", "0.200", Gi),
        chk("EX-01.9-GB", "sec01", "bolt conductance [W/K]", "1.185", Gb),
        chk("EX-01.9-RB", "sec01", "bolt resistance [K/W]", "0.844", 1 / Gb),
        chk("EX-01.9-GT", "sec01", "total conductance [W/K]", "1.385", Gi + Gb),
        chk("EX-01.9-RT", "sec01", "total resistance [K/W]", "0.722", 1 / (Gi + Gb)),
        chk("EX-01.9-SHARE", "sec01", "bolt share of heat flow [%]", "85.6", 100 * Gb / (Gi + Gb)),
        chk("EX-01.9-FACTOR", "sec01", "loss increase factor vs. bolt-free panel", "6.92", (Gi + Gb) / (0.040 * 0.100 / 0.020)),
        chk("EX-01.9-PCT", "sec01", "loss increase [%]", "592", 100 * ((Gi + Gb) / 0.200 - 1)),
    ]
    q0 = SIG_FULL * (400.0 ** 4 - 300.0 ** 4) / 1.50
    out += [
        chk("EX-01.11-TS4", "sec01", "shield T^4 [K^4]", "1.685e10", (400.0 ** 4 + 300.0 ** 4) / 2),
        chk("EX-01.11-TS", "sec01", "shield temperature [K]", "360.3", ((400.0 ** 4 + 300.0 ** 4) / 2) ** 0.25),
        chk("EX-01.11-RATIO", "sec01", "q1/q0", "0.02970", 1.50 / 50.5),
        chk("EX-01.11-RED", "sec01", "flux reduction [%]", "97.03", 100 * (1 - 1.50 / 50.5)),
        chk("EX-01.11-Q0", "sec01", "unshielded flux [W/m2]", "661.5", q0),
        chk("EX-01.11-Q1", "sec01", "shielded flux [W/m2]", "19.65", q0 * 1.50 / 50.5),
    ]
    E = 7.5 / 10.0
    out += [
        chk("EX-01.12-T15", "sec01", "T at 15 min [C]", "45.1", 39.5 + 7.5 * E),
        chk("EX-01.12-TSS", "sec01", "steady-state T [C]", "62.0", 22.0 + 10.0 / (1 - E)),
        chk("EX-01.12-TAU", "sec01", "time constant [min]", "17.38", -5.0 / math.log(E)),
    ]
    return out


# --------------------------------------------------------------------------------------
# §2
# --------------------------------------------------------------------------------------
def sec02():
    out = []
    Rv = 19.0 * 0.17611018
    Rth = Rv / 45.0
    Q = 40.0 / Rth
    A_ft2 = 45.0 / 0.3048 ** 2
    out += [
        chk("EX-02.3-RVAL", "sec02", "R-19 in SI [m2 K/W]", "3.346", Rv),
        chk("EX-02.3-RTH", "sec02", "wall resistance [K/W]", "0.07436", Rth),
        chk("EX-02.3-Q", "sec02", "heat leak [W]", "537.9", Q),
        chk("EX-02.3-TONS", "sec02", "heat leak [tons]", "0.153", Q / 3516.85),
        chk("EX-02.3-AFT2", "sec02", "area [ft2]", "484.376", A_ft2),
        chk("EX-02.3-BTUH", "sec02", "heat leak [BTU/h]", "1835.53", A_ft2 * 72.0 / 19.0),
    ]
    out += [
        chk("EX-02.4-P", "sec02", "interpolated Psat(32 C) [kPa]", "4.800", 4.2470 + 0.4 * (5.6290 - 4.2470)),
        chk("EX-02.4-L", "sec02", "interpolated Lv(32 C) [kJ/kg]", "2425.0", 2429.8 + 0.4 * (2417.9 - 2429.8)),
        chk("EX-02.4-EXACT", "sec02", "exact (1+e)^3 - 1", "5.10867e-3", 1.0017 ** 3 - 1),
    ]
    return out


# --------------------------------------------------------------------------------------
# §6
# --------------------------------------------------------------------------------------
def sec06():
    out = []
    Rs = 8.3144626 / 0.0180153
    vid = Rs * 393.15 / 198675.0
    out += [
        chk("EX-06.1-RS", "sec06", "steam gas constant [J/(kg K)]", "461.522", Rs),
        chk("EX-06.1-VID", "sec06", "ideal-gas v_g [m3/kg]", "0.91329", vid),
        chk("EX-06.1-VWRONG", "sec06", "v_g with gauge pressure [m3/kg]", "1.8639", Rs * 393.15 / 97350.0),
        chk("EX-06.1-OVER", "sec06", "gauge-pressure overestimate [%]", "104.1", 100 * (198675.0 / 97350.0 - 1)),
        chk("EX-06.1-Z", "sec06", "compressibility factor", "0.9766", 0.8919 / vid),
    ]
    R, M, T = 8.314463, 0.0280134, 300.0
    vavg = math.sqrt(8 * R * T / (math.pi * M))
    lam = 1.380649e-23 * T / (math.sqrt(2) * math.pi * (3.70e-10) ** 2 * 101325)
    out += [
        chk("EX-06.4-VMP", "sec06", "N2 most-probable speed [m/s]", "422.00", math.sqrt(2 * R * T / M)),
        chk("EX-06.4-VAVG", "sec06", "N2 mean speed [m/s]", "476.17", vavg),
        chk("EX-06.4-VRMS", "sec06", "N2 rms speed [m/s]", "516.84", math.sqrt(3 * R * T / M)),
        chk("EX-06.4-LAM", "sec06", "mean free path [m]", "6.721e-8", lam),
        chk("EX-06.4-Z", "sec06", "collision frequency [1/s]", "7.085e9", vavg / lam),
        chk("EX-06.4-N", "sec06", "number density [1/m3]", "2.446e25", 101325 / (1.380649e-23 * T)),
        chk("EX-06.4-TRATIO", "sec06", "T_false/T_actual shortfall [%]", "10.0", 100 * (1 - 0.75 / (5 / 6))),
    ]
    Vm, a, b = 5.000e-4, 0.3658, 4.286e-5
    Pi = R * 350.0 / Vm
    Pv = R * 350.0 / (Vm - b) - a / Vm ** 2
    dT = -(a * 10.0 / 28.94) * (1 / 5.000e-3 - 1 / 5.000e-2)
    out += [
        chk("EX-06.6-PI", "sec06", "ideal pressure [bar]", "58.201", Pi / 1e5),
        chk("EX-06.6-T1", "sec06", "RT/(Vm-b) [Pa]", "6.3658e6", R * 350.0 / (Vm - b)),
        chk("EX-06.6-PV", "sec06", "van der Waals pressure [bar]", "49.026", Pv / 1e5),
        chk("EX-06.6-Z", "sec06", "Z_vdW", "0.8424", Pv / Pi),
        chk("EX-06.6-DP", "sec06", "pressure reduction [bar]", "9.18", (Pi - Pv) / 1e5),
        chk("EX-06.6-DT", "sec06", "free-expansion temperature drop [K]", "-22.75", dT),
        chk("EX-06.6-T2", "sec06", "final temperature [K]", "327.25", 350.0 + dT),
    ]
    Tf = (3.0 * 600.0 + 7.5 * 300.0) / 10.5
    out += [
        chk("EX-06.7-P1", "sec06", "He initial pressure [kPa]", "997.74", 2 * R * 600 / 10.0),
        chk("EX-06.7-P2", "sec06", "N2 initial pressure [kPa]", "374.15", 3 * R * 300 / 20.0),
        chk("EX-06.7-TF", "sec06", "final temperature [K]", "385.714", Tf),
        chk("EX-06.7-PF", "sec06", "final pressure [kPa]", "534.50", 5 * R * Tf / 30.0),
        chk("EX-06.7-DU1", "sec06", "He energy change [kJ]", "-5.3450", 3 * R * (Tf - 600) / 1e3),
    ]
    return out


# --------------------------------------------------------------------------------------
# §3
# --------------------------------------------------------------------------------------
def sec03():
    out = []
    dT_a = 0.010 / (19.0e-6 * 4.990)
    dT_b = 0.010 / (19.0e-6 * 4.990 - 12.0e-6 * 5.000)
    out += [
        chk("EX-03.2-DTA", "sec03", "brass collar alone: Delta T [C]", "105.47", dT_a),
        chk("EX-03.2-TA", "sec03", "brass collar alone: T (full value in working) [C]", "125.5", 20.0 + dT_a),
        chk("EX-03.2-TA-2SF", "sec03", "brass collar alone: T reported to 2 s.f. [C]", "1.3e2", 20.0 + dT_a),
        chk("EX-03.2-DTB", "sec03", "collar + shaft together: Delta T [C]", "287.27", dT_b),
        chk("EX-03.2-TB-2SF", "sec03", "collar + shaft together: T reported to 2 s.f. [C]", "3.1e2", 20.0 + dT_b),
    ]
    out.append(chk("EX-03.3-DV", "sec03", "ethanol overflow [mL]", "16.365", (1100e-6 - 9.0e-6) * 500.0 * 30.0))
    d, dT, a1, a2 = 5.00e-4, 100.0, 1.2e-6, 19.0e-6
    Rap = d / ((a2 - a1) * dT)
    Rex = d * (1 + 0.5 * (a1 + a2) * dT) / ((a2 - a1) * dT)
    out += [
        chk("EX-03.4-R", "sec03", "bimetal radius, Invar 1.2e-6/K [m]", "0.2809", Rap),
        chk("EX-03.4-DTIP", "sec03", "tip deflection [m]", "0.01139", 0.0800 ** 2 / (2 * Rap)),
        chk("EX-03.4-REX", "sec03", "exact-formula radius [m]", "0.28118", Rex),
        chk("EX-03.4-DTIPEX", "sec03", "exact-formula tip deflection [cm]", "1.138", 100 * 0.0800 ** 2 / (2 * Rex)),
    ]
    W = 2 * 20 * 13.20 * G0 * 1.60
    out += [
        chk("EX-03.5-W", "sec03", "paddle-wheel work [J]", "8284.66", W),
        chk("EX-03.5-DT", "sec03", "temperature rise [K]", "0.35409", W / (5.50 * 4184 + 385)),
        chk("EX-03.5-DTF", "sec03", "temperature rise [F]", "0.637", 1.8 * W / (5.50 * 4184 + 385)),
    ]
    return out


# --------------------------------------------------------------------------------------
# §4
# --------------------------------------------------------------------------------------
def sec04():
    out = []
    cw = 4.184
    C = 100.0 * cw * (60.00 - 35.38) / (35.38 - 20.00) - 150.0 * cw
    cm = (200.0 * cw + C) * (27.86 - 20.00) / (0.2500 * (100.00 - 27.86))
    M = 3 * 8.3145 / (cm / 1000)       # example prints 3R = 24.943
    out += [
        chk("EX-04.1-CCAL", "sec04", "calorimeter constant C_cal [J/K]", "42.17", C),
        chk("EX-04.1-MEQ", "sec04", "water equivalent [g]", "10.08", C / cw),
        chk("EX-04.1-CM", "sec04", "metal specific heat [J/(kg K)]", "383.1", cm),
        chk("EX-04.1-M", "sec04", "Dulong-Petit molar mass [g/mol]", "65.1", M),
        # Identification: closer to Cu (385) than Zn (388); densities for the 250.0 g cylinder
        chk("EX-04.1-VCU", "sec04", "volume of 250.0 g copper (8.96 g/cm3) [cm3]", "27.9", 250.0 / 8.96),
        chk("EX-04.1-VZN", "sec04", "volume of 250.0 g zinc (7.14 g/cm3) [cm3]", "35.0", 250.0 / 7.14),
    ]
    assert abs(cm - 385) < abs(cm - 388)
    # Ex 04.4 (energies relative to 0 C liquid; Cu at -10 C; steam h(130 C) = 2737.2 kJ/kg)
    Eav = 41840.0 + 0.0600 * 2737200 - 385.0
    Enet = Eav - (80 * 2.093 * 10 + 80 * 333.55)
    E100 = (0.3400 * 4184 + 38.50) * 100.0
    ms = (Enet - E100) / 2256.4
    out += [
        chk("EX-04.4-ENET", "sec04", "net energy relative to 0 C liquid [J]", "177328.6", Enet),
        chk("EX-04.4-E100", "sec04", "all-liquid at 100 C checkpoint [J]", "146106.0", E100),
        chk("EX-04.4-E100G", "sec04", "all-vapor at 100 C checkpoint [J]", "913282.0", E100 + 0.3400 * 2256400),
        chk("EX-04.4-MS", "sec04", "uncondensed steam [g]", "13.84", ms),
        chk("EX-04.4-ML", "sec04", "final liquid [g]", "326.16", 340.0 - ms),
        chk("EX-04.4-MCOND", "sec04", "condensed steam (verified-by line) [g]", "46.1626", 60.0 - ms),
        chk("EX-04.4-QCOND", "sec04", "condensation heat (verified-by line) [J]", "104161.4", (60.0 - ms) * 2256.4),
    ]
    c1 = (7200.0 / 7.220 - 55.0) / 0.4000
    c0 = (7200.0 / 7.140 - 55.0) / 0.4000
    out += [
        chk("EX-04.5-C", "sec04", "drift-corrected specific heat [J/(kg K)]", "2355.6", c1),
        chk("EX-04.5-DC", "sec04", "overestimate without correction [J/(kg K)]", "27.9", c0 - c1),
        chk("EX-04.5-PCT", "sec04", "overestimate without correction [%]", "1.19", 100 * (c0 - c1) / c1),
    ]
    q = (204.0 * 4.050 + 18.0) * 6.62
    out += [
        chk("EX-04.6-Q", "sec04", "solution heat [J]", "5588.6", q),
        chk("EX-04.6-DH", "sec04", "neutralization enthalpy [kJ/mol]", "-55.89", -q / 0.1000 / 1e3),
        chk("EX-04.6-CCAL", "sec04", "calorimeter share [kJ/mol]", "1.19", 18.0 * 6.62 / 0.1000 / 1e3),
    ]
    Ct = 33090.5 / 3.1850
    n = 0.8565 / 114.23
    dU = -(Ct * 3.9410 - 48.0) / n / 1e3
    dnRT = -4.5 * 8.31446e-3 * 298.15
    out += [
        chk("EX-04.7-C", "sec04", "bomb heat capacity [J/K]", "10389.5", Ct),
        chk("EX-04.7-CKJ", "sec04", "bomb heat capacity [kJ/K]", "10.389", Ct / 1e3),
        chk("EX-04.7-N", "sec04", "moles of octane", "7.4980e-3", n),
        chk("EX-04.7-Q2", "sec04", "octane-run heat [J]", "40944.9", Ct * 3.9410),
        chk("EX-04.7-QV", "sec04", "net octane heat [J]", "40896.9", Ct * 3.9410 - 48.0),
        chk("EX-04.7-DU", "sec04", "Delta_c U [kJ/mol]", "-5454.4", dU),
        chk("EX-04.7-DNRT", "sec04", "Delta n RT [kJ/mol]", "-11.16", dnRT),
        chk("EX-04.7-DH", "sec04", "Delta_c H [kJ/mol]", "-5465.5", dU + dnRT),
    ]
    out += [
        chk("EX-04.8-CP", "sec04", "oil specific heat [J/(kg K)]", "2000", 24.0 / (1.5e-3 * 8.00)),
        chk("EX-04.8-QLOSS", "sec04", "heat loss [W]", "4.20", 33.00 - 1.800e-3 * 2000 * 8.00),
    ]
    Enet9 = 0.0500 * 4184 * 20.0 - (0.6000 * 2093 * 40.0 + 0.6000 * 333550)
    out += [
        chk("EX-04.9-ENET", "sec04", "net energy [J]", "-246178.0", Enet9),
        chk("EX-04.9-BOUND", "sec04", "Zone I boundary [J]", "-216807.5", -0.6500 * 333550),
        chk("EX-04.9-TF", "sec04", "final temperature [C]", "-21.59", (Enet9 + 0.6500 * 333550) / (0.6500 * 2093)),
    ]
    C = {"cal": 15.0 * 4.184, "gly": 350.0 * 2.427, "Al": 120.0 * 0.897, "Ag": 200.0 * 0.235}
    T0 = {"cal": 18.0, "gly": 18.0, "Al": 140.0, "Ag": 180.0}
    Tf = sum(C[k] * T0[k] for k in C) / sum(C.values())
    out += [
        chk("EX-04.10-SUMC", "sec04", "total heat capacity [J/K]", "1066.85", sum(C.values())),
        chk("EX-04.10-TF", "sec04", "final temperature [C]", "37.45", Tf),
        chk("EX-04.10-QGLY", "sec04", "glycerol heat [J]", "16518.5", C["gly"] * (Tf - 18.0)),
        chk("EX-04.10-QCAL", "sec04", "calorimeter heat [J]", "1220.4", C["cal"] * (Tf - 18.0)),
        chk("EX-04.10-QAL", "sec04", "aluminum heat [J]", "-11038.9", C["Al"] * (Tf - 140.0)),
        chk("EX-04.10-QAG", "sec04", "silver heat [J]", "-6700.0", C["Ag"] * (Tf - 180.0)),
    ]
    Qc = 5.000 * 37.13 * 701.85 / 1e3
    Qm = 5.000 * (0.5 * (37.13 + 47.32) * 301.85 + 0.5 * (47.32 + 54.31) * 400.0) / 1e3
    out += [
        chk("EX-04.11-QC", "sec04", "constant-Cp heat [kJ]", "130.30", Qc),
        chk("EX-04.11-QM", "sec04", "two-interval heat [kJ]", "165.36", Qm),
        chk("EX-04.11-ERR", "sec04", "constant-Cp error [%]", "21.2", 100 * (Qm - Qc) / Qm),
    ]
    return out


# --------------------------------------------------------------------------------------
# §5
# --------------------------------------------------------------------------------------
def sec05():
    out = []
    Pv1 = 0.600 * 4.2470
    Pa1 = 101.325 - Pv1
    w1 = 0.62198 * Pv1 / Pa1
    w2 = 0.62198 * 1.7057 / (101.325 - 1.7057)
    ma = Pa1 * 1e3 * 1000 * 0.028965 / (8.31446 * 303.15)
    out += [
        chk("EX-05.5-PV1", "sec05", "vapor partial pressure [kPa]", "2.5482", Pv1),
        chk("EX-05.5-W1", "sec05", "humidity ratio omega_1 [kg/kg]", "0.016046", w1),
        chk("EX-05.5-TDP", "sec05", "dew point by linear interpolation [C]", "21.26",
            20.0 + 5.0 * (Pv1 - 2.3393) / (3.1699 - 2.3393)),
        chk("EX-05.5-MA", "sec05", "mass of dry air in 1000 m3 room [kg]", "1135.1", ma),
        chk("EX-05.5-W2", "sec05", "humidity ratio omega_2 at 15 C [kg/kg]", "0.010650", w2),
        chk("EX-05.5-MCOND", "sec05", "condensed water [kg]", "6.125", ma * (w1 - w2)),
    ]
    dv = 1.00016e-3 - 1.0908e-3
    slope = 333550 / (273.15 * dv)
    out += [
        chk("EX-05.1-DV", "sec05", "fusion volume change [m3/kg]", "-9.064e-5", dv),
        chk("EX-05.1-SLOPE", "sec05", "Clapeyron slope [MPa/K]", "-13.47", slope / 1e6),
        chk("EX-05.1-SLOPEATM", "sec05", "Clapeyron slope [atm/K]", "-133.0", slope / 101325),
        chk("EX-05.1-DTM", "sec05", "melting-point shift at 150 atm [K]", "-1.121", 149.0 * 101325 / slope),
    ]
    f = 4.184 * 12.0 / 333.55
    mol = 12.0 / (3 * 1.853)
    out += [
        chk("EX-05.6-F", "sec05", "fraction frozen", "0.15053", f),
        chk("EX-05.6-M", "sec05", "ice formed [g]", "30.11", 200.0 * f),
        chk("EX-05.6-MV", "sec05", "ice formed, verified-by line [g]", "30.105", 200.0 * f),
        chk("EX-05.6-MOL", "sec05", "required molality [mol/kg]", "2.1587", mol),
        chk("EX-05.6-MCACL2", "sec05", "CaCl2 mass [g]", "47.91", 0.2000 * mol * 110.98),
    ]
    n = 150.0 / 44.010
    out += [
        chk("EX-05.7-QETH", "sec05", "max heat from ethanol [kJ]", "122.56", 500.0 * 2.440 * 100.46 / 1e3),
        chk("EX-05.7-TF", "sec05", "final bath temperature [C]", "-48.24", 22.00 - 85695 / 1220.0),
        chk("EX-05.7-N", "sec05", "moles of CO2", "3.4083", n),
        chk("EX-05.7-PID", "sec05", "ideal-gas pressure at triple point [MPa]", "5.115", n * R_FULL * 216.59 / 1.200e-3 / 1e6),
        chk("EX-05.7-MMIN", "sec05", "dry ice to hold the plateau [g]", "214.5", 122.56 / 571.3 * 1e3),
    ]
    out += [
        chk("EX-05.8-P", "sec05", "interpolated Psat(70 C) [kPa]", "33.68", (19.946 + 47.414) / 2),
        chk("EX-05.8-HFG", "sec05", "interpolated hfg(70 C) [kJ/kg]", "2332.85", (2357.7 + 2308.0) / 2),
        chk("EX-05.8-VG", "sec05", "interpolated vg(70 C) [m3/kg]", "5.536", (7.667 + 3.405) / 2),
        chk("EX-05.8-X", "sec05", "initial quality", "4.852e-5", (0.003106 - 0.0010030) / (43.34 - 0.0010030)),
    ]
    return out


# --------------------------------------------------------------------------------------
# §7
# --------------------------------------------------------------------------------------
def sec07():
    out = []
    R = 8.314463
    ln2 = math.log(2)
    W23 = R * 900.0 * ln2
    W41 = -R * 300.0 * ln2
    out += [
        chk("EX-07.6-DU12", "sec07", "isochoric 1->2 Delta U = Q [J]", "12471.7", 2.5 * R * 600.0),
        chk("EX-07.6-DH12", "sec07", "isochoric 1->2 Delta H [J]", "17460.4", 3.5 * R * 600.0),
        chk("EX-07.6-DS12", "sec07", "isochoric 1->2 Delta S [J/K]", "22.836", 2.5 * R * math.log(3)),
        chk("EX-07.6-W23", "sec07", "isothermal 2->3 W_by = Q at 900 K [J]", "5186.8", W23),
        chk("EX-07.6-DS23", "sec07", "isothermal 2->3 Delta S [J/K]", "5.763", R * ln2),
        chk("EX-07.6-W41", "sec07", "isothermal 4->1 W_by = Q at 300 K [J]", "-1728.9", W41),
        chk("EX-07.6-WNET", "sec07", "cycle net work [J]", "3457.9", W23 + W41),
        chk("EX-07.6-WNET-2", "sec07", "cycle net work, sum check to 0.01 J [J]", "3457.89", W23 + W41),
    ]
    out += [
        chk("EX-07.2-DU", "sec07", "Delta U A->B [J]", "-300.0", 1.5 * (100.0 * 6.000 - 400.0 * 2.000)),
        chk("EX-07.2-QI", "sec07", "Q along path I [J]", "1300.0", -300.0 + 400.0 * 4.000),
        chk("EX-07.2-QII", "sec07", "Q along path II [J]", "700.0", -300.0 + 0.5 * 500.0 * 4.000),
        chk("EX-07.2-WNET", "sec07", "rectangle cycle work [J]", "1200.0", 300.0 * 4.000),
    ]
    nRT = R_FULL * 298.0
    out += [
        chk("EX-07.3-ISO", "sec07", "isothermal work in [J]", "5152.3", nRT * math.log(8)),
        chk("EX-07.3-TA", "sec07", "T after adiabatic leg [K]", "684.62", 298.0 * 8 ** 0.4),
        chk("EX-07.3-WMAX", "sec07", "maximum-work path [J]", "8036.4", 2.5 * nRT * (8 ** 0.4 - 1)),
        chk("EX-07.3-TB", "sec07", "pre-cool temperature [K]", "129.71", 298.0 / 8 ** 0.4),
        chk("EX-07.3-WMIN", "sec07", "minimum-work path [J]", "3498.1", 2.5 * nRT * (1 - 8 ** -0.4)),
        chk("EX-07.3-W3", "sec07", "3-stage intercooled [J]", "5937.4", 3 * 2.5 * nRT * (2 ** 0.4 - 1)),
        chk("EX-07.3-PRE", "sec07", "3-stage pre-cooled staircase [J]", "4499.7", 3 * 2.5 * nRT * (1 - 2 ** -0.4)),
    ]
    T2 = 300.0 * 4.0 ** 0.25
    W = 2 * R * (300.0 - T2) / 0.25
    dU = 2 * 20.786 * (T2 - 300.0)
    out += [
        chk("EX-07.5-T2", "sec07", "polytropic T2 [K]", "424.264", T2),
        chk("EX-07.5-W", "sec07", "boundary work [kJ]", "-8.2655", W / 1e3),
        chk("EX-07.5-DU", "sec07", "Delta U [kJ]", "5.1659", dU / 1e3),
        chk("EX-07.5-CN", "sec07", "polytropic heat capacity [J/(mol K)]", "-12.472", 20.786 * (1.25 - 1.4) / 0.25),
        chk("EX-07.5-Q", "sec07", "heat [kJ]", "-3.0996", (dU + W) / 1e3),
        chk("EX-07.5-TMAX", "sec07", "chord T_max [K]", "75.170", 250.0 * 5.000 / (2 * R)),
        chk("EX-07.5-TA", "sec07", "chord end temperature [K]", "48.109", 400.0 * 2.000 / (2 * R)),
        chk("EX-07.5-VTURN", "sec07", "heat-reversal volume [L]", "5.833", 1.4 / 2.4 * 10.00),
    ]
    RT = R * 300.0
    muN = (2 * 0.1370 / RT - 3.870e-5) / 29.17
    muHe = (2 * 0.00346 / RT - 2.380e-5) / 20.79
    out += [
        chk("EX-07.7-MUN", "sec07", "N2 JT coefficient [K/bar]", "0.2439", muN * 1e5),
        chk("EX-07.7-DTN", "sec07", "N2 throttle Delta T [K]", "-24.39", muN * -1.000e7),
        chk("EX-07.7-MUHE", "sec07", "He JT coefficient [K/bar]", "-0.1011", muHe * 1e5),
        chk("EX-07.7-DTHE", "sec07", "He throttle Delta T [K]", "10.11", muHe * -1.000e7),
        chk("EX-07.7-X", "sec07", "flash quality", "0.09445", (632.18 - 419.06) / 2256.4),
        chk("EX-07.7-TINVN", "sec07", "N2 max inversion T [K]", "851.5", 2 * 0.1370 / (R * 3.870e-5)),
        chk("EX-07.7-TINVHE", "sec07", "He max inversion T [K]", "34.97", 2 * 0.00346 / (R * 2.380e-5)),
    ]
    out += [
        chk("EX-07.8-V2", "sec07", "nozzle exit speed [m/s]", "868.62", math.sqrt(50.0 ** 2 + 2 * 3.760e5)),
        chk("EX-07.8-TTANK", "sec07", "tank-filling final T [K]", "420.0", 1.4 * 300.0),
    ]
    QH = 2 * R * 390.0 * math.log(2)
    eta = 92.0 / 390.0
    out += [
        chk("EX-07.9-ETA", "sec07", "Carnot efficiency", "0.23590", eta),
        chk("EX-07.9-LN", "sec07", "ln(390/298)", "0.269053", math.log(390.0 / 298.0)),
        chk("EX-07.9-RATIO", "sec07", "1 + Cv/R from P-T adiabat", "4.0833", math.log(3) / math.log(390.0 / 298.0)),
        chk("EX-07.9-QH", "sec07", "Q_H [J]", "4495.3", QH),
        chk("EX-07.9-W", "sec07", "net work [J]", "1060.4", eta * QH),
        chk("EX-07.9-QC", "sec07", "Q_C [J]", "3434.8", 2 * R * 298.0 * math.log(2)),
    ]
    nR = 0.5000 * R
    out += [
        chk("EX-07.10-PLIFT", "sec07", "lift-off pressure [kPa]", "150.0", 100.0 + 50.986 * G0 / 0.01000 / 1e3),
        chk("EX-07.10-T1", "sec07", "T1 [K]", "240.54", 100.0 * 10.00 / nR),
        chk("EX-07.10-T3", "sec07", "T3 [K]", "5532.5", 1150.0 * 20.00 / nR),
        chk("EX-07.10-W", "sec07", "total boundary work [J]", "4000.0", 150.0 * 5.00 + 0.5 * (150.0 + 1150.0) * 5.00),
        chk("EX-07.10-Q", "sec07", "total heat [kJ]", "37.00", (1.5 * (1150.0 * 20.00 - 100.0 * 10.00) + 4000.0) / 1e3),
    ]
    T2c = 1.4 * 10.00 / (1.4 * 2.000 + 8.00) * 300.0
    out += [
        chk("EX-07.11-T2", "sec07", "partial charging T2 [K]", "388.89", T2c),
        chk("EX-07.11-T3", "sec07", "blowdown T3 [K]", "245.54", T2c * 0.2 ** (2 / 7)),
        chk("EX-07.11-MS", "sec07", "steam flow [kg/s]", "1.4211", 10.00 * (419.06 - 84.05) / (2776.5 - 419.06)),
        chk("EX-07.11-N2", "sec07", "final moles in tank", "37.113", 10.00e6 * 12.00e-3 / (R * T2c)),
    ]
    out += [
        chk("EX-07.12-W", "sec07", "ellipse cycle work [J]", "1884.96", math.pi * 3.000 * 200.0),
        chk("EX-07.12-DH", "sec07", "benzene Delta H [kJ/mol]", "-3267.62", -3263.9 - 1.5 * R * 1e-3 * 298.15),
    ]
    nRT2 = 2 * R * 300.0
    out += [
        chk("EX-07.13-WREV", "sec07", "reversible work [J]", "11486.9", nRT2 * math.log(10)),
        chk("EX-07.13-W1", "sec07", "one-step work [J]", "4489.8", nRT2 * 0.9),
        chk("EX-07.13-W2", "sec07", "optimal two-step work [J]", "6822.2", 2 * nRT2 * (1 - 10 ** -0.5)),
    ]
    T2s = 1100.0 * 0.125 ** (0.4 / 1.4)
    T2a = 1100.0 - 0.85 * (1100.0 - T2s)
    w = 1.0062 * (1100.0 - T2a) - 12.00
    QHX = 2.5 * 1.0062 * (T2a - 400.0)
    out += [
        chk("EX-07.14-T2S", "sec07", "isentropic exit T [K]", "607.25", T2s),
        chk("EX-07.14-T2A", "sec07", "actual exit T [K]", "681.16", T2a),
        chk("EX-07.14-W", "sec07", "specific shaft work [kJ/kg]", "409.43", w),
        chk("EX-07.14-WDOT", "sec07", "shaft power [kW]", "1023.6", 2.5 * w),
        chk("EX-07.14-QHX", "sec07", "recuperator duty [kW]", "707.26", QHX),
        chk("EX-07.14-TW", "sec07", "water exit T [K]", "337.26", 295.0 + QHX * 1e3 / (4.000 * 4184.0)),
    ]
    return out


# --------------------------------------------------------------------------------------
# §8 (labels 08.6/08.7/08.8 print as 8.7/8.8/8.6)
# --------------------------------------------------------------------------------------
def sec08():
    out = []
    R = 8.314463
    Tf = 4050.0 / 10.5
    dS1 = R * (3.0 * math.log(Tf / 600.0) + 2.0 * math.log(1.2))
    dS2 = R * (7.5 * math.log(Tf / 300.0) + 3.0 * math.log(0.9))
    out += [
        chk("EX-08.2-DS1", "sec08", "He entropy change [J/K]", "-7.9890", dS1),
        chk("EX-08.2-DS2", "sec08", "N2 entropy change [J/K]", "13.0435", dS2),
        chk("EX-08.2-DSU", "sec08", "entropy generated [J/K]", "5.0545", dS1 + dS2),
        chk("EX-08.2-MIX", "sec08", "mixing entropy [J/K]", "27.979", -R * (2 * math.log(0.4) + 3 * math.log(0.6))),
    ]
    out += [
        chk("EX-08.3-LN84", "sec08", "ln 84", "4.4308", math.log(84)),
        chk("EX-08.3-S", "sec08", "S of Einstein solid [J/K]", "6.117e-23", 1.380649e-23 * math.log(84)),
        chk("EX-08.3-OMEGA", "sec08", "C(100,50)", "1.0089e29", float(math.comb(100, 50))),
        chk("EX-08.3-LNOMEGA", "sec08", "ln C(100,50)", "66.7838", math.log(math.comb(100, 50))),
    ]
    hf = 4.217 * (393.15 - 273.16)
    sf = 4.217 * math.log(393.15 / 273.16)
    dH = 40.65 + (-0.04175) * (310.15 - 373.15)
    out += [
        chk("EX-08.4-HF", "sec08", "h_f(120 C) [kJ/kg]", "506.00", hf),
        chk("EX-08.4-UF", "sec08", "u_f(120 C) [kJ/kg]", "505.79", hf - 198.67 * 0.001060),
        chk("EX-08.4-HG", "sec08", "h_g(120 C) [kJ/kg]", "2708.60", hf + 2202.6),
        chk("EX-08.4-UG", "sec08", "u_g(120 C), from rounded h_g and P v_g [kJ/kg]", "2531.41", 2708.60 - round(198.67 * 0.8919, 2)),
        chk("EX-08.4-SF", "sec08", "s_f(120 C) [kJ/(kg K)]", "1.5356", sf),
        chk("EX-08.4-SG", "sec08", "s_g(120 C) [kJ/(kg K)]", "7.1380", sf + 2202.6 / 393.15),
        chk("EX-08.4-DH37", "sec08", "Kirchhoff Delta_vap H(37 C) [kJ/mol]", "43.280", dH),
        chk("EX-08.4-LV37", "sec08", "L_v(37 C) [kJ/kg]", "2402.4", dH / 0.0180153),
        chk("EX-08.4-MSWEAT", "sec08", "sweat mass [kg]", "2.0813", 5000.0 / 2402.4),
    ]
    dHr = -393.51 - (-110.53 - 241.83)
    dSr = (213.79 + 130.68) - (197.66 + 188.84)
    dGr = dHr - 298.15 * dSr / 1e3
    x = -dGr * 1e3 / (R * 298.15)
    lnK2 = x - (dHr * 1e3 / R) * (1 / 800.0 - 1 / 298.15)
    out += [
        chk("EX-08.5-DH", "sec08", "Delta_r H [kJ/mol]", "-41.15", dHr),
        chk("EX-08.5-DS", "sec08", "Delta_r S [J/(mol K)]", "-42.03", dSr),
        chk("EX-08.5-DG", "sec08", "Delta_r G(298) [kJ/mol]", "-28.62", dGr),
        chk("EX-08.5-LNK", "sec08", "ln K(298)", "11.5447", x),
        chk("EX-08.5-K", "sec08", "K(298)", "1.032e5", math.exp(x)),
        chk("EX-08.5-TSTAR", "sec08", "crossover T [K]", "979.06", dHr * 1e3 / dSr),
        chk("EX-08.5-LNK2", "sec08", "ln K(800)", "1.1315", lnK2),
        chk("EX-08.5-K2", "sec08", "K(800)", "3.100", math.exp(lnK2)),
    ]
    xr = 15400.0 / (R * 310.15)
    dS8 = 69.95 - (130.68 + 0.5 * 205.15)
    dG8 = -285.83 - 298.15 * dS8 / 1e3
    out += [
        chk("EX-08.8-EXP", "sec08", "exponent for K ratio", "5.9719", xr),
        chk("EX-08.8-RATIO", "sec08", "K_ii / K_i", "392.3", math.exp(xr)),
        chk("EX-08.8-DS", "sec08", "fuel-cell Delta_r S [J/(mol K)]", "-163.305", dS8),
        chk("EX-08.8-DG", "sec08", "fuel-cell Delta_r G [kJ/mol]", "-237.14", dG8),
        chk("EX-08.8-E", "sec08", "cell voltage [V]", "1.2289", -dG8 * 1e3 / (2 * 96485.33)),
        chk("EX-08.8-QREV", "sec08", "reversible heat [kJ/mol]", "-48.69", 298.15 * dS8 / 1e3),
    ]
    sgen = (6.9931 - 1.4188) - 2257.2 / 600.0
    out += [
        chk("EX-08.6-XIN", "sec08", "furnace exergy [kJ/kg]", "1128.6", 2257.2 * 0.5),
        chk("EX-08.6-SGEN", "sec08", "boiler entropy generation [kJ/(kg K)]", "1.8123", sgen),
        chk("EX-08.6-XD", "sec08", "boiler exergy destroyed [kJ/kg]", "543.69", 300.0 * sgen),
        chk("EX-08.6-ETAII", "sec08", "second-law efficiency [%]", "9.740", 100 * 109.92 / 1128.6),
        chk("EX-08.6-SGT", "sec08", "turbine entropy generation [kJ/(kg K)]", "0.05738", 0.2 * 109.92 / 383.15),
        chk("EX-08.6-XDT", "sec08", "turbine exergy destroyed [kJ/kg]", "17.213", 300.0 * 0.2 * 109.92 / 383.15),
    ]
    n = 100.0 / 18.0153
    out += [
        chk("EX-08.7-N", "sec08", "moles of ice", "5.55084", n),
        chk("EX-08.7-NR", "sec08", "nR [J/K]", "46.1522", n * R),
        chk("EX-08.7-S0", "sec08", "residual entropy [J/K]", "18.713", n * R * math.log(1.5)),
        chk("EX-08.7-NCO", "sec08", "equivalent moles of CO", "3.2470", n * math.log(1.5) / math.log(2)),
        chk("EX-08.7-SM", "sec08", "R ln(3/2) [J/(mol K)]", "3.371", R * math.log(1.5)),
    ]
    A = 12 * math.pi ** 4 * R / (5 * 2230.0 ** 3)
    Q = 398.0 * 5.000e-4 * 200.0 / 0.2500
    out += [
        chk("EX-08.9-A", "sec08", "Debye coefficient [J/(mol K^4)]", "1.753e-7", A),
        chk("EX-08.9-CV", "sec08", "Cv(10 K) [J/(mol K)]", "1.753e-4", A * 1e3),
        chk("EX-08.9-S", "sec08", "S(10 K) [J/(mol K)]", "5.843e-5", A * 1e3 / 3),
        chk("EX-08.9-U", "sec08", "U(10 K) - U(0) [J/mol]", "4.382e-4", A * 1e4 / 4),
        chk("EX-08.9-Q", "sec08", "rod conduction [W]", "159.20", Q),
        chk("EX-08.9-SGEN", "sec08", "entropy generation [W/K]", "0.21227", Q * (1 / 300.0 - 1 / 500.0)),
        chk("EX-08.9-X", "sec08", "exergy destruction [W]", "63.68", 300.0 * Q * (1 / 300.0 - 1 / 500.0)),
    ]
    return out


# --------------------------------------------------------------------------------------
# §9
# --------------------------------------------------------------------------------------
def sec09():
    out = []
    g = 1.4
    cv, Rs, r, T1, P1, qH = 718.6, 287.05, 9.500, 300.0, 100.0, 800e3
    rg = r ** (g - 1)
    eta = 1 - 1 / rg
    T2 = T1 * rg
    P2 = P1 * r ** g
    T3 = T2 + qH / cv
    P3 = P2 * T3 / T2
    w = eta * qH / 1e3
    v1 = Rs * T1 / (P1 * 1e3)
    v2 = v1 / r
    B = (2.0 ** g - 1) / (g * (2.0 - 1))
    T4 = T3 / rg
    out += [
        chk("EX-09.3-RG", "sec09", "9.5^0.4", "2.46087", rg),
        chk("EX-09.3-ETA", "sec09", "Otto efficiency", "0.59364", eta),
        chk("EX-09.3-T2", "sec09", "T2 [K]", "738.26", T2),
        chk("EX-09.3-P2", "sec09", "P2 [kPa]", "2337.8", P2),
        chk("EX-09.3-T3", "sec09", "T3 [K]", "1851.5", T3),
        chk("EX-09.3-P3", "sec09", "P3 [kPa]", "5863.2", P3),
        chk("EX-09.3-W", "sec09", "w_net [kJ/kg]", "474.91", w),
        chk("EX-09.3-MEP", "sec09", "MEP [kPa]", "616.37", w / (v1 - v2)),
        chk("EX-09.3-BRACKET", "sec09", "Diesel bracket factor at rc = 2", "1.17073", B),
        chk("EX-09.3-ED9", "sec09", "Diesel efficiency at r = 9.5", "0.52426", 1 - B / rg),
        chk("EX-09.3-ED18", "sec09", "Diesel efficiency at r = 18", "0.63158", 1 - B / 18.0 ** 0.4),
        chk("EX-09.3-T4", "sec09", "T4 [K]", "752.39", T4),
        chk("EX-09.3-QC", "sec09", "q_C [kJ/kg]", "325.09", cv * (T4 - T1) / 1e3),
    ]
    T1b, T3b, cp = 300.0, 1470.0, 1.0062
    T2s = math.sqrt(T1b * T3b)
    out += [
        chk("EX-09.4-T2S", "sec09", "T2* = T4* = sqrt(T1 T3) [K]", "664.08", T2s),
        chk("EX-09.4-RP", "sec09", "optimal pressure ratio (T3/T1)^(g/(2(g-1)))", "16.14", (T3b / T1b) ** (g / (2 * (g - 1)))),
        chk("EX-09.4-RP-VIA-T2", "sec09", "same via (T2*/T1)^3.5", "16.14", (T2s / T1b) ** 3.5),
        chk("EX-09.4-WMAX", "sec09", "max net work [kJ/kg]", "444.58", cp * (math.sqrt(T3b) - math.sqrt(T1b)) ** 2),
        chk("EX-09.4-ETA", "sec09", "Brayton efficiency at r_p,opt", "0.54825", 1 - T1b / T2s),
        chk("EX-09.4-BWR", "sec09", "back-work ratio", "0.45175", T2s / T3b),
    ]
    R = 8.314463
    W = R * 600.0 * math.log(2)
    Q12 = R * 900.0 * math.log(2)
    Qv = 2.5 * R * 600.0
    out += [
        chk("EX-09.4-W", "sec09", "Stirling net work [J]", "3457.9", W),
        chk("EX-09.4-Q12", "sec09", "Stirling isothermal heat in [J]", "5186.8", Q12),
        chk("EX-09.4-QV", "sec09", "Stirling isochoric heat [J]", "12471.7", Qv),
        chk("EX-09.4-E0", "sec09", "efficiency, no regenerator [%]", "19.58", 100 * W / (Q12 + Qv)),
        chk("EX-09.4-E85", "sec09", "efficiency, 85% regenerator [%]", "49.00", 100 * W / (Q12 + 0.15 * Qv)),
        chk("EX-09.4-E1", "sec09", "efficiency, ideal regenerator [%]", "66.67", 100 * W / Q12),
        chk("EX-09.4-RATIO", "sec09", "Q_isochor / Q_1->2", "2.404", Qv / Q12),
    ]
    nR = 2 * R
    V1 = nR * 600.0 / 1000.0  # L (kPa L = J)
    out += [
        chk("EX-09.2-V1", "sec09", "V1 [L]", "9.9774", V1),
        chk("EX-09.2-V3", "sec09", "V3 [L]", "112.88", 2 * V1 * 2 ** 2.5),
        chk("EX-09.2-V4", "sec09", "V4 [L]", "56.440", V1 * 2 ** 2.5),
        chk("EX-09.2-QH", "sec09", "Q_H [J]", "6915.8", nR * 600.0 * math.log(2)),
        chk("EX-09.2-QC", "sec09", "Q_C [J]", "3457.9", nR * 300.0 * math.log(2)),
        chk("EX-09.2-W23", "sec09", "adiabatic expansion work [J]", "12471.7", 2 * 2.5 * R * 300.0),
        chk("EX-09.2-WNET", "sec09", "net work [J]", "3457.9", nR * 300.0 * math.log(2)),
    ]
    x = (6.9931 - 1.4188) / 5.8192
    h = 461.29 + x * 2229.6
    wp = 0.001052 * (270.28 - 143.38)
    wt = 2718.6 - h
    out += [
        chk("EX-09.5-X", "sec09", "isentropic exit quality", "0.95792", x),
        chk("EX-09.5-H", "sec09", "isentropic exit enthalpy [kJ/kg]", "2597.1", h),
        chk("EX-09.5-WP", "sec09", "pump work [kJ/kg]", "0.1335", wp),
        chk("EX-09.5-QIN", "sec09", "boiler heat [kJ/kg]", "2257.2", 2718.6 - (461.29 + wp)),
        chk("EX-09.5-WT", "sec09", "ideal turbine work [kJ/kg]", "121.54", wt),
        chk("EX-09.5-ETA", "sec09", "first-law efficiency [%]", "5.379", 100 * (wt - wp) / 2257.2),
        chk("EX-09.5-WTA", "sec09", "actual turbine work [kJ/kg]", "97.23", 0.8 * wt),
        chk("EX-09.5-WNA", "sec09", "actual net work [kJ/kg]", "97.10", 0.8 * wt - wp),
        chk("EX-09.5-MDOT", "sec09", "steam flow [kg/s]", "0.5149", 50.0 / (0.8 * wt - wp)),
        chk("EX-09.5-X4", "sec09", "R134a throttle quality", "0.2767", (243.6 - 186.6) / 206.0),
        chk("EX-09.5-COP", "sec09", "COP_R", "4.139", 149.0 / 36.0),
    ]
    out += [
        chk("EX-09.6-ETA", "sec09", "combined efficiency", "0.5784", 0.38 + 0.32 - 0.38 * 0.32),
        chk("EX-09.6-W2", "sec09", "bottoming power [MW]", "99.20", 0.32 * 310.0),
        chk("EX-09.6-QC2", "sec09", "waste heat [MW]", "210.8", 310.0 - 99.2),
    ]
    r14 = 14.0 ** 0.4
    br = (1.5 * 1.6 ** 1.4 - 1) / ((1.5 - 1) + 1.4 * 1.5 * (1.6 - 1))
    brD = (1.6 ** 1.4 - 1) / (1.4 * (1.6 - 1))
    out += [
        chk("EX-09.7-QH", "sec09", "triangle cycle heat in [J]", "1600.0", 900.0 + (-300.0 + 1000.0)),
        chk("EX-09.7-ETA", "sec09", "triangle cycle efficiency", "0.3750", 600.0 / 1600.0),
        chk("EX-09.7-RG", "sec09", "14^0.4", "2.8738", r14),
        chk("EX-09.7-NUM", "sec09", "Dual numerator", "1.8964", 1.5 * 1.6 ** 1.4 - 1),
        chk("EX-09.7-BR", "sec09", "Dual bracket", "1.0775", br),
        chk("EX-09.7-EDUAL", "sec09", "Dual efficiency", "0.6251", 1 - br / r14),
        chk("EX-09.7-EOTTO", "sec09", "Otto efficiency [%]", "65.20", 100 * (1 - 1 / r14)),
        chk("EX-09.7-BRD", "sec09", "Diesel bracket", "1.1083", brD),
        chk("EX-09.7-EDIESEL", "sec09", "Diesel efficiency [%]", "61.44", 100 * (1 - brD / r14)),
    ]
    for rp, xs, es, er, t2, t4 in ((6.0, "1.6685", "40.07", "66.63", "500.6", "899.0"),
                                   (25.0, "2.5085", "60.14", "49.83", "752.5", "598.0")):
        x = rp ** (2 / 7)
        tag = f"EX-09.8-RP{int(rp)}"
        out += [
            chk(tag + "-X", "sec09", f"rp^(2/7) at rp={rp:g}", xs, x),
            chk(tag + "-ES", "sec09", f"simple Brayton efficiency at rp={rp:g} [%]", es, 100 * (1 - 1 / x)),
            chk(tag + "-ER", "sec09", f"regenerative efficiency at rp={rp:g} [%]", er, 100 * (1 - 0.2 * x)),
            chk(tag + "-T2", "sec09", f"compressor exit T at rp={rp:g} [K]", t2, 300.0 * x),
            chk(tag + "-T4", "sec09", f"turbine exit T at rp={rp:g} [K]", t4, 1500.0 / x),
        ]
    out += [
        chk("EX-09.8-RPSTAR", "sec09", "crossover pressure ratio", "16.719", 5.0 ** 1.75),
        chk("EX-09.8-ESTAR", "sec09", "efficiency at crossover [%]", "55.28", 100 * (1 - 1 / math.sqrt(5))),
        chk("EX-09.8-COP", "sec09", "cascade COP", "1.000", 12.0 / (12.0 / 2 + 18.0 / 3)),
    ]
    Q12 = 2 * R * 800.0 * math.log(5)
    Q34 = 2 * R * 400.0 * math.log(5)
    Qr = 2 * 2.5 * R * 400.0
    out += [
        chk("EX-09.9-Q12", "sec09", "Ericsson isothermal heat in [J]", "21410.6", Q12),
        chk("EX-09.9-Q34", "sec09", "Ericsson isothermal heat out [J]", "10705.3", Q34),
        chk("EX-09.9-W", "sec09", "Ericsson net work [J]", "10705.3", Q12 - Q34),
        chk("EX-09.9-QR", "sec09", "regenerator load [J]", "16628.9", Qr),
        chk("EX-09.9-E0", "sec09", "efficiency without regenerator [%]", "28.14", 100 * (Q12 - Q34) / (Q12 + Qr)),
        chk("EX-09.9-MULT", "sec09", "heating multiplier", "7.750", 0.25 + 0.75 * 300.0 / 30.0),
    ]
    return out


# --------------------------------------------------------------------------------------
# §10
# --------------------------------------------------------------------------------------
def planck_fraction(lT):
    """F(0 -> lambda T) for a blackbody, lambda T in um K (series form)."""
    x = 14387.768775 / lT
    tot = 0.0
    for n in range(1, 400):
        tot += math.exp(-n * x) / n * (x ** 3 + 3 * x ** 2 / n + 6 * x / n ** 2 + 6 / n ** 3)
    return 15 / math.pi ** 4 * tot


def sec10():
    out = []
    Ab = math.pi * 0.00400 ** 2
    Gc = 0.0400 * (0.0300 - Ab) / 0.0150
    Gb = 54.0 * Ab / 0.0150
    out += [
        chk("EX-10.2-RPURE", "sec10", "pure cork resistance [K/W]", "12.50", 0.0150 / (0.0400 * 0.0300)),
        chk("EX-10.2-GB", "sec10", "bolt conductance [W/K]", "0.18096", Gb),
        chk("EX-10.2-REQ", "sec10", "wall with bolts [K/W]", "3.834", 1 / (Gc + Gb)),
        chk("EX-10.2-F", "sec10", "bolt share [%]", "69.38", 100 * Gb / (Gc + Gb)),
        chk("EX-10.2-BALSA", "sec10", "wall with balsa dowels [K/W]", "12.49", 1 / (Gc + 0.050 * Ab / 0.0150)),
    ]
    out += [
        chk("EX-10.3-Q", "sec10", "steel plates heat rate [W]", "333.3", 40.0 / 0.1200),
        chk("EX-10.3-DTC", "sec10", "contact temperature jump [K]", "6.67", 40.0 / 0.1200 * 0.0200),
        chk("EX-10.5-Q", "sec10", "spherical shell loss [W]", "7.238", 60.0 / ((0.120 - 0.080) / (4 * math.pi * 0.0400 * 0.080 * 0.120))),
        chk("EX-10.6-KCU", "sec10", "Wiedemann-Franz Cu [W/(m K)]", "426.3", 2.443e-8 * 293.15 / 1.68e-8),
        chk("EX-10.6-K6061", "sec10", "Wiedemann-Franz 6061 [W/(m K)]", "179.5", 2.443e-8 * 293.15 / 3.99e-8),
        chk("EX-10.7-K", "sec10", "guarded hot plate k [W/(m K)]", "0.0400", (4.200 / 2) * 0.0120 / (0.0250 * 25.2)),
    ]
    S1 = 6 * 0.240 ** 2 / 0.0300
    S = S1 + 0.54 * 12 * 0.240 + 0.15 * 8 * 0.0300
    out += [
        chk("EX-10.8-Q1D", "sec10", "naive 1-D box loss [W]", "11.06", S1 * 0.0400 * 24.0),
        chk("EX-10.8-S", "sec10", "3-D shape factor [m]", "13.1112", S),
        chk("EX-10.8-Q3D", "sec10", "3-D box loss [W]", "12.59", S * 0.0400 * 24.0),
        chk("EX-10.8-INC", "sec10", "3-D increase [%]", "13.8", 100 * (S / S1 - 1)),
        chk("EX-10.10-KX", "sec10", "cut-bar k_x with the stated 14.41 K [W/(m K)]", "167.0", 109.0 * 30.0 / 25.0 * 18.40 / 14.41),
    ]
    num = 917.0 * 3.335e5 * (0.0800 ** 2 - 0.0200 ** 2)
    out += [
        chk("P10.1-DT", "sec10", "ice growth time [s]", "27613", num / (2 * 2.215 * 15.0)),
        chk("P10.1-DTH", "sec10", "ice growth time [h]", "7.670", num / (2 * 2.215 * 15.0) / 3600),
        chk("P10.2-KPAR", "sec10", "in-plane k [W/(m K)]", "265.5", 2 / 3 * 398 + 1 / 3 * 0.350),
        chk("P10.2-KSER", "sec10", "through-plane k [W/(m K)]", "1.048", 1 / ((2 / 3) / 398 + (1 / 3) / 0.350)),
    ]
    Rb = 1 / (4 * math.pi * 0.00100 ** 2 * 110)
    Rm = 0.00300 / (4 * math.pi * 0.220 * 0.00100 * 0.00400) + 1 / (4 * math.pi * 0.00400 ** 2 * 110)
    out += [
        chk("P10.3-RBARE", "sec10", "bare bead resistance [K/W]", "723.43", Rb),
        chk("P10.3-RMIN", "sec10", "critical-radius resistance [K/W]", "316.50", Rm),
        chk("P10.3-GAIN", "sec10", "heat transfer increase [%]", "128.6", 100 * (Rb / Rm - 1)),
    ]
    A = math.pi / 4 * 0.0300 ** 2
    Q = 1.45 * 4.184 * (22.85 - 18.20)
    out += [
        chk("P10.4-Q", "sec10", "Searle's bar heat rate [W]", "28.211", Q),
        chk("P10.4-K", "sec10", "brass k [W/(m K)]", "103.2", Q * 0.150 / (A * 58.0)),
    ]
    a, b, c = 6.25e-5, 0.100, -75.625
    Tm = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
    out += [
        chk("P10.5-Q", "sec10", "firebrick heat rate [W]", "975.0", 0.1625 * 1.50 * 800.0 / 0.200),
        chk("P10.5-TMID", "sec10", "midplane temperature [C]", "560.1", Tm),
    ]
    RA = (math.log(1.5) / 0.0250 + math.log(4 / 3) / 0.0500) / (2 * math.pi)
    RB = (math.log(1.5) / 0.0500 + math.log(4 / 3) / 0.0250) / (2 * math.pi)
    out += [
        chk("P10.6-RA", "sec10", "A inner [K/W]", "3.4970", RA),
        chk("P10.6-RB", "sec10", "B inner [K/W]", "3.1221", RB),
        chk("P10.6-INC", "sec10", "resistance gain [%]", "12.01", 100 * (RA / RB - 1)),
        chk("P10.7-Q", "sec10", "fuel pin surface flux [W/m2]", "4.50e5", 1.50e8 * 0.00600 / 2),
        chk("P10.7-DT", "sec10", "fuel pin centerline excess [K]", "450.0", 1.50e8 * 0.00600 ** 2 / (4 * 3.00)),
    ]
    Sb = 2 * math.pi * 25.0 / math.log(30.0)
    out += [
        chk("P10.8-S", "sec10", "buried pipe shape factor [m]", "46.184", Sb),
        chk("P10.8-Q", "sec10", "buried pipe loss [W]", "3071", Sb * 0.950 * 70.0),
        chk("P10.9-KSER", "sec10", "cork series bound [W/(m K)]", "0.0323", 1 / (0.220 / 0.190 + 0.780 / 0.0262)),
        chk("P10.9-KPAR", "sec10", "cork parallel bound [W/(m K)]", "0.0622", 0.220 * 0.190 + 0.780 * 0.0262),
        chk("P10.9-KME", "sec10", "Maxwell-Eucken k [W/(m K)]", "0.0536",
            0.190 * (2 * 0.190 + 0.0262 - 2 * 0.780 * (0.190 - 0.0262)) / (2 * 0.190 + 0.0262 + 0.780 * (0.190 - 0.0262))),
    ]
    G = 0.0420 * 0.280 / 0.0350
    Gs = 167 * 8 * math.pi / 4 * 0.00400 ** 2 / 0.0350
    out += [
        chk("P10.10-QC", "sec10", "cork enclosure loss [W]", "10.75", G * 32.0),
        chk("P10.10-QS", "sec10", "screw leak [W]", "15.35", Gs * 32.0),
        chk("P10.10-SHARE", "sec10", "screw share [%]", "58.8", 100 * Gs / (G + Gs)),
    ]
    return out


# --------------------------------------------------------------------------------------
# §11
# --------------------------------------------------------------------------------------
def sec11():
    out = []
    Tf = 303.15
    Ra = G0 * (1 / Tf) * 14.0 * 0.300 ** 3 / (1.60e-5 * 2.25e-5)
    num = 0.670 * Ra ** 0.25
    den = (1 + (0.492 / 0.711) ** (9 / 16)) ** (4 / 9)
    Nu = 0.68 + num / den
    h = 0.0265 / 0.300 * Nu
    Q = h * 0.0900 * 14.0
    Nu2 = 0.68 + 0.670 * (2 * Ra) ** 0.25 / den
    h2 = 0.0265 / 0.300 * Nu2
    Q2 = h2 * 0.0900 * 28.0
    out += [
        chk("EX-11.1-RA", "sec11", "Ra_L", "3.397e7", Ra),
        chk("EX-11.1-NUM", "sec11", "0.670 Ra^(1/4)", "51.15", num),
        chk("EX-11.1-DEN", "sec11", "[1 + (0.492/Pr)^(9/16)]^(4/9)", "1.3027", den),
        chk("EX-11.1-NU", "sec11", "Churchill-Chu Nu_L", "39.94", Nu),
        chk("EX-11.1-H", "sec11", "h [W/(m2 K)]", "3.53", h),
        chk("EX-11.1-H-4SF", "sec11", "h used in working [W/(m2 K)]", "3.528", h),
        chk("EX-11.1-Q", "sec11", "convective loss [W]", "4.45", Q),
        chk("EX-11.1-NU2", "sec11", "Nu_L at doubled Delta T", "47.37", Nu2),
        chk("EX-11.1-H2", "sec11", "h at doubled Delta T [W/(m2 K)]", "4.18", h2),
        chk("EX-11.1-Q2", "sec11", "loss at doubled Delta T [W]", "10.5", Q2),
        chk("EX-11.1-RATIO", "sec11", "Q2/Q1 including the 0.68 term", "2.37", Q2 / Q),
        chk("EX-11.1-POWLAW", "sec11", "pure power-law ratio 2^(5/4)", "2.38", 2 ** 1.25),
    ]
    dc = (1708 * 1.62e-5 * 2.28e-5 / (G0 * (1 / 305.0) * 15.0)) ** (1 / 3)
    hrad = 4 * 5.6704e-8 * 305.0 ** 3 / 49.0
    out += [
        chk("EX-11.2-DC", "sec11", "critical gap [mm]", "10.94", 1000 * dc),
        chk("EX-11.2-HRAD", "sec11", "foil-gap radiative conductance [W/(m2 K)]", "0.1313", hrad),
        chk("EX-11.2-KEFF", "sec11", "effective gap conductivity [W/(m K)]", "0.02781", 0.0265 + hrad * 0.0100),
    ]
    TGt = 3220 / 188.28
    TGb = 5400 / 418.4
    out += [
        chk("EX-11.4-TGTOP", "sec11", "top-layer gain [C]", "17.10", TGt),
        chk("EX-11.4-TGBOT", "sec11", "bottom-layer gain [C]", "9.47", 2180 / 230.12),
        chk("EX-11.4-TGBULK", "sec11", "mixed gain [C]", "12.91", TGb),
        chk("EX-11.4-LOSS", "sec11", "gain lost by swirling [C]", "4.20", TGt - TGb),
        chk("EX-11.4-PCT", "sec11", "gain lost by swirling [%]", "24.5", 100 * (TGt - TGb) / TGt),
        chk("EX-11.5-RATIO", "sec11", "Gr/Re^2", "2.174", (3.3967e7 / 0.711) / (0.250 * 0.300 / 1.60e-5) ** 2),
    ]
    A = math.pi * 0.0150 * 1.20
    NTU = 1850 * A / 83.60
    To = 80.0 - 60.0 * math.exp(-NTU)
    lm = (60.0 - (80.0 - To)) / math.log(60.0 / (80.0 - To))
    out += [
        chk("EX-11.6-NTU", "sec11", "NTU", "1.2514", NTU),
        chk("EX-11.6-EXP", "sec11", "exp(-NTU)", "0.28611", math.exp(-NTU)),
        chk("EX-11.6-TO", "sec11", "outlet temperature [C]", "62.83", To),
        chk("EX-11.6-Q", "sec11", "heat rate [W]", "3581", 83.60 * (To - 20.0)),
        chk("EX-11.6-DTOUT", "sec11", "outlet Delta T [K]", "17.167", 80.0 - To),
        chk("EX-11.6-LMTD", "sec11", "LMTD [K]", "34.23", lm),
        chk("EX-11.6-ARITH", "sec11", "arithmetic mean Delta T [K]", "38.58", (60.0 + 80.0 - To) / 2),
    ]
    RaD = G0 * (1 / 313.15) * 34.0 * 0.160 ** 3 / (1.70e-5 * 2.40e-5)
    den = (1 + (0.492 / 0.708) ** (9 / 16)) ** (4 / 9)
    Nu = 0.560 * (RaD / 64) ** 0.25 / den
    NuD = 0.82 * RaD ** 0.2 * 0.708 ** 0.034
    out += [
        chk("EX-11.7-RAD", "sec11", "Ra_D", "1.0689e7", RaD),
        chk("EX-11.7-RAL", "sec11", "Ra_L*", "1.6702e5", RaD / 64),
        chk("EX-11.7-NUM", "sec11", "0.560 Ra^(1/4)", "11.321", 0.560 * (RaD / 64) ** 0.25),
        chk("EX-11.7-DEN", "sec11", "Pr denominator", "1.3033", den),
        chk("EX-11.7-NU", "sec11", "Nu up", "8.686", Nu),
        chk("EX-11.7-HUP", "sec11", "h up [W/(m2 K)]", "5.907", 0.0272 / 0.0400 * Nu),
        chk("EX-11.7-NUD", "sec11", "Nu down", "20.630", NuD),
        chk("EX-11.7-HDN", "sec11", "h down [W/(m2 K)]", "3.507", 0.0272 / 0.160 * NuD),
    ]
    Nux = 0.332 * 1e5 ** 0.5 * 0.71 ** (1 / 3)
    out += [
        chk("P11.1-NU", "sec11", "trailing-edge Nu", "93.66", Nux),
        chk("P11.1-HX", "sec11", "trailing-edge h [W/(m2 K)]", "6.205", 0.0265 / 0.400 * Nux),
        chk("P11.1-HBAR", "sec11", "average h [W/(m2 K)]", "12.41", 2 * 0.0265 / 0.400 * Nux),
        chk("P11.2-H", "sec11", "droplet h [W/(m2 K)]", "104.8", 2 * 0.0262 / 0.000500),
        chk("P11.3-H2", "sec11", "half-diameter h [W/(m2 K)]", "8357", 2 ** 1.8 * 2400),
        chk("P11.4-TDB", "sec11", "dry-bulb temperature [C]", "38.21", 18.0 + 2.458e6 * 3.70e-4 / 45.0),
        chk("P11.5-RA", "sec11", "cell Rayleigh number", "888.9", 7.20e4 / 81),
    ]
    lmp = 65.0 / math.log(14.0)
    lmc = 15.0 / math.log(1.5)
    out += [
        chk("P11.6-LMPAR", "sec11", "parallel-flow LMTD [K]", "24.63", lmp),
        chk("P11.6-APAR", "sec11", "parallel-flow area [m2]", "1.218", 12000 / (400.0 * lmp)),
        chk("P11.6-LMCF", "sec11", "counterflow LMTD [K]", "36.99", lmc),
        chk("P11.6-ACF", "sec11", "counterflow area [m2]", "0.8109", 12000 / (400.0 * lmc)),
    ]
    st = 0.00420 / (2 * 0.712 ** (2 / 3))
    out += [
        chk("P11.7-PR", "sec11", "Pr^(2/3)", "0.79736", 0.712 ** (2 / 3)),
        chk("P11.7-ST", "sec11", "Stanton number", "0.002634", st),
        chk("P11.7-H", "sec11", "h [W/(m2 K)]", "37.42", 1.177 * 1006 * 12.0 * st),
    ]
    As = math.pi * 0.00120 * 0.0250
    h = 0.720 / (As * 54.0)
    Nu8 = h * 0.00120 / 0.0277
    Re = (Nu8 / (0.683 * 0.709 ** (1 / 3))) ** (1 / 0.466)
    out += [
        chk("P11.8-H", "sec11", "probe h [W/(m2 K)]", "141.47", h),
        chk("P11.8-NU", "sec11", "probe Nu", "6.1287", Nu8),
        chk("P11.8-RE", "sec11", "Re_D", "141.8", Re),
        chk("P11.8-U", "sec11", "air speed [m/s]", "2.09", 1.77e-5 * Re / 0.00120),
    ]
    return out


# --------------------------------------------------------------------------------------
# §12
# --------------------------------------------------------------------------------------
def sec12():
    out = []
    M = 0.350 * SIG_FULL * 2400.0 ** 4
    out += [
        chk("EX-12.1-WIEN", "sec12", "Wien peak at 2400 K [um]", "1.2074", 2897.772 / 2400.0),
        chk("EX-12.1-M", "sec12", "filament exitance M [W/m2]", "6.585e5", M),
        chk("EX-12.1-M-WORK", "sec12", "exitance as carried in working [W/m2]", "6.5845e5", M),
        chk("EX-12.1-L", "sec12", "Lambertian radiance [W/(m2 sr)]", "2.096e5", M / math.pi),
        chk("EX-12.1-A", "sec12", "filament area [cm2]", "1.898", 125.0 / M * 1e4),
    ]
    T1, T2 = 318.15, 295.15
    dEb = SIG_FULL * (T1 ** 4 - T2 ** 4)
    Ts = ((T1 ** 4 + T2 ** 4) / 2) ** 0.25
    out += [
        chk("EX-12.3-DEB", "sec12", "sigma (T1^4 - T2^4) [W/m2]", "150.64", dEb),
        chk("EX-12.3-CARD", "sec12", "cardboard walls eps = 0.92 [W/m2]", "128.3", dEb / (2 / 0.92 - 1)),
        chk("EX-12.3-FOIL", "sec12", "foil walls eps = 0.04 [W/m2]", "3.074", dEb / 49),
        chk("EX-12.3-2SH", "sec12", "foil walls + 2 shields [W/m2]", "1.025", dEb / 147),
        chk("EX-12.3-DROP0", "sec12", "card/foil drop factor", "41.7", (dEb / (2 / 0.92 - 1)) / (dEb / 49)),
        chk("EX-12.3-DROP2", "sec12", "card/2-shield drop factor", "125.2", (dEb / (2 / 0.92 - 1)) / (dEb / 147)),
        chk("EX-12.3-TS-K", "sec12", "single shield temperature [K]", "307.30", Ts),
        chk("EX-12.3-TS-C", "sec12", "single shield temperature [C]", "34.15", Ts - 273.15),
    ]
    from scipy.optimize import brentq
    s = 5.6704e-8
    def plate(a, e):
        return brentq(lambda T: 8.00 * (T - 308.15) + e * s * (T ** 4 - 291.15 ** 4) - 600.0 * a, 250, 500, xtol=1e-10)
    Tb, Tw, Tsel = plate(0.90, 0.90), plate(0.26, 0.90), plate(0.95, 0.09)
    out += [
        chk("EX-12.4-BLACK", "sec12", "black plate [C]", "64.97", Tb - 273.15),
        chk("EX-12.4-WHITE-K", "sec12", "white plate [K]", "312.59", Tw),
        chk("EX-12.4-WHITE", "sec12", "white plate [C]", "39.44", Tw - 273.15),
        chk("EX-12.4-COOLER", "sec12", "white vs black [C]", "25.5", Tb - Tw),
        chk("EX-12.4-SEL", "sec12", "selective plate [C]", "98.64", Tsel - 273.15),
        chk("EX-12.4-GAIN", "sec12", "selective boost [C]", "33.7", Tsel - Tb),
        chk("EX-12.6-F", "sec12", "crossed-string view factor", "0.4142", math.sqrt(2) - 1),
        chk("EX-12.6-CAV", "sec12", "cavity absorptance", "0.9375", 0.750 / (0.750 + 0.250 * 0.200)),
    ]
    Tm = (345.45 + 308.15) / 2
    hr = 4 * 0.900 * SIG_FULL * Tm ** 3
    ql = hr * 1.3345e-4 * 37.30
    qe = 0.900 * SIG_FULL * 1.3345e-4 * (345.45 ** 4 - 308.15 ** 4)
    out += [
        chk("EX-12.7-HRAD", "sec12", "linearized h_rad [W/(m2 K)]", "7.125", hr),
        chk("EX-12.7-QLIN", "sec12", "linearized loss [W]", "0.03546", ql),
        chk("EX-12.7-QEX", "sec12", "exact loss [W]", "0.03558", qe),
        chk("EX-12.7-FRAC", "sec12", "fractional difference", "0.00325", (qe - ql) / qe),
        chk("EX-12.7-TAYLOR", "sec12", "Taylor remainder", "0.003257", 0.25 * (37.30 / Tm) ** 2),
    ]
    T2 = 2400 * 0.8 ** 0.25
    Ts4 = (20.250 * 400.0 ** 4 + 1.500 * 300.0 ** 4) / 21.750
    out += [
        chk("P12.1-F", "sec12", "gray transfer factor", "0.04040", 1 / (1 / 0.050 + 0.250 * 19.0)),
        chk("P12.2-T2", "sec12", "100 W filament T [K]", "2270", T2),
        chk("P12.2-LAM", "sec12", "100 W Wien peak [um]", "1.277", 2897.77 / T2),
        chk("P12.3-TS4", "sec12", "asymmetric shield T^4 [K^4]", "2.4393e10", Ts4),
        chk("P12.3-TS", "sec12", "asymmetric shield T [K]", "395.2", Ts4 ** 0.25),
        chk("P12.3-FLIP", "sec12", "flipped shield T [K]", "310.6", ((1.500 * 400.0 ** 4 + 20.250 * 300.0 ** 4) / 21.750) ** 0.25),
        chk("P12.4-SIN", "sec12", "sin theta_s", "0.3026", 6.35 / math.sqrt(6.35 ** 2 + 20.0 ** 2)),
        chk("P12.4-C20", "sec12", "C_max at 20 cm", "10.92", 1 + (20.0 / 6.35) ** 2),
        chk("P12.4-C35", "sec12", "C_max at 35 cm", "31.38", 1 + (35.0 / 6.35) ** 2),
    ]
    # Planck fraction table rows and P12.5 (table values are printed to 5 decimals)
    for lT, val in ((1000, "0.00032"), (1400, "0.00779"), (1680, "0.02661"), (1800, "0.03934"), (2000, "0.06673"),
                    (2200, "0.10089"), (2400, "0.14026"), (2600, "0.18312"), (2880, "0.24603"), (2897.8, "0.25006"),
                    (3200, "0.31810"), (3600, "0.40361"), (3800, "0.44338"), (4000, "0.48088"), (4107.2, "0.50000"),
                    (4600, "0.57928"), (5000, "0.63375"), (6000, "0.73782"), (6480, "0.77492"), (7000, "0.80811"),
                    (8000, "0.85629"), (10000, "0.91420"), (15000, "0.96898"), (25000, "0.99222")):
        # slack 12 = +/-6e-5: the source table used an older second radiation constant
        out.append(chk(f"TAB-12.F-{lT:g}", "sec12", f"Planck fraction F(0->{lT:g} um K)", val, planck_fraction(lT),
                       method="series for F(0->lambda T), C2 = 14387.77 um K", slack=12))
    out += [
        chk("P12.5-BAND", "sec12", "1.2-2.7 um band fraction (table values)", "0.52889", 0.77492 - 0.24603),
        chk("P12.5-LMED", "sec12", "median wavelength [um]", "1.7113", 4107.2 / 2400),
        chk("P12.5-RATIO", "sec12", "lambda_med / lambda_max", "1.4174", 4107.2 / 2897.77),
    ]
    hr1 = 0.850 * SIG_FULL * (380.15 ** 2 + 300.15 ** 2) * 680.30
    A = math.pi * 0.0500 * 2.00
    Q1 = (6.80 + hr1) * A * 80.0
    Q2 = (6.80 + 0.040 / 0.850 * hr1) * A * 80.0
    out += [
        chk("P12.6-HRAD", "sec12", "bare-pipe h_rad [W/(m2 K)]", "7.692", hr1),
        chk("P12.6-Q1", "sec12", "bare-pipe loss [W]", "364.2", Q1),
        chk("P12.6-HRAD2", "sec12", "foil-pipe h_rad [W/(m2 K)]", "0.362", 0.040 / 0.850 * hr1),
        chk("P12.6-Q2", "sec12", "foil-pipe loss [W]", "180.0", Q2),
        chk("P12.6-RED", "sec12", "reduction [%]", "50.6", 100 * (1 - Q2 / Q1)),
    ]
    q = 0.850 * SIG_FULL * (450.0 ** 4 - 350.0 ** 4)
    A1 = math.pi * 0.0600 * 0.500
    Q = A1 * SIG_FULL * (360.0 ** 4 - 300.0 ** 4) / 8.000
    out += [
        chk("P12.7-Q", "sec12", "bead radiative flux [W/m2]", "1253.2", q),
        chk("P12.7-TG", "sec12", "true gas temperature [K]", "469.28", 450.0 + q / 65.0),
        chk("P12.8-Q", "sec12", "cylinder exchange [W]", "5.809", Q),
        chk("P12.8-FLAT", "sec12", "flat-plate formula [W]", "3.320", Q * 8.00 / 14.00),
        chk("P12.8-ERR", "sec12", "flat-plate error [%]", "-42.9", 100 * (8.00 / 14.00 - 1)),
    ]
    return out


# --------------------------------------------------------------------------------------
# §13
# --------------------------------------------------------------------------------------
def sec13():
    out = []
    r, l = 1.80e-3, 10.0e-3
    A = 2 * math.pi * r * l + 2 * math.pi * r * r
    V = math.pi * r * r * l
    tau = 2000 * 700 * V / (20.17 * A)
    out += [
        chk("EX-13.1-V", "sec13", "resistor volume [m3]", "1.0179e-7", V),
        chk("EX-13.1-BI", "sec13", "Biot number", "0.00154", 20.17 * V / A / 10.0),
        chk("EX-13.1-TAU", "sec13", "time constant [s]", "52.94", tau),
        chk("EX-13.1-T95", "sec13", "95% time [s]", "158.6", -tau * math.log(0.05)),
    ]
    tau2 = 903.0
    Tss = 22.00 + 24.00 * 2.37632
    T6 = Tss - (Tss - 22.00) * math.exp(-600 / tau2)
    T9 = Tss - (Tss - 22.00) * math.exp(-900 / tau2)
    out += [
        chk("EX-13.2-RATE", "sec13", "initial heating rate [C/min]", "3.789", 24.00 / 380.0 * 60),
        chk("EX-13.2-TSS", "sec13", "stagnation temperature [C]", "79.03", Tss),
        chk("EX-13.2-F10", "sec13", "1 - exp(-600/903)", "0.48544", 1 - math.exp(-600 / tau2)),
        chk("EX-13.2-T10", "sec13", "T(10 min) [C]", "49.69", T6),
        chk("EX-13.2-T15", "sec13", "T(15 min) [C]", "57.98", T9),
        chk("EX-13.2-LIN15ERR", "sec13", "linear-extrapolation error at 15 min [C]", "20.86", 22.00 + 24.00 / 380.0 * 900 - T9),
    ]
    out += [
        chk("EX-13.4-T7", "sec13", "probe reading at 2 tau [C]", "43.62", 47.00 - 25.00 * math.exp(-2)),
        chk("EX-13.4-T175", "sec13", "probe reading at 5 tau [C]", "46.83", 47.00 - 25.00 * math.exp(-5)),
        chk("EX-13.4-LAG", "sec13", "ramp lag [C]", "-0.16", -0.0450 * 3.50),
        chk("EX-13.5-D", "sec13", "penetration depth [mm]", "18.85", 2000 * math.sqrt(1.48e-7 * 600)),
        chk("EX-13.5-TAL", "sec13", "skin-aluminum contact T [C]", "20.61", (1100 * 34.0 + 24095.3 * 20.0) / (1100 + 24095.3)),
        chk("EX-13.5-TBALSA", "sec13", "skin-balsa contact T [C]", "32.95", (1100 * 34.0 + 89.44 * 20.0) / (1100 + 89.44)),
    ]
    tc = 215.0 / 0.14554
    out += [
        chk("EX-13.7-TAU", "sec13", "open-cup time constant [s]", "1477.3", tc),
        chk("EX-13.7-D6", "sec13", "cooling in 6 s [C]", "0.105", 26.00 * (1 - math.exp(-6.0 / tc))),
        chk("EX-13.7-D50", "sec13", "cooling in 50 s [C]", "0.865", 26.00 * (1 - math.exp(-50.0 / tc))),
        chk("EX-13.7-DIFF", "sec13", "extra loss when slow [C]", "0.76", 26.00 * (math.exp(-6.0 / tc) - math.exp(-50.0 / tc))),
    ]
    import numpy as np
    from scipy.integrate import solve_ivp
    C1, C2, R1, R2 = 167.36, 251.04, 3.50, 8.00
    R12 = 0.0180 / (0.620 * 0.00360)
    M = np.array([[-(1 / R1 + 1 / R12) / C1, 1 / (R12 * C1)], [1 / (R12 * C2), -(1 / R2 + 1 / R12) / C2]])
    bvec = np.array([16.00 / C1, 4.00 / C2])
    sol = solve_ivp(lambda t, y: M @ y + bvec, (0, 600.0), [0.0, 0.0], rtol=1e-10, atol=1e-12)
    th1, th2 = sol.y[:, -1]
    out += [
        chk("EX-13.8-R12", "sec13", "inter-layer resistance [K/W]", "8.0645", R12),
        chk("EX-13.8-A11", "sec13", "matrix a11 [1/s]", "-0.002448", M[0, 0]),
        chk("EX-13.8-A12", "sec13", "matrix a12 [1/s]", "0.0007409", M[0, 1]),
        chk("EX-13.8-A21", "sec13", "matrix a21 [1/s]", "0.0004939", M[1, 0]),
        chk("EX-13.8-A22", "sec13", "matrix a22 [1/s]", "-0.0009919", M[1, 1]),
        chk("EX-13.8-TTOP", "sec13", "top node at 600 s [C]", "53.73", 22.00 + th1),
        chk("EX-13.8-TBOT", "sec13", "bottom node at 600 s [C]", "33.82", 22.00 + th2),
        chk("EX-13.8-MIX", "sec13", "stirred reading [C]", "41.79", 22.00 + 0.4 * th1 + 0.6 * th2),
    ]
    out.append(chk("EX-13.9-DT", "sec13", "Regnault-Pfaundler corrected rise [C]", "9.154", 8.850 - 0.020 * 1.60 + 0.140 * 2.40))
    e = math.exp(-0.5)
    TA = 20.0 + ((200 * 85.0 + 25 * 5.0) / 225 - 20.0) * e
    TB = (200 * (20.0 + 65.0 * e) + 25 * 5.0) / 225
    out += [
        chk("P13.1-TA", "sec13", "cream first [C]", "54.03", TA),
        chk("P13.1-TB", "sec13", "cream last [C]", "53.38", TB),
        chk("P13.1-DIFF", "sec13", "difference [C]", "0.66", TA - TB),
    ]
    Tss3 = 23.00 + 14.80 * 2.400
    T3 = Tss3 - (Tss3 - 19.50) * math.exp(-0.8)
    Tss125 = 23.00 + 18.50 * 2.400
    T125 = Tss125 - (Tss125 - 19.50) * math.exp(-0.8)
    out += [
        chk("P13.3-T", "sec13", "100 W prediction [C]", "40.99", T3),
        chk("P13.3-T125", "sec13", "125 W final [C]", "45.88", T125),
        chk("P13.3-ERR", "sec13", "scaling-trap error [C]", "-4.3", 0.8 * T125 - T3),
        chk("P13.4-T", "sec13", "Cu-water contact T [C]", "96.69", (37000 * 100.0 + 1598 * 20.0) / 38598),
        chk("P13.5-DT", "sec13", "probe drain [C]", "-0.25", -1.012 / (104.6 + 1.012) * 26.00),
        chk("P13.6-LAG", "sec13", "falling-room lag [C]", "2.594", 3.00 * (1 - math.exp(-2))),
    ]
    from scipy.optimize import brentq
    lam = brentq(lambda x: 1 - x / math.tan(x) - 2.0, 0.1, math.pi - 1e-6)
    A1 = 4 * (math.sin(lam) - lam * math.cos(lam)) / (2 * lam - math.sin(2 * lam))
    th = A1 * math.exp(-lam ** 2 * 0.5)
    out += [
        chk("P13.7-LAM", "sec13", "sphere eigenvalue at Bi = 2", "2.0288", lam),
        chk("P13.7-A1", "sec13", "sphere A1 at Bi = 2", "1.4793", A1),
        chk("P13.7-RATIO", "sec13", "theta_s/theta_c", "0.4421", math.sin(lam) / lam),
        chk("P13.7-TC", "sec13", "center temperature [C]", "38.89", 20.0 + 100.0 * th),
        chk("P13.7-TS", "sec13", "surface temperature [C]", "28.35", 20.0 + 100.0 * th * math.sin(lam) / lam),
    ]
    dd = math.sqrt(5.40e-7 * 86400 / math.pi)
    dy = math.sqrt(5.40e-7 * 3.1536e7 / math.pi)
    out += [
        chk("P13.8-DDAY", "sec13", "diurnal damping depth [m]", "0.1219", dd),
        chk("P13.8-XDAY", "sec13", "diurnal anti-phase depth [m]", "0.3829", math.pi * dd),
        chk("P13.8-DYR", "sec13", "annual damping depth [m]", "2.328", dy),
        chk("P13.8-XYR", "sec13", "annual anti-phase depth [m]", "7.314", math.pi * dy),
    ]
    T2 = 21.00 + 26.80 * math.exp(-20.0 / 1200)
    Tf = 21.00 + (T2 - 21.00) * math.exp(-25.0 / 480.0)
    b = math.sqrt(1.30 * 2300 * 880)
    q = b * 40.0 / math.sqrt(math.pi * 100.0)
    out += [
        chk("P13.9-T2", "sec13", "after closed dwell [C]", "47.36", T2),
        chk("P13.9-TF", "sec13", "measured temperature [C]", "46.02", Tf),
        chk("P13.9-DROP", "sec13", "post-lamp drop [C]", "1.78", 47.80 - Tf),
        chk("P13.10-B", "sec13", "concrete effusivity", "1622.1", b),
        chk("P13.10-Q", "sec13", "surface flux at 100 s [W/m2]", "3661", q),
        chk("P13.10-E", "sec13", "absorbed energy per area [J/m2]", "7.321e5", 2 * q * 100.0),
    ]
    d0 = 16.50 * 2.400 * (1 - math.exp(-600 / (420.5 * 2.400)))
    d1 = 18.00 * 2.400 * (1 - math.exp(-600 / (528.5 * 2.400)))
    tau_be = 600 / -math.log(1 - d0 / 43.20)
    dfoil = 18.00 * 2.400 * (1 - math.exp(-600 / ((420.5 + 1.35) * 2.400)))
    out += [
        chk("P13.11-D0", "sec13", "bare-cup gain [C]", "17.75", d0),
        chk("P13.11-D1", "sec13", "collar gain [C]", "16.28", d1),
        chk("P13.11-DIFF", "sec13", "collar penalty [C]", "-1.47", d1 - d0),
        chk("P13.11-TAU", "sec13", "break-even tau [s]", "1134.1", tau_be),
        chk("P13.11-C1", "sec13", "break-even capacitance [J/K]", "472.55", tau_be / 2.400),
        chk("P13.11-DC", "sec13", "allowed added capacitance [J/K]", "52.05", tau_be / 2.400 - 420.5),
        chk("P13.11-M", "sec13", "maximum aluminum mass [g]", "57.8", (tau_be / 2.400 - 420.5) / 0.900),
        chk("P13.11-FOIL", "sec13", "foil-sleeve gain [C]", "19.32", dfoil),
        chk("P13.11-FOILNET", "sec13", "foil-sleeve net benefit [C]", "1.57", dfoil - d0),
    ]
    T1 = 120.00 - 50.00 * (1 - math.exp(-2))
    out += [
        chk("P13.12-T1", "sec13", "end of ramp [C]", "76.77", T1),
        chk("P13.12-T2", "sec13", "after 100 s hold [C]", "104.10", 120.00 - (120.00 - T1) * math.exp(-1)),
    ]
    return out


# --------------------------------------------------------------------------------------
# §14
# --------------------------------------------------------------------------------------
def coax(r1, r2, d):
    R1, R2 = r1 / d, r2 / d
    X = 1 + (1 + R2 ** 2) / R1 ** 2
    return 0.5 * (X - math.sqrt(X * X - 4 * (R2 / R1) ** 2)), X


def sec14():
    out = []
    dM = SIG_FULL * (335.15 ** 4 - 295.15 ** 4)
    Tm = (335.15 + 295.15) / 2
    out += [
        chk("EX-14.1-MS", "sec14", "sigma Ts^4 [W/m2]", "715.43", SIG_FULL * 335.15 ** 4),
        chk("EX-14.1-ME", "sec14", "sigma Te^4 [W/m2]", "430.31", SIG_FULL * 295.15 ** 4),
        chk("EX-14.1-DM", "sec14", "exitance difference [W/m2]", "285.12", dM),
        chk("EX-14.1-QSEL", "sec14", "selective collar [W]", "17.00", 4.00e-3 * (0.95 * 4500 - 0.09 * dM)),
        chk("EX-14.1-QBLK", "sec14", "black paint collar [W]", "15.90", 4.00e-3 * (0.94 * 4500 - 0.89 * dM)),
        chk("EX-14.1-QWHT", "sec14", "white paint collar [W]", "3.65", 4.00e-3 * (0.26 * 4500 - 0.90 * dM)),
        chk("EX-14.1-HRAD", "sec14", "linearized 4 sigma Tm^3 [W/(m2 K)]", "7.099", 4 * SIG_FULL * Tm ** 3),
        chk("EX-14.1-HRADDT", "sec14", "linearized flux at 40 K [W/m2]", "284.0", 4 * SIG_FULL * Tm ** 3 * 40),
    ]
    for lab, rs, rd, qd in (("SHINY", 0.88, 0.08, "36.91"), ("DULL", 0.62, 0.33, "28.03"), ("CARD", 0.04, 0.70, "8.97")):
        e1 = rs + 0.35 * rd
        out.append(chk(f"EX-14.2-{lab}", "sec14", f"{lab.lower()} reflector delivered power [W]", qd, 42.0 * (0.65 * e1 + 0.35 * e1 ** 2)))
    RF = ((1.325 - 1) / (1.325 + 1)) ** 2
    out.append(chk("EX-14.3-RF", "sec14", "air-water Fresnel reflectance", "0.01954", RF))
    for lab, mu, f1, tot in (("A", 0.450, "35.53", "93.14"), ("B", 1.040, "63.39", "97.79")):
        fL = (1 - RF) * (1 - math.exp(-mu * 3.80))
        df = (1 - RF) * math.exp(-mu * 3.80) * 0.8832 * (1 - math.exp(-mu * 3.80))
        out += [chk(f"EX-14.3-{lab}-TOP", "sec14", f"top 1 cm absorbed, mu={mu} [%]", f1, 100 * (1 - RF) * (1 - math.exp(-mu))),
                chk(f"EX-14.3-{lab}-TOT", "sec14", f"total absorbed, mu={mu} [%]", tot, 100 * (fL + df))]
    for lab, n, mu, dl, rho, cp, tau, C in (("BOPET", 1.64, 8.0, 0.0025, 1390, 1170, "0.8713", "0.2439"),
                                           ("GLASS", 1.47, 0.080, 0.200, 2210, 753, "0.9153", "19.970")):
        Rs = ((n - 1) / (n + 1)) ** 2
        ti = math.exp(-mu * dl)
        out += [chk(f"EX-14.4-{lab}-TAU", "sec14", f"{lab.lower()} NIR transmittance", tau, (1 - Rs) ** 2 * ti / (1 - Rs ** 2 * ti ** 2)),
                chk(f"EX-14.4-{lab}-C", "sec14", f"{lab.lower()} disk heat capacity [J/K]", C, rho * cp * 6.00e-3 * dl / 100)]
    hr = 4 * 5.6704e-8 * 308.65 ** 3 / 49
    k = 0.0265 + hr * 0.0100
    out += [
        chk("EX-14.5-RA", "sec14", "gap Rayleigh number", "602.8", 9.807 * (7.00 / 308.65) * 1e-6 / 3.69e-10),
        chk("EX-14.5-HRAD", "sec14", "foil-gap h_rad [W/(m2 K)]", "0.1361", hr),
        chk("EX-14.5-KEFF", "sec14", "effective k [W/(m K)]", "0.02786", k),
        chk("EX-14.5-Q", "sec14", "foil-air sleeve leak [W]", "0.878", k * 0.0450 * 21.0 / 0.030),
        chk("EX-14.5-PCT", "sec14", "cork extra leak [%]", "43.6", 100 * ((0.040 / k) - 1)),
        chk("EX-14.5-CCORK", "sec14", "cork sleeve heat capacity [J/K]", "424.6", 314500 * 0.0450 * 0.030),
    ]
    return out


# --------------------------------------------------------------------------------------
# §15 (labels 15.1b, 15.2 ... print as 15.2, 15.3 ...)
# --------------------------------------------------------------------------------------
def sec15():
    out = []
    Fc40 = coax(6.35, 3.75, 30.0)[0]
    Fa40 = coax(6.35, 15.0, 10.0)[0]
    Fc65, X65 = coax(6.35, 3.75, 55.0)
    Fa65 = coax(6.35, 15.0, 35.0)[0]
    out += [
        chk("EX-15.1-FC40", "sec15", "bulb-to-cup view factor at 40 cm", "0.01474", Fc40),
        chk("EX-15.1-FA40", "sec15", "bulb-to-aperture view factor at 40 cm", "0.66465", Fa40),
        chk("EX-15.1-GAIN", "sec15", "aperture/cup gain at 40 cm", "45.08", Fa40 / Fc40),
        chk("EX-15.1-X65", "sec15", "X for cup at 65 cm", "76.369", X65),
        chk("EX-15.1-FC65", "sec15", "cup view factor at 65 cm", "0.004567", Fc65),
        chk("EX-15.1-FA65", "sec15", "aperture view factor at 65 cm", "0.15160", Fa65),
        chk("EX-15.1-GAIN65", "sec15", "gain at 65 cm", "33.19", Fa65 / Fc65),
        chk("EX-12.2-FCUP", "sec12", "Ex 12.2 bare-cup view factor", "0.01474", Fc40),
        chk("EX-12.2-GAIN", "sec12", "Ex 12.2 gain", "45.1", 0.6647 / 0.01474),
    ]
    for h, fa, fc in ((40, "0.6647", "0.0147"), (45, "0.4776", "0.0110"), (50, "0.3454", "0.0085"),
                      (55, "0.2557", "0.0068"), (60, "0.1944", "0.0055"), (65, "0.1516", "0.0046")):
        out += [chk(f"TAB-15.4-FAP-{h}", "sec15", f"Table 15.4 F_bulb->ap (z_ap = 30.0 cm, d = {h - 30} cm)", fa, coax(6.35, 15.0, h - 30.0)[0]),
                chk(f"TAB-15.4-FCUP-{h}", "sec15", f"Table 15.4 F_bulb->cup (z_cup = 10.0 cm)", fc, coax(6.35, 3.75, h - 10.0)[0])]
    F, X = coax(14.50, 3.75, 14.30)
    fd = 2.15 * F
    out += [
        chk("EX-15.1b-X", "sec15", "aperture-to-cup X", "2.03949", X),
        chk("EX-15.1b-F", "sec15", "aperture-to-cup view factor", "0.03334", F),
        chk("EX-15.1b-QD", "sec15", "direct beam power [W]", "2.451", fd * 34.20),
        chk("EX-15.1b-QTOT", "sec15", "total power at glazing cap [W]", "30.352", fd * 34.20 + (1 - fd) * 34.20 * 0.8788),
        chk("EX-15.1b-QW", "sec15", "wall-delivered power [W]", "27.901", (1 - fd) * 34.20 * 0.8788),
    ]
    d1 = math.sqrt(14.5 ** 2 + 18.0 ** 2)
    d2 = math.sqrt(14.5 ** 2 + 17.0 ** 2)
    a = (d1 + d2) / 2
    b = math.sqrt(a * a - 17.5 ** 2)
    L1 = math.sqrt(1.190 ** 2 + 8.50 ** 2)
    out += [
        chk("EX-15.2-A", "sec15", "ellipse semi-major axis [cm]", "22.7289", a),
        chk("EX-15.2-B", "sec15", "ellipse semi-minor axis [cm]", "14.5035", b),
        chk("EX-15.2-R", "sec15", "radius at 18.5 cm [cm]", "13.318", b * math.sqrt(1 - 81.0 / a ** 2)),
        chk("EX-15.2-L", "sec15", "frustum slant height [cm]", "8.5829", L1),
        chk("EX-15.2-ROUT", "sec15", "unrolled outer radius [cm]", "104.58", 14.50 * L1 / 1.190),
    ]
    Ghs = 1 / 220.0 + 1 / 14.20 + 1 / 19.80
    Rtop = 1 / Ghs + 3.68
    G = 1 / Rtop + 1 / 9.42 + 1 / 185.0
    Gopen = 1 / 5.50 + 1 / 14.20 + 1 / 19.80
    out += [
        chk("EX-15.3-RTOP", "sec15", "glazed top resistance [K/W]", "11.650", Rtop),
        chk("EX-15.3-RENC", "sec15", "enclosure resistance [K/W]", "5.066", 1 / G),
        chk("EX-15.3-REFF", "sec15", "top-layer effective resistance [K/W]", "4.190", 1 / (G + 0.38 / 9.21)),
        chk("EX-15.3-ROPEN", "sec15", "open-top resistance [K/W]", "3.303", 1 / Gopen),
        chk("EX-15.3-RENCOPEN", "sec15", "open enclosure resistance [K/W]", "2.414", 1 / (Gopen + 1 / 9.42 + 1 / 185.0)),
    ]
    TGal = 27.70 * 220.6 / (220.6 + 0.150 * 896)
    out += [
        chk("EX-15.3b-TG", "sec15", "TG with aluminum sleeve [C]", "17.21", TGal),
        chk("EX-15.3b-LOST", "sec15", "TG lost [C]", "10.49", 27.70 - TGal),
    ]
    Tm = (215.0 * 49.70 + 203.4 * 29.34) / 418.4
    PE = 1 - abs(Tm - 49.70) / Tm
    out += [
        chk("EX-15.4-TMIX", "sec15", "mixed temperature [C]", "39.80", Tm),
        chk("EX-15.4-KAPPA", "sec15", "stratification factor", "1.556", 27.70 / (Tm - 22.00)),
        chk("EX-15.4-PE", "sec15", "PE after swirl", "0.7513", PE),
        chk("EX-15.4-LOST", "sec15", "points lost", "15.69", 30 - 30 * (Tm - 22.00) / 27.70 + 20 - 20 * PE),
        chk("EX-15.4-Q", "sec15", "two-body heat [J]", "2128.0", 215.0 * (49.70 - Tm)),
    ]
    md = 3.60e-3 * 6.65e-3 * (0.04680 - 0.00816)
    dm = (7384 - 1322) * 1.50e-4 * 18.0153 / (8.31446 * 313.15)
    out += [
        chk("EX-15.5-MDOT", "sec15", "evaporation rate [kg/s]", "9.250e-7", md),
        chk("EX-15.5-Q", "sec15", "evaporative power [W]", "2.226", 2.406e6 * md),
        chk("EX-15.5-DT", "sec15", "top-layer penalty [C]", "6.21", 2.406e6 * md * 600 / 215.0),
        chk("EX-15.5-DM", "sec15", "headspace saturation mass [g]", "6.292e-3", dm),
        chk("EX-15.5-RHO", "sec15", "ideal-gas vapor density at 40 C [g/m3]", "51.09", 7384 * 18.0153 / (8.31446 * 313.15)),
    ]
    Gf = 0.040 * 1.80e-5 / 0.012 + 0.0278 * 21.88e-4 / 0.010
    out += [
        chk("EX-15.6-G", "sec15", "fin pedestal conductance [W/K]", "6.143e-3", Gf),
        chk("EX-15.6-Q", "sec15", "fin pedestal leak [W]", "0.080", Gf * 13.0),
        chk("EX-15.6-QPLY", "sec15", "plywood floor leak [W]", "0.287", 0.120 * 22.06e-4 / 0.012 * 13.0),
    ]
    from scipy.optimize import brentq
    zw = brentq(lambda z: math.pi / (3 * 0.11) * ((2.65 + 0.11 * z) ** 3 - 2.65 ** 3) - 100.0, 1, 8)
    out += [
        chk("EX-15.6b-ZW", "sec15", "100 mL water depth [cm]", "3.876", zw),
        chk("EX-15.6b-R", "sec15", "water surface radius at the printed z_w = 3.876 cm [cm]", "3.0764", 2.650 + 0.1100 * 3.876),
        chk("EX-15.6b-CLEAR", "sec15", "dry clearance below lip [cm]", "3.62", 10.00 - zw - 2.50),
    ]
    return out


# --------------------------------------------------------------------------------------
# §16 (labels 16.2b, 16.3 ... print as 16.3, 16.4 ...)
# --------------------------------------------------------------------------------------
def Mt(t_min, tau=903.0):
    return (1 - math.exp(-60 * t_min / tau)) / (1 - math.exp(-600 / tau))


def sec16():
    out = []
    ES = 50 * 88.5 / 92.0
    PEa = 1 - 0.3 / 49.7
    PEb = 1 - 0.3 / 30.1
    TSb = 30 * 8.1 / 27.7
    out += [
        chk("EX-16.1-ES", "sec16", "exam score [pts]", "48.10", ES),
        chk("EX-16.1-FSA", "sec16", "Team Alpha final [pts]", "98.02", ES + 30 + 20 * PEa / 0.9980),
        chk("EX-16.1-FSB", "sec16", "Team Beta final [pts]", "76.71", ES + TSb + 20 * PEb / 0.9980),
        chk("EX-16.1-FSBPEN", "sec16", "Team Beta with violation [pts]", "68.13", ES + 0.7 * (TSb + 20 * PEb / 0.9980)),
    ]
    out += [
        chk("EX-16.0-DEN", "sec16", "1 - exp(-600/903)", "0.48544", 1 - math.exp(-600 / 903.0)),
        chk("EX-16.2-MT13", "sec16", "M_t(13 min)", "1.19156", Mt(13)),
        chk("EX-16.2-TG", "sec16", "TG_table(45 cm, 13 min) [C]", "33.01", 27.70 * Mt(13)),
        chk("EX-16.2-PRED", "sec16", "prediction [C]", "54.47", 19.60 + 27.70 * Mt(13) + (1 - math.exp(-780 / 903.0)) * 3.6 - 0.22),
    ]
    for m, val in ((11, "1.068"), (12, "1.132"), (13, "1.192"), (14, "1.247"), (15, "1.300")):
        out.append(chk(f"TAB-16.MT-{m}", "sec16", f"M_t({m} min) to 3 decimals", val, Mt(m)))
    for m, ks in ((10, "0.515"), (11, "0.481"), (12, "0.451"), (13, "0.422"), (14, "0.394"), (15, "0.369")):
        out.append(chk(f"TAB-16.KSTART-{m}", "sec16", f"k_start({m} min)", ks, math.exp(-60 * m / 903.0)))
    tau = 300 / math.log(16.17 / 11.60)
    dss = 16.17 ** 2 / (2 * 16.17 - 27.77)
    out += [
        chk("EX-16.2b-TAU", "sec16", "fitted tau [s]", "903.2", tau),
        chk("EX-16.2b-DSS", "sec16", "steady-state gain [C]", "57.21", dss),
        chk("EX-16.2b-TG900", "sec16", "15-min gain [C]", "36.09", dss * (1 - (11.60 / 16.17) ** 3)),
    ]
    TG53 = 0.800 * 21.3 + 0.600 * (0.800 * 17.5 - 0.800 * 21.3)
    out += [
        chk("EX-16.3-TG53", "sec16", "interpolated TG_100(53 cm) [C]", "15.22", TG53),
        chk("EX-16.3-TG14", "sec16", "TG_table(53 cm, 100 W, 14 min) as displayed [C]", "18.98", 15.22 * 1.247),
        chk("EX-16.3-PRED", "sec16", "prediction with table M14 = 1.247, k_room = 0.606 [C]", "40.10", 21.00 + 15.22 * 1.247 + 0.606 * 0.50 - 0.18),
        chk("EX-16.3-PREDX", "sec16", "prediction with exact M14 (verified-by line) [C]", "40.103", 21.00 + TG53 * Mt(14) + (1 - math.exp(-840 / 903.0)) * 0.50 - 0.18),
    ]
    out += [
        chk("EX-16.4-A", "sec16", "open-extraction cooling [C]", "0.932", 0.05 + 0.0245 * 36),
        chk("EX-16.4-B", "sec16", "staged-extraction cooling [C]", "0.547", 0.05 + 0.0070 * 22 + 0.0245 * 14),
    ]
    import statistics as st
    x = [49.6, 49.8, 49.7, 49.5, 49.9, 49.7]
    sr = st.stdev(x)
    ur = sr * math.sqrt(7 / 6)
    out += [
        chk("EX-16.5-S", "sec16", "repeatability s [C]", "0.1414", sr),
        chk("EX-16.5-URUN", "sec16", "single-run uncertainty [C]", "0.1528", ur),
        chk("EX-16.5-PE", "sec16", "expected PE", "0.99755", 1 - math.sqrt(2 / math.pi) * ur / 49.700),
        chk("EX-16.6-TG", "sec16", "R40 gain at 60 cm, 100 W, 12 min [C]", "12.32", 0.800 * 13.6 * Mt(12)),
        chk("EX-16.6-UNADJ", "sec16", "unadjusted prediction [C]", "34.17", 22.00 + 12.32 - 0.15),
        chk("EX-16.6-PRED", "sec16", "PAR38-adjusted prediction [C]", "36.14", 22.00 + 1.160 * 12.32 - 0.15),
        chk("EX-16.6-PE", "sec16", "unadjusted PE", "0.9474", 1 - 1.9 / 36.1),
        chk("EX-16.6-SAVE", "sec16", "PS points saved", "1.05", 20 * 1.9 / 36.1),
        chk("EX-16.6-DPS", "sec16", "verified-by ratio check [pts]", "1.091", 20 * 0.160 * 12.32 / 36.14),
    ]
    n = math.log(27.70 / 10.60) / math.log(45.50 / 25.50)
    out += [
        chk("EX-16.7-N", "sec16", "power-law exponent", "1.6589", n),
        chk("EX-16.7-A0", "sec16", "power-law amplitude", "5968.1", 27.70 * 25.50 ** n),
        chk("EX-16.7-SLOTA", "sec16", "Slot A prediction at 55 cm [C]", "16.00", 27.70 * (25.50 / 35.50) ** n),
        chk("EX-16.7-SLOTB", "sec16", "Slot B prediction at 55 cm [C]", "17.53", 27.70 * (25.50 / 33.60) ** n),
    ]
    return out


# --------------------------------------------------------------------------------------
# §17 - §20
# --------------------------------------------------------------------------------------
def sec17_20():
    out = []
    bapp = 1.120e-3 - 3 * 3.30e-6
    out += [
        chk("EX-17.1-S", "sec17", "capillary sensitivity [mm/K]", "2.2085", 250.0 * bapp / (math.pi / 4 * 0.400 ** 2)),
        chk("EX-17.1-T", "sec17", "stem-corrected temperature [C]", "66.97", 65.00 + 0.00104 * 45.0 * 42.0),
    ]
    inv = 1 / 298.15 + math.log(4912.0 / 10000.0) / 3892
    out += [
        chk("EX-17.2-INV", "sec17", "1/T [1/K]", "3.1713587e-3", inv),
        chk("EX-17.2-T", "sec17", "thermistor temperature [K]", "315.3223", 1 / inv),
        chk("EX-17.2-DRDT", "sec17", "dR/dT [ohm/K]", "-192.3", -3892 * inv ** 2 * 4912.0),
        chk("EX-17.2-SH", "sec17", "self-heating [C]", "0.0370", (3.30 / 14912.0) ** 2 * 4912.0 * 1000 / 6.50),
    ]
    A, B = 3.9083e-3, -5.775e-7
    tcvd = lambda R: (-A + math.sqrt(A * A - 4 * B * (1 - R / 100.0))) / (2 * B)
    Ta, To = 295.15, 317.15
    out += [
        chk("EX-17.3-TTRUE", "sec17", "RTD true temperature [C]", "43.18", tcvd(116.77)),
        chk("EX-17.3-BIAS", "sec17", "2-wire lead bias [C]", "1.815", tcvd(117.47) - tcvd(116.77)),
        chk("EX-17.3-IRW", "sec17", "IR reading on water [C]", "44.21", (Ta ** 4 + 0.96 / 0.95 * (To ** 4 - Ta ** 4)) ** 0.25 - 273.15),
        chk("EX-17.3-IRF", "sec17", "IR reading on foil [C]", "23.03", (Ta ** 4 + 0.04 / 0.95 * (To ** 4 - Ta ** 4)) ** 0.25 - 273.15),
    ]
    Teq = (215.0 * 49.70 + 0.450 * 21.50) / 215.45
    Tb = 100.00 + 0.03686 * (-18.0) - 0.000020 * 18.0 ** 2
    out += [
        chk("EX-17.4-TEQ", "sec17", "equilibrium after probe drain [C]", "49.641", Teq),
        chk("EX-17.4-DRAIN", "sec17", "probe drain [C]", "-0.059", Teq - 49.70),
        chk("EX-17.4-T2", "sec17", "reading at 2 tau [C]", "45.83", Teq - (Teq - 21.50) * math.exp(-2)),
        chk("EX-17.4-LOSS2", "sec17", "premature-reading loss at 2 tau [C]", "3.81", (Teq - 21.50) * math.exp(-2)),
        chk("EX-17.4-T5", "sec17", "reading at 5 tau [C]", "49.45", Teq - (Teq - 21.50) * math.exp(-5)),
        chk("EX-17.4-WITHIN5", "sec17", "gap to T_eq at 5 tau [C]", "0.19", (Teq - 21.50) * math.exp(-5)),
        chk("EX-17.4-TB", "sec17", "boiling point at 742 mmHg [C]", "99.330", Tb),
        chk("EX-17.4-TTRUE", "sec17", "two-point calibrated reading [C]", "44.56", Tb * 44.50 / 99.20),
    ]
    us, ur = 0.40 / math.sqrt(3), 0.10 / (2 * math.sqrt(3))
    u = math.sqrt(us ** 2 + ur ** 2 + 0.050 ** 2)
    uc = math.sqrt(2 * (ur ** 2 + 0.050 ** 2))
    cx = 100.00 * 4.184 * 5.40 / (85.00 * 52.60)
    rel = math.sqrt((0.15 / 100) ** 2 + (0.05 / 85) ** 2 + (uc / 5.40) ** 2 + (uc / 52.60) ** 2)
    out += [
        chk("EX-17.5-U", "sec17", "single-reading uncertainty [C]", "0.2380", u),
        chk("EX-17.5-UNC", "sec17", "uncorrelated TG uncertainty [C]", "0.3367", math.sqrt(2) * u),
        chk("EX-17.5-UC", "sec17", "correlated TG uncertainty [C]", "0.08165", uc),
        chk("EX-17.5-CX", "sec17", "specific heat [J/(g K)]", "0.50534", cx),
        chk("EX-17.5-REL", "sec17", "relative uncertainty", "0.01528", rel),
        chk("EX-17.5-UCX", "sec17", "standard uncertainty [J/(g K)]", "0.00772", cx * rel),
    ]
    Q = SIG_FULL * 5.000e-3 * 500.0 ** 4
    out += [
        chk("EX-17.6-T", "sec17", "thermocouple temperature [C]", "42.64", 40.0 + 10.0 * (1.724 - 1.612) / (2.036 - 1.612)),
        chk("EX-17.6-Q", "sec17", "cavity power [W]", "17.720", Q),
        chk("EX-17.6-U", "sec17", "power uncertainty [W]", "0.365", Q * math.sqrt(0.005 ** 2 + 0.020 ** 2)),
    ]
    x = (5.942025 - 1.1346) / (7.5445 - 1.1346)
    vfg = 1.6718 - 0.0010435
    out += [
        chk("EX-18.1-H", "sec18", "wet-steam enthalpy [kJ/kg]", "2077.77", 355.96 + x * (2651.7 - 355.96)),
        chk("EX-18.1-HBI", "sec18", "bilinear superheated h [kJ/kg]", "2804.85", 0.2 * 2782.3 + 0.3 * 2824.4 + 0.2 * 2776.1 + 0.3 * 2819.5),
        chk("EX-18.1-HFG", "sec18", "central-difference Clapeyron h_fg [kJ/kg]", "2262.5", 373.15 * vfg * (120.90 - 84.609) / 10),
        chk("EX-18.2-W", "sec18", "trapezoidal work [J]", "1037.5", 1.00 * (0.5 * 420.0 + 310.0 + 240.0 + 195.0 + 0.5 * 165.0)),
        chk("EX-18.3-TSS", "sec18", "3-point T_ss [C]", "61.663", (22.00 * 38.45 - 31.32 ** 2) / (22.00 + 38.45 - 2 * 31.32)),
    ]
    import numpy as np
    t = np.array([0, 2, 4, 6, 8, 10.0])
    Y = np.array([0.0, -0.13210, -0.26527, -0.39675, -0.52975, -0.66165])
    StY = float(((t - 5) * (Y - Y.mean())).sum())
    SYY = float(((Y - Y.mean()) ** 2).sum())
    m = StY / 70.0
    sres = math.sqrt((SYY - m * StY) / 4)
    out += [
        chk("EX-18.3-STY", "sec18", "S_tY", "-4.63268", StY),
        chk("EX-18.3-SYY", "sec18", "S_YY", "0.3065967", SYY),
        chk("EX-18.3-M", "sec18", "slope [1/min]", "-0.0661811", m),
        chk("EX-18.3-S", "sec18", "residual standard error", "3.86e-4", sres),
        chk("EX-18.3-UM", "sec18", "slope uncertainty [1/min]", "4.61e-5", sres / math.sqrt(70.0)),
        chk("EX-18.3-TAU", "sec18", "tau [min]", "15.110", -1 / m),
        chk("EX-18.3-UTAU", "sec18", "tau uncertainty [min]", "0.0105", sres / math.sqrt(70.0) / m ** 2),
    ]
    import statistics as st
    g = [21.30, 21.45, 21.20, 21.35, 21.40, 18.90]
    out += [
        chk("EX-18.3-SALL", "sec18", "all-run std [C]", "0.99983", st.stdev(g)),
        chk("EX-18.3-G", "sec18", "Grubbs statistic", "2.0337", abs(18.90 - st.mean(g)) / st.stdev(g)),
        chk("EX-18.3-UA", "sec18", "clean Type A uncertainty [C]", "0.0430", st.stdev(g[:5]) / math.sqrt(5)),
    ]
    T = np.array([313.15, 333.15, 353.15, 373.15])
    X = 1000 / T
    Yp = np.log(np.array([7.384, 19.946, 47.414, 101.42]))
    Sxx = float(((X - X.mean()) ** 2).sum())
    Sxy = float(((X - X.mean()) * (Yp - Yp.mean())).sum())
    mm = Sxy / Sxx
    bb = float(Yp.mean()) - mm * float(X.mean())
    out += [
        chk("EX-18.4-Y1", "sec18", "ln(7.384)", "1.99932", math.log(7.384)),
        chk("EX-18.4-SXX", "sec18", "S_XX", "0.146673", Sxx),
        chk("EX-18.4-SXY", "sec18", "S_XY", "-0.748562", Sxy),
        chk("EX-18.4-M", "sec18", "slope [K]", "-5.10360", mm),
        chk("EX-18.4-B", "sec18", "intercept", "18.3040", bb),
        chk("EX-18.4-DH", "sec18", "Delta H_vap [kJ/mol]", "42.43", -mm * 8.3144626),
        chk("EX-18.4-TB", "sec18", "normal boiling point [C]", "99.77", 1000 / ((math.log(101.325) - bb) / mm) - 273.15),
        chk("EX-18.4-2PT", "sec18", "two-point Delta H_vap [kJ/mol]", "42.42", 8.3144626 * math.log(101.42 / 7.384) / (1 / 313.15 - 1 / 373.15) / 1e3),
    ]
    out += [
        chk("EX-18.5-CS", "sec18", "solid specific heat [J/(kg K)]", "1750", 250.0 * 112.0 / (0.400 * 40.0)),
        chk("EX-18.5-LF", "sec18", "latent heat [kJ/kg]", "180.0", 250.0 * 288.0 / 0.400 / 1e3),
        chk("EX-18.5-SN", "sec18", "tin in liquid [g]", "162.80", 0.555 * 500.0 * 22.0 / 37.5),
    ]
    tt = [7875.0 / 511.0, 83387.5 / 508.0, 104600.0 / 488.0, 564100.0 / 468.0]
    t5 = 1800.0 - sum(tt)
    Tf = 1270.0 - 1170.0 * math.exp(-t5 / 1300.0)
    Vf = (250.0 / 18.01528) * 8.31446 * (Tf + 273.15) / 101325
    out += [
        chk("EX-19.1-T", "sec19", "time to dry steam [s]", "1599.25", sum(tt)),
        chk("EX-19.1-TF", "sec19", "final steam temperature [C]", "267.42", Tf),
        chk("EX-19.1-VF", "sec19", "final steam volume [m3]", "0.61556", Vf),
        chk("EX-19.1-W", "sec19", "boundary work [kJ]", "62.34", 101.325 * (Vf - 0.250 / 916.7)),
    ]
    QH = 2.00 * (0.92 * 1000.0 - 0.10 * SIG_FULL * (450.0 ** 4 - 300.0 ** 4))
    out += [
        chk("EX-19.2-QH", "sec19", "collector heat [W]", "1466.82", QH),
        chk("EX-19.2-QB", "sec19", "building heat [W]", "3789.3", 7.75 * QH / 3),
    ]
    x2s = (6.7450 - 0.6492) / 7.4996
    h2s = 191.81 + x2s * 2392.1
    w = 0.85 * (3116.1 - h2s)
    out += [
        chk("EX-19.3-X2S", "sec19", "isentropic quality", "0.81282", x2s),
        chk("EX-19.3-W", "sec19", "turbine work [kJ/kg]", "832.96", w),
        chk("EX-19.3-SGEN", "sec19", "entropy generation via identity [kJ/(kg K)]", "0.46085", (3116.1 - w - h2s) / 318.96),
    ]
    Tf4 = 300.0 + 12471.7 / (5.25 * 8.3144626)
    out += [
        chk("EX-19.4-TF", "sec19", "final temperature [K]", "585.71", Tf4),
        chk("EX-19.4-PF", "sec19", "final pressure [kPa]", "405.83", 2.500 * 8.3144626 * Tf4 / 0.03000 / 1e3),
    ]
    dV = 50.100 * ((9.50e-4 - 9.75e-6) * 50.00 - 8.20e-5 * 25.00)
    out += [
        chk("EX-19.5-DV", "sec19", "apparent volume change [cm3]", "2.2526", dV),
        chk("EX-19.5-H1", "sec19", "meniscus reading [cm]", "117.63", 5.00 + dV / 0.0200),
        chk("EX-19.5-EXACT", "sec19", "absolute-volume meniscus check [cm]", "117.634",
            (50.100 * (1 + 9.50e-4 * 50 - 8.20e-5 * 25) - 50.000 * (1 + 3 * 3.25e-6 * 50)) / 0.0200),
        chk("EX-19.6-T2", "sec19", "spring-piston final T [K]", "1347.05", 5600.0 / (0.500 * 8.3144626)),
    ]
    Teq7 = (0.800 * 1361.0 / (4 * 0.250 * SIG_FULL)) ** 0.25
    k = 12500.0 / (3 * 0.250 * SIG_FULL * math.pi * 0.25)
    out += [
        chk("EX-19.7-TEQ", "sec19", "probe equilibrium T [K]", "372.25", Teq7),
        chk("EX-19.7-DT", "sec19", "eclipse cooling time [s]", "9792.9", k * (1 / 280.0 ** 3 - 1 / Teq7 ** 3)),
    ]
    Cp = 3.5 * 8.3144626
    out += [
        chk("EX-19.8-W1", "sec19", "single-stage shaft work [kJ]", "15.251", 2 * Cp * 300.0 * (9 ** (2 / 7) - 1) / 1e3),
        chk("EX-19.8-W2", "sec19", "two-stage shaft work [kJ]", "12.877", 4 * Cp * 300.0 * (3 ** (2 / 7) - 1) / 1e3),
        chk("EX-19.8-WISO", "sec19", "isothermal work [kJ]", "10.961", 2 * 8.3144626 * 300.0 * math.log(9) / 1e3),
    ]
    out += [
        chk("EX-20.2-ETA", "sec20", "Carnot efficiency", "0.39988", 200.00 / 500.15),
        chk("EX-20.2-W3", "sec20", "no back-radiation answer [W]", "1453.79", SIG_FULL * 400.15 ** 4),
        chk("EX-20.2-BACK", "sec20", "back-radiation term [W]", "460.22", SIG_FULL * 300.15 ** 4),
        chk("EX-20.2-Q", "sec20", "net exchange [W]", "993.57", SIG_FULL * (400.15 ** 4 - 300.15 ** 4)),
        chk("EX-20.3-LOST", "sec20", "points lost", "16.25", (20 - 20 * 0.75) + (30 - 30 * 15.0 / 24.0)),
        chk("EX-20.4-Q", "sec20", "heat [J]", "-3518.55", 3.5 * 251.325 * -4.00),
        chk("EX-20.5-DH", "sec20", "benzene Delta H [kJ/mol]", "-3271.32", -10.500 * 7.780 / 0.0250 - 1.5 * 8.31446e-3 * 298.15),
        chk("EX-20.5-DSU", "sec20", "freezing Delta S_univ [J/K]", "46.40", 333550 * (1 / 263.15 - 1 / 273.15)),
    ]
    Rc = math.log(37.0 / 34.0) / (2 * math.pi * 0.0400) + 1 / (2 * math.pi * 0.0370 * 10.0)
    out += [
        chk("EX-20.7-RWIRE", "sec20", "insulated wire resistance [m K/W]", "9.4948", math.log(4) / (2 * math.pi * 0.04) + 1 / (2 * math.pi * 0.004 * 10)),
        chk("EX-20.7-RCUP", "sec20", "insulated cup resistance [m K/W]", "0.76659", Rc),
        chk("EX-20.7-DEC", "sec20", "cup loss decrease [%]", "38.94", 100 * (1 - 1 / (2 * math.pi * 0.0340 * 10.0) / Rc)),
        chk("EX-20.7-TG", "sec20", "TG with sleeve [C]", "16.90", 9200 / (418.4 + 126.0)),
    ]
    return out


def sec01_extra():
    # Ex 01.3 [printed 1.2] (as printed: L_f = 333.4, c_ice = 2.093)
    Q12 = 50 * 2.093 * 20 + 50 * 333.4
    Qav = 200 * 4.184 * 30 + 10 * 2256.4 + 10 * 4.184 * 100
    return [chk("EX-01.3-TF", "sec01", "three-phase mix final T [C]", "30.42", (Qav - Q12) / (260.0 * 4.184))]


SECTIONS = [sec00, sec01, sec02, sec03, sec04, sec05, sec06, sec07, sec08, sec09, sec10, sec11, sec12, sec13, sec14, sec15, sec16, sec17_20, sec01_extra]


def run_checks():
    out = []
    for fn in SECTIONS:
        out.extend(fn())
    return out


if __name__ == "__main__":
    res = run_checks()
    bad = [r for r in res if not r["passed"]]
    for r in bad:
        print("FAIL", r["id"], r["detail"])
    print(f"{len(res) - len(bad)}/{len(res)} pass")
