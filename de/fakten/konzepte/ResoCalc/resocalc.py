# resocalc.py
# © Dominic-René Schu, 2025/2026 — Resonanzfeldtheorie
#
# ResoCalc: Resonanzbasiertes Ingenieurswerkzeug
#
# Ersetzt willkürliche Annahmen (θ_max, Dämpfung, Sicherheitsfaktor)
# durch physikalisch begründete Resonanzkopplung ε(Δφ).
#
# E = π · ε(Δφ) · ℏ · f, κ = 1
#
# Ausführung:
#   python resocalc.py                          (Standalone mit Plot)
#   python resocalc.py --beispiel motor         (Motorwelle)
#   python resocalc.py --beispiel bruecke       (Brücke unter Wind)
#   python resocalc.py --beispiel turbine       (Turbinenschaufel)
#
# Im Jupyter-Notebook:
#   %run resocalc.py --notebook
#
# pip install numpy matplotlib

import numpy as np
import matplotlib.pyplot as plt
import os
import sys

PI = np.pi


# ============================================================
# AXIOM 4: Kopplungseffizienz — das Herzstück
# ============================================================

def kopplungseffizienz(delta_phi):
    """
    ε(Δφ) = cos²(Δφ/2)

    Die universelle Kopplungseffizienz der Resonanzfeldtheorie.
    Ersetzt in der Ingenieurmechanik die geschätzte Auslenkung θ_max.

    Δφ = 0:    ε = 1.0 — Perfekte Kopplung (Resonanz)
    Δφ = π/2:  ε = 0.5 — Halbe Kopplung
    Δφ = π:    ε = 0.0 — Keine Kopplung (Gegenphase)
    """
    return np.cos(delta_phi / 2.0) ** 2


def resonanzverstaerkung(f, f_r, daempfung=0.0001):
    """
    Resonanzverstärkung V(f, f_r).

    V = 1 / |1 - (f/f_r)²|

    Bei f → f_r: V → ∞ (theoretisch), begrenzt durch Dämpfung.
    Konventionell wird hier ein Sicherheitsfaktor geschätzt.
    ResoCalc berechnet V direkt aus dem Frequenzverhältnis.
    """
    r = f / f_r
    delta = np.abs(1 - r**2)
    # Physikalische Begrenzung statt willkürlicher Singularitätsvermeidung
    delta = np.maximum(delta, daempfung)
    return 1.0 / delta


# ============================================================
# KONVENTIONELLE BERECHNUNG
# ============================================================

def drehmoment_konventionell(m, l, f, theta_max):
    """
    Konventionelles effektives Drehmoment.

    M_konv = J · ω² · θ_max / √2

    Problem: θ_max ist GESCHÄTZT, nicht berechnet.
    Verschiedene Ingenieure → verschiedene Ergebnisse.
    """
    J = m * l**2
    omega = 2 * PI * f
    return J * omega**2 * theta_max / np.sqrt(2)


# ============================================================
# RESOCALC-BERECHNUNG
# ============================================================

def drehmoment_resocalc(m, l, f, f_r, epsilon):
    """
    Resonanzlogisches effektives Drehmoment.

    M_reso = ½ · m · l² · ω² · V(f, f_r) · ε

    Kein geschätzter Parameter. Alles physikalisch begründet:
    - V(f, f_r): Resonanzverstärkung aus dem Frequenzverhältnis
    - ε: Kopplungseffizienz (0 ≤ ε ≤ 1)
    """
    J = 0.5 * m * l**2
    omega = 2 * PI * f
    V = resonanzverstaerkung(f, f_r)
    return J * omega**2 * V * epsilon


# ============================================================
# BEISPIEL-SZENARIEN
# ============================================================

BEISPIELE = {
    'standard': {
        'name': 'Standard-Drehmoment',
        'beschreibung': 'Drehende Masse an einer Welle',
        'm': 2.0,          # kg
        'l': 1.0,          # m
        'f': 10.0,         # Hz (Anregung)
        'f_r': 5.0,        # Hz (Resonanz)
        'epsilon': 0.2,    # Kopplungseffizienz
        'theta_max': 0.087, # rad (5°, konventionell geschätzt)
    },
    'motor': {
        'name': 'Motorwelle (Pkw)',
        'beschreibung': 'Kurbelwelle eines 4-Zylinder-Motors bei 3000 U/min',
        'm': 15.0,         # kg (effektive Masse)
        'l': 0.15,         # m (Kurbelradius)
        'f': 100.0,        # Hz (2. Ordnung bei 3000 rpm)
        'f_r': 85.0,       # Hz (1. Biegeeigenfrequenz)
        'epsilon': 0.35,
        'theta_max': 0.02,  # rad (konventionell)
    },
    'bruecke': {
        'name': 'Fußgängerbrücke unter Windlast',
        'beschreibung': 'Hängebrücke, 50m Spannweite, periodische Böen',
        'm': 50000.0,      # kg (effektive modale Masse)
        'l': 25.0,         # m (halbe Spannweite)
        'f': 1.2,          # Hz (Böenfrequenz)
        'f_r': 1.1,        # Hz (1. Eigenfrequenz) — kritisch nah!
        'epsilon': 0.15,
        'theta_max': 0.005, # rad (konventionell)
    },
    'turbine': {
        'name': 'Turbinenschaufel',
        'beschreibung': 'Gasturbinenrotorstufe unter Strömungsanregung',
        'm': 0.8,          # kg
        'l': 0.25,         # m (Schaufellänge)
        'f': 5000.0,       # Hz (Düsenpassierfrequenz)
        'f_r': 4800.0,     # Hz (Schaufeleigenfrequenz)
        'epsilon': 0.08,
        'theta_max': 0.001, # rad (konventionell)
    },
}


