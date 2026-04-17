from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parameters
A1 = 2  # Amplitude of x(t)
A2 = 2  # Amplitude of y(t)
omega1 = 1  # Frequency of x(t)
omega2 = 1  # Frequency of y(t)
sigma = 1  # Width of damping
mu = 5  # Centre of damping

# Time range
t = np.linspace(-10, 10, 1000)

# Functions
x_t = A1 * np.sin(omega1 * t)
y_t = A2 * np.sin(omega2 * t)
g_t = np.exp(-((t - mu) ** 2) / (2 * sigma ** 2))

# Function z(t)
z_t = g_t * (x_t + y_t) / (1 + np.abs(t - mu))

# 3D plot of the curve
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(t, x_t, z_t, label='x(t) and z(t)')
ax.plot(t, y_t, z_t, label='y(t) and z(t)')

ax.set_xlabel('Time (t)')
ax.set_ylabel('x(t) and y(t)')
ax.set_zlabel('z(t)')
plt.title('3D Representation of Functions x(t), y(t) and z(t)')

plt.legend()
plt.show()
