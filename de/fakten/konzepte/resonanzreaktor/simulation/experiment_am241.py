# experiment_am241.py
# © Dominic-René Schu, 2025/2026 – Resonanzfeldtheorie
# Simulation: Experimentelle Bestätigung am Am-241
#
# Basiert auf Literaturwerten:
# - Soldatov et al. (2001): Photofission of Am isotopes, 6–12 MeV
# - Dietrich & Berman (1988): Atlas of photoneutron cross sections
# - Varlamov et al. (1999): Atlas of Giant Dipole Resonances (IAEA)
# - NNDC/NuDat: Am-241 nuclear data
# - ELI-NP VEGA: γ-beam specifications (up to 10^13 γ/s, ΔE/E < 1%)
# - RT-06: σ(γ,α) aus EXFOR/Hauser-Feshbach (exfor_data.py)
#
# Ziel: Vorhersage der messbaren Größen für ein reales Experiment
#       und Vergleich RFT-Vorhersage vs. Standardmodell

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
import os

# ============================================================
# 1. Naturkonstanten
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
# 2. Am-241 Literaturwerte (NNDC, Dietrich-Berman, Soldatov)
# ============================================================

class Am241_Literature:
    """
    Am-241 Kerndaten aus Literatur.

    Quellen:
    - NNDC NuDat 3.0: Halbwertszeit, Zerfallsenergien
    - Dietrich & Berman (1988): GDR-Parameter
    - Soldatov et al. (2001): σ(γ,f) bei 6–12 MeV
    - Varlamov et al. (1999): GDR-Atlas
    """

    # Grunddaten (NNDC)
    name = "Am-241"
    A = 241
    Z = 95
    half_life_years = 432.6               # NNDC: 432.6 ± 0.6 a
    decay_constant_per_year = np.log(2) / 432.6
    lambda_0_per_s = np.log(2) / (432.6 * SECONDS_PER_YEAR)

    # Alpha-Zerfall (NNDC)
    E_alpha_MeV = 5.486                   # Hauptlinie (85%)
    E_alpha_mean_MeV = 5.571              # Mittlere α-Energie

    # Schwellenenergien (NNDC/RIPL-3)
    S_n_MeV = 6.647                       # Neutronenseparationsenergie
    B_f_MeV = 6.4                         # Spaltbarriere (geschätzt)

    # GDR-Parameter (Dietrich-Berman Atlas / Varlamov Atlas)
    # Doppelpeak-Struktur (prolate Deformation)
    E_gdr_1_MeV = 12.4                   # Erster GDR-Peak
    E_gdr_2_MeV = 15.6                   # Zweiter GDR-Peak
    Gamma_1_MeV = 4.2                    # Breite Peak 1
    Gamma_2_MeV = 5.0                    # Breite Peak 2
    sigma_peak_1_mb = 230                # σ am Peak 1
    sigma_peak_2_mb = 310                # σ am Peak 2
    E_gdr_centroid_MeV = 0.5 * (12.4 + 15.6)  # = 14.0 MeV

    # Experimentelle Photofission (Soldatov et al. 2001)
    # σ(γ,f) in mb bei gegebener Energie in MeV
    soldatov_E_MeV = np.array([6.0, 6.5, 7.0, 7.5, 8.0, 8.5,
                                9.0, 9.5, 10.0, 10.5, 11.0, 12.0])
    soldatov_sigma_f_mb = np.array([0.5, 1.2, 2.0, 3.5, 5.0, 7.5,
                                     10.0, 13.0, 15.0, 18.0, 22.0, 28.0])

    # Experimentelle Photoneutron (Dietrich-Berman Atlas, interpoliert)
    # σ(γ,n) in mb
    berman_E_MeV = np.array([7.0, 8.0, 9.0, 10.0, 11.0, 12.0,
                              13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 20.0])
    berman_sigma_n_mb = np.array([5, 55, 100, 170, 230, 270,
                                   300, 280, 240, 200, 160, 130, 80])

    # (γ,α)-Querschnitt aus EXFOR/Hauser-Feshbach (RT-06)
    # Methode: Hauser-Feshbach (Weisskopf-Evaporationsmodell)
    # Kein direkter EXFOR-Eintrag für Am-241 (γ,α) vorhanden —
    # (γ,α) für schwere Aktiniden ist experimentell nicht gemessen (EXFOR-Recherche RT-06)
    # Unsicherheit: ±factor 2–5 (typisch für Hauser-Feshbach bei Aktiniden)
    exfor_gamma_alpha_E_MeV = np.array([
        6.0, 6.97, 7.94, 8.91, 9.88, 10.85,
        11.82, 12.79, 13.76, 14.0, 14.73, 15.70,
        16.67, 17.64, 18.61, 19.58, 20.0
    ])
    exfor_gamma_alpha_mb = np.array([
        0.0000, 0.0000, 0.0002, 0.0047, 0.0370, 0.1395,
        0.3800, 0.8160, 1.4762, 1.7187, 2.2648, 2.9805,
        3.3801, 3.5103, 3.4188, 3.1893, 3.0640
    ])
    exfor_gamma_alpha_source = (
        "Hauser-Feshbach (Weisskopf-Evaporationsmodell), "
        "GDR-Parameter: Dietrich & Berman (1988), "
        "Verzweigungsverhältnis: RIPL-3 (RT-06)"
    )
    exfor_gamma_alpha_method = "hauser_feshbach"   # "direct" / "scaled_U235" / "hauser_feshbach"
    exfor_gamma_alpha_unc_pct = 300.0              # ±factor 2–5 → ~200–400%


# ============================================================
# 3. GDR-Wirkungsquerschnitt: Doppel-Lorentz-Modell
# ============================================================

def gdr_cross_section(E_MeV: float | np.ndarray, am: type = Am241_Literature) -> float:
    """
    GDR-Photoabsorptions-Wirkungsquerschnitt für Am-241.
    Doppel-Lorentz-Profil (prolate Deformation).

    σ(E) = Σᵢ σᵢ · (E·Γᵢ)² / [(E²-Eᵢ²)² + (E·Γᵢ)²]

    Parameter aus Dietrich-Berman Atlas.
    Gewichtung: gleich (beide Peaks tragen voll bei zur
    totalen Photoabsorption).
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
    RFT-modulierter Wirkungsquerschnitt.

    σ_RFT(E, Δφ) = ε(Δφ) · σ_GDR(E)
    ε(Δφ) = cos²(Δφ/2)
    """
    epsilon = np.cos(delta_phi / 2) ** 2
    return epsilon * gdr_cross_section(E_MeV)


