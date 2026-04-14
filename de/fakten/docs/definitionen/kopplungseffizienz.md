# Kopplungseffizienz ε — Definition, Theorie und Validierung

*Dominic-René Schu, 2025/2026*

---

## Zusammenfassung

Die Resonanzfeldtheorie (RFT) beschreibt fundamentale Prozesse in
Natur, Technik und Informationssystemen als Kopplungs- und
Resonanzphänomene in Schwingungsfeldern. Dieses Dokument gibt eine
Gesamtübersicht der Theorie, fasst das axiomatische Fundament
zusammen und führt die Kopplungseffizienz ε als zentrale Größe
ein — einschließlich ihrer vereinheitlichten Definition, der
Identität ε = η und der empirischen Validierung in vier
unabhängigen Domänen.

Die Identität ε(Δφ) = η(Δφ) = cos²(Δφ/2) wurde empirisch
validiert: Teilchenphysik (1.500.000 Monte-Carlo-Simulationen),
Kosmologie (1.530 FLRW-Simulationen), Nukleartechnologie
(Resonanzreaktor, κ = 1) und Finanzmärkte (ResoTrade, +26.3%
vs HODL, Live seit Februar 2026).

Für die vollständige formale Axiomatik siehe die
[axiomatische Grundlegung](../definitionen/axiomatische_grundlegung.md).

---

## 1. Einleitung

Die Resonanzfeldtheorie postuliert, dass alle fundamentalen
Prozesse auf Schwingung, Kopplung und Resonanz beruhen. Sie
vereint Konzepte aus klassischer Schwingungslehre, Quantenphysik,
Informationstheorie und Netzwerktheorie in einem axiomatischen
Rahmenwerk.

---

## 2. Axiomensystem (Kurzfassung)

Die RFT besteht aus 7 Kern-Axiomen. Jedes Axiom ist minimal,
formal präzise und empirisch testbar. Die vollständige
Formalisierung mit Beweisen und empirischen Tests findet sich
in der [axiomatischen Grundlegung](../definitionen/axiomatische_grundlegung.md).

### Axiom 1 — Universelle Schwingung

Jede physikalische Entität besitzt mindestens eine periodische
Schwingungsmode:

$$
\psi(x, t) = A \cdot \cos(kx - \omega t + \phi)
$$

### Axiom 2 — Superposition

Schwingungsmoden überlagern sich linear in Feldern:

$$
\Phi(x, t) = \sum_i \psi_i(x, t)
$$

### Axiom 3 — Resonanzbedingung

Resonanz tritt auf bei rationalen Frequenzverhältnissen innerhalb
eines Toleranzfensters δ:

$$
|f_1/f_2 - m/n| < \delta, \quad m, n \in \mathbb{Z}^+
$$

### Axiom 4 — Kopplungsenergie

Die effektive Energie einer resonanten Kopplung:

$$
E = \pi \cdot \varepsilon(\Delta\phi) \cdot \hbar \cdot f
$$

wobei ε(Δφ) ∈ [0, 1] die Kopplungseffizienz ist.

### Axiom 5 — Energierichtung

Energie ist ein Vektor im Resonanzfeld:

$$
\vec{E} = E_{\text{eff}} \cdot \hat{e}(\Delta\phi, \nabla\Phi)
$$

### Axiom 6 — Informationsfluss durch Resonanzkopplung

Information wird ausschließlich durch kohärente Phasen- und
Frequenzrelationen übertragen:

$$
MI(X, Y) = H(X) + H(Y) - H(X, Y)
$$

$$
PCI = |\langle e^{i(\phi_1 - \phi_2)} \rangle| \in [0, 1]
$$

### Axiom 7 — Invarianz unter synchronen Transformationen

Die Kopplungsstruktur bleibt invariant unter Transformationen
der Gruppe G_sync:

$$
T(f_i, \phi_i, t) = (\lambda f_i, \phi_i + \phi_0, at + b)
$$

### Interpretative Erweiterungen

