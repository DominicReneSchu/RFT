"""
Zentrales Konfigurationsmodul fuer das Resonanzfeld-Framework.
PUBLIKATIONSVERSION — erweitert gegenueber Standardkonfiguration.

Aenderungen:
  - t_span_coupled: 40 -> 120 (3x laengere Integration)
  - steps_coupled: 4000 -> 12000 (proportional)
  - t_span_h0_scan: 60 -> 120
  - N_H0_POINTS: 21 -> 51 (erweiterter Bereich 0-100)
  - N_PHASE_POINTS: 15 -> 30 (feinere cos^2-Aufloesung)
  - Jackknife- und Bootstrap-Parameter
  - H0_EXTENDED_RANGE: 0-100 km/s/Mpc

Axiom-Bezug:
    - A1: Schwingungsparameter (m, Potential)
    - A4: Kopplungsparameter (alpha, kappa, g)
"""

# Modellparameter (Standardwerte)
MODEL_PARAMS = {
    "m": 1.0,           # Masse des skalaren Felds
    "lmbda": 0.1,       # Selbstkopplungskonstante (lambda*eps^4)
    "alpha": 0.5,       # Nichtminimale Kopplung an Raumzeit
    "kappa": 1.0,       # Gravitationskopplung (kappa = 8*pi*G)
    "g": 0.2,           # Feld-Feld-Kopplung (g*eps1*eps2)
}

# Anfangsbedingungen (1D FLRW) — stabilisiert
INITIAL_CONDITIONS = {
    "eps0": 0.3,         # eps(0)
    "epsdot0": 0.0,      # d_eps/dt(0)
    "a0": 1.0,           # Skalenfaktor a(0)
    "adot0": 0.3,        # da/dt(0)
}

# Numerische Parameter — PUBLIKATIONSVERSION
NUMERIC_PARAMS = {
    "rtol": 1e-10,
    "atol": 1e-12,
    "t_span_1d": (0, 20),
    "t_span_coupled": (0, 120),       # 40 -> 120
    "t_span_h0_scan": (0, 120),       # 60 -> 120
    "steps_1d": 2000,
    "steps_coupled": 12000,            # 4000 -> 12000
    "steps_3d": 300,
    "grid_3d": 64,
    "L_3d": 10.0,
    "dt_3d": 0.004,
}

# H0-Scan-Parameter — PUBLIKATIONSVERSION
H0_SCAN_PARAMS = {
    "h0_min": 0.0,           # Erweitert: 60 -> 0
    "h0_max": 100.0,         # Erweitert: 80 -> 100
    "n_h0_points": 51,       # 21 -> 51
    "n_phase_points": 30,    # 15 -> 30
    "n_jackknife": 30,       # Jackknife-Gruppen fuer Fehlerabschaetzung
    "n_bootstrap_phase": 1000,  # Bootstrap ueber Phasengruppen
}

# Visualisierungsoptionen
VIS_PARAMS = {
    "colormap": "RdBu",
    "vmin": -1,
    "vmax": 1,
    "slice_idx": None,
    "update_interval": 10,
}

# GPU-Optionen (fuer CuPy)
USE_CUDA = False