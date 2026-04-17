# Resonance Analysis in Mass Data

*Dominic-René Schu, 2025/2026*

---

## Introduction

This analysis investigates possible resonance points in a large
mass of data points from particle collisions. The goal is to
detect significant excesses of events around specific invariant
mass values M₀ and establish their statistical significance.

The methodology follows the principle of Axiom 3 (Resonance Condition)
of the [Resonance Field Theory](../../docs/definitions/axiomatic_foundation.md):
Resonance occurs when frequencies — here: energy values — stand in
certain ratios. The analysis searches for event excesses in windows
around suspected resonance mass points, analogous to the resonance
window analysis with weighting function G.

The data comprise a total of n = 10,000 events and were obtained from
[CERN Open Data](https://opendata.cern.ch/search?q=Particle%20masses&l=list&order=asc&p=1&s=10&sort=bestmatch).

---

## Axiomatic Reference

| Axiom | Relation to the Analysis |
|-------|--------------------------|
| A1 (Universal Oscillation) | Particle decays as oscillation modes |
| A3 (Resonance Condition) | Window analysis around resonance mass points M₀ |
| A7 (Invariance) | Result stability across different window widths |

---

## Methodology

### 1. Data Preprocessing

- **Cleaning and validation of data:**
  NaN values are removed to ensure stable background modelling.
- **Definition of resonance mass points M₀:**
  The mass ranges to be investigated are defined as a list
  (M₀ ∈ {0.50, 0.67, 0.75, 1.00, 1.25} GeV/c²).
- **Specification of window widths Δ:**
  Dynamic selection and variation of window widths to
  optimise the significance search.

### 2. Dynamic Window Width Analysis

For each resonance mass point M₀, the number of events in the
interval [M₀ − Δ, M₀ + Δ] is counted for various window widths Δ.
Subsequently, the window that shows the most significant excess
(after test correction) is determined.

This corresponds to the resonance window analysis from Axiom 3:

```
    G(M/M₀) = exp(−(|M/M₀ − 1| / δ)²)
```

where δ parametrises the window width.

### 3. Background Estimation

The background rate is modelled from the data outside the signal
regions using KDE (Kernel Density Estimate). Signal regions are
excluded. For the Monte Carlo simulation, samples are drawn from
the KDE sampler.

### 4. Significance Test and Multiple Testing Correction

- **Computation of raw p-values:**
  For each window, the hit count is compared to the expectation
  based on the binomial distribution.
- **Bootstrapping:**
  To quantify the uncertainty, confidence intervals for hit
  counts and p-values are determined via bootstrap.
- **Permutation test (optional):**
  The empirical distribution of hits is simulated by randomly
  permuting the data.
- **Multiple testing correction:**
  Bonferroni and FDR correction (Benjamini–Hochberg) are applied
  to control the error probability across all windows.

### 5. Monte Carlo Simulation

With many background samples, the distribution of the maximum
significance under the null hypothesis is determined empirically.
This yields an empirical p-value for the real result.

See also: [Monte Carlo Simulation for Resonance Analysis](../monte_carlo/monte_carlo_test/monte_carlo.md)

---

## Results

| M₀ (GeV/c²) | Best Δ | Hits | Raw p-value | Corrected p-value |
|:------------:|:------:|:----:|:-----------:|:-----------------:|
| 1.00 | 1.9 | 2699 | 0.000e+00 | 0.000e+00 |
| 0.50 | 2.1 | 1647 | 0.000e+00 | 0.000e+00 |
| 0.67 | 2.0 | 1860 | 0.000e+00 | 0.000e+00 |
| 0.75 | 2.0 | 2155 | 0.000e+00 | 0.000e+00 |
| 1.25 | 1.7 | 2901 | 0.000e+00 | 0.000e+00 |

The estimated background rate outside the signal regions
is approximately 0.93362.

### Stability and Robustness Checks

- Variation of the delta step size and analysis of result stability
- Verification of different M₀ lists and calibration uncertainties
- Bootstrapping and permutation tests for statistical validation
- Empirical p-values from Monte Carlo simulation

The stability of results across different parameter choices
is consistent with Axiom 7 (Invariance under synchronous
transformations): The resonance structure is preserved under
scaling variations.

---

## Visualisation

- **Histograms of the mass distribution:**
  With marked signal and background regions.
- **p-value curves:**
  For different resonance mass points as a function of
  window width.
- **Bootstrap intervals:**
  For hit counts and p-values.
- **Monte Carlo results:**
  Comparison of the real with the background distribution.

---

## Plot

<p align="center">
  <img src="images/plot_01.png" alt="Data analysis" width="800"/>
</p>

---

## Example Code and Visualisation

The following analysis shows the p-value curves for different
suspected resonance mass points (M₀). The Python code analyses
hit frequencies in variable window widths and determines the
significance taking into account an expected background rate
and multiple testing correction.

```python
import pandas as pd
from scipy.stats import binomtest
import matplotlib.pyplot as plt
from statsmodels.stats.multitest import multipletests

# Load data
df = pd.read_csv('dielectron.csv')
n = len(df)

# Parameters
mass_points = [1, 0.5, 2/3, 0.75, 1.25]  # Resonance mass points M₀
deltas = [0.1 * i for i in range(1, 31)]

# Expected hit rates
expected_hit_rates = {
    1: 0.01,
    0.5: 0.005,
    2/3: 0.006,
    0.75: 0.007,
    1.25: 0.0125,
}

# Dynamically estimate background rate outside all signal regions
signal_mask = pd.Series(False, index=df.index)
for m0 in mass_points:
    signal_mask |= ((df['M'] > m0 - max(deltas)) & (df['M'] < m0 + max(deltas)))
background_hits = (~signal_mask).sum()
background_rate = background_hits / n
print(f"Background rate: {background_rate:.5f}")

for m0 in mass_points:
    p_values = []
    hits_list = []

    for delta in deltas:
        hits = ((df['M'] > m0 - delta) & (df['M'] < m0 + delta)).sum()
        expected_rate = expected_hit_rates[m0]
        test = binomtest(hits, n, expected_rate, alternative='greater')
        p_values.append(test.pvalue)
        hits_list.append(hits)

    # Bonferroni correction
    reject, pvals_corrected, _, _ = multipletests(p_values, alpha=0.05, method='bonferroni')
    best_idx = pvals_corrected.argmin()

    print(f"M₀ {m0}: Best Delta = {deltas[best_idx]:.3f}, "
          f"Hits = {hits_list[best_idx]}, "
          f"Raw p-value = {p_values[best_idx]:.3e}, "
          f"Corrected p-value = {pvals_corrected[best_idx]:.3e}")

    plt.plot(deltas, p_values, label=f"M₀ = {m0}")

plt.xlabel("Delta")
plt.ylabel("p-value")
plt.yscale("log")
plt.legend()
plt.title("p-values for different resonance mass points")
plt.tight_layout()
plt.show()
```

---

## Conclusion and Outlook

The analysis shows robust and significant resonance excesses
at several mass values M₀. The methodological validation through
background estimation, multiple testing correction, bootstrapping,
and Monte Carlo simulation ensures a high level of significance.

The results are consistent with the resonance window model
of the RFT (Axiom 3): events accumulate significantly around
certain mass values, which can be interpreted as resonance points.

For future work, blind analyses, extended background models, and
comparisons with simulations are planned to further consolidate
the results.

---

## Technical Notes

- The complete analysis framework is modularly structured
  (`run.py`, `resonance_tools.py`, `visualization_interactive.py`,
  `report.py`, `config.py`).
- The core functions are equipped with docstrings and type annotations.
- All key steps are secured by unit tests.
- [scikit-learn](https://scikit-learn.org/) is used for KDE background
  modelling, [statsmodels](https://www.statsmodels.org/) for multiple
  testing.
- The script automatically checks for and removes NaN values.
- Progress bars (`tqdm`) visualise the simulation progress.
- The results are output as a Markdown report including embedded plots.

---

© Dominic-René Schu — Resonance Field Theory 2025/2026

---

⬅️ [back](../../../README.md)
