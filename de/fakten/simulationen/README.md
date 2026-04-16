# Simulationen zur Resonanzfeldtheorie

Numerische und interaktive Modelle zur Demonstration und
Analyse der Resonanzfeldtheorie (RFT). Alle Simulationen
laufen standalone mit Python ≥ 3.8.

Zentrale Gleichung (Axiom 4 — Kopplungseffizienz):

$$
E_{\text{eff}} = \pi \cdot \varepsilon(\Delta\varphi) \cdot h \cdot f
$$

mit ε(Δφ) = cos²(Δφ/2) ∈ [0, 1] als Kopplungseffizienz.

---

## Übersicht

| Simulation | Axiome | Beschreibung |
|------------|--------|-------------|
| [Resonanzfeld](resonanzfeld/simulation_resonanzfeldtheorie.md) | A1–A5 | Zwei Oszillatoren, Kopplungseffizienz, Energierichtung |
| [Doppelpendel](doppelpendel/begleitkapitel_doppelpendel.md) | A1, A2, A4 | Klassisches Doppelpendel mit dynamischer Kopplungseffizienz ε(θ₂−θ₁) |
| [Gekoppelte Oszillatoren](simulation_atommodell/simulation_atommodell.md) | A1–A4 | Energieaustausch, Resonanzerkennung, Live-Animation |
| [Numerische Demonstration](numerische_demonstration/README.md) | A3, A4, A5 | Konsistenz-Demonstration: Resonanzenergie, Kopplungseffizienz und Entropie über (A, τ) |
| [Resonanz-KI](resonanz_ki/begleitkapitel_resonanz_ki.md) | A1–A4 | Zwei gekoppelte Akteure, Fourier-Analyse des Resonanzfelds |
| [Raumzeit-Resonanzfeld](relativitaet_verbindung/README.md) | A1–A7 | Skalare Resonanzfelder in flacher und gekrümmter Raumzeit |
| [Schrödinger (1D)](schrödinger/README.md) | A1, A2, A4 | Referenz-QM und RFT-Resonanz-Hamiltonoperator — Korrespondenzprinzip |

---

## Schnellstart

```bash
# Resonanzfeld-Simulation (empfohlener Einstieg)
cd resonanzfeld
pip install numpy matplotlib
python simulation_resonanzfeldtheorie.py

# Gekoppelte Oszillatoren
cd simulation_atommodell
pip install numpy matplotlib scipy
python run.py

# Numerische Demonstration
cd numerische_demonstration
pip install numpy matplotlib
python resonanzfeld.py

# Doppelpendel
cd doppelpendel
pip install numpy matplotlib scipy
python doppelpendel.py

# Resonanz-KI
cd resonanz_ki
pip install numpy matplotlib
python resonanz_ki.py

# Raumzeit-Framework
cd relativitaet_verbindung
pip install -r requirements.txt
python run_1d.py

# Schrödinger (Referenz + RFT-Korrespondenz)
cd schrödinger
pip install numpy matplotlib
python python/schrodinger_1d_reference.py --checks
python python/schrodinger_1d_rft.py --checks
python python/schrodinger_1d_rft_dynamic.py --checks
python python/schrodinger_1d_rft_perturbation.py --checks
python python/schrodinger_1d_rft_experiment.py --checks
```

---

## Kopplungseffizienz-Modelle

Alle Simulationen verwenden ε ∈ (0, 1] als Kopplungseffizienz —
den Anteil der übertragenen Resonanzenergie. Drei komplementäre
Realisierungen:

| Modell | Formel | Abhängigkeit | Simulation |
|--------|--------|-------------|------------|
| Phasenbasiert | cos²(Δφ/2) | Phasendifferenz | Resonanzfeld, Resonanz-KI, Doppelpendel, Schrödinger |
| Frequenzbasiert (Lorentz) | 1/(1+(Δω/γ)²) | Frequenzverstimmung | Numerische Demonstration |
| Exponentiell | exp(−α·\|Δf\|) | Frequenzdifferenz | Gekoppelte Oszillatoren |

---

## Axiom-Zuordnung

| Axiom | Simulation | Was wird demonstriert |
|-------|-----------|----------------------|
| A1 Schwingung | Alle | Periodische Oszillation als Grundstruktur |
| A2 Superposition | Resonanzfeld, Doppelpendel, Resonanz-KI, Schrödinger | Interferenz und Schwebung |
| A3 Resonanzbedingung | Resonanzfeld, Oszillatoren, Num. Demo | Rationale Frequenzverhältnisse / Lorentz-Profil |
| A4 Kopplungseffizienz | Alle außer Raumzeit | ε bestimmt Anteil der übertragenen Energie |
| A5 Energierichtung | Resonanzfeld, Num. Demo | Entropie und Energiefluss |
| A7 Invarianz | Raumzeit-Framework | Resonanzstruktur unter Koordinatenwechsel |

---

## Hinweis zur Einordnung

Die Simulationen demonstrieren die **interne Konsistenz** der
Axiome und visualisieren Resonanzphänomene. Sie sind keine
empirischen Beweise. Die empirische Validierung erfolgt über
die [Monte-Carlo-Analyse](../empirisch/monte_carlo_test/monte_carlo.md)
mit unabhängigen Daten.

---

*© Dominic-René Schu, 2025/2026 — Resonanzfeldtheorie*

---

[Zurück zur Übersicht](../../README.md)