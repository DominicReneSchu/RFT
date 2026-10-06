from __future__ import annotations

from typing import Any

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from matplotlib.widgets import Button, TextBox
from matplotlib.animation import FuncAnimation
import matplotlib

# Use an interactive Matplotlib backend
matplotlib.use('TkAgg')  # Choose TkAgg backend when not working in a notebook environment

# Constants
g = 9.81  # Gravitational acceleration

# Differential equations for the double pendulum
def derivatives(t: float, state: np.ndarray, l1: float, l2: float, m1: float, m2: float) -> list[float]:
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

# Calculate positions of the pendulums
def calculate_positions(l1: float, l2: float, m1: float, m2: float, theta1_init: float, theta2_init: float, z1_init: float, z2_init: float, t_span: tuple[float, float], t_eval: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    state_init = [theta1_init, z1_init, theta2_init, z2_init]
    sol = solve_ivp(derivatives, t_span, state_init, args=(l1, l2, m1, m2), t_eval=t_eval)
    x1 = l1 * np.sin(sol.y[0])
    y1 = -l1 * np.cos(sol.y[0])
    x2 = l2 * np.sin(sol.y[2]) + x1
    y2 = -l2 * np.cos(sol.y[2]) + y1
    return x1, y1, x2, y2

# Set window and axes
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

# Input fields and button
ax_l1 = plt.axes([0.1, 0.02, 0.04, 0.025])  
entry_l1 = TextBox(ax_l1, 'L1', initial="1.0")

ax_l2 = plt.axes([0.1, 0.06, 0.04, 0.025])  
entry_l2 = TextBox(ax_l2, 'L2', initial="1.0")

ax_m1 = plt.axes([0.1, 0.1, 0.04, 0.025])  
entry_m1 = TextBox(ax_m1, 'M1', initial="1.0")

ax_m2 = plt.axes([0.1, 0.14, 0.04, 0.025])  
entry_m2 = TextBox(ax_m2, 'M2', initial="1.0")

ax_theta1 = plt.axes([0.1, 0.18, 0.04, 0.025])  
entry_theta1 = TextBox(ax_theta1, 'Theta1', initial="1.57")  # π/2

ax_theta2 = plt.axes([0.1, 0.22, 0.04, 0.025])  
entry_theta2 = TextBox(ax_theta2, 'Theta2', initial="1.57")  # π/2

# Button to start the calculation
ax_button = plt.axes([0.1, 0.26, 0.15, 0.04])  
button = Button(ax_button, 'Start Simulation', color='lightgoldenrodyellow', hovercolor='yellow')

# Animation logic
def animate(i: int, l1: float, l2: float, m1: float, m2: float, theta1_init: float, theta2_init: float) -> tuple[Any, Any]:
    t_span = (0, 10)
    t_eval = np.linspace(0, 10, 200)

    # Calculate positions of the pendulums for the current time step i
    x1, y1, x2, y2 = calculate_positions(l1, l2, m1, m2, theta1_init, theta2_init, 0.0, 0.0, t_span, t_eval[:i])
    
    # Clear the previous display
    ax.clear()
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.plot(x1, y1, label='Pendulum 1', color='r')
    ax.plot(x2, y2, label='Pendulum 2', color='b')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.legend()
    return ax.plot(x1, y1, label='Pendulum 1'), ax.plot(x2, y2, label='Pendulum 2')

# Button event to start the animation
def on_button_click(event: Any) -> None:
    try:
        # Input values from the fields
        l1 = float(entry_l1.text)
        l2 = float(entry_l2.text)
        m1 = float(entry_m1.text)
        m2 = float(entry_m2.text)
        theta1_init = float(entry_theta1.text)
        theta2_init = float(entry_theta2.text)

        # Start animation and store in a variable
        ani = FuncAnimation(fig, animate, frames=200, fargs=(l1, l2, m1, m2, theta1_init, theta2_init), interval=50)
        plt.draw()

    except ValueError:
        print("Invalid input! Please enter valid numbers.")

button.on_clicked(on_button_click)

# Adjust layout
fig.subplots_adjust(left=0.2, bottom=0.4)

# Adjust plt.show() to avoid immediate problems
if __name__ == "__main__":
    plt.show()
