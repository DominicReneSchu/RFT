# run.py
# © Dominic-René Schu, 2025/2026 – Resonanzfeldtheorie
# Resonanzreaktor: Publikationslauf (κ=1, mit Energiebilanz)
# Erweitert: 8 Isotope, Flussscan, Transmutationsketten

import numpy as np
import matplotlib.pyplot as plt
import os
from material import (PI, MEV_TO_J, SECONDS_PER_YEAR,
                       ALL_ACTINIDES, ALL_FISSION_PRODUCTS, ALL_ISOTOPES,
                       uranium_235, uranium_238, neptunium_237,
                       plutonium_239, plutonium_240, americium_241,
                       thorium_232, cesium_137, strontium_90)
from resonance import (simulate_decay, phase_scan, energy_scan,
                        coupling_efficiency, effective_decay_rate,
                        energy_balance, gdr_cross_section_rft)


def ensure_dir(path):
    os.makedirs(path, exist_ok=True)


def plot_energy_scan(isotope, output_dir):
    """Plot 1: GDR-Profil mit RFT-Kopplung."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    ax = axes[0]
    for dp, label, color in [(0, 'Δφ=0 (Resonanz)', 'red'),
                              (PI/2, 'Δφ=π/2', 'orange'),
                              (PI, 'Δφ=π (Anti)', 'blue')]:
        result = energy_scan(isotope, delta_phi=dp)
        ax.plot(result['E_gamma_MeV'], result['sigma_rft_mb'],
                color=color, label=f'{label}, ε={result["eta"]:.2f}')

    result_full = energy_scan(isotope, delta_phi=0)
    ax.plot(result_full['E_gamma_MeV'], result_full['sigma_standard_mb'],
            'k--', label='σ_GDR (Literatur)', linewidth=1)

    ax.set_xlabel('E_γ (MeV)')
    ax.set_ylabel('σ (mb)')
    ax.set_title(f'GDR mit RFT-Kopplung: {isotope.name}')
    ax.legend(fontsize=8)
    ax.set_xlim(5, 25)
    ax.grid(True, alpha=0.3)
    for E in isotope.E_gdr_peaks:
        ax.axvline(E, color='gray', linestyle=':', alpha=0.5)

    ax = axes[1]
    for dp, label, color in [(0, 'Δφ=0 (ε=1)', 'red'),
                              (PI/4, 'Δφ=π/4 (ε=0.85)', 'orange'),
                              (PI/2, 'Δφ=π/2 (ε=0.5)', 'green'),
                              (PI, 'Δφ=π (ε=0)', 'blue')]:
        result = energy_scan(isotope, delta_phi=dp)
        with np.errstate(divide='ignore', invalid='ignore'):
            ratio = result['sigma_rft_mb'] / result['sigma_standard_mb']
        ax.plot(result['E_gamma_MeV'], ratio,
                color=color, label=label)

    ax.axhline(1.0, color='k', linestyle='--', alpha=0.5)
    ax.set_xlabel('E_γ (MeV)')
    ax.set_ylabel('σ_RFT / σ_GDR')
    ax.set_title(f'RFT-Kopplung = ε(Δφ): {isotope.name}')
    ax.legend(fontsize=8)
    ax.set_xlim(5, 25)
    ax.set_ylim(-0.05, 1.15)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, f'energy_scan_{isotope.name}.png'),
                dpi=150)
    plt.close()
    print(f"  → energy_scan_{isotope.name}.png")


def plot_phase_scan(isotope, output_dir):
    """Plot 2: Phasenscan."""
    result = phase_scan(isotope, n_phases=100, photon_flux=1e12)

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    ax = axes[0]
    ax.plot(result['delta_phi'] / PI, result['eta'],
            'b-', label='η(Δφ) = cos²(Δφ/2) = ε(Δφ)', linewidth=2)
    ax.set_xlabel('Δφ / π')
    ax.set_ylabel('η = ε (Kopplungseffizienz)')
    ax.set_title(f'Kopplungseffizienz: {isotope.name}')
    ax.legend()
    ax.set_xlim(0, 2)
    ax.grid(True, alpha=0.3)

    ax = axes[1]
    ax.plot(result['delta_phi'] / PI, result['ratio'],
            'r-', linewidth=2)
    ax.axhline(1.0, color='k', linestyle='--', alpha=0.5,
               label='Standardmodell (λ₀)')
    ax.set_xlabel('Δφ / π')
    ax.set_ylabel('λ_eff / λ₀')
    ax.set_title(f'Effektive Zerfallsrate: {isotope.name}\n'
                 f'Φ_γ = 10¹² γ/(cm²·s), κ=1 (RFT)')
    ax.legend()
    ax.set_xlim(0, 2)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, f'phase_scan_{isotope.name}.png'),
                dpi=150)
    plt.close()
    print(f"  → phase_scan_{isotope.name}.png")


def plot_decay_comparison(isotope, output_dir):
    """Plot 3: Zerfall Standard vs. RFT."""
    t_max = min(5 * isotope.half_life, 1e8)

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    ax = axes[0]
    scenarios = [
        (0.0, 0.0, 'Kein Feld (Standard)', 'black', '--'),
        (1e12, 0.0, 'Φ=10¹², Δφ=0 (Resonanz)', 'red', '-'),
        (1e12, PI/2, 'Φ=10¹², Δφ=π/2', 'orange', '-'),
        (1e12, PI, 'Φ=10¹², Δφ=π (Anti)', 'blue', '-'),
    ]

    for flux, dp, label, color, ls in scenarios:
        result = simulate_decay(isotope, t_max,
                                 photon_flux=flux, delta_phi=dp)
        ax.plot(result['t_years'] / isotope.half_life,
                result['N_rft' if flux > 0 else 'N_standard'],
                color=color, linestyle=ls, label=label)

    ax.set_xlabel(f't / t½ (t½ = {isotope.half_life:.4g} Jahre)')
    ax.set_ylabel('N(t) / N₀')
    ax.set_title(f'Zerfall: {isotope.name} (κ=1)')
    ax.legend(fontsize=8)
    ax.set_xlim(0, 5)
    ax.set_ylim(0, 1)
    ax.grid(True, alpha=0.3)

    ax = axes[1]
    fluxes = np.logspace(8, 16, 100)
    t_half_ratios = []
    for flux in fluxes:
        lam_eff = effective_decay_rate(isotope, delta_phi=0.0,
                                        photon_flux=flux)
        t_half_ratios.append(isotope.lambda_0_per_s / lam_eff)

    ax.semilogx(fluxes, t_half_ratios, 'r-', linewidth=2)
    ax.axhline(1.0, color='k', linestyle='--', alpha=0.5)
    ax.set_xlabel('Photonenfluenz Φ_γ [γ/(cm²·s)]')
    ax.set_ylabel('t½_eff / t½_Standard')
    ax.set_title(f'Halbwertszeit-Reduktion (Δφ=0, κ=1)\n{isotope.name}')
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir,
                f'decay_comparison_{isotope.name}.png'), dpi=150)
    plt.close()
    print(f"  → decay_comparison_{isotope.name}.png")


def plot_flux_scan(output_dir):
    """Plot NEU: λ_eff/λ₀ als Funktion von Φ für alle Isotope."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    fluxes = np.logspace(8, 16, 200)

    # Links: Aktinide
    ax = axes[0]
    colors = ['darkgreen', 'green', 'purple', 'red', 'darkorange', 'blue']
    for iso, color in zip(ALL_ACTINIDES, colors):
        ratios = []
        for flux in fluxes:
            lam_eff = effective_decay_rate(iso, delta_phi=0.0,
                                            photon_flux=flux)
            ratios.append(lam_eff / iso.lambda_0_per_s)
        ax.loglog(fluxes, ratios, color=color, label=iso.name, linewidth=2)

    ax.axhline(1.0, color='k', linestyle='--', alpha=0.5)
    ax.set_xlabel('Photonenfluenz Φ_γ [γ/(cm²·s)]')
    ax.set_ylabel('λ_eff / λ₀')
    ax.set_title('Flussscan: Aktinide (Δφ=0, κ=1)')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(1e8, 1e16)

    # Rechts: Spaltprodukte
    ax = axes[1]
    for iso, color in zip(ALL_FISSION_PRODUCTS, ['brown', 'teal']):
        ratios = []
        for flux in fluxes:
            lam_eff = effective_decay_rate(iso, delta_phi=0.0,
                                            photon_flux=flux)
            ratios.append(lam_eff / iso.lambda_0_per_s)
        ax.loglog(fluxes, ratios, color=color, label=iso.name, linewidth=2)

    ax.axhline(1.0, color='k', linestyle='--', alpha=0.5)
    ax.set_xlabel('Photonenfluenz Φ_γ [γ/(cm²·s)]')
    ax.set_ylabel('λ_eff / λ₀')
    ax.set_title('Flussscan: Spaltprodukte (Δφ=0, κ=1)')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(1e8, 1e16)

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'flux_scan.png'), dpi=150)
    plt.close()
    print(f"  → flux_scan.png")


