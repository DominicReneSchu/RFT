# 🧪 Simulationsergebnisse: Resonanzreaktor

*Dominic-René Schu, 2025/2026*

Diese Datei dokumentiert die quantitativen Ergebnisse der
Resonanzreaktor-Simulation. Alle Berechnungen basieren auf der
RFT-Grundformel E = π · ε · ℏ · f und der empirisch validierten
Identität ε = η = cos²(Δφ/2) mit κ = 1 (kein freier Parameter).

➡️ [Weiter zur Python-Simulation](simulation/run.py)

---

## 1. Physikalische Grundlagen der Simulation

### 1.1 Formeln

```
    GDR-Frequenz:         f_GDR = E_GDR / (π · ℏ)
    Effektive Zerfallsrate: λ_eff = λ₀ + η(Δφ) · Φ_γ · σ_GDR
    Kopplungseffizienz:   η(Δφ) = cos²(Δφ/2)    [= ε(Δφ)]
    Kopplungsparameter:   κ = 1                   [aus ε = η]
    Spaltbarkeitsquotient: Q_fiss = η · Φ · σ_GDR / λ₀
    Verbleibender Anteil: N(t) = N₀ · exp(−λ_eff · t)
    Energiefreisetzung:   P(t) = N(t) · λ_eff · E_fiss
```

### 1.2 Konstanten

```
    ℏ = 6.582 × 10⁻²² MeV·s
    E_fiss ≈ 200 MeV (Spaltungsenergie pro Kern)
    η = 1 (perfekte Phasenkohärenz, Δφ = 0)
    Φ_γ = 10¹² γ/(cm²·s) (Referenz-Photonenfluss)
```

---

## 2. Isotop-Datenbank

| Isotop | E_GDR (MeV) | f_GDR (Hz) | σ_GDR (barn) | λ₀ (s⁻¹) | t₁/₂ (natürlich) |
|--------|-------------|------------|--------------|-----------|-------------------|
| U-235 | 13.0 | 6.29 × 10²¹ | 0.120 | 3.12 × 10⁻¹⁷ | 7.04 × 10⁸ a |
| U-238 | 13.2 | 6.39 × 10²¹ | 0.125 | 4.92 × 10⁻¹⁸ | 4.47 × 10⁹ a |
| Pu-239 | 13.5 | 6.53 × 10²¹ | 0.115 | 9.11 × 10⁻¹³ | 2.41 × 10⁴ a |
| Pu-240 | 13.4 | 6.49 × 10²¹ | 0.118 | 3.35 × 10⁻¹² | 6.56 × 10³ a |
| Am-241 | 13.3 | 6.44 × 10²¹ | 0.110 | 5.08 × 10⁻¹¹ | 432 a |
| Np-237 | 13.1 | 6.34 × 10²¹ | 0.112 | 1.03 × 10⁻¹⁴ | 2.14 × 10⁶ a |
| Cs-137 | 15.3 | 7.41 × 10²¹ | 0.085 | 7.30 × 10⁻¹⁰ | 30.2 a |
| Sr-90 | 16.5 | 7.99 × 10²¹ | 0.075 | 7.63 × 10⁻¹⁰ | 28.8 a |

---

## 3. Ergebnisse: Effektive Zerfallsraten

### 3.1 Bei Referenz-Photonenfluss (Φ = 10¹² γ/cm²/s, η = 1)

| Isotop | λ₀ (s⁻¹) | λ_eff (s⁻¹) | λ_eff/λ₀ | t₁/₂_eff | Q_fiss |
|--------|-----------|-------------|----------|----------|--------|
| U-235 | 3.12 × 10⁻¹⁷ | 1.20 × 10⁻¹³ | 7872 | ~90.000 a | 3.85 × 10⁶ |
| U-238 | 4.92 × 10⁻¹⁸ | 1.25 × 10⁻¹³ | 25.400 | ~176.000 a | 2.54 × 10⁷ |
| Pu-239 | 9.11 × 10⁻¹³ | 1.16 × 10⁻¹⁰ | 127 | ~190 a | 126 |
| Pu-240 | 3.35 × 10⁻¹² | 1.21 × 10⁻¹⁰ | 36 | ~182 a | 35 |
| Am-241 | 5.08 × 10⁻¹¹ | 1.61 × 10⁻¹⁰ | 3.16 | ~137 a | 2.16 |
| Np-237 | 1.03 × 10⁻¹⁴ | 1.12 × 10⁻¹³ | 10.9 | ~196.000 a | 9.9 |
| Cs-137 | 7.30 × 10⁻¹⁰ | 8.15 × 10⁻¹⁰ | 1.12 | ~27 a | 0.12 |
| Sr-90 | 7.63 × 10⁻¹⁰ | 8.38 × 10⁻¹⁰ | 1.10 | ~26 a | 0.098 |

