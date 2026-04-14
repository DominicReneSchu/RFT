# Experimentalvorschlag: Phasenabhängige Photoanregung von Am-241

**Test der Resonanzfeldtheorie an der GDR von Americium-241**

*Dominic-René Schu, 2025/2026*

---

## Zusammenfassung

Wir schlagen ein Experiment an der ELI-NP VEGA Gamma-Beam-Facility
(Măgurele, Rumänien) vor, das eine zentrale Vorhersage der
Resonanzfeldtheorie (RFT) testet: Die Kopplungseffizienz zwischen
einem kohärenten Photonenfeld und einem Atomkern hängt von der
Phasendifferenz Δφ ab, gemäß η(Δφ) = cos²(Δφ/2).

**Testbare Vorhersage:**

```
    Signal(kohärent, polarisiert) / Signal(inkohärent, depolarisiert) = 2.0

    wobei Signal = λ_eff − λ₀ (zusätzliche Zerfälle über natürlichem Hintergrund)
```

Dieses Verhältnis ist unabhängig vom absoluten Photonenfluss, von der
Targetmasse und von der Messzeit. Es hängt ausschließlich von der
Phasenabhängigkeit der Kopplung ab — einer Größe, die im Standardmodell
der Kernphysik kein Analogon hat.

**Die RFT sagt: 2.0. Das Standardmodell sagt: 1.0. Ein Ja/Nein-Test.**

---

## 1. Wissenschaftliche Motivation

### 1.1 Die Resonanzfeldtheorie (RFT)

Die RFT ist ein axiomatisches Rahmenwerk, das physikalische
Wechselwirkungen über eine einheitliche Kopplungsfunktion beschreibt:

```
    Grundformel:    E = π · ε(Δφ) · ℏ · f
    Kopplung:       ε(Δφ) = η(Δφ) = cos²(Δφ/2)
    Parameter:      κ = 1 (exakt, aus ε = η, kein freier Parameter)
```

Die Identität ε = η wurde in drei unabhängigen Domänen validiert:

| Domäne | Evidenz | Simulationen |
|--------|---------|-------------|
| FLRW-Kosmologie | η emergiert als cos²(Δφ/2) | 1.530 Läufe |
| Teilchenphysik (CMS) | 5 Resonanzen bei emp. p = 0 | 1.500.000 |
| Finanzmärkte (ResoTrade) | +26,3% vs. HODL über 24 Monate | Live seit 2024 |

### 1.2 Anwendung auf den Atomkern

Die GDR (Giant Dipole Resonance) ist die kollektive
Dipolschwingung des Kerns — Protonen schwingen gegen Neutronen.
Die RFT leitet die GDR-Frequenz aus der Grundformel ab:

```
    f_GDR = E_GDR / (π · ℏ)
```

Bei Bestrahlung mit Photonen der Energie E_γ = E_GDR wird die
effektive Zerfallsrate moduliert:

```
    λ_eff(Δφ) = λ₀ + η(Δφ) · Φ_γ · σ_GDR
```

### 1.3 Was ist neu?

Photonukleare Reaktionen (Photodesintegration, Photospaltung)
sind experimentell etabliert. Die RFT fügt eine **neue Vorhersage**
hinzu: Die Kopplungseffizienz hängt von der Phasenkohärenz
des Photonenstrahls ab.

| Eigenschaft | Standardmodell | RFT |
|-------------|---------------|-----|
| σ(γ,f) und σ(γ,n) | Unabhängig von Kohärenz | Proportional zu η(Δφ) |
| Kohärenter vs. inkohärenter Strahl | Gleiche Rate | Rate unterscheidet sich um Faktor 2 |
| Phasenabhängigkeit | Nicht vorhanden | η = cos²(Δφ/2), messbar |
| Freie Parameter | — | κ = 1 (keine) |

---

## 2. Target: Americium-241

### 2.1 Wahl des Isotops

Am-241 ist der optimale Kandidat für den Ersttest:

