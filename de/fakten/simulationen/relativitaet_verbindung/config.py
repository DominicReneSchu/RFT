"""
Zentrales Konfigurationsmodul für das Resonanzfeld-Framework.

Alle Standardparameter für Modell, Numerik und Visualisierung
sind hier definiert. Module importieren diese Werte als Defaults.

Axiom-Bezug:
    - A1: Schwingungsparameter (m, Potential)
    - A4: Kopplungsparameter (alpha, kappa)
"""

# Modellparameter (Standardwerte)
MODEL_PARAMS = {
    "m": 1.0,           # Masse des skalaren Felds
    "lmbda": 0.1,       # Selbstkopplungskonstante (λε⁴)
    "alpha": 0.5,       # Nichtminimale Kopplung an Raumzeit
    "kappa": 1.0,       # Gravitationskopplung (κ = 8πG)
}

# Anfangsbedingungen (1D FLRW) — stabilisiert
INITIAL_CONDITIONS = {
    "eps0": 0.3,         # ε(0)
    "epsdot0": 0.0,      # dε/dt(0)
    "a0": 1.0,           # Skalenfaktor a(0)
    "adot0": 0.3,        # da/dt(0) — stärkere Anfangsexpansion
}

# Numerische Parameter
NUMERIC_PARAMS = {
    "rtol": 1e-10,
    "atol": 1e-12,
    "t_span_1d": (0, 20),
    "steps_1d": 2000,
    "steps_3d": 300,
    "grid_3d": 64,
    "L_3d": 10.0,
    "dt_3d": 0.004,
}

# Visualisierungsoptionen
VIS_PARAMS = {
    "colormap": "RdBu",
    "vmin": -1,
    "vmax": 1,
    "slice_idx": None,   # Default: Mitte
    "update_interval": 10,
}

# GPU-Optionen (für CuPy)
USE_CUDA = False