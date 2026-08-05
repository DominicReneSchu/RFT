"""
RT-07 — Independent η Estimators: Comparison Analysis

This script calls scan_phase_coupling() over Δφ ∈ [0, π] in 20 steps,
computes all three independent compute_eta_independent() estimators per
Δφ value, and prints a comparison table.

Falsification criterion:
  - All three estimators < 5 % mean deviation from cos²(Δφ/2):
      → ε = η empirically strengthened by three independent methods.
  - Systematic deviation of one or more estimators:
      → Deviation pattern documented; hypothesis ε = η flagged for revision.

Output:
  - Table on stdout
  - Plot: rt07_estimator_comparison.png in the same directory
"""

import sys
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Path to core library
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "core"))
from coupled_flrw import coupled_flrw_sim, compute_eta_independent

N_STEPS = 20
THRESHOLD = 0.05  # 5 % falsification threshold

delta_phi_values = np.linspace(0, np.pi, N_STEPS)

eta_energy_list = []
eta_mi_list = []
eta_plv_list = []
eta_cos2_list = []

print("RT-07 — Independent η Estimators")
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

print(f"\nMean deviations from cos²(Δφ/2):")
print(f"  η_E  (energy transfer):     {mean_dev_e:.4f}  "
      f"({'< 5 %' if mean_dev_e < THRESHOLD else '≥ 5 %'})")
print(f"  η_MI (mutual information):  {mean_dev_mi:.4f}  "
      f"({'< 5 %' if mean_dev_mi < THRESHOLD else '≥ 5 %'})")
print(f"  η_PLV (phase locking):      {mean_dev_plv:.4f}  "
      f"({'< 5 %' if mean_dev_plv < THRESHOLD else '≥ 5 %'})")

all_pass = mean_dev_e < THRESHOLD and mean_dev_mi < THRESHOLD and mean_dev_plv < THRESHOLD

print()
if all_pass:
    print("✅ RESULT: All three estimators approximate cos²(Δφ/2) to < 5 %.")
    print("   ε = η empirically strengthened by three independent methods.")
    print("   K-2 (tautology critique of Pearson estimator) resolved.")
else:
    devs = {
        "η_E": mean_dev_e,
        "η_MI": mean_dev_mi,
        "η_PLV": mean_dev_plv,
    }
    failing = [k for k, v in devs.items() if v >= THRESHOLD]
    print(f"⚠️  WARNING: The following estimators deviate ≥ 5 %: {', '.join(failing)}")
    print("   Deviation pattern should be analysed; hypothesis ε = η flagged for revision.")
    if len(failing) >= 2:
        print("   CRITICAL: Multiple estimators deviate — ε = η must be re-evaluated.")

# --- Plot ---
fig, ax = plt.subplots(figsize=(9, 5))
x = delta_phi_values / np.pi

ax.plot(x, eta_cos2_arr, "k--", lw=2, label=r"$\cos^2(\Delta\phi/2)$ reference")
ax.plot(x, eta_energy_arr, "o-", color="tab:blue", ms=5,
        label=r"$\eta_E$ (energy transfer)")
ax.plot(x, eta_mi_arr, "s-", color="tab:orange", ms=5,
        label=r"$\eta_{MI}$ (mutual information)")
ax.plot(x, eta_plv_arr, "^-", color="tab:green", ms=5,
        label=r"$\eta_{PLV}$ (phase locking value)")

ax.set_xlabel(r"$\Delta\phi\,/\,\pi$", fontsize=13)
ax.set_ylabel(r"$\eta$", fontsize=13)
ax.set_title("RT-07 — Independent η Estimators vs. cos²(Δφ/2)", fontsize=13)
ax.legend(fontsize=11)
ax.set_xlim(0, 1)
ax.set_ylim(-0.05, 1.15)
ax.grid(True, alpha=0.3)

out_path = os.path.join(os.path.dirname(__file__), "rt07_estimator_comparison.png")
fig.tight_layout()
fig.savefig(out_path, dpi=150)
plt.close(fig)
print(f"\nPlot saved: {out_path}")
