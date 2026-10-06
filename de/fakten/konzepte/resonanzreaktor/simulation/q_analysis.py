# q_analysis.py
# © Dominic-René Schu, 2025/2026 – Resonanzfeldtheorie
from __future__ import annotations
# Q > 1 Analyse: Unter welchen Bedingungen liefert der
# Resonanzreaktor netto Energie?
#
# Erkenntnis: Q ist fluenzunabhängig (Φ kürzt sich).
# Q hängt ab von:
#   - Targetdicke d (Flächendichte)
#   - Neutronenmultiplikation k (sekundäre Spaltungen)
#   - Photonenabsorptionseffizienz (nicht jedes γ trifft einen Kern)
#   - Phasenkohärenz η

import numpy as np
import matplotlib.pyplot as plt
import os
from material import (plutonium_239, americium_241,
                       uranium_235, PI, MEV_TO_J)
from resonance import (coupling_efficiency, effective_decay_rate,
                        energy_balance)


def ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


# ============================================================
# 1. Analytische Q-Formel
# ============================================================

def Q_analytical(isotope: Isotope, E_decay_MeV: float, target_thickness_cm: float = 1.0,
                 density_g_cm3: float = 19.1, delta_phi: float = 0.0, k_mult: float = 1.0) -> float:
    """
    Analytischer Q-Faktor.
    
    Q = η · σ · n · d · (E_decay / E_γ) · k_mult
    
    wobei:
    - η = cos²(Δφ/2): Kopplungseffizienz
    - σ: GDR-Wirkungsquerschnitt am Zentroid (cm²)
    - n = ρ · N_A / A: Kerndichte (1/cm³)
    - d: Targetdicke (cm)
    - E_decay: Energie pro Zerfall (Spaltung: ~200 MeV)
    - E_γ: Photonenenergie (GDR-Zentroid)
    - k_mult: Neutronenmultiplikationsfaktor
      (k=1: nur Photospaltung, k>1: sekundäre Neutronen
       induzieren weitere Spaltungen)
    
    Args:
        isotope: Isotope-Objekt
        E_decay_MeV: Energie pro Zerfall/Spaltung in MeV
        target_thickness_cm: Targetdicke in cm
        density_g_cm3: Dichte in g/cm³
        delta_phi: Phasendifferenz
        k_mult: Neutronenmultiplikationsfaktor
    
    Returns:
        Q-Faktor (dimensionslos)
    """
    N_A = 6.02214076e23
    
    # Kerndichte
    n = density_g_cm3 * N_A / isotope.A  # 1/cm³
    
    # Kopplungseffizienz
    eta = coupling_efficiency(delta_phi)
    
    # Wirkungsquerschnitt am GDR-Zentroid
    sigma_mb = isotope.gdr_cross_section(isotope.E_gdr_centroid)
    sigma_cm2 = sigma_mb * 1e-27
    
    # Energieverhältnis
    energy_ratio = E_decay_MeV / isotope.E_gdr_centroid
    
    # Q-Faktor
    Q = eta * sigma_cm2 * n * target_thickness_cm * energy_ratio * k_mult
    
    return Q


