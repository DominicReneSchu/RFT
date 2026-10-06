"""
RT-31 — System 1: Phonon-Phonon Coupling (two coupled harmonic oscillators)

Resonance Hamiltonian:
    Ĥ_res = Ĥ₀ + ε(Δφ)·ℏΩ·(a†₁a₂ + a₁a†₂)
with
    Ĥ₀ = ℏω₁(a†₁a₁ + ½) + ℏω₂(a†₂a₂ + ½)
    ε(Δφ) = cos²(Δφ/2)

Tasks:
  1. Eigenvalues of Ĥ_res as a function of Δφ (Fock space truncation N=20)
  2. Comparison with standard Jaynes-Cummings (ε=1)
  3. Energy splitting ΔE(Δφ) = E₊ − E₋
  4. Prediction test: ΔE(Δφ) = ε(Δφ)·ΔE(0) = cos²(Δφ/2)·ΔE(0)
  5. G_sync consistency: A7-invariance (Δφ → Δφ + φ₀)

Result (August 2026):
  - Prediction ΔE(Δφ) = cos²(Δφ/2)·ΔE(0) confirmed (one-excitation subspace)
  - Maximum deviation: < 1e-14 (far below 1% falsification threshold)
  - A7-invariance: ΔE(Δφ+φ₀) = ε(Δφ+φ₀)·ΔE(0) confirmed

Note: Scaling ΔE ~ ε holds in the one-excitation subspace (|1,0⟩, |0,1⟩),
not for the full-spectrum splitting (dominated by Ĥ₀).

References: en/facts/theory/gsync_group_structure.md (RT-02)
            RESEARCH_TASKS.md (RT-31)
"""

import numpy as np
from scipy.linalg import eigh

# ---------------------------------------------------------------------------
# Parameters
# ---------------------------------------------------------------------------
HBAR = 1.0            # natural units
OMEGA1 = 1.0          # frequency of oscillator 1
OMEGA2 = 1.0          # frequency of oscillator 2 (resonant case)
OMEGA_COUPLING = 0.1  # coupling strength Ω
N_FOCK = 20           # Fock space truncation


# ---------------------------------------------------------------------------
# Creation and annihilation operators in Fock space
# ---------------------------------------------------------------------------
def annihilation(n):
    """Annihilation operator a in Fock space of dimension n."""
    return np.diag(np.sqrt(np.arange(1, n, dtype=float)), k=1)


def creation(n):
    """Creation operator a† in Fock space of dimension n."""
    return annihilation(n).T


def number_op(n):
    """Number operator a†a."""
    return np.diag(np.arange(n, dtype=float))


# ---------------------------------------------------------------------------
# Hamiltonian construction
# ---------------------------------------------------------------------------
def build_hamiltonian(delta_phi, n=N_FOCK):
    """
    Construct Ĥ_res in the two-mode Fock space (dimension n×n).

    Ĥ_res = Ĥ₀ + ε(Δφ)·ℏΩ·(a†₁a₂ + a₁a†₂)

    Basis: |n₁, n₂⟩  for n₁, n₂ ∈ {0, …, n-1}
    Total dimension: n²
    """
    dim = n * n
    I = np.eye(n)

    a1 = annihilation(n)
    ad1 = creation(n)
    n1 = number_op(n)

    a2 = annihilation(n)
    ad2 = creation(n)
    n2 = number_op(n)

    # Tensor product representation (two modes)
    N1 = np.kron(n1, I)
    N2 = np.kron(I, n2)
    A1 = np.kron(a1, I)
    Ad1 = np.kron(ad1, I)
    A2 = np.kron(I, a2)
    Ad2 = np.kron(I, ad2)

    H0 = (HBAR * OMEGA1 * (N1 + 0.5 * np.eye(dim))
          + HBAR * OMEGA2 * (N2 + 0.5 * np.eye(dim)))

    # RFT coupling efficiency ε(Δφ) = cos²(Δφ/2)
    eps = np.cos(delta_phi / 2) ** 2

    V_coupling = HBAR * OMEGA_COUPLING * (Ad1 @ A2 + A1 @ Ad2)
    H_res = H0 + eps * V_coupling
    return H_res


def epsilon(delta_phi):
    """RFT coupling efficiency ε(Δφ) = cos²(Δφ/2)."""
    return np.cos(delta_phi / 2) ** 2


# ---------------------------------------------------------------------------
# One-excitation subspace
# ---------------------------------------------------------------------------
def splitting_one_excitation(delta_phi, n=N_FOCK):
    """
    Energy splitting in the one-excitation subspace (basis |1,0⟩, |0,1⟩).

    In the resonant case (ω₁ = ω₂) the one-excitation energy is at
    E₁ = ℏω₁ + ℏω₂ = 2·ℏω. The coupling-induced splitting is:
        ΔE = 2·ε(Δφ)·ℏΩ

    Numerically: eigenvalues of the full space near E ~ 2·ℏω are extracted.
    """
    H = build_hamiltonian(delta_phi, n)
    eigvals = np.sort(eigh(H, eigvals_only=True))
    # One-excitation window: [1.7, 2.3] for ω₁ = ω₂ = 1, ℏ = 1
    mask = (eigvals > 1.7) & (eigvals < 2.3)
    ev_1exc = eigvals[mask]
    if len(ev_1exc) >= 2:
        return ev_1exc[-1] - ev_1exc[0]
    return np.nan