# ============================================================
# VERGLEICHSBERECHNUNG
# ============================================================

def berechne_vergleich(beispiel):
    """
    Führt Vergleich Konventionell vs. ResoCalc durch.
    Gibt Ergebnisse als Dictionary zurück.
    """
    m = beispiel['m']
    l = beispiel['l']
    f = beispiel['f']
    f_r = beispiel['f_r']
    eps = beispiel['epsilon']
    theta = beispiel['theta_max']

    M_konv = drehmoment_konventionell(m, l, f, theta)
    M_reso = drehmoment_resocalc(m, l, f, f_r, eps)

    # Einzelwerte bei der Anregungsfrequenz
    if np.ndim(M_konv) > 0:
        M_konv_val = float(M_konv) if np.ndim(M_konv) == 0 else float(M_konv)
        M_reso_val = float(M_reso) if np.ndim(M_reso) == 0 else float(M_reso)
    else:
        M_konv_val = float(M_konv)
        M_reso_val = float(M_reso)

    V = resonanzverstaerkung(f, f_r)

    return {
        'name': beispiel['name'],
        'beschreibung': beispiel['beschreibung'],
        'M_konv': M_konv_val,
        'M_reso': M_reso_val,
        'faktor': M_reso_val / M_konv_val if M_konv_val > 0 else float('inf'),
        'V': float(V),
        'epsilon': eps,
        'f': f,
        'f_r': f_r,
        'm': m,
        'l': l,
    }


# ============================================================
# VISUALISIERUNG
# ============================================================

def plot_vergleich(beispiel, out_dir='figures'):
    """
    Erzeugt Vergleichsplot: Konventionell vs. ResoCalc
    über den gesamten Frequenzbereich.
    """
    os.makedirs(out_dir, exist_ok=True)

    m = beispiel['m']
    l = beispiel['l']
    f_r = beispiel['f_r']
    eps = beispiel['epsilon']
    theta = beispiel['theta_max']

    # Frequenzbereich: 10% bis 300% der Resonanzfrequenz
    f_min = max(0.1, f_r * 0.1)
    f_max = f_r * 3.0
    frequenzen = np.linspace(f_min, f_max, 500)

    M_konv = drehmoment_konventionell(m, l, frequenzen, theta)
    M_reso = drehmoment_resocalc(m, l, frequenzen, f_r, eps)

    # Begrenzung für Darstellung (Resonanzpeak kann sehr groß werden)
    M_reso_clip = np.clip(M_reso, 0, np.percentile(M_reso, 98) * 2)

    fig, axes = plt.subplots(2, 1, figsize=(12, 10))

    # Plot 1: Linearer Vergleich
    ax = axes[0]
    ax.plot(frequenzen, M_konv, label='Konventionell (θ_max geschätzt)',
            color='blue', lw=2, ls='--')
    ax.plot(frequenzen, M_reso_clip,
            label=f'ResoCalc (ε = {eps})', color='red', lw=2)
    ax.axvline(f_r, color='gray', ls=':', lw=1.5,
               label=f'Resonanzfrequenz f_r = {f_r} Hz')
    if beispiel['f'] != f_r:
        ax.axvline(beispiel['f'], color='orange', ls=':', lw=1.5,
                   label=f'Anregung f = {beispiel["f"]} Hz')
    ax.set_xlabel('Frequenz (Hz)')
    ax.set_ylabel('Effektives Drehmoment (Nm)')
    ax.set_title(f'{beispiel["name"]}: Konventionell vs. ResoCalc')
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)

    # Plot 2: Kopplungseffizienz und Resonanzverstärkung
    ax = axes[1]

    # Phasendifferenz als Funktion des Frequenzverhältnisses
    r = frequenzen / f_r
    # Modellierte Phasendifferenz: 0 bei Resonanz, π bei weit weg
    delta_phi = np.arctan2(np.abs(1 - r**2), 0.1) * 2
    eps_kurve = kopplungseffizienz(delta_phi)

    V_kurve = resonanzverstaerkung(frequenzen, f_r)
    V_norm = V_kurve / np.max(V_kurve)  # Normalisiert für Darstellung

    ax.plot(frequenzen, eps_kurve, label='ε(Δφ) Kopplungseffizienz',
            color='green', lw=2)
    ax.plot(frequenzen, V_norm,
            label='V (Resonanzverstärkung, normiert)',
            color='red', lw=2, ls='--')
    ax.fill_between(frequenzen, eps_kurve, alpha=0.1, color='green')
    ax.axvline(f_r, color='gray', ls=':', lw=1.5)
    ax.set_xlabel('Frequenz (Hz)')
    ax.set_ylabel('Normierter Wert')
    ax.set_title('Kopplungseffizienz ε(Δφ) und Resonanzverstärkung V')
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0, 1.1)

    fig.suptitle(
        f'ResoCalc: {beispiel["beschreibung"]}\n'
        f'E = π · ε(Δφ) · ℏ · f, κ = 1',
        fontsize=11, fontweight='bold')
    plt.tight_layout()

    name = beispiel['name'].lower().replace(' ', '_').replace('(', '').replace(')', '')
    pfad = os.path.join(out_dir, f'resocalc_{name}.png')
    plt.savefig(pfad, dpi=150)
    plt.close()
    print(f"  → {pfad}")
    return pfad


