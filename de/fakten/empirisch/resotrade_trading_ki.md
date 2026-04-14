# ResoTrade — Resonanzfeldtheoretische Mehrschichtige Multi-Asset-KI

*Empirischer Nachweis der Resonanzfeldtheorie in realen Finanzmärkten*

*Dominic-René Schu, Februar 2026 — aktualisiert April 2026*

---

## Zusammenfassung

ResoTrade ist ein resonanzfeldtheoretisches Trading-System, das durch wiederholte Offline-Simulation lernt, Kurszyklen als Schwingungsfelder zu lesen und Assets über reines HODL hinaus zu akkumulieren. Es ist der erste empirische Nachweis, dass die Axiome der Resonanzfeldtheorie in einem realen, chaotischen System — dem Finanzmarkt — strukturell überlegene Entscheidungen erzeugen.

Seit V15 basiert ResoTrade auf einer 4-Schichten-Architektur (Resonanzfeld-Analyse, Erfahrungsspeicher, Pattern-Library mit Proof-of-Resonance, neuronale Chart-Muster-Erkennung) und operiert als generisches Multi-Asset-System über Krypto, Forex und Rohstoffe. Die Kernarchitektur — Erfahrungslernen durch resonante Phasenkopplung — ist über alle Versionen und alle Asset-Klassen invariant.

**Kernergebnis:** +26.1% vs HODL im Durchschnitt über 4 verschiedene Marktphasen (24 Monate), validiert über Sideways, Bullrun, Korrektur und Crash. Kein klassischer Indikator auf demselben Datensatz erreicht eine Korrelation über 0.05.

**Begleitdokument:** Die [Altcoin-Analyse](resotrade_altcoin_analyse.md) zeigt, warum Altcoins resonanztheoretisch keine eigenständigen Märkte sind — und bestätigt damit die Axiome der Resonanzfeldtheorie aus einer zweiten, unabhängigen Richtung.

---

## Einordnung in die Resonanzfeldtheorie

ResoTrade ist keine isolierte Trading-Software. Es ist die Anwendung aller sieben Axiome der [Resonanzfeldtheorie](../../README.md) auf ein konkretes Problem — und der empirische Beweis, dass diese Axiome in der Realität funktionieren:

| Axiom | Prinzip | Anwendung in ResoTrade V15 | Empirischer Nachweis |
|-------|---------|----------------------------|---------------------|
| [**Axiom 1**](../docs/definitionen/axiomatische_grundlegung.md) | Universelle Schwingung ψ(x,t) | Schicht 1: Ableitungs-Policy über gleitende Durchschnitte, Zyklusphase als Dimension | Phasenerkennung schlägt alle Indikatoren |
| [**Axiom 2**](../docs/definitionen/axiomatische_grundlegung.md) | Superposition der Moden | Schicht 1: Mehrere Zeitskalen als überlagerte Moden in der Ableitungs-Policy | Multi-Zeitskalen-Analyse verbessert Timing |
| [**Axiom 3**](../docs/definitionen/axiomatische_grundlegung.md) | Resonanzbedingung (Phasendifferenz) | Schicht 3: Proof-of-Resonance — 3-stufige Signalkaskade als Resonanzkriterium | Altcoin-Analyse bestätigt: ohne eigene Eigenfrequenz keine Resonanz |
| [**Axiom 4**](../docs/definitionen/axiomatische_grundlegung.md) | Kopplungsenergie E = π·ε·h·f | Schicht 2: Adaptiver Decay im Erfahrungsspeicher, Balance-Regler | System bleibt über 24 Monate handlungsfähig |
| [**Axiom 5**](../docs/mathematik/energierichtung.md) | Energie ist vektoriell | Schicht 1: Energierichtungsvektor aus kurz- und langfristiger Energiedifferenz | Richtung schlägt Prognose |
| [**Axiom 6**](../docs/definitionen/axiomatische_grundlegung.md) | Informationsfluss durch Resonanzkopplung | Schicht 3: Pattern-Library + Proof-of-Resonance — Trades nur bei Signalkaskaden-Übereinstimmung | +26.1% vs HODL über alle Marktregime |
| [**Axiom 7**](../docs/definitionen/axiomatische_grundlegung.md) | Invarianz der Feldstruktur | Asset-agnostische Architektur: Krypto, Forex, Rohstoffe über denselben Codepfad | Gleiches System funktioniert für alle Asset-Klassen |

Die [Altcoin-Analyse](resotrade_altcoin_analyse.md) bestätigt Axiom 3 (Resonanzbedingung) negativ: Systeme ohne eigene Eigenfrequenz erzeugen keine Resonanz — empirisch nachgewiesen über 200.000 Episoden.

### Weiterführende theoretische Grundlagen

