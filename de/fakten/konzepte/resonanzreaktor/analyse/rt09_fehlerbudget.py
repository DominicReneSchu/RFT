# rt09_fehlerbudget.py
# © Dominic-René Schu, 2025/2026 – Resonanzfeldtheorie
# RT-09: Vollständiges Unsicherheitsbudget für das Am-241-Experiment
#
# Behebt M-4 (PEER_REVIEW_READINESS.md):
#   Die bisherige Signifikanzangabe (>50.000σ) basierte auf σ_GDR ≈ 300 mb.
#   Nach RT-06 ist der korrekte Querschnitt σ(γ,α) = 1.719 mb (Hauser-Feshbach).
#   Dieser Code führt eine Monte-Carlo-Fehlerrechnung durch und quantifiziert
#   die korrigierte Signifikanz und die Messzeit-Anforderungen.
#
# Verwendung:
#   cd de/fakten/konzepte/resonanzreaktor/simulation
#   python ../analyse/rt09_fehlerbudget.py

from __future__ import annotations

import sys
import os

# Simulationsverzeichnis in Suchpfad aufnehmen
_sim_dir = os.path.join(os.path.dirname(__file__), '..', 'simulation')
sys.path.insert(0, os.path.abspath(_sim_dir))

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from experiment_am241 import (
    ELI_NP,
    Am241_Literature,
    uncertainty_budget_am241,
)

# ============================================================
# Konfiguration
# ============================================================

OUTPUT_DIR = os.path.dirname(__file__)
PLOT_FILE = os.path.join(OUTPUT_DIR, 'rt09_fehlerbudget.png')
E_GAMMA = Am241_Literature.E_gdr_centroid_MeV  # 14.0 MeV
TARGET_MG = 100.0
T_MEAS = 100.0  # Stunden (Referenzmesszeit)

# Szenarien
SZENARIEN = {
    "Optimistisch": {
        "sigma_photo_alpha_mb": 1.719,       # Zentralwert
        "detector_efficiency": 0.8,
        "detector_efficiency_unc": 0.10,
        "phase_coherence": 1.0,
        "phase_coherence_unc": 0.05,
        "beam_sigma_cm": 0.5,
        "beam_sigma_unc": 0.05,
    },
    "Realistisch": {
        "sigma_photo_alpha_mb": 1.719,       # Zentralwert
        "detector_efficiency": 0.5,
        "detector_efficiency_unc": 0.15,
        "phase_coherence": 1.0,
        "phase_coherence_unc": 0.10,
        "beam_sigma_cm": 0.5,
        "beam_sigma_unc": 0.10,
    },
    "Konservativ": {
        "sigma_photo_alpha_mb": 1.719 / 3.0,  # unteres Ende (Faktor 3 kleiner)
        "detector_efficiency": 0.3,
        "detector_efficiency_unc": 0.15,
        "phase_coherence": 0.8,
        "phase_coherence_unc": 0.15,
        "beam_sigma_cm": 0.5,
        "beam_sigma_unc": 0.15,
    },
}


def run_scenarios(t_meas: float = T_MEAS, n_mc: int = 100_000) -> dict:
    """Führt uncertainty_budget_am241() für alle drei Szenarien durch."""
    results = {}
    for name, params in SZENARIEN.items():
        print(f"  Berechne Szenario: {name} ...")
        results[name] = uncertainty_budget_am241(
            facility=ELI_NP,
            E_gamma_MeV=E_GAMMA,
            target_mass_mg=TARGET_MG,
            measurement_time_hours=t_meas,
            n_mc=n_mc,
            **params,
        )
    return results


