"""Startskript Stufe 6a: H0-Scan — Kosmologische Skalierung."""

import numpy as np
from config import MODEL_PARAMS
from core.h0_scan import scan_h0, hubble_tension_signature, export_results
from viz.plot_h0_scan import plot_h0_scan, plot_hubble_tension

# === H0-Scan: 60 bis 80 km/s/Mpc in 21 Schritten ===
print("=" * 60)
print("Stufe 6a: H0-Scan der Resonanzfeldkopplung")
print("=" * 60)

h0_values = np.linspace(60, 80, 21)
dphi_values = np.linspace(0, np.pi, 15)

print(f"\nH0-Bereich: {h0_values[0]:.0f} - {h0_values[-1]:.0f} km/s/Mpc")
print(f"Anzahl H0-Werte: {len(h0_values)}")
print(f"Phasenscan-Punkte: {len(dphi_values)}")
print(f"Simulationen gesamt: {len(h0_values) * len(dphi_values) + len(dphi_values)}")
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

# === Ergebnisse ===
print("\n" + "=" * 60)
print("Ergebnisse")
print("=" * 60)
print(f"\n  d_eta (flach, H=0):  {fit_result['d_eta_flat']:.4f}")
print(f"  d_eta (H0=60):       {fit_result['d_eta_mean'][0]:.4f}")
print(f"  d_eta (H0=67.4):     ", end="")

# Interpoliere fuer Planck-Wert
idx_planck = np.argmin(np.abs(h0_values - 67.4))
print(f"{fit_result['d_eta_mean'][idx_planck]:.4f}  (naechster Scan-Punkt)")

print(f"  d_eta (H0=73.0):     ", end="")
idx_shoes = np.argmin(np.abs(h0_values - 73.0))
print(f"{fit_result['d_eta_mean'][idx_shoes]:.4f}  (naechster Scan-Punkt)")

print(f"  d_eta (H0=80):       {fit_result['d_eta_mean'][-1]:.4f}")
print(f"\n  Steigung dd_eta/dH0: {fit_result['fit_slope']:.5f} / (km/s/Mpc)")

# === Hubble-Spannungs-Signatur ===
print("\n" + "=" * 60)
print("Hubble-Spannungs-Signatur")
print("=" * 60)

tension = hubble_tension_signature(fit_result)

print(f"\n  Planck 2018 (H0 = {tension['h0_planck']}):  d_eta = {tension['d_eta_planck']:.4f}")
print(f"  SH0ES       (H0 = {tension['h0_shoes']}):  d_eta = {tension['d_eta_shoes']:.4f}")
print(f"\n  Delta d_eta:         {tension['delta_d_eta']:.4f}")
print(f"  Relative Verschiebung: {tension['relative_shift']:.1f}%")

# === Plots ===
print("\nErstelle Plots ...")
plot_h0_scan(fit_result, save_path="bilder/h0_scan.png")
plot_hubble_tension(tension, fit_result, save_path="bilder/hubble_tension.png")

# === CSV-Export ===
export_results(fit_result, filepath="h0_scan_results.csv")
print("Ergebnisse exportiert: h0_scan_results.csv")

print("\nFertig.")