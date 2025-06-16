import pandas as pd
from scipy.stats import binomtest
import matplotlib.pyplot as plt
from statsmodels.stats.multitest import multipletests

# Daten laden
df = pd.read_csv('dielectron.csv')
n = len(df)

# Parameter
epsilons = [1, 0.5, 2/3, 0.75, 1.25]
deltas = [0.1 * i for i in range(1, 31)]

# Erwartete Trefferquoten (Beispielwerte, bitte ggf. anpassen oder dynamisch bestimmen)
expected_hit_rates = {
    1: 0.01,
    0.5: 0.005,
    2/3: 0.006,
    0.75: 0.007,
    1.25: 0.0125,
}

# Dynamische Schätzung der Hintergrundrate außerhalb aller Signalbereiche (optional)
signal_mask = pd.Series(False, index=df.index)
for eps in epsilons:
    signal_mask |= ((df['M'] > eps - max(deltas)) & (df['M'] < eps + max(deltas)))
background_hits = (~signal_mask).sum()
background_rate = background_hits / n
print(f"Geschätzte Hintergrundrate außerhalb der Signalbereiche: {background_rate:.5f}\n")

print(f"Anzahl Events: {n}\n")

for eps in epsilons:
    p_values = []
    hits_list = []

    for delta in deltas:
        hits = ((df['M'] > eps - delta) & (df['M'] < eps + delta)).sum()
        # Hier kannst du background_rate statt expected_hit_rates[eps] verwenden, falls keine Theoriequote vorliegt
        expected_rate = expected_hit_rates[eps]
        test = binomtest(hits, n, expected_rate, alternative='greater')
        p_values.append(test.pvalue)
        hits_list.append(hits)

    # Multiple-Test-Korrektur (Bonferroni)
    reject, pvals_corrected, _, _ = multipletests(p_values, alpha=0.05, method='bonferroni')
    best_idx = pvals_corrected.argmin()

    print(f"Epsilon {eps}: Best Delta = {deltas[best_idx]:.3f} | Treffer = {hits_list[best_idx]} von {n} | "
          f"p-Wert roh = {p_values[best_idx]:.3e} | p-Wert korrigiert = {pvals_corrected[best_idx]:.3e}\n")

    # Plot der unkorrierten p-Werte
    plt.plot(deltas, p_values, label=f"Epsilon {eps}")

plt.xlabel("Delta")
plt.ylabel("p-Wert")
plt.yscale("log")
plt.legend()
plt.title("p-Werte für verschiedene Epsilon-Resonanzen")
plt.tight_layout()
plt.show()