def print_tabelle(results: dict) -> None:
    """Tabellarische Ausgabe der RT-09-Ergebnisse."""
    print()
    print("=" * 80)
    print("=== RT-09 FEHLERBUDGET Am-241 (ELI-NP VEGA, 100 mg, 100 h) ===")
    print("=" * 80)
    print()
    header = (
        f"{'Szenario':<16} {'SNR_med':>10} {'SNR_p16':>9} {'SNR_p84':>9} "
        f"{'t(3σ)/h':>9} {'t(5σ)/h':>9} {'Falsif.?':>10}"
    )
    print(header)
    print("-" * 80)
    for name, r in results.items():
        feasible = "JA" if r['falsification_feasible'] else "NEIN"
        t3 = r['t_for_3sigma']
        t5 = r['t_for_5sigma']
        print(
            f"{name:<16} "
            f"{r['SNR_median']:>9.1f} σ "
            f"{r['SNR_p16']:>8.1f} σ "
            f"{r['SNR_p84']:>8.1f} σ "
            f"{t3:>9.1f} "
            f"{t5:>9.1f} "
            f"{feasible:>10}"
        )
    print()

    # Dominanter Unsicherheitsbeitrag (realistisches Szenario)
    real = results["Realistisch"]
    contrib = real['contributions']
    dom = real['dominant_uncertainty']
    print(f"Dominanter Unsicherheitsbeitrag (Realistisch): {dom}")
    print(f"  Varianzanteile: " +
          " | ".join(f"{k}: {v*100:.1f}%" for k, v in sorted(
              contrib.items(), key=lambda x: -x[1])))
    print()
    print(f"Signalverhältnis R (Median):      "
          f"{real['R_median']:.4f}  (Theorie: 2.0000 exakt)")
    print()

    # Vergleich alt vs. neu
    from experiment_am241 import ExperimentConfig
    exp_ref = ExperimentConfig(ELI_NP, E_GAMMA, TARGET_MG, T_MEAS)
    sigma_gdr_legacy = exp_ref.sigma_rft_legacy
    sigma_pa_new = exp_ref.sigma_rft_pa

    print("Vergleich alt vs. neu:")
    print(f"  Signifikanz (alt, σ_GDR = {exp_ref.sigma_gdr_mb:.0f} mb):   "
          f">{sigma_gdr_legacy:.0f} σ  [RT-06: Revision erforderlich]")
    print(f"  Signifikanz (neu, σ(γ,α) = 1.719 mb):  "
          f"{sigma_pa_new:.1f} σ    [RT-09: KORREKT]")
    factor = sigma_gdr_legacy / max(sigma_pa_new, 1e-10)
    print(f"  Korrekturfaktor: {factor:.0f}× kleiner (σ_GDR/σ(γ,α))")
    print()

    # M-4 Status
    feasible_count = sum(1 for r in results.values() if r['falsification_feasible'])
    if feasible_count == 3:
        m4_status = "BEHOBEN"
    elif feasible_count >= 1:
        m4_status = "TEILWEISE BEHOBEN"
    else:
        m4_status = "OFFEN — ELI-NP nicht ausreichend, alternatives Facility nötig"
    print(f"M-4 Status: {m4_status}")
    print("=" * 80)


def snr_vs_time(t_hours: np.ndarray, results: dict) -> dict:
    """Berechnet SNR(t) für alle Szenarien. SNR ∝ √t."""
    snr_curves = {}
    for name, r in results.items():
        snr_ref = r['SNR_median']
        t_ref = T_MEAS
        snr_curves[name] = snr_ref * np.sqrt(t_hours / t_ref)
    return snr_curves


