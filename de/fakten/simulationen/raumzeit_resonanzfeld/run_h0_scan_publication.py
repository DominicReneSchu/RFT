"""
Startskript Publikationsversion: H0-Scan mit erweiterter Statistik.

Erweiterungen:
  - 51 H0-Punkte (0-100 km/s/Mpc) x 30 Phasenpunkte = 1.560 Simulationen
  - t_span = (0, 120) — doppelte Integrationszeit
  - Jackknife-Fehler auf d_eta
  - Bootstrap-Fehler auf Steigung
  - Vollstaendiger JSON-Export aller Ergebnisse
  - Erweiterter Kontrolltest (3 Szenarien + 2 Zwischenstufen)
"""

from __future__ import annotations

import os
import json
import numpy as np
from config import MODEL_PARAMS, NUMERIC_PARAMS, H0_SCAN_PARAMS
from core.h0_scan import scan_h0, hubble_tension_signature, export_results
from core.flat_coupled import scan_phase_flat
from core.coupled_flrw import scan_phase_coupling
from viz.plot_h0_scan import plot_h0_scan, plot_hubble_tension

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

print("=" * 70)
print("PUBLIKATIONSLAUF: H0-Scan der Resonanzfeldkopplung")
print("=" * 70)

# Parameter aus config
h0_min = H0_SCAN_PARAMS["h0_min"]
h0_max = H0_SCAN_PARAMS["h0_max"]
n_h0 = H0_SCAN_PARAMS["n_h0_points"]
n_phase = H0_SCAN_PARAMS["n_phase_points"]
t_span = NUMERIC_PARAMS["t_span_h0_scan"]

h0_values = np.linspace(h0_min, h0_max, n_h0)
dphi_values = np.linspace(0, np.pi, n_phase)

n_total = n_h0 * n_phase + n_phase  # +flat
print(f"\nH0-Bereich: {h0_min:.0f} - {h0_max:.0f} km/s/Mpc")
print(f"H0-Punkte: {n_h0}")
print(f"Phasenscan-Punkte: {n_phase}")
print(f"Integrationszeit: t = {t_span[0]} bis {t_span[1]}")
print(f"Einzelsimulationen: {n_total}")
print()

# === Erweiterter Kontrolltest (5 Szenarien) ===
print("=" * 60)
print("Erweiterter Kontrolltest: 5 Expansionsszenarien")
print("=" * 60)

common = dict(m=MODEL_PARAMS["m"], lmbda=MODEL_PARAMS["lmbda"],
              g=MODEL_PARAMS["g"])

scenarios = [
    ("Flach (H=0)", 0.0),
    ("Langsam (adot0=0.1)", 0.1),
    ("FLRW Standard (adot0=0.3)", 0.3),
    ("Mittel (adot0=0.6)", 0.6),
    ("Schnell (adot0=1.0)", 1.0),
]

kontroll_ergebnisse = []
for name, adot0 in scenarios:
    print(f"\n  {name} ...")
    if adot0 == 0.0:
        scan = scan_phase_flat(
            delta_phi_values=dphi_values, t_span=t_span, **common
        )
    else:
        scan = scan_phase_coupling(
            delta_phi_values=dphi_values, t_span=t_span,
            alpha=MODEL_PARAMS["alpha"], kappa=MODEL_PARAMS["kappa"],
            adot0=adot0, **common,
        )
    v = np.isfinite(scan["eta_mean"])
    if np.any(v):
        d = np.nanmean(np.abs(scan["eta_mean"][v] - scan["eta_cos2"][v]))
    else:
        d = np.nan
    kontroll_ergebnisse.append((name, adot0, d))
    print(f"    <|d_eta|> = {d:.4f}")

print("\nZusammenfassung Kontrolltest:")
print(f"  {'Szenario':<30} {'adot0':>8} {'<|d_eta|>':>10}")
for name, adot0, d in kontroll_ergebnisse:
    print(f"  {name:<30} {adot0:8.1f} {d:10.4f}")
bestaetigt = all(
    kontroll_ergebnisse[i][2] <= kontroll_ergebnisse[i + 1][2]
    for i in range(len(kontroll_ergebnisse) - 1)
    if np.isfinite(kontroll_ergebnisse[i][2])
    and np.isfinite(kontroll_ergebnisse[i + 1][2])
)
print(f"\n  Monotonie bestaetigt: {bestaetigt}")

