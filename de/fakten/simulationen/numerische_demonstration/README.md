# Resonanzfeldtheorie — Numerische Demonstration

Numerische Analyse und Visualisierung: Resonanzenergie,
Kopplungseffizienz und Resonanzentropie über dem
(A, τ)-Parameterraum.

> **Einordnung:** Diese Simulation demonstriert die interne
> Konsistenz der Axiome A3–A5. Sie ist keine empirische
> Validierung. Für den empirischen Test siehe die
> [Monte-Carlo-Analyse](../../empirisch/monte_carlo_test/monte_carlo.md).

---

## Axiom-Bezug

| Axiom | Was demonstriert wird |
|-------|----------------------|
| A3 Resonanzbedingung | Lorentz-Profil: Peak bei ω_ext ≈ ω₀ |
| A4 Kopplungseffizienz | ε = E_res / A ∈ (0, 1] |
| A5 Stabiles Feld | Entropie S = −ε·ln(ε) ≥ 0 |

---

## Schnelleinstieg

```bash
pip install numpy matplotlib
python numerische_demonstration.py
```

Tests:
```bash
python tests/test_numerische_demonstration.py
```

---

## Dateistruktur

| Datei | Funktion |
|-------|----------|
| [`numerische_demonstration.py`](numerische_demonstration.py) | Hauptmodul: Berechnung + Visualisierung |
| [`begleitkapitel_numerische_demonstration.md`](begleitkapitel_numerische_demonstration.md) | Erläuterung und Einordnung |
| [`tests/test_numerische_demonstration.py`](tests/test_numerische_demonstration.py) | 16 Unit-Tests (standalone + pytest) |
| [`requirements.txt`](requirements.txt) | Abhängigkeiten |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | Beitragsrichtlinien |
| [`docs/index.md`](docs/index.md) | API-Dokumentation |

---

## API

```python
from numerische_demonstration import (
    berechne_resonanzenergie,
    berechne_kopplungseffizienz,
    berechne_resonanzentropie,
    plot_numerische_demonstration,
)
```

---

*© Dominic-René Schu, 2025/2026 — Resonanzfeldtheorie*

---

⬅️ [zurück](../README.md)