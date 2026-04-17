"""
Physics core of the coupled oscillators simulation.

Coupling operator, energy calculation, ODE solver.
Based on Axioms A1–A4 of Resonance Field Theory.

Dependencies: numpy, scipy
"""

from __future__ import annotations

from collections.abc import Callable
from typing import Any

import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import interp1d
from fractions import Fraction

PI = np.pi
H_DEFAULT = 1.0    # Planck constant (normalised)
ALPHA_DEFAULT = 3.0 # Coupling sharpness (modifiable via slider)


# --- Coupling operator (Axiom 4) ---

def kopplungsoperator(f1: float, f2: float, alpha: float = ALPHA_DEFAULT) -> float | np.ndarray:
    """Dynamic coupling operator ε(f1, f2).

    Models the frequency-dependent coupling strength between
    two oscillators. Maximum at f1 = f2 (perfect resonance).

    ε = exp(-α · |f1 - f2|) ∈ (0, 1]
    """
    return np.exp(-alpha * np.abs(f1 - f2))


# --- Resonance energy (Axiom 4) ---

def resonanzenergie(f: float, eps: float = 1.0, h: float = H_DEFAULT) -> float:
    """E = π · ε · h · f"""
    return PI * eps * h * f


# --- Resonance condition (Axiom 3) ---

def check_frequency_resonance(f1: float, f2: float, tolerance: float = 0.02) -> tuple[bool, int, int]:
    """Check whether f1/f2 ≈ n/m with n, m ∈ ℤ⁺."""
    if f2 == 0:
        return False, 0, 1
    ratio = Fraction(f1 / f2).limit_denominator(10)
    n, m = ratio.numerator, ratio.denominator
    is_resonant = np.isclose(f1 / f2, n / m, rtol=tolerance)
    return is_resonant, n, m


# --- Frequency estimation ---

def compute_frequencies(t: np.ndarray, x: np.ndarray, window: int = 500, dt: float | None = None) -> float:
    """Instantaneous natural frequency via sliding-window FFT."""
    if dt is None:
        dt = t[1] - t[0]
    n = len(x)
    if n < window:
        window = n
    xw = x[-window:]
    xw = xw - np.mean(xw)
    fft = np.fft.rfft(xw)
    freqs = np.fft.rfftfreq(window, dt)
    idx = np.argmax(np.abs(fft[1:])) + 1
    return freqs[idx]


# --- ODE system ---

def coupled_oscillators(t: float, y: list[float], omega1: float, omega2: float, get_k: Callable[[float, float], float], m: float) -> list[float]:
    """Coupled harmonic oscillators with dynamic coupling."""
    x1, v1, x2, v2 = y
    f1 = omega1 / (2 * PI)
    f2 = omega2 / (2 * PI)
    k_dyn = get_k(f1, f2)
    dx1dt = v1
    dv1dt = -omega1**2 * x1 + (k_dyn / m) * (x2 - x1)
    dx2dt = v2
    dv2dt = -omega2**2 * x2 + (k_dyn / m) * (x1 - x2)
    return [dx1dt, dv1dt, dx2dt, dv2dt]


def solve_coupled_oscillators(t_grid: np.ndarray, omega1: float, omega2: float, alpha: float, h: float,
                              y0: list[float] | None = None, m: float = 1.0) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Solve coupled ODE system with dynamic coupling operator."""
    if y0 is None:
        y0 = [1.0, 0.0, 0.0, 0.0]
    get_k = lambda f1, f2: kopplungsoperator(f1, f2, alpha)
    def ode(t: float, y: list[float]) -> list[float]:
        return coupled_oscillators(t, y, omega1, omega2, get_k, m)
    sol = solve_ivp(
        ode,
        (t_grid[0], t_grid[-1]), y0, t_eval=t_grid,
        rtol=1e-8, atol=1e-10
    )
    return sol.t, sol.y[0], sol.y[1], sol.y[2], sol.y[3]


def make_interpolators(t: np.ndarray, x1: np.ndarray, v1: np.ndarray, x2: np.ndarray, v2: np.ndarray) -> tuple[Any, Any, Any, Any]:
    """Cubic interpolation for animation."""
    x1i = interp1d(t, x1, kind='cubic', bounds_error=False,
                   fill_value="extrapolate")
    v1i = interp1d(t, v1, kind='cubic', bounds_error=False,
                   fill_value="extrapolate")
    x2i = interp1d(t, x2, kind='cubic', bounds_error=False,
                   fill_value="extrapolate")
    v2i = interp1d(t, v2, kind='cubic', bounds_error=False,
                   fill_value="extrapolate")
    return x1i, v1i, x2i, v2i


def resonance_condition(x1: float | np.ndarray, x2: float | np.ndarray, tolerance: float = 0.1) -> bool | np.ndarray:
    """Position-based resonance detection."""
    return np.abs(x1 - x2) < tolerance


def compute_energies(x1: np.ndarray, v1: np.ndarray, x2: np.ndarray, v2: np.ndarray, omega1: float, omega2: float, alpha: float, h: float, m: float = 1.0) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray, float | np.ndarray, float, float, np.ndarray]:
    """Calculate all energy components.

    Returns: T, V1, V2, Vc, E_total, eps, E_res1, E_res2, resonance_div
    """
    f1 = omega1 / (2 * PI)
    f2 = omega2 / (2 * PI)
    eps = kopplungsoperator(f1, f2, alpha)
    k = eps

    # Kinetic energy
    T = 0.5 * m * v1**2 + 0.5 * m * v2**2
    # Potential energy
    V1 = 0.5 * m * omega1**2 * x1**2
    V2 = 0.5 * m * omega2**2 * x2**2
    # Coupling energy
    Vc = 0.5 * k * (x1 - x2)**2
    # Total energy
    E = T + V1 + V2 + Vc

    # Resonance energy according to Axiom 4
    E_res1 = resonanzenergie(f1, eps, h)
    E_res2 = resonanzenergie(f2, eps, h)

    # Resonance divergence
    resonanz_div = np.abs(E - (E_res1 + E_res2))

    return T, V1, V2, Vc, E, eps, E_res1, E_res2, resonanz_div
