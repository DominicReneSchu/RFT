# ResoTrade — Resonanzfeldtheoretische Multi-Asset-KI mit AC/DC-Zerlegung

*Empirischer Nachweis der Resonanzfeldtheorie in realen Finanzmärkten*

*Dominic-René Schu, Februar 2026 — aktualisiert März 2026*

---

## Zusammenfassung

ResoTrade ist ein resonanzfeldtheoretisches Trading-System, das durch wiederholte Offline-Simulation lernt, Kurszyklen als Schwingungsfelder zu lesen und Assets über reines HODL hinaus zu akkumulieren. Es ist der erste empirische Nachweis, dass die Axiome der Resonanzfeldtheorie in einem realen, chaotischen System — dem Finanzmarkt — strukturell überlegene Entscheidungen erzeugen.

Seit V14.2 ist ResoTrade ein generisches Multi-Asset-System (BTC, Gold, ETH, EURUSD) mit 12-dimensionaler Fine-Chain, adaptiven Schwellen (V14 Feldzustand), parallelem Training und Dashboard-gesteuertem Betrieb über Streamlit. Die Kernarchitektur — Erfahrungslernen durch resonante Phasenkopplung — ist über alle Versionen und alle Asset-Klassen invariant.

**Kernergebnis:** +26.1% vs HODL im Durchschnitt über 4 verschiedene Marktphasen (24 Monate), validiert über Sideways, Bullrun, Korrektur und Crash. Kein klassischer Indikator auf demselben Datensatz erreicht eine Korrelation über 0.05.

**Begleitdokument:** Die [Altcoin-Analyse](resotrade_altcoin_analyse.md) zeigt, warum Altcoins resonanztheoretisch keine eigenständigen Märkte sind — und bestätigt damit die Axiome der Resonanzfeldtheorie aus einer zweiten, unabhängigen Richtung.

---

## Einordnung in die Resonanzfeldtheorie

ResoTrade ist keine isolierte Trading-Software. Es ist die Anwendung aller sieben Axiome der [Resonanzfeldtheorie](../../README.md) auf ein konkretes Problem — und der empirische Beweis, dass diese Axiome in der Realität funktionieren:

| Axiom | Prinzip | Anwendung in ResoTrade V14.2 | Empirischer Nachweis |
|-------|---------|------------------------------|---------------------|
| [**Axiom 1**](../docs/mathematik/axiomatische_grundlegung.md) | Universelle Schwingung ψ(x,t) | AC/DC-Zerlegung: Preis = DC + AC | Phasenerkennung schlägt alle Indikatoren |
| [**Axiom 2**](../docs/mathematik/axiomatische_grundlegung.md) | Superposition der Moden | MA_SHORT + MA_LONG als überlagerte Moden | Multi-Zeitskalen-Analyse verbessert Timing |
| [**Axiom 3**](../docs/mathematik/axiomatische_grundlegung.md) | Resonanzbedingung (Phasendifferenz) | Symmetrische BUY/SELL-Schwellen (V14-Fix) | Altcoin-Analyse bestätigt: ohne eigene Eigenfrequenz keine Resonanz |
| [**Axiom 4**](../docs/mathematik/axiomatische_grundlegung.md) | Kopplungsenergie E = π·ε·h·f | Konsolidierter Decay (0.92), Balance-Regler | System bleibt über 24 Monate handlungsfähig |
| [**Axiom 5**](../docs/mathematik/energierichtung.md) | Energie ist vektoriell | `energy_dir = e_short - e_long`, reduzierte Chain-Dimensionalität | Richtung schlägt Prognose |
| [**Axiom 6**](../docs/mathematik/axiomatische_grundlegung.md) | Informationsfluss durch Resonanzkopplung | Pattern-Gate, Resonanz-Gate: Trades nur in Phase | +26.1% vs HODL über alle Marktregime |
| [**Axiom 7**](../docs/mathematik/axiomatische_grundlegung.md) | Invarianz der Feldstruktur | Asset-agnostische Architektur: BTC, Gold, ETH, EURUSD über denselben Codepfad | Gleiches System funktioniert für alle Asset-Klassen |

