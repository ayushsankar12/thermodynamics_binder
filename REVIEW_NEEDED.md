# Review Needed — items for the team to confirm

Items here need a human decision or a source the overhaul could not access (chiefly the purchased 2027 Rules Manual). Nothing in this list was changed in the binder unless the entry says so.

---

## A. Device model

### A1. What C_eff = 380 J/K means (Ex 13.2, §16) — decision taken, please confirm
- **Problem:** Ex 13.2 and §16 use C_eff = 380 J/K with τ = 903 s. 100 mL of water alone is 100.0 g × 4.184 J/(g·K) = 418.4 J/K, plus a few J/K for the cup. A uniformly heated cup cannot have C_eff < 418 J/K.
- **Decision taken:** C_eff is now stated to be a **fitted, effective top-layer capacitance**: the value that makes the one-node model match the temperature the ES probes at the top center. Stratification makes that layer warm faster than the mixed average, so the fitted value can be below 418 J/K. The model's numbers (and the τ = 903 s behind the §16 nomogram multipliers) were kept, and are labeled as modeled values for the reference collector.
- **Still open:** §15 uses a different top-layer capacitance for the same reference cup (C_top,eff ≈ 215 J/K, κ_strat ≈ 1.56). 380 J/K implies much weaker stratification (418.4/380 ≈ 1.10). Phase 4's single device model has to pick one; the team's own calibration runs should replace both.
- **Why it matters:** if your device behaves well-mixed (e.g. no glazing, strong side heating), C ≈ 420–425 J/K and τ is ~11% longer than the reference model assumes, which shifts the 11–15 min multipliers.

---

## B. Rules items to check against your own Rules Manual (pp. C57–C59)
*(filled in during Phase 3)*

---

## C. Things the overhaul could not verify
*(filled in as they come up)*
