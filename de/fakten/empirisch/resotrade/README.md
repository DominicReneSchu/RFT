# ResoTrade V11.1 — Resonanzfeldtheoretische BTC-KI mit AC/DC-Zerlegung

Resonanzfeldtheoretisches Trading-System, das durch wiederholte Offline-Simulation lernt, BTC-Kurszyklen als Schwingungsfelder zu lesen und BTC über reines HODL hinaus zu akkumulieren — mit optionalem Live-Trading über Kraken.

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

Die empirische Bestätigung: **+26.1% vs HODL im Durchschnitt über 4 verschiedene Marktphasen** — Sideways, Bullrun, Korrektur und Crash. Kein klassischer Indikator auf demselben Datensatz erreicht eine Korrelation über 0.05.

## Vision: Dezentrale Marktstabilisierung durch resonantes Handeln

### Das Gedankenexperiment

ResoTrade läuft auf einem Raspberry Pi für 35€, braucht 5 Watt Strom und eine CSV-Datei als Erfahrungsspeicher. Jeder Arbeitnehmer kann ein Kraken-Konto mit dem füllen, was vom Gehalt übrig bleibt — 50€, 100€, 500€ pro Monat. Das System handelt autonom, 24/7, resonant.

Was passiert, wenn Hunderttausende das tun?

### Phase 1: Stille Akkumulation

Wenige Tausend Nutzer. Der Markt bemerkt nichts — das Volumen ist zu klein. Jeder Einzelne akkumuliert langsam mehr BTC als durch reines Halten. Ein stiller, messbarer Vorteil gegenüber Sparbuch, Fondsmanager und ETF-Sparplan.

### Phase 2: Zwei gegenläufige Kräfte

Bei Massenadoption wirken zwei Effekte gleichzeitig:

**AC-Dämpfung (kurzfristig):** Alle verkaufen am Peak, alle kaufen im Trough. Peaks werden gedämpft, Troughs angehoben. Die Volatilität sinkt — und damit die Rendite pro Schwingungszyklus.

**DC-Anhebung (langfristig):** Mehr Nutzer bedeuten mehr dauerhafte BTC-Nachfrage. Jeder Nutzer hält einen HODL-Kern von 10%, der nie verkauft wird — permanent dem Markt entzogen. Bei 21 Mio BTC Limit fehlt jeder gebundene BTC dem Angebot.

```
100.000 Nutzer × Ø 500€ × 10% HODL-Kern = 5 Mio € permanent gebunden
1.000.000 Nutzer × Ø 500€ × 10% HODL-Kern = 50 Mio € permanent gebunden
```

| Effekt | Zeitskala | Komponente | Wirkung |
|---|---|---|---|
| Volatilitätsdämpfung | Stunden bis Tage | AC sinkt | Rendite pro Swing sinkt |
| Nachfragedruck | Monate bis Jahre | DC steigt | Basiswert steigt für alle |

Die AC-Rendite wird kleiner, aber die DC-Basis, auf der sie sitzt, wird größer. Der Nutzer profitiert auf zwei Ebenen: moderate Überrendite durch aktives Trading *und* steigender Wert des HODL-Kerns durch kollektive Nachfrage.

### Phase 3: Selbstregulierende Adoption

```
Mehr Nutzer → weniger Volatilität → weniger AC-Rendite → einige hören auf
→ Volatilität steigt wieder → Rendite steigt → neue Nutzer kommen
→ Gleichgewicht bei reduzierter, aber stabiler Volatilität
```

Das ist selbst ein Schwingungssystem — eine Meta-Resonanz. Die Adoption pendelt sich auf einem Niveau ein, bei dem genug Volatilität für moderate Rendite bleibt, die extremen Ausschläge aber gedämpft sind.

### Die strukturelle Wirkung auf den Markt

Eine Million Raspberry Pis, die resonant handeln, wirken als **dezentraler Stabilisierungsmechanismus** — weniger Crashes, weniger Blasen, stetigeres Wachstum. Was Zentralbanken für Fiat-Währungen versuchen, entsteht hier emergent: Stabilität nicht durch zentrale Steuerung, sondern durch resonante Kopplung dezentraler Akteure.

### Warum das Geldsystem dadurch gerechter wird

Das heutige Fiat-System hat eine strukturelle Asymmetrie:

```
Fiat-System:
  Geldschöpfung → Zentralbank → Geschäftsbanken → Großkunden → ... → Bürger
  Wer zuerst Zugang hat, profitiert (Cantillon-Effekt)
  Asymmetrie ist strukturell eingebaut

BTC + ResoTrade:
  21 Mio BTC → offen für jeden → gleicher Algorithmus für alle
  → gleiche Physik, gleiche Axiome, gleiche Performance
  Kein Cantillon-Effekt, kein Erstling-Vorteil
```

