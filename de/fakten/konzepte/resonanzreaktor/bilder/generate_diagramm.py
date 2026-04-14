# generate_diagram.py
# © Dominic-René Schu, 2025/2026 – Resonanzfeldtheorie
# Erzeugt das aktualisierte Resonanzreaktor-Schemadiagramm
from __future__ import annotations

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
import os


def draw_resonanzreaktor() -> None:
    fig, ax = plt.subplots(1, 1, figsize=(14, 8))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8)
    ax.set_aspect('equal')
    ax.axis('off')

    # Titel
    ax.text(7, 7.6, 'Resonanzreaktor', fontsize=20, fontweight='bold',
            ha='center', va='center', family='sans-serif')
    ax.text(7, 7.2, 'Resonant gesteuerte Transmutation (RFT)',
            fontsize=11, ha='center', va='center', style='italic',
            color='gray')

    # === Hauptkomponenten als Boxen ===

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

    # 1. FEL (Photonenquelle)
    ax.text(2, 5.5, 'FEL / Synchrotron\nPhotonenquelle\nE_γ = 12–16 MeV',
            fontsize=9, ha='center', va='center', bbox=box_blue)

    # 2. Phasensteuerung
    ax.text(5.5, 5.5, 'Phasensteuerung\nPLL + DRN\nΔφ → 0 (Resonanz)',
            fontsize=9, ha='center', va='center', bbox=box_orange)

    # 3. Target (Resonanzkammer)
    ax.text(9, 5.5, 'Resonanzkammer\nAktinid-Target\n(Pu-239, Am-241, U-238)',
            fontsize=9, ha='center', va='center', bbox=box_highlight)

    # 4. Energieextraktion
    ax.text(12, 5.5, 'Energie-\nextraktion\n(thermisch)',
            fontsize=9, ha='center', va='center', bbox=box_green)

    # 5. Detektoren / Messung
    ax.text(9, 3.0, 'Detektoren\nα / n / γ_f / Spaltfragmente\n(ELIGANT, Si, HPGe)',
            fontsize=9, ha='center', va='center', bbox=box_style)

    # 6. Spaltprodukte
    ax.text(12, 3.0, 'Spaltprodukte\n(kurzlebig, t½ < 30 a)\nCs-137, Sr-90',
            fontsize=9, ha='center', va='center', bbox=box_green)

    # 7. Steuerung / DRN
    ax.text(5.5, 3.0, 'Deep Resonance\nNetwork (DRN)\nEchtzeit-Optimierung\nf, Δφ, Φ',
            fontsize=9, ha='center', va='center', bbox=box_orange)

    # 8. Elektrischer Output
    ax.text(12, 1.2, 'Elektrischer Output\n~280 MW (75 t Pu)\noder Impulsantrieb\nF = ṁ · v_f · η',
            fontsize=9, ha='center', va='center', bbox=box_green)

    # 9. Grundformel
    ax.text(2, 1.2, 'E = π · ε(Δφ) · ℏ · f\nε = η = cos²(Δφ/2)\nκ = 1 (kein freier Parameter)',
            fontsize=10, ha='center', va='center',
            bbox=dict(boxstyle="round,pad=0.4", facecolor='#FFFFF0',
                      edgecolor='black', linewidth=2),
            fontweight='bold', family='monospace')

    # === Pfeile ===

    arrow_kw = dict(arrowstyle='->', color='black', linewidth=1.5,
                    connectionstyle='arc3,rad=0')

    # FEL → Phasensteuerung
    ax.annotate('', xy=(4.0, 5.5), xytext=(3.2, 5.5),
                arrowprops=arrow_kw)
    ax.text(3.6, 5.85, 'γ-Strahl', fontsize=8, ha='center', color='blue')

    # Phasensteuerung → Target
    ax.annotate('', xy=(7.5, 5.5), xytext=(6.8, 5.5),
                arrowprops=arrow_kw)
    ax.text(7.15, 5.85, 'kohärent\nΔφ ≈ 0', fontsize=7, ha='center',
            color='darkorange')

    # Target → Energieextraktion
    ax.annotate('', xy=(11.0, 5.5), xytext=(10.3, 5.5),
                arrowprops=arrow_kw)
    ax.text(10.65, 5.85, '200 MeV\n/Spaltung', fontsize=7, ha='center',
            color='darkred')

    # Target → Detektoren
    ax.annotate('', xy=(9, 3.7), xytext=(9, 4.8),
                arrowprops=arrow_kw)
    ax.text(9.5, 4.25, 'α, n, γ', fontsize=8, ha='center', color='gray')

    # Target → Spaltprodukte
    ax.annotate('', xy=(11.0, 3.5), xytext=(10.3, 4.8),
                arrowprops=dict(arrowstyle='->', color='darkgreen',
                                linewidth=1.5))

    # Energieextraktion → Elektrischer Output
    ax.annotate('', xy=(12, 1.9), xytext=(12, 2.4),
                arrowprops=arrow_kw)

    # Energieextraktion → FEL (Rückkopplung)
    ax.annotate('', xy=(2, 4.8), xytext=(12, 4.8),
                arrowprops=dict(arrowstyle='->', color='green',
                                linewidth=1, linestyle='dashed',
                                connectionstyle='arc3,rad=-0.15'))
    ax.text(7, 4.55, 'Eigenstromversorgung (Rückkopplung)',
            fontsize=7, ha='center', color='green', style='italic')

    # DRN → Phasensteuerung (Feedback)
    ax.annotate('', xy=(5.5, 4.8), xytext=(5.5, 3.7),
                arrowprops=dict(arrowstyle='->', color='darkorange',
                                linewidth=1.5))

    # DRN → FEL (Feedback)
    ax.annotate('', xy=(2, 3.0), xytext=(4.2, 3.0),
                arrowprops=dict(arrowstyle='->', color='darkorange',
                                linewidth=1, linestyle='dashed'))
    ax.text(3.1, 3.25, 'f, Φ Steuerung', fontsize=7, ha='center',
            color='darkorange')

    # Detektoren → DRN (Feedback)
    ax.annotate('', xy=(6.8, 3.0), xytext=(7.6, 3.0),
                arrowprops=dict(arrowstyle='->', color='gray',
                                linewidth=1, linestyle='dashed'))
    ax.text(7.2, 3.25, 'Messdaten', fontsize=7, ha='center', color='gray')

    # Grundformel → DRN
    ax.annotate('', xy=(4.2, 2.0), xytext=(2.8, 1.8),
                arrowprops=dict(arrowstyle='->', color='black',
                                linewidth=1, linestyle='dotted'))

    # === Legende ===
    ax.text(0.5, 0.3, '© Dominic-René Schu — Resonanzfeldtheorie 2025/2026',
            fontsize=7, color='gray', style='italic')

    plt.tight_layout()
    plt.savefig('resonanzreaktor.png', dpi=200, bbox_inches='tight',
                facecolor='white')
    plt.savefig('resonanzreaktor.svg', bbox_inches='tight',
                facecolor='white')
    plt.close()
    print("→ resonanzreaktor.png")
    print("→ resonanzreaktor.svg")


if __name__ == "__main__":
    draw_resonanzreaktor()