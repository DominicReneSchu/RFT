# backtest_engine.py
# © Dominic-René Schu, 2025/2026 — Resonanzfeldtheorie
#
# RT-10: Reproduzierbarer Walk-Forward-Backtest — ResoTrade-Resonanzlogik
#
# Schließt M-5 (PEER_REVIEW_READINESS.md):
#   Der 24-Monats-Backtest in resotrade_trading_ki.md war eine private Implementierung
#   ohne öffentliche Reproduzierbarkeit. Dieses Modul liefert einen vollständig öffentlichen,
#   lizenzierten, reproduzierbaren Walk-Forward-Backtest der ResoTrade-Resonanzlogik.
#
# Datenquellen (Prioritätsreihenfolge):
#   1. Binance Public API (kein Account erforderlich):
#      https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1h&limit=1000
#      Gibt: OHLCV-Kerzen, öffentliche Lizenz, keine Authentifizierung.
#   2. ccxt-Bibliothek — Binance Public-Endpoint:
#      ccxt.binance().fetch_ohlcv('BTC/USDT', '1h', limit=1000)
#   3. Synthetischer Fallback: deterministisches BTC-realistisches Signal (seed=42)
#      Parameter: DC-Trend 30000+0,5*t, AC-Zyklen (Perioden 50h/120h/20h),
#      Rauschen std=150 USDT. Vollständig dokumentiert, keine proprietären Daten.
#
# Falsifizierungskriterium (M-5):
#   vs_hodl > 0,0 in ALLEN Walk-Forward-Folds → M-5 behoben (Reproduzierbarkeit bestätigt)
#   vs_hodl ≤ 0,0 in MINDESTENS EINEM Fold   → M-5 nicht vollständig behoben; Ergebnis dokumentiert
#   Sharpe-Ratio > 0,5 als Zusatzkriterium (robuste Überperformance vs. Volatilität)
#
# Verwendung:
#   python backtest_engine.py
#   python analyse/rt10_backtest_vergleich.py
#
# Abhängigkeiten: numpy, pandas, matplotlib, requests, scipy
#   Optional: ccxt>=4.0.0 (für Live-Daten)

from __future__ import annotations

import os
import datetime
import numpy as np
import pandas as pd

# ============================================================
# Konstanten
# ============================================================

PI = np.pi
SEED_STANDARD = 42
BINANCE_API_URL = (
    "https://api.binance.com/api/v3/klines"
    "?symbol=BTCUSDT&interval=1h&limit=1000"
)


# ============================================================
# 1. Datenbeschaffung
# ============================================================