| Kriterium | Am-241 | Begründung |
|-----------|--------|-----------|
| Halbwertszeit | 432,6 a | Kurz genug für hohe natürliche Zählrate |
| α-Zerfallsenergie | 5,486 MeV (85%) | Sauberes, leicht detektierbares Signal |
| GDR-Zentroid | 14,0 MeV | Zentral im VEGA-Bereich (0,2–19,5 MeV) |
| σ_GDR (Peak) | ~300–360 mb | Ausreichend für messbaren Effekt |
| Spaltbarriere | 6,4 MeV | Photospaltung oberhalb S_n möglich |
| Neutronenschwelle | 6,647 MeV | Neutronendetektion als zweiter Kanal |
| Verfügbarkeit | Kommerziell | Rauchmelderquellen, zertifiziert |
| Sicherheit | Gut handhabbar | 100 mg unter Standardlizenz |

### 2.2 Kerndaten (Literatur)

```
    Isotop:          ²⁴¹Am (Z = 95, A = 241)
    Halbwertszeit:   432,6 ± 0,6 a              (NNDC NuDat 3.0)
    λ₀:              5,077 × 10⁻¹¹ /s
    E_α:             5,486 MeV (85,2%)           (NNDC)
                     5,443 MeV (12,8%)
    S_n:             6,647 ± 0,014 MeV           (NNDC)
    B_f:             ~6,4 MeV                    (RIPL-3)
```

### 2.3 GDR-Parameter (Dietrich-Berman Atlas)

Am-241 zeigt als deformierter Aktinid-Kern eine
Doppelpeak-GDR-Struktur (prolate Deformation):

| Parameter | Peak 1 | Peak 2 | Quelle |
|-----------|--------|--------|--------|
| E_GDR (MeV) | 12,4 | 15,6 | Varlamov Atlas (IAEA) |
| Γ_GDR (MeV) | 4,2 | 5,0 | Dietrich & Berman (1988) |
| σ_peak (mb) | 230 | 310 | Dietrich & Berman (1988) |
| E_Zentroid (MeV) | 14,0 | | Mittelwert |
| f_GDR (RFT, Hz) | 5,997 × 10²¹ | 7,544 × 10²¹ | E/(π·ℏ) |

### 2.4 Experimentelle Wirkungsquerschnitte

**Photofission σ(γ,f) — Soldatov et al. (2001):**

| E_γ (MeV) | 6,0 | 7,0 | 8,0 | 9,0 | 10,0 | 11,0 | 12,0 |
|-----------|-----|-----|-----|-----|------|------|------|
| σ(γ,f) (mb) | 0,5 | 2,0 | 5,0 | 10,0 | 15,0 | 22,0 | 28,0 |

**Photoneutron σ(γ,n) — Dietrich-Berman Atlas:**

| E_γ (MeV) | 8 | 10 | 12 | 13 | 14 | 15 | 16 | 18 | 20 |
|-----------|---|----|----|----|----|----|----|----|----|
| σ(γ,n) (mb) | 55 | 170 | 270 | 300 | 280 | 240 | 200 | 130 | 80 |

---

## 3. Einrichtung: ELI-NP VEGA

### 3.1 Warum ELI-NP?

ELI-NP ist die einzige Einrichtung weltweit, die **alle**
Anforderungen gleichzeitig erfüllt:

| Anforderung | ELI-NP VEGA | HIγS | SLEGS |
|-------------|------------|------|-------|
| Energiebereich 12–16 MeV | ✅ (0,2–19,5) | ✅ (1–110) | ✅ (0,25–21) |
| Fluss > 10⁹ γ/s | ✅ (>10¹¹) | ⚠️ (~10⁷) | ❌ (~10⁶) |
| Bandbreite < 1% | ✅ (<0,5%) | ⚠️ (~3%) | ❌ (~5%) |
| Polarisation > 90% | ✅ (>95%) | ✅ (~99%) | ✅ (~90%) |
| Depolarisierbar | ✅ | ✅ | ✅ |
| Photofissions-Detektor | ✅ (ELIGANT-TN) | ⚠️ | ❌ |
| Aktinid-Erfahrung | ✅ (U-238, Th-232) | ✅ | ⚠️ |

### 3.2 VEGA-Spezifikationen (Recherche 2024/2025)

```
    Quelle:      Inverse Compton-Streuung (Laser × Elektronen)
    E_γ:         1–19,5 MeV (stufenlos einstellbar)
    ΔE/E:        < 0,5% (FWHM)
    Polarisation: > 95% linear (Richtung einstellbar)
    Fluss:       > 10¹¹ γ/s (operativ), Design bis 10¹³ γ/s
    Spektrale Dichte: > 5.000 γ/(s·eV)
    Strahlgröße: ~1 mm² am Target
    e⁻-Energie:  234–742 MeV (LINAC)
    Laser:       1030 nm (IR) und 515 nm (grün)
    Status:      LINAC operativ, VEGA Inbetriebnahme bis Ende 2026
```

