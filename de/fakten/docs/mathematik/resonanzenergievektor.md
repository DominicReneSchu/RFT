# Resonanzenergievektor als Richtungsgröße

*Dominic-René Schu, 2025/2026*

---

## Einleitung

In der klassischen Physik wird Energie als skalare Größe behandelt.
Die Richtung der Energieübertragung wird nur implizit (durch Impuls
oder Strahlungsrichtung) betrachtet. Die Resonanzfeldtheorie
(Axiom 5) macht diese Richtung explizit als zentrale physikalische
Größe nutzbar: Energie wird als gerichteter Vektor im
**Resonanzraum** aufgefasst.

**Definition Resonanzraum:** Abstrakter Richtungsraum, in dem jede
Energieform eine eindeutige Ausbreitungsrichtung besitzt. Er
ergänzt den klassischen Ortsraum um eine energetische
Orientierungsdimension.

---

## 1. Energie als gerichteter Vektor

Die Resonanzfeldtheorie postuliert (Axiom 5), dass jeder
Energieform ein Vektor im Resonanzraum zugeordnet werden kann:

```
    E⃗ = |E| · ê
```

- E⃗: Resonanzenergievektor
- |E|: Klassischer Betrag (E = π · ε · h · f, Axiom 4)
- ê: Normierte Richtung im Resonanzraum

---

## 2. Quantisierung und Eigenrichtungen

Energiezustände sind durch Frequenz und Richtung definiert:

```
    E⃗ₙ = h · fₙ · êₙ
```

- fₙ: Resonanzfrequenz
- êₙ: Eigenrichtung (Richtungsquantenzustand)

Dies erweitert die klassische Quantisierung um eine vektoriell-
richtungsabhängige Komponente, analog zu Spinorientierungen.

---

## 3. Kopplung und Energieübertragung

Die Übertragung erfolgt durch Projektion des Energievektors auf
die Richtung des Zielsystems:

```
    ΔE⃗_eff = κ · (E⃗₁ · ê₂) · ê₂
```

- κ ∈ [0, 1]: Kopplungskoeffizient (Resonanzgüte)
- E⃗₁ · ê₂: Skalarprodukt = Projektion auf Empfangsrichtung

Der skalare Übertragungsanteil:

```
    E_eff = κ · |E⃗₁| · cos(θ)
```

Die Kopplungseffizienz:

```
    η = κ · cos²(θ)
```

| Winkel θ | E_eff (κ=1) | η |
|----------|-------------|---|
| 0° | 1.0 | 1.0 |
| 45° | 0.707 | 0.5 |
| 90° | 0.0 | 0.0 |

**Vergleich mit dem Poynting-Vektor:**
Der klassische Poynting-Vektor S = (1/μ₀) · E_el × B beschreibt
den Energiefluss im elektromagnetischen Feld. Der
Resonanzenergievektor ist allgemeiner: Er erfasst quantisierte
Richtungszustände und ist nicht auf elektromagnetische Felder
beschränkt.

---

## 4. Tensorielle Beschreibung

In Systemen mit mehreren Kopplungen:

```
    E⃗_res = Σ_{i,j} T_ij(fᵢ, fⱼ) · (E⃗ᵢ · E⃗ⱼ) · ê_ij
```

- T_ij: Frequenzabhängige Komponenten des Kopplungstensors
- ê_ij: Resultierender Richtungsvektor

Der Tensor beschreibt die gewichtete Überlagerung mehrerer
Energiepfade — formal analog zum Suszeptibilitätstensor in
der Elektrodynamik.

---

## 5. Experimentelle Zugänglichkeit

- **Polarisationsexperimente:** Intensitätsverläufe als Funktion
  von θ zwischen Sender und Empfänger
- **Phased-Array-Antennen:** Richtungsabhängigkeit des
  Energietransfers im Frequenzraum
- **Molekularspektroskopie:** Richtungsabhängigkeit bei
  vibronischen Übergängen (FRET)
- **Stern-Gerlach-Experiment:** Neue Interpretation der
  beobachteten Aufspaltung als Eigenrichtungen im Resonanzraum

---

## Glossar

- **Resonanzraum:** Abstrakter Richtungsraum für Energieausbreitung
- **ê:** Normierte Richtung im Resonanzraum
- **êₙ:** Eigenrichtung (Richtungsquantenzustand)

---

## Literatur

- Born, M. & Wolf, E. (1999). *Principles of Optics*. Cambridge.
- Dirac, P. A. M. (1981). *The Principles of Quantum Mechanics*. Oxford.
- Feynman, R. P. et al. (1964). *The Feynman Lectures on Physics*. Addison-Wesley.
- Landau, L. D. & Lifschitz, E. M. (1987). *Lehrbuch der Theoretischen Physik, Bd. 1*. Akademie-Verlag.
- Penrose, R. (2004). *The Road to Reality*. Jonathan Cape.

---

© Dominic-René Schu — Resonanzfeldtheorie 2025/2026

---

[Zurück zur Übersicht](../../../README.md)