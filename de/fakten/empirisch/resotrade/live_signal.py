"""
ResoTrade V11.1 — Live-Signal-Generator mit Kraken-Integration.

V11.1-Erweiterungen:
  - Human-Hint-System: Mensch gibt Hinweise, keine Befehle
  - Erwartungsanzeige: System zeigt Prognose + Hint-Wirkung
  - Hint-Blockaden werden im Log und Erfahrungsspeicher erfasst

V9.4-Korrekturen:
  - HODL-Kern fest (nicht mehr zirkulaer)
  - State-Signatur enthaelt e_short (Bounce-Erkennung)
  - Fee aus config.KRAKEN_FEE_PCT (konsistent)

Intelligente Abtastung:
  - State-basierte Filterung (identische States werden uebersprungen)
  - Preisaenderungs-Schwelle (MIN_PRICE_CHANGE_PCT)
  - Getrennter Erfahrungsspeicher (Live vs. Offline)
"""

import csv
import time
import traceback
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import numpy as np
import pandas as pd

from config import (
    MA_SHORT_WINDOW,
    MA_LONG_WINDOW,
    VOLATILITY_WINDOW,
    LOOKBACK_HOURS,
    SIGNAL_INTERVAL_SECONDS,
    HODL_SHARE,
    TRADE_FRACTION_SMALL,
    TRADE_FRACTION_MEDIUM,
    KRAKEN_FEE_PCT,
    MIN_BTC_ORDER,
    MIN_USD_ORDER,
    MIN_CANDLES_FOR_SIGNAL,
    DRY_RUN,
    LIVE_LOG_DIR,
    MIN_PRICE_CHANGE_PCT,
    SKIP_IDENTICAL_STATES,
    PC_BIN_THRESHOLD,
)
from kraken_client import KrakenClient
from experience import (
    load_experience,
    persist_experience,
    add_experience,
    merge_status,
    EXPERIENCE_LIVE_CSV,
    EXPERIENCE_CSV,
)
from policy import (
    resonance_learning_policy,
    ma_profit_switch_policy,
    experience_confidence,
    experience_scores,
    make_chain,
)
from human_hint import load_hint, is_paused, hint_bias_adjustment

SIGNAL_LOG = LIVE_LOG_DIR / "signal_log.csv"

PERSIST_EVERY_N_CYCLES = 10
RELOAD_MERGED_EVERY_N_CYCLES = 60


def _ensure_log_dir():
    LIVE_LOG_DIR.mkdir(parents=True, exist_ok=True)


def _build_price_df(client: KrakenClient, lookback_hours: int = LOOKBACK_HOURS) -> pd.DataFrame:
    since = int(time.time()) - lookback_hours * 3600
    candles = client.get_ohlc(interval=60, since=since)

    if not candles:
        raise RuntimeError("Keine OHLC-Daten von Kraken erhalten")

    rows = []
    for c in candles:
        ts = datetime.fromtimestamp(int(c[0]), tz=timezone.utc)
        close = float(c[4])
        volume = float(c[6])
        rows.append({"ts": ts, "price": close, "volume": volume})

    df = pd.DataFrame(rows)
    df = df.sort_values("ts").reset_index(drop=True)
    df = df.drop_duplicates(subset="ts", keep="last").reset_index(drop=True)

    if len(df) < MIN_CANDLES_FOR_SIGNAL:
        print(f"[Live] Nur {len(df)} Kerzen verfuegbar, "
              f"mindestens {MIN_CANDLES_FOR_SIGNAL} empfohlen.")

    df["ma_short"] = df["price"].rolling(MA_SHORT_WINDOW, min_periods=1).mean()
    df["ma_long"] = df["price"].rolling(MA_LONG_WINDOW, min_periods=1).mean()

    vol = df["price"].pct_change().rolling(VOLATILITY_WINDOW, min_periods=2).std()
    df["volatility"] = vol.fillna(0.0)

    diff = (df["ma_short"] - df["ma_long"]) / (df["ma_long"].abs() + 1e-8)
    df["trend_bin"] = diff.apply(
        lambda x: "uptrend" if x > 0.01 else ("downtrend" if x < -0.01 else "sideways")
    )

    return df


