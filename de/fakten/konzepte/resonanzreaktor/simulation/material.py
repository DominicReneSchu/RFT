# material.py
# © Dominic-René Schu, 2025/2026 – Resonanzfeldtheorie
# Resonanzreaktor: Physikalisch fundierte Isotopendaten
#
# GDR-Daten aus:
# - Ishkhanov & Kapitonov (2021): Giant dipole resonance of atomic nuclei
# - RIPL-3: Reference Input Parameter Library
# - Berman & Fultz (1975): Measurements of giant dipole resonance

import numpy as np

# Naturkonstanten
HBAR = 1.054571817e-34      # J·s
HBAR_MEV = 6.582119569e-22  # MeV·s
PI = np.pi
MEV_TO_J = 1.602176634e-13  # J/MeV
K_B = 1.380649e-23          # J/K


def gdr_frequency(E_gdr_MeV):
    """
    Berechnet die Resonanzfrequenz aus der GDR-Energie
    über die RFT-Grundformel: E = π · ε · ℏ · f
    
    Für maximale Kopplung (ε = 1):
        f = E / (π · ℏ)
    
    Args:
        E_gdr_MeV: GDR-Energie in MeV
    
    Returns:
        Frequenz in Hz
    """
    E_J = E_gdr_MeV * MEV_TO_J
    return E_J / (PI * HBAR)


class Isotope:
    """
    Isotop mit physikalisch fundierten Kernresonanzdaten.
    
    GDR-Parameter (Giant Dipole Resonance):
    - Aktiniden zeigen Doppelpeak-Struktur (prolate Deformation)
    - Peak-Energien E1, E2 und Breiten Γ1, Γ2 aus Literatur
    - Resonanzfrequenzen aus RFT-Grundformel hergeleitet
    """
    
    def __init__(self, name, A, Z, half_life_years,
                 E_gdr_peaks_MeV, Gamma_gdr_MeV,
                 decay_constant, energy_per_decay_MeV,
                 sigma_gdr_peak_mb=None,
                 transmutations=None):
        """
        Args:
            name: Isotopenname
            A: Massenzahl
            Z: Ordnungszahl
            half_life_years: Halbwertszeit in Jahren
            E_gdr_peaks_MeV: Liste der GDR-Peak-Energien [E1, E2] in MeV
            Gamma_gdr_MeV: Liste der GDR-Breiten [Γ1, Γ2] in MeV
            decay_constant: Zerfallskonstante λ in 1/Jahr
            energy_per_decay_MeV: Energie pro Zerfall in MeV
            sigma_gdr_peak_mb: Peak-Wirkungsquerschnitt in mb
            transmutations: Liste möglicher Transmutationsprodukte
        """
        self.name = name
        self.A = A
        self.Z = Z
        self.half_life = half_life_years
        self.E_gdr_peaks = np.array(E_gdr_peaks_MeV)
        self.Gamma_gdr = np.array(Gamma_gdr_MeV)
        self.decay_constant = decay_constant
        self.energy_per_decay = energy_per_decay_MeV
        self.sigma_gdr_peak = sigma_gdr_peak_mb or 350.0  # mb, typisch für Aktiniden
        self.transmutations = transmutations or []
        
        # RFT-Resonanzfrequenzen aus Grundformel
        self.f_gdr = np.array([gdr_frequency(E) for E in self.E_gdr_peaks])
        
        # Zentroid-Energie und -Frequenz
        self.E_gdr_centroid = np.mean(self.E_gdr_peaks)
        self.f_gdr_centroid = gdr_frequency(self.E_gdr_centroid)
    
    def decay(self, time_years):
        """Exponentieller Zerfall: N(t)/N₀ = exp(-λt)"""
        return np.exp(-self.decay_constant * time_years)
    
    def energy_released(self, time_years):
        """Freigesetzte Energie über Zeitspanne in MeV"""
        return self.decay(time_years) * self.energy_per_decay
    
    def gdr_cross_section(self, E_gamma_MeV):
        """
        GDR-Photoabsorptions-Wirkungsquerschnitt als
        Summe zweier Lorentz-Profile (Doppelpeak-Struktur).
        
        σ(E) = Σᵢ σᵢ · (E·Γᵢ)² / [(E²-Eᵢ²)² + (E·Γᵢ)²]
        
        Args:
            E_gamma_MeV: Photonenenergie in MeV
        
        Returns:
            Wirkungsquerschnitt in mb
        """
        sigma = 0.0
        # Gewichtung: 1/3 auf niedrigen Peak, 2/3 auf hohen
        # (prolate Deformation: eine kurze, zwei lange Achsen)
        weights = [1.0 / 3.0, 2.0 / 3.0] if len(self.E_gdr_peaks) == 2 else [1.0]
        
        for i, (E_i, G_i) in enumerate(zip(self.E_gdr_peaks, self.Gamma_gdr)):
            w = weights[i] if i < len(weights) else 1.0
            numerator = (E_gamma_MeV * G_i) ** 2
            denominator = (E_gamma_MeV**2 - E_i**2)**2 + (E_gamma_MeV * G_i)**2
            sigma += w * self.sigma_gdr_peak * numerator / denominator
        
        return sigma
    
    def transmute(self):
        """Gibt das nächste Transmutationsprodukt zurück."""
        if self.transmutations:
            return self.transmutations[0]
        return self
    
    def info(self):
        """Gibt Zusammenfassung der Isotopendaten aus."""
        print(f"=== {self.name} (A={self.A}, Z={self.Z}) ===")
        print(f"  Halbwertszeit: {self.half_life:.0f} Jahre")
        print(f"  Zerfallskonstante: {self.decay_constant:.6e} /Jahr")
        print(f"  Energie/Zerfall: {self.energy_per_decay} MeV")
        print(f"  GDR-Peaks: {self.E_gdr_peaks} MeV")
        print(f"  GDR-Breiten: {self.Gamma_gdr} MeV")
        print(f"  GDR-Zentroid: {self.E_gdr_centroid:.1f} MeV")
        for i, (E, f) in enumerate(zip(self.E_gdr_peaks, self.f_gdr)):
            print(f"  RFT-Frequenz (Peak {i+1}): {f:.3e} Hz "
                  f"(aus E={E} MeV, f=E/(π·ℏ))")
        print(f"  σ_GDR(peak): {self.sigma_gdr_peak} mb")


