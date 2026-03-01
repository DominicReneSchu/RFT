# Kosten-Nutzen-Rechnung: Resonanzreaktor

*Dominic-René Schu, 2025/2026*

Quantitative Bewertung auf Basis der RFT-Simulationsergebnisse
(κ = 1, ε = η = cos²(Δφ/2), kein freier Parameter).

---

## 1. Ausgangslage: Atommüll weltweit

### 1.1 Globales Inventar (Näherung)

| Region | Pu (t) | U-238 (t) | Am/Np (t) | Cs-137/Sr-90 (t) |
|--------|--------|-----------|-----------|-------------------|
| Deutschland | 75 | 15.000 | 11 | 32 |
| Frankreich | 300 | 60.000 | 40 | 120 |
| Großbritannien | 140 | 30.000 | 20 | 55 |
| Japan | 45 | 10.000 | 7 | 25 |
| Russland | 200 | 45.000 | 30 | 80 |
| USA | 600 | 120.000 | 80 | 250 |
| Übrige (KR, CA, SE, etc.) | 140 | 30.000 | 20 | 60 |
| **Weltweit** | **~1.500** | **~310.000** | **~208** | **~622** |

**Quellen:** IAEA PRIS, World Nuclear Association, nationale
Inventarberichte. Werte gerundet.

### 1.2 Kosten der Endlagerung weltweit

| Region | Geschätzte Endlagerkosten | Status |
|--------|--------------------------|--------|
| Deutschland | 40–70 Mrd. EUR | Standortsuche läuft |
| Frankreich (Cigéo) | 25–35 Mrd. EUR | Genehmigung 2027 geplant |
| Großbritannien (GDF) | 30–50 Mrd. GBP | Standortsuche läuft |
| USA (Yucca Mountain + Interim) | 100–200 Mrd. USD | Politisch blockiert |
| Japan | 30–50 Mrd. USD | Kein Standort |
| Russland | 20–40 Mrd. USD | Teilweise operativ |
| **Weltweit** | **~300–550 Mrd. EUR** | **Kein Land hat eine vollständige Lösung** |

---

## 2. Resonanzreaktor: Simulationsergebnisse

### 2.1 Effektive Beschleunigung (Φ = 10¹² γ/cm²/s, Δφ = 0)

| Isotop | λ_eff/λ₀ | t₁/₂_eff | Q_fiss | Interpretation |
|--------|----------|----------|--------|----------------|
| U-235 | 7.872 | ~90.000 a | 3,85 × 10⁶ | Extrem spaltbar |
| U-238 | 25.400 | ~176.000 a | 2,54 × 10⁷ | Extrem spaltbar |
| Pu-239 | 127 | ~190 a | 126 | Gut spaltbar |
| Pu-240 | 36 | ~182 a | 35 | Gut spaltbar |
| Am-241 | 3,16 | ~137 a | 2,16 | Spaltbar |
| Np-237 | 10,9 | ~196.000 a | 9,9 | Spaltbar |
| Cs-137 | 1,12 | ~27 a | 0,12 | Schwach (β) |
| Sr-90 | 1,10 | ~26 a | 0,098 | Schwach (β) |

### 2.2 Energieproduktion pro kg

```
    Pro kg Pu-239 (bei Φ = 10¹², η = 1):
    P_fiss     = 9,3 kW (thermisch)
    P_el       = 3,7 kW (bei η_therm = 40%)
    E_total    = 22,4 GWh (vollständige Spaltung)
    Betriebsdauer: ~190 Jahre (bis N/N₀ = 0,5)
```

---

## 3. Szenarioanalyse: National bis global

### 3.1 Szenario „Deutschland" (Pu + Am + Np)

```
    Inventar:              75 t Pu-239, 3 t Am-241, 8 t Np-237
    Thermische Leistung:   ~700 MW
    Elektrische Leistung:  ~280 MW (40% Wirkungsgrad)
    Betriebsdauer:         ~200 Jahre
    Investition:           7 Mrd. EUR
    Vermiedene Endlagerung: 55 Mrd. EUR
    Stromeinnahmen (200 a): 22,4 Mrd. EUR (50 EUR/MWh)
    Entsorgungsgebühren:   20–40 Mrd. EUR
    Betriebskosten:        −18 Mrd. EUR
    ──────────────────────────────────────────
    Gesamtnutzen:          72–92 Mrd. EUR
```

