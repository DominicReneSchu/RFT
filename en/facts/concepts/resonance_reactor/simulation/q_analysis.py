# q_analysis.py
# © Dominic-René Schu, 2025/2026 – Resonance Field Theory
from __future__ import annotations
# Q > 1 Analysis: Under which conditions does the
# resonance reactor deliver net energy?
#
# Insight: Q is fluence-independent (Φ cancels out).
# Q depends on:
#   - Target thickness d (areal density)
#   - Neutron multiplication k (secondary fissions)
#   - Photon absorption efficiency (not every γ hits a nucleus)
#   - Phase coherence η

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
# 1. Analytical Q formula
# ============================================================

def Q_analytical(isotope: Isotope, E_decay_MeV: float, target_thickness_cm: float = 1.0,
                 density_g_cm3: float = 19.1, delta_phi: float = 0.0, k_mult: float = 1.0) -> float:
    """
    Analytical Q factor.
    
    Q = η · σ · n · d · (E_decay / E_γ) · k_mult
    
    where:
    - η = cos²(Δφ/2): coupling efficiency
    - σ: GDR cross section at centroid (cm²)
    - n = ρ · N_A / A: nuclear density (1/cm³)
    - d: target thickness (cm)
    - E_decay: energy per decay (fission: ~200 MeV)
    - E_γ: photon energy (GDR centroid)
    - k_mult: neutron multiplication factor
      (k=1: photofission only, k>1: secondary neutrons
       induce further fissions)
    
    Args:
        isotope: Isotope object
        E_decay_MeV: Energy per decay/fission in MeV
        target_thickness_cm: Target thickness in cm
        density_g_cm3: Density in g/cm³
        delta_phi: Phase difference
        k_mult: Neutron multiplication factor
    
    Returns:
        Q factor (dimensionless)
    """
    N_A = 6.02214076e23
    
    # Nuclear density
    n = density_g_cm3 * N_A / isotope.A  # 1/cm³
    
    # Coupling efficiency
    eta = coupling_efficiency(delta_phi)
    
    # Cross section at GDR centroid
    sigma_mb = isotope.gdr_cross_section(isotope.E_gdr_centroid)
    sigma_cm2 = sigma_mb * 1e-27
    
    # Energy ratio
    energy_ratio = E_decay_MeV / isotope.E_gdr_centroid
    
    # Q factor
    Q = eta * sigma_cm2 * n * target_thickness_cm * energy_ratio * k_mult
    
    return Q


def Q_with_absorption(isotope: Isotope, E_decay_MeV: float, target_thickness_cm: float = 1.0,
                       density_g_cm3: float = 19.1, delta_phi: float = 0.0, k_mult: float = 1.0) -> dict[str, float]:
    """
    Q factor with photon absorption in the target.
    
    Not every photon is absorbed. The absorption probability
    for a single photon in a layer of thickness d is:
    
    P_abs = 1 - exp(-μ·d)
    
    where μ = n · σ_total is the linear absorption coefficient.
    σ_total ≈ σ_GDR at centroid (dominant contribution at 12-15 MeV).
    
    Q_eff = P_abs · (E_decay / E_γ) · k_mult · η
    
    This is the physically more correct expression.
    """
    N_A = 6.02214076e23
    n = density_g_cm3 * N_A / isotope.A
    eta = coupling_efficiency(delta_phi)
    
    sigma_mb = isotope.gdr_cross_section(isotope.E_gdr_centroid)
    sigma_cm2 = sigma_mb * 1e-27
    
    # Linear absorption coefficient
    mu = n * sigma_cm2  # 1/cm
    
    # Absorption probability
    P_abs = 1.0 - np.exp(-mu * target_thickness_cm)
    
    # Mean free path
    mfp = 1.0 / mu if mu > 0 else np.inf
    
    # Energy ratio
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
# 2. Parameter studies
# ============================================================