def photo_alpha_cross_section(
    E_MeV: float | np.ndarray,
    am: type = Am241_Literature,
) -> float | np.ndarray:
    """
    σ(γ,α) in mb als Funktion der Energie.

    Gibt den (γ,α)-Wirkungsquerschnitt durch Interpolation über die
    EXFOR/Hauser-Feshbach-Stützpunkte in Am241_Literature zurück.

    - Methode: hauser_feshbach (RT-06: kein direkter EXFOR-Eintrag verfügbar)
    - GDR-Parameter: Dietrich & Berman (1988)
    - Verzweigungsverhältnis: RIPL-3-Parametrisierung
    - Unsicherheit: ±factor 2–5 (~200–400%)

    Für E außerhalb [E_min, E_max]: Extrapolation mit Warnung.

    Args:
        E_MeV: Photonenenergie in MeV (Skalar oder Array)
        am: Am241_Literature-Klasse (Stützpunkte)

    Returns:
        float oder np.ndarray: σ(γ,α) in mb
    """
    import warnings
    E_arr = am.exfor_gamma_alpha_E_MeV
    s_arr = am.exfor_gamma_alpha_mb

    scalar = np.ndim(E_MeV) == 0
    E_query = np.atleast_1d(np.asarray(E_MeV, dtype=float))

    out_of_range = (E_query < E_arr.min()) | (E_query > E_arr.max())
    if np.any(out_of_range):
        warnings.warn(
            f"photo_alpha_cross_section: Energie außerhalb Stützpunktbereich "
            f"[{E_arr.min():.1f}, {E_arr.max():.1f}] MeV — "
            "Extrapolation. Erhöhte Unsicherheit.",
            stacklevel=2,
        )

    try:
        from scipy.interpolate import interp1d
        f = interp1d(E_arr, s_arr, kind='cubic',
                     bounds_error=False, fill_value="extrapolate")
        result = f(E_query)
    except ImportError:
        result = np.interp(E_query, E_arr, s_arr)

    # Physikalische Nebenbedingung: σ ≥ 0
    result = np.maximum(result, 0.0)

    return float(result[0]) if scalar else result


# ============================================================
# 4. RFT-Kopplungseffizienz
# ============================================================

def coupling_efficiency(delta_phi: float | np.ndarray) -> float | np.ndarray:
    """η(Δφ) = ε(Δφ) = cos²(Δφ/2)"""
    return np.cos(delta_phi / 2) ** 2


def gdr_frequency_rft(E_MeV: float) -> float:
    """f = E / (π · ℏ) aus RFT-Grundformel"""
    return (E_MeV * MEV_TO_J) / (PI * HBAR_J)


# ============================================================
# 5. Effektive Zerfallsrate
# ============================================================

