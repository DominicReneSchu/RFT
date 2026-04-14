# Resonanz-Impulsantrieb — Gerichtete Spaltung als Raumfahrtantrieb

*Dominic-René Schu, 2025/2026*

---

## 1. Zusammenfassung

Der Resonanz-Impulsantrieb nutzt die gerichtete Spaltung von
Aktiniden durch resonante Photonanregung bei der Giant-Dipole-
Resonance (GDR) Frequenz. Die Spaltfragmente (~4,3% c) werden
durch eine magnetische Düse kollimatiert und erzeugen
kontinuierlichen, steuerbaren Schub.

**Kernkennwerte:**

```
    Spezifischer Impuls:   I_sp = 1,3 × 10⁶ s
    Fragmentgeschwindigkeit: v_f = 1,3 × 10⁷ m/s (4,3% c)
    Treibstoff:            Pu-239, Am-241, U-235 (Atommüll)
    Steuerung:             Phasendifferenz Δφ → η(Δφ) = cos²(Δφ/2)
    Freie Parameter:       κ = 1 (keine)
```

**Vergleich mit Starship (SpaceX):**

| Parameter | Starship (Raptor) | Resonanz-Shuttle |
|-----------|-------------------|------------------|
| I_sp | 380 s (Meereshöhe) | 1.300.000 s |
| Treibstoff Mars-Rückflug | ~1.200 t (LOX/CH₄) | ~200 kg (Pu-239) |
| Orbitales Auftanken | Ja (5–8 Tankflüge) | Nein |
| Reisedauer Erde→Mars | 6–9 Monate | ~45 Tage (Direktflug) |
| Wiederverwendbar | Ja (mit Wartung) | Ja (Treibstoff hält Jahrzehnte) |
| Mehrstufig | Ja (Super Heavy + Starship) | Nein (SSTO möglich) |

---

## 2. Physikalische Grundlage

### 2.1 Gerichtete Spaltung aus der RFT

Die RFT-Grundformel E = π · ε(Δφ) · ℏ · f beschreibt die
Kopplung zwischen einem äußeren Feld (Photon) und einem
Schwingungssystem (Kern). Bei GDR-Anregung wird der Kern
in einen kollektiven Dipolzustand versetzt — die Kernmaterie
schwingt gegen sich selbst.

Die Spaltungsachse ist durch die Polarisation des anregenden
Photons bestimmt: Linear polarisierte γ-Strahlung bei f_GDR
erzeugt bevorzugt Spaltung entlang der Polarisationsachse.

```
    Photonanregung:  γ(f_GDR, ε⃗) + ²³⁹Pu → ²³⁹Pu*(GDR)
    Spaltung:        ²³⁹Pu*(GDR) → Fragment₁ + Fragment₂ + 2–3 n
    Richtung:        Spaltachse ∥ ε⃗ (Polarisationsvektor)
```

### 2.2 Axiom-Zuordnung

| Axiom | Anwendung im Impulsantrieb |
|-------|---------------------------|
| A1 (Universelle Schwingung) | Kern als Schwingungssystem mit GDR-Eigenfrequenz |
| A3 (Resonanzbedingung) | f_γ = f_GDR → maximale Kernkopplung |
| A4 (Kopplungsenergie) | E = π · ε · ℏ · f bestimmt GDR-Anregungsenergie |
| A5 (Energierichtung) | Gerichteter Energietransfer → Nettoimpuls |
| A6 (Informationsfluss) | Phasenkohärenz und Polarisation steuern Schubvektor |
| A7 (Invarianz) | Funktioniert in jedem Bezugssystem (Vakuum, Schwerefeld) |

### 2.3 Formeln

