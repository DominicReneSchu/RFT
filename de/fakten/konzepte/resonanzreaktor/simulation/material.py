# material.py
# © Dominic-René Schu, 2025/2026 – Resonanzfeldtheorie
from __future__ import annotations
# Resonanzreaktor: Physikalisch fundierte Isotopendaten
#
# RFT-Hypothese (nicht Standardphysik): Resonante GDR-Feldkopplung bei ε(Δφ)
# moduliert die Coulomb-Barriere des α-Zerfalls. Der (γ,α)-Wirkungsquerschnitt
# sigma_photo_alpha dient als Proxy. Standardphysik sieht keinen direkten
# Mechanismus zur α-Zerfallsbeschleunigung durch GDR-Anregung. Diese Hypothese
# ist experimentell testbar: σ_coh > σ_incoh (falsifizierbare Vorhersage).
#
# GDR-Daten aus:
# - Ishkhanov & Kapitonov (2021): Giant dipole resonance of atomic nuclei
# - RIPL-3: IAEA-TECDOC-1768 — Reference Input Parameter Library für (γ,α)-Wirkungsquerschnitte
# - Berman & Fultz (1975): Measurements of giant dipole resonance,
#   Rev. Mod. Phys. 47, 713 — primäre GDR-Datenquelle
# - Dietrich & Berman (1988): Atlas of photoneutron cross sections
# - RT-06 (EXFOR/Hauser-Feshbach): σ(γ,α) Am-241 aus exfor_data.py
#
# K-6 Status: BEHOBEN (RT-06) — sigma_photo_alpha für Am-241 aus
# Hauser-Feshbach-Abschätzung (kein EXFOR-Eintrag für schwere Aktiniden).
# Am GDR-Zentroid (14.0 MeV): σ(γ,α) = 1.719 mb (Methode: hauser_feshbach,
# Unsicherheit ±factor 2–5). Bisheriger Schätzwert (aus GDR-Peak) bleibt
# als sigma_photo_alpha_estimated erhalten (Rückwärtskompatibilität).

import numpy as np

# Naturkonstanten
HBAR = 1.054571817e-34      # J·s
HBAR_MEV = 6.582119569e-22  # MeV·s
PI = np.pi
MEV_TO_J = 1.602176634e-13  # J/MeV
K_B = 1.380649e-23          # J/K
N_A = 6.02214076e23         # Avogadro
SECONDS_PER_YEAR = 365.25 * 24 * 3600


def gdr_frequency(E_gdr_MeV: float) -> float:
    """
    Berechnet die Resonanzfrequenz aus der GDR-Energie
    über die RFT-Grundformel: E = π · ε · ℏ · f
    mit f = E_GDR/(π·ℏ) (RFT-Resonanzfrequenz, rad/s; vgl. K-3)

    Für maximale Kopplung (ε = 1):
        f = E / (π · ℏ)

    Hinweis zu A3-Kompatibilität (K-9): Axiom A3 erfordert keine exakt rationalen
    Frequenzverhältnisse, sondern nur Verhältnisse innerhalb des Toleranzfensters δ:
    |f₁/f₂ − m/n| < δ. Die GDR-Frequenz f_GDR = E_GDR/(π·ℏ) ist irrational, liegt
    aber innerhalb δ eines rationalen Verhältnisses. Das Toleranzfenster δ ist ein
    Modellparameter der RFT (nicht freier Parameter, da physikalisch durch die
    Resonanzbreite Γ_GDR ≈ 4–5 MeV bestimmt).

    Frequenzdefinition (K-3):
        f_GDR = E_GDR / (π·ℏ)
        Diese RFT-Resonanzfrequenz entspricht f = ω/π (kein Standard-Hz).
        Standardphysik: f_Hz = E/h  oder  ω = E/ℏ (rad/s).
        Der klassische Planck-Grenzwert E = hf (Hz) entspricht ε = 1/(2π) ≈ 0.159
        in der RFT-Formel — d.h. ε ∈ [0, 1] erreicht E = hf nie bei ε = 1.
        Diese Diskrepanz ist eine offene Frage (→ RESEARCH_TASKS.md RT-01).

    Args:
        E_gdr_MeV: GDR-Energie in MeV

    Returns:
        float: Frequenz in rad/s — die RFT-Resonanzfrequenz f = E/(π·ℏ) = ω/π.
            Kein Standard-Hz (f_Hz = E/h) und keine Standard-Kreisfrequenz
            (ω_std = E/ℏ); siehe K-3 und RESEARCH_TASKS.md RT-01.
    """
    E_J = E_gdr_MeV * MEV_TO_J
    return E_J / (PI * HBAR)


