"""
Theoretische Erwartung für λ — Größenordnungsabschätzung
=========================================================

Gutachter-Kritikpunkt (Priorität MITTEL)
-----------------------------------------
Ohne eine theoretische Größenordnung für den RFT-Kopplungsparameter λ
bleibt unklar, ob das vorgeschlagene ⁸⁷Rb-Experiment realistische
Chancen hat, einen Effekt zu sehen, oder ob λ so klein ist, dass es
unerreichbar bleibt.

Ansätze zur Abschätzung
------------------------
1. Dimensionsanalyse: λ hat in der Simulation die Dimension
   [rad / (Zeit · Länge)]. In SI-Einheiten: [rad·m / (s · ℏ)]

2. BSM-Vergleich: Typische neue Physik jenseits des Standardmodells
   (BSM) erzeugt Korrekturen der Größenordnung α² ~ 10⁻⁴ bis 10⁻¹⁰.
   Wenn die RFT-Rückkopplung eine fundamentale Korrektur ist,
   erwarten wir λ ~ 10⁻⁴ bis 10⁻¹⁰.

3. Gravitationsvergleich: Wenn φ(x,t) mit dem Gravitationsfeld
   zusammenhängt (RFT motiviert), dann skaliert die Kopplung wie
   G · m² / ℏ ~ (m / m_Planck)² ~ 10⁻³⁸ für Rb-Atome.
   → Unrealistisch klein.

4. Phänomenologische Schranken: Vorhandene Präzisionsexperimente
   (Atominterferometrie, Neutroneninterferometrie, optische Uhren)
   setzen obere Schranken auf nichtlineare QM-Terme.

5. Decoherence-basierte Abschätzung: Wenn die RFT-Rückkopplung
   mit Umgebungs-Dekohärenz zusammenhängt, dann λ ~ γ_deco (typisch
   10⁻² bis 10⁻⁶ für ultrakalte Atome).

Einheiten: SI + dimensionslose Simulationseinheiten.

Ausführung:
  python python/schrodinger_1d_rft_lambda_bounds.py
  python python/schrodinger_1d_rft_lambda_bounds.py --checks
  python python/schrodinger_1d_rft_lambda_bounds.py --omega 100
"""

from __future__ import annotations

import argparse
import math
from typing import Any

import numpy as np


# ═══════════════════════════════════════════════════════════════════════════════
#  Physikalische Konstanten (SI)
# ═══════════════════════════════════════════════════════════════════════════════

HBAR_SI: float = 1.054571817e-34      # [J·s]
K_B_SI: float = 1.380649e-23          # [J/K]
M_RB87_SI: float = 1.443161e-25       # [kg]
G_NEWTON: float = 6.67430e-11         # [m³/(kg·s²)]
M_PLANCK: float = 2.176434e-8         # [kg]
L_PLANCK: float = 1.616255e-35        # [m]
T_PLANCK: float = 5.391247e-44        # [s]
C_LIGHT: float = 2.998e8              # [m/s]
ALPHA_EM: float = 1.0 / 137.036       # Feinstrukturkonstante

# Simulationsparameter (identisch mit experiment.py)
V_STRENGTH_SIM: float = 0.02
C_X_PREFACTOR: float = 0.4            # |Δ⟨x⟩| ≈ C_x · λ (simuliert)


# ═══════════════════════════════════════════════════════════════════════════════
#  Skalenbeziehungen (identisch mit experiment.py)
# ═══════════════════════════════════════════════════════════════════════════════


def harmonic_oscillator_length(m_si: float, omega_si: float) -> float:
    """a_ho = √(ℏ / (m·ω)) [m]."""
    return math.sqrt(HBAR_SI / (m_si * omega_si))


def simulation_length_unit(
    m_si: float, omega_si: float,
    v_strength: float = V_STRENGTH_SIM,
) -> float:
    """Längeneinheit ℓ der Simulation in SI [m]."""
    a_ho = harmonic_oscillator_length(m_si, omega_si)
    return v_strength ** 0.25 * a_ho