def Q_with_absorption(isotope: Isotope, E_decay_MeV: float, target_thickness_cm: float = 1.0,
                       density_g_cm3: float = 19.1, delta_phi: float = 0.0, k_mult: float = 1.0) -> dict[str, float]:
    """
    Q-Faktor mit Photonenabsorption im Target.
    
    Nicht jedes Photon wird absorbiert. Die Absorptionswahrscheinlichkeit
    für ein einzelnes Photon in einer Schicht der Dicke d ist:
    
    P_abs = 1 - exp(-μ·d)
    
    wobei μ = n · σ_total der lineare Absorptionskoeffizient ist.
    σ_total ≈ σ_GDR am Zentroid (dominanter Beitrag bei 12-15 MeV).
    
    Q_eff = P_abs · (E_decay / E_γ) · k_mult · η
    
    Das ist der physikalisch korrektere Ausdruck.
    """
    N_A = 6.02214076e23
    n = density_g_cm3 * N_A / isotope.A
    eta = coupling_efficiency(delta_phi)
    
    sigma_mb = isotope.gdr_cross_section(isotope.E_gdr_centroid)
    sigma_cm2 = sigma_mb * 1e-27
    
    # Linearer Absorptionskoeffizient
    mu = n * sigma_cm2  # 1/cm
    
    # Absorptionswahrscheinlichkeit
    P_abs = 1.0 - np.exp(-mu * target_thickness_cm)
    
    # Mittlere freie Weglänge
    mfp = 1.0 / mu if mu > 0 else np.inf
    
    # Energieverhältnis
    energy_ratio = E_decay_MeV / isotope.E_gdr_centroid
    
    Q = P_abs * energy_ratio * k_mult * eta
    
    return {
        'Q': Q,
        'P_abs': P_abs,
        'mu': mu,
        'mfp_cm': mfp,
        'n': n,
        'sigma_cm2': sigma_cm2,
        'eta': eta,
        'energy_ratio': energy_ratio,
        'k_mult': k_mult,
    }


# ============================================================
# 2. Parameterstudien
# ============================================================

def scan_thickness(isotope: Isotope, E_decay_MeV: float, density_g_cm3: float,
                   d_range_cm: tuple[float, float] = (0.01, 100), n_points: int = 200,
                   k_mult: float = 1.0, delta_phi: float = 0.0) -> tuple[np.ndarray, list[dict[str, float]]]:
    """Q als Funktion der Targetdicke."""
    d_values = np.logspace(np.log10(d_range_cm[0]),
                            np.log10(d_range_cm[1]), n_points)
    results = []
    for d in d_values:
        r = Q_with_absorption(isotope, E_decay_MeV,
                               target_thickness_cm=d,
                               density_g_cm3=density_g_cm3,
                               delta_phi=delta_phi,
                               k_mult=k_mult)
        results.append(r)
    
    return d_values, results


def scan_k_mult(isotope: Isotope, E_decay_MeV: float, density_g_cm3: float,
                target_thickness_cm: float = 10.0,
                k_range: tuple[float, float] = (1.0, 3.0), n_points: int = 200,
                delta_phi: float = 0.0) -> tuple[np.ndarray, list[dict[str, float]]]:
    """Q als Funktion des Neutronenmultiplikationsfaktors."""
    k_values = np.linspace(k_range[0], k_range[1], n_points)
    results = []
    for k in k_values:
        r = Q_with_absorption(isotope, E_decay_MeV,
                               target_thickness_cm=target_thickness_cm,
                               density_g_cm3=density_g_cm3,
                               delta_phi=delta_phi,
                               k_mult=k)
        results.append(r)
    
    return k_values, results


