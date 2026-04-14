"""
Doppelpendel-Simulation — Resonanzfeldtheorie (Axiome A1, A2, A4)

Interaktive Simulation eines Doppelpendels mit dynamischer
Kopplungseffizienz ε(Δφ) = cos²(Δφ/2) nach Axiom 4.

Abhängigkeiten: numpy, matplotlib, scipy
Ausführung: python doppelpendel.py
"""

from __future__ import annotations

from typing import Any

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from scipy.integrate import solve_ivp
from matplotlib.widgets import Slider, Button

g = 9.81
dt = 0.02
DEFAULT_TRAIL_LENGTH = 200


# --- Kopplungseffizienz (Axiom 4) ---

def kopplungseffizienz(delta_phi: float | np.ndarray) -> float | np.ndarray:
    """ε(Δφ) = cos²(Δφ/2) ∈ [0, 1]

    Maximale Kopplung bei Phasengleichheit (Δφ = 0),
    keine Kopplung bei Gegenphase (Δφ = π).
    """
    return np.cos(delta_phi / 2) ** 2


class DoublePendulumSim:
    """Doppelpendel mit dynamischer Kopplungseffizienz.

    Die Lagrange-Gleichungen enthalten die natürliche mechanische
    Kopplung. Zusätzlich moduliert die Kopplungseffizienz
    ε(θ₂−θ₁) = cos²((θ₂−θ₁)/2) einen Resonanz-Kopplungsterm
    mit Amplitude A (Slider-Parameter).

    Effektiver Kopplungsterm:
        τ = ± A · ε(θ₂−θ₁) · sin(θ₂−θ₁)
    """

    def __init__(self) -> None:
        self.theta1_0 = np.pi / 2
        self.omega1_0 = 0.0
        self.theta2_0 = np.pi / 2
        self.omega2_0 = 0.0
        self.L1 = 1.0
        self.L2 = 1.0
        self.m1 = 1.0
        self.m2 = 1.0
        self.trail_length = DEFAULT_TRAIL_LENGTH
        self.current_epsilon = 1.0  # wird pro Schritt aktualisiert
        self.reset()

    def derivatives(self, t: float, state: np.ndarray, m1: float, m2: float, L1: float, L2: float, amplitude: float) -> list[float]:
        theta1, omega1, theta2, omega2 = state
        delta = theta2 - theta1

        # Kopplungseffizienz (Axiom 4)
        eps = kopplungseffizienz(delta)

        denom1 = (m1 + m2) * L1 - m2 * L1 * np.cos(delta)**2

        # Resonanz-Kopplungsterm: A · ε(Δφ) · sin(Δφ)
        coupling = amplitude * eps * np.sin(delta)

        dtheta1_dt = omega1
        domega1_dt = (
            (m2 * L1 * omega1**2 * np.sin(delta) * np.cos(delta)
             + m2 * g * np.sin(theta2) * np.cos(delta)
             + m2 * L2 * omega2**2 * np.sin(delta)
             - (m1 + m2) * g * np.sin(theta1))
            / denom1
        ) + coupling

        denom2 = (L2 / L1) * denom1

        dtheta2_dt = omega2
        domega2_dt = (
            (-m2 * L2 * omega2**2 * np.sin(delta) * np.cos(delta)
             + (m1 + m2) * g * np.sin(theta1) * np.cos(delta)
             - (m1 + m2) * L1 * omega1**2 * np.sin(delta)
             - (m1 + m2) * g * np.sin(theta2))
            / denom2
        ) - coupling

        return [dtheta1_dt, domega1_dt, dtheta2_dt, domega2_dt]

    def reset(self) -> None:
        self.state = np.array([
            self.theta1_0, self.omega1_0,
            self.theta2_0, self.omega2_0
        ])
        self.trail1_x = []
        self.trail1_y = []
        self.trail2_x = []
        self.trail2_y = []
        self.current_epsilon = kopplungseffizienz(
            self.theta2_0 - self.theta1_0)

    def step(self, dt_step: float, amplitude: float) -> None:
        sol = solve_ivp(
            self.derivatives,
            (0, dt_step),
            self.state,
            args=(self.m1, self.m2, self.L1, self.L2, amplitude),
            t_eval=[dt_step],
            method='RK45'
        )
        self.state = sol.y[:, -1]

        # Kopplungseffizienz aktualisieren
        delta = self.state[2] - self.state[0]
        self.current_epsilon = kopplungseffizienz(delta)

        x1, y1, x2, y2 = self.get_positions()
        self.trail1_x.append(x1)
        self.trail1_y.append(y1)
        self.trail2_x.append(x2)
        self.trail2_y.append(y2)
        if len(self.trail1_x) > self.trail_length:
            self.trail1_x.pop(0)
            self.trail1_y.pop(0)
            self.trail2_x.pop(0)
            self.trail2_y.pop(0)

    def get_positions(self) -> tuple[float, float, float, float]:
        theta1, _, theta2, _ = self.state
        x1 = self.L1 * np.sin(theta1)
        y1 = -self.L1 * np.cos(theta1)
        x2 = x1 + self.L2 * np.sin(theta2)
        y2 = y1 - self.L2 * np.cos(theta2)
        return x1, y1, x2, y2

    def get_energies(self, amplitude: float) -> tuple[float, float, float]:
        """Kinetische, potentielle und Kopplungsenergie."""
        theta1, omega1, theta2, omega2 = self.state
        delta = theta1 - theta2

        T = (0.5 * self.m1 * (self.L1 * omega1)**2
             + 0.5 * self.m2 * (
                 (self.L1 * omega1)**2
                 + (self.L2 * omega2)**2
                 + 2 * self.L1 * self.L2 * omega1 * omega2
                 * np.cos(delta)))

        V = (-(self.m1 + self.m2) * g * self.L1 * np.cos(theta1)
             - self.m2 * g * self.L2 * np.cos(theta2))

        # Kopplungsenergie skaliert mit ε und Amplitude
        E_coupling = 0.5 * amplitude * self.current_epsilon * (
            self.L2 * theta2 - self.L1 * theta1)**2

        return T, V, E_coupling

    def get_kappa(self, amplitude: float) -> float:
        """Kopplungsverhältnis κ = E_coupling / |E_total|."""
        T, V, E_coupling = self.get_energies(amplitude)
        E_total = abs(T + V + E_coupling)
        return E_coupling / E_total if E_total > 0 else 0.0


