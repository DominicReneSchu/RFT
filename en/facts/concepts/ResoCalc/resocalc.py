# resocalc.py
# © Dominic-René Schu, 2025/2026 — Resonance Field Theory
#
# ResoCalc: Resonance-based engineering tool
#
# Replaces arbitrary assumptions (θ_max, damping, safety factor)
# with physically grounded resonance coupling ε(Δφ).
#
# E = π · ε(Δφ) · ℏ · f, κ = 1
#
# Usage:
#   python resocalc.py                          (Standalone with plot)
#   python resocalc.py --example motor          (Motor shaft)
#   python resocalc.py --example bridge         (Bridge under wind)
#   python resocalc.py --example turbine        (Turbine blade)
#
# In Jupyter notebook:
#   %run resocalc.py --notebook
#
# pip install numpy matplotlib

from __future__ import annotations

from typing import Any

import numpy as np
import matplotlib.pyplot as plt
import os
import sys

PI = np.pi


# ============================================================
# AXIOM 4: Coupling efficiency — the core
# ============================================================

def coupling_efficiency(delta_phi: float | np.ndarray) -> float | np.ndarray:
    """
    ε(Δφ) = cos²(Δφ/2)

    The universal coupling efficiency of Resonance Field Theory.
    Replaces the estimated deflection θ_max in engineering mechanics.

    Δφ = 0:    ε = 1.0 — Perfect coupling (resonance)
    Δφ = π/2:  ε = 0.5 — Half coupling
    Δφ = π:    ε = 0.0 — No coupling (anti-phase)
    """
    return np.cos(delta_phi / 2.0) ** 2


def resonance_amplification(f: float | np.ndarray, f_r: float, damping: float = 0.0001) -> float | np.ndarray:
    """
    Resonance amplification V(f, f_r).

    V = 1 / |1 - (f/f_r)²|

    At f → f_r: V → ∞ (theoretically), limited by damping.
    Conventionally, a safety factor is estimated here.
    ResoCalc calculates V directly from the frequency ratio.
    """
    r = f / f_r
    delta = np.abs(1 - r**2)
    # Physical limitation instead of arbitrary singularity avoidance
    delta = np.maximum(delta, damping)
    return 1.0 / delta


# ============================================================
# CONVENTIONAL CALCULATION
# ============================================================

def torque_conventional(m: float, l: float, f: float | np.ndarray, theta_max: float) -> float | np.ndarray:
    """
    Conventional effective torque.

    M_conv = J · ω² · θ_max / √2

    Problem: θ_max is ESTIMATED, not calculated.
    Different engineers → different results.
    """
    J = m * l**2
    omega = 2 * PI * f
    return J * omega**2 * theta_max / np.sqrt(2)


# ============================================================
# RESOCALC CALCULATION
# ============================================================

def torque_resocalc(m: float, l: float, f: float | np.ndarray, f_r: float, epsilon: float) -> float | np.ndarray:
    """
    Resonance-logical effective torque.

    M_reso = ½ · m · l² · ω² · V(f, f_r) · ε

    No estimated parameter. Everything physically grounded:
    - V(f, f_r): Resonance amplification from the frequency ratio
    - ε: Coupling efficiency (0 ≤ ε ≤ 1)
    """
    J = 0.5 * m * l**2
    omega = 2 * PI * f
    V = resonance_amplification(f, f_r)
    return J * omega**2 * V * epsilon


# ============================================================
# EXAMPLE SCENARIOS
# ============================================================

