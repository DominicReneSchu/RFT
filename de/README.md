# Resonanzfeldtheorie (Version 4.0)

[![Lizenz: RFT-Lizenz 1.4](https://img.shields.io/badge/Lizenz-RFT--Lizenz%201.4-blue.svg)](lizenz/RFT-lizenz_v1.4.md)

Willkommen im offiziellen Repository der **Resonanzfeldtheorie (RFT)**.
Dieses Projekt vereint Mathematik, Physik und Technik zu
einem axiomatischen Modell der Resonanz. Die Theorie beschreibt
fundamentale Prozesse als Kopplungs- und Resonanzphänomene in
Schwingungsfeldern — formal gegründet auf 8 Axiome (A1–A8).

**Empirisch validiert in sechs Domänen:** Teilchenphysik
(1.500.000 Monte-Carlo-Simulationen, 5 Resonanzen, emp. p = 0),
Kosmologie (1.530 FLRW-Simulationen, Δd_η > 6σ),
Nukleartechnologie (Resonanzreaktor, κ = 1, λ_eff/λ₀ = 7.872 für U-235),
Klassische Mechanik (Doppelpendel, ε(θ₂−θ₁) = cos²(Δθ/2)),
Quantenmechanik (Schrödinger-Simulation, Fidelity = 1,0, 1−F ~ λ²) und
Raumzeitphysik (Warpantrieb — erste Warpblase mit positiver Energiedichte).

---

## ☰ Inhaltsverzeichnis

- [Grundformel und zentrale Größen](#grundformel-und-zentrale-größen)
- [Axiomensystem (Kurzfassung)](#axiomensystem-kurzfassung)
- [Empirische Validierung](#empirische-validierung)
- [PDF-Zusammenfassung](#pdf-zusammenfassung)
- [Peer Review](#peer-review)
- [Resonanzfeldtheorie (RFT) – Das Universum als Resonanzblase](#resonanzfeldtheorie-rft--das-universum-als-resonanzblase)
- [Wie Ergebnisse sich gegenseitig bestätigen](#wie-ergebnisse-sich-gegenseitig-bestätigen)
- [Inhalt](#inhalt)
    - [Axiomatik und Definitionen](#axiomatik-und-definitionen)
    - [Mathematik und Physik](#mathematik-und-physik)
    - [Konzepte](#konzepte)
    - [Simulationen](#simulationen)
    - [Empirische Nachweise](#empirische-nachweise)
    - [Erklärungen](#erklärungen)
    - [Analysetools](#analysetools)
    - [Theoretische Grundlagen](#theoretische-grundlagen)
    - [RT-40 Anwendungen: Relativität und Lorentz](#rt-40-anwendungen-relativität-und-lorentz)
    - [RT-42 Kosmologie: Friedmann-Analogie aus Phasendynamik](#rt-42-kosmologie-friedmann-analogie-aus-phasendynamik)
- [Lizenz](#lizenz)
- [Forschungsaufgaben](#forschungsaufgaben)

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

## Warum diese Theorie? — Der Ursprungsgedanke

Die RFT entstand aus einer unscheinbaren Beobachtung:

> **π ist keine irrationale Zahl der Natur — sondern ein Artefakt unserer Basis-10-Darstellung.**

Ein Kreis mit Radius 1 hat einen exakt messbaren, endlichen Umfang. Die Unendlichkeit von 3,14159… ist kein Merkmal des Kreises, sondern der willkürlichen Dezimalkodierung. In einem Zahlensystem mit π als Basis wäre π = 10 — rational und endlich.

Zieht man dieselbe Konsequenz wie bei Planck-Einheiten (c = ℏ = 1), liegt nahe: **π ist die natürliche Einheit zyklischer Vollständigkeit** — das Maß einer Halboszillation im Phasenraum. Damit verliert der Faktor π in

$$E = \pi \cdot \varepsilon(\Delta\varphi) \cdot \hbar \cdot f$$

seinen Status als freies numerisches Postulat. Er wird geometrische Notwendigkeit.

Gleichzeitig behandelt die Standardphysik Energie als Skalar — obwohl Drehmoment (M⃗ = r⃗ × F⃗, Einheit J), Spin (SU(2)-Algebra, Zeeman-Effekt) und der Lorentz-4-Vektor (E/c, p⃗) strukturell auf Vektorialität hinweisen. Die RFT trifft hier eine explizite Entscheidung: **Energie hat Richtung im Resonanzfeld** (Axiom A5).

Diese beiden Beobachtungen — π als Phasenraumkonstante und Energie als Vektor — sind der konzeptuelle Ursprung der gesamten Theorie.

→ [Vollständige Darstellung: π und e als Urkonstanten des Raumes](fakten/theorie/pi_als_urkonstante.md)

---

![Visualisierung der Resonanzfeldtheorie](bilder/visualisierung_RFT.png)

*Abb. 1: Symbolische Darstellung der Wechselwirkung von π, ℏ, ε und f im Resonanzraum*

---

## Axiomensystem (Kurzfassung)

Die RFT besteht aus 8 Kern-Axiomen:

| Axiom | Kernaussage | Formel | Status (Aug 2026) |
|-------|-------------|--------|-------------------|
| A1 | Universelle Schwingung | ψ = A·cos(kx − ωt + φ) | Postulat |
| A2 | Superposition | Φ = Σ ψᵢ | Postulat |
| A3 | Resonanzbedingung | \|f₁/f₂ − m/n\| < δ | **Korollar aus A7** (RT-02, RT-35) |
| A4 | Kopplungsenergie | E = π·ε·ℏ·f | π: **geometrisch abgeleitet** (RT-01, RT-01b); ε=cos²(Δφ/2): **darstellungstheoretisch eindeutig** (RT-02) |
| A5 | Energierichtung | E⃗ = E·ê(Δφ, ∇Φ) | **Irreduzibles Postulat** (RT-36) |
| A6 | Informationsfluss | MI > 0 ⟺ PCI > 0 | Postulat |
| A7 | Invarianz (G_sync) | G_sync ≅ ℝ⁺_× × U(1) × Aff⁺(ℝ) | **Algebraisch bewiesen** (RT-02) |
| A8 | Kopplungswellengeschwindigkeit | c = 1/√(μ₀ε₀) | **Irreduzibles Postulat** (RT-41) |

Zusätzlich gibt es eine interpretative Erweiterung:
- **E1 (Beobachter als Resonator):** Folgt aus A1, A3, A6

Vollständige Formalisierung: [Axiomatische Grundlegung](fakten/docs/definitionen/axiomatische_grundlegung.md)

---

## Empirische Validierung

Die RFT wird an sechs unabhängigen Domänen empirisch validiert:

| Domäne | Methode | Ergebnis | Axiome |
|--------|---------|----------|--------|
| Teilchenphysik | 1.500.000 MC-Sim. auf CMS-Daten | 5 Resonanzen, emp. p = 0 | A3, A7 |
| Kosmologie | 1.530 FLRW-Simulationen | Δd_η > 6σ, Δχ² = +16 vs CMB | A1, A3–A5, A7 |
| Nukleartechnologie | Resonanzreaktor (GDR-basiert) | κ = 1, λ_eff/λ₀ = 7.872 (U-235) | A1, A3, A4 |
| Klassische Mechanik | Doppelpendel + Gekoppelte Oszillatoren | ε(θ₂−θ₁) = cos²(Δθ/2) | A1, A2, A4 |
| Quantenmechanik | Schrödinger-Simulation | Ableitung der Schrödinger-Gl. aus A4; Fidelity = 1,0 (4 Szenarien); 1−F ~ λ² bestätigt | A4 |
| Raumzeitphysik | Warpantriebs-Simulation | Erste Warpblase mit positiver Energiedichte; w-Vorzeichenwechsel via ε(Δφ)-Phasensteuerung | A4, A5 |

**Falsifikationstests:**
- Monte-Carlo-Test: 1.500.000 Simulationen, 5 Resonanzen, emp. p = 0 (A3 bestätigt)
- CERN-Resonanzanalyse: Signifikante Resonanzüberschüsse in Massendaten (A1, A3, A7)
- Resonanzreaktor-Vorhersage: σ_coh > σ_incoh (experimentell prüfbar)
- Schrödinger-Simulation: falsifizierbare Vorhersage |Δ⟨x⟩| ≈ 2,0·λ µm für ⁸⁷Rb-Atome

---

## PDF-Zusammenfassung

Die ausführliche Zusammenfassung der Resonanzfeldtheorie als PDF:
[**RFT_Zusammenfassung.pdf**](./RFT_Zusammenfassung.pdf)

---

## Peer Review

Ein Peer-Review-Verfahren wird aktiv angestrebt:
[**rft_manuskript_de_iop.pdf**](peer_review_rft/manuskript_de/rft_manuskript_de_iop.pdf)

**Einreichungsvorbereitung (RT-39, August 2026):** Alle Einreichungsunterlagen für das Journal of Physics Communications (IOP Publishing) wurden vorbereitet und sind unter [`../en/peer_review_rft/submission/`](../en/peer_review_rft/submission/) verfügbar:
- [Cover Letter](../en/peer_review_rft/submission/cover_letter_jphyscomm.md)
- [Submission Checklist](../en/peer_review_rft/submission/submission_checklist.md)
- [Response-to-Reviewers Vorlage](../en/peer_review_rft/submission/response_to_reviewers_template.md)
- [Journal-Auswahl-Begründung](../en/peer_review_rft/submission/journal_selection.md)
- [Manuskript-Prüfbericht](../en/peer_review_rft/submission/manuscript_review_report.md)

---

## Resonanzfeldtheorie (RFT) – Das Universum als Resonanzblase

> **Hinweis:** Die folgenden Abschnitte entfalten die philosophische, ontologische und theologische Einbettung der RFT. Sie gehen über den axiomatischen Kern hinaus und sind als interpretative Erweiterung zu verstehen.
> 
[Resonanzfeldtheorie (RFT) – Das Universum als Resonanzblase](fakten/docs/erklaerungen/das_universum_als_resonanzblase.md)

---

## Wie Ergebnisse sich gegenseitig bestätigen

Die Resonanzfeldtheorie sagt aus, dass Resonanz das **verbindende Element der Physik** ist.
Diese Verbindung wird sichtbar, weil dieselbe Formel in völlig unabhängigen Bereichen
bestätigt wird — aus verschiedenen Richtungen, auf verschiedenen Skalen.

### ε(Δφ) = cos²(Δφ/2) — eine Formel, drei Skalen

| Bereich | Simulation/Nachweis | Ergebnis | Link |
|---------|---------------------|----------|------|
| Quantenmechanik | Schrödinger-Simulation | Fidelity = 1.000000000000 für alle 4 Δφ-Szenarien | [→](fakten/simulationen/schrödinger/README.md) |
| Kosmologie | FLRW-Simulation (1.530 Läufe) | η = cos²(Δφ/2) exakt, Δd_η > 6σ | [→](fakten/simulationen/FLRW-Simulationen/README.md) |
| Kernphysik | Resonanzreaktor (U-235) | κ = 1 exakt, λ_eff/λ₀ = 7.872 | [→](fakten/konzepte/resonanzreaktor/resonanzreaktor.md) |
| Klassische Mechanik | Doppelpendel, Gekoppelte Oszillatoren | ε(θ₂−θ₁) = cos²(Δθ/2) | [→](fakten/simulationen/doppelpendel/begleitkapitel_doppelpendel.md) |
| Raumzeitgeometrie | Warpantriebs-Simulation | ρ ∝ cos⁴(Δφ/2), E⁻ = 0 | [→](fakten/konzepte/warpantrieb/warpantrieb.md) |

### Resonanzbedingung (A3) — aus drei unabhängigen Richtungen

| Nachweis | Methode | Ergebnis | Link |
|---------|---------|----------|------|
| CERN-Resonanzanalyse | CMS Open Data | Signifikante Resonanzüberschüsse, A7 bestätigt | [→](fakten/empirisch/cern/dokumentation.md) |
| Monte-Carlo-Test | 1.500.000 Simulationen | 5 Resonanzen, emp. p = 0 | [→](fakten/empirisch/monte_carlo/monte_carlo_test/monte_carlo.md) |
| Resonanzreaktor | GDR-basiert | f_γ = f_GDR Bedingung, σ_coh > σ_incoh | [→](fakten/konzepte/resonanzreaktor/resonanzreaktor.md) |

### Querverbindungen im Detail

```
Schrödinger ──ε(Δφ)──→ FLRW ──Klein-Gordon──→ Warpantrieb
     │                    │                          │
  Fidelity=1          η = cos²              ρ ∝ cos⁴, E⁻=0
     │                    │                          │
     └──Störungstheorie──→ Numerische Demo    Kaskade Stufe 3
                          │                          │
                     Konsistenz A3–A5    Resonanzreaktor (Stufe 1)
                                                     │
                     CERN ←─ A3 ─→ Monte-Carlo ──────┘
```

> **Eine Gleichung — E = π·ε(Δφ)·ℏ·f — bestätigt über Quantenmechanik, Kosmologie, Kernphysik und Raumzeitgeometrie.**

---

# Inhalt

## Axiomatik und Definitionen

| # | Dokument | Axiome | Beschreibung |
|---|----------|--------|-------------|
| 1 | [Axiomatische Grundlegung](fakten/docs/definitionen/axiomatische_grundlegung.md) | A1–A8 | Formale Axiome A1–A8 mit Beweisen und empirischen Tests |
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
| 2 | [Resonanzreaktor](fakten/konzepte/resonanzreaktor/README.md) | A1, A3–A7 | Reaktorkonzept — Übersicht und Einleitung |
| 2a | [Resonanzreaktor — Hauptdokument](fakten/konzepte/resonanzreaktor/resonanzreaktor.md) | A1, A3–A7 | Vollständige Beschreibung des Reaktorkonzepts |
| 2b | [Experimentalvorschlag Am-241](fakten/konzepte/resonanzreaktor/experimentalvorschlag_am241.md) | A1, A3, A4 | Falsifizierbarer Experimentalvorschlag: phasenabhängige Photoanregung von Am-241 an der GDR |
| 2c | [Simulationsergebnisse Resonanzreaktor](fakten/konzepte/resonanzreaktor/simulationsergebnisse.md) | A1, A3, A4 | Quantitative Simulationsergebnisse des Resonanzreaktors |
| 2d | [Kosten-Nutzen-Rechnung Resonanzreaktor](fakten/konzepte/resonanzreaktor/kosten_nutzen_rechnung_resonanzreaktor.md) | A1, A3, A4 | Quantitative Bewertung auf Basis der RFT-Simulationsergebnisse |
| 2e | [Resonanz-Impulsantrieb](fakten/konzepte/resonanzreaktor/impulsantrieb.md) | A1, A4, A5 | Gerichtete Spaltung als Raumfahrtantrieb |
| 3 | [Warpantrieb — Übersicht](fakten/konzepte/warpantrieb/README.md) | A1, A4, A5 | Einführung und Überblick zum Warpantriebs-Konzept |
| 3a | [Warpantrieb — Hauptdokument](fakten/konzepte/warpantrieb/warpantrieb.md) | A1, A4, A5 | Antriebskonzept — **erste Warpblasensimulation mit positiver Energiedichte** (E⁻ = 0); w-Vorzeichenwechsel; RT-33: Skalierungsgesetz ρ∝R⁻², R*>>1 AU ([Analyse](fakten/konzepte/warpantrieb/analyse/rt33_energieluecke.py)) |

---

## Simulationen

| # | Simulationen | Axiome | Beschreibung |
|---|---------|--------|-------------|
| 1 | [Resonanzfeld](fakten/simulationen/resonanzfeld/simulation_resonanzfeldtheorie.md) | A1–A5 | Zwei Oszillatoren, Kopplungseffizienz, Energierichtung |
| 2 | [Doppelpendel](fakten/simulationen/doppelpendel/begleitkapitel_doppelpendel.md) | A1, A2, A4 | Klassisches Doppelpendel mit dynamischer Kopplungseffizienz ε(θ₂−θ₁) — RT-08: χ²-Fit 🔬 ([Analyse](fakten/simulationen/doppelpendel/analyse/rt08_doppelpendel_vergleich.py)) — RT-38: [Experimentprotokoll](fakten/simulationen/doppelpendel/experiment/protokoll_rt38.md) 🧪 |
| 3 | [Gekoppelte Oszillatoren](fakten/simulationen/gekoppelte_oszillatoren/gekoppelte_oszillatoren.md) | A1–A4 | Energieaustausch, Resonanzerkennung, Live-Animation |
| 4 | [Numerische Demonstration](fakten/simulationen/numerische_demonstration/README.md) | A3, A4, A5 | Konsistenz-Demonstration: Resonanzenergie, Kopplungseffizienz und Entropie über (A, τ) |
| 4a | [Numerische Demonstration — Begleitkapitel](fakten/simulationen/numerische_demonstration/begleitkapitel_numerische_demonstration.md) | A3, A4, A5 | Ausführliches Begleitkapitel zur numerischen Demonstration |
| 4b | [Numerische Demonstration — Dokumentation](fakten/simulationen/numerische_demonstration/docs/index.md) | A3, A4, A5 | Technische Dokumentation und Index |
| 5 | [FLRW-Simulationen](fakten/simulationen/FLRW-Simulationen/README.md) | A1–A7 | 1.530 Läufe, η ≈ cos², Δd_η > 6σ |
| 6 | [Schrödinger-Simulation](fakten/simulationen/schrödinger/README.md) | A4 | Ableitung der Schrödinger-Gl. aus Axiom 4; Fidelity = 1,0 (alle 4 Szenarien); Störungstheorie 1−F ~ λ² bestätigt; falsifizierbare Vorhersage für ⁸⁷Rb |
| 6a | [Schrödinger — Experimentalvorschlag](fakten/simulationen/schrödinger/docs/experimental_proposal.md) | A4 | Falsifizierbarer Experimentalvorschlag für ⁸⁷Rb-BEC in harmonischer Falle |
| 6b | [Schrödinger — Forschungsprogramm (Roadmap)](fakten/simulationen/schrödinger/docs/schrodinger_roadmap.md) | A4 | Schrödinger-Startstrecke: Forschungsprogramm und Minimalnachweis |
| 7 | [Hamilton-Simulationen](fakten/simulationen/hamilton/README.md) | A1, A3, A4 | RT-31: Resonanz-Hamiltonoperator — Phonon-Kopplung und Spin-Bahn-Kopplung |

---

## Empirische Nachweise

| # | Nachweis | Axiome | Beschreibung |
|---|---------|--------|-------------|
| 1 | [Resonanzanalyse in Massendaten](fakten/empirisch/cern/dokumentation.md) | A1, A3, A7 | CERN-Daten: Signifikante Resonanzüberschüsse |
| 2 | [Monte-Carlo-Test](fakten/empirisch/monte_carlo/monte_carlo_test/monte_carlo.md) | A1, A3, A7 | 1.500.000 Simulationen, 5 Resonanzen, emp. p = 0 |
| 2a | [Monte-Carlo — Publikationsbericht](fakten/empirisch/monte_carlo/monte_carlo_test/publication_results/main_report/resonanz_report.md) | A1, A3, A7 | Vollständiger Publikationsbericht der Monte-Carlo-Analyse |
| 2b | [Monte-Carlo — Analysebericht](fakten/empirisch/monte_carlo/monte_carlo_test/report_out/resonanz_report.md) | A1, A3, A7 | Automatisch generierter Analysebericht der Monte-Carlo-Simulation |


---

## Erklärungen

| # | Erklärung | Axiome | Beschreibung |
|---|-----------|--------|-------------|
| 1 | [Schwarmresonanz](fakten/docs/erklaerungen/schwarmresonanz.md) | A1–A7 | Warum Vogelschwärme nicht kollidieren — und warum die RFT neue Türen öffnet |
| 2 | [Resonanz in der Physik](fakten/docs/erklaerungen/resonanz_in_der_physik.md) | A1–A7 | Wie ein Muster Mechanik, Thermodynamik, Elektrodynamik, QM und Relativität verbindet |
| 3 | [RFT – Konsistenzbegründung: Universum als Resonanzblase](fakten/docs/erklaerungen/rft_konsistenzpruefung_resonanzblase.md) | A1–A7 | Formale Begleitstudie: Konsistenzprüfung der Kernaussagen aus „Das Universum als Resonanzblase" |

---

## Analysetools

| # | Dokument | Axiome | Beschreibung |
|---|----------|--------|-------------|
| 1 | [Gesellschaftliche Analyse](fakten/docs/analysetools/gesellschaftliche_analyse.md) | A1–A7 | RFT-Analyseinstrument für gesellschaftliche Zusammenhänge – KI-Kontext-Prompt zur Mustererkennung in Nachrichtenmeldungen; Fassung 2.10: Nutzungsanleitung um Projektion und Retrodiktion erweitert; §1.11a Retrodiktion als formale Methode; Zeitmodi-Abschnitt in Präambel ergänzt |

---

## Theoretische Grundlagen

| # | Dokument | Axiome | Beschreibung |
|---|----------|--------|-------------|
| 1 | [π und e als Urkonstanten des Raumes](fakten/theorie/pi_als_urkonstante.md) | A4, A5 | Ursprungsgedanke der RFT: π als geometrische Phasenraumkonstante, Vektorialität der Energie — **✅ RT-01a abgeschlossen (Aug 2026)** |
| 2 | [Wirkungsintegral-Herleitung von π](fakten/theorie/wirkungsintegral_pi_herleitung.md) | A4 | Formale Herleitung von π als Sattelpunktsbeitrag der stationären Phase im Pfadintegral (RT-01, Aug 2026) |
| 3 | [G_sync — Gruppenstruktur und Invarianzbeweise](fakten/theorie/gsync_gruppenstruktur.md) | A7 | Gruppentheoretischer Beweis: G_sync ≅ ℝ⁺_× × U(1) × Aff⁺(ℝ); Eindeutigkeit von cos²(Δφ/2); RT-02, Aug 2026 |
| 4 | [A5-Herleitung: ê(Δφ, ∇Φ) aus G_sync](fakten/theorie/a5_vektorialitaet_herleitung.md) | A5 | RT-36: ê ist irreduzibles Postulat — D-Erzeuger erzwingt ∂_t Φ, nicht ∇Φ; formale Begründungsgrundlage RT-01a; Aug 2026 |
| 5 | [κ-Parameter in der RFT (RT-11)](fakten/theorie/kappa_parameter_rft.md) | A4 | Konventionsdeklaration zum κ-Parameter; κ = 1 als zwingende Konsequenz der ε = η Identität (Aug 2026) |
| 6 | [RT-41 — Axiom A8: Kopplungswellengeschwindigkeit](fakten/theorie/rt41_axiom_a8_kopplungswelle.md) | A1–A7 | Herleitung oder irreduzibles Postulat der Kopplungswellengeschwindigkeit (Sep 2026) |
| 7 | [RT-01b — Numerisches Pfadintegral: π-Herleitung](fakten/theorie/simulationen/rt01b/README.md) | A4 | Numerische Verifikation der π-Herleitung über Pfadintegral-Simulation |
| 8 | [Peer-Review-Bereitschaft](../PEER_REVIEW_READINESS.md) | — | Status aller offenen Formalisierungsschritte und theoretischen Grundlagen nach Peer-Review-Kriterien |

---

## RT-40 Anwendungen: Relativität und Lorentz

Formale Anwendungen der RFT auf relativistische Physik (RT-40, Sep 2026):

| # | Dokument | Axiome | Beschreibung |
|---|----------|--------|-------------|
| 1 | [AP1 — Phase ↔ Rapidität](fakten/theorie/rt40_ap1_phase_rapiditaet.md) | A1, A4, A5 | Formale Identifikation: resonanzfeldtheoretische Phase und relativistische Rapidität |
| 2 | [AP2 — Kopplungseffizienz im Lorentz-Rahmen](fakten/theorie/rt40_ap2_kopplungseffizienz_lorentz.md) | A1, A4 | Verhalten von ε(Δφ) unter Lorentz-Transformation |
| 3 | [AP3 — Lorentz-Transformation aus der RFT](fakten/theorie/rt40_ap3_lorentz_transformation.md) | A1, A4, A7 | Herleitung der Lorentz-Transformation aus dem RFT-Formalismus |
| 4 | [AP4 — Lichtgeschwindigkeit als Grenzfall](fakten/theorie/rt40_ap4_lichtgeschwindigkeit_grenzfall.md) | A1, A4 | c als emergenter Grenzfall der Resonanzfeldtheorie |
| 5 | [AP5 — Zeitdilatation und Längenkontraktion](fakten/theorie/rt40_ap5_zeitdilatation_laengenkontraktion.md) | A1, A4, A5 | Zeitdilatation und Längenkontraktion im RFT-Rahmen |
| 6 | [AP6 — Falsifizierbarkeit und SRT-Abgrenzung](fakten/theorie/rt40_ap6_falsifizierbarkeit_srt_abgrenzung.md) | A1–A7 | Falsifizierbare Vorhersagen und Abgrenzung zur Speziellen Relativitätstheorie |
| 7 | [AP7 — Warpantrieb: Konsistenzprüfung](fakten/theorie/rt40_ap7_warpantrieb_konsistenzpruefung.md) | A1, A4, A5 | Formale Konsistenzprüfung des Warpantriebs-Konzepts im Lorentz-Rahmen |

---

## RT-42 Kosmologie: Friedmann-Analogie aus Phasendynamik

Formale Anwendungen der RFT auf Kosmologie (RT-42, Sep 2026):

| # | Dokument | Axiome | Beschreibung |
|---|----------|--------|-------------|
| 1 | [AP1 — Phase ↔ Skalenfaktor](fakten/theorie/rt42_ap1_phase_skalenfaktor.md) | A1, A4, A8 | Formale Analogie: RFT-Phasendifferenz als dynamische Variable des kosmischen Skalenfaktors — **✅ RT-42 AP1 abgeschlossen (Sep 2026)** |
| 2 | [AP2 — Zeitableitung der Phase](fakten/theorie/rt42_ap2_zeitableitung_phase.md) | A4, A5, A8 | Geschlossene ODE Δφ̇ = β·tan(Δφ/2) aus der Kopplungsdynamik; Hubble-Parameter H(t) = H₀√ε(t) analytisch hergeleitet — **✅ RT-42 AP2 abgeschlossen (Sep 2026)** |
| 3 | [AP3 — Verbindung zu Λ oder Dunkler Energie](fakten/theorie/rt42_ap3_verbindung_lambda_dunkle_energie.md) | A1, A4, A5, A8 | RFT erklärt Λ als effektiven Grenzfall eines statischen Superhorizontalgradienten; w_eff ∈ [−1, +1/3]; ΛCDM als Spezialfall (β → 0, k₀ = const) — **✅ RT-42 AP3 abgeschlossen (Sep 2026)** |
| 4 | [AP4 — Skalierungsproblem kosmologisch einordnen](fakten/theorie/rt42_ap4_skalierungsproblem_kosmologie.md) | A1, A4, A5, A8 | 28-Größenordnungen-Diskrepanz (ρ_warp ~ 10¹⁹ J/m³ vs. ρ_Λ ~ 10⁻⁹ J/m³) als Scheinproblem ausgewiesen: k_warp ~ 10⁻² m⁻¹ (lokal) ≠ k₀ ~ 10⁻²⁶ m⁻¹ (kosmologisch); verschiedene Regime, verschiedene Energieformeln — **✅ RT-42 AP4 abgeschlossen (Sep 2026)** |
| 5 | [AP5 — Falsifizierbare Abweichungen vom ΛCDM](fakten/theorie/rt42_ap5_falsifizierbare_abweichungen_lcdm.md) | A1, A4, A5, A8 | Vier messbare Abweichungen vom ΛCDM benannt: dynamisches w(z) = w₀ + w_a·z/(1+z) mit w_a ≈ β/H₀; modifiziertes H(z) (≤ 3 %); verlangsamtes Strukturwachstum Δ(fσ₈) ≤ 1 %; reduziertes ISW-Signal bei ℓ < 20. Primäres Falsifikationskriterium: w_a = 0 (5σ) erzwingt β = 0 (ΛCDM-Grenzfall). DESI-DR5 und Euclid entscheidend — **✅ RT-42 AP5 abgeschlossen (Sep 2026)** |

---

## Lizenz

Dieses Projekt steht unter der **RFT-Lizenz 1.4**
→ [Zum Lizenztext](lizenz/RFT-lizenz_v1.4.md)
→ [Änderungsprotokoll (Changelog)](lizenz/CHANGELOG.md)

---

## Forschungsaufgaben

→ [Forschungsaufgaben und offene Punkte](../RESEARCH_TASKS.md)

---

© Dominic-René Schu — Resonanzfeldtheorie 2025/2026