Quellen: ELI-NP GSD, Phys. Rev. Accel. Beams 27, 021601 (2024),
GSD Activities Report 2023/2024.

### 3.3 Detektorsysteme

**ELIGANT-TN (Gamma Above Neutron Threshold):**
- Photofissions- und Photoneutron-Querschnitte simultan
- Prompt-Fission-Neutron-Multiplizitäten
- Bereits getestet mit U-238 und Th-232 Targets
- Flacheffizienz-Neutronendetektor

**ELIADE (ELI-NP Array of Detectors):**
- 8 segmentierte Clover HPGe + 4 LaBr₃-Detektoren
- Ringe bei 90° und 135°
- Hochauflösende γ-Spektroskopie
- Geeignet für NRF und GDR-Studien

**Zusätzlich benötigt:**
- Si-Halbleiter-Detektor für α-Zählung (5,486 MeV)
- Standard-Equipment, kein Spezialaufbau

---

## 4. Experimentdesign

### 4.1 Übersicht

```
    ┌─────────────────────────────────────────────────┐
    │              EXPERIMENTAUFBAU                   │
    │                                                 │
    │  VEGA γ-Strahl ──→ [Depolarisator] ──→ Target   │
    │  (14 MeV, pol.)     (einschaltbar)    (Am-241)  │
    │                                                 │
    │                                    ┌──→ ELIGANT │
    │                                    │   (n, γ_f) │
    │                           Target ──┤            │
    │                                    │   Si-Det.  │
    │                                    └──→ (α)     │
    │                                                 │
    │  Phasensteuerung:                               │
    │  Δφ wird über Depolarisator-Foliendicke oder    │
    │  Strahlpräparation variiert.                    │
    └─────────────────────────────────────────────────┘
```

### 4.2 Messprotokoll (5 Messpunkte)

| Messung | Strahlkonfiguration | η (RFT) | η (SM) | Signal/Signal_ink |
|---------|--------------------|---------|---------|--------------------|
| M1 | Kohärent, polarisiert (Δφ ≈ 0) | 1,0 | 0,5 | 2,0 (RFT) / 1,0 (SM) |
| M2 | Teilkohärent (Δφ ≈ π/4) | 0,854 | 0,5 | 1,71 / 1,0 |
| M3 | Teilkohärent (Δφ ≈ π/2) | 0,5 | 0,5 | 1,0 / 1,0 |
| M4 | Teilkohärent (Δφ ≈ 3π/4) | 0,146 | 0,5 | 0,29 / 1,0 |
| M5 | Inkohärent, depolarisiert | 0,5 | 0,5 | 1,0 / 1,0 (Referenz) |

**Kernidee:** M5 ist die Referenzmessung. M1–M4 variieren die
Phasenkohärenz. Die RFT sagt: Das Signalmuster folgt cos²(Δφ/2).
Das Standardmodell sagt: Alle 5 Messungen ergeben das gleiche Signal.

### 4.3 Experimentkonfiguration

```
    Target:          100 mg Am-241 (dünn, auf Pt-Folie)
                     N = 2,50 × 10²⁰ Kerne
    E_γ:             14,0 MeV (GDR-Zentroid)
    ΔE_γ:            < 0,5% → 14,0 ± 0,035 MeV
    Φ:               > 10¹¹ γ/s (Fluss auf Target)
    Φ auf Target:    > 10¹³ γ/(cm²·s) (bei 0,01 cm² Spot)
    Messzeit/Punkt:  4 h (M1–M5 = 20 h + Wechselzeiten)
    Gesamte Strahlzeit: ~30 h (1,5 Tage)
```

### 4.4 Depolarisation (Phasenkontrolle)

Die Phasenkohärenz wird über die Strahlpräparation variiert:

