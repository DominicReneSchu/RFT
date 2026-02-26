"""
debug_resotrade.py — Diagnose-Sonden für ResoTrade V11.1
Verifiziert alle V9.4-Fixes + V10-Erweiterungen + V11.1 Downtrend-Pause-Gate.
Ausführen: python debug_resotrade.py
"""
import numpy as np
import pandas as pd
import random
import math
import inspect
import importlib


def header(num, title):
    print(f"\n{'=' * 60}")
    print(f"SONDE {num}: {title}")
    print(f"{'=' * 60}")


# ============================================================
# SONDE 1: Fee-Konsistenz (3-Wege) — Bug #1
# ============================================================
def probe_fee_consistency():
    header(1, "Fee-Konsistenz (3-Wege)")
    from resonance_analysis import ALPHA
    from config import KRAKEN_FEE_PCT

    train_src = inspect.getsource(importlib.import_module('train_offline'))
    uses_config_fee = 'KRAKEN_FEE_PCT' in train_src and 'fee_pct=0.001' not in train_src

    fees = {
        'config (Live)': KRAKEN_FEE_PCT,
        'resonance_analysis (ALPHA/2)': ALPHA / 2,
    }

    all_match = True
    print(f"  {'Quelle':<30s} {'Fee':>8s} {'vs Config':>10s}")
    print(f"  {'-'*30} {'-'*8} {'-'*10}")
    for name, fee in fees.items():
        ratio = fee / KRAKEN_FEE_PCT if KRAKEN_FEE_PCT > 0 else float('inf')
        ok = abs(ratio - 1.0) < 0.01
        if not ok:
            all_match = False
        print(f"  {name:<30s} {fee*100:>7.3f}% {ratio:>9.2f}x {'✓' if ok else '⚠'}")

    print(f"\n  train_offline nutzt KRAKEN_FEE_PCT: {uses_config_fee}")
    if not uses_config_fee:
        all_match = False

    print(f"\n  {'✅ GEFIXT: Alle Fees konsistent' if all_match else '❌ Fees divergieren noch'}")


# ============================================================
# SONDE 2: HODL-Kern nicht zirkulär — Bug #2
# ============================================================
def probe_hodl_core_fixed():
    header(2, "HODL-Kern nicht zirkulär")
    from live_signal import run_once
    sig = inspect.signature(run_once)

    has_param = 'hodl_core_btc' in sig.parameters
    print(f"  run_once hat hodl_core_btc Parameter: {has_param}")

    src = inspect.getsource(run_once)
    has_fallback = 'if hodl_core_btc is None:' in src
    print(f"  Fallback bei None vorhanden:          {has_fallback}")

    from live_signal import run_loop
    loop_src = inspect.getsource(run_loop)
    passes_hodl = 'hodl_core_btc=hodl_core_btc' in loop_src
    print(f"  run_loop übergibt festen Wert:        {passes_hodl}")

    ok = has_param and has_fallback and passes_hodl
    print(f"\n  {'✅ GEFIXT: HODL-Kern fest' if ok else '❌ HODL-Kern noch zirkulär'}")


# ============================================================
# SONDE 3: Volatilitäts-Fenster konsistent — Bug #3
# ============================================================
def probe_volatility_window():
    header(3, "Volatilitäts-Fenster Env vs. Config")
    from config import VOLATILITY_WINDOW
    from env import TradingEnv

    src = inspect.getsource(TradingEnv._prepare_volatility)
    uses_config = 'VOLATILITY_WINDOW' in src
    has_hardcoded = 'window: int = 10' in src or 'window=10' in src

    print(f"  Config VOLATILITY_WINDOW:     {VOLATILITY_WINDOW}")
    print(f"  Env nutzt VOLATILITY_WINDOW:  {uses_config}")
    print(f"  Env hat hartkodierte 10:      {has_hardcoded}")

    ok = uses_config and not has_hardcoded
    print(f"\n  {'✅ GEFIXT: Fenster konsistent' if ok else '❌ Fenster divergieren noch'}")


# ============================================================
# SONDE 4: window_length nicht überschrieben — Bug #4
# ============================================================
def probe_window_length():
    header(4, "window_length Override entfernt")
    from train_offline import run_long_episode
    src = inspect.getsource(run_long_episode)
    has_override = 'env.window_length = len(env.df)' in src

    print(f"  Override vorhanden: {has_override}")
    print(f"\n  {'❌ Override noch aktiv' if has_override else '✅ GEFIXT: window_length wirksam'}")


# ============================================================
# SONDE 5: e_short in State-Signatur — Bug #5
# ============================================================
def probe_state_signature():
    header(5, "State-Signatur enthält e_short")
    from live_signal import _state_signature

    base = {'pos': 'LONG', 'pc_bin': 'down', 'trend_bin': 'downtrend',
            'vol_bin': 'mid', 'e_long': -0.015, 'e_short': 0.002,
            'cash_share': 0.30, 'sellable_share': 0.80}
    bounce = {**base, 'e_short': 0.025}

    sig_base = _state_signature(base)
    sig_bounce = _state_signature(bounce)
    different = sig_base != sig_bounce

    print(f"  Base  e_short=0.002: {sig_base}")
    print(f"  Bounce e_short=0.025: {sig_bounce}")
    print(f"  Signaturen verschieden: {different}")
    print(f"\n  {'✅ GEFIXT: Bounce erkannt' if different else '❌ Bounce noch verschluckt'}")


