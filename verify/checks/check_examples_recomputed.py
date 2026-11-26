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
    return out


SECTIONS = [sec00, sec01, sec02, sec03, sec04, sec05, sec06, sec07, sec09, sec11, sec12]


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