# ============================================================
# Isotopendaten: GDR aus Literatur, Frequenzen aus RFT
# ============================================================

# Americium-241: Tochterisotop, kurzlebiger
# GDR: Doppelpeak ~12 und ~15 MeV (Aktiniden-Systematik)
americium_241 = Isotope(
    name="Americium-241",
    A=241, Z=95,
    half_life_years=432.2,
    E_gdr_peaks_MeV=[11.8, 14.8],
    Gamma_gdr_MeV=[4.0, 5.5],
    decay_constant=np.log(2) / 432.2,  # λ = ln(2)/t½
    energy_per_decay_MeV=5.638,  # Alpha-Zerfall
    sigma_gdr_peak_mb=350,
)

# Plutonium-239: Ausgangsmaterial
# GDR: Doppelpeak ~12 und ~15 MeV
# Photoabsorption: Berman & Fultz (1975)
plutonium_239 = Isotope(
    name="Plutonium-239",
    A=239, Z=94,
    half_life_years=24110,
    E_gdr_peaks_MeV=[12.0, 15.0],
    Gamma_gdr_MeV=[4.2, 5.8],
    decay_constant=np.log(2) / 24110,
    energy_per_decay_MeV=5.245,  # Alpha-Zerfall (+ Spaltung: 200 MeV)
    sigma_gdr_peak_mb=360,
    transmutations=[americium_241],
)

# Uranium-235
# GDR: Doppelpeak ~11.5 und ~14.5 MeV
uranium_235 = Isotope(
    name="Uranium-235",
    A=235, Z=92,
    half_life_years=7.038e8,
    E_gdr_peaks_MeV=[11.5, 14.5],
    Gamma_gdr_MeV=[4.0, 5.5],
    decay_constant=np.log(2) / 7.038e8,
    energy_per_decay_MeV=4.679,  # Alpha-Zerfall (Spaltung: ~200 MeV)
    sigma_gdr_peak_mb=340,
    transmutations=[plutonium_239],
)

# Thorium-232
# GDR: Doppelpeak ~11.0 und ~14.0 MeV
thorium_232 = Isotope(
    name="Thorium-232",
    A=232, Z=90,
    half_life_years=1.405e10,
    E_gdr_peaks_MeV=[11.0, 14.0],
    Gamma_gdr_MeV=[3.8, 5.2],
    decay_constant=np.log(2) / 1.405e10,
    energy_per_decay_MeV=4.083,
    sigma_gdr_peak_mb=330,
)


# ============================================================
# Validierung: Isotopdaten ausgeben
# ============================================================
if __name__ == "__main__":
    for isotope in [uranium_235, plutonium_239, americium_241, thorium_232]:
        isotope.info()
        print()
    
    # Vergleich: alte vs. neue Resonanzfrequenzen
    print("=" * 60)
    print("VERGLEICH: Alte vs. neue Resonanzfrequenzen")
    print("=" * 60)
    old_freqs = {
        "Plutonium-239": 2.1e8,
        "Americium-241": 1.9e8,
        "Uranium-235": 1.5e8,
    }
    for name, f_old in old_freqs.items():
        iso = {"Plutonium-239": plutonium_239,
               "Americium-241": americium_241,
               "Uranium-235": uranium_235}[name]
        f_new = iso.f_gdr_centroid
        print(f"  {name}:")
        print(f"    Alt:  {f_old:.2e} Hz (willkürlich)")
        print(f"    Neu:  {f_new:.2e} Hz (aus GDR + RFT)")
        print(f"    Faktor: {f_new/f_old:.2e}")