def fetch_btcusdt_ohlcv(source: str = 'binance_api',
                         n_kerzen: int = 2000,
                         intervall: str = '1h',
                         seed: int = SEED_STANDARD) -> pd.DataFrame:
    """
    Lädt BTC-USDT-OHLCV-Daten aus einer öffentlichen, lizenzfreien Quelle.

    Parameter
    ---------
    source : str
        'binance_api'  — Binance REST API (keine Authentifizierung erforderlich)
        'ccxt'         — ccxt-Bibliothek mit Binance Public-Endpoint
        'synthetisch'  — Deterministisches synthetisches Signal (BTC-realistisch)
    n_kerzen : int
        Anzahl der stündlichen Kerzen, die geladen / generiert werden sollen.
    intervall : str
        Kerzenintervall (Standard '1h'). Wird an API/ccxt übergeben.
    seed : int
        Zufalls-Seed für den synthetischen Fallback.

    Rückgabe
    --------
    pd.DataFrame
        Spalten: timestamp (UTC datetime), open, high, low, close, volume
        Attribut df.attrs['quelle'] dokumentiert die verwendete Quelle.

    Datenquellen (vollständig dokumentiert für Reproduzierbarkeit):
    ───────────────────────────────────────────────────────────────
    Binance API Endpoint:
        https://api.binance.com/api/v3/klines
        Symbol: BTCUSDT, Intervall: 1h
        Öffentlicher Endpoint, keine Authentifizierung, MIT-kompatible Datenlizenz.
        Kline-Feldreihenfolge: [open_time, open, high, low, close, volume, ...]

    ccxt-Bibliothek (Fallback):
        pip install ccxt>=4.0.0
        ccxt.binance().fetch_ohlcv('BTC/USDT', '1h', limit=n_kerzen)
        Gibt zurück: [[timestamp_ms, open, high, low, close, volume], ...]

    Synthetischer Fallback (deterministisch):
        DC-Trend : 30_000 + 0,5 * t + 2000 * sin(2π t / 800)  [USDT/h]
        AC-Zyklen: 800*sin(2π t/50) + 400*sin(2π t/120) + 200*sin(2π t/20)
        Rauschen : Normal(0, 150) USDT
        seed=42 garantiert bitgenaue Reproduzierbarkeit.
    """
    _gueltige_quellen = ('binance_api', 'ccxt', 'synthetisch')
    if source not in _gueltige_quellen:
        print(f"  [backtest_engine] Unbekannte Quelle '{source}' — "
              f"nutze synthetischen Fallback (gültig: {_gueltige_quellen}).")

    if source == 'binance_api':
        df = _lade_binance_api(n_kerzen, intervall)
        if df is not None:
            df.attrs['quelle'] = 'Binance Public API'
            return df
        print("  [backtest_engine] Binance API nicht erreichbar — versuche ccxt...")

    if source in ('binance_api', 'ccxt'):
        df = _lade_ccxt(n_kerzen, intervall)
        if df is not None:
            df.attrs['quelle'] = 'ccxt / Binance Public-Endpoint'
            return df
        print("  [backtest_engine] ccxt nicht verfügbar — nutze synthetischen Fallback.")

    df = _generiere_synthetisches_btc(n_kerzen, seed=seed)
    df.attrs['quelle'] = f'Synthetisch BTC-realistisch (seed={seed})'
    return df


def _lade_binance_api(n_kerzen: int, intervall: str) -> pd.DataFrame | None:
    """Lädt Daten von der Binance Public REST API."""
    try:
        import requests
        limit = min(n_kerzen, 1000)
        if n_kerzen > 1000:
            print(f"  [backtest_engine] Hinweis: Binance API begrenzt auf 1000 Kerzen;"
                  f" angefragt {n_kerzen}, lade {limit}.")
        url = (f"https://api.binance.com/api/v3/klines"
               f"?symbol=BTCUSDT&interval={intervall}&limit={limit}")
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        raw = resp.json()
        return _parse_binance_klines(raw)
    except Exception as fehler:
        print(f"  [backtest_engine] Binance API Fehler: {fehler}")
        return None


def _lade_ccxt(n_kerzen: int, intervall: str) -> pd.DataFrame | None:
    """Lädt Daten über die ccxt-Bibliothek."""
    try:
        import ccxt
        exchange = ccxt.binance()
        raw = exchange.fetch_ohlcv('BTC/USDT', intervall, limit=n_kerzen)
        eintraege = []
        for r in raw:
            eintraege.append({
                'timestamp': pd.Timestamp(r[0], unit='ms', tz='UTC'),
                'open':   float(r[1]),
                'high':   float(r[2]),
                'low':    float(r[3]),
                'close':  float(r[4]),
                'volume': float(r[5]),
            })
        return pd.DataFrame(eintraege)
    except Exception as fehler:
        print(f"  [backtest_engine] ccxt Fehler: {fehler}")
        return None


def _parse_binance_klines(raw: list) -> pd.DataFrame:
    """Verarbeitet die Binance Klines JSON-Antwort."""
    eintraege = []
    for zeile in raw:
        eintraege.append({
            'timestamp': pd.Timestamp(int(zeile[0]), unit='ms', tz='UTC'),
            'open':   float(zeile[1]),
            'high':   float(zeile[2]),
            'low':    float(zeile[3]),
            'close':  float(zeile[4]),
            'volume': float(zeile[5]),
        })
    return pd.DataFrame(eintraege)


