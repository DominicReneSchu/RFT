"""
RT-07 — Unabhängige η-Estimatoren: Vergleichsanalyse

Dieses Skript ruft scan_phase_coupling() über Δφ ∈ [0, π] in 20 Schritten
auf, berechnet pro Δφ-Wert alle drei unabhängigen compute_eta_independent()-
Estimatoren und gibt eine Vergleichstabelle aus.

Falsifizierungskriterium:
  - Alle drei Estimatoren < 5 % mittlere Abweichung von cos²(Δφ/2):
      → ε = η empirisch durch drei unabhängige Methoden gestärkt.
  - Systematische Abweichung eines Estimators:
      → Abweichungsmuster dokumentiert, Hypothese ε = η zur Revision vorgemerkt.

Ausgabe:
  - Tabelle auf stdout
  - Plot: rt07_estimator_vergleich.png im selben Verzeichnis
"""

import sys
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Pfad zur core-Bibliothek
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "core"))
from coupled_flrw import coupled_flrw_sim, compute_eta_independent

N_STEPS = 20
THRESHOLD = 0.05  # 5 % Falsifizierungsschwelle

delta_phi_values = np.linspace(0, np.pi, N_STEPS)

eta_energy_list = []
eta_mi_list = []
eta_plv_list = []
eta_cos2_list = []

print("RT-07 — Unabhängige η-Estimatoren")
print("=" * 78)
print(f"{'Δφ':>8} {'η_E':>10} {'η_MI':>10} {'η_PLV':>10} "
      f"{'η_cos²':>10} {'|ΔE|':>8} {'|ΔMI|':>8} {'|ΔPLV|':>8}")
print("-" * 78)

for dphi in delta_phi_values:
    sol, results = coupled_flrw_sim(delta_phi_0=dphi)
    est = compute_eta_independent(sol, results)

    e_e = est["eta_energy"]
    e_mi = est["eta_mi"]
    e_plv = est["eta_plv"]
    e_ref = est["eta_cos2_ref"]

    d_e = abs(e_e - e_ref) if np.isfinite(e_e) and np.isfinite(e_ref) else float("nan")
    d_mi = abs(e_mi - e_ref) if np.isfinite(e_mi) and np.isfinite(e_ref) else float("nan")
    d_plv = abs(e_plv - e_ref) if np.isfinite(e_plv) and np.isfinite(e_ref) else float("nan")

    eta_energy_list.append(e_e)
    eta_mi_list.append(e_mi)
    eta_plv_list.append(e_plv)
    eta_cos2_list.append(e_ref)

    print(f"{dphi:8.4f} {e_e:10.4f} {e_mi:10.4f} {e_plv:10.4f} "
          f"{e_ref:10.4f} {d_e:8.4f} {d_mi:8.4f} {d_plv:8.4f}")

print("=" * 78)

eta_energy_arr = np.array(eta_energy_list)
eta_mi_arr = np.array(eta_mi_list)
eta_plv_arr = np.array(eta_plv_list)
eta_cos2_arr = np.array(eta_cos2_list)

mean_dev_e = float(np.nanmean(np.abs(eta_energy_arr - eta_cos2_arr)))
mean_dev_mi = float(np.nanmean(np.abs(eta_mi_arr - eta_cos2_arr)))
mean_dev_plv = float(np.nanmean(np.abs(eta_plv_arr - eta_cos2_arr)))

print(f"\nMittlere Abweichungen von cos²(Δφ/2):")
print(f"  η_E  (Energietransfer):     {mean_dev_e:.4f}  "
      f"({'< 5 %' if mean_dev_e < THRESHOLD else '≥ 5 %'})")
print(f"  η_MI (Mutual Information):  {mean_dev_mi:.4f}  "
      f"({'< 5 %' if mean_dev_mi < THRESHOLD else '≥ 5 %'})")
print(f"  η_PLV (Phase Locking):      {mean_dev_plv:.4f}  "
      f"({'< 5 %' if mean_dev_plv < THRESHOLD else '≥ 5 %'})")

all_pass = mean_dev_e < THRESHOLD and mean_dev_mi < THRESHOLD and mean_dev_plv < THRESHOLD

print()
if all_pass:
    print("✅ ERGEBNIS: Alle drei Estimatoren approximieren cos²(Δφ/2) auf < 5 %.")
    print("   ε = η empirisch durch drei unabhängige Methoden gestärkt.")
    print("   K-2 (Tautologie-Kritik des Pearson-Estimators) als behoben anzusehen.")
else:
    devs = {
        "η_E": mean_dev_e,
        "η_MI": mean_dev_mi,
        "η_PLV": mean_dev_plv,
    }
    failing = [k for k, v in devs.items() if v >= THRESHOLD]
    print(f"⚠️  WARNUNG: Folgende Estimatoren weichen ≥ 5 % ab: {', '.join(failing)}")
    print("   Abweichungsmuster zu analysieren; Hypothese ε = η zur Revision vormerken.")
    if len(failing) >= 2:
        print("   KRITISCH: Mehrere Estimatoren weichen ab — ε = η muss neu bewertet werden.")

# --- Plot ---
fig, ax = plt.subplots(figsize=(9, 5))
x = delta_phi_values / np.pi

ax.plot(x, eta_cos2_arr, "k--", lw=2, label=r"$\cos^2(\Delta\phi/2)$ Referenz")
ax.plot(x, eta_energy_arr, "o-", color="tab:blue", ms=5,
        label=r"$\eta_E$ (Energietransfer)")
ax.plot(x, eta_mi_arr, "s-", color="tab:orange", ms=5,
        label=r"$\eta_{MI}$ (Mutual Information)")
ax.plot(x, eta_plv_arr, "^-", color="tab:green", ms=5,
        label=r"$\eta_{PLV}$ (Phase Locking Value)")

ax.set_xlabel(r"$\Delta\phi\,/\,\pi$", fontsize=13)
ax.set_ylabel(r"$\eta$", fontsize=13)
ax.set_title("RT-07 — Unabhängige η-Estimatoren vs. cos²(Δφ/2)", fontsize=13)
ax.legend(fontsize=11)
ax.set_xlim(0, 1)
ax.set_ylim(-0.05, 1.15)
ax.grid(True, alpha=0.3)

out_path = os.path.join(os.path.dirname(__file__), "rt07_estimator_vergleich.png")
fig.tight_layout()
fig.savefig(out_path, dpi=150)
plt.close(fig)
print(f"\nPlot gespeichert: {out_path}")