# ============================================================
# SONDE 6: V11.1 Regime-Rule + MA-SELL-Guard
# ============================================================
def probe_ma_sell_guard_v10():
    header(6, "V11.1 Regime-Rule + MA-SELL-Guard")
    from env import TradingEnv

    n = 200

    # --- Szenario A: BEAR_STRONG + BUY → blockiert ---
    # e_long muss < -5% sein → Preis 90000, MA_LONG 100000 → e_long = -10%
    prices_a = [90000.0] * n
    df_a = pd.DataFrame({
        'price': prices_a,
        'ma_short': [89000.0] * n,
        'ma_long': [100000.0] * n,  # e_long = -10% → BEAR_STRONG
        'trend_bin': ['downtrend'] * n,
    })

    env_a = TradingEnv(df_a, start_btc=1.0, start_cash=10000.0,
                       fee_pct=0.0026, trend_col='trend_bin', hodl_core_btc=0.1)
    env_a.window_length = n
    env_a.reset()

    tested_a = 0
    blocked_a = 0
    for i in range(10, min(50, n - 1)):
        env_a._idx_global = i
        env_a._steps_remaining = n - i
        env_a._last_block_reason = "none"

        sig = inspect.signature(env_a._apply_regime_rule)
        params = list(sig.parameters.keys())

        if 'state' in params:
            state = env_a._build_state()
            # Verifiziere dass Regime tatsächlich BEAR_STRONG ist
            if tested_a == 0:
                print(f"  [Debug] Szenario A regime={state.get('regime')}, "
                      f"e_long={state.get('e_long', 0):.4f}")
            result = env_a._apply_regime_rule("BUY_SMALL", state)
        else:
            result = env_a._apply_regime_rule("BUY_SMALL")

        tested_a += 1
        if result == "HOLD":
            blocked_a += 1

    # --- Szenario B: BULL_STRONG + SELL → blockiert ---
    # e_long muss > +5% sein → Preis 110000, MA_LONG 100000 → e_long = +10%
    prices_b = [110000.0] * n
    df_b = pd.DataFrame({
        'price': prices_b,
        'ma_short': [111000.0] * n,
        'ma_long': [100000.0] * n,  # e_long = +10% → BULL_STRONG
        'trend_bin': ['uptrend'] * n,
    })

    env_b = TradingEnv(df_b, start_btc=1.0, start_cash=10000.0,
                       fee_pct=0.0026, trend_col='trend_bin', hodl_core_btc=0.1)
    env_b.window_length = n
    env_b.reset()

    tested_b = 0
    blocked_b = 0
    for i in range(10, min(50, n - 1)):
        env_b._idx_global = i
        env_b._steps_remaining = n - i
        env_b._last_block_reason = "none"

        sig = inspect.signature(env_b._apply_regime_rule)
        params = list(sig.parameters.keys())

        if 'state' in params:
            state = env_b._build_state()
            if tested_b == 0:
                print(f"  [Debug] Szenario B regime={state.get('regime')}, "
                      f"e_long={state.get('e_long', 0):.4f}")
            result = env_b._apply_regime_rule("SELL_SMALL", state)
        else:
            result = env_b._apply_regime_rule("SELL_SMALL")

        tested_b += 1
        if result == "HOLD":
            blocked_b += 1

    # --- Szenario C: NORMAL → durchgelassen ---
    prices_c = [100000.0] * n
    df_c = pd.DataFrame({
        'price': prices_c,
        'ma_short': [100000.0] * n,
        'ma_long': [100000.0] * n,  # e_long = 0% → NORMAL
        'trend_bin': ['sideways'] * n,
    })

    env_c = TradingEnv(df_c, start_btc=1.0, start_cash=10000.0,
                       fee_pct=0.0026, trend_col='trend_bin', hodl_core_btc=0.1)
    env_c.window_length = n
    env_c.reset()

    tested_c = 0
    passed_c = 0
    for i in range(10, min(50, n - 1)):
        env_c._idx_global = i
        env_c._steps_remaining = n - i
        env_c._last_block_reason = "none"

        sig = inspect.signature(env_c._apply_regime_rule)
        params = list(sig.parameters.keys())

        if 'state' in params:
            state = env_c._build_state()
            result = env_c._apply_regime_rule("BUY_SMALL", state)
        else:
            result = env_c._apply_regime_rule("BUY_SMALL")

        tested_c += 1
        if result == "BUY_SMALL":
            passed_c += 1

    print(f"  Szenario A (BEAR_STRONG, BUY blockiert):  {blocked_a}/{tested_a}")
    print(f"  Szenario B (BULL_STRONG, SELL blockiert):  {blocked_b}/{tested_b}")
    print(f"  Szenario C (NORMAL, durchgelassen):        {passed_c}/{tested_c}")

    ok = blocked_a > 0 and blocked_b > 0 and passed_c > 0
    print(f"\n  {'✅ V11.1: Regime-Rule korrekt' if ok else '❌ Regime-Rule fehlerhaft'}")

# ============================================================
# SONDE 7: Policy — Erfahrung kann Regel überstimmen — Bug #7
# ============================================================
def probe_policy_experience():
    header(7, "Policy — Erfahrung kann Regel überstimmen")
    from policy import (
        resonance_learning_policy, ma_profit_switch_policy,
        make_chain, ALL_ACTIONS,
    )

    state = {'pos': 'PARTIAL', 'pc_bin': 'flat', 'trend_bin': 'sideways',
             'step': 50, 'price': 95000.0, 'hist_high': 100000.0,
             'vol_bin': 'mid', 'rel_ma_short': -0.005, 'rel_ma_long': -0.005,
             'e_long': -0.005, 'e_short': -0.005,
             'cash_share': 0.40, 'sellable_share': 0.50,
             'regime': 'NORMAL', 'trend_strength': 0.01, 'trend_duration': 5}

    rule = ma_profit_switch_policy(state)

    exp = {}
    for a in ALL_ACTIONS:
        ch = make_chain(state, a)
        if a == "BUY_SMALL":
            exp[(ch, "success")] = 200
            exp[(ch, "failure")] = 20
            exp[(ch, "draw")] = 30
        elif a == "HOLD":
            exp[(ch, "success")] = 20
            exp[(ch, "failure")] = 150
            exp[(ch, "draw")] = 30
        else:
            exp[(ch, "success")] = 10
            exp[(ch, "failure")] = 10
            exp[(ch, "draw")] = 10

    random.seed(42)
    counts = {a: 0 for a in ALL_ACTIONS}
    n = 10000
    for _ in range(n):
        counts[resonance_learning_policy(state, exp, epsilon=0.0)] += 1

    rule_pct = counts[rule] / n * 100
    buy_pct = counts["BUY_SMALL"] / n * 100

    print(f"  Regel-Aktion: {rule}")
    print(f"  Erfahrung: BUY_SMALL stark positiv (S:200, F:20)")
    print(f"\n  Ergebnisse ({n} Trials):")
    for a in ALL_ACTIONS:
        if counts[a] > 0:
            print(f"    {a:14s}: {counts[a]:5d} ({counts[a]/n*100:5.1f}%)")

    ok = buy_pct > rule_pct
    print(f"\n  {'✅ GEFIXT: Erfahrung überstimmt Regel' if ok else '❌ Regel dominiert noch mit ' + f'{rule_pct:.0f}%'}")


