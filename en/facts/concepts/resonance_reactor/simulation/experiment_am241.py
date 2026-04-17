# experiment_am241.py
# © Dominic-René Schu, 2025/2026 – Resonance Field Theory
# Simulation: Experimental confirmation on Am-241
#
# Based on literature values:
# - Soldatov et al. (2001): Photofission of Am isotopes, 6–12 MeV
# - Dietrich & Berman (1988): Atlas of photoneutron cross sections
# - Varlamov et al. (1999): Atlas of Giant Dipole Resonances (IAEA)
# - NNDC/NuDat: Am-241 nuclear data
# - ELI-NP VEGA: γ-beam specifications (up to 10^13 γ/s, ΔE/E < 1%)
#
# Goal: Prediction of measurable quantities for a real experiment
#       and comparison RFT prediction vs. Standard Model

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
import os

# ============================================================
# 1. Natural constants
# ============================================================

HBAR_J = 1.054571817e-34       # ℏ in J·s
HBAR_MEV = 6.582119569e-22     # ℏ in MeV·s
PI = np.pi
MEV_TO_J = 1.602176634e-13     # J/MeV
N_A = 6.02214076e23            # Avogadro
BARN_TO_CM2 = 1e-24            # 1 barn = 10^-24 cm²
MB_TO_CM2 = 1e-27              # 1 mb = 10^-27 cm²
SECONDS_PER_YEAR = 365.25 * 24 * 3600


# ============================================================
# 2. Am-241 Literature values (NNDC, Dietrich-Berman, Soldatov)
# ============================================================

class Am241_Literature:
    """
    Am-241 nuclear data from literature.

    Sources:
    - NNDC NuDat 3.0: Half-life, decay energies
    - Dietrich & Berman (1988): GDR parameters
    - Soldatov et al. (2001): σ(γ,f) at 6–12 MeV
    - Varlamov et al. (1999): GDR Atlas
    """

    # Basic data (NNDC)
    name = "Am-241"
    A = 241
    Z = 95
    half_life_years = 432.6               # NNDC: 432.6 ± 0.6 y
    decay_constant_per_year = np.log(2) / 432.6
    lambda_0_per_s = np.log(2) / (432.6 * SECONDS_PER_YEAR)

    # Alpha decay (NNDC)
    E_alpha_MeV = 5.486                   # Main line (85%)
    E_alpha_mean_MeV = 5.571              # Mean α energy

    # Threshold energies (NNDC/RIPL-3)
    S_n_MeV = 6.647                       # Neutron separation energy
    B_f_MeV = 6.4                         # Fission barrier (estimated)

    # GDR parameters (Dietrich-Berman Atlas / Varlamov Atlas)
    # Double-peak structure (prolate deformation)
    E_gdr_1_MeV = 12.4                   # First GDR peak
    E_gdr_2_MeV = 15.6                   # Second GDR peak
    Gamma_1_MeV = 4.2                    # Width peak 1
    Gamma_2_MeV = 5.0                    # Width peak 2
    sigma_peak_1_mb = 230                # σ at peak 1
    sigma_peak_2_mb = 310                # σ at peak 2
    E_gdr_centroid_MeV = 0.5 * (12.4 + 15.6)  # = 14.0 MeV

    # Experimental photofission (Soldatov et al. 2001)
    # σ(γ,f) in mb at given energy in MeV
    soldatov_E_MeV = np.array([6.0, 6.5, 7.0, 7.5, 8.0, 8.5,
                                9.0, 9.5, 10.0, 10.5, 11.0, 12.0])
    soldatov_sigma_f_mb = np.array([0.5, 1.2, 2.0, 3.5, 5.0, 7.5,
                                     10.0, 13.0, 15.0, 18.0, 22.0, 28.0])

    # Experimental photoneutron (Dietrich-Berman Atlas, interpolated)
    # σ(γ,n) in mb
    berman_E_MeV = np.array([7.0, 8.0, 9.0, 10.0, 11.0, 12.0,
                              13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 20.0])
    berman_sigma_n_mb = np.array([5, 55, 100, 170, 230, 270,
                                   300, 280, 240, 200, 160, 130, 80])


# ============================================================
# 3. GDR cross section: Double Lorentz model
# ============================================================