def scan_thickness(isotope: Isotope, E_decay_MeV: float, density_g_cm3: float,
                   d_range_cm: tuple[float, float] = (0.01, 100), n_points: int = 200,
                   k_mult: float = 1.0, delta_phi: float = 0.0) -> tuple[np.ndarray, list[dict[str, float]]]:
    """Q as function of target thickness."""
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
    """Q as function of the neutron multiplication factor."""
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
    """Q as 2D function of Δφ and target thickness."""
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
    """Q(d) for various k_mult."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    # U-235 (ρ = 19.1 g/cm³)
    ax = axes[0]
    for k, ls, label in [(1.0, '--', 'k=1.0 (photofission only)'),
                           (1.2, '-.', 'k=1.2'),
                           (1.5, '-', 'k=1.5'),
                           (2.0, '-', 'k=2.0'),
                           (2.5, '-', 'k=2.5')]:
        d_vals, results = scan_thickness(
            uranium_235, 200.0, 19.1, k_mult=k)
        Qs = [r['Q'] for r in results]
        ax.semilogx(d_vals, Qs, ls, label=label, linewidth=2)
    
    ax.axhline(1.0, color='k', linestyle=':', alpha=0.7,
               label='Q = 1 (break-even)')
    ax.set_xlabel('Target thickness d (cm)')
    ax.set_ylabel('Q = P_out / P_in')
    ax.set_title('U-235: Q vs. target thickness\n'
                 'E_fission = 200 MeV, Δφ = 0, ρ = 19.1 g/cm³')
    ax.legend(fontsize=8)
    ax.set_xlim(0.01, 100)
    ax.set_ylim(0, 50)
    ax.grid(True, alpha=0.3)
    
    # Pu-239 (ρ = 19.8 g/cm³)
    ax = axes[1]
    for k, ls, label in [(1.0, '--', 'k=1.0 (photofission only)'),
                           (1.2, '-.', 'k=1.2'),
                           (1.5, '-', 'k=1.5'),
                           (2.0, '-', 'k=2.0'),
                           (2.5, '-', 'k=2.5')]:
        d_vals, results = scan_thickness(
            plutonium_239, 200.0, 19.8, k_mult=k)
        Qs = [r['Q'] for r in results]
        ax.semilogx(d_vals, Qs, ls, label=label, linewidth=2)
    
    ax.axhline(1.0, color='k', linestyle=':', alpha=0.7,
               label='Q = 1 (break-even)')
    ax.set_xlabel('Target thickness d (cm)')
    ax.set_ylabel('Q = P_out / P_in')
    ax.set_title('Pu-239: Q vs. target thickness\n'
                 'E_fission = 200 MeV, Δφ = 0, ρ = 19.8 g/cm³')
    ax.legend(fontsize=8)
    ax.set_xlim(0.01, 100)
    ax.set_ylim(0, 50)
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'q_vs_thickness.png'), dpi=150)
    plt.close()
    print("  → q_vs_thickness.png")


def plot_q_vs_k(output_dir: str) -> None:
    """Q(k_mult) for various target thicknesses."""
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
    ax.set_xlabel('Neutron multiplication factor k')
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
    ax.set_xlabel('Neutron multiplication factor k')
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
    """Q as 2D heatmap: Δφ vs. target thickness."""
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
        ax.set_xlabel('Target thickness d (cm)')
        ax.set_ylabel('Δφ / π')
        ax.set_title(f'{title}: Q(d, Δφ)\nk=1.5, E_fission=200 MeV')
        
        # Q=1 contour line
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
    """Minimum target thickness for Q=1 as function of k."""
    fig, ax = plt.subplots(1, 1, figsize=(8, 6))
    
    k_values = np.linspace(1.0, 3.0, 100)
    
    for iso, rho, color, label in [
        (uranium_235, 19.1, 'green', 'U-235'),
        (plutonium_239, 19.8, 'red', 'Pu-239')
    ]:
        d_breakeven = []
        for k in k_values:
            # Binary search for d where Q = 1
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
    
    ax.set_xlabel('Neutron multiplication factor k')
    ax.set_ylabel('Minimum target thickness for Q = 1 (cm)')
    ax.set_title('Break-even curve: Minimum target thickness\n'
                 'for net energy gain (Δφ = 0)')
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(1, 3)
    ax.set_ylim(0.01, 1000)
    
    # Annotations
    ax.axhline(10, color='gray', linestyle=':', alpha=0.5)
    ax.text(2.5, 12, 'typical target size\n(~10 cm)', fontsize=9,
            color='gray', ha='center')
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'break_even_curve.png'), dpi=150)
    plt.close()
    print("  → break_even_curve.png")


# ============================================================
# Main run
# ============================================================

def main() -> None:
    print("=" * 60)
    print("Q > 1 ANALYSIS: Resonance Reactor")
    print("Under which conditions: Net energy gain?")
    print("=" * 60)
    
    output_dir = "figures"
    ensure_dir(output_dir)
    
    # --- Analytical results ---
    print("\n=== 1. Physical base quantities ===\n")
    
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
        print(f"    Nuclear density n:    {n:.3e} /cm³")
        print(f"    σ_GDR(centroid):      {sigma_mb:.0f} mb "
              f"= {sigma_cm2:.3e} cm²")
        print(f"    μ = n·σ:              {mu:.3e} /cm")
        print(f"    Mean free path:       {mfp:.1f} cm")
        print(f"    P_abs (1 cm):         "
              f"{1-np.exp(-mu*1):.6f}")
        print(f"    P_abs (10 cm):        "
              f"{1-np.exp(-mu*10):.5f}")
        print(f"    P_abs (100 cm):       "
              f"{1-np.exp(-mu*100):.4f}")
        print(f"    E_fission/E_γ:        "
              f"{200.0/iso.E_gdr_centroid:.1f}")
        print()
    
    # --- Q table for various scenarios ---
    print("=== 2. Q factor: Parameter study ===\n")
    print(f"  {'Isotope':<10} {'d (cm)':<8} {'k':<6} "
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
    
    # --- Summary ---
    print("\n" + "=" * 60)
    print("SUMMARY: Q > 1 Conditions")
    print("=" * 60)
    
    print("""
  Key insight: Q is FLUENCE-INDEPENDENT.
  Φ_γ cancels out in P_out/P_in.
  
  Q depends on:
    1. Absorption probability P_abs = 1 - exp(-n·σ·d)
    2. Energy ratio E_decay / E_γ
    3. Neutron multiplication k
    4. Phase coherence η(Δφ)
    
  For Q > 1 (net energy gain) one needs:
    - Fissile isotopes (E_fission ≈ 200 MeV >> E_γ ≈ 13 MeV)
    - Sufficient target thickness (d >> mfp for high P_abs)
    - Neutron multiplication k > 1 (secondary fissions)
    - Phase coherence Δφ → 0 (η → 1)
    
  Critical insight:
    The mean free path for GDR photons in actinides
    is ~100 cm. I.e. with a 1 cm target only ~1% of the
    photons are absorbed. Only at d ~ 100 cm does P_abs
    become significant.
    
    HOWEVER: With neutron multiplication (k > 1) thinner
    targets suffice, because each photofission releases
    ~2.5 neutrons that induce further fissions.
""")
    
    print("Plots saved under:", output_dir)
    print("Done.")


if __name__ == "__main__":
    main()
