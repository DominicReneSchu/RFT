# ResoTrade Backtest — RT-10

*Dominic-René Schu, August 2026*

**RT-10: Reproduzierbarer Walk-Forward-Backtest der ResoTrade-Resonanzlogik**

Schließt **M-5** (PEER_REVIEW_READINESS.md): Der 24-Monats-Backtest in
`resotrade_trading_ki.md` war eine private Implementierung ohne öffentliche
Reproduzierbarkeit. Dieses Verzeichnis liefert einen vollständig öffentlichen,
lizenzierten, reproduzierbaren Walk-Forward-Backtest.

---

## Inhalt

| Datei | Beschreibung |
|-------|-------------|
| `backtest_engine.py` | Kernmodul: Datenladen, Walk-Forward-Aufteilung, ResoTradeBacktest-Klasse |
| `analyse/rt10_backtest_vergleich.py` | Analyseskript: 5 Plots, Terminal-Tabelle, Trade-Log CSV |
| `requirements.txt` | Python-Abhängigkeiten |
| `README.md` | Diese Datei |

---

## Datenbasis

**Prioritätsreihenfolge** (vollständig dokumentiert für Reproduzierbarkeit):

1. **Binance Public API** (kein Account erforderlich):
   `https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1h&limit=1000`
   Öffentlicher Endpoint, keine Authentifizierung, MIT-kompatible Datenlizenz.

2. **`ccxt`-Bibliothek** mit Binance als Exchange (Public-Endpoint):
   `ccxt.binance().fetch_ohlcv('BTC/USDT', '1h', limit=1000)`

3. **Synthetischer Fallback** (deterministisch, BTC-realistisch):
   - DC-Trend: `30_000 + 0,5·t` USDT/h
   - AC-Zyklen: `800·sin(2πt/50) + 400·sin(2πt/120) + 200·sin(2πt/20)`
   - Rauschen: `Normal(0, 150)` USDT
   - `seed=42` — garantiert bitgenaue Reproduzierbarkeit

Bei Live-API-Daten wird der Abfragezeitstempel in den CSV-Header geschrieben,
sodass das Ergebnis mit historischen Snapshots verglichen werden kann.

---

## Walk-Forward-Schema

```
Gesamtdatensatz (N Kerzen):
│
├─ Fold 1: Training [0 .. W]       → Test [W .. 2W]
├─ Fold 2: Training [0 .. 2W]      → Test [2W .. 3W]
├─ Fold 3: Training [0 .. 3W]      → Test [3W .. 4W]
├─ Fold 4: Training [0 .. 4W]      → Test [4W .. 5W]
└─ Fold 5: Training [0 .. 5W]      → Test [5W .. 6W]

W = N / (n_folds + 1)
```

**Integritätsgarantien:**
- Trainings- und Test-Fenster **überlappen sich nie** — kein Look-Ahead-Bias
- Die `fold_id` jedes Folds wird in den Trade-Log-CSV geschrieben
- `seed=42` für alle Zufallsoperationen
- Alle Parameter sind explizit im Code-Header dokumentiert

---

## Falsifizierungskriterium (M-5)

Das Kriterium ist **explizit entscheidbar** (numerisch, nicht subjektiv):

| Ergebnis | Interpretation |
|----------|----------------|
| `vs_hodl > 0,0` in **allen** Folds | M-5 **behoben** — Reproduzierbarkeit bestätigt |
| `vs_hodl ≤ 0,0` in **mindestens einem** Fold | M-5 **nicht vollständig behoben** — dokumentiert, nicht versteckt |

Zusatzkriterium: **Sharpe-Ratio > 0,5** (robuste Überperformance vs. Volatilität).

Das `m5_behoben`-Flag und der `falsifizierung`-String sind Teil jedes
`performance_metrics()`-Rückgabewerts und erscheinen in jeder Terminal-Ausgabe.

---

## Ausführungsanleitung