def scan_phase_and_thickness(isotope: Isotope, E_decay_MeV: float, density_g_cm3: float,
                              k_mult: float = 1.5) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Q als 2D-Funktion von Δφ und Targetdicke."""
    d_values = np.logspace(-1, 2, 100)  # 0.1 - 100 cm
    phi_values = np.linspace(0, PI, 50)
    
    Q_grid = np.zeros((len(phi_values), len(d_values)))
    
    for i, phi in enumerate(phi_values):
        for j, d in enumerate(d_values):
            r = Q_with_absorption(isotope, E_decay_MeV,
                                   target_thickness_cm=d,
                                   density_g_cm3=density_g_cm3,
                                   delta_phi=phi,
                                   k_mult=k_mult)
            Q_grid[i, j] = r['Q']
    
    return d_values, phi_values, Q_grid


# ============================================================
# 3. Plots
# ============================================================

def plot_q_vs_thickness(output_dir: str) -> None:
    """Q(d) für verschiedene k_mult."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    # U-235 (ρ = 19.1 g/cm³)
    ax = axes[0]
    for k, ls, label in [(1.0, '--', 'k=1.0 (nur Photospaltung)'),
                           (1.2, '-.', 'k=1.2'),
                           (1.5, '-', 'k=1.5'),
                           (2.0, '-', 'k=2.0'),
                           (2.5, '-', 'k=2.5')]:
        d_vals, results = scan_thickness(
            uranium_235, 200.0, 19.1, k_mult=k)
        Qs = [r['Q'] for r in results]
        ax.semilogx(d_vals, Qs, ls, label=label, linewidth=2)
    
    ax.axhline(1.0, color='k', linestyle=':', alpha=0.7,
               label='Q = 1 (Break-even)')
    ax.set_xlabel('Targetdicke d (cm)')
    ax.set_ylabel('Q = P_out / P_in')
    ax.set_title('U-235: Q vs. Targetdicke\n'
                 'E_Spaltung = 200 MeV, Δφ = 0, ρ = 19.1 g/cm³')
    ax.legend(fontsize=8)
    ax.set_xlim(0.01, 100)
    ax.set_ylim(0, 50)
    ax.grid(True, alpha=0.3)
    
    # Pu-239 (ρ = 19.8 g/cm³)
    ax = axes[1]
    for k, ls, label in [(1.0, '--', 'k=1.0 (nur Photospaltung)'),
                           (1.2, '-.', 'k=1.2'),
                           (1.5, '-', 'k=1.5'),
                           (2.0, '-', 'k=2.0'),
                           (2.5, '-', 'k=2.5')]:
        d_vals, results = scan_thickness(
            plutonium_239, 200.0, 19.8, k_mult=k)
        Qs = [r['Q'] for r in results]
        ax.semilogx(d_vals, Qs, ls, label=label, linewidth=2)
    
    ax.axhline(1.0, color='k', linestyle=':', alpha=0.7,
               label='Q = 1 (Break-even)')
    ax.set_xlabel('Targetdicke d (cm)')
    ax.set_ylabel('Q = P_out / P_in')
    ax.set_title('Pu-239: Q vs. Targetdicke\n'
                 'E_Spaltung = 200 MeV, Δφ = 0, ρ = 19.8 g/cm³')
    ax.legend(fontsize=8)
    ax.set_xlim(0.01, 100)
    ax.set_ylim(0, 50)
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'q_vs_thickness.png'), dpi=150)
    plt.close()
    print("  → q_vs_thickness.png")


def plot_q_vs_k(output_dir: str) -> None:
    """Q(k_mult) für verschiedene Targetdicken."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    # U-235
    ax = axes[0]
    for d, color, label in [(1.0, 'blue', 'd = 1 cm'),
                              (5.0, 'green', 'd = 5 cm'),
                              (10.0, 'orange', 'd = 10 cm'),
                              (20.0, 'red', 'd = 20 cm'),
                              (50.0, 'darkred', 'd = 50 cm')]:
        k_vals, results = scan_k_mult(
            uranium_235, 200.0, 19.1,
            target_thickness_cm=d)
        Qs = [r['Q'] for r in results]
        ax.plot(k_vals, Qs, color=color, label=label, linewidth=2)
    
    ax.axhline(1.0, color='k', linestyle=':', alpha=0.7)
    ax.set_xlabel('Neutronenmultiplikationsfaktor k')
    ax.set_ylabel('Q')
    ax.set_title('U-235: Q vs. k\nΔφ = 0')
    ax.legend(fontsize=9)
    ax.set_xlim(1, 3)
    ax.grid(True, alpha=0.3)
    
    # Pu-239
    ax = axes[1]
    for d, color, label in [(1.0, 'blue', 'd = 1 cm'),
                              (5.0, 'green', 'd = 5 cm'),
                              (10.0, 'orange', 'd = 10 cm'),
                              (20.0, 'red', 'd = 20 cm'),
                              (50.0, 'darkred', 'd = 50 cm')]:
        k_vals, results = scan_k_mult(
            plutonium_239, 200.0, 19.8,
            target_thickness_cm=d)
        Qs = [r['Q'] for r in results]
        ax.plot(k_vals, Qs, color=color, label=label, linewidth=2)
    
    ax.axhline(1.0, color='k', linestyle=':', alpha=0.7)
    ax.set_xlabel('Neutronenmultiplikationsfaktor k')
    ax.set_ylabel('Q')
    ax.set_title('Pu-239: Q vs. k\nΔφ = 0')
    ax.legend(fontsize=9)
    ax.set_xlim(1, 3)
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'q_vs_k_mult.png'), dpi=150)
    plt.close()
    print("  → q_vs_k_mult.png")


def plot_q_heatmap(output_dir: str) -> None:
    """Q als 2D-Heatmap: Δφ vs. Targetdicke."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    for ax, iso, rho, title in [
        (axes[0], uranium_235, 19.1, 'U-235'),
        (axes[1], plutonium_239, 19.8, 'Pu-239')
    ]:
        d_vals, phi_vals, Q_grid = scan_phase_and_thickness(
            iso, 200.0, rho, k_mult=1.5)
        
        im = ax.pcolormesh(d_vals, phi_vals / PI, Q_grid,
                            shading='auto', cmap='RdYlGn',
                            vmin=0, vmax=max(5, np.max(Q_grid) * 0.8))
        ax.set_xscale('log')
        ax.set_xlabel('Targetdicke d (cm)')
        ax.set_ylabel('Δφ / π')
        ax.set_title(f'{title}: Q(d, Δφ)\nk=1.5, E_Spaltung=200 MeV')
        
        # Q=1 Konturlinie
        cs = ax.contour(d_vals, phi_vals / PI, Q_grid,
                         levels=[1.0], colors='black',
                         linewidths=2, linestyles='--')
        ax.clabel(cs, fmt='Q=%.0f', fontsize=10)
        
        plt.colorbar(im, ax=ax, label='Q')
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'q_heatmap.png'), dpi=150)
    plt.close()
    print("  → q_heatmap.png")