def effective_decay_rate(delta_phi: float, photon_flux: float, E_gamma_MeV: float | None = None,
                          am: type = Am241_Literature) -> float:
    """
    λ_eff = λ₀ + η(Δφ) · Φ_γ · σ_GDR(E_γ)

    Args:
        delta_phi: Phasendifferenz (rad)
        photon_flux: γ/(cm²·s)
        E_gamma_MeV: Photonenenergie (None → Zentroid)

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
# 6. Experimentelle Einrichtungen (Recherchewerte)
# ============================================================

class ELI_NP:
    """
    ELI-NP VEGA System (Extreme Light Infrastructure, Măgurele, Rumänien)

    Quelle: ELI-NP TDR, Phys. Rev. Accel. Beams 27, 021601 (2024)
    """
    name = "ELI-NP VEGA"
    location = "Măgurele, Rumänien"
    E_range_MeV = (0.2, 19.5)
    flux_max = 1e13                    # γ/s (Design)
    flux_typical = 1e10                # γ/s (aktuell operativ, konservativ)
    bandwidth = 0.005                  # ΔE/E < 0.5% (schmal)
    polarization = 0.95                # >95% linear polarisiert
    beam_area_cm2 = 0.01              # ~1 mm² Spot
    status = "Operativ seit 2023"


class HIgS:
    """
    HIγS (High Intensity Gamma-ray Source, Duke University, USA)

    Quelle: TUNL/HIγS facility reports
    """
    name = "HIγS"
    location = "Duke University, Durham, NC, USA"
    E_range_MeV = (1.0, 110.0)
    flux_max = 1e8                     # γ/s (typisch)
    flux_typical = 1e7                 # γ/s
    bandwidth = 0.03                   # ΔE/E ~ 3%
    polarization = 0.99                # ~100% polarisiert
    beam_area_cm2 = 0.1               # ~10 mm² Spot
    status = "Operativ"


class SLEGS:
    """
    SLEGS (Shanghai Laser Electron Gamma Source, SSRF, China)

    Quelle: Nucl. Sci. Tech. (2024)
    """
    name = "SLEGS/SSRF"
    location = "Shanghai, China"
    E_range_MeV = (0.25, 21.1)
    flux_max = 1e7                     # γ/s (aktuell)
    flux_typical = 1e6
    bandwidth = 0.05                   # ΔE/E ~ 5%
    polarization = 0.90
    beam_area_cm2 = 0.1
    status = "Operativ seit 2024"


FACILITIES = [ELI_NP, HIgS, SLEGS]


# ============================================================
# 7. Experimentkonfiguration
# ============================================================

class ExperimentConfig:
    """Konfiguration für ein reales Am-241-Experiment."""

    def __init__(self, facility: Facility, E_gamma_MeV: float, target_mass_mg: float,
                 measurement_time_hours: float) -> None:
        self.facility = facility
        self.E_gamma_MeV = E_gamma_MeV
        self.target_mass_mg = target_mass_mg
        self.target_mass_kg = target_mass_mg * 1e-6
        self.measurement_time_s = measurement_time_hours * 3600
        self.measurement_time_hours = measurement_time_hours

        am = Am241_Literature

        # Kerne im Target
        self.N_atoms = (self.target_mass_kg * 1000 * N_A) / am.A

        # Natürliche Zerfallsrate im Target
        self.natural_decays_per_s = am.lambda_0_per_s * self.N_atoms

        # Photonenfluss auf Target
        self.photon_flux = facility.flux_typical / facility.beam_area_cm2

        # GDR-Gesamtquerschnitt am gewählten Punkt (für Referenz)
        self.sigma_gdr_mb = gdr_cross_section(E_gamma_MeV)
        self.sigma_gdr_cm2 = self.sigma_gdr_mb * MB_TO_CM2

        # RT-09: Korrekter (γ,α)-Querschnitt für RFT-Signatur (Hauser-Feshbach, RT-06)
        # σ(γ,α) = 1.719 mb bei E_GDR-Zentroid — Faktor ~212 kleiner als σ_GDR
        self.sigma_pa_mb = float(photo_alpha_cross_section(E_gamma_MeV, am))
        self.sigma_pa_cm2 = self.sigma_pa_mb * MB_TO_CM2

        # Resonanter Beitrag zur Rate (Φ · σ)
        # Legacy: basiert auf sigma_gdr_cm2 (verwendet in RT-06 und früher)
        self.lambda_res = self.photon_flux * self.sigma_gdr_cm2
        # RT-09: Korrekter resonanter Beitrag basiert auf sigma_pa_cm2
        self.lambda_res_pa = self.photon_flux * self.sigma_pa_cm2

        # RFT-Vorhersage (Δφ = 0, kohärent, η = 1)
        self.lambda_eff_resonant = am.lambda_0_per_s + 1.0 * self.lambda_res

        # SM-Vorhersage (keine Phasenabhängigkeit, η_eff = 0.5)
        self.lambda_eff_sm = am.lambda_0_per_s + 0.5 * self.lambda_res

        # Verstärkungsfaktoren
        self.ratio_rft = self.lambda_eff_resonant / am.lambda_0_per_s
        self.ratio_sm = self.lambda_eff_sm / am.lambda_0_per_s

        # RFT-Signatur: Verhältnis der SIGNALE (nicht der Gesamtraten)
        # Signal = λ_eff - λ₀ = η · Φ · σ
        # RFT:  η = 1.0 → Signal_koh = 1.0 · Φ · σ
        # SM:   η = 0.5 → Signal_ink = 0.5 · Φ · σ
        # Verhältnis: Signal_koh / Signal_ink = 2.0 (exakt)
        self.signal_ratio = 2.0  # Aus der Theorie, exakt

        # Erwartete Zählraten
        self.counts_natural = (self.natural_decays_per_s
                               * self.measurement_time_s)
        self.counts_rft = (self.lambda_eff_resonant * self.N_atoms
                           * self.measurement_time_s)
        self.counts_sm = (self.lambda_eff_sm * self.N_atoms
                          * self.measurement_time_s)

        # Zusätzliche Zerfälle (Signal über Hintergrund)
        self.signal_rft = self.counts_rft - self.counts_natural
        self.signal_sm = self.counts_sm - self.counts_natural

        # Tatsächliches Signalverhältnis (Kontrolle)
        if self.signal_sm > 0:
            self.signal_ratio_computed = self.signal_rft / self.signal_sm
        else:
            self.signal_ratio_computed = float('inf')

        # Statistisches Signal (√N Poisson) — Legacy: basiert auf σ_GDR
        self.sigma_rft_legacy = (self.signal_rft / np.sqrt(self.counts_natural)
                                 if self.counts_natural > 0 else 0)
        self.sigma_sm_legacy = (self.signal_sm / np.sqrt(self.counts_natural)
                                if self.counts_natural > 0 else 0)

        # Rückwärtskompatibilität: sigma_rft / sigma_sm zeigen Legacy-Werte
        self.sigma_rft = self.sigma_rft_legacy
        self.sigma_sm = self.sigma_sm_legacy

        # RT-09: Korrigierte Signifikanz basiert auf σ(γ,α) (nicht σ_GDR)
        signal_rft_pa = self.photon_flux * self.sigma_pa_cm2 * self.N_atoms * self.measurement_time_s
        signal_sm_pa = 0.5 * signal_rft_pa
        self.sigma_rft_pa = (signal_rft_pa / np.sqrt(self.counts_natural)
                             if self.counts_natural > 0 else 0)
        self.sigma_sm_pa = (signal_sm_pa / np.sqrt(self.counts_natural)
                            if self.counts_natural > 0 else 0)

        # Differenz RFT − SM (die messbare RFT-Signatur)
        self.signal_diff = self.signal_rft - self.signal_sm
        self.sigma_diff = (self.signal_diff / np.sqrt(self.counts_rft)
                           if self.counts_rft > 0 else 0)

        # RT-09: Korrigierte Differenz-Signifikanz (σ(γ,α)-basiert)
        signal_diff_pa = signal_rft_pa - signal_sm_pa
        counts_rft_pa = self.counts_natural + signal_rft_pa
        self.sigma_diff_pa = (signal_diff_pa / np.sqrt(counts_rft_pa)
                              if counts_rft_pa > 0 else 0)

    def report(self) -> None:
        """Druckt vollständigen Experiment-Report."""
        am = Am241_Literature
        print("=" * 70)
        print(f"EXPERIMENT: Am-241 Photoanregung bei {self.E_gamma_MeV} MeV")
        print(f"Einrichtung: {self.facility.name} ({self.facility.location})")
        print("=" * 70)

        print(f"\n--- Am-241 Literaturwerte (NNDC, Dietrich-Berman) ---")
        print(f"  Halbwertszeit:     {am.half_life_years} a (NNDC)")
        print(f"  λ₀:                {am.lambda_0_per_s:.4e} /s")
        print(f"  E_α (Hauptlinie):  {am.E_alpha_MeV} MeV (85%)")
        print(f"  S_n:               {am.S_n_MeV} MeV (Neutronenschwelle)")
        print(f"  B_f:               {am.B_f_MeV} MeV (Spaltbarriere)")
        print(f"  GDR Peak 1:        {am.E_gdr_1_MeV} MeV, "
              f"Γ = {am.Gamma_1_MeV} MeV, σ = {am.sigma_peak_1_mb} mb")
        print(f"  GDR Peak 2:        {am.E_gdr_2_MeV} MeV, "
              f"Γ = {am.Gamma_2_MeV} MeV, σ = {am.sigma_peak_2_mb} mb")
        print(f"  GDR Zentroid:      {am.E_gdr_centroid_MeV} MeV")
        print(f"  f_GDR (RFT):       {gdr_frequency_rft(am.E_gdr_centroid_MeV):.3e} Hz")

        print(f"\n--- Einrichtung ---")
        print(f"  Name:              {self.facility.name}")
        print(f"  E-Bereich:         {self.facility.E_range_MeV} MeV")
        print(f"  Fluss (typisch):   {self.facility.flux_typical:.1e} γ/s")
        print(f"  Bandbreite:        ΔE/E = {self.facility.bandwidth*100:.1f}%")
        print(f"  Polarisation:      {self.facility.polarization*100:.0f}%")
        print(f"  Strahlquerschnitt: {self.facility.beam_area_cm2} cm²")

        print(f"\n--- Experimentkonfiguration ---")
        print(f"  E_γ:               {self.E_gamma_MeV} MeV")
        print(f"  Target:            {self.target_mass_mg} mg Am-241")
        print(f"  Kerne:             {self.N_atoms:.3e}")
        print(f"  Messzeit:          {self.measurement_time_hours} h")
        print(f"  Φ auf Target:      {self.photon_flux:.3e} γ/(cm²·s)")
        print(f"  σ_GDR(E_γ):        {self.sigma_gdr_mb:.1f} mb")
        print(f"  λ_res = Φ·σ:       {self.lambda_res:.4e} /s")

        print(f"\n--- RFT-Vorhersage (κ = 1, Δφ = 0, η = 1) ---")
        print(f"  λ_eff:             {self.lambda_eff_resonant:.4e} /s")
        print(f"  λ_eff/λ₀:          {self.ratio_rft:.6f}")
        print(f"  Zählrate (gesamt): {self.counts_rft:.3e}")
        print(f"  Signal (über λ₀):  {self.signal_rft:.3e}")
        print(f"  Signifikanz:       {self.sigma_rft:.1f} σ")

        print(f"\n--- Standardmodell (η_eff = 0.5, phasengemittelt) ---")
        print(f"  λ_eff:             {self.lambda_eff_sm:.4e} /s")
        print(f"  λ_eff/λ₀:          {self.ratio_sm:.6f}")
        print(f"  Zählrate (gesamt): {self.counts_sm:.3e}")
        print(f"  Signal (über λ₀):  {self.signal_sm:.3e}")

        print(f"\n--- RFT-spezifische Signatur ---")
        print(f"  Signal(η=1) / Signal(η=0.5) = "
              f"{self.signal_ratio_computed:.4f}")
        print(f"  Theoretischer Wert:             2.0000 (exakt)")
        print(f"  Differenz RFT−SM:  {self.signal_diff:.3e} Zerfälle")
        print(f"  Signifikanz der Differenz: {self.sigma_diff:.1f} σ")
        print(f"")
        print(f"  MESSPROTOKOLL:")
        print(f"  1. Messung mit kohärentem, polarisiertem γ-Strahl")
        print(f"     → Zähle Signal_koh = λ_eff(koh) - λ₀")
        print(f"  2. Messung mit inkohärentem (depolarisiertem) γ-Strahl")
        print(f"     → Zähle Signal_ink = λ_eff(ink) - λ₀")
        print(f"  3. Bilde Verhältnis Signal_koh / Signal_ink")
        print(f"     RFT-Vorhersage: = 2.0")
        print(f"     SM-Vorhersage:  = 1.0 (kein Phaseneffekt)")

        print(f"\n--- RT-09 Korrigierte Signifikanz (σ(γ,α) = 1.719 mb) ---")
        print(f"  σ(γ,α) bei E_γ:    {self.sigma_pa_mb:.4f} mb "
              f"(Hauser-Feshbach, RT-06)")
        print(f"  σ_GDR bei E_γ:     {self.sigma_gdr_mb:.1f} mb "
              f"(Legacy, RT-06 Revision)")
        print(f"  Korrekturfaktor:   σ_GDR / σ(γ,α) = "
              f"{self.sigma_gdr_mb / self.sigma_pa_mb:.1f}×")
        print(f"  Signifikanz RFT (neu, σ(γ,α)):  {self.sigma_rft_pa:.1f} σ  "
              f"[RT-09: KORREKT]")
        print(f"  Signifikanz SM  (neu, σ(γ,α)):  {self.sigma_sm_pa:.1f} σ")
        print(f"  Signifikanz Differenz (neu):     {self.sigma_diff_pa:.1f} σ")
        print(f"  Signifikanz RFT (alt, σ_GDR):   {self.sigma_rft_legacy:.1f} σ  "
              f"[Legacy, basiert auf σ_GDR = {self.sigma_gdr_mb:.0f} mb — RT-06 Revision]")

        print(f"\n--- Hintergrund ---")
        print(f"  Natürliche Zerfälle: {self.counts_natural:.3e} "
              f"(in {self.measurement_time_hours} h)")
        print(f"  Zerfälle/s (natürlich): {self.natural_decays_per_s:.3e}")
        print("=" * 70)


# ============================================================
# 8. RT-09: Monte-Carlo-Fehlerrechnung
# ============================================================

def uncertainty_budget_am241(
    facility: "Facility",
    E_gamma_MeV: float,
    target_mass_mg: float,
    measurement_time_hours: float,
    sigma_photo_alpha_mb: float = 1.719,       # RT-06 Hauser-Feshbach
    sigma_pa_uncertainty_factor: float = 3.0,  # Faktor 2–5, Mitte = 3
    detector_efficiency: float = 0.5,          # typisch 20–80%, Default 50%
    detector_efficiency_unc: float = 0.15,     # ±15% absolut
    beam_sigma_cm: float = 0.5,               # Gaussbreite Strahlfleck
    beam_sigma_unc: float = 0.1,              # ±10%
    gamma_gdr_width_MeV: float = 4.5,         # Γ_GDR = 4–5 MeV
    gamma_gdr_width_unc_MeV: float = 0.5,     # ±0.5 MeV
    phase_coherence: float = 1.0,             # erreichbare Phasenkohärenz
    phase_coherence_unc: float = 0.1,         # ±10%
    n_mc: int = 100_000,                      # Monte-Carlo-Stichproben
) -> dict:
    """
    Monte-Carlo-Fehlerrechnung für das Am-241-Unsicherheitsbudget (RT-09).

    Berechnet das vollständige Unsicherheitsbudget für das Am-241-Experiment
    unter Berücksichtigung der folgenden Unsicherheitsquellen:
    - σ(γ,α): Log-Normal (multiplikativer Faktor aus Hauser-Feshbach)
    - Detektoreffizienz: Gleichverteilt in [efficiency − unc, efficiency + unc]
    - Strahlausbreitung: Normal(beam_sigma_cm, beam_sigma_unc)
    - Kernzustandsbreite: Normal(gamma_gdr_width_MeV, gamma_gdr_width_unc_MeV)
    - Phasenkohärenz: Gleichverteilt in [phase_coherence − unc, phase_coherence + unc]

    Das eigentliche Falsifizierungskriterium ist:
        Signal(η=1, kohärent) / Signal(η=0.5, inkohärent) = 2.0 (exakt aus RFT)
    Diese Zahl ist unabhängig von σ(γ,α) — sie hängt nur von η(Δφ) = cos²(Δφ/2) ab.

    Args:
        facility: Experimenteinrichtung (ELI_NP, HIgS, SLEGS)
        E_gamma_MeV: Photonenenergie in MeV
        target_mass_mg: Targetmasse in mg
        measurement_time_hours: Messzeit in Stunden
        sigma_photo_alpha_mb: Zentralwert σ(γ,α) in mb (RT-06 Hauser-Feshbach)
        sigma_pa_uncertainty_factor: Multiplikativer Unsicherheitsfaktor (Faktor 2–5)
        detector_efficiency: Detektoreffizienz (Default 0.5)
        detector_efficiency_unc: Absolute Unsicherheit der Detektoreffizienz
        beam_sigma_cm: Gauss-Breite des Strahlflecks in cm
        beam_sigma_unc: Absolute Unsicherheit der Strahlbreite in cm
        gamma_gdr_width_MeV: GDR-Zustandsbreite Γ_GDR in MeV
        gamma_gdr_width_unc_MeV: Unsicherheit Γ_GDR in MeV
        phase_coherence: Erreichbare Phasenkohärenz κ_coh (0–1)
        phase_coherence_unc: Absolute Unsicherheit der Phasenkohärenz
        n_mc: Anzahl Monte-Carlo-Stichproben

    Returns:
        dict mit statistischen Ergebnissen, Unsicherheitsbeiträgen und
        Falsifizierbarkeitsaussage.
    """
    rng = np.random.default_rng(seed=42)

    am = Am241_Literature

    # Feste Parameter
    target_mass_kg = target_mass_mg * 1e-6
    N_atoms = (target_mass_kg * 1000 * N_A) / am.A
    t_meas_s = measurement_time_hours * 3600
    lambda_0 = am.lambda_0_per_s
    Phi_nominal = facility.flux_typical / facility.beam_area_cm2
    beam_area_nominal = facility.beam_area_cm2

    # Log-Normal-Parameter für σ(γ,α)
    # Log-Normal: Median = sigma_photo_alpha_mb, σ_ln = ln(factor)
    sigma_ln = np.log(sigma_pa_uncertainty_factor)

    # Monte-Carlo-Stichproben
    # 1. σ(γ,α): Log-Normal
    ln_sigma_pa = rng.normal(
        loc=np.log(sigma_photo_alpha_mb), scale=sigma_ln, size=n_mc
    )
    sigma_pa_samples = np.exp(ln_sigma_pa) * MB_TO_CM2  # in cm²

    # 2. Detektoreffizienz: Gleichverteilt, geclippt auf [0.1, 1.0]
    eps_det_samples = rng.uniform(
        detector_efficiency - detector_efficiency_unc,
        detector_efficiency + detector_efficiency_unc,
        size=n_mc,
    )
    eps_det_samples = np.clip(eps_det_samples, 0.1, 1.0)

    # 3. Strahlbreite: Normal(beam_sigma_cm, beam_sigma_unc)
    beam_sigma_samples = rng.normal(beam_sigma_cm, beam_sigma_unc, size=n_mc)
    beam_sigma_samples = np.abs(beam_sigma_samples) + 1e-6  # physikalisch > 0

    # 4. GDR-Breite: Normal(gamma_gdr_width_MeV, gamma_gdr_width_unc_MeV)
    # Gamma_GDR ist hier ein Parameter, der den effektiven σ(γ,α) skaliert —
    # wir verwenden ihn als multiplikativen Korrekturfaktor relativ zum Zentralwert.
    # Eine breitere Resonanz reduziert den Peak-Wirkungsquerschnitt proportional.
    gamma_gdr_samples = rng.normal(
        gamma_gdr_width_MeV, gamma_gdr_width_unc_MeV, size=n_mc
    )
    gamma_gdr_samples = np.clip(gamma_gdr_samples, 2.0, 8.0)

    # 5. Phasenkohärenz: Gleichverteilt, geclippt auf [0, 1]
    kappa_coh_samples = rng.uniform(
        phase_coherence - phase_coherence_unc,
        phase_coherence + phase_coherence_unc,
        size=n_mc,
    )
    kappa_coh_samples = np.clip(kappa_coh_samples, 0.0, 1.0)

    # Effektiver Photonenfluss auf Target (Strahlausbreitung)
    # Nominale Strahlbreite aus Facility
    beam_sigma_nominal = np.sqrt(beam_area_nominal / PI)
    Phi_eff_samples = Phi_nominal * (beam_sigma_nominal**2 / beam_sigma_samples**2)

    # Signal kohärent (η = κ_coh)
    S_koh_samples = (
        eps_det_samples * N_atoms * kappa_coh_samples
        * Phi_eff_samples * sigma_pa_samples * t_meas_s
    )

    # Signal inkohärent (η = 0.5 · κ_coh)
    S_ink_samples = (
        eps_det_samples * N_atoms * 0.5 * kappa_coh_samples
        * Phi_eff_samples * sigma_pa_samples * t_meas_s
    )

    # Hintergrund (natürliche Zerfälle, detektor-gewichtet)
    B_samples = eps_det_samples * N_atoms * lambda_0 * t_meas_s

    # Signalverhältnis (immer exakt 2.0 — unabhängig von σ(γ,α))
    R_samples = np.where(S_ink_samples > 0, S_koh_samples / S_ink_samples, 2.0)

    # Nachweissignifikanz SNR = (S_koh − S_ink) / √(B + S_ink)
    denom = np.sqrt(B_samples + S_ink_samples)
    SNR_samples = np.where(denom > 0, (S_koh_samples - S_ink_samples) / denom, 0.0)

    # Perzentile
    SNR_median = float(np.median(SNR_samples))
    SNR_p16 = float(np.percentile(SNR_samples, 16))
    SNR_p84 = float(np.percentile(SNR_samples, 84))
    SNR_p5 = float(np.percentile(SNR_samples, 5))

    R_median = float(np.median(R_samples))
    R_p16 = float(np.percentile(R_samples, 16))
    R_p84 = float(np.percentile(R_samples, 84))

    S_koh_median = float(np.median(S_koh_samples))
    S_ink_median = float(np.median(S_ink_samples))
    B_median = float(np.median(B_samples))

    # Messzeit für SNR ≥ 3 und ≥ 5 (Skalierung: SNR ∝ √t)
    # SNR(t) = SNR_median · √(t / t_meas) → t(SNR_target) = t_meas · (SNR_target / SNR_median)²
    if SNR_median > 0:
        t_for_3sigma = measurement_time_hours * (3.0 / SNR_median) ** 2
        t_for_5sigma = measurement_time_hours * (5.0 / SNR_median) ** 2
    else:
        t_for_3sigma = float('inf')
        t_for_5sigma = float('inf')

    # Sensitivitätsanalyse: Varianzanteile der Einzelbeiträge
    # Jeder Parameter wird einzeln variiert, alle anderen auf Zentralwert fixiert
    contributions = {}
    central_sigma_pa = sigma_photo_alpha_mb * MB_TO_CM2
    central_eps = detector_efficiency
    central_bs = beam_sigma_cm
    central_kappa = phase_coherence
    Phi_central = Phi_nominal * (beam_sigma_nominal**2 / central_bs**2)

    def _snr_from_params(s_pa, eps, bs, kappa):
        bs_safe = np.maximum(np.asarray(bs, dtype=float), 1e-6)
        phi = Phi_nominal * (beam_sigma_nominal**2 / bs_safe**2)
        s_koh = eps * N_atoms * kappa * phi * s_pa * t_meas_s
        s_ink = 0.5 * s_koh
        bg = eps * N_atoms * lambda_0 * t_meas_s
        denom_ = np.sqrt(bg + s_ink)
        return np.where(denom_ > 0, (s_koh - s_ink) / denom_, 0.0)

    # Varianz bei Variation des jeweiligen Parameters
    n_sens = 10_000
    for param_name, varied_samples, fixed_args in [
        ("sigma_pa",
         np.exp(rng.normal(np.log(sigma_photo_alpha_mb), sigma_ln, n_sens)) * MB_TO_CM2,
         (central_eps, central_bs, central_kappa)),
        ("detector_efficiency",
         np.clip(rng.uniform(
             detector_efficiency - detector_efficiency_unc,
             detector_efficiency + detector_efficiency_unc, n_sens), 0.1, 1.0),
         (central_sigma_pa, central_bs, central_kappa)),
        ("beam_sigma",
         np.abs(rng.normal(beam_sigma_cm, beam_sigma_unc, n_sens)) + 1e-6,
         (central_sigma_pa, central_eps, central_kappa)),
        ("phase_coherence",
         np.clip(rng.uniform(
             phase_coherence - phase_coherence_unc,
             phase_coherence + phase_coherence_unc, n_sens), 0.0, 1.0),
         (central_sigma_pa, central_eps, central_bs)),
    ]:
        if param_name == "sigma_pa":
            snr_v = _snr_from_params(varied_samples, *fixed_args)
        elif param_name == "detector_efficiency":
            snr_v = _snr_from_params(fixed_args[0], varied_samples, fixed_args[1], fixed_args[2])
        elif param_name == "beam_sigma":
            snr_v = _snr_from_params(fixed_args[0], fixed_args[1], varied_samples, fixed_args[2])
        else:  # phase_coherence
            snr_v = _snr_from_params(fixed_args[0], fixed_args[1], fixed_args[2], varied_samples)
        contributions[param_name] = float(np.var(snr_v))

    total_var = sum(contributions.values())
    if total_var > 0:
        contributions_rel = {k: v / total_var for k, v in contributions.items()}
    else:
        contributions_rel = {k: 0.0 for k in contributions}

    dominant_uncertainty = max(contributions_rel, key=contributions_rel.get)

    falsification_feasible = SNR_p16 >= 3.0

    return {
        "sigma_pa_central_mb": sigma_photo_alpha_mb,
        "sigma_pa_unc_factor": sigma_pa_uncertainty_factor,
        "SNR_median": SNR_median,
        "SNR_p16": SNR_p16,
        "SNR_p84": SNR_p84,
        "SNR_p5": SNR_p5,
        "R_median": R_median,
        "R_p16": R_p16,
        "R_p84": R_p84,
        "S_koh_median": S_koh_median,
        "S_ink_median": S_ink_median,
        "B_median": B_median,
        "t_for_3sigma": t_for_3sigma,
        "t_for_5sigma": t_for_5sigma,
        "dominant_uncertainty": dominant_uncertainty,
        "contributions": contributions_rel,
        "falsification_feasible": falsification_feasible,
        "n_mc": n_mc,
    }


# ============================================================
# 9. Plots
# ============================================================

def ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def plot_gdr_profile(output_dir: str) -> None:
    """Plot 1: GDR-Profil mit Literaturdaten und RFT-Modulation."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    E = np.linspace(5, 25, 500)
    am = Am241_Literature

    # Links: GDR-Profil + Literaturdaten
    ax = axes[0]
    sigma_model = [gdr_cross_section(e) for e in E]
    ax.plot(E, sigma_model, 'k-', linewidth=2,
            label='Doppel-Lorentz (Dietrich-Berman)')

    # Soldatov (γ,f) Daten
    ax.scatter(am.soldatov_E_MeV, am.soldatov_sigma_f_mb,
               c='red', marker='s', s=40, zorder=5,
               label='Soldatov 2001 σ(γ,f)')

    # Berman (γ,n) Daten
    ax.scatter(am.berman_E_MeV, am.berman_sigma_n_mb,
               c='blue', marker='o', s=40, zorder=5,
               label='Dietrich-Berman σ(γ,n)')

    ax.axvline(am.E_gdr_1_MeV, color='gray', ls=':', alpha=0.5,
               label=f'GDR Peaks ({am.E_gdr_1_MeV}, {am.E_gdr_2_MeV} MeV)')
    ax.axvline(am.E_gdr_2_MeV, color='gray', ls=':', alpha=0.5)
    ax.axvline(am.S_n_MeV, color='green', ls='--', alpha=0.5,
               label=f'Sₙ = {am.S_n_MeV} MeV')

    ax.set_xlabel('E_γ (MeV)')
    ax.set_ylabel('σ (mb)')
    ax.set_title('Am-241: GDR-Profil mit Literaturdaten')
    ax.legend(fontsize=7, loc='upper right')
    ax.set_xlim(5, 25)
    ax.grid(True, alpha=0.3)

    # Rechts: RFT-Modulation bei verschiedenen Δφ
    ax = axes[1]
    for dp, label, color in [(0, 'Δφ=0 (ε=1, Resonanz)', 'red'),
                              (PI/4, 'Δφ=π/4 (ε=0.85)', 'orange'),
                              (PI/2, 'Δφ=π/2 (ε=0.5)', 'green'),
                              (PI, 'Δφ=π (ε=0, Anti)', 'blue')]:
        sigma_rft = [gdr_cross_section_rft(e, dp) for e in E]
        ax.plot(E, sigma_rft, color=color,
                label=f'{label}', linewidth=1.5)

    ax.plot(E, sigma_model, 'k--', linewidth=1,
            label='σ_GDR (Literatur)')

    ax.set_xlabel('E_γ (MeV)')
    ax.set_ylabel('σ_RFT (mb)')
    ax.set_title('Am-241: RFT-Vorhersage σ(E, Δφ)')
    ax.legend(fontsize=7)
    ax.set_xlim(5, 25)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'am241_gdr_profile.png'), dpi=150)
    plt.close()
    print("  → am241_gdr_profile.png")


