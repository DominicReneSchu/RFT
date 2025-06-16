import os
import sys
from simulation.weather_data import get_weather_data
from simulation.chaotic_dynamics import calculate_lyapunov_exponent
from simulation.resonance_theory import resonance_field_interaction
from simulation.schu_equation import schu_equation
from simulation.time_dynamics import multi_dimensional_time
#© Dominic Schu, 2025 – Alle Rechte vorbehalten.
def main():
    # Schritt 1: Frage nach dem OpenWeather API-Schlüssel
    api_key = input("Bitte gib deinen OpenWeather API-Schlüssel ein: ").strip()

    if not api_key:
        print("Fehler: Kein API-Schlüssel angegeben!")
        sys.exit(1)

    # Schritt 2: Frage nach dem gewünschten Datum zur Vorhersage (im Format TT.MM.JJJJ)
    forecast_date = input("Datum zur Vorhersage (TT.MM.JJJJ): ").strip()

    # Schritt 3: Beispielhafte Koordinaten für Zeven
    latitude = 53.2923
    longitude = 9.5286

    # Schritt 4: Hole historische Wetterdaten von OpenWeather
    historical_data = get_weather_data(latitude, longitude, api_key)

    if historical_data is None:
        print("Fehler beim Abrufen der Wetterdaten.")
        sys.exit(1)

    # Hier kannst du die gewonnenen Daten verwenden, um deine Vorhersagen zu berechnen.
    historical_temp = historical_data["current_temp"]  # Verwende 'current_temp' anstelle von 'historical_temp'
    wind_speed = historical_data["wind_speed"]  # Verwende 'wind_speed'
    humidity = historical_data["humidity"]  # Verwende 'humidity'

    # Schritt 5: Berechne die Amplitude als eine Variation (hier einfach als Beispiel)
    amplitude = historical_temp * 0.1  # Beispielhafte Amplitude-Berechnung (anpassen je nach Logik)

    # Schritt 6: Berechnungen der Chaostheorie (z. B. Lyapunov-Exponenten)
    lyapunov_exp = calculate_lyapunov_exponent(historical_temp, amplitude)
    
    # Schritt 7: Berechnung der Resonanzfelder
    resonance_result = resonance_field_interaction(historical_temp, wind_speed, humidity)
    
    # Schritt 8: Berechnung der Resonanzfeld-Gleichung
    schu_result = schu_equation(resonance_result)
    
    # Schritt 9: Zeitdynamik
    time_dynamics = multi_dimensional_time(schu_result)
    
    # Schritt 10: Ausgabe der Ergebnisse
    print(f"\nVorhersage für {forecast_date} basierend auf den gewonnenen Daten:")
    print(f"Historischer Mittelwert der Temperatur: {historical_temp}°C")
    print(f"Amplitudenberechnung: {amplitude}°C")
    print(f"Lyapunov-Exponenten: {lyapunov_exp}")
    print(f"Resonanzfeld-Interaktion: {resonance_result}")
    print(f"Resonanzfeld-Gleichung Ergebnis: {schu_result}")
    print(f"Zeitsimulation: {time_dynamics}")

if __name__ == "__main__":
    main()
