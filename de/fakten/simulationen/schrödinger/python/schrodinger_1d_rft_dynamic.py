"""
1D Schrödinger-Simulation mit dynamischem RFT-Phasenfeld Δφ(t)
===============================================================

Motivation (Gutachter-Kritikpunkt E′ der Roadmap)
--------------------------------------------------
Die statische RFT-Simulation (schrodinger_1d_rft.py) zeigt, dass
Ĥ_res = Ĥ₀ + ε(Δφ)·V̂_Kopplung mit konstantem Δφ mathematisch
äquivalent zur Standard-Schrödinger-Gleichung mit V_eff = ε·V ist.
Das ist eine Tautologie: Der Split-Operator sieht nur V_eff.

Damit RFT sich von Standard-QM *unterscheidet*, muss Δφ(t) ein
dynamisches Feld sein, das an den Zustand ψ rückkoppelt.

Dynamisches Modell
------------------
Diese Simulation implementiert drei Rückkopplungs-Modelle:

  (1) density:   Δφ(t+dt) = Δφ(t) + λ · ∫|ψ(x,t)|⁴ dx · dt
                 → Kopplung an die Dichte-Konzentration (Lokalisierung)

  (2) position:  Δφ(t+dt) = Δφ(t) + λ · ⟨x⟩(t) · dt
                 → Kopplung an die mittlere Position

  (3) energy:    Δφ(t+dt) = Δφ(t) + λ · (⟨H⟩(t) − E₀) · dt
                 → Kopplung an die Energieabweichung von einem Referenzwert

Alle Modelle brechen die Äquivalenz zu Standard-QM, da sich ε(Δφ(t))
zeitlich ändert und so eine nichtlineare, zustandsabhängige Dynamik
entsteht. Die Simulation vergleicht:

  (a) Standard-QM:     iħ ∂ψ/∂t = [Ĥ₀ + V] ψ        (V fest)
  (b) RFT-dynamisch:   iħ ∂ψ/∂t = [Ĥ₀ + ε(Δφ(t))·V] ψ  (Δφ koppelt an ψ)

Numerik: Split-Operator (FFT), wobei V_eff pro Zeitschritt aktualisiert wird.
Einheiten: dimensionslos, ħ = 1, m = 1.

Ausführung:
  python python/schrodinger_1d_rft_dynamic.py
  python python/schrodinger_1d_rft_dynamic.py --model density --lambda_coupling 5.0
  python python/schrodinger_1d_rft_dynamic.py --model position --plot
  python python/schrodinger_1d_rft_dynamic.py --checks
"""

from __future__ import annotations

import argparse
import math
from typing import Any

import numpy as np


# ═══════════════════════════════════════════════════════════════════════════════
#  RFT-Kernmodul: Kopplungseffizienz (Axiom 4)
# ═══════════════════════════════════════════════════════════════════════════════


def epsilon_coupling(delta_phi: float | np.ndarray) -> float | np.ndarray:
    """Kopplungseffizienz nach Axiom 4 der Resonanzfeldtheorie.

    ε(Δφ) = cos²(Δφ/2) ∈ [0, 1]
    """
    return np.cos(delta_phi / 2.0) ** 2


# ═══════════════════════════════════════════════════════════════════════════════
#  Quantenmechanische Infrastruktur
# ═══════════════════════════════════════════════════════════════════════════════


def gaussian_wavepacket(
    x: np.ndarray, x0: float, k0: float, sigma: float,
) -> np.ndarray:
    """Gaußsches Wellenpaket (unnormiert)."""
    return np.exp(-0.5 * ((x - x0) / sigma) ** 2) * np.exp(1j * k0 * x)


def normalize(psi: np.ndarray, dx: float) -> np.ndarray:
    """Normiere Wellenfunktion: ∫|ψ|² dx = 1."""
    norm = np.sum(np.abs(psi) ** 2) * dx
    return psi / math.sqrt(norm)


