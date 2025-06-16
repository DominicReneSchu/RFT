# run.py
#© Dominic Schu, 2025 – Alle Rechte vorbehalten.

from material import plutonium_239
from simulation import simulate_resonance, plot_results

def main():
    """
    Hauptfunktion, um die Resonanz-Simulation auszuführen.
    """
    # --- Parameter der Simulation ---
    material = plutonium_239  # Startmaterial für die Simulation
    neutron_flux = 1e13  # Neutronenfluss (Teilchen/cm²/s)
    time_steps = 10  # Anzahl der Zeitschritte
    time_step_size = 1  # Zeitschrittdauer in Jahren
    temperature = 350  # Temperatur in Kelvin

    # --- Simulation ausführen ---
    print("Starte die Resonanz-Simulation...")
    excitation_levels, materials = simulate_resonance(
        material, neutron_flux, time_steps, time_step_size, temperature
    )

    # --- Ergebnisse ausgeben ---
    print("\nSimulationsergebnisse:")
    for step, (excitation, mat) in enumerate(zip(excitation_levels, materials)):
        print(f"Schritt {step + 1}: Material = {mat}, Anregungsniveau = {excitation:.2f}")

    # --- Ergebnisse visualisieren ---
    plot_results(time_steps, excitation_levels, materials)

if __name__ == "__main__":
    main()