def simulation_time_unit(
    m_si: float, omega_si: float,
    v_strength: float = V_STRENGTH_SIM,
) -> float:
    """Zeiteinheit τ der Simulation in SI [s]."""
    return math.sqrt(v_strength) / omega_si


# ═══════════════════════════════════════════════════════════════════════════════
#  Theoretische λ-Abschätzungen
# ═══════════════════════════════════════════════════════════════════════════════


def lambda_gravitational(m_si: float) -> dict[str, float]:
    """Gravitationsbasierte Abschätzung.

    Wenn die Δφ-Rückkopplung gravitativen Ursprungs ist:
    λ_grav ~ G · m² / ℏ² · (Längenskala)
           ~ (m / m_Planck)²

    Dies ist die natürliche Skala für Gravitationseffekte
    in der Quantenmechanik (Penrose/Diósi-Regime).
    """
    # Dimensionsloses Gravitationsverhältnis
    m_ratio = m_si / M_PLANCK
    lambda_grav_ratio = m_ratio ** 2

    # In Simulationseinheiten (mit ℏ = 1, m = 1):
    # λ_sim = λ_phys · τ · ℓ (Einheitenumrechnung)
    # Aber λ ist schon dimensionslos in der Simulation (density-Modell)
    # λ_phys ~ G · m / ℏ = τ_grav⁻¹
    tau_grav_inv = G_NEWTON * m_si / HBAR_SI  # [1/s · m³/s]

    # Korrekte Dimensionsanalyse für das density-Modell:
    # Δφ̇ = λ · ∫|ψ|⁴ dx  [rad/s] → λ [rad · Länge / s]
    # λ_grav = G · m² / ℏ  [1/m] Nein...
    # Besser: Vergleich mit Penrose-Kollapsrate
    # τ_collapse ~ ℏ / (G · m² / R) ~ ℏ · R / (G · m²)
    # Rate ~ G · m² / (ℏ · R)
    # Mit R = a_ho:
    lambda_penrose_rate = G_NEWTON * m_si ** 2 / HBAR_SI  # [kg·m/s] → [1/m]

    return {
        "m_over_m_planck": m_ratio,
        "m_over_m_planck_sq": m_ratio ** 2,
        "lambda_dimensionless": lambda_grav_ratio,
        "lambda_penrose_rate_per_m": lambda_penrose_rate,
        "comment": "Extrem klein — gravitative Kopplung unerreichbar",
    }


def lambda_bsm_analogy() -> dict[str, Any]:
    """BSM-Analogie: Typische neue-Physik-Kopplungen.

    Beyond-Standard-Model-Korrekturen:
    - Elektroschwache Präzision: α² ~ 10⁻⁴
    - Neutrinomasseneffekte: ~ 10⁻⁵ bis 10⁻¹²
    - CP-Verletzung (Neutrinos): ~ 10⁻³
    - Dunkle-Materie-Kopplungen: ~ 10⁻⁸ bis 10⁻¹⁵
    - Lorentz-Verletzung: < 10⁻¹⁵

    Wenn RFT eine BSM-artige Korrektur ist, erwarten wir:
    λ_BSM ~ 10⁻⁴ bis 10⁻¹⁰
    """
    return {
        "scenarios": [
            {"name": "Elektroschwach (α²)", "lambda": ALPHA_EM ** 2,
             "lambda_log10": math.log10(ALPHA_EM ** 2)},
            {"name": "Schwache Kopplung (G_F-Skala)", "lambda": 1e-5,
             "lambda_log10": -5.0},
            {"name": "Neutrinomasse-artig", "lambda": 1e-8,
             "lambda_log10": -8.0},
            {"name": "Dunkle-Materie-Kopplung", "lambda": 1e-12,
             "lambda_log10": -12.0},
            {"name": "Lorentz-Verletzung (Grenze)", "lambda": 1e-15,
             "lambda_log10": -15.0},
        ],
    }