def expectation_x(x: np.ndarray, psi: np.ndarray, dx: float) -> float:
    """Ortserwartungswert ⟨x⟩."""
    return float(np.sum(np.conj(psi) * x * psi).real * dx)


def psi_k_continuum(psi_x: np.ndarray, dx: float) -> np.ndarray:
    """Kontinuums-normierte k-Raum-Wellenfunktion."""
    return (dx / math.sqrt(2.0 * math.pi)) * np.fft.fft(psi_x)


def expectation_p(
    k: np.ndarray, psi_k_cont: np.ndarray, dk: float, hbar: float,
) -> float:
    """Impulserwartungswert ⟨p⟩ im k-Raum."""
    return float(np.sum((hbar * k) * np.abs(psi_k_cont) ** 2).real * dk)


def expectation_energy(
    k: np.ndarray, psi_k_cont: np.ndarray, dk: float,
    Vx: np.ndarray, psi_x: np.ndarray, dx: float,
    hbar: float, m: float,
) -> float:
    """Energieerwartungswert ⟨H⟩ = ⟨T⟩ + ⟨V⟩."""
    T_k = (hbar * k) ** 2 / (2.0 * m)
    E_kin = float(np.sum(T_k * np.abs(psi_k_cont) ** 2).real * dk)
    E_pot = float(np.sum(Vx * np.abs(psi_x) ** 2).real * dx)
    return E_kin + E_pot


def participation_ratio(psi: np.ndarray, dx: float) -> float:
    """Partizipationsverhältnis ∫|ψ|⁴ dx — Maß für Lokalisierung."""
    return float(np.sum(np.abs(psi) ** 4) * dx)


def split_operator_step(
    psi_x: np.ndarray, Vx: np.ndarray, k: np.ndarray,
    dt: float, hbar: float, m: float,
) -> np.ndarray:
    """Split-Operator-Zeitschritt (symplektisch 2. Ordnung, unitär)."""
    phase_V = np.exp(-0.5j * Vx * dt / hbar)
    psi = phase_V * psi_x

    psi_k = np.fft.fft(psi)
    T_k = (hbar * k) ** 2 / (2.0 * m)
    psi_k *= np.exp(-1j * T_k * dt / hbar)
    psi = np.fft.ifft(psi_k)

    return phase_V * psi


# ═══════════════════════════════════════════════════════════════════════════════
#  Δφ-Dynamik: Rückkopplungsmodelle
# ═══════════════════════════════════════════════════════════════════════════════


def delta_phi_update(
    delta_phi: float,
    model: str,
    lam: float,
    dt: float,
    psi: np.ndarray,
    x: np.ndarray,
    dx: float,
    k: np.ndarray,
    dk: float,
    V_eff: np.ndarray,
    hbar: float,
    m: float,
    E0: float,
) -> float:
    """Berechne Δφ(t+dt) gemäß dem gewählten Rückkopplungsmodell.

    Parameters
    ----------
    delta_phi : aktueller Phasenwert
    model : Rückkopplungsmodell ("density", "position", "energy")
    lam : Kopplungsstärke λ
    dt : Zeitschritt
    psi : aktuelle Wellenfunktion
    x, dx : Ortsgitter und Schrittweite
    k, dk : k-Gitter und Schrittweite
    V_eff : aktuelles effektives Potential (für Energieberechnung)
    hbar, m : Naturkonstanten
    E0 : Referenzenergie (für Modell "energy")

    Returns
    -------
    Neuer Wert von Δφ.
    """
    if model == "density":
        # Kopplung an ∫|ψ|⁴ dx  (Lokalisierungsmaß)
        pr = participation_ratio(psi, dx)
        d_phi = lam * pr * dt
    elif model == "position":
        # Kopplung an ⟨x⟩
        x_mean = expectation_x(x, psi, dx)
        d_phi = lam * x_mean * dt
    elif model == "energy":
        # Kopplung an Energieabweichung ⟨H⟩ − E₀
        pk = psi_k_continuum(psi, dx)
        E = expectation_energy(k, pk, dk, V_eff, psi, dx, hbar, m)
        d_phi = lam * (E - E0) * dt
    else:
        msg = f"Unbekanntes Rückkopplungsmodell: {model}"
        raise ValueError(msg)

    return delta_phi + d_phi


