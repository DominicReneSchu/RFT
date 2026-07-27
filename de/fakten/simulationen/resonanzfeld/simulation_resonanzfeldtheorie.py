"""
Resonanzfeld-Simulation (Axiome A1-A5)

Interaktive Visualisierung der Resonanzfeldtheorie.
Läuft standalone (python simulation_resonanzfeldtheorie.py)
und in Jupyter Notebook.

Abhängigkeiten: numpy, matplotlib
"""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, RadioButtons
from fractions import Fraction


def epsilon_model(delta_phi: float | np.ndarray) -> float | np.ndarray:
    """Kopplungseffizienz als Funktion der Phasendifferenz (Axiom 4).

    Standardmodell: ε(Δφ) = cos²(Δφ/2)

    Returns
    -------
    float or ndarray
        Kopplungseffizienz ε ∈ [0, 1]
    """
    return np.cos(delta_phi / 2) ** 2


def check_resonance(f1: float, f2: float, tolerance: float = 0.01) -> tuple[bool, int, int]:
    """Prüfe Resonanzbedingung (Axiom 3).

    Resonanz tritt auf, wenn f1/f2 ≈ n/m mit n, m ∈ ℤ⁺.
    """
    if f2 == 0:
        return False, 0, 1
    ratio = Fraction(f1 / f2).limit_denominator(10)
    n, m = ratio.numerator, ratio.denominator
    is_resonant = np.isclose(f1 / f2, n / m, rtol=tolerance)
    return is_resonant, n, m


def energy_direction(psi: np.ndarray, window_short: int = 50, window_long: int = 200) -> np.ndarray:
    """Berechne Energierichtungsvektor (Axiom 5).

    energy_dir = e_short - e_long
    """
    kernel_s = np.ones(window_short) / window_short
    kernel_l = np.ones(window_long) / window_long
    e_short = np.convolve(psi ** 2, kernel_s, mode='same')
    e_long = np.convolve(psi ** 2, kernel_l, mode='same')
    return e_short - e_long


