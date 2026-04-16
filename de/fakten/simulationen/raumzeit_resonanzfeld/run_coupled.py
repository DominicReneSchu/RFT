"""Startskript: Gekoppelte FLRW-Resonanzfeldsimulation."""

from __future__ import annotations

import numpy as np
from config import MODEL_PARAMS, NUMERIC_PARAMS
from core.coupled_flrw import coupled_flrw_sim, scan_phase_coupling
from viz.plot_coupled import plot_coupled_results, plot_phase_scan

print("Starte gekoppelte Simulation (dphi_0 = pi/4) ...")
sol, results = coupled_flrw_sim(
    eps1_0=0.3, eps2_0=0.3, delta_phi_0=np.pi / 4,
    a0=1.0, adot0=0.3,
    m=MODEL_PARAMS["m"], lmbda=MODEL_PARAMS["lmbda"],
    alpha=MODEL_PARAMS["alpha"], kappa=MODEL_PARAMS["kappa"],
    g=MODEL_PARAMS["g"], t_span=(0, 40),
    rtol=NUMERIC_PARAMS["rtol"], atol=NUMERIC_PARAMS["atol"],
)
plot_coupled_results(sol, results, alpha=MODEL_PARAMS["alpha"], kappa=MODEL_PARAMS["kappa"], g=MODEL_PARAMS["g"])

print("Starte Phasenscan (20 Simulationen) ...")
scan = scan_phase_coupling(
    delta_phi_values=np.linspace(0, np.pi, 20), t_span=(0, 40),
    m=MODEL_PARAMS["m"], lmbda=MODEL_PARAMS["lmbda"],
    alpha=MODEL_PARAMS["alpha"], kappa=MODEL_PARAMS["kappa"],
    g=MODEL_PARAMS["g"],
)
plot_phase_scan(scan)
print("Fertig.")