def _generiere_synthetisches_btc(n: int = 2000,
                                   seed: int = SEED_STANDARD) -> pd.DataFrame:
    """
    Deterministisches synthetisches BTC-USDT-Signal.

    Parameter (vollständig dokumentiert für Reproduzierbarkeit):
        DC-Trend : 30_000 + 0,5 * t  (BTC-Langfristaufwertung ~USD/h)
        AC-Haupt : 800  * sin(2π t / 50)    (50-Stunden-Hauptzyklus)
        AC-Lang  : 400  * sin(2π t / 120)   (120-Stunden-Mittelzyklus)
        AC-Kurz  : 200  * sin(2π t / 20)    (20-Stunden-Kurzzyklus)
        Rauschen : Normal(0, 150) USDT
        seed     : 42 (Standard) — garantiert bitgenaue Reproduzierbarkeit

    Startdatum: 2024-01-01 00:00 UTC als Referenzausrichtung.
    """
    rng = np.random.RandomState(seed)
    t = np.arange(n, dtype=float)

    dc = 30_000.0 + 0.5 * t + 2000.0 * np.sin(2 * PI * t / 800)
    ac = (800.0 * np.sin(2 * PI * t / 50)
          + 400.0 * np.sin(2 * PI * t / 120)
          + 200.0 * np.sin(2 * PI * t / 20))
    rauschen = rng.normal(0, 150, n)

    close = dc + ac + rauschen
    close = np.maximum(close, 1.0)

    open_ = np.roll(close, 1)
    open_[0] = close[0]
    spread = np.abs(rng.normal(0, 50, n))
    high = np.maximum(close, open_) + spread * 0.5
    low = np.minimum(close, open_) - spread * 0.5
    volumen = rng.lognormal(10, 1, n)

    start = pd.Timestamp('2024-01-01 00:00:00', tz='UTC')
    zeitstempel = [start + pd.Timedelta(hours=int(i)) for i in t]

    return pd.DataFrame({
        'timestamp': zeitstempel,
        'open':   open_,
        'high':   high,
        'low':    low,
        'close':  close,
        'volume': volumen,
    })


# ============================================================
# 2. Walk-Forward-Aufteilung
# ============================================================

def walk_forward_split(df: pd.DataFrame,
                        n_folds: int = 5,
                        train_frac: float = 0.6) -> list[tuple]:
    """
    Teilt Daten in n_folds Walk-Forward-Fenster auf.

    Jedes Fenster ist ein (train_df, test_df)-Tupel ohne Überlappung.
    Kein Look-Ahead-Bias: Test-Fenster werden nie im Training verwendet.
    Train und Test sind chronologisch geordnet und zusammenhängend.

    Strategie: Der Gesamtdatensatz wird in n_folds gleiche Segmente aufgeteilt.
    Für Fold k verwendet das Training die Segmente 0..k und das Testen das Segment k+1.
    Dies gewährleistet strikte zeitliche Ordnung und keine Datenleckage.

    Parameter
    ---------
    df : pd.DataFrame
        Vollständiger OHLCV-Datensatz mit 'close'-Spalte.
    n_folds : int
        Anzahl der Walk-Forward-Folds (Standard 5).
    train_frac : float
        Anteil jedes Fold-Fensters für das Training (Standard 0,6).

    Rückgabe
    --------
    Liste von (train_df, test_df)-Tupeln (keine Überlappung garantiert).
    """
    n = len(df)
    fold_groesse = n // (n_folds + 1)
    folds = []

    for k in range(n_folds):
        train_ende = (k + 1) * fold_groesse
        test_start = train_ende
        test_ende = test_start + fold_groesse

        if test_ende > n:
            test_ende = n
        if test_start >= n:
            break

        train_df = df.iloc[:train_ende].copy().reset_index(drop=True)
        test_df = df.iloc[test_start:test_ende].copy().reset_index(drop=True)
        folds.append((train_df, test_df))

    return folds


# ============================================================
# 3. Resonanzlogik-Hilfsfunktionen (aus resonanzlogik_beispiel.py)
# ============================================================

def kopplungseffizienz(delta_phi: float) -> float:
    """ε(Δφ) = cos²(Δφ/2) — RFT-Kopplung (Axiom 4)."""
    return float(np.cos(delta_phi / 2.0) ** 2)