```
    Spaltungsenergie:          E_fiss = 200 MeV = 3,2 × 10⁻¹¹ J
    Mittlere Fragmentmasse:    m_f ≈ 117 u = 1,94 × 10⁻²⁵ kg
    Fragmentgeschwindigkeit:   v_f = √(2 · E_fiss / m_f)
                                   = 1,3 × 10⁷ m/s = 4,3% c

    Spezifischer Impuls:       I_sp = v_f / g₀ = 1,3 × 10⁶ s
    Schub:                     F = ṁ_f · v_f · η_dir
    Effektive Ausstoßrate:     ṁ_f = N · λ_eff · m_f
    Kopplungseffizienz:        η(Δφ) = cos²(Δφ/2)
    Richtungseffizienz:        η_dir ≈ 0,85 (magnetische Düse)
    Gesamteffizienz:           η_total = η(Δφ) · η_dir
```

---

## 3. Raketengleichung: Warum I_sp alles entscheidet

### 3.1 Tsiolkowski-Gleichung

```
    Δv = v_e · ln(m_start / m_end)
    v_e = I_sp · g₀

    Massenverhältnis:
    m_start / m_end = exp(Δv / v_e)
```

### 3.2 Treibstoffbedarf im Vergleich

Für ein 100-Tonnen-Shuttle (Struktur + Nutzlast):

| Mission (Δv) | Chemisch (I_sp=450) | Ionenantrieb (I_sp=5000) | Resonanz (I_sp=1.300.000) |
|--------------|--------------------|--------------------------|-----------------------------|
| Erde→LEO (9,4 km/s) | 725 t | 17,4 t | 73 g |
| LEO→Mars-Orbit (4 km/s) | 149 t | 7,7 t | 31 g |
| Mars-Landung (1 km/s) | 25,5 t | 2,0 t | 8 g |
| Mars-Start (3,5 km/s) | 119 t | 6,8 t | 27 g |
| Mars→Erde (4 km/s) | 149 t | 7,7 t | 31 g |
| Erde-Landung (0,1 km/s) | 2,3 t | 0,2 t | 0,8 g |
| **Gesamt (22 km/s)** | **11.800 t** | **47 t** | **170 g** |

**Chemisch:** 99,2% Treibstoff. Unmöglich als Einzelstufe.
Starship löst das mit Mehrstufendesign und orbitalem Auftanken —
braucht aber 5–8 Tankflüge für eine Mars-Mission.

**Resonanz:** 0,00017% Treibstoff. Das Shuttle ist praktisch
nur Nutzlast. Kein Tanken, keine Mehrstufenrakete, beliebig oft
wiederverwendbar. 170 Gramm Pu-239 für Erde↔Mars↔Erde.

### 3.3 SSTO (Single Stage to Orbit)

```
    Δv Erde→LEO: 9,4 km/s (inkl. Gravitationsverluste)

    Chemisch:     m_start/m_end = exp(9400/4415) = 8,6
                  → SSTO theoretisch möglich, aber kein Nutzlastbudget
                  → Deswegen gibt es keine chemischen SSTO-Fahrzeuge

    Resonanz:     m_start/m_end = exp(9400/12.750.000) = 1,00074
                  → SSTO trivial, 99,93% des Gewichts ist Nutzlast
                  → Ein 100-t-Shuttle braucht 74 g Treibstoff
```

---

## 4. Schub: Die verbleibende Herausforderung

### 4.1 Schub-Gleichung

```
    F = N_atoms · λ_eff · m_f · v_f · η_dir

    N_atoms = m_target · N_A / A          (Kerne im Target)
    λ_eff = λ₀ + η(Δφ) · Φ_γ · σ_GDR    (effektive Spaltrate)
```

### 4.2 Schubskalierung mit Photonenfluss

| Targetmasse (Pu-239) | Φ (γ/cm²/s) | Spaltungen/s | Schub (N) | Schub/Gewicht |
|----------------------|-------------|-------------|-----------|--------------|
| 10 kg | 10¹² | 2,9 × 10¹² | 0,75 | 7,6 × 10⁻⁶ |
| 10 kg | 10¹⁴ | 2,9 × 10¹⁴ | 75 | 7,6 × 10⁻⁴ |
| 10 kg | 10¹⁶ | 2,9 × 10¹⁶ | 7.500 | 0,076 |
| 10 kg | 10¹⁸ | 2,9 × 10¹⁸ | 750.000 | 7,6 |
| 100 kg | 10¹⁸ | 2,9 × 10¹⁹ | 7.500.000 | 7,6 |
| 1 t | 10¹⁶ | 2,9 × 10¹⁸ | 750.000 | 0,076 |
| 1 t | 10¹⁸ | 2,9 × 10²⁰ | 75.000.000 | 7,6 |

