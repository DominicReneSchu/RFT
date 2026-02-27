# resonance.py
# © Dominic-René Schu, 2025/2026 – Resonanzfeldtheorie
# Resonanzreaktor: RFT-Kopplungsmodell für resonante Transmutation
#
# Kernidee:
# - Standardmodell: Kernzerfall ist stochastisch, Rate λ = const
# - RFT: Resonante Anregung bei GDR-Frequenz moduliert die
#   effektive Zerfallsrate über die Kopplungseffizienz η(Δφ)
#
# Bewährte Elemente aus FLRW-Simulation:
# - η(Δφ) = cos²(Δφ/2) als Kopplungseffizienz
# - Phasenscan über Δφ = 0...2π

import numpy as np
from material import (HBAR, HBAR_MEV, PI, MEV_TO_J, K_B,
                       plutonium_239, americium_241, uranium_235)


# ============================================================
# 1. Kopplungseffizienz η(Δφ) – bewährt aus FLRW
# ============================================================

def coupling_efficiency(delta_phi):
    """
    Kopplungseffizienz zwischen externem Feld und Kernzustand.
    
    η(Δφ) = cos²(Δφ/2)
    
    - η = 1 bei Δφ = 0 (perfekte Phasenkohärenz, Resonanz)
    - η = 0 bei Δφ = π (Antiresonanz)
    
    Identisch mit der in den FLRW-Simulationen validierten Form.
    
    Args:
        delta_phi: Phasendifferenz in Radiant (Skalar oder Array)
    
    Returns:
        η ∈ [0, 1]
    """
    return np.cos(delta_phi / 2) ** 2


# ============================================================
# 2. GDR-Wirkungsquerschnitt mit RFT-Erweiterung
# ============================================================

def gdr_cross_section_rft(isotope, E_gamma_MeV, delta_phi=0.0):
    """
    GDR-Wirkungsquerschnitt mit RFT-Phasenkorrektur.
    
    σ_RFT(E, Δφ) = σ_GDR(E) · [1 + η(Δφ) · κ]
    
    Standardmodell: κ = 0 → σ_RFT = σ_GDR (keine Phasenabhängigkeit)
    RFT:            κ > 0 → phasenkohärente Anregung verstärkt σ
    
    Args:
        isotope: Isotope-Objekt
        E_gamma_MeV: Photonenenergie in MeV
        delta_phi: Phasendifferenz (0 = kohärent)
    
    Returns:
        Wirkungsquerschnitt in mb
    """
    sigma_base = isotope.gdr_cross_section(E_gamma_MeV)
    eta = coupling_efficiency(delta_phi)
    
    # κ: Kopplungsverstärkungsfaktor
    # Muss experimentell bestimmt werden
    # Konservativer Ansatz: κ = 0.1 (10% Verstärkung bei η=1)
    kappa = 0.1
    
    return sigma_base * (1.0 + eta * kappa)


# ============================================================
# 3. Effektive Zerfallsrate mit RFT-Modulation
# ============================================================

