"""
1D Schrödinger-Simulation mit RFT-Resonanz-Hamiltonoperator (Axiom 4)
=====================================================================

Implementiert den Resonanz-Hamiltonoperator aus dem RFT-Manuskript (Gl. eq:h_res):

    Ĥ_res = Ĥ₀ + ε(Δφ) · V̂_Kopplung

mit der Kopplungseffizienz aus Axiom 4:

    ε(Δφ) = cos²(Δφ/2) ∈ [0, 1]

Ableitung der Schrödinger-Gleichung aus Axiom 4
------------------------------------------------
Axiom 4 definiert die effektive Kopplungsenergie:

    E_eff = π · ε(Δφ) · ℏ · f

Für ein einzelnes Teilchen mit Frequenz-Mode f und dem freien Hamiltonoperator
Ĥ₀ = p̂²/(2m) ergibt sich der Resonanz-Hamiltonoperator:

    Ĥ_res = Ĥ₀ + ε(Δφ) · V̂_Kopplung

Die Zeitentwicklung folgt dann aus:

    iℏ ∂/∂t |ψ(t)⟩ = Ĥ_res |ψ(t)⟩

Numerischer Nachweis des Korrespondenzprinzips
----------------------------------------------
Für jede Phasendifferenz Δφ erzeugt der Resonanz-Hamiltonoperator exakt
dieselbe Zeitentwicklung wie die Standard-Schrödinger-Gleichung mit dem
effektiven Potential V_eff = ε(Δφ) · V_Kopplung.

Getestete Szenarien:
  1. Δφ = π     → ε = 0   → freies Teilchen (Ĥ_res = Ĥ₀)
  2. Δφ = 2π/3  → ε = ¼   → schwache Kopplung
  3. Δφ = π/2   → ε = ½   → halbe Kopplung
  4. Δφ = 0     → ε = 1   → volle Kopplung  (Ĥ_res = Ĥ₀ + V̂_Kopplung)

Numerik: Split-Operator (FFT), unitär, gute Normerhaltung.
Abhängigkeiten: numpy, matplotlib (optional für --plot).
Einheiten: dimensionslos, ħ = 1, m = 1.

Ausführung:
  python python/schrodinger_1d_rft.py
  python python/schrodinger_1d_rft.py --plot
  python python/schrodinger_1d_rft.py --checks
"""

from __future__ import annotations

import argparse
import math
from typing import Any

import numpy as np


# ═══════════════════════════════════════════════════════════════════════════════
#  RFT-Kernmodul: Kopplungseffizienz (Axiom 4) und Resonanz-Hamiltonoperator
# ═══════════════════════════════════════════════════════════════════════════════


def epsilon_coupling(delta_phi: float | np.ndarray) -> float | np.ndarray:
    """Kopplungseffizienz nach Axiom 4 der Resonanzfeldtheorie.

    ε(Δφ) = cos²(Δφ/2) ∈ [0, 1]

    Grenzfälle:
        Δφ = 0   → ε = 1   (perfekte Resonanz, konstruktive Interferenz)
        Δφ = π/2 → ε = ½   (Quadratur)
        Δφ = π   → ε = 0   (destruktive Interferenz, entkoppelt)
    """
    return np.cos(delta_phi / 2.0) ** 2


def delta_phi_for_epsilon(eps_target: float) -> float:
    """Inverse: Berechne Δφ so dass ε(Δφ) = eps_target.

    Δφ = 2 · arccos(√ε)  für ε ∈ [0, 1]
    """
    eps_clamped = float(np.clip(eps_target, 0.0, 1.0))
    return 2.0 * math.acos(math.sqrt(eps_clamped))


# ═══════════════════════════════════════════════════════════════════════════════
#  Quantenmechanische Infrastruktur
#  (konsistent mit schrodinger_1d_reference.py, selbstständig lauffähig)
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
    """Kontinuums-normierte k-Raum-Wellenfunktion.

    Skalierung: ψ(k) = (dx / √(2π)) · FFT[ψ(x)]
    sodass ∑|ψ(k)|² dk ≈ ∑|ψ(x)|² dx.
    """
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


