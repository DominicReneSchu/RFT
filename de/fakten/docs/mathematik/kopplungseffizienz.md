# Kopplungseffizienz ε — Vereinheitlichte Definition

*Dominic-René Schu, 2025/2026*

---

## 1. Motivation

In früheren Versionen der Resonanzfeldtheorie wurden für die
Kopplungsgröße in der Energieformel E = π·ε·h·f verschiedene
Symbole (ε, 𝓔, 𝜀) und verschiedene Definitionen verwendet.
Dieses Dokument vereinheitlicht die Notation und Definition
verbindlich für alle Dokumente der RFT.

---

## 2. Verbindliche Definition

### 2.1 Symbol und Name

| Symbol | Name | Verwendung |
|:------:|:-----|:-----------|
| **ε** | Kopplungseffizienz | In Formeln und mathematischen Texten |
| **ε(Δφ)** | Phasenabhängige Kopplungseffizienz | Wenn die Abhängigkeit explizit ist |

Das kalligraphische Symbol **𝓔** wird als typographische Variante
von ε akzeptiert (insbesondere in Diagrammen und Simulationen),
bezeichnet aber dieselbe Größe.

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
    ε(Δφ) = cos²(Δφ/2)
```

Dieses Modell ergibt:
- ε(0) = 1 (perfekte Kopplung bei Phasengleichheit)
- ε(π) = 0 (keine Kopplung bei Gegenphase)
- ε(π/2) = 0.5 (halbe Kopplung bei 90° Phasenverschiebung)

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
    E_eff = π · ε(Δφ) · h · f
```

### 3.2 Grenzfälle

| Bedingung | ε | Energie | Physik |
|-----------|---|---------|--------|
| Perfekte Kopplung | 1 | π·h·f | Maximale Resonanzenergie |
| Neutrale Kopplung | 1/π ≈ 0.318 | h·f | Klassische Quantenenergie |
| Natürliche Dämpfung | 1/e ≈ 0.368 | (π/e)·h·f ≈ 1.155·h·f | Nach einer Relaxationszeit |
| Halbe Kopplung | 0.5 | π·h·f/2 | 90° Phasenverschiebung |
| Keine Kopplung | 0 | 0 | Entkoppelte Systeme |

### 3.3 Herleitung des Faktors π

Der Faktor π entsteht aus der Integration der Kopplungseffizienz
über einen Halbzyklus des Resonanzpfads im Phasenraum:

```
    ∫₀^π cos²(φ/2) dφ = π/2
```

Normiert auf die Kopplungseinheit ergibt sich die Grundformel
E_eff = π · ε · h · f (vollständige Herleitung: siehe
axiomatische_grundlegung.md §4.1).

---

## 4. Einordnung früherer Definitionen

### 4.1 Das Intervall [1/e, e]

In der ursprünglichen Fassung des Definitions-Papers wurde ein
„natürliches Resonanzintervall" ε ∈ [1/e, e] angegeben. Dieses
Intervall wird wie folgt eingeordnet:

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

### 4.2 Die Definition 𝓔 := √(e · 1/e) = 1

In der README wurde definiert:

```
    𝓔 := √(e · 1/e) = 1
```

Dies beschreibt den **Referenzzustand**: Das geometrische Mittel
zwischen maximalem Wachstum (e) und maximalem Zerfall (1/e)
ergibt die neutrale Kopplung. In der neuen Notation:

```
    ε = 1 entspricht perfekter Kopplung
    → E_eff = π · h · f (maximale Resonanzenergie)
```

### 4.3 Der Spezialfall ε = 1/e

In der `energie_axiomatische_herleitung.md` wurde ε = 1/e als
universeller Korrekturfaktor dargestellt. Korrekte Einordnung:

```
    ε = 1/e ≈ 0.368
```

Dieser Wert entsteht als natürlicher Kopplungszustand nach
einer Relaxationszeit τ in einem gedämpften System:

```
    ε(t) = e^{−t/τ}  →  ε(τ) = 1/e
```

Es handelt sich um einen physikalisch wichtigen Spezialfall
(typische Kopplung nach Einschwingvorgang), nicht um den
allgemeinen Fall.

---

## 5. Abgrenzung: ε vs. K_ij vs. G

| Größe | Symbol | Wertebereich | Bedeutung |
|-------|--------|-------------|-----------|
| Kopplungseffizienz | ε(Δφ) | [0, 1] | Anteil übertragener Resonanzenergie |
| Kopplungsstärke | K_ij | [0, ∞) | Absolutwert der Kopplung zwischen Moden |
| Resonanzgewichtung | G(f₁/f₂) | [0, 1] | Frequenz-Resonanzfenster (Axiom 3) |

Die Energieformel verwendet ausschließlich ε:

```
    E_eff = π · ε(Δφ) · h · f
```

Die Kopplungsstärke K_ij beschreibt, wie stark zwei Moden
grundsätzlich wechselwirken. Die Kopplungseffizienz ε beschreibt,
wie viel dieser Wechselwirkung tatsächlich in Energietransfer
umgesetzt wird.

---

## 6. Konsequenzen für bestehende Dokumente

| Dokument | Alte Definition | Neue Definition | Änderung |
|----------|----------------|-----------------|----------|
| axiomatische_grundlegung.md | ε(Δφ) ∈ [0,1] | ε(Δφ) ∈ [0,1] | ✅ Bereits korrekt |
| paper_resonanzfeldtheorie.md | ε ∈ [1/e, e] | ε ∈ [0,1]; K_ij ∈ [1/e, e] | Intervall korrigieren |
| README.md (DE) | 𝓔 := √(e·1/e) = 1 | ε = 1 (Spezialfall) | Einordnung erg��nzen |
| energie_axiomatische_herleitung.md | ε = 1/e (universell) | ε = 1/e (Spezialfall) | Umschreiben als Spezialfall |
| tau_resonanzkoeffizient.md | τ* = π/𝓔 (𝓔 = Konstante) | τ*(Δφ) = π/ε(Δφ) | Funktion statt Konstante |
| energieuebertragung.md | ε ∈ [1/e, e] | ε ∈ [0,1] | Intervall korrigieren |
| resonanzfeld_gleichung.md | 𝓔 = Kopplungsoperator | ε = Kopplungseffizienz | Symbol vereinheitlichen |
| resonanzlexikon.md | ε ∈ [0.37, 2.72] | ε ∈ [0,1] | Intervall korrigieren |
| Simulationen (Python) | 𝓔(t), schu_koppler | ε(t), coupling_efficiency | Variablennamen anpassen |

---

## 7. Zusammenfassung

Die Kopplungseffizienz ε der Resonanzfeldtheorie ist:

1. **Eine Funktion**, kein fester Wert: ε = ��(Δφ, Kohärenz, ...)
2. **Beschränkt auf [0, 1]**: Effizienz > 100% ist physikalisch
   nicht definiert
3. **Das Standardmodell** ist ε(Δφ) = cos²(Δφ/2)
4. **Spezialfälle**: ε = 1 (perfekt), ε = 1/e (natürliche
   Dämpfung), ε = 1/π (klassischer Grenzfall E = h·f)
5. **Nicht zu verwechseln** mit der Kopplungsstärke K_ij, die
   unbeschränkt sein kann

Diese Definition ist verbindlich für alle Dokumente der
Resonanzfeldtheorie ab Version 2026.

---

© Dominic-René Schu — Resonanzfeldtheorie 2025/2026

---

[Zurück zur Übersicht](../../../README.md)