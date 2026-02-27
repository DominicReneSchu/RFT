# resonance.py
# © Dominic-René Schu, 2025/2026 – Resonanzfeldtheorie
# Resonanzreaktor: RFT-Kopplungsmodell für resonante Transmutation
#
# Kernidee:
# - Standardmodell: Kernzerfall ist stochastisch, Rate λ = const
# - RFT: Resonante Anregung bei GDR-Frequenz moduliert die
#   effektive Zerfallsrate über die Kopplungseffizienz η(Δφ)
#
# κ-Herleitung:
# - RFT-Grundformel: E = π · ε(Δφ) · ℏ · f
# - ε(Δφ) = ½(1 + cos Δφ) = cos²(Δφ/2) = η(Δφ)
# - Reaktionsrate: R = ε · Φ_γ · σ · N = η · Φ_γ · σ · N
# - Vergleich: λ_res = η · κ · Φ · σ → κ = 1 (exakt)
# - Kein freier Parameter.

import numpy as np
from material import (HBAR, HBAR_MEV, PI, MEV_TO_J, K_B,
                       plutonium_239, americium_241, uranium_235)


# ============================================================
# 1. Kopplungseffizienz η(Δφ) – aus RFT-Axiom 4
# ============================================================

def coupling_efficiency(delta_phi):
    """
    Kopplungseffizienz zwischen externem Feld und Kernzustand.
    
    η(Δφ) = cos²(Δφ/2) = ½(1 + cos Δφ)
    
    Identisch mit dem Kopplungsoperator ε(Δφ) der RFT-Grundformel.
    Validiert in FLRW-Simulationen (1530 Einzelläufe).
    
    - η = 1 bei Δφ = 0 (perfekte Phasenkohärenz)
    - η = 0 bei Δφ = π (Antiresonanz)
    
    Args:
        delta_phi: Phasendifferenz in Radiant
    
    Returns:
        η ∈ [0, 1]
    """
    return np.cos(delta_phi / 2) ** 2


def coupling_operator(delta_phi):
    """
    Kopplungsoperator ε(Δφ) der RFT-Grundformel.
    
    ε(Δφ) = ½(1 + cos Δφ) = cos²(Δφ/2) = η(Δφ)
    
    Im Resonanzreaktor-Kontext: ε bestimmt den Bruchteil
    der Photonenenergie, der resonant an den Kern koppelt.
    
    E_eff = ε(Δφ) · E_γ
    
    Args:
        delta_phi: Phasendifferenz in Radiant
    
    Returns:
        ε ∈ [0, 1]
    """
    return 0.5 * (1.0 + np.cos(delta_phi))


# ============================================================
# 2. GDR-Wirkungsquerschnitt mit RFT-Kopplung
# ============================================================

def gdr_cross_section_rft(isotope, E_gamma_MeV, delta_phi=0.0):
    """
    GDR-Wirkungsquerschnitt mit RFT-Kopplungsoperator.
    
    σ_RFT(E, Δφ) = ε(Δφ) · σ_GDR(E)
    
    Herleitung:
    - Photonenenergie koppelt über ε an den Kern
    - E_eff = ε · E_γ → effektiver Wirkungsquerschnitt
    - Bei ε = 1: volle Kopplung (kohärente Anregung)
    - Bei ε = 0: keine Kopplung (destruktive Interferenz)
    
    Standardmodell-Vergleich:
    - SM: σ = σ_GDR(E), unabhängig von Phase
    - RFT: σ = ε(Δφ) · σ_GDR(E), phasenabhängig
    
    Args:
        isotope: Isotope-Objekt
        E_gamma_MeV: Photonenenergie in MeV
        delta_phi: Phasendifferenz
    
    Returns:
        Wirkungsquerschnitt in mb
    """
    sigma_base = isotope.gdr_cross_section(E_gamma_MeV)
    epsilon = coupling_operator(delta_phi)
    return epsilon * sigma_base