def gdr_cross_section(E_MeV: float | np.ndarray, am: type = Am241_Literature) -> float:
    """
    GDR photoabsorption cross section for Am-241.
    Double Lorentz profile (prolate deformation).

    σ(E) = Σᵢ σᵢ · (E·Γᵢ)² / [(E²-Eᵢ²)² + (E·Γᵢ)²]

    Parameters from Dietrich-Berman Atlas.
    Weighting: equal (both peaks contribute fully to
    total photoabsorption).
    """
    sigma = 0.0

    peaks = [
        (am.E_gdr_1_MeV, am.Gamma_1_MeV, am.sigma_peak_1_mb),
        (am.E_gdr_2_MeV, am.Gamma_2_MeV, am.sigma_peak_2_mb),
    ]

    for E_i, G_i, sigma_i in peaks:
        num = (E_MeV * G_i) ** 2
        den = (E_MeV**2 - E_i**2)**2 + (E_MeV * G_i)**2
        sigma += sigma_i * num / den

    return sigma


def gdr_cross_section_rft(E_MeV: float | np.ndarray, delta_phi: float = 0.0) -> float | np.ndarray:
    """
    RFT-modulated cross section.

    σ_RFT(E, Δφ) = ε(Δφ) · σ_GDR(E)
    ε(Δφ) = cos²(Δφ/2)
    """
    epsilon = np.cos(delta_phi / 2) ** 2
    return epsilon * gdr_cross_section(E_MeV)


# ============================================================
# 4. RFT coupling efficiency
# ============================================================

def coupling_efficiency(delta_phi: float | np.ndarray) -> float | np.ndarray:
    """η(Δφ) = ε(Δφ) = cos²(Δφ/2)"""
    return np.cos(delta_phi / 2) ** 2


def gdr_frequency_rft(E_MeV: float) -> float:
    """f = E / (π · ℏ) from RFT fundamental formula"""
    return (E_MeV * MEV_TO_J) / (PI * HBAR_J)


# ============================================================
# 5. Effective decay rate
# ============================================================

def effective_decay_rate(delta_phi: float, photon_flux: float, E_gamma_MeV: float | None = None,
                          am: type = Am241_Literature) -> float:
    """
    λ_eff = λ₀ + η(Δφ) · Φ_γ · σ_GDR(E_γ)

    Args:
        delta_phi: Phase difference (rad)
        photon_flux: γ/(cm²·s)
        E_gamma_MeV: Photon energy (None → centroid)

    Returns:
        λ_eff in 1/s
    """
    if E_gamma_MeV is None:
        E_gamma_MeV = am.E_gdr_centroid_MeV

    sigma_mb = gdr_cross_section(E_gamma_MeV)
    sigma_cm2 = sigma_mb * MB_TO_CM2
    eta = coupling_efficiency(delta_phi)

    return am.lambda_0_per_s + eta * photon_flux * sigma_cm2


# ============================================================
# 6. Experimental facilities (researched values)
# ============================================================

class ELI_NP:
    """
    ELI-NP VEGA System (Extreme Light Infrastructure, Măgurele, Romania)

    Source: ELI-NP TDR, Phys. Rev. Accel. Beams 27, 021601 (2024)
    """
    name = "ELI-NP VEGA"
    location = "Măgurele, Romania"
    E_range_MeV = (0.2, 19.5)
    flux_max = 1e13                    # γ/s (design)
    flux_typical = 1e10                # γ/s (currently operational, conservative)
    bandwidth = 0.005                  # ΔE/E < 0.5% (narrow)
    polarization = 0.95                # >95% linearly polarized
    beam_area_cm2 = 0.01              # ~1 mm² spot
    status = "Operational since 2023"


class HIgS:
    """
    HIγS (High Intensity Gamma-ray Source, Duke University, USA)

    Source: TUNL/HIγS facility reports
    """
    name = "HIγS"
    location = "Duke University, Durham, NC, USA"
    E_range_MeV = (1.0, 110.0)
    flux_max = 1e8                     # γ/s (typical)
    flux_typical = 1e7                 # γ/s
    bandwidth = 0.03                   # ΔE/E ~ 3%
    polarization = 0.99                # ~100% polarized
    beam_area_cm2 = 0.1               # ~10 mm² spot
    status = "Operational"


class SLEGS:
    """
    SLEGS (Shanghai Laser Electron Gamma Source, SSRF, China)

    Source: Nucl. Sci. Tech. (2024)
    """
    name = "SLEGS/SSRF"
    location = "Shanghai, China"
    E_range_MeV = (0.25, 21.1)
    flux_max = 1e7                     # γ/s (current)
    flux_typical = 1e6
    bandwidth = 0.05                   # ΔE/E ~ 5%
    polarization = 0.90
    beam_area_cm2 = 0.1
    status = "Operational since 2024"