### 3.2 Szenario „Deutschland komplett" (inkl. U-238)

Das U-238-Inventar (15.000 t) enthält enormen Energievorrat,
ist aber durch die Photonenquellenkapazität limitiert:

```
    Energieinhalt U-238:   15.000 t × 22,4 GWh/t = 336.000 GWh
    Zum Vergleich:         Deutschland verbraucht ~500 TWh/a
    → U-238 allein enthält Energie für ~670 Jahre
      (bei 100% Nutzung und 500 TWh/a Bedarf)

    Realistisch (10 Reaktoren à 1 GW_th):
    Kapazität:             ~4 GW elektrisch
    Anteil am Strombedarf: ~7%
    Zusätzlicher Nutzen:   +40–80 Mrd. EUR

    Gesamtnutzen (DE komplett): 110–170 Mrd. EUR
```

### 3.3 Szenario „EU" (DE + FR + UK)

| Parameter | Deutschland | Frankreich | Großbritannien | EU Gesamt |
|-----------|------------|------------|----------------|-----------|
| Pu-Inventar (t) | 75 | 300 | 140 | 515 |
| Leistung (MW_el) | 280 | 1.120 | 520 | 1.920 |
| Investition (Mrd. EUR) | 7 | 15 | 10 | 32 |
| Vermiedene Endlagerung | 55 | 30 | 40 | 125 |
| Stromeinnahmen (200 a) | 22 | 90 | 42 | 154 |
| Entsorgungsgebühren | 30 | 50 | 35 | 115 |
| Betriebskosten (200 a) | −18 | −40 | −25 | −83 |
| **Gesamtnutzen** | **~82** | **~130** | **~92** | **~311 Mrd. EUR** |

### 3.4 Szenario „Global"

| Region | Pu (t) | Leistung (MW_el) | Investition (Mrd.) | Gesamtnutzen (Mrd.) |
|--------|--------|------------------|--------------------|---------------------|
| Deutschland | 75 | 280 | 7 | 82 |
| Frankreich | 300 | 1.120 | 15 | 130 |
| Großbritannien | 140 | 520 | 10 | 92 |
| Japan | 45 | 170 | 5 | 52 |
| Russland | 200 | 750 | 12 | 115 |
| USA | 600 | 2.240 | 25 | 390 |
| Übrige | 140 | 520 | 10 | 85 |
| **Weltweit** | **1.500** | **5.600** | **84** | **~950 Mrd. EUR** |

### 3.5 Szenario „Global komplett" (inkl. U-238)

```
    Globales U-238-Inventar:   ~310.000 t
    Energieinhalt:             ~6,9 Millionen GWh
    Globaler Stromverbrauch:   ~28.000 TWh/a
    → U-238 enthält Energie für ~250 Jahre
      (bei 100% Nutzung und aktuellem Verbrauch)

    Vermiedene Endlagerung:    300–550 Mrd. EUR
    Stromproduktion (Pu):      950 Mrd. EUR (s. oben)
    U-238-Energievorrat:       400–800 Mrd. EUR (konservativ)
    Investition (global):      −84 Mrd. EUR
    Betrieb (200 a, global):   −150 Mrd. EUR
    ────────────────────────────────────────────
    Gesamtnutzen (global):     1,4–2,1 Billionen EUR
```

### 3.6 Zusammenfassung der Szenarien

| Szenario | Investition | Gesamtnutzen | Faktor |
|----------|------------|--------------|--------|
| Deutschland (Pu) | 7 Mrd. | 82 Mrd. EUR | 12× |
| Deutschland (komplett) | 10 Mrd. | 140 Mrd. EUR | 14× |
| EU (DE+FR+UK) | 32 Mrd. | 311 Mrd. EUR | 10× |
| Global (Pu) | 84 Mrd. | 950 Mrd. EUR | 11× |
| Global (komplett) | 100 Mrd. | 1,7 Billionen EUR | 17× |