# ============================================================
# SONDE 8: SELL bei e_long 1-3% auch bei Cash >20% — Bug #8
# ============================================================
def probe_sell_cash_gate():
    header(8, "SELL bei e_long 1-3% — Cash-Gate gesenkt")
    from policy import ma_profit_switch_policy

    cash_levels = [0.05, 0.10, 0.15, 0.20, 0.30, 0.40, 0.60]
    sells = 0
    print(f"  State: pos=LONG, e_long=1.5%, trend=sideways, vol=mid\n")

    for cs in cash_levels:
        state = {'pos': 'LONG', 'pc_bin': 'flat', 'trend_bin': 'sideways',
                 'step': 50, 'price': 101500.0, 'hist_high': 105000.0,
                 'vol_bin': 'mid', 'rel_ma_short': 0.015, 'rel_ma_long': 0.015,
                 'e_long': 0.015, 'e_short': 0.010,
                 'cash_share': cs, 'sellable_share': 0.80,
                 'regime': 'NORMAL', 'trend_strength': 0.005, 'trend_duration': 5}
        action = ma_profit_switch_policy(state)
        is_sell = action.startswith("SELL")
        if is_sell:
            sells += 1
        print(f"    Cash {cs*100:3.0f}%: {action:14s} {'✓' if is_sell else '✗'}")

    ok = sells >= 5
    print(f"\n  SELL bei {sells}/{len(cash_levels)} Cash-Levels")
    print(f"  {'✅ GEFIXT: Gewinnmitnahme bei moderatem Cash' if ok else '❌ Noch zu restriktiv'}")


# ============================================================
# SONDE 9: Exploration — MEDIUM wird exploriert — Bug #9
# ============================================================
def probe_exploration_medium():
    header(9, "Exploration — MEDIUM in PARTIAL")
    from policy import _exploration_action

    state = {'pos': 'PARTIAL', 'pc_bin': 'flat', 'trend_bin': 'sideways',
             'e_long': 0.003, 'e_short': 0.002,
             'cash_share': 0.40, 'sellable_share': 0.50}

    random.seed(42)
    counts = {}
    n = 50000
    for _ in range(n):
        a = _exploration_action(state)
        counts[a] = counts.get(a, 0) + 1

    has_medium = any("MEDIUM" in a for a in counts)

    print(f"  Exploration ({n} Samples):")
    for a in sorted(counts.keys()):
        print(f"    {a:14s}: {counts[a]:5d} ({counts[a]/n*100:5.1f}%)")

    print(f"\n  {'✅ GEFIXT: MEDIUM wird exploriert' if has_medium else '❌ MEDIUM fehlt noch'}")


# ============================================================
# SONDE 10: Diagnostik Filter — Bug #10
# ============================================================
def probe_diagnostics_filter():
    header(10, "Diagnostik — Trade-Fluss Filter")
    from diagnostics import summarize_episode_trades
    src = inspect.getsource(summarize_episode_trades)

    uses_startswith = '.str.startswith("SELL")' in src or ".str.startswith('SELL')" in src
    uses_exact = '== "SELL"]' in src or "== 'SELL']" in src

    print(f"  Nutzt .str.startswith(): {uses_startswith}")
    print(f"  Nutzt == 'SELL':         {uses_exact}")

    ok = uses_startswith and not uses_exact
    print(f"\n  {'✅ GEFIXT: Filter matcht SELL_SMALL/SELL_MEDIUM' if ok else '❌ Filter noch fehlerhaft'}")


# ============================================================
# SONDE 11: Merge-Gewichte — Bug #11
# ============================================================
def probe_merge_weights():
    header(11, "Merge — Gewichtung Offline ≥ Live")
    from experience import merge_experience
    sig = inspect.signature(merge_experience)
    live_w = sig.parameters['live_weight'].default
    offline_w = sig.parameters['offline_weight'].default

    print(f"  Live-Gewicht:    {live_w}")
    print(f"  Offline-Gewicht: {offline_w}")
    print(f"  Ratio Live/Off:  {live_w/offline_w:.2f}")

    ok = live_w <= offline_w
    print(f"\n  {'✅ GEFIXT: Offline ≥ Live' if ok else '❌ Live dominiert noch'}")


# ============================================================
# SONDE 12: main.py Defaults — Bug #12
# ============================================================
def probe_main_defaults():
    header(12, "main.py — HODL-Share Default + Diagnostik")
    from main import run_training_passes
    sig = inspect.signature(run_training_passes)
    hodl_default = sig.parameters['hodl_share'].default
    from config import HODL_SHARE

    print(f"  main.py Default: {hodl_default}")
    print(f"  config.py:       {HODL_SHARE}")

    ok_hodl = abs(hodl_default - HODL_SHARE) < 0.001
    print(f"  Konsistent:      {ok_hodl}")

    src = inspect.getsource(run_training_passes)
    unlink_pos = src.find('unlink()')
    loop_pos = src.find('for p in range')
    before_loop = unlink_pos < loop_pos if unlink_pos > 0 and loop_pos > 0 else False

    print(f"  Diagnostik-Löschung vor Loop: {before_loop}")

    ok = ok_hodl and before_loop
    print(f"\n  {'✅ GEFIXT: Defaults korrekt' if ok else '❌ Defaults noch inkonsistent'}")


# ============================================================
# SONDE 13: analyze_logs HODL-Kern + Benchmark — Bug #13
# ============================================================
def probe_analyze_logs():
    header(13, "analyze_logs — HODL-Kern fest + All-In Benchmark")
    from pathlib import Path

    src_path = Path("analyze_logs.py")
    if not src_path.exists():
        print("  analyze_logs.py nicht gefunden")
        return

    src = src_path.read_text(encoding="utf-8")

    has_fixed_core = 'hodl_core_fixed' in src
    has_allin = 'allin_btc' in src
    has_circular = 'hodl_core = sim_btc * HODL_SHARE' in src

    print(f"  Fester HODL-Kern:      {has_fixed_core}")
    print(f"  All-In-BTC Benchmark:  {has_allin}")
    print(f"  Zirkulärer Kern:       {has_circular}")

    ok = has_fixed_core and has_allin and not has_circular
    print(f"\n  {'✅ GEFIXT: Kern fest + fairer Benchmark' if ok else '❌ Noch nicht vollständig gefixt'}")


