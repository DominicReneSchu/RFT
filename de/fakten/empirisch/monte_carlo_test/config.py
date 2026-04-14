"""
Zentrale Parameter fuer die Monte-Carlo-Resonanzanalyse.
PUBLIKATIONSVERSION — erweitert gegenueber Standardlauf.

Aenderungen:
  - N_SIMULATIONS: 10000 -> 50000 (staerkere empirische p-Werte)
  - N_BOOTSTRAP: 5000 -> 10000
  - Fuenfte Resonanz: phi(1020) bei 1.020 GeV
  - KDE_BANDWIDTH_VARIATIONS fuer Systematik-Check
  - RANDOM_SEEDS fuer Reproduzierbarkeit ueber 10 unabhaengige Laeufe

M0_VALUES: Resonanzmassenstellen (in GeV) im Dielectron-Kanal.
           - phi:      ~1.020 GeV (schmal, Gamma ~ 4.3 MeV)
           - J/psi:    ~3.1 GeV   (schmal, sigma ~ 0.05 GeV)
           - Upsilon(1S): ~9.46 GeV  (schmal, sigma ~ 0.1 GeV)
           - Upsilon(2S): ~10.02 GeV (schmal, sigma ~ 0.1 GeV)
           - Z-Boson:  ~91.2 GeV  (breit, Gamma ~ 2.5 GeV)

SIGNAL_EXCLUSION_WIDTH: Halbe Breite (GeV) fuer Signalausschluss
           beim KDE-Training. Soll nur den schmalen Peak entfernen,
           NICHT das gesamte Suchfenster.

DELTAS:    Fensterbreiten (halbe Breite) um jede Massenstelle.

N_SIMULATIONS:  Anzahl der Monte-Carlo-Pseudo-Experimente.
N_BOOTSTRAP:    Anzahl der Bootstrap-Wiederholungen.
HIST_BINS:      Anzahl der Bins fuer Histogramme.
KDE_BANDWIDTH:  Bandbreite fuer den Kernel-Density-Estimator.
"""

from __future__ import annotations

# Resonanzmassenstellen M0 (in GeV) — erweitert um phi(1020)
M0_VALUES = [1.020, 3.1, 9.46, 10.02, 91.2]

# Schmale Ausschlussbreite fuer KDE-Hintergrund-Training
# Nur der Kernbereich der Resonanz wird entfernt
SIGNAL_EXCLUSION_WIDTH = {
    1.020: 0.010,  # phi(1020): +-10 MeV (Gamma = 4.3 MeV)
    3.1: 0.15,     # J/psi: +-150 MeV
    9.46: 0.20,    # Upsilon(1S): +-200 MeV
    10.02: 0.20,   # Upsilon(2S): +-200 MeV
    91.2: 4.0,     # Z-Boson: +-4 GeV (Gamma_Z ~ 2.5 GeV)
}

# Fensterbreiten (halbe Breite, in GeV)
DELTAS = [0.02 * i for i in range(1, 51)] + [1.0 + 0.5 * i for i in range(1, 19)]

# Simulationsparameter — Publikationsversion
N_SIMULATIONS = 50000
N_BOOTSTRAP = 10000
HIST_BINS = 100
KDE_BANDWIDTH = 0.5

# Systematik-Check: KDE-Bandbreiten-Variation
KDE_BANDWIDTH_VARIATIONS = [0.3, 0.5, 0.7]

# Reproduzierbarkeit: 10 unabhaengige Seeds
RANDOM_SEEDS = [42, 137, 256, 314, 577, 691, 823, 947, 1024, 1337]