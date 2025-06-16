import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from scipy.integrate import solve_ivp
from matplotlib.widgets import Slider, Button

g = 9.81
dt = 0.02
DEFAULT_TRAIL_LENGTH = 200

class DoublePendulumSim:
    def __init__(self):
        self.theta1_0 = np.pi / 2
        self.omega1_0 = 0.0
        self.theta2_0 = np.pi / 2
        self.omega2_0 = 0.0
        self.L1 = 1.0
        self.L2 = 1.0
        self.m1 = 1.0
        self.m2 = 1.0
        self.trail_length = DEFAULT_TRAIL_LENGTH
        self.reset()

    def derivatives(self, t, state, m1, m2, L1, L2, E):
        θ1, ω1, θ2, ω2 = state
        delta = θ2 - θ1
        denom1 = (m1 + m2) * L1 - m2 * L1 * np.cos(delta)**2
        coupling1 = E * np.sin(delta)
        coupling2 = -E * np.sin(delta)

        dθ1_dt = ω1
        dω1_dt = ((m2 * L1 * ω1**2 * np.sin(delta) * np.cos(delta) +
                  m2 * g * np.sin(θ2) * np.cos(delta) +
                  m2 * L2 * ω2**2 * np.sin(delta) -
                  (m1 + m2) * g * np.sin(θ1)) / denom1) + coupling1

        denom2 = (L2 / L1) * denom1

        dθ2_dt = ω2
        dω2_dt = ((-m2 * L2 * ω2**2 * np.sin(delta) * np.cos(delta) +
                  (m1 + m2) * g * np.sin(θ1) * np.cos(delta) -
                  (m1 + m2) * L1 * ω1**2 * np.sin(delta) -
                  (m1 + m2) * g * np.sin(θ2)) / denom2) + coupling2

        return [dθ1_dt, dω1_dt, dθ2_dt, dω2_dt]

    def reset(self):
        self.state = np.array([self.theta1_0, self.omega1_0, self.theta2_0, self.omega2_0])
        self.trail1_x = []
        self.trail1_y = []
        self.trail2_x = []
        self.trail2_y = []

    def step(self, dt, E):
        sol = solve_ivp(
            self.derivatives,
            (0, dt),
            self.state,
            args=(self.m1, self.m2, self.L1, self.L2, E),
            t_eval=[dt],
            method='RK45'
        )
        self.state = sol.y[:, -1]
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

    def get_positions(self):
        θ1, _, θ2, _ = self.state
        x1 = self.L1 * np.sin(θ1)
        y1 = -self.L1 * np.cos(θ1)
        x2 = x1 + self.L2 * np.sin(θ2)
        y2 = y1 - self.L2 * np.cos(θ2)
        return x1, y1, x2, y2

    def get_energies(self):
        θ1, ω1, θ2, ω2 = self.state
        T = 0.5 * self.m1 * (self.L1 * ω1) ** 2 + \
            0.5 * self.m2 * ((self.L1 * ω1) ** 2 + (self.L2 * ω2) ** 2 +
                             2 * self.L1 * self.L2 * ω1 * ω2 * np.cos(θ1 - θ2))
        V = -(self.m1 + self.m2) * g * self.L1 * np.cos(θ1) - self.m2 * g * self.L2 * np.cos(θ2)
        E_val = s_E.val if 's_E' in globals() else 1.0
        E_coupling = 0.5 * E_val * (self.L2 * θ2 - self.L1 * θ1) ** 2
        return T, V, E_coupling

    def get_kappa(self):
        T, V, E_coupling = self.get_energies()
        E_total = abs(T + V + E_coupling)
        return E_coupling / E_total if E_total > 0 else 0.0

# Simulation zuerst anlegen!
sim = DoublePendulumSim()

fig = plt.figure(figsize=(12, 7))
plt.subplots_adjust(left=0.33, right=0.98, top=0.93, bottom=0.07)
panel = plt.axes([0.03, 0.07, 0.28, 0.86], frameon=True)
panel.axis('off')
ax = plt.axes([0.36, 0.10, 0.62, 0.83])
ax.set_xlim(-2.2, 2.2)
ax.set_ylim(-2.2, 2.2)
ax.set_aspect('equal')
ax.axis('off')