# ============================================================
# SONDE 14: train_offline HODL-Share Default — Bug #1/#12
# ============================================================
def probe_train_hodl_default():
    header(14, "train_offline — HODL-Share Default")
    from train_offline import train_offline as tf
    from config import HODL_SHARE
    sig = inspect.signature(tf)
    hodl_default = sig.parameters['hodl_share'].default

    print(f"  train_offline Default: {hodl_default}")
    print(f"  config.py HODL_SHARE: {HODL_SHARE}")

    ok = abs(hodl_default - HODL_SHARE) < 0.001
    print(f"\n  {'✅ GEFIXT: Konsistent' if ok else '❌ Noch divergent: ' + str(hodl_default) + ' vs ' + str(HODL_SHARE)}")


# ============================================================
# SONDE 15: Cooldown Overtrading — angepasst an V11.1
# ============================================================
def probe_cooldown_overtrading():
    header(15, "Cooldown — Overtrading-Schutz")
    from env import TradingEnv

    # Prüfe welche Cooldown-Methode existiert
    has_cooldown_rule = hasattr(TradingEnv, '_apply_cooldown_rule')
    has_cooldown = hasattr(TradingEnv, '_apply_cooldown')

    method_name = None
    if has_cooldown_rule:
        method_name = '_apply_cooldown_rule'
    elif has_cooldown:
        method_name = '_apply_cooldown'

    if method_name is None:
        print(f"  ❌ Keine Cooldown-Methode gefunden")
        return

    print(f"  Cooldown-Methode: {method_name}")

    method = getattr(TradingEnv, method_name)
    src = inspect.getsource(method)
    has_medium_downgrade = 'MEDIUM' in src and 'SMALL' in src

    print(f"  MEDIUM→SMALL Herabstufung: {has_medium_downgrade}")

    # Funktionstest
    prices = [100000.0] * 50
    df = pd.DataFrame({
        'price': prices,
        'ma_short': prices,
        'ma_long': prices,
        'trend_bin': ['sideways'] * 50,
    })
    env = TradingEnv(df, start_btc=0.5, start_cash=50000.0,
                     fee_pct=0.0026, trend_col='trend_bin', hodl_core_btc=0.05)
    env.window_length = 50
    env.reset()

    # Simuliere kürzlichen Trade
    env._last_trade_step = 10
    if hasattr(env, '_last_trade_direction'):
        env._last_trade_direction = "BUY"
    if hasattr(env, '_consecutive_trades'):
        env._consecutive_trades = 5

    env._steps_remaining = 50 - 11  # Step 11
    result = getattr(env, method_name)("BUY_MEDIUM")

    downgraded = result == "BUY_SMALL"
    print(f"  Schneller Folge-Trade (BUY_MEDIUM): {result}")
    print(f"  Herabgestuft: {downgraded}")

    ok = has_medium_downgrade
    print(f"\n  {'✅ GEFIXT: Overtrading wird gebremst' if ok else '❌ Kein Overtrading-Schutz'}")


# ============================================================
# SONDE 16: Docstring Version V11
# ============================================================
def probe_docstring():
    header(16, "Docstring Version V11")
    from env import TradingEnv

    env_doc = TradingEnv.__doc__ or ""

    has_v11 = "V11" in env_doc
    has_ac_dc = "AC" in env_doc or "ac_dc" in env_doc.lower() or "AC/DC" in env_doc

    print(f"  env.py TradingEnv Docstring enthält V11: {has_v11}")
    print(f"  env.py Docstring enthält AC/DC:          {has_ac_dc}")

    ok = has_v11
    print(f"\n  {'✅ Docstrings auf V11+' if ok else '❌ Docstrings veraltet'}")


# ============================================================
# SONDE 17: Signal-Strength — Starkes Signal → mehr Erfahrung
# ============================================================
def probe_signal_strength_direction():
    header(17, "Signal-Strength — Starkes Signal → mehr Erfahrung")
    from policy import _signal_strength

    weak = {'e_long': 0.002, 'e_short': 0.001}
    strong = {'e_long': 0.050, 'e_short': 0.030}

    sig_w = _signal_strength(weak)
    sig_s = _signal_strength(strong)

    rule_weak = max(0.20, 0.50 - 0.30 * sig_w)
    rule_strong = max(0.20, 0.50 - 0.30 * sig_s)

    print(f"  Schwaches Signal (e=0.2%): sig={sig_w:.3f}, min_rule={rule_weak:.3f}")
    print(f"  Starkes Signal  (e=5.0%):  sig={sig_s:.3f}, min_rule={rule_strong:.3f}")

    ok = rule_strong < rule_weak
    print(f"\n  {'✅ GEFIXT: Stark → mehr Erfahrung' if ok else '❌ Noch invertiert'}")


# ============================================================
# SONDE 18: V10 — Energierichtungsvektor im State
# ============================================================
def probe_energy_dir_in_state():
    header(18, "V10 — energy_dir im State")
    from env import TradingEnv

    prices = list(np.linspace(100000, 95000, 200)) + list(np.linspace(95000, 98000, 100))
    n = len(prices)
    df = pd.DataFrame({
        'price': prices,
        'ma_short': pd.Series(prices).rolling(24, min_periods=1).mean(),
        'ma_long': pd.Series(prices).rolling(168, min_periods=1).mean(),
        'trend_bin': ['sideways'] * n,
    })

    env = TradingEnv(df, start_btc=1.0, start_cash=10000.0,
                     fee_pct=0.0026, trend_col='trend_bin', hodl_core_btc=0.1)
    env.window_length = n
    state = env.reset()

    has_key = 'energy_dir' in state
    print(f"  energy_dir im State vorhanden: {has_key}")

    if has_key:
        e_s = state.get('e_short', 0.0)
        e_l = state.get('e_long', 0.0)
        expected = e_s - e_l
        actual = state['energy_dir']
        match = abs(actual - expected) < 1e-10
        print(f"  e_short={e_s:.6f}, e_long={e_l:.6f}")
        print(f"  Erwartet: {expected:.6f}")
        print(f"  Tatsächlich: {actual:.6f}")
        print(f"  Korrekt berechnet: {match}")
        ok = match
    else:
        ok = False

    print(f"\n  {'✅ V10: energy_dir korrekt im State' if ok else '❌ energy_dir fehlt oder falsch'}")


