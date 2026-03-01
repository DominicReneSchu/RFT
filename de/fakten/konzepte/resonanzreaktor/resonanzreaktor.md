# Resonanzreaktor – Resonant gesteuerte Transmutation von Atommüll

*Dominic-René Schu, 2025/2026*

---

## 1. Grundprinzip

Der Resonanzreaktor nutzt die Resonanzfeldtheorie (RFT) zur gezielten
Modulation nuklearer Zerfallsraten durch resonante Photonanregung bei
der Giant-Dipole-Resonance (GDR) Frequenz eines Isotops.

Die zentrale Vorhersage: Die Zerfallsrate eines Isotops ist nicht
konstant (wie im Standardmodell), sondern modulierbar durch resonante
Kopplung bei der Eigenfrequenz des Kerns — in direktem Widerspruch
zur stochastischen Standardannahme.

**RFT-Grundformel (Axiom 4):**

```
    E = π · ε(Δφ) · ℏ · f
```

**Anwendung auf den Resonanzreaktor:**

```
    f_GDR = E_GDR / (π · ℏ)
    λ_eff(Δφ) = λ₀ + η(Δφ) · Φ_γ · σ_GDR
```

Dabei ist:
- **f_GDR**: GDR-Resonanzfrequenz des Isotops (aus E_GDR über die Grundformel)
- **λ₀**: natürliche Zerfallskonstante
- **λ_eff**: effektive (modulierte) Zerfallskonstante
- **η(Δφ)**: Kopplungseffizienz = cos²(Δφ/2) (identisch mit ε)
- **Φ_γ**: Photonenfluss bei f_GDR [γ/(cm²·s)]
- **σ_GDR**: GDR-Wirkungsquerschnitt des Isotops [barn]

**Kernresultat:** κ = 1 exakt (aus ε = η, kein freier Parameter).

---

## 2. Axiom-Zuordnung

| Axiom | Anwendung im Resonanzreaktor |
|-------|------------------------------|
| A1 (Universelle Schwingung) | Kern als Schwingungssystem mit GDR-Eigenfrequenz |
| A3 (Resonanzbedingung) | Kopplung bei f_γ = f_GDR (rationales Frequenzverhältnis 1:1) |
| A4 (Kopplungsenergie) | E = π · ε · ℏ · f bestimmt f_GDR aus E_GDR |
| A5 (Energierichtung) | Gerichteter Energietransfer: Photon → Kern → Spaltung |
| A6 (Informationsfluss) | Nur kohärente Photonenfelder koppeln effektiv |
| A7 (Invarianz) | Ergebnisse stabil über Isotope und Flussregime |

---

## 3. Isotop-spezifische Parameter

### 3.1 GDR-Energien und Resonanzfrequenzen

```
    f_GDR = E_GDR / (π · ℏ)
    ℏ = 6.582 × 10⁻²² MeV·s
```

| Isotop | E_GDR (MeV) | f_GDR (Hz) | σ_GDR (barn) | λ₀ (s⁻¹) | t₁/₂ |
|--------|-------------|------------|--------------|-----------|-------|
| U-235 | 13.0 | 6.29 × 10²¹ | 0.120 | 3.12 × 10⁻¹⁷ | 7.04 × 10⁸ a |
| Pu-239 | 13.5 | 6.53 × 10²¹ | 0.115 | 9.11 × 10⁻¹³ | 2.41 × 10⁴ a |
| Am-241 | 13.3 | 6.44 × 10²¹ | 0.110 | 5.08 × 10⁻¹¹ | 432 a |
| Cs-137 | 15.3 | 7.41 × 10²¹ | 0.085 | 7.30 × 10⁻¹⁰ | 30.2 a |
| Sr-90 | 16.5 | 7.99 × 10²¹ | 0.075 | 7.63 × 10⁻¹�� | 28.8 a |

### 3.2 Effektive Zerfallsraten

Bei perfekter Resonanz (ε = η = 1, Δφ = 0):

```
    λ_eff = λ₀ + 1.0 · Φ_γ · σ_GDR
```

| Isotop | Φ_γ (γ/cm²/s) | λ_eff/λ₀ | Interpretation |
|--------|---------------|----------|----------------|
| U-235 | 10¹² | 7872 | Zerfall 7872× beschleunigt |
| Pu-239 | 10¹² | 127 | Zerfall 127× beschleunigt |
| Am-241 | 10¹² | 3.16 | Zerfall 3× beschleunigt |
| Cs-137 | 10¹² | 1.12 | Zerfall 12% beschleunigt |

**Physik:** Je länger die natürliche Halbwertszeit, desto stärker
der relative Effekt — weil λ₀ klein ist und der Resonanzterm
η · Φ · σ dominiert.

---

## 4. Die Identität ε = η im Resonanzreaktor

### 4.1 Warum κ = 1