# --- Simulation ---
sim = DoublePendulumSim()

# --- Layout ---
fig = plt.figure(figsize=(12, 7))
fig.canvas.manager.set_window_title(
    'Doppelpendel — Resonanzfeldtheorie (A1, A2, A4)')
plt.subplots_adjust(left=0.33, right=0.98, top=0.93, bottom=0.07)

panel = plt.axes([0.03, 0.07, 0.28, 0.86], frameon=True)
panel.axis('off')

ax = plt.axes([0.36, 0.10, 0.62, 0.83])
ax.set_xlim(-2.2, 2.2)
ax.set_ylim(-2.2, 2.2)
ax.set_aspect('equal')
ax.axis('off')

fig.text(0.5, 0.98, "Doppelpendel — Resonanzfeldtheorie",
         ha='center', va='top', fontsize=15,
         color="#224488", weight='bold')
info_text_header = (
    r"$\theta_1$, $\theta_2$: Winkel | "
    r"$m_1$, $m_2$: Massen | "
    r"$L_1$, $L_2$: Längen | "
    r"$A$: Kopplungsamplitude | "
    r"$\varepsilon(\Delta\varphi) = \cos^2(\Delta\varphi/2)$: "
    r"Kopplungseffizienz (dynamisch)"
)
fig.text(0.5, 0.954, info_text_header,
         ha='center', va='top', fontsize=9, color="#224488")

line, = ax.plot([], [], 'o-', lw=2, color='blue')
trail1, = ax.plot([], [], 'r-', lw=1, alpha=0.5)
trail2, = ax.plot([], [], 'g-', lw=1, alpha=0.5)

# --- Slider ---
slider_height = 0.04
slider_gap = 0.01
slider_start = 0.88
slider_objects = {}
slider_labels = [
    (r'$\theta_1$ (rad)', 0, 2 * np.pi, 'theta1_0'),
    (r'$\theta_2$ (rad)', 0, 2 * np.pi, 'theta2_0'),
    (r'$\omega_1$ (rad/s)', -10, 10, 'omega1_0'),
    (r'$\omega_2$ (rad/s)', -10, 10, 'omega2_0'),
    (r'$m_1$ (kg)', 0.1, 5.0, 'm1'),
    (r'$m_2$ (kg)', 0.1, 5.0, 'm2'),
    (r'$L_1$ (m)', 0.1, 2.0, 'L1'),
    (r'$L_2$ (m)', 0.1, 2.0, 'L2'),
    (r'$A$ (Amplitude)', 0.0, 5.0, 'amplitude'),
    ('Spurlänge', 50, 1000, 'trail_length'),
]