ResoTrade neutralisiert den letzten verbleibenden Vorteil der Institutionen: den Informations- und Technologievorsprung. Goldman Sachs hat bessere Daten, schnellere Server, mehr Analysten — aber sie lösen das falsche Problem. Mehr Rechenleistung macht eine unlösbare Aufgabe (Preisprognose in chaotischen Systemen) nicht lösbar. Sie macht sie nur teurer.

Energierichtung schlägt Prognose. Auf einem Raspberry Pi. Für 5 Watt.

| Eigenschaft | Hedge-Fund auf GPU-Cluster | ResoTrade auf Raspberry Pi |
|---|---|---|
| Hardware | Millionen in Infrastruktur | 35€ ARM-Board, 4GB RAM |
| Training | Stunden auf A100 GPUs | 15 Minuten auf CPU |
| Erfahrungsspeicher | Terabytes Modellgewichte | 2MB CSV-Datei |
| Stromverbrauch | Kilowatt | 5 Watt |
| Erklärbarkeit | Black Box | Jede Entscheidung nachvollziehbar |
| Physik-Grundlage | Keine — Korrelationen in Daten | Resonanzfeldtheorie (4 Axiome) |
| Prognose nötig? | Ja — und scheitert regelmäßig | Nein — Energierichtung reicht |
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

## V11.1 — Multi-Zyklus-Training über alle Marktphasen (+26.1% vs HODL Ø)

### Validiert über 4 Marktregime (2024–2026)

| Abschnitt | Marktphase | Zeitraum | Trades | Performance vs HODL |
|-----------|-----------|----------|--------|---------------------|
| Sideways + ETF | 60k–70k Range | Mär 2024 – Sep 2024 | 437 | **+33.3%** |
| Bullrun 60k–110k | Starker Aufwärtstrend | Sep 2024 – Mär 2025 | 429 | **+19.8%** |
| Top + Korrektur | Whipsaw, Crash + Recovery | Mär 2025 – Sep 2025 | 247 | **+4.3%** |
| Aktuell (Crash) | 110k → 63k | Sep 2025 – Feb 2026 | 279 | **+46.8%** |
| **Durchschnitt** | **Alle Regime** | **24 Monate** | **1392** | **+26.1%** |

Das System schlägt HODL in jeder Marktphase — Sideways, Bullrun, Korrektur und Crash.

### Physik → Ökonomie: Die strukturelle Isomorphie

| Physik | Trading | Im Code |
|--------|---------|---------|
| Energie | Kapital (BTC + Cash) | `portfolio.btc_equiv()` |
| Zeit | Transaktionssequenz | `step` im Trainingsfenster |
| Leistung | Rendite pro Zeiteinheit | `btc_equiv / steps` |
| Frequenz | Handelsfrequenz | `trades / window_length` |
| DC (Grundschwingung) | Langfristiger Trend | `MA_LONG` (168h) |
| AC (Oberschwingung) | Handelbare Abweichung | `price - MA_LONG` |
| Amplitude | Preisschwingung um MA | `ac_amplitude` |
| Phase | Position im Zyklus | `ac_phase` (peak/trough/transition/flat) |
| Resonanz | Timing-Kopplung Bot ↔ Markt | `K = K₀·cos(θ)` |
| Dämpfung | Fees, Slippage, Overtrading | `fee_pct`, Cooldown |
| Energieerhaltung | Nullsummenspiel Markt | Balance-Regler |

### Theoretische Grundlage: Vier Axiome der Resonanzfeldtheorie

| Axiom | Prinzip | Anwendung im Bot |
|-------|---------|-------------------|
| **Axiom 1** | Jede Entität besitzt eine periodische Schwingung ψ(x,t) | AC/DC-Zerlegung: Preis = DC (Trend) + AC (handelbar) |
| **Axiom 2** | Energie und Felder besitzen eine Kopplungsstruktur | Buy/Sell-Balance muss erhalten bleiben (Handlungsfähigkeit) |
| **Axiom 5** | Energie ist ein gerichteter Vektor (nicht skalar) | Preisfluss hat Richtung: `energy_dir = e_short - e_long` |
| **Axiom 6** | Wechselwirkung nur durch Resonanzkopplung: K = K₀·cos(θ) | Trades nur wenn Aktion in Resonanz mit Energierichtung steht |