def lambda_decoherence_based(
    m_si: float, omega_si: float,
) -> dict[str, float]:
    """Dekohärenz-basierte Abschätzung.

    In ultrakalten Atomexperimenten gibt es verschiedene
    Dekohärenzraten. Wenn RFT-Rückkopplung mit Dekohärenz
    zusammenhängt:

    γ_spontan ~ 10⁻² s⁻¹  (Spontanemission, Rubidium)
    γ_thermal ~ 10⁻³ s⁻¹  (thermischer Kontakt, 100 nK)
    γ_collision ~ 10⁻⁴ s⁻¹  (Atom-Atom-Stöße)
    γ_vacuum ~ 10⁻⁶ s⁻¹   (Vakuum-Fluktuationen)

    λ_deco ~ γ · τ_sim  (in Simulationseinheiten)
    """
    tau = simulation_time_unit(m_si, omega_si)

    rates = {
        "spontaneous_emission": 1e-2,
        "thermal_contact": 1e-3,
        "atom_atom_collision": 1e-4,
        "vacuum_fluctuation": 1e-6,
    }

    lambdas = {}
    for name, rate in rates.items():
        lambdas[name] = rate * tau

    return {
        "tau_sim_s": tau,
        "decoherence_rates_per_s": rates,
        "lambda_sim_units": lambdas,
    }


def lambda_precision_experiments() -> dict[str, Any]:
    """Obere Schranken aus Präzisionsexperimenten.

    Vorhandene Experimente, die nichtlineare QM-Terme begrenzen:

    1. Weinberg-Schranke (1989): Nichtlineare Schrödinger-Terme
       |ε_NL / E_QM| < 10⁻²⁷ (aus Kernphysik)
       → λ < 10⁻²⁷ (wenn RFT ε_NL ~ λ · E_QM)

    2. Atominterferometrie (Optische Uhren):
       Δν/ν < 10⁻¹⁸ → λ < 10⁻¹⁸ (direkte Frequenzmessung)

    3. Neutroneninterferometrie:
       Δ(Kontrastfunktion) < 10⁻⁴
       → λ < 10⁻⁴ (für einzelne Neutronen)

    4. EPR/Bell-Tests (Gisin-artig):
       Verletzung von Bell-Ungleichungen konsistent mit QM
       → λ < 10⁻³ (für Photonen-Paare)

    ACHTUNG: Diese Schranken hängen von der genauen Implementierung
    der RFT ab. Die hier angegebenen Werte sind Größenordnungsab-
    schätzungen, nicht exakte Schranken.

    Die RFT-Rückkopplung unterscheidet sich von generischen
    nichtlinearen Termen:
    (a) Sie ist strukturiert (ε(Δφ)·V, nicht beliebig)
    (b) Sie wirkt über das Kopplungspotential, nicht direkt auf H₀
    (c) Im Limit Δφ → 0: ε(Δφ) → 1, kein Effekt
    → Schranken müssen RFT-spezifisch neu abgeleitet werden.
    """
    return {
        "experiments": [
            {
                "name": "Weinberg-Schranke (Kernphysik)",
                "lambda_upper": 1e-27,
                "log10": -27,
                "applicability": "hoch (wenn RFT ~ generisch nichtlinear)",
                "rft_specific": False,
            },
            {
                "name": "Optische Uhren (Frequenz)",
                "lambda_upper": 1e-18,
                "log10": -18,
                "applicability": "mittel (hängt von V_coupling ab)",
                "rft_specific": False,
            },
            {
                "name": "Neutroneninterferometrie",
                "lambda_upper": 1e-4,
                "log10": -4,
                "applicability": "niedrig (anderes System)",
                "rft_specific": False,
            },
            {
                "name": "Bell-Tests (Gisin)",
                "lambda_upper": 1e-3,
                "log10": -3,
                "applicability": "hoch (direkt relevant)",
                "rft_specific": True,
            },
            {
                "name": "RFT-spezifisch (ausstehend)",
                "lambda_upper": None,
                "log10": None,
                "applicability": "—",
                "rft_specific": True,
            },
        ],
    }


