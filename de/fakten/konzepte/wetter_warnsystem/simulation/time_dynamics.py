import numpy as np
#© Dominic Schu, 2025 – Alle Rechte vorbehalten.
def multi_dimensional_time(t, dimension=2, time_scale=1.0):
    """
    Berechnet den Zeitfaktor in mehreren Dimensionen basierend auf der Zeit t.
    
    Parameter:
        t (float): Der aktuelle Zeitpunkt.
        dimension (int): Die Anzahl der Dimensionen, die in die Zeitberechnung einfließen (default: 2).
        time_scale (float): Ein Skalierungsfaktor, der die Zykluslänge der Zeit in allen Dimensionen beeinflusst (default: 1.0).
    
    Rückgabe:
        float: Der berechnete Zeitfaktor.
    """
    # Mehrdimensionale Zeit mit Skalierungsfaktor
    time_factor = np.prod([np.cos(t * (dimension + i) * time_scale) for i in range(dimension)])
    
    return time_factor