def plot_break_even_curve(output_dir: str) -> None:
    """Minimale Targetdicke für Q=1 als Funktion von k."""
    fig, ax = plt.subplots(1, 1, figsize=(8, 6))
    
    k_values = np.linspace(1.0, 3.0, 100)
    
    for iso, rho, color, label in [
        (uranium_235, 19.1, 'green', 'U-235'),
        (plutonium_239, 19.8, 'red', 'Pu-239')
    ]:
        d_breakeven = []
        for k in k_values:
            # Binäre Suche nach d bei dem Q = 1
            d_lo, d_hi = 0.001, 1000
            for _ in range(100):
                d_mid = (d_lo + d_hi) / 2
                r = Q_with_absorption(iso, 200.0,
                                       target_thickness_cm=d_mid,
                                       density_g_cm3=rho,
                                       k_mult=k)
                if r['Q'] < 1.0:
                    d_lo = d_mid
                else:
                    d_hi = d_mid
            d_breakeven.append(d_mid)
        
        ax.semilogy(k_values, d_breakeven, color=color,
                     label=label, linewidth=2)
    
    ax.set_xlabel('Neutronenmultiplikationsfaktor k')
    ax.set_ylabel('Minimale Targetdicke für Q = 1 (cm)')
    ax.set_title('Break-even-Kurve: Minimale Targetdicke\n'
                 'für Netto-Energiegewinn (Δφ = 0)')
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(1, 3)
    ax.set_ylim(0.01, 1000)
    
    # Annotationen
    ax.axhline(10, color='gray', linestyle=':', alpha=0.5)
    ax.text(2.5, 12, 'typische Targetgröße\n(~10 cm)', fontsize=9,
            color='gray', ha='center')
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'break_even_curve.png'), dpi=150)
    plt.close()
    print("  → break_even_curve.png")


# ============================================================
# Hauptlauf
# ============================================================

