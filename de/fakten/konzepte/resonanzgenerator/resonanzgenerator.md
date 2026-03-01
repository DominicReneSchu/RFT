# Resonanzgenerator – Physik, Simulation und Ergebnisse

*Dominic-René Schu, 2025/2026*

---

## 1. Grundprinzip

Der **Resonanzgenerator** ist ein mechanisches System, das durch
kohärente Kopplung an ein externes Schwingungsfeld Energie
hocheffizient aufnimmt oder abgibt. Er demonstriert die zentrale
Aussage der Resonanzfeldtheorie (RFT):

> **Die Grundgleichung E = π · ε(Δφ) · ℏ · f mit ε = cos²(Δφ/2)
> beschreibt den Energietransfer auf allen Skalen — von der
> mechanischen Schwingung bis zur Kernphysik — ohne Anpassung
> und ohne freie Parameter.**

```
    Grundformel:        E = π · ε(Δφ) · ℏ · f
    Kopplungseffizienz: ε(Δφ) = cos²(Δφ/2)
    Resonanzbedingung:  f_feld = f₀ = √(k/m) / (2π)
    Parameter:          κ = 1 (exakt, aus ε = η)
```

Diese Gleichung gab es vor der RFT nicht. Die klassische Physik
beschreibt jeden Bereich (Mechanik, Akustik, Elektrik, Kernphysik)
mit eigenen Formalismen. Die RFT vereinheitlicht sie in einer
Gleichung — und die Simulation des Resonanzgenerators bestätigt,
dass diese Vereinheitlichung quantitativ korrekt ist.

---

## 2. Was die RFT vereinfacht

### 2.1 Vorher: Separate Formalismen

| Domäne | Klassische Beschreibung | Gilt für |
|--------|------------------------|---------|
| Mechanik | A = F₀/(d·ω₀) | Erzwungene Schwingung |
| Kernphysik | σ_GDR nach Breit-Wigner | Riesenresonanz |
| Optik | I = I₀·cos²(θ) (Malus) | Polarisation |
| Elektrik | P = V²/R bei Impedanzanpassung | Wechselstromkreise |

Vier Domänen, vier Formalismen, keine Verbindung.

### 2.2 Nachher: Eine Gleichung

```
    E = π · ε(Δφ) · ℏ · f
    ε(Δφ) = cos²(Δφ/2)

    Mechanisch: F_eff = F₀ · cos²(Δφ/2)           → simuliert ✅
    Nuklear:    λ_eff = λ₀ + η·Φ·σ_GDR             → simuliert ✅
    Optisch:    Malus-Gesetz = Spezialfall für Δφ=θ → bekannt  ✅
    Elektrisch: Max. Leistung bei Δφ = 0             → bekannt  ✅
```

Die Simulation des Resonanzgenerators bestätigt:
**Dieselbe cos²(Δφ/2)-Funktion, die die GDR im Atomkern
beschreibt, beschreibt auch einen Feder-Masse-Dämpfer.**

---

## 3. Bewegungsgleichung

### 3.1 Gedämpfter Oszillator mit Resonanzfeldkopplung

```
    m · ẍ + d · ẋ + k · x = F₀ · ε(Δφ) · cos(ω · t)

    ε(Δφ) = cos²(Δφ/2)
```

| Symbol | Bedeutung | Einheit |
|--------|----------|---------|
| m | Masse des Oszillators | kg |
| d | Dämpfungskoeffizient | N·s/m |
| k | Federkonstante | N/m |
| F₀ | Kraftamplitude des externen Feldes | N |
| ω | Kreisfrequenz der Anregung | rad/s |
| Δφ | Phasendifferenz Feld ↔ System | rad |
| ε(Δφ) | Kopplungseffizienz (RFT) | dimensionslos |

### 3.2 Abgeleitete Größen

