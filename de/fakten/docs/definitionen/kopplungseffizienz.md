# Kopplungseffizienz ε — Vereinheitlichte Definition

*Dominic-René Schu, 2025/2026*

---

## 1. Motivation

In früheren Versionen der Resonanzfeldtheorie wurden für die
Kopplungsgröße in der Energieformel E = π·ε·ℏ·f verschiedene
Symbole (ε, 𝓔, 𝜀) und verschiedene Definitionen verwendet.
Dieses Dokument vereinheitlicht die Notation und Definition
verbindlich für alle Dokumente der RFT.

**Aktueller Stand (März 2026):** Die Identität ε = η wurde in
vier unabhängigen Domänen empirisch bestätigt:
- FLRW-Simulationen (1.530 Einzelläufe, d_η = 0.043 im flachen Fall)
- Monte Carlo auf CMS-Daten (1.500.000 Simulationen, 5 Resonanzen)
- Resonanzreaktor (κ = 1, kein freier Parameter)
- ResoTrade (Kopplungseffizienz als Pause-Gate, +26.3% vs HODL)

Alle Dokumente, Simulationen und Definitionen wurden auf die
vereinheitlichte Notation umgestellt (siehe §8).

---

## 2. Verbindliche Definition

### 2.1 Symbol und Name

| Symbol | Name | Verwendung |
|:------:|:-----|:-----------|
| **ε** | Kopplungseffizienz | In Formeln und mathematischen Texten |
| **ε(Δφ)** | Phasenabhängige Kopplungseffizienz | Wenn die Abhängigkeit explizit ist |
| **η(Δφ)** | Kopplungseffizienz (Observable) | In FLRW-Simulationen (Kreuzterm) |

Das kalligraphische Symbol **𝓔** war eine typographische Variante
aus früheren Versionen. In allen aktuellen Dokumenten und
Simulationen wird einheitlich **ε** verwendet.

**Identität:** ε(Δφ) = η(Δφ) = cos²(Δφ/2). Der theoretische
Operator ε und die messbare Observable η sind identisch.

### 2.2 Definition

Die Kopplungseffizienz ε beschreibt, welcher Anteil der maximal
möglichen Resonanzenergie tatsächlich zwischen zwei gekoppelten
Moden übertragen wird.

```
    ε : Zustandsraum → [0, 1]

    ε = 1    perfekte Kopplung (Phasengleichheit, maximale Kohärenz)
    ε = 0    keine Kopplung (Phasenorthogonalität, Dekohärenz)
```

### 2.3 Standardmodell

Das Standardmodell der Kopplungseffizienz als Funktion der
Phasendifferenz Δφ zwischen zwei Moden ist:

```
    ε(Δφ) = cos²(Δφ/2) = ½(1 + cos Δφ)
```

Dieses Modell ergibt:
- ε(0) = 1 (perfekte Kopplung bei Phasengleichheit)
- ε(π) = 0 (keine Kopplung bei Gegenphase)
- ε(π/2) = 0.5 (halbe Kopplung bei 90° Phasenverschiebung)

**Empirische Validierung:**
- FLRW-Simulationen: η(Δφ) emergiert als Kreuzterm und folgt
  cos²(Δφ/2) mit d_η = 0.043 ± 0.008 im flachen Fall
- Resonanzreaktor: ε = η eliminiert κ → κ = 1 exakt
- ResoTrade: ε → 0 im Crash → Pause-Gate → +44.9% vs HODL
- Monte Carlo: ε = 1 bei Teilchenmasse M₀ → 5 Resonanzen, emp. p = 0

### 2.4 Allgemeinere Modelle

Für Systeme mit endlicher Resonanzbreite kann alternativ ein
Gauß-Modell verwendet werden:

```
    ε(Δφ) = exp(−(Δφ/δ)²)
```

wobei δ die Breite des Kopplungsfensters beschreibt.

Beide Modelle erfüllen: ε ∈ [0, 1], ε(0) = 1, monoton fallend
mit |Δφ|.

---

## 3. Die Energieformel

### 3.1 Grundform (Axiom 4)

