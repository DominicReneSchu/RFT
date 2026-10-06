"""
Central parameters for the Monte Carlo resonance analysis.
PUBLICATION VERSION — extended compared to the standard run.

Changes:
  - N_SIMULATIONS: 10000 -> 50000 (stronger empirical p-values)
  - N_BOOTSTRAP: 5000 -> 10000
  - Fifth resonance: phi(1020) at 1.020 GeV
  - KDE_BANDWIDTH_VARIATIONS for systematic check
  - RANDOM_SEEDS for reproducibility over 10 independent runs

M0_VALUES: Resonance mass points (in GeV) in the dielectron channel.
           - phi:      ~1.020 GeV (narrow, Gamma ~ 4.3 MeV)
           - J/psi:    ~3.1 GeV   (narrow, sigma ~ 0.05 GeV)
           - Upsilon(1S): ~9.46 GeV  (narrow, sigma ~ 0.1 GeV)
           - Upsilon(2S): ~10.02 GeV (narrow, sigma ~ 0.1 GeV)
           - Z boson:  ~91.2 GeV  (broad, Gamma ~ 2.5 GeV)

SIGNAL_EXCLUSION_WIDTH: Half-width (GeV) for signal exclusion
           during KDE training. Should only remove the narrow peak,
           NOT the entire search window.

DELTAS:    Window half-widths around each mass point.

N_SIMULATIONS:  Number of Monte Carlo pseudo-experiments.
N_BOOTSTRAP:    Number of bootstrap repetitions.
HIST_BINS:      Number of bins for histograms.
KDE_BANDWIDTH:  Bandwidth for the Kernel Density Estimator.
"""

from __future__ import annotations

# Resonance mass points M0 (in GeV) — extended to include phi(1020)
M0_VALUES = [1.020, 3.1, 9.46, 10.02, 91.2]

# Narrow exclusion width for KDE background training
# Only the core region of the resonance is removed
SIGNAL_EXCLUSION_WIDTH = {
    1.020: 0.010,  # phi(1020): +-10 MeV (Gamma = 4.3 MeV)
    3.1: 0.15,     # J/psi: +-150 MeV
    9.46: 0.20,    # Upsilon(1S): +-200 MeV
    10.02: 0.20,   # Upsilon(2S): +-200 MeV
    91.2: 4.0,     # Z boson: +-4 GeV (Gamma_Z ~ 2.5 GeV)
}

# Window half-widths (in GeV)
DELTAS = [0.02 * i for i in range(1, 51)] + [1.0 + 0.5 * i for i in range(1, 19)]

# Simulation parameters — publication version
N_SIMULATIONS = 50000
N_BOOTSTRAP = 10000
HIST_BINS = 100
KDE_BANDWIDTH = 0.5

# Systematic check: KDE bandwidth variation
KDE_BANDWIDTH_VARIATIONS = [0.3, 0.5, 0.7]

# Reproducibility: 10 independent seeds
RANDOM_SEEDS = [42, 137, 256, 314, 577, 691, 823, 947, 1024, 1337]