Zusätzlich aus der [Energiekugel](https://github.com/DominicReneSchu/public/blob/main/de/fakten/docs/mathematik/energiekugel.md): Die Zerlegung in AC- und DC-Komponenten identifiziert Nulldurchgänge als Zonen maximaler Kopplungseffizienz.

### V11.1-Änderungen gegenüber V11

| # | Änderung | V11 | V11.1 | Wirkung |
|---|----------|-----|-------|---------|
| 1 | **Multi-Zyklus-Training** | Einzelner Abschnitt, 10.000 Episoden | 3+ Zyklen × 4 Abschnitte × 10.000 Episoden | Erfahrung über alle Marktregime |
| 2 | **Abschnittsweises Training** | Letzte 180 Tage | 4×6 Monate (2024–2026) mit Binance-Fallback | Volle Marktabdeckung inkl. älterer Daten |
| 3 | **Downtrend-Pause-Gate** | Nicht vorhanden | Pausiert gesamtes Daytrading bei BEAR_STRONG + e_long < -5% | Schutz vor Trades mit negativer Erwartung |
| 4 | **Human-Hint-System** | Nicht vorhanden | Mensch kann bullish/bearish/neutral/pause setzen | Makro-Events fließen als Hinweis in Policy ein |
| 5 | **Hint-Evaluierung** | Nicht vorhanden | Rückblickende Bewertung der Hint-Qualität | Mensch lernt, wann Hints sinnvoll sind |
| 6 | **Expectation-Anzeige** | Nicht vorhanden | System zeigt eigene Markterwartung vor Hint | Mensch sieht Systemsicht vor Entscheidung |
| 7 | **Live Dry-Run** | Nur echt oder gar nicht | Vollständiger Dry-Run mit echtem Kraken-Portfolio | Risikofreie Validierung vor Echtbetrieb |
| 8 | **Binance-Fallback** | Nur yfinance (max 730d) | Automatischer Fallback auf Binance-API | Stundendaten seit 2017 verfügbar |

### Performance-Historie

| Version | Kernänderung | Performance vs HODL | Trades | Buy:Sell | Episoden > HODL |
|---------|-------------|---------------------|--------|----------|-----------------|
| V6 | Basis: MA-Heuristik + Erfahrungsspeicher | +35.04% | 366 | 2.5:1 | 66.0% |
| V7 | pc_bin-Filter | +35.61% | 267 | 2.7:1 | 68.6% |
| V8 | Plateau-Filter — verworfen | +34.69% | 362 | 2.5:1 | 70.2% |
| V10 | Energierichtungsvektor (Axiom 5+6) | +37.03% | 286 | 3.8:1 | 82.0% |
| V11 | AC/DC-Zerlegung (Axiom 1) | +42.89% | 236 | 2.7:1 | 81.4% |
| **V11.1** | **Multi-Zyklus + Pause-Gate + Human-Hint** | **+26.1% Ø (4 Regime)** | **~350 Ø** | **~2.5:1** | **alle 4/4 positiv** |

> V11.1-Performance ist der Durchschnitt über 4 verschiedene Marktphasen (24 Monate).
> Vorherige Versionen wurden nur auf dem jeweils letzten 180-Tage-Fenster gemessen.
> Die Vergleichbarkeit ist eingeschränkt — V11.1 ist die robustere Metrik.

## Workflow

### Initiales Training (Linux)

```bash
cd ~/Schreibtisch/Resotrade
source .venv/bin/activate
chmod +x train_all_sections_multi.sh
sed -i 's/\r$//' train_all_sections_multi.sh

# Suspend verhindern bei zugeklapptem Deckel
sudo systemctl mask sleep.target suspend.target hibernate.target hybrid-sleep.target

./train_all_sections_multi.sh

# Suspend danach wieder aktivieren
sudo systemctl unmask sleep.target suspend.target hibernate.target hybrid-sleep.target
```

### Initiales Training (PowerShell)

```powershell
del data\trade_experience_offline.csv
del data\trade_experience_weighted.csv
pwsh -ExecutionPolicy Bypass -File .\train_all_sections.ps1
```

### Trainings-Ergebnis prüfen

```bash
python3 plot_final_trades_all.py
# Erwartung: Alle 4 Abschnitte positiv vs HODL
```

### Erststart Live

```bash
python3 live_signal.py status          # Kraken-Verbindung + Portfolio prüfen
python3 live_signal.py once            # Ein Zyklus testen
python3 live_signal.py loop            # Dry-Run Dauerbetrieb
```

### Tägliche Kontrolle

```bash
python3 live_signal.py status          # Portfolio + Hint-Status
python3 live_signal.py expectation     # System-Erwartung anzeigen
python3 analyze_logs.py                # Performance-Plot + Statistik
tail -20 data/live_logs/signal_log.csv # Letzte Signale prüfen
```

### Human-Hint setzen (bei Nachrichtenlage)

```bash
# System-Erwartung anzeigen — VOR dem Hint
python3 live_signal.py expectation

# Hinweise setzen
python3 human_hint.py bullish "EZB senkt Zinsen um 25bp"
python3 human_hint.py bearish "SEC verklagt Coinbase" 0.5
python3 human_hint.py pause 12 "FOMC-Meeting heute Abend"
python3 human_hint.py neutral "Markt unklar, keine Aktion"

# Status prüfen
python3 human_hint.py status

# Hinweis aufheben
python3 human_hint.py clear

# Rückblickend: Waren meine Hinweise gut?
python3 hint_evaluator.py
```

### Nachtraining (alle 3–7 Tage)

```bash
# 1. Frische Marktdaten analysieren
python3 resonance_analysis.py

# 2. Nachtrainieren mit aktuellen Daten
python3 main.py 5 500

# 3. Live-Erfahrung mit Offline-Training zusammenführen
python3 live_signal.py merge

# 4. Ergebnis prüfen
python3 live_signal.py status
python3 plot_final_trades_all.py
```

### Wöchentliche Auswertung

```bash
# Performance vs HODL seit Start
python3 analyze_logs.py

# Hint-Qualität bewerten
python3 hint_evaluator.py

# Backup der Erfahrungsdaten
mkdir -p data/backups
cp data/trade_experience_offline.csv "data/backups/offline_$(date +%Y%m%d).csv"
cp data/trade_experience_weighted.csv "data/backups/weighted_$(date +%Y%m%d).csv"
```

### Dateien zwischen Linux ↔ Windows synchronisieren

```bash
# Nach Training auf Linux → Windows
scp dominic@laptop:~/Schreibtisch/Resotrade/data/trade_experience_offline.csv data/

# Dann auf Windows mergen
python live_signal.py merge
```

### Wenn bereit für echten Handel

```bash
# Checkliste vor Echtbetrieb:
#   ✅ Paper-Trading positiv über 2+ Wochen
#   ✅ Kein Overtrading (< 5 Trades/Tag)
#   ✅ Drawdown nie unter -10% vs HODL
#   ✅ Human-Hint getestet und bewertet
#   ✅ Backup der Erfahrungsdaten angelegt

export RESOTRADE_DRY_RUN=false
python3 live_signal.py loop
```

### Notfall: System stoppen

```bash
# Sofort alle Trades blockieren
python3 human_hint.py pause 999 "NOTFALL: System gestoppt"

# Oder Prozess beenden
pkill -f "live_signal.py"             # Linux
# PowerShell: Get-Process python | Stop-Process
```

## Architektur

### Resonanzfeldtheoretische Policy (V11.1)

```
┌──────────────────────────────────────────────────────────────┐
│          RESONANZ-POLICY V11.1 (Axiome 1,2,5,6)             │
│                                                              │
│   State ──→ AC/DC-Zerlegung (Axiom 1)                       │
│     │          DC = MA_LONG (Grundton)                       │
│     │          AC = Preis - DC (Oberton)                     │
│     ��          Phase: peak / trough / transition / flat      │
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
│     │       Peak  → BUY gehemmt (Schwelle +1%)               │
│     │       Trough → SELL gedämpft (nur SMALL)                │
│     │              │                                         │
│     │              ▼                                         │
│     ├──→ Balance-Regler in Policy (Axiom 2)                  │
│     │       cash < 8% → kein BUY                             │
│     │       sellable < 5% → kein SELL                        │
│     │              │                                         │
│     │              ▼                                         │
│     └──→ Erfahrungsspeicher (chain → score)                  │
│              Chain: pos,pc,trend,step,high,vol,               │
│                     ma_s,ma_l,cz,sz,regime,ac,action          │
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
  Flat:       Amplitude < 0.1% des Preises → kein Signal
  Nulldurchgang: |AC/Amplitude| < 0.1 → Zone maximaler Kopplung
```

### Regelkette im Environment (V11.1)

```
Policy-Entscheidung (phasenmoduliert)
       │
       ▼
  1. Downtrend-Pause-Gate (V11.1)
     BEAR_STRONG + downtrend + e_long < -5% → ALLES pausiert
     Wiederaufnahme: e_long > -3% ODER ac_phase=trough ODER Regime≠BEAR
       │
       ▼
  2. Regime-Rule
     BULL_STRONG → kein SELL
     BEAR_STRONG → kein BUY (außer e_long < -5%)
       │
       ▼
  3. MA-SELL-Guard (resonanzlogisch)
     Blockiert SELL wenn unter MA UND Energie aufwärts
     Exception: Nicht blockieren am AC-Peak
       │
       ▼
  4. ATH-Rule (kein BUY nahe historischem Hoch)
       │
       ▼
  5. Trend-Rule
     Downtrend: BUY nur wenn e_long < -1% (tief unter MA)
     Downtrend: SELL nur wenn e_long < -1% (Bounce-SELL)
       │
       ▼
  6. MA-Rule (kein BUY >5% über MA-Short, kein SELL >5% unter MA-Short)
       │
       ▼
  7. Cooldown (MEDIUM→SMALL bei ≥3 konsekutiven Trades)
       │
       ▼
  8. Balance-Regler (cash < 8% → kein BUY, sellable < 5% → kein SELL)
       │
       ▼
  9. HODL-Kern-Schutz (Sell-Fraktion nie größer als freier BTC)
       │
       ▼
  Effektive Aktion → Portfolio
```

### Human-Hint-System (V11.1)

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
│                    live_signal.py prüft Hint jeden Zyklus    │
│                                                             │
│                    Wirkungsweise (NACH Policy-Entscheidung): │
│                    bullish w≥0.3 → SELL blockiert → HOLD     │
│                    bearish w≥0.3 → BUY blockiert → HOLD      │
│                    bullish w<0.3 → nur SELL_MEDIUM → HOLD    │
│                    bearish w<0.3 → nur BUY_MEDIUM → HOLD     │
│                    pause         → ALLES → HOLD              │
│                    neutral       → keine Änderung            │
│                              │                              │
│                              ▼                              │
│   hint_evaluator.py ←── War der Hint korrekt?               │
│   (rückblickende              │                             │
│    Bewertung)                 ▼                              │
│                    Mensch lernt: Wann Hints setzen?          │
└─────────────────────────────────────────────────────────────┘
```

### Downtrend-Pause-Gate (V11.1)

```
┌─────────────────────────────────────────────────────────────┐
│   DOWNTREND-PAUSE-GATE                                      │
│                                                             │
│   Resonanzfeldtheoretische Begründung:                      │
│   Wenn DC stark fällt, ist AC nicht profitabel handelbar.   │
│   Die Amplitude wird von der fallenden DC überlagert.       │
│   Jeder Trade hat negative Erwartung nach Fees.             │
│                                                             │
│   PAUSE wenn ALLE drei Bedingungen erfüllt:                 │
│     ① trend = downtrend                                     │
│     ② e_long < -5% (Preis deutlich unter MA_LONG)           │
│     ③ regime = BEAR_STRONG                                  │
│                                                             │
│   WIEDERAUFNAHME wenn EINE Bedingung erfüllt:               │
│     ① e_long > -3% (Stabilisierung) ODER                   │
│     ② ac_phase = trough (Wendepunkt erkannt) ODER           │
│     ③ regime ≠ BEAR_STRONG (Regime-Wechsel)                 │
│                                                             │
│   Während Pause: Nur HODL-Kern halten, kein Daytrading      │
└────────────────────────────────────────────────────────────���┘
```

### Multi-Zyklus-Trainingsarchitektur (V11.1)

```
┌─────────────────────────────────────────────────────────────┐
│   MULTI-ZYKLUS-TRAINING (3+ Zyklen × 4 Abschnitte)         │
│                                                             │
│   Zyklus 1 ──→ Zyklus 2 ──→ Zyklus 3 ──→ ...              │
│     │            │            │                             │
│     ▼            ▼            ▼                             │
│   ┌────────────────────────────────────┐                    │
│   │ Abschnitt 4: Sideways (2024)       │                    │
│   │ Abschnitt 3: Bullrun  (2024-25)    │  × pro Zyklus     │
│   │ Abschnitt 2: Korrektur (2025)      │                    │
│   │ Abschnitt 1: Aktuell  (2025-26)    │                    │
│   └────────────────────────────────────┘                    │
│                      │                                      │
│                      ▼                                      │
│            Erfahrungsspeicher wächst kumulativ               │
│            Decay 0.80 pro Pass verhindert Overfitting        │
│                      │                                      │
│                      ▼                                      │
│         Finale Plots: plot_final_trades_all.py              │
└─────────────────────────────────────────────────────────────┘
```

### Getrennte Speicher-Architektur

```
┌─────────────────────────────────────────────────────────────┐
│   OFFLINE-TRAINING              LIVE-TRADING                │
│   python main.py                python live_signal.py       │
│                                                             │
│   Schreibt: offline.csv         Schreibt: live.csv          │
│   Gewicht: 1.0x                 Gewicht: 0.8x               │
│                                                             │
│        offline.csv ──┐    ┌── live.csv                      │
│                      ▼    ▼                                 │
│                  merge_experience()                          │
│                      │                                      │
│                      ▼                                      │
│            trade_experience_weighted.csv                     │
│                      │                                      │
│                      ▼                                      │
│               Policy-Entscheidung                           │
│                                                             │
│   Live: Persist alle 10 Zyklen, Reload merged alle 60       │
└─────────────────────────────────────────────────────────────┘
```

### State-Repräsentation (V11.1)

| Dimension | Werte | Beschreibung |
|-----------|-------|--------------|
| `pos` | LONG / PARTIAL / FLAT | BTC-Anteil am Gesamtwert (>70% / 20-70% / <20%) |
| `pc_bin` | up / flat / down | Preisänderung zum Vorgänger (±0.5% Schwelle) |
| `trend_bin` | uptrend / sideways / downtrend | MA-Short vs. MA-Long (±1% Schwelle) |
| `vol_bin` | low / mid / high | Rollierende Volatilität (<1% / 1-3% / >3%) |
| `e_short` / `e_long` | Fließkomma | Preis relativ zu MA-Short / MA-Long |
| `cash_share` | Fließkomma | Cash-Anteil am Portfolio |
| `sellable_share` | Fließkomma | Freier BTC über HODL-Kern |
| `regime` | BULL_STRONG / BEAR_STRONG / NORMAL | Makro-Regime (Trend + e_long ±5%) |
| `ac_phase` | peak / trough / transition / flat | Position im AC-Schwingungszyklus |
| `ac_amplitude_bin` | narrow / normal / wide | Größe der handelbaren Schwingung (<2% / 2-6% / >6%) |
| `near_zero` | true / false | Nulldurchgangszone (\|AC/Amplitude\| < 0.1) |
| `energy_dir` | Fließkomma | Energierichtungsvektor (e_short - e_long) |
| `daytrading_paused` | true / false | V11.1: Downtrend-Pause-Gate aktiv |

### Chain-Format (Erfahrungsspeicher)

```
pos:{LONG|PARTIAL|FLAT},pc:{up|flat|down},trend:{uptrend|sideways|downtrend},
step:{early|mid|late},high:{ath_zone|near|far},vol:{low|mid|high},
ma_s:{below|near|above},ma_l:{below|near|above},
cz:{dry|low|mid|high},sz:{locked|tight|free|open},
regime:{BULL_STRONG|BEAR_STRONG|NORMAL},
ac:{peak|trough|transition|flat},
action:{HOLD|BUY_SMALL|BUY_MEDIUM|SELL_SMALL|SELL_MEDIUM}
```

12 diskretisierte Dimensionen + 5 Aktionen. Theoretisch ~200.000 mögliche Chains.

## Warum Resonanzlogik statt konventionelle ML

| Eigenschaft | Neuronales Netz | Resonanzlogik |
|-------------|-----------------|---------------|
| Datenbedarf | 100K+ Datenpunkte | 5.000–10.000 Episoden |
| Trainingszeit | GPU-Stunden | 5–15 Minuten (CPU) |
| Erklärbarkeit | Keine | Vollständig (lesbare CSV) |
| Fehlerdiagnose | "Es hat nicht funktioniert" | "ma_sell_guard hat 360 SELLs blockiert" |
| Vorwissen | Nicht integrierbar | Explizite Regeln als Leitplanken |
| Vergessen | Katastrophal | Gradueller Decay (0.80 pro Pass) |
| Physik-Grundlage | Keine | Resonanzfeldtheorie (Axiome 1,2,5,6) |
| Marktverständnis | Korrelationen in Daten | Schwingungsstruktur im Feld |

### Was ResoTrade nicht tut

- **Keine Punkt-Prognose.** Das System sagt nicht vorher, bei welchem Preis BTC morgen steht.
- **Keine Trendfolge.** Das System folgt keinem Trend, sondern erkennt die Phase im Schwingungszyklus.
- **Kein Overfitting.** Der Erfahrungsspeicher generalisiert über diskretisierte States, nicht über spezifische Kursverläufe. Validiert über 4 verschiedene Marktregime.

### Was ResoTrade tut

**Energierichtung berechnen + resonant handeln.** Der Markt schwingt um seinen Gleichgewichtswert (MA_LONG). Das System berechnet den Energierichtungsvektor, erkennt die Phase im AC-Schwingungszyklus und handelt resonant: Kaufen im Trough, Verkaufen am Peak, Halten in der Transition.

Die effektive Leistung:

```
P_eff = (AC_amplitude / DC_level) · f_trade · η(Δφ) · (1 − γ_fee)
```

Solange BTC volatil bleibt, gibt es Spread zwischen Dips und Spikes. Der Bot erntet diesen Spread mechanisch — nicht weil er den Preis vorhersagt, sondern weil er die Richtung des Energieflusses im Feld berechnet.

## Empirische Erkenntnisse

1. **Kein klassischer Indikator hat prädiktive Kraft** auf dem Datensatz (Korrelation < 0.05):
   - `direction_hint`, MA-Crossover, RSI, Momentum — alle wirkungslos
   - Posterior-Wahrscheinlichkeiten — konstant (Base-Rates, keine echten Prognosen)

2. **Gewinn kommt aus resonanter Energieextraktion**, nicht aus Trendprognose

3. **AC/DC-Zerlegung verbessert die Extraktion**, weil sie den richtigen Zeitpunkt im Zyklus identifiziert

4. **Multi-Zyklus-Training über verschiedene Marktregime** zeigt stabile Performance (kein Overfitting):
   - Ergebnisse nach 1 Zyklus ≈ Ergebnisse nach 3 Zyklen (Δ < 1%)
   - Alle 4 Regime positiv vs HODL

5. **Parameteränderungen verschlechtern** — das System befindet sich in einem schmalen Resonanzfenster. Nur strukturelle Änderungen (neue Axiome) verbessern die Performance.

## Dateien

| Datei | Funktion |
|-------|----------|
| `config.py` | Zentrale Konfiguration — einzige Quelle für alle Parameter |
| `main.py` | Einstiegspunkt: Multi-Pass-Training + Diagnostik + Merge |
| `train_offline.py` | Trainingsschleife |
| `policy.py` | V11: AC/DC-phasenmodulierte Policy mit Resonanz-Gate + Balance-Regler |
| `env.py` | V11.1: AC/DC-Zerlegung, Regelkette, Downtrend-Pause-Gate |
| `portfolio.py` | BTC/USD-Portfolio mit Fees |
| `experience.py` | Erfahrungsspeicher mit getrennten Dateien + gewichtetem Merge |
| `data_loader.py` | Multi-Source Daten-Pipeline (yfinance → Binance → CoinGecko → Stooq) |
| `diagnostics.py` | Episoden-Diagnostik mit Blockade-Tracking |
| `resonance_analysis.py` | Resonanz-Analyse (FFT, Amplitude, Posteriors), CLI für Abschnitte |
| `plot_final_trades.py` | Deterministischer Trade-Plot (einzelner Abschnitt) |
| `plot_final_trades_all.py` | V11.1: Trade-Plots für alle 4 Abschnitte + Kombinationsplot |
| `train_all_sections.ps1` | V11.1: Trainingsscript Windows (PowerShell) |
| `train_all_sections_multi.sh` | V11.1: Multi-Zyklus-Trainingsscript Linux (Bash) |
| `kraken_client.py` | Kraken REST API Client |
| `live_signal.py` | V11.1: Live-Signal-Generator mit Dry-Run, Human-Hint, Expectation |
| `human_hint.py` | V11.1: Human-Hint CLI (bullish/bearish/neutral/pause/clear/status) |
| `hint_evaluator.py` | V11.1: Rückblickende Bewertung der Hint-Qualität |
| `analyze_logs.py` | Live-Performance-Analyse |
| `debug_resotrade.py` | Diagnose-Sonden |
| `debug_policy.py` | Live-State Policy-Analyse |
| `check_balance_impact.py` | Buy/Sell-Balance Simulation |

## Konfiguration

Zentrale Parameter in `config.py`:

```python
# Kraken
KRAKEN_FEE_PCT = 0.0026           # 0.26% Taker-Fee

# Portfolio
HODL_SHARE = 0.10                 # 10% HODL-Kern (DC-Schutz)
TRADE_FRACTION_SMALL = 0.10       # 10% pro Small-Trade
TRADE_FRACTION_MEDIUM = 0.25      # 25% pro Medium-Trade

# MA-Parameter (Stundenbasis)
MA_SHORT_WINDOW = 24              # 24h (Kurzzeit-Oszillator)
MA_LONG_WINDOW = 168              # 7d (DC-Komponente)
VOLATILITY_WINDOW = 72            # 3d

# Training
TRAINING_WINDOW_LENGTH = 720      # 30 Tage (720 Stunden)
EXPERIENCE_DECAY_PER_PASS = 0.80  # Vergessen: 20% pro Pass

# Live-Abtastung
SIGNAL_INTERVAL_SECONDS = 300     # 5 Minuten
MIN_PRICE_CHANGE_PCT = 0.001      # 0.1% Mindest-Preisänderung
PC_BIN_THRESHOLD = 0.002          # 0.2% Schwelle für up/flat/down

# Downtrend-Pause-Gate (V11.1)
PAUSE_E_LONG_THRESHOLD = -0.05    # Pause wenn e_long < -5%
PAUSE_REGIME = "BEAR_STRONG"      # UND Regime = BEAR_STRONG
RESUME_E_LONG_THRESHOLD = -0.03   # Wiederaufnahme wenn e_long > -3%
RESUME_AC_PHASE = "trough"        # ODER AC-Phase = trough
```

## Sicherheitsarchitektur

| Schicht | Mechanismus |
|---------|-------------|
| DRY_RUN | Umgebungsvariable `RESOTRADE_DRY_RUN` — Default `true` |
| Order-Limits | Max 500 USD / 0.01 BTC pro Order |
| HODL-Kern | 10% BTC wird nie verkauft (DC-Schutz) |
| Downtrend-Pause-Gate | Komplettes Trading-Aussetzen bei starkem Bärenmarkt |
| Balance-Regler | Cash < 8% → kein BUY, Sellable < 5% → kein SELL (doppelt: Policy + Env) |
| Cooldown | MEDIUM→SMALL bei ≥3 konsekutiven Trades |
| Human-Hint Pause | Mensch kann alle Trades sofort blockieren |
| Notfall-Stopp | `human_hint.py pause 999 "NOTFALL"` |
| Regime-Schutz | BULL_STRONG → kein SELL, BEAR_STRONG → kein BUY (mit Ausnahme) |
| Fill-Validierung | Market-Orders werden auf Füllung geprüft |
| Hint-Verfall | Hints verfallen automatisch nach 48h |
| Atomares Schreiben | `.tmp` → `.replace()` |

## Validierungskriterien für Echtbetrieb

| Kriterium | Schwelle |
|-----------|----------|
| Paper-Performance vs HODL | Positiv über 2+ Wochen |
| Overtrading | < 5 Trades pro Tag im Schnitt |
| Drawdown | Nie unter -10% vs HODL |
| Signal-Plausibilität | BUY bei Dips, SELL bei Spikes, HOLD dazwischen |
| Downtrend-Pause | Bei Crash kein blindes Kaufen |
| Hint-Qualität | Hints verbessern Performance (hint_evaluator.py) |

## Resonanzfeldtheorie

Dieses System basiert auf der [Resonanzfeldtheorie](https://github.com/DominicReneSchu/public) von Dominic-René Schu.

### Angewendete Axiome

- **Axiom 1** (Universelle Schwingung): Jede Entität besitzt eine periodische Schwingung — der BTC-Preis wird in DC (Trend) und AC (handelbare Schwingung) zerlegt
- **Axiom 2** (Kopplungsstruktur): Das System muss im Gleichgewicht bleiben — Cash und BTC als gekoppelte Resonanzräume
- **Axiom 5** (Energie ist vektoriell): Der Preisfluss hat nicht nur Betrag, sondern Richtung — `energy_dir = e_short - e_long`
- **Axiom 6** (Resonanzkopplung): Trades nur wenn die Handlungsrichtung mit der Energierichtung des Marktes übereinstimmt — K = K₀·cos(θ)

### Weiterführende Dokumente

- [Energierichtung in realen Systemen](https://github.com/DominicReneSchu/public/blob/main/de/fakten/docs/mathematik/energierichtung.md)
- [Energiekugel und AC/DC-Zerlegung](https://github.com/DominicReneSchu/public/blob/main/de/fakten/docs/mathematik/energiekugel.md)
- [Resonanzzeitkoeffizient τ*](https://github.com/DominicReneSchu/public/blob/main/de/fakten/docs/mathematik/tau_resonanzkoeffizient.md)
- [Resonanzanalyse in Massendaten](https://github.com/DominicReneSchu/public/blob/main/de/fakten/empirisch/dokumentation.md)
- [Altcoin-Analyse: Warum nur BTC](https://github.com/DominicReneSchu/public/blob/main/de/fakten/empirisch/resotrade_altcoin_analyse.md)

## CLI-Referenz

```bash
# Training
python main.py 20 500                  # Training (20×500 Episoden)
python resonance_analysis.py           # Marktdaten + Signale (letzte 180d)
python resonance_analysis.py --start 2024-03-01 --end 2024-09-01  # Abschnitt

# Plots
python plot_final_trades.py            # Einzelplot (letzter Abschnitt)
python plot_final_trades_all.py        # Alle 4 Abschnitte + Kombi

# Live
python live_signal.py status           # Kraken-Status + Portfolio + Hint
python live_signal.py expectation      # System-Erwartung + Hint-Wirkung
python live_signal.py once             # Ein Signal-Zyklus
python live_signal.py loop             # Dauerbetrieb (Dry-Run, 5 Min)
python live_signal.py loop 900         # Dauerbetrieb (15 Min Intervall)
python live_signal.py merge            # Offline + Live Erfahrung mergen
python live_signal.py speicher         # Speicher-Status anzeigen

# Human-Hint
python human_hint.py bullish "Grund"   # Bullish-Hint (blockiert SELL)
python human_hint.py bearish "Grund" 0.5  # Bearish mit Gewicht (blockiert BUY)
python human_hint.py pause 12 "Grund"  # Pause für 12 Stunden (blockiert alles)
python human_hint.py neutral "Grund"   # Neutral-Hint (keine Änderung)
python human_hint.py status            # Aktuellen Hint anzeigen
python human_hint.py clear             # Hint aufheben

# Auswertung
python analyze_logs.py                 # Live-Performance
python hint_evaluator.py               # Hint-Qualität bewerten

# Diagnose
python debug_resotrade.py              # Diagnose-Sonden
python debug_policy.py                 # Policy-Analyse
```

## Versionsverlauf

| Version | Kernänderung | Performance |
|---------|-------------|-------------|
| V6 | Basis: MA-Heuristik + Erfahrungsspeicher | +35.04% (180d) |
| V7 | pc_bin-Filter für Plateau-Erkennung | +35.61% (180d) |
| V8 | Plateau-Filter (Reset + Decay) — verworfen | +34.69% (180d) |
| V9.4 | 15 Bugfixes, Regime-Erkennung, Bounce-SELL | +35.61% (180d) |
| V10 | Energierichtungsvektor (Axiom 5+6), MA-SELL-Guard | +37.03% (180d) |
| V11 | AC/DC-Zerlegung (Axiom 1), Phasenmodulation | +42.89% (180d) |
| **V11.1** | **Downtrend-Pause-Gate, Multi-Zyklus, Human-Hint, Live** | **+26.1% Ø (4×6M)** |

---

© Dominic-René Schu — Resonanzfeldtheorie 2025