class Isotope:
    """
    Isotop mit physikalisch fundierten Kernresonanzdaten.

    GDR-Parameter (Giant Dipole Resonance):
    - Aktiniden zeigen Doppelpeak-Struktur (prolate Deformation)
    - Leichtere Kerne (Cs, Sr) zeigen Einzelpeak-Struktur
    - Peak-Energien und Breiten aus Literatur
    - Resonanzfrequenzen aus RFT-Grundformel hergeleitet
    """

    def __init__(self, name: str, A: int, Z: int, half_life_years: float,
                 E_gdr_peaks_MeV: list[float], Gamma_gdr_MeV: list[float],
                 decay_constant: float, energy_per_decay_MeV: float,
                 sigma_gdr_peak_mb: float | None = None,
                 transmutations: list[Isotope] | None = None,
                 decay_type: str = "alpha",
                 fissile: bool = False,
                 fission_energy_MeV: float = 200.0) -> None:
        """
        Args:
            name: Isotopenname
            A: Massenzahl
            Z: Ordnungszahl
            half_life_years: Halbwertszeit in Jahren
            E_gdr_peaks_MeV: Liste der GDR-Peak-Energien in MeV
            Gamma_gdr_MeV: Liste der GDR-Breiten in MeV
            decay_constant: Zerfallskonstante λ in 1/Jahr
            energy_per_decay_MeV: Energie pro Zerfall in MeV
            sigma_gdr_peak_mb: Peak-Wirkungsquerschnitt in mb
            transmutations: Liste möglicher Transmutationsprodukte
            decay_type: Zerfallstyp ("alpha", "beta", "sf")
            fissile: Ob durch GDR-Anregung spaltbar
            fission_energy_MeV: Spaltungsenergie in MeV
        """
        self.name = name
        self.A = A
        self.Z = Z
        self.half_life = half_life_years
        self.E_gdr_peaks = np.array(E_gdr_peaks_MeV)
        self.Gamma_gdr = np.array(Gamma_gdr_MeV)
        self.decay_constant = decay_constant
        self.energy_per_decay = energy_per_decay_MeV
        self.sigma_gdr_peak = sigma_gdr_peak_mb or 350.0
        self.transmutations = transmutations or []
        self.decay_type = decay_type
        self.fissile = fissile
        self.fission_energy = fission_energy_MeV

        # RFT-Resonanzfrequenzen aus Grundformel
        self.f_gdr = np.array([gdr_frequency(E) for E in self.E_gdr_peaks])

        # Zentroid-Energie und -Frequenz
        self.E_gdr_centroid = np.mean(self.E_gdr_peaks)
        self.f_gdr_centroid = gdr_frequency(self.E_gdr_centroid)

        # Zerfallskonstante in 1/s
        self.lambda_0_per_s = decay_constant / SECONDS_PER_YEAR

    def decay(self, time_years: float) -> float | np.ndarray:
        """Exponentieller Zerfall: N(t)/N₀ = exp(-λt)"""
        return np.exp(-self.decay_constant * time_years)

    def energy_released(self, time_years: float) -> float | np.ndarray:
        """Freigesetzte Energie über Zeitspanne in MeV"""
        return self.decay(time_years) * self.energy_per_decay

    def gdr_cross_section(self, E_gamma_MeV: float) -> float:
        """
        (γ,α)-Wirkungsquerschnitt (sigma_photo_alpha) als
        Summe von Lorentz-Profilen über GDR-Peaks.

        RFT-Hypothese: resonante GDR-Anregung moduliert α-Zerfallsbarriere
        via (γ,α)-Kanal. Dieser Querschnitt dient als Proxy für den
        RFT-vorhergesagten Barrierenmodulationseffekt.

        σ(E) = Σᵢ wᵢ · σ_peak · (E·Γᵢ)² / [(E²-Eᵢ²)² + (E·Γᵢ)²]
        """
        sigma = 0.0
        n_peaks = len(self.E_gdr_peaks)
        if n_peaks == 2:
            weights = [1.0 / 3.0, 2.0 / 3.0]
        else:
            weights = [1.0] * n_peaks

        for i, (E_i, G_i) in enumerate(zip(self.E_gdr_peaks, self.Gamma_gdr)):
            w = weights[i] if i < len(weights) else 1.0
            numerator = (E_gamma_MeV * G_i) ** 2
            denominator = (E_gamma_MeV**2 - E_i**2)**2 + (E_gamma_MeV * G_i)**2
            sigma += w * self.sigma_gdr_peak * numerator / denominator

        return sigma

    def sigma_photo_alpha_at_centroid_barn(self) -> float:
        """sigma_photo_alpha am Zentroid in barn (für λ_eff-Berechnungen).

        RFT-Hypothese: resonante GDR-Feldkopplung via (γ,α)-Kanal moduliert
        die α-Zerfalls-Coulomb-Barriere. sigma_photo_alpha dient als Proxy.
        """
        sigma_mb = self.gdr_cross_section(self.E_gdr_centroid)
        return sigma_mb * 1e-3  # mb → barn (1 barn = 10⁻²⁴ cm²)

    def transmute(self) -> Isotope:
        """Gibt das nächste Transmutationsprodukt zurück."""
        if self.transmutations:
            return self.transmutations[0]
        return self

    def info(self) -> None:
        """Gibt Zusammenfassung der Isotopendaten aus."""
        print(f"=== {self.name} (A={self.A}, Z={self.Z}) ===")
        print(f"  Halbwertszeit: {self.half_life:.4g} Jahre")
        print(f"  Zerfallskonstante: {self.decay_constant:.6e} /Jahr")
        print(f"  λ₀: {self.lambda_0_per_s:.6e} /s")
        print(f"  Zerfall: {self.decay_type}"
              f"{'  (spaltbar)' if self.fissile else ''}")
        print(f"  Energie/Zerfall: {self.energy_per_decay} MeV"
              f"{'  (Spaltung: ' + str(self.fission_energy) + ' MeV)' if self.fissile else ''}")
        print(f"  GDR-Peaks: {self.E_gdr_peaks} MeV")
        print(f"  GDR-Breiten: {self.Gamma_gdr} MeV")
        print(f"  GDR-Zentroid: {self.E_gdr_centroid:.1f} MeV")
        for i, (E, f) in enumerate(zip(self.E_gdr_peaks, self.f_gdr)):
            print(f"  RFT-Frequenz (Peak {i+1}): {f:.3e} Hz "
                  f"(aus E={E} MeV, f=E/(π·ℏ))")
        print(f"  σ_photo_alpha (Peak): {self.sigma_gdr_peak} mb")