FACILITIES = [ELI_NP, HIgS, SLEGS]


# ============================================================
# 7. Experiment configuration
# ============================================================

class ExperimentConfig:
    """Configuration for a real Am-241 experiment."""

    def __init__(self, facility: Facility, E_gamma_MeV: float, target_mass_mg: float,
                 measurement_time_hours: float) -> None:
        self.facility = facility
        self.E_gamma_MeV = E_gamma_MeV
        self.target_mass_mg = target_mass_mg
        self.target_mass_kg = target_mass_mg * 1e-6
        self.measurement_time_s = measurement_time_hours * 3600
        self.measurement_time_hours = measurement_time_hours

        am = Am241_Literature

        # Nuclei in the target
        self.N_atoms = (self.target_mass_kg * 1000 * N_A) / am.A

        # Natural decay rate in the target
        self.natural_decays_per_s = am.lambda_0_per_s * self.N_atoms

        # Photon flux on target
        self.photon_flux = facility.flux_typical / facility.beam_area_cm2

        # Cross section at the selected point
        self.sigma_gdr_mb = gdr_cross_section(E_gamma_MeV)
        self.sigma_gdr_cm2 = self.sigma_gdr_mb * MB_TO_CM2

        # Resonant contribution to the rate (Φ · σ)
        self.lambda_res = self.photon_flux * self.sigma_gdr_cm2

        # RFT prediction (Δφ = 0, coherent, η = 1)
        self.lambda_eff_resonant = am.lambda_0_per_s + 1.0 * self.lambda_res

        # SM prediction (no phase dependence, η_eff = 0.5)
        self.lambda_eff_sm = am.lambda_0_per_s + 0.5 * self.lambda_res

        # Amplification factors
        self.ratio_rft = self.lambda_eff_resonant / am.lambda_0_per_s
        self.ratio_sm = self.lambda_eff_sm / am.lambda_0_per_s

        # RFT signature: Ratio of SIGNALS (not total rates)
        # Signal = λ_eff - λ₀ = η · Φ · σ
        # RFT:  η = 1.0 → Signal_coh = 1.0 · Φ · σ
        # SM:   η = 0.5 → Signal_inc = 0.5 · Φ · σ
        # Ratio: Signal_coh / Signal_inc = 2.0 (exact)
        self.signal_ratio = 2.0  # From theory, exact

        # Expected count rates
        self.counts_natural = (self.natural_decays_per_s
                               * self.measurement_time_s)
        self.counts_rft = (self.lambda_eff_resonant * self.N_atoms
                           * self.measurement_time_s)
        self.counts_sm = (self.lambda_eff_sm * self.N_atoms
                          * self.measurement_time_s)

        # Additional decays (signal above background)
        self.signal_rft = self.counts_rft - self.counts_natural
        self.signal_sm = self.counts_sm - self.counts_natural

        # Actual signal ratio (control)
        if self.signal_sm > 0:
            self.signal_ratio_computed = self.signal_rft / self.signal_sm
        else:
            self.signal_ratio_computed = float('inf')

        # Statistical signal (√N Poisson)
        self.sigma_rft = (self.signal_rft / np.sqrt(self.counts_natural)
                          if self.counts_natural > 0 else 0)
        self.sigma_sm = (self.signal_sm / np.sqrt(self.counts_natural)
                         if self.counts_natural > 0 else 0)

        # Difference RFT − SM (the measurable RFT signature)
        self.signal_diff = self.signal_rft - self.signal_sm
        self.sigma_diff = (self.signal_diff / np.sqrt(self.counts_rft)
                           if self.counts_rft > 0 else 0)

    def report(self) -> None:
        """Prints complete experiment report."""
        am = Am241_Literature
        print("=" * 70)
        print(f"EXPERIMENT: Am-241 photoexcitation at {self.E_gamma_MeV} MeV")
        print(f"Facility: {self.facility.name} ({self.facility.location})")
        print("=" * 70)

        print(f"\n--- Am-241 literature values (NNDC, Dietrich-Berman) ---")
        print(f"  Half-life:         {am.half_life_years} y (NNDC)")
        print(f"  λ₀:                {am.lambda_0_per_s:.4e} /s")
        print(f"  E_α (main line):   {am.E_alpha_MeV} MeV (85%)")
        print(f"  S_n:               {am.S_n_MeV} MeV (neutron threshold)")
        print(f"  B_f:               {am.B_f_MeV} MeV (fission barrier)")
        print(f"  GDR Peak 1:        {am.E_gdr_1_MeV} MeV, "
              f"Γ = {am.Gamma_1_MeV} MeV, σ = {am.sigma_peak_1_mb} mb")
        print(f"  GDR Peak 2:        {am.E_gdr_2_MeV} MeV, "
              f"Γ = {am.Gamma_2_MeV} MeV, σ = {am.sigma_peak_2_mb} mb")
        print(f"  GDR centroid:      {am.E_gdr_centroid_MeV} MeV")
        print(f"  f_GDR (RFT):       {gdr_frequency_rft(am.E_gdr_centroid_MeV):.3e} Hz")

        print(f"\n--- Facility ---")
        print(f"  Name:              {self.facility.name}")
        print(f"  E range:           {self.facility.E_range_MeV} MeV")
        print(f"  Flux (typical):    {self.facility.flux_typical:.1e} γ/s")
        print(f"  Bandwidth:         ΔE/E = {self.facility.bandwidth*100:.1f}%")
        print(f"  Polarization:      {self.facility.polarization*100:.0f}%")
        print(f"  Beam cross-section: {self.facility.beam_area_cm2} cm²")

        print(f"\n--- Experiment configuration ---")
        print(f"  E_γ:               {self.E_gamma_MeV} MeV")
        print(f"  Target:            {self.target_mass_mg} mg Am-241")
        print(f"  Nuclei:            {self.N_atoms:.3e}")
        print(f"  Measurement time:  {self.measurement_time_hours} h")
        print(f"  Φ on target:       {self.photon_flux:.3e} γ/(cm²·s)")
        print(f"  σ_GDR(E_γ):        {self.sigma_gdr_mb:.1f} mb")
        print(f"  λ_res = Φ·σ:       {self.lambda_res:.4e} /s")

        print(f"\n--- RFT prediction (κ = 1, Δφ = 0, η = 1) ---")
        print(f"  λ_eff:             {self.lambda_eff_resonant:.4e} /s")
        print(f"  λ_eff/λ₀:          {self.ratio_rft:.6f}")
        print(f"  Count rate (total): {self.counts_rft:.3e}")
        print(f"  Signal (above λ₀): {self.signal_rft:.3e}")
        print(f"  Significance:      {self.sigma_rft:.1f} σ")

        print(f"\n--- Standard Model (η_eff = 0.5, phase-averaged) ---")
        print(f"  λ_eff:             {self.lambda_eff_sm:.4e} /s")
        print(f"  λ_eff/λ₀:          {self.ratio_sm:.6f}")
        print(f"  Count rate (total): {self.counts_sm:.3e}")
        print(f"  Signal (above λ₀): {self.signal_sm:.3e}")

        print(f"\n--- RFT-specific signature ---")
        print(f"  Signal(η=1) / Signal(η=0.5) = "
              f"{self.signal_ratio_computed:.4f}")
        print(f"  Theoretical value:              2.0000 (exact)")
        print(f"  Difference RFT−SM: {self.signal_diff:.3e} decays")
        print(f"  Significance of the difference: {self.sigma_diff:.1f} σ")
        print(f"")
        print(f"  MEASUREMENT PROTOCOL:")
        print(f"  1. Measurement with coherent, polarized γ beam")
        print(f"     → Count Signal_coh = λ_eff(coh) - λ₀")
        print(f"  2. Measurement with incoherent (depolarized) γ beam")
        print(f"     → Count Signal_inc = λ_eff(inc) - λ₀")
        print(f"  3. Form ratio Signal_coh / Signal_inc")
        print(f"     RFT prediction: = 2.0")
        print(f"     SM prediction:  = 1.0 (no phase effect)")

        print(f"\n--- Background ---")
        print(f"  Natural decays: {self.counts_natural:.3e} "
              f"(in {self.measurement_time_hours} h)")
        print(f"  Decays/s (natural): {self.natural_decays_per_s:.3e}")
        print("=" * 70)


