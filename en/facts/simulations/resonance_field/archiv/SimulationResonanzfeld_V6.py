import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Gleichungen für das Doppelpendel
def equations(t, state, m1, m2, l1, l2, g):
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

# Funktion zur Simulation
def simulate(m1, m2, l1, l2, θ1, θ2):
    initial_state = [θ1, θ2, 0, 0]
    t_span = (0, 20)
    t_eval = np.linspace(0, 20, 500)
    g = 9.81  # Gravitationskonstante

    sol = solve_ivp(equations, t_span, initial_state, t_eval=t_eval, args=(m1, m2, l1, l2, g))
    
    x1 = l1 * np.sin(sol.y[0])
    y1 = -l1 * np.cos(sol.y[0])

    x2 = x1 + l2 * np.sin(sol.y[1])
    y2 = y1 - l2 * np.cos(sol.y[1])

    return x1, y1, x2, y2, sol.t

# Funktion zur Erstellung des Plots
def plot_doppelpendel(m1, m2, l1, l2, θ1, θ2):
    x1, y1, x2, y2, t = simulate(m1, m2, l1, l2, θ1, θ2)

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

# Funktion zur Aktualisierung des Plots
def update_plot():
    m1 = float(m1_slider.get())
    m2 = float(m2_slider.get())
    l1 = float(l1_slider.get())
    l2 = float(l2_slider.get())
    θ1 = float(θ1_slider.get())
    θ2 = float(θ2_slider.get())
    
    fig = plot_doppelpendel(m1, m2, l1, l2, θ1, θ2)
    
    for widget in canvas_frame.winfo_children():
        widget.destroy()

    canvas = FigureCanvasTkAgg(fig, master=canvas_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Tkinter GUI-Fenster erstellen
root = tk.Tk()
root.title("Doppelpendel-Simulation mit Schiebereglern")

# Canvas für den Matplotlib-Plot in Tkinter integrieren
canvas_frame = tk.Frame(root)
canvas_frame.grid(row=0, column=0, padx=10, pady=10)

# Schieberegler für die Parameter
m1_slider = tk.Scale(root, from_=0.1, to=5, orient="horizontal", length=300, label="Masse 1 (m1)", command=lambda e: update_plot())
m1_slider.set(1.0)

m2_slider = tk.Scale(root, from_=0.1, to=5, orient="horizontal", length=300, label="Masse 2 (m2)", command=lambda e: update_plot())
m2_slider.set(1.0)

l1_slider = tk.Scale(root, from_=0.1, to=2, orient="horizontal", length=300, label="Länge 1 (l1)", command=lambda e: update_plot())
l1_slider.set(1.0)

l2_slider = tk.Scale(root, from_=0.1, to=2, orient="horizontal", length=300, label="Länge 2 (l2)", command=lambda e: update_plot())
l2_slider.set(1.0)

θ1_slider = tk.Scale(root, from_=-np.pi, to=np.pi, orient="horizontal", length=300, label="Winkel 1 (θ1)", command=lambda e: update_plot())
θ1_slider.set(np.pi / 2)

θ2_slider = tk.Scale(root, from_=-np.pi, to=np.pi, orient="horizontal", length=300, label="Winkel 2 (θ2)", command=lambda e: update_plot())
θ2_slider.set(np.pi / 2)

# Platzierung der Schieberegler
m1_slider.grid(row=1, column=0, padx=10, pady=5)
m2_slider.grid(row=2, column=0, padx=10, pady=5)
l1_slider.grid(row=3, column=0, padx=10, pady=5)
l2_slider.grid(row=4, column=0, padx=10, pady=5)
θ1_slider.grid(row=5, column=0, padx=10, pady=5)
θ2_slider.grid(row=6, column=0, padx=10, pady=5)

# Starte mit dem ersten Plot
update_plot()

# Tkinter GUI starten
root.mainloop()