slider_y = slider_start
for label, vmin, vmax, key in slider_labels:
    ax_slider = plt.axes([0.06, slider_y, 0.22, slider_height])
    if key == 'trail_length':
        slider = Slider(ax_slider, label, vmin, vmax,
                        valinit=DEFAULT_TRAIL_LENGTH, valstep=10)
    elif key == 'amplitude':
        slider = Slider(ax_slider, label, vmin, vmax, valinit=1.0)
    else:
        slider = Slider(ax_slider, label, vmin, vmax,
                        valinit=getattr(sim, key))
    slider_objects[key] = slider
    slider_y -= slider_height + slider_gap

s_theta1 = slider_objects['theta1_0']
s_theta2 = slider_objects['theta2_0']
s_omega1 = slider_objects['omega1_0']
s_omega2 = slider_objects['omega2_0']
s_m1 = slider_objects['m1']
s_m2 = slider_objects['m2']
s_L1 = slider_objects['L1']
s_L2 = slider_objects['L2']
s_amp = slider_objects['amplitude']
s_trail = slider_objects['trail_length']


# --- Energieanzeige ---
def update_info_text() -> str:
    amp = s_amp.val
    T, V, E_c = sim.get_energies(amp)
    kappa = sim.get_kappa(amp)
    eps = sim.current_epsilon
    delta = sim.state[2] - sim.state[0]
    return (
        f"T = {T:.2f} J | V = {V:.2f} J | "
        f"E_kopplung = {E_c:.2f} J | "
        f"κ = {kappa:.3f} | "
        f"ε = {eps:.3f} (Δφ = {delta:.2f} rad)"
    )


energy_text = ax.text(0, 2.05, update_info_text(),
                      fontsize=9, color='navy', ha='center')


# --- Animation ---
def init() -> tuple[Any, ...]:
    line.set_data([], [])
    trail1.set_data([], [])
    trail2.set_data([], [])
    energy_text.set_text("")
    return line, trail1, trail2, energy_text


def update(frame: int) -> tuple[Any, ...]:
    sim.step(dt, s_amp.val)
    x1, y1, x2, y2 = sim.get_positions()
    line.set_data([0, x1, x2], [0, y1, y2])
    trail1.set_data(sim.trail1_x, sim.trail1_y)
    trail2.set_data(sim.trail2_x, sim.trail2_y)
    energy_text.set_text(update_info_text())
    return line, trail1, trail2, energy_text


def reset(event: Any | None = None) -> None:
    sim.theta1_0 = s_theta1.val
    sim.omega1_0 = s_omega1.val
    sim.theta2_0 = s_theta2.val
    sim.omega2_0 = s_omega2.val
    sim.m1 = s_m1.val
    sim.m2 = s_m2.val
    sim.L1 = s_L1.val
    sim.L2 = s_L2.val
    sim.trail_length = int(s_trail.val)
    sim.reset()


def sliders_on_changed(val: float) -> None:
    reset()


for slider in slider_objects.values():
    slider.on_changed(sliders_on_changed)

# --- Buttons ---
reset_button_ax = plt.axes([0.06, 0.05, 0.1, 0.04])
reset_button = Button(reset_button_ax, 'Reset')
reset_button.on_clicked(reset)

gif_button_ax = plt.axes([0.18, 0.05, 0.1, 0.04])
gif_button = Button(gif_button_ax, 'GIF exportieren')


def export_gif(event: Any) -> None:
    reset()
    frames = 500
    interval_ms = dt * 1000

    def update_frame(frame: int) -> tuple[Any, ...]:
        sim.step(dt, s_amp.val)
        x1, y1, x2, y2 = sim.get_positions()
        line.set_data([0, x1, x2], [0, y1, y2])
        trail1.set_data(sim.trail1_x, sim.trail1_y)
        trail2.set_data(sim.trail2_x, sim.trail2_y)
        energy_text.set_text(update_info_text())
        return line, trail1, trail2, energy_text

    anim_gif = FuncAnimation(fig, update_frame, frames=frames,
                             interval=interval_ms, blit=True)
    writer = PillowWriter(fps=30)
    anim_gif.save("doppelpendel.gif", writer=writer)
    print("GIF exportiert: doppelpendel.gif")


gif_button.on_clicked(export_gif)

anim = FuncAnimation(fig, update, init_func=init,
                     interval=20, blit=True)
plt.show()