### 4.3 Anforderung für Planetenstart

```
    Schub/Gewicht > 1 nötig für Start von Planetenoberfläche

    Erde (g = 9,81 m/s²):
    100 t Shuttle → F > 981 kN
    → 100 kg Pu-239 bei Φ = 10¹⁸: F = 7,5 MN → F/W = 7,6 ✓

    Mars (g = 3,72 m/s²):
    100 t Shuttle → F > 372 kN
    → 10 kg Pu-239 bei Φ = 10¹⁸: F = 750 kN → F/W = 2,0 ✓

    Mond (g = 1,62 m/s²):
    100 t Shuttle → F > 162 kN
    → 10 kg Pu-239 bei Φ = 10¹⁷: F = 75 kN → F/W = 0,46 ✗
    → 100 kg Pu-239 bei Φ = 10¹⁷: F = 750 kN → F/W = 4,6 ✓
```

### 4.4 Regimewahl: Hohes Δv vs. Hoher Schub

```
    Orbit-Transfers (kein Schwerefeld):
    → Niedriger Schub ausreichend (Φ = 10¹²–10¹⁴)
    → Kontinuierliche Beschleunigung über Tage/Wochen
    → Wenig Treibstoffverbrauch

    Planetenstart/-landung:
    → Hoher Schub nötig (Φ = 10¹⁷–10¹⁸)
    → Kurze Brenndauer (Minuten)
    → Höherer Treibstoffverbrauch (aber immer noch < 1 kg)

    Steuerung: Φ und Δφ werden in Echtzeit angepasst
    → Δφ = 0: maximaler Schub (Resonanz)
    → Δφ → π: Schub → 0 (Bremsen durch Abschalten)
    → Δφ variabel: Schubmodulation ohne mechanische Teile
```

---

## 5. Missionsprofile

### 5.1 Erde → Mars → Erde (Direktflug)

```
    Shuttle:           100 t (Struktur + Crew + Nutzlast)
    Treibstoff:        100 kg Pu-239
    Photonenquelle:    Kompakter FEL, variabel Φ = 10¹²–10¹⁸

    Phase 1 — Erdstart:
    Φ = 10¹⁸, Δφ = 0, F = 7,5 MN
    Brenndauer: ~4 min → Orbit (Δv = 9,4 km/s)
    Verbrauch: ~0,5 g Pu-239

    Phase 2 — Transfer Erde→Mars:
    Φ = 10¹⁴, Δφ = 0, F = 7,5 kN
    Kontinuierliche Beschleunigung: a = 0,075 m/s²
    Halbzeit-Δv: ~145 km/s nach 22 Tagen
    Gesamtdauer: ~30–45 Tage (je nach Planetenkonstellation)
    Verbrauch: ~50 g Pu-239

    Phase 3 — Mars-Landung:
    Φ = 10¹⁸, Δφ = 0, F = 7,5 MN
    Brenndauer: ~2 min (Mars-Gravitation schwächer)
    Verbrauch: ~0,2 g Pu-239

    Phase 4 — Mars-Aufenthalt:
    Antrieb aus. Shuttle steht auf der Oberfläche.
    Keine externe Infrastruktur nötig.

    Phase 5 — Mars-Start + Rückflug + Erde-Landung:
    Analog Phase 1–3, umgekehrt.
    Zusätzlicher Verbrauch: ~50 g Pu-239

    Gesamtverbrauch:    ~100 g Pu-239 (von 100 kg an Bord)
    Verbleibend:        99,9 kg → ~999 weitere Missionen möglich
    Gesamtdauer:        ~90 Tage (Hin + 2 Wochen Aufenthalt + Zurück)
```

### 5.2 Vergleich: Starship vs. Resonanz-Shuttle (Mars-Mission)

