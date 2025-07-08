import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from collections import Counter
from itertools import product

def analytic_distribution(dice):
    outcomes = [sum(p) for p in product(range(1, 7), repeat=dice)]
    counter = Counter(outcomes)
    total = 6**dice
    x_vals = np.array(sorted(counter.keys()))
    y_vals = np.array([counter[x] / total for x in x_vals])
    return x_vals, y_vals

def plot_dice_sum_vs_gauss(dice, trials, seed=None):
    if seed is not None:
        np.random.seed(seed)
    sums = np.random.randint(1, 7, (trials, dice)).sum(axis=1)
    counter = Counter(sums)
    x_emp = np.array(sorted(counter.keys()))
    y_emp = np.array([counter[x] / trials for x in x_emp])
    x_theo, y_theo = analytic_distribution(dice) if dice <= 10 else (None, None)

    dice_mean = dice * 3.5
    dice_std = np.sqrt(dice * 35 / 12)
    x_range = np.linspace(min(x_emp), max(x_emp), 500)
    gauss = norm.pdf(x_range, dice_mean, dice_std)
    gauss *= sum(y_emp) * (x_emp[1] - x_emp[0])

    plt.figure(figsize=(10, 5))
    plt.bar(x_emp, y_emp, width=0.8, alpha=0.5, label='Simulation')
    if x_theo is not None:
        plt.plot(x_theo, y_theo, 'ko', label='Theorie (diskret)')
    plt.plot(x_range, gauss, 'r-', lw=2, label='Normalverteilung (Gauß)')
    plt.title(f'Summenverteilung bei {dice} Würfeln, {trials:,} Würfe')
    plt.xlabel('Augensumme')
    plt.ylabel('Wahrscheinlichkeit')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Gruppenelemente werden dialogisch abgefragt und inkludiert
    while True:
        try:
            dice = int(input("Anzahl der Würfel: "))
            if dice < 1:
                print("Bitte mindestens 1 Würfel angeben.")
                continue
            break
        except ValueError:
            print("Bitte eine ganze Zahl eingeben.")
    while True:
        try:
            trials = int(input("Anzahl der Würfe (Simulationen): "))
            if trials < 1:
                print("Bitte mindestens 1 Simulation angeben.")
                continue
            break
        except ValueError:
            print("Bitte eine ganze Zahl eingeben.")

    plot_dice_sum_vs_gauss(dice, trials)