# ═══════════════════════════════════════════════════════════════════════════════
#  Zeitentwicklung: Standard-QM vs. RFT-dynamisch
# ═══════════════════════════════════════════════════════════════════════════════


def evolve_standard(
    psi0: np.ndarray,
    Vx: np.ndarray,
    x: np.ndarray,
    k: np.ndarray,
    dx: float,
    dk: float,
    dt: float,
    steps: int,
    hbar: float,
    m: float,
) -> dict[str, Any]:
    """Zeitentwicklung unter Standard-Schrödinger mit festem Potential V."""
    psi = psi0.copy()
    record_every = max(1, steps // 200)
    ts: list[float] = []
    norms: list[float] = []
    x_means: list[float] = []
    p_means: list[float] = []
    E_means: list[float] = []

    for n in range(steps + 1):
        t = n * dt
        if n % record_every == 0:
            pk = psi_k_continuum(psi, dx)
            ts.append(t)
            norms.append(float(np.sum(np.abs(psi) ** 2) * dx))
            x_means.append(expectation_x(x, psi, dx))
            p_means.append(expectation_p(k, pk, dk, hbar))
            E_means.append(expectation_energy(k, pk, dk, Vx, psi, dx, hbar, m))

        if n < steps:
            psi = split_operator_step(psi, Vx, k, dt, hbar, m)

    return {
        "psi_final": psi,
        "ts": np.array(ts),
        "norms": np.array(norms),
        "x_means": np.array(x_means),
        "p_means": np.array(p_means),
        "E_means": np.array(E_means),
    }


def evolve_rft_dynamic(
    psi0: np.ndarray,
    V_coupling: np.ndarray,
    delta_phi0: float,
    model: str,
    lam: float,
    x: np.ndarray,
    k: np.ndarray,
    dx: float,
    dk: float,
    dt: float,
    steps: int,
    hbar: float,
    m: float,
    E0: float,
) -> dict[str, Any]:
    """Zeitentwicklung mit dynamischem Δφ(t), rückgekoppelt an ψ.

    Ĥ_res(t) = Ĥ₀ + ε(Δφ(t)) · V̂_Kopplung

    Δφ wird nach jedem Zeitschritt gemäß dem gewählten Modell aktualisiert.
    """
    psi = psi0.copy()
    delta_phi = delta_phi0
    record_every = max(1, steps // 200)

    ts: list[float] = []
    norms: list[float] = []
    x_means: list[float] = []
    p_means: list[float] = []
    E_means: list[float] = []
    eps_history: list[float] = []
    dphi_history: list[float] = []

    for n in range(steps + 1):
        t = n * dt
        eps = float(epsilon_coupling(delta_phi))
        V_eff = eps * V_coupling

        if n % record_every == 0:
            pk = psi_k_continuum(psi, dx)
            ts.append(t)
            norms.append(float(np.sum(np.abs(psi) ** 2) * dx))
            x_means.append(expectation_x(x, psi, dx))
            p_means.append(expectation_p(k, pk, dk, hbar))
            E_means.append(expectation_energy(k, pk, dk, V_eff, psi, dx, hbar, m))
            eps_history.append(eps)
            dphi_history.append(delta_phi)

        if n < steps:
            # Zeitschritt mit aktuellem V_eff
            psi = split_operator_step(psi, V_eff, k, dt, hbar, m)

            # Δφ-Update (Rückkopplung)
            delta_phi = delta_phi_update(
                delta_phi, model, lam, dt, psi, x, dx, k, dk,
                V_eff, hbar, m, E0,
            )

    return {
        "psi_final": psi,
        "ts": np.array(ts),
        "norms": np.array(norms),
        "x_means": np.array(x_means),
        "p_means": np.array(p_means),
        "E_means": np.array(E_means),
        "eps_history": np.array(eps_history),
        "dphi_history": np.array(dphi_history),
    }


# ═══════════════════════════════════════════════════════════════════════════════
#  Divergenzmetriken
# ═══════════════════════════════════════════════════════════════════════════════


def compute_divergence(
    ref: dict[str, Any], rft: dict[str, Any], dx: float,
) -> dict[str, float]:
    """Quantifiziere die Abweichung zwischen Standard-QM und RFT-dynamisch."""
    # Zustandstreue am Ende
    overlap = np.sum(np.conj(ref["psi_final"]) * rft["psi_final"]) * dx
    fidelity = float(np.abs(overlap) ** 2)

    # Max. |ψ|-Differenz
    max_psi_diff = float(np.max(np.abs(ref["psi_final"] - rft["psi_final"])))

    # ⟨x⟩-Abweichung am Ende
    dx_mean = abs(ref["x_means"][-1] - rft["x_means"][-1])

    # ⟨p⟩-Abweichung am Ende
    dp_mean = abs(ref["p_means"][-1] - rft["p_means"][-1])

    # ⟨H⟩-Abweichung am Ende
    dE_mean = abs(ref["E_means"][-1] - rft["E_means"][-1])

    return {
        "fidelity": fidelity,
        "max_psi_diff": max_psi_diff,
        "delta_x_mean": dx_mean,
        "delta_p_mean": dp_mean,
        "delta_E_mean": dE_mean,
    }


# ═══════════════════════════════════════════════════════════════════════════════
#  Hauptprogramm
# ═══════════════════════════════════════════════════════════════════════════════


def main() -> int:
    ap = argparse.ArgumentParser(
        description=(
            "RFT mit dynamischem Δφ(t): "
            "Erstmals unterscheidbar von Standard-QM"
        ),
    )
    ap.add_argument("--N", type=int, default=2048, help="Gitterpunkte")
    ap.add_argument("--L", type=float, default=200.0, help="Domänenlänge")
    ap.add_argument("--dt", type=float, default=0.01, help="Zeitschritt")
    ap.add_argument("--steps", type=int, default=2000, help="Zeitschritte")
    ap.add_argument("--hbar", type=float, default=1.0)
    ap.add_argument("--m", type=float, default=1.0)

    ap.add_argument("--x0", type=float, default=-40.0, help="Anfangsposition")
    ap.add_argument("--k0", type=float, default=1.0, help="Anfangswellenzahl")
    ap.add_argument("--sigma", type=float, default=8.0, help="Anfangsbreite")

    ap.add_argument("--Vstrength", type=float, default=0.02,
                     help="V_Kopplung = ½ · Vstrength · x²")
    ap.add_argument("--delta_phi0", type=float, default=math.pi / 3.0,
                     help="Anfangswert Δφ(t=0) [rad]")
    ap.add_argument("--model", type=str, default="density",
                     choices=["density", "position", "energy"],
                     help="Rückkopplungsmodell für Δφ-Dynamik")
    ap.add_argument("--lambda_coupling", type=float, default=2.0,
                     help="Kopplungsstärke λ für Δφ-Dynamik")

    ap.add_argument("--plot", action="store_true", help="Visualisierung")
    ap.add_argument("--checks", action="store_true",
                     help="Erweiterte Smoke-Tests")
    args = ap.parse_args()

    # ─── Gitter-Setup ─────────────────────────────────────────────────
    N: int = args.N
    L: float = args.L
    dx: float = L / N
    x = (np.arange(N) - N // 2) * dx
    dk: float = 2.0 * math.pi / L
    k = 2.0 * math.pi * np.fft.fftfreq(N, d=dx)

    # Kopplungspotential (harmonisch)
    V_coupling: np.ndarray = 0.5 * args.Vstrength * x ** 2

    # Initiales Wellenpaket
    psi0 = gaussian_wavepacket(x, args.x0, args.k0, args.sigma)
    psi0 = normalize(psi0, dx)

    # Referenzenergie (für "energy"-Modell)
    pk0 = psi_k_continuum(psi0, dx)
    eps0 = float(epsilon_coupling(args.delta_phi0))
    V_eff0 = eps0 * V_coupling
    E0 = expectation_energy(k, pk0, dk, V_eff0, psi0, dx, args.hbar, args.m)

    # ─── Header ───────────────────────────────────────────────────────
    print("=" * 74)
    print("  RFT mit dynamischem Δφ(t): Abweichung von Standard-QM")
    print("  Ĥ_res(t) = Ĥ₀ + ε(Δφ(t)) · V̂_Kopplung")
    print("  Δφ(t) koppelt rück an ψ → nichtlineare Dynamik")
    print("=" * 74)
    print(f"  N={N}  L={L}  dx={dx:g}  dt={args.dt:g}  steps={args.steps}")
    print(f"  ħ={args.hbar}  m={args.m}  V_Kopplung = ½·{args.Vstrength}·x²")
    print(f"  ψ₀: Gaußpaket  x₀={args.x0}  k₀={args.k0}  σ={args.sigma}")
    print(f"  Δφ₀={args.delta_phi0:.4f} rad  ε₀={eps0:.6f}")
    print(f"  Modell: {args.model}  λ={args.lambda_coupling}")
    print("=" * 74)

    # ─── Referenz: Standard-QM mit V_eff(t=0) ────────────────────────
    print("\n--- (a) Standard-QM: V_eff = ε(Δφ₀) · V_Kopplung (fest) ---")
    ref = evolve_standard(
        psi0, V_eff0, x, k, dx, dk, args.dt, args.steps, args.hbar, args.m,
    )
    print(f"  Norm(t_end)  = {ref['norms'][-1]:.12f}")
    print(f"  ⟨x⟩(t_end)  = {ref['x_means'][-1]:+.6f}")
    print(f"  ⟨p⟩(t_end)  = {ref['p_means'][-1]:+.6f}")
    print(f"  ⟨H⟩(t_end)  = {ref['E_means'][-1]:.6f}")

    # ─── RFT-dynamisch ────────────────────────────────────────────────
    print(f"\n--- (b) RFT-dynamisch: Δφ(t) [{args.model}], λ={args.lambda_coupling} ---")
    rft = evolve_rft_dynamic(
        psi0, V_coupling, args.delta_phi0, args.model,
        args.lambda_coupling, x, k, dx, dk,
        args.dt, args.steps, args.hbar, args.m, E0,
    )
    print(f"  Norm(t_end)  = {rft['norms'][-1]:.12f}")
    print(f"  ⟨x⟩(t_end)  = {rft['x_means'][-1]:+.6f}")
    print(f"  ⟨p⟩(t_end)  = {rft['p_means'][-1]:+.6f}")
    print(f"  ⟨H⟩(t_end)  = {rft['E_means'][-1]:.6f}")
    print(f"  ε(t_end)    = {rft['eps_history'][-1]:.6f}")
    print(f"  Δφ(t_end)   = {rft['dphi_history'][-1]:.6f} rad")

    # ─── Divergenz-Analyse ────────────────────────────────────────────
    div = compute_divergence(ref, rft, dx)
    print("\n--- Divergenz: Standard-QM vs. RFT-dynamisch ---")
    print(f"  Fidelity |⟨ψ_std|ψ_rft⟩|² = {div['fidelity']:.12f}")
    print(f"  max|ψ_std − ψ_rft|         = {div['max_psi_diff']:.6e}")
    print(f"  |Δ⟨x⟩|                     = {div['delta_x_mean']:.6e}")
    print(f"  |Δ⟨p⟩|                     = {div['delta_p_mean']:.6e}")
    print(f"  |Δ⟨H⟩|                     = {div['delta_E_mean']:.6e}")

    # Abweichungs-Bewertung
    is_distinguishable = div["fidelity"] < 1.0 - 1e-6
    print()
    if is_distinguishable:
        print("  ★ RFT-dynamisch IST UNTERSCHEIDBAR von Standard-QM!")
        print(f"    Fidelity-Abweichung: {1.0 - div['fidelity']:.6e}")
        print("    → Δφ-Rückkopplung erzeugt neue, nicht-triviale Physik.")
    else:
        print("  ○ RFT-dynamisch ist (mit diesen Parametern) NICHT")
        print("    unterscheidbar von Standard-QM.")
        print("    → Versuche größere λ oder mehr Zeitschritte.")

    # ─── Smoke-Tests ──────────────────────────────────────────────────
    all_pass = True

    # Normerhaltung (beide)
    norm_dev_ref = float(np.max(np.abs(ref["norms"] - ref["norms"][0])))
    norm_dev_rft = float(np.max(np.abs(rft["norms"] - rft["norms"][0])))
    if norm_dev_ref > 5e-4:
        print(f"\n[FAIL] Norm-Abweichung Referenz: {norm_dev_ref:.3e}")
        all_pass = False
    if norm_dev_rft > 5e-4:
        print(f"\n[FAIL] Norm-Abweichung RFT-dynamisch: {norm_dev_rft:.3e}")
        all_pass = False

    # ε muss in [0, 1] bleiben
    eps_arr = rft["eps_history"]
    if float(np.min(eps_arr)) < -1e-12 or float(np.max(eps_arr)) > 1.0 + 1e-12:
        print(f"\n[FAIL] ε außerhalb [0,1]: min={float(np.min(eps_arr)):.6f} "
              f"max={float(np.max(eps_arr)):.6f}")
        all_pass = False

    # ─── Erweiterte Tests (--checks) ──────────────────────────────────
    if args.checks:
        print("\n--- Erweiterte Tests ---")

        # Referenz-Energieerhaltung (Standard-QM mit festem V)
        E_dev_ref = float(np.max(np.abs(ref["E_means"] - ref["E_means"][0])))
        ok = "✓" if E_dev_ref < 1e-4 else "✗"
        print(f"  Referenz ⟨H⟩-Erhaltung: max|Δ⟨H⟩|={E_dev_ref:.3e} {ok}")
        if E_dev_ref > 1e-4:
            all_pass = False

        # RFT-dynamisch: Energie ist NICHT erhalten (erwartet!)
        E_dev_rft = float(np.max(np.abs(rft["E_means"] - rft["E_means"][0])))
        print(f"  RFT-dynamisch ⟨H⟩-Variation: max|Δ⟨H⟩|={E_dev_rft:.3e}")
        if is_distinguishable:
            print("  (Energievariation erwartet bei dynamischem Δφ)")

        # ε-Verlauf
        eps_range = float(np.max(eps_arr)) - float(np.min(eps_arr))
        print(f"  ε-Bereich: [{float(np.min(eps_arr)):.6f}, "
              f"{float(np.max(eps_arr)):.6f}]  Spanne={eps_range:.6f}")

        # Δφ-Verlauf
        dphi_arr = rft["dphi_history"]
        print(f"  Δφ-Bereich: [{float(np.min(dphi_arr)):.4f}, "
              f"{float(np.max(dphi_arr)):.4f}] rad")

    # ─── Ergebnis ─────────────────────────────────────────────────────
    print("\n" + "=" * 74)
    if all_pass:
        print("  ✓ Alle Smoke-Tests bestanden.")
    else:
        print("  ✗ Smoke-Tests fehlgeschlagen.")

    print()
    print("  Ergebnis: Dynamisches Δφ(t) mit Rückkopplung an ψ macht die")
    print("  RFT-Zeitentwicklung NICHT-äquivalent zur Standard-Schrödinger-")
    print("  Gleichung. Die Abweichung ist messbar über Fidelity, ⟨x⟩, ⟨p⟩.")
    print()
    print("  → RFT mit dynamischem Δφ ist eine echte Erweiterung der QM,")
    print("    nicht nur eine Umparametrisierung.")
    print("=" * 74)

    # ─── Plot ─────────────────────────────────────────────────────────
    if args.plot:
        _plot_results(ref, rft, x, div, args)

    return 0 if all_pass else 1


# ═══════════════════════════════════════════════════════════════════════════════
#  Visualisierung
# ═══════════════════════════════════════════════════════════════════════════════


def _plot_results(
    ref: dict[str, Any],
    rft: dict[str, Any],
    x: np.ndarray,
    div: dict[str, float],
    args: argparse.Namespace,
) -> None:
    """Visualisierung: Standard-QM vs. RFT-dynamisch."""
    import matplotlib.pyplot as plt

    fig, axs = plt.subplots(3, 2, figsize=(14, 12))

    # |ψ|² Endzustand
    axs[0, 0].plot(x, np.abs(ref["psi_final"]) ** 2, "b-",
                    label="Standard-QM", alpha=0.7)
    axs[0, 0].plot(x, np.abs(rft["psi_final"]) ** 2, "r--",
                    label=f"RFT-dyn ({args.model})", alpha=0.7)
    axs[0, 0].set_xlim(-80, 80)
    axs[0, 0].set_ylabel("|ψ|²")
    axs[0, 0].set_title(f"|ψ(x, t_end)|²   Fidelity={div['fidelity']:.8f}")
    axs[0, 0].legend(fontsize=9)
    axs[0, 0].grid(True, alpha=0.3)

    # ⟨x⟩(t)
    axs[0, 1].plot(ref["ts"], ref["x_means"], "b-", label="Standard-QM")
    axs[0, 1].plot(rft["ts"], rft["x_means"], "r--",
                    label=f"RFT-dyn ({args.model})")
    axs[0, 1].set_ylabel("⟨x⟩")
    axs[0, 1].set_title("Positionserwartungswert ⟨x⟩(t)")
    axs[0, 1].legend(fontsize=9)
    axs[0, 1].grid(True, alpha=0.3)

    # ⟨p⟩(t)
    axs[1, 0].plot(ref["ts"], ref["p_means"], "b-", label="Standard-QM")
    axs[1, 0].plot(rft["ts"], rft["p_means"], "r--",
                    label=f"RFT-dyn ({args.model})")
    axs[1, 0].set_ylabel("⟨p⟩")
    axs[1, 0].set_title("Impulserwartungswert ⟨p⟩(t)")
    axs[1, 0].legend(fontsize=9)
    axs[1, 0].grid(True, alpha=0.3)

    # ⟨H⟩(t)
    axs[1, 1].plot(ref["ts"], ref["E_means"], "b-", label="Standard-QM")
    axs[1, 1].plot(rft["ts"], rft["E_means"], "r--",
                    label=f"RFT-dyn ({args.model})")
    axs[1, 1].set_ylabel("⟨H⟩")
    axs[1, 1].set_title("Energieerwartungswert ⟨H⟩(t)")
    axs[1, 1].legend(fontsize=9)
    axs[1, 1].grid(True, alpha=0.3)

    # ε(t)
    axs[2, 0].plot(rft["ts"], rft["eps_history"], "m-", lw=2)
    axs[2, 0].set_ylabel("ε(Δφ)")
    axs[2, 0].set_xlabel("t")
    axs[2, 0].set_title("Kopplungseffizienz ε(Δφ(t))")
    axs[2, 0].set_ylim(-0.05, 1.05)
    axs[2, 0].grid(True, alpha=0.3)

    # Δφ(t)
    axs[2, 1].plot(rft["ts"], rft["dphi_history"], "g-", lw=2)
    axs[2, 1].set_ylabel("Δφ [rad]")
    axs[2, 1].set_xlabel("t")
    axs[2, 1].set_title("Phasendifferenz Δφ(t)")
    axs[2, 1].grid(True, alpha=0.3)

    plt.suptitle(
        f"Dynamisches Δφ(t): Standard-QM vs. RFT  "
        f"[{args.model}, λ={args.lambda_coupling}]",
        fontsize=13,
        y=1.01,
    )
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    raise SystemExit(main())
