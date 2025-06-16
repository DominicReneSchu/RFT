import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parameter
A1 = 2  # Amplitude von x(t)
A2 = 2  # Amplitude von y(t)
omega1 = 1  # Frequenz von x(t)
omega2 = 1  # Frequenz von y(t)
sigma = 1  # Breite der Dämpfung
mu = 5  # Zentrum der Dämpfung

# Zeitbereich
t = np.linspace(-10, 10, 1000)

# Funktionen
x_t = A1 * np.sin(omega1 * t)
y_t = A2 * np.sin(omega2 * t)
g_t = np.exp(-((t - mu) ** 2) / (2 * sigma ** 2))

# Funktion z(t)
z_t = g_t * (x_t + y_t) / (1 + np.abs(t - mu))

# 3D-Plot der Kurve
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(t, x_t, z_t, label='x(t) und z(t)')
ax.plot(t, y_t, z_t, label='y(t) und z(t)')

ax.set_xlabel('Zeit (t)')
ax.set_ylabel('x(t) und y(t)')
ax.set_zlabel('z(t)')
plt.title('3D-Darstellung der Funktionen x(t), y(t) und z(t)')

plt.legend()
plt.show()
