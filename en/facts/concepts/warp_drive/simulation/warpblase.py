"""
Warp-Blase im Raumresonanzfeld – 3D, Mehrfachblasen, Interaktivität, Energiemapping
© Dominic Schu, 2025 – Alle Rechte vorbehalten.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 (needed for 3D plotting)
from matplotlib.widgets import Slider, Button

# --- Parameterbereich und Grid ---
size = 100
x = np.linspace(-5, 5, size)
y = np.linspace(-5, 5, size)
X, Y = np.meshgrid(x, y)

# --- Default-Parameter ---
dt = 0.05
t0 = 0.0
f_default = 160e9  # Hz
radius_default = 1.5
n_bubbles_default = 2
motion_ampl_default = 0.5
energy_map = True  # Energiemapping anzeigen

# --- Blasenparameter ---
f = f_default
radius = radius_default
n_bubbles = n_bubbles_default
motion_ampl = motion_ampl_default

def bubble_centers(t, n_bubbles, ampl):
    """
    Erzeugt eine Liste von Bubble-Zentren, die sich sinusförmig bewegen.
    """
    centers = []
    for i in range(n_bubbles):
        ang = 2 * np.pi * i / n_bubbles
        x0 = 2.0 * np.cos(ang) + ampl * np.sin(2 * np.pi * (0.1 + 0.05 * i) * t)
        y0 = 2.0 * np.sin(ang)
        centers.append((x0, y0))
    return centers

def warp_field(t, centers, radius, f):
    """
    Feld mit mehreren Warp-Blasen und sanften Übergängen.
    """
    base_wave = np.sin(2 * np.pi * f * t)
    field = base_wave * np.ones_like(X)
    phase_front = np.pi
    phase_back = 0

    for center in centers:
        R = np.sqrt((X - center[0])**2 + (Y - center[1])**2)
        front_mask = X > center[0] + radius
        back_mask = X < center[0] - radius
        inside_bubble = np.exp(- (R / radius)**6)
        field[front_mask] = np.sin(2 * np.pi * f * t + phase_front)
        field[back_mask] = np.sin(2 * np.pi * f * t + phase_back)
        field *= (1 - inside_bubble)
    return field

def energy_density(field, dx):
    """
    Lokale (normierte) Energiedichte: |Gradient(field)|^2
    """
    grad_x, grad_y = np.gradient(field, dx)
    E = grad_x**2 + grad_y**2
    return E / np.max(E)

def update_plot(val):
    """
    Update-Funktion für Slider-Interaktion.
    """
    global t, f, radius, n_bubbles, motion_ampl
    f = f_slider.val * 1e9
    radius = radius_slider.val
    n_bubbles = int(n_bubbles_slider.val)
    motion_ampl = motion_slider.val
    t = 0.0

    field = warp_field(t, bubble_centers(t, n_bubbles, motion_ampl), radius, f)
    surf[0].remove()
    if energy_map:
        E = energy_density(field, x[1] - x[0])
        surf[0] = ax.plot_surface(X, Y, E, cmap='inferno', edgecolor='none')
        ax.set_zlabel('Energiedichte')
    else:
        surf[0] = ax.plot_surface(X, Y, field, cmap='RdBu', edgecolor='none', vmin=-1, vmax=1)
        ax.set_zlabel('Feld')
    fig.canvas.draw_idle()

def animate(frame):
    """
    Animation für t > 0
    """
    global t
    t += dt
    centers = bubble_centers(t, n_bubbles, motion_ampl)
    field = warp_field(t, centers, radius, f)
    surf[0].remove()
    if energy_map:
        E = energy_density(field, x[1] - x[0])
        surf[0] = ax.plot_surface(X, Y, E, cmap='inferno', edgecolor='none')
    else:
        surf[0] = ax.plot_surface(X, Y, field, cmap='RdBu', edgecolor='none', vmin=-1, vmax=1)
    return surf

def reset(event):
    update_plot(None)

# --- Plot Setup ---
fig = plt.figure(figsize=(9, 7))
ax = fig.add_subplot(111, projection='3d')

# Mausinteraktivität aktivieren (3D-Drehung)
ax.mouse_init()

t = t0
centers = bubble_centers(t, n_bubbles, motion_ampl)
field = warp_field(t, centers, radius, f)
if energy_map:
    E = energy_density(field, x[1] - x[0])
    surf = [ax.plot_surface(X, Y, E, cmap='inferno', edgecolor='none')]
    ax.set_zlabel('Energiedichte')
else:
    surf = [ax.plot_surface(X, Y, field, cmap='RdBu', edgecolor='none', vmin=-1, vmax=1)]
    ax.set_zlabel('Feld')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title("Warp-Blasen im Raumresonanzfeld (3D, Interaktiv, Energie)")

plt.subplots_adjust(left=0.12, right=0.95, bottom=0.23, top=0.92)

# --- Slider für Interaktivität ---
axcolor = 'lightgoldenrodyellow'
ax_f = plt.axes([0.12, 0.13, 0.32, 0.03], facecolor=axcolor)
ax_radius = plt.axes([0.12, 0.09, 0.32, 0.03], facecolor=axcolor)
ax_n_bubbles = plt.axes([0.12, 0.05, 0.32, 0.03], facecolor=axcolor)
ax_motion = plt.axes([0.60, 0.13, 0.32, 0.03], facecolor=axcolor)
ax_reset = plt.axes([0.60, 0.07, 0.1, 0.04])

f_slider = Slider(ax_f, 'Frequenz [GHz]', 10, 400, valinit=f_default / 1e9, valfmt='%1.0f')
radius_slider = Slider(ax_radius, 'Radius', 0.5, 3.5, valinit=radius_default, valfmt='%1.2f')
n_bubbles_slider = Slider(ax_n_bubbles, 'Blasenanzahl', 1, 5, valinit=n_bubbles_default, valstep=1)
motion_slider = Slider(ax_motion, 'Bewegung', 0.0, 2.0, valinit=motion_ampl_default, valfmt='%1.2f')
button_reset = Button(ax_reset, 'Reset', color='w', hovercolor='0.85')

f_slider.on_changed(update_plot)
radius_slider.on_changed(update_plot)
n_bubbles_slider.on_changed(update_plot)
motion_slider.on_changed(update_plot)
button_reset.on_clicked(reset)

ani = animation.FuncAnimation(fig, animate, frames=300, interval=50, blit=False)

plt.show()