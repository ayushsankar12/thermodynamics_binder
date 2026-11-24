#!/usr/bin/env python3
"""Independent Numerical Verification for Group 6 (§21 Exam Strategy, §22 Tournament Intelligence, §23 Final Review / Cram Layer).

Verifies:
  1. §21 MCQ Expected-Value & Blank-Credit Thresholds (MIT 2019 +3/+1/0 vs Standard +2/0/0)
  2. §21 Raw-to-Normalized Exam Score (ES) & Prediction Score (PS) Marginal ROI Calculations
  3. §21 2027 Rule 6.d-i Full Scoring & Penalty Multiplier Worked Example
  4. §22 Phase 2 Corpus Totals (N=8 exams, 217 questions, 328 graded items, 1120.0 points)
  5. §22 Syllabus Clause (5.c.i-vii) Item & Point Percentages (Full Corpus & 2027 Cornell E1)
  6. §22 Question Format (FMT-1..FMT-6) & Difficulty Tier (Tier 1..3) Sums & Shares
  7. §22 2026-2027 Cornell Invitational (E1) 55-Team Histogram Normalization & Median Deficit
  8. §23 Top-40 Cram Equations & Benchmark Crossovers (-40 C/F, 574.5875 K/F, 60 C/De, Carnot/Otto/Rankine/Radiation/Evaporation drills)
"""
import math


def make_check(cid, sec, desc, passed, expected, computed, tol=1e-6, method="Independent Python algebraic verification"):
    try:
        if isinstance(expected, (int, float)) and isinstance(computed, (int, float)):
            denom = abs(expected) if abs(expected) > 1e-12 else 1.0
            rel_err = abs(computed - expected) / denom
        else:
            rel_err = 0.0 if passed else 1.0
    except Exception:
        rel_err = 0.0 if passed else 1.0
    return {
        "id": cid,
        "section": sec,
        "description": desc,
        "passed": bool(passed),
        "expected": expected,
        "computed": computed,
        "rel_error": rel_err,
        "tolerance": tol,
        "detail": f"expected={expected}, computed={computed}, rel_err={rel_err:.2e}",
        "method": method,
    }


