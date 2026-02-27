"""
Animation und Visualisierung der gekoppelten Oszillatoren.

Abhängigkeiten: numpy
"""

import numpy as np


def smooth_max(arr, window):
    """Maximum der letzten window Werte. Funktioniert auch für Skalare."""
    arr = np.asarray(arr)
    if arr.ndim == 0:
        return arr
    if len(arr) < window:
        return np.max(arr)
    return np.max(arr[-window:])


def init(
    line1, line2, line1_path, line2_path,
    sinus_line1, sinus_line2, resonance_line,
    kin_line, pot_line, coup_line, tot_line,
    eps_line, e_res1_line, e_res2_line, resdiv_line
):
    """Setze alle Plotelemente auf Startzustand."""
    for line in [
        line1, line2, line1_path, line2_path,
        sinus_line1, sinus_line2, resonance_line,
        kin_line, pot_line, coup_line, tot_line,
        eps_line, e_res1_line, e_res2_line, resdiv_line
    ]:
        line.set_data([], [])
    return (
        line1, line2, line1_path, line2_path,
        sinus_line1, sinus_line2, resonance_line,
        kin_line, pot_line, coup_line, tot_line,
        eps_line, e_res1_line, e_res2_line, resdiv_line
    )


def update(
    frame,
    line1, line2, line1_path, line2_path,
    sinus_line1, sinus_line2, resonance_line,
    kin_line, pot_line, coup_line, tot_line,
    eps_line, e_res1_line, e_res2_line, resdiv_line,
    energy_ax, coupling_ax, resdiv_ax,
    t, x1_interp, v1_interp, x2_interp, v2_interp,
    ax_traj, ax_sin, resonance_condition_func,
    params, resonance_history
):
    omega1 = params['omega1']
    omega2 = params['omega2']
    alpha = params['alpha']
    h = params['h']
    m = params.get('m', 1.0)
    t_now = t[frame]
    x1_vals = x1_interp(t[:frame+1])
    v1_vals = v1_interp(t[:frame+1])
    x2_vals = x2_interp(t[:frame+1])
    v2_vals = v2_interp(t[:frame+1])

    # Trajektorie
    line1.set_data([x1_vals[-1]], [0])
    line2.set_data([x2_vals[-1]], [0.5])
    line1_path.set_data(x1_vals, np.zeros_like(x1_vals))
    line2_path.set_data(x2_vals, np.full_like(x2_vals, 0.5))
    sinus_line1.set_data(t[:frame+1], x1_vals)
    sinus_line2.set_data(t[:frame+1], x2_vals)

    ax_traj.set_title("Trajektorie der Oszillatoren")
    ax_sin.set_title("Zeitlicher Verlauf der Auslenkungen")

    # Energien
    from parameters_and_functions import compute_energies
    T, V1, V2, Vc, E, eps, E_res1, E_res2, res_div = compute_energies(
        x1_vals, v1_vals, x2_vals, v2_vals,
        omega1, omega2, alpha, h, m
    )

    time_window = t[:frame+1]
    kin_line.set_data(time_window, T)
    pot_line.set_data(time_window, V1 + V2)
    coup_line.set_data(time_window, Vc)
    tot_line.set_data(time_window, E)
    eps_line.set_data(time_window, eps * np.ones_like(time_window))
    e_res1_line.set_data(time_window,
                         E_res1 * np.ones_like(time_window))
    e_res2_line.set_data(time_window,
                         E_res2 * np.ones_like(time_window))
    resdiv_line.set_data(time_window, res_div)

    # Dynamische y-Achsen
    window = 50
    energy_ax.set_ylim(0, smooth_max(E, window) * 1.2)
    combined = np.maximum(
        np.array(E_res1) + np.array(E_res2),
        eps * np.ones_like(np.array(E_res1))
    )
    coupling_ax.set_ylim(0, smooth_max(combined, window) * 1.2)
    resdiv_ax.set_ylim(0, smooth_max(res_div, window) * 1.2)

    return (
        line1, line2, line1_path, line2_path,
        sinus_line1, sinus_line2, resonance_line,
        kin_line, pot_line, coup_line, tot_line,
        eps_line, e_res1_line, e_res2_line, resdiv_line
    )