def plot_energy_balance(output_dir):
    """Plot 4: Energiebilanz – Q-Faktor als Funktion der Fluenz."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    fluxes = np.logspace(8, 16, 200)

    ax = axes[0]
    for iso, color in [(uranium_235, 'green'),
                        (plutonium_239, 'red'),
                        (americium_241, 'blue')]:
        Qs = []
        for flux in fluxes:
            eb = energy_balance(iso, delta_phi=0.0, photon_flux=flux)
            Qs.append(eb['Q_alpha'])
        ax.loglog(fluxes, Qs, color=color, label=iso.name, linewidth=2)

    ax.axhline(1.0, color='k', linestyle='--', alpha=0.5,
               label='Q = 1 (Break-even)')
    ax.set_xlabel('Photonenfluenz Φ_γ [γ/(cm²·s)]')
    ax.set_ylabel('Q = P_out / P_in')
    ax.set_title('Energiebilanz: α-Zerfall\n1 kg Target, Δφ=0')
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(1e8, 1e16)

    ax = axes[1]
    for iso, color in [(uranium_235, 'green'),
                        (plutonium_239, 'red'),
                        (americium_241, 'blue')]:
        if not iso.fissile:
            continue
        Qs = []
        for flux in fluxes:
            eb = energy_balance(iso, delta_phi=0.0, photon_flux=flux)
            Qs.append(eb['Q_fission'])
        ax.loglog(fluxes, Qs, color=color, label=iso.name, linewidth=2)

    ax.axhline(1.0, color='k', linestyle='--', alpha=0.5,
               label='Q = 1 (Break-even)')
    ax.set_xlabel('Photonenfluenz Φ_γ [γ/(cm²·s)]')
    ax.set_ylabel('Q = P_out(Spaltung) / P_in')
    ax.set_title('Energiebilanz: Spaltung (200 MeV/Zerfall)\n'
                 '1 kg Target, Δφ=0')
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(1e8, 1e16)

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'energy_balance.png'), dpi=150)
    plt.close()
    print(f"  → energy_balance.png")


def print_summary_table():
    """Druckt die vollständige Ergebnistabelle für alle Isotope."""
    print("\n" + "=" * 90)
    print("ERGEBNISTABELLE: Alle Isotope bei Φ = 10¹² γ/(cm²·s), Δφ = 0, κ = 1")
    print("=" * 90)
    print(f"{'Isotop':<16} {'E_GDR':>7} {'f_GDR':>12} {'λ₀ (1/s)':>12} "
          f"{'λ_eff/λ₀':>10} {'Q_fiss':>10} {'Typ':>6}")
    print("-" * 90)

    for iso in ALL_ISOTOPES:
        lam_eff = effective_decay_rate(iso, delta_phi=0.0, photon_flux=1e12)
        ratio = lam_eff / iso.lambda_0_per_s

        if iso.fissile:
            eb = energy_balance(iso, delta_phi=0.0, photon_flux=1e12)
            q_fiss = eb['Q_fission']
            q_str = f"{q_fiss:.2e}" if q_fiss > 100 else f"{q_fiss:.3f}"
        else:
            q_str = "—"

        print(f"  {iso.name:<14} {iso.E_gdr_centroid:>6.1f}  "
              f"{iso.f_gdr_centroid:>11.3e}  {iso.lambda_0_per_s:>11.3e}  "
              f"{ratio:>9.1f}  {q_str:>9}  {iso.decay_type:>5}")

    print("-" * 90)


def main():
    print("=" * 60)
    print("RESONANZREAKTOR: Publikationslauf V2")
    print("κ = 1 (aus RFT-Grundformel, kein freier Parameter)")
    print(f"Isotope: {len(ALL_ISOTOPES)} "
          f"({len(ALL_ACTINIDES)} Aktinide, "
          f"{len(ALL_FISSION_PRODUCTS)} Spaltprodukte, "
          f"1 Thorium)")
    print("=" * 60)

    output_dir = "figures"
    ensure_dir(output_dir)

    # Hauptisotope für Detailplots
    detail_isotopes = [uranium_235, plutonium_239, americium_241,
                       cesium_137]

    # 1. Isotopendaten
    print("\n=== 1. Isotopendaten ===\n")
    for iso in ALL_ISOTOPES:
        iso.info()
        print()

    # 2. Energiescans
    print("=== 2. Energiescans ===")
    for iso in detail_isotopes:
        plot_energy_scan(iso, output_dir)

    # 3. Phasenscans
    print("\n=== 3. Phasenscans ===")
    for iso in detail_isotopes:
        plot_phase_scan(iso, output_dir)

    # 4. Zerfallsvergleiche
    print("\n=== 4. Zerfallsvergleiche ===")
    for iso in detail_isotopes:
        plot_decay_comparison(iso, output_dir)

    # 5. Flussscan (NEU)
    print("\n=== 5. Flussscan ===")
    plot_flux_scan(output_dir)

    # 6. Energiebilanz
    print("\n=== 6. Energiebilanz ===")
    plot_energy_balance(output_dir)

    # 7. Zusammenfassung
    print_summary_table()

    print(f"\n{'=' * 60}")
    print("Herleitung: ε(Δφ) = η(Δφ) = cos²(Δφ/2) → κ = 1")
    print("Kein freier Parameter.")
    print(f"Plots gespeichert unter: {output_dir}/")
    print("Fertig.")


if __name__ == "__main__":
    main()