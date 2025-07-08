# Von der Punktwolke zur Glockenkurve

**Wie man die Normalverteilung aus zwei Würfeln herleiten kann**  
*Ein alternativer Zugang zur Gauß-Glocke – anschaulich, systemisch, resonant*

---

## 1. Ausgangspunkt: Zwei Würfel

Wir beginnen mit einem einfachen Experiment:

> Zwei ideale sechsseitige Würfel werden gleichzeitig geworfen. Die Augensumme wird notiert.

### Wahrscheinlichkeitsverteilung der Augensummen

| Summe | Anzahl Kombinationen | Wahrscheinlichkeit |
| ----- | -------------------- | ------------------ |
| 2     | 1                    | 1/36 ≈ 2,78 %      |
| 3     | 2                    | 2/36 ≈ 5,56 %      |
| 4     | 3                    | 3/36 ≈ 8,33 %      |
| 5     | 4                    | 4/36 ≈ 11,11 %     |
| 6     | 5                    | 5/36 ≈ 13,89 %     |
| 7     | 6                    | 6/36 ≈ 16,67 %     |
| 8     | 5                    | 5/36 ≈ 13,89 %     |
| 9     | 4                    | 4/36 ≈ 11,11 %     |
| 10    | 3                    | 3/36 ≈ 8,33 %      |
| 11    | 2                    | 2/36 ≈ 5,56 %      |
| 12    | 1                    | 1/36 ≈ 2,78 %      |

> Die Verteilung ist diskret, symmetrisch und bildet ein Dreieck mit Maximum bei Summe 7.

---

## 2. Idee: Punktwolke als Funktion deuten

Wir interpretieren die Wahrscheinlichkeiten als Punktwerte einer Funktion:

**f(s) := P(S = s)**

Nun stellen wir die Hypothese auf:

> **Die Form dieser Punktwolke kann durch eine glockenförmige Funktion angenähert werden.**

### Ansatz einer exponentiellen Dichte

**f(s) = a · exp(-b · (s - c)²)**

Dabei ist:

- **a**: maximale Höhe (Amplitude)
- **b**: Steilheit (inverse Varianz)
- **c**: Zentrum der Glocke (hier: 7)

Durch Einsetzen der Punktwahrscheinlichkeiten lassen sich a und b schätzen.

> Beispiel: f(7) = 6/36 = 1/6 → a = 1/6  
> f(6) = 5/36 = (1/6) · exp(-b) → b = -ln(5/6) ≈ 0,182

---

## 3. Von zwei zu vielen Würfeln

Wenn wir die Summenverteilung für mehr als zwei Würfel betrachten, entsteht eine immer glattere Glocke:

- Bei 3 Würfeln: erste Krümmung zur Glocke
- Bei 5 Würfeln: deutlich glockenförmige Struktur
- Bei 10+ Würfeln: Näherung an echte Normalverteilung

> Die Wahrscheinlichkeitsverteilung der Summe unabhängiger Gleichverteilungen konvergiert gegen die Normalverteilung (Zentraler Grenzwertsatz).

---

## 4. Interaktive Simulation (Python)

Die folgende Python-Simulation erlaubt es, durch Eingabe der Würfelanzahl und Anzahl der Würfe die resultierende Wahrscheinlichkeitsverteilung der Augensummen zu erzeugen – und mit der theoretischen Gauß-Glocke zu vergleichen:

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from collections import Counter

# Parameter eingeben
dice = int(input("Anzahl der Würfel: "))
trials = int(input("Anzahl der Simulationen: "))

# Simulation
sums = [sum(np.random.randint(1, 7, dice)) for _ in range(trials)]
counter = Counter(sums)

# Wahrscheinlichkeiten
x_vals = np.array(sorted(counter.keys()))
y_vals = np.array([counter[x] / trials for x in x_vals])

# Erwartungswert und Standardabweichung
mittelwert = dice * 3.5
stdabw = np.sqrt(dice * 35 / 12)
x_range = np.linspace(min(x_vals), max(x_vals), 500)
gauss = norm.pdf(x_range, mittelwert, stdabw)

# Plot
plt.figure(figsize=(10, 5))
plt.bar(x_vals, y_vals, width=0.8, alpha=0.6, label='Simulierte Verteilung')
plt.plot(x_range, gauss, 'r-', lw=2, label='Gauß-Glocke')
plt.title(f'Summenverteilung bei {dice} Würfeln')
plt.xlabel('Augensumme')
plt.ylabel('Wahrscheinlichkeit')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
```

> Durch Eingabe verschiedener Würfelzahlen wird die Annäherung an die Glocke visuell erfahrbar.

---

## 5. Didaktische Schlussfolgerung

**Dieser Zugang ist konkret, greifbar, experimentell und mathematisch exakt.**

| Klassisch (Gauß)                      | Alternativ (Schu)                          |
| ------------------------------------- | ------------------------------------------ |
| Astronomische Fehleranalyse           | Würfelsummen und Punktwahrscheinlichkeiten |
| Funktionstheorie und Integralrechnung | Exponentieller Fit über empirische Punkte  |
| Top-down (Definition der Dichte)      | Bottom-up (Beobachtung der Struktur)       |

### Resonanzdidaktik

- Lernende erleben selbst die Struktur
- Die Glocke entsteht aus dem Feld, nicht aus Formeln
- Diskret und stetig werden nicht getrennt, sondern verbunden

---

## 6. Ausblick und Erweiterung

- Interaktive Python-Simulation: Punktwolke → Fit → Dichtefunktion (oben integriert)
- Vergleich mit realen Messdaten (Fehlerverteilungen, Schwankungen, etc.)
- Verbindung zur Statistik (Mittelwert, Varianz, Standardabweichung)

---

## 7. Fazit

> Die Glockenkurve ist keine abstrakte Formel, sondern eine emergente Ordnung aus Zufallsstruktur.  
> Ihr Ursprung liegt im Resonanzfeld zwischen diskretem Ereignis und stetiger Gestalt.  
> **Jeder kann sie selbst entdecken – mit zwei Würfeln.**

---