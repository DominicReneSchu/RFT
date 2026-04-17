# Monte Carlo Simulation for Resonance Analysis

*Dominic-René Schu, 2025/2026*

*[Detailed results and interpretation report → report_out/resonance_report.md](./report_out/resonance_report.md)*

---

## Introduction

The Monte Carlo simulation is a central tool in the statistical
evaluation of scientific datasets. In this analysis it is used to
determine the probability with which an observed excess of events in
the vicinity of a suspected resonance mass point (M₀) could be
explained purely by chance through the background.

### Scientific Context

Monte Carlo tests are standard in modern physics, data science,
and many other research fields when analytical solutions are too
complex or unavailable. They allow a robust, empirical determination
of significances, especially for adaptive or non-trivial search
procedures such as this resonance analysis.

### Relation to Resonance Field Theory

This simulation validates the predictions of Axiom 3
(Resonance Condition) of the
[Resonance Field Theory](../../../docs/definitions/axiomatic_foundation.md):
If resonance points are physically real, the observed excesses must
lie significantly above the background — even under conservative
simulation of the null hypothesis.

The stability of the results over many simulation runs
is consistent with Axiom 7 (Invariance): The resonance structure
is preserved under variation of the simulation parameters.

This analysis forms, together with
[ResoTrade](../../resotrade/resotrade_trading_ki.md), the empirical basis
of the Resonance Field Theory — particle physics and financial
markets as two independent domains in which resonance structures
are demonstrated.

---

## Dataset

CMS Open Data Dielectron dataset (electron–positron pairs
from proton–proton collisions):

| Property | Value |
|----------|-------|
| Events | 99,915 (after NaN removal) |
| Observable | Invariant mass M (GeV) |
| Mass range | 2.00 – 110.00 GeV |
| Source | CMS Open Data |

---

## Investigated Resonance Mass Points

The analysis searches for excesses at four known particle
resonances in the dielectron channel:

| Resonance | M₀ (GeV) | Natural width | Signal exclusion |
|-----------|----------|---------------|-----------------|
| J/ψ (Charmonium) | 3.10 | σ ≈ 0.05 GeV | ±0.15 GeV |
| Υ(1S) (Bottomonium) | 9.46 | σ ≈ 0.1 GeV | ±0.20 GeV |
| Υ(2S) (Bottomonium) | 10.02 | σ ≈ 0.1 GeV | ±0.20 GeV |
| Z boson | 91.20 | Γ ≈ 2.5 GeV | ±4.0 GeV |

The signal exclusion defines the narrow region around each
mass point that is removed when training the background model.
The search windows (Δ) are independent of this and vary
from 0.02 to 10.0 GeV.

---

## Objective

The goal is to quantify the empirical significance (p-value) of
the observations by simulating many background scenarios and
comparing them with the real data.

---

## Methodology

### Background Modelling

* The background distribution is extracted from the measurement
  data — with explicit exclusion of the narrow signal regions
  (around the investigated M₀ values).
* A Kernel Density Estimator (KDE, bandwidth 0.5 GeV) is used
  to produce a smooth probability distribution.
* The expected hit rate is computed **Δ-dependent** from the
  KDE background model (numerical integration), not specified as
  a fixed value. This prevents large windows from generating
  trivial significances.

### Execution of the Monte Carlo Simulation

* 10,000 *pseudo-experiments* are performed, each drawing the
  same number of events as in the original dataset from the
  KDE model.
* For each *pseudo-experiment*, the full resonance analysis
  is repeated:
  * Hit counts in variable windows (Δ = 0.02–10.0 GeV)
    around each resonance mass point M₀ are determined.
  * The p-values are computed using binomial test + Bonferroni
    correction over all window widths.
  * The respective optimal window sizes are determined automatically.
* Bootstrap confidence intervals (5,000 repetitions) are computed
  for hit counts and p-values.

### Determination of the Empirical p-value

* The empirical p-value is the fraction of simulation runs in
  which an excess as extreme or more extreme than in the real
  data was found.
* If the empirical p-value = 0, no comparable signal was produced
  by pure background in any of the 10,000 simulations.

---

## Results

### Summary (10,000 MC simulations, 26 Feb 2026)

| M₀ (GeV) | Resonance | Δ_opt (GeV) | Hits | Bootstrap [16%, 84%] | p_corr | empir. p |
|-----------|-----------|-------------|------|-----------------------|--------|----------|
| 3.10 | J/ψ | 0.440 | 3256 | [3200, 3313] | 1.02e-121 | 0 |
| 9.46 | Υ(1S) | 0.780 | 4186 | [4122, 4248] | 3.01e-201 | 0 |
| 10.02 | Υ(2S) | 0.840 | 4625 | [4559, 4691] | 5.16e-188 | 0 |
| 91.20 | Z boson | 0.040 | 52 | [45, 59] | 0.00e+00 | 0 |