EXAMPLES = {
    'standard': {
        'name': 'Standard Torque',
        'description': 'Rotating mass on a shaft',
        'm': 2.0,          # kg
        'l': 1.0,          # m
        'f': 10.0,         # Hz (excitation)
        'f_r': 5.0,        # Hz (resonance)
        'epsilon': 0.2,    # Coupling efficiency
        'theta_max': 0.087, # rad (5°, conventionally estimated)
    },
    'motor': {
        'name': 'Motor Shaft (Car)',
        'description': 'Crankshaft of a 4-cylinder engine at 3000 RPM',
        'm': 15.0,         # kg (effective mass)
        'l': 0.15,         # m (crank radius)
        'f': 100.0,        # Hz (2nd order at 3000 rpm)
        'f_r': 85.0,       # Hz (1st bending natural frequency)
        'epsilon': 0.35,
        'theta_max': 0.02,  # rad (conventional)
    },
    'bridge': {
        'name': 'Pedestrian Bridge Under Wind Load',
        'description': 'Suspension bridge, 50m span, periodic gusts',
        'm': 50000.0,      # kg (effective modal mass)
        'l': 25.0,         # m (half span)
        'f': 1.2,          # Hz (gust frequency)
        'f_r': 1.1,        # Hz (1st natural frequency) — critically close!
        'epsilon': 0.15,
        'theta_max': 0.005, # rad (conventional)
    },
    'turbine': {
        'name': 'Turbine Blade',
        'description': 'Gas turbine rotor stage under flow excitation',
        'm': 0.8,          # kg
        'l': 0.25,         # m (blade length)
        'f': 5000.0,       # Hz (nozzle passing frequency)
        'f_r': 4800.0,     # Hz (blade natural frequency)
        'epsilon': 0.08,
        'theta_max': 0.001, # rad (conventional)
    },
}


# ============================================================
# COMPARISON CALCULATION
# ============================================================

def compute_comparison(example: dict[str, Any]) -> dict[str, Any]:
    """
    Performs comparison: Conventional vs. ResoCalc.
    Returns results as a dictionary.
    """
    m = example['m']
    l = example['l']
    f = example['f']
    f_r = example['f_r']
    eps = example['epsilon']
    theta = example['theta_max']

    M_conv = torque_conventional(m, l, f, theta)
    M_reso = torque_resocalc(m, l, f, f_r, eps)

    # Single values at the excitation frequency
    if np.ndim(M_conv) > 0:
        M_conv_val = float(M_conv) if np.ndim(M_conv) == 0 else float(M_conv)
        M_reso_val = float(M_reso) if np.ndim(M_reso) == 0 else float(M_reso)
    else:
        M_conv_val = float(M_conv)
        M_reso_val = float(M_reso)

    V = resonance_amplification(f, f_r)

    return {
        'name': example['name'],
        'description': example['description'],
        'M_conv': M_conv_val,
        'M_reso': M_reso_val,
        'factor': M_reso_val / M_conv_val if M_conv_val > 0 else float('inf'),
        'V': float(V),
        'epsilon': eps,
        'f': f,
        'f_r': f_r,
        'm': m,
        'l': l,
    }


# ============================================================
# VISUALIZATION
# ============================================================

def plot_comparison(example: dict[str, Any], out_dir: str = 'figures') -> str:
    """
    Generates comparison plot: Conventional vs. ResoCalc
    across the entire frequency range.
    """
    os.makedirs(out_dir, exist_ok=True)

    m = example['m']
    l = example['l']
    f_r = example['f_r']
    eps = example['epsilon']
    theta = example['theta_max']

    # Frequency range: 10% to 300% of the resonance frequency
    f_min = max(0.1, f_r * 0.1)
    f_max = f_r * 3.0
    frequencies = np.linspace(f_min, f_max, 500)

    M_conv = torque_conventional(m, l, frequencies, theta)
    M_reso = torque_resocalc(m, l, frequencies, f_r, eps)

    # Clipping for display (resonance peak can become very large)
    M_reso_clip = np.clip(M_reso, 0, np.percentile(M_reso, 98) * 2)

    fig, axes = plt.subplots(2, 1, figsize=(12, 10))

    # Plot 1: Linear comparison
    ax = axes[0]
    ax.plot(frequencies, M_conv, label='Conventional (θ_max estimated)',
            color='blue', lw=2, ls='--')
    ax.plot(frequencies, M_reso_clip,
            label=f'ResoCalc (ε = {eps})', color='red', lw=2)
    ax.axvline(f_r, color='gray', ls=':', lw=1.5,
               label=f'Resonance frequency f_r = {f_r} Hz')
    if example['f'] != f_r:
        ax.axvline(example['f'], color='orange', ls=':', lw=1.5,
                   label=f'Excitation f = {example["f"]} Hz')
    ax.set_xlabel('Frequency (Hz)')
    ax.set_ylabel('Effective Torque (Nm)')
    ax.set_title(f'{example["name"]}: Conventional vs. ResoCalc')
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)

    # Plot 2: Coupling efficiency and resonance amplification
    ax = axes[1]

    # Phase difference as a function of the frequency ratio
    r = frequencies / f_r
    # Modeled phase difference: 0 at resonance, π far away
    delta_phi = np.arctan2(np.abs(1 - r**2), 0.1) * 2
    eps_curve = coupling_efficiency(delta_phi)

    V_curve = resonance_amplification(frequencies, f_r)
    V_norm = V_curve / np.max(V_curve)  # Normalized for display

    ax.plot(frequencies, eps_curve, label='ε(Δφ) Coupling efficiency',
            color='green', lw=2)
    ax.plot(frequencies, V_norm,
            label='V (Resonance amplification, normalized)',
            color='red', lw=2, ls='--')
    ax.fill_between(frequencies, eps_curve, alpha=0.1, color='green')
    ax.axvline(f_r, color='gray', ls=':', lw=1.5)
    ax.set_xlabel('Frequency (Hz)')
    ax.set_ylabel('Normalized Value')
    ax.set_title('Coupling Efficiency ε(Δφ) and Resonance Amplification V')
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0, 1.1)

    fig.suptitle(
        f'ResoCalc: {example["description"]}\n'
        f'E = π · ε(Δφ) · ℏ · f, κ = 1',
        fontsize=11, fontweight='bold')
    plt.tight_layout()

    name = example['name'].lower().replace(' ', '_').replace('(', '').replace(')', '')
    filepath = os.path.join(out_dir, f'resocalc_{name}.png')
    plt.savefig(filepath, dpi=150)
    plt.close()
    print(f"  → {filepath}")
    return filepath


