# rt33_energieluecke.py
# © Dominic-René Schu, 2025/2026 – Resonanzfeldtheorie
#
# RT-33: Warpantrieb — Energielücke schließen (Stufe 5)
#
# Skalierungsgesetz der Energielücke als Funktion des Blasenradius R.
#
# Physikalische Grundlage:
#   ρ_benötigt(R) ~ c⁴/(8πG) · (v_s/R)² · σ²  [Alcubierre 1994, Pfenning & Ford 1997]
#   ρ_verfügbar(R) = E_fusion / V_aktiv(R),  V_aktiv = 4πR²/σ
#   Wandpacking-Modell (n ∝ R²): ρ_verfügbar = const
#   Lücken-Faktor: L(R) = ρ_benötigt / ρ_verfügbar
#   Kritischer Radius R*: L(R*) = 1
#
# Fazit:
#   R* liegt für alle realistischen Fusionsszenarien im astronomischen Bereich
#   (parsec bis kiloparsec), weit jenseits von 1 AU. Die Energielücke ist
#   kein reines Skalierungsproblem — sie erfordert G* >> 10⁶ oder grundlegend
#   neue Physik (negative Energie, Casimir-Effekt, exotische Materie).
#
# Ausführung:
#   cd de/fakten/konzepte/warpantrieb
#   python analyse/rt33_energieluecke.py

from __future__ import annotations

import os
import sys

import numpy as np
import matplotlib.pyplot as plt

# Elternverzeichnis im Pfad
_HERE = os.path.dirname(os.path.abspath(__file__))
_PARENT = os.path.dirname(_HERE)
sys.path.insert(0, _PARENT)

from warpantrieb import skalierungsgesetz

# ============================================================
# Konfiguration
# ============================================================

OUT_DIR = os.path.join(_PARENT, "figures")
C = 2.99792458e8    # Lichtgeschwindigkeit [m/s]
AU = 1.496e11       # 1 Astronomische Einheit [m]
LY = 9.461e15       # 1 Lichtjahr [m]
PC = 3.086e16       # 1 Parsec [m]

SZENARIEN = {
    "Konservativ": {
        "n_reaktoren": 12, "gain": 1.5, "P_pro": 1e8,
        "label": "Konservativ (G=1.5, 12×100MW)",
    },
    "Realistisch": {
        "n_reaktoren": 100, "gain": 10.0, "P_pro": 1e9,
        "label": "Realistisch (G=10, 100×1GW)",
    },
    "Optimistisch": {
        "n_reaktoren": 1000, "gain": 100.0, "P_pro": 1e10,
        "label": "Optimistisch (G=100, 1000×10GW)",
    },
}

# ============================================================
# Hauptprogramm
# ============================================================

