import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Parameter für das Doppelpendel
m1 = 1.0  # Masse des ersten Pendels
m2 = 1.0  # Masse des zweiten Pendels
l1 = 1.0  # Länge des ersten Pendels
l2 = 1.0  # Länge des zweiten Pendels
g = 9.81  # Gravitationskonstante

# Gleichungen für das Doppelpendel
def equations(t, state):
    θ1, θ2, ω1, ω2 = state
    Δθ = θ2 - θ1
    denom1 = (m1 + m2) * l1 - m2 * l1 * np.cos(Δθ)**2
    denom2 = (l2 / l1) * denom1

    dω1_dt = (m2 * l2 * ω2**2 * np.sin(Δθ) * np.cos(Δθ)
              + m2 * g * np.sin(θ2) * np.cos(Δθ)
              + m2 * l2 * np.sin(Δθ) * ω2**2
              - (m1 + m2) * g * np.sin(θ1)) / denom1

    dω2_dt = (- m2 * l2 * ω2**2 * np.sin(Δθ) * np.cos(Δθ)
              + (m1 + m2) * g * np.sin(θ1) * np.cos(Δθ)
              - (m1 + m2) * l1 * ω1**2 * np.sin(Δθ)
              - (m1 + m2) * g * np.sin(θ2)) / denom2

    return [ω1, ω2, dω1_dt, dω2_dt]

# Initialbedingungen: [θ1, θ2, ω1, ω2]
initial_state = [np.pi / 2, np.pi / 2, 0, 0]

# Zeitspanne für die Simulation
t_span = (0, 20)
t_eval = np.linspace(0, 20, 500)

# Lösung der Differentialgleichungen
sol = solve_ivp(equations, t_span, initial_state, t_eval=t_eval)

# Berechnung der Positionen der Pendel
x1 = l1 * np.sin(sol.y[0])
y1 = -l1 * np.cos(sol.y[0])

x2 = x1 + l2 * np.sin(sol.y[1])
y2 = y1 - l2 * np.cos(sol.y[1])

# Erstellen der interaktiven Plot-Anzeige
def plot_doppelpendel():
    fig, ax = plt.subplots(figsize=(6, 5), dpi=100)
    ax.plot(x1, y1, label="Pendulum 1", color="b")
    ax.plot(x2, y2, label="Pendulum 2", color="r")
    ax.set_title("Doppelpendel-Simulation")
    ax.set_xlabel("X Position")
    ax.set_ylabel("Y Position")
    ax.legend()
    ax.set_aspect('equal')
    ax.set_xlim([-2, 2])
    ax.set_ylim([-2, 2])

    return fig

# Tkinter GUI-Fenster erstellen
root = tk.Tk()
root.title("Doppelpendel-Simulation")

# Canvas für den Matplotlib-Plot in Tkinter integrieren
canvas_frame = tk.Frame(root)
canvas_frame.grid(row=0, column=0, padx=10, pady=10)

# Plot der Doppelpendel-Simulation
fig = plot_doppelpendel()

# Canvas erstellen und Plot anzeigen
canvas = FigureCanvasTkAgg(fig, master=canvas_frame)
canvas.draw()
canvas.get_tk_widget().pack()

# Tkinter GUI starten
root.mainloop()