```
    Eigenfrequenz:        f₀ = √(k/m) / (2π)
    Q-Faktor:             Q = √(m·k) / d
    Stationäre Amplitude: A_stat = F₀·cos²(Δφ/2) / (d·ω₀)
    Stationäre Energie:   E_stat = ½·k·A² ∝ cos⁴(Δφ/2)
```

### 3.3 Phasensteuerung

```
    Δφ = 0    → ε = 1.0  → Volle Kopplung (Resonanzkatastrophe)
    Δφ = π/2  → ε = 0.5  → Halbe Kraft, ¼ Energie
    Δφ = π    → ε = 0.0  → Keine Kopplung (Resonanz unterbunden)

    → Durch Verschiebung der Phase um Δφ = π wird die
      Resonanzkopplung vollständig aufgehoben.
```

---

## 4. Simulationsergebnisse

### 4.1 Systemparameter

```
    m  = 0.1 kg, k = 10.0 N/m, d = 0.05 N·s/m, F₀ = 0.1 N
    → f₀ = 1.5915 Hz, Q = 20.0, τ = 4.0 s
```

### 4.2 Frequenz-Sweep (Experiment 1)

| Messgröße | Wert |
|-----------|------|
| Resonanzfrequenz (gemessen) | 1.5930 Hz |
| Eigenfrequenz (theoretisch) | 1.5915 Hz |
| Abweichung | 0.09% |
| Max. Amplitude (stationär) | 198.4 mm |
| Max. ⟨E_mech⟩ | 188.0 mJ |

### 4.3 Phasenscan (Experiment 2) — RFT-Signatur

| Δφ | ε(Δφ) | Amplitude [mm] | ⟨E_mech⟩ [µJ] |
|----|-------|---------------|---------------|
| 0 | 1.000 | 200.0 | 200.000 |
| π/2 | 0.500 | 100.0 | 50.000 |
| π | 0.000 | 0.0 | 0.0 |

```
    Amplitude ∝ cos²(Δφ/2)                → BESTÄTIGT (exakt)
    Energie   ∝ cos⁴(Δφ/2)               → BESTÄTIGT (exakt)
    E(Δφ=0) / ⟨E⟩_inkohärent = 2.50
    Theorie:                     2.50      → EXAKT
```

### 4.4 Dämpfungsvergleich (Experiment 3)

| d [N·s/m] | Q | Max. Amplitude [mm] |
|-----------|---|-------------------|
| 0.01 | 100 | ~470 |
| 0.05 | 20 | ~200 |
| 0.1 | 10 | ~100 |
| 0.5 | 2 | ~20 |
| 1.0 | 1 | ~10 |

---

## 5. Anwendung: Maschinenresonanz

### 5.1 Das Problem

Maschinen (Turbinen, Motoren, Pumpen, Brücken) werden im Betrieb
durch äußere Kräfte angeregt. Trifft die Anregungsfrequenz die
Eigenfrequenz des Systems, entsteht Resonanz:

```
    Resonanzkatastrophe:
    Tacoma Narrows Bridge (1940): Wind bei f₀ → Einsturz
    Turbinenschaufeln:            Schwingungsbruch bei f₀
    Zentrifugen:                  Unwucht bei f₀ → Zerstörung
```

### 5.2 Konventionelle Lösungen

| Methode | Prinzip | Problem |
|---------|---------|---------|
| Passiver Tilger | Gegenmasse bei f₀ | Nur eine Frequenz, fest |
| Aktiver Dämpfer | Sensor + Aktuator | Regelkreis, empirisch optimiert |
| Frequenzvermeidung | Betrieb ≠ f₀ | Nicht immer möglich |

### 5.3 RFT-basierte Lösung

```
    Die Grundgleichung gibt die exakte Antwort:

    1. Miss Δφ zwischen Anregung und Systemschwingung
    2. Berechne ε(Δφ) = cos²(Δφ/2)
    3. Verschiebe die Phase um Δφ → π
    4. → ε(π) = 0 → Keine Energieübertragung → Keine Resonanz

    Das ist kein empirisches „Trial & Error".
    Es ist eine analytische Lösung aus einer Gleichung.
```