In früheren Fassungen enthielt die Formel einen freien
Kopplungsparameter κ:

```
    λ_eff = λ₀ + κ · η(Δφ) · Φ_γ · σ_GDR    (alt)
```

Die FLRW-Simulationen (1.530 Läufe) haben bewiesen, dass
ε(Δφ) = η(Δφ) = cos²(Δφ/2) — der theoretische Operator
und die messbare Observable sind identisch. Daraus folgt:

```
    κ = 1 exakt (kein freier Parameter)
    λ_eff = λ₀ + η(Δφ) · Φ_γ · σ_GDR    (aktuell)
```

### 4.2 Phasenabhängigkeit

Die Kopplungseffizienz hängt von der Phasendifferenz Δφ zwischen
dem Photonenfeld und der GDR-Eigenmode des Kerns ab:

```
    η(Δφ) = cos²(Δφ/2)

    Δφ = 0:   η = 1.0   perfekte Kopplung (maximale Beschleunigung)
    Δφ = π/2: η = 0.5   halbe Kopplung
    Δφ = π:   η = 0.0   keine Kopplung (destruktive Interferenz)
```

**Konsequenz:** Die Phasenkohärenz des Photonenfeldes bestimmt
die Effizienz der Transmutation. Inkohärentes Licht (thermisch)
mittelt über alle Phasen → η_eff ≈ 0.5.

---

## 5. Spaltbarkeitsquotient Q_fission

Der Spaltbarkeitsquotient quantifiziert, ob ein Isotop unter
resonanter Anregung effektiv spaltbar ist:

```
    Q_fiss = η · Φ_γ · σ_GDR / λ₀
```

| Isotop | Q_fiss (Φ = 10¹² γ/cm²/s) | Interpretation |
|--------|---------------------------|----------------|
| U-235 | 3.85 × 10⁶ | Extrem spaltbar |
| Pu-239 | 1.26 × 10² | Gut spaltbar |
| Am-241 | 2.16 | Spaltbar |
| Cs-137 | 0.12 | Schwer spaltbar (β-Strahler) |
| Sr-90 | 0.098 | Schwer spaltbar (β-Strahler) |

**Grenze:** Q_fiss > 1 bedeutet, dass die resonante Anregung
den Zerfall dominiert. Für β-Strahler (Cs-137, Sr-90) liegt
Q_fiss < 1 — hier ist GDR-Anregung weniger effektiv, weil der
Zerfallskanal β-Emission statt Spaltung ist.

---

## 6. Systemkomponenten

| Komponente | Funktion | Technologische Basis |
|------------|----------|---------------------|
| **Photonenquelle** | Kohärenter Photonenfluss bei f_GDR | Synchrotron / FEL (6–17 MeV) |
| **Resonanzkammer** | Brennstoff-Target unter Bestrahlung | Abgeschirmte Kavität, Brennstab-Geometrie |
| **Phasensteuerung** | Maximierung von η(Δφ) → 1 | Phasenregelkreis (PLL), FPGA |
| **Kühlung** | Wärmeabfuhr aus Spaltungsprozessen | Natrium/Blei-Kühlmittel oder Helium |
| **Energieextraktion** | Spaltungsenergie → Elektrizität | Thermischer Kreislauf / Direkte Wandlung |
| **Steuerung** | Echtzeitoptimierung von f, Δφ, Φ | Deep-Resonance-Network (DRN) |

---

## 7. Vergleich: RFT-Vorhersage vs. Standardmodell

| Aspekt | Standardmodell | RFT (Resonanzreaktor) |
|--------|---------------|----------------------|
| Zerfallsrate | λ = const (stochastisch) | λ_eff = λ₀ + η·Φ·σ (modulierbar) |
| Beeinflussung | Nicht möglich | Durch resonante Photonanregung |
| Kopplungsparameter | — | κ = 1 (aus ε = η, kein freier Parameter) |
| Phasenabhängigkeit | — | η = cos²(Δφ/2) bestimmt Effizienz |
| Transmutation | Nur durch Neutronenbeschuss | Zusätzlich durch GDR-Photoanregung |
| Energieformel | E = ℏω | E = π · ε · ℏ · f |
| Testbare Vorhersage | — | λ_eff/λ₀ messbar bei bekanntem Φ·σ |

**Entscheidender Unterschied:** Die RFT sagt vorher, dass
Kernzerfall durch resonante Anregung bei der GDR-Eigenfrequenz
messbar beschleunigt werden kann — das Standardmodell
betrachtet Kernzerfall als rein stochastisch und prinzipiell
nicht modulierbar.

---

## 8. Experimentelle Überprüfbarkeit

### 8.1 Minimales Experiment