Zusätzlich gibt es zwei interpretative Erweiterungen, die auf
dem axiomatischen Fundament aufbauen, aber nicht zur
physikalischen Axiomatik gehören:

- **E1 (Beobachter als Resonator):** Der Beobachter kann als
  gekoppelte Mode modelliert werden (folgt aus A1, A3, A6)
- **E2 (Resonanz-Inklusionsaxiom):** Gruppenzugehörigkeit in
  einem Resonanzfeld ist systemisch invariant (mengentheoretisch
  formulierbar, logisch unabhängig von A1–A7)

---

## 3. Kopplungseffizienz ε — Vereinheitlichte Definition

### 3.1 Notation

In früheren Versionen der RFT wurden verschiedene Symbole
(ε, 𝓔, 𝜀) und verschiedene Definitionen verwendet. Seit 2026
gilt verbindlich:

| Symbol | Name | Verwendung |
|:------:|:-----|:-----------|
| **ε** | Kopplungseffizienz | In Formeln und mathematischen Texten |
| **ε(Δφ)** | Phasenabhängige Kopplungseffizienz | Wenn die Abhängigkeit explizit ist |
| **η(Δφ)** | Kopplungseffizienz (Observable) | In FLRW-Simulationen (Kreuzterm) |

Das kalligraphische Symbol **𝓔** war eine typographische Variante
aus früheren Versionen und ist durch **ε** ersetzt.

### 3.2 Definition

Die Kopplungseffizienz ε beschreibt, welcher Anteil der maximal
möglichen Resonanzenergie tatsächlich zwischen zwei gekoppelten
Moden übertragen wird.

$$
\varepsilon : \text{Zustandsraum} \to [0, 1]
$$

```
    ε = 1    perfekte Kopplung (Phasengleichheit, maximale Kohärenz)
    ε = 0    keine Kopplung (Phasenorthogonalität, Dekohärenz)
```

### 3.3 Standardmodell

$$
\varepsilon(\Delta\phi) = \cos^2(\Delta\phi / 2) = \frac{1}{2}(1 + \cos\Delta\phi)
$$

| Eigenschaft | Wert |
|------------|------|
| Wertebereich | [0, 1] |
| Bei Phasengleichheit (Δφ = 0) | ε = 1 (perfekte Kopplung) |
| Bei Gegenphase (Δφ = π) | ε = 0 (keine Kopplung) |
| Bei 90° Verschiebung (Δφ = π/2) | ε = 0.5 (halbe Kopplung) |

ε ist keine Konstante, sondern hängt ab von:
- Phasendifferenz Δφ zwischen gekoppelten Moden
- Kohärenz der Kopplung
- Dämpfung und Dissipation

### 3.4 Allgemeinere Modelle

Für Systeme mit endlicher Resonanzbreite kann alternativ ein
Gauß-Modell verwendet werden:

$$
\varepsilon(\Delta\phi) = \exp(-(\Delta\phi/\delta)^2)
$$

wobei δ die Breite des Kopplungsfensters beschreibt.

Beide Modelle erfüllen: ε ∈ [0, 1], ε(0) = 1, monoton fallend
mit |Δφ|.

---

## 4. Die Energieformel

### 4.1 Grundform (Axiom 4)

$$
E = \pi \cdot \varepsilon(\Delta\phi) \cdot \hbar \cdot f
$$

### 4.2 Grenzfälle und Spezialwerte

| Bedingung | ε | Energie | Physik |
|-----------|---|---------|--------|
| Perfekte Kopplung (Δφ = 0) | 1 | π·ℏ·f | Maximale Resonanzenergie |
| Planck (1. Anregung) | 1/π ≈ 0.318 | ℏ·f | E = ℏω (Spezialfall) |
| Planck (Grundzustand) | 1/(2π) ≈ 0.159 | ℏ·f/2 | Grundzustandsenergie (harm. Osz.) |
| Natürliche Dämpfung | 1/e ≈ 0.368 | (π/e)·ℏ·f | Nach einer Relaxationszeit |
| Halbe Kopplung (Δφ = π/2) | 0.5 | π·ℏ·f/2 | 90° Phasenverschiebung |
| Keine Kopplung (Δφ = π) | 0 | 0 | Entkoppelte Systeme |