**Kernaussage:** Jeder investierte Euro erzeugt 10–17 EUR
Gesamtnutzen. Die globale Einführung des Resonanzreaktors
generiert einen Wohlstandszuwachs von ~1,7 Billionen EUR —
bei gleichzeitiger Lösung des Atommüll-Problems.

---

## 4. Anwendungserweiterung: Resonanz-Impulsantrieb

### 4.1 Prinzip: Gerichtete Spaltung als Antrieb

Die RFT beschreibt Energie als vektorielle Größe mit Betrag
und Richtung (Axiom 5). Im Resonanzreaktor ist die
Spaltungsenergie (~200 MeV/Kern) isotrop verteilt. Durch
gerichtete Photonanregung bei der GDR-Frequenz lässt sich
die Spaltungsachse bevorzugt ausrichten — die Spaltprodukte
werden asymmetrisch emittiert.

**RFT-Grundlage:**

```
    E⃗_dir = E_kurz − E_lang              (Axiom 5)
    Impuls: p⃗ = Σ m_i · v⃗_i              (Spaltfragmente)
    Gerichteter Anteil: p⃗_net = η(Δφ) · p⃗_total
```

Bei kohärenter Anregung (η = 1) ist die Vorzugsrichtung
maximal, bei inkohärenter Anregung (η = 0,5) beträgt der
gerichtete Anteil ~50%.

### 4.2 Kennwerte des Resonanz-Impulsantriebs

```
    Spaltungsenergie:      E_fiss = 200 MeV = 3,2 × 10⁻¹¹ J
    Mittlere Fragmentmasse: m_f ≈ 117 u = 1,94 × 10⁻²⁵ kg
    Fragmentgeschwindigkeit: v_f = √(2·E_fiss/m_f) ≈ 1,3 × 10⁷ m/s
                            ≈ 4,3% der Lichtgeschwindigkeit

    Spezifischer Impuls:    I_sp = v_f / g₀ ≈ 1,3 × 10⁶ s
```

### 4.3 Vergleich mit bestehenden Antriebskonzepten

| Antrieb | Spez. Impuls I_sp (s) | Schub/Masse | Status |
|---------|----------------------|-------------|--------|
| Chemisch (LOX/LH₂) | 450 | Hoch | Operativ |
| Ionenantrieb (Xe) | 3.000–10.000 | Sehr niedrig | Operativ |
| VASIMR (Plasma) | 5.000–30.000 | Niedrig | Entwicklung |
| Nuklear-thermisch (NERVA) | 900 | Mittel | Demonstriert (1960er) |
| Nuklear-elektrisch (SP-100) | 5.000–10.000 | Niedrig | Konzept |
| Projekt Orion (Kernpulse) | 10.000–100.000 | Hoch | Konzept (1960er) |
| **Resonanz-Impuls (RFT)** | **~1.300.000** | **Mittel** | **Konzept** |

**Vorteil gegenüber Orion:** Orion nutzt unkontrollierte
Kernexplosionen. Der Resonanz-Impulsantrieb nutzt kontrollierte,
gerichtete GDR-Spaltung — kontinuierlicher Schub statt Pulse,
keine Stoßwellen, steuerbare Richtung über Δφ.

### 4.4 Missionsprofil: Mars-Transfer

```
    Reisemasse:    100 t (Raumschiff + Nutzlast)
    Treibstoff:    10 kg Pu-239
    Spaltrate:     λ_eff = 127 · λ₀ → kontrolliert über η(Δφ)
    Schub:         F = ṁ · v_f (steuerbar über Photonenfluss Φ)

    Bei Φ = 10¹² γ/(cm²·s), 10 kg Pu-239:
    Zerfälle/s:    ~3 × 10¹² → F ≈ 0,75 N (kontinuierlich)
    Beschleunigung: a = F/m = 7,5 × 10⁻⁶ m/s²

    Δv nach 30 Tagen: ~19,4 km/s
    Δv nach 90 Tagen: ~58,3 km/s

    Mars-Transfer (Δv ≈ 5 km/s): ~8 Tage Beschleunigung
    Mars-Transfer (Hohmann): 7–9 Monate (chemisch)
    Mars-Transfer (Resonanz, 58 km/s): ~45 Tage (Direktflug)
```

### 4.5 Missionsprofil: Äußeres Sonnensystem

