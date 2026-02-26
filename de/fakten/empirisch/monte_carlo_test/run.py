import os
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
from config import (
    M0_VALUES,
    DELTAS,
    EXPECTED_HIT_RATES,
    N_SIMULATIONS,
    N_BOOTSTRAP,
    HIST_BINS,
)

# Basisverzeichnis relativ zum Skript
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def main():
    # --- Daten laden ---
    data_path = os.path.join(SCRIPT_DIR, "dielectron.csv")
    df = pd.read_csv(data_path)
    n = len(df)

    # Signalbereiche für Hintergrundextraktion
    def get_signal_mask(df, m0_values, delta_max):
        mask = pd.Series(False, index=df.index)
        for m0 in m0_values:
            mask |= (df["M"] > m0 - delta_max) & (df["M"] < m0 + delta_max)
        return mask

    max_delta = max(DELTAS)
    signal_mask = get_signal_mask(df, M0_VALUES, max_delta)

    # Hintergrunddaten vorbereiten
    background_data = df.loc[~signal_mask, "M"].values
    num_nans = np.isnan(background_data).sum()
    if num_nans > 0:
        print(f"Achtung: {num_nans} NaN-Werte im Hintergrund entfernt!")
    background_data = background_data[~np.isnan(background_data)]
    background_sampler = create_kde_sampler(background_data, bandwidth=0.05)

    # --- Resonanzanalyse auf echten Daten ---
    real_results, real_hits_dict, real_pvals_dict = resonance_analysis(
        df["M"].values, M0_VALUES, DELTAS, EXPECTED_HIT_RATES, n
    )

    # Bootstrap-Konfidenzintervalle
    for m0, res in real_results.items():
        delta = res["best_delta"]
        hits_median, hits_16, hits_84 = bootstrap_hits(
            df["M"].values, m0, delta, n_bootstrap=N_BOOTSTRAP
        )
        res["hits_median"] = hits_median
        res["hits_16"] = hits_16
        res["hits_84"] = hits_84
        pval_ci = bootstrap_pvalue(
            df["M"].values, m0, delta, EXPECTED_HIT_RATES[m0], n,
            n_bootstrap=N_BOOTSTRAP,
        )
        res["pval_bootstrap"] = pval_ci

    # --- Monte-Carlo-Simulation ---
    print(
        f"\nMonte-Carlo-Simulation läuft... "
        f"({N_SIMULATIONS} Durchläufe, KDE-Sampling)"
    )
    sim_p_values = {m0: [] for m0 in M0_VALUES}
    sim_hits = {m0: [] for m0 in M0_VALUES}
    sim_hits_per_m0_delta = {m0: [] for m0 in M0_VALUES}
    sim_pvals_per_m0_delta = {m0: [] for m0 in M0_VALUES}

    for _ in tqdm(range(N_SIMULATIONS), desc="Simulationen"):
        simulated_data = background_sampler(n)
        sim_results, sim_hits_dict, sim_pvals_dict = resonance_analysis(
            simulated_data, M0_VALUES, DELTAS, EXPECTED_HIT_RATES, n
        )
        for m0 in M0_VALUES:
            sim_p_values[m0].append(sim_results[m0]["p_corr"])
            sim_hits[m0].append(sim_results[m0]["hits"])
            sim_hits_per_m0_delta[m0].append(sim_hits_dict[m0])
            sim_pvals_per_m0_delta[m0].append(sim_pvals_dict[m0])

    # In numpy-Arrays umwandeln
    for m0 in M0_VALUES:
        sim_hits_per_m0_delta[m0] = np.array(sim_hits_per_m0_delta[m0])
        sim_pvals_per_m0_delta[m0] = np.array(sim_pvals_per_m0_delta[m0])

    # Empirische p-Werte
    empirical_p_values = {}
    for m0 in M0_VALUES:
        real_p = real_results[m0]["p_corr"]
        count_lower = np.sum(np.array(sim_p_values[m0]) <= real_p)
        empirical_p_values[m0] = count_lower / N_SIMULATIONS

    # --- Interaktive Visualisierung ---
    print("Starte interaktive Visualisierung ...")
    figs_hist = interactive_hits_histogram(sim_hits, real_results, M0_VALUES)
    for fig in figs_hist:
        fig.show()

    figs_pval = interactive_pval_curve(
        DELTAS, sim_pvals_per_m0_delta, real_pvals_dict, real_results, M0_VALUES
    )
    for fig in figs_pval:
        fig.show()

    real_hits_heatmap = np.array([real_hits_dict[m0] for m0 in M0_VALUES])
    sim_hits_heatmap = np.mean(
        np.array([sim_hits_per_m0_delta[m0] for m0 in M0_VALUES]), axis=1
    )
    fig_heatmap = interactive_heatmap_contrast(
        real_hits_heatmap,
        DELTAS,
        [f"{m0:.2f}" for m0 in M0_VALUES],
        "Δ",
        "M₀",
        "Echte Treffer Heatmap",
    )
    fig_heatmap.show()

    # --- Automatischer Report ---
    report_dir = os.path.join(SCRIPT_DIR, "report_out")
    print("Erzeuge Report ...")
    generate_report(
        output_dir=report_dir,
        real_results=real_results,
        sim_hits=sim_hits,
        empirical_p_values=empirical_p_values,
        m0_values=M0_VALUES,
        deltas=DELTAS,
        sim_pvals_per_m0_delta=sim_pvals_per_m0_delta,
        real_pvals_matrix=real_pvals_dict,
        real_hits_matrix=real_hits_dict,
        sim_hits_heatmap=sim_hits_heatmap,
        blind_results=None,
    )


if __name__ == "__main__":
    main()