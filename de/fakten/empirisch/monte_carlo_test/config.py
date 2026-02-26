"""
Zentrale Parameter für die Monte-Carlo-Resonanzanalyse.

M0_VALUES: Resonanzmassenstellen (in GeV), an denen nach Überschüssen
           gesucht wird. Diese sind physikalische Massenhypothesen,
           NICHT die Kopplungseffizienz ε der Resonanzfeldtheorie.

DELTAS:    Fensterbreiten (halbe Breite) um jede Massenstelle M₀.

EXPECTED_HIT_RATES: Erwartete Trefferraten unter der Nullhypothese
                    (reiner Hintergrund) für jede Massenstelle.
                    Abgeschätzt aus der Hintergrunddichte im jeweiligen
                    Massenbereich.

N_SIMULATIONS:  Anzahl der Monte-Carlo-Pseudo-Experimente.
N_BOOTSTRAP:    Anzahl der Bootstrap-Wiederholungen für Konfidenzintervalle.
HIST_BINS:      Anzahl der Bins für Histogramm-Darstellungen.
"""

# Resonanzmassenstellen M₀ (in GeV)
M0_VALUES = [1, 0.5, 2/3, 0.75, 1.25]

# Fensterbreiten (halbe Breite, in GeV)
DELTAS = [0.1 * i for i in range(1, 31)]

# Erwartete Trefferraten unter Nullhypothese (pro Massenstelle)
EXPECTED_HIT_RATES = {
    1: 0.01,
    0.5: 0.005,
    2/3: 0.006,
    0.75: 0.007,
    1.25: 0.0125,
}

# Simulationsparameter
N_SIMULATIONS = 10000
N_BOOTSTRAP = 5000
HIST_BINS = 100