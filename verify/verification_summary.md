# Independent Numerical Verification Summary (`verify/verify_all.py`)

- **Date:** `2026-11-22T23:15:12`
- **Python Interpreter:** `C:\Users\ayush\AppData\Local\Programs\Python\Python310\python.exe` (`3.10.4`)
- **Modules Executed:** `8`
- **Total Checks Run:** **`274`** | **Passed:** **`274`** | **Failed:** **`0`** | **Elapsed:** `0.73 s`

| Module | Check ID | Section | Result | Detail | Verification Method |
|---|---|---|---|---|---|
| `check_sec00` | `SEC00_EX01_CLEAN_SCORE` | `sec00` | PASS | expected=94.435744 computed=94.435744 rel_err=7.524086785811082e-17 | Direct evaluation of 2027 Rule 6.c-f and v2.0.0 Scoresheet formulas |
| `check_sec00` | `SEC00_EX01_PENALTY_STACK` | `sec00` | PASS | expected=76.514519 computed=76.514519 rel_err=0.0 | Independent penalty factor verification against 2027ThermodynamicsBC_scoresheet.xlsx cell AG8 |
| `check_sec00` | `SEC00_EX02_TIEBREAKER_AND_PE_TRAP` | `sec00` | PASS | expected=0.25 computed=0.25 rel_err=0.0 | Rule 6.b, 6.f.i, 6.j tiebreaker and partial-derivative sensitivity analysis |
| `check_sec00` | `SEC00_PENALTY_MATRIX_GRID` | `sec00` | PASS | expected=0.0 computed=1.1102230246251565e-16 rel_err=1.1102230246251565e-16 | Exact power-law verification across 12 penalty states |
| `check_sec01_appA` | `C01_R_NA_kB` | `QS-01/AppA` | PASS | exp=8.31446, comp=8.31446, rel_err=0.00e+00 <= 1.0e-12 | CODATA 2022 exact product N_A*k_B |
| `check_sec01_appA` | `C02_Stefan_Boltzmann` | `QS-01/AppA` | PASS | exp=5.67037e-08, comp=5.67037e-08, rel_err=3.25e-11 <= 1.0e-09 | Exact Planck radiation integral |
| `check_sec01_appA` | `C03_Wien_b` | `QS-01/AppA` | PASS | exp=0.00289777, comp=0.00289777, rel_err=6.39e-11 <= 1.0e-09 | Transcendental Planck root x=4.96511423 |
| `check_sec01_appA` | `C04_Radiation_c1` | `AppA` | PASS | exp=3.74177e-16, comp=3.74177e-16, rel_err=5.15e-11 <= 1.0e-09 | CODATA 2022 definition |
| `check_sec01_appA` | `C05_Radiation_c2` | `AppA` | PASS | exp=0.0143878, comp=0.0143878, rel_err=3.50e-10 <= 1.0e-09 | CODATA 2022 definition |
| `check_sec01_appA` | `C06_Faraday_F` | `AppA` | PASS | exp=96485.3, comp=96485.3, rel_err=1.51e-16 <= 1.0e-09 | CODATA 2022 exact product |
| `check_sec01_appA` | `C07_Vm_STP_1bar` | `QS-01/AppA` | PASS | exp=0.022711, comp=0.022711, rel_err=6.54e-11 <= 1.0e-08 | Ideal gas law V_m = R*T/P |
| `check_sec01_appA` | `C08_Vm_STP_1atm` | `QS-01/AppA` | PASS | exp=0.022414, comp=0.022414, rel_err=2.24e-10 <= 1.0e-08 | Ideal gas law V_m = R*T/P |
| `check_sec01_appA` | `C09_Loschmidt_n0` | `AppA` | PASS | exp=2.68678e+25, comp=2.68678e+25, rel_err=2.97e-10 <= 1.0e-08 | Number density P/(k_B*T) |
| `check_sec01_appA` | `C10_R_Latm` | `QS-01/AppA` | PASS | exp=0.0820574, comp=0.0820574, rel_err=1.17e-11 <= 1.0e-09 | R / 101.325 kPa/atm |
| `check_sec01_appA` | `C11_R_calth` | `QS-01/AppA` | PASS | exp=1.9872, comp=1.9872, rel_err=2.05e-11 <= 1.0e-09 | R / 4.184 J/cal_th |
| `check_sec01_appA` | `C12_R_LTorr` | `QS-01/AppA` | PASS | exp=62.3636, comp=62.3636, rel_err=2.45e-11 <= 1.0e-08 | R * 760 / 101.325 |
| `check_sec01_appA` | `C13_Inter_C_F` | `QS-01/AppA` | PASS | exp=-40, comp=-40, rel_err=0.00e+00 <= 1.0e-12 | Linear intersection T = 1.8*T + 32 |
| `check_sec01_appA` | `C14_Inter_K_F` | `QS-01/AppA` | PASS | exp=574.587, comp=574.587, rel_err=0.00e+00 <= 1.0e-10 | Linear intersection T = 1.8*(T-273.15)+32 |
| `check_sec01_appA` | `C15_Inter_C_De` | `QS-01/AppA` | PASS | exp=60, comp=60, rel_err=0.00e+00 <= 1.0e-12 | Linear intersection T = 150 - 1.5*T |
| `check_sec01_appA` | `C16_Inter_F_De` | `QS-01/AppA` | PASS | exp=96.3636, comp=96.3636, rel_err=0.00e+00 <= 1.0e-10 | Exact rational root T_C=1180/33, T_F=T_De=1060/11 |
| `check_sec01_appA` | `C17_Inter_C_Ro` | `QS-01/AppA` | PASS | exp=15.7895, comp=15.7895, rel_err=0.00e+00 <= 1.0e-10 | Exact rational root +300/19 |
| `check_sec01_appA` | `C18_Water_Lv_0.01C` | `AppA` | PASS | exp=2500.9, comp=2500.9, rel_err=2.45e-07 <= 1.0e-03 | NIST IAPWS-95 enthalpy difference |
| `check_sec01_appA` | `C19_Water_Pr_0.01C` | `AppA` | PASS | exp=13.61, comp=13.6061, rel_err=2.89e-04 <= 2.0e-03 | Dimensionless Prandtl identity |
| `check_sec01_appA` | `C18_Water_Lv_4.0C` | `AppA` | PASS | exp=2491.39, comp=2491.39, rel_err=1.20e-06 <= 1.0e-03 | NIST IAPWS-95 enthalpy difference |
| `check_sec01_appA` | `C19_Water_Pr_4.0C` | `AppA` | PASS | exp=11.67, comp=11.6653, rel_err=4.00e-04 <= 2.0e-03 | Dimensionless Prandtl identity |
| `check_sec01_appA` | `C18_Water_Lv_20.0C` | `AppA` | PASS | exp=2453.49, comp=2453.49, rel_err=1.63e-06 <= 1.0e-03 | NIST IAPWS-95 enthalpy difference |
| `check_sec01_appA` | `C19_Water_Pr_20.0C` | `AppA` | PASS | exp=7.01, comp=7.00911, rel_err=1.28e-04 <= 2.0e-03 | Dimensionless Prandtl identity |
| `check_sec01_appA` | `C18_Water_Lv_25.0C` | `AppA` | PASS | exp=2441.67, comp=2441.67, rel_err=0.00e+00 <= 1.0e-03 | NIST IAPWS-95 enthalpy difference |
| `check_sec01_appA` | `C19_Water_Pr_25.0C` | `AppA` | PASS | exp=6.14, comp=6.13691, rel_err=5.03e-04 <= 2.0e-03 | Dimensionless Prandtl identity |
| `check_sec01_appA` | `C18_Water_Lv_40.0C` | `AppA` | PASS | exp=2405.97, comp=2405.97, rel_err=0.00e+00 <= 1.0e-03 | NIST IAPWS-95 enthalpy difference |
| `check_sec01_appA` | `C19_Water_Pr_40.0C` | `AppA` | PASS | exp=4.34, comp=4.34108, rel_err=2.49e-04 <= 2.0e-03 | Dimensionless Prandtl identity |
| `check_sec01_appA` | `C18_Water_Lv_60.0C` | `AppA` | PASS | exp=2357.62, comp=2357.62, rel_err=1.93e-16 <= 1.0e-03 | NIST IAPWS-95 enthalpy difference |
| `check_sec01_appA` | `C19_Water_Pr_60.0C` | `AppA` | PASS | exp=3, comp=2.9961, rel_err=1.30e-03 <= 2.0e-03 | Dimensionless Prandtl identity |
| `check_sec01_appA` | `C18_Water_Lv_100.0C` | `AppA` | PASS | exp=2256.43, comp=2256.43, rel_err=0.00e+00 <= 1.0e-03 | NIST IAPWS-95 enthalpy difference |
| `check_sec01_appA` | `C19_Water_Pr_100.0C` | `AppA` | PASS | exp=1.75, comp=1.75286, rel_err=1.64e-03 <= 2.0e-03 | Dimensionless Prandtl identity |
| `check_sec01_appA` | `C20_Gas_gamma_He` | `QS-05/AppA` | PASS | exp=1.6667, comp=1.66667, rel_err=2.00e-05 <= 5.0e-04 | Classical equipartition theorem |
| `check_sec01_appA` | `C21_Gas_Mayer_He` | `QS-05/AppA` | PASS | exp=8.31446, comp=8.314, rel_err=5.56e-05 <= 5.0e-04 | Mayer ideal gas identity |
| `check_sec01_appA` | `C20_Gas_gamma_Ne` | `QS-05/AppA` | PASS | exp=1.6667, comp=1.66667, rel_err=2.00e-05 <= 5.0e-04 | Classical equipartition theorem |
| `check_sec01_appA` | `C21_Gas_Mayer_Ne` | `QS-05/AppA` | PASS | exp=8.31446, comp=8.314, rel_err=5.56e-05 <= 5.0e-04 | Mayer ideal gas identity |
| `check_sec01_appA` | `C20_Gas_gamma_Ar` | `QS-05/AppA` | PASS | exp=1.6667, comp=1.66667, rel_err=2.00e-05 <= 5.0e-04 | Classical equipartition theorem |
| `check_sec01_appA` | `C21_Gas_Mayer_Ar` | `QS-05/AppA` | PASS | exp=8.31446, comp=8.314, rel_err=5.56e-05 <= 5.0e-04 | Mayer ideal gas identity |
| `check_sec01_appA` | `C20_Gas_gamma_H2` | `QS-05/AppA` | PASS | exp=1.4, comp=1.4, rel_err=0.00e+00 <= 5.0e-04 | Classical equipartition theorem |
| `check_sec01_appA` | `C21_Gas_Mayer_H2` | `QS-05/AppA` | PASS | exp=8.31446, comp=8.315, rel_err=6.46e-05 <= 5.0e-04 | Mayer ideal gas identity |
| `check_sec01_appA` | `C20_Gas_gamma_N2` | `QS-05/AppA` | PASS | exp=1.4, comp=1.4, rel_err=0.00e+00 <= 5.0e-04 | Classical equipartition theorem |
| `check_sec01_appA` | `C21_Gas_Mayer_N2` | `QS-05/AppA` | PASS | exp=8.31446, comp=8.315, rel_err=6.46e-05 <= 5.0e-04 | Mayer ideal gas identity |
| `check_sec01_appA` | `C22_QS02_Bimetallic` | `QS-02` | PASS | exp=2.85714, comp=2.85714, rel_err=5.00e-11 <= 1.0e-06 | Small-angle arc length difference |
| `check_sec01_appA` | `C23_QS03_IceMix` | `QS-03` | PASS | exp=8.0631, comp=8.0631, rel_err=1.78e-09 <= 1.0e-05 | Enthalpy balance relative to 0 C liquid water |
| `check_sec01_appA` | `C24_QS04_LeverRule` | `QS-04` | PASS | exp=0.520871, comp=0.520871, rel_err=6.48e-09 <= 1.0e-06 | Tie-line mass balance (w0-wa)/(wE-wa) |
| `check_sec01_appA` | `C25_QS06_AdiabaticWork` | `QS-06` | PASS | exp=-741.101, comp=-741.101, rel_err=1.53e-16 <= 1.0e-10 | Closed-form polytropic integral |
| `check_sec01_appA` | `C26_QS08_OttoEff` | `QS-08` | PASS | exp=0.564725, comp=0.564725, rel_err=3.25e-08 <= 1.0e-06 | 1 - r^(1-gamma) |
| `check_sec01_appA` | `C27_QS09_CritRadius` | `QS-09` | PASS | exp=0.004, comp=0.004, rel_err=0.00e+00 <= 1.0e-12 | dR_cyl/dr_o = 0 extremum |
| `check_sec01_appA` | `C28_QS11_RadShields` | `QS-11` | PASS | exp=0.333333, comp=0.333333, rel_err=0.00e+00 <= 1.0e-12 | Series radiative surface+space resistances |
| `check_sec01_appA` | `C29_QS12_CollectorTf` | `QS-12/QS-13` | PASS | exp=41.1898, comp=41.1899, rel_err=3.99e-06 <= 1.0e-04 | Exact exponential ODE solution |
| `check_sec01_appA` | `C30_QS13_Rule6f_PE` | `QS-13` | PASS | exp=0.980583, comp=0.980583, rel_err=1.13e-16 <= 1.0e-09 | Rule 6.f PE = 1 - \|Tf - Tpred\|/Tf |
| `check_sec02_05` | `sec02_worked_examples` | `check_sec02_05` | PASS | ex02.1=True, ex02.2=True (dU=573.2 J), ex02.3=True (W_cyc=400.0 J), ex02.4=True | ex02.1=True, ex02.2=True (dU=573.2 J), ex02.3=True (W_cyc=400.0 J), ex02.4=True |
| `check_sec02_05` | `sec03_worked_examples` | `check_sec02_05` | PASS | ex03.1=True, ex03.2=True, ex03.3=True, ex03.4=True, ex03.5=True (dT=0.3541 K) | ex03.1=True, ex03.2=True, ex03.3=True, ex03.4=True, ex03.5=True (dT=0.3541 K) |
| `check_sec02_05` | `sec04_worked_examples` | `check_sec02_05` | PASS | curve=True, ex04.1..11=[True, True, True, True, True, True, True, True, True, True, True] | curve=True, ex04.1..11=[True, True, True, True, True, True, True, True, True, True, True] |
| `check_sec02_05` | `sec05_worked_examples` | `check_sec02_05` | PASS | ex05.1..8=[True, True, True, True, True, True, True, True] | ex05.1..8=[True, True, True, True, True, True, True, True] |
| `check_sec02_05` | `sec02_05_structure_and_figures` | `check_sec02_05` | PASS | All 4 chapters, 10 figure labels, 26 worked examples & 8 scientists verified | All 4 chapters, 10 figure labels, 26 worked examples & 8 scientists verified |
| `check_sec02_05` | `sec02_05_json_consistency` | `check_sec02_05` | PASS | k_B*N_A=8.3144626 J/(mol K) == R=8.3144626, scientists=8 | k_B*N_A=8.3144626 J/(mol K) == R=8.3144626, scientists=8 |
| `check_sec06_09` | `ex06_1` | `sec06` | PASS | expected=0.97658, computed=0.976581, rel_err=1.37e-06 (tol=5.0e-04) | Direct molar PV_m/(RT) evaluation vs specific gas constant R_s*T/P_abs |
| `check_sec06_09` | `ex06_2` | `sec06` | PASS | expected=-1.33, computed=-1.32996, rel_err=2.84e-05 (tol=5.0e-04) | Mole conservation n_Af + n_Bf = n_Ai + n_Bi at uniform P_f |
| `check_sec06_09` | `ex06_3` | `sec06` | PASS | expected=0.62492, computed=0.624919, rel_err=1.02e-06 (tol=5.0e-04) | Hydrostatic + NIST P_sat subtraction and Graham flux product identity |
| `check_sec06_09` | `ex06_4` | `sec06` | PASS | expected=6.7208e-08, computed=6.72078e-08, rel_err=3.14e-06 (tol=5.0e-04) | Number density n_# = P/(k_B*T) hard-sphere collision cross-section |
| `check_sec06_09` | `ex06_5` | `sec06` | PASS | expected=545.36, computed=545.358, rel_err=4.37e-06 (tol=5.0e-04) | Extensive mole-weighted C_P/C_V ratio vs acoustic wave equation |
| `check_sec06_09` | `ex06_6` | `sec06` | PASS | expected=-22.751, computed=-22.7519, rel_err=3.96e-05 (tol=5.0e-04) | Internal energy conservation dU_vdW = n*C_V*dT + a*n^2*(1/V1 - 1/V2) = 0 |
| `check_sec06_09` | `ex06_7` | `sec06` | PASS | expected=534.5, computed=534.501, rel_err=2.19e-06 (tol=5.0e-04) | Simultaneous mechanical pressure balance P_1f = P_2f and internal energy conservation |
| `check_sec06_09` | `ex07_1` | `sec07` | PASS | expected=632.75, computed=632.745, rel_err=7.90e-06 (tol=5.0e-04) | Cross-checked Physics dU = Q - W_by vs Chemistry dU = q + w_on |
| `check_sec06_09` | `ex07_2` | `sec07` | PASS | expected=1200, computed=1200, rel_err=0.00e+00 (tol=1.0e-05) | Trapezoidal/rectangular area integration vs leg-by-leg First Law sum |
| `check_sec06_09` | `ex07_3` | `sec07` | PASS | expected=5937.4, computed=5937.36, rel_err=6.86e-06 (tol=5.0e-04) | Staircase adiabatic + isobaric enthalpy change across N=3 equal pressure ratios |
| `check_sec06_09` | `ex07_4` | `sec07` | PASS | expected=-6.4853, computed=-6.48528, rel_err=2.95e-06 (tol=5.0e-04) | Direct state-function dU = n*R*(T2-T1)/(gamma-1) evaluation |
| `check_sec06_09` | `ex07_5` | `sec07` | PASS | expected=-3.0996, computed=-3.09957, rel_err=1.07e-05 (tol=5.0e-04) | Polytropic molar heat capacity C_n = C_V*(n-gamma)/(n-1) vs First Law dU + W_by |
| `check_sec06_09` | `ex07_6` | `sec07` | PASS | expected=3457.4, computed=3457.89, rel_err=1.41e-04 (tol=5.0e-04) | Sum of isothermal expansion and compression work around closed 4-leg cycle |
| `check_sec06_09` | `ex07_7` | `sec07` | PASS | expected=-24.389, computed=-24.3911, rel_err=8.49e-05 (tol=5.0e-04) | Virial/vdW Joule-Thomson coefficient mu_JT = (2a/(RT) - b)/C_P |
| `check_sec06_09` | `ex07_8` | `sec07` | PASS | expected=868.62, computed=868.62, rel_err=4.67e-07 (tol=5.0e-04) | Steady-Flow Energy Equation kinetic energy balance v_2 = sqrt(v_1^2 + 2*dh) |
| `check_sec06_09` | `ex07_9` | `sec07` | PASS | expected=1060.3, computed=1060.42, rel_err=1.12e-04 (tol=5.0e-04) | Isothermal pressure-ratio work nRT_H*ln(P2/P3) times Carnot efficiency |
| `check_sec06_09` | `ex07_10` | `sec07` | PASS | expected=37, computed=37, rel_err=2.01e-07 (tol=5.0e-04) | Piecewise P-V area integration plus monatomic state-function dU |
| `check_sec06_09` | `ex07_11` | `sec07` | PASS | expected=1.4211, computed=1.42108, rel_err=1.73e-05 (tol=5.0e-04) | Unsteady control-volume energy ledger and steady-flow adiabatic T-junction enthalpy balance |
| `check_sec06_09` | `ex07_12` | `sec07` | PASS | expected=-3267.62, computed=-3267.62, rel_err=4.79e-07 (tol=5.0e-04) | dH_rxn = dU_rxn + dn_gas*R*T and ellipse area pi*a*b |
| `check_sec06_09` | `ex07_13` | `sec07` | PASS | expected=6822.2, computed=6822.24, rel_err=5.63e-06 (tol=5.0e-04) | AM-GM geometric-mean intermediate pressure P_mid = sqrt(P1*P2) work optimization |
| `check_sec06_09` | `ex07_14` | `sec07` | PASS | expected=1023.6, computed=1023.59, rel_err=1.23e-05 (tol=5.0e-04) | SFEE turbine enthalpy + kinetic energy balance coupled to counterflow recuperator |
| `check_sec06_09` | `ex08_1` | `sec08` | PASS | expected=219.92, computed=219.919, rel_err=6.16e-06 (tol=5.0e-04) | Piecewise reversible warming/melting entropy integral and geometric-mean T_f,rev = sqrt(T_H*T_C) |
| `check_sec06_09` | `ex08_2` | `sec08` | PASS | expected=5.0545, computed=5.05454, rel_err=8.07e-06 (tol=5.0e-04) | State-function (T,V) ideal-gas entropy change across coupled subsystems |
| `check_sec06_09` | `ex08_3` | `sec08` | PASS | expected=66.7839, computed=66.7838, rel_err=8.74e-07 (tol=5.0e-04) | Exact combinatorics math.comb(9,6) and math.comb(100,50) Boltzmann multiplicity |
| `check_sec06_09` | `ex08_4` | `sec08` | PASS | expected=2.0813, computed=2.08124, rel_err=2.98e-05 (tol=5.0e-04) | Kirchhoff enthalpy cycle at 310.15 K and u_g = h_g - P_sat*v_g |
| `check_sec06_09` | `ex08_5` | `sec08` | PASS | expected=3.1002, computed=3.10019, rel_err=4.45e-06 (tol=5.0e-04) | Two-point Van't Hoff equation cross-checked against exp(-dG_800/(R*T)) |
| `check_sec06_09` | `ex08_6` | `sec08` | PASS | expected=17.213, computed=17.2131, rel_err=5.92e-06 (tol=5.0e-04) | Gouy-Stodola theorem x_dest = T_0 * s_gen across boiler and irreversible turbine |
| `check_sec06_09` | `ex08_7` | `sec08` | PASS | expected=18.713, computed=18.7131, rel_err=6.35e-06 (tol=5.0e-04) | Bernal-Fowler ice rules multiplicity Omega = (3/2)^N -> S_0 = n*R*ln(3/2) |
| `check_sec06_09` | `ex08_8` | `sec08` | PASS | expected=1.2289, computed=1.22889, rel_err=6.95e-06 (tol=5.0e-04) | Nernst/Gibbs electrochemistry identity E_cell = -dG/(n_e*F) |
| `check_sec06_09` | `ex08_9` | `sec08` | PASS | expected=63.68, computed=63.68, rel_err=2.23e-16 (tol=5.0e-04) | Boundary entropy balance T_0*Q_dot*(1/T_C - 1/T_H) vs Carnot lost power Q_dot*(1 - T_0/T_H) |
| `check_sec06_09` | `ex09_1` | `sec09` | PASS | expected=14.341, computed=14.3408, rel_err=1.09e-05 (tol=5.0e-04) | Second-Law efficiency scaling of Carnot COP_HP and First-Law Q_H = Q_C + W_in |
| `check_sec06_09` | `ex09_2` | `sec09` | PASS | expected=3457.8, computed=3457.89, rel_err=2.54e-05 (tol=5.0e-04) | Sum of 4 Carnot leg works (isothermal + adiabatic cancellation) |
| `check_sec06_09` | `ex09_3` | `sec09` | PASS | expected=616.35, computed=616.367, rel_err=2.74e-05 (tol=5.0e-04) | MEP = w_net / (v_BDC - v_TDC) from Otto cycle vertex state ledger |
| `check_sec06_09` | `ex09_4` | `sec09` | PASS | expected=444.58, computed=444.583, rel_err=6.32e-06 (tol=5.0e-04) | AM-GM geometric-mean compressor/turbine exit temperature T_2^* = sqrt(T_1*T_3) |
| `check_sec06_09` | `ex09_5` | `sec09` | PASS | expected=0.515, computed=0.514931, rel_err=1.34e-04 (tol=5.0e-04) | Isentropic steam dome quality interpolation and turbine-minus-pump shaft work balance |
| `check_sec06_09` | `ex09_6` | `sec09` | PASS | expected=210.8, computed=210.8, rel_err=1.35e-16 (tol=5.0e-04) | Cascaded series efficiency 1 - (1 - eta_1)*(1 - eta_2) |
| `check_sec06_09` | `ex09_7` | `sec09` | PASS | expected=0.6251, computed=0.625055, rel_err=7.14e-05 (tol=5.0e-04) | Dual-cycle 5-vertex First-Law derivation and positive-heat leg summation |
| `check_sec06_09` | `ex09_8` | `sec09` | PASS | expected=16.7185, computed=16.7185, rel_err=4.56e-07 (tol=5.0e-04) | Equating simple and regenerative Brayton efficiencies at T_2 = T_4 = sqrt(T_1*T_3) |
| `check_sec06_09` | `ex09_9` | `sec09` | PASS | expected=7.75, computed=7.75, rel_err=0.00e+00 (tol=5.0e-04) | Zero-entropy-generation reversible engine + heat pump energy & entropy balance |
| `check_sec10_13` | `EX-10.1-Q` | `sec10` | PASS | expected=1.34283, computed=1.34283, rel_err=0.00e+00 (tol=1.0e-06) | 5x5 linear nodal matrix solve vs series sum R_tot=18.6174 K/W (Q=1.3428 W) |
| `check_sec10_13` | `EX-10.1-T12` | `sec10` | PASS | expected=39.8454, computed=39.8454, rel_err=0.00e+00 (tol=1.0e-06) | Nodal matrix solve T_12 = T_in - Q*(R_in + R1) = 39.85 C |
| `check_sec10_13` | `EX-10.2-R-STEEL` | `sec10` | PASS | expected=3.834, computed=3.83404, rel_err=9.62e-06 (tol=1.0e-03) | Parallel conductance G_tot = G_ins + G_bolts (69.3% heat leak through 0.168% area!) |
| `check_sec10_13` | `EX-10.2-FRAC` | `sec10` | PASS | expected=0.6933, computed=0.693791, rel_err=7.08e-04 (tol=1.0e-03) | G_bolts / (G_ins + G_bolts) |
| `check_sec10_13` | `EX-10.3-Q` | `sec10` | PASS | expected=333.333, computed=333.333, rel_err=1.00e-06 (tol=1.0e-03) | Series sum 2*(L/(kA)) + 1/(h_c A) = 0.120 K/W |
| `check_sec10_13` | `EX-10.3-DT-INT` | `sec10` | PASS | expected=6.6667, computed=6.66667, rel_err=5.00e-06 (tol=1.0e-03) | DeltaT_c = Q / (h_c A) |
| `check_sec10_13` | `EX-10.4-RCRIT` | `sec10` | PASS | expected=2.32321, computed=2.32321, rel_err=1.52e-06 (tol=1.0e-04) | Brent root-finding on R_tot(r_o) = R_tot(r_i) (Lienhard p. 70 gives 2.32) |
| `check_sec10_13` | `EX-10.5-SPH` | `sec10` | PASS | expected=7.2382, computed=7.23823, rel_err=4.07e-06 (tol=1.0e-03) | Q = k * sqrt(A_i A_o) * DeltaT / (r_o - r_i) |
| `check_sec10_13` | `EX-10.6-WF-CU` | `sec10` | PASS | expected=426.29, computed=426.29, rel_err=5.98e-07 (tol=1.0e-03) | Sommerfeld Lorenz number L_0 = (pi^2/3)*(k_B/e)^2 = 2.443e-8 W*Ohm/K^2 |
| `check_sec10_13` | `EX-10.6-WF-6061` | `sec10` | PASS | expected=179.49, computed=179.49, rel_err=2.33e-06 (tol=1.0e-03) | k_e = L_0 * T / rho_e |
| `check_sec10_13` | `EX-10.7-GHP` | `sec10` | PASS | expected=0.04, computed=0.04, rel_err=1.73e-16 (tol=1.0e-04) | k = (P_elec / 2) * L / (A * DeltaT) accounting for bidirectional 2-slab split |
| `check_sec10_13` | `EX-11.1-RAL` | `sec11` | PASS | expected=3.395e+07, computed=3.39666e+07, rel_err=4.90e-04 (tol=2.0e-03) | Ra_L = g * beta * DeltaT * L^3 / (nu * alpha) |
| `check_sec10_13` | `EX-11.1-Q` | `sec11` | PASS | expected=4.439, computed=4.44584, rel_err=1.54e-03 (tol=2.0e-03) | Churchill & Chu (1975) laminar correlation Nu_L = 40.53 -> h = 3.58 W/m2K |
| `check_sec10_13` | `EX-11.2-DELTAC` | `sec11` | PASS | expected=10.935, computed=10.9364, rel_err=1.30e-04 (tol=2.0e-03) | Ra_c = 1708 threshold inversion |
| `check_sec10_13` | `EX-11.2-KEFF` | `sec11` | PASS | expected=0.02781, computed=0.0278133, rel_err=1.20e-04 (tol=2.0e-03) | k_eff = k_air + h_rad_foil * delta |
| `check_sec10_13` | `EX-11.3-QEVAP` | `sec11` | PASS | expected=2.215, computed=2.21496, rel_err=1.64e-05 (tol=1.0e-04) | Dalton partial density mass fraction + Sherwood mass transfer Q_evap = L_v * m_dot |
| `check_sec10_13` | `EX-11.4-STRAT` | `sec11` | PASS | expected=17.102, computed=17.1022, rel_err=1.10e-05 (tol=2.0e-03) | 2-layer energy conservation check (C_top*dT_top + C_bot*dT_bot = 5400 J) |
| `check_sec10_13` | `EX-11.4-ECONS` | `sec11` | PASS | expected=5400, computed=5400, rel_err=0.00e+00 (tol=1.0e-06) | First-Law energy balance |
| `check_sec10_13` | `EX-11.5-MIXED` | `sec11` | PASS | expected=2.173, computed=2.1742, rel_err=5.54e-04 (tol=2.0e-03) | Gr_L / Re_L^2 at u_inf = 0.25 m/s |
| `check_sec10_13` | `EX-12.1-WIEN` | `sec12` | PASS | expected=1.2074, computed=1.2074, rel_err=4.13e-06 (tol=1.0e-04) | b_Wien / T_fil |
| `check_sec10_13` | `EX-12.1-RADIANCE` | `sec12` | PASS | expected=209480, computed=209592, rel_err=5.35e-04 (tol=1.0e-03) | L = eps * sigma * T^4 / pi (Cornell 2027 E1 & Lienhard Eq. 10.7b) |
| `check_sec10_13` | `EX-12.2-F-AP40` | `sec12` | PASS | expected=0.6647, computed=0.664654, rel_err=6.92e-05 (tol=1.0e-03) | Lienhard Table 10.3 Case 3 exact analytical formula |
| `check_sec10_13` | `EX-12.2-GAIN` | `sec12` | PASS | expected=45.13, computed=45.0802, rel_err=1.10e-03 (tol=2.0e-03) | Ratio of coaxial view factors at h=40 cm |
| `check_sec10_13` | `EX-12.3-Q-CARD` | `sec12` | PASS | expected=128.43, computed=128.323, rel_err=8.37e-04 (tol=1.0e-03) | Lienhard Eq. (10.24) q = sigma*(T1^4 - T2^4)/(2/eps - 1) |
| `check_sec10_13` | `EX-12.3-Q-SHIELD` | `sec12` | PASS | expected=1.0256, computed=1.02476, rel_err=8.21e-04 (tol=1.0e-03) | Lienhard Eq. (10.31) N-shield network (125.2x reduction) |
| `check_sec10_13` | `EX-12.4-BLACK` | `sec12` | PASS | expected=64.9656, computed=64.9656, rel_err=5.73e-07 (tol=1.0e-04) | Root of coupled convection + Stefan-Boltzmann balance (~65 C in Lienhard Ex 10.12) |
| `check_sec10_13` | `EX-12.4-SELECTIVE` | `sec12` | PASS | expected=98.6446, computed=98.6446, rel_err=2.03e-07 (tol=1.0e-04) | Root of coupled convection + Stefan-Boltzmann balance |
| `check_sec10_13` | `EX-12.5-TEQ` | `sec12` | PASS | expected=254.58, computed=254.578, rel_err=7.31e-06 (tol=1.0e-03) | ((1-A)*S_0 / (4*sigma))^(1/4) |
| `check_sec10_13` | `EX-12.5-TGH` | `sec12` | PASS | expected=302.75, computed=302.746, rel_err=1.28e-05 (tol=1.0e-03) | 2-node radiative balance T_s = 2^(1/4) * T_eq |
| `check_sec10_13` | `EX-13.1-TAU` | `sec13` | PASS | expected=52.93, computed=52.9398, rel_err=1.86e-04 (tol=2.0e-03) | tau = rho * c_p * V / (h_eff * A) |
| `check_sec10_13` | `EX-13.1-T95` | `sec13` | PASS | expected=158.57, computed=158.594, rel_err=1.49e-04 (tol=2.0e-03) | Exact exponential inversion -tau * ln(0.05) |
| `check_sec10_13` | `EX-13.2-T10M` | `sec13` | PASS | expected=49.6857, computed=49.6857, rel_err=5.80e-12 (tol=1.0e-05) | RK45 ODE integration vs exact exponential T_ss - (T_ss - T_i)exp(-t/tau) = 49.69 C |
| `check_sec10_13` | `EX-13.2-T15M` | `sec13` | PASS | expected=57.981, computed=57.981, rel_err=9.39e-12 (tol=1.0e-05) | RK45 ODE integration vs exact exponential = 57.98 C |
| `check_sec10_13` | `EX-13.3-TSS` | `sec13` | PASS | expected=68, computed=68, rel_err=0.00e+00 (tol=1.0e-05) | T_ss = (T1^2 - T0*T2)/(2*T1 - T0 - T2) verified by forward substitution |
| `check_sec10_13` | `EX-13.3-TAU` | `sec13` | PASS | expected=1042.82, computed=1042.82, rel_err=2.06e-06 (tol=1.0e-04) | tau = Delta_t / ln((T1 - T0)/(T2 - T1)) |
| `check_sec10_13` | `EX-13.3-FWD` | `sec13` | PASS | expected=41, computed=41, rel_err=1.73e-16 (tol=1.0e-06) | Exact analytical inversion check |
| `check_sec10_13` | `EX-13.4-STEP2TAU` | `sec13` | PASS | expected=43.617, computed=43.6166, rel_err=8.76e-06 (tol=1.0e-04) | T_w - (T_w - T_p0)*exp(-2) |
| `check_sec10_13` | `EX-13.4-STEP5TAU` | `sec13` | PASS | expected=46.832, computed=46.8316, rel_err=9.58e-06 (tol=1.0e-04) | T_w - (T_w - T_p0)*exp(-5) |
| `check_sec10_13` | `EX-13.5-PENETRATION` | `sec13` | PASS | expected=18.847, computed=18.8468, rel_err=1.32e-05 (tol=1.0e-03) | delta_t = 2 * sqrt(alpha_w * t) |
| `check_sec10_13` | `EX-13.5-EFFUSIVITY-AL` | `sec13` | PASS | expected=20.612, computed=20.6112, rel_err=3.83e-05 (tol=1.0e-03) | Lienhard Eq. (5.51) effusivity-weighted average (b_1 T_1 + b_2 T_2)/(b_1 + b_2) |
| `check_sec10_13` | `EX-13.5-EFFUSIVITY-BALSA` | `sec13` | PASS | expected=32.947, computed=32.9472, rel_err=7.28e-06 (tol=1.0e-03) | Lienhard Eq. (5.51) effusivity-weighted average |
| `check_sec10_13` | `EX-13.6-TVAC` | `sec13` | PASS | expected=2013.93, computed=2013.93, rel_err=1.40e-06 (tol=1.0e-04) | Closed-form power-law integral vs RK45 integration (T_final = 300.000 K) |
| `check_sec10_13` | `EX-13.6-RKCHK` | `sec13` | PASS | expected=300, computed=300, rel_err=2.07e-11 (tol=1.0e-05) | Independent scipy.integrate.solve_ivp RK45 check |
| `check_sec10_13` | `EX-10.8-3DBOX` | `sec10` | PASS | expected=12.5868, computed=12.5868, rel_err=3.81e-06 (tol=1.0e-04) | Langmuir/Lienhard 3D box shape factor S = A_in/L + 0.54*sum(L_edge) + 0.15*8*L |
| `check_sec10_13` | `EX-10.9-FIN-ETA` | `sec10` | PASS | expected=0.9547, computed=0.954654, rel_err=4.86e-05 (tol=2.0e-04) | Analytical hyperbolic tangent fin solution |
| `check_sec10_13` | `EX-10.9-FIN-EPS` | `sec10` | PASS | expected=29.595, computed=29.5943, rel_err=2.50e-05 (tol=2.0e-04) | Ratio of fin heat transfer to bare base footprint |
| `check_sec10_13` | `EX-10.10-CUTBAR` | `sec10` | PASS | expected=167, computed=167, rel_err=2.08e-07 (tol=1.0e-04) | Series heat-flux continuity q''_ref = q''_x |
| `check_sec10_13` | `EX-11.6-LMTD` | `sec11` | PASS | expected=3580.87, computed=3580.87, rel_err=2.54e-16 (tol=1.0e-06) | Exact identity m_dot*cp*(T_out - T_in) = h*A_s*DeltaT_lm (3581.0 W) |
| `check_sec10_13` | `EX-11.7-H-UP` | `sec11` | PASS | expected=5.90672, computed=5.90672, rel_err=4.16e-07 (tol=1.0e-04) | Raithby & Hollands L* = D/4 correlation |
| `check_sec10_13` | `EX-11.7-H-DOWN` | `sec11` | PASS | expected=3.50714, computed=3.50714, rel_err=4.47e-07 (tol=1.0e-04) | Kadambi & Drake stable Ra_D^(1/5) correlation |
| `check_sec10_13` | `EX-12.6-CAV` | `sec12` | PASS | expected=0.9375, computed=0.9375, rel_err=0.00e+00 (tol=1.0e-05) | Hohlraum multiple-reflection series sum alpha_s / (alpha_s + (1-alpha_s)*A_ap/A_cav) |
| `check_sec10_13` | `EX-12.6-HOTTEL` | `sec12` | PASS | expected=0.414214, computed=0.414214, rel_err=2.68e-16 (tol=1.0e-06) | Lienhard Table 10.2 Case 1 & Case 4 exact agreement |
| `check_sec10_13` | `EX-12.7-HRAD` | `sec12` | PASS | expected=7.1246, computed=7.1246, rel_err=2.43e-07 (tol=1.0e-04) | Lienhard Eq. (2.31) h_rad = 4*eps*sigma*T_m^3 |
| `check_sec10_13` | `EX-12.7-EXACT` | `sec12` | PASS | expected=0.0355795, computed=0.035464, rel_err=3.25e-03 (tol=4.0e-03) | Taylor remainder (1/4)*(DeltaT/T_m)^2 = 0.00325 |
| `check_sec10_13` | `EX-13.7-COOL6S` | `sec13` | PASS | expected=0.1054, computed=0.105387, rel_err=1.24e-04 (tol=1.0e-03) | Exponential cooling decay during Rule 5.II.g removal |
| `check_sec10_13` | `EX-13.7-COOL50S` | `sec13` | PASS | expected=0.8653, computed=0.865283, rel_err=1.93e-05 (tol=1.0e-03) | Exponential cooling decay during Rule 5.II.g removal |
| `check_sec10_13` | `EX-13.8-2NODE-TOP` | `sec13` | PASS | expected=53.7346, computed=53.7346, rel_err=4.12e-07 (tol=1.0e-04) | Coupled 2-node RK45 integration (Clarifications #1-#4 top-layer gain +31.73 C) |
| `check_sec10_13` | `EX-13.8-2NODE-BOT` | `sec13` | PASS | expected=33.8248, computed=33.8248, rel_err=1.45e-06 (tol=1.0e-04) | Coupled 2-node RK45 integration (DeltaT_strat = 19.91 C) |
| `check_sec10_13` | `EX-13.9-REGNAULT` | `sec13` | PASS | expected=9.154, computed=9.154, rel_err=1.94e-16 (tol=1.0e-04) | Dickinson equal-area drift integral correction (+0.304 C recovered) |
| `check_sec14_16` | `SEC14:EQ14.1_WIEN_LAMP` | `§14.1` | PASS | expected=1.2074, computed=1.2074, rel_err=4.13e-06 (tol=1.0e-03) | Wien displacement law b / T_fil |
| `check_sec14_16` | `SEC14:EQ14.1_WIEN_WATER` | `§14.1` | PASS | expected=9.4038, computed=9.40377, rel_err=3.11e-06 (tol=1.0e-03) | Wien displacement law b / T_water |
| `check_sec14_16` | `SEC14:EX14.1_BLACK_CR` | `§14.1` | PASS | expected=16.997, computed=16.9974, rel_err=2.10e-05 (tol=1.0e-03) | Two-band Stefan-Boltzmann balance A_c*(alpha_NIR*q_NIR - eps_MIR*sigma*(T_s^4-T_e^4)) |
| `check_sec14_16` | `SEC14:EX14.1_MATTE_BLACK` | `§14.1` | PASS | expected=15.905, computed=15.905, rel_err=1.94e-06 (tol=1.0e-03) | Two-band Stefan-Boltzmann balance |
| `check_sec14_16` | `SEC14:EX14.1_WHITE_PAINT` | `§14.1` | PASS | expected=3.6535, computed=3.65356, rel_err=1.76e-05 (tol=1.0e-03) | Two-band Stefan-Boltzmann balance |
| `check_sec14_16` | `SEC14:EX14.2_SHINY_FOIL` | `§14.2` | PASS | expected=36.91, computed=36.908, rel_err=5.36e-05 (tol=1.0e-03) | Specular + forward diffuse ray-bounce polynomial sum |
| `check_sec14_16` | `SEC14:EX14.2_SHINY_MASS` | `§14.2` | PASS | expected=4.7037, computed=4.70368, rel_err=3.57e-06 (tol=2.0e-03) | Volumetric heat capacity rho * c_p * delta * A_w |
| `check_sec14_16` | `SEC14:EX14.2_DULL_FOIL` | `§14.2` | PASS | expected=28.031, computed=28.0313, rel_err=9.48e-06 (tol=1.0e-03) | Specular + forward diffuse ray-bounce polynomial sum |
| `check_sec14_16` | `SEC14:EX14.2_WHITE_CARD` | `§14.2` | PASS | expected=8.9746, computed=8.97451, rel_err=1.03e-05 (tol=1.0e-03) | Specular + forward diffuse ray-bounce polynomial sum |
| `check_sec14_16` | `SEC14:EX14.3_970NM_TOP1CM` | `§14.3` | PASS | expected=0.35528, computed=0.355291, rel_err=3.14e-05 (tol=1.0e-03) | Beer-Lambert attenuation (1 - R_F)*(1 - exp(-mu_a * z)) |
| `check_sec14_16` | `SEC14:EX14.3_970NM_2PASS` | `§14.3` | PASS | expected=0.93148, computed=0.931421, rel_err=6.36e-05 (tol=1.0e-03) | Two-pass Beer-Lambert integral with bottom mirror return |
| `check_sec14_16` | `SEC14:EX14.3_1200NM_TOP1CM` | `§14.3` | PASS | expected=0.63398, computed=0.633912, rel_err=1.07e-04 (tol=1.0e-03) | Beer-Lambert attenuation (1 - R_F)*(1 - exp(-mu_a * z)) |
| `check_sec14_16` | `SEC14:EX14.3_1200NM_2PASS` | `§14.3` | PASS | expected=0.97788, computed=0.97794, rel_err=6.12e-05 (tol=1.0e-03) | Two-pass Beer-Lambert integral with bottom mirror return |
| `check_sec14_16` | `SEC14:EX14.3_1440NM_TOP1CM` | `§14.3` | PASS | expected=0.98045, computed=0.98046, rel_err=1.04e-05 (tol=1.0e-03) | Beer-Lambert attenuation (1 - R_F)*(1 - exp(-mu_a * z)) |
| `check_sec14_16` | `SEC14:EX14.3_1440NM_2PASS` | `§14.3` | PASS | expected=0.98045, computed=0.98046, rel_err=1.04e-05 (tol=1.0e-03) | Two-pass Beer-Lambert integral with bottom mirror return |
| `check_sec14_16` | `SEC14:EX14.4_BOPET_TAU` | `§14.4` | PASS | expected=0.8714, computed=0.871264, rel_err=1.56e-04 (tol=1.0e-03) | Airy multiple-reflection slab transmittance formula |
| `check_sec14_16` | `SEC14:EX14.4_BOPET_CDISK` | `§14.4` | PASS | expected=0.24395, computed=0.243945, rel_err=2.05e-05 (tol=1.0e-03) | Calorimetric capacitance rho * c_p * A * delta |
| `check_sec14_16` | `SEC14:EX14.4_GLASS_TAU` | `§14.4` | PASS | expected=0.9153, computed=0.915314, rel_err=1.48e-05 (tol=1.0e-03) | Airy multiple-reflection slab transmittance formula |
| `check_sec14_16` | `SEC14:EX14.4_GLASS_DRAIN` | `§14.4` | PASS | expected=1.6719, computed=1.67187, rel_err=1.79e-05 (tol=1.0e-03) | Headspace calorimetric perturbation C_disk * dT_g / C_top |
| `check_sec14_16` | `SEC14:EX14.5_RA_DELTA` | `§14.5` | PASS | expected=602.7, computed=602.756, rel_err=9.30e-05 (tol=2.0e-03) | Rayleigh-Benard stability parameter g*beta*dT*delta^3/(nu*alpha) |
| `check_sec14_16` | `SEC14:EX14.5_Q_FOIL_AIR` | `§14.5` | PASS | expected=0.8776, computed=0.877623, rel_err=2.63e-05 (tol=2.0e-03) | Parallel conduction + radiation across 3 series air-foil gaps |
| `check_sec14_16` | `SEC14:EX14.5_Q_CORK` | `§14.5` | PASS | expected=1.26, computed=1.26, rel_err=0.00e+00 (tol=1.0e-03) | Fourier conduction k_cork * A_m * dT / L_tot |
| `check_sec14_16` | `SEC15:EX15.1_F_AP_40CM` | `§15.2` | PASS | expected=0.66471, computed=0.664654, rel_err=8.42e-05 (tol=1.0e-03) | Lienhard Table 10.3 Case 3 coaxial parallel disks formula |
| `check_sec14_16` | `SEC15:EX15.1_RATIO_40CM` | `§15.2` | PASS | expected=45.08, computed=45.0802, rel_err=5.02e-06 (tol=1.0e-03) | View-factor ratio F_{bulb->ap} / F_{bulb->cup} |
| `check_sec14_16` | `SEC15:EX15.1_F_AP_65CM` | `§15.2` | PASS | expected=0.15162, computed=0.151596, rel_err=1.59e-04 (tol=1.0e-03) | Lienhard Table 10.3 Case 3 coaxial parallel disks formula |
| `check_sec14_16` | `SEC15:EX15.1B_F_WALL` | `§15.2` | PASS | expected=0.96656, computed=0.96666, rel_err=1.04e-04 (tol=1.0e-03) | Enclosure summation rule F_{1->s} = 1 - F_{1->2} |
| `check_sec14_16` | `SEC15:EX15.1B_Q_GROSS` | `§15.2` | PASS | expected=30.353, computed=30.3521, rel_err=3.03e-05 (tol=1.0e-03) | Direct collimated beam + specular frustum wall delivery |
| `check_sec14_16` | `SEC15:EX15.2_ELLIPSOID_A` | `§15.3` | PASS | expected=22.7289, computed=22.7289, rel_err=1.06e-06 (tol=1.0e-03) | Fermat equal-path focal distance sum 2a = d1 + d2 |
| `check_sec14_16` | `SEC15:EX15.2_ELLIPSOID_R185` | `§15.3` | PASS | expected=13.318, computed=13.318, rel_err=2.25e-06 (tol=1.0e-03) | Canonical prolate ellipsoid equation r(z) = b*sqrt(1 - (z-z_c)^2/a^2) |
| `check_sec14_16` | `SEC15:EX15.2_UNROLLED_ROUT` | `§15.3` | PASS | expected=104.58, computed=104.582, rel_err=1.44e-05 (tol=1.0e-03) | Pythagorean slant height and similar-triangles cone development |
| `check_sec14_16` | `SEC15:EX15.3_R_TOP_GLAZED` | `§15.4` | PASS | expected=11.65, computed=11.6498, rel_err=1.38e-05 (tol=1.0e-03) | Series-parallel thermal resistance network reduction |
| `check_sec14_16` | `SEC15:EX15.3_R_ENC_GLAZED` | `§15.4` | PASS | expected=5.066, computed=5.06584, rel_err=3.15e-05 (tol=1.0e-03) | Parallel combination of top, radial, and base resistance branches |
| `check_sec14_16` | `SEC15:EX15.3_R_ENC_OPEN` | `§15.4` | PASS | expected=2.414, computed=2.41366, rel_err=1.40e-04 (tol=1.0e-03) | Parallel combination with open-cup evaporative conductance |
| `check_sec14_16` | `SEC15:EX15.3B_HEAVY_AL_TG` | `§15.4` | PASS | expected=17.213, computed=17.213, rel_err=8.18e-07 (tol=1.0e-03) | Calorimetric thermal-mass partitioning TG_0 * C_sys0 / (C_sys0 + C_Al) |
| `check_sec14_16` | `SEC15:EX15.4_T_MIXED` | `§15.5` | PASS | expected=39.8, computed=39.8022, rel_err=5.62e-05 (tol=1.0e-03) | Two-node energy conservation (C_top*T_top + C_bot*T_bot)/(C_top + C_bot) |
| `check_sec14_16` | `SEC15:EX15.4_KAPPA_STRAT` | `§15.5` | PASS | expected=1.5562, computed=1.55598, rel_err=1.39e-04 (tol=1.0e-03) | Ratio of stratified top-layer gain to bulk mixed gain |
| `check_sec14_16` | `SEC15:EX15.4_SWIRL_PTS_LOST` | `§15.5` | PASS | expected=15.69, computed=15.6931, rel_err=1.96e-04 (tol=2.0e-03) | Official v2.0.0 Scoresheet TS + PS loss calculation |
| `check_sec14_16` | `SEC15:EX15.5_Q_EVAP_OPEN` | `§15.5` | PASS | expected=1335.4, computed=1335.39, rel_err=7.45e-06 (tol=1.0e-03) | Lienhard §11.7 convective mass-transfer latent heat loss L_v * m_dot * t |
| `check_sec14_16` | `SEC15:EX15.5_Q_SAT_HEADSPACE` | `§15.5` | PASS | expected=15.138, computed=15.1376, rel_err=2.48e-05 (tol=1.0e-03) | Ideal-gas saturated vapor mass capacity in trapped cup headspace |
| `check_sec14_16` | `SEC15:EX15.6_Q_BASE_FINS` | `§15.6` | PASS | expected=0.07986, computed=0.0798543, rel_err=7.11e-05 (tol=2.0e-03) | Parallel conductive network across 3 knife-edge fins and foil-air cavity |
| `check_sec14_16` | `SEC15:EX15.6B_FRUSTUM_ZW` | `§15.6` | PASS | expected=3.8732, computed=3.87575, rel_err=6.57e-04 (tol=1.0e-03) | Exact cubic frustum inversion V(z) = (pi*z/3)*(r_b^2 + r_b*r(z) + r(z)^2) |
| `check_sec14_16` | `SEC15:EX15.6B_DRY_CLEARANCE` | `§15.6` | PASS | expected=3.6268, computed=3.62425, rel_err=7.02e-04 (tol=1.0e-03) | Vertical dry margin H_cup - z_w - d_overhang >= 1.5 cm |
| `check_sec14_16` | `SEC16:EX16.1_FS_ALPHA` | `§16.1` | PASS | expected=98.017, computed=98.0169, rel_err=6.12e-07 (tol=1.0e-03) | Official 2027 Scoresheet v2.0.0 formula ES + TS + PS |
| `check_sec14_16` | `SEC16:EX16.1_FS_BETA` | `§16.1` | PASS | expected=76.711, computed=76.7107, rel_err=3.46e-06 (tol=1.0e-03) | Official 2027 Scoresheet v2.0.0 formula ES + TS + PS |
| `check_sec14_16` | `SEC16:EX16.1_FS_BETA_PEN` | `§16.1` | PASS | expected=68.133, computed=68.1269, rel_err=9.01e-05 (tol=1.0e-03) | Rule 6.g penalty multiplier M_pen = 0.7^(V_constr) applied to TS and PS |
| `check_sec14_16` | `SEC16:EX16.2_M13` | `§16.2` | PASS | expected=1.1916, computed=1.19156, rel_err=3.13e-05 (tol=1.0e-03) | Lumped exponential growth ratio (1 - exp(-780/903))/(1 - exp(-600/903)) |
| `check_sec14_16` | `SEC16:EX16.2_TPRED` | `§16.2` | PASS | expected=54.47, computed=54.4687, rel_err=2.45e-05 (tol=1.0e-03) | Linear superposition T_start + TG_table + k_room*(T_room - T_start) - dT_cool |
| `check_sec14_16` | `SEC16:EX16.2B_TAU_3PT` | `§16.2` | PASS | expected=903.21, computed=903.199, rel_err=1.18e-05 (tol=1.0e-03) | Equal-interval 3-point ratio dt / ln(TG1 / (TG2 - TG1)) |
| `check_sec14_16` | `SEC16:EX16.2B_DTSS_3PT` | `§16.2` | PASS | expected=57.214, computed=57.2142, rel_err=3.52e-06 (tol=1.0e-03) | Equal-interval 3-point ratio TG1^2 / (2*TG1 - TG2) |
| `check_sec14_16` | `SEC16:EX16.3_NATL_INTERP` | `§16.3` | PASS | expected=40.204, computed=40.2078, rel_err=9.50e-05 (tol=1.0e-03) | Piecewise-linear height interpolation + 14-min exponential time scaling |
| `check_sec14_16` | `SEC16:EX16.4_COOL_OPEN` | `§16.4` | PASS | expected=48.988, computed=48.988, rel_err=0.00e+00 (tol=1.0e-03) | Open-cup post-lamp cooling decay T_top(600) - (delta_ext + r_open*t_open) |
| `check_sec14_16` | `SEC16:EX16.4_COOL_DELAYED` | `§16.4` | PASS | expected=49.373, computed=49.373, rel_err=1.44e-16 (tol=1.0e-03) | Two-stage closed-hood + open-cup cooling decay integral |
| `check_sec14_16` | `SEC16:EX16.5_S_REP` | `§16.5` | PASS | expected=0.14142, computed=0.141421, rel_err=9.59e-06 (tol=1.0e-03) | JCGM GUM Type A sample standard deviation with nu = n - 1 = 5 |
| `check_sec14_16` | `SEC16:EX16.5_EXP_PE` | `§16.5` | PASS | expected=0.99755, computed=0.997548, rel_err=2.30e-06 (tol=1.0e-04) | Half-normal expectation E[\|err\|] = sqrt(2/pi)*s_rep*sqrt(1+1/n) |
| `check_sec14_16` | `SEC16:EX16.6_PAR38_TPRED` | `§16.5` | PASS | expected=36.234, computed=36.234, rel_err=0.00e+00 (tol=1.0e-03) | Beam-shape mismatch scaling factor kappa_beam * TG_table |
| `check_sec14_16` | `SEC16:EX16.6_PS_SAVED` | `§16.5` | PASS | expected=1.0497, computed=1.04972, rel_err=2.26e-05 (tol=2.0e-03) | Rule 6.f Prediction Score difference 20 * (PE_adj - PE_unadj) |
| `check_sec14_16` | `SEC16:EX16.7_POWERLAW_N` | `§16.5` | PASS | expected=1.6589, computed=1.65893, rel_err=1.99e-05 (tol=1.0e-03) | Two-point log-log slope ln(TG1/TG2) / ln(d2/d1) |
| `check_sec14_16` | `SEC16:EX16.7_POWERLAW_SLOTB` | `§16.5` | PASS | expected=17.52, computed=17.5284, rel_err=4.77e-04 (tol=1.0e-03) | Inverse effective-distance power law TG1 * (d1 / d_SlotB)^n |
| `check_sec17_20` | `sec17:ex17.1:capillary_sensitivity` | `sec17` | PASS | expected=2.20847, computed=2.20847, rel_err=1.00e-07 <= tol=1.0e-04 | Volumetric expansion (beta_liq - 3*alpha_glass)*V_bulb/(pi*r^2) |
| `check_sec17_20` | `sec17:ex17.1:stem_emergence` | `sec17` | PASS | expected=66.9656, computed=66.9656, rel_err=0.00e+00 <= tol=1.0e-04 | Stem correction T_true = T_read + k_g * N * (T_read - T_stem) |
| `check_sec17_20` | `sec17:ex17.2:ntc_temp_C` | `sec17` | PASS | expected=42.1723, computed=42.1723, rel_err=3.99e-08 <= tol=1.0e-04 | Direct inversion of R(T) = R0*exp(beta*(1/T - 1/T0)) |
| `check_sec17_20` | `sec17:ex17.2:ntc_alpha_R` | `sec17` | PASS | expected=-0.0391439, computed=-0.0391439, rel_err=1.22e-06 <= tol=1.0e-04 | Analytical derivative (1/R)(dR/dT) = -beta/T^2 |
| `check_sec17_20` | `sec17:ex17.2:ntc_self_heating` | `sec17` | PASS | expected=0.0370085, computed=0.0370085, rel_err=9.02e-07 <= tol=1.0e-03 | Voltage divider Joule power P = (V_ref/(R_s+R))^2 * R / delta_diss |
| `check_sec17_20` | `sec17:ex17.3:pt100_true_temp` | `sec17` | PASS | expected=43.1842, computed=43.1842, rel_err=2.45e-07 <= tol=1.0e-04 | Quadratic root of R0*(1 + A*t + B*t^2) = 116.77 Ohm |
| `check_sec17_20` | `sec17:ex17.3:pt100_lead_error` | `sec17` | PASS | expected=1.81471, computed=1.81471, rel_err=2.22e-06 <= tol=1.0e-03 | Difference between 117.47 Ohm and 116.77 Ohm CVD solutions |
| `check_sec17_20` | `sec17:ex17.3:ir_water_read` | `sec17` | PASS | expected=44.2084, computed=44.2084, rel_err=5.05e-07 <= tol=1.0e-04 | Background-compensated radiometric balance (T_amb^4 + (eps/eps_set)*(T_obj^4 - T_amb^4))^(1/4) |
| `check_sec17_20` | `sec17:ex17.3:ir_foil_read` | `sec17` | PASS | expected=23.0297, computed=23.0297, rel_err=1.13e-06 <= tol=1.0e-04 | Background-compensated radiometric balance showing -20.97 C error on low-eps metal |
| `check_sec17_20` | `sec17:ex17.4:probe_eq_temp` | `sec17` | PASS | expected=46.4393, computed=46.4393, rel_err=7.00e-08 <= tol=1.0e-04 | Calorimetric energy balance (C_top*T_w0 + C_p*T_p0)/(C_top + C_p) |
| `check_sec17_20` | `sec17:ex17.4:probe_2tau_vs_5tau` | `sec17` | PASS | expected=46.2713, computed=46.2713, rel_err=6.87e-08 <= tol=1.0e-04 | First-order step response T_eq - (T_eq - T_p0)*exp(-5) |
| `check_sec17_20` | `sec17:ex17.4:two_point_calibration` | `sec17` | PASS | expected=44.5583, computed=44.5583, rel_err=3.48e-07 <= tol=1.0e-04 | ITS-90 steam point at 742 mmHg (99.330 C) + 2-point linear interpolation |
| `check_sec17_20` | `sec17:ex17.5:gum_rule4f_corr_TG` | `sec17` | PASS | expected=0.08165, computed=0.0816497, rel_err=4.19e-06 <= tol=1.0e-04 | JCGM GUM correlated difference with r_sys = +1 cancelling u_B,sys |
| `check_sec17_20` | `sec17:ex17.5:gum_calorimetry_uc` | `sec17` | PASS | expected=0.007723, computed=0.00772404, rel_err=1.34e-04 <= tol=1.0e-03 | Quadrature propagation of relative uncertainties in c_x = m_w*c_w*dT_w/(m_x*dT_x) |
| `check_sec17_20` | `sec17:ex17.6:type_t_cjc_temp` | `sec17` | PASS | expected=42.6415, computed=42.6415, rel_err=1.33e-08 <= tol=1.0e-04 | Law of Intermediate Temperatures E(0,T) = E(0,20) + dV + linear ITS-90 interpolation |
| `check_sec17_20` | `sec17:ex17.6:stefan_boltzmann_gum_uQ` | `sec17` | PASS | expected=0.365308, computed=0.365306, rel_err=6.82e-06 <= tol=1.0e-04 | Power-law GUM propagation Q_dot * sqrt((u_A/A)^2 + (4*u_T/T)^2) |
| `check_sec17_20` | `sec18:ex18.1:wet_steam_enthalpy` | `sec18` | PASS | expected=2077.76, computed=2077.76, rel_err=0.00e+00 <= tol=1.0e-04 | Lever rule h = h_f + ((s - s_f)/(s_g - s_f))*(h_g - h_f) |
| `check_sec17_20` | `sec18:ex18.1:bilinear_superheated_h` | `sec18` | PASS | expected=2804.85, computed=2804.85, rel_err=0.00e+00 <= tol=1.0e-05 | 2D bilinear Lagrange interpolation across (T, P) steam grid |
| `check_sec17_20` | `sec18:ex18.1:clapeyron_central_diff` | `sec18` | PASS | expected=2262.55, computed=2262.54, rel_err=6.09e-06 <= tol=1.0e-04 | Clapeyron h_fg = T * v_fg * (P(105)-P(95))/(2*5) |
| `check_sec17_20` | `sec18:ex18.2:trapezoidal_pv_work` | `sec18` | PASS | expected=1037.5, computed=1037.5, rel_err=0.00e+00 <= tol=1.0e-06 | numpy.trapz(P_kPa, V_L) over 4 equal 1.0 L subintervals |
| `check_sec17_20` | `sec18:ex18.3:semilog_tau_min` | `sec18` | PASS | expected=15.1101, computed=15.1101, rel_err=9.75e-07 <= tol=1.0e-04 | Linear least squares of ln((T_ss-T)/(T_ss-T_i)) vs t |
| `check_sec17_20` | `sec18:ex18.3:semilog_u_tau` | `sec18` | PASS | expected=0.0104962, computed=0.0104962, rel_err=2.69e-06 <= tol=1.0e-03 | s_yx / sqrt(S_tt) * tau^2 |
| `check_sec17_20` | `sec18:ex18.3:three_point_Tss` | `sec18` | PASS | expected=61.6632, computed=61.6632, rel_err=5.92e-08 <= tol=1.0e-04 | Exact algebraic relation (T1*T3 - T2^2)/(T1 + T3 - 2*T2) |
| `check_sec17_20` | `sec18:ex18.3:grubbs_statistic` | `sec18` | PASS | expected=2.03367, computed=2.03367, rel_err=3.41e-07 <= tol=1.0e-04 | max\|x_i - mean\| / s_sample with ddof=1 (exceeds G_crit=1.887) |
| `check_sec17_20` | `sec18:ex18.4:clausius_clapeyron_dHvap` | `sec18` | PASS | expected=42.4192, computed=42.4337, rel_err=3.41e-04 <= tol=1.0e-03 | NumPy polyfit slope of ln(P_sat) vs 1000/T multiplied by -R |
| `check_sec17_20` | `sec18:ex18.4:clausius_clapeyron_Tb` | `sec18` | PASS | expected=99.769, computed=99.765, rel_err=3.98e-05 <= tol=1.0e-03 | Inversion of OLS fit at P = 101.325 kPa |
| `check_sec17_20` | `sec18:ex18.5:heating_curve_Lf` | `sec18` | PASS | expected=180, computed=180, rel_err=0.00e+00 <= tol=1.0e-05 | Q_dot * dt_fus / m |
| `check_sec17_20` | `sec18:ex18.5:eutectic_lever_Sn_mass` | `sec18` | PASS | expected=162.8, computed=162.8, rel_err=1.75e-16 <= tol=1.0e-04 | w_L * ((w_0 - w_alpha)/(w_L - w_alpha)) * m_tot |
| `check_sec17_20` | `sec19:ex19.1:time_to_dry_steam` | `sec19` | PASS | expected=1599.25, computed=1599.25, rel_err=1.73e-07 <= tol=1.0e-04 | Piecewise energy balance across subcooled ice, fusion, liquid warming, and vaporization |
| `check_sec17_20` | `sec19:ex19.1:final_superheated_temp` | `sec19` | PASS | expected=267.42, computed=267.419, rel_err=2.64e-06 <= tol=1.0e-04 | Exact first-order ODE T_ss - (T_ss - 100)*exp(-t_5/(m*c_p*R_wall)) |
| `check_sec17_20` | `sec19:ex19.1:piston_boundary_work` | `sec19` | PASS | expected=62.309, computed=62.3436, rel_err=5.56e-04 <= tol=1.0e-03 | P*(V_final - V_ice) using ideal gas steam volume at 540.57 K |
| `check_sec17_20` | `sec19:ex19.2:cascade_building_heat` | `sec19` | PASS | expected=3789.29, computed=3789.28, rel_err=2.35e-06 <= tol=1.0e-04 | Coupled radiative balance * Carnot efficiency * Carnot heat-pump COP |
| `check_sec17_20` | `sec19:ex19.3:rankine_actual_work` | `sec19` | PASS | expected=832.957, computed=832.959, rel_err=1.84e-06 <= tol=1.0e-04 | eta_t * (h1 - (h_f + x_2s*h_fg)) |
| `check_sec17_20` | `sec19:ex19.3:rankine_exergy_destruction` | `sec19` | PASS | expected=137.402, computed=137.401, rel_err=8.65e-06 <= tol=1.0e-04 | T_0 * (s_2a - s_1) = (1 - eta_t)*(h_1 - h_2s)*(T_0 / T_sat) |
| `check_sec17_20` | `sec19:ex19.4:two_compartment_P_final` | `sec19` | PASS | expected=405.817, computed=405.825, rel_err=1.99e-05 <= tol=1.0e-04 | Conservation of internal energy Delta_U = (n_A*C_VA + n_B*C_VB)*Delta_T = Q |
| `check_sec17_20` | `sec19:ex19.5:dilatometer_meniscus_h1` | `sec19` | PASS | expected=117.631, computed=117.631, rel_err=3.19e-07 <= tol=1.0e-04 | h_0 + V_l0*((beta_l - 3*alpha_g)*dT - kappa_eff*dP)/A_c |
| `check_sec17_20` | `sec19:ex19.6:spring_piston_heat_Q` | `sec19` | PASS | expected=13, computed=13, rel_err=0.00e+00 <= tol=1.0e-05 | First Law Q = 2.5*(P2*V2 - P1*V1) + 0.5*(P1 + P2)*(V2 - V1) |
| `check_sec17_20` | `sec19:ex19.7:vacuum_radiative_cooling_time` | `sec19` | PASS | expected=9793.03, computed=9792.86, rel_err=1.73e-05 <= tol=1.0e-04 | Closed-form T^-4 integral C_p/(3*eps*sigma*A)*(T_f^-3 - T_i^-3) |
| `check_sec17_20` | `sec19:ex19.8:intercooled_work_saved` | `sec19` | PASS | expected=2.374, computed=2.37405, rel_err=2.03e-05 <= tol=1.0e-03 | Single-stage minus two-stage adiabatic enthalpy rise |
| `check_sec17_20` | `sec20:ex20.1:naive_impossible_Tf` | `sec20` | PASS | expected=-19.8996, computed=-19.8996, rel_err=8.84e-07 <= tol=1.0e-04 | Demonstrates false T_f < -15 C when skipping plateau inequality check |
| `check_sec17_20` | `sec20:ex20.1:true_melted_ice_mass` | `sec20` | PASS | expected=30.0765, computed=30.0765, rel_err=1.02e-08 <= tol=1.0e-04 | (m_w*c_w*T_w - m_ice*c_ice*\|T_ice\|) / L_f |
| `check_sec17_20` | `sec20:ex20.2:carnot_kelvin_efficiency` | `sec20` | PASS | expected=0.39988, computed=0.39988, rel_err=9.00e-08 <= tol=1.0e-04 | 1 - 300.15/500.15 (vs false 0.8811 in Celsius) |
| `check_sec17_20` | `sec20:ex20.2:stefan_boltzmann_kelvin` | `sec20` | PASS | expected=993.575, computed=993.575, rel_err=2.84e-07 <= tol=1.0e-04 | sigma * (400.15^4 - 300.15^4) (vs false 5.67 W/m^2 for (Delta_T)^4) |
| `check_sec17_20` | `sec20:ex20.3:device_pe_true` | `sec20` | PASS | expected=0.75, computed=0.75, rel_err=0.00e+00 <= tol=1.0e-05 | Official 2027 Rule 6.f formula with T_final in Celsius in denominator |
| `check_sec17_20` | `sec20:ex20.3:device_total_points_lost` | `sec20` | PASS | expected=16.25, computed=16.25, rel_err=0.00e+00 <= tol=1.0e-05 | 5.00 pts lost on PS + 11.25 pts lost on TS |
| `check_sec17_20` | `sec20:ex20.4:isobaric_compression_Q` | `sec20` | PASS | expected=-3518.55, computed=-3518.55, rel_err=0.00e+00 <= tol=1.0e-05 | Q = 3.5 * (P_gauge + P_atm) * (V2 - V1) |
| `check_sec17_20` | `sec20:ex20.5:bomb_calorimeter_dHc` | `sec20` | PASS | expected=-3271.32, computed=-3271.32, rel_err=1.33e-07 <= tol=1.0e-04 | dU_c + dn_gas * R * T |
| `check_sec17_20` | `sec20:ex20.5:freezing_universe_entropy` | `sec20` | PASS | expected=46.4041, computed=46.4041, rel_err=2.71e-08 <= tol=1.0e-04 | L_f * (1/T_surr - 1/T_m) > 0 |
| `check_sec17_20` | `sec20:ex20.7:wire_rcrit_heat_increase_pct` | `sec20` | PASS | expected=67.6232, computed=67.6239, rel_err=1.06e-05 <= tol=1.0e-04 | (R_bare / R_ins - 1) * 100% |
| `check_sec17_20` | `sec20:ex20.7:parasitic_sleeve_TG_loss` | `sec20` | PASS | expected=5.0888, computed=5.08919, rel_err=7.64e-05 <= tol=1.0e-04 | E_net/C_w - E_net/(C_w + C_Al) |
| `check_sec21_23` | `SEC21_MCQ_EV_BLANK_RULE` | `§21.3` | PASS | expected=1.5, computed=1.5, rel_err=0.00e+00 | Probability expectation E[X] = 3/k vs 1.0 blank credit |
| `check_sec21_23` | `SEC21_SCORING_PENALTY_EXAMPLE` | `§21.2` | PASS | expected=86.8961, computed=86.8961, rel_err=0.00e+00 | Direct evaluation of 2027 Rules 6.c-i equations |
| `check_sec21_23` | `SEC22_CORPUS_CLAUSE_SUMS` | `§22.2` | PASS | expected=1120.0, computed=1120.0, rel_err=0.00e+00 | Exact summation over 7 syllabus clauses |
| `check_sec21_23` | `SEC22_FORMAT_TIER_SUMS` | `§22.3` | PASS | expected=328, computed=328, rel_err=0.00e+00 | Matrix cross-tabulation sum check |
| `check_sec21_23` | `SEC22_CORNELL2027_HISTOGRAM` | `§22.4` | PASS | expected=55, computed=55, rel_err=0.00e+00 | Histogram bin integration and Rule 6.d scaling |
| `check_sec21_23` | `SEC23_SCALE_INTERSECTIONS` | `§23.2` | PASS | expected=574.5875, computed=574.5874999999999, rel_err=1.98e-16 | Linear Fixed-Point Algebraic Solution |
| `check_sec21_23` | `SEC23_EVAPORATION_PENALTY_DRILL` | `§23.6` | PASS | expected=6.154884, computed=6.154884, rel_err=0.00e+00 | Latent heat balance Q_evap = m_evap * L_v / C_eff |
| `check_sec21_23` | `SEC23_EXERGY_SECOND_LAW_EFF` | `§23.6` | PASS | expected=0.097395, computed=0.097395, rel_err=0.00e+00 | Exergy balance eta_2 = W_net / [Q_in*(1 - T_0/T_src)] |
