"""Start script Level 6a: H0 scan — cosmological scaling."""

import numpy as np
from config import MODEL_PARAMS
from core.h0_scan import scan_h0, hubble_tension_signature, export_results
from viz.plot_h0_scan import plot_h0_scan, plot_hubble_tension

# === H0 scan: 60 to 80 km/s/Mpc in 21 steps ===
print("=" * 60)
print("Level 6a: H0 Scan of Resonance Field Coupling")
print("=" * 60)

h0_values = np.linspace(60, 80, 21)
dphi_values = np.linspace(0, np.pi, 15)

print(f"\nH0 range: {h0_values[0]:.0f} - {h0_values[-1]:.0f} km/s/Mpc")
print(f"Number of H0 values: {len(h0_values)}")
print(f"Phase scan points: {len(dphi_values)}")
print(f"Total simulations: {len(h0_values) * len(dphi_values) + len(dphi_values)}")
print()

fit_result = scan_h0(
    h0_values=h0_values,
    delta_phi_values=dphi_values,
    t_span=(0, 60),
    m=MODEL_PARAMS["m"],
    lmbda=MODEL_PARAMS["lmbda"],
    alpha=MODEL_PARAMS["alpha"],
    kappa=MODEL_PARAMS["kappa"],
    g=MODEL_PARAMS["g"],
)

# === Results ===
print("\n" + "=" * 60)
print("Results")
print("=" * 60)
print(f"\n  d_eta (flat, H=0):  {fit_result['d_eta_flat']:.4f}")
print(f"  d_eta (H0=60):      {fit_result['d_eta_mean'][0]:.4f}")
print(f"  d_eta (H0=67.4):    ", end="")

# Interpolate for Planck value
idx_planck = np.argmin(np.abs(h0_values - 67.4))
print(f"{fit_result['d_eta_mean'][idx_planck]:.4f}  (nearest scan point)")

print(f"  d_eta (H0=73.0):    ", end="")
idx_shoes = np.argmin(np.abs(h0_values - 73.0))
print(f"{fit_result['d_eta_mean'][idx_shoes]:.4f}  (nearest scan point)")

print(f"  d_eta (H0=80):      {fit_result['d_eta_mean'][-1]:.4f}")
print(f"\n  Slope dd_eta/dH0: {fit_result['fit_slope']:.5f} / (km/s/Mpc)")

# === Hubble tension signature ===
print("\n" + "=" * 60)
print("Hubble Tension Signature")
print("=" * 60)

tension = hubble_tension_signature(fit_result)

print(f"\n  Planck 2018 (H0 = {tension['h0_planck']}):  d_eta = {tension['d_eta_planck']:.4f}")
print(f"  SH0ES       (H0 = {tension['h0_shoes']}):  d_eta = {tension['d_eta_shoes']:.4f}")
print(f"\n  Delta d_eta:           {tension['delta_d_eta']:.4f}")
print(f"  Relative shift:        {tension['relative_shift']:.1f}%")

# === Plots ===
print("\nCreating plots ...")
plot_h0_scan(fit_result, save_path="images/h0_scan.png")
plot_hubble_tension(tension, fit_result, save_path="images/hubble_tension.png")

# === CSV export ===
export_results(fit_result, filepath="h0_scan_results.csv")
print("Results exported: h0_scan_results.csv")

print("\nDone.")
