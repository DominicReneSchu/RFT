from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Parameters for the double pendulum
m1 = 1.0  # Mass of the first pendulum
m2 = 1.0  # Mass of the second pendulum
L1 = 1.0  # Length of the first pendulum
L2 = 1.0  # Length of the second pendulum
g = 9.81  # Gravitational acceleration

# Initial conditions
theta1_0 = np.pi / 2  # Initial angle of the first pendulum (90 degrees)
theta2_0 = np.pi / 2  # Initial angle of the second pendulum (90 degrees)
omega1_0 = 0.0  # Initial angular velocity of the first pendulum
omega2_0 = 0.0  # Initial angular velocity of the second pendulum

# Differential equation for the double pendulum
def equations(Y: np.ndarray, t: float, m1: float, m2: float, L1: float, L2: float, g: float) -> list[float]:
    theta1, theta2, omega1, omega2 = Y
    delta_theta = theta2 - theta1
    
    # Calculation of accelerations
    dtheta1_dt = omega1
    dtheta2_dt = omega2
    
    denominator1 = (m1 + m2) * L1 - m2 * L1 * np.cos(delta_theta) ** 2
    denominator2 = (L2 / L1) * denominator1
    
    # Angular accelerations
    d2theta1_dt2 = (-m2 * L2 * omega2 ** 2 * np.sin(delta_theta) * np.cos(delta_theta) 
                    + m2 * g * np.sin(theta2) * np.cos(delta_theta) 
                    + m2 * L2 * omega2 ** 2 * np.sin(delta_theta) 
                    - (m1 + m2) * g * np.sin(theta1)) / denominator1

    d2theta2_dt2 = (m2 * L2 * omega2 ** 2 * np.sin(delta_theta) * np.cos(delta_theta) 
                    + (m1 + m2) * g * np.sin(theta1) * np.cos(delta_theta) 
                    - (m1 + m2) * L1 * omega1 ** 2 * np.sin(delta_theta) 
                    - (m1 + m2) * g * np.sin(theta2)) / denominator2
    
    return [dtheta1_dt, dtheta2_dt, d2theta1_dt2, d2theta2_dt2]

# Time span for the simulation
t = np.linspace(0, 10, 1000)

# Initial values
initial_conditions = [theta1_0, theta2_0, omega1_0, omega2_0]

# Numerical solution of the differential equation
solution = odeint(equations, initial_conditions, t, args=(m1, m2, L1, L2, g))

# Extract the angles and velocities
theta1 = solution[:, 0]
theta2 = solution[:, 1]

# Visualisation of the pendulum motion
fig, ax = plt.subplots(figsize=(8, 6))

# Positions of the pendulums
x1 = L1 * np.sin(theta1)
y1 = -L1 * np.cos(theta1)
x2 = x1 + L2 * np.sin(theta2)
y2 = y1 - L2 * np.cos(theta2)

ax.plot(x1, y1, label="First Pendulum", color='b')
ax.plot(x2, y2, label="Second Pendulum", color='r')
ax.set_title("Double Pendulum Motion")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()
ax.set_aspect('equal')
plt.show()
