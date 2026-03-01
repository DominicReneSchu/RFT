# Nichtlineare Resonanzanalyse

*Dominic-René Schu, 2025/2026*

---

![Simulation nichtlineare Resonanzfeldanalyse](./nichtlineare_resonanzanalyse.png)

*Abb. 1: 6-Panel-Dashboard der nichtlinearen Resonanzanalyse*

---

## 1. Überblick

Die nichtlineare Resonanzanalyse erweitert den linearen
Resonanzgenerator um zwei physikalische Effekte:

- **Duffing-Nichtlinearität (β):** Kubischer Term β·x³ in der
  Rückstellkraft → Frequenzverschiebung, Chaosübergang
- **Energieabhängige Dämpfung (α_d):** d(E) = d₀·(1 + α_d·E)
  → Amplitudensättigung bei hoher Energie

Die zentrale Frage: **Bleibt ε(Δφ) = cos²(Δφ/2) auch im
nichtlinearen Regime gültig?**

Antwort: **Ja.** Die Phasenkopplung bestimmt den Energieeintrag
unabhängig von der internen Dynamik des Systems.

---

## 2. Physik

### 2.1 Bewegungsgleichung

```
    m·ẍ + d(E)·ẋ + k·x + β·x³ = F₀·cos²(Δφ/2)·cos(ω_f·t)

    d(E) = d₀ · (1 + α_d · E)      (energieabhängige Dämpfung)
    ε(Δφ) = cos²(Δφ/2)             (RFT-Kopplungseffizienz)
```

### 2.2 Nichtlineare Effekte

| β = 0 (linear) | β > 0 (Duffing) |
|-----------------|-----------------|
| Eigenfrequenz f₀ = const | f₀ verschiebt sich mit Amplitude |
| Phasenraum: Ellipse | Phasenraum: deformiert |
| Immer periodisch | Periodisch → quasiperiodisch → chaotisch |
| A ∝ 1/d (exakt) | A begrenzt durch β·x³ |

---

## 3. Ergebnisse

### 3.1 Duffing-Scan (β = 0 → 50)

| β | A_stat [mm] | E_stat [µJ] | Regime |
|---|------------|------------|--------|
| 0.0 | 200.0 | 200.000 | Periodisch |
| 1.0 | 199.7 | 199.436 | Periodisch |
| 5.0 | 192.8 | 186.245 | Periodisch |
| 20.0 | 159.4 | 127.850 | Periodisch |
| 50.0 | 127.4 | 82.012 | Periodisch |

**Erkenntnis:** Nichtlinearität reduziert die Amplitude, aber
die Phasenkopplung ε(Δφ) = cos²(Δφ/2) bleibt exakt gültig.
Der Duffing-Term wirkt wie eine zusätzliche amplitudenabhängige
Federkonstante — er verändert die interne Dynamik, nicht die
externe Kopplung.

### 3.2 Energieabhängige Dämpfung (α_d = 0 → 1.0)

```
    α_d = 0.0:   A = 200 mm (unbegrenzt durch Dämpfung)
    α_d = 0.01:  A ≈ 190 mm (leichte Sättigung)
    α_d = 0.1:   A ≈ 175 mm (moderate Sättigung)
    α_d = 0.5:   A ≈ 150 mm (starke Sättigung)
    α_d = 1.0:   A ≈ 125 mm (dominante Sättigung)
```

**Erkenntnis:** Energieabhängige Dämpfung begrenzt die maximale
Schwingungsamplitude — physikalisch sinnvoll, da reale Systeme
bei hoher Energie mehr Verluste haben. Das Sättigungsniveau
hängt von α_d ab, aber die Phasenabhängigkeit bleibt cos²(Δφ/2).

### 3.3 Phasenscan (nichtlinear, β = 0)

```
    E(Δφ=0) / ⟨E⟩_inkohärent = 2.5000
    Theorie:                     2.5000  → EXAKT

    Amplitude folgt cos²(Δφ/2)          → EXAKT
    Energie folgt cos⁴(Δφ/2)           → EXAKT
```

---

## 4. Relevanz für die Maschinenresonanz

Die nichtlineare Analyse bestätigt, dass die RFT-Phasensteuerung
auch unter realen Bedingungen funktioniert:

| Realer Effekt | Modellparameter | Auswirkung auf ε(Δφ) |
|---------------|----------------|---------------------|
| Materialnichtlinearität | β > 0 | Keine (ε bleibt cos²) |
| Energieverluste bei hoher Amplitude | α_d > 0 | Keine (ε bleibt cos²) |
| Schwankende Anregungsfrequenz | ω_f ≠ ω₀ | Reduziert Amplitude, ε unverändert |
| Chaotische Dynamik | β >> 1 | Breitband-FFT, aber ε(Δφ) steuert den Energieeintrag |

**Kernaussage:** Die Phasensteuerung Δφ → π unterbindet die
Resonanzkopplung unabhängig von der internen Nichtlinearität.

---

## 5. Simulation

### 5.1 Ausführung

```bash
# Matplotlib-Modus (4 Plots als PNG)
python nichtlineare_resonanzanalyse.py

# Interaktiver Modus (optional, benötigt Streamlit)
streamlit run nichtlineare_resonanzanalyse.py
```

### 5.2 Erzeugte Plots

| Plot | Inhalt |
|------|--------|
| `nichtlinear_dashboard.png` | 6-Panel: Zeit, Phasenraum, Poincaré, FFT, STFT, Energie |
| `nichtlinear_phasenscan.png` | RFT-Signatur: cos², cos⁴, Verhältnis koh/ink |
| `nichtlinear_duffing.png` | β-Scan: 5 Stärken, Phasenraum, Ergebnistabelle |
| `nichtlinear_daempfung.png` | α_d-Scan: Sättigung bei hoher Energie |

---

## 6. Zusammenfassung

```
    Frage:  Gilt ε(Δφ) = cos²(Δφ/2) auch nichtlinear?
    Antwort: Ja. Die Kopplung ist eine Eigenschaft der
             Feld-System-Schnittstelle, nicht der internen Dynamik.

    Nichtlinearität (β):     Verändert Amplitude und Frequenz
    Energiedämpfung (α_d):   Begrenzt die maximale Energie
    Phasenkopplung ε(Δφ):    Bleibt exakt cos²(Δφ/2)

    → Die RFT-Grundgleichung ist robust gegen Nichtlinearitäten.
    → Maschinenresonanz kann durch Δφ → π unterbunden werden,
      unabhängig von der internen Systemdynamik.
```

---

→ [Linearer Resonanzgenerator](resonanzgenerator.md)
→ [Zurück zur Übersicht](README.md)

---

© Dominic-René Schu — Resonanzfeldtheorie 2025/2026