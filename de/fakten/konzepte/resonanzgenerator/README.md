# ⚡ Resonanzgenerator

*Dominic-René Schu, 2025/2026*

Der **Resonanzgenerator** ist die makroskopische Bestätigung
der RFT-Grundgleichung. Er zeigt, dass

> **E = π · ε(Δφ) · ℏ · f  mit  ε = cos²(Δφ/2)**

nicht nur die Riesendipolresonanz im Atomkern beschreibt
(→ [Resonanzreaktor](../resonanzreaktor/README.md)),
sondern auch einen gewöhnlichen mechanischen Oszillator —
ohne Anpassung und ohne freie Parameter.

**Diese Gleichung gab es vor der RFT nicht.** Die klassische
Physik beschreibt Mechanik, Kernphysik, Optik und Elektrik
jeweils mit eigenen Formalismen. Die RFT vereinheitlicht sie.

---

## Zentrale Ergebnisse

| Messgröße | Wert |
|-----------|------|
| Resonanzfrequenz f₀ | 1.5915 Hz (Theorie = Simulation, Δ < 0.1%) |
| ε(Δφ) = cos²(Δφ/2) | Exakt bestätigt (Amplitude + Energie) |
| E(Δφ=0) / ⟨E⟩_ink | 2.50 (Theorie = Simulation, exakt) |
| Δφ = π → ε = 0 | Resonanz vollständig unterbunden |
| κ | 1 (parameterfrei, wie beim Resonanzreaktor) |

---

## Praktische Anwendung

**Maschinenresonanz unterbinden:**

```
    Problem:  Maschine wird bei f₀ angeregt → Resonanzkatastrophe
    Lösung:   Phase um Δφ = π verschieben
    Ergebnis: ε(π) = cos²(π/2) = 0 → Keine Kopplung
    Vorteil:  Analytisch aus einer Gleichung, nicht empirisch
```

---

## Axiom-Zuordnung

| Axiom | Anwendung |
|-------|----------|
| A1 (Universelle Schwingung) | System als Oszillator mit f₀ |
| A3 (Resonanzbedingung) | Maximale Kopplung bei f = f₀ |
| A4 (Kopplungsenergie) | E = π · ε · ℏ · f |
| A5 (Energierichtung) | Feld → System → mechanische Arbeit |
| A7 (Invarianz) | Gleiche Physik makro ↔ nuklear |

---

## Dokumente

| Datei | Beschreibung |
|-------|-------------|
| [resonanzgenerator.md](resonanzgenerator.md) | Physik, Ergebnisse, Maschinenresonanz |
| [nichtlineare_resonanzanalyse.md](nichtlineare_resonanzanalyse.md) | Nichtlinearität, Duffing, Chaos |
| [resonanzgenerator.py](resonanzgenerator.py) | Simulation: Frequenz-Sweep, Phasenscan |
| [nichtlineare_resonanzanalyse.py](nichtlineare_resonanzanalyse.py) | Simulation: Duffing, Energiedämpfung |

---

## Ausführung

```bash
python resonanzgenerator.py                    # → figures/ (4 Plots)
python nichtlineare_resonanzanalyse.py          # → figures/ (4 Plots)
streamlit run nichtlineare_resonanzanalyse.py   # Interaktiv (optional)
```

---

## Zusammenfassung

```
    Grundformel:   E = π · ε(Δφ) · ℏ · f
    Kopplung:      ε = cos²(Δφ/2), κ = 1
    Bestätigt:     Amplitude ∝ cos², Energie ∝ cos⁴, Signatur = 2.50
    Anwendung:     Δφ → π unterbindet Maschinenresonanz
    Verbindung:    Gleiche Formel wie Resonanzreaktor (10²¹ Hz Abstand)
    Neu:           Diese vereinheitlichende Gleichung gab es vorher nicht
```

✅ Grundformel bestätigt (Frequenz-Sweep)
✅ Phasenscan exakt (cos², cos⁴, Signatur 2.50)
✅ Nichtlinearität untersucht (Duffing, Energiedämpfung)
✅ Anwendung identifiziert (Maschinenresonanz)
✅ Skalenübergang bestätigt (Makro ↔ Nuklear, κ = 1)

---

© Dominic-René Schu — Resonanzfeldtheorie 2025/2026

---

[Zurück zur Übersicht](../../../README.md)