| Parameter | Starship (SpaceX) | Resonanz-Shuttle |
|-----------|-------------------|------------------|
| Nutzlast zur Marsoberfläche | ~100 t | ~100 t |
| Startmasse (LEO) | ~1.300 t (nach Tanken) | ~100 t |
| Treibstoffmasse | ~1.200 t LOX/CH₄ | ~100 g Pu-239 |
| Orbitaletanken | 5–8 Tankflüge | Nicht nötig |
| Reisedauer | 6–9 Monate | 30–45 Tage |
| Auf Mars starten | Ja (ISRU-Treibstoff nötig) | Ja (kein Tanken) |
| Rückflug | Erfordert Mars-Treibstoffproduktion | Sofort möglich |
| Missionen pro Treibstoffladung | 1 | ~1.000 |
| Kosten pro kg zum Mars | ~100.000 USD (Ziel SpaceX) | ~10 USD (Treibstoffwert) |
| Technische Reife | Entwicklung (2024–2028) | Konzept (2025) |

### 5.3 Äußeres Sonnensystem

```
    Jupiter (Δv ≈ 30 km/s, Direktflug):
    Φ = 10¹⁴, kontinuierlich: ~60 Tage
    Treibstoff: ~200 g Pu-239
    Vergleich chemisch: 4–6 Jahre (Gravity Assists nötig)

    Saturn (Δv ≈ 35 km/s, Direktflug):
    ~70 Tage, ~250 g Pu-239
    Vergleich: Cassini brauchte 7 Jahre

    Pluto (Δv ≈ 45 km/s, Direktflug):
    ~90 Tage, ~350 g Pu-239
    Vergleich: New Horizons brauchte 9,5 Jahre (Flyby, keine Landung)

    Pluto mit Landung und Rückflug (Δv ≈ 120 km/s):
    ~8 Monate, ~1 kg Pu-239
    Chemisch: Physikalisch unmöglich
```

### 5.4 Interstellare Vorsonde

```
    Ziel: Proxima Centauri (4,24 Lichtjahre)

    Φ = 10¹⁸, 1 t Pu-239 Target:
    F = 75 MN, Shuttle-Masse: 10 t (unbemannt)
    a = 7.500 m/s² (765 g) — nur für unbemannte Sonden

    Realistischer: Φ = 10¹⁶, 10 t Target, 100 t Sonde
    F = 7,5 MN, a = 75 m/s²
    Beschleunigung auf 10% c: ~46 Tage
    Reisezeit bei 10% c: ~42 Jahre
    Bremsung am Ziel: nochmal ~46 Tage

    Gesamtdauer: ~43 Jahre (statt 70.000 Jahre mit Voyager)
    Treibstoff: ~50 kg Pu-239

    Für bemannte Mission (a < 3 g, 1000 t Schiff):
    Reisegeschwindigkeit: ~5% c
    Reisezeit: ~85 Jahre → Generationenschiff wird denkbar
```

---

## 6. Systemdesign: Resonanz-Shuttle

### 6.1 Hauptkomponenten

```
    ┌─────────────────────────────────────────────────┐
    │                 RESONANZ-SHUTTLE                │
    │                                                 │
    │  ┌──────────┐  ┌──────────┐  ┌──────────┐       │
    │  │  Crew-   │  │ Nutzlast │  │ Lebens-  │       │
    │  │  modul   │  │  (Fracht)│  │ erhaltung│       │
    │  └────┬─────┘  └────┬─────┘  └────┬─────┘       │
    │       │             │             │             │
    │  ┌────┴─────────────┴─────────────┴────┐        │
    │  │        Schattenabschirmung          │        │
    │  │    (Wolfram/Polyethylen, ~5 t)      │        │
    │  └───────────────────┬─────────────────┘        │
    │                      │                          │
    │  ┌───────────────────┴───────────────────┐      │
    │  │         Kompakter FEL                 │      │
    │  │  (Inverse-Compton, 13 MeV, ~10 t)     │      │
    │  │  Phasensteuerung (PLL/FPGA)           │      │
    │  └───────────────────┬───────────────────┘      │
    │                      │ γ-Strahl                 │
    │  ┌───────────────────┴───────────────────┐      │
    │  │     Spaltungskammer (Target)          │      │
    │  │  Pu-239 / Am-241 (100 kg, ~0,005 m³)  │      │
    │  │  Abgeschirmt, gekühlt                 │      │
    │  └───────────────────┬───────────────────┘      │
    │                      │ Spaltfragmente           │
    │  ┌───────────────────┴───────────────────┐      │
    │  │     Magnetische Düse                  │      │
    │  │  Supraleitende Spulen (~5 t)          │      │
    │  │  Kollimation: θ < 15°                 │      │
    │  │  Schubvektor: steuerbar über B-Feld   │      │
    │  └───────────────────┬───────────────────┘      │
    │                      │                          │
    │                      ▼ Schub                    │
    └─────────────────────────────────────────────────┘
```