def effective_decay_rate(isotope, delta_phi, kappa=0.1,
                         photon_flux=0.0, E_gamma_MeV=None):
    """
    Effektive Zerfallsrate unter resonanter Anregung.
    
    λ_eff(Δφ) = λ₀ + η(Δφ) · κ · Φ_γ · σ_GDR(E_γ)
    
    Ohne Bestrahlung (Φ_γ = 0): λ_eff = λ₀ (Standardmodell)
    Mit Bestrahlung bei Resonanz (η = 1):
        λ_eff = λ₀ + κ · Φ_γ · σ_GDR(E_GDR)
    
    Args:
        isotope: Isotope-Objekt
        delta_phi: Phasendifferenz
        kappa: Kopplungsstärke
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
    
    # Kopplungseffizienz
    eta = coupling_efficiency(delta_phi)
    
    # Effektive Rate
    lambda_eff = lambda_0 + eta * kappa * photon_flux * sigma_cm2
    
    return lambda_eff


# ============================================================
# 4. Transmutationssimulation: Mit vs. ohne Resonanz
# ============================================================

def simulate_decay(isotope, time_years, n_points=1000,
                   photon_flux=0.0, E_gamma_MeV=None,
                   delta_phi=0.0, kappa=0.1):
    """
    Simuliert den Zerfall eines Isotops über Zeit.
    
    Vergleicht:
    - Standardmodell: N(t) = N₀ · exp(-λ₀·t)
    - RFT: N(t) = N₀ · exp(-λ_eff·t)
    
    Args:
        isotope: Isotope-Objekt
        time_years: Simulationszeitraum in Jahren
        n_points: Anzahl Zeitpunkte
        photon_flux: γ/(cm²·s), 0 = kein externes Feld
        E_gamma_MeV: Photonenenergie
        delta_phi: Phasendifferenz
        kappa: Kopplungsstärke
    
    Returns:
        dict mit t, N_standard, N_rft, lambda_0, lambda_eff
    """
    t_years = np.linspace(0, time_years, n_points)
    t_seconds = t_years * 365.25 * 24 * 3600
    
    # Standardmodell
    lambda_0 = isotope.decay_constant / (365.25 * 24 * 3600)
    N_standard = np.exp(-lambda_0 * t_seconds)
    
    # RFT-Modell
    lambda_eff = effective_decay_rate(
        isotope, delta_phi, kappa, photon_flux, E_gamma_MeV
    )
    N_rft = np.exp(-lambda_eff * t_seconds)
    
    # Effektive Halbwertszeiten
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
               E_gamma_MeV=None, kappa=0.1):
    """
    Phasenscan: λ_eff als Funktion von Δφ.
    
    Analog zum Phasenscan in den FLRW-Simulationen.
    
    Args:
        isotope: Isotope-Objekt
        n_phases: Anzahl Phasenwerte
        photon_flux: γ/(cm²·s)
        E_gamma_MeV: Photonenenergie
        kappa: Kopplungsstärke
    
    Returns:
        dict mit delta_phi, eta, lambda_eff, ratio
    """
    delta_phis = np.linspace(0, 2 * PI, n_phases)
    etas = coupling_efficiency(delta_phis)
    
    lambda_effs = np.array([
        effective_decay_rate(isotope, dp, kappa, photon_flux, E_gamma_MeV)
        for dp in delta_phis
    ])
    
    lambda_0 = isotope.decay_constant / (365.25 * 24 * 3600)
    
    return {
        'delta_phi': delta_phis,
        'eta': etas,
        'lambda_eff': lambda_effs,
        'lambda_0': lambda_0,
        'ratio': lambda_effs / lambda_0,
        'eta_theo': np.cos(delta_phis / 2) ** 2,
    }


def energy_scan(isotope, E_range_MeV=(5, 25), n_energies=200,
                delta_phi=0.0):
    """
    Energiescan: Wirkungsquerschnitt als Funktion von E_γ.
    
    Vergleicht σ_GDR (Standard) mit σ_RFT (phasenkorrigiert).
    
    Args:
        isotope: Isotope-Objekt
        E_range_MeV: (E_min, E_max) in MeV
        n_energies: Anzahl Energiepunkte
        delta_phi: Phasendifferenz
    
    Returns:
        dict mit E_gamma, sigma_standard, sigma_rft
    """
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
    print("=== RFT-Kopplungsmodell: Validierung ===\n")
    
    # 1. Kopplungseffizienz
    print("1. η(Δφ) Stichproben:")
    for dp in [0, PI/4, PI/2, 3*PI/4, PI]:
        print(f"   Δφ = {dp/PI:.2f}π → η = {coupling_efficiency(dp):.4f}")
    
    # 2. GDR-Wirkungsquerschnitt Pu-239
    print(f"\n2. σ_GDR(Pu-239) bei E = {plutonium_239.E_gdr_centroid:.1f} MeV:")
    sigma = plutonium_239.gdr_cross_section(plutonium_239.E_gdr_centroid)
    print(f"   σ = {sigma:.1f} mb")
    
    # 3. Effektive Zerfallsrate
    print(f"\n3. λ_eff(Pu-239) bei Φ_γ = 1e12 γ/(cm²·s):")
    for dp in [0, PI/2, PI]:
        lam = effective_decay_rate(plutonium_239, dp,
                                    photon_flux=1e12)
        lam_0 = plutonium_239.decay_constant / (365.25 * 24 * 3600)
        print(f"   Δφ = {dp/PI:.1f}π: λ_eff/λ₀ = {lam/lam_0:.6f}")