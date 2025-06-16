import numpy as np

def smooth_max(arr, window):
    """Gibt das Maximum der letzten window Werte eines Arrays zurück. Funktioniert auch für Skalare."""
    arr = np.asarray(arr)
    if arr.ndim == 0:  # Skalar
        return arr
    if len(arr) < window:
        return np.max(arr)
    return np.max(arr[-window:])

def init(
    line1, line2, line1_path, line2_path, sinus_line1, sinus_line2, resonance_line,
    kin_line, pot_line, coup_line, tot_line,
    schu_e_line, schu_e1_line, schu_e2_line, resdiv_line
):
    """
    Setzt alle Plotelemente auf den Startzustand (leere Daten).
    """
    for line in [
        line1, line2, line1_path, line2_path, sinus_line1, sinus_line2, resonance_line,
        kin_line, pot_line, coup_line, tot_line,
        schu_e_line, schu_e1_line, schu_e2_line, resdiv_line
    ]:
        line.set_data([], [])
    return (
        line1, line2, line1_path, line2_path, sinus_line1, sinus_line2, resonance_line,
        kin_line, pot_line, coup_line, tot_line,
        schu_e_line, schu_e1_line, schu_e2_line, resdiv_line
    )

def update(
    frame,
    line1, line2, line1_path, line2_path, sinus_line1, sinus_line2, resonance_line,
    kin_line, pot_line, coup_line, tot_line,
    schu_e_line, schu_e1_line, schu_e2_line, resdiv_line,
    energy_ax, schu_ax, resdiv_ax,
    t, x1_interp, v1_interp, x2_interp, v2_interp, ax_traj, ax_sin, resonance_condition_func,
    params, resonance_history
):
    omega1 = params['omega1']
    omega2 = params['omega2']
    schu_alpha = params['schu_alpha']
    schu_h = params['schu_h']
    m = params.get('m', 1.0)
    t_now = t[frame]
    x1_vals = x1_interp(t[:frame+1])
    v1_vals = v1_interp(t[:frame+1])
    x2_vals = x2_interp(t[:frame+1])
    v2_vals = v2_interp(t[:frame+1])

    # Trajektorie und Sinusverlauf
    line1.set_data([x1_vals[-1]], [0])
    line2.set_data([x2_vals[-1]], [0.5])
    line1_path.set_data(x1_vals, np.zeros_like(x1_vals))
    line2_path.set_data(x2_vals, np.full_like(x2_vals, 0.5))
    sinus_line1.set_data(t[:frame+1], x1_vals)
    sinus_line2.set_data(t[:frame+1], x2_vals)

    # Titel
    ax_traj.set_title("Trajektorie der Oszillatoren")
    ax_sin.set_title("Zeitlicher Verlauf der Auslenkungen")

    # Energie-Berechnung
    from parameters_and_functions import compute_energies
    T, V1, V2, Vc, E, schu_e, E_schu1, E_schu2, res_div = compute_energies(
        x1_vals, v1_vals, x2_vals, v2_vals, omega1, omega2, schu_alpha, schu_h, m
    )

    # Update Energielinien
    time_window = t[:frame+1]
    kin_line.set_data(time_window, T)
    pot_line.set_data(time_window, V1 + V2)
    coup_line.set_data(time_window, Vc)
    tot_line.set_data(time_window, E)
    schu_e_line.set_data(time_window, schu_e * np.ones_like(time_window))
    schu_e1_line.set_data(time_window, E_schu1 * np.ones_like(time_window))
    schu_e2_line.set_data(time_window, E_schu2 * np.ones_like(time_window))
    resdiv_line.set_data(time_window, res_div)

    # Dynamische Skalierung der y-Achsen mit Gleitfenster
    window = 50
    energy_ax.set_ylim(0, smooth_max(E, window) * 1.2)
    schu_combined = np.array(E_schu1) + np.array(E_schu2)
    combined_arr = np.maximum(schu_combined, schu_e * np.ones_like(schu_combined))
    schu_ax.set_ylim(0, smooth_max(combined_arr, window) * 1.2)
    resdiv_ax.set_ylim(0, smooth_max(res_div, window) * 1.2)

    return (
        line1, line2, line1_path, line2_path, sinus_line1, sinus_line2, resonance_line,
        kin_line, pot_line, coup_line, tot_line,
        schu_e_line, schu_e1_line, schu_e2_line, resdiv_line
    )