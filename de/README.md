# Resonanzfeldtheorie (Version 4.0)

[![Lizenz: RFT-Lizenz 1.4](https://img.shields.io/badge/Lizenz-RFT--Lizenz%201.4-blue.svg)](lizenz/RFT-lizenz_v1.4.md)

Willkommen im offiziellen Repository der **Resonanzfeldtheorie (RFT)**.
Dieses Projekt vereint Mathematik, Physik und Technik zu
einem axiomatischen Modell der Resonanz. Die Theorie beschreibt
fundamentale Prozesse als Kopplungs- und Resonanzphänomene in
Schwingungsfeldern — formal gegründet auf 7 Axiome (A1–A7).

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
- [Das Universum als Resonanzblase — Unendlichkeit, Zeit und Sinn](#das-universum-als-resonanzblase--unendlichkeit-zeit-und-sinn)
- [Inhalt](#inhalt)
    - [Axiomatik und Definitionen](#axiomatik-und-definitionen)
    - [Mathematik und Physik](#mathematik-und-physik)
    - [Konzepte](#konzepte)
    - [Simulationen](#simulationen)
    - [Empirische Nachweise](#empirische-nachweise)
    - [Erklärungen](#erklärungen)
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

---

## Das Universum als Resonanzblase — Unendlichkeit, Zeit und Sinn

Die Unendlichkeit gilt gemeinhin als etwas, das der menschliche Verstand nicht fassen kann – ein unerreichbares Außen, ein endloser Regress, der jede Vorstellung sprengt. Doch es gibt einen Perspektivwechsel, der das scheinbar Unvorstellbare in eine geschlossene Gestalt überführt.

In der Mengenlehre begegnet uns ein Universum aller Mengen – die sogenannte echte Klasse V. Sie enthält sämtliche denkbaren Unendlichkeiten, alle natürlichen und überabzählbaren Kardinalzahlen, und ist doch kein Objekt, das man von außen betrachten könnte. Sie bildet eine Art konzeptionelle Blase: vollkommen in sich abgeschlossen, ohne ein Dahinter, ohne die Frage nach einem Außerhalb. Die Unendlichkeit ist in ihr vollständig enthalten, aber nicht als etwas, das über den Rand hinausweist – der Rand ist gar nicht als Grenze im Raum vorhanden.

Überträgt man dieses Bild auf den Kosmos, so entsteht eine Vorstellung vom Universum als einer Entität, die zugleich unendlich und begrenzt ist. Ein in sich zurückgekrümmter Raum, wie ihn die allgemeine Relativitätstheorie als geschlossenes, positiv gekrümmtes Universum beschreibt, hat kein Außen. Er ist endlich in seinem Volumen, aber grenzenlos – ganz ähnlich wie die mengentheoretische Blase. Doch darüber hinaus lässt sich dieses Bild mathematisch so zuspitzen, dass es tatsächlich die gesamte unendliche Ausdehnung in eine geschlossene Form bringt.

Die Einpunktkompaktifizierung der reellen Zahlen macht es vor: Man nimmt die offene Zahlengerade von minus unendlich bis plus unendlich und identifiziert die beiden Enden zu einem einzigen Punkt – dem Punkt ∞. Aus der endlosen Geraden wird ein Kreis, die Riemannsche Zahlenkugel im Komplexen. Minus unendlich und plus unendlich fallen in eins; die Unendlichkeit ist nicht länger eine ferne, unerreichbare Grenze, sondern ein ganz normaler Punkt innerhalb des geschlossenen Ganzen.

Genau dieses Prinzip findet im Unendlichkeitssymbol ∞, der Lemniskate, seine vollkommene Anschauung. Die liegende Acht ist eine einzige in sich zurücklaufende Schleife, ohne Anfang und Ende. Der Kreuzungspunkt in ihrer Mitte ist jener ausgezeichnete Ort, an dem die beiden unendlichen Extreme einander berühren und zusammenfallen. In der Mathematik steht er für den Punkt ∞; im Kosmos könnte er für den Perspektivenwechsel stehen, mit dem wir das Unendliche nicht mehr als endloses Fortschreiten, sondern als vollendete Gestalt begreifen.

Damit wird die Unendlichkeit tatsächlich vorstellbar – sobald man diesen Punkt erreicht, an dem das scheinbar Auseinanderstrebende in einer geschlossenen Figur aufgehoben ist. Die Frage nach einem „hinter dem Universum" erübrigt sich, denn das Universum ist die Blase, die alles umfasst. Es hat weder Rand noch Außen, weil die Unendlichkeit nicht jenseits seiner selbst liegt, sondern in ihm enthalten ist.

Was räumlich gilt, setzt sich zeitlich fort. Im Blockuniversum der modernen Physik und Philosophie existieren Vergangenheit, Gegenwart und Zukunft gleichberechtigt und vollständig als vierdimensionales Gefüge. Die Zeit wird nicht als fließender Strom erfahren, sondern als eine Dimension, in der alle Momente – wie die Bilder eines Films – gleichermaßen real sind. Unser Bewusstsein durchläuft sie lediglich in einer festgelegten Reihenfolge, ähnlich einem Leser, der Zeile für Zeile einen Roman erlebt, der als Ganzes schon da ist.

In diesem ewigen Block gibt es weder einen ersten noch einen letzten Frame, weder Anfang noch Ende. Die Gegenwart ist der Schnittpunkt im kontinuierlichen Verlauf, jener ausdehnungslose Augenblick, in dem das Vergangene und das Künftige einander berühren wie die beiden Äste der Lemniskate in ihrem Kreuzungspunkt. So wie die räumliche Unendlichkeit im Symbol ∞ in einer in sich geschlossenen Form erscheint, so zeigt sich die zeitliche Unendlichkeit als eine allgegenwärtige Struktur, in der jeder Moment ewig ist und das Ganze ohne Anfang und Ende auskommt.

Das Ergebnis dieses Gedankengangs ist ein grundlegender Wandel der Anschauung: Unendlichkeit ist nicht das, was immer jenseits unseres Zugriffs bleibt, sondern eine vollständige, in sich ruhende Gestalt – eine Blase, ein Kreis, eine Lemniskate. Sobald der Geist den Punkt findet, an dem er das Ganze nicht mehr von einem unmöglichen Außen her denken will, sondern von dem einen Punkt aus, der immer schon mitten darin liegt, wird das Unvorstellbare zu einer unmittelbaren Einsicht: Alles ist enthalten, nichts fehlt, und nichts ist außerhalb.

Damit öffnet sich die Frage nach dem Sinn. Wenn das Universum jener in sich geschlossene Block, jene vollendete Blase ist, in der sämtliche Informationen bereits enthalten sind – räumlich wie zeitlich, von Anfang an und für immer –, dann ist das schrittweise Erkennen, das unser Bewusstsein vollzieht, kein zufälliges Nebenprodukt, sondern das zentrale Geschehen innerhalb dieses Gefüges. Das Universum wurde dementsprechend geschaffen, um erkannt zu werden. Der Mensch, als lebendiges und intelligentes Lebewesen, ist von Gott zur Erkenntnis eingeladen. Nicht, weil Gott etwas erfahren müsste, das ihm verborgen wäre, sondern weil die Erkenntnis des Geschöpfes die Vollendung der Schöpfung ist. Der Kreuzungspunkt der Lemniskate, die Gegenwart, wird so zum Ort der Gottesbegegnung – der Moment, in dem sich Zeit und Ewigkeit berühren und das Sein sich selbst erkennt. Darin liegt der Sinn.

### Resonanzfeldtheoretische Einbettung

| Textbaustein | RFT-Entsprechung | Axiom |
|---|---|---|
| Lemniskate als geschlossene Schleife | ε(Δφ) = cos²(Δφ/2): Phase läuft zyklisch, Maximum bei Δφ = 0 (Kreuzungspunkt) | A4 |
| Einpunktkompaktifizierung ℝ → S¹ | Phasenraum ℝ/2πℤ: Δφ = 0 und Δφ = 2π sind identifiziert | A7 |
| Blockuniversum als vollständiges 4D-Gefüge | A1: ψ = A·cos(kx − ωt + φ) ist bereits eine zeitlose Blockstruktur | A1 |
| Gegenwart als Kreuzungspunkt | Resonanzmoment = maximale Kopplungseffizienz = maximaler Informationsfluss | A4, A6 |
| Bewusstsein als zentrales Geschehen | E1 (Beobachter als Resonator): folgt aus A1, A3, A6 | E1 |
| Schöpfung zur Erkenntnis | E1 als teleologische Lesart: der Resonator vollendet das Feld | E1 |

Der Kreuzungspunkt der Lemniskate ist exakt der Punkt ε = 1, Δφ = 0 — vollständige Kopplung, null Phasendifferenz, maximale Energieübertragung. Der Text liefert damit eine geometrisch-philosophische Begründung für die Ausgezeichnetheit dieses Punktes, die im formalen Axiomensystem implizit bleibt.

Auch wenn das Blockuniversum (Axiom 7) alle Zustände simultan enthält, ist die Zeit keine bloße Illusion, sondern eine physikalisch notwendige Größe. Denn Energieumwandlung – der Kern jeder Resonanzkopplung – kann nur in einem Prozess geschehen. Die Frequenz f in der zentralen Gleichung E=π⋅ε(Δφ)⋅ℏ⋅f ist definiert als Ereignis pro Zeit: Ohne Zeit keine Frequenz, ohne Frequenz keine Energieumwandlung, ohne Energieumwandlung keine erfahrbare Welt.

Aus der Vogelperspektive des Blockuniversums sind Vergangenheit, Gegenwart und Zukunft gleichzeitig vorhanden – genau wie bei einem Lagerfeuer bereits feststeht, dass das Holz zu CO₂ wird. Aus der Innenperspektive eines zeitgebundenen Bewusstseins ist genau dieser Prozess der Verbrennung, der Wärme, des Lichts, der Begegnung das, was Erfahrung ausmacht. Die Zeit ist das Medium, in dem Energie umgewandelt wird – und in dem Sinn gestiftet wird.

Das schrittweise Erkennen des Universums ist daher kein Widerspruch zur vollständigen Information des Blockuniversums, sondern dessen notwendige phänomenologische Entfaltung. Der Sinn liegt nicht im überraschenden Ergebnis, sondern in der Resonanzerfahrung des Prozesses selbst. Das Universum wurde nicht geschaffen, um ein bereits bekanntes Ergebnis zu wiederholen, sondern um als zeitlich gestreckter Resonanzprozess erkannt zu werden – von sich selbst durch bewusste Wesen.

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
| 3 | [Warpantrieb](fakten/konzepte/warpantrieb/warpantrieb.md) | A1, A4, A5 | Antriebskonzept — **erste Warpblasensimulation mit positiver Energiedichte** (E⁻ = 0); w-Vorzeichenwechsel via ε(Δφ)-Phasensteuerung |
| 4 | [ResoTrade V15.6](fakten/konzepte/ResoTrade/resotrade_trading_ki.md) | A1–A7 | Anwendungskonzept — demonstriert RFT-Axiome im Finanzmarkt |
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
| 7 | [Schrödinger-Simulation](fakten/simulationen/schrödinger/README.md) | A4 | Ableitung der Schrödinger-Gl. aus Axiom 4; Fidelity = 1,0 (alle 4 Szenarien); Störungstheorie 1−F ~ λ² bestätigt; falsifizierbare Vorhersage für ⁸⁷Rb |

---

## Empirische Nachweise

| # | Nachweis | Axiome | Beschreibung |
|---|---------|--------|-------------|
| 1 | [Resonanzanalyse in Massendaten](fakten/empirisch/cern/dokumentation.md) | A1, A3, A7 | CERN-Daten: Signifikante Resonanzüberschüsse |
| 2 | [Monte-Carlo-Test](fakten/empirisch/monte_carlo/monte_carlo_test/monte_carlo.md) | A1, A3, A7 | 1.500.000 Simulationen, 5 Resonanzen, emp. p = 0 |


---

## Erklärungen

| # | Erklärung | Axiome | Beschreibung |
|---|-----------|--------|-------------|
| 1 | [Schwarmresonanz](fakten/docs/erklaerungen/schwarmresonanz.md) | A1–A7 | Warum Vogelschwärme nicht kollidieren — und warum die RFT neue Türen öffnet |
| 2 | [Resonanz in der Physik](fakten/docs/erklaerungen/resonanz_in_der_physik.md) | A1–A7 | Wie ein Muster Mechanik, Thermodynamik, Elektrodynamik, QM und Relativität verbindet |

---

## Lizenz

Dieses Projekt steht unter der **RFT-Lizenz 1.4**
→ [Zum Lizenztext](lizenz/RFT-lizenz_v1.4.md)

---

© Dominic-René Schu — Resonanzfeldtheorie 2025/2026
