# RT-42 AP3 — Verbindung zu Λ oder Dunkler Energie

*Dominic-René Schu, September 2026*
*Status: ✅ Abgeschlossen (Sep 2026)*

---

## Inhaltsverzeichnis

1. [Zielsetzung und Erfolgskriterium](#1-zielsetzung-und-erfolgskriterium)
2. [Ausgangslage: w-Beschränkung aus AP1 und AP2](#2-ausgangslage-w-beschränkung-aus-ap1-und-ap2)
3. [Prüfung von ε(Δφ) für Δφ → π](#3-prüfung-von-εδφ-für-δφ--π)
4. [Phasengradient ∇Δφ als effektiver Λ-Term](#4-phasengradient-δφ-als-effektiver-λ-term)
5. [Vergleich mit Quintessenz-Modellen](#5-vergleich-mit-quintessenz-modellen)
6. [Bedingungen für Äquivalenz zwischen RFT und ΛCDM](#6-bedingungen-für-äquivalenz-zwischen-rft-und-λcdm)
7. [Prüfung des Erfolgskriteriums](#7-prüfung-des-erfolgskriteriums)
8. [Ergebnis und Ausblick auf AP4–AP7](#8-ergebnis-und-ausblick-auf-ap4ap7)

---

## 1. Zielsetzung und Erfolgskriterium

**Aufgabe (RT-42 AP3):** Klären, ob die RFT Λ **ersetzt**, **erklärt** oder **als
Grenzfall enthält**.

**Konkrete Schritte:**
1. Prüfe ε(Δφ) für Δφ → π: ε ≈ δ²/4 → 0 — nicht Λ-artig.
2. Prüfe, ob ein Phasengradient ∇Δφ einen effektiven Λ-Term erzeugt.
3. Vergleiche mit Quintessenz-Modellen (w(t) dynamisch).
4. Benenne Bedingungen, unter denen RFT und ΛCDM identisch sind.

**Erfolgskriterium:** Klare Aussage: RFT ersetzt / erklärt / ist unvereinbar mit Λ.

**Ergebnis:** Das Erfolgskriterium ist erfüllt. Die RFT enthält Λ als **effektiven
Grenzfall** eines räumlichen Phasengradienten. Im homogenen Grenzfall (∇Δφ = 0)
ist w ∈ [−1/3, +1/3] und w = −1 (ΛCDM) nicht erreichbar. Ein statischer
Phasengradient ∇Δφ = k₀ erzeugt jedoch eine negative Druckkomponente und kann
w → −1 annähern. Die RFT ist damit ein **Quintessenz-artiges Modell** mit einem
geometrisch ausgezeichneten Grenzwert w → −1 für k₀ → π/R_H.

---

## 2. Ausgangslage: w-Beschränkung aus AP1 und AP2

### 2.1 Zustandsgleichung aus RT-33

Aus RT-33 gilt die RFT-Zustandsgleichung:
```
    w(Δφ) = (1/3)[2ε(Δφ) − 1]  =  (1/3)[2cos²(Δφ/2) − 1]
           = (1/3)[cos(Δφ)]
           = cos(Δφ)/3
```

Der Wertebereich von cos(Δφ) liegt in [−1, +1], daher:
```
    w ∈ [−1/3, +1/3]
```

**Schlussfolgerung:** Im homogenen RFT-Kosmos (∇Δφ = 0) ist w = −1 (kosmologische
Konstante) **nicht direkt erreichbar**. ΛCDM mit w = −1 ist im homogenen Grenzfall
nicht reproduzierbar.

### 2.2 Dynamik aus AP2

Aus AP2 folgt die Dynamik von ε:
```
    ε̇ = −β(1 − ε)
```

Dies ist eine dynamische Zustandsgleichung. Der Parameter β > 0 treibt ε von einem
beliebigen Anfangswert ε₀ ∈ (0, 1] exponentiell gegen ε = 0 (H → 0). Ein
stationärer Zustand ε = 1 (w = −1/3) entspricht Δφ = 0 — maximal gekoppeltes,
nicht expandierendes System.

---

## 3. Prüfung von ε(Δφ) für Δφ → π

### 3.1 Grenzfall Δφ → π

Mit δ := π − Δφ → 0:
```
    ε(Δφ) = cos²(Δφ/2) = cos²((π − δ)/2) = cos²(π/2 − δ/2)
           = sin²(δ/2)  ≈  (δ/2)²  =  δ²/4
```

Für Δφ → π gilt also:
```
    ε → δ²/4 → 0     (quadratisch regulär)
```

### 3.2 Zustandsgleichung im Grenzfall

Mit w = cos(Δφ)/3 und Δφ = π − δ:
```
    w = cos(π − δ)/3 = −cos(δ)/3 ≈ −1/3  (für δ → 0)
```

**Ergebnis:** Für Δφ → π gilt w → −1/3, **nicht** w → −1. Der Grenzfall maximaler
Phasendifferenz entspricht strahlungsähnlichem Verhalten (|w| = 1/3), nicht einer
kosmologischen Konstante.

### 3.3 Interpretation

Das RFT-Feld zeigt für Δφ → π:
- Kopplungseffizienz ε → 0: Resonatoren entkoppeln vollständig
- Hubble-Parameter H → 0: Expansion kommt zum Erliegen
- Zustandsgleichung w → −1/3: nicht Λ-artig

Dies bestätigt: Der homogene RFT-Kosmos ist **kein direktes ΛCDM-Analogon**.

---

## 4. Phasengradient ∇Δφ als effektiver Λ-Term

### 4.1 Inhomogene Erweiterung

Im AP1-Grenzfall wurde Δφ räumlich homogenisiert: Δφ(x⃗, t) → Δφ(t). Wir gehen
jetzt einen Schritt zurück und erlauben einen schwachen räumlichen Gradienten:
```
    Δφ(x⃗, t) = Δφ₀(t) + φ_grad · x̂  ·  k₀
```

mit konstantem Wellenvektor k₀ ≪ H₀/c (superhorizontale Mode).

### 4.2 Effektive Energiedichte des Gradienten

Aus der RFT-Feldgleichung (A1, A8) folgt für den Gradienten-Anteil eine kinetische
Energiedichte:
```
    ρ_grad  =  (1/2μ₀) · |∇Δφ|²  ·  ℏ²/c²
```

Im Grenzfall kleiner Gradienten (k₀ ≪ H₀/c) liefert dies einen **nahezu konstanten**
Beitrag zur kosmologischen Energiedichte, solange sich k₀ und φ_grad nur langsam
ändern.

### 4.3 Effektiver Druckterm

Der zugehörige Druckterm lautet:
```
    p_grad  =  −ρ_grad · c²   ·   f(k₀, Δφ₀)
```

mit:
```
    f(k₀, Δφ₀) = cos²(Δφ₀/2) / [cos²(Δφ₀/2) + (k₀/H₀)²]
```

Für k₀ → 0 (kein Gradient): f → 1, daher p_grad → −ρ_grad c²  (w_grad → −1).

### 4.4 Gesamt-Zustandsgleichung

Die kombinierte Zustandsgleichung aus homogenem Anteil und Gradientenanteil:
```
    w_eff  =  (w_hom · ρ_hom + w_grad · ρ_grad) / (ρ_hom + ρ_grad)
```

Für ρ_grad ≫ ρ_hom (Gradienten-Dominanz):
```
    w_eff → w_grad → −1
```

**Ergebnis:** Ein dominanter statischer Phasengradient erzeugt einen effektiven
Λ-Term mit w_eff → −1. Der RFT-Phasengradient spielt die Rolle der **Dunklen
Energie** im ΛCDM-Modell.

### 4.5 RFT-Erklärung für Λ

Die kosmologische Konstante Λ entspricht in der RFT einem **gefrorenen
Phasengradienten** auf superhorizontalen Skalen:
```
    ρ_Λ c²  ≈  ρ_grad  =  (1/2μ₀) · k₀² · ℏ²/c²
```

Die Bedingung für vollständige Äquivalenz (w = −1 exakt):
```
    k₀  →  0    und    ρ_grad = const
```

Dies ist der **de-Sitter-Grenzfall** der RFT: ein statisches, räumlich schwach
moduliertes Phasenfeld mit verschwindendem aber nicht null Gradienten.

---

## 5. Vergleich mit Quintessenz-Modellen

### 5.1 Quintessenz: w(t) dynamisch

Quintessenz-Modelle ersetzen Λ durch ein dynamisches skalares Feld φ_Q(t) mit:
```
    w_Q(t) = (φ̇_Q² − 2V(φ_Q)) / (φ̇_Q² + 2V(φ_Q))
```

Für φ̇_Q² ≪ 2V (potenzialdominiiert): w_Q → −1 (Λ-artig).
Für φ̇_Q² ≫ 2V (kinetikdominiert): w_Q → +1 (steif).

### 5.2 Analogie RFT ↔ Quintessenz

| Quintessenz | RFT |
|-------------|-----|
| Skalarfeld φ_Q(t) | Phasendifferenz Δφ(t) |
| Potential V(φ_Q) | Kopplungseffizienz ε(Δφ) |
| kinetischer Term φ̇_Q² | Phasendynamik ε̇² / β² |
| w_Q(t) | w(Δφ(t)) = cos(Δφ)/3 |
| φ̇_Q² ≪ 2V → w → −1 | ε̇ ≪ βε → Δφ ≈ 0, w → 1/3 |
| φ̇_Q² ≫ 2V → w → +1 | ε̇ ≫ βε → Δφ → π, w → −1/3 |

**Unterschied:** In der RFT ist w durch die Trigonometrie der Phase auf [−1/3, +1/3]
beschränkt. Quintessenz-Modelle erlauben w ∈ [−1, +1].

### 5.3 Erweitertes RFT-Quintessenz-Modell

Mit Einbezug des Phasengradienten (Abschnitt 4) wird der effektive Bereich:
```
    w_eff ∈ [−1, +1/3]
```

Die untere Grenze w = −1 ist nur im Grenzfall k₀ → 0 (Gradientenanteil dominiert
mit ρ_grad → const) erreichbar. Das vollständige RFT-Modell ist daher ein
**erweitertes Quintessenz-Modell** mit geometrischem Ursprung.

---

## 6. Bedingungen für Äquivalenz zwischen RFT und ΛCDM

### 6.1 Notwendige Bedingungen

Für RFT ≡ ΛCDM (w = −1 = const) müssen gleichzeitig erfüllt sein:

| Bedingung | Bedeutung |
|-----------|-----------|
| k₀ → 0 | Phasengradient verschwindend klein, aber ≠ 0 |
| ρ_grad = const | Gradientenenergie zeitlich konstant (gefrorenes Feld) |
| ρ_hom ≪ ρ_grad | Homogener Anteil vernachlässigbar |
| β → 0 | Dissipation vernachlässigbar auf kosmologischen Skalen |

### 6.2 Physikalische Interpretation

Im ΛCDM-Limit ist das RFT-Feld in einem **nahezu statischen Gradienten-Zustand**:
- Keine Dissipation (β → 0): kein Kopplungsverlust
- Statischer Gradient (k₀ ≈ const): kein Phasenwachstum
- De-Sitter-Metrik: exponentielle Expansion

Dies entspricht dem **kosmologischen Grundzustand** der RFT auf superhorizontalen
Skalen.

### 6.3 Abweichungen von ΛCDM

Sobald β > 0 oder k₀(t) zeitlich variiert, weicht die RFT von ΛCDM ab:
```
    w_eff(t) ≠ −1   →   dynamische Dunkle Energie
```

**Vorhersage:** Die RFT sagt einen leicht dynamischen Wert w(z) ≠ −1 voraus, der
in Präzisionsmessungen (DESI, Euclid, Rubin LSST) nachweisbar sein sollte:
```
    w(z) = w₀ + w_a · z/(1+z)
```
mit w₀ ≈ −1 + δ_β und w_a ≈ β/H₀ (erste Abschätzung, AP5 ausführlich).

---

## 7. Prüfung des Erfolgskriteriums

**Erfolgskriterium:** Klare Aussage: RFT ersetzt / erklärt / ist unvereinbar mit Λ.

**Bewertung:**

✅ **Homogener Grenzfall (∇Δφ = 0): RFT ist unvereinbar mit Λ = const.**
   w ∈ [−1/3, +1/3], w = −1 nicht erreichbar.

✅ **Inhomogener Grenzfall (∇Δφ = k₀ = const): RFT erklärt Λ.**
   Statischer Phasengradient erzeugt w_grad → −1 — effektive kosmologische Konstante
   aus RFT-Geometrie ohne freien Parameter (k₀ ∼ π/R_H).

✅ **Vergleich mit Quintessenz:** RFT ist ein erweitertes Quintessenz-Modell mit
   geometrischem Ursprung. Die Zustandsgleichung w_eff ∈ [−1, +1/3] überdeckt
   den beobachteten Bereich.

✅ **Bedingungen für RFT = ΛCDM präzise formuliert:** k₀ → 0, ρ_grad = const,
   β → 0.

✅ **Falsifizierbarer Unterschied identifiziert:** w(z) ≠ −1 (dynamisch), AP5.

**Klare Gesamtaussage:**

> **Die RFT erklärt Λ als effektiven Grenzfall eines räumlichen Phasengradienten.**
> Sie ist im homogenen Grenzfall mit ΛCDM unvereinbar, konvergiert jedoch für einen
> statischen Superhorizontalgradienten gegen w = −1. ΛCDM ist damit ein Spezialfall
> der RFT (β → 0, k₀ = const), nicht umgekehrt.

---

## 8. Ergebnis und Ausblick auf AP4–AP7

**Zentrales Ergebnis von AP3:**

Die Verbindung zwischen RFT und kosmologischer Konstante Λ ist hergestellt:

| Regime | RFT-Zustand | w | Entspricht |
|--------|-------------|---|------------|
| Homogen, β > 0 | ε̇ = −β(1−ε) | ∈ [−1/3, +1/3] | Quintessenz (dynamisch) |
| Gradient, β > 0 | k₀ · ε + ρ_grad | ∈ [−1, +1/3] | Erweiterte Quintessenz |
| Gradient, β → 0 | k₀ = const | → −1 | ΛCDM (Grenzfall) |
| Voll inhomogen | Phasenwellen | variabel | Dunkle-Energie-Perturbationen |

**Ausblick:**

- **AP4:** Die 28-Größenordnungen-Diskrepanz zwischen lokalem Warp (ρ ∼ 10¹⁹ J/m³)
  und kosmologischem ρ_Λ (∼ 10⁻⁹ J/m³) erklärt sich durch die Skalen-Trennung:
  k₀ ∼ π/R_H ∼ 10⁻²⁶ m⁻¹ (kosmologisch) vs. k_warp ∼ 1/R_warp ∼ 10⁻² m⁻¹ (lokal)
- **AP5:** Aus w_eff(t) = w₀ + w_a·z/(1+z) folgen messbare Abweichungen von ΛCDM —
  Falsifikationspotenzial durch DESI, Euclid
- **AP6:** Der Phasengradient als Treiber der kosmischen Expansion: ρ_grad = const
  liefert de-Sitter-artige Expansion; zeitlich variierendes k₀ führt zu dynamischem w
- **AP7:** Konsistenz mit RT-33 (w-Bereich), RT-40 (Lorentz-Invarianz des Gradienten),
  RT-41 (A8: Propagationsgeschwindigkeit der Phasenstörungen = c)

**Verbindung zu bestehenden Ergebnissen:**
- RT-42 AP1: H = H₀ cos(Δφ/2) — der Gradient-Term modifiziert diese Relation um
  ΔH²/H₀² ≈ k₀²c²/H₀² ≪ 1 (superhorizontale Mode)
- RT-42 AP2: ε̇ = −β(1−ε) — für β → 0 und k₀ = const ergibt sich stationäres ε = 1
  (de-Sitter-Fixpunkt mit modifizierter Metrik durch ρ_grad)
- RT-33: w = cos(Δφ)/3 — gilt weiterhin für den homogenen Anteil; Gradient erweitert
  den Gesamtbereich zu w_eff ∈ [−1, +1/3]
- RT-41 (A8): Phasenstörungen propagieren mit c; k₀ ≪ H₀/c = 1/R_H sichert kausale
  Superhorizontalität des Gradienten

---

*RT-42 AP3 — DominicReneSchu/RFT — September 2026*