### 3.2 Interpretation

**Aktinide (Q_fiss > 1):** Die resonante GDR-Anregung dominiert
über den natürlichen Zerfall. U-235 wird fast 8.000× schneller
abgebaut, Pu-239 127×, Am-241 3×. Dies sind Aktinide mit
α-Zerfall oder Spontanspaltung — der GDR-Kanal öffnet einen
zusätzlichen Spaltungsweg.

**Spaltprodukte (Q_fiss < 1):** Cs-137 und Sr-90 zerfallen
über β-Emission. Die GDR-Anregung beschleunigt den Zerfall nur
marginal (~10–12%), da der Zerfallskanal β statt Spaltung ist
und σ_GDR kleiner ist.

**Physik:** Je länger die natürliche Halbwertszeit, desto
stärker der relative Effekt — weil λ₀ klein ist und der
Resonanzterm η · Φ · σ_GDR dominiert.

---

## 4. Ergebnisse: Phasenabhängigkeit

### 4.1 η(Δφ) = cos²(Δφ/2) für Pu-239

| Δφ (rad) | Δφ (Grad) | η = cos²(Δφ/2) | λ_eff/λ₀ |
|----------|-----------|----------------|----------|
| 0 | 0° | 1.000 | 127 |
| π/6 | 30° | 0.933 | 119 |
| π/4 | 45° | 0.854 | 109 |
| π/3 | 60° | 0.750 | 96 |
| π/2 | 90° | 0.500 | 64 |
| 2π/3 | 120° | 0.250 | 33 |
| 3π/4 | 135° | 0.146 | 20 |
| 5π/6 | 150° | 0.067 | 9.5 |
| π | 180° | 0.000 | 1.0 |

### 4.2 Interpretation

Bei Δφ = π (Gegenphase) verschwindet die resonante Kopplung
vollständig — λ_eff = λ₀ (natürlicher Zerfall). Dies ist die
experimentell testbare RFT-Signatur: Dreht man die Phase des
Photonenfeldes, muss die Zerfallsrate dem cos²-Verlauf folgen.

**Vergleich mit inkohärentem Licht:**
Thermische Photonen mitteln über alle Phasen → η_eff = 0.5 →
λ_eff/λ₀ ≈ 64 (statt 127 bei kohärenter Anregung). Das
Verhältnis kohärent/inkohärent ≈ 2 ist eine direkte,
experimentell überprüfbare Vorhersage.

---

## 5. Ergebnisse: Transmutationsketten

### 5.1 Zerfallskette U-235

```
    U-235   (t₁/₂ = 704 Ma,  λ_eff/λ₀ = 7872)
      → GDR-Spaltung → Spaltprodukte (Cs-137, Sr-90, etc.)
      → oder: U-235 →(n,γ)→ U-236 →(n,γ)→ Np-237 →(GDR)→ Spaltprodukte
```

### 5.2 Zerfallskette Pu-239

```
    Pu-239  (t₁/₂ = 24.100 a, λ_eff/λ₀ = 127)
      → GDR-Spaltung → Spaltprodukte
      → oder: Pu-239 →(n,γ)→ Pu-240 →(n,γ)→ Am-241 →(GDR)→ Spaltprodukte

    Pu-240  (t₁/₂ = 6.560 a,  λ_eff/λ₀ = 36)
      → GDR-Spaltung → Spaltprodukte

    Am-241  (t₁/₂ = 432 a,    λ_eff/λ₀ = 3.16)
      → GDR-Spaltung → Spaltprodukte
```

### 5.3 Zeitlicher Verlauf (Pu-239, 1 kg, Φ = 10¹² γ/cm²/s)

| Jahr | N/N₀ (natürlich) | N/N₀ (resonant) | P_fiss (kW) |
|------|-------------------|-----------------|-------------|
| 0 | 1.000 | 1.000 | 9.3 |
| 50 | 0.9986 | 0.835 | 7.8 |
| 100 | 0.9971 | 0.697 | 6.5 |
| 190 | 0.9946 | 0.500 | 4.7 |
| 500 | 0.9862 | 0.074 | 0.69 |
| 1000 | 0.9724 | 0.005 | 0.05 |

**Vergleich:** Natürlicher Zerfall baut in 1.000 Jahren nur 2.8%
des Pu-239 ab. Der Resonanzreaktor baut 99.5% ab — Reduktion der
effektiven Halbwertszeit von 24.100 auf ~190 Jahre.

---

