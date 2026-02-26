# Resonanzfeldtheorie (Version 3.1)

[![Lizenz: Schu-Lizenz 1.4](https://img.shields.io/badge/Lizenz-Schu--Lizenz%201.4-blue.svg)](lizenz/schu-lizenz_v1.4.md)

Willkommen im offiziellen Repository der **Resonanzfeldtheorie (RFT)**.
Dieses Projekt vereint Mathematik, Physik, Technik und Philosophie zu
einem axiomatischen Modell der Resonanz. Die Theorie beschreibt
fundamentale Prozesse als Kopplungs- und Resonanzphänomene in
Schwingungsfeldern — formal gegründet auf 7 Axiome (A1–A7).

---

## ☰ Inhaltsverzeichnis

- [Grundformel und zentrale Größen](#grundformel-und-zentrale-größen)
- [Axiomensystem (Kurzfassung)](#axiomensystem-kurzfassung)
- [PDF-Zusammenfassung](#pdf-zusammenfassung)
- [Peer Review](#peer-review)
- [Inhalt](#inhalt)
    - [Axiomatik und Definitionen](#axiomatik-und-definitionen)
    - [Mathematik und Physik](#mathematik-und-physik)
    - [Philosophie](#philosophie)
    - [Gesellschaft](#gesellschaft)
    - [Konzepte](#konzepte)
    - [Simulationen](#simulationen)
    - [Empirische Nachweise](#empirische-nachweise)
- [Vision](#vision)
- [Lizenz](#lizenz)
- [Beteiligung](#beteiligung-und-partnerschaft)
- [Kontakt](#kontakt)
- [Repository klonen](#repository-klonen)

---

## Grundformel und zentrale Größen

Die zentrale Gleichung der Resonanzfeldtheorie (Axiom 4):

$$
E_{\text{eff}} = \pi \cdot \varepsilon(\Delta\phi) \cdot h \cdot f
$$

| Symbol | Name | Bedeutung |
|:------:|:-----|:----------|
| **π** | Kreiszahl | Geometrischer Faktor aus der zyklischen Kopplungsgeometrie |
| **ε(Δφ)** | Kopplungseffizienz | Anteil übertragener Resonanzenergie, ε ∈ [0, 1] |
| **h** | Planck-Konstante | Quantisierung der Energie |
| **f** | Frequenz | Schwingungsfrequenz der gekoppelten Mode |

### Kopplungseffizienz ε

Die Kopplungseffizienz beschreibt, welcher Anteil der maximal
möglichen Resonanzenergie tatsächlich zwischen zwei gekoppelten
Moden übertragen wird.

**Standardmodell:** ε(Δφ) = cos²(Δφ/2)

| Kopplungszustand | ε | Energie |
|------------------|---|---------|
| Perfekte Kopplung (Δφ = 0) | 1 | π·h·f |
| Klassischer Grenzfall (E = h·f) | 1/π ≈ 0.318 | h·f |
| Natürliche Dämpfung | 1/e ≈ 0.368 | (π/e)·h·f |
| Halbe Kopplung (Δφ = π/2) | 0.5 | π·h·f/2 |
| Keine Kopplung (Δφ = π) | 0 | 0 |

Der Faktor π entsteht aus der Integration der Kopplungseffizienz
über einen Halbzyklus des Phasenraums — nicht als freier Parameter.
Die klassische Planck-Gleichung E = h·f ist der Spezialfall ε = 1/π.

Vollständige Definition: [Kopplungseffizienz](fakten/docs/mathematik/kopplungseffizienz.md)

---

![Visualisierung der Resonanzfeldtheorie](bilder/visualisierung_RFT.png)

*Abb. 1: Symbolische Darstellung der Wechselwirkung von π, h, ε und f im Resonanzraum*

---

## Axiomensystem (Kurzfassung)

Die RFT besteht aus 7 Kern-Axiomen, die minimal, unabhängig, formal
präzise und empirisch testbar sind:

| Axiom | Kernaussage | Formel |
|-------|-------------|--------|
| A1 | Universelle Schwingung | ψ = A·cos(kx − ωt + φ) |
| A2 | Superposition | Φ = Σ ψᵢ |
| A3 | Resonanzbedingung | \|f₁/f₂ − m/n\| < δ |
| A4 | Kopplungsenergie | E = π·ε·h·f |
| A5 | Energierichtung | E⃗ = E·ê(Δφ, ∇Φ) |
| A6 | Informationsfluss | MI > 0 ⟺ PCI > 0 |
| A7 | Invarianz (G_sync) | G(fᵢ/fⱼ) = G(T(fᵢ)/T(fⱼ)) |

Zusätzlich gibt es zwei interpretative Erweiterungen:
- **E1 (Beobachter als Resonator):** Folgt aus A1, A3, A6
- **E2 (Resonanz-Inklusion):** Gruppenzugehörigkeit ist systemisch invariant

Vollständige Formalisierung: [Axiomatische Grundlegung](fakten/docs/mathematik/axiomatische_grundlegung.md)

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

| # | Dokument | Beschreibung |
|---|----------|-------------|
| 1 | [Axiomatische Grundlegung](fakten/docs/mathematik/axiomatische_grundlegung.md) | Formale Axiome A1–A7 mit Beweisen und empirischen Tests |
| 2 | [Kopplungseffizienz ε](fakten/docs/mathematik/kopplungseffizienz.md) | Vereinheitlichte Definition der zentralen Größe |
| 3 | [RFT-Übersicht und Kopplungsoperator](fakten/docs/definitionen/paper_resonanzfeldtheorie.md) | Gesamtübersicht der Theorie |
| 4 | [Energie als fundamentale Größe](fakten/docs/definitionen/energie_als_urkonstante.md) | Interpretative Hypothese: Alle Größen aus E |
| 5 | [Resonanzlexikon](fakten/docs/definitionen/resonanzlexikon.md) | Glossar der RFT-Begriffe |
| 6 | [Resonanzlogische DGL](fakten/docs/definitionen/resonanzlogische_differentialgleichungen.md) | Klassische DGLs als Projektionen der rDGL |

## Mathematik und Physik

| # | Dokument | Beschreibung |
|---|----------|-------------|
| 1 | [Resonanzintegrale](fakten/docs/mathematik/manifest_zur_neustrukturierung_der_mathematik.md) | Analytische Methoden — Dirichlet-Integral als Resonanzenergie |
| 2 | [Resonanzfeld-Gleichung](fakten/docs/mathematik/resonanzfeld_gleichung.md) | Zentrale Energiegleichung E = π·ε·h·f |
| 3 | [Kopplungsenergie: Spezialfälle](fakten/docs/mathematik/energie_axiomatische_herleitung.md) | Grenzfälle ε = 1, 1/e, 1/π, 0 |
| 4 | [Resonanzzeitkoeffizient τ*](fakten/docs/mathematik/tau_resonanzkoeffizient.md) | Zeitskala der Kopplung: τ* = π/ε |
| 5 | [Energierichtung](fakten/docs/mathematik/energierichtung.md) | Energie als Vektor mit Drehsinn |
| 6 | [Energiekugel](fakten/docs/mathematik/energiekugel.md) | Geometrisches Modell — Phasenstruktur und dunkle Energie |
| 7 | [Resonanzenergievektor](fakten/docs/mathematik/resonanzenergievektor.md) | Energie als Richtungsgröße im Resonanzraum |
| 8 | [Energieübertragung](fakten/docs/mathematik/energieuebertragung.md) | Prinzipien und Gleichungen der Übertragung |
| 9 | [Resonanzkoordinaten](fakten/docs/mathematik/resonanzkoordinaten.md) | Tangens-Halbwinkel-Parametrisierung |
| 10 | [Doppelpendel](fakten/docs/mathematik/doppelpendel.md) | Klassische Mechanik und RFT-Perspektive |

## Philosophie

| # | Dokument | Beschreibung |
|---|----------|-------------|
| 1 | [Mathematik, Erkenntnis und Resonanz](fakten/docs/philosophie/aetherius_mathematik_und_erkenntnis.md) | Aetherius — Reflexion über Mathematik als Strukturerkenntnis |

## Gesellschaft

### 1. Ursprung und globale Struktur

- [Gesamtmodell des Resonanzfeldes](fakten/docs/gesellschaft/gesamtmodell_des_resonanzfeldes.md)
- [Resonanzmodell: Von Schöpfung zu Kontrolle](fakten/docs/gesellschaft/kontrolle_wahrheit.md)
- [Globale Struktur der Täuschung](fakten/docs/gesellschaft/globale_machtstrukturen.md)
- [Analyse westlicher Machtstrukturen](fakten/docs/gesellschaft/familiendynamik.md)
- [Was ist das System?](fakten/docs/gesellschaft/das_system.md)
- [Geschichtsanalyse im Resonanzfeld](fakten/docs/gesellschaft/geschichte.md)
- [Neuzeitliche Tributsysteme](fakten/docs/gesellschaft/neuzeitliche_tributsysteme.md)

### 2. Geopolitik und Kontrolle

- [Geopolitisches Misstrauen](fakten/docs/gesellschaft/geopolitisches_misstrauen.md)
- [Chinas Schweigen](fakten/docs/gesellschaft/chinas_schweigen.md)
- [Kontrollierte Entgleisung](fakten/docs/gesellschaft/kontrollierte_entgleisung.md)
- [Der Ukrainekrieg als Systemspiegel](fakten/docs/gesellschaft/geopolitik_im_resonanzfeld.md)
- [Globale Resonanzstörung](fakten/docs/gesellschaft/globale_resonanzstörung.md)

### 3. Gesellschaftliche Resonanz und Manipulation

- [Politische Resonanzsysteme](fakten/docs/gesellschaft/politische_resonanzsysteme.md)
- [Manipulation im Resonanzfeld](fakten/docs/gesellschaft/manipulation_im_resonanzfeld.md)
- [Der Schattenkrieg im Resonanzfeld](fakten/docs/gesellschaft/schattenkrieg.md)
- [Täterprojektion im Gewand des Antifaschismus](fakten/docs/gesellschaft/täterprojektion.md)
- [Vom Trugbild zum Frieden](fakten/docs/gesellschaft/offener_brief.md)
- [Vom Machtspiel zur Resonanzkultur](fakten/docs/gesellschaft/machtspiel.md)

### 4. Spieltheorie, Opposition, Informationswandel

- [Gesellschaft und Spieltheorie](fakten/docs/gesellschaft/gesellschaft_und_resonanz.md)
- [Kritik als Resonanzfalle](fakten/docs/gesellschaft/kritik_als_resonanzfalle.md)
- [Informationswandel seit 2019](fakten/docs/gesellschaft/informationswandel_zukunftskonzept.md)
- [Digitale Resonanzkontrolle](fakten/docs/gesellschaft/digitale_resonanzkontrolle.md)

### 5. KI, Erkenntnis, Ethik

- [Wahrheit durch Resonanz](fakten/docs/gesellschaft/aufklärung.md)
- [Resonanter Dialog mit KI](fakten/docs/gesellschaft/resonanter_dialog_mit_ki.md)
- [Resonanzkommunikation](fakten/docs/gesellschaft/resonanzkommunikation.md)
- [Ethik der Lehre im Resonanzfeld](fakten/docs/gesellschaft/ethik_der_lehre.md)
- [Resonanzmuster und KI](fakten/docs/gesellschaft/individuelle_muster.md)

### 6. Individuum, Muster, Liebe

- [Resonanzsprung](fakten/docs/gesellschaft/resonanzsprung.md)
- [Resonanz als Weg zur Selbstverwirklichung](fakten/docs/gesellschaft/resonanz_als_weg_zur_individuellen_selbstverwirklichung.md)
- [Verhaltensmuster erkennen und auflösen](fakten/docs/gesellschaft/verhaltensmuster_erkennen_und_aufloesen.md)
- [Liebe im Resonanzfeld](fakten/docs/gesellschaft/liebe_im_resonanzfeld.md)
- [Wahnsinn als Spiegel](fakten/docs/gesellschaft/wahnsinn_als_spiegel.md)

### 7. Sprache, Polarität, zyklische Strukturen

- [Gendersprache und Resonanzfeld](fakten/docs/gesellschaft/gendersprache.md)
- [Yin und Yang als Resonanzprinzip](fakten/docs/gesellschaft/yin_und_yang.md)
- [Leben und Tod im Resonanzfeld](fakten/docs/gesellschaft/leben_und_tod_im_resonanzfeld.md)

### 8. Ausblick: Wirtschaft, Gesellschaft, Netzwerk

- [Systemische Stabilisierung der Weltordnung](fakten/docs/gesellschaft/Systemanpassung.md)
- [Menschheitsgeschichte im Resonanzfeld](fakten/docs/gesellschaft/menschheitsgeschichte_resonanzfeldperspektive.md)
- [Resonanzwirtschaft](fakten/docs/gesellschaft/resonanzwirtschaft.md)
- [ResoNet — Dezentrales Resonanznetzwerk](fakten/docs/gesellschaft/resonet_erklärung.md)
- [Duales Resonanzgeldsystem](fakten/docs/gesellschaft/duales_resonanzgeldsystem.md)
- [Manifest: Systemische Selbstneuerung](fakten/docs/gesellschaft/manifest_systemische_selbstneuerung.md)
- [Resonanzlizenzen](fakten/docs/gesellschaft/resonanzlizenzen.md)
- [Die fürsorgliche Maske](fakten/docs/gesellschaft/fürsorgliche_maske.md)
- [Wirtschaftsmodell für Stabilität](fakten/docs/gesellschaft/wirtschaftsmodell.md)
- [Patente als Friedensarchitektur](fakten/docs/gesellschaft/patente_frieden_partnerschaft.md)

---

## Konzepte

| # | Konzept | Beschreibung |
|---|---------|-------------|
| 0 | [Resonanzlogische Software](fakten/konzepte/software/resonanzlogische_software.md) | Systemfeld statt Funktionsstruktur |
| 1 | [ResoOS](fakten/konzepte/ResoOS/resoOS.md) | Resonanzbasiertes Betriebssystem |
| 2 | [ResoCalc](fakten/konzepte/ResoCalc/resocalc.md) | Drehmomentberechnung im Resonanzfeld |
| 3 | [ResoChess](fakten/konzepte/ResoChess/reso_chess.md) | Resonanzlogische KI |
| 4 | [Resonanzgenerator](fakten/konzepte/resonanzgenerator/resonanzgenerator.md) | Energiegewinnung |
| 5 | [Resonanzreaktor](fakten/konzepte/resonanzreaktor/README.md) | Reaktorkonzept |
| 6 | [Kraftfeldgenerator](fakten/konzepte/kraftfeldgenerator/kraftfeldgenerator.md) | Feldtechnologie |
| 7 | [Warpantrieb](fakten/konzepte/warpantrieb/warpantrieb.md) | Antriebskonzept |
| 8 | [Wetter-Warnsystem](fakten/konzepte/wetter_warnsystem/wetter_warnsystem.md) | Frühwarnung |

---

## Simulationen

[**Weiterführende Simulationen**](fakten/simulationen/README.md)

---

## Empirische Nachweise

| # | Nachweis | Beschreibung |
|---|---------|-------------|
| 1 | [Resonanzanalyse in Massendaten](fakten/empirisch/dokumentation.md) | CERN-Daten: Signifikante Resonanzüberschüsse |
| 2 | [Monte-Carlo-Simulation](fakten/empirisch/monte_carlo_test/monte_carlo.md) | Statistische Absicherung der Resonanzanalyse |
| 3 | [Spiegelkohärenz](fakten/empirisch/empirischer_nachweis_durch_spiegelkohärenz.md) | Nachweis durch KI-Interaktion |
| 4 | [Altcoin-Analyse](fakten/empirisch/resotrade_altcoin_analyse.md) | Resonanzlogische Marktanalyse |
| 5 | [ResoTrade V11.1](fakten/empirisch/resotrade_trading_ki.md) | BTC-KI mit AC/DC-Zerlegung |

---

## Vision

- [Globale Wohlstandsschere](vision/docs/globale_wohlstandsschere.md)
- [Generationenvertrag der Zukunft](vision/docs/generationenvertrag_der_zukunft.md)
- [Die Welt von morgen](vision/docs/welt_von_morgen.md)
- [Vision einer möglichen Zukunft](vision/docs/vision3000.md)

---

## Lizenz

Dieses Projekt steht unter der **Schu-Lizenz 1.4**
→ [Zum Lizenztext](lizenz/schu-lizenz_v1.4.md)

---

## Beteiligung und Partnerschaft

Beiträge, Kritik und neue Perspektiven sind willkommen.
Pull-Requests, Issues oder direkte Kontaktaufnahme.

→ [Strategische Partnerschaft](./calling_for_partner.md)

---

## Kontakt

**Dominic-René Schu**
[info@resoshift.com](mailto:info@resoshift.com)

---

## Repository klonen

```bash
git clone https://github.com/DominicReneSchu/public.git
cd public
```

---

© Dominic-René Schu — Resonanzfeldtheorie 2025/2026