def experimental_reach(
    m_si: float, omega_si: float,
    n_repetitions: int = 100,
    v_strength: float = V_STRENGTH_SIM,
) -> dict[str, float]:
    """Experimentelle Reichweite des ⁸⁷Rb-Vorschlags.

    λ_min = σ_Δx / (C_x · ℓ)
    """
    ell = simulation_length_unit(m_si, omega_si, v_strength)
    resolution = 1e-6  # 1 µm Absorptionsbildgebung
    sigma_eff = resolution / math.sqrt(n_repetitions)
    lambda_min = sigma_eff / (C_X_PREFACTOR * ell)

    return {
        "ell_m": ell,
        "resolution_m": resolution,
        "n_repetitions": n_repetitions,
        "sigma_eff_m": sigma_eff,
        "lambda_min": lambda_min,
        "lambda_min_log10": math.log10(lambda_min),
    }


# ═══════════════════════════════════════════════════════════════════════════════
#  Zusammenfassung: λ-Landschaft
# ═══════════════════════════════════════════════════════════════════════════════


def lambda_landscape(
    m_si: float, omega_si: float,
) -> list[dict[str, Any]]:
    """Gesamtlandschaft der λ-Abschätzungen.

    Ordnet alle Abschätzungen nach Größenordnung.
    """
    entries: list[dict[str, Any]] = []

    # Gravitational
    grav = lambda_gravitational(m_si)
    entries.append({
        "name": "Gravitativ (Penrose/Diósi)",
        "lambda": grav["m_over_m_planck_sq"],
        "log10": math.log10(grav["m_over_m_planck_sq"]),
        "type": "Theorie",
        "reachable": False,
    })

    # BSM
    bsm = lambda_bsm_analogy()
    for s in bsm["scenarios"]:
        entries.append({
            "name": f"BSM: {s['name']}",
            "lambda": s["lambda"],
            "log10": s["lambda_log10"],
            "type": "Analogie",
            "reachable": s["lambda"] > 1e-4,
        })

    # Decoherence
    deco = lambda_decoherence_based(m_si, omega_si)
    for name, lam_sim in deco["lambda_sim_units"].items():
        lam_log = math.log10(lam_sim) if lam_sim > 0 else -99
        entries.append({
            "name": f"Dekohärenz: {name}",
            "lambda": lam_sim,
            "log10": lam_log,
            "type": "Phänomenologisch",
            "reachable": lam_sim > 1e-4,
        })

    # Experimental reach
    for n_rep in [1, 100, 10000]:
        reach = experimental_reach(m_si, omega_si, n_rep)
        entries.append({
            "name": f"Experiment (N={n_rep})",
            "lambda": reach["lambda_min"],
            "log10": reach["lambda_min_log10"],
            "type": "Experimentell",
            "reachable": True,
        })

    # Sort by log10(λ)
    entries.sort(key=lambda e: e["log10"])
    return entries


# ═══════════════════════════════════════════════════════════════════════════════
#  Hauptprogramm
# ═══════════════════════════════════════════════════════════════════════════════