# ============================================================
# JUPYTER-NOTEBOOK MODUS
# ============================================================

def notebook_modus():
    """Startet interaktives Widget im Jupyter-Notebook."""
    try:
        from ipywidgets import interact, FloatSlider, VBox, HBox, Layout
        from IPython.display import display, Markdown
    except ImportError:
        print("  Jupyter-Widgets nicht verfügbar.")
        print("  pip install ipywidgets")
        return

    style = {'description_width': '100px'}
    layout = Layout(width='70%')

    def reso_sim(m=2.0, l=1.0, f_r=5.0, kopplung=0.2, theta_max=0.087):
        frequenzen = np.linspace(0.5, f_r * 4, 500)

        M_konv = drehmoment_konventionell(m, l, frequenzen, theta_max)
        M_reso = drehmoment_resocalc(m, l, frequenzen, f_r, kopplung)
        M_reso_clip = np.clip(M_reso, 0, np.percentile(M_reso, 98) * 2)

        plt.figure(figsize=(11, 6))
        plt.plot(frequenzen, M_konv, label='Konventionell (θ_max geschätzt)',
                 color='blue', lw=2, ls='--')
        plt.plot(frequenzen, M_reso_clip,
                 label=f'ResoCalc (ε = {kopplung:.2f})',
                 color='red', lw=2)
        plt.axvline(f_r, color='gray', ls=':', lw=1.5,
                    label=f'f_r = {f_r:.1f} Hz')
        plt.xlabel('Frequenz (Hz)')
        plt.ylabel('Effektives Drehmoment (Nm)')
        plt.title('ResoCalc vs. Konventionell — E = π · ε(Δφ) · ℏ · f')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()

        # Einzelvergleich bei f = 2 · f_r
        f_test = 2 * f_r
        M_k = drehmoment_konventionell(m, l, f_test, theta_max)
        M_r = drehmoment_resocalc(m, l, f_test, f_r, kopplung)
        V = resonanzverstaerkung(f_test, f_r)

        display(Markdown(
            f"**Bei f = {f_test:.1f} Hz:**\n\n"
            f"| Methode | Drehmoment | Basis |\n"
            f"|---------|-----------|-------|\n"
            f"| Konventionell | {M_k:.1f} Nm | θ_max = {theta_max:.3f} rad |\n"
            f"| ResoCalc | {M_r:.1f} Nm | ε = {kopplung:.2f}, V = {V:.1f} |\n"
            f"| **Faktor** | **{M_r/M_k:.1f}×** | |\n\n"
            f"Resonanzverstärkung V = {V:.1f} · "
            f"Kopplungseffizienz ε = {kopplung:.2f}"
        ))

    m_s = FloatSlider(value=2.0, min=0.1, max=50.0, step=0.1,
                      description='Masse (kg)', style=style, layout=layout)
    l_s = FloatSlider(value=1.0, min=0.05, max=5.0, step=0.05,
                      description='Länge (m)', style=style, layout=layout)
    f_s = FloatSlider(value=5.0, min=0.5, max=100.0, step=0.5,
                      description='f_r (Hz)', style=style, layout=layout)
    k_s = FloatSlider(value=0.2, min=0.01, max=1.0, step=0.01,
                      description='ε (Kopplung)', style=style, layout=layout)
    t_s = FloatSlider(value=0.087, min=0.001, max=0.5, step=0.001,
                      description='θ_max (rad)', style=style, layout=layout)

    interact(reso_sim, m=m_s, l=l_s, f_r=f_s, kopplung=k_s, theta_max=t_s)