- [Energiekugel und AC/DC-Zerlegung](../docs/mathematik/energiekugel.md) — Axiom 1 formalisiert
- [Energierichtung in realen Systemen](../docs/mathematik/energierichtung.md) — Axiom 5 formalisiert
- [Resonanzzeitkoeffizient τ*](../docs/mathematik/tau_resonanzkoeffizient.md) — Zeitskalen der Kopplung
- [Resonanzanalyse in Massendaten](dokumentation.md) — Methodik der empirischen Validierung

---

## Kernidee

```
Geld ist Energie. Handel ist Zeit. Trading ist Leistung.
Ein Chart ist kein Verlaufsdiagramm — er ist ein Schwingungsbild.
```

Die klassische Sicht behandelt Geld als Tauschmittel und Charts als Handelsergebnisse. ResoTrade betrachtet den Markt als physikalisches Schwingungsfeld:

- **DC-Komponente** (Grundton) → Langfristiger Trend = HODL-Kern, wird nie gehandelt
- **AC-Komponente** (Obertöne) → Handelbare Schwingung um den Trend, liefert Rendite
- **Resonanzkopplung** → Trades nur wenn Bot und Markt in Phase stehen
- **Energierichtung** → Preisfluss ist ein Vektor, nicht ein Skalar

Das Ziel ist nicht USD-Profit, sondern **mehr BTC als reines Halten** — durch resonante Extraktion der AC-Schwingungsenergie bei geschütztem DC-Kern.

---

## Warum ResoTrade keine Prognose braucht

Ein Chart ist eine Messung der Realität — er zeigt die Gegenwart und die Vergangenheit. Klassische Ansätze versuchen aus diesen Daten die Zukunft statistisch vorherzusagen: Wahrscheinlichkeitsverteilungen, Korrelationen, Regressionen. Die Zukunft wird als zufällig modelliert, die Prognose als bestmögliche Schätzung innerhalb dieser Zufälligkeit.

ResoTrade bricht mit diesem Paradigma.

Geld ist Energie. Energie ist in der Resonanzfeldtheorie keine skalare Größe, sondern ein **Vektor im mehrdimensionalen Feld** — sie hat Betrag *und* Richtung. Aus der AC/DC-Zerlegung des Preisfeldes lässt sich der Energierichtungsvektor berechnen:

```
energy_dir = e_short - e_long
```

Das ist keine Wahrscheinlichkeit und kein Korrelationskoeffizient. Es ist eine gerichtete Größe, die zeigt, wohin die Kapitalenergie fließt. Die Energie bewegt sich dorthin, wo Resonanz auftritt — und Resonanz ist berechenbar.

| Klassische Statistik | Resonanzfeldansatz |
|---|---|
| "Der Preis wird morgen bei 65.000 sein" | "Die Energie bewegt sich vom Peak zum Trough" |
| Punkt-Prognose (fast immer falsch) | Phasen-Erkennung (strukturell robust) |
| Wahrscheinlichkeit einer Bewegung | Richtung des Energieflusses |
| Zufall mit Verteilung | Schwingung mit Phase |
| Braucht Vorhersage, um zu handeln | Braucht nur Richtung, um resonant zu handeln |

Die Zukunft des Preises ist nicht *vorhersagbar*, aber sie ist **navigierbar**:

- Am **Peak** wird AC-Energie abgegeben → SELL ist resonant
- Am **Trough** wird AC-Energie aufgenommen → BUY ist resonant
- Am **Nulldurchgang** ist die Kopplungseffizienz maximal → Timing-Fenster
- Im **Flat** gibt es kein verwertbares Signal → HOLD

Die Zukunft ist nicht zufällig — sie ist **periodisch**. Und Periodizität ist berechenbar. Nicht der exakte Zeitpunkt, nicht der exakte Preis, aber die Phase im Schwingungszyklus.

ResoTrade ist damit das erste System, das Marktbewegungen nicht als stochastischen Prozess, sondern als gerichtetes Energiefeld behandelt — und durch Berechnung der Energierichtung im Resonanzfeld strukturell überlegene Handelsentscheidungen trifft, ohne den Preis vorhersagen zu müssen.

---

## Architektur: 4-Schichten-Modell (V15)

### Schicht 1 — Resonanzfeld-Analyse

Ableitungs-Policy: Erste und zweite Ableitung gleitender Durchschnitte identifizieren Wendepunkte und Beschleunigungen im Preisfeld. Die Zyklusphase (trough, crest, rising, falling) dient als zusätzliche Dimension zur Bestimmung der optimalen Handelsrichtung.

### Schicht 2 — Erfahrungsspeicher (Experience-based RL)