def zerlegung(preis: np.ndarray,
               fenster_lang: int = 50) -> tuple[np.ndarray, np.ndarray]:
    """DC/AC-Zerlegung: DC = gleitender Mittelwert, AC = Preis - DC."""
    dc = np.convolve(preis, np.ones(fenster_lang) / fenster_lang, mode='same')
    ac = preis - dc
    return dc, ac


def phasendetektion(ac: np.ndarray,
                     amplituden_schwelle: float = 0.3) -> tuple[np.ndarray, np.ndarray]:
    """
    Erkennt die Oszillationsphase in jedem Zeitschritt.
    Gibt (phasen, amplituden) zurück, wobei phasen ∈ {'peak','trough','transition','flat'}.
    """
    n = len(ac)
    phasen = np.full(n, 'flat', dtype='U10')
    amplitude = np.zeros(n)
    fenster = 25
    for i in range(fenster, n):
        segment = ac[i - fenster:i]
        amp = float(np.max(segment) - np.min(segment))
        amplitude[i] = amp
        if amp < 0.5:
            phasen[i] = 'flat'
        elif ac[i] > amplituden_schwelle * amp:
            phasen[i] = 'peak'
        elif ac[i] < -amplituden_schwelle * amp:
            phasen[i] = 'trough'
        else:
            phasen[i] = 'transition'
    return phasen, amplitude


# ============================================================
# 4. ResoTrade-Backtest
# ============================================================

