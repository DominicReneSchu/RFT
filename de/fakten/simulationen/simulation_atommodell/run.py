"""
Gekoppelte Oszillatoren — Interaktive Simulation (Axiome A1–A4)

Einstiegspunkt mit UI, Slidern und Animation.

Abhängigkeiten: numpy, matplotlib, scipy
Ausführung: python run.py
"""

from __future__ import annotations

from typing import Any

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider, Button
from parameters_and_functions import (
    solve_coupled_oscillators, make_interpolators,
    resonance_condition, check_frequency_resonance
)
from animation import update, init


def main() -> None:
    t = np.linspace(0, 50, 4000)
    m = 1.0

    # Kopplungsparameter
    alpha_0 = 3.0
    h_0 = 1.0

    # Initialfrequenzen
    omega1_0 = 2 * np.pi * 1.0
    omega2_0 = 2 * np.pi * 1.02

    # --- Layout ---
    axcolor = 'lightgoldenrodyellow'
    fig = plt.figure(figsize=(18, 13))
    fig.canvas.manager.set_window_title(
        'Gekoppelte Oszillatoren — Resonanzfeldtheorie (A1–A4)')

    ax_traj = plt.subplot2grid((3, 2), (0, 0))
    ax_sin = plt.subplot2grid((3, 2), (0, 1))
    energy_ax = plt.subplot2grid((3, 2), (1, 0), colspan=2)
    coupling_ax = plt.subplot2grid((3, 2), (2, 0))
    resdiv_ax = plt.subplot2grid((3, 2), (2, 1))
    plt.subplots_adjust(left=0.07, right=0.98, top=0.94,
                        bottom=0.25, wspace=0.22, hspace=0.36)

    # --- Slider ---
    ax_f1 = plt.axes([0.17, 0.18, 0.7, 0.025], facecolor=axcolor)
    ax_f2 = plt.axes([0.17, 0.15, 0.7, 0.025], facecolor=axcolor)
    ax_alpha = plt.axes([0.17, 0.12, 0.7, 0.025], facecolor=axcolor)
    ax_tol = plt.axes([0.17, 0.09, 0.7, 0.025], facecolor=axcolor)
    ax_speed = plt.axes([0.17, 0.06, 0.7, 0.025], facecolor=axcolor)

    f1_slider = Slider(ax_f1, 'Frequenz 1 (Hz)', 0.7, 1.3,
                       valinit=1.0, valstep=0.005)
    f2_slider = Slider(ax_f2, 'Frequenz 2 (Hz)', 0.7, 1.3,
                       valinit=1.02, valstep=0.005)
    alpha_slider = Slider(ax_alpha, 'α (Kopplungsschärfe)', 0.1, 8.0,
                          valinit=alpha_0, valstep=0.01)
    tol_slider = Slider(ax_tol, 'Toleranz', 0.01, 0.5,
                        valinit=0.1, valstep=0.01)
    speed_slider = Slider(ax_speed, 'Geschwindigkeit', 10, 200,
                          valinit=50, valstep=1)

    # --- Buttons ---
    ax_export = plt.axes([0.82, 0.01, 0.13, 0.035])
    btn_export = Button(ax_export, 'Export CSV',
                        color='lightblue', hovercolor='deepskyblue')

    ax_gif = plt.axes([0.66, 0.01, 0.13, 0.035])
    btn_gif = Button(ax_gif, 'Export GIF',
                     color='lightgreen', hovercolor='limegreen')

    # --- Initiale Lösung ---
    def current_omegas() -> tuple[float, float]:
        return 2 * np.pi * f1_slider.val, 2 * np.pi * f2_slider.val

    t_num, x1_num, v1_num, x2_num, v2_num = \
        solve_coupled_oscillators(t, *current_omegas(),
                                  alpha_slider.val, h_0, m=m)
    x1_interp, v1_interp, x2_interp, v2_interp = \
        make_interpolators(t_num, x1_num, v1_num, x2_num, v2_num)

    # --- Trajektorien-Plot ---
    line1, = ax_traj.plot([], [], 'bo', markersize=8,
                          label='Oszillator 1')
    line2, = ax_traj.plot([], [], 'ro', markersize=8,
                          label='Oszillator 2')
    line1_path, = ax_traj.plot([], [], 'b-', linewidth=0.5, alpha=0.5)
    line2_path, = ax_traj.plot([], [], 'r-', linewidth=0.5, alpha=0.5)
    ax_traj.set_xlim(-1.5, 1.5)
    ax_traj.set_ylim(-1, 1.5)
    ax_traj.set_xlabel("Position")
    ax_traj.set_ylabel("Y-Achse")
    ax_traj.legend(loc='upper left')
    ax_traj.set_title("Trajektorien")

    # --- Sinusplot ---
    sinus_line1, = ax_sin.plot([], [], 'b-', label='Oszillator 1')
    sinus_line2, = ax_sin.plot([], [], 'r-', label='Oszillator 2')
    resonance_line, = ax_sin.plot([], [], 'g|', markersize=15,
                                  label='Resonanz')
    ax_sin.set_xlim(t[0], t[-1])
    ax_sin.set_ylim(-1.2, 1.2)
    ax_sin.set_xlabel("Zeit [s]")
    ax_sin.set_ylabel("Amplitude")
    ax_sin.legend(fontsize='small')
    ax_sin.set_title("Auslenkungen")

    # --- Energieplot ---
    kin_line, = energy_ax.plot([], [], color='blue', label='kinetisch')
    pot_line, = energy_ax.plot([], [], color='orange',
                               label='potenziell')
    coup_line, = energy_ax.plot([], [], color='purple',
                                label='Kopplung')
    tot_line, = energy_ax.plot([], [], color='black', linestyle='--',
                               label='gesamt')
    energy_ax.set_xlim(t[0], t[-1])
    energy_ax.set_ylim(0, 2)
    energy_ax.set_xlabel("Zeit [s]")
    energy_ax.set_ylabel("Energie")
    energy_ax.legend(loc="upper right")
    energy_ax.set_title("Energieverlauf (A4)")

    # --- Kopplungsoperator-Plot ---
    eps_line, = coupling_ax.plot([], [], color='red',
                                 label='ε — Kopplungsoperator')
    e_res1_line, = coupling_ax.plot([], [], color='magenta',
                                     linestyle='--', label='E_res(f₁)')
    e_res2_line, = coupling_ax.plot([], [], color='cyan',
                                     linestyle='--', label='E_res(f₂)')
    coupling_ax.set_xlim(t[0], t[-1])
    coupling_ax.set_ylim(0, 1.1)
    coupling_ax.set_xlabel("Zeit [s]")
    coupling_ax.set_ylabel("ε / E_res")
    coupling_ax.legend(fontsize='small')
    coupling_ax.set_title("Kopplungsoperator ε und Resonanzenergien")

    # --- Resonanzdivergenz-Plot ---
    resdiv_line, = resdiv_ax.plot([], [], color='green',
                                   label='Resonanz-Divergenz')
    resdiv_ax.set_xlim(t[0], t[-1])
    resdiv_ax.set_ylim(0, 1.1)
    resdiv_ax.set_xlabel("Zeit [s]")
    resdiv_ax.set_ylabel("ΔE")
    resdiv_ax.legend(fontsize='small')
    resdiv_ax.set_title("Resonanz-Divergenz |E_mech − E_res|")

    # --- Parameter-Container ---
    params = {
        'tol_slider': tol_slider,
        'min_resonance_distance': 1.0,
        'omega1': 2 * np.pi * f1_slider.val,
        'omega2': 2 * np.pi * f2_slider.val,
        'alpha': alpha_slider.val,
        'h': h_0,
        'm': m
    }

    resonance_history = []

    # --- Animation-Funktionen ---
    def wrapped_init() -> tuple[Any, ...]:
        resonance_history.clear()
        return init(
            line1, line2, line1_path, line2_path,
            sinus_line1, sinus_line2, resonance_line,
            kin_line, pot_line, coup_line, tot_line,
            eps_line, e_res1_line, e_res2_line, resdiv_line
        )

    def recalc_interpolators() -> None:
        nonlocal x1_interp, v1_interp, x2_interp, v2_interp
        nonlocal t_num, x1_num, v1_num, x2_num, v2_num
        params['omega1'] = 2 * np.pi * f1_slider.val
        params['omega2'] = 2 * np.pi * f2_slider.val
        params['alpha'] = alpha_slider.val

        # Resonanz-Check (Axiom 3)
        f1 = f1_slider.val
        f2 = f2_slider.val
        is_res, n, m_r = check_frequency_resonance(f1, f2)
        if is_res:
            fig.suptitle(
                f'Gekoppelte Oszillatoren — '
                f'✓ Resonanz: f₁/f₂ ≈ {n}/{m_r}',
                fontsize=12, color='green')
        else:
            fig.suptitle(
                f'Gekoppelte Oszillatoren — '
                f'✗ Keine Resonanz: f₁/f₂ ≈ {f1/f2:.3f}',
                fontsize=12, color='gray')

        t_num, x1_num, v1_num, x2_num, v2_num = \
            solve_coupled_oscillators(
                t, params['omega1'], params['omega2'],
                params['alpha'], params['h'], m=params['m'])
        x1_interp, v1_interp, x2_interp, v2_interp = \
            make_interpolators(t_num, x1_num, v1_num, x2_num, v2_num)
        resonance_history.clear()

    def update_wrapper(frame: int, *args: Any) -> tuple[Any, ...]:
        return update(
            frame, *args,
            t, x1_interp, v1_interp, x2_interp, v2_interp,
            ax_traj, ax_sin, resonance_condition,
            params, resonance_history
        )

    ani = FuncAnimation(
        fig,
        update_wrapper,
        frames=len(t),
        init_func=wrapped_init,
        interval=1000 / speed_slider.val,
        blit=True,
        fargs=(
            line1, line2, line1_path, line2_path,
            sinus_line1, sinus_line2, resonance_line,
            kin_line, pot_line, coup_line, tot_line,
            eps_line, e_res1_line, e_res2_line, resdiv_line,
            energy_ax, coupling_ax, resdiv_ax
        )
    )

    # --- Callbacks ---
    def update_params(val: float) -> None:
        recalc_interpolators()

    def update_speed(val: float) -> None:
        ani.event_source.interval = 1000 / speed_slider.val

    f1_slider.on_changed(update_params)
    f2_slider.on_changed(update_params)
    alpha_slider.on_changed(update_params)
    tol_slider.on_changed(lambda val: None)
    speed_slider.on_changed(update_speed)

    def on_export(event: Any) -> None:
        import csv
        filename = "resonanzzeiten.csv"
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Resonanzzeitpunkt'])
            for t_res in resonance_history:
                writer.writerow([t_res])
        btn_export.label.set_text("Exportiert!")

    btn_export.on_clicked(on_export)

    def on_export_gif(event: Any) -> None:
        btn_gif.label.set_text("Export läuft...")
        fig.canvas.draw()
        gif_frames = 500
        frame_indices = np.linspace(0, len(t) - 1, gif_frames,
                                    dtype=int)

        gif_ani = FuncAnimation(
            fig,
            update_wrapper,
            frames=frame_indices,
            init_func=wrapped_init,
            blit=True,
            fargs=(
                line1, line2, line1_path, line2_path,
                sinus_line1, sinus_line2, resonance_line,
                kin_line, pot_line, coup_line, tot_line,
                eps_line, e_res1_line, e_res2_line, resdiv_line,
                energy_ax, coupling_ax, resdiv_ax
            )
        )
        gif_ani.save('animation.gif', writer='pillow', fps=25)
        btn_gif.label.set_text("GIF exportiert!")

    btn_gif.on_clicked(on_export_gif)

    # Initial Resonanz-Check
    recalc_interpolators()
    plt.show()


if __name__ == "__main__":
    main()