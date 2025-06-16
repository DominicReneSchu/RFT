import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import interp1d

# --- Schu-Konstanten ---
PI = np.pi
h = 1.0  # Planck-Konstante (Skalierungsfaktor, anpassbar)
alpha = 3.0  # Schärfeparameter für Kopplungsoperator (per Slider modifizierbar)

def schu_koppler(f1, f2, alpha=alpha):
    """Dynamischer Kopplungsoperator nach Resonanzfeldtheorie."""
    return np.exp(-alpha * np.abs(f1 - f2))

def schu_energie(f, schu_e=1.0, h=h):
    """Resonanzfeld-Gleichung: E = pi * schu_e * h * f"""
    return PI * schu_e * h * f

def compute_frequencies(t, x, window=500, dt=None):
    """Schätzt die momentane Eigenfrequenz über einen Gleitfenster-Fourier-Ansatz."""
    if dt is None:
        dt = t[1] - t[0]
    n = len(x)
    if n < window:
        window = n
    xw = x[-window:]
    tw = t[-window:]
    xw = xw - np.mean(xw)
    fft = np.fft.rfft(xw)
    freqs = np.fft.rfftfreq(window, dt)
    idx = np.argmax(np.abs(fft[1:])) + 1  # Max. außer DC
    return freqs[idx]

def coupled_oscillators(t, y, omega1, omega2, get_k, m):
    x1, v1, x2, v2 = y
    # Frequenzbestimmung für dynamischen Koppler
    f1 = omega1 / (2 * np.pi)
    f2 = omega2 / (2 * np.pi)
    k_dyn = get_k(f1, f2)
    dx1dt = v1
    dv1dt = -omega1**2 * x1 + (k_dyn / m) * (x2 - x1)
    dx2dt = v2
    dv2dt = -omega2**2 * x2 + (k_dyn / m) * (x1 - x2)
    return [dx1dt, dv1dt, dx2dt, dv2dt]

def solve_coupled_oscillators(t_grid, omega1, omega2, schu_alpha, schu_h, y0=None, m=1.0):
    if y0 is None:
        y0 = [1.0, 0.0, 0.0, 0.0]
    get_k = lambda f1, f2: schu_koppler(f1, f2, schu_alpha)
    def ode(t, y):
        # Frequenzen instantan aus aktuellen Zuständen schätzen
        # Hier vereinfachend: konstante Eigenfrequenz (siehe Bonus für fortgeschrittene Methode)
        return coupled_oscillators(t, y, omega1, omega2, get_k, m)
    sol = solve_ivp(
        ode,
        (t_grid[0], t_grid[-1]), y0, t_eval=t_grid,
        rtol=1e-8, atol=1e-10
    )
    return sol.t, sol.y[0], sol.y[1], sol.y[2], sol.y[3]

def make_interpolators(t, x1, v1, x2, v2):
    x1i = interp1d(t, x1, kind='cubic', bounds_error=False, fill_value="extrapolate")
    v1i = interp1d(t, v1, kind='cubic', bounds_error=False, fill_value="extrapolate")
    x2i = interp1d(t, x2, kind='cubic', bounds_error=False, fill_value="extrapolate")
    v2i = interp1d(t, v2, kind='cubic', bounds_error=False, fill_value="extrapolate")
    return x1i, v1i, x2i, v2i

def resonance_condition(x1, x2, tolerance=0.1):
    return np.abs(x1 - x2) < tolerance

def compute_energies(x1, v1, x2, v2, omega1, omega2, schu_alpha, schu_h, m=1.0):
    # Frequenzschätzung für dynamischen Koppler
    dt = 1 if len(x1) < 2 else (1 / (len(x1) - 1))
    f1 = omega1 / (2 * np.pi)
    f2 = omega2 / (2 * np.pi)
    schu_e = schu_koppler(f1, f2, schu_alpha)
    k = schu_e
    # Kinetische Energie
    T = 0.5 * m * v1**2 + 0.5 * m * v2**2
    # Potentielle Energie beider Federn
    V1 = 0.5 * m * omega1**2 * x1**2
    V2 = 0.5 * m * omega2**2 * x2**2
    # Kopplungsenergie (dynamisch)
    Vc = 0.5 * k * (x1 - x2)**2
    # Gesamtenergie
    E = T + V1 + V2 + Vc
    # Schu-Energie nach Theorie
    E_schu1 = schu_energie(f1, schu_e, schu_h)
    E_schu2 = schu_energie(f2, schu_e, schu_h)
    # Resonanz-Divergenz
    resonanz_div = np.abs(E - (E_schu1 + E_schu2))
    return T, V1, V2, Vc, E, schu_e, E_schu1, E_schu2, resonanz_div