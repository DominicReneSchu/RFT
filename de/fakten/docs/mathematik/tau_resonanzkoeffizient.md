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

τ* ist eine **Funktion** der Phasendifferenz, keine Konstante.
Mit ε(Δφ) = cos²(Δφ/2) (Standardmodell) ergibt sich:

```
    τ*(Δφ) = π / cos²(Δφ/2)
```

Da ε = η (Identität aus FLRW-Simulationen), ist τ* direkt
mit der messbaren Kopplungseffizienz verknüpft.

---

## 2. Definition und Wertebereich

```
    τ*(Δφ) = π / ε(Δφ)        mit ε ∈ (0, 1]
```

| Kopplungszustand | ε | τ* | Bedeutung |
|------------------|---|-----|-----------|
| Perfekte Kopplung | 1 | π ≈ 3.14 | Minimale Transferzeit |
| Halbe Kopplung | 0.5 | 2π ≈ 6.28 | Doppelte Transferzeit |
| Natürliche Dämpfung | 1/e ≈ 0.368 | π·e ≈ 8.54 | Nach Relaxation (Spezialfall) |
| Planck (1. Anregung) | 1/π ≈ 0.318 | π² ≈ 9.87 | E = ℏ·f (Spezialfall) |
| Planck (Grundzustand) | 1/(2π) ≈ 0.159 | 2π² ≈ 19.74 | E = ½ℏ·f (Spezialfall) |
| Schwache Kopplung | 0.1 | 10π ≈ 31.4 | Langsamer Transfer |
| Keine Kopplung | 0 | → ∞ | Kein Transfer möglich |

**Physikalische Interpretation:** τ* ist invers proportional zur
Kopplungseffizienz. Je schwächer die Kopplung, desto mehr Zyklen
werden benötigt, um Energie zu übertragen.

**Bemerkenswert:** Beim Planck-Grundzustand (ε = 1/(2π)) beträgt
die Transferzeit τ* = 2π² — ein Produkt der beiden fundamentalen
geometrischen Konstanten der RFT.

---

## 3. Komplexe Zeitstruktur

Die klassische Einheit der Energienormierung:

```
    E / (ℏ·f) = π · ε
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
    E = π · ε · ℏ · f · (cos(α) + i · sin(α))
```

Die Planck-Grundzustandsenergie E = ½ℏf nutzt nur den Realteil
bei ε = 1/(2π) und verliert die Phasenstruktur.

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

**Beispiel:** Bei ε = 1/e (natürliche Dämpfung, Spezialfall):

```
    η_ges = (1/e)² = 1/e² ≈ 0.135 (13.5%)
```

Bei ε = 0.85 (leichte Verstimmung, Δφ ≈ π/4):

```
    ε(π/4) = cos²(π/8) ≈ 0.85
    η_ges = 0.85² ≈ 0.73 (73%)
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
    ε(t) = ε₀ · e^(−λt)    →    dε/dt = −λ · ε
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
    ε(t) = 1 − e^(−λt)    →    τ*(t) = π / (1 − e^(−λt))
```

τ* fällt von ∞ (keine Kopplung) auf π (perfekte Kopplung).

---

## 6. Empirische Verankerung

| Domäne | τ*-Bezug | Beobachtung |
|--------|----------|-------------|
| FLRW | τ*(0) = π | η = 1.0 bei Δφ = 0, minimale Transferzeit |
| FLRW | τ*(π) → ∞ | η = 0.0 bei Δφ = π, kein Transfer |
| FLRW | τ* wächst mit H₀ | Hubble-Reibung erhöht d_η → effektiv höheres τ* |
| Resonanzreaktor | τ* = π (bei Resonanz) | κ = 1, ε = η = 1 bei Δφ = 0 |
| ResoTrade | τ* → ∞ im Crash | ε → 0, Pause-Gate, kein Trade |
| ResoTrade | τ* ≈ π in Phase | ε ≈ 1, schneller Energietransfer, Trade aktiv |
| ResoTrade | Einschwingen | Konvergenz nach 3 Zyklen (Δ < 1%), konsistent mit τ*(t) = π/(1−e^(−λt)) |

Die Hubble-Reibung in FLRW-Simulationen lässt sich als
effektive Erhöhung von τ* interpretieren: Stärkere Expansion
verschiebt η systematisch unter cos²(Δφ/2), was einem
langsameren Energietransfer zwischen den Resonanzfeldern
entspricht.

---

## 7. Fazit

Der Resonanzzeitkoeffizient τ*(Δφ) = π/ε(Δφ) verbindet die
Kopplungseffizienz mit der Zeitskala des Energietransfers:

1. τ* ist eine **Funktion** der Phasendifferenz, keine Konstante
2. Perfekte Kopplung (ε = 1) ergibt die minimale Transferzeit τ* = π
3. Planck-Grundzustand (ε = 1/(2π)) ergibt τ* = 2π²
4. Die Sender-Empfänger-Asymmetrie ergibt η_ges = ε_S · ε_E
5. Die Dynamik dτ*/dt = λ·τ* beschreibt den Kopplungszerfall
6. Hubble-Reibung erhöht τ* effektiv (FLRW-Simulationen)

**Korrektur gegenüber früherer Fassung:** In einer früheren
Version wurde τ* = π/𝓔 als Konstante (mit 𝓔 = 1) definiert.
Das ist nicht korrekt. τ* ist eine Funktion: τ*(Δφ) = π/ε(Δφ).
Der Fall τ* = π (bei ε = 1) ist der Spezialfall perfekter
Kopplung, nicht der allgemeine Zustand.

---

© Dominic-René Schu — Resonanzfeldtheorie 2025/2026

---

[Zurück zur Übersicht](../../../README.md)