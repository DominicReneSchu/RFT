import os
import numpy as np
import pandas as pd
from tqdm import tqdm
from resonance_tools import (
    create_kde_sampler,
    create_kde_model,
    expected_rate_from_kde,
    precompute_expected_rates,
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
    SIGNAL_EXCLUSION_WIDTH,
    DELTAS,
    N_SIMULATIONS,
    N_BOOTSTRAP,
    HIST_BINS,
    KDE_BANDWIDTH,
)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def main():
    # --- Daten laden ---
    data_path = os.path.join(SCRIPT_DIR, "dielectron.csv")
    df = pd.read_csv(data_path)
    mass_data = df["M"].dropna().values
    n = len(mass_data)
    print(f"Datensatz geladen: {n} Ereignisse (nach NaN-Entfernung)")
    print(f"Massenbereich: {mass_data.min():.2f} – {mass_data.max():.2f} GeV")

    # --- Signalbereiche mit schmaler Breite maskieren ---
    signal_mask = np.zeros(n, dtype=bool)
    for m0 in M0_VALUES:
        excl = SIGNAL_EXCLUSION_WIDTH[m0]
        signal_mask |= (mass_data > m0 - excl) & (mass_data < m0 + excl)

    background_data = mass_data[~signal_mask]
    print(f"Hintergrunddaten: {len(background_data)} Ereignisse "
          f"({len(background_data)/n*100:.1f}%)")
    print(f"Ausgeschlossene Signalbereiche:")
    for m0 in M0_VALUES:
        excl = SIGNAL_EXCLUSION_WIDTH[m0]
        n_excl = np.sum((mass_data > m0 - excl) & (mass_data < m0 + excl))
        print(f"  M₀={m0:.2f} ± {excl:.2f} GeV: {n_excl} Ereignisse entfernt")

    # --- KDE-Modell erstellen ---
    background_sampler = create_kde_sampler(background_data, bandwidth=KDE_BANDWIDTH)
    kde_background = create_kde_model(background_data, bandwidth=KDE_BANDWIDTH)

    # --- Erwartete Raten EINMAL vorberechnen ---
    print("\nVorberechnung der erwarteten Raten (einmalig) ...")
    expected_rates = precompute_expected_rates(kde_background, M0_VALUES, DELTAS)

    print(f"\nErwartete Raten aus KDE-Hintergrund:")
    print(f"{'M₀':>8} {'Δ=0.05':>12} {'Δ=0.10':>12} {'Δ=0.50':>12} {'Δ=2.00':>12}")
    for m0 in M0_VALUES:
        rates = []
        for d in [0.05, 0.10, 0.50, 2.00]:
            if d in expected_rates[m0]:
                rates.append(expected_rates[m0][d])
            else:
                rates.append(expected_rate_from_kde(kde_background, m0, d))
        print(f"{m0:8.2f} {rates[0]:12.6f} {rates[1]:12.6f} "
              f"{rates[2]:12.6f} {rates[3]:12.6f}")

    # --- Resonanzanalyse auf echten Daten ---
    print("\nResonanzanalyse auf echten Daten ...")
    real_results, real_hits_dict, real_pvals_dict = resonance_analysis(
        mass_data, M0_VALUES, DELTAS, n, expected_rates
    )

    # --- Bootstrap-Konfidenzintervalle ---
    print("Bootstrap-Konfidenzintervalle ...")
    for m0, res in real_results.items():
        delta = res["best_delta"]
        hits_median, hits_16, hits_84 = bootstrap_hits(
            mass_data, m0, delta, n_bootstrap=N_BOOTSTRAP
        )
        res["hits_median"] = hits_median
        res["hits_16"] = hits_16
        res["hits_84"] = hits_84

        rate_at_best = expected_rates[m0][delta]
        pval_ci = bootstrap_pvalue(
            mass_data, m0, delta, rate_at_best, n,
            n_bootstrap=N_BOOTSTRAP,
        )
        res["pval_bootstrap"] = pval_ci

    # --- Ergebnisse anzeigen ---
    print(f"\nErgebnisse der Resonanzanalyse:")
    print(f"{'M₀':>8} {'Δ_opt':>8} {'Hits':>6} {'Median':>8} "
          f"{'p_raw':>12} {'p_corr':>12}")
    for m0 in M0_VALUES:
        res = real_results[m0]
        print(f"{m0:8.2f} {res['best_delta']:8.3f} {res['hits']:6d} "
              f"{res['hits_median']:8.1f} "
              f"{res['p_raw']:12.2e} {res['p_corr']:12.2e}")

    # --- Monte-Carlo-Simulation ---
    print(
        f"\nMonte-Carlo-Simulation ({N_SIMULATIONS} Durchläufe, KDE-Sampling) ..."
    )
    sim_p_values = {m0: [] for m0 in M0_VALUES}
    sim_hits = {m0: [] for m0 in M0_VALUES}
    sim_hits_per_m0_delta = {m0: [] for m0 in M0_VALUES}
    sim_pvals_per_m0_delta = {m0: [] for m0 in M0_VALUES}

    for _ in tqdm(range(N_SIMULATIONS), desc="Simulationen"):
        simulated_data = background_sampler(n)
        sim_results, sim_hits_dict, sim_pvals_dict = resonance_analysis(
            simulated_data, M0_VALUES, DELTAS, n, expected_rates
        )
        for m0 in M0_VALUES:
            sim_p_values[m0].append(sim_results[m0]["p_corr"])
            sim_hits[m0].append(sim_results[m0]["hits"])
            sim_hits_per_m0_delta[m0].append(sim_hits_dict[m0])
            sim_pvals_per_m0_delta[m0].append(sim_pvals_dict[m0])

    for m0 in M0_VALUES:
        sim_hits_per_m0_delta[m0] = np.array(sim_hits_per_m0_delta[m0])
        sim_pvals_per_m0_delta[m0] = np.array(sim_pvals_per_m0_delta[m0])

    # --- Empirische p-Werte ---
    empirical_p_values = {}
    for m0 in M0_VALUES:
        real_p = real_results[m0]["p_corr"]
        count_lower = np.sum(np.array(sim_p_values[m0]) <= real_p)
        empirical_p_values[m0] = count_lower / N_SIMULATIONS

    print(f"\nEmpirische p-Werte:")
    for m0 in M0_VALUES:
        print(f"  M₀={m0:.2f} GeV: empir. p = {empirical_p_values[m0]:.4f}")

    # --- Interaktive Visualisierung ---
    print("\nInteraktive Visualisierung ...")
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
        "Δ (GeV)",
        "M₀ (GeV)",
        "Echte Treffer Heatmap",
    )
    fig_heatmap.show()

    # --- Report ---
    report_dir = os.path.join(SCRIPT_DIR, "report_out")
    print("\nErzeuge Report ...")
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
    print("Fertig.")


if __name__ == "__main__":
    main()