# ============================================================
# 3. Effektive Zerfallsrate – kein freier Parameter
# ============================================================

def effective_decay_rate(isotope, delta_phi, photon_flux=0.0,
                         E_gamma_MeV=None):
    """
    Effektive Zerfallsrate unter resonanter Anregung.
    
    λ_eff(Δφ) = λ₀ + η(Δφ) · Φ_γ · σ_GDR(E_γ)
    
    Herleitung aus RFT (kein freier Parameter):
    - RFT-Grundformel: E = π · ε · ℏ · f
    - ε = η = cos²(Δφ/2)
    - Reaktionsrate: R = ε · Φ · σ · N
    - → λ_res = η · Φ · σ  (κ = 1, exakt)
    
    Grenzfälle:
    - Φ_γ = 0: λ_eff = λ₀ (Standardmodell)
    - Δφ = 0, Φ > 0: λ_eff = λ₀ + Φ · σ (maximale Kopplung)
    - Δφ = π: λ_eff = λ₀ (keine resonante Kopplung)
    
    Args:
        isotope: Isotope-Objekt
        delta_phi: Phasendifferenz
        photon_flux: Photonenfluenz in γ/(cm²·s)
        E_gamma_MeV: Photonenenergie (None → Zentroid)
    
    Returns:
        λ_eff in 1/s
    """
    # Natürliche Zerfallsrate in 1/s
    lambda_0 = isotope.decay_constant / (365.25 * 24 * 3600)
    
    if photon_flux == 0.0:
        return lambda_0
    
    # Photonenenergie: Default = GDR-Zentroid
    if E_gamma_MeV is None:
        E_gamma_MeV = isotope.E_gdr_centroid
    
    # GDR-Wirkungsquerschnitt in cm²
    sigma_mb = isotope.gdr_cross_section(E_gamma_MeV)
    sigma_cm2 = sigma_mb * 1e-27  # mb → cm²
    
    # Kopplungseffizienz (= Kopplungsoperator)
    eta = coupling_efficiency(delta_phi)
    
    # Effektive Rate: κ = 1 (aus RFT hergeleitet)
    lambda_eff = lambda_0 + eta * photon_flux * sigma_cm2
    
    return lambda_eff


# ============================================================
# 4. Energiebilanz
# ============================================================

def energy_balance(isotope, delta_phi=0.0, photon_flux=1e12,
                   E_gamma_MeV=None, target_mass_kg=1.0,
                   time_seconds=3600):
    """
    Energiebilanz: Eingestrahlt vs. freigesetzt.
    
    Eingestrahlt:
        P_in = Φ_γ · A_target · E_γ
    
    Freigesetzt (durch beschleunigten Zerfall):
        P_out = (λ_eff - λ₀) · N · E_decay
    
    Netto:
        P_net = P_out - P_in
        Q = P_out / P_in  (Energiegewinnfaktor)
    
    Args:
        isotope: Isotope-Objekt
        delta_phi: Phasendifferenz
        photon_flux: γ/(cm²·s)
        E_gamma_MeV: Photonenenergie
        target_mass_kg: Targetmasse in kg
        time_seconds: Bestrahlungsdauer in s
    
    Returns:
        dict mit P_in, P_out, P_net, Q und Details
    """
    if E_gamma_MeV is None:
        E_gamma_MeV = isotope.E_gdr_centroid
    
    # Teilchenzahl im Target
    N_A = 6.02214076e23  # Avogadro
    N = target_mass_kg * 1000 * N_A / isotope.A  # Anzahl Kerne
    
    # Target-Fläche (Näherung: zylindrisch, 10 cm²)
    A_target_cm2 = 10.0
    
    # --- Eingestrahlte Leistung ---
    E_gamma_J = E_gamma_MeV * MEV_TO_J
    P_in_W = photon_flux * A_target_cm2 * E_gamma_J
    
    # --- Freigesetzte Leistung (resonant induziert) ---
    lambda_0 = isotope.decay_constant / (365.25 * 24 * 3600)
    lambda_eff = effective_decay_rate(isotope, delta_phi,
                                       photon_flux, E_gamma_MeV)
    
    # Zusätzliche Zerfälle pro Sekunde durch Resonanz
    delta_lambda = lambda_eff - lambda_0
    decays_per_second = delta_lambda * N
    
    # Energie pro Zerfall
    # Alpha-Zerfall: E_decay MeV
    # Bei Spaltung (U-235, Pu-239): ~200 MeV
    E_decay_J = isotope.energy_per_decay * MEV_TO_J
    
    P_out_W = decays_per_second * E_decay_J
    
    # --- Netto ---
    P_net_W = P_out_W - P_in_W
    Q = P_out_W / P_in_W if P_in_W > 0 else 0
    
    # --- Spaltungsenergie (falls spaltbar) ---
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
# 5. Simulationsfunktionen (wie vorher, κ entfernt)
# ============================================================

