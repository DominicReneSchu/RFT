# Die Resonanzfeld-Gleichung

*Dominic-René Schu, 2025/2026*

---

## 1. Einleitung

Die Resonanzfeld-Gleichung verknüpft Resonanzfrequenz, Kopplungseffizienz
und Energiefluss. Sie ist die zentrale Energiegleichung der
Resonanzfeldtheorie, abgeleitet aus Axiom 4
(siehe [axiomatische Grundlegung](axiomatische_grundlegung.md)).

---

## 2. Grundform

```
    E_eff = π · ε(Δφ) · h · f
```

- **ε(Δφ)**: Kopplungseffizienz, ε ∈ [0, 1]
  (siehe [Vereinheitlichte Definition](kopplungseffizienz.md))
- **π**: Geometrischer Faktor aus der zyklischen Kopplungsgeometrie
- **h**: Plancksches Wirkungsquantum
- **f**: Resonanzfrequenz

---

## 3. Phasenmodulierte Form

Unter Einbeziehung der komplexen Zeitstruktur (§5 der
[axiomatischen Grundlegung](axiomatische_grundlegung.md)):

```
    E = π · ε · h · f · e^{iα}
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

## 4. Frequenzabhängigkeit

- Für f → 0: Energie vernachlässigbar (Axiom 1)
- Linearer Anstieg mit f bei konstanter Kopplung
- Bei harmonischem Verhältnis f₁/f₂ = n/m: maximale
  Resonanzgewichtung G (Axiom 3)

---

## 5. Nutzbare Energie und Dissipation

In realen Systemen tritt Dissipation auf. Die nutzbare Energie
nach Abzug der Verluste:

```
    E_nutz(f) = π · ε · h · f · (1 − γ(f))
```

wobei γ(f) der frequenzabhängige Dissipationsfaktor ist.

Für ein System mit exponentieller Dämpfung:

```
    γ(f) = 1 − e^{−f/f_c}
```

wobei f_c die kritische Frequenz ist, oberhalb derer Dissipation
vernachlässigbar wird. Bei hohen Frequenzen (f ≫ f_c) gilt
γ → 0 und E_nutz → π·ε·h·f.

---

## 6. Leistung über ein Frequenzintervall

```
    P(f₁, f₂) = ∫_{f₁}^{f₂} π · ε(f) · h · f · (1 − γ(f)) df
```

Für konstantes ε und vernachlässigbare Dissipation:

```
    P = (π · ε · h / 2) · (f₂² − f₁²)
```

---

## 7. Vergleich zur klassischen Energiebeschreibung

| Eigenschaft | Klassisch (E = h·f) | RFT (E = π·ε·h·f) |
|-------------|--------------------|--------------------|
| Kopplungseffizienz | Nicht modelliert | ε(Δφ) ∈ [0,1] |
| Geometrie | Nicht enthalten | π aus Kopplungsgeometrie |
| Phasenstruktur | Nicht enthalten | e^{iα} |
| Dissipation | Separat modelliert | Integriert über γ(f) |
| Grenzfall | — | ε = 1/π → E = h·f |

---

## 8. Anwendungen

- **Resonanzbasierte Energiegewinnung:** Nutzung spezifischer
  Frequenzbereiche zur Maximierung der Energieausbeute in
  Schwingungssystemen (Axiome 1, 3, 4)
- **Effiziente Energiespeicherung:** Steuerung von
  Phasenverschiebungen zur Minimierung von Verlusten (Axiom 6)
- **Mess- und Steuerungstechnik:** Phasenmodulation zur
  Echtzeit-Überwachung von Energieflüssen (Axiome 5, 6)

---

## 9. Fazit

Die Resonanzfeld-Gleichung E = π·ε·h·f verallgemeinert die
klassische Planck-Gleichung durch:

1. Die Kopplungseffizienz ε als zentrale physikalische Größe
2. Den geometrischen Faktor π aus der Kopplungsgeometrie
3. Die phasenmodulierte Erweiterung e^{iα} für komplexe Zeitstruktur

---

© Dominic-René Schu — Resonanzfeldtheorie 2025/2026

---

[Zurück zur Übersicht](../../../README.md)