def _build_live_state(
    df: pd.DataFrame,
    btc_balance: float,
    usd_balance: float,
    hodl_core_btc: float,
) -> dict:
    idx = len(df) - 1
    cur_price = float(df.loc[idx, "price"])

    if idx > 0:
        prev_price = float(df.loc[idx - 1, "price"])
        rel = (cur_price - prev_price) / max(1e-8, prev_price)
        if rel > PC_BIN_THRESHOLD:
            pc_bin = "up"
        elif rel < -PC_BIN_THRESHOLD:
            pc_bin = "down"
        else:
            pc_bin = "flat"
    else:
        pc_bin = "flat"

    btc_value = btc_balance * cur_price
    total_value = btc_value + usd_balance

    if total_value <= 0:
        pos = "FLAT"
        cash_share = 0.0
        sellable_share = 0.0
    else:
        btc_share = btc_value / total_value
        cash_share = usd_balance / total_value

        if btc_share > 0.70:
            pos = "LONG"
        elif btc_share < 0.20:
            pos = "FLAT"
        else:
            pos = "PARTIAL"

        free_btc = max(0.0, btc_balance - hodl_core_btc)
        sellable_share = free_btc / btc_balance if btc_balance > 1e-8 else 0.0

    ma_s = float(df.loc[idx, "ma_short"])
    ma_l = float(df.loc[idx, "ma_long"])
    rel_short = (cur_price - ma_s) / ma_s if ma_s > 0 else 0.0
    rel_long = (cur_price - ma_l) / ma_l if ma_l > 0 else 0.0

    v = float(df.loc[idx, "volatility"])
    if v < 0.01:
        vol_bin = "low"
    elif v < 0.03:
        vol_bin = "mid"
    else:
        vol_bin = "high"

    hist_high = float(df["price"].max())

    effective_step = idx
    if len(df) < MIN_CANDLES_FOR_SIGNAL:
        effective_step = min(idx, 10)

    state = {
        "pos": pos,
        "pc_bin": pc_bin,
        "price": cur_price,
        "step": effective_step,
        "hist_high": hist_high,
        "vol_bin": vol_bin,
        "rel_ma_short": rel_short,
        "rel_ma_long": rel_long,
        "e_long": rel_long,
        "e_short": rel_short,
        "cash_share": cash_share,
        "sellable_share": sellable_share,
        "trend_bin": str(df.loc[idx, "trend_bin"]),
    }

    return state


def _compute_order_volume(
    action: str,
    btc_balance: float,
    usd_balance: float,
    cur_price: float,
    hodl_core_btc: float,
) -> float:
    if action == "HOLD":
        return 0.0

    if action in ("BUY_SMALL", "SELL_SMALL"):
        fraction = TRADE_FRACTION_SMALL
    elif action in ("BUY_MEDIUM", "SELL_MEDIUM"):
        fraction = TRADE_FRACTION_MEDIUM
    else:
        return 0.0

    if action.startswith("BUY"):
        available_usd = usd_balance * fraction
        if available_usd < MIN_USD_ORDER:
            return 0.0
        if cur_price <= 0:
            return 0.0
        btc_to_buy = (available_usd * (1.0 - KRAKEN_FEE_PCT)) / cur_price
        return btc_to_buy

    if action.startswith("SELL"):
        free_btc = max(0.0, btc_balance - hodl_core_btc)
        if free_btc < MIN_BTC_ORDER:
            return 0.0
        btc_to_sell = free_btc * fraction
        if btc_to_sell < MIN_BTC_ORDER:
            return 0.0
        return btc_to_sell

    return 0.0


def _evaluate_live_step(
    btc_before: float,
    usd_before: float,
    btc_after: float,
    usd_after: float,
    price_before: float,
    price_after: float,
) -> str:
    if price_before <= 0 or price_after <= 0:
        return "draw"

    btc_equiv_actual = btc_after + usd_after / price_after
    btc_equiv_hold = btc_before + usd_before / price_after

    delta = btc_equiv_actual - btc_equiv_hold

    btc_equiv_before = btc_before + usd_before / price_before
    threshold = max(1e-8, btc_equiv_before * 1e-5)

    if delta > threshold:
        return "success"
    elif delta < -threshold:
        return "failure"
    return "draw"


def _state_signature(state: dict) -> str:
    e_long = state.get("e_long", 0.0)
    e_long_binned = round(e_long / 0.005) * 0.005

    e_short = state.get("e_short", 0.0)
    e_short_binned = round(e_short / 0.005) * 0.005

    cash = state.get("cash_share", 0.0)
    cash_binned = round(cash / 0.01) * 0.01

    sell = state.get("sellable_share", 0.0)
    sell_binned = round(sell / 0.05) * 0.05

    return (
        f"{state.get('pos', '?')}|"
        f"{state.get('pc_bin', '?')}|"
        f"{state.get('trend_bin', '?')}|"
        f"{state.get('vol_bin', '?')}|"
        f"{e_long_binned:.3f}|"
        f"{e_short_binned:.3f}|"
        f"{cash_binned:.2f}|"
        f"{sell_binned:.2f}"
    )