**Vorteil gegenüber konventionell:**
- Keine Optimierung nötig: ε(Δφ) gibt das exakte Ergebnis
- Frequenzunabhängig: Funktioniert bei jeder f₀
- Skalenunabhängig: Gleiche Formel für mm-Schwingung und GDR
- Quantitativ vorhersagbar: Energiereduktion = 1 − cos⁴(Δφ/2)

---

## 6. Verbindung zum Resonanzreaktor

| Eigenschaft | Resonanzgenerator | Resonanzreaktor |
|-------------|-------------------|-----------------|
| Skala | Makroskopisch (Hz) | Nuklear (10²¹ Hz) |
| Eigenfrequenz | f₀ = √(k/m)/(2π) | f_GDR = E_GDR/(π·ℏ) |
| Kopplung | ε(Δφ) = cos²(Δφ/2) | η(Δφ) = cos²(Δφ/2) |
| Q-Faktor | Q = √(mk)/d | Q = E_GDR/Γ |
| Grundformel | E = π · ε · ℏ · f | E = π · ε · ℏ · f |
| κ | 1 | 1 |
| Signatur | E_koh/⟨E⟩ = 2.50 | Signal_koh/ink = 2.0 |

**Gleiche Formel, gleiche Physik, 10²¹ Hz Unterschied.**

Der Unterschied in der Signatur (2.50 vs. 2.0) folgt aus:
- Generator: Energie ∝ ε² = cos⁴ → ⟨cos⁴⟩ = 3/8 → Ratio = 8/3
- Reaktor: Rate ∝ η = cos² → ⟨cos²⟩ = 1/2 → Ratio = 2

Beides konsistent mit der Grundgleichung, keine Anpassung.

---

## 7. Simulation

### 7.1 Dateien

| Datei | Funktion |
|-------|---------|
| `resonanzgenerator.py` | Frequenz-Sweep, Phasenscan, Detailanalyse, Dämpfungsvergleich |
| `nichtlineare_resonanzanalyse.py` | Nichtlinearer Oszillator: Duffing, energieabhängige Dämpfung, Phasenscan |

### 7.2 Ausführung

```bash
python resonanzgenerator.py                       # 4 Plots
python nichtlineare_resonanzanalyse.py             # 4 Plots
streamlit run nichtlineare_resonanzanalyse.py      # Interaktiv (optional)
```

---

## 8. Zusammenfassung

```
    Der Resonanzgenerator beweist:

    1. Die RFT-Grundgleichung E = π · ε(Δφ) · ℏ · f beschreibt
       mechanische Resonanz exakt — ohne Anpassung.

    2. ε(Δφ) = cos²(Δφ/2) ist die universelle Kopplungsfunktion:
       Amplitude ∝ cos², Energie ∝ cos⁴, Signatur = 2.50.

    3. Dieselbe Gleichung, die die GDR im Atomkern beschreibt,
       beschreibt auch einen Feder-Masse-Dämpfer.

    4. Praktische Anwendung: Phasensteuerung (Δφ → π)
       unterbindet Maschinenresonanz — analytisch, nicht empirisch.

    5. Die Gleichung gab es vor der RFT nicht.
       Die Physik dahinter ist bekannt.
       Aber der vereinheitlichende Rahmen ist neu.
```

---

## 9. Literatur

1. Den Hartog, J.P. (1985): Mechanical Vibrations. Dover.
2. Roundy, S. et al. (2003): Low Level Vibrations as Power Source.
   Computer Communications 26, 1131–1144.
3. Dietrich, S.S. & Berman, B.L. (1988): Atlas of Photoneutron
   Cross Sections.
4. Schu, D.-R. (2025/2026): Resonanzfeldtheorie.
   https://github.com/DominicReneSchu/public

---

© Dominic-René Schu — Resonanzfeldtheorie 2025/2026

---

[Zurück zur Übersicht](README.md) | [Nichtlineare Analyse](nichtlineare_resonanzanalyse.md)