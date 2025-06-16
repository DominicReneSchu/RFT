# simulation.py
#© Dominic Schu, 2025 – Alle Rechte vorbehalten.
import numpy as np
import matplotlib.pyplot as plt
from material import plutonium_239, americium_241
from resonance import simulate_resonance

def plot_results(time_steps, excitation_levels, materials):
    """
    Visualisiert die Ergebnisse der Simulation.
    
    Args:
        time_steps (int): Anzahl der Zeitschritte.
        excitation_levels (list): Exzitationslevel des Materials über die Zeit.
        materials (list): Liste der transmutierten Materialien pro Zeitschritt.
    """
    time = np.arange(1, time_steps + 1)

    plt.figure(figsize=(12, 6))

    # Plot des Exzitationslevels
    plt.subplot(2, 1, 1)
    plt.plot(time, excitation_levels, label="Exzitationslevel")
    plt.title('Resonanzanregung des Materials')
    plt.xlabel('Zeitschritt')
    plt.ylabel('Exzitationslevel')
    plt.legend()

    # Plot der Materialtransmutation
    plt.subplot(2, 1, 2)
    plt.step(time, materials, label="Material", where="post")
    plt.title('Materialtransmutation')
    plt.xlabel('Zeitschritt')
    plt.ylabel('Material')
    plt.legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Festlegung der Simulationsparameter
    material = plutonium_239  # Startmaterial
    neutron_flux = 1e13  # Neutronenfluss
    time_steps = 10  # Anzahl der Zeitschritte
    time_step_size = 1  # Dauer eines Zeitschritts in Jahren
    temperature = 350  # Temperatur in Kelvin

    # Ausführung der Simulation
    excitation_levels, materials = simulate_resonance(
        material, neutron_flux, time_steps, time_step_size, temperature
    )

    # Ergebnisse visualisieren
    plot_results(time_steps, excitation_levels, materials)