# Resonanzfeldtheorie (Version 4.0)

[![Lizenz: Schu-Lizenz 1.4](https://img.shields.io/badge/Lizenz-Schu--Lizenz%201.4-blue.svg)](lizenz/schu-lizenz_v1.4.md)

Willkommen im offiziellen Repository der **Resonanzfeldtheorie (RFT)**.
Dieses Projekt vereint Mathematik, Physik und Technik zu
einem axiomatischen Modell der Resonanz. Die Theorie beschreibt
fundamentale Prozesse als Kopplungs- und Resonanzphänomene in
Schwingungsfeldern — formal gegründet auf 7 Axiome (A1–A7).

**Empirisch validiert in vier Domänen:** Teilchenphysik
(1.500.000 Monte-Carlo-Simulationen, 5 Resonanzen, emp. p = 0),
Kosmologie (1.530 FLRW-Simulationen, Δd_η > 6σ),
Nukleartechnologie (Resonanzreaktor, κ = 1) und
Finanzmärkte (ResoTrade, +26.3% vs HODL, Live seit Feb. 2026).

---

## ☰ Inhaltsverzeichnis

- [Grundformel und zentrale Größen](#grundformel-und-zentrale-größen)
- [Axiomensystem (Kurzfassung)](#axiomensystem-kurzfassung)
- [Empirische Validierung](#empirische-validierung)
- [PDF-Zusammenfassung](#pdf-zusammenfassung)
- [Peer Review](#peer-review)
- [Inhalt](#inhalt)
    - [Axiomatik und Definitionen](#axiomatik-und-definitionen)
    - [Mathematik und Physik](#mathematik-und-physik)
    - [Konzepte](#konzepte)
    - [Simulationen](#simulationen)
    - [Empirische Nachweise](#empirische-nachweise)
- [Lizenz](#lizenz)

---

## Grundformel und zentrale Größen

Die zentrale Gleichung der Resonanzfeldtheorie (Axiom 4):

$$
E = \pi \cdot \varepsilon(\Delta\phi) \cdot \hbar \cdot f
$$

| Symbol | Name | Bedeutung |
|:------:|:-----|:----------|
| **π** | Kreiszahl | Geometrischer Faktor aus der zyklischen Kopplungsgeometrie |
| **ε(Δφ)** | Kopplungseffizienz | Anteil übertragener Resonanzenergie, ε ∈ [0, 1] |
| **ℏ** | Red. Planck-Konstante | Wirkungsquantum (ℏ = h/2π) |
| **f** | Frequenz | Schwingungsfrequenz der gekoppelten Mode |

### Kopplungseffizienz ε

Die Kopplungseffizienz beschreibt, welcher Anteil der maximal
möglichen Resonanzenergie tatsächlich zwischen zwei gekoppelten
Moden übertragen wird.

**Standardmodell:** ε(Δφ) = cos²(Δφ/2) = ½(1 + cos Δφ)

| Kopplungszustand | ε | Energie |
|------------------|---|---------|
| Perfekte Kopplung (Δφ = 0) | 1 | π·ℏ·f |
| Planck-Spezialfall (Grundzustand) | 1/(2π) ≈ 0.159 | ½·ℏ·f |
| Natürliche Dämpfung | 1/e ≈ 0.368 | (π/e)·ℏ·f |
| Halbe Kopplung (Δφ = π/2) | 0.5 | π·ℏ·f/2 |
| Keine Kopplung (Δφ = π) | 0 | 0 |

Der Faktor π entsteht aus der Integration der Kopplungseffizienz
über einen Halbzyklus des Phasenraums — nicht als freier Parameter.
Die Planck-Grundzustandsenergie E = ½ℏf ist der Spezialfall
ε = 1/(2π).

### Identität ε = η

Die FLRW-Simulationen zeigen: Der theoretische Operator ε und
die messbare Observable η (Kreuzterm zweier gekoppelter
Skalarfelder) sind identisch:

$$
\varepsilon(\Delta\phi) = \eta(\Delta\phi) = \cos^2(\Delta\phi / 2)
$$

Diese Identität eliminiert den letzten freien Parameter:
Im Resonanzreaktor folgt κ = 1 exakt.

Vollständige Definition: [Kopplungseffizienz](fakten/docs/definitionen/kopplungseffizienz.md)

---

![Visualisierung der Resonanzfeldtheorie](bilder/visualisierung_RFT.png)

*Abb. 1: Symbolische Darstellung der Wechselwirkung von π, ℏ, ε und f im Resonanzraum*

---

## Axiomensystem (Kurzfassung)

Die RFT besteht aus 7 Kern-Axiomen, die minimal, unabhängig, formal
präzise und empirisch testbar sind:

| Axiom | Kernaussage | Formel |
|-------|-------------|--------|
| A1 | Universelle Schwingung | ψ = A·cos(kx − ωt + φ) |
| A2 | Superposition | Φ = Σ ψᵢ |
| A3 | Resonanzbedingung | \|f₁/f₂ − m/n\| < δ |
| A4 | Kopplungsenergie | E = π·ε·ℏ·f |
| A5 | Energierichtung | E⃗ = E·ê(Δφ, ∇Φ) |
| A6 | Informationsfluss | MI > 0 ⟺ PCI > 0 |
| A7 | Invarianz (G_sync) | G(fᵢ/fⱼ) = G(T(fᵢ)/T(fⱼ)) |

Zusätzlich gibt es eine interpretative Erweiterung:
- **E1 (Beobachter als Resonator):** Folgt aus A1, A3, A6

Vollständige Formalisierung: [Axiomatische Grundlegung](fakten/docs/definitionen/axiomatische_grundlegung.md)

---

## Empirische Validierung

Die RFT wird an vier unabhängigen Domänen empirisch validiert:

| Domäne | Methode | Ergebnis | Axiome |
|--------|---------|----------|--------|
| Teilchenphysik | 1.500.000 MC-Sim. auf CMS-Daten | 5 Resonanzen, emp. p = 0 | A3, A7 |
| Kosmologie | 1.530 FLRW-Simulationen | Δd_η > 6σ, Δχ² = +16 vs CMB | A1, A3–A5, A7 |
| Nukleartechnologie | Resonanzreaktor (GDR-basiert) | κ = 1, Q_fiss ≈ 1.0 | A1, A3, A4 |
| Finanzmärkte | ResoTrade (24 Mo., 4 Regime) | +26.3% vs HODL, Live +4.13% | A1–A7 |

**Falsifikationstests:**
- Altcoin-Analyse: 200.000 Episoden, Draw-Rate 98.4% (A3 bestätigt negativ)
- Klassische Indikatoren: RSI, MACD, Momentum — alle Korrelation < 0.05
- Resonanzreaktor-Vorhersage: σ_coh > σ_incoh (experimentell prüfbar)

---

## PDF-Zusammenfassung

Die ausführliche Zusammenfassung der Resonanzfeldtheorie als PDF:
[**RFT_Zusammenfassung.pdf**](./RFT_Zusammenfassung.pdf)

---

## Peer Review

Ein Peer-Review-Verfahren wird aktiv angestrebt:
[**rft_manuskript_de_iop.pdf**](peer_review_rft/manuskript_de/rft_manuskript_de_iop.pdf)

---

# Inhalt

## Axiomatik und Definitionen

| # | Dokument | Axiome | Beschreibung |
|---|----------|--------|-------------|
| 1 | [Axiomatische Grundlegung](fakten/docs/definitionen/axiomatische_grundlegung.md) | A1–A7 | Formale Axiome A1–A7 mit Beweisen und empirischen Tests |
| 2 | [Kopplungseffizienz ε](fakten/docs/definitionen/kopplungseffizienz.md) | A1–A7 | Vereinheitlichte Definition, ε = η Identität |
| 3 | [Energie als fundamentale Größe](fakten/docs/definitionen/energie_als_urkonstante.md) | A1–A5, A7 | Interpretative Hypothese: Alle Größen aus E |
| 4 | [Resonanzlexikon](fakten/docs/definitionen/resonanzlexikon.md) | A1–A7 | Glossar der RFT-Begriffe |
| 5 | [Resonanzlogische DGL](fakten/docs/definitionen/resonanzlogische_differentialgleichungen.md) | A1–A4, A6, A7 | Klassische DGLs als Projektionen der rDGL |

## Mathematik und Physik

| # | Dokument | Axiome | Beschreibung |
|---|----------|--------|-------------|
| 1 | [Resonanzintegrale](fakten/docs/mathematik/resonanzintegrale.md) | A1–A4, A7 | Analytische Methoden — Dirichlet-Integral als Resonanzenergie |
| 2 | [Resonanzfeld-Gleichung](fakten/docs/mathematik/resonanzfeld_gleichung.md) | A1, A3, A5, A6 | Zentrale Energiegleichung E = π·ε·ℏ·f |
| 3 | [Kopplungsenergie: Spezialfälle](fakten/docs/mathematik/kopplungsenergie.md) | A4 | Grenzfälle ε = 1, 1/(2π), 1/e, 0 |
| 4 | [Resonanzzeitkoeffizient τ*](fakten/docs/mathematik/tau_resonanzkoeffizient.md) | A4 | Zeitskala der Kopplung: τ*(Δφ) = π/ε(Δφ) |
| 5 | [Energierichtung](fakten/docs/mathematik/energierichtung.md) | A2, A4, A5, A6 | Energie als Vektor mit Drehsinn |
| 6 | [Energiekugel](fakten/docs/mathematik/energiekugel.md) | A1, A2, A4, A5, A7 | Geometrisches Modell — Phasenstruktur und dunkle Energie |
| 7 | [Resonanzenergievektor](fakten/docs/mathematik/resonanzenergievektor.md) | A4, A5 | Energie als Richtungsgröße im Resonanzraum |
| 8 | [Energieübertragung](fakten/docs/mathematik/energieuebertragung.md) | A1, A3, A4, A6 | Prinzipien und Gleichungen der Übertragung |
| 9 | [Resonanzkoordinaten](fakten/docs/mathematik/resonanzkoordinaten.md) | A1, A4 | Tangens-Halbwinkel-Parametrisierung |
| 10 | [Doppelpendel](fakten/docs/mathematik/doppelpendel.md) | A1, A2, A4 | Klassische Mechanik und RFT-Perspektive |

---

## Konzepte

| # | Konzept | Axiome | Beschreibung |
|---|---------|--------|-------------|
| 1 | [ResoCalc](fakten/konzepte/ResoCalc/resocalc.md) | A1, A3, A4 | Drehmomentberechnung im Resonanzfeld |
| 2 | [Resonanzreaktor](fakten/konzepte/resonanzreaktor/README.md) | A1, A3–A7 | Reaktorkonzept |
| 3 | [Warpantrieb](fakten/konzepte/warpantrieb/warpantrieb.md) | A1, A4, A5 | Antriebskonzept |
| 4 | [ResoTrade V15.6](fakten/konzepte/ResoTrade/resotrade_trading_ki.md) | A1–A7 | +26.3% vs HODL, Live seit April 2026 |
| 5 | [ResoAgent](fakten/konzepte/ResoAgent/ResoAgent.md) | A1–A7 | Resonanzlogische Agenten-KI |

---

## Simulationen

| # | Simulationen | Axiome | Beschreibung |
|---|---------|--------|-------------|
| 1 | [Resonanzfeld](fakten/simulationen/resonanzfeld/simulation_resonanzfeldtheorie.md) | A1–A5 | Zwei Oszillatoren, Kopplungseffizienz, Energierichtung |
| 2 | [Doppelpendel](fakten/simulationen/doppelpendel/begleitkapitel_doppelpendel.md) | A1, A2, A4 | Klassisches Doppelpendel mit dynamischer Kopplungseffizienz ε(θ₂−θ₁) |
| 3 | [Gekoppelte Oszillatoren](fakten/simulationen/gekoppelte_oszillatoren/gekoppelte_oszillatoren.md) | A1–A4 | Energieaustausch, Resonanzerkennung, Live-Animation |
| 4 | [Numerische Demonstration](fakten/simulationen/numerische_demonstration/README.md) | A3, A4, A5 | Konsistenz-Demonstration: Resonanzenergie, Kopplungseffizienz und Entropie über (A, τ) |
| 5 | [FLRW-Simulationen](fakten/simulationen/FLRW-Simulationen/README.md) | A1–A7 | 1.530 Läufe, η ≈ cos², Δd_η > 6σ |
| 6 | [Altcoin-Analyse](fakten/simulationen/altcoin_analyse/resotrade_altcoin_analyse.md) | A3 | 200.000 Episoden, Falsifikationstest |
| 7 | [Schrödinger-Simulation](fakten/simulationen/schrödinger/README.md) | A4 | Ableitung der Schrödinger-Gleichung aus Axiom 4 |

---

## Empirische Nachweise

| # | Nachweis | Axiome | Beschreibung |
|---|---------|--------|-------------|
| 1 | [Resonanzanalyse in Massendaten](fakten/empirisch/cern/dokumentation.md) | A1, A3, A7 | CERN-Daten: Signifikante Resonanzüberschüsse |
| 2 | [Monte-Carlo-Test](fakten/empirisch/monte_carlo/monte_carlo_test/monte_carlo.md) | A1, A3, A7 | 1.500.000 Simulationen, 5 Resonanzen, emp. p = 0 |


---

## Lizenz

Dieses Projekt steht unter der **Schu-Lizenz 1.4**
→ [Zum Lizenztext](lizenz/schu-lizenz_v1.4.md)

---

© Dominic-René Schu — Resonanzfeldtheorie 2025/2026