class ResonanzfeldSimulation:
    """Interaktive Resonanzfeld-Simulation mit matplotlib-Slidern."""

    H = 6.626e-34  # Plancksches Wirkungsquantum

    def __init__(self) -> None:
        self.t_max = 10
        self.n_points = 1000
        self.coupling_type = 'linear'

        # --- Figure mit 3 Subplots + Slider-Bereich ---
        self.fig = plt.figure(figsize=(13, 11))
        self.fig.canvas.manager.set_window_title(
            'Resonanzfeldtheorie – Simulation (A1–A5)')

        # Platz für Slider unten
        self.fig.subplots_adjust(bottom=0.28)

        self.ax1 = self.fig.add_subplot(3, 1, 1)
        self.ax2 = self.fig.add_subplot(3, 1, 2)
        self.ax3 = self.fig.add_subplot(3, 1, 3)

        # --- Slider ---
        ax_f1 = self.fig.add_axes([0.15, 0.17, 0.55, 0.02])
        ax_f2 = self.fig.add_axes([0.15, 0.13, 0.55, 0.02])
        ax_dp = self.fig.add_axes([0.15, 0.09, 0.55, 0.02])
        ax_tm = self.fig.add_axes([0.15, 0.05, 0.55, 0.02])

        self.sl_f1 = Slider(ax_f1, 'f₁ (Hz)', 0.1, 10.0,
                            valinit=2.0, valstep=0.1)
        self.sl_f2 = Slider(ax_f2, 'f₂ (Hz)', 0.1, 10.0,
                            valinit=3.0, valstep=0.1)
        self.sl_dp = Slider(ax_dp, 'Δφ (rad)', 0.0, np.pi,
                            valinit=0.0, valstep=0.05,
                            valfmt='%.2f')
        self.sl_tm = Slider(ax_tm, 't_max (s)', 1.0, 20.0,
                            valinit=10.0, valstep=1.0)

        self.sl_f1.on_changed(self._update)
        self.sl_f2.on_changed(self._update)
        self.sl_dp.on_changed(self._update)
        self.sl_tm.on_changed(self._update)

        # --- RadioButtons für Kopplungstyp ---
        ax_radio = self.fig.add_axes([0.78, 0.05, 0.18, 0.14])
        self.radio = RadioButtons(
            ax_radio,
            ('linear', 'quadratisch', 'trigonometrisch'),
            active=0
        )
        self.radio.on_clicked(self._set_coupling)

        # Erster Plot
        self._update(None)

    def _set_coupling(self, label: str) -> None:
        self.coupling_type = label
        self._update(None)

    def _update(self, _val: float | None) -> None:
        f1 = self.sl_f1.val
        f2 = self.sl_f2.val
        delta_phi = self.sl_dp.val
        t_max = self.sl_tm.val

        # --- Berechnung ---
        t = np.linspace(0, t_max, self.n_points)
        eps = epsilon_model(delta_phi)
        is_resonant, n, m = check_resonance(f1, f2)
        f_mean = (f1 + f2) / 2
        E_eff = np.pi * eps * self.H * f_mean

        # Axiom 1 & 2: Schwingungen
        psi1 = np.cos(2 * np.pi * f1 * t)
        psi2 = np.cos(2 * np.pi * f2 * t + delta_phi)
        psi_total = psi1 + psi2

        # Axiom 4: Energieübertragung
        if self.coupling_type == 'linear':
            e_trans = eps * psi1 * psi2
        elif self.coupling_type == 'quadratisch':
            e_trans = eps * psi1 ** 2 * psi2
        else:
            e_trans = eps * np.sin(psi1) * np.sin(psi2)
        e_trans *= np.exp(-0.1 * t)

        # Axiom 5: Energierichtung
        e_dir = energy_direction(psi_total)

        # --- Plot 1: Schwingungen (A1, A2, A3) ---
        self.ax1.clear()
        self.ax1.plot(t, psi1, alpha=0.8,
                      label=f'ψ₁: f₁ = {f1:.1f} Hz')
        self.ax1.plot(t, psi2, alpha=0.8,
                      label=f'ψ₂: f₂ = {f2:.1f} Hz')
        self.ax1.plot(t, psi_total, 'k--', alpha=0.4,
                      label='Superposition Φ')
        res_text = (f'✓ Resonanz: f₁/f₂ ≈ {n}/{m}'
                    if is_resonant
                    else f'✗ Keine Resonanz: f₁/f₂ ≈ {f1/f2:.3f}')
        color = '#90EE90' if is_resonant else '#FFB6C1'
        self.ax1.text(0.02, 0.92, res_text,
                      transform=self.ax1.transAxes, fontsize=9,
                      verticalalignment='top',
                      bbox=dict(facecolor=color, alpha=0.7))
        self.ax1.set_ylabel('Amplitude')
        self.ax1.set_title('A1 & A2: Schwingung und Superposition')
        self.ax1.legend(loc='upper right', fontsize=8)
        self.ax1.grid(True, alpha=0.3)

        # --- Plot 2: Energieübertragung (A4) ---
        self.ax2.clear()
        self.ax2.plot(t, e_trans, 'r-', alpha=0.8,
                      label='Energieübertragung')
        self.ax2.axhline(0, color='gray', linewidth=0.5)
        info = (f'ε(Δφ={delta_phi:.2f}) = {eps:.3f}\n'
                f'E_eff = {E_eff:.2e} J')
        self.ax2.text(0.02, 0.92, info,
                      transform=self.ax2.transAxes, fontsize=9,
                      verticalalignment='top',
                      bbox=dict(facecolor='lightyellow', alpha=0.7))
        self.ax2.set_ylabel('Energie [a.u.]')
        self.ax2.set_title(
            f'A4: Kopplungsenergie '
            f'(ε = {eps:.3f}, Modell: {self.coupling_type})')
        self.ax2.legend(loc='upper right', fontsize=8)
        self.ax2.grid(True, alpha=0.3)

        # --- Plot 3: Energierichtung (A5) ---
        self.ax3.clear()
        self.ax3.fill_between(t, e_dir, 0, where=e_dir > 0,
                              color='green', alpha=0.3,
                              label='Aufbau')
        self.ax3.fill_between(t, e_dir, 0, where=e_dir < 0,
                              color='red', alpha=0.3,
                              label='Abbau')
        self.ax3.plot(t, e_dir, 'k-', linewidth=0.5)
        self.ax3.axhline(0, color='gray', linewidth=0.5)
        self.ax3.set_xlabel('Zeit [s]')
        self.ax3.set_ylabel('Energierichtung')
        self.ax3.set_title(
            'A5: Energierichtungsvektor (e_short − e_long)')
        self.ax3.legend(loc='upper right', fontsize=8)
        self.ax3.grid(True, alpha=0.3)

        self.fig.canvas.draw_idle()

    def show(self) -> None:
        plt.show()


if __name__ == '__main__':
    print("Resonanzfeldtheorie – Interaktive Simulation")
    print("=" * 50)
    print("E = π · ε(Δφ) · h · f")
    print("ε(Δφ) = cos²(Δφ/2) ∈ [0, 1]")
    print()
    print("Slider bewegen zum Ändern der Parameter.")
    print("=" * 50)

    sim = ResonanzfeldSimulation()
    sim.show()