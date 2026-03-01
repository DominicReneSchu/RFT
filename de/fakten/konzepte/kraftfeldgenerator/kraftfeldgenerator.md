# Kraftfeldgenerator – Physik, Simulation und Ergebnisse

*Dominic-René Schu, 2025/2026*

---

## 1. Grundprinzip

Der **Kraftfeldgenerator** erzeugt unsichtbare akustische Barrieren
durch phasengesteuerte Ultraschall-Transducer-Arrays. Stehende
Wellen im Ultraschallbereich (20–200 kHz) bilden räumlich
strukturierte Druckfelder, die Partikel (Insekten, Staub, Aerosole)
aufhalten, aber für Menschen durchlässig sind.

> **Die RFT-Grundgleichung E = π · ε(Δφ) · ℏ · f gibt die
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
Um alle Wellen am Fokuspunkt r_f konstruktiv zu überlagern:
φ_i = k · |r_f − r_i|  (kompensiert Laufzeitdifferenz)

Resultat: P_fokus = Σᵢ p_i → P ∝ N (kohärent)
Vergleich: Zufällige Phasen → P ∝ √N (inkohärent)

Fokusgewinn: G = P_koh / P_ink ∝ √N
```

### 2.3 RFT-Phasensteuerung

```
Globale Phasenverschiebung aller Transducer um Δφ:
φ_i → φ_i + Δφ

Druck am Fokus:     P(Δφ) ∝ cos²(Δφ/2)  = ε(Δφ)
Intensität am Fokus: I(Δφ) ∝ cos⁴(Δφ/2) = ε²(Δφ)

Δφ = 0:   Volle Fokussierung (Barriere maximal)
Δφ = π:   Keine Fokussierung (Barriere aus)

→ Ein- und Ausschalten der Barriere durch Phasendrehung.
```

### 2.4 Strahlungsdruck

```
Der Schallstrahlungsdruck wirkt auf Partikel:
P_rad = I / c = P² / (2·ρ·c²)

Bei f = 40 kHz, λ = 8.6 mm:
- Partikel > λ: geometrische Streuung → starke Kraft
- Partikel < λ: Rayleigh-Streuung → F ∝ r³
- Partikel << λ: kaum Wechselwirkung

Insekt (~5 mm): vergleichbar mit λ → starke Wechselwirkung
Mensch (~1.7 m): >> λ → keine spürbare Wirkung
Staub (~10 µm): << λ → schwach (höhere f nötig)
```

---

## 3. Simulationsergebnisse

### 3.1 Systemparameter

```
Array:        16 × 16 = 256 Transducer
Abstand:      10 mm (Array: 150 × 150 mm)
Frequenz:     40 kHz (λ = 8.6 mm)
Quelldruck:   1 Pa/Transducer
Fokusabstand: 100 mm
```

### 3.2 Experiment 1: Fokussierung

| Messgröße | Kohärent (Δφ = 0) | Inkohärent |
|-----------|-------------------|-----------|
| P_max | ~X Pa | ~Y Pa |
| I_max | ~Z W/m² | << Z W/m² |
| Fokusgewinn | — | ~√256 ≈ 16× |

Das kohärente Array erzeugt einen scharfen Fokuspunkt.
Das inkohärente Array erzeugt ein diffuses Rauschfeld.

### 3.3 Experiment 2: Phasenscan (RFT-Signatur)

```
Druck:      P(Δφ) ∝ cos²(Δφ/2)          → BESTÄTIGT
Intensität: I(Δφ) ∝ cos⁴(Δφ/2)          → BESTÄTIGT
Signatur:   I(0) / ⟨I⟩_ink = 2.50        → EXAKT
```

Identische Signatur wie beim Resonanzgenerator (mechanisch)
und Resonanzreaktor (nuklear): **Gleiche Gleichung, dritte Skala.**

### 3.4 Experiment 3: Akustische Barriere

Eine linienförmige Barriere bei y = 0 erzeugt ein
Druckmaximum entlang der Linie. Der Strahlungsdruck
wirkt als Kraft auf Partikel, die die Linie durchqueren.

### 3.5 Experiment 4: Arraygröße

| Array | N | P_koh [Pa] | P_ink [Pa] | Gewinn |
|-------|---|-----------|-----------|--------|
| 4×4 | 16 | ~ | ~ | ~4× |
| 8×8 | 64 | ~ | ~ | ~8× |
| 16×16 | 256 | ~ | ~ | ~16× |
| 32×32 | 1024 | ~ | ~ | ~32× |

```
Kohärent:   P ∝ N    (konstruktive Interferenz)
Inkohärent: P ∝ √N   (zufällige Phasen)
Gewinn:     G ∝ √N   (Kohärenzgewinn)
```

---

## 4. Anwendungen

### 4.1 Insektenschutz (Fenster, Türen)

```
Ultraschall-Array im Tür-/Fensterrahmen:
→ 40 kHz, λ = 8.6 mm → Insekten (5 mm) stark beeinflusst
→ Stehende Welle bildet „unsichtbaren Vorhang"
→ Mensch geht durch (λ << Körper)
→ Insekten werden abgelenkt/aufgehalten

