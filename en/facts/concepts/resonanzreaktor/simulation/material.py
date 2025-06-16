# material.py
#© Dominic Schu, 2025 – Alle Rechte vorbehalten.
import numpy as np

class Isotope:
    def __init__(self, name, half_life, resonance_freq, decay_constant, energy_per_decay=None, transmutations=None):
        """
        Erstellt eine Instanz eines Isotops mit den gegebenen Eigenschaften.
        
        Args:
            name (str): Name des Isotops.
            half_life (float): Halbwertszeit in Jahren.
            resonance_freq (float): Resonanzfrequenz in Hz.
            decay_constant (float): Zerfallskonstante in 1/Jahr.
            energy_per_decay (float, optional): Energie pro Zerfall in MeV.
            transmutations (list, optional): Eine Liste von Isotopen, die durch Transmutation erreicht werden.
        """
        self.name = name
        self.half_life = half_life
        self.resonance_freq = resonance_freq
        self.decay_constant = decay_constant
        self.energy_per_decay = energy_per_decay
        self.transmutations = transmutations or []  # Liste von Transmutationen

    def decay(self, time):
        """Berechnet den Zerfall des Materials über eine gegebene Zeitspanne."""
        return np.exp(-self.decay_constant * time)  # Exponentieller Zerfall

    def energy_released(self, time):
        """Berechnet die freigesetzte Energie über eine gegebene Zeitspanne."""
        if self.energy_per_decay is not None:
            decay_factor = self.decay(time)
            return decay_factor * self.energy_per_decay
        else:
            return 0  # Wenn keine Energie pro Zerfall definiert wurde

    def transmute(self):
        """Führt Transmutation durch und gibt die nächste Stufe der Transmutationskette zurück."""
        if self.transmutations:
            return self.transmutations[0]  # Gibt das erste transmutierte Isotop zurück
        return self  # Keine Transmutation, bleibt unverändert

# Beispiele für Isotope mit einer Transmutationskette
americium_241 = Isotope("Americium-241", 432, 1.9e8, 0.00015, energy_per_decay=5.5)
plutonium_239 = Isotope("Plutonium-239", 24000, 2.1e8, 0.0002, energy_per_decay=200, transmutations=[americium_241])
uranium_235 = Isotope("Uranium-235", 700000000, 1.5e8, 0.0001, energy_per_decay=200, transmutations=[plutonium_239])
thorium_232 = Isotope("Thorium-232", 1400000000, 1.8e8, 0.00005, energy_per_decay=100)

def simulate_decay_chain(isotope, time_span):
    """
    Simuliert den Zerfall und die Transmutation eines Isotops über eine gegebene Zeitspanne.
    
    Args:
        isotope (Isotope): Das Ausgangsisotop.
        time_span (float): Die Zeitspanne in Jahren.
    """
    current_isotope = isotope
    for year in range(int(time_span)):
        print(f"Jahr {year}: {current_isotope.name} mit {current_isotope.energy_released(year):.2f} MeV freigegebener Energie")
        if current_isotope.transmutations:
            next_isotope = current_isotope.transmute()
            if next_isotope.name != current_isotope.name:
                print(f"Transmutation zu {next_isotope.name} erfolgt.")
                current_isotope = next_isotope
        else:
            print(f"Kein weiterer Zerfall oder Transmutation für {current_isotope.name}.")
            break
    print(f"Endgültiges Isotop: {current_isotope.name}")

if __name__ == "__main__":
    # Beispiel: Simulation der Zerfallskette für Uranium-235 über 10 Jahre
    simulate_decay_chain(uranium_235, 10)