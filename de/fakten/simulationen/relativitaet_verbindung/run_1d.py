from core.flrw_1d import flrw_1d_sim
from viz.plot_1d import plot_1d_results

# Starte 1D-FLRW-Resonanzfeldsimulation mit Standardparametern
sol, V = flrw_1d_sim()
plot_1d_results(sol, V)