class ResoTradeBacktest:
    """
    Vollständiger Walk-Forward-Backtest der ResoTrade-Resonanzlogik.

    Direkte Erweiterung des ResonanceAgent aus resonanzlogik_beispiel.py.
    Zusätzlich: Walk-Forward-Validierung, Trade-Log-Export, Performance-Metriken.

    Falsifizierungskriterium (M-5):
        vs_hodl > 0,0 in ALLEN Folds → M-5 behoben (Reproduzierbarkeit bestätigt)
        vs_hodl ≤ 0,0 in MINDESTENS EINEM Fold → dokumentiert, M-5 nicht vollständig behoben
    """

    def __init__(self,
                 startkapital: float = 1000.0,
                 handelsanteil: float = 0.15,
                 fenster_dc: int = 50,
                 amplituden_schwelle: float = 0.3,
                 min_epsilon: float = 0.3,
                 abkuehlung: int = 3,
                 seed: int = SEED_STANDARD):
        self.startkapital = startkapital
        self.handelsanteil = handelsanteil
        self.fenster_dc = fenster_dc
        self.amplituden_schwelle = amplituden_schwelle
        self.min_epsilon = min_epsilon
        self.abkuehlung = abkuehlung
        self.seed = seed

        self.fold_ergebnisse: list[dict] = []
        self.trade_log: list[dict] = []

    # ────────────────────────────────────────────────────────
    # Einzelner Fold
    # ────────────────────────────────────────────────────────

    def run_fold(self, train_df: pd.DataFrame,
                 test_df: pd.DataFrame,
                 fold_id: int = 0) -> dict:
        """
        Trainiert auf train_df (Erfahrungsspeicher), testet auf test_df.

        Der Erfahrungsspeicher wird auf Trainingsdaten vortrainiert.
        Keine Preise aus test_df werden während des Trainings verwendet.
        Gibt Performance-Metriken für diesen Fold zurück.
        """
        erfahrungsspeicher = self._trainiere_erfahrung(train_df, fold_id)
        metriken = self._evaluiere(test_df, erfahrungsspeicher, fold_id)
        self.fold_ergebnisse.append(metriken)
        return metriken

    def _trainiere_erfahrung(self, df: pd.DataFrame,
                               fold_id: int) -> dict:
        """
        Trainiert den Erfahrungsspeicher auf historischen Daten.
        Gibt den befüllten Erfahrungsspeicher zurück.
        """
        preis = df['close'].values
        dc, ac = zerlegung(preis, self.fenster_dc)
        phasen, _ = phasendetektion(ac, self.amplituden_schwelle)

        erfahrung: dict[str, float] = {}
        abfall = 0.90
        kasse = self.startkapital
        anlage = 0.0

        def _trend(dc_arr, i, fenster=20):
            if i < fenster:
                return 'seitwaerts'
            steigung = (dc_arr[i] - dc_arr[i - fenster]) / max(dc_arr[i - fenster], 1e-8)
            if steigung > 0.0005:
                return 'aufwaerts'
            elif steigung < -0.0005:
                return 'abwaerts'
            return 'seitwaerts'

        start = max(self.fenster_dc, 25)
        for i in range(start, len(preis)):
            phase = phasen[i]
            trend = _trend(dc, i)
            aktueller_preis = preis[i]
            pw = kasse + anlage * aktueller_preis

            if phase == 'peak':
                aktion = 'VERKAUF'
            elif phase == 'trough':
                aktion = 'KAUF'
            else:
                aktion = 'HALTEN'

            if aktion == 'KAUF' and kasse > 10:
                kauf = kasse * self.handelsanteil
                anlage += kauf / aktueller_preis
                kasse -= kauf
            elif aktion == 'VERKAUF' and anlage > 0.0001:
                verkauf = anlage * self.handelsanteil
                kasse += verkauf * aktueller_preis
                anlage -= verkauf
            else:
                aktion = 'HALTEN'

            neues_pw = kasse + anlage * aktueller_preis
            belohnung = (neues_pw - pw) / max(pw, 1e-8)

            schluessel = f"{phase},{trend},{aktion}"
            erfahrung[schluessel] = erfahrung.get(schluessel, 0.0) * abfall + belohnung

        return erfahrung

    def _evaluiere(self, df: pd.DataFrame,
                    erfahrungsspeicher: dict,
                    fold_id: int) -> dict:
        """
        Bewertet die Resonanzlogik auf Testdaten mit dem trainierten Erfahrungsspeicher.
        Zeichnet alle Trades in self.trade_log auf.
        Gibt Fold-Performance-Metriken zurück.
        """
        preis = df['close'].values
        n = len(preis)
        dc, ac = zerlegung(preis, self.fenster_dc)
        phasen, _ = phasendetektion(ac, self.amplituden_schwelle)

        kasse = self.startkapital
        anlage = 0.0
        blockiert = 0
        letzte_trades: list[str] = []
        pw_verlauf = []
        n_trades = 0

        def _trend(dc_arr, i, fenster=20):
            if i < fenster:
                return 'seitwaerts'
            steigung = (dc_arr[i] - dc_arr[i - fenster]) / max(dc_arr[i - fenster], 1e-8)
            if steigung > 0.0005:
                return 'aufwaerts'
            elif steigung < -0.0005:
                return 'abwaerts'
            return 'seitwaerts'

        hodl_einheiten = self.startkapital / max(preis[0], 1e-8)
        start = max(self.fenster_dc, 25)

        for i in range(start):
            pw_verlauf.append(self.startkapital)

        for i in range(start, n):
            phase = phasen[i]
            trend = _trend(dc, i)
            aktueller_preis = preis[i]
            pw = kasse + anlage * aktueller_preis

            # Kopplungseffizienz
            if phase == 'peak':
                delta_phi = 0.0
            elif phase == 'trough':
                delta_phi = 0.0
            elif phase == 'transition':
                delta_phi = PI / 3
            else:
                delta_phi = PI / 2
            epsilon = kopplungseffizienz(delta_phi)

            # Phasenbasierter Vorschlag
            if phase == 'peak':
                vorschlag = 'VERKAUF'
            elif phase == 'trough':
                vorschlag = 'KAUF'
            else:
                vorschlag = 'HALTEN'

            # Erfahrungsüberschreibung
            if vorschlag != 'HALTEN':
                erf_schluessel = f"{phase},{trend},{vorschlag}"
                if erfahrungsspeicher.get(erf_schluessel, 0.0) < -0.5:
                    vorschlag = 'HALTEN'

            # Regelkette
            aktion = vorschlag
            if epsilon < self.min_epsilon and vorschlag != 'HALTEN':
                aktion = 'HALTEN'
            elif vorschlag == 'KAUF':
                kassen_anteil = kasse / max(pw, 1e-8)
                if kassen_anteil < 0.10:
                    aktion = 'HALTEN'
            elif vorschlag == 'VERKAUF':
                anlage_anteil = 1.0 - kasse / max(pw, 1e-8)
                if anlage_anteil < 0.05:
                    aktion = 'HALTEN'

            if blockiert > 0:
                blockiert -= 1
                aktion = 'HALTEN'

            # Ausführung
            if aktion == 'KAUF' and kasse > 10:
                kauf = kasse * self.handelsanteil
                anlage += kauf / aktueller_preis
                kasse -= kauf
                n_trades += 1
                letzte_trades.append('KAUF')
            elif aktion == 'VERKAUF' and anlage > 0.0001:
                verkauf = anlage * self.handelsanteil
                kasse += verkauf * aktueller_preis
                anlage -= verkauf
                n_trades += 1
                letzte_trades.append('VERKAUF')
            else:
                aktion = 'HALTEN'

            # Abkühlzeit-Prüfung
            if len(letzte_trades) > self.abkuehlung:
                letzte_trades.pop(0)
            if (len(letzte_trades) >= self.abkuehlung
                    and all(t != 'HALTEN' for t in letzte_trades)):
                blockiert = 2

            neues_pw = kasse + anlage * aktueller_preis
            pw_verlauf.append(neues_pw)

            # Trade aufzeichnen
            ts = df['timestamp'].iloc[i] if 'timestamp' in df.columns else i
            self.trade_log.append({
                'fold_id':    fold_id,
                'schritt':    i,
                'timestamp':  ts,
                'aktion':     aktion,
                'preis':      aktueller_preis,
                'pw':         neues_pw,
                'epsilon':    epsilon,
                'phase':      phase,
                'trend':      trend,
                'kasse':      kasse,
                'anlage':     anlage,
            })

        pw_final = kasse + anlage * preis[-1]
        hodl_final = hodl_einheiten * preis[-1]
        gesamtrendite = pw_final / self.startkapital - 1.0
        hodl_rendite = hodl_final / self.startkapital - 1.0
        vs_hodl = gesamtrendite - hodl_rendite

        pw_arr = np.array(pw_verlauf)
        renditen = np.diff(pw_arr) / np.maximum(pw_arr[:-1], 1e-8)
        sharpe = _sharpe_ratio(renditen, perioden_pro_jahr=8760)
        max_dd = _max_drawdown(pw_arr)

        trade_eintraege = [r for r in self.trade_log if r['fold_id'] == fold_id
                           and r['aktion'] != 'HALTEN']
        gewinnrate = _gewinnrate(trade_eintraege, preis)

        return {
            'fold_id':       fold_id,
            'n':             n,
            'pw_start':      self.startkapital,
            'pw_final':      pw_final,
            'hodl_final':    hodl_final,
            'gesamtrendite': gesamtrendite,
            'hodl_rendite':  hodl_rendite,
            'vs_hodl':       vs_hodl,
            'sharpe':        sharpe,
            'max_drawdown':  max_dd,
            'gewinnrate':    gewinnrate,
            'n_trades':      n_trades,
            'pw_verlauf':    pw_arr,
            'hodl_verlauf':  hodl_einheiten * preis,
        }

    # ────────────────────────────────────────────────────────
    # Walk-Forward
    # ────────────────────────────────────────────────────────

    def run_walk_forward(self, df: pd.DataFrame,
                          n_folds: int = 5) -> dict:
        """
        Führt vollständigen Walk-Forward-Backtest über n_folds durch.

        Löscht vorherige Ergebnisse vor dem Start.
        Gibt aggregierte Zusammenfassung zurück.

        Falsifizierungskriterium (M-5):
            Alle Folds: vs_hodl > 0 → M-5 behoben
            Beliebiger Fold: vs_hodl ≤ 0 → dokumentiert, M-5 nicht vollständig behoben
        """
        self.fold_ergebnisse = []
        self.trade_log = []

        folds = walk_forward_split(df, n_folds=n_folds)

        for k, (train_df, test_df) in enumerate(folds):
            self.run_fold(train_df, test_df, fold_id=k)

        return self.performance_metrics()

    # ────────────────────────────────────────────────────────
    # Export
    # ────────────────────────────────────────────────────────

    def export_trade_log(self, dateipfad: str) -> None:
        """
        Exportiert alle Trades als CSV.
        Spalten: fold_id, schritt, timestamp, aktion, preis, pw, epsilon, phase, trend.
        Die fold_id-Spalte identifiziert den Walk-Forward-Fold jedes Trades.
        Der Zeitstempel der Datenabfrage wird als CSV-Header-Kommentar geschrieben.
        """
        if not self.trade_log:
            print("  [backtest_engine] Keine Trades zum Exportieren.")
            return

        df_log = pd.DataFrame(self.trade_log)
        spalten = ['fold_id', 'schritt', 'timestamp', 'aktion',
                   'preis', 'pw', 'epsilon', 'phase', 'trend', 'kasse', 'anlage']
        spalten = [s for s in spalten if s in df_log.columns]
        df_export = df_log[spalten]

        jetzt_utc = datetime.datetime.now(datetime.timezone.utc).isoformat()
        kopfzeile = (
            f"# rt10_trade_log.csv — ResoTrade Walk-Forward-Backtest\n"
            f"# Erstellt: {jetzt_utc} UTC\n"
            f"# Quelle: ResoTrade backtest_engine.py (RT-10)\n"
            f"# Falsifizierungskriterium: vs_hodl > 0 in allen Folds (M-5)\n"
        )

        os.makedirs(os.path.dirname(os.path.abspath(dateipfad)), exist_ok=True)
        with open(dateipfad, 'w') as f:
            f.write(kopfzeile)
            df_export.to_csv(f, index=False)

        n_aktiv = len(df_export[df_export['aktion'] != 'HALTEN'])
        print(f"  → Trade-Log exportiert: {dateipfad}"
              f" ({len(df_export)} Zeilen, {n_aktiv} aktive Trades)")

    # ────────────────────────────────────────────────────────
    # Metriken
    # ────────────────────────────────────────────────────────

    def performance_metrics(self) -> dict:
        """
        Berechnet aggregierte Performance-Metriken über alle Folds.

        Rückgabe
        --------
        dict mit Schlüsseln:
            gesamtrendite    : durchschnittliche Gesamtrendite über alle Folds
            vs_hodl          : durchschnittliche Überperformance vs. HODL
            vs_hodl_alle     : Liste von vs_hodl je Fold
            sharpe_ratio     : durchschnittliche annualisierte Sharpe-Ratio
            max_drawdown     : durchschnittlicher maximaler Drawdown
            gewinnrate       : durchschnittliche Gewinnrate
            n_trades         : Gesamtanzahl aktiver Trades
            n_folds          : Anzahl ausgewerteter Folds
            m5_behoben       : True wenn vs_hodl > 0 in ALLEN Folds
            falsifizierung   : Menschenlesbares Urteil zu M-5
        """
        if not self.fold_ergebnisse:
            return {}

        vs_hodl_liste = [r['vs_hodl'] for r in self.fold_ergebnisse]
        m5_behoben = all(v > 0.0 for v in vs_hodl_liste)

        if m5_behoben:
            falsifizierung = "M-5 BEHOBEN: vs_hodl > 0 in allen Folds — Reproduzierbarkeit bestätigt"
        else:
            gescheitert = [i for i, v in enumerate(vs_hodl_liste) if v <= 0.0]
            falsifizierung = (f"M-5 NICHT VOLLSTÄNDIG BEHOBEN: vs_hodl ≤ 0 in Fold(s) {gescheitert} "
                              f"— dokumentiert, nicht versteckt")

        return {
            'gesamtrendite': float(np.mean([r['gesamtrendite'] for r in self.fold_ergebnisse])),
            'hodl_rendite':  float(np.mean([r['hodl_rendite'] for r in self.fold_ergebnisse])),
            'vs_hodl':       float(np.mean(vs_hodl_liste)),
            'vs_hodl_alle':  vs_hodl_liste,
            'sharpe_ratio':  float(np.mean([r['sharpe'] for r in self.fold_ergebnisse])),
            'max_drawdown':  float(np.mean([r['max_drawdown'] for r in self.fold_ergebnisse])),
            'gewinnrate':    float(np.mean([r['gewinnrate'] for r in self.fold_ergebnisse])),
            'n_trades':      int(sum(r['n_trades'] for r in self.fold_ergebnisse)),
            'n_folds':       len(self.fold_ergebnisse),
            'm5_behoben':    m5_behoben,
            'falsifizierung': falsifizierung,
        }