# ============================================================
# Isotopendaten: GDR aus Literatur, Frequenzen aus RFT
# ============================================================

# --- Aktinide (Doppelpeak-GDR, spaltbar) ---

americium_241 = Isotope(
    name="Americium-241",
    A=241, Z=95,
    half_life_years=432.2,
    E_gdr_peaks_MeV=[11.8, 14.8],
    Gamma_gdr_MeV=[4.0, 5.5],
    decay_constant=np.log(2) / 432.2,
    energy_per_decay_MeV=5.638,
    sigma_gdr_peak_mb=350,
    decay_type="alpha",
    fissile=True,
    fission_energy_MeV=200.0,
)

# RT-06: σ(γ,α) Am-241 aus EXFOR/Hauser-Feshbach
# Kein direkter EXFOR-Eintrag verfügbar — Hauser-Feshbach verwendet.
# Am GDR-Zentroid (14.0 MeV): σ(γ,α) = 1.719 mb (exfor_data.py)
# Bisheriger GDR-Peak-Schätzwert (Rückwärtskompatibilität):
americium_241.sigma_photo_alpha_estimated = (
    americium_241.sigma_photo_alpha_at_centroid_barn()
)  # barn — aus GDR-Peak-Abschätzung (vor RT-06)

# Echter Wert aus RT-06 (Hauser-Feshbach, RIPL-3):
americium_241.sigma_photo_alpha = 1.719e-3   # barn (1.719 mb → barn)
americium_241.sigma_photo_alpha_method = "hauser_feshbach"
americium_241.sigma_photo_alpha_unc_pct = 300.0  # ±factor 2–5

