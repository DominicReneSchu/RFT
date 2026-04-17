# Resonanzfeld-Simulation

Interaktive Simulation der Resonanzfeldtheorie (RFT). Visualisiert
die Energieübertragung zwischen zwei gekoppelten Oszillatoren
basierend auf der Grundformel (Axiom 4):

$$
E_{\text{eff}} = \pi \cdot \varepsilon(\Delta\varphi) \cdot h \cdot f
$$

mit der Kopplungseffizienz:

$$
\varepsilon(\Delta\varphi) = \cos^2(\Delta\varphi / 2) \in [0, 1]
$$

---

## Axiome der Resonanzfeldtheorie

| Axiom | Kernaussage | Formel |
|-------|-------------|--------|
| A1 | Universelle Schwingung | ψ = A·cos(kx − ωt + φ) |
| A2 | Superposition | Φ = Σ ψᵢ |
| A3 | Resonanzbedingung | \|f₁/f₂ − m/n\| < δ |
| A4 | Kopplungsenergie | E = π·ε(Δφ)·h·f |
| A5 | Energierichtung | E⃗ = E·ê(Δφ, ∇Φ) |
| A6 | Informationsfluss | MI > 0 ⟺ PCI > 0 |
| A7 | Invarianz | Resonanzstruktur ist transformationsinvariant |

Vollständige Axiomatik:
[axiomatische_grundlegung.md](../../docs/definitionen/axiomatische_grundlegung.md)

---

## Was die Simulation zeigt

### Schwingungen und Superposition (A1, A2)

Zwei Oszillatoren mit Frequenzen f₁ und f₂ schwingen unabhängig.
Ihre Superposition erzeugt Interferenzmuster — konstruktiv bei
Resonanz, destruktiv bei Verstimmung.

### Resonanzbedingung (A3)

Die Simulation prüft automatisch, ob f₁/f₂ ein rationales
Verhältnis n/m bildet (innerhalb einer Toleranz δ = 1%).
Bei Resonanz wird die Kopplung aktiviert.

### Kopplungseffizienz (A4)

Die Kopplungseffizienz ε(Δφ) = cos²(Δφ/2) bestimmt den
Anteil der übertragenen Resonanzenergie:

- Δφ = 0 → ε = 1 (perfekte Kopplung, Phasengleichheit)
- Δφ = π/2 → ε = 0.5 (halbe Kopplung)
- Δφ = π → ε = 0 (keine Kopplung, Gegenphase)

### Energierichtung (A5)

Der Energierichtungsvektor wird als Differenz der
Momentanenergien auf zwei Zeitskalen berechnet und
zeigt, in welche Richtung Energie fließt.

### Kopplungsarten

Drei Modelle der Energieübertragung:

- **Linear:** E_trans = ε · ψ₁ · ψ₂
- **Quadratisch:** E_trans = ε · ψ₁² · ψ₂
- **Trigonometrisch:** E_trans = ε · sin(ψ₁) · sin(ψ₂)

---

## Grenzfälle der Kopplungseffizienz

| Bedingung | ε | Energie | Physik |
|-----------|---|---------|--------|
| Perfekte Kopplung (Δφ = 0) | 1 | π·h·f | Maximale Resonanzenergie |
| Klassischer Grenzfall (ε = 1/π) | 0.318 | h·f | Planck-Gleichung |
| Natürliche Dämpfung (ε = 1/e) | 0.368 | (π/e)·h·f | Nach Relaxationszeit |
| Halbe Kopplung (Δφ = π/2) | 0.5 | π·h·f/2 | 90° Phasenverschiebung |
| Keine Kopplung (Δφ = π) | 0 | 0 | Entkoppelte Systeme |

---

<p align="center">
  <img src="bilder/simulation_rft.png" alt="RFT" width="800"/>
</p>

---

## Voraussetzungen

- Python ≥ 3.8
- Installierte Pakete:

```bash
pip install numpy matplotlib
```

---

## Ausführung

```bash
python simulation_resonanzfeldtheorie.py
```

Die interaktiven Slider im matplotlib-Fenster ermöglichen
Echtzeit-Variation aller Parameter:

- **f₁, f₂** — Frequenzen der beiden Oszillatoren
- **Δφ** — Phasendifferenz (bestimmt ε über cos²(Δφ/2))
- **t_max** — Simulationsdauer
- **Kopplung** — Kopplungsmodell (linear, quadratisch, trigonometrisch)

---

## Quellcode

[simulation_resonanzfeldtheorie.py](simulation_resonanzfeldtheorie.py)

---

*© Dominic-René Schu, 2025/2026 — Resonanzfeldtheorie*

---

⬅️ [zurück zur Übersicht](../../../README.md#simulationen)