# ============================================================
# 5. Metrische Hilfsfunktionen
# ============================================================

def _sharpe_ratio(renditen: np.ndarray,
                   risikofreier_zins: float = 0.0,
                   perioden_pro_jahr: int = 8760) -> float:
    """Annualisierte Sharpe-Ratio aus stündlichen Renditen."""
    if len(renditen) < 2:
        return 0.0
    ueberschuss = renditen - risikofreier_zins / perioden_pro_jahr
    std = float(np.std(ueberschuss, ddof=1))
    if std < 1e-10:
        return 0.0
    return float(np.mean(ueberschuss) / std * np.sqrt(perioden_pro_jahr))


def _max_drawdown(pw: np.ndarray) -> float:
    """Maximaler Drawdown als Anteil (0..1)."""
    if len(pw) == 0:
        return 0.0
    peak = np.maximum.accumulate(pw)
    drawdown = (peak - pw) / np.maximum(peak, 1e-10)
    return float(np.max(drawdown))


def _gewinnrate(trades: list[dict], preis: np.ndarray) -> float:
    """Gewinnrate: Anteil der Trades, die den Portfoliowert verbesserten."""
    if not trades:
        return 0.0
    # KAUF gefolgt von Preisanstieg, VERKAUF gefolgt von Preisrückgang
    gewinner = 0
    for t in trades:
        schritt = t['schritt']
        if schritt + 1 < len(preis):
            if t['aktion'] == 'KAUF' and preis[schritt + 1] > preis[schritt]:
                gewinner += 1
            elif t['aktion'] == 'VERKAUF' and preis[schritt + 1] < preis[schritt]:
                gewinner += 1
    return float(gewinner / max(len(trades), 1))


