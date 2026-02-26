"""
ResoTrade V11.1 — Trading-Environment mit Downtrend-Pause-Gate.

Regelkette:
  1. Downtrend-Pause-Gate (NEU V11.1) — komplette Trading-Pause
  2. Regime-Rule (BULL_STRONG/BEAR_STRONG)
  3. MA-SELL-Guard (resonanzlogisch, Peak-Exception)
  4. ATH-Rule (kein BUY nahe Allzeithoch)
  5. Trend-Rule (kein BUY im Downtrend nahe MA)
  6. MA-Rule (kein BUY >5% über MA-Short)
  7. Cooldown (MEDIUM→SMALL bei Overtrading)
  8. Balance-Regler (Cash/Sellable-Schutz)

Blockade-Tracking: Jede Regel meldet ihren Eingriff.
"""
from typing import Optional

import numpy as np
import pandas as pd

from portfolio import Portfolio
from config import (
    MA_SHORT_WINDOW,
    MA_LONG_WINDOW,
    VOLATILITY_WINDOW,
    KRAKEN_FEE_PCT,
    HODL_SHARE,
    PAUSE_E_LONG_THRESHOLD,
    PAUSE_REGIME,
    RESUME_E_LONG_THRESHOLD,
    RESUME_AC_PHASE,
)


# Blockade-Gründe als Konstanten
BLOCK_NONE = "none"
BLOCK_ATH = "ath_rule"
BLOCK_TREND = "trend_rule"
BLOCK_MA = "ma_rule"
BLOCK_MA_SELL_GUARD = "ma_sell_guard"
BLOCK_HODL_KERN = "hodl_kern"
BLOCK_NO_CASH = "no_cash"
BLOCK_FRACTION_ZERO = "fraction_zero"
BLOCK_REGIME = "regime"
BLOCK_COOLDOWN = "cooldown"
BLOCK_BALANCE = "balance"
BLOCK_DOWNTREND_PAUSE = "downtrend_pause"