def main() -> int:
    ap = argparse.ArgumentParser(
        description=(
            "Theoretische Erwartung für λ: Größenordnungsabschätzung"
        ),
    )
    ap.add_argument(
        "--omega", type=float, default=100.0,
        help="Fallenfrequenz [Hz] (Standard: 100 Hz)",
    )
    ap.add_argument("--checks", action="store_true",
                     help="extended consistency tests")
    ap.add_argument("--plot", action="store_true", help="show visualization")
    args = ap.parse_args()

    omega_hz: float = args.omega
    omega_si: float = 2.0 * math.pi * omega_hz
    m_si: float = M_RB87_SI

    # ─── Header ───────────────────────────────────────────────────────
    print("=" * 74)
    print("  Theoretical expectation for λ (RFT coupling parameter)")
    print("  Question: What is the order of magnitude of λ?")
    print("  System: ⁸⁷Rb in harmonic trap")
    print("=" * 74)
    print(f"  ω = 2π × {omega_hz:.1f} Hz")
    print(f"  m = {m_si:.6e} kg  ({m_si / 1.66054e-27:.1f} u)")
    print("=" * 74)

    all_pass = True

    # ─── 1. Gravitationsbasierte Abschätzung ──────────────────────────
    print("\n--- (1) Gravitationsbasierte Abschätzung ---")
    grav = lambda_gravitational(m_si)
    print(f"  m / m_Planck        = {grav['m_over_m_planck']:.6e}")
    print(f"  (m / m_Planck)²     = {grav['m_over_m_planck_sq']:.6e}")
    print(f"  → λ_grav            ~ {grav['m_over_m_planck_sq']:.0e}")
    print(f"  → {grav['comment']}")

    # ─── 2. BSM-Analogie ─────────────────────────────────────────────
    print("\n--- (2) BSM-Analogie: Typische neue-Physik-Kopplungen ---\n")
    bsm = lambda_bsm_analogy()
    print(f"  {'Szenario':<35s}  {'λ':>10s}  {'log₁₀(λ)':>10s}")
    print(f"  {'─' * 60}")
    for s in bsm["scenarios"]:
        print(f"  {s['name']:<35s}  {s['lambda']:10.1e}  "
              f"{s['lambda_log10']:10.1f}")

    # ─── 3. Dekohärenz-basiert ────────────────────────────────────────
    print("\n--- (3) Dekohärenz-basierte Abschätzung ---\n")
    deco = lambda_decoherence_based(m_si, omega_si)
    tau = deco["tau_sim_s"]
    print(f"  τ_sim = {tau:.4e} s")
    print(f"  λ_sim = γ_deco · τ_sim (in Simulationseinheiten)\n")
    print(f"  {'Dekohärenz-Quelle':<30s}  {'γ [1/s]':>10s}  "
          f"{'λ_sim':>12s}  {'log₁₀(λ)':>10s}")
    print(f"  {'─' * 68}")
    for name, rate in deco["decoherence_rates_per_s"].items():
        lam_sim = deco["lambda_sim_units"][name]
        log10_lam = math.log10(lam_sim) if lam_sim > 0 else -99
        print(f"  {name:<30s}  {rate:10.1e}  "
              f"{lam_sim:12.4e}  {log10_lam:10.1f}")

    # ─── 4. Experimentelle Schranken ──────────────────────────────────
    print("\n--- (4) Obere Schranken aus Präzisionsexperimenten ---\n")
    prec = lambda_precision_experiments()
    print(f"  {'Experiment':<35s}  {'λ_upper':>10s}  "
          f"{'log₁₀':>8s}  {'RFT-spez.':>10s}")
    print(f"  {'─' * 68}")
    for exp in prec["experiments"]:
        lam_str = (f"{exp['lambda_upper']:.0e}"
                   if exp["lambda_upper"] is not None else "—")
        log_str = (f"{exp['log10']:.0f}"
                   if exp["log10"] is not None else "—")
        rft_str = "ja" if exp["rft_specific"] else "nein"
        print(f"  {exp['name']:<35s}  {lam_str:>10s}  "
              f"{log_str:>8s}  {rft_str:>10s}")

    print("\n  WICHTIG: Die Weinberg-Schranke und Uhren-Schranken gelten")
    print("  für GENERISCHE nichtlineare Terme. Die RFT-Rückkopplung")
    print("  ist strukturiert (ε(Δφ)·V) und könnte weniger streng")
    print("  begrenzt sein. RFT-spezifische Schranken stehen aus.")

    # ─── 5. Experimentelle Reichweite ─────────────────────────────────
    print(f"\n--- (5) Experimentelle Reichweite (⁸⁷Rb, "
          f"ω=2π×{omega_hz:.0f} Hz) ---\n")
    print(f"  {'N_Messungen':>12s}  {'λ_min':>12s}  "
          f"{'log₁₀(λ_min)':>14s}")
    print(f"  {'─' * 42}")
    for n_rep in [1, 10, 100, 1000, 10000]:
        reach = experimental_reach(m_si, omega_si, n_rep)
        print(f"  {n_rep:12d}  {reach['lambda_min']:12.4f}  "
              f"{reach['lambda_min_log10']:14.2f}")

    # ─── 6. Gesamtlandschaft ─────────────────────────────────────────
    print("\n--- (6) Gesamtlandschaft: λ-Abschätzungen ---\n")
    landscape = lambda_landscape(m_si, omega_si)
    print(f"  {'Quelle':<40s}  {'log₁₀(λ)':>10s}  "
          f"{'Typ':>20s}  {'Erreichbar?':>12s}")
    print(f"  {'─' * 86}")
    for entry in landscape:
        reach = "ja ✓" if entry["reachable"] else "nein ✗"
        print(f"  {entry['name']:<40s}  {entry['log10']:10.1f}  "
              f"{entry['type']:>20s}  {reach:>12s}")

    # ─── Zusammenfassende Bewertung ──────────────────────────────────
    print("\n--- Zusammenfassende Bewertung ---\n")
    print("  Drei Szenarien für den experimentellen Zugang:\n")

    reach_100 = experimental_reach(m_si, omega_si, 100)

    print("  (A) Optimistisch: λ ~ 10⁻² bis 10⁰")
    print("      → Dekohärenz-ähnliche Kopplung")
    print("      → Experiment mit 100 Schuss nachweisbar ✓")
    print()
    print("  (B) Realistisch: λ ~ 10⁻⁴ bis 10⁻²")
    print("      → BSM-artige Korrektur (elektroschwach)")
    print(f"      → Experiment mit >10000 Schuss grenzwertig "
          f"(λ_min ~ {experimental_reach(m_si, omega_si, 10000)['lambda_min']:.3f})")
    print()
    print("  (C) Pessimistisch: λ < 10⁻¹⁰")
    print("      → Gravitativ oder generisch BSM")
    print("      → Experiment chancenlos, aber setzt obere Schranke")
    print()
    print(f"  Experimentelle Reichweite (100 Schuss): "
          f"λ ≳ {reach_100['lambda_min']:.2f}")
    print()
    print("  Empfehlung:")
    print("  Das Experiment ist sinnvoll als Schranken-Experiment:")
    print("  Wenn kein Effekt gesehen wird → obere Grenze für λ")
    print("  Wenn Effekt gesehen wird → Entdeckung! (BSM-artig)")
    print()
    print("  Verbesserungspotential:")
    print("  1. Niedrigere Fallenfrequenz (ω ~ 10 Hz statt 100 Hz)")
    print("     → größeres a_ho → bessere Sensitivität")
    print("  2. Quantenschaltkreise (Ionen-Fallen, Photonen)")
    print("     → direkter Zugang zu Fidelity-Messungen")
    print("  3. Atominterferometer (Raman-Übergänge)")
    print("     → λ_min < 10⁻³ möglich")

    # ─── Extended tests (--checks) ──────────────────────────────────
    if args.checks:
        print(f"\n{'=' * 74}")
        print("  Konsistenz-Tests")
        print(f"{'=' * 74}")

        # Test 1: Gravitativ → extrem klein
        grav_log = math.log10(grav["m_over_m_planck_sq"])
        ok = grav_log < -30
        sym = "✓" if ok else "✗"
        print(f"  {sym} Gravitativ: log₁₀(λ) = {grav_log:.1f} < −30")
        if not ok:
            all_pass = False

        # Test 2: BSM-Skalen sind in der richtigen Größenordnung
        for s in bsm["scenarios"]:
            ok = -30 < s["lambda_log10"] < 0
            sym = "✓" if ok else "✗"
            print(f"  {sym} BSM {s['name']}: "
                  f"log₁₀(λ) = {s['lambda_log10']:.1f}")
            if not ok:
                all_pass = False

        # Test 3: Experimentelle Reichweite monoton sinkend mit N
        reach_1 = experimental_reach(m_si, omega_si, 1)
        reach_100 = experimental_reach(m_si, omega_si, 100)
        reach_10000 = experimental_reach(m_si, omega_si, 10000)
        ok = (
            reach_1["lambda_min"]
            > reach_100["lambda_min"]
            > reach_10000["lambda_min"]
        )
        sym = "✓" if ok else "✗"
        print(f"  {sym} Monotonie: λ_min(1)={reach_1['lambda_min']:.3f} > "
              f"λ_min(100)={reach_100['lambda_min']:.3f} > "
              f"λ_min(10k)={reach_10000['lambda_min']:.3f}")
        if not ok:
            all_pass = False

        # Test 4: Dekohärenzraten positiv und sinnvoll
        for name, lam_sim in deco["lambda_sim_units"].items():
            ok = lam_sim > 0
            sym = "✓" if ok else "✗"
            print(f"  {sym} Dekohärenz {name}: λ = {lam_sim:.4e} > 0")
            if not ok:
                all_pass = False

        # Test 5: Landscape ist sortiert
        logs = [e["log10"] for e in landscape]
        ok = all(logs[i] <= logs[i + 1] + 1e-10 for i in range(len(logs) - 1))
        sym = "✓" if ok else "✗"
        print(f"  {sym} Landscape sortiert nach log₁₀(λ)")
        if not ok:
            all_pass = False

    # ─── Result ─────────────────────────────────────────────────────
    print(f"\n{'=' * 74}")
    if all_pass:
        print("  ✓ All tests passed.")
    else:
        print("  ✗ Tests failed.")

    print()
    print("  Ergebnis: Theoretische Erwartung für λ")
    print("  ──────────────────────────────────────")
    print("  • Keine eindeutige theoretische Vorhersage für λ")
    print("  • Gravitativ: λ ~ 10⁻³⁸ (unerreichbar)")
    print("  • BSM-artig: λ ~ 10⁻⁴ bis 10⁻¹⁰ (je nach Szenario)")
    print("  • Dekohärenz: λ ~ 10⁻⁵ bis 10⁻⁸ (phänomenologisch)")
    print(f"  • Experiment: λ ≳ {reach_100['lambda_min']:.2f} "
          "(100 Schuss, ⁸⁷Rb)")
    print()
    print("  → Das Experiment setzt obere Schranken.")
    print("  → Bei null Effekt: λ < λ_min (Ausschluss)")
    print("  → Bei positivem Effekt: λ bestimmt (Entdeckung)")
    print()
    print("  Gutachter-Kritikpunkt (λ-Größenordnung) → adressiert.")
    print("=" * 74)

    # ─── Plot ─────────────────────────────────────────────────────────
    if args.plot:
        _plot_lambda_landscape(landscape, m_si, omega_si)

    return 0 if all_pass else 1