# ============================================================
# JUPYTER NOTEBOOK MODE
# ============================================================

def notebook_mode() -> None:
    """Starts interactive widget in Jupyter notebook."""
    try:
        from ipywidgets import interact, FloatSlider, VBox, HBox, Layout
        from IPython.display import display, Markdown
    except ImportError:
        print("  Jupyter widgets not available.")
        print("  pip install ipywidgets")
        return

    style = {'description_width': '100px'}
    layout = Layout(width='70%')

    def reso_sim(m: float = 2.0, l: float = 1.0, f_r: float = 5.0, coupling: float = 0.2, theta_max: float = 0.087) -> None:
        frequencies = np.linspace(0.5, f_r * 4, 500)

        M_conv = torque_conventional(m, l, frequencies, theta_max)
        M_reso = torque_resocalc(m, l, frequencies, f_r, coupling)
        M_reso_clip = np.clip(M_reso, 0, np.percentile(M_reso, 98) * 2)

        plt.figure(figsize=(11, 6))
        plt.plot(frequencies, M_conv, label='Conventional (θ_max estimated)',
                 color='blue', lw=2, ls='--')
        plt.plot(frequencies, M_reso_clip,
                 label=f'ResoCalc (ε = {coupling:.2f})',
                 color='red', lw=2)
        plt.axvline(f_r, color='gray', ls=':', lw=1.5,
                    label=f'f_r = {f_r:.1f} Hz')
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Effective Torque (Nm)')
        plt.title('ResoCalc vs. Conventional — E = π · ε(Δφ) · ℏ · f')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()

        # Single comparison at f = 2 · f_r
        f_test = 2 * f_r
        M_k = torque_conventional(m, l, f_test, theta_max)
        M_r = torque_resocalc(m, l, f_test, f_r, coupling)
        V = resonance_amplification(f_test, f_r)

        display(Markdown(
            f"**At f = {f_test:.1f} Hz:**\n\n"
            f"| Method | Torque | Basis |\n"
            f"|--------|--------|-------|\n"
            f"| Conventional | {M_k:.1f} Nm | θ_max = {theta_max:.3f} rad |\n"
            f"| ResoCalc | {M_r:.1f} Nm | ε = {coupling:.2f}, V = {V:.1f} |\n"
            f"| **Factor** | **{M_r/M_k:.1f}×** | |\n\n"
            f"Resonance amplification V = {V:.1f} · "
            f"Coupling efficiency ε = {coupling:.2f}"
        ))

    m_s = FloatSlider(value=2.0, min=0.1, max=50.0, step=0.1,
                      description='Mass (kg)', style=style, layout=layout)
    l_s = FloatSlider(value=1.0, min=0.05, max=5.0, step=0.05,
                      description='Length (m)', style=style, layout=layout)
    f_s = FloatSlider(value=5.0, min=0.5, max=100.0, step=0.5,
                      description='f_r (Hz)', style=style, layout=layout)
    k_s = FloatSlider(value=0.2, min=0.01, max=1.0, step=0.01,
                      description='ε (Coupling)', style=style, layout=layout)
    t_s = FloatSlider(value=0.087, min=0.001, max=0.5, step=0.001,
                      description='θ_max (rad)', style=style, layout=layout)

    interact(reso_sim, m=m_s, l=l_s, f_r=f_s, coupling=k_s, theta_max=t_s)