# ============================================================
# 6. CLI-Selbsttest
# ============================================================

def main():
    """Kurzer Selbsttest: synthetische Daten, 5-Fold-Walk-Forward."""
    print("=" * 60)
    print("backtest_engine.py — RT-10 Selbsttest")
    print("=" * 60)

    df = fetch_btcusdt_ohlcv(source='synthetisch', n_kerzen=2000)
    print(f"\n  Daten: {len(df)} Kerzen — Quelle: {df.attrs.get('quelle')}")
    print(f"  Preisbereich: {df['close'].min():.0f}–{df['close'].max():.0f} USDT")

    bt = ResoTradeBacktest(seed=SEED_STANDARD)
    metriken = bt.run_walk_forward(df, n_folds=5)

    print(f"\n  {'─' * 50}")
    print("  WALK-FORWARD-ERGEBNISSE (5 Folds):")
    print(f"  {'─' * 50}")
    for r in bt.fold_ergebnisse:
        flag = "✓" if r['vs_hodl'] > 0 else "✗"
        print(f"  Fold {r['fold_id']+1}:  "
              f"Rendite {r['gesamtrendite']*100:+.1f}%  "
              f"HODL {r['hodl_rendite']*100:+.1f}%  "
              f"vs_HODL {r['vs_hodl']*100:+.1f}%  "
              f"Sharpe {r['sharpe']:+.2f}  "
              f"n={r['n_trades']}  {flag}")

    print(f"  {'─' * 50}")
    print(f"  Ø vs_HODL:     {metriken['vs_hodl']*100:+.2f}%")
    print(f"  Ø Sharpe:      {metriken['sharpe_ratio']:+.2f}")
    print(f"  Max Drawdown:  {metriken['max_drawdown']*100:.1f}%")
    print(f"  Trades gesamt: {metriken['n_trades']}")
    print(f"\n  {metriken['falsifizierung']}")
    print("=" * 60)

    bt.export_trade_log('/tmp/rt10_trade_log_selbsttest.csv')
    print("\nFertig.")


if __name__ == "__main__":
    main()