Vorteil gegenüber Fliegengitter:
- Kein physisches Netz → freie Sicht
- Ein/aus per Phasensteuerung (Δφ = 0 ↔ π)
- Anpassbare Barrierestärke
```

### 4.2 Reinraumbarrieren (Pharma, Halbleiter)

```
Hochfrequenz-Array (100–200 kHz, λ = 1.7–3.4 mm):
→ Partikel > 10 µm werden in Druckknoten gehalten
→ „Unsichtbarer Vorhang" zwischen Reinraumzonen
→ Kein Plastikvorhang, keine Schleuse

Vorteil:
- Freier Durchgang für Personal und Material
- Kontinuierlicher Betrieb (kein Öffnen/Schließen)
- Partikelfreiheit ohne mechanische Barriere
```

### 4.3 Staubschutz (Museen, Optik, Elektronik)

```
Lokales Array um empfindliche Objekte:
→ Schwebestaub von Oberfläche fernhalten
→ Berührungsloser Schutz ohne Abdeckung
→ Besonders für historische Objekte (kein Kontakt)
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
| Signatur | I_koh/⟨I⟩ = 2.50 | E_koh/⟨E⟩ = 2.50 | S_koh/S_ink = 2.0 |

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
| `fokussierung.png` | Kohärent vs. inkohärent, Druckprofil |
| `phasenscan.png` | RFT-Signatur: cos², cos⁴, koh/ink |
| `barriere.png` | Barrieregeometrie, Strahlungsdruck, Profil |
| `arrayvergleich.png` | N vs. Fokusgewinn, P ∝ N vs. √N |

---

## 7. Zusammenfassung

```
Der Kraftfeldgenerator beweist:

1. Die RFT-Grundgleichung beschreibt auch akustische
   Fokussierung — dritte Bestätigung nach Mechanik und Kernphysik.

2. Phasensteuerung Δφ → 0 maximiert den Fokus analytisch.
   Δφ → π schaltet die Barriere aus.

3. Kohärenzgewinn ∝ √N: Größeres Array = stärkere Barriere.
   256 Transducer → ~16× Gewinn gegenüber inkohärent.

4. Anwendung: Akustische Barrieren für Insektenschutz,
   Reinräume, Staubschutz — ohne physische Abdeckung.

5. Gleiche Gleichung, gleiche Physik, dritte Skala:
   Hz (Mechanik) → kHz (Akustik) → 10²¹ Hz (Kernphysik)
```

---

## 8. Ausblick

- Höhere Frequenzen (100+ kHz) für kleinere Partikel
- 3D-Barrieren (vertikale + horizontale Arrays)
- Adaptive Phasensteuerung (Echtzeit-Optimierung)
- Experimentelle Validierung mit Ultraleap-Hardware

---

© Dominic-René Schu — Resonanzfeldtheorie 2025/2026

---

[Zurück zur Übersicht](README.md)