# ============================================================
# MAIN PROGRAM
# ============================================================

def main() -> None:
    print("=" * 60)
    print("RESOCALC: Resonance-Based Engineering Tool")
    print("ε(Δφ) replaces θ_max — Physics instead of estimation")
    print("E = π · ε(Δφ) · ℏ · f, κ = 1")
    print("=" * 60)

    # Arguments
    notebook = '--notebook' in sys.argv
    example_name = 'standard'

    for i, arg in enumerate(sys.argv[1:]):
        if arg == '--example' and i + 2 < len(sys.argv):
            example_name = sys.argv[i + 2]
        if arg in EXAMPLES:
            example_name = arg

    if notebook:
        notebook_mode()
        return

    if example_name == 'all':
        example_list = list(EXAMPLES.keys())
    else:
        if example_name not in EXAMPLES:
            print(f"\n  Unknown example: '{example_name}'")
            print(f"  Available: {', '.join(EXAMPLES.keys())}, all")
            sys.exit(1)
        example_list = [example_name]

    out = 'figures'
    os.makedirs(out, exist_ok=True)

    for name in example_list:
        example = EXAMPLES[name]

        print(f"\n{'─' * 60}")
        print(f"  {example['name']}")
        print(f"  {example['description']}")
        print(f"{'─' * 60}")

        result = compute_comparison(example)

        print(f"\n  Parameters:")
        print(f"    Mass:                {result['m']:.1f} kg")
        print(f"    Length:              {result['l']:.2f} m")
        print(f"    Excitation:          {result['f']:.1f} Hz")
        print(f"    Resonance frequency: {result['f_r']:.1f} Hz")
        print(f"    Coupling ε:          {result['epsilon']:.2f}")

        print(f"\n  Result:")
        print(f"    Conventional:        {result['M_conv']:>12.1f} Nm"
              f"  (θ_max = {example['theta_max']:.4f} rad)")
        print(f"    ResoCalc:            {result['M_reso']:>12.1f} Nm"
              f"  (ε = {result['epsilon']}, V = {result['V']:.1f})")
        print(f"    Factor:              {result['factor']:>12.1f}×")

        if result['factor'] > 2:
            print(f"\n  ⚠ WARNING: Conventional method underestimates"
                  f" the torque by factor {result['factor']:.1f}!")
            print(f"    At resonance this can lead to failure.")

        plot_comparison(example, out)

    # Summary
    if len(example_list) > 1:
        print(f"\n{'=' * 60}")
        print("SUMMARY OF ALL EXAMPLES:")
        print(f"{'=' * 60}")
        print(f"{'Example':30s} {'Conv. (Nm)':>12s} {'Reso (Nm)':>12s}"
              f" {'Factor':>8s}")
        print(f"{'─'*30} {'─'*12} {'─'*12} {'─'*8}")
        for name in example_list:
            result = compute_comparison(EXAMPLES[name])
            print(f"{result['name']:30s} {result['M_conv']:>12.1f}"
                  f" {result['M_reso']:>12.1f} {result['factor']:>7.1f}×")

    print(f"\n{'=' * 60}")
    print(f"""
  RESOCALC — PARADIGM SHIFT:
  ──────────────────────────
  CONVENTIONAL:
    Engineer estimates θ_max → result varies
    At resonance: formula breaks down
    Solution: add safety factors

  RESOCALC:
    ε(Δφ) = cos²(Δφ/2) → physically grounded
    At resonance: V grows large, ε limits
    Result: Realistic, reproducible

  USAGE:
    python resocalc.py                    (Standard)
    python resocalc.py --example motor    (Motor shaft)
    python resocalc.py --example bridge   (Bridge)
    python resocalc.py --example turbine  (Turbine)
    python resocalc.py --example all      (All)
    python resocalc.py --notebook         (Jupyter)

  E = π · ε(Δφ) · ℏ · f, κ = 1
""")


if __name__ == "__main__":
    main()
