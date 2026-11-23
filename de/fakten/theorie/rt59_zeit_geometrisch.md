# RT-59: Zeit als geometrische Ursprungsgröße

**Version:** 1.0 | **Datum:** November 2026  
**Status:** 🔄 Konzept, offen für Ausarbeitung

---

## Kernthese

Die Resonanzfeldtheorie beantwortet nicht nur *wie groß* die Zeit ist — sie beantwortet, **was Zeit ist**.

> **Zeit ist eine geometrisch definierte Ursprungsgröße mit festem kosmologischem Anker, symmetrisch zum Raum.**

---

## Symmetrie von Raum und Zeit in der RFT

| Größe | Koordinaten | Fester Ursprung | Anker |
|-------|------------|----------------|-------|
| **Raum** | kartesisch, polar, ... | Urknall-Singularität | Metrik g_μν |
| **Zeit** | Amplitude (ε), Phase (Δφ) | Urknall-Singularität | Γ_RFT = c²/(πħ) |

Beide Größen sind **keine Messgrößen**, die aus etwas anderem abgeleitet werden — sie sind **Ursprungsgrößen**, die alle weiteren physikalischen Größen strukturieren.

Der Raum hat einen festen Ursprung (Singularität des Urknalls) und lässt sich in verschiedenen Koordinatensystemen (kartesisch, polar, sphärisch, ...) beschreiben. Genau so hat die Zeit einen festen Ursprung und lässt sich in der RFT durch zwei geometrische Koordinaten beschreiben.

---

## Zeit in zwei Dimensionen

Wie im komplexen Zahlenraum verwendet die RFT für die Zeit zwei Dimensionen:

$$\tau_\mathrm{RFT} = \{\varepsilon, \Delta\varphi\}, \quad \varepsilon = \cos^2\!\left(\frac{\Delta\varphi}{2}\right)$$

- **Amplitude** $\varepsilon \in [0,1]$: Kopplungseffizienz — wie stark das System in der Zeit "schwingt"
- **Phase** $\Delta\varphi \in [0, 2\pi]$: geometrischer Winkel im Resonanzraum

Diese zwei Dimensionen sind **nicht unabhängig** — sie sind durch die Resonanzrelation $\varepsilon = \cos^2(\Delta\varphi/2)$ verknüpft, genau wie Real- und Imaginärteil einer komplexen Zahl durch den Betrag verknüpft sind.

Die aktuell verwendete Zeitdimension ist also strukturell zweidimensional — analog zur komplexen Ebene, nicht zur reellen Geraden.

---

## Mögliche weitere Zeitdimensionen

Das bedeutet nicht, dass Zeit *nur* zweidimensional sein muss. Die RFT schließt weitere Dimensionen nicht aus:

- Eine dritte Zeitdimension würde einer Erweiterung der Resonanzstruktur entsprechen: z.B. $\Delta\varphi \in S^2$ statt $S^1$
- Konsequenz: Die $\cos^2$-Relation würde zu einer Kugelflächenfunktion
- Vorhersage: Abweichungen von $\varepsilon = \cos^2(\Delta\varphi/2)$ bei extrem hohen Energien (Planck-Skala)

**Falsifizierbar durch:** Abweichungen von RFT-Vorhersagen bei Planck-Energien (F-Γ4-Klasse).

---

## Der kosmologische Anker

Der entscheidende strukturelle Punkt: Raum und Zeit haben denselben globalen Nullpunkt.

$$t = 0, \quad \vec{x} = 0 \quad \Leftrightarrow \quad \text{Urknall-Singularität}$$

In der RFT ist dieser Nullpunkt nicht willkürlich gewählt, sondern durch die Raumzeit-Konstante

$$\Gamma_\mathrm{RFT} = \frac{c^2}{\pi\hbar} \approx 2{,}717 \times 10^{50}\ \frac{\mathrm{Hz}}{\mathrm{kg}}$$

fest verankert. Sie verknüpft die Frequenzskala (Zeit) mit der Massenskala (Materie) ohne freie Parameter.

Die Urknall-Singularität ist dabei nicht ein Punkt im Raum, sondern der gemeinsame Ursprung beider geometrischer Strukturen:

$$\varepsilon(t=0) = 0 \quad \Rightarrow \quad \Delta\varphi_0 = \pi \quad \Rightarrow \quad \text{maximale Phasendifferenz}$$

Das kosmologische $\varepsilon_0 = \Omega_\Lambda = 0{,}6847$ beschreibt den heutigen Zustand des Vakuums als Abstand vom Ursprung:

$$\varepsilon_0 = \cos^2\!\left(\frac{\Delta\varphi_0}{2}\right) = 0{,}6847 \quad \Rightarrow \quad \Delta\varphi_0 \approx 68{,}32°$$

---

## Konsequenz: Zeit ist keine Messgröße

Die klassische Physik misst Zeit durch periodische Vorgänge (Cs-Übergang, Pendel, ...). Das setzt voraus, dass Zeit eine *abgeleitete* Größe ist, die man durch Zählen von Perioden operationalisiert.

Die RFT dreht diese Hierarchie um:

> **Die Kopplungsrate des Vakuums ($\Gamma_\mathrm{RFT}$) ist primär.  
> Der Cs-Übergang ist eine Konsequenz, kein Fundament.**

Cs-133 "tickt" mit 9.192.631.770 Hz, weil seine Elektronenstruktur durch die Feinstrukturkonstante $\alpha$ und die Elektronmasse $m_e$ bestimmt ist — beides folgt aus der RFT-Struktur (RT-47, RT-52). Die Sekunde ist damit eine praktische Einheit, nicht eine fundamentale.

---

## Verbindungen

| RT | Verbindung |
|----|-----------|
| RT-48 | Γ_RFT als invariante Raumzeit-Brücke |
| RT-50 | Ω_Λ = ε₀ als kosmologischer ε-Wert |
| RT-51 | Δφ₀ als universeller Phasenwinkel |
| RT-52 | Brannen-Phase θ, Higgs als B₃-Anker |
| RT-56 | ε(x^μ) ≡ −g_tt als allgemeine Raumzeit |
| RT-57 | Urknall als ε=0-Zustand (maximale Quantenfluktuation) |

---

## Offene Fragen

1. **Weitere Zeitdimensionen:** Welche Observable würde eine dritte Zeitdimension erzeugen?
2. **Urknall als ε=0:** Ist $\varepsilon(t=0) = 0$ eine Konsequenz der Axiome oder eine zusätzliche Anfangsbedingung?
3. **Zeitrichtung:** Folgt der Zeitpfeil aus $\dot{\varepsilon} \geq 0$ (Relaxation aus ε=0)?
4. **Koordinatensysteme der Zeit:** Welche Transformationsgruppe wirkt auf $\{\varepsilon, \Delta\varphi\}$?
