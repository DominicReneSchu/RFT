import numpy as np
#© Dominic Schu, 2025 – Alle Rechte vorbehalten.
def calculate_lyapunov_exponent(initial_conditions, time_steps):
    """
    Berechnet den Lyapunov-Exponenten basierend auf den Anfangsbedingungen und der Anzahl der Zeitschritte.
    
    Parameter:
        initial_conditions (list): Anfangsbedingungen des Systems.
        time_steps (int): Anzahl der Zeitschritte.
    
    Rückgabe:
        float: Der Lyapunov-Exponent des Systems.
    """
    temp_variation = []
    for i in range(time_steps):
        # Beispiel einer chaotischen Zeitreihe
        temp_variation.append(np.sin(i * 0.1) * initial_conditions[0] + initial_conditions[1])
    
    lyapunov_exponent = np.mean(temp_variation) / np.max(np.abs(temp_variation))
    return lyapunov_exponent
