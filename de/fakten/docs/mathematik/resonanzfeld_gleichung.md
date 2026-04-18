# Die Resonanzfeld-Gleichung

*Dominic-René Schu, 2025/2026*

---

## 1. Einleitung

Die Resonanzfeld-Gleichung verknüpft Resonanzfrequenz, Kopplungseffizienz
und Energiefluss. Sie ist die zentrale Energiegleichung der
Resonanzfeldtheorie, abgeleitet aus Axiom 4
(siehe [axiomatische Grundlegung](../definitionen/axiomatische_grundlegung.md)).

Die Identität ε(Δφ) = η(Δφ) = cos²(Δφ/2) stellt sicher, dass
die Gleichung keinen freien Parameter enthält — der theoretische
Operator und die messbare Observable sind identisch.

---

## 2. Grundform

```
    E = π · ε(Δφ) · ℏ · f
```

- **ε(Δφ)**: Kopplungseffizienz, ε ∈ [0, 1]
  (siehe [Vereinheitlichte Definition](../definitionen/kopplungseffizienz.md))
- **π**: Geometrischer Faktor aus der zyklischen Kopplungsgeometrie
- **ℏ**: Reduziertes Plancksches Wirkungsquantum (ℏ = h/2π)
- **f**: Resonanzfrequenz

**Standardmodell:** ε(Δφ) = cos²(Δφ/2) = ½(1 + cos Δφ)

**Identität:** ε(Δφ) = η(Δφ) — validiert in 1.530 FLRW-Simulationen
(d_η = 0.043 ± 0.008 im flachen Fall). Konsequenz: κ = 1 im
Resonanzreaktor (kein freier Parameter).

---

## 3. Spezialfälle

| Kopplungszustand | ε | Energie | Physik |
|------------------|---|---------|--------|
| Perfekte Resonanz (Δφ = 0) | 1 | π·ℏ·f | Maximale Kopplung |
| Natürliche Dämpfung | 1/e ≈ 0.368 | (π/e)·ℏ·f | Nach Relaxationszeit (Spezialfall) |
| Planck (1. Anregung) | 1/π ≈ 0.318 | ℏ·f | E = ℏω (Spezialfall) |
| Planck (Grundzustand) | 1/(2π) ≈ 0.159 | ½·ℏ·f | E = ½ℏf (Spezialfall) |
| Halbe Kopplung (Δφ = π/2) | 0.5 | π·ℏ·f/2 | 90° Phasenverschiebung |
| Entkoppelt (Δφ = π) | 0 | 0 | Destruktive Interferenz |

Vollständige Herleitung: [Kopplungsenergie: Spezialfälle](kopplungsenergie.md)

---

## 4. Phasenmodulierte Form

Unter Einbeziehung der komplexen Zeitstruktur:

```
    E = π · ε · ℏ · f · e^{iα}
```

- **α**: Phasenwinkel zwischen Beobachterzeit und Feldzeit
- **e^{iα} = cos(α) + i·sin(α)**: Euler-Darstellung

Der Realteil beschreibt den messbaren Energietransfer, der
Imaginärteil die latente Phasenkopplung.

**Herleitung:** Aus Axiom 6 (Informationsfluss durch kohärente
Phasen- und Frequenzrelationen) folgt, dass die volle
Kopplungsenergie eine Phaseninformation enthält. Die Projektion
auf die reale Zeitachse (α = 0) ergibt die Grundform.

---

## 5. Frequenzabhängigkeit

- Für f → 0: Energie vernachlässigbar (Axiom 1)
- Linearer Anstieg mit f bei konstanter Kopplung
- Bei harmonischem Verhältnis f₁/f₂ = n/m: maximale
  Resonanzgewichtung G (Axiom 3)

**Resonanzreaktor-Anwendung:** Die GDR-Frequenzen f_GDR = E_GDR/(π·ℏ)
folgen direkt aus der Grundform. Für U-235: f = 6.3 × 10²¹ Hz
bei E_GDR = 13.0 MeV.

---

## 6. Nutzbare Energie und Dissipation

In realen Systemen tritt Dissipation auf. Die nutzbare Energie
nach Abzug der Verluste:

```
    E_nutz(f) = π · ε · ℏ · f · (1 − γ(f))
```

wobei γ(f) der frequenzabhängige Dissipationsfaktor ist.

Für ein System mit exponentieller Dämpfung:

```
    γ(f) = 1 − e^(−f/f_c)
```

wobei f_c die kritische Frequenz ist, oberhalb derer Dissipation
vernachlässigbar wird. Bei hohen Frequenzen (f ≫ f_c) gilt
γ → 0 und E_nutz → π·ε·ℏ·f.

In FLRW-Simulationen tritt die Hubble-Reibung als kosmologische
Dissipationsquelle auf: d_η wächst mit H₀ (Steigung
0.00113 ± 0.00017 pro km/s/Mpc).

---

## 7. Leistung über ein Frequenzintervall

```
    P(f₁, f₂) = ∫_{f₁}^{f₂} π · ε(f) · ℏ · f · (1 − γ(f)) df
```

Für konstantes ε und vernachlässigbare Dissipation:

```
    P = (π · ε · ℏ / 2) · (f₂² − f₁²)
```

---

## 8. Vergleich zur klassischen Energiebeschreibung

| Eigenschaft | Klassisch | RFT |
|-------------|-----------|-----|
| Energieformel | E = ℏω | E = π·ε·ℏ·f |
| Kopplungseffizienz | Nicht modelliert | ε(Δφ) ∈ [0, 1] |
| Geometrie | Nicht enthalten | π aus Kopplungsgeometrie |
| Phasenstruktur | Nicht enthalten | e^{iα} |
| Dissipation | Separat modelliert | Integriert über γ(f) |
| Zerfall | λ = const | λ_eff = λ₀ + η·Φ·σ |
| Freie Parameter | — | Keine (ε = η, κ = 1) |
| Grundzustand | E = ½ℏf | ε = 1/(2π) → E = ½ℏf |

---

## 9. Anwendungen

| Domäne | Anwendung der Gleichung | Ergebnis |
|--------|------------------------|----------|
| Teilchenphysik | Resonanzbedingung bei M₀ | 5 Resonanzen, emp. p = 0 |
| Kosmologie | Klein-Gordon in FLRW | η ≈ cos², Δχ² = +16 |
| Resonanzreaktor | f_GDR = E_GDR/(π·ℏ) | κ = 1, Q_fiss ≈ 1.0 |
| Doppelpendel | Dynamische Kopplungseffizienz ε(θ₂−θ₁) | ε = cos²(Δθ/2) bestätigt |
| Energiespeicherung | Phasensteuerung → Verlustminimierung | Axiom 6 |
| Messtechnik | Phasenmodulation → Energiefluss-Monitoring | Axiome 5, 6 |

---

## 10. Fazit

Die Resonanzfeld-Gleichung E = π·ε·ℏ·f verallgemeinert die
klassische Planck-Relation durch:

1. Die Kopplungseffizienz ε(Δφ) ∈ [0, 1] als zentrale Größe
2. Die Identität ε = η (Operator = Observable, kein freier Parameter)
3. Den geometrischen Faktor π aus der Kopplungsgeometrie
4. Die phasenmodulierte Erweiterung e^{iα} für komplexe Zeitstruktur
5. Den Planck-Grundzustand als Spezialfall ε = 1/(2π)

Empirisch validiert in vier Domänen: Teilchenphysik, Kosmologie,
Nukleartechnologie und Klassische Mechanik.

---

© Dominic-René Schu — Resonanzfeldtheorie 2025/2026

---

[Zurück zur Übersicht](../../../README.md)