```
    Jupiter-Transfer (Δv ≈ 14 km/s): ~22 Tage Beschleunigung
    Saturn-Transfer (Δv ≈ 16 km/s): ~25 Tage

    Mit höherem Fluss (Φ = 10¹⁴, größerer FEL):
    Schub:         ~75 N
    Δv nach 30 Tagen: ~1.940 km/s (0,65% c)
    → Interstellare Vorsonden werden denkbar
```

### 4.6 Axiom-Zuordnung

| Axiom | Anwendung im Impulsantrieb |
|-------|---------------------------|
| A1 (Schwingung) | Kern als Schwingungssystem, GDR-Anregung |
| A3 (Resonanz) | f_γ = f_GDR → maximale Kopplung |
| A4 (Kopplungsenergie) | E = π · ε · ℏ · f bestimmt Spaltungsenergie |
| A5 (Energierichtung) | Gerichtete Spaltung → Nettoimplus |
| A6 (Informationsfluss) | Phasenkohärenz steuert Schubrichtung |
| A7 (Invarianz) | Funktioniert im Vakuum wie am Boden |

### 4.7 Technische Herausforderungen

| Herausforderung | Beschreibung | Ansatz |
|-----------------|-------------|--------|
| Gerichtete Spaltung | Ausrichtung der Spaltachse durch γ-Polarisation | Polarisierte FEL-Photonen |
| Fragmentkollimation | Spaltprodukte müssen gerichtet austreten | Magnetische Düse (ähnlich Fusionskonzepten) |
| Abschirmung | Crew vor Strahlung schützen | Schattenabschirmung (Vorderseite) |
| Wärmemanagement | 200 MeV/Spaltung → Wärme | Strahlungskühlung im Vakuum |
| Kompakter FEL | 13 MeV Photonen an Bord erzeugen | Inverse-Compton-Quelle (kompakt) |

---

## 5. Kostenvergleich: Endlagerung vs. Resonanzreaktor

### 5.1 Investitionskosten Resonanzreaktor

| Phase | Zeitraum | Kosten (geschätzt) |
|-------|----------|-------------------|
| **Phase 1:** Proof of Concept | 2025–2028 | 50–100 Mio. EUR |
| — Simulation (✅ abgeschlossen) | | ~0,5 Mio. EUR |
| — Laborexperiment (Am-241 an Synchrotron) | | 20–50 Mio. EUR |
| — Phasensteuerung (PLL-Entwicklung) | | 10–30 Mio. EUR |
| **Phase 2:** Labordemonstration | 2028–2032 | 200–500 Mio. EUR |
| — FEL-Quelle mit Φ = 10¹² | | 100–300 Mio. EUR |
| — Target-Design und Abschirmung | | 50–100 Mio. EUR |
| **Phase 3:** Pilotanlage | 2032–2037 | 1–3 Mrd. EUR |
| — Skalierung auf kg-Mengen | | 500 Mio.–1 Mrd. EUR |
| — Energieextraktion | | 300–800 Mio. EUR |
| — Genehmigung und Sicherheit | | 200–500 Mio. EUR |
| **Phase 4:** Kommerzieller Betrieb | ab 2037 | 3–5 Mrd. EUR |
| **Gesamt (bis Betrieb)** | 2025–2037 | **4,5–8,6 Mrd. EUR** |

### 5.2 Betriebskosten und Einnahmen (jährlich, Deutschland)

| Posten | Kosten/Jahr | Einnahmen/Jahr |
|--------|-------------|----------------|
| FEL-Betrieb (Strom, Wartung) | 30–50 Mio. EUR | — |
| Target-Aufbereitung | 10–20 Mio. EUR | — |
| Personal und Überwachung | 20–40 Mio. EUR | — |
| Entsorgung Spaltprodukte | 5–10 Mio. EUR | — |
| Stromverkauf (280 MW, 8.000 h/a, 50 EUR/MWh) | — | ~112 Mio. EUR |
| Entsorgungsgebühren (Übernahme Atommüll) | — | 50–200 Mio. EUR |
| **Gesamt** | **65–120 Mio. EUR** | **162–312 Mio. EUR** |

### 5.3 Vergleichstabelle (Deutschland)