```
    E = π · ε(Δφ) · ℏ · f
```

### 3.2 Grenzfälle

| Bedingung | ε | Energie | Physik |
|-----------|---|---------|--------|
| Perfekte Kopplung | 1 | π·ℏ·f | Maximale Resonanzenergie |
| Planck (1. Anregung) | 1/π ≈ 0.318 | ��·f | E = ℏω (Spezialfall) |
| Planck (Grundzustand) | 1/(2π) ≈ 0.159 | ½·ℏ·f | Grundzustandsenergie (harm. Osz.) |
| Natürliche Dämpfung | 1/e ≈ 0.368 | (π/e)·ℏ·f | Nach einer Relaxationszeit (Spezialfall) |
| Halbe Kopplung | 0.5 | π·ℏ·f/2 | 90° Phasenverschiebung |
| Keine Kopplung | 0 | 0 | Entkoppelte Systeme |

### 3.3 Herleitung des Faktors π

Der Faktor π entsteht aus der Integration der Kopplungseffizienz
über einen Halbzyklus des Resonanzpfads im Phasenraum:

```
    ∫₀^π cos²(φ/2) dφ = π/2
```

Normiert auf die Kopplungseinheit ergibt sich die Grundformel
E = π · ε · ℏ · f (vollständige Herleitung: siehe
[axiomatische Grundlegung](axiomatische_grundlegung.md) §4.1).

---

## 4. Die Identität ε = η

### 4.1 Herleitung

In der FLRW-Simulation wird die Kopplungseffizienz als
zeitgemittelter Kreuzterm zweier gekoppelter Skalarfelder
extrahiert:

```
    η(Δφ) = ⟨ε₁ · ε₂⟩ / √(⟨ε₁²⟩ · ⟨ε₂²⟩)
```

Die analytische Erwartung für harmonische Felder ist
η_theo = cos²(Δφ/2). Da gleichzeitig der theoretische
Kopplungsoperator ε(Δφ) = cos²(Δφ/2) gilt, folgt:

```
    ε(Δφ) = η(Δφ) = cos²(Δφ/2)
```

### 4.2 Konsequenzen

| Domäne | Konsequenz |
|--------|-----------|
| FLRW-Kosmologie | η emergiert als Observable, d_η skaliert mit H₀ |
| Resonanzreaktor | κ = 1 exakt (kein freier Parameter) |
| ResoTrade | ε → 0 als messbares Gate-Kriterium |
| Monte Carlo | ε = 1 bei Resonanzmasse → Axiom 3 bestätigt |
| Allgemein | Operator und Observable sind identisch |

### 4.3 Empirische Evidenz

```
    Flach (H = 0):      d_η = 0.043 ± 0.008  → cos² fast exakt
    Planck (H₀ = 67.4): d_η = 0.140 ± 0.025  → Hubble-Reibung
    SH0ES (H₀ = 73.0):  d_η = 0.149 ± 0.026  → Δd_η > 6σ
```

Die Abweichung von cos² ist systematisch und wird durch die
Raumzeitexpansion erklärt (Hubble-Reibung). Im flachen Grenzfall
ist die Identität ε = η bis auf d_η ≈ 0.04 exakt.

---

## 5. Einordnung früherer Definitionen

### 5.1 Das Intervall [1/e, e]

In der ursprünglichen Fassung wurde ein „natürliches
Resonanzintervall" ε ∈ [1/e, e] angegeben. Einordnung:

- Der Bereich ε ∈ [1/e, 1] beschreibt physikalisch sinnvolle
  Kopplungszustände (gedämpft bis perfekt)
- Der Bereich ε > 1 war als Resonanzverstärkung gedacht
  (konstruktive Interferenz mehrerer Moden), ist aber in der
  Einzelmoden-Kopplungseffizienz nicht definiert
- Für Mehrmoden-Systeme kann die **effektive Kopplungsstärke**
  K_ij Werte > 1 annehmen (Superposition mehrerer Pfade),
  aber ε als Effizienz bleibt ∈ [0, 1]