# ============================================================
# SONDE 19: V10 — Resonanz-Gate blockiert anti-resonante Trades
# ============================================================
def probe_resonance_gate():
    header(19, "V10 — Resonanz-Gate (Axiom 6)")
    from policy import ma_profit_switch_policy

    # BUY bei stark fallender Energie (energy_dir << -0.005) → sollte blockiert werden
    state_anti_buy = {
        'pos': 'PARTIAL', 'pc_bin': 'down', 'trend_bin': 'sideways',
        'step': 50, 'price': 95000.0, 'hist_high': 100000.0,
        'vol_bin': 'mid', 'rel_ma_short': -0.04, 'rel_ma_long': -0.02,
        'e_long': -0.04, 'e_short': -0.06,
        'cash_share': 0.50, 'sellable_share': 0.50,
        'regime': 'NORMAL', 'trend_strength': 0.01, 'trend_duration': 5,
    }

    # SELL bei stark steigender Energie → sollte blockiert werden
    state_anti_sell = {
        'pos': 'LONG', 'pc_bin': 'up', 'trend_bin': 'sideways',
        'step': 50, 'price': 102000.0, 'hist_high': 105000.0,
        'vol_bin': 'mid', 'rel_ma_short': 0.03, 'rel_ma_long': 0.01,
        'e_long': 0.03, 'e_short': 0.05,
        'cash_share': 0.30, 'sellable_share': 0.50,
        'regime': 'NORMAL', 'trend_strength': 0.01, 'trend_duration': 5,
    }

    # Resonanter BUY (energy_dir ~0) → sollte erlaubt sein
    state_resonant_buy = {
        'pos': 'PARTIAL', 'pc_bin': 'flat', 'trend_bin': 'sideways',
        'step': 50, 'price': 96000.0, 'hist_high': 100000.0,
        'vol_bin': 'mid', 'rel_ma_short': -0.04, 'rel_ma_long': -0.04,
        'e_long': -0.04, 'e_short': -0.04,
        'cash_share': 0.50, 'sellable_share': 0.50,
        'regime': 'NORMAL', 'trend_strength': 0.01, 'trend_duration': 5,
    }

    action_anti_buy = ma_profit_switch_policy(state_anti_buy)
    action_anti_sell = ma_profit_switch_policy(state_anti_sell)
    action_resonant_buy = ma_profit_switch_policy(state_resonant_buy)

    buy_blocked = not action_anti_buy.startswith("BUY")
    sell_blocked = not action_anti_sell.startswith("SELL")
    buy_allowed = action_resonant_buy.startswith("BUY")

    print(f"  Anti-resonanter BUY  (energy_dir=-0.02): {action_anti_buy:14s} {'✓ blockiert' if buy_blocked else '✗ durchgelassen'}")
    print(f"  Anti-resonanter SELL (energy_dir=+0.02): {action_anti_sell:14s} {'✓ blockiert' if sell_blocked else '✗ durchgelassen'}")
    print(f"  Resonanter BUY      (energy_dir= 0.00): {action_resonant_buy:14s} {'✓ erlaubt' if buy_allowed else '✗ blockiert'}")

    ok = buy_blocked and sell_blocked and buy_allowed
    print(f"\n  {'✅ V10: Resonanz-Gate korrekt' if ok else '❌ Resonanz-Gate fehlerhaft'}")


# ============================================================
# SONDE 20: V10 — Balance-Regler
# ============================================================
def probe_balance_regler():
    header(20, "V10 — Balance-Regler (Axiom 2)")
    from policy import ma_profit_switch_policy

    state_low_cash = {
        'pos': 'PARTIAL', 'pc_bin': 'flat', 'trend_bin': 'sideways',
        'step': 50, 'price': 96000.0, 'hist_high': 100000.0,
        'vol_bin': 'mid', 'rel_ma_short': -0.04, 'rel_ma_long': -0.04,
        'e_long': -0.04, 'e_short': -0.04,
        'cash_share': 0.05, 'sellable_share': 0.50,
        'regime': 'NORMAL', 'trend_strength': 0.01, 'trend_duration': 5,
    }

    state_low_sell = {
        'pos': 'LONG', 'pc_bin': 'flat', 'trend_bin': 'sideways',
        'step': 50, 'price': 103000.0, 'hist_high': 105000.0,
        'vol_bin': 'mid', 'rel_ma_short': 0.03, 'rel_ma_long': 0.03,
        'e_long': 0.03, 'e_short': 0.03,
        'cash_share': 0.30, 'sellable_share': 0.03,
        'regime': 'NORMAL', 'trend_strength': 0.01, 'trend_duration': 5,
    }

    state_normal = {
        'pos': 'PARTIAL', 'pc_bin': 'flat', 'trend_bin': 'sideways',
        'step': 50, 'price': 96000.0, 'hist_high': 100000.0,
        'vol_bin': 'mid', 'rel_ma_short': -0.04, 'rel_ma_long': -0.04,
        'e_long': -0.04, 'e_short': -0.04,
        'cash_share': 0.40, 'sellable_share': 0.50,
        'regime': 'NORMAL', 'trend_strength': 0.01, 'trend_duration': 5,
    }

    action_low_cash = ma_profit_switch_policy(state_low_cash)
    action_low_sell = ma_profit_switch_policy(state_low_sell)
    action_normal = ma_profit_switch_policy(state_normal)

    buy_blocked = not action_low_cash.startswith("BUY")
    sell_blocked = not action_low_sell.startswith("SELL")
    normal_trades = action_normal != "HOLD"

    print(f"  Cash  5% → BUY:     {action_low_cash:14s} {'✓ blockiert' if buy_blocked else '✗ durchgelassen'}")
    print(f"  Sell  3% → SELL:    {action_low_sell:14s} {'✓ blockiert' if sell_blocked else '✗ durchgelassen'}")
    print(f"  Normal   → Trade:   {action_normal:14s} {'✓ erlaubt' if normal_trades else '✗ blockiert'}")

    ok = buy_blocked and sell_blocked and normal_trades
    print(f"\n  {'✅ V10: Balance-Regler korrekt' if ok else '❌ Balance-Regler fehlerhaft'}")