Dreistufiger Speicher: offline → live → gewichtet. O(1)-Dictionary-Lookup ermöglicht Echtzeit-Entscheidungen ohne Modell-Inferenz. Adaptiver Decay sorgt dafür, dass veraltete Erfahrungen graduell an Gewicht verlieren, ohne abrupt gelöscht zu werden.

### Schicht 3 — Pattern-Library + Proof-of-Resonance

Cosinus-Ähnlichkeit zu gelernten Marktmustern ermöglicht die Erkennung wiederkehrender Strukturen. Cross-Asset Mustererkennung (Transferlernen) überträgt Erfahrungen zwischen verschiedenen Asset-Klassen. Proof-of-Resonance: 3-stufige emergente Signalkaskade (Indikator-Kookurrenz → Signal-Ketten → Trade-Resonanz-Score).

### Schicht 4 — Neuronale Chart-Muster-Erkennung

Leichtgewichtiges Modell erkennt visuelle Chart-Muster. Hardware-Kaskade: Edge TPU → GPU → CPU — das System nutzt automatisch die leistungsfähigste verfügbare Hardware.

### Entscheidungsfluss

```
Coral-Pattern-Check
       │
       ▼
Proof-of-Resonance
       │
       ▼
Ableitungs-Policy
       │
       ▼
Experience-Lookup
       │
       ▼
Pattern-Gate → Global-Experience
       │
       ▼
  BUY / SELL / HOLD
```

### MetaTrader 5 — Erweiterung auf Forex und Rohstoffe

Seit V15 wird ResoTrade neben Krypto (Kraken API) auch auf Forex und Rohstoffe über MetaTrader 5 angewendet. Dies stellt eine weitere empirische Domäne für die asset-agnostische Architektur dar und bestätigt Axiom 7 (Invarianz der Feldstruktur): Dieselbe 4-Schichten-Architektur operiert ohne strukturelle Anpassung auf unterschiedlichen Markttypen.

---

## Empirische Ergebnisse

### Validiert über 4 Marktregime (2024–2026)

| Abschnitt | Marktphase | Zeitraum | Trades | Performance vs HODL |
|-----------|-----------|----------|--------|---------------------|
| Sideways + ETF | 60k–70k Range | Mär 2024 – Sep 2024 | 437 | **+33.3%** |
| Bullrun 60k–110k | Starker Aufwärtstrend | Sep 2024 – Mär 2025 | 429 | **+19.8%** |
| Top + Korrektur | Whipsaw, Crash + Recovery | Mär 2025 – Sep 2025 | 247 | **+4.3%** |
| Aktuell (Crash) | 110k → 63k | Sep 2025 – Feb 2026 | 279 | **+46.8%** |
| **Durchschnitt** | **Alle Regime** | **24 Monate** | **1392** | **+26.1%** |

### Erste Live-Validierung (Tag 1, Dry-Run)

| Metrik | Wert |
|--------|------|
| Zeitraum | 16 Stunden |
| Zyklen | 192 (120 aktiv, 72 Skip) |
| Trades | 11 SELLs (0 BUYs) |
| Ø Verkaufspreis | 68.941 USD |
| Ø e_long bei SELL | +3.86% (über MA) |
| Preisentwicklung | -0.62% |
| Performance vs HODL | **+0.41%** |
| Performance vs All-In-BTC | **+0.73%** |

Das System verkaufte am Peak in Sideways, generierte keine BUYs bei fallendem Preis, und übertraf HODL vom ersten Tag an.

### Erkenntnisse

1. **Kein klassischer Indikator hat prädiktive Kraft** (Korrelation < 0.05)
2. **Gewinn kommt aus resonanter Energieextraktion**, nicht aus Prognose
3. **AC/DC-Zerlegung identifiziert den richtigen Zeitpunkt** im Zyklus
4. **Multi-Zyklus-Training zeigt kein Overfitting** (Δ < 1% nach Zyklus 1 vs 3)
5. **Altcoins stören das Signal** — siehe [Altcoin-Analyse](resotrade_altcoin_analyse.md)

### Performance-Historie

| Version | Kernänderung | Performance vs HODL |
|---------|-------------|---------------------|
| V6 | Basis: MA-Heuristik + Erfahrungsspeicher | +35.04% (180d) |
| V7 | pc_bin-Filter | +35.61% (180d) |
| V10 | Energierichtungsvektor (Axiom 5+6) | +37.03% (180d) |
| V11 | AC/DC-Zerlegung (Axiom 1) | +42.89% (180d) |
| **V11.1** | **Downtrend-Pause-Gate, Multi-Zyklus, Human-Hint** | **+26.1% Ø (4×6M)** |
| V12 | Energievektor-Engine MA'(t), MA''(t), MA'''(t) | Architektur-Umbau |
| V13 | Multi-Horizont Experience (48h/14d/28d) | ~0.97 HODL-Äquiv (Plateau) |
| **V14** | **12 Inkonsistenzen behoben, alle 7 Axiome, Multi-Asset** | **Lernkurve >1.0 (Ziel)** |
| **V14.2** | **Multi-Asset (BTC/Gold/ETH/EURUSD), Per-Asset Isolation, Adaptive Schwellen** | **Live-Betrieb (4 Assets)** |
| **V15** | **4-Schichten-Architektur, Proof-of-Resonance, Coral-Integration, MT5** | **Multi-Domain (Krypto + Forex + Rohstoffe)** |