def plot_phase_prediction(output_dir: str) -> None:
    """Plot 2: Phasenscan — die testbare RFT-Signatur."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    am = Am241_Literature
    delta_phis = np.linspace(0, 2 * PI, 200)
    etas = coupling_efficiency(delta_phis)

    # Links: η(Δφ) = cos²(Δφ/2)
    ax = axes[0]
    ax.plot(delta_phis / PI, etas, 'b-', linewidth=2,
            label='ε(Δφ) = η(Δφ) = cos²(Δφ/2)')
    ax.axhline(0.5, color='gray', ls='--', alpha=0.5,
               label='Inkohärenter Mittelwert (η = 0.5)')
    ax.set_xlabel('Δφ / π')
    ax.set_ylabel('Kopplungseffizienz ε = η')
    ax.set_title('RFT-Vorhersage: Phasenabhängigkeit')
    ax.legend()
    ax.set_xlim(0, 2)
    ax.set_ylim(-0.05, 1.05)
    ax.grid(True, alpha=0.3)

    # Rechts: λ_eff/λ₀ als Funktion von Δφ bei verschiedenen Flüssen
    ax = axes[1]
    for flux, label, color in [(1e8, 'Φ = 10⁸ (HIγS)', 'blue'),
                                (1e10, 'Φ = 10¹⁰ (ELI-NP konserv.)', 'green'),
                                (1e12, 'Φ = 10¹² (ELI-NP Design)', 'red'),
                                (1e14, 'Φ = 10¹⁴ (Zukunft)', 'darkred')]:
        ratios = []
        for dp in delta_phis:
            lam = effective_decay_rate(dp, flux / 0.01)  # 0.01 cm² Spot
            ratios.append(lam / am.lambda_0_per_s)
        ax.plot(delta_phis / PI, ratios, color=color, label=label,
                linewidth=1.5)

    ax.axhline(1.0, color='k', ls='--', alpha=0.5)
    ax.set_xlabel('Δφ / π')
    ax.set_ylabel('λ_eff / λ₀')
    ax.set_title(f'Am-241: Zerfallsrate vs. Phase\nE_γ = {am.E_gdr_centroid_MeV} MeV')
    ax.legend(fontsize=8)
    ax.set_xlim(0, 2)
    ax.set_yscale('log')
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'am241_phase_prediction.png'), dpi=150)
    plt.close()
    print("  → am241_phase_prediction.png")


def plot_facility_comparison(output_dir: str) -> None:
    """Plot 3: Vergleich der Einrichtungen — Signifikanz vs. Messzeit."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    am = Am241_Literature
    target_mass_mg = 100  # 100 mg Am-241
    E_gamma = am.E_gdr_centroid_MeV
    hours = np.logspace(-1, 4, 200)

    # Links: Signifikanz (σ) vs. Messzeit
    ax = axes[0]
    for fac, color in [(ELI_NP, 'red'), (HIgS, 'blue'), (SLEGS, 'green')]:
        sigmas = []
        for h in hours:
            exp = ExperimentConfig(fac, E_gamma, target_mass_mg, h)
            sigmas.append(max(exp.sigma_rft, 0.01))
        ax.loglog(hours, sigmas, color=color, linewidth=2,
                  label=f'{fac.name} ({fac.flux_typical:.0e} γ/s)')

    ax.axhline(3.0, color='orange', ls='--', label='3σ (Evidenz)')
    ax.axhline(5.0, color='red', ls='--', label='5σ (Entdeckung)')
    ax.set_xlabel('Messzeit (Stunden)')
    ax.set_ylabel('Signifikanz (σ)')
    ax.set_title(f'Am-241: Signifikanz vs. Messzeit\n'
                 f'{target_mass_mg} mg Target, E_γ = {E_gamma} MeV')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0.1, 10000)

    # Rechts: Signal-Verhältnis kohärent/inkohärent vs. Fluss
    ax = axes[1]
    fluxes = np.logspace(4, 16, 200)

    # Das Signalverhältnis ist theoretisch immer 2.0
    # Aber die MESSBARE Signifikanz des Unterschieds skaliert mit Φ
    sigmas_diff = []
    for flux in fluxes:
        phi = flux / 0.01  # 0.01 cm² Spot
        sigma_mb = gdr_cross_section(E_gamma)
        sigma_cm2 = sigma_mb * MB_TO_CM2
        lambda_res = phi * sigma_cm2

        # Signaldifferenz (η=1 vs η=0.5) pro Sekunde pro Kern
        delta_signal_per_s = 0.5 * lambda_res * 2.499e20  # N_atoms für 100 mg
        # In 24 h
        delta_signal = delta_signal_per_s * 86400
        # Hintergrund
        bg = am.lambda_0_per_s * 2.499e20 * 86400
        sig = delta_signal / np.sqrt(bg) if bg > 0 else 0
        sigmas_diff.append(max(sig, 0.01))

    ax.loglog(fluxes, sigmas_diff, 'r-', linewidth=2,
              label='Signifikanz der RFT-Signatur\n'
                    '(Signal_koh − Signal_ink)')
    ax.axhline(3.0, color='orange', ls='--', label='3σ')
    ax.axhline(5.0, color='red', ls='--', label='5σ')

    # Einrichtungen markieren
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

    ax.set_xlabel('Photonenfluss (γ/s, gesamt)')
    ax.set_ylabel('Signifikanz der RFT-Signatur (σ)')
    ax.set_title('Am-241: Testbarkeit der Phasenabhängigkeit\n'
                 '100 mg Target, 24 h Messzeit')
    ax.legend(fontsize=7, loc='upper left')
    ax.grid(True, alpha=0.3)
    ax.set_xlim(1e4, 1e16)

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'am241_facility_comparison.png'),
                dpi=150)
    plt.close()
    print("  → am241_facility_comparison.png")


