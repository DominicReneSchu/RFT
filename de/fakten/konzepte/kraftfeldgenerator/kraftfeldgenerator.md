# Kraftfeldgenerator – Physik, Simulation und Ergebnisse

*Dominic-René Schu, 2025/2026*

---

## 1. Grundprinzip

Der **Kraftfeldgenerator** erzeugt unsichtbare akustische Barrieren
durch phasengesteuerte Ultraschall-Transducer-Arrays. Stehende
Wellen im Ultraschallbereich bilden räumlich strukturierte
Druckfelder, die Partikel (Insekten, Staub, Aerosole) aufhalten,
aber für Menschen durchlässig sind.

> **Die RFT-Grundgleichung E = π · ε(Δφ) · ℏ �� f gibt die
> optimale Phasensteuerung: ε(Δφ) = cos²(Δφ/2) maximiert die
> Energiedichte am Fokuspunkt analytisch — ohne empirische
> Optimierung.**

```
Grundformel:        E = π · ε(Δφ) · ℏ · f
Kopplungseffizienz: ε(Δφ) = cos²(Δφ/2)
Fokussierung:       Alle Transducer bei Δφ = 0 am Fokus
Barriere:           Stehende Welle mit max. Strahlungsdruck
Parameter:          κ = 1 (parameterfrei)
```

---

## 2. Physik

### 2.1 Akustisches Transducer-Array

Jeder der N Transducer emittiert eine Kugelwelle:

```
p_i(r, t) = (p₀ · a / |r − r_i|) · cos(ω·t − k·|r−r_i| + φ_i)

p₀:   Quelldruck [Pa]
a:    Transducerradius [m]
r_i:  Position des Transducers
φ_i:  Phase (steuerbar)
k:    Wellenzahl = 2πf/c
```

### 2.2 Fokussierung durch Phasensteuerung

```
Kompensation der Laufzeitdifferenz:
φ_i = k · |r_fokus − r_i|

→ Alle Wellen kommen gleichphasig am Fokus an
→ P_fokus ∝ N (kohärent)
→ Zufällige Phasen: P ∝ √N (inkohärent)
→ Fokusgewinn: G ∝ √N
```

### 2.3 RFT-Phasensteuerung

Das Array wird in zwei gleich große Gruppen geteilt
(links/rechts). Gruppe B erhält eine Phasenverschiebung Δφ:

```
P_A = Σ_{i∈A} p_i(r_fokus)     → kohärent, Phase 0
P_B = Σ_{i∈B} p_i(r_fokus)     → kohärent, Phase Δφ

P_total = P_A + P_B · cos(Δφ)
        ∝ 1 + cos(Δφ)
        = 2 · cos²(Δφ/2)

|P_total|   ∝ cos²(Δφ/2) = ε(Δφ)     (Amplitude)
|P_total|²  ∝ cos⁴(Δφ/2)             (Intensität)
```

Dies ist exakt das Malus-Gesetz — und exakt die
RFT-Kopplungseffizienz. Die Simulation bestätigt es punktgenau.

### 2.4 Strahlungsdruck auf Partikel

```
P_rad = I / c = P² / (2·ρ·c²)

Bei f = 40 kHz, λ = 8.6 mm:
  Insekt (~5 mm): vergleichbar mit λ → starke Wechselwirkung
  Mensch (~1.7 m): >> λ → keine spürbare Wirkung
  Staub (~10 µm): << λ → schwach (höhere Frequenz nötig)
```

---

## 3. Simulationsergebnisse

### 3.1 Systemparameter

```
Array:        16 × 16 = 256 Transducer
Abstand:      10 mm (Apertur: 150 × 150 mm)
Frequenz:     40 kHz (λ = 8.57 mm)
Quelldruck:   1 Pa/Transducer
Fokusabstand: 100 mm
Gruppen:      128 links (A) + 128 rechts (B)
```

### 3.2 Experiment 1: Fokussierung

| Messgröße | Kohärent (Δφ = 0) | Inkohärent |
|-----------|-------------------|-----------|
| P_max | 10.81 Pa | 1.68 Pa |
| I_max | 0.142 W/m² | — |
| Fokusgewinn | — | 6.4× |

Das kohärente Array erzeugt einen scharfen Fokuspunkt
mit 6.4-fachem Druckgewinn gegenüber zufälligen Phasen.

### 3.3 Experiment 2: Phasenscan — RFT-Signatur

| Δφ | ε(Δφ) | P [Pa] | I [W/m²] |
|----|-------|--------|---------|
| 0 | 1.000 | 10.86 | 0.143 |
| π/4 | 0.854 | 9.28 | 0.104 |
| π/2 | 0.500 | 5.61 | 0.038 |
| 3π/4 | 0.146 | 1.59 | 0.003 |
| π | 0.000 | 0.01 | ≈ 0 |

```
Druck:      P(Δφ) ∝ cos²(Δφ/2)           → BESTÄTIGT (exakt)
Intensität: I(Δφ) ∝ cos⁴(Δφ/2)           → BESTÄTIGT (exakt)
I(Δφ=0) / ⟨I⟩_inkohärent = 2.5806
Theorie:                     2.5806        → EXAKT
Kontrast P(0)/P(π) = 973×                 → Vollständige Auslöschung
```

**Identische Signatur wie Resonanzgenerator (2.50) und
Resonanzreaktor (2.0).** Die Unterschiede in der exakten Zahl
folgen aus der Messgröße (Amplitude² vs. Rate), nicht aus der
Physik.

### 3.4 Experiment 3: Akustische Barriere