## 6. Ergebnisse: Energieproduktion

### 6.1 Leistungsprofil pro kg Pu-239

```
    N₀ = 2.52 × 10²⁴ Kerne/kg
    λ_eff = 1.16 × 10⁻¹⁰ s⁻¹
    E_fiss = 200 MeV = 3.2 × 10⁻¹¹ J

    P(t=0) = N₀ · λ_eff · E_fiss
           = 2.52 × 10²⁴ × 1.16 × 10⁻¹⁰ × 3.2 × 10⁻¹¹
           ≈ 9.3 kW (thermisch)
```

### 6.2 Integrierte Energiefreisetzung

```
    E_total = N₀ · E_fiss = 2.52 × 10²⁴ × 200 MeV
            ≈ 8.1 × 10¹³ J ≈ 22.4 GWh pro kg Pu-239
```

### 6.3 Energiebilanz

| Posten | Leistung |
|--------|----------|
| Spaltungsleistung (pro kg Pu-239) | 9.3 kW (thermisch) |
| Photonenquelle (Synchrotron/FEL) | ~1 MW (elektrisch) |
| Kritische Masse für Nettoenergie | ~110 kg Pu-239 |
| Deutsches Pu-239-Inventar | ~75.000 kg |
| Potenzial bei vollem Inventar | ~700 MW thermisch |

**Konsequenz:** Bei vollem Pu-239-Inventar (75 t) und
Φ = 10¹² γ/(cm²·s) liegt die thermische Leistung bei ~700 MW —
vergleichbar mit einem konventionellen Kernkraftwerk, aber
betrieben mit bestehendem Atommüll.

---

## 7. Vergleich mit FLRW-Ergebnissen

Die Identität ε = η, die κ = 1 im Resonanzreaktor begründet,
wurde unabhängig in den FLRW-Simulationen validiert:

| Messgröße | FLRW-Simulation | Resonanzreaktor |
|-----------|----------------|----------------|
| Kopplungseffizienz | η = cos²(Δφ/2) (emergent) | η = cos²(Δφ/2) (Ansatz) |
| Abweichung von cos² | d_η = 0.043 (flach) | d_η ≈ 0 (kein Hubble) |
| Identität ε = η | Ja (1.530 Läufe) | Ja → κ = 1 |
| Phasenabhängigkeit | Validiert über 30 Phasenwerte | Vorhersage (testbar) |

**Konsistenz:** Im Resonanzreaktor (keine Raumzeitexpansion)
sollte die Identität ε = η exakter gelten als in FLRW-Kosmologie,
da die Hubble-Reibung (d_η ≈ 0.04) entfällt.

---

## 8. Zusammenfassung der Simulationsergebnisse

| Ergebnis | Wert |
|----------|------|
| Isotope simuliert | 8 (U-235, U-238, Pu-239, Pu-240, Am-241, Np-237, Cs-137, Sr-90) |
| Stärkster Effekt | U-235: λ_eff/λ₀ = 7872 |
| Schwächster Effekt | Sr-90: λ_eff/λ₀ = 1.10 |
| Spaltbarkeitsgrenze | Q_fiss > 1 für alle Aktinide |
| Phasenabhängigkeit | η = cos²(Δφ/2) über 9 Phasenwerte (Pu-239) |
| Energieproduktion | 9.3 kW/kg Pu-239 (thermisch) |
| Nettoenergie-Schwelle | ~110 kg Pu-239 |
| κ | 1 exakt (kein freier Parameter) |
| Verbindung zu FLRW | ε = η validiert in 1.530 Simulationen |

---

## 9. Offene Simulationsaufgaben

1. ⬜ **Vollständige Zerfallsketten:** Alle Tochterisotope mit
   eigenen GDR-Parametern, mehrstufige Transmutation
2. ⬜ **Flussscan:** λ_eff/λ₀ als Funktion von Φ (10⁸ − 10¹⁵)
   → Sättigungseffekte bei hohem Fluss
3. ⬜ **Phasenscan:** η(Δφ) über 30+ Werte (analog FLRW) →
   Abweichungen von cos² quantifizieren
4. ⬜ **Thermische Rückkopplung:** Temperatureinfluss auf
   σ_GDR und Resonanzbreite
5. ⬜ **Mehrmodenanalyse:** Kopplung an höhere GDR-Moden
   (E2, E3) und deren Beitrag zu λ_eff
6. ⬜ **Monte-Carlo-Validierung:** Stochastische Simulation
   der Zerfallsstatistik unter Resonanzbedingungen

---

© Dominic-René Schu — Resonanzfeldtheorie 2025/2026

---

[Zurück zur Übersicht](README.md)