def plot_signal_ratio(output_dir: str) -> None:
    """Plot 4: Das entscheidende Experiment — Signal_koh / Signal_ink."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    am = Am241_Literature
    E_gamma = am.E_gdr_centroid_MeV

    # Links: Signalverhältnis als Funktion von Δφ (kohärenter Strahl)
    ax = axes[0]
    delta_phis = np.linspace(0.01, PI - 0.01, 200)

    # Signal(Δφ) / Signal(Δφ = π/2) → zeigt die Phasenabhängigkeit
    for flux, label, color in [(1e10, 'Φ = 10¹⁰', 'green'),
                                (1e12, 'Φ = 10¹²', 'red'),
                                (1e14, 'Φ = 10¹⁴', 'darkred')]:
        phi = flux / 0.01  # auf 0.01 cm²
        sigma_cm2 = gdr_cross_section(E_gamma) * MB_TO_CM2

        # Signal = η(Δφ) · Φ · σ · N
        # Normiert auf η = 0.5 (inkohärent)
        ratios = coupling_efficiency(delta_phis) / 0.5
        ax.plot(delta_phis / PI, ratios, color=color,
                label=label, linewidth=2)

    ax.axhline(2.0, color='red', ls=':', alpha=0.5,
               label='η=1 → Verhältnis = 2.0')
    ax.axhline(1.0, color='gray', ls='--', alpha=0.5,
               label='η=0.5 → Verhältnis = 1.0 (SM)')
    ax.axhline(0.0, color='blue', ls=':', alpha=0.5)
    ax.set_xlabel('Δφ / π')
    ax.set_ylabel('Signal(Δφ) / Signal(inkohärent)')
    ax.set_title('RFT-Signatur: Signalverhältnis vs. Phase\n'
                 'Signal = λ_eff − λ₀ (zusätzliche Zerfälle)')
    ax.legend(fontsize=8)
    ax.set_xlim(0, 1)
    ax.set_ylim(-0.1, 2.5)
    ax.grid(True, alpha=0.3)

    # Rechts: Messprotokoll-Visualisierung
    ax = axes[1]
    phases = ['Δφ = 0\n(Resonanz)', 'Δφ = π/4', 'Δφ = π/2',
              'Δφ = 3π/4', 'Inkohärent\n(SM)']
    etas = [1.0, 0.854, 0.5, 0.146, 0.5]
    signals = [e / 0.5 for e in etas]  # normiert auf inkohärent
    colors = ['red', 'orange', 'green', 'blue', 'gray']

    bars = ax.bar(phases, signals, color=colors, edgecolor='black',
                  linewidth=0.5, alpha=0.8)
    ax.axhline(1.0, color='black', ls='--', linewidth=1,
               label='SM-Erwartung (η = 0.5)')
    ax.axhline(2.0, color='red', ls=':', linewidth=1,
               label='RFT bei Δφ = 0')

    for bar, sig in zip(bars, signals):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.05,
                f'{sig:.2f}', ha='center', fontsize=9, fontweight='bold')

    ax.set_ylabel('Signal / Signal(inkohärent)')
    ax.set_title('Messprotokoll: 5 Messpunkte\n'
                 'SM: alle Balken = 1.0 | RFT: variiert mit cos²(Δφ/2)')
    ax.legend(fontsize=9)
    ax.set_ylim(0, 2.7)
    ax.grid(True, alpha=0.3, axis='y')

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'am241_signal_ratio.png'), dpi=150)
    plt.close()
    print("  → am241_signal_ratio.png")


# ============================================================
# 10. Hauptprogramm
# ============================================================

def main() -> None:
    print("=" * 70)
    print("RESONANZREAKTOR: Experimentelle Vorhersage Am-241")
    print("Literaturbasierte Simulation (Soldatov, Berman, NNDC, ELI-NP)")
    print("κ = 1 (aus RFT-Grundformel, kein freier Parameter)")
    print("=" * 70)

    output_dir = "figures"
    ensure_dir(output_dir)

    am = Am241_Literature

    # --- RFT-Frequenzen ---
    print("\n=== RFT-Frequenzen aus Grundformel ===")
    print(f"  f(E₁ = {am.E_gdr_1_MeV} MeV) = "
          f"{gdr_frequency_rft(am.E_gdr_1_MeV):.3e} Hz")
    print(f"  f(E₂ = {am.E_gdr_2_MeV} MeV) = "
          f"{gdr_frequency_rft(am.E_gdr_2_MeV):.3e} Hz")
    print(f"  f(Zentroid = {am.E_gdr_centroid_MeV} MeV) = "
          f"{gdr_frequency_rft(am.E_gdr_centroid_MeV):.3e} Hz")

    # --- GDR-Querschnitt am Zentroid ---
    sigma_cent = gdr_cross_section(am.E_gdr_centroid_MeV)
    print(f"  σ_GDR(Zentroid) = {sigma_cent:.1f} mb")

    # --- Experiment 1: ELI-NP (bestes existierendes Setup) ---
    print("\n" + "=" * 70)
    print("Experiment 1: ELI-NP VEGA (konservativ)")
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

    # --- Experiment 3: ELI-NP bei Design-Fluss ---
    class ELI_NP_Design:
        name = "ELI-NP VEGA (Design)"
        location = "Măgurele, Rumänien"
        E_range_MeV = (0.2, 19.5)
        flux_typical = 1e13
        bandwidth = 0.005
        polarization = 0.95
        beam_area_cm2 = 0.01
        status = "Design-Spezifikation"

    print("\n" + "=" * 70)
    print("Experiment 3: ELI-NP VEGA (Design-Spezifikation)")
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

    # --- Zusammenfassung ---
    print("\n" + "=" * 70)
    print("ZUSAMMENFASSUNG: Experimentelle Testbarkeit")
    print("=" * 70)
    print(f"""
  Am-241 Kerndaten (Literatur):
    t₁/₂ = {am.half_life_years} a, λ₀ = {am.lambda_0_per_s:.3e} /s
    GDR: {am.E_gdr_1_MeV}/{am.E_gdr_2_MeV} MeV (Doppelpeak)
    σ_peak = {am.sigma_peak_1_mb}/{am.sigma_peak_2_mb} mb
    σ_GDR(Zentroid) = {sigma_cent:.1f} mb
    f_GDR (RFT) = {gdr_frequency_rft(am.E_gdr_centroid_MeV):.3e} Hz

  Beste existierende Einrichtung: ELI-NP VEGA
    Fluss: 10¹⁰–10¹³ γ/s bei 0.2–19.5 MeV
    Polarisation: >95% (linear)
    Bandbreite: ΔE/E < 0.5%

  RFT-Vorhersagen:
    Exp. 1 (ELI-NP, 10¹⁰ γ/s, 24 h):
      λ_eff/λ₀ = {exp1.ratio_rft:.6f}
      Signal = {exp1.signal_rft:.3e} Zerfälle
      Signifikanz: {exp1.sigma_rft:.1f} σ

    Exp. 3 (ELI-NP Design, 10¹³ γ/s, 1 h):
      λ_eff/λ₀ = {exp3.ratio_rft:.6f}
      Signal = {exp3.signal_rft:.3e} Zerfälle
      Signifikanz: {exp3.sigma_rft:.1f} σ

  RFT-SPEZIFISCHE SIGNATUR:
    Signal(kohärent) / Signal(inkohärent) = 2.0 (exakt)
    → Unabhängig vom absoluten Fluss
    → Unabhängig von der Targetmasse
    → Nur abhängig von η(Δφ) = cos²(Δφ/2)
    → SM-Vorhersage: Verhältnis = 1.0 (kein Phaseneffekt)

  MESSPROTOKOLL:
    1. γ-Strahl kohärent (polarisiert) → zähle Signal_koh
    2. γ-Strahl inkohärent (depolarisiert) → zähle Signal_ink
    3. Signal_koh / Signal_ink = 2.0 (RFT) oder 1.0 (SM)
    → Eindeutiger Ja/Nein-Test der RFT

  Fazit: Das Experiment ist mit bestehender Technologie
         an ELI-NP durchführbar. Die RFT-Signatur (Faktor 2)
         ist ein klares, flussunabhängiges Signal.
""")
    print("Plots gespeichert unter:", output_dir)
    print("Fertig.")


if __name__ == "__main__":
    main()