**Korrektur:** Das Intervall [1/e, e] gilt für die Kopplungsstärke
K_ij zwischen Moden (die durch konstruktive Interferenz verstärkt
werden kann), nicht für die Kopplungseffizienz ε.

### 5.2 Die Definition 𝓔 := √(e · 1/e) = 1

In einer früheren README wurde definiert:

```
    𝓔 := √(e · 1/e) = 1
```

Dies beschreibt den **Referenzzustand**: Das geometrische Mittel
zwischen maximalem Wachstum (e) und maximalem Zerfall (1/e)
ergibt die neutrale Kopplung. In der aktuellen Notation:

```
    ε = 1 entspricht perfekter Kopplung
    → E = π · ℏ · f (maximale Resonanzenergie)
```

Diese Definition ist in der aktuellen README durch die
vereinheitlichte Notation ersetzt.

### 5.3 Der Spezialfall ε = 1/e

In einer früheren Fassung der `energie_axiomatische_herleitung.md`
wurde ε = 1/e als universeller Korrekturfaktor dargestellt.
Korrekte Einordnung:

```
    ε = 1/e ≈ 0.368
```

Dieser Wert entsteht als natürlicher Kopplungszustand nach
einer Relaxationszeit τ in einem gedämpften System:

```
    ε(t) = e^(−t/τ)  →  ε(τ) = 1/e
```

Es handelt sich um einen physikalisch wichtigen Spezialfall
(typische Kopplung nach Einschwingvorgang), nicht um den
allgemeinen Fall. Das Dokument wurde entsprechend korrigiert.

---

## 6. Abgrenzung: ε vs. η vs. K_ij vs. G

| Größe | Symbol | Wertebereich | Bedeutung |
|-------|--------|-------------|-----------|
| Kopplungseffizienz (Operator) | ε(Δφ) | [0, 1] | Theoretischer Kopplungsoperator |
| Kopplungseffizienz (Observable) | η(Δφ) | [0, 1] | Messbarer Kreuzterm (FLRW) |
| Kopplungsstärke | K_ij | [0, ∞) | Absolutwert der Kopplung zwischen Moden |
| Resonanzgewichtung | G(f₁/f₂) | [0, 1] | Frequenz-Resonanzfenster (Axiom 3) |

**Identität:** ε = η (bewiesen durch cos²-Identität, validiert
in FLRW mit 1.530 Simulationen).

Die Energieformel verwendet ausschließlich ε:

```
    E = π · ε(Δφ) · ℏ · f
```

Die Kopplungsstärke K_ij beschreibt, wie stark zwei Moden
grundsätzlich wechselwirken. Die Kopplungseffizienz ε beschreibt,
wie viel dieser Wechselwirkung tatsächlich in Energietransfer
umgesetzt wird.

---

## 7. Anwendungen

### 7.1 FLRW-Kosmologie

```
    η(Δφ) = ⟨ε₁·ε₂⟩ / √(⟨ε₁²⟩·⟨ε₂²⟩)
    d_η = ⟨|η_sim − η_theo|⟩
    dd_η/dH₀ = (0.00113 ± 0.00017) (km/s/Mpc)⁻¹
    Δd_η (SH0ES − Planck) = 0.0063 ± 0.0010 (> 6σ)
    Δχ² = +16 vs Planck-2018-CMB
```

### 7.2 Resonanzreaktor

```
    λ_eff(Δφ) = λ₀ + η(Δφ) · Φ_γ · σ_GDR
    κ = 1 (aus ε = η, kein freier Parameter)
    f_GDR = E_GDR / (π·ℏ)

    U-235: GDR 13.0 MeV, f = 6.3×10²¹ Hz, λ_eff/λ₀ = 7872
    Pu-239: GDR 13.5 MeV, Q_fiss ≈ 1.0 bei Φ = 10¹² γ/(cm²·s)
    Am-241: GDR 13.3 MeV, α-Zerfall beschleunigbar
```

### 7.3 ResoTrade