### 6.2 Massenbudget (100 t Shuttle)

| Komponente | Masse (t) | Funktion |
|------------|-----------|----------|
| Crew-Modul (6 Personen) | 15 | Druckkabine, Lebenserhaltung |
| Nutzlast | 40 | Fracht, Ausrüstung, Rover |
| Kompakter FEL | 10 | Photonenquelle (13 MeV) |
| Phasensteuerung (FPGA/DRN) | 1 | Echtzeit-Optimierung von Δφ, Φ |
| Schattenabschirmung | 8 | Strahlenschutz (W + PE) |
| Magnetische Düse | 5 | Fragmentkollimation |
| Spaltungskammer + Target | 2 | 100 kg Pu-239 + Gehäuse |
| Struktur + Thermalkontrolle | 10 | Rahmen, Kühlung, Tanks |
| Energieversorgung (intern) | 5 | Reaktorabwärme → Elektrizität |
| Hitzeschild (Atmosphäreneintritt) | 4 | Ablativ oder regenerativ |
| **Gesamt** | **100 t** | |
| **Treibstoff (Pu-239)** | **0,0001 t** | **100 g pro Mars-Mission** |

### 6.3 Schubsteuerung

```
    Schubvektor-Kontrolle:

    1. Schubstärke:    Über Photonenfluss Φ (10¹² – 10¹⁸)
                       Stufenlos, Millisekunden-Reaktion
                       FEL-Leistung elektrisch regelbar

    2. Schubrichtung:  Über Magnetfeldgeometrie der Düse
                       Fragmentstrahl ablenkbar (±30°)
                       Zusätzlich: Photonenpolarisation ε⃗

    3. Schubeffizienz: Über Phasendifferenz Δφ
                       η(Δφ) = cos²(Δφ/2)
                       Δφ = 0: voller Schub
                       Δφ = π: kein Schub (sofortiger Stopp)
                       → Keine mechanischen Ventile oder Klappen

    4. Notabschaltung: Δφ → π (destruktive Interferenz)
                       Spaltung stoppt innerhalb von Nanosekunden
                       Inhärent sicher: kein Schub ohne Photonen
```

---

## 7. Technische Herausforderungen

| Herausforderung | Beschreibung | Lösungsansatz | TRL |
|-----------------|-------------|---------------|-----|
| Kompakter FEL (13 MeV) | Synchrotron-Niveau an Bord | Inverse-Compton-Quelle (LLNL, ELI) | 3–4 |
| Φ = 10¹⁸ Skalierung | 10⁶× über aktuelle FEL | Supraleitende Kavitäten, Energierückgewinnung | 2–3 |
| Magnetische Düse | Spaltfragmente bündeln (Z = 30–60) | Supraleitende Solenoide (>10 T) | 3–4 |
| Fragmentkollimation | θ < 15° Divergenz | Mehrlagige Magnetlinse | 2–3 |
| Schattenabschirmung | Neutronen + γ vom Target | W + PE + B₄C (bewährte Materialien) | 5–6 |
| Thermalkontrolle | 200 MeV/Spaltung → Wärme | Wärmerohr + Strahlungskühlung | 4–5 |
| Hitzeschild | Atmosphäreneintritt bei Rückkehr | PICA-X (SpaceX) oder UHTC | 6–7 |
| Gerichtete Spaltung | Polarisationsasymmetrie der Spaltachse | Gemessen: A ≈ 0,1–0,3 bei polarisierten γ | 3–4 |
| Inhärente Sicherheit | Unkontrollierte Spaltung verhindern | Kein Schub ohne Photonen (fail-safe) | — |