```
    Target:     Am-241 (t₁/₂ = 432 a, Q_fiss = 2.16)
    Quelle:     Synchrotron bei E_γ = 13.3 MeV (f_GDR)
    Fluss:      Φ = 10¹⁰ − 10¹² γ/(cm²·s)
    Messgröße:  Zerfallsrate λ_eff vs. λ₀
    Vorhersage: λ_eff/λ₀ = 1 + Q_fiss = 3.16 bei Φ = 10¹²
```

### 8.2 Signatur

Die RFT-spezifische Signatur ist die **Phasenabhängigkeit**:
Dreht man die Phase des Photonenfeldes relativ zum Target,
muss η = cos²(Δφ/2) beobachtet werden — ein Effekt, den das
Standardmodell nicht vorhersagt.

### 8.3 Nullexperiment

```
    Kontrolle:  Gleiches Target, gleicher Fluss, aber
                thermische (inkohärente) Photonen
    Erwartung:  η_eff ≈ 0.5 (Mittelung über alle Phasen)
    Vorhersage: λ_eff(kohärent)/λ_eff(inkohärent) ≈ 2
```

---

## 9. Anwendung: Atommüll-Transmutation

### 9.1 Transmutationskette

```
    U-235  →(n,γ)→  U-236  →(n,γ)→  Np-237  →(GDR)→  Spaltprodukte
    Pu-239 →(n,γ)→  Pu-240 →(n,γ)→  Am-241  →(GDR)→  Spaltprodukte
```

### 9.2 Atommüll-Inventar und Transmutationszeiten

| Isotop | Menge (DE, t) | t₁/₂ (natürlich) | t₁/₂_eff (resonant) | Reduktionsfaktor |
|--------|--------------|-------------------|---------------------|-----------------|
| U-235 | ~5 | 7.04 × 10⁸ a | ~90.000 a | 7872× |
| Pu-239 | ~75 | 24.100 a | ~190 a | 127× |
| Am-241 | ~3 | 432 a | ~137 a | 3.2× |

### 9.3 Energiebilanz

Jede Spaltung setzt ~200 MeV frei. Bei resonanter Beschleunigung
des Pu-239-Zerfalls:

```
    P_fiss = N · λ_eff · E_fiss
    Bei 1 kg Pu-239: N ≈ 2.5 × 10²⁴ Kerne
    λ_eff = 127 · λ₀ = 1.16 × 10⁻¹⁰ s⁻¹
    P_fiss ≈ 2.5 × 10²⁴ × 1.16 × 10⁻¹⁰ × 200 MeV
           ≈ 9.3 kW (thermisch, pro kg Pu-239)
```

---

## 10. Offene Fragen

1. **Experimentelle Bestätigung:** Die Vorhersage λ_eff/λ₀ > 1
   bei GDR-Anregung muss experimentell verifiziert werden.
2. **Photonenquellenleistung:** Synchrotron-Quellen mit
   Φ = 10¹² γ/(cm²·s) bei 13 MeV sind technisch anspruchsvoll.
3. **Phasenkohärenz:** Praktische Realisierung der Phasensteuerung
   auf nuklearer Skala.
4. **Nichtlineare Effekte:** Sättigung bei hohen Flüssen
   (analog zur FLRW-Sättigung bei hohem H₀).
5. **Vollständige Zerfallskette:** Simulation aller Tochterisotope
   mit ihren jeweiligen GDR-Parametern.

---

## 11. Zusammenfassung

| Kernaussage | Ergebnis |
|-------------|----------|
| Grundformel | E = π · ε · ℏ · f → f_GDR = E_GDR/(π·ℏ) |
| Effektive Zerfallsrate | λ_eff = λ₀ + η · Φ · σ_GDR |
| Kopplungsparameter | κ = 1 exakt (aus ε = η) |
| Standardmodell | ε(Δφ) = η(Δφ) = cos²(Δφ/2) |
| Stärkster Effekt | U-235: λ_eff/λ₀ = 7872 bei Φ = 10¹² |
| Spaltbarkeit | Q_fiss > 1 für Aktinide (U, Pu, Am) |
| Testbare Vorhersage | Phasenabhängigkeit η = cos²(Δφ/2) |
| Hauptanwendung | Transmutation langlebiger Aktinide |
| Verbindung zu FLRW | ε = η validiert in 1.530 Simulationen |

---

## 12. Quellen

- Berman, B.L., Fultz, S.C. (1975): Measurements of the giant
  dipole resonance with monoenergetic photons.
  *Rev. Mod. Phys.* **47**, 713
- Dietrich, S.S., Berman, B.L. (1988): Atlas of photoneutron
  cross sections. *Atomic Data and Nuclear Data Tables* **38**, 199
- Planck Collaboration (2020): *A&A* **641**, A6 (Planck-2018)
- Schu, D.-R. (2025/2026): Resonanzfeldtheorie
  ([GitHub](https://github.com/DominicReneSchu/public))

---

© Dominic-René Schu — Resonanzfeldtheorie 2025/2026

---

[Zurück zur Übersicht](README.md)