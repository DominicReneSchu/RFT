# Kopplungsenergie: Axiomatische Herleitung und Spezialfälle

*Dominic-René Schu, 2025/2026*

---

## 1. Einordnung

Die Resonanzfeldtheorie beschreibt Energieübertragung als Resultat
kohärenter Resonanzkopplung zwischen Feldern. Die axiomatische
Grundlage liefert Axiom 4 (Kopplungsenergie), formalisiert in der
[axiomatischen Grundlegung](../definitionen/axiomatische_grundlegung.md).

---

## 2. Allgemeine Energieformel (Axiom 4)

Die effektive Energie einer resonanten Kopplung lautet:

```
    E_eff = π · ε(Δφ) · h · f
```

Dabei ist:
- ε(Δφ) die Kopplungseffizienz, ε ∈ [0, 1]
  (siehe [Vereinheitlichte Definition](kopplungseffizienz.md))
- π der geometrische Faktor aus der zyklischen Kopplungsgeometrie
- h das Plancksche Wirkungsquantum
- f die Frequenz der gekoppelten Mode

Das Standardmodell der Kopplungseffizienz ist:

```
    ε(Δφ) = cos²(Δφ/2)
```

---

## 3. Grenzfälle und Spezialfälle

### 3.1 Perfekte Kopplung (ε = 1)

Bei vollständiger Phasensynchronisation (Δφ = 0) wird die maximale
Resonanzenergie übertragen:

```
    E_max = π · h · f ≈ 3.14 · h · f
```

### 3.2 Klassischer Grenzfall (ε = 1/π)

Die klassische Planck-Formel E = h·f ergibt sich als Spezialfall:

```
    ε = 1/π ≈ 0.318
    E = π · (1/π) · h · f = h · f
```

Physikalisch entspricht dies einer partiell entkoppelten Messung,
bei der nur die Projektion auf die reale Zeitachse erfasst wird.
Die klassische Physik beschreibt somit den Kopplungszustand
ε = 1/π — eine Vereinfachung, die die volle Resonanzstruktur
nicht abbildet.

### 3.3 Natürliche Dämpfung (ε = 1/e)

Für ein gedämpftes System mit exponentieller Relaxation gilt
nach einer Zeitkonstante τ:

```
    ε(t) = e^{−t/τ}    →    ε(τ) = 1/e ≈ 0.368
```

Die zugehörige Energie:

```
    E = π · (1/e) · h · f = (π/e) · h · f ≈ 1.155 · h · f
```

Der Faktor π/e ≈ 1.155 ist eine Konsequenz des Kopplungszustands
nach einer Relaxationszeit — keine universelle Konstante.

**Physikalische Bedeutung:** Dieser Zustand tritt auf in:
- Gedämpften Oszillatoren nach dem Einschwingvorgang
- Kavitäten mit endlicher Güte Q
- Systemen mit natürlicher Dissipation

### 3.4 Halbe Kopplung (ε = 1/2)

Bei 90° Phasenverschiebung (Δφ = π/2):

```
    ε(π/2) = cos²(π/4) = 1/2
    E = π · h · f / 2 ≈ 1.57 · h · f
```

### 3.5 Keine Kopplung (ε = 0)

Bei Gegenphase (Δφ = π):

```
    ε(π) = cos²(π/2) = 0
    E = 0
```

Destruktive Interferenz — keine Energieübertragung.

---

## 4. Übersicht der Spezialfälle

| Kopplungszustand | ε | Energie | Bedingung |
|------------------|---|---------|-----------|
| Perfekte Resonanz | 1 | π·h·f | Δφ = 0 |
| Natürliche Dämpfung | 1/e ≈ 0.368 | (π/e)·h·f ≈ 1.155·h·f | Nach Relaxationszeit τ |
| Klassischer Grenzfall | 1/π ≈ 0.318 | h·f | Projektion auf reale Zeitachse |
| Halbe Kopplung | 1/2 | π·h·f/2 | Δφ = π/2 |
| Entkoppelt | 0 | 0 | Δφ = π |

---

## 5. Komplexe Zeitstruktur

Die Energieformel lässt sich in komplexer Schreibweise darstellen:

```
    E = π · ε · h · f · e^{iα}
```

wobei α der Phasenwinkel zwischen Beobachterzeit und Feldzeit ist.
Die klassische Formel E = h·f erfasst nur den Realteil:

```
    Re(E) = π · ε · h · f · cos(α)
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

## 6. Fazit

Die klassische Planck-Gleichung E = h·f ist ein Spezialfall der
Resonanzfeld-Energieformel E = π·ε·h·f mit ε = 1/π. Die RFT
verallgemeinert den Energiebegriff durch:

1. Die Kopplungseffizienz ε(Δφ) ∈ [0, 1] als zentrale Größe
2. Den geometrischen Faktor π aus der zyklischen Kopplungsgeometrie
3. Die komplexe Zeitstruktur (Phasenwinkel α)

Der häufig zitierte Faktor π/e ≈ 1.155 beschreibt den natürlichen
Kopplungszustand nach einer Relaxationszeit und ist ein wichtiger,
aber nicht der allgemeine Fall.

---

© Dominic-René Schu — Resonanzfeldtheorie 2025/2026

---

[Zurück zur Übersicht](../../../README.md)