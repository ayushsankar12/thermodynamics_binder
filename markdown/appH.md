<!-- Source: src/appH.tex | Tab: Tab 9: INDEX/APP | Target: 1 pp -->
# Appendix H: Open Questions, Revision Log & Duplex Maintenance Guide {#app:H}

> **[SCOPE: VERIFY AGAINST RULES | Tournament-Specific Open Questions Register, QA Audit Summary & Selective Duplex Leaf Reprinting Protocol]**

## Tournament-Specific Open Questions Register

Because national rules allow local Event Supervisors and Tournament Directors to select specific operating points within the official ranges (`Rules 4.a, 4.c, 4.f, 5.II.a`) or announce site-dependent adjustments under General Rule 7 (`p. C1`), resolve these 5 items for each upcoming tournament:

| **#** | **Open Tournament Variable** | **2027 National Default Baseline ( **[S01,S02,S05]**)** | **How the Binder & Team Adapt Once Announced** |
| --- | --- | --- | --- |
| **Q1** | **Target Tournament Tier & Date** | National Schedule (`p. C78`): May 14–15, 2027 at Ohio State Univ.; Invitationals run Nov 2026–Feb 2027. | Enter date on §`app:F`; select Regional ($h=40–50 cm$, $t=10 min$) vs. State/National ($h=40–65 cm$, $t=10–15 min$) lookup rows in §`sec:16` / `QS-13`. |
| **Q2** | **Exact Bulb Wattage & Reflector Shape (`4.a, 5.II.a`)** | Untinted $100\text{--}125 W$ incandescent/IR heat lamp bulb (typically $100\text{ W}$ or $125\text{ W}$ clear R40/BR40). | At block start (`5.II.a`), read announced wattage $P_{\mathrm{bulb}}$ and select the $100\text{ W}$ or $125\text{ W}$ column (or linear interpolation $\mathrm{TG} \propto P_{\mathrm{bulb}}$) in §`sec:16`. |
| **Q3** | **ES Thermometer Type & Immersion Depth (`4.f, 5.II.g`)** | Digital probe, non-mercury glass, or IR reading to $0.1 °C$; `Clarif. #4` recommends **top water layer near cup center**. | If ES announces top-center probing (default), use $\kappa_{\mathrm{strat,top}}$ table in §`sec:16`; if ES announces mid-depth or IR surface reading, apply depth offset $\Delta T_{\mathrm{depth}}$. |
| **Q4** | **Device Testing Schedule Format (`p. C2` & ES Guide **[S05]**)** | Device tested concurrently during the 50-min written test block (staggered across 2–3 lamp setups per ES). | If run concurrently, follow Fig. `fig:00:timeline` choreography; if run in a separate self-scheduled device block, both partners spend all $50 min$ on Part I. |
| **Q5** | **Post-`2026-11-22` National Clarifications or Corrections** | Verified **0 corrections** and **9 clarifications** as of `2026-11-22` ( **[S02,S03]**). | Check `soinc.org/events/rules-corrections` and `soinc.org/division-c-events` 7 days and 24 hours before competition (§`app:F`). |

## Build Pipeline, QA Sign-Off & Selective Duplex Leaf Reprinting

### [FORMULA & DECISION CARD: Rebuilding & Verifying All 4 Production PDFs]

Run from `C: science olympiad Thermodynamics-Binder` using **Python 3.10.4** (`python`, which auto-prepends offline **MiKTeX 25.12** `pdflatex + makeindex`):
- **Build All 4 Targets (`output/*.pdf`):**<br>
    `python build/build.py –target all`<br>
    (*Or* `–target main|gray|quickref|device`)
- **Run Automated Mechanical & Visual QA:**<br>
    `python qa/pdfcheck.py`<br>
    `python verify/verify_all.py`
- **Mandatory Release Gates (`build/pdfcheck-report.md`):**
- **P1:** Exact US Letter ($612.0 \times 792.0\text{ pt}$) on every page.
- **P2:** Main/Gray $\le 280\text{ pp}$; QuickRef $== 12\text{ pp}$.
- **P3:** Zero unresolved cross-reference markers or leaked raw LaTeX macros.
- **P4:** Zero text spans in $0.72\text{ in}$ ($51.84\text{ pt}$) inner 3-hole punch margin.
- **P5–P6:** Footer `Page N of M` + `2026-11-22`; min font $\ge 5.0\text{ pt}$; $100\%$ embedded Type 1 fonts.
    

### [FORMULA & DECISION CARD: Selective Duplex-Safe Page-Pair Replacement]

Because the binder uses `twoside` duplex margins ($0.75\text{ in}$ inner 3-hole punch margin, $0.50\text{ in}$ outer thumb-tab margin), **every physical sheet in the binder is an odd–even duplex leaf pair $(2k-1,\; 2k)$**:
- **Page-Count-Neutral Edits:** Keep edits inside a chapter's final ` clearpage` (or inside a 1-page `quicksheet`) so downstream page numbers do not shift.
- **Identify Physical Leaf Pair $(2k-1,\; 2k)$:**
- Edited **odd page $p=2k-1$** (front/recto) $\Rightarrow$ reprint pages **$p$ to $p+1$**.
- Edited **even page $p=2k$** (back/verso) $\Rightarrow$ reprint pages **$p-1$ to $p$**.
- **Print Settings:** Select **Actual Size / 100%** (never “Fit to Printable Area”), **Two-Sided: Flip on Long Edge**, punch on the $0.75\text{ in}$ inner margin, and swap the single leaf into the 3-ring binder.

**Binder Revision & Verification Sign-Off Ledger.**

| **Rev** | **Date** | **Scope** | **Summary of Verified Updates & QA Sign-Off** | **QA Status** |
| --- | --- | --- | --- | --- |
| **v1.0** | `2026-11-22` | Full Release | Initial 2026–2027 Division C Thermodynamics Binder (§§ 0–23, App. A–H, 54 vector figures, 5 indices, 12-pp QuickRef, Device Handbook, Grayscale Proof). Verified against `official-2027-C.pdf` + 9 National Clarifications + 0 Corrections + `verify_all.py` + `pdfcheck.py`. | **PASS (P1–P6 & V1)** |
| **v1.1** | ........ | ........ | ........ | ........ |
| **v1.2** | ........ | ........ | ........ | ........ |
| **v2.0** | ........ | ........ | ........ | ........ |