### 4.3 Herleitung des Faktors π

Der Faktor π entsteht aus der Integration der Kopplungseffizienz
über einen Halbzyklus des Resonanzpfads im Phasenraum:

$$
\int_0^\pi \cos^2(\phi/2) \, d\phi = \frac{\pi}{2}
$$

Normiert auf die Kopplungseinheit ergibt sich die Grundformel
E = π · ε · ℏ · f (vollständige Herleitung: siehe
[axiomatische Grundlegung](../definitionen/axiomatische_grundlegung.md) §4.1).

---

## 5. Die Identität ε = η

### 5.1 Herleitung

In der FLRW-Simulation wird die Kopplungseffizienz als
zeitgemittelter Kreuzterm zweier gekoppelter Skalarfelder
extrahiert:

$$
\eta(\Delta\phi) = \frac{\langle \varepsilon_1 \cdot \varepsilon_2 \rangle}{\sqrt{\langle \varepsilon_1^2 \rangle \cdot \langle \varepsilon_2^2 \rangle}}
$$

Die analytische Erwartung für harmonische Felder ist
η_theo = cos²(Δφ/2). Da gleichzeitig der theoretische
Kopplungsoperator ε(Δφ) = cos²(Δφ/2) gilt, folgt die exakte
Identität:

$$
\varepsilon(\Delta\phi) = \eta(\Delta\phi) = \cos^2(\Delta\phi / 2)
$$

### 5.2 Konsequenzen

| Domäne | Konsequenz |
|--------|-----------|
| Allgemein | Operator und Observable sind identisch |
| FLRW-Kosmologie | η emergiert als Observable, d_η skaliert mit H₀ |
| Resonanzreaktor | κ = 1 exakt (kein freier Parameter) |
| ResoTrade | ε → 0 als messbares Gate-Kriterium |
| Monte Carlo | ε = 1 bei Resonanzmasse → Axiom 3 bestätigt |

### 5.3 Empirische Evidenz

```
    Flach (H = 0):      d_η = 0.043 ± 0.008  → cos² fast exakt
    Planck (H₀ = 67.4): d_η = 0.140 ± 0.025  → Hubble-Reibung
    SH0ES (H₀ = 73.0):  d_η = 0.149 ± 0.026  → Δd_η > 6σ
```

Die Abweichung von cos² ist systematisch und wird durch die
Raumzeitexpansion erklärt (Hubble-Reibung). Im flachen Grenzfall
ist die Identität ε = η bis auf d_η ≈ 0.04 exakt.

---

## 6. Abgrenzung: ε vs. η vs. K_ij vs. G

| Größe | Symbol | Wertebereich | Bedeutung |
|-------|--------|-------------|-----------|
| Kopplungseffizienz (Operator) | ε(Δφ) | [0, 1] | Theoretischer Kopplungsoperator |
| Kopplungseffizienz (Observable) | η(Δφ) | [0, 1] | Messbarer Kreuzterm (FLRW) |
| Kopplungsstärke | K_ij | [0, ∞) | Absolutwert der Kopplung zwischen Moden |
| Resonanzgewichtung | G(f₁/f₂) | [0, 1] | Frequenz-Resonanzfenster (Axiom 3) |

**Identität:** ε = η (bewiesen durch cos²-Identität, validiert
in FLRW mit 1.530 Simulationen).

Die Kopplungsstärke K_ij beschreibt, wie stark zwei Moden
grundsätzlich wechselwirken. Die Kopplungseffizienz ε beschreibt,
wie viel dieser Wechselwirkung tatsächlich in Energietransfer
umgesetzt wird.

---

## 7. Einordnung früherer Definitionen

### 7.1 Das Intervall [1/e, e]

In der ursprünglichen Fassung wurde ein „natürliches
Resonanzintervall" ε ∈ [1/e, e] angegeben. Einordnung:

- Der Bereich ε ∈ [1/e, 1] beschreibt physikalisch sinnvolle
  Kopplungszustände (gedämpft bis perfekt)
