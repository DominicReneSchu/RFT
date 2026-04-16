"""
Publikationslauf: Monte-Carlo-Resonanzanalyse.

Erweiterungen gegenueber run.py:
  - 50.000 Simulationen (statt 10.000)
  - 10.000 Bootstrap-Wiederholungen
  - Fuenfte Resonanz: phi(1020)
  - Systematik-Check ueber 3 KDE-Bandbreiten
  - Seed-Variation ueber 10 unabhaengige Laeufe
  - Automatischer Export aller Ergebnisse als CSV + JSON
"""

from __future__ import annotations

from typing import Any

import os
import json
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
from report import generate_report
from config import (
    M0_VALUES,
    SIGNAL_EXCLUSION_WIDTH,
    DELTAS,
    N_SIMULATIONS,
    N_BOOTSTRAP,
    HIST_BINS,
    KDE_BANDWIDTH,
    KDE_BANDWIDTH_VARIATIONS,
    RANDOM_SEEDS,
)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def run_single_analysis(mass_data: np.ndarray, n: int, bandwidth: float, seed: int, m0_values: list[float], deltas: list[float]) -> dict[str, Any]:
    """Fuehrt eine vollstaendige MC-Analyse fuer einen Seed + Bandbreite durch."""
    rng = np.random.RandomState(seed)

    # Signalbereiche maskieren
    signal_mask = np.zeros(n, dtype=bool)
    for m0 in m0_values:
        excl = SIGNAL_EXCLUSION_WIDTH[m0]
        signal_mask |= (mass_data > m0 - excl) & (mass_data < m0 + excl)
    background_data = mass_data[~signal_mask]

    # KDE-Modell
    background_sampler = create_kde_sampler(background_data, bandwidth=bandwidth)
    kde_background = create_kde_model(background_data, bandwidth=bandwidth)

    # Erwartete Raten vorberechnen
    expected_rates = precompute_expected_rates(kde_background, m0_values, deltas)

    # Resonanzanalyse auf echten Daten
    real_results, real_hits_dict, real_pvals_dict = resonance_analysis(
        mass_data, m0_values, deltas, n, expected_rates
    )

    # Bootstrap-Konfidenzintervalle
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

    # Monte-Carlo-Simulation
    sim_p_values = {m0: [] for m0 in m0_values}
    sim_hits = {m0: [] for m0 in m0_values}
    sim_hits_per_m0_delta = {m0: [] for m0 in m0_values}
    sim_pvals_per_m0_delta = {m0: [] for m0 in m0_values}

    for i in tqdm(range(N_SIMULATIONS),
                  desc=f"MC bw={bandwidth:.1f} seed={seed}"):
        simulated_data = background_sampler(n)
        sim_results, sim_hits_dict, sim_pvals_dict = resonance_analysis(
            simulated_data, m0_values, deltas, n, expected_rates
        )
        for m0 in m0_values:
            sim_p_values[m0].append(sim_results[m0]["p_corr"])
            sim_hits[m0].append(sim_results[m0]["hits"])
            sim_hits_per_m0_delta[m0].append(sim_hits_dict[m0])
            sim_pvals_per_m0_delta[m0].append(sim_pvals_dict[m0])

    for m0 in m0_values:
        sim_hits_per_m0_delta[m0] = np.array(sim_hits_per_m0_delta[m0])
        sim_pvals_per_m0_delta[m0] = np.array(sim_pvals_per_m0_delta[m0])

    # Empirische p-Werte
    empirical_p_values = {}
    for m0 in m0_values:
        real_p = real_results[m0]["p_corr"]
        count_lower = np.sum(np.array(sim_p_values[m0]) <= real_p)
        empirical_p_values[m0] = count_lower / N_SIMULATIONS

    return {
        "real_results": real_results,
        "empirical_p_values": empirical_p_values,
        "sim_hits": sim_hits,
        "sim_hits_per_m0_delta": sim_hits_per_m0_delta,
        "sim_pvals_per_m0_delta": sim_pvals_per_m0_delta,
        "real_hits_dict": real_hits_dict,
        "real_pvals_dict": real_pvals_dict,
        "bandwidth": bandwidth,
        "seed": seed,
    }