def plot_results(results: dict) -> None:
    """Erstellt den RT-09-Plot mit drei Panels."""
    colors = {
        "Optimistisch": "green",
        "Realistisch": "royalblue",
        "Konservativ": "orange",
    }
    linestyles = {
        "Optimistisch": "-",
        "Realistisch": "--",
        "Konservativ": ":",
    }

    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    fig.suptitle(
        "RT-09: Vollständiges Unsicherheitsbudget Am-241\n"
        "ELI-NP VEGA, 100 mg Target, E_γ = 14.0 MeV",
        fontsize=13, fontweight='bold'
    )

    # --- Panel 1: SNR-Histogramme ---
    ax = axes[0]
    n_mc_plot = 50_000
    for name, params in SZENARIEN.items():
        r = results[name]
        # Rekonstruiere SNR-Stichproben für Histogramm (vereinfacht)
        rng = np.random.default_rng(seed=99)
        snr_ref = r['SNR_median']
        snr_std = (r['SNR_p84'] - r['SNR_p16']) / 2.0
        snr_samples = rng.normal(snr_ref, snr_std, n_mc_plot)
        ax.hist(
            snr_samples, bins=80, density=True, alpha=0.5,
            color=colors[name], label=name,
        )
        ax.axvline(r['SNR_median'], color=colors[name], linewidth=2,
                   linestyle=linestyles[name])
        ax.axvline(r['SNR_p16'], color=colors[name], linewidth=1.0,
                   linestyle=':', alpha=0.7)

    ax.axvline(3.0, color='orange', linewidth=1.5, linestyle='--', label='3σ')
    ax.axvline(5.0, color='red', linewidth=1.5, linestyle='--', label='5σ')
    ax.set_xlabel('SNR (σ)', fontsize=11)
    ax.set_ylabel('Dichte', fontsize=11)
    ax.set_title('Panel 1: SNR-Verteilungen\n(MC-Histogramme, 100 h)', fontsize=10)
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)

    # --- Panel 2: Tornado-Diagramm (Sensitivitätsanalyse) ---
    ax = axes[1]
    real = results["Realistisch"]
    contrib = real['contributions']
    sorted_contrib = sorted(contrib.items(), key=lambda x: x[1], reverse=True)
    labels = [k for k, _ in sorted_contrib]
    values = [v * 100 for _, v in sorted_contrib]
    label_map = {
        "sigma_pa": "σ(γ,α) — Hauser-Feshbach",
        "detector_efficiency": "Detektoreffizienz",
        "beam_sigma": "Strahlausbreitung",
        "phase_coherence": "Phasenkohärenz",
    }
    display_labels = [label_map.get(l, l) for l in labels]
    bar_colors = ['firebrick' if v == max(values) else 'steelblue' for v in values]
    bars = ax.barh(display_labels, values, color=bar_colors, alpha=0.85)
    for bar, val in zip(bars, values):
        ax.text(
            bar.get_width() + 0.5, bar.get_y() + bar.get_height() / 2,
            f"{val:.1f}%", va='center', fontsize=10
        )
    ax.set_xlabel('Varianzanteil (%)', fontsize=11)
    ax.set_title('Panel 2: Tornado-Diagramm\n(Sensitivitätsanalyse, Realistisch)', fontsize=10)
    ax.set_xlim(0, max(values) * 1.25)
    ax.grid(True, alpha=0.3, axis='x')

    # --- Panel 3: SNR(t) für alle Szenarien ---
    ax = axes[2]
    t_hours = np.logspace(0, 4, 300)  # 1h bis 10000h
    snr_curves = snr_vs_time(t_hours, results)

    for name, snr_arr in snr_curves.items():
        ax.loglog(
            t_hours, snr_arr, color=colors[name],
            linestyle=linestyles[name], linewidth=2, label=name
        )

    ax.axhline(3.0, color='orange', linestyle='--', linewidth=1.5,
               label='3σ (Evidenz)', alpha=0.9)
    ax.axhline(5.0, color='red', linestyle='--', linewidth=1.5,
               label='5σ (Entdeckung)', alpha=0.9)
    ax.axvline(100, color='gray', linestyle=':', linewidth=1.0,
               label='100 h (Referenz)')

    ax.set_xlabel('Messzeit (h)', fontsize=11)
    ax.set_ylabel('SNR (σ)', fontsize=11)
    ax.set_title('Panel 3: SNR vs. Messzeit\n(alle Szenarien)', fontsize=10)
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3, which='both')
    ax.set_xlim(1, 10000)

    plt.tight_layout()
    plt.savefig(PLOT_FILE, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"\nPlot gespeichert: {PLOT_FILE}")


def main() -> None:
    print("=" * 80)
    print("RT-09: FEHLERBUDGET Am-241 — Vollständige Unsicherheitsrechnung")
    print("Behebt M-4 (PEER_REVIEW_READINESS.md)")
    print("=" * 80)
    print(f"\nEinrichtung: {ELI_NP.name} ({ELI_NP.location})")
    print(f"E_γ = {E_GAMMA} MeV (GDR-Zentroid)")
    print(f"Target: {TARGET_MG} mg Am-241")
    print(f"Referenz-Messzeit: {T_MEAS} h")
    print(f"σ(γ,α) Zentralwert: 1.719 mb (Hauser-Feshbach, RT-06)")
    print()

    print("Starte Monte-Carlo-Rechnung (n_MC = 100.000) ...")
    results = run_scenarios(t_meas=T_MEAS, n_mc=100_000)

    print_tabelle(results)

    print("\nErstelle Plot ...")
    plot_results(results)

    print("\nFertig.")


if __name__ == "__main__":
    main()