def simulate_decay(isotope, time_years, n_points=1000,
                   photon_flux=0.0, E_gamma_MeV=None,
                   delta_phi=0.0):
    """Simuliert Zerfall: Standard vs. RFT."""
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


def phase_scan(isotope, n_phases=30, photon_flux=1e12,
               E_gamma_MeV=None):
    """Phasenscan: λ_eff als Funktion von Δφ."""
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


def energy_scan(isotope, E_range_MeV=(5, 25), n_energies=200,
                delta_phi=0.0):
    """Energiescan: σ als Funktion von E_γ."""
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
# Validierung
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("RFT-Kopplungsmodell: κ = 1 (aus Grundformel)")
    print("=" * 60)
    
    # 1. ε = η Identität
    print("\n1. Kopplungsoperator ε = Kopplungseffizienz η:")
    for dp in [0, PI/4, PI/2, 3*PI/4, PI]:
        eps = coupling_operator(dp)
        eta = coupling_efficiency(dp)
        print(f"   Δφ = {dp/PI:.2f}π → ε = {eps:.4f}, η = {eta:.4f}, "
              f"Δ = {abs(eps-eta):.2e}")
    
    # 2. Verstärkungsfaktoren (κ=1 vs κ=0.1)
    print(f"\n2. λ_eff/λ₀ bei Φ = 10¹² γ/(cm²·s), Δφ = 0:")
    for iso in [uranium_235, plutonium_239, americium_241]:
        lam_0 = iso.decay_constant / (365.25 * 24 * 3600)
        lam_eff = effective_decay_rate(iso, 0.0, photon_flux=1e12)
        print(f"   {iso.name}: λ_eff/λ₀ = {lam_eff/lam_0:.1f}")
    
    # 3. Energiebilanz
    print(f"\n3. Energiebilanz (1 kg Target, Φ = 10¹² γ/(cm²·s)):")
    for iso in [uranium_235, plutonium_239]:
        eb = energy_balance(iso, delta_phi=0.0, photon_flux=1e12,
                            target_mass_kg=1.0)
        print(f"\n   {eb['isotope']}:")
        print(f"     Kerne:        {eb['N_atoms']:.3e}")
        print(f"     λ_eff/λ₀:     {eb['lambda_ratio']:.1f}")
        print(f"     Zerfälle/s:   {eb['decays_per_second']:.3e}")
        print(f"     P_in:         {eb['P_in_W']:.3e} W")
        print(f"     P_out(α):     {eb['P_out_alpha_W']:.3e} W")
        print(f"     Q(α):         {eb['Q_alpha']:.3f}")
        if eb['Q_fission'] > 0:
            print(f"     P_out(Spalt): {eb['P_out_fission_W']:.3e} W")
            print(f"     Q(Spaltung):  {eb['Q_fission']:.3f}")