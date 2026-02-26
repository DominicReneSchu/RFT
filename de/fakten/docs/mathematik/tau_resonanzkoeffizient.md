# Der Resonanzzeitkoeffizient τ*

*Dominic-René Schu, 2025/2026*

---

## 1. Einleitung

In der klassischen Physik ist Energie eine skalare Größe. In der
Resonanzfeldtheorie ist Energie funktional mit der Kopplungseffizienz
und damit mit der Phasenstruktur zwischen Systemen verknüpft.

Der dimensionslose **Resonanzzeitkoeffizient**:

```
    τ*(Δφ) = π / ε(Δφ)
```

beschreibt die Zeitskala der Resonanzkopplung: Wie viele
Kopplungszyklen sind nötig, um eine vollständige Energieübertragung
zu erreichen?

---

## 2. Definition und Wertebereich

```
    τ*(Δφ) = π / ε(Δφ)        mit ε ∈ (0, 1]
```

| Kopplungszustand | ε | τ* | Bedeutung |
|------------------|---|-----|-----------|
| Perfekte Kopplung | 1 | π ≈ 3.14 | Minimale Transferzeit |
| Halbe Kopplung | 0.5 | 2π ≈ 6.28 | Doppelte Transferzeit |
| Natürliche Dämpfung | 1/e ≈ 0.368 | π·e ≈ 8.54 | Nach Relaxation |
| Schwache Kopplung | 0.1 | 10π ≈ 31.4 | Langsamer Transfer |
| Keine Kopplung | 0 | → ∞ | Kein Transfer möglich |

**Physikalische Interpretation:** τ* ist invers proportional zur
Kopplungseffizienz. Je schwächer die Kopplung, desto mehr Zyklen
werden benötigt, um Energie zu übertragen.

---

## 3. Komplexe Zeitstruktur

Die klassische Einheit der Energienormierung:

```
    E / (h·f) = 1
```

wird in der RFT geometrisch als Hypotenuse eines Zeit-Zeit-Dreiecks
interpretiert:

```
    1 = √(cos²(α) + sin²(α))
```

mit:
- Reale Zeitkomponente: t_r = cos(α) · t
- Imaginäre Zeitkomponente: t_i = sin(α) · t

Der Winkel α beschreibt die Phasenlage zwischen gekoppelten Systemen.
Die komplexe Energieprojektion:

```
    E = π · ε · h · f · (cos(α) + i · sin(α))
```

Die klassische Formel E = h·f nutzt nur den Realteil bei ε = 1/π
und verliert die Phasenstruktur.

---

## 4. Sender-Empfänger-Asymmetrie

Die Kopplungseffizienz kann für Sender und Empfänger unterschiedlich
sein, wenn die Phasendifferenz asymmetrisch wirkt:

- **Sendeeffizienz:** ε_S = ε(Δφ_S) — wie effizient ein System
  Energie in das Feld einkoppelt
- **Empfangseffizienz:** ε_E = ε(Δφ_E) — wie effizient ein System
  Energie aus dem Feld auskoppelt

Die Gesamteffizienz des Transfers:

```
    η_ges = ε_S · ε_E
```

Für den symmetrischen Fall (ε_S = ε_E = ε):

```
    η_ges = ε²
```

**Beispiel:** Bei ε = 1/e (natürliche Dämpfung):

```
    η_ges = (1/e)² = 1/e² ≈ 0.135 (13.5%)
```

Bei ε = 0.86 (leichte Verstimmung, Δφ ≈ π/4):

```
    η_ges = 0.86² ≈ 0.74 (74%)
```

---

## 5. Dynamik des Resonanzzeitkoeffizienten

Für ein System mit zeitabhängiger Kopplungseffizienz ε(t):

```
    τ*(t) = π / ε(t)
```

Die zeitliche Änderung:

```
    dτ*/dt = −π / ε² · dε/dt
```

Für exponentiellen Kopplungszerfall (gedämpftes System):

```
    ε(t) = ε₀ · e^{−λt}    →    dε/dt = −λ · ε
```

folgt:

```
    dτ*/dt = λ · τ*
```

Dies beschreibt ein exponentielles Wachstum von τ*: Die
Transferzeit steigt exponentiell, wenn die Kopplung exponentiell
abnimmt — konsistent mit der physikalischen Intuition.

Für anwachsende Kopplung (Einschwingvorgang):

```
    ε(t) = 1 − e^{−λt}    →    τ*(t) = π / (1 − e^{−λt})
```

τ* fällt von ∞ (keine Kopplung) auf π (perfekte Kopplung).

---

## 6. Fazit

Der Resonanzzeitkoeffizient τ* = π/ε verbindet die Kopplungseffizienz
mit der Zeitskala des Energietransfers:

1. τ* ist eine **Funktion** der Phasendifferenz, keine Konstante
2. Perfekte Kopplung (ε = 1) ergibt die minimale Transferzeit τ* = π
3. Die Sender-Empfänger-Asymmetrie ergibt η_ges = ε_S · ε_E
4. Die Dynamik dτ*/dt = λ·τ* beschreibt den Kopplungszerfall

---

© Dominic-René Schu — Resonanzfeldtheorie 2025/2026

---

[Zurück zur Übersicht](../../../README.md)