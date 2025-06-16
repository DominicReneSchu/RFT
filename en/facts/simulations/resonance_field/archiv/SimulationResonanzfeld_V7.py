import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Konstanten
g = 9.81  # Erdbeschleunigung
l1 = 1.0  # Länge des ersten Pendels
l2 = 1.0  # Länge des zweiten Pendels
m1 = 1.0  # Masse des ersten Pendels
m2 = 1.0  # Masse des zweiten Pendels

# Differentialgleichungen für das Doppelpendel
def derivatives(t, state):
    theta1, z1, theta2, z2 = state
    delta_theta = theta2 - theta1
    den1 = (m1 + m2) * l1 - m2 * l1 * np.cos(delta_theta) ** 2
    den2 = (l2 / l1) * den1

    dz1 = ((m2 * l2 * z2 ** 2 * np.sin(delta_theta) * np.cos(delta_theta)
            + m2 * g * np.sin(theta2) * np.cos(delta_theta)
            + m2 * l2 * z2 ** 2 * np.sin(delta_theta)
            - (m1 + m2) * g * np.sin(theta1))
           / den1)
    
    dz2 = ((- m2 * l1 * z1 ** 2 * np.sin(delta_theta) * np.cos(delta_theta)
            + (m1 + m2) * g * np.sin(theta1) * np.cos(delta_theta)
            - (m1 + m2) * l1 * z1 ** 2 * np.sin(delta_theta)
            - (m1 + m2) * g * np.sin(theta2))
           / den2)

    return [z1, dz1, z2, dz2]

# Anfangswerte
theta1_init = np.pi / 2
theta2_init = np.pi / 2
z1_init = 0.0
z2_init = 0.0
state_init = [theta1_init, z1_init, theta2_init, z2_init]

# Zeitspanne für die Simulation
t_span = (0, 10)
t_eval = np.linspace(0, 10, 200)  # Weniger Punkte für weniger Rechenaufwand

# Berechnungen
sol = solve_ivp(derivatives, t_span, state_init, t_eval=t_eval)

# Setzen des Fensters und der Achsen
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

# Berechne die Positionen der Pendel
x1 = l1 * np.sin(sol.y[0])
y1 = -l1 * np.cos(sol.y[0])
x2 = l2 * np.sin(sol.y[2]) + x1
y2 = -l2 * np.cos(sol.y[2]) + y1

# Erstelle die Linien für das Pendel
line1, = ax.plot([], [], lw=2, label='Pendulum 1')
line2, = ax.plot([], [], lw=2, label='Pendulum 2')

# Funktion zur Aktualisierung der Animation
def update_plot(frame):
    line1.set_data(x1[:frame], y1[:frame])
    line2.set_data(x2[:frame], y2[:frame])
    return line1, line2

# Animation durchführen
from matplotlib.animation import FuncAnimation
ani = FuncAnimation(fig, update_plot, frames=len(t_eval), interval=50, blit=True)

plt.show()
