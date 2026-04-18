# Doppelpendel — Interaktive Simulation

Interaktive Simulation eines Doppelpendels mit dynamischer
Kopplungseffizienz ε(Δφ) = cos²(Δφ/2) nach Axiom 4.
Demonstriert chaotische Dynamik, Energieaustausch und
Resonanzkopplung.

<p align="center">
  <img src="doppelpendel.gif" alt="Animation Doppelpendel" width="800"/>
</p>

---

## Axiom-Bezug

| Axiom | Umsetzung |
|-------|-----------|
| A1 Schwingung | Beide Pendelarme schwingen mit Eigenfrequenz |
| A2 Superposition | Interferenz der Schwingungsmuster in den Trails |
| A4 Kopplungseffizienz | ε(Δφ) = cos²((θ₂−θ₁)/2) berechnet sich dynamisch aus dem Zustand |

---

## 1. Kopplungseffizienz (Axiom 4)

Die Kopplungseffizienz ε bestimmt den Anteil der übertragenen
Resonanzenergie und wird **dynamisch** aus der Phasendifferenz
der Pendelarme berechnet:

$$
\varepsilon(\Delta\varphi) = \cos^2\!\left(\frac{\theta_2 - \theta_1}{2}\right) \in [0, 1]
$$

### Grenzfälle

| Δφ = θ₂ − θ₁ | ε | Bedeutung |
|---------------|---|-----------|
| 0 | 1.0 | Perfekte Kopplung — Pendel in Phase |
| π/2 | 0.5 | Halbe Kopplung |
| π | 0.0 | Keine Kopplung — Pendel in Gegenphase |

### Effektiver Kopplungsterm

Der Resonanz-Kopplungsterm in den Bewegungsgleichungen lautet:

$$
\tau_{\text{kopplung}} = \pm\, A \cdot \varepsilon(\theta_2 - \theta_1) \cdot \sin(\theta_2 - \theta_1)
$$

- **A** (Slider): Kopplungsamplitude — skaliert die Stärke
- **ε** (dynamisch): Kopplungseffizienz — bestimmt den Anteil
- **sin(Δφ)**: Richtung des Kopplungsdrehmoments

Da ε bei Phasengleichheit maximal ist und bei Gegenphase
verschwindet, wird Energie bevorzugt übertragen, wenn die
Pendel ähnliche Phase haben — genau wie Axiom 4 es fordert.

---

## 2. Interaktive Steuerung

| Slider | Bedeutung |
|--------|-----------|
| θ₁, θ₂ | Startwinkel beider Pendelarme |
| ω₁, ω₂ | Anfangswinkelgeschwindigkeiten |
| m₁, m₂ | Massen |
| L₁, L₂ | Pendellängen |
| A | Kopplungsamplitude (Stärke des Resonanzterms) |
| Spurlänge | Trail-Länge (letzte N Positionen) |

**Wichtig:** ε ist kein Slider — die Kopplungseffizienz wird
in jedem Zeitschritt automatisch aus dem aktuellen Zustand
berechnet und live angezeigt.

---

## 3. Energieanzeige

Live über dem Pendel:

- **T** — Kinetische Energie
- **V** — Potentielle Energie
- **E_kopplung** — Kopplungsenergie (skaliert mit A · ε)
- **κ** = E_kopplung / |E_gesamt| — Kopplungsverhältnis
- **ε** — Aktuelle Kopplungseffizienz + Phasendifferenz Δφ

---

## 4. Trails und Chaos

Die farbigen Spuren der Massenpunkte visualisieren die
chaotische Dynamik:

- **A = 0:** Reines Doppelpendel ohne Zusatzkopplung
- **A klein:** Schwache Resonanzkopplung, klassisches Chaos
- **A groß:** Starke Synchronisationstendenz, Trails werden
  regelmäßiger wenn ε ≈ 1 (Pendel in Phase)

---

## 5. Physikalischer Hintergrund

Das Doppelpendel ist ein klassisches nichtlineares, chaotisches
System. Die Bewegungsgleichungen folgen aus der Lagrange-Mechanik
und sind in Standardliteratur (z.B. Goldstein, "Classical
Mechanics") hergeleitet.

Die **natürliche mechanische Kopplung** ist bereits in den
Lagrange-Gleichungen enthalten (gemeinsame Aufhängung). Der
Resonanz-Kopplungsterm A · ε · sin(Δφ) modelliert eine
**zusätzliche** Wechselwirkung, die die Interpretation als
Resonanzsystem im Sinne der RFT ermöglicht.

---

## 6. Ausführung

```bash
pip install numpy matplotlib scipy
python doppelpendel.py
```

---

## 7. Erweiterungsmöglichkeiten

- Energieplot als Zeitreihe (T, V, E_kopplung, ε)
- Poincaré-Schnitte für Chaosanalyse
- Pendel-Kette (mehr als zwei Pendel)
- FFT der Winkelbewegungen
- Dämpfungsterm
- Axiom 5: Energierichtung als Vektor

---

## Quellcode

[doppelpendel.py](doppelpendel.py)

---

*© Dominic-René Schu, 2025/2026 — Resonanzfeldtheorie*

---

## Querbestätigung innerhalb der RFT

Dieses Ergebnis bestätigt und wird bestätigt durch unabhängige Resultate aus anderen Bereichen:

| Ergebnis hier | Bestätigt durch | Bereich | Link |
|---|---|---|---|
| ε(θ₂−θ₁) = cos²(Δθ/2) als klassisch-mechanisches Analogon | Gekoppelte Oszillatoren: lineares klassisches Pendant | Klassische Mechanik | [→ Gekoppelte Oszillatoren](../gekoppelte_oszillatoren/gekoppelte_oszillatoren.md) |
| Energierichtung und Phasenabhängigkeit | Warpantrieb: Vorn/Hinten-Asymmetrie als makroskopische Energierichtung | Raumzeitgeometrie | [→ Warpantrieb](../../konzepte/warpantrieb/warpantrieb.md) |
| ε(Δφ) = cos²(Δφ/2) auch im Doppelpendel bestätigt | Schrödinger-Simulation: dieselbe Formel auf Quantenskala, Fidelity = 1.000000000000 | Quantenmechanik | [→ Schrödinger](../schrödinger/README.md) |

> **Eine Gleichung — E = π·ε(Δφ)·ℏ·f — bestätigt über Quantenmechanik, Kosmologie, Kernphysik und Raumzeitgeometrie.**

---

⬅️ [zurück zur Übersicht](../../../README.md#simulationen)