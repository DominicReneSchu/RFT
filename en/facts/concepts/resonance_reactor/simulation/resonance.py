# resonance.py
# © Dominic-René Schu, 2025/2026 – Resonance Field Theory
from __future__ import annotations
# Resonance Reactor: RFT coupling model for resonant transmutation
#
# Core idea:
# - Standard Model: Nuclear decay is stochastic, rate λ = const
# - RFT: Resonant excitation at GDR frequency modulates the
#   effective decay rate via the coupling efficiency η(Δφ)
#
# κ derivation:
# - RFT fundamental formula: E = π · ε(Δφ) · ℏ · f
# - ε(Δφ) = ½(1 + cos Δφ) = cos²(Δφ/2) = η(Δφ)
# - Reaction rate: R = ε · Φ_γ · σ · N = η · Φ_γ · σ · N
# - Comparison: λ_res = η · κ · Φ · σ → κ = 1 (exact)
# - No free parameter.

import numpy as np
from material import (HBAR, HBAR_MEV, PI, MEV_TO_J, K_B,
                       plutonium_239, americium_241, uranium_235)


# ============================================================
# 1. Coupling efficiency η(Δφ) – from RFT Axiom 4
# ============================================================

def coupling_efficiency(delta_phi: float | np.ndarray) -> float | np.ndarray:
    """
    Coupling efficiency between external field and nuclear state.
    
    η(Δφ) = cos²(Δφ/2) = ½(1 + cos Δφ)
    
    Identical to the coupling operator ε(Δφ) of the RFT fundamental formula.
    Validated in FLRW simulations (1530 individual runs).
    
    - η = 1 at Δφ = 0 (perfect phase coherence)
    - η = 0 at Δφ = π (anti-resonance)
    
    Args:
        delta_phi: Phase difference in radians
    
    Returns:
        η ∈ [0, 1]
    """
    return np.cos(delta_phi / 2) ** 2


def coupling_operator(delta_phi: float | np.ndarray) -> float | np.ndarray:
    """
    Coupling operator ε(Δφ) of the RFT fundamental formula.
    
    ε(Δφ) = ½(1 + cos Δφ) = cos²(Δφ/2) = η(Δφ)
    
    In the resonance reactor context: ε determines the fraction
    of the photon energy that resonantly couples to the nucleus.
    
    E_eff = ε(Δφ) · E_γ
    
    Args:
        delta_phi: Phase difference in radians
    
    Returns:
        ε ∈ [0, 1]
    """
    return 0.5 * (1.0 + np.cos(delta_phi))


# ============================================================
# 2. GDR cross section with RFT coupling
# ============================================================

def gdr_cross_section_rft(isotope: Isotope, E_gamma_MeV: float, delta_phi: float = 0.0) -> float:
    """
    GDR cross section with RFT coupling operator.
    
    σ_RFT(E, Δφ) = ε(Δφ) · σ_GDR(E)
    
    Derivation:
    - Photon energy couples via ε to the nucleus
    - E_eff = ε · E_γ → effective cross section
    - At ε = 1: full coupling (coherent excitation)
    - At ε = 0: no coupling (destructive interference)
    
    Standard Model comparison:
    - SM: σ = σ_GDR(E), independent of phase
    - RFT: σ = ε(Δφ) · σ_GDR(E), phase-dependent
    
    Args:
        isotope: Isotope object
        E_gamma_MeV: Photon energy in MeV
        delta_phi: Phase difference
    
    Returns:
        Cross section in mb
    """
    sigma_base = isotope.gdr_cross_section(E_gamma_MeV)
    epsilon = coupling_operator(delta_phi)
    return epsilon * sigma_base


# ============================================================
# 3. Effective decay rate – no free parameter
# ============================================================

def effective_decay_rate(isotope: Isotope, delta_phi: float, photon_flux: float = 0.0,
                         E_gamma_MeV: float | None = None) -> float:
    """
    Effective decay rate under resonant excitation.
    
    λ_eff(Δφ) = λ₀ + η(Δφ) · Φ_γ · σ_GDR(E_γ)
    
    Derivation from RFT (no free parameter):
    - RFT fundamental formula: E = π · ε · ℏ · f
    - ε = η = cos²(Δφ/2)
    - Reaction rate: R = ε · Φ · σ · N
    - → λ_res = η · Φ · σ  (κ = 1, exact)
    
    Limiting cases:
    - Φ_γ = 0: λ_eff = λ₀ (Standard Model)
    - Δφ = 0, Φ > 0: λ_eff = λ₀ + Φ · σ (maximum coupling)
    - Δφ = π: λ_eff = λ₀ (no resonant coupling)
    
    Args:
        isotope: Isotope object
        delta_phi: Phase difference
        photon_flux: Photon fluence in γ/(cm²·s)
        E_gamma_MeV: Photon energy (None → centroid)
    
    Returns:
        λ_eff in 1/s
    """
    # Natural decay rate in 1/s
    lambda_0 = isotope.decay_constant / (365.25 * 24 * 3600)
    
    if photon_flux == 0.0:
        return lambda_0
    
    # Photon energy: default = GDR centroid
    if E_gamma_MeV is None:
        E_gamma_MeV = isotope.E_gdr_centroid
    
    # GDR cross section in cm²
    sigma_mb = isotope.gdr_cross_section(E_gamma_MeV)
    sigma_cm2 = sigma_mb * 1e-27  # mb → cm²
    
    # Coupling efficiency (= coupling operator)
    eta = coupling_efficiency(delta_phi)
    
    # Effective rate: κ = 1 (derived from RFT)
    lambda_eff = lambda_0 + eta * photon_flux * sigma_cm2
    
    return lambda_eff