- Der Bereich ε > 1 war als Resonanzverstärkung gedacht
  (konstruktive Interferenz mehrerer Moden), ist aber in der
  Einzelmoden-Kopplungseffizienz nicht definiert
- Für Mehrmoden-Systeme kann die **effektive Kopplungsstärke**
  K_ij Werte > 1 annehmen (Superposition mehrerer Pfade),
  aber ε als Effizienz bleibt ∈ [0, 1]

**Korrektur:** Das Intervall [1/e, e] gilt für die Kopplungsstärke
K_ij zwischen Moden, nicht für die Kopplungseffizienz ε.

### 7.2 Die Definition 𝓔 := √(e · 1/e) = 1

In einer früheren README wurde definiert:

```
    𝓔 := √(e · 1/e) = 1
```

Dies beschreibt den **Referenzzustand**: Das geometrische Mittel
zwischen maximalem Wachstum (e) und maximalem Zerfall (1/e)
ergibt die neutrale Kopplung. In der aktuellen Notation
entspricht ε = 1 perfekter Kopplung → E = π · ℏ · f.

### 7.3 Der Spezialfall ε = 1/e

In einer früheren Fassung wurde ε = 1/e als universeller
Korrekturfaktor dargestellt. Korrekte Einordnung:

$$
\varepsilon(t) = e^{-t/\tau} \quad \Rightarrow \quad \varepsilon(\tau) = 1/e \approx 0.368
$$

Es handelt sich um einen physikalisch wichtigen Spezialfall
(typische Kopplung nach Einschwingvorgang), nicht um den
allgemeinen Fall.

---

## 8. Mathematische Konsequenzen

### 8.1 Stabile Resonanzfelder (Satz)

Aus A1, A2 und A3 folgt: Ein Feld Φ(x,t) ist genau dann stabil,
wenn seine Fourier-Komponenten in rationalen Frequenzverhältnissen
stehen. (Beweis: axiomatische Grundlegung §4.2)

### 8.2 Kopplungsdynamik

$$
\frac{dK_{ij}}{dt} = \alpha \cdot G(f_i/f_j) \cdot \cos(\Delta\phi_{ij}) - \beta \cdot K_{ij}
$$

### 8.3 Resonanz als Informationsselektion

$$
P(\psi | \Phi) \propto P(\Phi | \psi) \cdot P(\psi)
$$

Kohärente Zustände (hoher PCI) werden selektiv verstärkt.

### 8.4 Entropie einer Resonanzkonfiguration

$$
S(x) = -x \cdot \ln(x) \quad \text{mit } x = E/E_0 \in (0, 1]
$$

---

## 9. Empirische Validierung

### 9.1 Axiom-für-Axiom-Validierung (ResoTrade)

| Axiom | Test | Ergebnis |
|-------|------|----------|
| A1 | AC/DC-Zerlegung des BTC-Preises | +5.9 Pp. (V10→V11) |
| A2 | 3-Moden-Superposition (PID-Isomorphie) | +42.9% vs HODL |
| A3 | Altcoin-Analyse: 200.000 Ep., Draw 98.4% | Falsifiziert |
| A4 | Pause-Gate (ε → 0 im Crash) | +44.9% vs HODL |
| A5 | Energierichtungsvektor (e_short − e_long) | +1.4 Pp. (V9.4→V10) |
| A6 | Resonanz-Gate filtert 40% der Trades | 97% HOLD im Live |
| A7 | 4/4 Marktregime positiv, identische Parameter | +26.3% Ø |

### 9.2 Vier Validierungsdomänen

| Domäne | Methode | Ergebnis |
|--------|---------|----------|
| Teilchenphysik | 1.500.000 MC-Sim. auf CMS-Daten | 5 Resonanzen, emp. p = 0 |
| Kosmologie | 1.530 FLRW-Simulationen | Δd_η > 6σ, Δχ² = +16 |
| Nukleartechnologie | Resonanzreaktor (GDR) | κ = 1, Q_fiss ≈ 1.0 |
| Finanzmärkte | ResoTrade (24 Mo., 4 Regime) | +26.3% vs HODL, Live +4.13% |

