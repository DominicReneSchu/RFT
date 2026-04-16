"""Kontrolltest: Falsifizierbare Vorhersage der Resonanzfeldtheorie."""

from __future__ import annotations

import numpy as np
from config import MODEL_PARAMS
from core.flat_coupled import scan_phase_flat
from core.coupled_flrw import scan_phase_coupling
from viz.plot_control import plot_control_comparison

dphi_values = np.linspace(0, np.pi, 25)
common = dict(m=MODEL_PARAMS["m"], lmbda=MODEL_PARAMS["lmbda"], g=MODEL_PARAMS["g"])

print("Fall 1/3: Flache Raumzeit (H = 0) ...")
scan_flat = scan_phase_flat(delta_phi_values=dphi_values, t_span=(0, 60), **common)
d1 = np.nanmean(np.abs(scan_flat["eta_mean"] - scan_flat["eta_cos2"]))
print(f"  <|d_eta|> = {d1:.4f}")

print("Fall 2/3: FLRW-Expansion (adot0 = 0.3) ...")
scan_flrw = scan_phase_coupling(delta_phi_values=dphi_values, t_span=(0, 60), alpha=MODEL_PARAMS["alpha"], kappa=MODEL_PARAMS["kappa"], adot0=0.3, **common)
d2 = np.nanmean(np.abs(scan_flrw["eta_mean"] - scan_flrw["eta_cos2"]))
print(f"  <|d_eta|> = {d2:.4f}")

print("Fall 3/3: Starke Expansion (adot0 = 1.0) ...")
scan_fast = scan_phase_coupling(delta_phi_values=dphi_values, t_span=(0, 60), alpha=MODEL_PARAMS["alpha"], kappa=MODEL_PARAMS["kappa"], adot0=1.0, **common)
d3 = np.nanmean(np.abs(scan_fast["eta_mean"] - scan_fast["eta_cos2"]))
print(f"  <|d_eta|> = {d3:.4f}")

print("\nErstelle Vergleichsplot ...")
plot_control_comparison(scan_flat, scan_flrw, scan_fast)

print("\n=== Ergebnis ===")
print(f"  d_eta (flach):    {d1:.4f}")
print(f"  d_eta (FLRW):     {d2:.4f}")
print(f"  d_eta (schnell):  {d3:.4f}")

if d1 < d2:
    print("\n  Vorhersage bestaetigt: d_eta(H>0) > d_eta(H=0)")
    if d3 > d2:
        print("  Verstaerkung bestaetigt: d_eta(H>>0) > d_eta(H>0)")
else:
    print("\n  Vorhersage NICHT bestaetigt.")

print("\nFertig.")