fig.text(0.5, 0.98, "Doppelpendel-Simulation", ha='center', va='top', fontsize=15, color="#224488", weight='bold')
info_text = (
    r"$\theta_1$, $\theta_2$: Winkel | $m_1$, $m_2$: Massen | $L_1$, $L_2$: Längen | "
    r"$\mathcal{E}$: Kopplungsstärke (Kopplungsoperator) | "
    r"Mehr zur Theorie: Fakten > Mathematik > Doppelpendel"
)
fig.text(0.5, 0.954, info_text, ha='center', va='top', fontsize=10, color="#224488")
doc_url = "https://github.com/DominicReneSchu/public/blob/main/fakten/docs/mathematik/doppelpendel.md"
fig.text(0.03, 0.03, f"ℹ️ Dokumentation: {doc_url}", ha='left', va='bottom', fontsize=9, color="#224488")

line, = ax.plot([], [], 'o-', lw=2, color='blue')
trail1, = ax.plot([], [], 'r-', lw=1, alpha=0.5)
trail2, = ax.plot([], [], 'g-', lw=1, alpha=0.5)

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
    (r'$\mathcal{E}$', 1/np.e, np.e, 'E'),
    ('Spurlänge', 50, 1000, 'trail_length'),
]
slider_y = slider_start
for label, vmin, vmax, key in slider_labels:
    ax_slider = plt.axes([0.06, slider_y, 0.22, slider_height])
    if key == 'trail_length':
        slider = Slider(ax_slider, label, vmin, vmax, valinit=DEFAULT_TRAIL_LENGTH, valstep=10)
    elif key == 'E':
        slider = Slider(ax_slider, label, vmin, vmax, valinit=1.0)
    else:
        slider = Slider(ax_slider, label, vmin, vmax, valinit=getattr(sim, key))
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
s_E = slider_objects['E']
s_trail = slider_objects['trail_length']

def update_info_text():
    T, V, E_c = sim.get_energies()
    kappa = sim.get_kappa()
    txt = (
        f"Kinetische Energie: {T:.2f} J | Potentielle Energie: {V:.2f} J | "
        f"Kopplungsenergie: {E_c:.2f} J | Verhältnis κ = {kappa:.3f}"
    )
    return txt

energy_text = ax.text(0, 2.05, update_info_text(), fontsize=9, color='navy', ha='center')

def init():
    line.set_data([], [])
    trail1.set_data([], [])
    trail2.set_data([], [])
    energy_text.set_text("")
    return line, trail1, trail2, energy_text

def update(frame):
    sim.step(dt, s_E.val)
    x1, y1, x2, y2 = sim.get_positions()
    line.set_data([0, x1, x2], [0, y1, y2])
    trail1.set_data(sim.trail1_x, sim.trail1_y)
    trail2.set_data(sim.trail2_x, sim.trail2_y)
    energy_text.set_text(update_info_text())
    return line, trail1, trail2, energy_text

def reset(event=None):
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

def sliders_on_changed(val):
    reset()

for slider in slider_objects.values():
    slider.on_changed(sliders_on_changed)

reset_button_ax = plt.axes([0.06, 0.05, 0.1, 0.04])
reset_button = Button(reset_button_ax, 'Reset')
reset_button.on_clicked(reset)

gif_button_ax = plt.axes([0.18, 0.05, 0.1, 0.04])
gif_button = Button(gif_button_ax, 'GIF exportieren')

def export_gif(event):
    reset()
    frames = 500
    interval = dt * 1000  # in ms
    
    def update_frame(frame):
        sim.step(dt, s_E.val)
        x1, y1, x2, y2 = sim.get_positions()
        line.set_data([0, x1, x2], [0, y1, y2])
        trail1.set_data(sim.trail1_x, sim.trail1_y)
        trail2.set_data(sim.trail2_x, sim.trail2_y)
        energy_text.set_text(update_info_text())
        return line, trail1, trail2, energy_text

    anim = FuncAnimation(fig, update_frame, frames=frames, interval=interval, blit=True)
    writer = PillowWriter(fps=30)
    anim.save("doppelpendel.gif", writer=writer)
    print("GIF exportiert: doppelpendel.gif")

gif_button.on_clicked(export_gif)

anim = FuncAnimation(fig, update, init_func=init, interval=20, blit=True)
plt.show()
