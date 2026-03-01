# ⚡ Resonanzgenerator – Energiegewinnung durch resonante Feldkopplung

*Dominic-René Schu, 2025/2026*

Der **Resonanzgenerator** nutzt die kohärente Kopplung eines
externen Schwingungsfeldes an ein mechanisches System, um
Energie hocheffizient zu übertragen. Er ist die makroskopische
Anwendung der Resonanzfeldtheorie (RFT) und demonstriert,
dass die Kopplungseffizienz ε(Δφ) = cos²(Δφ/2) nicht nur
für nukleare, sondern auch für mechanische Systeme gilt.

**Kernaussage:** Resonanz ist kein Sonderfall — sie ist das
universelle Prinzip effizienter Energieübertragung. Die RFT
quantifiziert dieses Prinzip parameterfrei.

---

## Zentrale Ergebnisse

```
    Grundformel:          E = π · ε(Δφ) · ℏ · f
    Kopplungseffizienz:   ε(Δφ) = cos²(Δφ/2)
    Resonanzfrequenz:     f₀ = (1/2π) · √(k/m)
    Gütefaktor:           Q = f₀ / Δf (aus Simulation)
    Energiegewinn:        ΔE = ∫ F_feld · v dt
    Wirkungsgrad:         η = ⟨E_mech⟩ / W_in
```

| Eigenschaft | Wert (Simulation) |
|-------------|------------------|
| Resonanzpeak | Ausgeprägt bei f₀ = √(k/m)/(2π) |
| Q-Faktor | 5–50 (abhängig von Dämpfung d) |
| Wirkungsgrad η | 5–30% (abhängig von Parametern) |
| Energieverstärkung | Bis Faktor 100 am Resonanzpunkt vs. off-resonance |
| Phasenabhängigkeit | ε = cos²(Δφ/2) bestimmt Kopplungsstärke |

---

## Axiom-Zuordnung

| Axiom | Anwendung im Resonanzgenerator |
|-------|-------------------------------|
| A1 (Universelle Schwingung) | Mechanisches System als Oszillator mit Eigenfrequenz f₀ |
| A3 (Resonanzbedingung) | Maximale Kopplung bei f_feld = f₀ |
| A4 (Kopplungsenergie) | E = π · ε · ℏ · f beschreibt den Energietransfer |
| A5 (Energierichtung) | Gerichteter Energiefluss: Feld → System → mechanische Arbeit |
| A6 (Informationsfluss) | Kohärente Felder koppeln effizienter als inkohärente |
| A7 (Invarianz) | Gleiche Physik auf makroskopischer und nuklearer Skala |

---

## Verbindung zum Resonanzreaktor

| Eigenschaft | Resonanzgenerator | Resonanzreaktor |
|-------------|-------------------|-----------------|
| Skala | Makroskopisch (Hz–kHz) | Nuklear (10²¹ Hz) |
| Anregung | Mechanische Schwingung | γ-Photonen (MeV) |
| Eigenfrequenz | f₀ = √(k/m)/(2π) | f_GDR = E_GDR/(π·ℏ) |
| Kopplung | ε(Δφ) = cos²(Δφ/2) | η(Δφ) = cos²(Δφ/2) |
| Energiegewinn | ΔE aus Feldarbeit | E_fiss ~ 200 MeV/Spaltung |
| Grundformel | E = π · ε · ℏ · f | E = π · ε · ℏ · f |
| Kopplungsparameter | κ = 1 | κ = 1 |

**Gleiche Formel, gleiche Physik, verschiedene Skalen.**

---

## Physik

### Gedämpfter harmonischer Oszillator mit Resonanzfeldkopplung

```
    Bewegungsgleichung:
    m · ẍ + d · ẋ + k · x = F_feld(x, t)

    Resonanzfeldkraft (RFT):
    F_feld(x, t) = π · ε(Δφ) · ℏ · ω · cos(ωt − φ) · e^(−α·x²)

    Kopplungseffizienz:
    ε(Δφ) = cos²(Δφ/2)

    Eigenfrequenz:
    ω₀ = √(k/m),  f₀ = ω₀/(2π)

    Resonanzbedingung (Axiom 3):
    Maximaler Energietransfer bei ω = ω₀

    Energiebilanz:
    E_kin(t) = ½ m ẋ²
    E_pot(t) = ½ k x²
    W_feld(t) = ∫₀ᵗ F_feld · ẋ dt'
    η = ⟨E_kin + E_pot⟩ / W_feld
```