# ============================================================
# 4. Energy balance
# ============================================================

def energy_balance(isotope: Isotope, delta_phi: float = 0.0, photon_flux: float = 1e12,
                   E_gamma_MeV: float | None = None, target_mass_kg: float = 1.0,
                   time_seconds: float = 3600) -> dict[str, float | str]:
    """
    Energy balance: irradiated vs. released.
    
    Irradiated:
        P_in = Φ_γ · A_target · E_γ
    
    Released (through accelerated decay):
        P_out = (λ_eff - λ₀) · N · E_decay
    
    Net:
        P_net = P_out - P_in
        Q = P_out / P_in  (energy gain factor)
    
    Args:
        isotope: Isotope object
        delta_phi: Phase difference
        photon_flux: γ/(cm²·s)
        E_gamma_MeV: Photon energy
        target_mass_kg: Target mass in kg
        time_seconds: Irradiation duration in s
    
    Returns:
        dict with P_in, P_out, P_net, Q and details
    """
    if E_gamma_MeV is None:
        E_gamma_MeV = isotope.E_gdr_centroid
    
    # Number of particles in the target
    N_A = 6.02214076e23  # Avogadro
    N = target_mass_kg * 1000 * N_A / isotope.A  # Number of nuclei
    
    # Target area (approximation: cylindrical, 10 cm²)
    A_target_cm2 = 10.0
    
    # --- Irradiated power ---
    E_gamma_J = E_gamma_MeV * MEV_TO_J
    P_in_W = photon_flux * A_target_cm2 * E_gamma_J
    
    # --- Released power (resonantly induced) ---
    lambda_0 = isotope.decay_constant / (365.25 * 24 * 3600)
    lambda_eff = effective_decay_rate(isotope, delta_phi,
                                       photon_flux, E_gamma_MeV)
    
    # Additional decays per second through resonance
    delta_lambda = lambda_eff - lambda_0
    decays_per_second = delta_lambda * N
    
    # Energy per decay
    # Alpha decay: E_decay MeV
    # For fission (U-235, Pu-239): ~200 MeV
    E_decay_J = isotope.energy_per_decay * MEV_TO_J
    
    P_out_W = decays_per_second * E_decay_J
    
    # --- Net ---
    P_net_W = P_out_W - P_in_W
    Q = P_out_W / P_in_W if P_in_W > 0 else 0
    
    # --- Fission energy (if fissile) ---
    fissile = isotope.name in ["Uranium-235", "Plutonium-239"]
    E_fission_MeV = 200.0 if fissile else 0.0
    P_out_fission_W = decays_per_second * E_fission_MeV * MEV_TO_J if fissile else 0.0
    Q_fission = P_out_fission_W / P_in_W if (P_in_W > 0 and fissile) else 0.0
    
    return {
        'isotope': isotope.name,
        'N_atoms': N,
        'lambda_0': lambda_0,
        'lambda_eff': lambda_eff,
        'lambda_ratio': lambda_eff / lambda_0,
        'eta': coupling_efficiency(delta_phi),
        'P_in_W': P_in_W,
        'P_out_alpha_W': P_out_W,
        'P_out_fission_W': P_out_fission_W,
        'P_net_alpha_W': P_net_W,
        'P_net_fission_W': P_out_fission_W - P_in_W,
        'Q_alpha': Q,
        'Q_fission': Q_fission,
        'decays_per_second': decays_per_second,
        'photon_flux': photon_flux,
        'E_gamma_MeV': E_gamma_MeV,
    }


# ============================================================
# 5. Simulation functions (as before, κ removed)
# ============================================================