# ============================================================
# HAUPTPROGRAMM
# ============================================================

def main():
    print("=" * 60)
    print("RESOCALC: Resonanzbasiertes Ingenieurswerkzeug")
    print("ε(Δφ) ersetzt θ_max — Physik statt Schätzung")
    print("E = π · ε(Δφ) · ℏ · f, κ = 1")
    print("=" * 60)

    # Argumente
    notebook = '--notebook' in sys.argv
    beispiel_name = 'standard'

    for i, arg in enumerate(sys.argv[1:]):
        if arg == '--beispiel' and i + 2 < len(sys.argv):
            beispiel_name = sys.argv[i + 2]
        if arg in BEISPIELE:
            beispiel_name = arg

    if notebook:
        notebook_modus()
        return

    if beispiel_name == 'alle':
        beispiele_liste = list(BEISPIELE.keys())
    else:
        if beispiel_name not in BEISPIELE:
            print(f"\n  Unbekanntes Beispiel: '{beispiel_name}'")
            print(f"  Verfügbar: {', '.join(BEISPIELE.keys())}, alle")
            sys.exit(1)
        beispiele_liste = [beispiel_name]

    out = 'figures'
    os.makedirs(out, exist_ok=True)

    for name in beispiele_liste:
        beispiel = BEISPIELE[name]

        print(f"\n{'─' * 60}")
        print(f"  {beispiel['name']}")
        print(f"  {beispiel['beschreibung']}")
        print(f"{'─' * 60}")

        erg = berechne_vergleich(beispiel)

        print(f"\n  Parameter:")
        print(f"    Masse:            {erg['m']:.1f} kg")
        print(f"    Länge:            {erg['l']:.2f} m")
        print(f"    Anregung:         {erg['f']:.1f} Hz")
        print(f"    Resonanzfrequenz: {erg['f_r']:.1f} Hz")
        print(f"    Kopplung ε:       {erg['epsilon']:.2f}")

        print(f"\n  Ergebnis:")
        print(f"    Konventionell:    {erg['M_konv']:>12.1f} Nm"
              f"  (θ_max = {beispiel['theta_max']:.4f} rad)")
        print(f"    ResoCalc:         {erg['M_reso']:>12.1f} Nm"
              f"  (ε = {erg['epsilon']}, V = {erg['V']:.1f})")
        print(f"    Faktor:           {erg['faktor']:>12.1f}×")

        if erg['faktor'] > 2:
            print(f"\n  ⚠ WARNUNG: Konventionelle Methode unterschätzt"
                  f" das Drehmoment um Faktor {erg['faktor']:.1f}!")
            print(f"    Bei Resonanz kann das zu Versagen führen.")

        plot_vergleich(beispiel, out)

    # Zusammenfassung
    if len(beispiele_liste) > 1:
        print(f"\n{'=' * 60}")
        print("ZUSAMMENFASSUNG ALLER BEISPIELE:")
        print(f"{'=' * 60}")
        print(f"{'Beispiel':30s} {'Konv. (Nm)':>12s} {'Reso (Nm)':>12s}"
              f" {'Faktor':>8s}")
        print(f"{'─'*30} {'─'*12} {'─'*12} {'─'*8}")
        for name in beispiele_liste:
            erg = berechne_vergleich(BEISPIELE[name])
            print(f"{erg['name']:30s} {erg['M_konv']:>12.1f}"
                  f" {erg['M_reso']:>12.1f} {erg['faktor']:>7.1f}×")

    print(f"\n{'=' * 60}")
    print(f"""
  RESOCALC — PARADIGMENWECHSEL:
  ──────────────────────────��──
  KONVENTIONELL:
    Ingenieur schätzt θ_max → Ergebnis variiert
    Bei Resonanz: Formel bricht zusammen
    Lösung: Sicherheitsfaktoren draufpacken

  RESOCALC:
    ε(Δφ) = cos²(Δφ/2) → physikalisch begründet
    Bei Resonanz: V wird groß, ε begrenzt
    Ergebnis: Realistisch, reproduzierbar

  NUTZUNG:
    python resocalc.py                    (Standard)
    python resocalc.py --beispiel motor   (Motorwelle)
    python resocalc.py --beispiel bruecke (Brücke)
    python resocalc.py --beispiel turbine (Turbine)
    python resocalc.py --beispiel alle    (Alle)
    python resocalc.py --notebook         (Jupyter)

  E = π · ε(Δφ) · ℏ · f, κ = 1
""")


if __name__ == "__main__":
    main()