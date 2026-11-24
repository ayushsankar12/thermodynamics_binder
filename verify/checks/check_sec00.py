#!/usr/bin/env python3
"""Independent numerical verification for §0 (Competition Command Center) and Appendices D--H."""
import math

def run_checks() -> list[dict]:
    results = []

    # Check 1: Worked Example 0.1 (ex:00.1) — Clean Run vs. Penalized Run Scoring Audit
    part1_alpha = 78.20
    part1_max = 85.00
    t_start = 21.4
    t_final = 36.6
    t_pred = 36.3
    tg_max = 16.0
    pe_max = 0.9950

    es_alpha = 50.0 * (part1_alpha / part1_max)
    tg_alpha = max(0.0, t_final - t_start)
    ts_alpha = 30.0 * (tg_alpha / tg_max)
    pe_alpha = max(0.0, 1.0 - abs(t_final - t_pred) / t_final)
    ps_alpha = 20.0 * (pe_alpha / pe_max)
    fs_alpha = es_alpha + ts_alpha + ps_alpha

    exp_es = 46.0
    exp_tg = 15.2
    exp_ts = 28.5
    exp_pe = 36.3 / 36.6
    exp_ps = 20.0 * (36.3 / 36.6) / 0.9950
    exp_fs = exp_es + exp_ts + exp_ps

    err1 = max(
        abs(es_alpha - exp_es),
        abs(tg_alpha - exp_tg),
        abs(ts_alpha - exp_ts),
        abs(pe_alpha - exp_pe),
        abs(ps_alpha - exp_ps),
        abs(fs_alpha - exp_fs),
    )
    results.append({
        "id": "SEC00_EX01_CLEAN_SCORE",
        "section": "sec00",
        "description": "Worked Example 0.1 Team Alpha clean run ES, TG, TS, PE, PS, and FS",
        "passed": err1 < 1e-12 and abs(fs_alpha - 94.435744) < 1e-5,
        "expected": round(exp_fs, 6),
        "computed": round(fs_alpha, 6),
        "rel_error": err1 / exp_fs,
        "tolerance": 1e-9,
        "method": "Direct evaluation of 2027 Rule 6.c-f and v2.0.0 Scoresheet formulas",
    })

    # Check 2: Worked Example 0.1 Team Beta penalty stacking (Vc=1, Vp=1 -> M_pen = 0.7 * 0.9 = 0.63)
    m_pen_beta = (0.7 ** 1) * (0.9 ** 1)
    ts_beta = ts_alpha * m_pen_beta
    ps_beta = ps_alpha * m_pen_beta
    fs_beta = es_alpha + ts_beta + ps_beta
    delta_pen = fs_alpha - fs_beta

    exp_fs_beta = exp_es + exp_ts * 0.63 + exp_ps * 0.63
    err2 = abs(fs_beta - exp_fs_beta)
    results.append({
        "id": "SEC00_EX01_PENALTY_STACK",
        "section": "sec00",
        "description": "Worked Example 0.1 Team Beta penalty multiplier (0.7^1 * 0.9^1 = 0.63) and 17.92 pt loss",
        "passed": err2 < 1e-12 and abs(m_pen_beta - 0.63) < 1e-12 and abs(delta_pen - 17.921225) < 1e-4,
        "expected": round(exp_fs_beta, 6),
        "computed": round(fs_beta, 6),
        "rel_error": err2 / exp_fs_beta,
        "tolerance": 1e-9,
        "method": "Independent penalty factor verification against 2027ThermodynamicsBC_scoresheet.xlsx cell AG8",
    })

    # Check 3: Worked Example 0.2 (ex:00.2) — Tiebreaker TB1 (Best TS) & PE Celsius vs Kelvin Denominator Trap
    fs_gamma = 44.00 + 29.00 + 18.50
    fs_delta = 45.50 + 27.50 + 18.50
    tb1_gamma_wins = (abs(fs_gamma - fs_delta) < 1e-12) and (29.00 > 27.50)

    tf_c = 32.0
    tf_k = tf_c + 273.15
    d_err = 0.40
    d_pe_c = d_err / tf_c
    d_ps_c = 20.0 * d_pe_c
    ratio_k_c = tf_k / tf_c

    results.append({
        "id": "SEC00_EX02_TIEBREAKER_AND_PE_TRAP",
        "section": "sec00",
        "description": "Worked Example 0.2 Tiebreaker TB1 (Best TS) and PE Celsius vs Kelvin denominator sensitivity",
        "passed": tb1_gamma_wins and abs(d_pe_c - 0.0125) < 1e-12 and abs(d_ps_c - 0.25) < 1e-12 and abs(ratio_k_c - 9.5359375) < 1e-9,
        "expected": 0.25,
        "computed": round(d_ps_c, 6),
        "rel_error": abs(d_ps_c - 0.25) / 0.25,
        "tolerance": 1e-9,
        "method": "Rule 6.b, 6.f.i, 6.j tiebreaker and partial-derivative sensitivity analysis",
    })

    # Check 4: Penalty Multiplier Matrix (0.7^Vc * 0.9^Vp) for Vc in 0..3, Vp in 0..2
    expected_grid = {
        (0, 0): 1.0000,
        (0, 1): 0.9000,
        (0, 2): 0.8100,
        (1, 0): 0.7000,
        (1, 1): 0.6300,
        (1, 2): 0.5670,
        (2, 0): 0.4900,
        (2, 1): 0.4410,
        (2, 2): 0.3969,
        (3, 0): 0.3430,
        (3, 1): 0.3087,
        (3, 2): 0.27783,
    }
    max_grid_err = 0.0
    for (vc, vp), val in expected_grid.items():
        comp = (0.7 ** vc) * (0.9 ** vp)
        max_grid_err = max(max_grid_err, abs(comp - val))

    results.append({
        "id": "SEC00_PENALTY_MATRIX_GRID",
        "section": "sec00",
        "description": "Penalty multiplier table M_pen = 0.7^Vc * 0.9^Vp across Vc=0..3, Vp=0..2",
        "passed": max_grid_err < 1e-12,
        "expected": 0.0,
        "computed": max_grid_err,
        "rel_error": max_grid_err,
        "tolerance": 1e-12,
        "method": "Exact power-law verification across 12 penalty states",
    })

    return results

if __name__ == "__main__":
    recs = run_checks()
    for r in recs:
        status = "PASS" if r["passed"] else "FAIL"
        print(f"[{status}] {r['id']}: {r['description']} (computed={r['computed']}, expected={r['expected']})")
    assert all(r["passed"] for r in recs), "One or more checks failed!"
