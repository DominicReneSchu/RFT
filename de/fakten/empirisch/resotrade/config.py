"""
ResoTrade V11.1 — Konfiguration für Live-Trading.
Alle Parameter an einem Ort. Keine API-Keys hier — die liegen in kraken.key
oder im OS-Keyring.

Resonanzfeldtheoretische Grundlage (RFT V3.1):
  A1: Universelle Schwingung — AC/DC-Zerlegung des Preisfeldes
  A2: Superposition — MA_SHORT + MA_LONG als überlagerte Moden
  A4: Kopplungsenergie E = π·ε·h·f — Balance-Regler
  A5: Energierichtung — energy_dir = e_short - e_long
  A6: Informationsfluss — Resonanz-Gate (Trades nur bei Phasenkohärenz)
  A7: Invarianz — Regime-invariante Performance über alle Marktphasen
"""
import os
from pathlib import Path

# === Pfade ===
BASE_DIR = Path(__file__).parent
KRAKEN_KEY_FILE = BASE_DIR / "kraken.key"
DATA_DIR = BASE_DIR / "data"
EXPERIENCE_CSV = DATA_DIR / "trade_experience_weighted.csv"
LIVE_LOG_DIR = DATA_DIR / "live_logs"

# === Kraken ===
KRAKEN_PAIR = "XXBTZUSD"
KRAKEN_ORDER_PAIR = "XBTUSD"
KRAKEN_FEE_PCT = 0.0026

# === Portfolio-Relativ-Modus ===
HODL_SHARE = 0.10
TRADE_FRACTION_SMALL = 0.10
TRADE_FRACTION_MEDIUM = 0.25
MIN_BTC_ORDER = 0.0001
MIN_USD_ORDER = 5.0

# === MA-Parameter (Stundenbasis) ===
# A2 (Superposition Φ = Σψᵢ): Der Preis ist die Überlagerung von
# MA_SHORT (24h-Mode) und MA_LONG (168h-Mode). Beide Zeitskalen werden
# separat ausgewertet (e_short, e_long) und ihre Differenz ergibt den
# Energierichtungsvektor (A5).
MA_SHORT_WINDOW = 24
MA_LONG_WINDOW = 168
VOLATILITY_WINDOW = 72
MIN_CANDLES_FOR_SIGNAL = 168

# === Live-Signal ===
SIGNAL_INTERVAL_SECONDS = 300     # Alle 5 Minuten abtasten
LOOKBACK_HOURS = 336              # 14 Tage OHLC-History

# === Intelligente Abtastung ===
MIN_PRICE_CHANGE_PCT = 0.001      # 0.1% Mindest-Preisänderung für Neubewertung
SKIP_IDENTICAL_STATES = True       # Identische States überspringen

# === Sicherheit ===
DRY_RUN = os.environ.get("RESOTRADE_DRY_RUN", "true").lower() != "false"
MAX_SINGLE_ORDER_USD = 500.0
MAX_SINGLE_ORDER_BTC = 0.01
COOLDOWN_SECONDS = 60

# === Zentralisierte Schwellen ===
PC_BIN_THRESHOLD = 0.002          # 0.2% Schwelle für pc_bin (up/flat/down)
HOLD_NOISE_PCT = 0.0005           # 0.05% Noise-Korridor für HOLD-Bewertung
CANDLE_INTERVAL_MINUTES = 60      # Kerzenintervall in Minuten
EVAL_HORIZON_HOURS = 1            # Bewertungshorizont im Training
TRADE_COOLDOWN_STEPS = 5          # Cooldown-Schritte bei Richtungswechsel (Env)
# Decay — V9.4: Pro PASS, nicht pro Episode
# 0.90 pro Pass → nach 5 Passes: 0.9^5 = 0.59 (behält 59%)
# nach 10 Passes: 0.9^10 = 0.35 (behält 35%)
EXPERIENCE_DECAY_PER_PASS = 0.80  # war 0.90 — aggressiverer Vergessens-Faktor

# === V9.4: Korrektur-Parameter ===
# Referenzwert für Score-Normalisierung. War implizit 5.0, was bei
# Raten im Bereich -0.3..+0.3 (Spread ~0.6) die Erfahrung auf ~12%
# dämpfte. Neuer Wert 1.0 → volle Skalierung ab Spread ≥ 1.0,
# proportional darunter.
NORM_SPREAD_REF = 1.0

# Erlaubt Gewinnmitnahmen (SELL bei e_long 1-3%) auch bei low volatility.
# War vorher blockiert ("damped"), was bei ruhigen Märkten alle kleinen
# Schwingungen ungenutzt ließ.
SELL_LOW_VOL_ENABLED = True

# === Makro-Regime ===
REGIME_MIN_DURATION = 18         # 18h (war 12 — etwas mehr Geduld)
REGIME_MIN_STRENGTH = 0.02       # 2% MA-Divergenz (bleibt)

# A7 (Invarianz unter G_sync): Die Resonanzstruktur ist skalierungsinvariant.
# Das Training über 4 verschiedene Marktregime (Sideways, Bullrun, Korrektur,
# Crash) bestätigt: Die Axiome gelten regime-invariant.
TRAINING_WINDOW_LENGTH = 720

# === Downtrend-Pause-Gate (V11.1) ===
# A1 + A4: Wenn DC stark fällt (BEAR_STRONG + e_long < -5%), ist die
# AC-Schwingung nicht profitabel handelbar — die Kopplungseffizienz ε → 0.
# Das System hält nur den HODL-Kern und wartet auf Stabilisierung.
PAUSE_TREND = "downtrend"              # Trend muss Downtrend sein
PAUSE_E_LONG_THRESHOLD = -0.05         # e_long < -5% (deutlich unter MA_LONG)
PAUSE_REGIME = "BEAR_STRONG"           # Regime muss BEAR_STRONG sein

# Stabilisierung: Daytrading wird wieder aufgenommen wenn:
RESUME_E_LONG_THRESHOLD = -0.03        # e_long > -3% ODER
RESUME_AC_PHASE = "trough"             # AC-Phase = trough (Wendepunkt)