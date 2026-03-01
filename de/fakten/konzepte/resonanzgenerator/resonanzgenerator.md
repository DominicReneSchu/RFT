# Resonanzgenerator – Physik, Simulation und Ergebnisse

*Dominic-René Schu, 2025/2026*

---

## 1. Grundprinzip

Der **Resonanzgenerator** ist ein mechanisches System, das durch
kohärente Kopplung an ein externes Schwingungsfeld Energie
hocheffizient aufnimmt. Er demonstriert die zentrale Vorhersage
der Resonanzfeldtheorie (RFT): Die Kopplungseffizienz zwischen
Feld und System ist keine Konstante, sondern folgt der
universellen Funktion ε(Δφ) = cos²(Δφ/2).

```
    Grundformel:        E = π · ε(Δφ) · ℏ · f
    Kopplungseffizienz: ε(Δφ) = cos²(Δφ/2)
    Resonanzbedingung:  f_feld = f₀ = √(k/m) / (2π)
    Parameter:          κ = 1 (exakt, aus ε = η)
```

---

## 2. Bewegungsgleichung

### 2.1 Gedämpfter Oszillator mit Resonanzfeldkopplung

```
    m · ẍ + d · ẋ + k · x = F_feld(t, Δφ)

    wobei:
    F_feld(t, Δφ) = F₀ · ε(Δφ) · cos(ω · t)
    ε(Δφ)         = cos²(Δφ/2)
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

### 2.2 Abgeleitete Größen

```
    Eigenfrequenz:       f₀ = ω₀/(2π) = √(k/m) / (2π)
    Eigenkreisfrequenz:  ω₀ = √(k/m)
    Q-Faktor:            Q = √(m·k) / d
    Abklingzeit:         τ = 2m/d
    Stationäre Amplitude: A_stat = F₀·ε / (d·ω₀) = F₀·cos²(Δφ/2)/(d·ω₀)
    Stationäre Energie:  E_stat = ½·k·A_stat² ∝ ε² = cos⁴(Δφ/2)