```
    Kopplungseffizienz als Gate-Kriterium:
    ε → 0 (Crash, DC fällt stark) → Pause → +44.9% vs HODL
    ε → 1 (Phasenkohärenz) → Trade erlaubt → systematisch profitabel
    24 Monate, 4 Regime, 1392 Trades, +26.3% vs HODL
    Live seit Feb. 2026 (+4.13% in 2 Wochen)
```

### 7.4 Monte-Carlo (CMS-Daten)

```
    Resonanzbedingung (A3): ε = 1 bei M₀ = Teilchenmasse
    5 Resonanzen detektiert mit emp. p = 0:
    φ(1020), J/ψ, Υ(1S), Υ(2S), Z-Boson
    1.500.000 Gesamtsimulationen (30 Seeds × 50.000)
    Stabil über 3 KDE-Bandbreiten
```

---

## 8. Dokumentenstatus: Vereinheitlichung abgeschlossen

Alle Dokumente wurden auf die verbindliche Definition
ε(Δφ) ∈ [0, 1] mit Standardmodell cos²(Δφ/2) und
ℏ (statt h) umgestellt:

| Dokument | Korrektur | Status |
|----------|-----------|--------|
| axiomatische_grundlegung.md | ε(Δφ) ∈ [0,1] | ✅ Bereits korrekt |
| paper_resonanzfeldtheorie.md | ε ∈ [0,1]; K_ij ∈ [1/e, e] | ✅ Korrigiert |
| README.md (DE) | ε ∈ [0,1], ℏ, ε = η, Planck 1/(2π) | ✅ Korrigiert |
| energie_axiomatische_herleitung.md | ε = 1/e als Spezialfall, ℏ, ε = η | ✅ Korrigiert |
| tau_resonanzkoeffizient.md | τ*(Δφ) = π/ε(Δφ) (Funktion), ℏ | ✅ Korrigiert |
| energieuebertragung.md | ε ∈ [0,1], ℏ, ε = η | ✅ Korrigiert |
| resonanzfeld_gleichung.md | ε = Kopplungseffizienz, ℏ, ε = η | ✅ Korrigiert |
| resonanzlexikon.md | ε ∈ [0,1], ℏ, Planck 1/(2π) | ✅ Korrigiert |
| Simulationen (Python) | coupling_efficiency (statt schu_koppler) | ✅ Korrigiert |
| rft_manuskript_de_iop.tex | ε = η (Gl. 9), ℏ | ✅ Bereits korrekt |
| RFT_Zusammenfassung.tex | ε = η Identität, ℏ | ✅ Bereits korrekt |

---

## 9. Zusammenfassung

Die Kopplungseffizienz ε der Resonanzfeldtheorie ist:

1. **Eine Funktion**, kein fester Wert: ε = ε(Δφ, Kohärenz, ...)
2. **Beschränkt auf [0, 1]**: Effizienz > 100% ist physikalisch
   nicht definiert
3. **Das Standardmodell** ist ε(Δφ) = cos²(Δφ/2)
4. **Identisch mit der Observable η**: ε(Δφ) = η(Δφ), validiert
   in FLRW-Simulationen (1.530 Läufe, d_η = 0.043 im flachen Fall)
5. **Eliminiert κ**: Im Resonanzreaktor folgt κ = 1 exakt
6. **Spezialfälle**: ε = 1 (perfekt), ε = 1/(2π) (Planck-Grundzustand),
   ε = 1/π (Planck 1. Anregung), ε = 1/e (natürliche Dämpfung)
7. **Nicht zu verwechseln** mit der Kopplungsstärke K_ij, die
   unbeschränkt sein kann
8. **Empirisch bestätigt** in vier Domänen: Teilchenphysik,
   Kosmologie, Nukleartechnologie, Finanzmärkte
9. **Notation vereinheitlicht**: Alle Dokumente und Simulationen
   verwenden ε (statt 𝓔), ℏ (statt h), cos²(Δφ/2) als
   Standardmodell

Diese Definition ist verbindlich für alle Dokumente der
Resonanzfeldtheorie ab Version 2026.

---

© Dominic-René Schu — Resonanzfeldtheorie 2025/2026

---

[Zurück zur Übersicht](../../../README.md)