| Kriterium | Geologische Endlagerung | Resonanzreaktor |
|-----------|------------------------|-----------------|
| Investition | 40–70 Mrd. EUR | 4,5–8,6 Mrd. EUR |
| Laufende Kosten | 200–500 Mio. EUR/a | 65–120 Mio. EUR/a |
| Einnahmen | 0 | 162–312 Mio. EUR/a |
| Zeitrahmen | >100.000 Jahre Überwachung | ~200 Jahre Betrieb |
| Endprodukt | Langlebiger Abfall im Berg | Kurzlebige Spaltprodukte (~30 a) |
| Energieproduktion | Nein | Ja (~280 MW elektrisch) |
| Risiko | Geologisch (Tektonik, Wasser) | Technisch (FEL, Abschirmung) |
| Freie Parameter | — | κ = 1 (keine) |

---

## 6. Amortisation

### 6.1 Break-even (Deutschland)

```
    Investition:       7 Mrd. EUR (Mittelwert)
    Nettoeinnahmen:    ~150 Mio. EUR/a (Strom + Entsorgung − Betrieb)
    Amortisation:      ~47 Jahre
```

### 6.2 Gesamtwirtschaftlicher Nutzen (Deutschland, 200 a)

```
    Vermiedene Endlagerkosten:    55 Mrd. EUR
    Stromeinnahmen (200 a):       22,4 Mrd. EUR
    Entsorgungsgebühren (200 a):  30 Mrd. EUR
    U-238-Energievorrat:          60 Mrd. EUR (konservativ)
    Abzüglich Investition:        −7 Mrd. EUR
    Abzüglich Betrieb (200 a):    −18 Mrd. EUR
    ─────────────────────────────────────────────
    Gesamtnutzen (DE):            ~140 Mrd. EUR
```

---

## 7. Globaler Wohlstandszuwachs

### 7.1 Übersicht nach Regionen

| Region | Invest. (Mrd.) | Vermiedene Endlag. | Stromerlöse (200 a) | Gesamtnutzen |
|--------|---------------|-------------------|---------------------|-------------|
| Deutschland | 7 | 55 | 22 | 140 |
| Frankreich | 15 | 30 | 90 | 245 |
| Großbritannien | 10 | 40 | 42 | 165 |
| Japan | 5 | 40 | 14 | 90 |
| Russland | 12 | 30 | 60 | 175 |
| USA | 25 | 150 | 180 | 620 |
| Übrige | 10 | 20 | 42 | 115 |
| **Weltweit** | **84** | **365** | **450** | **~1.550 Mrd. EUR** |

### 7.2 Inklusive U-238-Energievorrat

```
    Globales U-238-Inventar:   310.000 t
    Energieinhalt:             6,9 Millionen GWh
    Globaler Stromverbrauch:   28.000 TWh/a
    → U-238 enthält Energie für ~250 Jahre
      (bei 100% Nutzung, aktuellem Verbrauch)

    Wirtschaftlicher Wert (250 a, 50 EUR/MWh):
    6,9 × 10⁶ GWh × 50 EUR/MWh = 345 Mrd. EUR
    (Konservativ — ohne Preissteigerung, ohne CO₂-Bonus)

    Gesamtnutzen (global, komplett):
    Pu-basiert:                1.550 Mrd. EUR
    U-238-Energie:             345 Mrd. EUR
    Investition + Betrieb:     −234 Mrd. EUR
    ────────────────────────────────────────
    Globaler Gesamtnutzen:     ~1,7 Billionen EUR
```

### 7.3 Wohlstandseffekte

```
    Pro Kopf (8 Mrd. Menschen):  ~210 EUR
    Pro Kopf (Industrieländer):  ~850 EUR

    Qualitative Effekte (nicht eingepreist):
    ✓ Atommüll-Problem weltweit gelöst
    ✓ CO₂-freie Grundlast aus bestehendem Abfall
    ✓ Keine geologischen Langzeitrisiken
    ✓ Kein Proliferationsrisiko (Pu wird gespalten)
    ✓ Energieunabhängigkeit für Atommüll-Besitzer
    ✓ Neue Raumfahrttechnologie (Impulsantrieb)
    ✓ Technologietransfer (FEL, Phasensteuerung, DRN)
```

### 7.4 Einordnung