# ============================================================
# SONDE 21: V10 — BUY-Schwellen angehoben
# ============================================================
def probe_buy_thresholds_v10():
    header(21, "V10 — BUY-Schwellen angehoben")
    from policy import ma_profit_switch_policy

    results = {}

    for e_val, label in [(-0.025, "DT -2.5%"), (-0.035, "DT -3.5%"), (-0.045, "DT -4.5%")]:
        state = {
            'pos': 'PARTIAL', 'pc_bin': 'flat', 'trend_bin': 'downtrend',
            'step': 50, 'price': 100000 * (1 + e_val), 'hist_high': 105000.0,
            'vol_bin': 'mid', 'rel_ma_short': e_val, 'rel_ma_long': e_val,
            'e_long': e_val, 'e_short': e_val,
            'cash_share': 0.40, 'sellable_share': 0.50,
            'regime': 'NORMAL', 'trend_strength': 0.01, 'trend_duration': 5,
        }
        action = ma_profit_switch_policy(state)
        is_buy = action.startswith("BUY")
        results[label] = (action, is_buy)
        print(f"  {label}: {action:14s} {'✓ BUY' if is_buy else '✗ kein BUY'}")

    for e_val, label in [(-0.015, "SW -1.5%"), (-0.025, "SW -2.5%"), (-0.035, "SW -3.5%")]:
        state = {
            'pos': 'PARTIAL', 'pc_bin': 'flat', 'trend_bin': 'sideways',
            'step': 50, 'price': 100000 * (1 + e_val), 'hist_high': 105000.0,
            'vol_bin': 'mid', 'rel_ma_short': e_val, 'rel_ma_long': e_val,
            'e_long': e_val, 'e_short': e_val,
            'cash_share': 0.40, 'sellable_share': 0.50,
            'regime': 'NORMAL', 'trend_strength': 0.01, 'trend_duration': 5,
        }
        action = ma_profit_switch_policy(state)
        is_buy = action.startswith("BUY")
        results[label] = (action, is_buy)
        print(f"  {label}: {action:14s} {'✓ BUY' if is_buy else '✗ kein BUY'}")

    dt_low_blocked = not results["DT -2.5%"][1]
    dt_deep_buys = results["DT -4.5%"][1]
    sw_low_blocked = not results["SW -1.5%"][1]
    sw_deep_buys = results["SW -3.5%"][1]

    ok = dt_low_blocked and dt_deep_buys and sw_low_blocked and sw_deep_buys
    print(f"\n  DT -2.5% blockiert: {dt_low_blocked}, DT -4.5% kauft: {dt_deep_buys}")
    print(f"  SW -1.5% blockiert: {sw_low_blocked}, SW -3.5% kauft: {sw_deep_buys}")
    print(f"\n  {'✅ V10: BUY-Schwellen korrekt angehoben' if ok else '❌ BUY-Schwellen nicht korrekt'}")


# ============================================================
# SONDE 22: V11.1 — Downtrend-Pause-Gate
# ============================================================
def probe_downtrend_pause_gate():
    header(22, "V11.1 — Downtrend-Pause-Gate")
    from env import TradingEnv

    # Prüfe ob Gate existiert
    has_method = hasattr(TradingEnv, '_check_downtrend_pause')
    has_block = False
    try:
        from env import BLOCK_DOWNTREND_PAUSE
        has_block = True
    except ImportError:
        pass

    print(f"  _check_downtrend_pause vorhanden: {has_method}")
    print(f"  BLOCK_DOWNTREND_PAUSE definiert:  {has_block}")

    if not has_method:
        print(f"\n  ❌ Downtrend-Pause-Gate nicht implementiert")
        return

    # Config-Parameter prüfen
    try:
        from config import (
            PAUSE_E_LONG_THRESHOLD,
            PAUSE_REGIME,
            RESUME_E_LONG_THRESHOLD,
            RESUME_AC_PHASE,
        )
        has_config = True
        print(f"  Config-Parameter vorhanden:        True")
        print(f"    PAUSE_E_LONG_THRESHOLD:  {PAUSE_E_LONG_THRESHOLD}")
        print(f"    PAUSE_REGIME:            {PAUSE_REGIME}")
        print(f"    RESUME_E_LONG_THRESHOLD: {RESUME_E_LONG_THRESHOLD}")
        print(f"    RESUME_AC_PHASE:         {RESUME_AC_PHASE}")
    except ImportError:
        has_config = False
        print(f"  Config-Parameter vorhanden:        False")
        print(f"\n  ❌ Config-Parameter fehlen")
        return

    n = 500

    # --- Szenario A: BEAR_STRONG + downtrend + e_long < -5% → Pause ---
    prices_crash = list(np.linspace(100000, 80000, n))
    ma_long_crash = list(np.linspace(100000, 95000, n))  # MA fällt langsamer
    ma_short_crash = list(np.linspace(100000, 82000, n))

    df_crash = pd.DataFrame({
        'price': prices_crash,
        'ma_short': ma_short_crash,
        'ma_long': ma_long_crash,
        'trend_bin': ['downtrend'] * n,
    })

    env = TradingEnv(df_crash, start_btc=1.0, start_cash=10000.0,
                     fee_pct=0.0026, trend_col='trend_bin', hodl_core_btc=0.1)
    env.window_length = n
    env.reset()

    # Manuell in Crash-Position setzen (Mitte der Daten)
    test_idx = n // 2  # Preis ~90000, MA_LONG ~97500 → e_long = -7.7%
    env._idx_global = test_idx
    env._steps_remaining = n - test_idx

    state = env._build_state()
    e_long = state.get('e_long', 0.0)
    regime = state.get('regime', 'NORMAL')
    trend = state.get('trend_bin', 'sideways')

    print(f"\n  Szenario A (Crash):")
    print(f"    e_long={e_long:.4f}, regime={regime}, trend={trend}")

    # Regime manuell setzen falls nicht automatisch BEAR_STRONG
    env._cached_regime = "BEAR_STRONG"
    env._trend_duration = 100

    pause_triggered = env._check_downtrend_pause({
        'trend_bin': 'downtrend',
        'e_long': e_long,
        'regime': 'BEAR_STRONG',
        'ac_phase': 'transition',
    })
    print(f"    Pause ausgelöst: {pause_triggered}")
    print(f"    _daytrading_paused: {env._daytrading_paused}")

    # --- Szenario B: Wiederaufnahme bei e_long > -3% ---
    resume_by_elong = False
    if env._daytrading_paused:
        still_paused = env._check_downtrend_pause({
            'trend_bin': 'downtrend',
            'e_long': -0.02,  # > -3% → Resume
            'regime': 'BEAR_STRONG',
            'ac_phase': 'transition',
        })
        resume_by_elong = not still_paused
        print(f"\n  Szenario B (e_long > -3%):")
        print(f"    Resume ausgelöst: {resume_by_elong}")
        print(f"    _daytrading_paused: {env._daytrading_paused}")

    # --- Szenario C: Wiederaufnahme bei ac_phase = trough ---
    # Pause erneut auslösen
    env._daytrading_paused = False
    env._check_downtrend_pause({
        'trend_bin': 'downtrend',
        'e_long': -0.08,
        'regime': 'BEAR_STRONG',
        'ac_phase': 'transition',
    })

    resume_by_trough = False
    if env._daytrading_paused:
        still_paused = env._check_downtrend_pause({
            'trend_bin': 'downtrend',
            'e_long': -0.06,  # Immer noch unter -3%
            'regime': 'BEAR_STRONG',
            'ac_phase': 'trough',  # Aber Wendepunkt!
        })
        resume_by_trough = not still_paused
        print(f"\n  Szenario C (ac_phase=trough):")
        print(f"    Resume ausgelöst: {resume_by_trough}")

    # --- Szenario D: Wiederaufnahme bei Regime-Wechsel ---
    env._daytrading_paused = False
    env._check_downtrend_pause({
        'trend_bin': 'downtrend',
        'e_long': -0.08,
        'regime': 'BEAR_STRONG',
        'ac_phase': 'transition',
    })

    resume_by_regime = False
    if env._daytrading_paused:
        still_paused = env._check_downtrend_pause({
            'trend_bin': 'downtrend',
            'e_long': -0.06,
            'regime': 'NORMAL',  # Regime gewechselt!
            'ac_phase': 'transition',
        })
        resume_by_regime = not still_paused
        print(f"\n  Szenario D (regime → NORMAL):")
        print(f"    Resume ausgelöst: {resume_by_regime}")

    # --- Szenario E: Kein Pause in normalem Markt ---
    env._daytrading_paused = False
    no_pause_normal = not env._check_downtrend_pause({
        'trend_bin': 'sideways',
        'e_long': -0.02,
        'regime': 'NORMAL',
        'ac_phase': 'transition',
    })
    print(f"\n  Szenario E (normaler Markt):")
    print(f"    Keine Pause: {no_pause_normal}")

    # --- Gesamtbewertung ---
    ok = (pause_triggered
          and resume_by_elong
          and resume_by_trough
          and resume_by_regime
          and no_pause_normal)

    print(f"\n  Zusammenfassung:")
    print(f"    Pause bei Crash:         {'✓' if pause_triggered else '✗'}")
    print(f"    Resume bei e_long > -3%: {'✓' if resume_by_elong else '✗'}")
    print(f"    Resume bei trough:       {'✓' if resume_by_trough else '✗'}")
    print(f"    Resume bei Regime-Δ:     {'✓' if resume_by_regime else '✗'}")
    print(f"    Kein Pause bei normal:   {'✓' if no_pause_normal else '✗'}")

    print(f"\n  {'✅ V11.1: Downtrend-Pause-Gate korrekt' if ok else '❌ Downtrend-Pause-Gate fehlerhaft'}")