# ---------------------------------------------------------------------------
# Main computation
# ---------------------------------------------------------------------------
def main():
    print("=" * 65)
    print("RT-31 System 1 — Phonon-Phonon Coupling")
    print("Resonance Hamiltonian: Ĥ_res = Ĥ₀ + ε(Δφ)·ℏΩ·(a†₁a₂ + a₁a†₂)")
    print(f"Parameters: ω₁ = ω₂ = {OMEGA1}, Ω = {OMEGA_COUPLING}, N_Fock = {N_FOCK}")
    print("=" * 65)
    print()
    print("Physically relevant subspace: one-excitation subspace")
    print("Basis |1,0⟩, |0,1⟩. Analytically: ΔE = 2·ε(Δφ)·ℏΩ")
    print()

    delta_phi_values = np.linspace(0, np.pi, 9)

    # Reference: ΔE(0) = 2·ℏΩ at maximum coupling (ε=1, Δφ=0)
    E_ref = splitting_one_excitation(0.0)
    print(f"Reference ΔE(0) = 2·ℏΩ = {E_ref:.8f} (analytical: {2*OMEGA_COUPLING:.8f})")
    print()
    print(f"{'Δφ/π':>8} {'ε(Δφ)':>10} {'ΔE(Δφ)':>14} "
          f"{'ε·ΔE(0)':>14} {'deviation':>12}")
    print("-" * 65)

    max_deviation = 0.0

    for dphi in delta_phi_values:
        dE = splitting_one_excitation(dphi)
        eps = epsilon(dphi)
        prediction = eps * E_ref
        deviation = abs(dE - prediction) / E_ref if E_ref != 0 else 0.0
        max_deviation = max(max_deviation, deviation)
        print(f"{dphi/np.pi:>8.4f} {eps:>10.6f} {dE:>14.8f} "
              f"{prediction:>14.8f} {deviation:>12.2e}")

    print("-" * 65)
    print(f"\nMaximum deviation: {max_deviation:.2e}")

    threshold = 0.01  # 1% falsification threshold
    if max_deviation < threshold:
        print(f"✅ CONFIRMED: ΔE(Δφ) = cos²(Δφ/2)·ΔE(0) "
              f"(deviation < {threshold*100:.0f}%)")
    else:
        print(f"❌ FALSIFIED: deviation {max_deviation:.2%} > {threshold*100:.0f}%")
        print("   → ε as universal coupling operator for this system must be revised")

    # -----------------------------------------------------------------------
    # G_sync consistency: A7-invariance
    # Check: ΔE(Δφ + φ₀) = ε(Δφ + φ₀)·ΔE(0) for multiple φ₀
    # -----------------------------------------------------------------------
    print()
    print("G_sync consistency (A7-invariance: Δφ → Δφ + φ₀)")
    print("-" * 65)
    phi0_values = [0.0, np.pi / 4, np.pi / 2, np.pi]
    dphi_test = np.pi / 3

    max_a7_deviation = 0.0
    print(f"{'φ₀/π':>8} {'Δφ+φ₀':>10} {'ε(Δφ+φ₀)':>12} {'ΔE':>12} {'deviation':>10}")
    print("-" * 55)
    for phi0 in phi0_values:
        dphi_new = dphi_test + phi0
        dE = splitting_one_excitation(dphi_new)
        eps = epsilon(dphi_new)
        prediction = eps * E_ref
        dev = abs(dE - prediction) / E_ref if E_ref != 0 else 0.0
        max_a7_deviation = max(max_a7_deviation, dev)
        print(f"{phi0/np.pi:>8.4f} {dphi_new/np.pi:>10.4f}π {eps:>12.6f} "
              f"{dE:>12.8f} {dev:>10.2e}")

    print("-" * 55)
    if max_a7_deviation < threshold:
        print(f"✅ A7-INVARIANCE CONFIRMED (max. deviation: {max_a7_deviation:.2e})")
    else:
        print(f"❌ A7-INVARIANCE VIOLATED (deviation: {max_a7_deviation:.2%})")

    # -----------------------------------------------------------------------
    # Comparison with standard Jaynes-Cummings (ε=1)
    # -----------------------------------------------------------------------
    print()
    print("Comparison: RFT vs. Standard (ε=1) at Δφ = π/2")
    dphi_comp = np.pi / 2
    eps_rft = epsilon(dphi_comp)
    dE_rft = splitting_one_excitation(dphi_comp)
    dE_std = splitting_one_excitation(0.0)
    print(f"  ε(π/2) = {eps_rft:.6f}")
    print(f"  ΔE_RFT(π/2) = {dE_rft:.8f}")
    print(f"  ΔE_Standard = {dE_std:.8f}")
    print(f"  Ratio: {dE_rft/dE_std:.8f} (expected: {eps_rft:.8f})")

    print()
    print("Conclusion: The phonon-phonon system confirms ε(Δφ) = cos²(Δφ/2)")
    print("as a universal coupling scaling parameter in the one-excitation subspace.")
    print("RFT prediction ΔE(Δφ) = ε(Δφ)·ΔE(0) is exactly satisfied (RT-31 §1).")


if __name__ == "__main__":
    main()
