# run.py
# © Dominic-René Schu, 2025/2026 – Resonanzfeldtheorie
# Resonanzreaktor: Publikationslauf
#
# Erzeugt:
# 1. Isotopendaten und RFT-Frequenzen
# 2. Energiescan: GDR-Profil mit/ohne Phasenkohärenz
# 3. Phasenscan: λ_eff(Δφ) – analog zu FLRW
# 4. Zerfallsvergleich: Standard vs. RFT
# 5. Alle Plots als PNG

import numpy as np
import matplotlib.pyplot as plt
import os
from material import (plutonium_239, americium_241,
                       uranium_235, thorium_232, PI)
from resonance import (simulate_decay, phase_scan, energy_scan,
                        coupling_efficiency, effective_decay_rate)


def ensure_dir(path):
    os.makedirs(path, exist_ok=True)


def plot_energy_scan(isotope, output_dir):
    """Plot 1: GDR-Wirkungsquerschnitt mit RFT-Korrektur."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # Links: σ(E) für verschiedene Phasen
    ax = axes[0]
    for dp, label, color in [(0, 'Δφ=0 (Resonanz)', 'red'),
                              (PI/2, 'Δφ=π/2', 'orange'),
                              (PI, 'Δφ=π (Anti)', 'blue')]:
        result = energy_scan(isotope, delta_phi=dp)
        ax.plot(result['E_gamma_MeV'], result['sigma_rft_mb'],
                color=color, label=f'{label}, η={result["eta"]:.2f}')
    
    # Standard (ohne RFT)
    result_std = energy_scan(isotope, delta_phi=PI)  # η=0
    ax.plot(result_std['E_gamma_MeV'], result_std['sigma_standard_mb'],
            'k--', label='Standard (ohne RFT)', linewidth=1)
    
    ax.set_xlabel('E_γ (MeV)')
    ax.set_ylabel('σ (mb)')
    ax.set_title(f'GDR-Wirkungsquerschnitt: {isotope.name}')
    ax.legend(fontsize=8)
    ax.set_xlim(5, 25)
    ax.grid(True, alpha=0.3)
    
    # GDR-Peak-Markierungen
    for E in isotope.E_gdr_peaks:
        ax.axvline(E, color='gray', linestyle=':', alpha=0.5)
    
    # Rechts: Verhältnis σ_RFT / σ_Standard
    ax = axes[1]
    result_res = energy_scan(isotope, delta_phi=0)
    ratio = result_res['sigma_rft_mb'] / result_res['sigma_standard_mb']
    ax.plot(result_res['E_gamma_MeV'], ratio, 'r-')
    ax.axhline(1.0, color='k', linestyle='--', alpha=0.5)
    ax.set_xlabel('E_γ (MeV)')
    ax.set_ylabel('σ_RFT / σ_Standard')
    ax.set_title(f'RFT-Verstärkung bei Δφ=0: {isotope.name}')
    ax.set_xlim(5, 25)
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, f'energy_scan_{isotope.name}.png'),
                dpi=150)
    plt.close()
    print(f"  → energy_scan_{isotope.name}.png")


def plot_phase_scan(isotope, output_dir):
    """Plot 2: Phasenscan – analog zu FLRW."""
    result = phase_scan(isotope, n_phases=100, photon_flux=1e12)
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # Links: η(Δφ) und λ_eff/λ₀
    ax = axes[0]
    ax.plot(result['delta_phi'] / PI, result['eta'],
            'b-', label='η(Δφ) = cos²(Δφ/2)', linewidth=2)
    ax.set_xlabel('Δφ / π')
    ax.set_ylabel('η (Kopplungseffizienz)')
    ax.set_title(f'Kopplungseffizienz: {isotope.name}')
    ax.legend()
    ax.set_xlim(0, 2)
    ax.grid(True, alpha=0.3)
    
    # Rechts: λ_eff / λ₀
    ax = axes[1]
    ax.plot(result['delta_phi'] / PI, result['ratio'],
            'r-', linewidth=2)
    ax.axhline(1.0, color='k', linestyle='--', alpha=0.5,
               label='Standardmodell (λ₀)')
    ax.set_xlabel('Δφ / π')
    ax.set_ylabel('λ_eff / λ₀')
    ax.set_title(f'Effektive Zerfallsrate: {isotope.name}\n'
                 f'Φ_γ = 10¹² γ/(cm²·s)')
    ax.legend()
    ax.set_xlim(0, 2)
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, f'phase_scan_{isotope.name}.png'),
                dpi=150)
    plt.close()
    print(f"  → phase_scan_{isotope.name}.png")


def plot_decay_comparison(isotope, output_dir):
    """Plot 3: Zerfallsvergleich Standard vs. RFT."""
    # Zeitraum: 5 Halbwertszeiten
    t_max = 5 * isotope.half_life
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # Links: N(t) für verschiedene Szenarien
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
    
    ax.set_xlabel(f't / t½ (t½ = {isotope.half_life:.0f} Jahre)')
    ax.set_ylabel('N(t) / N₀')
    ax.set_title(f'Zerfall: {isotope.name}')
    ax.legend(fontsize=8)
    ax.set_xlim(0, 5)
    ax.set_ylim(0, 1)
    ax.grid(True, alpha=0.3)
    
    # Rechts: Halbwertszeit-Reduktion als Funktion der Fluenz
    ax = axes[1]
    fluxes = np.logspace(8, 16, 100)
    t_half_ratios = []
    
    for flux in fluxes:
        lam_eff = effective_decay_rate(isotope, delta_phi=0.0,
                                        photon_flux=flux)
        lam_0 = isotope.decay_constant / (365.25 * 24 * 3600)
        t_half_ratios.append(lam_0 / lam_eff)
    
    ax.semilogx(fluxes, t_half_ratios, 'r-', linewidth=2)
    ax.axhline(1.0, color='k', linestyle='--', alpha=0.5)
    ax.set_xlabel('Photonenfluenz Φ_γ [γ/(cm²·s)]')
    ax.set_ylabel('t½_eff / t½_Standard')
    ax.set_title(f'Halbwertszeit-Reduktion bei Resonanz (Δφ=0)\n'
                 f'{isotope.name}')
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir,
                f'decay_comparison_{isotope.name}.png'), dpi=150)
    plt.close()
    print(f"  → decay_comparison_{isotope.name}.png")


def main():
    print("=" * 60)
    print("RESONANZREAKTOR: Publikationslauf")
    print("RFT-fundierte Simulation resonanter Transmutation")
    print("=" * 60)
    
    output_dir = "figures"
    ensure_dir(output_dir)
    
    isotopes = [uranium_235, plutonium_239, americium_241]
    
    # --- 1. Isotopendaten ---
    print("\n=== 1. Isotopendaten mit RFT-Frequenzen ===\n")
    for iso in isotopes:
        iso.info()
        print()
    
    # --- 2. Energiescans ---
    print("=== 2. Energiescans (GDR-Profile) ===")
    for iso in isotopes:
        plot_energy_scan(iso, output_dir)
    
    # --- 3. Phasenscans ---
    print("\n=== 3. Phasenscans (η → λ_eff) ===")
    for iso in isotopes:
        plot_phase_scan(iso, output_dir)
    
    # --- 4. Zerfallsvergleiche ---
    print("\n=== 4. Zerfallsvergleiche (Standard vs. RFT) ===")
    for iso in isotopes:
        plot_decay_comparison(iso, output_dir)
    
    # --- 5. Zusammenfassung ---
    print("\n" + "=" * 60)
    print("ZUSAMMENFASSUNG")
    print("=" * 60)
    
    print("\nRFT-Vorhersage (falsifizierbar):")
    print("  σ_coh > σ_incoh bei gleicher Photonenfluenz")
    print("  am GDR-Peak der Aktiniden (12-15 MeV)")
    print()
    
    for iso in isotopes:
        lam_0 = iso.decay_constant / (365.25 * 24 * 3600)
        lam_res = effective_decay_rate(iso, delta_phi=0.0,
                                        photon_flux=1e12)
        lam_anti = effective_decay_rate(iso, delta_phi=PI,
                                         photon_flux=1e12)
        print(f"  {iso.name}:")
        print(f"    GDR-Zentroid: {iso.E_gdr_centroid:.1f} MeV")
        print(f"    f_RFT: {iso.f_gdr_centroid:.3e} Hz")
        print(f"    λ_eff/λ₀ (Resonanz):     {lam_res/lam_0:.6f}")
        print(f"    λ_eff/λ₀ (Antiresonanz): {lam_anti/lam_0:.6f}")
        print()
    
    print("Plots gespeichert unter:", output_dir)
    print("Fertig.")


if __name__ == "__main__":
    main()