```

### 2.3 Energiebilanz

```
    Kinetische Energie:  E_kin(t) = ½ m ẋ²
    Potenzielle Energie: E_pot(t) = ½ k x²
    Feldarbeit:          W_feld(t) = ∫₀ᵗ F_feld(t') · ẋ(t') dt'
    Dissipation:         W_diss(t) = ∫₀ᵗ d · ẋ(t')² dt'
    Bilanz:              W_feld = (E_kin + E_pot) + W_diss
    Wirkungsgrad:        η_mech = ⟨E_kin + E_pot⟩ / W_feld
```

---

## 3. Simulationsergebnisse

### 3.1 Systemparameter

```
    m  = 0.1 kg         (Masse)
    k  = 10.0 N/m       (Federkonstante)
    d  = 0.05 N·s/m     (Dämpfung)
    F₀ = 0.1 N          (Kraftamplitude)

    → f₀ = 1.5915 Hz
    → ω₀ = 10.0 rad/s
    → Q  = 20.0
    → τ  = 4.0 s
```

### 3.2 Experiment 1: Frequenz-Sweep (Δφ = 0)

200 Frequenzen im Bereich 0.5–15 Hz, Simulationszeit 20 s, Start aus Ruhe.

| Messgröße | Wert |
|-----------|------|
| Resonanzfrequenz (gemessen) | 1.5930 Hz |
| Eigenfrequenz (theoretisch) | 1.5915 Hz |
| Abweichung | 0.09% |
| Max. Amplitude (stationär) | 198.4 mm |
| Max. ⟨E_mech⟩ | 188.0 mJ |
| Kumulierte Feldarbeit | 1597 mJ |
| P_in (theoretisch, Resonanz) | 100 mW |
| Q-Faktor (theoretisch) | 20.0 |

**Ergebnis:** Die gemessene Resonanzfrequenz stimmt auf 0.09%
mit dem theoretischen Wert überein. Der Resonanzpeak ist scharf
(Q = 20) und dominiert die Energieaufnahme.

### 3.3 Experiment 2: Phasenscan (f = f₀)

50 Phasen im Bereich Δφ ∈ [0, 2π], bei exakter Resonanzfrequenz.

| Δφ | ε(Δφ) | Amplitude [mm] | ⟨E_mech⟩ [µJ] |
|----|-------|---------------|---------------|
| 0 (Resonanz) | 1.000 | 198.6 | 188.220 |
| π/4 | 0.854 | 169.6 | 137.303 |
| π/2 | 0.500 | 102.5 | 50.120 |
| 3π/4 | 0.146 | 29.0 | 4.014 |
| π (Anti) | 0.000 | 0.2 | 0.2 |

**RFT-Signatur:**

```
    Amplitude ∝ ε(Δφ) = cos²(Δφ/2)           → BESTÄTIGT
    Energie   ∝ ε²(Δφ) = cos⁴(Δφ/2)          → BESTÄTIGT
    E(Δφ=0) / ⟨E⟩_inkohärent = 2.5806
    Theorie (cos⁴ / ⟨cos⁴⟩):   2.5806         → EXAKT
```

Die Simulation reproduziert die theoretische cos²-Abhängigkeit
punktgenau. Das Verhältnis kohärent/inkohärent ist 2.58 — nicht
2.0 wie beim Resonanzreaktor, weil hier die Energie ∝ ε² ∝ cos⁴
geht (Amplitude quadratisch in der Energie).

### 3.4 Experiment 3: Detailanalyse am Resonanzpunkt

```
    Zeitsignal:   Amplitude wächst exponentiell bis t ≈ 4τ = 8 s
                  Danach stationärer Zustand (Energiezufuhr = Dissipation)
    Phasenraum:   Saubere Ellipse (stationär), konsistent mit Q = 20
    FFT:          Dominanter Peak bei f₀ = 1.59 Hz, keine Obertöne
                  → Lineares System, kohärente Kopplung
    Energieverlauf: W_feld wächst linear (stationäre Leistung)
                    E_mech sättigt bei ~188 mJ
```

### 3.5 Experiment 4: Dämpfungsvergleich

| d [N·s/m] | Q | Max. Amplitude [mm] | Charakteristik |
|-----------|---|-------------------|----------------|
| 0.01 | 100 | ~470 | Sehr scharf, langsames Einschwingen |
| 0.05 | 20 | ~200 | Standard (Referenz) |
| 0.1 | 10 | ~100 | Mäßig scharf |
| 0.5 | 2 | ~20 | Breit, schnell stationär |
| 1.0 | 1 | ~10 | Überkritisch, fast kein Peak |

**Erkenntnis:** Die Amplitude bei Resonanz skaliert mit 1/d
(stationär: A = F₀/(d·ω₀)). Der Q-Faktor bestimmt die
Selektivität der Frequenzkopplung — identisch zum nuklearen
Fall (GDR-Breite Γ ~ 1/Q).

---

## 4. Verbindung zum Resonanzreaktor

| Eigenschaft | Resonanzgenerator | Resonanzreaktor |
|-------------|-------------------|-----------------|
| Skala | Makroskopisch (Hz) | Nuklear (10²¹ Hz) |
| Eigenfrequenz | f₀ = √(k/m)/(2π) | f_GDR = E_GDR/(π·ℏ) |
| Anregung | Mechanische Kraft F₀·cos(ωt) | Photonenfluss Φ_γ bei E_GDR |
| Kopplung | ε(Δφ) = cos²(Δφ/2) | η(Δφ) = cos²(Δφ/2) |
| Dämpfung / Breite | d → Q = √(mk)/d | Γ_GDR → Q = E_GDR/Γ |
| Amplitude ∝ | F₀·ε/(d·ω₀) | Φ·σ_GDR·η |
| Energie ∝ | ε² = cos⁴(Δφ/2) | η (linear, da Rate × Einzelenergie) |
| Phasensignatur | E_koh/⟨E⟩ = 2.58 | Signal_koh/Signal_ink = 2.0 |
| κ | 1 | 1 |

**Gleiche Grundformel, gleiche Kopplungsfunktion, verschiedene Skalen.**

Der Unterschied im Verhältnis (2.58 vs. 2.0) kommt daher, dass
beim Generator die messbare Energie ∝ Amplitude² ∝ ε² geht,
während beim Reaktor die messbare Rate ∝ η (linear) geht.

---

## 5. Physikalische Interpretation

### 5.1 Was Resonanz physikalisch bedeutet

Die Simulation bestätigt quantitativ:

1. **Resonanz ist kein Zufall, sondern Bedingung.** Der Peak bei
   f₀ ist scharf und reproduzierbar — das System „wählt"
   selektiv die Eigenfrequenz aus dem Anregungsspektrum.

2. **Phasenkohärenz bestimmt den Energietransfer.** Ein kohärentes
   Feld (Δφ = 0) überträgt die volle Energie. Ein inkohärentes
   Feld (zufälliges Δφ) überträgt im Mittel nur 3/8 der Energie
   (⟨cos⁴⟩ = 3/8).

3. **Der Q-Faktor ist das Gütemaß.** Hoher Q-Faktor bedeutet:
   schmale Bandbreite, hohe Selektivität, lange Einschwingzeit.
   Identisch zur GDR-Physik (Γ_GDR = E_GDR/Q_GDR).

### 5.2 Was die RFT hinzufügt

Die klassische Physik des gedämpften Oszillators ist vollständig
verstanden. Die RFT fügt hinzu:

- **ε(Δφ) = cos²(Δφ/2)** als universelle Kopplungsfunktion,
  die auf allen Skalen gilt (makroskopisch → nuklear)
- **κ = 1** als parameterfreie Konsequenz der Identität ε = η
- **Skalenübergreifende Vorhersage:** Dieselbe Gleichung
  E = π · ε · ℏ · f beschreibt sowohl den mechanischen
  Oszillator als auch die GDR des Atomkerns

---

## 6. Anwendungsbereiche

### 6.1 Energy Harvesting

```
    Vibrationsquelle (Gebäude, Brücke, Maschine)
    → Piezo/MEMS-Oszillator bei Eigenfrequenz f₀
    → RFT-optimierte Phasenkopplung: ε → 1
    → Leistung: P ∝ F₀² · cos⁴(Δφ/2) / d
    → Typisch: µW–mW (Sensorversorgung, IoT)
```

### 6.2 Schwingungskompensation mit Energierückgewinnung

```
    Unerwünschte Vibrationen in Strukturen
    → Resonanzgenerator absorbiert bei f₀
    → Energie wird nicht dissipiert, sondern geerntet
    → Doppelter Nutzen: Dämpfung + Stromversorgung
```

### 6.3 Skalierung zur nuklearen Domäne

```
    Makro:   f₀ ~ 1 Hz     → Resonanzgenerator
    Mikro:   f₀ ~ 1 MHz    → MEMS-Harvester
    Nuklear: f₀ ~ 10²¹ Hz  → Resonanzreaktor

    Alle mit: E = π · ε(Δφ) · ℏ · f, κ = 1
```

---

## 7. Simulation

### 7.1 Dateien

| Datei | Funktion |
|-------|---------|
| `resonanzgenerator.py` | Frequenz-Sweep, Phasenscan, Detailanalyse, Dämpfungsvergleich |
| `nichtlineare_resonanzanalyse.py` | Streamlit-App: nichtlinearer Oszillator mit Poincaré, Wavelet |

### 7.2 Ausführung

```bash
# Frequenz-Sweep + Phasenscan (4 Plots)
pip install numpy matplotlib scipy
python resonanzgenerator.py

# Interaktive nichtlineare Analyse
pip install streamlit numpy matplotlib scipy pywt
streamlit run nichtlineare_resonanzanalyse.py
```

### 7.3 Erzeugte Plots

| Plot | Inhalt |
|------|--------|
| `frequenz_sweep.png` | Resonanzkurve, ⟨E_mech⟩, Feldarbeit vs. Frequenz |
| `phasenscan.png` | Amplitude, Energie, RFT-Signatur vs. Δφ |
| `resonanz_detail.png` | Zeitsignal, Energieverlauf, Phasenraum, FFT |
| `daempfung_vergleich.png` | Q = 1...100, Resonanzschärfe vs. Dämpfung |

---

## 8. Literatur

1. Den Hartog, J.P. (1985): Mechanical Vibrations.
   Dover Publications. (Standardwerk gedämpfter Oszillator)

2. Roundy, S. et al. (2003): A Study of Low Level Vibrations
   as a Power Source for Wireless Sensor Nodes.
   Computer Communications 26, 1131–1144. (Energy Harvesting)

3. Dietrich, S.S. & Berman, B.L. (1988): Atlas of Photoneutron
   Cross Sections. (GDR als nukleares Analogon)

4. Schu, D.-R. (2025/2026): Resonanzfeldtheorie.
   https://github.com/DominicReneSchu/public

---

© Dominic-René Schu — Resonanzfeldtheorie 2025/2026

---

[Zurück zur Übersicht](README.md) | [Nichtlineare Analyse](nichtlineare_resonanzanalyse.md)