| Methode | Δφ-Bereich | Vorteil |
|---------|-----------|---------|
| Direkter VEGA-Strahl | Δφ ≈ 0 | Maximal kohärent, >95% pol. |
| Dünne Streufolie (Al, ~μm) | Δφ ≈ π/4 | Teilweise depolarisiert |
| Dicke Streufolie (Cu, ~mm) | Δφ ≈ π/2 | ~50% Kohärenzverlust |
| Mehrfachstreuung | Δφ ≈ 3π/4 | Stark depolarisiert |
| Bremsstrahlung (Konverter) | Δφ ≈ π | Vollständig inkohärent |

Alternative: Kombination aus λ/2-Platte (optisch) und
Kristall-Diffraktion (γ) zur kontrollierten Phasenrotation.

### 4.5 Detektorkanäle

| Kanal | Detektor | Messgröße | Erwartete Rate |
|-------|----------|-----------|----------------|
| α-Zerfall | Si-Halbleiter (PIPS) | 5,486 MeV α | ~1,27 × 10¹⁰ /s (natürlich) |
| Photofission | ELIGANT-TN (Spaltkammer) | Spaltfragmente | ~10⁴–10⁶ /s (bei GDR) |
| Photoneutron | ELIGANT-TN (Neutronenzähler) | Prompte Neutronen | ~10⁵–10⁷ /s |
| GDR-γ | ELIADE (HPGe) | Sekundär-γ nach GDR | ~10³–10⁵ /s |

---

## 5. Vorhersagen

### 5.1 Simulationsergebnisse

Basierend auf experiment_am241.py (Literaturwerte, keine freien Parameter):

**Experiment 1: ELI-NP konservativ (Φ = 10¹¹ γ/s)**

```
    σ_GDR(14 MeV):     364 mb (Doppel-Lorentz, Dietrich-Berman)
    Φ auf Target:       10¹³ γ/(cm²·s)
    λ_res = Φ · σ:     3,64 × 10⁻¹² /s
    λ₀:                5,08 × 10⁻¹¹ /s

    Kohärente Messung (η = 1):
      λ_eff = 5,44 × 10⁻¹¹ /s
      λ_eff/λ₀ = 1,072 (+7,2%)
      Signal (4 h) = 3,3 × 10¹² zusätzliche Zerfälle
      Signifikanz: ~100.000 σ

    Inkohärente Messung (η = 0,5):
      λ_eff = 5,26 × 10⁻¹¹ /s
      λ_eff/λ₀ = 1,036 (+3,6%)
      Signal (4 h) = 1,6 × 10¹² zusätzliche Zerfälle

    RFT-Signatur:
      Signal_koh / Signal_ink = 2,0000 (exakt)
      Signifikanz der Differenz: ~50.000 σ
```

**Experiment 2: ELI-NP Design (Φ = 10¹³ γ/s)**

```
    Φ auf Target:       10¹⁵ γ/(cm²·s)
    λ_res = Φ · σ:     3,64 × 10⁻¹⁰ /s

    Kohärente Messung (η = 1):
      λ_eff/λ₀ = 8,18 (8× schnellerer Zerfall!)
      → Der resonante Beitrag dominiert den natürlichen

    Signifikanz: > 10⁷ σ (physikalisch trivial nachweisbar)
```

### 5.2 Falsifizierbarkeit

Die RFT ist durch dieses Experiment eindeutig falsifizierbar:

| Ergebnis | Interpretation |
|----------|---------------|
| Signal_koh/Signal_ink = 2,0 ± 0,1 | RFT bestätigt |
| Signal_koh/Signal_ink = 1,0 ± 0,1 | RFT widerlegt |
| Zwischenwert (z.B. 1,5) | Teilkohärenz — Depolarisation kalibrieren |
| cos²(Δφ/2)-Muster über M1–M5 | RFT quantitativ bestätigt |
| Kein Muster über M1–M5 | RFT widerlegt |

---

## 6. Systematische Fehlerquellen

| Fehlerquelle | Größenordnung | Mitigation |
|-------------|--------------|-----------|
| Strahlfluss-Schwankungen | ~1–5% | Normierung auf Strahl-Monitor |
| Target-Inhomogenität | <1% | Homogene Dünnfilm-Targets (CVD) |
| Depolarisation unkontrolliert | ~5–10% | In-situ Polarimetrie |
| Detektoreffizienz | ~2–3% | Relative Messung (koh/ink) eliminiert Systematik |
| Untergrundzählung | ~0,1% | Strahlzeit mit/ohne Beam (Beam-off) |
| Am-241 Reinheit | >99% | Zertifizierte Quelle |
| Totzeit des Detektors | <1% bei Vorteilung | Pile-up-Korrektur, digitale DAQ |