# ============================================================
# 8. Plots
# ============================================================

def ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def plot_gdr_profile(output_dir: str) -> None:
    """Plot 1: GDR profile with literature data and RFT modulation."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    E = np.linspace(5, 25, 500)
    am = Am241_Literature

    # Left: GDR profile + literature data
    ax = axes[0]
    sigma_model = [gdr_cross_section(e) for e in E]
    ax.plot(E, sigma_model, 'k-', linewidth=2,
            label='Double Lorentz (Dietrich-Berman)')

    # Soldatov (γ,f) data
    ax.scatter(am.soldatov_E_MeV, am.soldatov_sigma_f_mb,
               c='red', marker='s', s=40, zorder=5,
               label='Soldatov 2001 σ(γ,f)')

    # Berman (γ,n) data
    ax.scatter(am.berman_E_MeV, am.berman_sigma_n_mb,
               c='blue', marker='o', s=40, zorder=5,
               label='Dietrich-Berman σ(γ,n)')

    ax.axvline(am.E_gdr_1_MeV, color='gray', ls=':', alpha=0.5,
               label=f'GDR peaks ({am.E_gdr_1_MeV}, {am.E_gdr_2_MeV} MeV)')
    ax.axvline(am.E_gdr_2_MeV, color='gray', ls=':', alpha=0.5)
    ax.axvline(am.S_n_MeV, color='green', ls='--', alpha=0.5,
               label=f'Sₙ = {am.S_n_MeV} MeV')

    ax.set_xlabel('E_γ (MeV)')
    ax.set_ylabel('σ (mb)')
    ax.set_title('Am-241: GDR profile with literature data')
    ax.legend(fontsize=7, loc='upper right')
    ax.set_xlim(5, 25)
    ax.grid(True, alpha=0.3)

    # Right: RFT modulation at various Δφ
    ax = axes[1]
    for dp, label, color in [(0, 'Δφ=0 (ε=1, resonance)', 'red'),
                              (PI/4, 'Δφ=π/4 (ε=0.85)', 'orange'),
                              (PI/2, 'Δφ=π/2 (ε=0.5)', 'green'),
                              (PI, 'Δφ=π (ε=0, anti)', 'blue')]:
        sigma_rft = [gdr_cross_section_rft(e, dp) for e in E]
        ax.plot(E, sigma_rft, color=color,
                label=f'{label}', linewidth=1.5)

    ax.plot(E, sigma_model, 'k--', linewidth=1,
            label='σ_GDR (literature)')

    ax.set_xlabel('E_γ (MeV)')
    ax.set_ylabel('σ_RFT (mb)')
    ax.set_title('Am-241: RFT prediction σ(E, Δφ)')
    ax.legend(fontsize=7)
    ax.set_xlim(5, 25)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'am241_gdr_profile.png'), dpi=150)
    plt.close()
    print("  → am241_gdr_profile.png")


def plot_phase_prediction(output_dir: str) -> None:
    """Plot 2: Phase scan — the testable RFT signature."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    am = Am241_Literature
    delta_phis = np.linspace(0, 2 * PI, 200)
    etas = coupling_efficiency(delta_phis)

    # Left: η(Δφ) = cos²(Δφ/2)
    ax = axes[0]
    ax.plot(delta_phis / PI, etas, 'b-', linewidth=2,
            label='ε(Δφ) = η(Δφ) = cos²(Δφ/2)')
    ax.axhline(0.5, color='gray', ls='--', alpha=0.5,
               label='Incoherent average (η = 0.5)')
    ax.set_xlabel('Δφ / π')
    ax.set_ylabel('Coupling efficiency ε = η')
    ax.set_title('RFT prediction: Phase dependence')
    ax.legend()
    ax.set_xlim(0, 2)
    ax.set_ylim(-0.05, 1.05)
    ax.grid(True, alpha=0.3)

    # Right: λ_eff/λ₀ as function of Δφ at various fluxes
    ax = axes[1]
    for flux, label, color in [(1e8, 'Φ = 10⁸ (HIγS)', 'blue'),
                                (1e10, 'Φ = 10¹⁰ (ELI-NP conserv.)', 'green'),
                                (1e12, 'Φ = 10¹² (ELI-NP design)', 'red'),
                                (1e14, 'Φ = 10¹⁴ (future)', 'darkred')]:
        ratios = []
        for dp in delta_phis:
            lam = effective_decay_rate(dp, flux / 0.01)  # 0.01 cm² spot
            ratios.append(lam / am.lambda_0_per_s)
        ax.plot(delta_phis / PI, ratios, color=color, label=label,
                linewidth=1.5)

    ax.axhline(1.0, color='k', ls='--', alpha=0.5)
    ax.set_xlabel('Δφ / π')
    ax.set_ylabel('λ_eff / λ₀')
    ax.set_title(f'Am-241: Decay rate vs. phase\nE_γ = {am.E_gdr_centroid_MeV} MeV')
    ax.legend(fontsize=8)
    ax.set_xlim(0, 2)
    ax.set_yscale('log')
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'am241_phase_prediction.png'), dpi=150)
    plt.close()
    print("  → am241_phase_prediction.png")


