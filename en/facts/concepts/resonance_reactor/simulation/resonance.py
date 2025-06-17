# resonance.py
#© Dominic Schu, 2025 – Alle Rechte vorbehalten.
import numpy as np
from material import americium_241

def resonance_field(frequency, temperature):
    """
    Berechnet das Resonanzfeld unter Berücksichtigung der Temperatur.
    
    Args:
        frequency (float): Die Resonanzfrequenz des Materials.
        temperature (float): Die Temperatur des Systems in Kelvin.
    
    Returns:
        tuple: Angepasste Resonanzfrequenz und Breite des Resonanzfensters.
    """
    adjusted_frequency = frequency * (1 + 0.01 * (temperature - 300))  # Temperaturabhängigkeit
    resonance_window = 0.1 * adjusted_frequency  # Breite des Resonanzfensters
    return adjusted_frequency, resonance_window

def excite_material(material, time, temperature):
    """
    Berechnet die Anregung des Materials basierend auf der Resonanzfrequenz und Zeit.
    
    Args:
        material (Isotope): Das Material, das angeregt werden soll.
        time (float): Die vergangene Zeit in Sekunden.
        temperature (float): Die Temperatur des Systems in Kelvin.
    
    Returns:
        tuple: Anregungsgrad und Resonanzfenster.
    """
    decay_effect = material.decay(time)
    resonance_freq, resonance_window = resonance_field(material.resonance_freq, temperature)
    
    # Modifizierte Anregung, abhängig vom Zerfall des Materials und der Resonanzfrequenz
    excitation_level = np.sin(resonance_freq * time) * decay_effect  # Einfache Schwingungsberechnung
    return excitation_level, resonance_window

def transmutation(material, neutron_flux, threshold_neutron_flux=1e12):
    """
    Transmutiert langlebige Isotope in weniger gefährliche Isotope, wenn ein Schwellenwert des Neutronenflusses überschritten wird.
    
    Args:
        material (Isotope): Das aktuelle Material.
        neutron_flux (float): Der aktuelle Neutronenfluss.
        threshold_neutron_flux (float, optional): Schwellenwert für die Transmutation.
        
    Returns:
        Isotope: Das transmutierte Material oder das ursprüngliche Material, falls keine Transmutation stattfindet.
    """
    transmutations_dict = {
        "Plutonium-239": americium_241,
        # Hier können weitere Transmutationen hinzugefügt werden
    }

    # Überprüfen, ob das Material transmutiert werden kann
    if material.name in transmutations_dict and neutron_flux > threshold_neutron_flux:
        return transmutations_dict[material.name]  # Transmutation wird durchgeführt
    return material  # Keine Transmutation

def simulate_resonance(material, neutron_flux, time_steps, time_step_size, temperature=300):
    """
    Simuliert die Resonanz und Transmutation eines Isotops über mehrere Zeitschritte.
    
    Args:
        material (Isotope): Das Ausgangsmaterial.
        neutron_flux (float): Der Neutronenfluss.
        time_steps (int): Anzahl der Zeitschritte.
        time_step_size (float): Größe eines Zeitschritts (in Jahren).
        temperature (float): Temperatur des Systems (in Kelvin).
        
    Returns:
        list: Liste von Anregungsniveaus pro Zeitschritt.
        list: Liste von Materialnamen pro Zeitschritt.
    """
    excitation_levels = []
    materials = []

    for step in range(time_steps):
        # Berechne die Anregung des Materials und aktualisiere das Material basierend auf der Transmutation
        excitation_level, _ = excite_material(material, step * time_step_size, temperature)
        excitation_levels.append(excitation_level)
        
        # Transmutiere das Material, falls notwendig
        material = transmutation(material, neutron_flux)
        materials.append(material.name)

    return excitation_levels, materials