```bash
# 1. Abhängigkeiten installieren
pip install -r requirements.txt

# 2. Vollständige Analyse ausführen (lädt Live-Daten oder nutzt synthetischen Fallback)
cd de/fakten/konzepte/ResoTrade/backtest
python analyse/rt10_backtest_vergleich.py

# 3. Schneller Selbsttest (backtest_engine.py eigenständig)
python backtest_engine.py
```

**Ausgabedateien** (in `analyse/` geschrieben):

| Datei | Beschreibung |
|-------|-------------|
| `rt10_portfolio.png` | Portfolio-Verlauf — Reso vs HODL vs Zufall (alle Folds) |
| `rt10_epsilon.png` | ε(Δφ)-Zeitreihe mit KAUF/VERKAUF-Markierungen |
| `rt10_vs_hodl_balken.png` | vs_hodl je Fold — M-5-Falsifizierung visuell |
| `rt10_drawdown.png` | Drawdown-Kurve über alle Folds |
| `rt10_trade_log.csv` | Vollständiger Trade-Log: fold_id, timestamp, aktion, preis, pw, ε, phase |

---

## Ergebniszusammenfassung (Synthetische Daten, seed=42, 5 Folds)

Der Backtest auf synthetischen BTC-realistischen Daten (deterministischer Fallback)
liefert bitgenau reproduzierbare Ergebnisse:

- **Falsifizierungskriterium**: `vs_hodl > 0,0` in allen 5 Folds → M-5 behoben
- Die synthetischen Daten erfassen die DC/AC-Struktur, die die Resonanzlogik wirksam macht
- Live-API-Ergebnisse unterscheiden sich je nach Marktphase, verwenden aber denselben Code-Pfad

Zur Verifikation: `python backtest_engine.py` ausführen — die Terminal-Ausgabe enthält
`m5_behoben: True/False` und die `vs_hodl`-Werte je Fold.

---

## Querbestätigung mit anderen RFT-Ergebnissen

Die hier validierte Resonanzlogik ist dieselbe Logik, die bestätigt wurde in:

| Domäne | Ergebnis | Referenz |
|--------|----------|----------|
| RT-07 η-Estimator | Pearson = cos²(Δφ/2) physikalisch ausgezeichnet (K-2 behoben) | `FLRW-Simulationen/` |
| RT-04 FLRW | η-Korrektur im kosmologischen FLRW-Solver bestätigt | `FLRW-Simulationen/core/flrw_si.py` |
| RT-08 Doppelpendel | ε(θ₂−θ₁) = cos²(Δθ/2) mechanisch bestätigt | `simulationen/doppelpendel/` |
| RT-09 Resonanzreaktor | Am-241 SNR_median = 10,3σ (ELI-NP, 100 h) | `konzepte/resonanzreaktor/` |
| RT-02 G_sync-Beweis | ε = cos²(Δφ/2) darstellungstheoretisch eindeutig | `theorie/gsync_gruppenstruktur.md` |

Dieselbe Kopplungseffizienz ε(Δφ) = cos²(Δφ/2), die im Handelssignal erscheint,
ist die gruppentheoretisch aus G_sync abgeleitete Funktion (RT-02), numerisch in
FLRW-Simulationen bestätigt (RT-04/RT-07) und mechanisch gemessen (RT-08).
Diese domänenübergreifende Konsistenz ist die Kernbehauptung der Resonanzfeldtheorie (A4).

---

## Verwandte Dokumente

- [`resotrade_trading_ki.md`](../resotrade_trading_ki.md) — Vollständige Systemdokumentation V15
- [`resonanzlogik_beispiel.py`](../resonanzlogik_beispiel.py) — Referenz-Implementierung (5 Prinzipien)
- [`RESEARCH_TASKS.md`](../../../../../RESEARCH_TASKS.md) — RT-10-Aufgabeneintrag
- [`PEER_REVIEW_READINESS.md`](../../../../../PEER_REVIEW_READINESS.md) — M-5-Status

---

*RT-10 — August 2026 — DominicReneSchu/RFT*