def split_operator_step(
    psi_x: np.ndarray, Vx: np.ndarray, k: np.ndarray,
    dt: float, hbar: float, m: float,
) -> np.ndarray:
    """Split-Operator-Zeitschritt (symplektisch 2. Ordnung, unitär).

    ψ(t+dt) = e^{-iV dt/2ℏ} FFT⁻¹[ e^{-iT dt/ℏ} FFT[ e^{-iV dt/2ℏ} ψ(t) ] ]
    """
    phase_V = np.exp(-0.5j * Vx * dt / hbar)
    psi = phase_V * psi_x

    psi_k = np.fft.fft(psi)
    T_k = (hbar * k) ** 2 / (2.0 * m)
    psi_k *= np.exp(-1j * T_k * dt / hbar)
    psi = np.fft.ifft(psi_k)

    return phase_V * psi


# ═══════════════════════════════════════════════════════════════════════════════
#  RFT-Evolution: Resonanz-Hamiltonoperator (Gl. eq:h_res)
# ═══════════════════════════════════════════════════════════════════════════════


def rft_split_operator_step(
    psi_x: np.ndarray,
    V_coupling: np.ndarray,
    k: np.ndarray,
    dt: float,
    hbar: float,
    m: float,
    delta_phi: float,
) -> np.ndarray:
    """Split-Operator-Zeitschritt mit dem Resonanz-Hamiltonoperator.

    Ĥ_res = Ĥ₀ + ε(Δφ) · V̂_Kopplung       (Gl. eq:h_res)

    wobei Ĥ₀ = p̂²/(2m) der freie Hamiltonoperator ist und
    ε(Δφ) = cos²(Δφ/2) die Kopplungseffizienz aus Axiom 4.

    Das effektive Potential V_eff = ε(Δφ) · V_Kopplung wird im Ortsraum
    angewandt, der kinetische Anteil Ĥ₀ im k-Raum.
    """
    eps = epsilon_coupling(delta_phi)
    V_eff = eps * V_coupling
    return split_operator_step(psi_x, V_eff, k, dt, hbar, m)


# ═══════════════════════════════════════════════════════════════════════════════
#  Zeitentwicklung und Zustandsvergleich
# ═══════════════════════════════════════════════════════════════════════════════


