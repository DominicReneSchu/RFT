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
    # --- Load data ---
    df = pd.read_csv('dielectron.csv')
    n = len(df)

    # Signal regions for classical model
    def get_signal_mask(df, epsilons, delta_max):
        mask = pd.Series(False, index=df.index)
        for eps in epsilons:
            mask |= ((df['M'] > eps - delta_max) & (df['M'] < eps + delta_max))
        return mask
    max_delta = max(DELTAS)
    signal_mask = get_signal_mask(df, EPSILONS, max_delta)

    # Prepare background data (remove NaNs!)
    background_data = df.loc[~signal_mask, 'M'].values
    num_nans = np.isnan(background_data).sum()
    if num_nans > 0:
        print(f"Warning: {num_nans} NaN values removed from background!")
    background_data = background_data[~np.isnan(background_data)]
    background_sampler = create_kde_sampler(background_data, bandwidth=0.05)

    # --- Classical resonance analysis ---
    real_results, real_hits_dict, real_pvals_dict = resonance_analysis(
        df['M'].values, EPSILONS, DELTAS, EXPECTED_HIT_RATES, n
    )

    # Bootstrap confidence intervals for hit counts and p-values
    for eps, res in real_results.items():
        delta = res['best_delta']
        hits_median, hits_16, hits_84 = bootstrap_hits(df['M'].values, eps, delta, n_bootstrap=N_BOOTSTRAP)
        res['hits_median'] = hits_median
        res['hits_16'] = hits_16
        res['hits_84'] = hits_84
        pval_ci = bootstrap_pvalue(df['M'].values, eps, delta, EXPECTED_HIT_RATES[eps], n, n_bootstrap=N_BOOTSTRAP)
        res['pval_bootstrap'] = pval_ci

    # --- Monte Carlo simulation ---
    print(f"\nRunning Monte Carlo simulation... ({N_SIMULATIONS} runs, KDE sampling)")
    sim_p_values = {eps: [] for eps in EPSILONS}
    sim_hits = {eps: [] for eps in EPSILONS}
    sim_hits_per_epsilon_delta = {eps: [] for eps in EPSILONS}
    sim_pvals_per_epsilon_delta = {eps: [] for eps in EPSILONS}

    for idx in tqdm(range(N_SIMULATIONS), desc="Simulations", total=N_SIMULATIONS):
        simulated_data = background_sampler(n)
        sim_results, sim_hits_dict, sim_pvals_dict = resonance_analysis(
            simulated_data, EPSILONS, DELTAS, EXPECTED_HIT_RATES, n
        )
        for eps in EPSILONS:
            sim_p_values[eps].append(sim_results[eps]['p_corr'])
            sim_hits[eps].append(sim_results[eps]['hits'])
            sim_hits_per_epsilon_delta[eps].append(sim_hits_dict[eps])
            sim_pvals_per_epsilon_delta[eps].append(sim_pvals_dict[eps])

    # Convert to numpy arrays
    for eps in EPSILONS:
        sim_hits_per_epsilon_delta[eps] = np.array(sim_hits_per_epsilon_delta[eps])
        sim_pvals_per_epsilon_delta[eps] = np.array(sim_pvals_per_epsilon_delta[eps])

    # Empirical p-values
    empirical_p_values = {}
    for eps in EPSILONS:
        real_p = real_results[eps]['p_corr']
        count_lower = np.sum(np.array(sim_p_values[eps]) <= real_p)
        empirical_p = count_lower / N_SIMULATIONS
        empirical_p_values[eps] = empirical_p

    # --- Interactive visualization ---
    print("Starting interactive visualization ...")
    figs_hist = interactive_hits_histogram(sim_hits, real_results, EPSILONS)
    for fig in figs_hist:
        fig.show()

    figs_pval = interactive_pval_curve(DELTAS, sim_pvals_per_epsilon_delta, real_pvals_dict, real_results, EPSILONS)
    for fig in figs_pval:
        fig.show()

    real_hits_heatmap = np.array([real_hits_dict[eps] for eps in EPSILONS])
    sim_hits_heatmap = np.mean(np.array([sim_hits_per_epsilon_delta[eps] for eps in EPSILONS]), axis=1)
    fig_heatmap = interactive_heatmap_contrast(real_hits_heatmap, DELTAS, [f"{e:.2f}" for e in EPSILONS], "Δ", "ε", "Real Hits Heatmap")
    fig_heatmap.show()

    # --- Automatic report ---
    print("Generating report ...")
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
        blind_results=None  # Optional: dict with blind analysis results
    )

if __name__ == "__main__":
    main()