def _log_signal(
    timestamp: str,
    state: dict,
    action: str,
    rule_action: str,
    confidence: float,
    volume_btc: float,
    btc_balance: float,
    usd_balance: float,
    order_result: Optional[dict] = None,
    live_eval: str = "",
    skipped: bool = False,
    hint_info: str = "",
):
    _ensure_log_dir()
    file_exists = SIGNAL_LOG.exists()
    with SIGNAL_LOG.open("a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow([
                "timestamp", "price", "pos", "trend", "e_long", "vol_bin",
                "cash_share", "sellable_share",
                "rule_action", "final_action", "confidence",
                "volume_btc", "btc_balance", "usd_balance",
                "order_status", "live_eval", "skipped", "hint_info",
            ])
        writer.writerow([
            timestamp,
            f"{state.get('price', 0.0):.2f}",
            state.get("pos", "?"),
            state.get("trend_bin", "?"),
            f"{state.get('e_long', 0.0):.6f}",
            state.get("vol_bin", "?"),
            f"{state.get('cash_share', 0.0):.4f}",
            f"{state.get('sellable_share', 0.0):.4f}",
            rule_action,
            action,
            f"{confidence:.4f}",
            f"{volume_btc:.8f}",
            f"{btc_balance:.8f}",
            f"{usd_balance:.2f}",
            order_result.get("status", "none") if order_result else "none",
            live_eval,
            "yes" if skipped else "no",
            hint_info,
        ])


# ================================================================
# V11.1: Erwartungsanzeige
# ================================================================

def expectation():
    """
    Zeigt dem Menschen, was das System aktuell erwartet,
    und welchen Effekt ein gesetzter Hint haette.

    Aufruf: python live_signal.py expectation
    """
    client = KrakenClient()
    exp = load_experience()
    hint = load_hint()

    # Daten + State bauen
    df = _build_price_df(client)
    btc, usd = client.get_btc_usd_balance()
    cur_price = float(df["price"].iloc[-1])
    hodl_core = btc * HODL_SHARE

    state = _build_live_state(df, btc, usd, hodl_core)

    # Policy-Entscheidung
    action = resonance_learning_policy(state, exp, epsilon=0.0)
    rule_action = ma_profit_switch_policy(state)
    scores = experience_scores(state, exp)
    confidence = experience_confidence(scores)

    # Scores fuer Erwartung
    s_buy = scores.get("BUY_SMALL", {}).get("success", 0)
    f_buy = scores.get("BUY_SMALL", {}).get("failure", 0)
    s_sell = scores.get("SELL_SMALL", {}).get("success", 0)
    f_sell = scores.get("SELL_SMALL", {}).get("failure", 0)

    buy_wr = s_buy / max(1, s_buy + f_buy)
    sell_wr = s_sell / max(1, s_sell + f_sell)

    trend = state.get("trend_bin", "unknown")

    # Erwartung ableiten
    if sell_wr > buy_wr + 0.05 and trend == "downtrend":
        exp_dir = "FALLEND"
        conf_pct = min(95, int((sell_wr - buy_wr) * 200 + 50))
    elif buy_wr > sell_wr + 0.05 and trend == "uptrend":
        exp_dir = "STEIGEND"
        conf_pct = min(95, int((buy_wr - sell_wr) * 200 + 50))
    else:
        exp_dir = "SEITWAERTS"
        conf_pct = max(30, int(50 - abs(buy_wr - sell_wr) * 100))

    total_value = btc * cur_price + usd

    print("")
    print("============================================================")
    print("ResoTrade V11.1 - Live-Erwartung")
    print("============================================================")
    print(f"  Preis:          {cur_price:.2f} USD")
    print(f"  Trend:          {trend}")
    print(f"  e_long:         {state.get('e_long', 0) * 100:+.2f}%")
    print(f"  e_short:        {state.get('e_short', 0) * 100:+.2f}%")
    print(f"  Volatilitaet:   {state.get('vol_bin', '?')}")
    print(f"  Position:       {state.get('pos', '?')}")
    print(f"  Portfolio:      {btc:.8f} BTC + {usd:.2f} USD = {total_value:.2f} USD")
    print(f"")
    print(f"  ERWARTUNG:      {exp_dir} (Konfidenz: {conf_pct}%)")
    print(f"  Buy-Winrate:    {buy_wr:.3f}")
    print(f"  Sell-Winrate:   {sell_wr:.3f}")
    print(f"")
    print(f"  Regel-Vorschlag: {rule_action}")
    print(f"  Policy-Aktion:   {action} (Konfidenz: {confidence:.3f})")
    print(f"")

    # Hint-Status und Wirkung
    if hint:
        bias = hint.get("bias", "neutral").upper()
        reason = hint.get("reason", "-")
        weight = hint.get("weight", 0.3)
        print(f"  --- Human Hint AKTIV ---")
        print(f"  Bias:           {bias}")
        print(f"  Gewicht:        {weight}")
        print(f"  Grund:          {reason}")

        if is_paused(hint):
            print(f"  PAUSE:          aktiv bis {hint['pause_until']}")
            print(f"  Wirkung:        {action} -> HOLD (Pause)")
        else:
            adj_action, adj_reason = hint_bias_adjustment(hint, action, trend)
            if adj_action != action:
                print(f"  Wirkung:        {action} -> {adj_action}")
                print(f"                  ({adj_reason})")
            else:
                print(f"  Wirkung:        keine (Aktion passt zum Hint)")
    else:
        print(f"  Human Hint:     KEINER (System autonom)")

    print(f"")
    print("============================================================")
    print("")
    print("Hinweis setzen:")
    print('  python human_hint.py bullish "EZB senkt Zinsen"')
    print('  python human_hint.py bearish "SEC verklagt Boerse" 0.5')
    print('  python human_hint.py pause 12 "FOMC in 6h"')
    print("  python human_hint.py status")
    print("  python human_hint.py clear")
    print("")