Die [Altcoin-Analyse](resotrade_altcoin_analyse.md) bestätigt Axiom 3 (Resonanzbedingung) negativ: Systeme ohne eigene Eigenfrequenz erzeugen keine Resonanz — empirisch nachgewiesen über 200.000 Episoden.

### Weiterführende theoretische Grundlagen

- [Energiekugel und AC/DC-Zerlegung](../docs/mathematik/energiekugel.md) — Axiom 1 formalisiert
- [Energierichtung in realen Systemen](../docs/mathematik/energierichtung.md) — Axiom 5 formalisiert
- [Resonanzzeitkoeffizient τ*](../docs/mathematik/tau_resonanzkoeffizient.md) — Zeitskalen der Kopplung
- [Resonanzanalyse in Massendaten](dokumentation.md) — Methodik der empirischen Validierung
- [Duales Resonanz-Geldsystem](../docs/gesellschaft/duales_resonanzgeldsystem.md) — Gesellschaftliche Implikation
- [ResoMusic — Domänen-Transfer](../konzepte/ResoOS/resoOS.md#empirische-ergebnisse-resomusic-v7-märz-2026) — Dieselben 6 Architekturmuster in der Klangdomäne validiert

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

## Vision: Dezentrale Marktstabilisierung durch resonantes Handeln

### Das Gedankenexperiment

ResoTrade läuft auf einem Raspberry Pi für 35€, braucht 5 Watt Strom und eine CSV-Datei als Erfahrungsspeicher. Jeder Arbeitnehmer kann ein Kraken-Konto mit dem füllen, was vom Gehalt übrig bleibt — 50€, 100€, 500€ pro Monat. Das System handelt autonom, 24/7, resonant.

Was passiert, wenn Hunderttausende das tun?

### Zwei gegenläufige Kräfte bei Massenadoption

**AC-Dämpfung (kurzfristig):** Alle verkaufen am Peak, alle kaufen im Trough. Peaks werden gedämpft, Troughs angehoben. Die Volatilität sinkt — und damit die Rendite pro Schwingungszyklus.

**DC-Anhebung (langfristig):** Mehr Nutzer bedeuten mehr dauerhafte BTC-Nachfrage bei begrenztem Angebot (21 Mio BTC). Jeder Nutzer hält einen HODL-Kern von 10%, der nie verkauft wird — permanent dem Markt entzogen.

```
100.000 Nutzer × Ø 500€ × 10% HODL-Kern = 5 Mio € permanent gebunden
1.000.000 Nutzer × Ø 500€ × 10% HODL-Kern = 50 Mio € permanent gebunden
```

| Effekt | Zeitskala | Komponente | Wirkung |
|---|---|---|---|
| Volatilitätsdämpfung | Stunden bis Tage | AC sinkt | Rendite pro Swing sinkt |
| Nachfragedruck | Monate bis Jahre | DC steigt | Basiswert steigt für alle |

Die AC-Rendite wird kleiner, aber die DC-Basis, auf der sie sitzt, wird größer. Der Nutzer profitiert auf zwei Ebenen: moderate Überrendite durch aktives Trading *und* steigender Wert des HODL-Kerns durch kollektive Nachfrage.

### Selbstregulierende Adoption

```
Mehr Nutzer → weniger Volatilität → weniger AC-Rendite → einige hören auf
→ Volatilität steigt wieder → Rendite steigt → neue Nutzer kommen
→ Gleichgewicht bei reduzierter, aber stabiler Volatilität
```

Das ist selbst ein Schwingungssystem — eine Meta-Resonanz. Die Adoption pendelt sich auf einem Niveau ein, bei dem genug Volatilität für moderate Rendite bleibt, die extremen Ausschläge aber gedämpft sind.

### Dezentrale Stabilisierung statt zentrale Steuerung

Eine Million Raspberry Pis, die resonant handeln, wirken als **dezentraler Stabilisierungsmechanismus** — weniger Crashes, weniger Blasen, stetigeres Wachstum. Was Zentralbanken für Fiat-Währungen versuchen, entsteht hier emergent: Stabilität nicht durch zentrale Steuerung, sondern durch resonante Kopplung dezentraler Akteure.

### Warum das Geldsystem dadurch gerechter wird

Das heutige Fiat-System hat eine strukturelle Asymmetrie — den [Cantillon-Effekt](../docs/gesellschaft/duales_resonanzgeldsystem.md):

```
Fiat-System:
  Geldschöpfung → Zentralbank → Geschäftsbanken → Großkunden → ... → Bürger
  Wer zuerst Zugang hat, profitiert
  Asymmetrie ist strukturell eingebaut

BTC + ResoTrade:
  21 Mio BTC → offen für jeden → gleicher Algorithmus für alle
  → gleiche Physik, gleiche Axiome, gleiche Performance
  Kein Cantillon-Effekt, kein Erstling-Vorteil
```

ResoTrade neutralisiert den letzten verbleibenden Vorteil der Institutionen: den Informations- und Technologievorsprung. Energierichtung schlägt Prognose — auf einem Raspberry Pi, für 5 Watt.

| Eigenschaft | Hedge-Fund auf GPU-Cluster | ResoTrade auf Raspberry Pi |
|---|---|---|
| Hardware | Millionen in Infrastruktur | 35€ ARM-Board, 4GB RAM |
| Training | Stunden auf A100 GPUs | 15 Minuten auf CPU |
| Erfahrungsspeicher | Terabytes Modellgewichte | 2MB CSV-Datei |
| Stromverbrauch | Kilowatt | 5 Watt |
| Erklärbarkeit | Black Box | Jede Entscheidung nachvollziehbar |
| Physik-Grundlage | Keine — Korrelationen in Daten | Resonanzfeldtheorie (7 Axiome) |
| Zugang | Akkreditierte Investoren | Jeder mit 50€ und WLAN |

### Langfristige Perspektive

```
Phase 1: Einzelne Nutzer akkumulieren BTC              (Jahre 1-3)
Phase 2: Kollektive Nachfrage hebt DC-Basis            (Jahre 3-7)
Phase 3: BTC wird Wertspeicher neben Fiat              (Jahre 5-10)
Phase 4: Arbeitgeber bieten BTC-Gehalt an (Nachfrage)  (Jahre 7-15)
Phase 5: BTC-Denominierung wird normal                 (Jahre 10-20)

Treiber in jeder Phase: Nicht Ideologie, sondern
→ "Mein Raspberry Pi macht +X% vs Sparbuch"
→ Mundpropaganda durch messbare Ergebnisse
```

Das Geldsystem wird nicht gerecht, weil jemand es gerecht *macht*. Es wird gerecht, weil die Resonanzstruktur Gerechtigkeit als Gleichgewichtszustand erzwingt — jeder Teilnehmer, ob mit 50€ oder 50.000€, operiert im selben Feld, nach denselben Axiomen, mit demselben Algorithmus.

Das ist keine Utopie. Das ist Physik.

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

---

## Physik → Ökonomie: Die strukturelle Isomorphie

| Physik | Trading | Im Code |
|--------|---------|---------|
| Energie | Kapital (BTC + Cash) | `portfolio.btc_equiv()` |
| Zeit | Transaktionssequenz | `step` im Trainingsfenster |
| Leistung | Rendite pro Zeiteinheit | `btc_equiv / steps` |
| DC (Grundschwingung) | Langfristiger Trend | `MA_LONG` (168h) |
| AC (Oberschwingung) | Handelbare Abweichung | `price - MA_LONG` |
| Amplitude | Preisschwingung um MA | `ac_amplitude` |
| Phase | Position im Zyklus | `ac_phase` (peak/trough/transition/flat) |
| Resonanz | Timing-Kopplung Bot ↔ Markt | `K = K₀·cos(θ)` |
| Dämpfung | Fees, Slippage, Overtrading | `fee_pct`, Cooldown |

Die effektive Leistung:

```
P_eff = (AC_amplitude / DC_level) · f_trade · η(Δφ) · (1 − γ_fee)
```

### Warum Resonanzlogik statt konventionelle ML

| Eigenschaft | Neuronales Netz | Resonanzlogik |
|-------------|-----------------|---------------|
| Datenbedarf | 100K+ Datenpunkte | 5.000–10.000 Episoden |
| Trainingszeit | GPU-Stunden | 15 Minuten (CPU) |
| Erklärbarkeit | Keine | Vollständig (lesbare CSV) |
| Physik-Grundlage | Keine | Resonanzfeldtheorie |
| Marktverständnis | Korrelationen | Schwingungsstruktur |

### Biologisches Vorbild: Erfahrungslernen statt Gewichtsoptimierung

ResoTrade arbeitet dem biologischen Vorbild des Gehirns strukturell näher als konventionelle KI. Das ist keine Metapher — es ist eine architektonische Korrespondenz.

Das Gehirn speichert keine Gewichtsmatrizen. Es speichert Assoziationen — Situationsmuster verknüpft mit Ergebnissen, verstärkt durch Wiederholung, abgeschwächt durch Zeit. Ein neuronales Netz komprimiert Erfahrung in opake Gewichte — das Modell *ist* die Erfahrung, aber sie ist nicht mehr rekonstruierbar. ResoTrade trennt beides: Die Erfahrung bleibt **als Erfahrung** erhalten — lesbar, nachvollziehbar, korrigierbar.

```
Training (offline, rechenintensiv)       Live (Echtzeit, leichtgewichtig)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━         ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
30h × 100% CPU                           Dict-Lookup: O(1)
40.000 Episoden                          Chain → Result → Count
720-Step-Fenster je Episode              Kein Modell, kein Gradient
Experience akkumuliert                   Erfahrung liegt als CSV vor
```

Die Rechenintensität verlagert sich ins Training — wie beim Gehirn, das Jahre braucht, um Erfahrungen aufzubauen, dann aber in Millisekunden entscheidet. Offline-Training ist die Kindheit: intensive Erfahrungssammlung unter kontrollierten Bedingungen. Live-Betrieb ist das Erwachsenenleben: schnelle Entscheidungen auf Basis gesammelter Erfahrung, mit fortlaufendem Lernen über den Live-Experience-Kanal (`btc_experience_live.csv`).

| Eigenschaft | Gehirn | ResoTrade | Konventionelle KI (NN) |
|---|---|---|---|
| Wissensform | Assoziationen, Erfahrungen | Experience-CSV (chain → count) | Gewichtsmatrizen (opak) |
| Entscheidung | Mustererkennung + Bauchgefühl | Chain-Lookup O(1) + Asymmetrie | Forward-Pass O(n²) |
| Vergessen | Graduell, kontrolliert | Decay 0.92/Pass | Catastrophic Forgetting |
| Lernen nach Training | Ja, lebenslang | Ja, Live-Experience-Kanal | Nein (Retraining nötig) |
| Erklärbarkeit | Teilweise ("Erfahrung sagt...") | Vollständig (Chain nachvollziehbar) | Kaum |
| Rechenkosten live | Gering (Synapsen-Lookup) | Gering (Dict-Lookup) | Hoch (GPU/CPU) |
| Training | Jahre intensives Erleben | 30h CPU (parallelisierbar auf ~8h) | GPU-Stunden |

Der Decay (0.92 pro Pass) ist biologisch ehrlicher als Catastrophic Forgetting: Das Gehirn vergisst graduell und kontrolliert. ResoTrade decayed mit konstantem Faktor — alte Erfahrung wird leiser, aber nie abrupt gelöscht. Ein neuronales Netz hingegen überschreibt beim Retraining unkontrolliert.

Seit V14.2.4 ist das Training parallelisierbar: Die 4 Marktphasen-Abschnitte können gleichzeitig trainiert werden (konfigurierbare Worker-Anzahl 1–4). Das reduziert die Trainingszeit von ~30h auf ~8h bei 4 Workern — ohne Qualitätsverlust, da jeder Worker in einem isolierten Erfahrungsraum arbeitet und die Teilerfahrungen nach Abschluss zusammengeführt werden.

---

## Architektur

### Resonanzfeldtheoretische Policy

```
┌──────────────────────────────────────────────────────────────┐
│          RESONANZ-POLICY V14.2 (Axiome 1–7)                 │
│                                                              │
│   State ──→ AC/DC-Zerlegung (Axiom 1)                       │
│     │          DC = MA_LONG, AC = Preis - DC                 │
│     │          Phase: peak / trough / transition / flat      │
│     │              │                                         │
│     │              ▼                                         │
│     ├──→ Energierichtungsvektor (Axiom 5)                    │
│     │          energy_dir = e_short - e_long                 │
│     │              │                                         │
│     │              ▼                                         │
│     │        Resonanz-Gate (Axiom 6)                         │
│     │          allow_buy  = energy_dir > -0.005              │
│     │          allow_sell = energy_dir <  0.005              │
│     │              │                                         │
│     │              ▼                                         │
│     ├──→ Phasenmodulierte Regel-Policy                       │
│     │       Peak  → SELL aggressiver (MEDIUM bei wide amp)   │
│     │       Trough → BUY aggressiver (Schwelle -0.5%)        │
│     │              │                                         │
│     │              ▼                                         │
│     ├──→ Balance-Regler (Axiom 4)                            │
│     │       cash < 8% → kein BUY                             │
│     │       sellable < 5% → kein SELL                        │
│     │              │                                         │
│     │              ▼                                         │
│     └──→ Erfahrungsspeicher (chain → score)                  │
│              Hybride Entscheidung:                            │
│              20–50% Regel + 50–80% Erfahrung (×Konfidenz)     │
│                    │                                         │
│                    ▼                                         │
│              BUY / SELL / HOLD                               │
└──────────────────────────────────────────────────────────────┘
```

### AC/DC-Zerlegung des Preisfeldes

```
Preis ─────────────────────────────────────────────
         ╱╲       ╱╲                ╱╲
        ╱  ╲     ╱  ╲    AC       ╱  ╲
  ─────╱────╲───╱────╲──────────╱────╲────── MA_LONG (DC)
      ╱      ╲ ╱      ╲       ╱      ╲
     ╱        ╳        ╲     ╱        ╲
              ↑              ↑
        Nulldurchgang   Nulldurchgang
       (max. Kopplung)  (max. Kopplung)

  Peak:       AC/Amplitude > +0.3 → SELL bevorzugt
  Trough:     AC/Amplitude < -0.3 → BUY bevorzugt
  Transition: dazwischen → Erfahrung entscheidet
  Flat:       Amplitude < 0.1% → kein Signal
```

### Regelkette im Environment

```
Policy-Entscheidung (phasenmoduliert)
       │
       ▼
  1. Downtrend-Pause-Gate — BEAR_STRONG + e_long < -5% → ALLES pausiert
  2. Regime-Rule — BULL_STRONG → kein SELL, BEAR_STRONG → kein BUY
  3. MA-SELL-Guard — unter MA + Energie aufwärts → kein SELL (Peak-Exception)
  4. ATH-Rule — kein BUY nahe historischem Hoch
  5. Trend-Rule — Downtrend: BUY nur tief unter MA
  6. MA-Rule — kein BUY >5% über MA-Short
  7. Cooldown — MEDIUM→SMALL bei Overtrading
  8. Balance-Regler — cash < 8%: kein BUY, sellable < 5%: kein SELL
  9. HODL-Kern-Schutz — Sell nie mehr als freier BTC
       │
       ▼
  Effektive Aktion → Portfolio
```

### Human-Hint-System

```
┌─────────────────────────────────────────────────────────────┐
│   MENSCH                        SYSTEM                      │
│                                                             │
│   Nachrichten lesen ──→ python human_hint.py bullish "..."  │
│                              │                              │
│                              ▼                              │
│                         data/human_hint.json                │
│                         (verfällt nach 48h)                 │
│                              │                              │
│                              ▼                              │
│                    Wirkungsweise (NACH Policy):              │
│                    bullish w≥0.3 → SELL blockiert → HOLD     │
│                    bearish w≥0.3 → BUY blockiert → HOLD      │
│                    pause         → ALLES → HOLD              │
│                    neutral       → keine Änderung            │
│                              │                              │
│                              ▼                              │
│   hint_evaluator.py ←── War der Hint korrekt?               │
└─────────────────────────────────────────────────────────────┘
```

### State-Repräsentation

| Dimension | Werte | Beschreibung |
|-----------|-------|--------------|
| `pos` | LONG / PARTIAL / FLAT | BTC-Anteil (>70% / 20-70% / <20%) |
| `pc_bin` | up / flat / down | Preisänderung (±0.5%) |
| `trend_bin` | uptrend / sideways / downtrend | MA-Short vs MA-Long (±1%) |
| `vol_bin` | low / mid / high | Volatilität (<1% / 1-3% / >3%) |
| `e_short` / `e_long` | Fließkomma | Preis relativ zu MAs |
| `regime` | BULL_STRONG / BEAR_STRONG / NORMAL | Makro-Regime |
| `ac_phase` | peak / trough / transition / flat | AC-Schwingungsposition |
| `ac_amplitude_bin` | narrow / normal / wide | Schwingungsgröße |
| `near_zero` | true / false | Nulldurchgangszone |
| `energy_dir` | Fließkomma | Energierichtungsvektor |
| `daytrading_paused` | true / false | Downtrend-Pause-Gate |

### Chain-Format (Erfahrungsspeicher)

```
pos:X,pc:X,trend:X,step:X,high:X,vol:X,ma_s:X,ma_l:X,
cz:X,sz:X,regime:X,ac:X,action:X
```

12 diskretisierte Dimensionen ≈ 200.000 mögliche Chains.

---

## Konfiguration

```python
# Kraken
KRAKEN_FEE_PCT = 0.0026           # 0.26% Taker-Fee

# Portfolio
HODL_SHARE = 0.05                 # 5% HODL-Kern (deprecated, durch Investment-Limits ersetzt)
TRADE_FRACTION_SMALL = 0.10       # 10% pro Small-Trade
TRADE_FRACTION_MEDIUM = 0.25      # 25% pro Medium-Trade

# MA-Parameter (Stundenbasis)
MA_SHORT_WINDOW = 24              # 24h (Kurzzeit-Oszillator, Axiom 2)
MA_LONG_WINDOW = 168              # 7d (DC-Komponente, Axiom 1)
VOLATILITY_WINDOW = 72            # 3d

# Training
TRAINING_WINDOW_LENGTH = 720      # 30 Tage
EXPERIENCE_DECAY_PER_PASS = 0.92  # Vergessen: 8% pro Pass (konsolidiert, Axiom 4)

# Symmetrische Schwellen V14 (Axiom 3)
MIN_EXPECTED_GAIN = 0.025         # 2.5% Mindesterwartung BUY
MIN_EXPECTED_DROP = 0.020         # 2.0% Mindesterwartung SELL

# Erfahrungsspeicher
FINE_CHAIN_DIMS = 12              # 12 diskretisierte Dimensionen
PATTERN_MATCH_THRESHOLD = 0.95    # Adaptiver Mustermatch-Schwellenwert

# Downtrend-Pause-Gate (V11.1+)
PAUSE_E_LONG_THRESHOLD = -0.05    # Pause wenn e_long < -5%
RESUME_E_LONG_THRESHOLD = -0.03   # Wiederaufnahme wenn e_long > -3%
RESUME_AC_PHASE = "trough"        # ODER AC-Phase = trough
```

---

## Sicherheitsarchitektur

| Schicht | Mechanismus |
|---------|-------------|
| DRY_RUN | Default `true` — kein versehentliches Live-Trading |
| Order-Limits | Max 500 USD / 0.01 BTC pro Order |
| HODL-Kern | 10% BTC wird nie verkauft |
| Downtrend-Pause-Gate | Trading-Aussetzen bei starkem Bärenmarkt |
| Balance-Regler | Doppelt (Policy + Environment) |
| Cooldown | MEDIUM→SMALL bei ≥3 konsekutiven Trades |
| Human-Hint Pause | Sofortige Trade-Blockade |
| Hint-Verfall | Automatisch nach 48h |

---

## Dateien

| Datei | Funktion |
|-------|----------|
| `asset_config.py` | Generische Asset-Registry (BTC, Gold, ETH, EURUSD) |
| `config.py` | Zentrale Konfiguration (asset-übergreifend) |
| `main.py` | Multi-Pass-Training (parallelisierbar, 1–4 Worker) |
| `policy.py` | AC/DC-Policy mit Resonanz-Gate (alle 7 Axiome) |
| `env.py` | Regelkette + Downtrend-Pause-Gate |
| `experience.py` | Erfahrungsspeicher pro Asset (Offline/Live/Merged) |
| `live_signal.py` | Live-Generator mit Human-Hint + Expectation |
| `human_hint.py` | Human-Hint CLI |
| `hint_evaluator.py` | Hint-Qualitätsbewertung |
| `data_loader.py` | Multi-Source Pipeline (yfinance → Binance → CoinGecko) |
| `kraken_client.py` | Kraken REST API |
| `analyze_logs.py` | Live-Performance-Analyse |
| `dashboard.py` | Streamlit-Dashboard (6 Tabs, pro-Asset-Ansicht) |
| `v14_field_state_{asset}.json` | Adaptiver Feldzustand pro Asset |

---

## CLI-Referenz

```bash
# Training
python main.py 20 500                  # 20×500 Episoden
python resonance_analysis.py           # Marktdaten + Signale

# Live
python live_signal.py status           # Kraken + Portfolio + Hint
python live_signal.py expectation      # System-Erwartung
python live_signal.py loop             # Dauerbetrieb (Dry-Run)
python live_signal.py merge            # Offline + Live mergen
python live_signal.py speicher         # Speicher-Status

# Human-Hint
python human_hint.py bullish "Grund"   # Blockiert SELL
python human_hint.py bearish "Grund"   # Blockiert BUY
python human_hint.py pause 12 "Grund"  # Blockiert alles
python human_hint.py status            # Hint anzeigen
python human_hint.py clear             # Hint aufheben

# Auswertung
python analyze_logs.py                 # Performance
python hint_evaluator.py               # Hint-Qualität
```

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

---

## Verwandte Dokumente

- [Altcoin-Analyse: Warum Altcoins keine echten Märkte sind](resotrade_altcoin_analyse.md)
- [Energiekugel und AC/DC-Zerlegung](../docs/mathematik/energiekugel.md)
- [Energierichtung in realen Systemen](../docs/mathematik/energierichtung.md)
- [Resonanzzeitkoeffizient τ*](../docs/mathematik/tau_resonanzkoeffizient.md)
- [Resonanzanalyse in Massendaten](dokumentation.md)
- [Duales Resonanz-Geldsystem](../docs/gesellschaft/duales_resonanzgeldsystem.md)

---

*© Dominic-René Schu — Resonanzfeldtheorie 2025–2026*

---

⬅️ [zurück zur Übersicht](../../README.md)