class TradingEnv:
    """
    Offline-Umgebung über einen BTC-Preis-DataFrame.

    V11.1-Änderungen:
      - Downtrend-Pause-Gate: Komplettes Trading-Aussetzen bei
        BEAR_STRONG + downtrend + e_long < -5%
      - Wiederaufnahme bei Stabilisierung (e_long > -3%,
        ac_phase=trough, oder Regime-Wechsel)
      - AC/DC-Zerlegung im State
      - Energierichtungsvektor
      - Resonanzlogischer MA-SELL-Guard mit Peak-Exception
      - Balance-Regler
      - Cooldown
    """

    def __init__(
        self,
        df: pd.DataFrame,
        start_btc: float = 0.0,
        start_cash: float = 0.0,
        fee_pct: float = 0.001,
        price_col: str = "price",
        trend_col: Optional[str] = None,
        trade_fraction_small: float = 0.10,
        trade_fraction_medium: float = 0.25,
        ath_buffer_pct: float = 0.0,
        window_length: int = 90,
        min_btc_for_full_sell: float = 0.1,
        min_btc_trade_fraction: float = 0.05,
        ma_short_col: Optional[str] = "ma_short",
        ma_long_col: Optional[str] = "ma_long",
        hodl_core_btc: float = 0.6,
    ):
        self.df = df.reset_index(drop=True).copy()
        self.start_btc = float(start_btc)
        self.start_cash = float(start_cash)
        self.fee_pct = float(fee_pct)
        self.price_col = price_col
        self.trend_col = trend_col
        self.trade_fraction_small = max(0.0, min(1.0, float(trade_fraction_small)))
        self.trade_fraction_medium = max(0.0, min(1.0, float(trade_fraction_medium)))
        self.ath_buffer_pct = max(0.0, float(ath_buffer_pct))
        self.window_length = max(1, int(window_length))
        self.min_btc_for_full_sell = float(min_btc_for_full_sell)
        self.min_btc_trade_fraction = max(0.0, min(1.0, float(min_btc_trade_fraction)))
        self.ma_short_col = ma_short_col
        self.ma_long_col = ma_long_col

        self.hodl_core_btc = max(0.0, float(hodl_core_btc))

        self._idx_global = 0
        self._steps_remaining = 0
        self.portfolio: Optional[Portfolio] = None
        self._prev_price: Optional[float] = None
        self._hist_high_price: float = 0.0
        self._start_total_btc_equiv: float = 0.0

        # V9: Blockade-Tracking
        self._last_block_reason: str = BLOCK_NONE

        # V10: Cooldown-Tracking
        self._last_trade_step: int = -100
        self._consecutive_trades: int = 0

        # V11.1: Downtrend-Pause-Gate
        self._daytrading_paused: bool = False
        self._pause_step: int = -1
        self._pause_count: int = 0

        self._prepare_volatility()
        self._prepare_ac_dc()

    # ---------------- Vorverarbeitung ----------------

    def _prepare_volatility(self, window: int = None):
        if window is None:
            window = VOLATILITY_WINDOW
        prices = self.df[self.price_col].astype(float)
        vol = prices.pct_change().rolling(window, min_periods=2).std()
        self.df["volatility"] = vol.fillna(0.0)

    def _prepare_ac_dc(self):
        """
        V11: AC/DC-Zerlegung des Preisfeldes.
        DC = MA_LONG (Grundton), AC = Preis - DC (Oberton).
        """
        prices = self.df[self.price_col].astype(float)

        # DC-Komponente
        if self.ma_long_col and self.ma_long_col in self.df.columns:
            dc = self.df[self.ma_long_col].astype(float)
        else:
            dc = prices.rolling(MA_LONG_WINDOW, min_periods=1).mean()

        # AC-Komponente
        ac = prices - dc

        # Rollierende AC-Amplitude (Peak-to-Trough über Fenster)
        ac_amp = ac.rolling(MA_LONG_WINDOW, min_periods=1).apply(
            lambda x: x.max() - x.min(), raw=True
        )

        self.df["ac_value"] = ac
        self.df["ac_amplitude"] = ac_amp
        self.df["dc_value"] = dc

    # ---------------- Basis-Fensterlogik ----------------

    def _random_start_index(self) -> int:
        n = len(self.df)
        if n <= self.window_length:
            return 0
        max_start = n - self.window_length
        return int(np.random.randint(0, max_start + 1))

    def reset(self):
        self._idx_global = self._random_start_index()
        self._steps_remaining = self.window_length

        first_price = float(self.df.loc[self._idx_global, self.price_col])
        self.portfolio = Portfolio(
            btc=self.start_btc,
            cash=self.start_cash,
            price=first_price,
        )
        self._prev_price = None
        self._hist_high_price = first_price
        self._start_total_btc_equiv = self.start_btc + (
            self.start_cash / first_price if first_price > 0 else 0
        )
        self._last_block_reason = BLOCK_NONE
        self._last_trade_step = -100
        self._consecutive_trades = 0

        # V11.1: Pause zurücksetzen
        self._daytrading_paused = False
        self._pause_step = -1
        self._pause_count = 0

        state = self._build_state()
        return state

    # ---------------- Zustandsabbildung ----------------

    def _price_change_bin(self, cur_price: float) -> str:
        if self._prev_price is None:
            return "flat"
        rel = (cur_price - self._prev_price) / max(1e-8, self._prev_price)
        if rel > 0.005:
            return "up"
        elif rel < -0.005:
            return "down"
        return "flat"

    def _position_state(self) -> str:
        if self.portfolio is None:
            return "FLAT"

        price = self.portfolio.price
        if price <= 0:
            return "FLAT" if self.portfolio.btc <= 1e-8 else "LONG"

        btc_value = self.portfolio.btc * price
        total_value = btc_value + self.portfolio.cash

        if total_value <= 0:
            return "FLAT"

        btc_share = btc_value / total_value

        if btc_share > 0.70:
            return "LONG"
        elif btc_share < 0.20:
            return "FLAT"
        return "PARTIAL"

    def _cash_share(self) -> float:
        if self.portfolio is None:
            return 0.0
        price = self.portfolio.price
        if price <= 0:
            return 0.0
        total = self.portfolio.btc * price + self.portfolio.cash
        if total <= 0:
            return 0.0
        return self.portfolio.cash / total

    def _sellable_share(self) -> float:
        if self.portfolio is None:
            return 0.0
        btc = self.portfolio.btc
        if btc <= 1e-8:
            return 0.0
        free = self._max_sellable_btc()
        return free / btc

    def _rel_to_ma(self, cur_price: float) -> tuple:
        rel_short = 0.0
        rel_long = 0.0

        if self.ma_short_col and self.ma_short_col in self.df.columns:
            ma_s = float(self.df.loc[self._idx_global, self.ma_short_col])
            if ma_s > 0:
                rel_short = (cur_price - ma_s) / ma_s

        if self.ma_long_col and self.ma_long_col in self.df.columns:
            ma_l = float(self.df.loc[self._idx_global, self.ma_long_col])
            if ma_l > 0:
                rel_long = (cur_price - ma_l) / ma_l

        return rel_short, rel_long

    def _vol_bin(self) -> str:
        v = float(self.df.loc[self._idx_global, "volatility"])
        if v < 0.01:
            return "low"
        elif v < 0.03:
            return "mid"
        return "high"

    def _regime(self, e_long: float, trend: str) -> str:
        """V10: Makro-Regime-Erkennung."""
        if trend == "uptrend" and e_long > 0.05:
            return "BULL_STRONG"
        if trend == "downtrend" and e_long < -0.05:
            return "BEAR_STRONG"
        return "NORMAL"

    def _ac_phase(self) -> tuple:
        """
        V11: AC-Phasenerkennung.
        Returns: (phase, amplitude_bin, near_zero)
        """
        ac = float(self.df.loc[self._idx_global, "ac_value"])
        amp = float(self.df.loc[self._idx_global, "ac_amplitude"])

        if amp < 0.001:
            return "flat", "narrow", False

        # Amplitude-Bin
        cur_price = float(self.df.loc[self._idx_global, self.price_col])
        rel_amp = amp / cur_price if cur_price > 0 else 0
        if rel_amp < 0.02:
            amp_bin = "narrow"
        elif rel_amp < 0.06:
            amp_bin = "normal"
        else:
            amp_bin = "wide"

        # Phase
        ac_ratio = ac / amp if amp > 0 else 0
        if ac_ratio > 0.3:
            phase = "peak"
        elif ac_ratio < -0.3:
            phase = "trough"
        else:
            phase = "transition"

        # Nulldurchgang
        near_zero = abs(ac_ratio) < 0.1

        return phase, amp_bin, near_zero

    def _energy_direction(self, e_short: float, e_long: float) -> float:
        """V10: Energierichtungsvektor (Axiom 5)."""
        return e_short - e_long

    @staticmethod
    def _prob_bin(p: float) -> str:
        if p >= 0.6:
            return "high"
        elif p >= 0.5:
            return "mid"
        elif p > 0:
            return "low"
        return "none"

    def _build_state(self) -> dict:
        cur_price = float(self.df.loc[self._idx_global, self.price_col])
        pc_bin = self._price_change_bin(cur_price)
        pos = self._position_state()
        rel_short, rel_long = self._rel_to_ma(cur_price)
        vol_bin = self._vol_bin()
        cash_share = self._cash_share()
        sellable_share = self._sellable_share()

        trend = "sideways"
        if self.trend_col is not None and self.trend_col in self.df.columns:
            trend = str(self.df.loc[self._idx_global, self.trend_col])

        regime = self._regime(rel_long, trend)
        ac_phase, ac_amp_bin, near_zero = self._ac_phase()
        energy_dir = self._energy_direction(rel_short, rel_long)

        state: dict = {
            "pos": pos,
            "pc_bin": pc_bin,
            "price": cur_price,
            "step": self.window_length - self._steps_remaining,
            "hist_high": self._hist_high_price,
            "vol_bin": vol_bin,
            "rel_ma_short": rel_short,
            "rel_ma_long": rel_long,
            "e_long": rel_long,
            "e_short": rel_short,
            "cash_share": cash_share,
            "sellable_share": sellable_share,
            "trend_bin": trend,
            "regime": regime,
            "ac_phase": ac_phase,
            "ac_amplitude_bin": ac_amp_bin,
            "near_zero": near_zero,
            "energy_dir": energy_dir,
            "daytrading_paused": self._daytrading_paused,
        }

        # Posterior-Bins (falls vorhanden)
        prob_cols = {
            "prob_res_signal_buy_1D": "prob_res_buy_1d_bin",
            "prob_res_signal_sell_1D": "prob_res_sell_1d_bin",
            "prob_trad_signal_buy_1D": "prob_trad_buy_1d_bin",
            "prob_trad_signal_sell_1D": "prob_trad_sell_1d_bin",
        }
        for col_name, state_key in prob_cols.items():
            if col_name in self.df.columns:
                raw = self.df.loc[self._idx_global, col_name]
                try:
                    p = float(raw) if raw == raw else 0.0
                except Exception:
                    p = 0.0
                state[state_key] = self._prob_bin(p)

        return state

    # ---------------- HODL-Kern / Trading-Hülle ----------------

    def _max_sellable_btc(self) -> float:
        if self.portfolio is None:
            return 0.0
        return max(0.0, self.portfolio.btc - self.hodl_core_btc)

    # ---------------- V11.1: Downtrend-Pause-Gate ----------------

    def _check_downtrend_pause(self, state: dict) -> bool:
        """
        V11.1: Downtrend-Pause-Gate.

        Resonanzfeldtheoretische Begründung:
        Wenn die DC-Komponente stark fällt (BEAR_STRONG + e_long < -5%),
        ist die AC-Schwingung nicht profitabel handelbar — die Amplitude
        wird von der fallenden DC überlagert. Jeder Trade in dieser Phase
        hat negative Erwartung nach Fees.

        Das Gate pausiert das gesamte Daytrading, nicht einzelne Trades.

        Wiederaufnahme wenn:
        - e_long > -3% (Preis nähert sich MA wieder an) ODER
        - ac_phase == "trough" (Wendepunkt im AC-Zyklus erkannt) ODER
        - regime wechselt von BEAR_STRONG zu NORMAL
        """
        trend = state.get("trend_bin", "sideways")
        e_long = float(state.get("e_long", 0.0))
        regime = state.get("regime", "NORMAL")
        ac_phase = state.get("ac_phase", "flat")

        if self._daytrading_paused:
            # === Prüfe Wiederaufnahme ===
            resume = False

            if e_long > RESUME_E_LONG_THRESHOLD:
                resume = True

            if ac_phase == RESUME_AC_PHASE:
                resume = True

            if regime != PAUSE_REGIME:
                resume = True

            if resume:
                self._daytrading_paused = False
                return False

            return True  # Weiterhin pausiert

        else:
            # === Prüfe ob Pause einsetzen soll ===
            if (trend == "downtrend"
                    and e_long < PAUSE_E_LONG_THRESHOLD
                    and regime == PAUSE_REGIME):
                self._daytrading_paused = True
                self._pause_step = self.window_length - self._steps_remaining
                self._pause_count += 1
                return True

            return False

    # ---------------- Regel-Module ----------------

    def _apply_regime_rule(self, action: str, state: dict) -> str:
        """V10: Regime-basierte Blockade."""
        regime = state.get("regime", "NORMAL")
        if regime == "BULL_STRONG" and action.startswith("SELL"):
            self._last_block_reason = BLOCK_REGIME
            return "HOLD"
        if regime == "BEAR_STRONG" and action.startswith("BUY"):
            self._last_block_reason = BLOCK_REGIME
            return "HOLD"
        return action

    def _apply_ma_sell_guard(self, action: str, state: dict) -> str:
        """
        V11: Resonanzlogischer MA-SELL-Guard.
        Blockiert SELL nur wenn unter MA UND Energie aufwärts.
        Exception: Nicht blockieren am AC-Peak.
        """
        if not action.startswith("SELL"):
            return action

        e_long = float(state.get("e_long", 0.0))
        energy_dir = float(state.get("energy_dir", 0.0))
        ac_phase = state.get("ac_phase", "flat")

        # Peak-Exception: Am AC-Peak immer SELL erlauben
        if ac_phase == "peak":
            return action

        # Unter MA UND Energie aufwärts → SELL blockieren
        if e_long < 0 and energy_dir > 0.005:
            self._last_block_reason = BLOCK_MA_SELL_GUARD
            return "HOLD"

        return action

    def _apply_ath_rule(self, action: str, cur_price: float) -> str:
        if not action.startswith("BUY"):
            return action
        if self._hist_high_price <= 0:
            return action
        threshold = self._hist_high_price * (1.0 - self.ath_buffer_pct)
        if cur_price >= threshold:
            self._last_block_reason = BLOCK_ATH
            return "HOLD"
        return action

    def _apply_trend_rule(self, action: str) -> str:
        if self.trend_col is None or self.trend_col not in self.df.columns:
            return action

        trend = str(self.df.loc[self._idx_global, self.trend_col])

        if trend == "downtrend":
            if action.startswith("BUY"):
                cur_price = float(self.df.loc[self._idx_global, self.price_col])
                e_long = 0.0
                if self.ma_long_col and self.ma_long_col in self.df.columns:
                    ma_l = float(self.df.loc[self._idx_global, self.ma_long_col])
                    if ma_l > 0:
                        e_long = (cur_price - ma_l) / ma_l

                if e_long < -0.01:
                    return action
                self._last_block_reason = BLOCK_TREND
                return "HOLD"

            if action.startswith("SELL"):
                cur_price = float(self.df.loc[self._idx_global, self.price_col])
                e_long = 0.0
                if self.ma_long_col and self.ma_long_col in self.df.columns:
                    ma_l = float(self.df.loc[self._idx_global, self.ma_long_col])
                    if ma_l > 0:
                        e_long = (cur_price - ma_l) / ma_l

                if e_long < -0.01:
                    self._last_block_reason = BLOCK_TREND
                    return "HOLD"
                return action

        return action

    def _apply_ma_rule(self, action: str, cur_price: float) -> str:
        if self.ma_short_col is None or self.ma_short_col not in self.df.columns:
            return action
        ma_val = float(self.df.loc[self._idx_global, self.ma_short_col])
        if ma_val <= 0:
            return action
        rel = (cur_price - ma_val) / ma_val
        if action.startswith("BUY") and rel > 0.05:
            self._last_block_reason = BLOCK_MA
            return "HOLD"
        if action.startswith("SELL") and rel < -0.05:
            self._last_block_reason = BLOCK_MA
            return "HOLD"
        return action

    def _apply_cooldown(self, action: str) -> str:
        """V10: Overtrading-Schutz. MEDIUM→SMALL bei zu schnellem Handeln."""
        if action == "HOLD":
            return action

        current_step = self.window_length - self._steps_remaining
        steps_since_last = current_step - self._last_trade_step

        if steps_since_last <= 2:
            self._consecutive_trades += 1
        else:
            self._consecutive_trades = max(0, self._consecutive_trades - 1)

        # Bei Overtrading: MEDIUM → SMALL
        if self._consecutive_trades >= 3:
            if action == "BUY_MEDIUM":
                self._last_block_reason = BLOCK_COOLDOWN
                return "BUY_SMALL"
            if action == "SELL_MEDIUM":
                self._last_block_reason = BLOCK_COOLDOWN
                return "SELL_SMALL"

        return action

    def _apply_balance_regler(self, action: str, state: dict) -> str:
        """V10: Balance-Regler (Axiom 2 — Kopplungsstruktur)."""
        cash_share = float(state.get("cash_share", 0.0))
        sellable_share = float(state.get("sellable_share", 1.0))

        if action.startswith("BUY") and cash_share < 0.08:
            self._last_block_reason = BLOCK_BALANCE
            return "HOLD"
        if action.startswith("SELL") and sellable_share < 0.05:
            self._last_block_reason = BLOCK_BALANCE
            return "HOLD"

        return action

    def _adjust_sell_fraction(self, base_fraction: float) -> float:
        if self.portfolio is None:
            return base_fraction
        btc = self.portfolio.btc
        if btc <= 1e-8:
            return base_fraction
        if btc < self.min_btc_for_full_sell:
            frac = min(base_fraction, self.min_btc_trade_fraction)
            return frac
        return base_fraction

    def _fraction_for_action(self, action: str) -> float:
        if action == "BUY_SMALL" or action == "SELL_SMALL":
            return self.trade_fraction_small
        if action == "BUY_MEDIUM" or action == "SELL_MEDIUM":
            return self.trade_fraction_medium
        return 0.0

    # ---------------- Schritt-Logik ----------------

    @property
    def last_block_reason(self) -> str:
        """V9: Gibt den Blockade-Grund des letzten step()-Aufrufs zurück."""
        return self._last_block_reason

    def step(self, action: str) -> tuple:
        if self.portfolio is None:
            raise RuntimeError("Env not reset")

        # V9: Blockade-Grund zurücksetzen
        self._last_block_reason = BLOCK_NONE

        cur_price = float(self.df.loc[self._idx_global, self.price_col])

        if cur_price > self._hist_high_price:
            self._hist_high_price = cur_price

        # State für Regel-Entscheidungen
        state = self._build_state()

        # === V11.1: Downtrend-Pause-Gate (VOR allen anderen Regeln) ===
        if action != "HOLD" and self._check_downtrend_pause(state):
            self._last_block_reason = BLOCK_DOWNTREND_PAUSE
            self.portfolio.price = cur_price
            self._prev_price = cur_price
            self._idx_global += 1
            self._steps_remaining -= 1
            done = (self._idx_global >= len(self.df)
                    or self._steps_remaining <= 0)
            if done:
                return {}, True
            next_state = self._build_state()
            return next_state, done

        # === Regelkette V11 ===
        effective_action = self._apply_regime_rule(action, state)
        effective_action = self._apply_ma_sell_guard(effective_action, state)
        effective_action = self._apply_ath_rule(effective_action, cur_price)
        effective_action = self._apply_trend_rule(effective_action)
        effective_action = self._apply_ma_rule(effective_action, cur_price)
        effective_action = self._apply_cooldown(effective_action)
        effective_action = self._apply_balance_regler(effective_action, state)

        self.portfolio.price = cur_price

        fraction = self._fraction_for_action(effective_action)
        if effective_action.startswith("SELL"):
            fraction = self._adjust_sell_fraction(fraction)

        if fraction <= 1e-6 or effective_action == "HOLD":
            if effective_action != "HOLD" and self._last_block_reason == BLOCK_NONE:
                self._last_block_reason = BLOCK_FRACTION_ZERO
            effective_action = "HOLD"
            fraction = 0.0

        trade_type = "HOLD"
        if effective_action.startswith("BUY"):
            trade_type = "BUY"
        elif effective_action.startswith("SELL"):
            trade_type = "SELL"

        if trade_type == "SELL":
            max_sell = self._max_sellable_btc()
            if max_sell <= 0.0:
                trade_type = "HOLD"
                fraction = 0.0
                self._last_block_reason = BLOCK_HODL_KERN
            else:
                btc_total = self.portfolio.btc
                if btc_total > 0:
                    max_fraction = max_sell / btc_total
                    fraction = min(fraction, max_fraction)
                    if fraction <= 1e-6:
                        trade_type = "HOLD"
                        fraction = 0.0
                        self._last_block_reason = BLOCK_HODL_KERN

        if trade_type == "BUY":
            if self.portfolio.cash <= 1.0:
                trade_type = "HOLD"
                fraction = 0.0
                self._last_block_reason = BLOCK_NO_CASH

        # Trade ausführen
        self.portfolio.apply_trade(
            trade_type,
            fraction=fraction,
            fee_pct=self.fee_pct,
        )

        # Cooldown-Tracking
        if trade_type != "HOLD":
            current_step = self.window_length - self._steps_remaining
            self._last_trade_step = current_step

        self._prev_price = cur_price
        self._idx_global += 1
        self._steps_remaining -= 1

        done = (
            self._idx_global >= len(self.df)
            or self._steps_remaining <= 0
        )
        if done:
            return {}, True

        next_state = self._build_state()
        return next_state, done

    def current_portfolio(self) -> Portfolio:
        if self.portfolio is None:
            raise RuntimeError("Env not reset")
        return self.portfolio