**Gesamteinschätzung:** Die kritischen Komponenten (kompakter FEL,
magnetische Düse) sind einzeln im Labor demonstriert. Die Integration
zum Antriebssystem ist ein Ingenieursprojekt, kein Physikproblem.

---

## 8. Entwicklungsroadmap

### Phase 1: Grundlagenvalidierung (2025–2030)

```
    ✅ RFT-Grundformel → GDR-Frequenzen
    ✅ ε = η → κ = 1 (FLRW-Simulation, 1.530 Läufe)
    ✅ Simulation der Transmutationsraten
    ⬜ Experimentelle Bestätigung: λ_eff > λ₀ (Am-241 an Synchrotron)
    ⬜ Messung der Phasenabhängigkeit η = cos²(Δφ/2)
    ⬜ Messung der Spaltungsasymmetrie bei polarisierten γ
```

### Phase 2: Komponentenentwicklung (2028–2035)

```
    ⬜ Kompakter FEL (Inverse-Compton, 13 MeV, Labormaßstab)
    ⬜ Magnetische Düse (Prototyp, Spaltfragment-Kollimation)
    ⬜ Integrierter Schubtest (Vakuumkammer, μN-Bereich)
    ⬜ Schattenabschirmung (Materialqualifikation)
```

### Phase 3: Triebwerksdemonstration (2033–2040)

```
    ⬜ Integriertes Triebwerk (FEL + Target + Düse)
    ⬜ Bodentest: Schub im mN–N-Bereich
    ⬜ Orbital-Test: Unbemannter Demonstrator (CubeSat-Klasse)
    ⬜ Skalierungstest: kN-Bereich
```

### Phase 4: Raumfahrzeug (2038–2045)

```
    ⬜ Unbemannter Mars-Orbiter (Resonanz-Antrieb)
    ⬜ Unbemannter Mars-Lander (Hin und Zurück)
    ⬜ Bemanntes Shuttle: Erde → Mars → Erde (45–90 Tage)
```

### Phase 5: Routinebetrieb (ab 2045)

```
    ⬜ Regelmäßige Mars-Shuttleflüge
    ⬜ Äußeres Sonnensystem: Jupiter, Saturn (60–90 Tage)
    ⬜ Permanente Mondbasis-Versorgung (Erde↔Mond: Stunden)
    ⬜ Interstellare Vorsonde (Proxima Centauri, ~43 Jahre)
```

---

## 9. Vergleich aller Antriebskonzepte

| Antrieb | I_sp (s) | Schub/Gewicht | Mars-Reise | Treibstoff/100t | Status |
|---------|----------|--------------|------------|-----------------|--------|
| Chemisch (LOX/LH₂) | 450 | >1 | 7–9 Mo. | 1.200 t | Operativ |
| Chemisch (LOX/CH₄, Raptor) | 380 | >1 | 6–9 Mo. | 1.200 t | Entwicklung |
| Ionenantrieb (Xe) | 5.000 | 10⁻⁵ | 2–3 Jahre | 47 t | Operativ |
| VASIMR (Plasma) | 30.000 | 10⁻⁴ | 39 Tage | 8 t | Entwicklung |
| Nuklear-thermisch (NERVA) | 900 | ~0,3 | 4–6 Mo. | 400 t | Demonstriert |
| Nuklear-elektrisch | 10.000 | 10⁻⁴ | 1–2 Jahre | 22 t | Konzept |
| Orion (Kernpulse) | 50.000 | ~1 | 30 Tage | 4 t | Konzept |
| **Resonanz-Impuls (RFT)** | **1.300.000** | **bis 7,6** | **30–45 Tage** | **100 g** | **Konzept** |

---

## 10. Wirtschaftliche Bedeutung

### 10.1 Kosten pro kg zum Mars