def plot_facility_comparison(output_dir: str) -> None:
    """Plot 3: Comparison of facilities — significance vs. measurement time."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    am = Am241_Literature
    target_mass_mg = 100  # 100 mg Am-241
    E_gamma = am.E_gdr_centroid_MeV
    hours = np.logspace(-1, 4, 200)

    # Left: Significance (σ) vs. measurement time
    ax = axes[0]
    for fac, color in [(ELI_NP, 'red'), (HIgS, 'blue'), (SLEGS, 'green')]:
        sigmas = []
        for h in hours:
            exp = ExperimentConfig(fac, E_gamma, target_mass_mg, h)
            sigmas.append(max(exp.sigma_rft, 0.01))
        ax.loglog(hours, sigmas, color=color, linewidth=2,
                  label=f'{fac.name} ({fac.flux_typical:.0e} γ/s)')

    ax.axhline(3.0, color='orange', ls='--', label='3σ (evidence)')
    ax.axhline(5.0, color='red', ls='--', label='5σ (discovery)')
    ax.set_xlabel('Measurement time (hours)')
    ax.set_ylabel('Significance (σ)')
    ax.set_title(f'Am-241: Significance vs. measurement time\n'
                 f'{target_mass_mg} mg target, E_γ = {E_gamma} MeV')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0.1, 10000)

    # Right: Signal ratio coherent/incoherent vs. flux
    ax = axes[1]
    fluxes = np.logspace(4, 16, 200)

    # The signal ratio is theoretically always 2.0
    # But the MEASURABLE significance of the difference scales with Φ
    sigmas_diff = []
    for flux in fluxes:
        phi = flux / 0.01  # 0.01 cm² spot
        sigma_mb = gdr_cross_section(E_gamma)
        sigma_cm2 = sigma_mb * MB_TO_CM2
        lambda_res = phi * sigma_cm2

        # Signal difference (η=1 vs η=0.5) per second per nucleus
        delta_signal_per_s = 0.5 * lambda_res * 2.499e20  # N_atoms for 100 mg
        # In 24 h
        delta_signal = delta_signal_per_s * 86400
        # Background
        bg = am.lambda_0_per_s * 2.499e20 * 86400
        sig = delta_signal / np.sqrt(bg) if bg > 0 else 0
        sigmas_diff.append(max(sig, 0.01))

    ax.loglog(fluxes, sigmas_diff, 'r-', linewidth=2,
              label='Significance of the RFT signature\n'
                    '(Signal_coh − Signal_inc)')
    ax.axhline(3.0, color='orange', ls='--', label='3σ')
    ax.axhline(5.0, color='red', ls='--', label='5σ')

    # Mark facilities
    for fac, color, marker in [(ELI_NP, 'red', 'D'),
                                (HIgS, 'blue', 'o'),
                                (SLEGS, 'green', 's')]:
        phi = fac.flux_typical / fac.beam_area_cm2
        sigma_cm2 = gdr_cross_section(E_gamma) * MB_TO_CM2
        lr = phi * sigma_cm2
        ds = 0.5 * lr * 2.499e20 * 86400
        bg = am.lambda_0_per_s * 2.499e20 * 86400
        sig = ds / np.sqrt(bg) if bg > 0 else 0
        ax.scatter([fac.flux_typical], [max(sig, 0.01)],
                   c=color, marker=marker, s=100, zorder=5,
                   label=f'{fac.name}')

    ax.set_xlabel('Photon flux (γ/s, total)')
    ax.set_ylabel('Significance of the RFT signature (σ)')
    ax.set_title('Am-241: Testability of phase dependence\n'
                 '100 mg target, 24 h measurement time')
    ax.legend(fontsize=7, loc='upper left')
    ax.grid(True, alpha=0.3)
    ax.set_xlim(1e4, 1e16)

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'am241_facility_comparison.png'),
                dpi=150)
    plt.close()
    print("  → am241_facility_comparison.png")


def plot_signal_ratio(output_dir: str) -> None:
    """Plot 4: The decisive experiment — Signal_coh / Signal_inc."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    am = Am241_Literature
    E_gamma = am.E_gdr_centroid_MeV

    # Left: Signal ratio as function of Δφ (coherent beam)
    ax = axes[0]
    delta_phis = np.linspace(0.01, PI - 0.01, 200)

    # Signal(Δφ) / Signal(Δφ = π/2) → shows the phase dependence
    for flux, label, color in [(1e10, 'Φ = 10¹⁰', 'green'),
                                (1e12, 'Φ = 10¹²', 'red'),
                                (1e14, 'Φ = 10¹⁴', 'darkred')]:
        phi = flux / 0.01  # on 0.01 cm²
        sigma_cm2 = gdr_cross_section(E_gamma) * MB_TO_CM2

        # Signal = η(Δφ) · Φ · σ · N
        # Normalized to η = 0.5 (incoherent)
        ratios = coupling_efficiency(delta_phis) / 0.5
        ax.plot(delta_phis / PI, ratios, color=color,
                label=label, linewidth=2)

    ax.axhline(2.0, color='red', ls=':', alpha=0.5,
               label='η=1 → ratio = 2.0')
    ax.axhline(1.0, color='gray', ls='--', alpha=0.5,
               label='η=0.5 → ratio = 1.0 (SM)')
    ax.axhline(0.0, color='blue', ls=':', alpha=0.5)
    ax.set_xlabel('Δφ / π')
    ax.set_ylabel('Signal(Δφ) / Signal(incoherent)')
    ax.set_title('RFT signature: Signal ratio vs. phase\n'
                 'Signal = λ_eff − λ₀ (additional decays)')
    ax.legend(fontsize=8)
    ax.set_xlim(0, 1)
    ax.set_ylim(-0.1, 2.5)
    ax.grid(True, alpha=0.3)

    # Right: Measurement protocol visualization
    ax = axes[1]
    phases = ['Δφ = 0\n(resonance)', 'Δφ = π/4', 'Δφ = π/2',
              'Δφ = 3π/4', 'Incoherent\n(SM)']
    etas = [1.0, 0.854, 0.5, 0.146, 0.5]
    signals = [e / 0.5 for e in etas]  # normalized to incoherent
    colors = ['red', 'orange', 'green', 'blue', 'gray']

    bars = ax.bar(phases, signals, color=colors, edgecolor='black',
                  linewidth=0.5, alpha=0.8)
    ax.axhline(1.0, color='black', ls='--', linewidth=1,
               label='SM expectation (η = 0.5)')
    ax.axhline(2.0, color='red', ls=':', linewidth=1,
               label='RFT at Δφ = 0')

    for bar, sig in zip(bars, signals):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.05,
                f'{sig:.2f}', ha='center', fontsize=9, fontweight='bold')

    ax.set_ylabel('Signal / Signal(incoherent)')
    ax.set_title('Measurement protocol: 5 measurement points\n'
                 'SM: all bars = 1.0 | RFT: varies with cos²(Δφ/2)')
    ax.legend(fontsize=9)
    ax.set_ylim(0, 2.7)
    ax.grid(True, alpha=0.3, axis='y')

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'am241_signal_ratio.png'), dpi=150)
    plt.close()
    print("  → am241_signal_ratio.png")