# ============================================================
# SONDE 23: V11.1 — Human-Hint-System
# ============================================================
def probe_human_hint_system():
    header(23, "V11.1 — Human-Hint-System")
    import json
    import os
    from datetime import datetime, timezone, timedelta

    # --- 23a: Module importierbar ---
    try:
        from human_hint import (
            create_hint, load_hint, clear_hint,
            is_paused, hint_bias_adjustment,
            HINT_PATH, DEFAULT_WEIGHT, HINT_EXPIRY_HOURS,
        )
        importable = True
    except ImportError as e:
        importable = False
        print(f"  ❌ Import fehlgeschlagen: {e}")
        return

    print(f"  human_hint.py importierbar:    {importable}")
    print(f"  DEFAULT_WEIGHT:                {DEFAULT_WEIGHT}")
    print(f"  HINT_EXPIRY_HOURS:             {HINT_EXPIRY_HOURS}")

    # --- 23b: Hint erstellen + laden ---
    test_hint_path = os.path.join("data", "human_hint_test.json")
    original_path = HINT_PATH

    # Temporaer umleiten damit echte Hints nicht ueberschrieben werden
    import human_hint
    human_hint.HINT_PATH = test_hint_path

    try:
        hint = create_hint("bullish", "Unittest: EZB senkt Zinsen", weight=0.4)
        loaded = load_hint()
        hint_created = loaded is not None
        bias_correct = loaded.get("bias") == "bullish" if loaded else False
        weight_correct = loaded.get("weight") == 0.4 if loaded else False
        reason_correct = "EZB" in loaded.get("reason", "") if loaded else False

        print(f"\n  Hint erstellt + geladen:       {hint_created}")
        print(f"  Bias korrekt (bullish):        {bias_correct}")
        print(f"  Gewicht korrekt (0.4):         {weight_correct}")
        print(f"  Grund enthalten:               {reason_correct}")

        # --- 23c: Bias-Adjustment ---
        # Bullish Hint → SELL blockieren
        adj_sell, reason_sell = hint_bias_adjustment(loaded, "SELL_SMALL", "sideways")
        sell_blocked = adj_sell == "HOLD"

        # Bullish Hint → BUY durchlassen
        adj_buy, reason_buy = hint_bias_adjustment(loaded, "BUY_SMALL", "sideways")
        buy_passed = adj_buy == "BUY_SMALL"

        # Bullish Hint → HOLD unveraendert
        adj_hold, reason_hold = hint_bias_adjustment(loaded, "HOLD", "sideways")
        hold_passed = adj_hold == "HOLD"

        print(f"\n  Bullish + SELL_SMALL → HOLD:   {sell_blocked} (wurde: {adj_sell})")
        print(f"  Bullish + BUY_SMALL → BUY:     {buy_passed} (wurde: {adj_buy})")
        print(f"  Bullish + HOLD → HOLD:         {hold_passed} (wurde: {adj_hold})")

        # --- 23d: Bearish Hint ---
        clear_hint()
        create_hint("bearish", "Unittest: SEC verklagt Boerse", weight=0.5)
        loaded_bear = load_hint()

        adj_buy_bear, _ = hint_bias_adjustment(loaded_bear, "BUY_SMALL", "sideways")
        buy_blocked_bear = adj_buy_bear == "HOLD"

        adj_sell_bear, _ = hint_bias_adjustment(loaded_bear, "SELL_SMALL", "sideways")
        sell_passed_bear = adj_sell_bear == "SELL_SMALL"

        print(f"\n  Bearish + BUY_SMALL → HOLD:    {buy_blocked_bear} (wurde: {adj_buy_bear})")
        print(f"  Bearish + SELL_SMALL → SELL:    {sell_passed_bear} (wurde: {adj_sell_bear})")

        # --- 23e: Pause ---
        clear_hint()
        create_hint("neutral", "Unittest: FOMC Pause", pause_hours=2)
        loaded_pause = load_hint()
        paused = is_paused(loaded_pause)

        adj_pause, reason_pause = hint_bias_adjustment(loaded_pause, "BUY_MEDIUM", "uptrend")
        pause_blocks = adj_pause == "HOLD"

        print(f"\n  Pause aktiv:                   {paused}")
        print(f"  Pause blockiert BUY_MEDIUM:    {pause_blocks} (wurde: {adj_pause})")

        # --- 23f: Neutral Hint → kein Eingriff ---
        clear_hint()
        create_hint("neutral", "Unittest: keine Nachrichten")
        loaded_neutral = load_hint()

        adj_neutral, reason_neutral = hint_bias_adjustment(loaded_neutral, "SELL_MEDIUM", "downtrend")
        neutral_passes = adj_neutral == "SELL_MEDIUM"

        print(f"\n  Neutral + SELL_MEDIUM → SELL:  {neutral_passes} (wurde: {adj_neutral})")

        # --- 23g: Abgelaufener Hint → None ---
        clear_hint()
        create_hint("bullish", "Unittest: abgelaufen")
        # Timestamp manuell auf vor 49h setzen
        with open(test_hint_path) as f:
            old_hint = json.load(f)
        old_ts = datetime.now(timezone.utc) - timedelta(hours=49)
        old_hint["timestamp"] = old_ts.isoformat()
        with open(test_hint_path, "w") as f:
            json.dump(old_hint, f)
        expired = load_hint()
        expired_none = expired is None

        print(f"\n  Abgelaufener Hint (49h) → None: {expired_none}")

        # --- 23h: Integration in live_signal.py ---
        from live_signal import run_once
        src = inspect.getsource(run_once)
        has_hint_import = "hint_bias_adjustment" in src or "load_hint" in src
        has_hint_call = "hint_bias_adjustment" in src

        print(f"\n  live_signal.py importiert Hint: {has_hint_import}")
        print(f"  live_signal.py ruft Hint auf:   {has_hint_call}")

        # --- 23i: Log-Spalte hint_info ---
        from live_signal import _log_signal
        sig = inspect.signature(_log_signal)
        has_hint_param = "hint_info" in sig.parameters

        print(f"  _log_signal hat hint_info:      {has_hint_param}")

        # --- 23j: expectation-Kommando ---
        has_expectation = hasattr(__import__("live_signal"), "expectation")
        print(f"  live_signal.py hat expectation:  {has_expectation}")

        # --- Gesamtbewertung ---
        ok = all([
            hint_created, bias_correct, weight_correct, reason_correct,
            sell_blocked, buy_passed, hold_passed,
            buy_blocked_bear, sell_passed_bear,
            paused, pause_blocks,
            neutral_passes,
            expired_none,
            has_hint_import, has_hint_call,
            has_hint_param,
            has_expectation,
        ])

        print(f"\n  Zusammenfassung:")
        print(f"    Hint CRUD:               {'✓' if hint_created and bias_correct else '✗'}")
        print(f"    Bullish-Blockade:         {'✓' if sell_blocked and buy_passed else '✗'}")
        print(f"    Bearish-Blockade:         {'✓' if buy_blocked_bear and sell_passed_bear else '✗'}")
        print(f"    Pause:                    {'✓' if paused and pause_blocks else '✗'}")
        print(f"    Neutral durchlaessig:     {'✓' if neutral_passes else '✗'}")
        print(f"    Ablauf nach 48h:          {'✓' if expired_none else '✗'}")
        print(f"    Live-Integration:         {'✓' if has_hint_import and has_hint_call else '✗'}")
        print(f"    Log + Expectation:        {'✓' if has_hint_param and has_expectation else '✗'}")

        print(f"\n  {'✅ V11.1: Human-Hint-System komplett' if ok else '❌ Human-Hint-System unvollstaendig'}")

    finally:
        # Aufraemen: Test-Hint loeschen, Pfad zuruecksetzen
        human_hint.HINT_PATH = original_path
        if os.path.exists(test_hint_path):
            os.remove(test_hint_path)
        # Test-Log-Eintraege bleiben im echten Log — kein Problem