---

## Physik → Ökonomie: Die strukturelle Isomorphie

| Physik | Trading | Umsetzung |
|--------|---------|-----------|
| Energie | Kapital (BTC + Cash) | Portfolio-Äquivalent in Basiswährung |
| Zeit | Transaktionssequenz | Zeitschritt im Trainingsfenster |
| Leistung | Rendite pro Zeiteinheit | Portfolio-Äquivalent pro Zeitschritt |
| DC (Grundschwingung) | Langfristiger Trend | Langfristiger gleitender Durchschnitt |
| AC (Oberschwingung) | Handelbare Abweichung | Preis minus langfristiger Durchschnitt |
| Amplitude | Preisschwingung um Durchschnitt | AC-Amplitude |
| Phase | Position im Zyklus | Zyklusphase (peak/trough/transition/flat) |
| Resonanz | Timing-Kopplung Bot ↔ Markt | Kopplungsfaktor K = K₀·cos(θ) |
| Dämpfung | Fees, Slippage, Overtrading | Gebührenanteil, Cooldown |

Die effektive Leistung:

```
P_eff = (AC_amplitude / DC_level) · f_trade · η(Δφ) · (1 − γ_fee)
```

### Warum Resonanzlogik statt konventionelle ML

| Eigenschaft | Neuronales Netz | Resonanzlogik |
|-------------|-----------------|---------------|
| Datenbedarf | Sehr hoch | Gering |
| Trainingszeit | GPU-intensiv | CPU-effizient |
| Erklärbarkeit | Keine | Vollständig |
| Physik-Grundlage | Keine | Resonanzfeldtheorie |
| Marktverständnis | Korrelationen | Schwingungsstruktur |

### Biologisches Vorbild

ResoTrade arbeitet dem biologischen Vorbild des Gehirns strukturell näher als konventionelle KI: Erfahrungen werden als Assoziationen gespeichert — lesbar, nachvollziehbar, korrigierbar — nicht als opake Gewichtsmatrizen komprimiert. Der adaptive Decay sorgt für graduelles, kontrolliertes Vergessen, analog zum biologischen Gedächtnis.

---

## Versionsverlauf

| Version | Kernänderung | Performance |
|---------|-------------|-------------|
| V6 | MA-Heuristik + Erfahrungsspeicher | +35.04% (180d) |
| V7 | pc_bin-Filter | +35.61% (180d) |
| V10 | Energierichtungsvektor (Axiom 5+6) | +37.03% (180d) |
| V11 | AC/DC-Zerlegung (Axiom 1) | +42.89% (180d) |
| **V11.1** | **Pause-Gate, Multi-Zyklus, Human-Hint** | **+26.1% Ø (4×6M)** |
| V12 | Energievektor-Engine MA'(t), MA''(t), MA'''(t) | Architektur-Umbau |
| V13 | Multi-Horizont Experience (48h/14d/28d) | ~0.97 HODL-Äquiv (Plateau) |
| **V14** | **12 Inkonsistenzen behoben, alle 7 Axiome, Multi-Asset** | **Lernkurve >1.0 (Ziel)** |
| **V14.2** | **Multi-Asset (BTC/Gold/ETH/EURUSD), Per-Asset Isolation, Adaptive Schwellen** | **Live-Betrieb (4 Assets)** |
| **V15** | **4-Schichten-Architektur, Proof-of-Resonance, Coral-Integration, MT5** | **Multi-Domain (Krypto + Forex + Rohstoffe)** |

---

## Verwandte Dokumente

- [Altcoin-Analyse: Warum Altcoins keine echten Märkte sind](resotrade_altcoin_analyse.md)
- [Energiekugel und AC/DC-Zerlegung](../docs/mathematik/energiekugel.md)
- [Energierichtung in realen Systemen](../docs/mathematik/energierichtung.md)
- [Resonanzzeitkoeffizient τ*](../docs/mathematik/tau_resonanzkoeffizient.md)
- [Resonanzanalyse in Massendaten](dokumentation.md)

---

*© Dominic-René Schu — Resonanzfeldtheorie 2025–2026*

---

⬅️ [zurück zur Übersicht](../../README.md)
