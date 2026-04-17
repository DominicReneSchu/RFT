# generate_diagram.py
# © Dominic-René Schu, 2025/2026 – Resonance Field Theory
# Generates the updated resonance reactor schema diagram
from __future__ import annotations

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
import os


def draw_resonance_reactor() -> None:
    fig, ax = plt.subplots(1, 1, figsize=(14, 8))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8)
    ax.set_aspect('equal')
    ax.axis('off')

    # Title
    ax.text(7, 7.6, 'Resonance Reactor', fontsize=20, fontweight='bold',
            ha='center', va='center', family='sans-serif')
    ax.text(7, 7.2, 'Resonantly controlled transmutation (RFT)',
            fontsize=11, ha='center', va='center', style='italic',
            color='gray')

    # === Main components as boxes ===

    box_style = dict(boxstyle="round,pad=0.3", facecolor='white',
                     edgecolor='black', linewidth=1.5)
    box_highlight = dict(boxstyle="round,pad=0.3", facecolor='#FFE0E0',
                         edgecolor='darkred', linewidth=2)
    box_green = dict(boxstyle="round,pad=0.3", facecolor='#E0FFE0',
                     edgecolor='darkgreen', linewidth=1.5)
    box_blue = dict(boxstyle="round,pad=0.3", facecolor='#E0E0FF',
                    edgecolor='darkblue', linewidth=1.5)
    box_orange = dict(boxstyle="round,pad=0.3", facecolor='#FFF0D0',
                      edgecolor='darkorange', linewidth=1.5)

    # 1. FEL (photon source)
    ax.text(2, 5.5, 'FEL / Synchrotron\nPhoton source\nE_γ = 12–16 MeV',
            fontsize=9, ha='center', va='center', bbox=box_blue)

    # 2. Phase control
    ax.text(5.5, 5.5, 'Phase control\nPLL + DRN\nΔφ → 0 (resonance)',
            fontsize=9, ha='center', va='center', bbox=box_orange)

    # 3. Target (resonance chamber)
    ax.text(9, 5.5, 'Resonance chamber\nActinide target\n(Pu-239, Am-241, U-238)',
            fontsize=9, ha='center', va='center', bbox=box_highlight)

    # 4. Energy extraction
    ax.text(12, 5.5, 'Energy\nextraction\n(thermal)',
            fontsize=9, ha='center', va='center', bbox=box_green)

    # 5. Detectors / measurement
    ax.text(9, 3.0, 'Detectors\nα / n / γ_f / fission fragments\n(ELIGANT, Si, HPGe)',
            fontsize=9, ha='center', va='center', bbox=box_style)

    # 6. Fission products
    ax.text(12, 3.0, 'Fission products\n(short-lived, t½ < 30 y)\nCs-137, Sr-90',
            fontsize=9, ha='center', va='center', bbox=box_green)

    # 7. Control / DRN
    ax.text(5.5, 3.0, 'Deep Resonance\nNetwork (DRN)\nReal-time optimization\nf, Δφ, Φ',
            fontsize=9, ha='center', va='center', bbox=box_orange)

    # 8. Electrical output
    ax.text(12, 1.2, 'Electrical output\n~280 MW (75 t Pu)\nor impulse drive\nF = ṁ · v_f · η',
            fontsize=9, ha='center', va='center', bbox=box_green)

    # 9. Fundamental formula
    ax.text(2, 1.2, 'E = π · ε(Δφ) · ℏ · f\nε = η = cos²(Δφ/2)\nκ = 1 (no free parameter)',
            fontsize=10, ha='center', va='center',
            bbox=dict(boxstyle="round,pad=0.4", facecolor='#FFFFF0',
                      edgecolor='black', linewidth=2),
            fontweight='bold', family='monospace')

    # === Arrows ===

    arrow_kw = dict(arrowstyle='->', color='black', linewidth=1.5,
                    connectionstyle='arc3,rad=0')

    # FEL → Phase control
    ax.annotate('', xy=(4.0, 5.5), xytext=(3.2, 5.5),
                arrowprops=arrow_kw)
    ax.text(3.6, 5.85, 'γ beam', fontsize=8, ha='center', color='blue')

    # Phase control → Target
    ax.annotate('', xy=(7.5, 5.5), xytext=(6.8, 5.5),
                arrowprops=arrow_kw)
    ax.text(7.15, 5.85, 'coherent\nΔφ ≈ 0', fontsize=7, ha='center',
            color='darkorange')

    # Target → Energy extraction
    ax.annotate('', xy=(11.0, 5.5), xytext=(10.3, 5.5),
                arrowprops=arrow_kw)
    ax.text(10.65, 5.85, '200 MeV\n/fission', fontsize=7, ha='center',
            color='darkred')

    # Target → Detectors
    ax.annotate('', xy=(9, 3.7), xytext=(9, 4.8),
                arrowprops=arrow_kw)
    ax.text(9.5, 4.25, 'α, n, γ', fontsize=8, ha='center', color='gray')

    # Target → Fission products
    ax.annotate('', xy=(11.0, 3.5), xytext=(10.3, 4.8),
                arrowprops=dict(arrowstyle='->', color='darkgreen',
                                linewidth=1.5))

    # Energy extraction → Electrical output
    ax.annotate('', xy=(12, 1.9), xytext=(12, 2.4),
                arrowprops=arrow_kw)

    # Energy extraction → FEL (feedback)
    ax.annotate('', xy=(2, 4.8), xytext=(12, 4.8),
                arrowprops=dict(arrowstyle='->', color='green',
                                linewidth=1, linestyle='dashed',
                                connectionstyle='arc3,rad=-0.15'))
    ax.text(7, 4.55, 'Self-power supply (feedback)',
            fontsize=7, ha='center', color='green', style='italic')

    # DRN → Phase control (feedback)
    ax.annotate('', xy=(5.5, 4.8), xytext=(5.5, 3.7),
                arrowprops=dict(arrowstyle='->', color='darkorange',
                                linewidth=1.5))

    # DRN → FEL (feedback)
    ax.annotate('', xy=(2, 3.0), xytext=(4.2, 3.0),
                arrowprops=dict(arrowstyle='->', color='darkorange',
                                linewidth=1, linestyle='dashed'))
    ax.text(3.1, 3.25, 'f, Φ control', fontsize=7, ha='center',
            color='darkorange')

    # Detectors → DRN (feedback)
    ax.annotate('', xy=(6.8, 3.0), xytext=(7.6, 3.0),
                arrowprops=dict(arrowstyle='->', color='gray',
                                linewidth=1, linestyle='dashed'))
    ax.text(7.2, 3.25, 'Measurement data', fontsize=7, ha='center', color='gray')

    # Fundamental formula → DRN
    ax.annotate('', xy=(4.2, 2.0), xytext=(2.8, 1.8),
                arrowprops=dict(arrowstyle='->', color='black',
                                linewidth=1, linestyle='dotted'))

    # === Legend ===
    ax.text(0.5, 0.3, '© Dominic-René Schu — Resonance Field Theory 2025/2026',
            fontsize=7, color='gray', style='italic')

    plt.tight_layout()
    plt.savefig('resonance_reactor.png', dpi=200, bbox_inches='tight',
                facecolor='white')
    plt.savefig('resonance_reactor.svg', bbox_inches='tight',
                facecolor='white')
    plt.close()
    print("→ resonance_reactor.png")
    print("→ resonance_reactor.svg")


if __name__ == "__main__":
    draw_resonance_reactor()