# ============================================================
# 9. Main program
# ============================================================

def main() -> None:
    print("=" * 70)
    print("RESONANCE REACTOR: Experimental prediction Am-241")
    print("Literature-based simulation (Soldatov, Berman, NNDC, ELI-NP)")
    print("κ = 1 (from RFT fundamental formula, no free parameter)")
    print("=" * 70)

    output_dir = "figures"
    ensure_dir(output_dir)

    am = Am241_Literature

    # --- RFT frequencies ---
    print("\n=== RFT frequencies from fundamental formula ===")
    print(f"  f(E₁ = {am.E_gdr_1_MeV} MeV) = "
          f"{gdr_frequency_rft(am.E_gdr_1_MeV):.3e} Hz")
    print(f"  f(E₂ = {am.E_gdr_2_MeV} MeV) = "
          f"{gdr_frequency_rft(am.E_gdr_2_MeV):.3e} Hz")
    print(f"  f(centroid = {am.E_gdr_centroid_MeV} MeV) = "
          f"{gdr_frequency_rft(am.E_gdr_centroid_MeV):.3e} Hz")

    # --- GDR cross section at centroid ---
    sigma_cent = gdr_cross_section(am.E_gdr_centroid_MeV)
    print(f"  σ_GDR(centroid) = {sigma_cent:.1f} mb")

    # --- Experiment 1: ELI-NP (best existing setup) ---
    print("\n" + "=" * 70)
    print("Experiment 1: ELI-NP VEGA (conservative)")
    exp1 = ExperimentConfig(
        facility=ELI_NP,
        E_gamma_MeV=am.E_gdr_centroid_MeV,
        target_mass_mg=100,
        measurement_time_hours=24
    )
    exp1.report()

    # --- Experiment 2: HIγS ---
    print("\n" + "=" * 70)
    print("Experiment 2: HIγS")
    exp2 = ExperimentConfig(
        facility=HIgS,
        E_gamma_MeV=am.E_gdr_centroid_MeV,
        target_mass_mg=100,
        measurement_time_hours=168
    )
    exp2.report()

    # --- Experiment 3: ELI-NP at design flux ---
    class ELI_NP_Design:
        name = "ELI-NP VEGA (Design)"
        location = "Măgurele, Romania"
        E_range_MeV = (0.2, 19.5)
        flux_typical = 1e13
        bandwidth = 0.005
        polarization = 0.95
        beam_area_cm2 = 0.01
        status = "Design specification"

    print("\n" + "=" * 70)
    print("Experiment 3: ELI-NP VEGA (design specification)")
    exp3 = ExperimentConfig(
        facility=ELI_NP_Design,
        E_gamma_MeV=am.E_gdr_centroid_MeV,
        target_mass_mg=100,
        measurement_time_hours=1
    )
    exp3.report()

    # --- Plots ---
    print("\n=== Plots ===")
    plot_gdr_profile(output_dir)
    plot_phase_prediction(output_dir)
    plot_facility_comparison(output_dir)
    plot_signal_ratio(output_dir)

    # --- Summary ---
    print("\n" + "=" * 70)
    print("SUMMARY: Experimental testability")
    print("=" * 70)
    print(f"""
  Am-241 nuclear data (literature):
    t₁/₂ = {am.half_life_years} y, λ₀ = {am.lambda_0_per_s:.3e} /s
    GDR: {am.E_gdr_1_MeV}/{am.E_gdr_2_MeV} MeV (double peak)
    σ_peak = {am.sigma_peak_1_mb}/{am.sigma_peak_2_mb} mb
    σ_GDR(centroid) = {sigma_cent:.1f} mb
    f_GDR (RFT) = {gdr_frequency_rft(am.E_gdr_centroid_MeV):.3e} Hz

  Best existing facility: ELI-NP VEGA
    Flux: 10¹⁰–10¹³ γ/s at 0.2–19.5 MeV
    Polarization: >95% (linear)
    Bandwidth: ΔE/E < 0.5%

  RFT predictions:
    Exp. 1 (ELI-NP, 10¹⁰ γ/s, 24 h):
      λ_eff/λ₀ = {exp1.ratio_rft:.6f}
      Signal = {exp1.signal_rft:.3e} decays
      Significance: {exp1.sigma_rft:.1f} σ

    Exp. 3 (ELI-NP design, 10¹³ γ/s, 1 h):
      λ_eff/λ₀ = {exp3.ratio_rft:.6f}
      Signal = {exp3.signal_rft:.3e} decays
      Significance: {exp3.sigma_rft:.1f} σ

  RFT-SPECIFIC SIGNATURE:
    Signal(coherent) / Signal(incoherent) = 2.0 (exact)
    → Independent of the absolute flux
    → Independent of the target mass
    → Only dependent on η(Δφ) = cos²(Δφ/2)
    → SM prediction: ratio = 1.0 (no phase effect)

  MEASUREMENT PROTOCOL:
    1. γ beam coherent (polarized) → count Signal_coh
    2. γ beam incoherent (depolarized) → count Signal_inc
    3. Signal_coh / Signal_inc = 2.0 (RFT) or 1.0 (SM)
    → Definitive yes/no test of the RFT

  Conclusion: The experiment is feasible with existing technology
              at ELI-NP. The RFT signature (factor 2)
              is a clear, flux-independent signal.
""")
    print("Plots saved under:", output_dir)
    print("Done.")


if __name__ == "__main__":
    main()
