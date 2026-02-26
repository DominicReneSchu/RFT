"""
Zentrale Parameter für die Monte-Carlo-Resonanzanalyse.

M0_VALUES: Resonanzmassenstellen (in GeV) im Dielectron-Kanal.
           - J/ψ:     ~3.1 GeV   (schmal, σ ≈ 0.05 GeV)
           - Υ(1S):   ~9.46 GeV  (schmal, σ ≈ 0.1 GeV)
           - Υ(2S):   ~10.02 GeV (schmal, σ ≈ 0.1 GeV)
           - Z-Boson:  ~91.2 GeV (breit, Γ ≈ 2.5 GeV)

SIGNAL_EXCLUSION_WIDTH: Halbe Breite (GeV) für Signalausschluss
           beim KDE-Training. Soll nur den schmalen Peak entfernen,
           NICHT das gesamte Suchfenster.

DELTAS:    Fensterbreiten (halbe Breite) um jede Massenstelle.

N_SIMULATIONS:  Anzahl der Monte-Carlo-Pseudo-Experimente.
N_BOOTSTRAP:    Anzahl der Bootstrap-Wiederholungen.
HIST_BINS:      Anzahl der Bins für Histogramme.
KDE_BANDWIDTH:  Bandbreite für den Kernel-Density-Estimator.
"""

# Resonanzmassenstellen M₀ (in GeV)
M0_VALUES = [3.1, 9.46, 10.02, 91.2]

# Schmale Ausschlussbreite für KDE-Hintergrund-Training
# Nur der Kernbereich der Resonanz wird entfernt
SIGNAL_EXCLUSION_WIDTH = {
    3.1: 0.15,     # J/ψ: ±150 MeV
    9.46: 0.20,    # Υ(1S): ±200 MeV
    10.02: 0.20,   # Υ(2S): ±200 MeV
    91.2: 4.0,     # Z-Boson: ±4 GeV (Γ_Z ≈ 2.5 GeV)
}

# Fensterbreiten (halbe Breite, in GeV)
DELTAS = [0.02 * i for i in range(1, 51)] + [1.0 + 0.5 * i for i in range(1, 19)]

# Simulationsparameter
N_SIMULATIONS = 10000
N_BOOTSTRAP = 5000
HIST_BINS = 100
KDE_BANDWIDTH = 0.5