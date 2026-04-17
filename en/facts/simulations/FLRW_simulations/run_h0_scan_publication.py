"""
Start script publication version: H0 scan with extended statistics.

Extensions:
  - 51 H0 points (0-100 km/s/Mpc) x 30 phase points = 1,560 simulations
  - t_span = (0, 120) — double integration time
  - Jackknife error on d_eta
  - Bootstrap error on slope
  - Full JSON export of all results
  - Extended control test (3 scenarios + 2 intermediate levels)
"""

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
print("PUBLICATION RUN: H0 Scan of Resonance Field Coupling")
print("=" * 70)

# Parameters from config
h0_min = H0_SCAN_PARAMS["h0_min"]
h0_max = H0_SCAN_PARAMS["h0_max"]
n_h0 = H0_SCAN_PARAMS["n_h0_points"]
n_phase = H0_SCAN_PARAMS["n_phase_points"]
t_span = NUMERIC_PARAMS["t_span_h0_scan"]

h0_values = np.linspace(h0_min, h0_max, n_h0)
dphi_values = np.linspace(0, np.pi, n_phase)

n_total = n_h0 * n_phase + n_phase  # +flat
print(f"\nH0 range: {h0_min:.0f} - {h0_max:.0f} km/s/Mpc")
print(f"H0 points: {n_h0}")
print(f"Phase scan points: {n_phase}")
print(f"Integration time: t = {t_span[0]} to {t_span[1]}")
print(f"Individual simulations: {n_total}")
print()

# === Extended control test (5 scenarios) ===
print("=" * 60)
print("Extended control test: 5 expansion scenarios")
print("=" * 60)

common = dict(m=MODEL_PARAMS["m"], lmbda=MODEL_PARAMS["lmbda"],
              g=MODEL_PARAMS["g"])

scenarios = [
    ("Flat (H=0)", 0.0),
    ("Slow (adot0=0.1)", 0.1),
    ("FLRW standard (adot0=0.3)", 0.3),
    ("Medium (adot0=0.6)", 0.6),
    ("Fast (adot0=1.0)", 1.0),
]

control_results = []
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
    control_results.append((name, adot0, d))
    print(f"    <|d_eta|> = {d:.4f}")

print("\nControl test summary:")
print(f"  {'Scenario':<30} {'adot0':>8} {'<|d_eta|>':>10}")
for name, adot0, d in control_results:
    print(f"  {name:<30} {adot0:8.1f} {d:10.4f}")
confirmed = all(
    control_results[i][2] <= control_results[i + 1][2]
    for i in range(len(control_results) - 1)
    if np.isfinite(control_results[i][2])
    and np.isfinite(control_results[i + 1][2])
)
print(f"\n  Monotonicity confirmed: {confirmed}")

# === Main scan ===
print("\n" + "=" * 60)
print("H0 scan (publication version)")
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

# === Results ===
print("\n" + "=" * 60)
print("Results")
print("=" * 60)
print(f"\n  Individual simulations: {fit_result['n_simulations']}")
print(f"  d_eta (flat, H=0):  {fit_result['d_eta_flat']:.4f} "
      f"+- {fit_result['d_eta_flat_jk']:.4f} (Jackknife)")

# Selected H0 values
for h0_show in [0, 60, 67.4, 73.0, 80, 100]:
    idx = np.argmin(np.abs(h0_values - h0_show))
    d = fit_result["d_eta_mean"][idx]
    jk = fit_result["d_eta_jk_err"][idx]
    print(f"  d_eta (H0={h0_show:5.1f}):   {d:.4f} +- {jk:.4f}")

slope = fit_result["fit_slope"]
slope_err = fit_result.get("fit_slope_err", np.nan)
print(f"\n  Slope dd_eta/dH0: ({slope:.5f} +- {slope_err:.5f}) / (km/s/Mpc)")

# === Hubble tension ===
print("\n" + "=" * 60)
print("Hubble Tension Signature")
print("=" * 60)

tension = hubble_tension_signature(fit_result)

print(f"\n  Planck 2018 (H0={tension['h0_planck']}): "
      f"d_eta = {tension['d_eta_planck']:.4f}")
print(f"  SH0ES       (H0={tension['h0_shoes']}): "
      f"d_eta = {tension['d_eta_shoes']:.4f}")
print(f"\n  Delta d_eta:            {tension['delta_d_eta']:.4f} "
      f"+- {tension['delta_d_eta_err']:.4f}")
print(f"  Relative shift:         {tension['relative_shift']:.1f}%")

# === Plots ===
images_dir = os.path.join(SCRIPT_DIR, "images")
os.makedirs(images_dir, exist_ok=True)
print("\nCreating plots ...")
plot_h0_scan(fit_result, save_path=os.path.join(images_dir, "h0_scan.png"))
plot_hubble_tension(tension, fit_result,
                    save_path=os.path.join(images_dir, "hubble_tension.png"))

# === CSV export ===
out_dir = os.path.join(SCRIPT_DIR, "publication_results")
os.makedirs(out_dir, exist_ok=True)
export_results(fit_result,
               filepath=os.path.join(out_dir, "h0_scan_results.csv"))

# === JSON export ===
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
        for name, a, d in control_results
    ],
}
json_path = os.path.join(out_dir, "h0_scan_publication.json")
with open(json_path, "w") as f:
    json.dump(export, f, indent=2)
print(f"\nJSON exported: {json_path}")

print("\n" + "=" * 70)
print("PUBLICATION RUN COMPLETED")
print("=" * 70)
