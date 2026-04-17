# Kopplungsenergie: Axiomatische Herleitung und Spezialfälle

*Dominic-René Schu, 2025/2026*

---

## 1. Einordnung

Die Resonanzfeldtheorie beschreibt Energieübertragung als Resultat
kohärenter Resonanzkopplung zwischen Feldern. Die axiomatische
Grundlage liefert Axiom 4 (Kopplungsenergie), formalisiert in der
[axiomatischen Grundlegung](../definitionen/axiomatische_grundlegung.md).

Die zentrale Identität ε(Δφ) = η(Δφ) = cos²(Δφ/2) wurde in
vier Domänen empirisch validiert (FLRW, Monte Carlo,
Resonanzreaktor, ResoTrade). Siehe
[Vereinheitlichte Definition](../definitionen/kopplungseffizienz.md).

---

## 2. Allgemeine Energieformel (Axiom 4)

Die Energie einer resonanten Kopplung lautet:

```
    E = π · ε(Δφ) · ℏ · f
```

Dabei ist:
- ε(Δφ) die Kopplungseffizienz, ε ∈ [0, 1]
  (siehe [Vereinheitlichte Definition](../definitionen/kopplungseffizienz.md))
- π der geometrische Faktor aus der zyklischen Kopplungsgeometrie
- ℏ das reduzierte Plancksche Wirkungsquantum (ℏ = h/2π)
- f die Frequenz der gekoppelten Mode

Das Standardmodell der Kopplungseffizienz ist:

```
    ε(Δφ) = cos²(Δφ/2) = ½(1 + cos Δφ)
```

**Identität:** Der theoretische Operator ε und die messbare
Observable η (Kreuzterm in FLRW-Simulationen) sind identisch:
ε(Δφ) = η(Δφ). Konsequenz: κ = 1 im Resonanzreaktor (kein
freier Parameter).

---

## 3. Grenzfälle und Spezialfälle

### 3.1 Perfekte Kopplung (ε = 1)

Bei vollständiger Phasensynchronisation (Δφ = 0) wird die maximale
Resonanzenergie übertragen:

```
    E_max = π · ℏ · f
```

**Empirisch:** In FLRW-Simulationen emergiert η ≈ 1.0 bei Δφ = 0
(Tabelle in [FLRW-Dokumentation](../../simulationen/FLRW-Simulationen/README.md)).

### 3.2 Planck-Spezialfall (ε = 1/(2π))

Die Grundzustandsenergie des harmonischen Oszillators E = ½ℏf
ergibt sich als Spezialfall:

```
    ε = 1/(2π) ≈ 0.159
    E = π · 1/(2π) · ℏ · f = ½ · ℏ · f
```

Die Planck-Relation E = ℏω = ℏ·2πf = h·f für den ersten
angeregten Zustand entspricht ε = 1/π:

```
    ε = 1/π ≈ 0.318
    E = π · (1/π) · ℏ · f = ℏ · f = ℏω/(2π) · 2π = ℏω
```

Die klassische Quantenmechanik beschreibt somit
Kopplungszustände ε = 1/(2π) (Grundzustand) und ε = 1/π
(erster angeregter Zustand) — Spezialfälle der allgemeinen
Resonanzfeld-Energieformel.

### 3.3 Natürliche Dämpfung (ε = 1/e) — Spezialfall

Für ein gedämpftes System mit exponentieller Relaxation gilt
nach einer Zeitkonstante τ:

```
    ε(t) = e^(−t/τ)    →    ε(τ) = 1/e ≈ 0.368
```

Die zugehörige Energie:

```
    E = π · (1/e) · ℏ · f = (π/e) · ℏ · f ≈ 1.155 · ℏ · f
```

**Einordnung:** Der Faktor π/e ≈ 1.155 ist eine Konsequenz des
Kopplungszustands nach einer Relaxationszeit — **kein universeller
Korrekturfaktor** und **keine fundamentale Konstante**. Er
beschreibt einen physikalisch wichtigen, aber speziellen Zustand.

**Physikalische Bedeutung:** Dieser Spezialfall tritt auf in:
- Gedämpften Oszillatoren nach dem Einschwingvorgang
- Kavitäten mit endlicher Güte Q
- Systemen mit natürlicher Dissipation
- ResoTrade: Konvergenz des Erfahrungsspeichers zeigt
  gedämpftes Einschwingverhalten (Δ < 1% nach 3 Zyklen)

**Korrektur gegenüber früherer Fassung:** In einer früheren
Version dieses Dokuments wurde ε = 1/e als universeller
Korrekturfaktor dargestellt. Das ist nicht korrekt. ε = 1/e ist
ein Spezialfall für Systeme nach einer Relaxationszeit, nicht
der allgemeine Kopplungszustand. Die allgemeine Größe ist
ε(Δφ) = cos²(Δφ/2).