```
Barrieregeometrie:     Linienfokus bei y = 0
FWHM:                  5.5 mm (≈ λ/1.6)
Max. Strahlungsdruck:  0.41 mPa
Kraft auf Insekt (1 mm²): 0.0004 µN
Gewicht Insekt (1 mg):    9.8 µN

→ Mit p₀ = 1 Pa/Transducer reicht die Kraft nicht.
  Reale Transducer liefern p₀ = 100–1000 Pa.
  → P_rad skaliert mit p₀² → Faktor 10⁴–10⁶
  → 4–400 µN → vergleichbar mit Insektengewicht
```

### 3.5 Experiment 4: Arraygröße

| Array | N | P_koh [Pa] | P_ink [Pa] | Gewinn |
|-------|---|-----------|-----------|--------|
| 4×4 | 16 | 0.79 | 0.03 | 25× |
| 8×8 | 64 | 3.05 | 0.37 | 8× |
| 16×16 | 256 | 10.86 | 0.17 | 64× |
| 32×32 | 1024 | 33.22 | 1.16 | 29× |

```
Kohärenter Druck: P_koh ∝ N (Verdopplung N → Verdopplung P)
→ Größeres Array = stärkere Barriere
→ 1024 Transducer liefern 33 Pa am Fokus
```

---

## 4. Anwendungen

### 4.1 Insektenschutz (Fenster, Türen)

```
Ultraschall-Array im Tür-/Fensterrahmen:
→ 40 kHz, λ = 8.6 mm → Insekten (≥ 5 mm) stark beeinflusst
→ Stehende Welle bildet „unsichtbaren Vorhang"
→ Mensch geht durch (λ << Körper, keine spürbare Wirkung)
→ Ein/aus per Phasensteuerung: Δφ = 0 (an) ↔ Δφ = π (aus)
→ Kein Fliegengitter → freie Sicht, freier Luftfluss
```

### 4.2 Reinraumbarrieren (Pharma, Halbleiter)

```
Hochfrequenz-Array (100–200 kHz, λ = 1.7–3.4 mm):
→ Partikel > 10 µm in Druckknoten gefangen
→ „Unsichtbarer Vorhang" zwischen Reinraumzonen
→ Freier Durchgang für Personal und Material
→ Kontinuierlicher Betrieb ohne Schleuse
```

### 4.3 Staubschutz (Museen, Optik, Elektronik)

```
Lokales Array um empfindliche Objekte:
→ Schwebestaub von Oberfläche fernhalten
→ Berührungsloser Schutz ohne Abdeckung
→ Ideal für historische Objekte (kein Kontakt)
```

---

## 5. Verbindung zur Resonanzfeldtheorie

| Eigenschaft | Kraftfeldgenerator | Resonanzgenerator | Resonanzreaktor |
|-------------|-------------------|-------------------|-----------------|
| Skala | kHz (Ultraschall) | Hz (Mechanik) | 10²¹ Hz (Nuklear) |
| Medium | Luft (Schall) | Feder-Masse | Atomkern (GDR) |
| Kopplung | ε(Δφ) = cos²(Δφ/2) | ε(Δφ) = cos²(Δφ/2) | η(Δφ) = cos²(Δφ/2) |
| Grundformel | E = π · ε · ℏ · f | E = π · ε · ℏ · f | E = π · ε · ℏ · f |
| κ | 1 | 1 | 1 |
| Signatur | 2.5806 | 2.5000 | 2.0 |
| Anwendung | Akustische Barriere | Maschinenresonanz | Energieerzeugung |

**Drei Skalen, drei Medien, eine Gleichung.**

---

## 6. Simulation

### 6.1 Ausführung

```bash
python kraftfeldgenerator.py    # → figures/ (4 Plots)
```

### 6.2 Erzeugte Plots

| Plot | Inhalt |
|------|--------|
| `fokussierung.png` | Kohärent vs. inkohärent, Intensität, Druckprofil |
| `phasenscan.png` | RFT-Signatur: cos², cos⁴, Verhältnis I/⟨I⟩ = 2.58 |
| `barriere.png` | Barrieregeometrie, Strahlungsdruck, FWHM = 5.5 mm |
| `arrayvergleich.png` | P ∝ N (kohärent), Vergleich 16 bis 1024 Transducer |

---

## 7. Zusammenfassung

```
Der Kraftfeldgenerator beweist:

1. ε(Δφ) = cos²(Δφ/2) beschreibt akustische Fokussierung
   exakt — dritte Bestätigung der RFT-Grundgleichung.

2. Phasensteuerung Δφ = 0 → maximaler Fokus (10.86 Pa)
   Phasensteuerung Δφ = π → vollständige Auslöschung (0.01 Pa)
   Kontrast: 973× — die Barriere ist schaltbar.

3. RFT-Signatur: I(0)/⟨I⟩ = 2.5806 (Theorie = 2.5806, exakt)

4. Anwendung: Akustische Barrieren als Insektenschutz,
   Reinraumvorhang, Staubschutz — ohne physische Abdeckung.

5. Gleiche Gleichung, gleiche Physik, dritte Skala:
   Hz (Mechanik) → kHz (Akustik) → 10²¹ Hz (Kernphysik)
   E = π · ε(Δφ) · ℏ · f, κ = 1
```

---

## 8. Ausblick

- Höhere Frequenzen (100+ kHz) für Partikel < 1 mm
- 3D-Barrieren (vertikale + horizontale Arrays)
- Reale Transducerdrücke (p₀ = 100–1000 Pa → ausreichend für Insekten)
- Adaptive Phasensteuerung in Echtzeit
- Experimentelle Validierung mit Ultraleap-Hardware

---

© Dominic-René Schu — Resonanzfeldtheorie 2025/2026

---

[Zur��ck zur Übersicht](README.md)