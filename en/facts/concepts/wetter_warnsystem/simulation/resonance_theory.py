import numpy as np
#© Dominic Schu, 2025 – Alle Rechte vorbehalten.
def resonance_field_interaction(temperature, wind_speed, humidity, temp_factor=0.1, wind_factor=0.05, humidity_factor=0.1):
    """
    Berechnet die Resonanzfeld-Interaktion basierend auf Temperatur, Windgeschwindigkeit und Luftfeuchtigkeit.
    
    Parameter:
        temperature (float): Temperatur in °C.
        wind_speed (float): Windgeschwindigkeit in m/s.
        humidity (float): Luftfeuchtigkeit in %.
        temp_factor (float): Anpassungsfaktor für die Temperatur (default: 0.1).
        wind_factor (float): Anpassungsfaktor für die Windgeschwindigkeit (default: 0.05).
        humidity_factor (float): Anpassungsfaktor für die Luftfeuchtigkeit (default: 0.1).
    
    Rückgabe:
        float: Der berechnete Resonanzfaktor.
    """
    # Berechnung des Resonanzfaktors unter Verwendung der gegebenen Faktoren
    resonance_factor = np.cos(temperature * temp_factor) * np.sin(wind_speed * wind_factor) * np.exp(-humidity * humidity_factor)
    
    return resonance_factor
