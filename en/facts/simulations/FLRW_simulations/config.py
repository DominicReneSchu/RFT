"""
Central configuration module for the resonance field framework.
PUBLICATION VERSION — extended relative to standard configuration.

Changes:
  - t_span_coupled: 40 -> 120 (3x longer integration)
  - steps_coupled: 4000 -> 12000 (proportional)
  - t_span_h0_scan: 60 -> 120
  - N_H0_POINTS: 21 -> 51 (extended range 0-100)
  - N_PHASE_POINTS: 15 -> 30 (finer cos^2 resolution)
  - Jackknife and bootstrap parameters
  - H0_EXTENDED_RANGE: 0-100 km/s/Mpc

Axiom reference:
    - A1: Oscillation parameters (m, potential)
    - A4: Coupling parameters (alpha, kappa, g)
"""

# Model parameters (default values)
MODEL_PARAMS = {
    "m": 1.0,           # Mass of the scalar field
    "lmbda": 0.1,       # Self-coupling constant (lambda*eps^4)
    "alpha": 0.5,       # Non-minimal coupling to spacetime
    "kappa": 1.0,       # Gravitational coupling (kappa = 8*pi*G)
    "g": 0.2,           # Field-field coupling (g*eps1*eps2)
}

# Initial conditions (1D FLRW) — stabilised
INITIAL_CONDITIONS = {
    "eps0": 0.3,         # eps(0)
    "epsdot0": 0.0,      # d_eps/dt(0)
    "a0": 1.0,           # Scale factor a(0)
    "adot0": 0.3,        # da/dt(0)
}

# Numerical parameters — PUBLICATION VERSION
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

# H0 scan parameters — PUBLICATION VERSION
H0_SCAN_PARAMS = {
    "h0_min": 0.0,           # Extended: 60 -> 0
    "h0_max": 100.0,         # Extended: 80 -> 100
    "n_h0_points": 51,       # 21 -> 51
    "n_phase_points": 30,    # 15 -> 30
    "n_jackknife": 30,       # Jackknife groups for error estimation
    "n_bootstrap_phase": 1000,  # Bootstrap over phase groups
}

# Visualisation options
VIS_PARAMS = {
    "colormap": "RdBu",
    "vmin": -1,
    "vmax": 1,
    "slice_idx": None,
    "update_interval": 10,
}

# GPU options (for CuPy)
USE_CUDA = False

# ---------------------------------------------------------------------------
# Planck-2018 SI parameters (arXiv:1807.06209)
# ---------------------------------------------------------------------------
PLANCK_2018 = {
    "H0": 67.36,            # Hubble constant [km/s/Mpc]
    "H0_err": 0.54,         # 1σ uncertainty
    "Omega_m": 0.3153,      # Matter density parameter
    "Omega_r": 9.14e-5,     # Radiation density parameter
    "Omega_Lambda": 0.6847, # Λ density parameter
    "Omega_b_h2": 0.02237,  # Baryon density × h²
    "Omega_c_h2": 0.1200,   # CDM density × h²
    "tau": 0.0544,          # Optical depth
    "As": 2.1e-9,           # Primordial amplitude
    "ns": 0.9649,           # Spectral index
    # SH0ES reference (Riess et al. 2022, arXiv:2112.04510)
    "H0_SH0ES": 73.04,      # [km/s/Mpc]
    "H0_SH0ES_err": 1.04,   # 1σ uncertainty
}
