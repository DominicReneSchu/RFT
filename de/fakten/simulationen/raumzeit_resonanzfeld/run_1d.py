"""Startskript: 1D-FLRW-Resonanzfeldsimulation."""

from __future__ import annotations

from config import MODEL_PARAMS, INITIAL_CONDITIONS, NUMERIC_PARAMS
from core.flrw_1d import flrw_1d_sim
from viz.plot_1d import plot_1d_results

sol, V = flrw_1d_sim(
    eps0=INITIAL_CONDITIONS["eps0"],
    epsdot0=INITIAL_CONDITIONS["epsdot0"],
    a0=INITIAL_CONDITIONS["a0"],
    adot0=INITIAL_CONDITIONS["adot0"],
    m=MODEL_PARAMS["m"],
    lmbda=MODEL_PARAMS["lmbda"],
    alpha=MODEL_PARAMS["alpha"],
    kappa=MODEL_PARAMS["kappa"],
    t_span=NUMERIC_PARAMS["t_span_1d"],
    rtol=NUMERIC_PARAMS["rtol"],
    atol=NUMERIC_PARAMS["atol"],
)

plot_1d_results(
    sol, V,
    alpha=MODEL_PARAMS["alpha"],
    kappa=MODEL_PARAMS["kappa"],
)