# ================================================================
# V11.1: run_once mit Hint-Integration
# ================================================================

def run_once(
    client: Optional[KrakenClient] = None,
    exp: Optional[dict] = None,
    live_exp: Optional[dict] = None,
    prev_cycle: Optional[dict] = None,
    last_state_sig: Optional[str] = None,
    last_price: Optional[float] = None,
    hodl_core_btc: Optional[float] = None,
) -> dict:
    """
    Einzelner Signal-Zyklus mit intelligenter Abtastung.

    V11.1: Human-Hint wird nach Policy-Entscheidung geprueft.
    Der Hint modifiziert die Aktion als Hinweis, nicht als Befehl.
    Hint-Blockaden werden im Log erfasst.
    """
    if client is None:
        client = KrakenClient()
    if exp is None:
        exp = load_experience()
    if live_exp is None:
        live_exp = load_experience(path=EXPERIENCE_LIVE_CSV)

    now = datetime.now(timezone.utc).isoformat()

    # 1. Daten holen
    print(f"\n[Live] {now} -- Hole Daten von Kraken...")
    df = _build_price_df(client)
    cur_price = float(df["price"].iloc[-1])
    print(f"[Live] {len(df)} Kerzen geladen, letzter Preis: {cur_price:.2f}")

    # 2. Portfolio holen
    btc_balance, usd_balance = client.get_btc_usd_balance()
    total_value = btc_balance * cur_price + usd_balance

    if total_value <= 0:
        print("[Live] Portfolio-Wert ist 0 -- ueberspringe Zyklus")
        return {
            "timestamp": now, "action": "HOLD", "rule_action": "HOLD",
            "volume_btc": 0.0, "confidence": 0.0, "state": {},
            "order_result": None, "btc_balance": btc_balance,
            "usd_balance": usd_balance, "price": cur_price,
            "chain": None, "state_sig": None, "skipped": True,
        }

    if hodl_core_btc is None:
        hodl_core_btc = btc_balance * HODL_SHARE

    # 3. State bauen
    state = _build_live_state(df, btc_balance, usd_balance, hodl_core_btc)
    state_sig = _state_signature(state)

    # 4. Intelligente Filterung: State geaendert?
    if SKIP_IDENTICAL_STATES and last_state_sig is not None:
        state_changed = (state_sig != last_state_sig)

        price_changed = True
        if last_price is not None and last_price > 0:
            price_delta_pct = abs(cur_price - last_price) / last_price
            price_changed = (price_delta_pct >= MIN_PRICE_CHANGE_PCT)

        if not state_changed and not price_changed:
            print(f"[Live] State unveraendert, Preis < {MIN_PRICE_CHANGE_PCT*100:.1f}% "
                  f"-- ueberspringe Zyklus")
            _log_signal(
                now, state, "HOLD", "HOLD", 0.0, 0.0,
                btc_balance, usd_balance, skipped=True,
            )
            return {
                "timestamp": now, "action": "HOLD", "rule_action": "HOLD",
                "volume_btc": 0.0, "confidence": 0.0, "state": state,
                "order_result": None, "btc_balance": btc_balance,
                "usd_balance": usd_balance, "price": cur_price,
                "chain": None, "state_sig": state_sig, "skipped": True,
            }

        if state_changed:
            print(f"[Live] State geaendert -> Neubewertung")
        else:
            print(f"[Live] Preis {price_delta_pct*100:.2f}% -> Neubewertung")

    print(f"[Live] Portfolio: {btc_balance:.8f} BTC + {usd_balance:.2f} USD "
          f"= {total_value:.2f} USD total")
    print(f"[Live] HODL-Kern (fest): {hodl_core_btc:.8f} BTC "
          f"(Frei: {max(0.0, btc_balance - hodl_core_btc):.8f} BTC)")

    # 5. Vorherigen Zyklus bewerten
    live_eval = ""
    if (prev_cycle is not None
            and prev_cycle.get("chain") is not None
            and not prev_cycle.get("skipped", False)):
        live_eval = _evaluate_live_step(
            btc_before=prev_cycle["btc_balance"],
            usd_before=prev_cycle["usd_balance"],
            btc_after=btc_balance,
            usd_after=usd_balance,
            price_before=prev_cycle["price"],
            price_after=cur_price,
        )
        add_experience(prev_cycle["chain"], live_eval, live_exp)
        print(f"[Live] Bewertung vorheriger Zyklus: {live_eval} "
              f"(Aktion war: {prev_cycle['action']})")

    # 6. Policy abfragen
    action = resonance_learning_policy(state, exp, epsilon=0.0)
    rule_action = ma_profit_switch_policy(state)
    scores = experience_scores(state, exp)
    confidence = experience_confidence(scores)

    print(f"[Live] State: pos={state['pos']}, trend={state['trend_bin']}, "
          f"e_long={state['e_long']:.4f}, vol={state['vol_bin']}, "
          f"cash={state['cash_share']:.2%}, sellable={state['sellable_share']:.2%}")
    print(f"[Live] Regel-Vorschlag: {rule_action}")
    print(f"[Live] Policy-Aktion:   {action} (Konfidenz: {confidence:.3f})")

    # ============================================================
    # V11.1: Human Hint Integration
    # ============================================================
    hint = load_hint()
    hint_info = ""
    original_action = action

    if hint is not None:
        trend = state.get("trend_bin", "sideways")
        action, hint_reason = hint_bias_adjustment(hint, action, trend)

        if hint_reason:
            hint_info = hint_reason
            print(f"[Hint] {original_action} -> {action} ({hint_reason})")
            print(f"[Hint] Grund: {hint.get('reason', '-')}")
        else:
            bias = hint.get("bias", "neutral")
            print(f"[Hint] Aktiv ({bias}), keine Aenderung fuer {action}")

    # Chain wird mit der FINALEN Aktion gebaut (nach Hint)
    chain = make_chain(state, action)

    # 7. Order-Volumen
    volume_btc = _compute_order_volume(
        action, btc_balance, usd_balance, cur_price, hodl_core_btc
    )

    # 8. Order platzieren
    order_result = None
    if action != "HOLD" and volume_btc > 0:
        side = "buy" if action.startswith("BUY") else "sell"
        print(f"[Live] -> {side.upper()} {volume_btc:.8f} BTC "
              f"(= {volume_btc * cur_price:.2f} USD)")
        order_result = client.place_order(
            side=side,
            volume_btc=volume_btc,
            order_type="market",
        )
    else:
        if action == "HOLD":
            if hint_info:
                print(f"[Live] -> HOLD (durch Hint: {hint_info})")
            else:
                print("[Live] -> HOLD -- kein Trade")
        else:
            print(f"[Live] -> {action} -- Volume zu klein, uebersprungen")

    # 9. Loggen (mit Hint-Info)
    _log_signal(
        now, state, action, rule_action, confidence,
        volume_btc, btc_balance, usd_balance, order_result,
        live_eval, skipped=False, hint_info=hint_info,
    )

    return {
        "timestamp": now,
        "action": action,
        "rule_action": rule_action,
        "volume_btc": volume_btc,
        "confidence": confidence,
        "state": state,
        "order_result": order_result,
        "btc_balance": btc_balance,
        "usd_balance": usd_balance,
        "price": cur_price,
        "chain": chain,
        "state_sig": state_sig,
        "skipped": False,
    }