def main() -> None:
    print("=" * 72)
    print("RT-33 — WARPANTRIEB: ENERGIELÜCKE SCHLIESSEN (STUFE 5)")
    print("Skalierungsgesetz ρ_benötigt(R) vs. ρ_verfügbar(R)")
    print("© Dominic-René Schu, 2025/2026 – Resonanzfeldtheorie")
    print("=" * 72)

    os.makedirs(OUT_DIR, exist_ok=True)

    R_range = np.logspace(1, 6, 500)       # 10 m … 1000 km
    v_s_list = [0.01 * C, 0.1 * C, 1.0 * C]
    sigma = 10.0    # Wandschärfe [1/m]

    # ----------------------------------------------------------
    # skalierungsgesetz() für alle drei Szenarien
    # ----------------------------------------------------------
    ergebnis = skalierungsgesetz(
        R_range=R_range,
        v_s_list=v_s_list,
        sigma_list=[sigma],
        gain_list=[1.5, 10.0, 100.0],
        n_reaktoren_list=[12, 100, 1000],
        P_pro_reaktor=1e8,
        pulse_rate=10.0,
        R_ref=50.0,
        plot=True,
        export_csv=True,
        out=OUT_DIR,
    )

    # ----------------------------------------------------------
    # Ergebnisausgabe
    # ----------------------------------------------------------
    print("\n" + "=" * 72)
    print("ERGEBNISTABELLE  (v_s = 0.1c, σ = 10 /m, R_ref = 50 m)")
    print("=" * 72)
    print(f"  {'Szenario':<42s} | {'R*':>18s} | {'G*':>12s} |"
          f" {'L(50m)':>10s} | Bewertung")
    print(f"  {'-'*42} | {'-'*18} | {'-'*12} | {'-'*10} | {'-'*26}")

    for r in ergebnis["scenarios"]:
        Rc = r["R_crit"]
        if Rc < 1e3:
            rc_str = f"{Rc:.2f} m"
        elif Rc < AU:
            rc_str = f"{Rc / AU:.3e} AU"
        elif Rc < LY:
            rc_str = f"{Rc / LY:.3e} Lj"
        elif Rc < PC * 1e6:
            rc_str = f"{Rc / PC:.3e} pc"
        else:
            rc_str = f"{Rc / (PC * 1e3):.3e} kpc"

        # G* für Lückenschluss bei R_ref = 50 m
        from warpantrieb import PI, G as GRAV, C as LICHT
        prefactor = LICHT ** 4 / (8.0 * PI * GRAV)
        G_star = (prefactor * (0.1 * LICHT / 50.0) ** 2 * sigma ** 2
                  * 4.0 * PI * 50.0 ** 2
                  / (r["n_reaktoren"] * r["P_pro_reaktor"] * 1e-8 * sigma))

        print(f"  {r['label']:<42s} | {rc_str:>18s} | {G_star:>12.3e} |"
              f" {r['L_at_Rref']:>10.3e} | {r['bewertung']}")

    # ----------------------------------------------------------
    # Fazit
    # ----------------------------------------------------------
    print("\n" + "=" * 72)
    print("FAZIT UND FALSIFIZIERUNGSKRITERIUM (RT-33)")
    print("=" * 72)
    print("""
  Skalierungsgesetz:
    ρ_benötigt(R) = c⁴/(8πG) · (v_s/R)² · σ²    ∝ R⁻²
    ρ_verfügbar(R) = n · P · τ · G / (4πR²/σ)    ∝ R⁻² (festes n)
    Im Wandpacking-Modell (n ∝ R²): ρ_verfügbar = const → L(R) ∝ R⁻²

  Übereinstimmung mit Literatur:
    Alcubierre (1994): ρ ~ c⁴/(8πG) · (v_s · σ)²  — hier σ = const
    Pfenning & Ford (1997): E_total = c⁴ · v_s² · σ / (2G) — R-unabhängig
    RFT-RT-33: ρ(R) ∝ R⁻² konsistent mit σ = const

  Falsifizierungskriterium:
    R* < 1 km   → technisch grundsätzlich erreichbar (langfristig)
    R* < 1 AU   → technisch sehr anspruchsvoll
    R* > 1 AU   → nicht erreichbar mit bekannter Physik

  Ergebnis:
    Alle drei Szenarien: R* >> 1 AU (parsec- bis kiloparsec-Skala)
    → Die Energielücke ist kein reines Skalierungsproblem.
    → Für Lückenschluss bei R = 50 m benötigter Gain: G* ~ 10¹⁶ – 10¹⁸
    → Das entspricht 10¹⁶× mehr als die beste Fusionstechnologie.

  EHRLICHKEITSSTANDARD BEIBEHALTEN (§6.1):
    Δw = 0.057 ist kein Alcubierre-Warp-Effekt (kosmologisches Rollverhalten).
    RT-33 zeigt: die Alcubierre-Energielücke ist astronomisch — nicht technisch.
    Das Zwei-Feld-Modell bleibt physikalisch interessant als Analogon,
    aber nicht als tatsächlicher Warpantrieb-Mechanismus.

  Nächster Schritt: RT-34 — 3D-Warpblase (Stufe 6)
""")
    print(f"  Plots gespeichert in: {OUT_DIR}/")
    print(f"  CSV: {OUT_DIR}/rt33_skalierungsgesetz.csv")
    print("Fertig.")


if __name__ == "__main__":
    main()