def simulate_decay(isotope: Isotope, time_years: float, n_points: int = 1000,
                   photon_flux: float = 0.0, E_gamma_MeV: float | None = None,
                   delta_phi: float = 0.0) -> dict[str, float | np.ndarray]:
    """Simulates decay: standard vs. RFT."""
    t_years = np.linspace(0, time_years, n_points)
    t_seconds = t_years * 365.25 * 24 * 3600
    
    lambda_0 = isotope.decay_constant / (365.25 * 24 * 3600)
    N_standard = np.exp(-lambda_0 * t_seconds)
    
    lambda_eff = effective_decay_rate(
        isotope, delta_phi, photon_flux, E_gamma_MeV
    )
    N_rft = np.exp(-lambda_eff * t_seconds)
    
    t_half_standard = np.log(2) / lambda_0 / (365.25 * 24 * 3600)
    t_half_rft = np.log(2) / lambda_eff / (365.25 * 24 * 3600)
    
    return {
        't_years': t_years,
        'N_standard': N_standard,
        'N_rft': N_rft,
        'lambda_0': lambda_0,
        'lambda_eff': lambda_eff,
        't_half_standard_years': t_half_standard,
        't_half_rft_years': t_half_rft,
        'eta': coupling_efficiency(delta_phi),
        'delta_phi': delta_phi,
    }


def phase_scan(isotope: Isotope, n_phases: int = 30, photon_flux: float = 1e12,
               E_gamma_MeV: float | None = None) -> dict[str, float | np.ndarray]:
    """Phase scan: λ_eff as function of Δφ."""
    delta_phis = np.linspace(0, 2 * PI, n_phases)
    etas = coupling_efficiency(delta_phis)
    
    lambda_effs = np.array([
        effective_decay_rate(isotope, dp, photon_flux, E_gamma_MeV)
        for dp in delta_phis
    ])
    
    lambda_0 = isotope.decay_constant / (365.25 * 24 * 3600)
    
    return {
        'delta_phi': delta_phis,
        'eta': etas,
        'lambda_eff': lambda_effs,
        'lambda_0': lambda_0,
        'ratio': lambda_effs / lambda_0,
    }


def energy_scan(isotope: Isotope, E_range_MeV: tuple[float, float] = (5, 25), n_energies: int = 200,
                delta_phi: float = 0.0) -> dict[str, float | np.ndarray]:
    """Energy scan: σ as function of E_γ."""
    E_gamma = np.linspace(E_range_MeV[0], E_range_MeV[1], n_energies)
    
    sigma_standard = np.array([
        isotope.gdr_cross_section(E) for E in E_gamma
    ])
    
    sigma_rft = np.array([
        gdr_cross_section_rft(isotope, E, delta_phi) for E in E_gamma
    ])
    
    return {
        'E_gamma_MeV': E_gamma,
        'sigma_standard_mb': sigma_standard,
        'sigma_rft_mb': sigma_rft,
        'delta_phi': delta_phi,
        'eta': coupling_efficiency(delta_phi),
    }


# ============================================================
# Validation
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("RFT coupling model: κ = 1 (from fundamental formula)")
    print("=" * 60)
    
    # 1. ε = η identity
    print("\n1. Coupling operator ε = coupling efficiency η:")
    for dp in [0, PI/4, PI/2, 3*PI/4, PI]:
        eps = coupling_operator(dp)
        eta = coupling_efficiency(dp)
        print(f"   Δφ = {dp/PI:.2f}π → ε = {eps:.4f}, η = {eta:.4f}, "
              f"Δ = {abs(eps-eta):.2e}")
    
    # 2. Amplification factors (κ=1 vs κ=0.1)
    print(f"\n2. λ_eff/λ₀ at Φ = 10¹² γ/(cm²·s), Δφ = 0:")
    for iso in [uranium_235, plutonium_239, americium_241]:
        lam_0 = iso.decay_constant / (365.25 * 24 * 3600)
        lam_eff = effective_decay_rate(iso, 0.0, photon_flux=1e12)
        print(f"   {iso.name}: λ_eff/λ₀ = {lam_eff/lam_0:.1f}")
    
    # 3. Energy balance
    print(f"\n3. Energy balance (1 kg target, Φ = 10¹² γ/(cm²·s)):")
    for iso in [uranium_235, plutonium_239]:
        eb = energy_balance(iso, delta_phi=0.0, photon_flux=1e12,
                            target_mass_kg=1.0)
        print(f"\n   {eb['isotope']}:")
        print(f"     Nuclei:       {eb['N_atoms']:.3e}")
        print(f"     λ_eff/λ₀:     {eb['lambda_ratio']:.1f}")
        print(f"     Decays/s:     {eb['decays_per_second']:.3e}")
        print(f"     P_in:         {eb['P_in_W']:.3e} W")
        print(f"     P_out(α):     {eb['P_out_alpha_W']:.3e} W")
        print(f"     Q(α):         {eb['Q_alpha']:.3f}")
        if eb['Q_fission'] > 0:
            print(f"     P_out(fiss):  {eb['P_out_fission_W']:.3e} W")
            print(f"     Q(fission):   {eb['Q_fission']:.3f}")