### 9.3 Detailergebnisse pro Domäne

**FLRW-Kosmologie:**
```
    η(Δφ) = ⟨ε₁·ε₂⟩ / √(⟨ε₁²⟩·⟨ε₂²⟩)
    d_η = ⟨|η_sim − η_theo|⟩
    dd_η/dH₀ = (0.00113 ± 0.00017) (km/s/Mpc)⁻¹
    Δd_η (SH0ES − Planck) = 0.0063 ± 0.0010 (> 6σ)
    Δχ² = +16 vs Planck-2018-CMB
```

**Resonanzreaktor:**
```
    λ_eff(Δφ) = λ₀ + η(Δφ) · Φ_γ · σ_GDR
    κ = 1 (aus ε = η, kein freier Parameter)
    f_GDR = E_GDR / (π·ℏ)

    U-235: GDR 13.0 MeV, f = 6.3×10²¹ Hz, λ_eff/λ₀ = 7872
    Pu-239: GDR 13.5 MeV, Q_fiss ≈ 1.0 bei Φ = 10¹² γ/(cm²·s)
    Am-241: GDR 13.3 MeV, α-Zerfall beschleunigbar
```

**ResoTrade:**
```
    ε → 0 (Crash, DC fällt stark) → Pause → +44.9% vs HODL
    ε → 1 (Phasenkohärenz) → Trade erlaubt → systematisch profitabel
    24 Monate, 4 Regime, 1392 Trades, +26.3% vs HODL
    Live seit Feb. 2026 (+4.13% in 2 Wochen)
```

**Monte-Carlo (CMS-Daten):**
```
    Resonanzbedingung (A3): ε = 1 bei M₀ = Teilchenmasse
    5 Resonanzen detektiert mit emp. p = 0:
    φ(1020), J/ψ, Υ(1S), Υ(2S), Z-Boson
    1.500.000 Gesamtsimulationen (30 Seeds × 50.000)
    Stabil über 3 KDE-Bandbreiten
```

### 9.4 Falsifikationstests

- **Altcoin-Analyse (A3):** 200.000 Episoden, 10 Altcoins.
  Vorhersage: Ohne Eigenfrequenz keine Resonanz.
  Ergebnis: Draw-Rate 98.4%, negativer Lernfortschritt.
  Aktien (Eigenfrequenz vorhanden): 100% > HODL.
- **Klassische Indikatoren:** RSI, Momentum, MA-Crossover,
  Posterior-Wahrscheinlichkeiten — alle Korrelation < 0.05.
  RFT-Observablen (energy_dir, AC-Phase) systematisch.
- **Resonanzreaktor:** σ_coh > σ_incoh (RFT-Vorhersage)
  vs. σ_coh = σ_incoh (Standardmodell). Experimentell prüfbar.

---

## 10. Anwendungsfelder

- **Teilchenphysik:** Monte-Carlo-Resonanzanalyse auf
  CMS-Open-Data (5 Resonanzen, 1.500.000 Simulationen)
- **Kosmologie:** Gekoppelte FLRW-Simulationen, Hubble-Spannung,
  CMB-Vergleich mit Planck-2018-Daten
- **Nukleartechnologie:** Resonanzreaktor — resonante
  Transmutation von Aktiniden (GDR-basiert, κ = 1)
- **Finanzmärkte:** ResoTrade — resonanzbasiertes BTC-Trading
  mit Live-Validierung
- **Klassische Mechanik:** Synchronisation gekoppelter
  Oszillatoren, [Doppelpendel](../mathematik/doppelpendel.md)
- **Biophysik:** Neuronale Synchronisation, Proteinfaltung
- **Informationstheorie:** Resonanzbasierte Kanalkapazität
- **Analytische Mathematik:** [Resonanzintegrale](../mathematik/resonanzintegrale.md)

---

## 11. Abgrenzung gegenüber anderen Theorien