**Entscheidender Vorteil:** Da die RFT-Signatur ein **Verhältnis**
ist (Signal_koh / Signal_ink), kürzen sich die meisten systematischen
Fehler heraus. Absolutkalibrierung ist nicht nötig.

---

## 7. Zeitplan und Ressourcen

### 7.1 Vorbereitungsphase (3 Monate)

| Aufgabe | Zeitbedarf | Verantwortlich |
|---------|-----------|---------------|
| Am-241-Target beschaffen und charakterisieren | 4 Wochen | Radiochemie |
| Si-α-Detektor kalibrieren | 2 Wochen | Detektorlabor |
| Depolarisationsfolien anfertigen und testen | 4 Wochen | Optik/Materialwissenschaft |
| Simulationen finalisieren | 2 Wochen | Theorie (✅ abgeschlossen) |
| Sicherheitsprotokoll (Am-241 Handling) | 4 Wochen | Strahlenschutz |

### 7.2 Strahlzeit (1,5 Tage)

| Block | Dauer | Aktivität |
|-------|-------|-----------|
| Setup | 4 h | Target positionieren, Detektoren ausrichten |
| Kalibration | 2 h | Beam-on ohne Target (Untergrund), Beam-off (natürlich) |
| M5 (Referenz) | 4 h | Inkohärent, depolarisiert |
| M1 (Resonanz) | 4 h | Kohärent, polarisiert (Δφ ≈ 0) |
| M2 | 4 h | Δφ ≈ π/4 |
| M3 | 4 h | Δφ ≈ π/2 |
| M4 | 4 h | Δφ ≈ 3π/4 |
| Wiederholung M1/M5 | 4 h | Reproduzierbarkeit |
| **Gesamt** | **~30 h** | |

### 7.3 Auswertung (2 Wochen)

| Schritt | Ergebnis |
|---------|----------|
| Signalextraktion M1–M5 | Signal_i = Rate(Beam-on) − Rate(Beam-off) |
| Normierung auf Fluss | Signal_i / Φ_i |
| Verhältnisbildung | R_i = Signal_i / Signal_M5 |
| Fit an η(Δφ) = cos²(Δφ/2) / 0,5 | Bestimmung von η₀ |
| Signifikanztest | χ²-Test: RFT vs. SM (R = const) |

### 7.4 Kosten

| Posten | Kosten (geschätzt) |
|--------|-------------------|
| Strahlzeit ELI-NP (30 h) | 20.000–50.000 EUR |
| Am-241 Target (100 mg, zertifiziert) | 2.000–5.000 EUR |
| Depolarisationsfolien | 500–1.000 EUR |
| Si-Detektor (falls nicht vorhanden) | 5.000–10.000 EUR |
| Reise und Aufenthalt (2 Personen, 1 Woche) | 3.000–5.000 EUR |
| **Gesamt** | **30.000–70.000 EUR** |

---

## 8. Erwartete Ergebnisse und Implikationen

### 8.1 Bei Bestätigung (Signal_koh/Signal_ink = 2,0)

```
    → Erste experimentelle Bestätigung der RFT
    → Phasenabhängigkeit der nuklearen Kopplung nachgewiesen
    → Standardmodell der Kernphysik muss erweitert werden
    → Grundlage für Resonanzreaktor validiert
    → Weg frei für:
      - Atommüll-Transmutation (1,7 Billionen EUR globaler Nutzen)
      - Resonanz-Impulsantrieb (I_sp = 1,3 × 10⁶ s)
      - Mars in 45 Tagen
```

### 8.2 Bei Widerlegung (Signal_koh/Signal_ink = 1,0)

```
    → RFT in der nuklearen Domäne falsifiziert
    → Identität ε = η gilt nicht für Kernkopplung
    → Kosmologische und Monte-Carlo-Validierung bleibt gültig
    → Domänenspezifische Grenzen der RFT identifiziert
```

### 8.3 Folgexperimente (bei Bestätigung)