def run_loop(interval_seconds: int = SIGNAL_INTERVAL_SECONDS):
    """
    Endlosschleife mit intelligenter Abtastung.
    V11.1: Prueft jeden Zyklus auf Human Hints.
    """
    _ensure_log_dir()
    client = KrakenClient()
    dry_str = " [DRY RUN]" if DRY_RUN else " [LIVE]"

    print(f"\n{'=' * 60}")
    print(f"ResoTrade V11.1 -- Live-Signal-Loop{dry_str}")
    print(f"{'=' * 60}")
    print(f"  Abtastintervall:   {interval_seconds}s ({interval_seconds / 60:.0f} min)")
    print(f"  HODL-Share:        {HODL_SHARE * 100:.0f}%")
    print(f"  Live-Lernen:       AKTIV (getrennte Speicher)")
    print(f"  State-Filter:      {'AN' if SKIP_IDENTICAL_STATES else 'AUS'}")
    print(f"  Min Preis-Delta:   {MIN_PRICE_CHANGE_PCT * 100:.1f}%")
    print(f"  pc_bin-Schwelle:   {PC_BIN_THRESHOLD * 100:.1f}%")
    print(f"  Human-Hint:        AKTIV (prueft data/human_hint.json)")
    print(f"{'=' * 60}")

    # Verbindungstest
    try:
        btc, usd = client.get_btc_usd_balance()
        ticker = client.get_ticker()
        print(f"\n  Kraken-Verbindung OK")
        print(f"   BTC: {btc:.8f}")
        print(f"   USD: {usd:.2f}")
        print(f"   BTC/USD: {ticker['last']:.2f}")
    except Exception as e:
        print(f"\n  Kraken-Verbindung fehlgeschlagen: {e}")
        return

    # Speicher laden
    exp = load_experience()
    live_exp = load_experience(path=EXPERIENCE_LIVE_CSV)
    print(f"   Merged-Speicher: {len(exp)} Eintraege")
    print(f"   Live-Speicher:   {len(live_exp)} Eintraege")

    if not exp and not live_exp:
        print("   Beide Speicher leer -- Policy nutzt nur Regelwissen.")

    # HODL-Kern einmalig fest berechnen
    hodl_core_btc = btc * HODL_SHARE
    print(f"   HODL-Kern (fest): {hodl_core_btc:.8f} BTC "
          f"({HODL_SHARE*100:.0f}% von {btc:.8f})")

    # Hint-Status beim Start anzeigen
    hint = load_hint()
    if hint:
        print(f"\n   Human Hint AKTIV: {hint.get('bias', '?').upper()} "
              f"(w={hint.get('weight', 0.3)}) "
              f"-- {hint.get('reason', '-')}")
    else:
        print(f"\n   Human Hint: keiner gesetzt (System autonom)")

    print(f"\n   Speicher-Architektur:")
    print(f"   Policy liest:    {EXPERIENCE_CSV.name}")
    print(f"   Live schreibt:   {EXPERIENCE_LIVE_CSV.name}")
    print(f"   Persist alle:    {PERSIST_EVERY_N_CYCLES} Zyklen")
    print(f"   Reload merged:   {RELOAD_MERGED_EVERY_N_CYCLES} Zyklen")

    cycle = 0
    skipped_count = 0
    active_count = 0
    hint_block_count = 0
    prev_cycle: Optional[dict] = None
    last_state_sig: Optional[str] = None
    last_price: Optional[float] = None

    while True:
        cycle += 1
        print(f"\n{'--' * 15} Zyklus {cycle} "
              f"(aktiv:{active_count}, skip:{skipped_count}, "
              f"hint-block:{hint_block_count}) "
              f"{'--' * 5}")
        try:
            result = run_once(
                client, exp=exp, live_exp=live_exp,
                prev_cycle=prev_cycle,
                last_state_sig=last_state_sig,
                last_price=last_price,
                hodl_core_btc=hodl_core_btc,
            )

            # State-Tracking aktualisieren
            last_state_sig = result.get("state_sig")
            last_price = result.get("price")

            if result.get("skipped", False):
                skipped_count += 1
            else:
                active_count += 1
                prev_cycle = result

            # V11.1: Hint-Blockaden zaehlen (fuer Statistik)
            # Pruefen ob im Log hint_info steht
            hint_check = load_hint()
            if hint_check and not result.get("skipped", False):
                # Hint war aktiv in diesem Zyklus
                pass  # hint_info ist im result nicht direkt, aber im Log

            # Live-Speicher periodisch sichern
            if cycle % PERSIST_EVERY_N_CYCLES == 0:
                persist_experience(live_exp, path=EXPERIENCE_LIVE_CSV)
                print(f"[Live] Live-Speicher gesichert "
                      f"({len(live_exp)} Eintraege)")

            # Merged-Speicher periodisch neu laden
            if cycle % RELOAD_MERGED_EVERY_N_CYCLES == 0:
                exp = load_experience()
                print(f"[Live] Merged-Speicher neu geladen "
                      f"({len(exp)} Eintraege)")
                merge_status()
                if (active_count + skipped_count) > 0:
                    print(f"[Live] Effizienz: {active_count} aktiv / "
                          f"{skipped_count} uebersprungen "
                          f"= {active_count/(active_count+skipped_count)*100:.0f}% "
                          f"Nutzrate")

                # V11.1: Hint-Status bei jedem Reload anzeigen
                hint_reload = load_hint()
                if hint_reload:
                    print(f"[Hint] Aktiv: {hint_reload.get('bias', '?').upper()} "
                          f"(w={hint_reload.get('weight', 0.3)}) "
                          f"-- {hint_reload.get('reason', '-')}")

        except KeyboardInterrupt:
            print("\n[Live] Beendet durch Benutzer.")
            persist_experience(live_exp, path=EXPERIENCE_LIVE_CSV)
            print(f"[Live] Live-Speicher gesichert ({len(live_exp)} Eintraege)")
            print(f"[Live] Gesamt: {active_count} aktive / "
                  f"{skipped_count} uebersprungene Zyklen")
            break
        except Exception as e:
            print(f"[Live] Fehler im Zyklus {cycle}: {e}")
            traceback.print_exc()
            prev_cycle = None

        try:
            print(f"[Live] Naechster Zyklus in {interval_seconds}s...")
            time.sleep(interval_seconds)
        except KeyboardInterrupt:
            print("\n[Live] Beendet durch Benutzer.")
            persist_experience(live_exp, path=EXPERIENCE_LIVE_CSV)
            print(f"[Live] Live-Speicher gesichert ({len(live_exp)} Eintraege)")
            print(f"[Live] Gesamt: {active_count} aktive / "
                  f"{skipped_count} uebersprungene Zyklen")
            break


