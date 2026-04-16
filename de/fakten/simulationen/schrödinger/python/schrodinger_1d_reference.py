"""
1D Schrödinger-Referenzsimulation (Freies Teilchen + optional Potential)
Zweck: Referenzmodell für spätere Resonanz-/Phasen-Gittermodelle.

Numerik: Split-Operator (FFT), unitär -> gute Normerhaltung.
Abhängigkeiten: numpy, matplotlib (optional für Plot).

Einheiten:
- Standardmäßig dimensionslos mit ħ = 1, m = 1.
- Dann ist E(k) = k^2 / (2m) = k^2/2 und die Zeit ist entsprechend skaliert.

Ausführung:
  python python/schrodinger_1d_reference.py --plot
"""

from __future__ import annotations
import argparse
import math
import numpy as np


def gaussian_wavepacket(x: np.ndarray, x0: float, k0: float, sigma: float) -> np.ndarray:
    """Unnormalized Gaussian wavepacket; caller must normalize separately."""
    psi = np.exp(-0.5 * ((x - x0) / sigma) ** 2) * np.exp(1j * k0 * x)
    return psi


def potential(x: np.ndarray, kind: str, strength: float, x0: float = 0.0) -> np.ndarray:
    if kind == "free":
        return np.zeros_like(x, dtype=float)
    if kind == "harmonic":
        # V = 0.5 * strength * (x-x0)^2  (strength acts like m*omega^2)
        return 0.5 * strength * (x - x0) ** 2
    if kind == "well":
        # simple square well: V=0 inside |x-x0|<L/2 else V=strength
        L = 4.0
        V = np.ones_like(x, dtype=float) * strength
        V[np.abs(x - x0) < (L / 2)] = 0.0
        return V
    raise ValueError(f"unknown potential kind: {kind}")


def normalize(psi: np.ndarray, dx: float) -> np.ndarray:
    norm = np.sum(np.abs(psi) ** 2) * dx
    return psi / math.sqrt(norm)


def expectation_x(x: np.ndarray, psi: np.ndarray, dx: float) -> float:
    return float(np.sum(np.conj(psi) * x * psi).real * dx)


def psi_k_continuum(psi_x: np.ndarray, dx: float, dk: float) -> np.ndarray:
    """
    Build a k-space wavefunction ψ(k) that is normalized in the *continuum* sense:
        ∑ |ψ(k)|^2 dk  ≈  ∑ |ψ(x)|^2 dx

    Notes on conventions:
    - numpy.fft.fft returns unnormalized discrete coefficients.
    - If ψ(x) is normalized with ∑|ψ|^2 dx = 1, then the raw FFT coefficients
      must be rescaled to represent a continuum ψ(k) for expectation values.
    """
    # raw discrete FFT coefficients
    psi_k_raw = np.fft.fft(psi_x)
    # scaling chosen so that (Σ |psi_k_cont|^2 dk) matches (Σ |psi_x|^2 dx)
    # With numpy's FFT conventions this is achieved by:
    #   psi_k_cont = (dx / sqrt(2π)) * psi_k_raw
    # and using k-grid with dk = 2π/L.
    return (dx / math.sqrt(2.0 * math.pi)) * psi_k_raw


def expectation_p_from_k(k: np.ndarray, psi_k_cont: np.ndarray, dk: float, hbar: float) -> float:
    # <p> = ∫ ħ k |ψ(k)|^2 dk
    return float(np.sum((hbar * k) * (np.abs(psi_k_cont) ** 2)) * dk)


def expectation_p_from_x(psi_x: np.ndarray, k: np.ndarray, dx: float, hbar: float) -> float:
    """
    Zweite unabhängige Kontrolle von <p> direkt im Ortsraum via Ableitungsoperator.

    Berechnet <p> = Re( ∫ ψ*(x) (-iħ ∂_x) ψ(x) dx ).

    Implementierung: Ableitung über FFT (spektral exakt für periodische Randbedingungen):
        ∂_x ψ = IFFT( i k · FFT(ψ) )

    Hinweis: Das x-Gitter hat periodische Randbedingungen (impliziert durch FFT).
    Für ein gut lokalisiertes Wellenpaket, das den Rand nicht erreicht, stimmt
    dieses Ergebnis mit dem k-Raum-Erwartungswert überein.
    """
    dpsi_dx = np.fft.ifft(1j * k * np.fft.fft(psi_x))
    integrand = np.conj(psi_x) * (-1j * hbar) * dpsi_dx
    return float(np.sum(integrand).real * dx)