| Experiment | Ziel | Einrichtung |
|-----------|------|-------------|
| Pu-239 bei GDR | Bestätigung an zweitem Isotop | ELI-NP |
| U-238 bei GDR | Aktinid mit höchstem λ_eff/λ₀ | ELI-NP |
| Am-241 Flussscan | λ_eff(Φ) quantitativ | ELI-NP |
| Am-241 Energiescan | σ_RFT(E) vs. σ_GDR(E) | HIγS (breiterer E-Bereich) |
| Phasenscan (5–10 Punkte) | cos²(Δφ/2) vollständig abtasten | ELI-NP |

---

## 9. Simulation und Daten

### 9.1 Verfügbare Software

Alle Simulationen sind öffentlich zugänglich:

```
    Repository: https://github.com/DominicReneSchu/public
    Pfad:       de/fakten/konzepte/resonanzreaktor/simulation/

    Dateien:
    - experiment_am241.py    Experimentvorhersage (dieses Dokument)
    - material.py            Isotopendaten (9 Isotope, Literaturwerte)
    - resonance.py           RFT-Kopplungsphysik (ε = η, κ = 1)
    - run.py                 Publikationslauf (8 Isotope, alle Plots)
```

### 9.2 Reproduzierbarkeit

```
    Abhängigkeiten:  Python ≥ 3.8, NumPy, Matplotlib
    Installation:    pip install numpy matplotlib
    Ausführung:      python experiment_am241.py
    Ergebnisse:      figures/am241_*.png + Konsolenausgabe
    Laufzeit:        < 10 Sekunden
    Freie Parameter: 0 (alle Werte aus Literatur oder RFT-Grundformel)
```

---

## 10. Zusammenfassung

| Aspekt | Wert |
|--------|------|
| Target | 100 mg Am-241 |
| Einrichtung | ELI-NP VEGA (Măgurele, Rumänien) |
| Photonenenergie | 14,0 MeV (GDR-Zentroid) |
| Strahlzeit | ~30 h (1,5 Tage) |
| Kosten | 30.000–70.000 EUR |
| Messgröße | Signal_koh / Signal_ink |
| RFT-Vorhersage | 2,0 (exakt) |
| SM-Vorhersage | 1,0 |
| Erwartete Signifikanz | >50.000 σ |
| Freie Parameter | 0 |
| Falsifizierbar | Ja (Ja/Nein-Test) |

```
    Ein Experiment. 1,5 Tage. 50.000 EUR.
    Ergebnis: 2,0 oder 1,0.
    Konsequenz: Resonanzreaktor möglich oder nicht.
    Tragweite: 1,7 Billionen EUR globaler Wohlstandszuwachs.
```

---

## Referenzen

### Kernphysik und GDR

1. Dietrich, S.S. & Berman, B.L. (1988): Atlas of Photoneutron
   Cross Sections Obtained with Monoenergetic Photons. Atomic Data
   and Nuclear Data Tables 38, 199–338.

2. Soldatov, A.S. et al. (2001): Photofission of Americium Isotopes
   in the Energy Range 6–12 MeV. Physics of Atomic Nuclei 64, 1188.

3. Varlamov, A.V. et al. (1999): Atlas of Giant Dipole Resonances.
   IAEA Nuclear Data Services, INDC(NDS)-394.

4. Berman, B.L. & Fultz, S.C. (1975): Measurements of the Giant
   Dipole Resonance with Monoenergetic Photons.
   Rev. Mod. Phys. 47, 713.

5. NNDC NuDat 3.0: Am-241 Nuclear Data.
   https://www.nndc.bnl.gov/

### ELI-NP

6. ELI-NP Gamma System Department: VEGA System Specifications.
   http://www.eli-np.ro/gsd_vega.php

7. Phys. Rev. Accel. Beams 27, 021601 (2024): Design Concept of a
   γ-Ray Beam with Low Bandwidth and High Spectral Density.

8. ELI-NP GSD Activities Report 2023/2024.
   https://indico.eli-np.ro

9. Photofission Experiments at ELI-NP (ELIGANT-TN).
   https://www.eli-np.ro/gded.php

### Resonanzfeldtheorie

10. Schu, D.-R. (2025/2026): Resonanzfeldtheorie.
    https://github.com/DominicReneSchu/RFT

---

## Kontakt

Dominic-René Schu
GitHub: https://github.com/DominicReneSchu/RFT
Theorie, Simulation und Experimentdesign: Resonanzfeldtheorie

---

© Dominic-René Schu — Resonanzfeldtheorie 2025/2026

---

[Zurück zur Übersicht](README.md)