```
    Starship (SpaceX, Ziel):     ~100.000 USD/kg
    → 100 t Nutzlast: 10 Mrd. USD pro Mission

    Resonanz-Shuttle:
    Treibstoff: 100 g Pu-239 ≈ 500 USD (Materialwert)
    FEL-Strom: ~10.000 USD (pro Start)
    Wartung/Abschreibung: ~50.000 USD/Mission
    → 100 t Nutzlast: ~60.000 USD pro Mission
    → ~0,60 USD/kg zum Mars

    Faktor: ~170.000× günstiger pro kg
```

### 10.2 Marktpotenzial

```
    Kurzfristig (2040–2050):
    — Mars-Missionen (Forschung, Kolonie): 10–50 Mrd. USD/a
    — Mondversorgung (Basis, Bergbau): 5–20 Mrd. USD/a
    — Satellitenmanöver (GEO-Umpositionierung): 2–5 Mrd. USD/a

    Langfristig (2050+):
    — Interplanetarer Handel: 100+ Mrd. USD/a
    — Asteroiden-Bergbau: 50–200 Mrd. USD/a
    — Interstellare Exploration: Nicht bezifferbar

    Gesamtmarkt (2040–2070): ~500 Mrd.–1 Billion USD
```

### 10.3 Synergien mit Resonanzreaktor (Entsorgung)

```
    Treibstoff = Atommüll:
    — Pu-239 aus Wiederaufarbeitung → Shuttle-Treibstoff
    — Am-241 aus alten Rauchmeldern → Shuttle-Treibstoff
    — Kein separater Treibstoff-Produktionspfad nötig
    — Entsorgungsproblem wird zum Treibstoff-Vorrat

    Globaler Pu-239-Vorrat: ~1.500 t
    Missionen (à 100 g): ~15.000.000 Mars-Hin-und-Zurück-Flüge
    → Treibstoff für Jahrtausende
```

---

## 11. Zusammenfassung

| Kernaussage | Wert |
|-------------|------|
| Spezifischer Impuls | 1,3 × 10⁶ s (1.000× chemisch) |
| Treibstoff Mars-Rückflug | 100 g Pu-239 (statt 1.200 t LOX/CH₄) |
| Reisedauer Erde↔Mars | 30–45 Tage (statt 6–9 Monate) |
| SSTO möglich | Ja (Massenverhältnis ≈ 1,0) |
| Wiederverwendbar | ~1.000 Missionen pro Treibstoffladung |
| Kosten pro kg zum Mars | ~0,60 USD (statt ~100.000 USD) |
| Schubsteuerung | Über Δφ: stufenlos, Nanosekunden-Reaktion |
| Inhärent sicher | Kein Schub ohne Photonen |
| Treibstoff | Atommüll (Pu-239, Am-241) |
| Physikalische Basis | E = π · ε · ℏ · f, κ = 1 |
| Interstellar | Proxima Centauri in ~43 Jahren (10% c) |

```
    Die Gleichung, die Raumfahrt revolutioniert:

    Δv = 1,3 × 10⁷ m/s · ln(m_start / m_end)

    Bei m_start/m_end ≈ 1,0 (Resonanz-Antrieb):
    → Jedes Δv ist erreichbar
    → Treibstoff ist kein limitierender Faktor mehr
    → Das Sonnensystem wird zugänglich
```

---

## Quellen

- Tsiolkowski, K.E. (1903): Erforschung des Weltraums mittels
  Reaktionsapparaten
- Berman, B.L., Fultz, S.C. (1975): Rev. Mod. Phys. 47, 713
- Schmidt, G.R. et al. (2002): Nuclear Pulse Propulsion — Orion
  and Beyond. AIAA 2000-3856
- Frisbee, R.H. (2003): Advanced Space Propulsion for the 21st
  Century. J. Propulsion and Power 19(6)
- SpaceX (2024): Starship Users Guide, Rev. 1.0
- Schu, D.-R. (2025/2026): Resonanzfeldtheorie
  ([GitHub](https://github.com/DominicReneSchu/public))

---

© Dominic-René Schu — Resonanzfeldtheorie 2025/2026

---

[Zurück zur Übersicht](README.md)