def main() -> None:
    print("=" * 60)
    print("Q > 1 ANALYSE: Resonanzreaktor")
    print("Unter welchen Bedingungen: Netto-Energiegewinn?")
    print("=" * 60)
    
    output_dir = "figures"
    ensure_dir(output_dir)
    
    # --- Analytische Ergebnisse ---
    print("\n=== 1. Physikalische Grundgrößen ===\n")
    
    for iso, rho, name in [
        (uranium_235, 19.1, "U-235"),
        (plutonium_239, 19.8, "Pu-239")
    ]:
        N_A = 6.02214076e23
        n = rho * N_A / iso.A
        sigma_mb = iso.gdr_cross_section(iso.E_gdr_centroid)
        sigma_cm2 = sigma_mb * 1e-27
        mu = n * sigma_cm2
        mfp = 1.0 / mu
        
        print(f"  {name} (ρ = {rho} g/cm³):")
        print(f"    Kerndichte n:         {n:.3e} /cm³")
        print(f"    σ_GDR(Zentroid):      {sigma_mb:.0f} mb "
              f"= {sigma_cm2:.3e} cm²")
        print(f"    μ = n·σ:              {mu:.3e} /cm")
        print(f"    Mittlere freie Wegl.: {mfp:.1f} cm")
        print(f"    P_abs (1 cm):         "
              f"{1-np.exp(-mu*1):.6f}")
        print(f"    P_abs (10 cm):        "
              f"{1-np.exp(-mu*10):.5f}")
        print(f"    P_abs (100 cm):       "
              f"{1-np.exp(-mu*100):.4f}")
        print(f"    E_Spaltung/E_γ:       "
              f"{200.0/iso.E_gdr_centroid:.1f}")
        print()
    
    # --- Q-Tabelle für verschiedene Szenarien ---
    print("=== 2. Q-Faktor: Parameterstudie ===\n")
    print(f"  {'Isotop':<10} {'d (cm)':<8} {'k':<6} "
          f"{'P_abs':<10} {'Q':<10} {'Status'}")
    print("  " + "-" * 60)
    
    for iso, rho in [(uranium_235, 19.1), (plutonium_239, 19.8)]:
        for d in [1, 5, 10, 20, 50]:
            for k in [1.0, 1.5, 2.0]:
                r = Q_with_absorption(iso, 200.0,
                                       target_thickness_cm=d,
                                       density_g_cm3=rho,
                                       k_mult=k)
                status = "✓ Q>1" if r['Q'] > 1.0 else "  Q<1"
                print(f"  {iso.name:<10} {d:<8} {k:<6.1f} "
                      f"{r['P_abs']:<10.6f} {r['Q']:<10.3f} {status}")
        print()
    
    # --- Plots ---
    print("=== 3. Plots ===")
    plot_q_vs_thickness(output_dir)
    plot_q_vs_k(output_dir)
    plot_q_heatmap(output_dir)
    plot_break_even_curve(output_dir)
    
    # --- Zusammenfassung ---
    print("\n" + "=" * 60)
    print("ZUSAMMENFASSUNG: Q > 1 Bedingungen")
    print("=" * 60)
    
    print("""
  Schlüsselerkenntnis: Q ist FLUENZUNABHÄNGIG.
  Φ_γ kürzt sich in P_out/P_in heraus.
  
  Q hängt ab von:
    1. Absorptionswahrscheinlichkeit P_abs = 1 - exp(-n·σ·d)
    2. Energieverhältnis E_decay / E_γ
    3. Neutronenmultiplikation k
    4. Phasenkohärenz η(Δφ)
    
  Für Q > 1 (Netto-Energiegewinn) braucht man:
    - Spaltbare Isotope (E_Spaltung ≈ 200 MeV >> E_γ ≈ 13 MeV)
    - Ausreichende Targetdicke (d >> mfp für hohe P_abs)
    - Neutronenmultiplikation k > 1 (sekundäre Spaltungen)
    - Phasenkohärenz Δφ → 0 (η → 1)
    
  Kritische Erkenntnis:
    Die mittlere freie Weglänge für GDR-Photonen in Aktiniden
    ist ~100 cm. D.h. bei 1 cm Target absorbiert nur ~1% der
    Photonen. Erst bei d ~ 100 cm wird P_abs signifikant.
    
    ABER: Mit Neutronenmultiplikation (k > 1) reichen dünnere
    Targets, weil jede Photospaltung ~2.5 Neutronen freisetzt,
    die weitere Spaltungen induzieren.
""")
    
    print("Plots gespeichert unter:", output_dir)
    print("Fertig.")


if __name__ == "__main__":
    main()