### 3.4 Halbe Kopplung (ε = 1/2)

Bei 90° Phasenverschiebung (Δφ = π/2):

```
    ε(π/2) = cos²(π/4) = 1/2
    E = π · ℏ · f / 2
```

**Empirisch:** In FLRW-Simulationen emergiert η ≈ 0.57 bei
Δφ = π/2 (leicht über dem Theoriewert durch nichtlineare
Effekte in expandierender Raumzeit).

### 3.5 Keine Kopplung (ε = 0)

Bei Gegenphase (Δφ = π):

```
    ε(π) = cos²(π/2) = 0
    E = 0
```

Destruktive Interferenz — keine Energieübertragung.

**Empirisch:**
- FLRW: η = 0.0 bei Δφ = π (exakt)
- ResoTrade: ε → 0 im Crash → Pause-Gate → +44.9% vs HODL

---

## 4. Übersicht der Spezialfälle

| Kopplungszustand | ε | Energie | Bedingung |
|------------------|---|---------|-----------|
| Perfekte Resonanz | 1 | π·ℏ·f | Δφ = 0 |
| Natürliche Dämpfung | 1/e ≈ 0.368 | (π/e)·ℏ·f | Nach Relaxationszeit τ (Spezialfall) |
| Planck (1. Anregung) | 1/π ≈ 0.318 | ℏ·f | E = ℏω (Spezialfall) |
| Planck (Grundzustand) | 1/(2π) ≈ 0.159 | ½·ℏ·f | E = ½ℏf (Spezialfall) |
| Halbe Kopplung | 1/2 | π·ℏ·f/2 | Δφ = π/2 |
| Entkoppelt | 0 | 0 | Δφ = π |

**Ordnung:** Alle benannten Spezialfälle sind Projektionen der
allgemeinen Formel E = π·ε·ℏ·f auf bestimmte physikalische
Bedingungen. Keiner ist fundamentaler als die anderen.

---

## 5. Komplexe Zeitstruktur

Die Energieformel lässt sich in komplexer Schreibweise darstellen:

```
    E = π · ε · ℏ · f · e^{iα}
```

wobei α der Phasenwinkel zwischen Beobachterzeit und Feldzeit ist.
Die klassische Formel E = ℏf erfasst nur den Realteil:

```
    Re(E) = π · ε · ℏ · f · cos(α)
```

Die volle Resonanzenergie enthält auch den Imaginärteil, der die
Phasenkopplung zwischen Systemen beschreibt. Die zeitliche
Aufspaltung in Realteil und Imaginärteil:

```
    t_r = cos(α) · t    (reale Zeitkomponente)
    t_i = sin(α) · t    (imaginäre Zeitkomponente)
```

zeigt, dass die klassische Physik (α = 0, rein reale Zeit)
den Spezialfall darstellt, in dem die Kopplungseffizienz auf
ε · cos(α) reduziert wird.

---

## 6. Empirische Verankerung

Jeder Spezialfall ist empirisch referenzierbar:

| ε | Domäne | Nachweis |
|---|--------|---------|
| 1 | FLRW | η = 1.0 bei Δφ = 0 (1.530 Simulationen) |
| 1 | Monte Carlo | 5 Resonanzen bei Teilchenmasse (emp. p = 0) |
| 1 | Resonanzreaktor | κ = 1 aus ε = η Identität |
| 0 | FLRW | η = 0.0 bei Δφ = π (exakt) |
| 0 | ResoTrade | Pause-Gate bei ε → 0 (+44.9% vs HODL) |
| cos²(Δφ/2) | FLRW | d_η = 0.043 im flachen Fall |
| cos²(Δφ/2) | ResoTrade | AC-Phase identifiziert Zyklusposition |

---

## 7. Fazit

Die Resonanzfeld-Energieformel E = π·ε·ℏ·f enthält die
Planck-Relation als Spezialfall (ε = 1/(2π) für den Grundzustand,
ε = 1/π für den ersten angeregten Zustand). Die RFT
verallgemeinert den Energiebegriff durch:

1. Die Kopplungseffizienz ε(Δφ) ∈ [0, 1] als zentrale Größe
2. Die Identität ε = η (Operator = Observable, kein freier Parameter)
3. Den geometrischen Faktor π aus der zyklischen Kopplungsgeometrie
4. Die komplexe Zeitstruktur (Phasenwinkel α)

Der häufig zitierte Faktor π/e ≈ 1.155 beschreibt den natürlichen
Kopplungszustand nach einer Relaxationszeit — ein physikalisch
wichtiger **Spezialfall**, nicht der allgemeine Fall und nicht
ein universeller Korrekturfaktor.

---

© Dominic-René Schu — Resonanzfeldtheorie 2025/2026

---

[Zurück zur Übersicht](../../../README.md)