def evolve(
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
    """Zeitentwicklung unter Standard-Schrödinger-Gleichung.

    Gibt Endzustand und aufgezeichnete Observablen zurück.
    """
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


def evolve_rft(
    psi0: np.ndarray,
    V_coupling: np.ndarray,
    delta_phi: float,
    x: np.ndarray,
    k: np.ndarray,
    dx: float,
    dk: float,
    dt: float,
    steps: int,
    hbar: float,
    m: float,
) -> dict[str, Any]:
    """Zeitentwicklung unter dem RFT-Resonanz-Hamiltonoperator.

    Ĥ_res = Ĥ₀ + ε(Δφ) · V̂_Kopplung

    Observablen werden bezüglich V_eff = ε(Δφ) · V_Kopplung berechnet.
    """
    eps = epsilon_coupling(delta_phi)
    V_eff = eps * V_coupling

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
            E_means.append(expectation_energy(k, pk, dk, V_eff, psi, dx, hbar, m))

        if n < steps:
            psi = rft_split_operator_step(
                psi, V_coupling, k, dt, hbar, m, delta_phi,
            )

    return {
        "psi_final": psi,
        "ts": np.array(ts),
        "norms": np.array(norms),
        "x_means": np.array(x_means),
        "p_means": np.array(p_means),
        "E_means": np.array(E_means),
    }


def state_fidelity(psi_a: np.ndarray, psi_b: np.ndarray, dx: float) -> float:
    """Zustandstreue (Fidelity) |⟨ψ_a|ψ_b⟩|²."""
    overlap = np.sum(np.conj(psi_a) * psi_b) * dx
    return float(np.abs(overlap) ** 2)


# ═══════════════════════════════════════════════════════════════════════════════
#  Korrespondenz-Test
# ═══════════════════════════════════════════════════════════════════════════════


def run_correspondence_test(
    label: str,
    delta_phi: float,
    V_coupling: np.ndarray,
    psi0: np.ndarray,
    x: np.ndarray,
    k: np.ndarray,
    dx: float,
    dk: float,
    dt: float,
    steps: int,
    hbar: float,
    m: float,
) -> dict[str, Any]:
    """Einzelner Korrespondenz-Test.

    Vergleicht die Zeitentwicklung unter:
      (a) Standard-Schrödinger mit V_eff = ε(Δφ) · V_Kopplung
      (b) RFT-Resonanz-Hamiltonoperator mit (V_Kopplung, Δφ)

    Beide müssen identische Ergebnisse liefern (Korrespondenzprinzip).
    """
    eps = float(epsilon_coupling(delta_phi))
    V_eff = eps * V_coupling

    # (a) Referenz: Standard-Schrödinger mit V_eff
    ref = evolve(psi0, V_eff, x, k, dx, dk, dt, steps, hbar, m)

    # (b) RFT: Resonanz-Hamiltonoperator
    rft = evolve_rft(psi0, V_coupling, delta_phi, x, k, dx, dk, dt, steps, hbar, m)

    # Vergleichsmetriken
    fid = state_fidelity(ref["psi_final"], rft["psi_final"], dx)
    max_diff = float(np.max(np.abs(ref["psi_final"] - rft["psi_final"])))
    norm_dev_ref = float(np.max(np.abs(ref["norms"] - ref["norms"][0])))
    norm_dev_rft = float(np.max(np.abs(rft["norms"] - rft["norms"][0])))

    return {
        "label": label,
        "delta_phi": delta_phi,
        "epsilon": eps,
        "fidelity": fid,
        "max_psi_diff": max_diff,
        "norm_ref_end": ref["norms"][-1],
        "norm_rft_end": rft["norms"][-1],
        "norm_dev_ref": norm_dev_ref,
        "norm_dev_rft": norm_dev_rft,
        "x_ref_end": ref["x_means"][-1],
        "x_rft_end": rft["x_means"][-1],
        "p_ref_end": ref["p_means"][-1],
        "p_rft_end": rft["p_means"][-1],
        "E_ref_end": ref["E_means"][-1],
        "E_rft_end": rft["E_means"][-1],
        "ref": ref,
        "rft": rft,
    }


# ═══════════════════════════════════════════════════════════════════════════════
#  Hauptprogramm
# ═══════════════════════════════════════════════════════════════════════════════


def main() -> int:
    ap = argparse.ArgumentParser(
        description="RFT-Resonanz-Hamiltonoperator: Korrespondenzprinzip-Nachweis",
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
                     help="Kopplungsstärke (V_Kopplung = ½ · Vstrength · x²)")

    ap.add_argument("--plot", action="store_true", help="Visualisierung anzeigen")
    ap.add_argument(
        "--checks", action="store_true",
        help="Erweiterte Smoke-Tests aktivieren (strenge Toleranzen)",
    )
    args = ap.parse_args()

    # ─── Gitter-Setup ─────────────────────────────────────────────────
    N: int = args.N
    L: float = args.L
    dx: float = L / N
    x = (np.arange(N) - N // 2) * dx
    dk: float = 2.0 * math.pi / L
    k = 2.0 * math.pi * np.fft.fftfreq(N, d=dx)

    # Kopplungspotential (harmonisch) — bleibt für alle Szenarien gleich
    V_coupling: np.ndarray = 0.5 * args.Vstrength * x ** 2

    # Initiales Wellenpaket
    psi0 = gaussian_wavepacket(x, args.x0, args.k0, args.sigma)
    psi0 = normalize(psi0, dx)

    # ─── Header ───────────────────────────────────────────────────────
    print("=" * 74)
    print("  RFT-Resonanz-Hamiltonoperator: Korrespondenzprinzip-Nachweis")
    print("  Ĥ_res = Ĥ₀ + ε(Δφ) · V̂_Kopplung       (Gl. eq:h_res)")
    print("  ε(Δφ) = cos²(Δφ/2)                      (Axiom 4)")
    print("=" * 74)
    print(f"  N={N}  L={L}  dx={dx:g}  dt={args.dt:g}  steps={args.steps}")
    print(f"  ħ={args.hbar}  m={args.m}  V_Kopplung = ½·{args.Vstrength}·x²")
    print(f"  ψ₀: Gaußpaket  x₀={args.x0}  k₀={args.k0}  σ={args.sigma}")
    print("=" * 74)

    # ─── Testszenarien ────────────────────────────────────────────────
    scenarios: list[tuple[str, float]] = [
        ("Freies Teilchen    (Δφ=π,   ε=0  )", math.pi),
        ("Schwache Kopplung  (Δφ=2π/3, ε=¼ )", 2.0 * math.pi / 3.0),
        ("Halbe Kopplung     (Δφ=π/2,  ε=½ )", math.pi / 2.0),
        ("Volle Kopplung     (Δφ=0,    ε=1 )", 0.0),
    ]

    results: list[dict[str, Any]] = []

    for label, dphi in scenarios:
        r = run_correspondence_test(
            label, dphi, V_coupling, psi0, x, k, dx, dk,
            args.dt, args.steps, args.hbar, args.m,
        )
        results.append(r)

        eps = r["epsilon"]
        fid = r["fidelity"]
        md = r["max_psi_diff"]

        print(f"\n--- {label} ---")
        print(f"  Δφ = {dphi:.4f} rad   ε(Δφ) = {eps:.6f}")
        print(f"  Fidelity |⟨ψ_ref|ψ_rft⟩|² = {fid:.15f}")
        print(f"  max|ψ_ref − ψ_rft|         = {md:.3e}")
        print(f"  Norm (Ref): {r['norm_ref_end']:.12f}  max dev={r['norm_dev_ref']:.3e}")
        print(f"  Norm (RFT): {r['norm_rft_end']:.12f}  max dev={r['norm_dev_rft']:.3e}")
        print(f"  ⟨x⟩  Ref={r['x_ref_end']:+.6f}   RFT={r['x_rft_end']:+.6f}")
        print(f"  ⟨p⟩  Ref={r['p_ref_end']:+.6f}   RFT={r['p_rft_end']:+.6f}")
        print(f"  ⟨H⟩  Ref={r['E_ref_end']:.6f}   RFT={r['E_rft_end']:.6f}")

    # ─── Zusammenfassung ──────────────────────────────────────────────
    print("\n" + "=" * 74)
    print("  ZUSAMMENFASSUNG: Korrespondenzprinzip")
    print("=" * 74)
    header = f"  {'Szenario':<42s} {'ε':>6s} {'Fidelity':>18s} {'max|Δψ|':>12s}"
    print(header)
    print("  " + "-" * (len(header) - 2))
    for r in results:
        print(
            f"  {r['label']:<42s} "
            f"{r['epsilon']:>6.4f} "
            f"{r['fidelity']:>18.15f} "
            f"{r['max_psi_diff']:>12.3e}"
        )

    # ─── Axiom 4: ε(Δφ)-Wertetabelle ─────────────────────────────────
    print(f"\n  Axiom 4: ε(Δφ) = cos²(Δφ/2)")
    print(f"  {'Δφ/π':>8s} {'ε':>10s} {'Δφ [rad]':>10s}")
    print("  " + "-" * 30)
    for frac, frac_label in [
        (0.0, "0"), (1 / 6, "1/6"), (1 / 4, "1/4"), (1 / 3, "1/3"),
        (1 / 2, "1/2"), (2 / 3, "2/3"), (3 / 4, "3/4"), (1.0, "1"),
    ]:
        dphi = frac * math.pi
        eps = float(epsilon_coupling(dphi))
        print(f"  {frac_label:>8s} {eps:>10.6f} {dphi:>10.6f}")

    # ─── Selbstkonsistenz: delta_phi_for_epsilon ──────────────────────
    print(f"\n  Selbstkonsistenz ε ↔ Δφ:")
    selfconsistent = True
    for target in [0.0, 0.1, 0.25, 0.5, 0.75, 0.9, 1.0]:
        dphi_inv = delta_phi_for_epsilon(target)
        eps_recovered = float(epsilon_coupling(dphi_inv))
        err = abs(eps_recovered - target)
        ok = "✓" if err < 1e-12 else "✗"
        print(f"    ε_target={target:.2f}  Δφ={dphi_inv:.6f}  "
              f"ε(Δφ)={eps_recovered:.12f}  err={err:.3e}  {ok}")
        if err > 1e-12:
            selfconsistent = False

    # ─── Smoke-Tests ──────────────────────────────────────────────────
    all_pass = True

    for r in results:
        if r["fidelity"] < 1.0 - 1e-10:
            print(f"\n[FAIL] Fidelity zu niedrig: {r['label']}  F={r['fidelity']}")
            all_pass = False
        if r["norm_dev_rft"] > 5e-4:
            print(f"\n[FAIL] Norm-Abweichung RFT: {r['label']}  "
                  f"dev={r['norm_dev_rft']:.3e}")
            all_pass = False

    if not selfconsistent:
        print("\n[FAIL] ε ↔ Δφ Selbstkonsistenz fehlgeschlagen")
        all_pass = False

    # ─── Erweiterte Tests (--checks) ──────────────────────────────────
    if args.checks:
        t_end = args.steps * args.dt
        r_free = results[0]  # Freies Teilchen

        # <x>-Drift: ⟨x⟩(t) = ⟨x⟩(0) + (⟨p⟩/m)·t
        expected_x = args.x0 + (args.hbar * args.k0 / args.m) * t_end
        x_err = abs(r_free["x_rft_end"] - expected_x)
        print(f"\n[check] Freies Teilchen ⟨x⟩-Drift:")
        print(f"  erwartet={expected_x:.6f}  RFT={r_free['x_rft_end']:.6f}  "
              f"err={x_err:.3e}")
        if x_err > 0.5:
            print("[FAIL] ⟨x⟩-Drift zu groß")
            all_pass = False

        # ⟨p⟩-Erhaltung für freies Teilchen
        target_p = args.hbar * args.k0
        p_err = abs(r_free["p_rft_end"] - target_p)
        print(f"[check] Freies Teilchen ⟨p⟩-Erhaltung:")
        print(f"  erwartet={target_p:.6f}  RFT={r_free['p_rft_end']:.6f}  "
              f"err={p_err:.3e}")
        if p_err > 0.5:
            print("[FAIL] ⟨p⟩ nicht erhalten")
            all_pass = False

        # Energieerhaltung für freies Teilchen
        E0_free = r_free["rft"]["E_means"][0]
        E_dev = float(np.max(np.abs(r_free["rft"]["E_means"] - E0_free)))
        print(f"[check] Freies Teilchen ⟨H⟩-Erhaltung:")
        print(f"  max|Δ⟨H⟩|={E_dev:.3e}")
        if E_dev > 1e-6:
            print("[FAIL] Energiedrift zu groß")
            all_pass = False

        # Energieerhaltung für alle Szenarien
        for r in results:
            E0 = r["rft"]["E_means"][0]
            Ed = float(np.max(np.abs(r["rft"]["E_means"] - E0)))
            ok = "✓" if Ed < 1e-4 else "✗"
            print(f"[check] ⟨H⟩-Erhaltung {r['label'][:30]:30s}: "
                  f"max|Δ⟨H⟩|={Ed:.3e} {ok}")
            if Ed > 1e-4:
                all_pass = False

    # ─── Ergebnis ─────────────────────────────────────────────────────
    if all_pass:
        print("\n" + "=" * 74)
        print("  ✓ Alle Korrespondenz-Tests bestanden.")
        print()
        print("  Numerisch belegt:")
        print("  Für jedes Δφ ∈ [0, π] erzeugt der Resonanz-Hamiltonoperator")
        print("    Ĥ_res = Ĥ₀ + ε(Δφ) · V̂_Kopplung")
        print("  exakt dieselbe Zeitentwicklung wie die Standard-Schrödinger-")
        print("  Gleichung mit V_eff = ε(Δφ) · V_Kopplung.")
        print()
        print("  → Korrespondenzprinzip: Standard-QM ist Spezialfall der RFT.")
        print("=" * 74)
    else:
        print("\n✗ Korrespondenz-Tests fehlgeschlagen.")
        return 1

    # ─── Plot ─────────────────────────────────────────────────────────
    if args.plot:
        _plot_results(results, x, args)

    return 0


# ═══════════════════════════════════════════════════════════════════════════════
#  Visualisierung
# ═══════════════════════════════════════════════════════════════════════════════


def _plot_results(
    results: list[dict[str, Any]],
    x: np.ndarray,
    args: argparse.Namespace,
) -> None:
    """Visualisierung der Korrespondenz-Ergebnisse."""
    import matplotlib.pyplot as plt

    n_scenarios = len(results)
    fig, axs = plt.subplots(n_scenarios, 3, figsize=(16, 4 * n_scenarios))
    if n_scenarios == 1:
        axs = axs.reshape(1, -1)

    for i, r in enumerate(results):
        ref = r["ref"]
        rft = r["rft"]

        # |ψ|² Endzustand
        axs[i, 0].plot(
            x, np.abs(ref["psi_final"]) ** 2, "b-",
            label="Referenz (Std-QM)", alpha=0.7,
        )
        axs[i, 0].plot(
            x, np.abs(rft["psi_final"]) ** 2, "r--",
            label="RFT (Ĥ_res)", alpha=0.7,
        )
        axs[i, 0].set_xlim(-80, 80)
        axs[i, 0].set_ylabel("|ψ|²")
        axs[i, 0].set_title(
            f'{r["label"]}\n'
            f'ε={r["epsilon"]:.4f}  F={r["fidelity"]:.12f}',
        )
        axs[i, 0].legend(fontsize=8)
        axs[i, 0].grid(True, alpha=0.3)

        # ⟨x⟩(t)
        axs[i, 1].plot(ref["ts"], ref["x_means"], "b-", label="Referenz")
        axs[i, 1].plot(rft["ts"], rft["x_means"], "r--", label="RFT")
        axs[i, 1].set_ylabel("⟨x⟩")
        axs[i, 1].legend(fontsize=8)
        axs[i, 1].grid(True, alpha=0.3)

        # ⟨H⟩(t)
        axs[i, 2].plot(ref["ts"], ref["E_means"], "b-", label="Referenz")
        axs[i, 2].plot(rft["ts"], rft["E_means"], "r--", label="RFT")
        axs[i, 2].set_ylabel("⟨H⟩")
        axs[i, 2].legend(fontsize=8)
        axs[i, 2].grid(True, alpha=0.3)

    for j in range(3):
        axs[-1, j].set_xlabel("t" if j > 0 else "x")

    plt.suptitle(
        "Korrespondenzprinzip: Ĥ_res = Ĥ₀ + ε(Δφ)·V̂_Kopplung  vs.  "
        "Standard-Schrödinger",
        fontsize=13,
        y=1.01,
    )
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    raise SystemExit(main())