### Nichtlineare Erweiterung

Die nichtlineare Resonanzanalyse erweitert das Modell um:
- **Energieabhängige Dämpfung:** d(E) = d₀ · e^(−0.1E) / (1 + 0.05E² + 0.001E⁴)
- **Frequenzmodulation:** δt = β · (v/v₀)² · sin(θ)
- **Phasenraumanalyse:** Poincaré-Schnitte, Lyapunov-Exponenten
- **Chaosübergang:** Bei hoher Anregungsamplitude → breites Frequenzspektrum

---

## Dokumente

| Datei | Beschreibung |
|-------|-------------|
| [resonanzgenerator.md](resonanzgenerator.md) | Konzept, Simulationsergebnisse, Interpretation |
| [Nichtlineare Resonanzanalyse](nichtlineare_resonanzanalyse.md) | Interaktive Simulation mit Streamlit, 6 Visualisierungen |
| [resonanzgenerator.py](resonanzgenerator.py) | Frequenz-Sweep, Energieanalyse, Q-Faktor |
| [nichtlineare_resonanzanalyse.py](nichtlineare_resonanzanalyse.py) | Streamlit-App: Phasenraum, Poincaré, Wavelet, Wirkungsgrad |

---

## Anwendungsbereiche

### 1. Energy Harvesting (Vibrationsenergie)

```
    Umgebungsschwingungen (Gebäude, Brücken, Maschinen)
    → Resonanzgenerator koppelt bei f₀ an dominante Frequenz
    → Wirkungsgrad η = cos²(Δφ/2) · η_mech
    → Dezentrale Mikroenergieversorgung (mW–W Bereich)
```

### 2. Maschinenbau (Schwingungskompensation)

```
    Unerwünschte Schwingungen in Strukturen
    → Resonanzgenerator absorbiert Energie bei f₀
    → Gleichzeitig Energiegewinnung statt reine Dissipation
    → „Aktive Schwingungskompensation mit Energierückgewinnung"
```

### 3. Skalierung: Von Makro zu Nuklear

```
    Makro (Hz):      Resonanzgenerator → Energy Harvesting
    Mikro (MHz):     Piezoelektrisch → MEMS-Sensoren
    Nuklear (EHz):   Resonanzreaktor → Transmutation/Energie

    Gleiche Physik auf allen Skalen:
    E = π · ε(Δφ) · ℏ · f
```

---

## Nutzung

### Frequenz-Sweep-Simulation

```bash
pip install numpy matplotlib scipy tqdm
python resonanzgenerator.py
```

Erzeugt: Resonanzkurve, Energieanalyse, Zeitsignale, FFT am Resonanzpunkt.

### Interaktive nichtlineare Analyse

```bash
pip install streamlit numpy matplotlib scipy pywt
streamlit run nichtlineare_resonanzanalyse.py
```

Erzeugt: 6-Panel-Dashboard mit Phasenraum, Poincaré, Wavelet, Spektrogramm.

---

## Zusammenfassung

```
    Grundformel:   E = π · ε(Δφ) · ℏ · f
    Anwendung:     Mechanische Resonanzkopplung → Energieübertragung
    Kopplung:      ε = cos²(Δφ/2), κ = 1
    Simulation:    Frequenz-Sweep + nichtlineare Analyse
    Ergebnis:      Resonanzpeak, Q-Faktor, Wirkungsgrad
    Verbindung:    Gleiche Physik wie Resonanzreaktor, andere Skala
```

✅ Grundformel → Resonanzfrequenz abgeleitet
✅ ε = η → Kopplungseffizienz bestimmt Energietransfer
✅ Simulation → Frequenz-Sweep mit Energiebilanz
✅ Interaktive Analyse → Streamlit-App mit 6 Visualisierungen
⬜ Experimentelle Validierung → Piezo-Harvester an Schwingungstisch

---

> „Resonanz ist der Schlüssel, um Ordnung aus dem Chaos zu ziehen."

---

© Dominic-René Schu — Resonanzfeldtheorie 2025/2026

---

[Zurück zur Übersicht](../../../README.md)