def expectation_energy_from_k_and_x(
    k: np.ndarray,
    psi_k_cont: np.ndarray,
    dk: float,
    Vx: np.ndarray,
    psi_x: np.ndarray,
    dx: float,
    hbar: float,
    m: float,
) -> float:
    """
    Berechnet den Energieerwartungswert ⟨H⟩ = ⟨T⟩ + ⟨V⟩.

    ⟨T⟩ wird im k-Raum berechnet:  ⟨T⟩ = ∫ (ħk)²/(2m) |ψ(k)|² dk
    ⟨V⟩ wird im Ortsraum berechnet: ⟨V⟩ = ∫ V(x) |ψ(x)|² dx
    """
    T_k = (hbar * k) ** 2 / (2.0 * m)
    E_kin = float(np.sum(T_k * np.abs(psi_k_cont) ** 2).real * dk)
    E_pot = float(np.sum(Vx * np.abs(psi_x) ** 2).real * dx)
    return E_kin + E_pot


def split_operator_step(
    psi_x: np.ndarray,
    Vx: np.ndarray,
    k: np.ndarray,
    dt: float,
    hbar: float,
    m: float,
) -> np.ndarray:
    """
    One time step using split-operator:
      psi(t+dt) = exp(-i V dt/2ħ) FFT^-1[ exp(-i T dt/ħ) FFT[ exp(-i V dt/2ħ) psi(t) ] ]
    with T = p^2/(2m) = (ħ k)^2/(2m)
    """
    phase_V = np.exp(-0.5j * Vx * dt / hbar)
    psi = phase_V * psi_x

    psi_k = np.fft.fft(psi)
    T_k = (hbar * k) ** 2 / (2.0 * m)
    phase_T = np.exp(-1j * T_k * dt / hbar)
    psi_k *= phase_T
    psi = np.fft.ifft(psi_k)

    psi = phase_V * psi
    return psi


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--N", type=int, default=2048, help="grid points")
    ap.add_argument("--L", type=float, default=200.0, help="domain length")
    ap.add_argument("--dt", type=float, default=0.01, help="time step")
    ap.add_argument("--steps", type=int, default=2000, help="number of steps")
    ap.add_argument("--hbar", type=float, default=1.0)
    ap.add_argument("--m", type=float, default=1.0)

    ap.add_argument("--x0", type=float, default=-40.0, help="initial center")
    ap.add_argument("--k0", type=float, default=1.0, help="initial wave number")
    ap.add_argument("--sigma", type=float, default=8.0, help="initial width")

    ap.add_argument("--V", type=str, default="free", choices=["free", "harmonic", "well"])
    ap.add_argument("--Vstrength", type=float, default=0.02)

    ap.add_argument("--plot", action="store_true")
    ap.add_argument(
        "--checks",
        action="store_true",
        help="Enable extended smoke checks (energy drift, position drift) for free particle",
    )
    args = ap.parse_args()

    N = args.N
    L = args.L
    dx = L / N
    x = (np.arange(N) - N // 2) * dx  # centered grid

    # k grid matching numpy FFT conventions
    dk = 2.0 * math.pi / L
    k = 2.0 * math.pi * np.fft.fftfreq(N, d=dx)

    Vx = potential(x, args.V, args.Vstrength)

    psi = gaussian_wavepacket(x, args.x0, args.k0, args.sigma)
    psi = normalize(psi, dx)

    # initial diagnostics
    psi_k0 = psi_k_continuum(psi, dx=dx, dk=dk)
    x_mean0 = expectation_x(x, psi, dx)
    p_mean0 = expectation_p_from_k(k, psi_k0, dk, args.hbar)
    p_mean0_x = expectation_p_from_x(psi, k, dx, args.hbar)
    E_mean0 = expectation_energy_from_k_and_x(k, psi_k0, dk, Vx, psi, dx, args.hbar, args.m)
    norm0 = float(np.sum(np.abs(psi) ** 2) * dx)

    # evolve
    record_every = max(1, args.steps // 200)
    xs = []
    norms = []
    x_means = []
    p_means = []
    p_means_x = []
    E_means = []
    ts = []

    for n in range(args.steps + 1):
        t = n * args.dt
        if n % record_every == 0:
            psi_k = psi_k_continuum(psi, dx=dx, dk=dk)
            norm = float(np.sum(np.abs(psi) ** 2) * dx)
            x_mean = expectation_x(x, psi, dx)
            p_mean = expectation_p_from_k(k, psi_k, dk, args.hbar)
            p_mean_x = expectation_p_from_x(psi, k, dx, args.hbar)
            E_mean = expectation_energy_from_k_and_x(
                k, psi_k, dk, Vx, psi, dx, args.hbar, args.m,
            )

            ts.append(t)
            norms.append(norm)
            x_means.append(x_mean)
            p_means.append(p_mean)
            p_means_x.append(p_mean_x)
            E_means.append(E_mean)
            # store a snapshot of |psi|^2 occasionally (downsample)
            xs.append(np.abs(psi) ** 2)

        if n < args.steps:
            psi = split_operator_step(psi, Vx, k, args.dt, args.hbar, args.m)

    # final diagnostics
    norm1 = norms[-1]
    max_norm_dev = float(np.max(np.abs(np.array(norms) - norm0)))
    E_mean_end = E_means[-1]
    max_E_dev = float(np.max(np.abs(np.array(E_means) - E_mean0)))

    print("== Schrödinger 1D Reference ==")
    print(f"N={N}  L={L}  dx={dx:g}  dt={args.dt:g}  steps={args.steps}")
    print(f"hbar={args.hbar}  m={args.m}  V={args.V}  Vstrength={args.Vstrength}")
    print("---")
    print(f"norm(t0)={norm0:.12f}")
    print(f"norm(t_end)={norm1:.12f}")
    print(f"max |norm - norm(t0)| over run: {max_norm_dev:.3e}")
    print(f"<x>(t0)={x_mean0:.6f}  <x>(t_end)={x_means[-1]:.6f}")
    print(f"<p>(t0)={p_mean0:.6f}  <p>(t_end)={p_means[-1]:.6f}  [k-Raum]")
    print(f"<p>(t0)={p_mean0_x:.6f}  <p>(t_end)={p_means_x[-1]:.6f}  [x-Raum via Ableitung]")
    print(f"<H>(t0)={E_mean0:.6f}  <H>(t_end)={E_mean_end:.6f}  drift={E_mean_end - E_mean0:.3e}")
    print(f"max |<H> - <H>(t0)| over run: {max_E_dev:.3e}")

    if args.plot:
        import matplotlib.pyplot as plt

        ts_arr = np.array(ts)
        norms_arr = np.array(norms)
        x_means_arr = np.array(x_means)
        p_means_arr = np.array(p_means)
        E_means_arr = np.array(E_means)

        fig, axs = plt.subplots(4, 1, figsize=(10, 12), sharex=True)

        axs[0].plot(ts_arr, norms_arr, lw=2)
        axs[0].set_ylabel("Norm ∫|ψ|² dx")
        axs[0].grid(True)

        axs[1].plot(ts_arr, x_means_arr, lw=2)
        axs[1].set_ylabel("<x>")
        axs[1].grid(True)

        axs[2].plot(ts_arr, p_means_arr, lw=2)
        axs[2].set_ylabel("<p>")
        axs[2].grid(True)

        axs[3].plot(ts_arr, E_means_arr, lw=2)
        axs[3].set_ylabel("<H>")
        axs[3].set_xlabel("t")
        axs[3].grid(True)

        plt.tight_layout()
        plt.show()

    # simple smoke criterion for CI usage
    if max_norm_dev > 5e-4:
        # threshold chosen loose enough for default dt; tighten later
        return 2

    # optional physics-smoke for the default free packet:
    # momentum expectation should be close to ħ*k0 (within discretization error)
    if args.V == "free":
        target_p = args.hbar * args.k0
        # loose threshold; tighten once mapping/stability is pinned down
        if abs(p_means[-1] - target_p) > 0.5:
            print(f"[smoke] unexpected <p> (k-Raum): got {p_means[-1]:.6f}, expected ~ {target_p:.6f}")
            return 3
        if abs(p_means_x[-1] - target_p) > 0.5:
            print(f"[smoke] unexpected <p> (x-Raum): got {p_means_x[-1]:.6f}, expected ~ {target_p:.6f}")
            return 3

    # extended checks (opt-in via --checks)
    if args.checks and args.V == "free":
        t_end = args.steps * args.dt
        # position drift: <x>(t_end) ≈ <x>(t0) + (<p>/m) * t_end
        expected_x_end = x_mean0 + (p_mean0 / args.m) * t_end
        x_drift_err = abs(x_means[-1] - expected_x_end)
        print(f"[check] <x> drift: expected={expected_x_end:.6f}  got={x_means[-1]:.6f}  err={x_drift_err:.3e}")
        if x_drift_err > 0.5:
            print(f"[smoke] unexpected <x> drift: err={x_drift_err:.3e} > 0.5")
            return 4

        # energy conservation: <H> should stay constant for free particle
        print(f"[check] <H> drift: max |<H>-<H>(t0)|={max_E_dev:.3e}")
        if max_E_dev > 1e-6:
            print(f"[smoke] unexpected <H> drift: {max_E_dev:.3e} > 1e-6")
            return 5

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
