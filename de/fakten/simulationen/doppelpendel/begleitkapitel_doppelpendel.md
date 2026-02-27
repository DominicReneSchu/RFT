# Doppelpendel — Interaktive Simulation

Interaktive Simulation eines Doppelpendels mit zusätzlichem
Resonanz-Kopplungsterm. Demonstriert chaotische Dynamik,
Energieaustausch und Kopplungseffekte im Rahmen der
Resonanzfeldtheorie (Axiome A1, A2).

<p align="center">
  <img src="doppelpendel.gif" alt="Animation Doppelpendel" width="800"/>
</p>

---

## Axiom-Bezug

| Axiom | Umsetzung |
|-------|-----------|
| A1 Schwingung | Beide Pendelarme schwingen mit Eigenfrequenz |
| A2 Superposition | Interferenz der Schwingungsmuster in den Trails |
| A4 Kopplung | Zusätzlicher Resonanzterm ε·sin(θ₂−θ₁) |

---

## 1. Physikalische Grundlagen

Das Doppelpendel besteht aus zwei starren Pendelarmen, verbunden
über ein Scharnier. Die Bewegungsgleichungen folgen aus der
Lagrange-Mechanik und sind gekoppelt und nichtlinear.

### Natürliche Kopplung

Die Lagrange-Gleichungen enthalten bereits die mechanische
Kopplung zwischen den Pendeln (über die gemeinsame Aufhängung).

### Resonanz-Kopplungsterm

Zusätzlich modelliert der Slider ε einen externen
Resonanz-Kopplungsoperator:

$$
\tau_{\text{kopplung}} = \pm\, \varepsilon \cdot \sin(\theta_2 - \theta_1)
$$

Dieser Term wirkt als zusätzliches Drehmoment, das die
Synchronisation der Oszillatoren verstärkt (ε > 0) oder
abschwächt (ε ≈ 0).

| ε-Wert | Verhalten |
|--------|-----------|
| 0.0 | Keine Zusatzkopplung (reines Doppelpendel) |
| 1.0 | Moderate Resonanzkopplung |
| e ≈ 2.72 | Maximale Kopplung (obere Grenze) |

---

## 2. Interaktive Steuerung

| Slider | Bedeutung |
|--------|-----------|
| θ₁, θ₂ | Startwinkel beider Pendelarme |
| ω₁, ω₂ | Anfangswinkelgeschwindigkeiten |
| m₁, m₂ | Massen |
| L₁, L₂ | Pendellängen |
| ε | Resonanz-Kopplungsstärke |
| Spurlänge | Trail-Länge (letzte N Positionen) |

---

## 3. Energieanzeige

Live-Anzeige über dem Pendel:

- **T** — Kinetische Energie
- **V** — Potentielle Energie
- **E_kopplung** — Kopplungsenergie (Resonanzterm)
- **κ** = E_kopplung / |E_gesamt| — Kopplungsverhältnis
- **ε** — Aktueller Kopplungsoperator

---

## 4. Trails und Chaos

Die farbigen Spuren (Trails) der Massenpunkte visualisieren
die chaotische Dynamik. Typische Beobachtungen:

- Bei kleinem ε: Annähernd klassisches Doppelpendel-Chaos
- Bei großem ε: Verstärkte Synchronisationsmuster
- Phasenübergänge bei Variation von ε sichtbar in den Trails

---

## 5. Technische Umsetzung

| Komponente | Implementierung |
|-----------|-----------------|
| ODE-Löser | `scipy.integrate.solve_ivp` (RK45) |
| Animation | `matplotlib.animation.FuncAnimation` |
| Interaktion | `matplotlib.widgets.Slider`, `Button` |
| Export | GIF über `PillowWriter` |
| Kapselung | `DoublePendulumSim`-Klasse |

---

## 6. Ausführung

```bash
pip install numpy matplotlib scipy
python doppelpendel.py
```

---

## 7. Erweiterungsmöglichkeiten

- Energieplot als Zeitreihe (T, V, E_kopplung)
- Poincaré-Schnitte für Chaosanalyse
- Mehrere Pendel (Pendel-Kette)
- Frequenzanalyse (FFT) der Winkelbewegungen
- Dämpfungsterm
- Integration von Axiom 5 (Energierichtung)

---

## Quellcode

[doppelpendel.py](doppelpendel.py)

---

*© Dominic-René Schu, 2025/2026 — Resonanzfeldtheorie*

---

⬅️ [zurück zur Übersicht](../README.md)