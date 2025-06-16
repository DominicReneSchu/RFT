import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D

# Parameter für das Doppelpendel
m1 = 1.0  # Masse des ersten Pendels
m2 = 1.0  # Masse des zweiten Pendels
L1 = 1.0  # Länge des ersten Pendels
L2 = 1.0  # Länge des zweiten Pendels
g = 9.81  # Erdbeschleunigung

# Anfangsbedingungen
theta1_0 = np.pi / 2  # Anfangswinkel des ersten Pendels (90 Grad)
theta2_0 = np.pi / 2  # Anfangswinkel des zweiten Pendels (90 Grad)
omega1_0 = 0.0  # Anfangsgeschwindigkeit des ersten Pendels
omega2_0 = 0.0  # Anfangsgeschwindigkeit des zweiten Pendels

# Differentialgleichung für das Doppelpendel
def equations(Y, t, m1, m2, L1, L2, g):
    theta1, theta2, omega1, omega2 = Y
    delta_theta = theta2 - theta1
    
    # Berechnungen der Beschleunigungen
    dtheta1_dt = omega1
    dtheta2_dt = omega2
    
    denominator1 = (m1 + m2) * L1 - m2 * L1 * np.cos(delta_theta) ** 2
    denominator2 = (L2 / L1) * denominator1
    
    # Winkelbeschleunigungen
    d2theta1_dt2 = (-m2 * L2 * omega2 ** 2 * np.sin(delta_theta) * np.cos(delta_theta) 
                    + m2 * g * np.sin(theta2) * np.cos(delta_theta) 
                    + m2 * L2 * omega2 ** 2 * np.sin(delta_theta) 
                    - (m1 + m2) * g * np.sin(theta1)) / denominator1

    d2theta2_dt2 = (m2 * L2 * omega2 ** 2 * np.sin(delta_theta) * np.cos(delta_theta) 
                    + (m1 + m2) * g * np.sin(theta1) * np.cos(delta_theta) 
                    - (m1 + m2) * L1 * omega1 ** 2 * np.sin(delta_theta) 
                    - (m1 + m2) * g * np.sin(theta2)) / denominator2
    
    return [dtheta1_dt, dtheta2_dt, d2theta1_dt2, d2theta2_dt2]

# Zeitspanne für die Simulation
t = np.linspace(0, 10, 1000)

# Anfangswerte
initial_conditions = [theta1_0, theta2_0, omega1_0, omega2_0]

# Numerische Lösung der Differentialgleichung
solution = odeint(equations, initial_conditions, t, args=(m1, m2, L1, L2, g))

# Extrahiere die Winkel und Geschwindigkeiten
theta1 = solution[:, 0]
theta2 = solution[:, 1]

# Berechnung der Positionen der Pendel
x1 = L1 * np.sin(theta1)
y1 = -L1 * np.cos(theta1)
x2 = x1 + L2 * np.sin(theta2)
y2 = y1 - L2 * np.cos(theta2)

# Resonanzfunktionen
A1 = 2
A2 = 2
ω1 = 1
ω2 = 1
σ = 1
μ = 0

x_resonance = A1 * np.sin(ω1 * t)
y_resonance = A2 * np.sin(ω2 * t)
g_t = np.exp(-((t - μ) ** 2) / (2 * σ ** 2))

z_resonance = g_t * (x_resonance + y_resonance) / (1 + np.abs(t - μ))

# 3D-Plot
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')

# Doppelpendelbewegung
ax.plot(x2, y2, z_resonance, label="Doppelpendel + Resonanz", color="b")

# Achsenbeschriftungen
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z (Resonanz)')

ax.set_title("Doppelpendel mit Resonanzfeld")
ax.legend()

# Zeige die 3D-Animation
plt.show()