# ============================================================
# MAIN
# ============================================================
if __name__ == "__main__":
    probes = [
        probe_fee_consistency,           # 1
        probe_hodl_core_fixed,           # 2
        probe_volatility_window,         # 3
        probe_window_length,             # 4
        probe_state_signature,           # 5
        probe_ma_sell_guard_v10,         # 6
        probe_policy_experience,         # 7
        probe_sell_cash_gate,            # 8
        probe_exploration_medium,        # 9
        probe_diagnostics_filter,        # 10
        probe_merge_weights,             # 11
        probe_main_defaults,             # 12
        probe_analyze_logs,              # 13
        probe_train_hodl_default,        # 14
        probe_cooldown_overtrading,      # 15
        probe_docstring,                 # 16
        probe_signal_strength_direction, # 17
        probe_energy_dir_in_state,       # 18
        probe_resonance_gate,            # 19
        probe_balance_regler,            # 20
        probe_buy_thresholds_v10,        # 21
        probe_downtrend_pause_gate,      # 22
        probe_human_hint_system,         # 23 — V11.1 NEU
    ]

    for probe in probes:
        try:
            probe()
        except Exception as e:
            print(f"\n  ❌ FEHLER: {e}")
            import traceback
            traceback.print_exc()

    print(f"\n{'=' * 60}")
    print(f"Debug-Sonden abgeschlossen. ({len(probes)} Sonden)")
    print(f"{'=' * 60}")
    print(f"\nBitte Ausgabe auf ✅/❌ prüfen.")
    print(f"Alle ✅ = System konsistent, bereit für Training + Live.")