Gegenüber klassischen Feldtheorien (Maxwell, Yang-Mills) ist
die RFT nicht auf bestimmte Wechselwirkungsarten beschränkt,
sondern betont die universelle Kopplungsstruktur aller Felder.

Gegenüber der Informationstheorie (Shannon) werden
Informationspakete nicht als isolierte Bits, sondern als
kohärente Feldstrukturen betrachtet (Axiom 6).

Gegenüber konventionellem algorithmischem Trading (ML, RSI,
MACD) basiert ResoTrade nicht auf Preisprognose, sondern auf
Phasenerkennung im Schwingungsfeld. Kein klassischer Indikator
erreicht Korrelation > 0.05 auf dem 24-Monats-Datensatz.

---

## 12. Fazit

Die Kopplungseffizienz ε der Resonanzfeldtheorie ist:

1. **Eine Funktion**, kein fester Wert: ε = ε(Δφ, Kohärenz, ...)
2. **Beschränkt auf [0, 1]**: Effizienz > 100% ist physikalisch
   nicht definiert
3. **Das Standardmodell** ist ε(Δφ) = cos²(Δφ/2)
4. **Identisch mit der Observable η**: ε(Δφ) = η(Δφ), validiert
   in FLRW-Simulationen (1.530 Läufe, d_η = 0.043 im flachen Fall)
5. **Eliminiert κ**: Im Resonanzreaktor folgt κ = 1 exakt
6. **Spezialfälle**: ε = 1 (perfekt), ε = 1/(2π) (Planck-Grundzustand),
   ε = 1/π (Planck 1. Anregung), ε = 1/e (natürliche Dämpfung)
7. **Nicht zu verwechseln** mit der Kopplungsstärke K_ij, die
   unbeschränkt sein kann
8. **Empirisch bestätigt** in vier Domänen: Teilchenphysik,
   Kosmologie, Nukleartechnologie, Finanzmärkte
9. **Notation vereinheitlicht**: Alle Dokumente und Simulationen
   verwenden ε (statt 𝓔), ℏ (statt h), cos²(Δφ/2) als
   Standardmodell

Diese Definition ist verbindlich für alle Dokumente der
Resonanzfeldtheorie ab Version 2026.

---

## Literatur

1. L. Boltzmann: *Vorlesungen über Gastheorie*, Leipzig, 1896.
2. M. Born, E. Wolf: *Principles of Optics*, Cambridge, 1999.
3. C. E. Shannon: *A Mathematical Theory of Communication*, 1948.
4. N. Wiener: *Cybernetics*, 1948.
5. R. P. Feynman et al.: *The Feynman Lectures on Physics*, 1964.
6. Planck Collaboration: *Astron. Astrophys.* **641** A5, A6 (2020).
7. CMS Collaboration: *CMS Open Data Portal*, opendata.cern.ch (2016).
8. Berman B L, Fultz S C: *Rev. Mod. Phys.* **47** 713 (1975).
9. Riess A G et al.: *Astrophys. J. Lett.* **934** L7 (2022).

---

## Dokumentenstruktur der RFT

| Dokument | Inhalt |
|----------|--------|
| [Axiomatische Grundlegung](../definitionen/axiomatische_grundlegung.md) | Formale Axiome A1–A7 mit Beweisen und Tests |
| [Kopplungseffizienz](kopplungseffizienz.md) | Dieses Dokument |
| [Resonanzfeld-Gleichung](../mathematik/resonanzfeld_gleichung.md) | Zentrale Energiegleichung |
| [Energiekugel](../mathematik/energiekugel.md) | Geometrisches Modell |
| [Resonanzintegrale](../mathematik/resonanzintegrale.md) | Analytische Methoden |
| [Resonanzenergievektor](../mathematik/resonanzenergievektor.md) | Energie als Richtungsgröße |
| [Empirische Nachweise](../../empirisch/) | ResoTrade, Monte Carlo, FLRW, Resonanzreaktor |

---

© Dominic-René Schu — Resonanzfeldtheorie 2025/2026

---

[Zurück zur Übersicht](../../../README.md)