def status():
    """Zeigt aktuellen Kraken-Status, letztes Signal, Hint-Status und Speicher-Status."""
    client = KrakenClient()

    print(f"\n{'=' * 50}")
    print("ResoTrade V11.1 -- Kraken Status")
    print(f"{'=' * 50}")

    btc, usd = client.get_btc_usd_balance()
    ticker = client.get_ticker()
    cur_price = ticker["last"]
    total = btc * cur_price + usd
    hodl_core = btc * HODL_SHARE

    print(f"\nPortfolio:")
    print(f"  BTC:        {btc:.8f} (= {btc * cur_price:.2f} USD)")
    print(f"  USD:        {usd:.2f}")
    print(f"  Total:      {total:.2f} USD")
    print(f"  BTC-Anteil: {(btc * cur_price / total * 100) if total > 0 else 0:.1f}%")

    print(f"\nHODL-Kern:")
    print(f"  Kern:       {hodl_core:.8f} BTC ({HODL_SHARE * 100:.0f}%)")
    print(f"  Frei:       {max(0.0, btc - hodl_core):.8f} BTC")

    print(f"\nMarkt:")
    print(f"  BTC/USD:    {cur_price:.2f}")
    print(f"  Bid/Ask:    {ticker['bid']:.2f} / {ticker['ask']:.2f}")
    print(f"  Spread:     {(ticker['ask'] - ticker['bid']):.2f} "
          f"({(ticker['ask'] - ticker['bid']) / cur_price * 100:.3f}%)")
    print(f"  24h Vol:    {ticker['volume_24h']:.2f} BTC")

    # V11.1: Human Hint Status
    hint = load_hint()
    print(f"\nHuman Hint:")
    if hint:
        from datetime import timedelta
        ts = datetime.fromisoformat(hint["timestamp"])
        now = datetime.now(timezone.utc)
        age = now - ts
        remaining = timedelta(hours=48) - age
        print(f"  Status:     AKTIV")
        print(f"  Bias:       {hint.get('bias', '?').upper()}")
        print(f"  Gewicht:    {hint.get('weight', 0.3)}")
        print(f"  Grund:      {hint.get('reason', '-')}")
        print(f"  Alter:      {age.total_seconds()/3600:.1f}h")
        print(f"  Verbleibt:  {max(0, remaining.total_seconds()/3600):.1f}h")
        if is_paused(hint):
            print(f"  PAUSE:      aktiv bis {hint['pause_until']}")
    else:
        print(f"  Status:     KEINER (System autonom)")

    # Letztes Signal
    if SIGNAL_LOG.exists():
        try:
            df = pd.read_csv(SIGNAL_LOG)
            if not df.empty:
                last = df.iloc[-1]
                print(f"\nLetztes Signal:")
                print(f"  Zeit:       {last.get('timestamp', '?')}")
                print(f"  Aktion:     {last.get('final_action', '?')}")
                print(f"  Regel:      {last.get('rule_action', '?')}")
                print(f"  Konfidenz:  {last.get('confidence', '?')}")
                print(f"  Volume:     {last.get('volume_btc', '?')} BTC")
                print(f"  Status:     {last.get('order_status', '?')}")
                if "live_eval" in df.columns:
                    print(f"  Bewertung:  {last.get('live_eval', '?')}")
                if "skipped" in df.columns:
                    print(f"  Skip:       {last.get('skipped', '?')}")
                if "hint_info" in df.columns:
                    hi = last.get("hint_info", "")
                    if hi and str(hi) != "nan" and str(hi).strip():
                        print(f"  Hint:       {hi}")
                print(f"\n  Signale gesamt: {len(df)}")

                if "skipped" in df.columns:
                    active = len(df[df["skipped"] != "yes"])
                    skipped = len(df[df["skipped"] == "yes"])
                    print(f"  Davon aktiv:     {active}")
                    print(f"  Davon skip:      {skipped}")
                    if active + skipped > 0:
                        print(f"  Nutzrate:        "
                              f"{active / (active + skipped) * 100:.0f}%")

                # V11.1: Hint-Statistik im Log
                if "hint_info" in df.columns:
                    hint_entries = df[
                        df["hint_info"].notna()
                        & (df["hint_info"] != "")
                        & (df["hint_info"].astype(str).str.strip() != "")
                    ]
                    if len(hint_entries) > 0:
                        print(f"\n  Hint-Blockaden gesamt: {len(hint_entries)}")

                if "live_eval" in df.columns:
                    evals = df["live_eval"].value_counts().to_dict()
                    total_evals = sum(
                        v for k, v in evals.items()
                        if k in ("success", "failure", "draw")
                    )
                    if total_evals > 0:
                        print(f"\n  Live-Lern-Statistik:")
                        for k in ("success", "failure", "draw"):
                            cnt = evals.get(k, 0)
                            pct = cnt / total_evals * 100
                            print(f"    {k:10s}: {cnt:5d} ({pct:.1f}%)")
                        s = evals.get("success", 0)
                        f_cnt = evals.get("failure", 0)
                        ratio = f"{s / f_cnt:.2f} : 1" if f_cnt > 0 else "inf : 1"
                        print(f"    S:F Ratio: {ratio}")
        except Exception:
            pass

    # Speicher-Status
    print(f"\nErfahrungsspeicher:")
    merge_status()

    print(f"\nKonfiguration:")
    print(f"  Modus:          {'DRY RUN' if DRY_RUN else 'LIVE'}")
    print(f"  Intervall:      {SIGNAL_INTERVAL_SECONDS}s "
          f"({SIGNAL_INTERVAL_SECONDS / 60:.0f} min)")
    print(f"  State-Filter:   {'AN' if SKIP_IDENTICAL_STATES else 'AUS'}")
    print(f"  Min Preis-Delta: {MIN_PRICE_CHANGE_PCT * 100:.1f}%")
    print(f"  pc_bin-Schwelle: {PC_BIN_THRESHOLD * 100:.1f}%")
    print(f"  Human-Hint:     AKTIV")


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        cmd = sys.argv[1].lower()
        if cmd == "status":
            status()
        elif cmd == "expectation":
            expectation()
        elif cmd == "once":
            result = run_once()
        elif cmd == "loop":
            interval = int(sys.argv[2]) if len(sys.argv) > 2 else SIGNAL_INTERVAL_SECONDS
            run_loop(interval_seconds=interval)
        elif cmd == "merge":
            print("Manueller Merge: Offline + Live -> Weighted")
            from experience import merge_experience
            merge_experience()
            merge_status()
        elif cmd == "speicher":
            print("Speicher-Status:")
            merge_status()
        else:
            print(f"Unbekannter Befehl: {cmd}")
            print("Nutzung: python live_signal.py [status|expectation|once|loop|merge|speicher]")
    else:
        print("ResoTrade V11.1 -- Live-Signal mit Human-Hint-System")
        print("Nutzung:")
        print("  python live_signal.py status       -- Kraken + Hint + Speicher-Info")
        print("  python live_signal.py expectation   -- System-Erwartung + Hint-Wirkung")
        print("  python live_signal.py once          -- Ein Signal-Zyklus")
        print("  python live_signal.py loop          -- Endlos-Schleife")
        print("  python live_signal.py loop 900      -- Endlos-Schleife (15 min)")
        print("  python live_signal.py merge         -- Manueller Merge Offline+Live")
        print("  python live_signal.py speicher      -- Speicher-Status anzeigen")
        print(f"\n  Modus:          {'DRY RUN' if DRY_RUN else 'LIVE'}")
        print(f"  Intervall:      {SIGNAL_INTERVAL_SECONDS}s")
        print(f"  Human-Hint:     AKTIV")
        print("")
        print("Hint setzen:")
        print('  python human_hint.py bullish "Grund"')
        print('  python human_hint.py bearish "Grund" 0.5')
        print('  python human_hint.py pause 12 "FOMC"')
        print("  python human_hint.py status")
        print("  python human_hint.py clear")