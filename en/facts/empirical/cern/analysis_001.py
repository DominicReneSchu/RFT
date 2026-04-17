from __future__ import annotations

import pandas as pd
from scipy.stats import binomtest
import matplotlib.pyplot as plt
from statsmodels.stats.multitest import multipletests

# Load data
df = pd.read_csv('dielectron.csv')
n = len(df)

# Parameters
epsilons = [1, 0.5, 2/3, 0.75, 1.25]
deltas = [0.1 * i for i in range(1, 31)]

# Expected hit rates (example values, adjust or determine dynamically if needed)
expected_hit_rates = {
    1: 0.01,
    0.5: 0.005,
    2/3: 0.006,
    0.75: 0.007,
    1.25: 0.0125,
}

# Dynamic estimation of the background rate outside all signal regions (optional)
signal_mask = pd.Series(False, index=df.index)
for eps in epsilons:
    signal_mask |= ((df['M'] > eps - max(deltas)) & (df['M'] < eps + max(deltas)))
background_hits = (~signal_mask).sum()
background_rate = background_hits / n
print(f"Estimated background rate outside signal regions: {background_rate:.5f}\n")

print(f"Number of events: {n}\n")

for eps in epsilons:
    p_values = []
    hits_list = []

    for delta in deltas:
        hits = ((df['M'] > eps - delta) & (df['M'] < eps + delta)).sum()
        # You can use background_rate instead of expected_hit_rates[eps] if no theory rate is available
        expected_rate = expected_hit_rates[eps]
        test = binomtest(hits, n, expected_rate, alternative='greater')
        p_values.append(test.pvalue)
        hits_list.append(hits)

    # Multiple testing correction (Bonferroni)
    reject, pvals_corrected, _, _ = multipletests(p_values, alpha=0.05, method='bonferroni')
    best_idx = pvals_corrected.argmin()

    print(f"Epsilon {eps}: Best Delta = {deltas[best_idx]:.3f} | Hits = {hits_list[best_idx]} of {n} | "
          f"Raw p-value = {p_values[best_idx]:.3e} | Corrected p-value = {pvals_corrected[best_idx]:.3e}\n")

    # Plot uncorrected p-values
    plt.plot(deltas, p_values, label=f"Epsilon {eps}")

plt.xlabel("Delta")
plt.ylabel("p-value")
plt.yscale("log")
plt.legend()
plt.title("p-values for different epsilon resonances")
plt.tight_layout()
plt.show()
