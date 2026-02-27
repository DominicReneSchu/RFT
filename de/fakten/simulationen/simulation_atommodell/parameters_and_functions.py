"""
Physik-Kern der gekoppelten Oszillatoren-Simulation.

Kopplungsoperator, Energieberechnung, ODE-Löser.
Basiert auf Axiomen A1–A4 der Resonanzfeldtheorie.

Abhängigkeiten: numpy, scipy
"""

import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import interp1d
from fractions import Fraction

PI = np.pi
H_DEFAULT = 1.0    # Planck-Konstante (normiert)
ALPHA_DEFAULT = 3.0 # Kopplungsschärfe (per Slider modifizierbar)


# --- Kopplungsoperator (Axiom 4) ---

def kopplungsoperator(f1, f2, alpha=ALPHA_DEFAULT):
    """Dynamischer Kopplungsoperator ε(f1, f2).

    Modelliert die frequenzabhängige Kopplungsstärke zwischen
    zwei Oszillatoren. Maximum bei f1 = f2 (perfekte Resonanz).

    ε = exp(-α · |f1 - f2|) ∈ (0, 1]
    """
    return np.exp(-alpha * np.abs(f1 - f2))


# --- Resonanzenergie (Axiom 4) ---

def resonanzenergie(f, eps=1.0, h=H_DEFAULT):
    """E = π · ε · h · f"""
    return PI * eps * h * f


# --- Resonanzbedingung (Axiom 3) ---

def check_frequency_resonance(f1, f2, tolerance=0.02):
    """Prüfe ob f1/f2 ≈ n/m mit n, m ∈ ℤ⁺."""
    if f2 == 0:
        return False, 0, 1
    ratio = Fraction(f1 / f2).limit_denominator(10)
    n, m = ratio.numerator, ratio.denominator
    is_resonant = np.isclose(f1 / f2, n / m, rtol=tolerance)
    return is_resonant, n, m


# --- Frequenzschätzung ---

def compute_frequencies(t, x, window=500, dt=None):
    """Momentane Eigenfrequenz über Gleitfenster-FFT."""
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


# --- ODE-System ---

def coupled_oscillators(t, y, omega1, omega2, get_k, m):
    """Gekoppelte harmonische Oszillatoren mit dynamischer Kopplung."""
    x1, v1, x2, v2 = y
    f1 = omega1 / (2 * PI)
    f2 = omega2 / (2 * PI)
    k_dyn = get_k(f1, f2)
    dx1dt = v1
    dv1dt = -omega1**2 * x1 + (k_dyn / m) * (x2 - x1)
    dx2dt = v2
    dv2dt = -omega2**2 * x2 + (k_dyn / m) * (x1 - x2)
    return [dx1dt, dv1dt, dx2dt, dv2dt]


def solve_coupled_oscillators(t_grid, omega1, omega2, alpha, h,
                              y0=None, m=1.0):
    """Löse gekoppeltes ODE-System mit dynamischem Kopplungsoperator."""
    if y0 is None:
        y0 = [1.0, 0.0, 0.0, 0.0]
    get_k = lambda f1, f2: kopplungsoperator(f1, f2, alpha)
    def ode(t, y):
        return coupled_oscillators(t, y, omega1, omega2, get_k, m)
    sol = solve_ivp(
        ode,
        (t_grid[0], t_grid[-1]), y0, t_eval=t_grid,
        rtol=1e-8, atol=1e-10
    )
    return sol.t, sol.y[0], sol.y[1], sol.y[2], sol.y[3]


def make_interpolators(t, x1, v1, x2, v2):
    """Kubische Interpolation für Animation."""
    x1i = interp1d(t, x1, kind='cubic', bounds_error=False,
                   fill_value="extrapolate")
    v1i = interp1d(t, v1, kind='cubic', bounds_error=False,
                   fill_value="extrapolate")
    x2i = interp1d(t, x2, kind='cubic', bounds_error=False,
                   fill_value="extrapolate")
    v2i = interp1d(t, v2, kind='cubic', bounds_error=False,
                   fill_value="extrapolate")
    return x1i, v1i, x2i, v2i


def resonance_condition(x1, x2, tolerance=0.1):
    """Positionsbasierte Resonanzerkennung."""
    return np.abs(x1 - x2) < tolerance


def compute_energies(x1, v1, x2, v2, omega1, omega2, alpha, h, m=1.0):
    """Berechne alle Energiekomponenten.

    Returns: T, V1, V2, Vc, E_total, eps, E_res1, E_res2, resonanz_div
    """
    f1 = omega1 / (2 * PI)
    f2 = omega2 / (2 * PI)
    eps = kopplungsoperator(f1, f2, alpha)
    k = eps

    # Kinetische Energie
    T = 0.5 * m * v1**2 + 0.5 * m * v2**2
    # Potentielle Energie
    V1 = 0.5 * m * omega1**2 * x1**2
    V2 = 0.5 * m * omega2**2 * x2**2
    # Kopplungsenergie
    Vc = 0.5 * k * (x1 - x2)**2
    # Gesamtenergie
    E = T + V1 + V2 + Vc

    # Resonanzenergie nach Axiom 4
    E_res1 = resonanzenergie(f1, eps, h)
    E_res2 = resonanzenergie(f2, eps, h)

    # Resonanz-Divergenz
    resonanz_div = np.abs(E - (E_res1 + E_res2))

    return T, V1, V2, Vc, E, eps, E_res1, E_res2, resonanz_div