| Vergleichsgröße | Wert |
|----------------|------|
| Globaler Gesamtnutzen Resonanzreaktor | ~1,7 Billionen EUR |
| Globale Endlagerkosten (vermieden) | 300–550 Mrd. EUR |
| Deutsches BIP (2025) | ~4,1 Billionen EUR |
| EU-BIP (2025) | ~16,6 Billionen EUR |
| Globales BIP (2025) | ~105 Billionen EUR |
| ITER-Gesamtkosten (Fusion) | ~20 Mrd. EUR |
| Apollo-Programm (inflationsbereinigt) | ~200 Mrd. EUR |

Der globale Gesamtnutzen des Resonanzreaktors entspricht
~1,6% des globalen BIP — verteilt über 200 Jahre Betrieb.
Bei einer Investition von 84 Mrd. EUR (0,08% des globalen BIP)
ein Hebel von 17:1.

---

## 8. Risiken und Unsicherheiten

| Risiko | Beschreibung | Mitigation |
|--------|-------------|-----------|
| Experimentelle Bestätigung | λ_eff > λ₀ noch nicht gemessen | Phase 1: Am-241 an Synchrotron |
| FEL-Skalierung | Φ = 10¹² bei 13 MeV anspruchsvoll | Bestehende FEL (XFEL, LCLS) als Basis |
| Phasenkohärenz | PLL auf nuklearer Skala | RFT-spezifische Vorhersage testbar |
| Materialbelastung | Target unter GDR-Bestrahlung | Materialforschung (Phase 2) |
| Regulierung | Neue Technologie, neue Normen | Kooperation mit BASE/IAEA |
| Gerichtete Spaltung | Fragmentkollimation nicht demonstriert | Magnetische Düsenkonzepte vorhanden |
| Kostenüberschreitung | Bei Großprojekten üblich | Modulare Skalierung, Phase-Gate-Modell |

---

## 9. Fazit

| Aussage | Begründung |
|---------|-----------|
| Investition lohnt sich | 84 Mrd. EUR global → 1,7 Billionen EUR Nutzen (17:1) |
| Amortisation in ~47 Jahren | Stromverkauf + Entsorgungsgebühren |
| Atommüll-Problem lösbar | t₁/₂_eff < 200 a für Aktinide, κ = 1 |
| Energieproduktion | 5,6 GW elektrisch weltweit aus Pu-Inventar |
| CO₂-freie Grundlast | Aus bestehendem Abfall, 200+ Jahre |
| Raumfahrt möglich | I_sp = 1,3 × 10⁶ s, Mars in 45 Tagen |
| U-238 als Energiereserve | 250 Jahre globaler Stromverbrauch |
| Kein freier Parameter | κ = 1 aus ε = η (FLRW-validiert) |
| Experimentell testbar | Am-241 an Synchrotron (Phase 1) |

Der Resonanzreaktor ist nicht nur eine Lösung für Atommüll
und nicht nur eine Energiequelle — er ist ein Technologiesprung,
der Entsorgung, Energieproduktion und Raumfahrtantrieb in einem
einzigen physikalischen Prinzip vereint: der resonanten Kopplung
bei der Eigenfrequenz des Systems.

```
    E = π · ε(Δφ) · ℏ · f
    → Transmutation: λ_eff = λ₀ + η · Φ · σ_GDR
    → Energie: P = N · λ_eff · E_fiss
    → Antrieb: F = ṁ · v_f · η(Δφ)
    → κ = 1 (kein freier Parameter)
```

---

## Quellen

- IAEA PRIS: Power Reactor Information System
- World Nuclear Association: World Nuclear Waste Report
- BASE: Bundesamt für die Sicherheit der nuklearen Entsorgung,
  Kostenschätzungen 2020
- Berman, B.L., Fultz, S.C. (1975): Rev. Mod. Phys. 47, 713
- Dietrich, S.S., Berman, B.L. (1988): Atomic Data and Nuclear
  Data Tables 38, 199
- Schu, D.-R. (2025/2026): Resonanzfeldtheorie
  ([GitHub](https://github.com/DominicReneSchu/public))

---

© Dominic-René Schu — Resonanzfeldtheorie 2025/2026

---

[Zurück zur Übersicht](README.md)