def main() -> None:
    # Daten laden
    data_path = os.path.join(SCRIPT_DIR, "dielectron.csv")
    df = pd.read_csv(data_path)
    mass_data = df["M"].dropna().values
    n = len(mass_data)

    print("=" * 70)
    print("PUBLIKATIONSLAUF: Monte-Carlo-Resonanzanalyse")
    print("=" * 70)
    print(f"Datensatz: {n} Ereignisse")
    print(f"Massenbereich: {mass_data.min():.2f} - {mass_data.max():.2f} GeV")
    print(f"Resonanzen: {M0_VALUES}")
    print(f"Simulationen pro Lauf: {N_SIMULATIONS}")
    print(f"Bootstrap-Wiederholungen: {N_BOOTSTRAP}")
    print(f"KDE-Bandbreiten: {KDE_BANDWIDTH_VARIATIONS}")
    print(f"Seeds: {RANDOM_SEEDS}")
    print(f"Gesamtzahl MC-Laeufe: "
          f"{len(KDE_BANDWIDTH_VARIATIONS)} x {len(RANDOM_SEEDS)} = "
          f"{len(KDE_BANDWIDTH_VARIATIONS) * len(RANDOM_SEEDS)}")
    print(f"Gesamtzahl Simulationen: "
          f"{len(KDE_BANDWIDTH_VARIATIONS) * len(RANDOM_SEEDS) * N_SIMULATIONS:,}")
    print()

    # Ausgabeverzeichnis
    out_dir = os.path.join(SCRIPT_DIR, "publication_results")
    os.makedirs(out_dir, exist_ok=True)

    # Hauptlauf: Standard-Bandbreite, erster Seed
    print("=== HAUPTLAUF (bw=0.5, seed=42) ===")
    main_result = run_single_analysis(
        mass_data, n, KDE_BANDWIDTH, 42, M0_VALUES, DELTAS
    )

    # Ergebnisse anzeigen
    print(f"\nHauptlauf-Ergebnisse ({N_SIMULATIONS} Simulationen):")
    print(f"{'M0':>8} {'Resonanz':>12} {'D_opt':>8} {'Hits':>6} "
          f"{'p_corr':>12} {'emp_p':>8}")
    resonanz_namen = {
        1.020: "phi(1020)",
        3.1: "J/psi",
        9.46: "Y(1S)",
        10.02: "Y(2S)",
        91.2: "Z-Boson",
    }
    for m0 in M0_VALUES:
        res = main_result["real_results"][m0]
        emp_p = main_result["empirical_p_values"][m0]
        name = resonanz_namen.get(m0, f"{m0:.2f}")
        print(f"{m0:8.3f} {name:>12} {res['best_delta']:8.3f} "
              f"{res['hits']:6d} {res['p_corr']:12.2e} {emp_p:8.4f}")

    # Hauptlauf-Report
    report_dir = os.path.join(out_dir, "main_report")
    sim_hits_heatmap = np.mean(
        np.array([main_result["sim_hits_per_m0_delta"][m0]
                  for m0 in M0_VALUES]), axis=1
    )
    generate_report(
        output_dir=report_dir,
        real_results=main_result["real_results"],
        sim_hits=main_result["sim_hits"],
        empirical_p_values=main_result["empirical_p_values"],
        m0_values=M0_VALUES,
        deltas=DELTAS,
        sim_pvals_per_m0_delta=main_result["sim_pvals_per_m0_delta"],
        real_pvals_matrix=main_result["real_pvals_dict"],
        real_hits_matrix=main_result["real_hits_dict"],
        sim_hits_heatmap=sim_hits_heatmap,
        blind_results=None,
    )

    # Systematik-Check: KDE-Bandbreiten-Variation
    print("\n=== SYSTEMATIK-CHECK: KDE-Bandbreiten ===")
    systematik_results = []
    for bw in KDE_BANDWIDTH_VARIATIONS:
        print(f"\n--- Bandbreite = {bw:.1f} GeV ---")
        result = run_single_analysis(
            mass_data, n, bw, 42, M0_VALUES, DELTAS
        )
        systematik_results.append(result)
        for m0 in M0_VALUES:
            emp_p = result["empirical_p_values"][m0]
            print(f"  M0={m0:.3f}: emp_p = {emp_p:.4f}")

    # Seed-Variation (nur Standard-Bandbreite)
    print("\n=== SEED-VARIATION (bw=0.5) ===")
    seed_results = []
    for seed in RANDOM_SEEDS:
        print(f"\n--- Seed = {seed} ---")
        result = run_single_analysis(
            mass_data, n, KDE_BANDWIDTH, seed, M0_VALUES, DELTAS
        )
        seed_results.append(result)

    # Zusammenfassung Seed-Variation
    print("\n=== ZUSAMMENFASSUNG SEED-VARIATION ===")
    print(f"{'M0':>8} {'emp_p (mean)':>12} {'emp_p (std)':>12} "
          f"{'emp_p (max)':>12}")
    for m0 in M0_VALUES:
        emp_ps = [r["empirical_p_values"][m0] for r in seed_results]
        print(f"{m0:8.3f} {np.mean(emp_ps):12.6f} "
              f"{np.std(emp_ps):12.6f} {np.max(emp_ps):12.6f}")

    # Export: Hauptergebnisse als JSON
    export = {
        "n_events": int(n),
        "n_simulations": N_SIMULATIONS,
        "n_bootstrap": N_BOOTSTRAP,
        "m0_values": M0_VALUES,
        "kde_bandwidth": KDE_BANDWIDTH,
        "main_results": {},
    }
    for m0 in M0_VALUES:
        res = main_result["real_results"][m0]
        export["main_results"][str(m0)] = {
            "resonance": resonanz_namen.get(m0, str(m0)),
            "best_delta": float(res["best_delta"]),
            "hits": int(res["hits"]),
            "p_corr": float(res["p_corr"]),
            "empirical_p": float(main_result["empirical_p_values"][m0]),
            "hits_median": float(res.get("hits_median", 0)),
            "hits_16": float(res.get("hits_16", 0)),
            "hits_84": float(res.get("hits_84", 0)),
        }
    export["systematik"] = {
        str(bw): {
            str(m0): float(r["empirical_p_values"][m0])
            for m0 in M0_VALUES
        }
        for bw, r in zip(KDE_BANDWIDTH_VARIATIONS, systematik_results)
    }
    export["seed_variation"] = {
        str(m0): {
            "mean": float(np.mean([r["empirical_p_values"][m0]
                                   for r in seed_results])),
            "std": float(np.std([r["empirical_p_values"][m0]
                                 for r in seed_results])),
            "max": float(np.max([r["empirical_p_values"][m0]
                                 for r in seed_results])),
        }
        for m0 in M0_VALUES
    }

    json_path = os.path.join(out_dir, "publication_results.json")
    with open(json_path, "w") as f:
        json.dump(export, f, indent=2)
    print(f"\nErgebnisse exportiert: {json_path}")

    # Export: CSV
    rows = []
    for m0 in M0_VALUES:
        res = main_result["real_results"][m0]
        rows.append({
            "M0_GeV": m0,
            "Resonance": resonanz_namen.get(m0, str(m0)),
            "Delta_opt_GeV": res["best_delta"],
            "Hits": res["hits"],
            "p_corr": res["p_corr"],
            "empirical_p": main_result["empirical_p_values"][m0],
            "N_sim": N_SIMULATIONS,
            "KDE_bw": KDE_BANDWIDTH,
        })
    csv_path = os.path.join(out_dir, "publication_results.csv")
    pd.DataFrame(rows).to_csv(csv_path, index=False)
    print(f"CSV exportiert: {csv_path}")

    print("\n" + "=" * 70)
    print("PUBLIKATIONSLAUF ABGESCHLOSSEN")
    print("=" * 70)


if __name__ == "__main__":
    main()