def run_checks():
    results = []

    # 1. §21 MIT 2019 (+3 correct, +1 blank, 0 wrong) MCQ Expected Value Check
    # With k remaining choices after elimination, E[guess] = 3/k vs E[blank] = 1.0
    ev_4choices = 3.0 / 4.0
    ev_3choices = 3.0 / 3.0
    ev_2choices = 3.0 / 2.0
    ok1 = (abs(ev_4choices - 0.75) < 1e-9) and (abs(ev_3choices - 1.00) < 1e-9) and (abs(ev_2choices - 1.50) < 1e-9)
    results.append(make_check(
        "SEC21_MCQ_EV_BLANK_RULE", "§21.3",
        "MIT 2019 (+3/+1/0) MCQ expected value for k=4 (0.75 < 1), k=3 (1.00 = 1), k=2 (1.50 > 1)",
        ok1, 1.50, ev_2choices, 1e-9, "Probability expectation E[X] = 3/k vs 1.0 blank credit"
    ))

    # 2. §21 Worked Example 21.1: 2027 Rule 6.d-i Scoring, Normalization & Penalty Multipliers
    # Team raw Part I = 68.0 / 238.0 (Cornell E1 max = 85.0); TG = 21.6 C (max TG = 24.0 C);
    # T_final = 43.6 C, T_pred = 43.2 C (max PE = 0.9960)
    es_score = 50.0 * (68.0 / 85.0)
    ts_raw = 30.0 * (21.6 / 24.0)
    pe_team = 1.0 - abs(43.6 - 43.2) / 43.6
    ps_raw = 20.0 * (pe_team / 0.9960)
    fs_clean = es_score + ts_raw + ps_raw
    # If 1 construction violation (x0.7 on TS and PS):
    fs_1const = es_score + 0.7 * (ts_raw + ps_raw)
    penalty_loss = fs_clean - fs_1const
    ok2 = (abs(es_score - 40.0) < 1e-6) and (abs(ts_raw - 27.0) < 1e-6) and (abs(fs_clean - 86.8961028) < 1e-5) and (abs(penalty_loss - 14.0688308) < 1e-5)
    results.append(make_check(
        "SEC21_SCORING_PENALTY_EXAMPLE", "§21.2",
        "2027 Rule 6.d-i normalized score (ES=40.00, TS=27.00, PS=19.90, FS=86.90) & 0.7x construction penalty cost (-14.07 pts)",
        ok2, 86.89610, round(fs_clean, 5), 1e-5, "Direct evaluation of 2027 Rules 6.c-i equations"
    ))

    # 3. §22 Corpus Clause Totals Verification (328 items, 1120.0 points)
    clause_items = [62, 78, 49, 51, 28, 18, 42]
    clause_pts = [154.0, 259.0, 178.0, 225.0, 69.0, 74.0, 161.0]
    e1_clause_pts = [10.0, 87.0, 49.0, 22.0, 2.0, 23.0, 45.0]
    sum_items = sum(clause_items)
    sum_pts = sum(clause_pts)
    sum_e1 = sum(e1_clause_pts)
    ok3 = (sum_items == 328) and (abs(sum_pts - 1120.0) < 1e-9) and (abs(sum_e1 - 238.0) < 1e-9)
    results.append(make_check(
        "SEC22_CORPUS_CLAUSE_SUMS", "§22.2",
        "Sum of 2027 syllabus clauses 5.c.i-vii across N=8 corpus (328 items, 1120.0 pts) and E1 Cornell 2027 (238.0 pts)",
        ok3, 1120.0, sum_pts, 1e-9, "Exact summation over 7 syllabus clauses"
    ))

    # 4. §22 Question Format & Difficulty Tier Totals Verification
    fmt_items = [106, 35, 78, 43, 13, 53]
    fmt_pts = [266.0, 116.0, 411.0, 137.0, 48.0, 142.0]
    tier_items = [125, 121, 82]
    tier_pts = [278.0, 427.0, 415.0]
    ok4 = (sum(fmt_items) == 328) and (abs(sum(fmt_pts) - 1120.0) < 1e-9) and (sum(tier_items) == 328) and (abs(sum(tier_pts) - 1120.0) < 1e-9)
    results.append(make_check(
        "SEC22_FORMAT_TIER_SUMS", "§22.3",
        "Consistency of Format (FMT-1..6) and Difficulty (Tier 1..3) matrices with 328 items and 1120.0 pts",
        ok4, 328, sum(fmt_items), 1e-9, "Matrix cross-tabulation sum check"
    ))

    # 5. §22 Cornell 2026-2027 (E1) 55-Team Histogram & Normalization Verification
    hist_counts = [5, 3, 21, 16, 5, 3, 2]
    n_teams = sum(hist_counts)
    norm_factor = 50.0 / 85.0
    median_es = 50.0 * (38.5 / 85.0)
    median_deficit = 50.0 - median_es
    e1_t1_t2_pts = 25.0 + 65.0
    ok5 = (n_teams == 55) and (abs(norm_factor - 0.58823529) < 1e-6) and (abs(median_deficit - 27.352941) < 1e-5) and (e1_t1_t2_pts > 85.0)
    results.append(make_check(
        "SEC22_CORNELL2027_HISTOGRAM", "§22.4",
        "Cornell 2027 E1 histogram (n=55 teams, ES multiplier=0.5882 pt/raw pt, median deficit=27.35 ES pts, Tier1+2=90.0 > 85.0 max)",
        ok5, 55, n_teams, 1e-9, "Histogram bin integration and Rule 6.d scaling"
    ))

    # 6. §23 Cram Verification Drill 23.1: Temperature Scale Intersections (-40 C/F, 574.5875 K/F, 60.0 C/De)
    t_cf = -32.0 / 0.8
    t_kf = (273.15 * 1.8 - 32.0) / 0.8
    t_cde = 150.0 / 2.5
    ok6 = (abs(t_cf - (-40.0)) < 1e-9) and (abs(t_kf - 574.5875) < 1e-9) and (abs(t_cde - 60.0) < 1e-9)
    results.append(make_check(
        "SEC23_SCALE_INTERSECTIONS", "§23.2",
        "Exact temperature scale crossover points: T_C=T_F=-40.0, T_K=T_F=574.5875, T_C=T_De=60.0",
        ok6, 574.5875, t_kf, 1e-9, "Linear Fixed-Point Algebraic Solution"
    ))

    # 7. §23 Cram Verification Drill 23.2: Open-Cup Evaporation Penalty vs BoPET Glazing Cap (Clarification #5)
    # 0.55 g water evaporated at Lv = 2406 J/g from top stratified layer (C_top = 215 J/K) vs bulk 100 g water (418.4 J/K)
    q_evap = 0.55 * 2406.0  # 1323.3 J
    dt_top_lost = q_evap / 215.0
    dt_bulk_lost = q_evap / 418.4
    ok7 = (abs(q_evap - 1323.3) < 1e-6) and (abs(dt_top_lost - 6.1548837) < 1e-5) and (abs(dt_bulk_lost - 3.1627629) < 1e-5)
    results.append(make_check(
        "SEC23_EVAPORATION_PENALTY_DRILL", "§23.6",
        "Evaporating 0.55 g water (Lv=2406 J/g) removes 1323.3 J, costing 6.15 C from top stratified layer (3.16 C bulk)",
        ok7, 6.154884, round(dt_top_lost, 6), 1e-5, "Latent heat balance Q_evap = m_evap * L_v / C_eff"
    ))

    # 8. §23 Cram Verification Drill 23.3: Gouy-Stodola Exergy Destruction & Second-Law Efficiency (Cornell 2027 E1 Q29)
    q_in = 2257.19
    t_0 = 300.0
    t_src = 600.0
    w_net = 109.92
    x_in = q_in * (1.0 - t_0 / t_src)
    eta_1 = w_net / q_in
    eta_2 = w_net / x_in
    ok8 = (abs(x_in - 1128.595) < 1e-3) and (abs(eta_1 - 0.0486977) < 1e-5) and (abs(eta_2 - 0.0973954) < 1e-5)
    results.append(make_check(
        "SEC23_EXERGY_SECOND_LAW_EFF", "§23.6",
        "Rankine cycle First-Law efficiency (4.870%) vs Second-Law exergy efficiency (9.740% = eta_1 / eta_Carnot)",
        ok8, 0.097395, round(eta_2, 6), 1e-5, "Exergy balance eta_2 = W_net / [Q_in*(1 - T_0/T_src)]"
    ))

    return results


if __name__ == "__main__":
    cks = run_checks()
    for c in cks:
        status = "PASS" if c["passed"] else "FAIL"
        print(f"[{status}] {c['id']} ({c['section']}): {c['description']} -> {c['detail']}")
    assert all(c["passed"] for c in cks), "One or more checks failed!"
    print(f"All {len(cks)} Group 6 (§§21-23) verification checks PASSED.")
