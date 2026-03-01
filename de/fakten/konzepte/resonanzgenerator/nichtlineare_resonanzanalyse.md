# Nichtlineare Resonanzanalyse – Interaktive Simulation

*Dominic-René Schu, 2025/2026*

---

![Simulation nichtlineare Resonanzfeldanalyse](./nichtlineare_resonanzanalyse.png)

*Abb. 1: Nichtlineare Resonanzanalyse – 6-Panel-Dashboard (Streamlit)*

---

## 1. Überblick

Die nichtlineare Resonanzanalyse erweitert den linearen
Resonanzgenerator um energieabhängige Dämpfung und
frequenzmodulierte Kopplung. Damit werden Phänomene sichtbar,
die im linearen Modell nicht auftreten:

- Chaosübergänge (periodisch → quasiperiodisch → chaotisch)
- Resonanzinseln im Phasenraum
- Breitband-Frequenzspektren bei starker Anregung
- Intermittenz und plötzliche Regimewechsel

Die Simulation ist als interaktive Streamlit-App realisiert.

---

## 2. Physik

### 2.1 Nichtlinearer Oszillator

```
    m · ẍ + d(E) · ẋ + k · x = A_f · cos(ω_f · t · (1 + δt))

    Energieabhängige Dämpfung:
    d(E) = d₀ · exp(−0.1·E) / (1 + 0.05·E² + 0.001·E⁴)

    Frequenzmodulation (Phasenraum-Rückkopplung):
    δt = β · (v/v₀)² · sin(θ)
    θ  = arctan(v/x)
```

### 2.2 Interpretation im RFT-Rahmen

Die nichtlineare Dämpfung d(E) modelliert die energieabhängige
Resonanzeffizienz: Bei hoher Systemenergie wird die Kopplung
schwächer — analog zur Sättigung der GDR bei hohem Photonenfluss.

Die Frequenzmodulation δt modelliert die phasenraumabhängige
Kopplung — die Effektivität der Feldkopplung hängt vom
momentanen Zustand (x, v) des Systems ab.

---

## 3. Visualisierungen

### 3.1 Zeitverlauf x(t)
Periodisch bei schwacher Anregung, chaotisch bei starker.
Amplitude und Frequenz variieren mit den Systemparametern.

### 3.2 Phasenraumdiagramm (x, v)
Geschlossene Ellipsen → periodisch.
Gefüllte Flächen → chaotisch.
Strukturierte Muster → quasiperiodisch (Resonanzinseln).

### 3.3 Poincaré-Schnitt
Stroboskopische Abtastung bei Anregungsphase = 0 (mod 2π).
Einzelpunkte → Periode-1. Inseln → höhere Perioden.
Staubwolke → Chaos.

### 3.4 Frequenzspektrum (FFT)
Einzelner Peak → periodisch. Harmonische → nichtlinear.
Breites Spektrum → chaotisch.

### 3.5 Spektrogramm (STFT)
Zeit-Frequenz-Analyse: Zeigt Übergänge zwischen Regimen.

### 3.6 Wavelet-Skalogramm (Morlet)
Hohe Auflösung für nichtstationäre Phänomene.

---

## 4. Parametersteuerung

| Parameter | Bereich | Beschreibung |
|-----------|---------|-------------|
| A_f | 0.1–5.0 | Anregungsamplitude |
| ω_f | 0.1–5.0 | Anregungsfrequenz |
| d₀ | 0.01–1.0 | Grunddämpfung |
| k | 0.1–5.0 | Federkonstante |
| v₀ | 0.01–5.0 | Normgeschwindigkeit (Rückkopplung) |
| T | 10–500 | Simulationsdauer [s] |

### Optimale Parameter für maximale Energieübertragung

| Parameter | Empfehlung | Begründung |
|-----------|-----------|-----------|
| A_f | 1.0–1.5 | Genügend Energie, aber kein Chaos |
| ω_f | 1.0–1.05 | Nahe Eigenfrequenz ω₀ = √k |
| d₀ | 0.05–0.1 | Unterkritische Dämpfung |
| k | 1.0 | Standard-Eigenfrequenz |

### Anzeichen effektiver Resonanz

- Große, regelmäßige Auslenkungen im Zeitplot
- Hauptpeak im FFT bei der Anregungsfrequenz
- Klare Resonanzinseln im Poincaré-Schnitt
- Hoher Wirkungsgrad η (angezeigt nach Simulation)

---

## 5. Wirkungsgrad

```
    η = ⟨E_mech⟩ / W_in

    E_mech = ½mv² + ½kx²     (mittlere mechanische Energie)
    W_in = ∫ F_feld · v dt    (eingebrachte Feldarbeit)
```

Typische Werte:

| Regime | η | Beschreibung |
|--------|---|-------------|
| Resonanz (ω_f ≈ ω₀, niedrige A_f) | 5–30% | Effizient, periodisch |
| Nichtlineare Resonanz (moderate A_f) | 10–50% | Optimal durch Rückkopplung |
| Chaotisch (hohe A_f) | 1–5% | Energie verteilt sich breitbandig |
| Off-Resonanz (ω_f ≠ ω₀) | <1% | Keine Kopplung |

---

## 6. Verbindung zur linearen Simulation

| Aspekt | Linearer Generator | Nichtlineare Analyse |
|--------|-------------------|---------------------|
| Dämpfung | d = const | d(E) energieabhängig |
| Frequenz | ω_f = const | ω_f · (1 + δt) moduliert |
| Verhalten | Immer periodisch | Periodisch → chaotisch |
| Kopplung | ε(Δφ) = cos²(Δφ/2) | ε(Δφ, E, x, v) nichtlinear |
| Analyse | Frequenz-Sweep, Phasenscan | Poincaré, Wavelet, Spektrogramm |
| Simulation | `resonanzgenerator.py` | `nichtlineare_resonanzanalyse.py` |

Beide Simulationen bestätigen das Grundprinzip:
**Resonanz maximiert den Energietransfer.**

---

## 7. Nutzung

```bash
pip install streamlit numpy matplotlib scipy pywt
streamlit run nichtlineare_resonanzanalyse.py
```

Die App läuft im Browser. Parameter einstellen → „Start Simulation"
→ 6-Panel-Dashboard + Wirkungsgrad werden angezeigt.

---

## 8. Weiterführend

- Lyapunov-Exponenten (Chaosmaß) → geplant
- Batch-Parameter-Scans (Bifurkationsdiagramme) → geplant
- Kopplung an Phasenscan aus resonanzgenerator.py → geplant

---

→ [Python-Simulation](nichtlineare_resonanzanalyse.py)
→ [Linearer Resonanzgenerator](resonanzgenerator.md)
→ [Zurück zur Übersicht](README.md)

---

© Dominic-René Schu — Resonanzfeldtheorie 2025/2026