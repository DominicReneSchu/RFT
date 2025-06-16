# Zentrale Parameter für die Resonanzanalyse

EPSILONS = [1, 0.5, 2/3, 0.75, 1.25]
DELTAS = [0.1 * i for i in range(1, 31)]
EXPECTED_HIT_RATES = {
    1: 0.01,
    0.5: 0.005,
    2/3: 0.006,
    0.75: 0.007,
    1.25: 0.0125,
}

N_SIMULATIONS = 10000
N_BOOTSTRAP = 5000
HIST_BINS = 100