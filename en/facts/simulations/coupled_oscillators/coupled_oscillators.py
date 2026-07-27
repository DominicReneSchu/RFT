"""
Coupled Oscillators — Minimal Example

Standalone script for quick verification of the ODE solution
without interactive sliders. Uses fixed parameters.

Usage: python coupled_oscillators.py
"""

from __future__ import annotations

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from parameters_and_functions import kopplungsoperator

# Parameters
m = 1.0
f1, f2 = 1.0, 1.02
omega1, omega2 = 2 * np.pi * f1, 2 * np.pi * f2
alpha = 3.0
eps = kopplungsoperator(f1, f2, alpha)

def coupled_oscillators(t: float, y: list[float]) -> list[float]:
    x1, v1, x2, v2 = y
    k = eps
    dx1dt = v1
    dv1dt = -omega1**2 * x1 + (k / m) * (x2 - x1)
    dx2dt = v2
    dv2dt = -omega2**2 * x2 + (k / m) * (x1 - x2)
    return [dx1dt, dv1dt, dx2dt, dv2dt]

# Solution
y0 = [1.0, 0.0, 0.0, 0.0]
t_span = (0, 50)
t_eval = np.linspace(*t_span, 3000)
sol = solve_ivp(coupled_oscillators, t_span, y0, t_eval=t_eval)

# Plot
plt.figure(figsize=(10, 5))
plt.plot(sol.t, sol.y[0], label=f'x₁ (f₁ = {f1} Hz)')
plt.plot(sol.t, sol.y[2], label=f'x₂ (f₂ = {f2} Hz)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()
plt.title(f'Coupled Oscillators (ε = {eps:.4f}, α = {alpha})')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