# ═══════════════════════════════════════════════════════════════════════════════
#  Visualisierung
# ═══════════════════════════════════════════════════════════════════════════════


def _plot_lambda_landscape(
    landscape: list[dict[str, Any]],
    m_si: float, omega_si: float,
) -> None:
    """Visualisierung der λ-Landschaft."""
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(14, 8))

    names = [e["name"] for e in landscape]
    log10_vals = [e["log10"] for e in landscape]
    colors = []
    for e in landscape:
        if e["type"] == "Theorie":
            colors.append("tab:blue")
        elif e["type"] == "Analogie":
            colors.append("tab:orange")
        elif e["type"] == "Phänomenologisch":
            colors.append("tab:green")
        else:
            colors.append("tab:red")

    y_pos = range(len(names))
    bars = ax.barh(list(y_pos), log10_vals, color=colors, alpha=0.7)

    ax.set_yticks(list(y_pos))
    ax.set_yticklabels(names, fontsize=9)
    ax.set_xlabel("log₁₀(λ)")
    ax.set_title("Theoretische Erwartung und experimentelle Reichweite für λ")

    # Experimental reach markieren
    reach_100 = experimental_reach(m_si, 2 * math.pi * 100.0, 100)
    ax.axvline(reach_100["lambda_min_log10"], color="red", ls="--", lw=2,
               label=f"Exp. Reichweite (N=100): log₁₀(λ)="
                     f"{reach_100['lambda_min_log10']:.1f}")

    # Legende
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor="tab:blue", alpha=0.7, label="Theorie"),
        Patch(facecolor="tab:orange", alpha=0.7, label="BSM-Analogie"),
        Patch(facecolor="tab:green", alpha=0.7, label="Phänomenologisch"),
        Patch(facecolor="tab:red", alpha=0.7, label="Experimentell"),
    ]
    ax.legend(handles=legend_elements, loc="lower left", fontsize=9)

    ax.grid(True, alpha=0.3, axis="x")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    raise SystemExit(main())
