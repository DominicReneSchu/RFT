import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

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

# Visualisierung der Pendelbewegung
fig, ax = plt.subplots(figsize=(8, 6))

# Positionen der Pendel
x1 = L1 * np.sin(theta1)
y1 = -L1 * np.cos(theta1)
x2 = x1 + L2 * np.sin(theta2)
y2 = y1 - L2 * np.cos(theta2)

ax.plot(x1, y1, label="Erstes Pendel", color='b')
ax.plot(x2, y2, label="Zweites Pendel", color='r')
ax.set_title("Doppelpendel Bewegung")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()
ax.set_aspect('equal')
plt.show()