**All four resonances are detected with extreme significance.**
In none of the 10,000 pseudo-experiments was a comparable excess
produced by pure background (empirical p-value = 0 for all mass points).

### Physical Interpretation of the Results

* **J/ψ (3.10 GeV):** Optimal window Δ = 0.44 GeV, 3,256 hits.
  The window width reflects the detector resolution at low masses.
* **Υ(1S) and Υ(2S) (9.46 / 10.02 GeV):** Windows Δ = 0.78–0.84
  GeV, 4,186/4,625 hits. The two peaks are only 0.56 GeV apart,
  resulting in partial overlap of the search windows.
* **Z boson (91.20 GeV):** Extremely narrow optimal window
  Δ = 0.04 GeV with 52 hits. The KDE background density is
  practically zero after excluding the Z peak at 91.2 GeV —
  therefore few hits suffice for maximum significance.

---

## Visualisation of Results

### 1. Monte Carlo Hits vs. Real Hits

The histogram shows how frequently certain hit counts in the
optimal window for each resonance mass point M₀ occurred in the
Monte Carlo simulation. The red line marks the value from the
real data.

![Histogram MC vs Real](report_out/figures/hist_mc_vs_real_hits.png)

---

### 2. p-value Curves over Window Width Δ

For each resonance mass point M₀, the p-values from the
MC simulations (median and 68% interval) and the real data
as a function of Δ.

![p-value curves](report_out/figures/pvalue_curves.png)

---

### 3. Heatmaps: Hit Count over M₀ and Δ

The heatmaps show the hit counts for all combinations of
M₀ and Δ, once for the real data and once as the mean
of the Monte Carlo simulations.

![Heatmaps hit count](report_out/figures/heatmaps_hits.png)

---

## Interpretation

* The Monte Carlo simulation shows how exceptional the observed
  excesses are compared to the background.
* Empirical p-values = 0 across all four mass points argue
  for an extremely low probability that the findings arise by chance.
* The graphical comparison (histograms, p-value curves,
  heatmaps) makes the difference between signal and background
  clear.
* The consistency of results across different resonance widths
  (narrow: J/ψ, Υ; broad: Z) confirms the robustness of the method.

### Significance for Resonance Field Theory

The results confirm Axiom 3 of the Resonance Field Theory:
Resonance points produce measurable, significant excesses that
cannot be reproduced by any background model. The invariance of
the results over 10,000 simulation runs is consistent with Axiom 7.

Together with [ResoTrade](../../resotrade/resotrade_trading_ki.md),
it becomes clear: resonance structures are not restricted to
particle physics — they manifest wherever oscillations with a
pronounced natural frequency are present (Axiom 1).

---

## Code Notes

* The simulation uses `scikit-learn` for KDE, `numpy` and
  `pandas` for data handling, `matplotlib` for static and
  `plotly` for interactive visualisation.
* Progress bars (`tqdm`) show the simulation progress.
* All key parameters (M₀, Δ, signal exclusion widths,
  KDE bandwidth) are centrally configured in `config.py`.
* The expected hit rates are precomputed Δ-dependent from the
  KDE background model (`precompute_expected_rates`),
  which drastically reduces the runtime of the 10,000 simulations.
* The most important plots are automatically stored in the
  `report_out/figures` folder and are directly embedded here.

### Running the Simulation

1. Navigate to the project directory.
2. Ensure all required Python packages are installed
   (see `requirements.txt`).
3. Start the main script:

   ```bash
   python en/facts/empirical/monte_carlo/monte_carlo_test/run.py
   ```

4. The generated results and plots can be found in the
   `report_out/` folder.

---

## Conclusion

The Monte Carlo method provides a robust way to statistically
validate resonance effects. The analysis detects all four
investigated particle resonances (J/ψ, Υ(1S), Υ(2S), Z boson)
with empirical p-value = 0 over 10,000 simulation runs.

The methodology — KDE-based background modelling with
Δ-dependent expected rates, Bonferroni-corrected binomial tests,
and bootstrap confidence intervals — is transferable to any dataset
with suspected resonance structures.

---

© Dominic-René Schu — Resonance Field Theory 2025/2026

---

⬅️ [back](../../../../README.md)