# === Hauptscan ===
print("\n" + "=" * 60)
print("H0-Scan (Publikationsversion)")
print("=" * 60)

fit_result = scan_h0(
    h0_values=h0_values,
    delta_phi_values=dphi_values,
    t_span=t_span,
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
print(f"\n  Einzelsimulationen: {fit_result['n_simulations']}")
print(f"  d_eta (flach, H=0):  {fit_result['d_eta_flat']:.4f} "
      f"+- {fit_result['d_eta_flat_jk']:.4f} (Jackknife)")

# Ausgewaehlte H0-Werte
for h0_show in [0, 60, 67.4, 73.0, 80, 100]:
    idx = np.argmin(np.abs(h0_values - h0_show))
    d = fit_result["d_eta_mean"][idx]
    jk = fit_result["d_eta_jk_err"][idx]
    print(f"  d_eta (H0={h0_show:5.1f}):   {d:.4f} +- {jk:.4f}")

slope = fit_result["fit_slope"]
slope_err = fit_result.get("fit_slope_err", np.nan)
print(f"\n  Steigung dd_eta/dH0: ({slope:.5f} +- {slope_err:.5f}) / (km/s/Mpc)")

# === Hubble-Spannung ===
print("\n" + "=" * 60)
print("Hubble-Spannungs-Signatur")
print("=" * 60)

tension = hubble_tension_signature(fit_result)

print(f"\n  Planck 2018 (H0={tension['h0_planck']}): "
      f"d_eta = {tension['d_eta_planck']:.4f}")
print(f"  SH0ES       (H0={tension['h0_shoes']}): "
      f"d_eta = {tension['d_eta_shoes']:.4f}")
print(f"\n  Delta d_eta:            {tension['delta_d_eta']:.4f} "
      f"+- {tension['delta_d_eta_err']:.4f}")
print(f"  Relative Verschiebung:  {tension['relative_shift']:.1f}%")

# === Plots ===
bilder_dir = os.path.join(SCRIPT_DIR, "bilder")
os.makedirs(bilder_dir, exist_ok=True)
print("\nErstelle Plots ...")
plot_h0_scan(fit_result, save_path=os.path.join(bilder_dir, "h0_scan.png"))
plot_hubble_tension(tension, fit_result,
                    save_path=os.path.join(bilder_dir, "hubble_tension.png"))

# === CSV-Export ===
out_dir = os.path.join(SCRIPT_DIR, "publication_results")
os.makedirs(out_dir, exist_ok=True)
export_results(fit_result,
               filepath=os.path.join(out_dir, "h0_scan_results.csv"))

# === JSON-Export ===
export = {
    "h0_range": [float(h0_min), float(h0_max)],
    "n_h0_points": int(n_h0),
    "n_phase_points": int(n_phase),
    "t_span": list(t_span),
    "n_simulations_total": int(fit_result["n_simulations"]),
    "model_params": MODEL_PARAMS,
    "d_eta_flat": float(fit_result["d_eta_flat"]),
    "d_eta_flat_jk": float(fit_result["d_eta_flat_jk"]),
    "fit_slope": float(slope),
    "fit_slope_err": float(slope_err),
    "fit_intercept": float(fit_result["fit_intercept"]),
    "hubble_tension": {
        "h0_planck": tension["h0_planck"],
        "h0_shoes": tension["h0_shoes"],
        "d_eta_planck": float(tension["d_eta_planck"]),
        "d_eta_shoes": float(tension["d_eta_shoes"]),
        "delta_d_eta": float(tension["delta_d_eta"]),
        "delta_d_eta_err": float(tension["delta_d_eta_err"]),
        "relative_shift_pct": float(tension["relative_shift"]),
    },
    "control_test": [
        {"scenario": name, "adot0": float(a), "d_eta": float(d)}
        for name, a, d in kontroll_ergebnisse
    ],
}
json_path = os.path.join(out_dir, "h0_scan_publication.json")
with open(json_path, "w") as f:
    json.dump(export, f, indent=2)
print(f"\nJSON exportiert: {json_path}")

print("\n" + "=" * 70)
print("PUBLIKATIONSLAUF ABGESCHLOSSEN")
print("=" * 70)