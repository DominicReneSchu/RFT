# Zentrales Konfigurationsmodul für das Resonanzfeld-Framework

# Modellparameter (Standardwerte)
MODEL_PARAMS = {
    "m": 1.0,
    "lmbda": 0.1,
    "alpha": 0.5,
    "kappa": 1.0,
}

# Numerische Parameter
NUMERIC_PARAMS = {
    "rtol": 1e-8,
    "atol": 1e-10,
    "steps_1d": 2000,
    "steps_3d": 300,
    "grid_3d": 64,
    "dt_3d": 0.004,
}

# Visualisierungsoptionen
VIS_PARAMS = {
    "colormap": "RdBu",
    "vmin": -1,
    "vmax": 1,
    "slice_idx": None,  # Default: Mitte
}

# GPU-Optionen (für CuPy)
USE_CUDA = False