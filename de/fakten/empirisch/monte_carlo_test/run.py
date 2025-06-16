import numpy as np
import pandas as pd
from tqdm import tqdm
from resonance_tools import (
    create_kde_sampler,
    resonance_analysis,
    bootstrap_hits,
    bootstrap_pvalue,
)
from visualization_interactive import (
    interactive_hits_histogram,
    interactive_pval_curve,
    interactive_heatmap_contrast,
)
from report import generate_report
from config import EPSILONS, DELTAS, EXPECTED_HIT_RATES, N_SIMULATIONS, N_BOOTSTRAP, HIST_BINS

def main():
    # --- Daten laden ---
    df = pd.read_csv('dielectron.csv')
    n = len(df)

    # Signalbereiche für klassisches Modell
    def get_signal_mask(df, epsilons, delta_max):
        mask = pd.Series(False, index=df.index)
        for eps in epsilons:
            mask |= ((df['M'] > eps - delta_max) & (df['M'] < eps + delta_max))
        return mask
    max_delta = max(DELTAS)
    signal_mask = get_signal_mask(df, EPSILONS, max_delta)

    # Hintergrunddaten vorbereiten (NaNs entfernen!)
    background_data = df.loc[~signal_mask, 'M'].values
    num_nans = np.isnan(background_data).sum()
    if num_nans > 0:
        print(f"Achtung: {num_nans} NaN-Werte im Hintergrund entfernt!")
    background_data = background_data[~np.isnan(background_data)]
    background_sampler = create_kde_sampler(background_data, bandwidth=0.05)

    # --- Klassische Resonanzanalyse ---
    real_results, real_hits_dict, real_pvals_dict = resonance_analysis(
        df['M'].values, EPSILONS, DELTAS, EXPECTED_HIT_RATES, n
    )

    # Bootstrap-Konfidenzintervalle für Trefferzahl und p-Werte
    for eps, res in real_results.items():
        delta = res['best_delta']
        hits_median, hits_16, hits_84 = bootstrap_hits(df['M'].values, eps, delta, n_bootstrap=N_BOOTSTRAP)
        res['hits_median'] = hits_median
        res['hits_16'] = hits_16
        res['hits_84'] = hits_84
        pval_ci = bootstrap_pvalue(df['M'].values, eps, delta, EXPECTED_HIT_RATES[eps], n, n_bootstrap=N_BOOTSTRAP)
        res['pval_bootstrap'] = pval_ci

    # --- Monte-Carlo-Simulation ---
    print(f"\nMonte-Carlo-Simulation läuft... ({N_SIMULATIONS} Durchläufe, KDE-Sampling)")
    sim_p_values = {eps: [] for eps in EPSILONS}
    sim_hits = {eps: [] for eps in EPSILONS}
    sim_hits_per_epsilon_delta = {eps: [] for eps in EPSILONS}
    sim_pvals_per_epsilon_delta = {eps: [] for eps in EPSILONS}

    for idx in tqdm(range(N_SIMULATIONS), desc="Simulationen", total=N_SIMULATIONS):
        simulated_data = background_sampler(n)
        sim_results, sim_hits_dict, sim_pvals_dict = resonance_analysis(
            simulated_data, EPSILONS, DELTAS, EXPECTED_HIT_RATES, n
        )
        for eps in EPSILONS:
            sim_p_values[eps].append(sim_results[eps]['p_corr'])
            sim_hits[eps].append(sim_results[eps]['hits'])
            sim_hits_per_epsilon_delta[eps].append(sim_hits_dict[eps])
            sim_pvals_per_epsilon_delta[eps].append(sim_pvals_dict[eps])

    # In numpy-Arrays umwandeln
    for eps in EPSILONS:
        sim_hits_per_epsilon_delta[eps] = np.array(sim_hits_per_epsilon_delta[eps])
        sim_pvals_per_epsilon_delta[eps] = np.array(sim_pvals_per_epsilon_delta[eps])

    # Empirische p-Werte
    empirical_p_values = {}
    for eps in EPSILONS:
        real_p = real_results[eps]['p_corr']
        count_lower = np.sum(np.array(sim_p_values[eps]) <= real_p)
        empirical_p = count_lower / N_SIMULATIONS
        empirical_p_values[eps] = empirical_p

    # --- Interaktive Visualisierung ---
    print("Starte interaktive Visualisierung ...")
    figs_hist = interactive_hits_histogram(sim_hits, real_results, EPSILONS)
    for fig in figs_hist:
        fig.show()

    figs_pval = interactive_pval_curve(DELTAS, sim_pvals_per_epsilon_delta, real_pvals_dict, real_results, EPSILONS)
    for fig in figs_pval:
        fig.show()

    real_hits_heatmap = np.array([real_hits_dict[eps] for eps in EPSILONS])
    sim_hits_heatmap = np.mean(np.array([sim_hits_per_epsilon_delta[eps] for eps in EPSILONS]), axis=1)
    fig_heatmap = interactive_heatmap_contrast(real_hits_heatmap, DELTAS, [f"{e:.2f}" for e in EPSILONS], "Δ", "ε", "Echte Treffer Heatmap")
    fig_heatmap.show()

    # --- Automatischer Report ---
    print("Erzeuge Report ...")
    generate_report(
        output_dir="report_out",
        real_results=real_results,
        sim_hits=sim_hits,
        empirical_p_values=empirical_p_values,
        EPSILONS=EPSILONS,
        DELTAS=DELTAS,
        sim_pvals_per_epsilon_delta=sim_pvals_per_epsilon_delta,
        real_pvals_matrix=real_pvals_dict,
        real_hits_matrix=real_hits_dict,
        sim_hits_heatmap=sim_hits_heatmap,
        blind_results=None  # Optional: dict mit Blind-Analyse-Ergebnissen
    )

if __name__ == "__main__":
    main()