plutonium_240 = Isotope(
    name="Plutonium-240",
    A=240, Z=94,
    half_life_years=6561,
    E_gdr_peaks_MeV=[11.9, 14.9],
    Gamma_gdr_MeV=[4.1, 5.6],
    decay_constant=np.log(2) / 6561,
    energy_per_decay_MeV=5.256,
    sigma_gdr_peak_mb=355,
    decay_type="alpha",
    fissile=True,
    fission_energy_MeV=200.0,
    transmutations=[americium_241],
)

plutonium_239 = Isotope(
    name="Plutonium-239",
    A=239, Z=94,
    half_life_years=24110,
    E_gdr_peaks_MeV=[12.0, 15.0],
    Gamma_gdr_MeV=[4.2, 5.8],
    decay_constant=np.log(2) / 24110,
    energy_per_decay_MeV=5.245,
    sigma_gdr_peak_mb=360,
    decay_type="alpha",
    fissile=True,
    fission_energy_MeV=200.0,
    transmutations=[plutonium_240],
)

neptunium_237 = Isotope(
    name="Neptunium-237",
    A=237, Z=93,
    half_life_years=2.14e6,
    E_gdr_peaks_MeV=[11.6, 14.6],
    Gamma_gdr_MeV=[3.9, 5.4],
    decay_constant=np.log(2) / 2.14e6,
    energy_per_decay_MeV=4.959,
    sigma_gdr_peak_mb=345,
    decay_type="alpha",
    fissile=True,
    fission_energy_MeV=200.0,
)

uranium_238 = Isotope(
    name="Uranium-238",
    A=238, Z=92,
    half_life_years=4.468e9,
    E_gdr_peaks_MeV=[11.4, 14.4],
    Gamma_gdr_MeV=[3.9, 5.4],
    decay_constant=np.log(2) / 4.468e9,
    energy_per_decay_MeV=4.270,
    sigma_gdr_peak_mb=345,
    decay_type="alpha",
    fissile=True,
    fission_energy_MeV=200.0,
)

uranium_235 = Isotope(
    name="Uranium-235",
    A=235, Z=92,
    half_life_years=7.038e8,
    E_gdr_peaks_MeV=[11.5, 14.5],
    Gamma_gdr_MeV=[4.0, 5.5],
    decay_constant=np.log(2) / 7.038e8,
    energy_per_decay_MeV=4.679,
    sigma_gdr_peak_mb=340,
    decay_type="alpha",
    fissile=True,
    fission_energy_MeV=200.0,
    transmutations=[plutonium_239],
)

thorium_232 = Isotope(
    name="Thorium-232",
    A=232, Z=90,
    half_life_years=1.405e10,
    E_gdr_peaks_MeV=[11.0, 14.0],
    Gamma_gdr_MeV=[3.8, 5.2],
    decay_constant=np.log(2) / 1.405e10,
    energy_per_decay_MeV=4.083,
    sigma_gdr_peak_mb=330,
    decay_type="alpha",
    fissile=True,
    fission_energy_MeV=200.0,
)

# --- Spaltprodukte (Einzelpeak-GDR, β-Strahler, nicht spaltbar) ---

cesium_137 = Isotope(
    name="Cesium-137",
    A=137, Z=55,
    half_life_years=30.17,
    E_gdr_peaks_MeV=[15.3],
    Gamma_gdr_MeV=[5.0],
    decay_constant=np.log(2) / 30.17,
    energy_per_decay_MeV=1.176,
    sigma_gdr_peak_mb=230,
    decay_type="beta",
    fissile=False,
)

strontium_90 = Isotope(
    name="Strontium-90",
    A=90, Z=38,
    half_life_years=28.8,
    E_gdr_peaks_MeV=[16.5],
    Gamma_gdr_MeV=[4.5],
    decay_constant=np.log(2) / 28.8,
    energy_per_decay_MeV=0.546,
    sigma_gdr_peak_mb=180,
    decay_type="beta",
    fissile=False,
)

# ============================================================
# Sammlung aller Isotope
# ============================================================

ALL_ACTINIDES = [uranium_235, uranium_238, neptunium_237,
                 plutonium_239, plutonium_240, americium_241]
ALL_FISSION_PRODUCTS = [cesium_137, strontium_90]
ALL_ISOTOPES = ALL_ACTINIDES + ALL_FISSION_PRODUCTS + [thorium_232]


# ============================================================
# Validierung
# ============================================================
if __name__ == "__main__":
    for isotope in ALL_ISOTOPES:
        isotope.info()
        print()