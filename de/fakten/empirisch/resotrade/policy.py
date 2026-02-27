"""
ResoTrade V11.1 — Policy mit Energierichtungsvektor + AC/DC-Zerlegung.

Resonanzfeldtheoretische Grundlage (RFT V3.1, Axiome A1–A7):

  A1 (Universelle Schwingung):
      ψ(x,t) = A·cos(kx − ωt + φ)
      → AC/DC-Zerlegung des Preisfeldes: Preis = DC (Trend) + AC (handelbar)

  A2 (Superposition):
      Φ = Σ ψᵢ
      → MA_SHORT (24h) und MA_LONG (168h) als überlagerte Moden im Preissignal

  A4 (Kopplungsenergie):
      E = π·ε(Δφ)·h·f
      → Balance-Regler: Cash ↔ BTC als gekoppelte Resonanzräume.
        Die Kopplungseffizienz ε erfordert, dass beide Seiten gefüllt sind.

  A5 (Energierichtung):
      E⃗ = E·ê(Δφ, ∇Φ)
      → energy_dir = e_short - e_long (Richtung des Kapitalflusses im Feld)

  A6 (Informationsfluss durch Resonanzkopplung):
      MI(X,Y) > 0 ⟺ PCI > 0
      → Resonanz-Gate: Trades nur wenn Phasenkohärenz zwischen Aktion
        und Energierichtung besteht. energy_dir nahe 0 = niedrige Kohärenz.

  A7 (Invarianz unter G_sync):
      G(fᵢ/fⱼ) = G(T(fᵢ)/T(fⱼ))
      → Regime-Invarianz: System funktioniert über alle Marktphasen.

Vier Ebenen:
  1. Makro-Regime (BULL_STRONG/BEAR_STRONG/NORMAL) → erlaubte Aktionen
  2. AC/DC-Phase (peak/trough/transition/flat) → Trade-Timing + Sizing
  3. Energierichtungs-Policy → resonante Trades
  4. Erfahrungsspeicher → datenbasierte Verfeinerung
"""
import random
import math
from typing import Literal

from config import NORM_SPREAD_REF, SELL_LOW_VOL_ENABLED
from experience import load_experience

Action = Literal[
    "HOLD",
    "BUY_SMALL",
    "BUY_MEDIUM",
    "SELL_SMALL",
    "SELL_MEDIUM",
]

ALL_ACTIONS: list = [
    "HOLD",
    "BUY_SMALL",
    "BUY_MEDIUM",
    "SELL_SMALL",
    "SELL_MEDIUM",
]


def _step_bin(step: int, window_length: int = 90) -> str:
    if window_length <= 0:
        return "mid"
    x = step / float(window_length)
    if x < 1 / 3:
        return "early"
    elif x < 2 / 3:
        return "mid"
    return "late"


def _near_high_flag(price: float, hist_high: float) -> str:
    if hist_high <= 0:
        return "far"
    rel = (hist_high - price) / hist_high
    if rel < 0.01:
        return "ath_zone"
    elif rel < 0.03:
        return "near"
    return "far"


def _ma_bin(rel: float) -> str:
    if rel < -0.02:
        return "below"
    elif rel > 0.02:
        return "above"
    return "near"


def _cash_zone(cash_share: float) -> str:
    if cash_share < 0.05:
        return "dry"
    elif cash_share < 0.20:
        return "low"
    elif cash_share < 0.50:
        return "mid"
    return "high"


def _sellable_zone(sellable_share: float) -> str:
    if sellable_share < 0.01:
        return "locked"
    elif sellable_share < 0.10:
        return "tight"
    elif sellable_share < 0.30:
        return "free"
    return "open"


def make_chain(state: dict, action: Action) -> str:
    """
    V11: Chain enthält Regime + AC-Phase.

    12 diskretisierte Dimensionen + 5 Aktionen.
    Jede Dimension bildet eine Mode im Zustandsraum ab (A2: Superposition).
    """
    pos = state.get("pos", "FLAT")
    pc_bin = state.get("pc_bin", "flat")
    trend = state.get("trend_bin", "none")
    step = int(state.get("step", 0))
    price = float(state.get("price", 0.0) or 0.0)
    hist_high = float(state.get("hist_high", 0.0) or 0.0)
    vol_bin = state.get("vol_bin", "mid")
    rel_ma_short = float(state.get("rel_ma_short", 0.0) or 0.0)
    rel_ma_long = float(state.get("rel_ma_long", 0.0) or 0.0)
    cash_share = float(state.get("cash_share", 0.0) or 0.0)
    sellable_share = float(state.get("sellable_share", 1.0) or 1.0)
    regime = state.get("regime", "NORMAL")
    ac_phase = state.get("ac_phase", "flat")

    sb = _step_bin(step)
    nh = _near_high_flag(price, hist_high)
    ma_s = _ma_bin(rel_ma_short)
    ma_l = _ma_bin(rel_ma_long)
    cz = _cash_zone(cash_share)
    sz = _sellable_zone(sellable_share)

    return (
        f"pos:{pos},pc:{pc_bin},trend:{trend},"
        f"step:{sb},high:{nh},vol:{vol_bin},"
        f"ma_s:{ma_s},ma_l:{ma_l},"
        f"cz:{cz},sz:{sz},"
        f"regime:{regime},"
        f"ac:{ac_phase},"
        f"action:{action}"
    )


# ===== Volatilitäts-Modulation =====

_WARMUP_STEPS = 40


def _vol_scale(vol_bin: str) -> str:
    if vol_bin == "low":
        return "damped"
    if vol_bin == "high":
        return "amplified"
    return "neutral"


# ===== Regime-Filter =====

def _allowed_actions_for_regime(state: dict) -> list:
    """
    Makro-Regime bestimmt erlaubte Aktionen.

    A7 (Invarianz): Die Regime-Klassifikation ist invariant unter
    synchronen Transformationen — sie gilt in jeder Marktphase.
    """
    regime = state.get("regime", "NORMAL")
    e_long = float(state.get("e_long", 0.0) or 0.0)

    if regime == "BULL_STRONG":
        return ["HOLD", "BUY_SMALL", "BUY_MEDIUM"]

    if regime == "BEAR_STRONG":
        allowed = ["HOLD", "SELL_SMALL", "SELL_MEDIUM"]
        if e_long < -0.05:
            allowed.extend(["BUY_SMALL", "BUY_MEDIUM"])
        return allowed

    return list(ALL_ACTIONS)


# ===== Energierichtungsvektor (A5) =====

def _energy_direction(state: dict) -> float:
    """
    Resonanzfeldtheoretischer Energierichtungsvektor (A5).

    A5: E⃗ = E_eff · ê(Δφ, ∇Φ)
    Im diskreten Mehrskalensystem:
        energy_dir = e_short - e_long

    Positiv → Preis bewegt sich aufwärts relativ zum MA-System
    Negativ → Preis bewegt sich abwärts

    Die Richtung ist eine verwertbare Observable, die über skalare
    Indikatoren (RSI, Momentum) hinausgeht — empirisch bestätigt:
    alle skalaren Indikatoren haben Korrelation < 0.05.
    """
    e_long = float(state.get("e_long", 0.0) or 0.0)
    e_short = float(state.get("e_short", 0.0) or 0.0)
    return e_short - e_long


# ===== MA-Regel-Policy =====

def ma_profit_switch_policy(state: dict) -> Action:
    """
    Resonanzlogische Policy V11.1 — Energierichtung + AC/DC-Phase + Balance.

    Implementiert vier Axiome der RFT (V3.1):

    1. A1 (Universelle Schwingung): AC/DC-Zerlegung bestimmt Phase + Timing
       Peak → SELL bevorzugt, Trough → BUY bevorzugt
    2. A5 (Energierichtung): energy_dir = e_short - e_long
       Nur resonante Trades (Aktion in Richtung des Energieflusses)
    3. A6 (Informationsfluss): Resonanz-Gate filtert phasenkohärente Trades
       allow_buy/allow_sell nur wenn Energierichtung nicht gegenläufig
    4. A4 (Kopplungsenergie): Balance-Regler hält Kopplungseffizienz ε > 0
       Cash < 8% → kein BUY, Sellable < 5% → kein SELL
    """
    pos = state.get("pos", "FLAT")
    e_long = float(state.get("e_long", 0.0) or 0.0)
    e_short = float(state.get("e_short", 0.0) or 0.0)
    trend = state.get("trend_bin", "none")
    vol_bin = state.get("vol_bin", "mid")
    step = int(state.get("step", 0))
    cash_share = float(state.get("cash_share", 0.0) or 0.0)
    sellable_share = float(state.get("sellable_share", 1.0) or 1.0)

    # A1: AC/DC-Phase aus State (Universelle Schwingung)
    ac_phase = state.get("ac_phase", "flat")
    ac_amp_bin = state.get("ac_amplitude_bin", "normal")
    ac_value = float(state.get("ac_value", 0.0) or 0.0)

    # A5: Energierichtungsvektor
    energy_dir = _energy_direction(state)

    action: Action = "HOLD"

    thr_small = 0.01
    thr_medium = 0.03

    vol_mod = _vol_scale(vol_bin)
    cz = _cash_zone(cash_share)
    sz = _sellable_zone(sellable_share)

    sell_vol_mod = vol_mod
    if SELL_LOW_VOL_ENABLED and vol_mod == "damped":
        sell_vol_mod = "neutral"

    # === Resonanz-Gate (A6: Informationsfluss durch Resonanzkopplung) ===
    # MI(X,Y) > 0 ⟺ PCI > 0: Trades nur wenn Phasenkohärenz besteht.
    # BUY nur wenn Energie nicht stark abwärts (Aktion wäre anti-resonant)
    # SELL nur wenn Energie nicht stark aufwärts (Aktion wäre anti-resonant)
    RESONANCE_GATE = 0.005
    allow_buy = energy_dir > -RESONANCE_GATE
    allow_sell = energy_dir < RESONANCE_GATE

    # === SELL-Modus 1: Resonanzverstärkte Gewinnmitnahme ===
    # A1: AC-Phase moduliert Timing und Sizing
    # Peak → SELL ist resonant (AC-Energie wird abgegeben)
    # Trough → SELL ist anti-resonant (AC-Energie wird aufgenommen)
    if allow_sell and sz != "locked" and pos in ("LONG", "PARTIAL") and e_long > 0:
        if trend == "uptrend":
            pass  # Keine Gewinnmitnahme im Uptrend — HODL
        elif step < _WARMUP_STEPS:
            if e_long > thr_medium and trend != "downtrend":
                if sell_vol_mod == "amplified":
                    action = "SELL_SMALL"
        else:
            sell_boost = ac_phase == "peak"
            sell_dampen = ac_phase == "trough"

            if e_long > thr_medium:
                if trend != "downtrend":
                    if sell_dampen:
                        action = "SELL_SMALL"  # Trough: nur SMALL (anti-resonant)
                    elif sz == "tight":
                        action = "SELL_SMALL"
                    elif cz == "dry":
                        action = "SELL_MEDIUM"
                    elif sell_boost and ac_amp_bin == "wide":
                        action = "SELL_MEDIUM"  # Peak + breite Schwingung → MEDIUM
                    elif sell_vol_mod != "damped":
                        action = "SELL_MEDIUM" if cz == "low" else "SELL_SMALL"
                    else:
                        action = "SELL_SMALL"
                else:
                    if sz != "tight":
                        action = "SELL_SMALL"
            elif e_long > thr_small:
                if trend in ("sideways", "none"):
                    if sell_dampen:
                        pass  # Trough + schwaches Signal → HOLD
                    elif sell_vol_mod != "damped":
                        if cz not in ("high",):
                            if sz != "tight":
                                action = "SELL_SMALL"

    # === SELL-Modus 2: Bounce-SELL im Downtrend ===
    if action == "HOLD" and allow_sell and sz != "locked" and pos in ("LONG", "PARTIAL"):
        if trend == "downtrend" and e_short > 0.01 and e_long < 0:
            if cz not in ("high",):
                action = "SELL_SMALL"

    # === BUY-Logik (höhere Schwellen — konservativ) ===
    # A1: Trough → BUY ist resonant (niedrigere Schwelle)
    #     Peak → BUY ist anti-resonant (höhere Schwelle)
    if action == "HOLD" and allow_buy:
        can_buy = False
        if pos in ("FLAT", "PARTIAL"):
            can_buy = True
        elif pos == "LONG" and cash_share > 0.05:
            can_buy = True

        if can_buy and e_long < 0:
            has_medium_cash = cash_share > 0.10

            if trend == "downtrend":
                thr_small_eff = 0.04
                thr_medium_eff = 0.06
            else:
                thr_small_eff = 0.03
                thr_medium_eff = 0.04

            # A1: AC-Phase moduliert BUY-Schwellen
            if ac_phase == "peak":
                thr_small_eff += 0.01
                thr_medium_eff += 0.01
            elif ac_phase == "trough" and ac_amp_bin != "narrow":
                thr_small_eff -= 0.005
                thr_medium_eff -= 0.005

            if e_long < -thr_medium_eff:
                if trend == "downtrend":
                    if cz == "high":
                        action = "BUY_MEDIUM"
                    elif vol_mod == "amplified" and has_medium_cash:
                        action = "BUY_MEDIUM"
                    else:
                        action = "BUY_SMALL"
                else:
                    if cz == "high":
                        action = "BUY_MEDIUM"
                    elif vol_mod != "damped" and has_medium_cash:
                        action = "BUY_MEDIUM"
                    else:
                        action = "BUY_SMALL"
            elif e_long < -thr_small_eff:
                if trend == "downtrend":
                    action = "BUY_MEDIUM" if cz == "high" else "BUY_SMALL"
                elif trend in ("uptrend", "sideways", "none"):
                    if cz == "high":
                        action = "BUY_MEDIUM"
                    elif vol_mod == "amplified" and has_medium_cash:
                        action = "BUY_MEDIUM"
                    else:
                        action = "BUY_SMALL"

    # === BUY-Modus 2: Regime-Akkumulation ===
    if action == "HOLD" and allow_buy and pos in ("PARTIAL", "FLAT"):
        regime = state.get("regime", "NORMAL")
        if regime == "BULL_STRONG" or trend == "uptrend":
            if cash_share > 0.05 and e_long < 0.01:
                action = "BUY_SMALL"

    # === BALANCE-REGLER (A4: Kopplungsenergie E = π·ε·h·f) ===
    # Die Kopplungseffizienz ε erfordert, dass beide Resonanzräume
    # (Cash und BTC) gefüllt sind. Bei ε → 0 bricht die Kopplung ab,
    # das System verliert seine Handlungsfähigkeit.
    if action.startswith("BUY") and cash_share < 0.08:
        action = "HOLD"
    if action.startswith("SELL") and sellable_share < 0.05:
        action = "HOLD"

    return action


# ===== Erfahrungsbasierte Policy =====

def experience_scores(state: dict, exp: dict) -> dict:
    scores: dict = {}
    for a in ALL_ACTIONS:
        chain = make_chain(state, a)
        s = exp.get((chain, "success"), 0)
        f = exp.get((chain, "failure"), 0)
        scores[a] = float(s - f)
    return scores


def experience_rates(state: dict, exp: dict) -> dict:
    rates: dict = {}
    for a in ALL_ACTIONS:
        chain = make_chain(state, a)
        s = exp.get((chain, "success"), 0)
        f = exp.get((chain, "failure"), 0)
        d = exp.get((chain, "draw"), 0)
        decisive = s + f
        if decisive > 0:
            rates[a] = float(s) / decisive
        else:
            rates[a] = 0.5
    return rates


def experience_confidence(scores: dict) -> float:
    total = sum(abs(v) for v in scores.values())
    return 1.0 - math.exp(-total / 100.0)


def _experience_counts(state: dict, exp: dict) -> dict:
    counts: dict = {}
    for a in ALL_ACTIONS:
        chain = make_chain(state, a)
        s = exp.get((chain, "success"), 0)
        f = exp.get((chain, "failure"), 0)
        d = exp.get((chain, "draw"), 0)
        counts[a] = s + f + d
    return counts


# ===== Score-Normalisierung =====

def _normalize_score(score: float, all_scores: dict) -> float:
    vals = list(all_scores.values())
    mn = min(vals)
    mx = max(vals)
    spread = mx - mn

    if spread < 1e-9:
        return 0.5

    base = (score - mn) / spread

    if spread < NORM_SPREAD_REF:
        k = spread / NORM_SPREAD_REF
        return 0.5 + (base - 0.5) * k

    return base


# ===== Signal-Stärke =====

def _signal_strength(state: dict) -> float:
    e_long = abs(float(state.get("e_long", 0.0) or 0.0))
    e_short = abs(float(state.get("e_short", 0.0) or 0.0))
    e_max = max(e_long, e_short)
    return min(1.0, e_max / (e_max + 0.02))


# ===== Hybride Lern-Policy =====

def resonance_learning_policy(
    state: dict,
    exp: dict,
    epsilon: float = 0.05,
    experience_weight: float = 0.6,
) -> Action:
    """
    Hybride Policy: Regelwissen + Erfahrung.

    Verbindet die resonanzlogische Regel-Policy (A1, A4, A5, A6)
    mit dem Erfahrungsspeicher. Der Erfahrungsanteil steigt mit der
    Konfidenz (Anzahl gesehener States). Exploration ist regime-bewusst.
    """
    allowed = _allowed_actions_for_regime(state)
    if len(allowed) == 1:
        return allowed[0]

    if random.random() < epsilon:
        return _exploration_action(state, allowed)

    rule_action = ma_profit_switch_policy(state)

    if rule_action not in allowed:
        rule_action = "HOLD"

    rates = experience_rates(state, exp)
    counts = _experience_counts(state, exp)
    scores = experience_scores(state, exp)
    confidence = experience_confidence(scores)

    sig = _signal_strength(state)
    min_rule_share = max(0.20, 0.50 - 0.30 * sig)
    eff_weight = experience_weight * confidence
    rule_share = max(min_rule_share, 1.0 - eff_weight)
    exp_share = 1.0 - rule_share

    MIN_COUNTS_FOR_TRUST = 50
    MIN_COUNTS_FOR_PARTIAL = 5

    allowed_rates = {a: rates[a] for a in allowed}
    norm_rates = {a: _normalize_score(r, allowed_rates) for a, r in allowed_rates.items()}

    adj_scores: dict = {}
    for a in allowed:
        count = counts[a]
        if count < MIN_COUNTS_FOR_PARTIAL:
            adj_scores[a] = 0.5
        elif count < MIN_COUNTS_FOR_TRUST:
            trust = (count - MIN_COUNTS_FOR_PARTIAL) / (MIN_COUNTS_FOR_TRUST - MIN_COUNTS_FOR_PARTIAL)
            adj_scores[a] = 0.5 + (norm_rates[a] - 0.5) * trust
        else:
            adj_scores[a] = norm_rates[a]

    combined: dict = {}
    for a in allowed:
        rule_bonus = 0.7 if a == rule_action else 0.1
        combined[a] = rule_share * rule_bonus + exp_share * adj_scores[a]

    max_score = max(combined.values())
    best = [a for a, s in combined.items() if abs(s - max_score) < 1e-9]
    return random.choice(best)


# ===== Gerichtete Exploration =====

def _exploration_action(state: dict, allowed: list = None) -> Action:
    """
    Regime-bewusste Exploration.

    A5 (Energierichtung) lenkt die Exploration: Bei negativem e_long
    werden BUY-Aktionen bevorzugt exploriert, bei positivem e_long
    SELL-Aktionen — resonant mit der Energierichtung.
    """
    if allowed is None:
        allowed = list(ALL_ACTIONS)

    pos = state.get("pos", "FLAT")
    e_long = float(state.get("e_long", 0.0) or 0.0)
    e_short = float(state.get("e_short", 0.0) or 0.0)
    cash_share = float(state.get("cash_share", 0.0) or 0.0)
    sellable_share = float(state.get("sellable_share", 1.0) or 1.0)
    trend = state.get("trend_bin", "none")

    can_sell = sellable_share >= 0.01
    can_buy = cash_share > 0.05

    if trend == "downtrend" and e_short > 0.01 and e_long < 0 and can_sell:
        choices = ["HOLD", "SELL_SMALL", "SELL_SMALL", "SELL_MEDIUM"]
    elif e_long < -0.01 and can_buy:
        choices = ["HOLD", "BUY_SMALL", "BUY_SMALL", "BUY_MEDIUM"]
    elif e_long > 0.01 and pos in ("LONG", "PARTIAL") and can_sell:
        choices = ["HOLD", "SELL_SMALL", "SELL_SMALL", "SELL_MEDIUM"]
    else:
        if pos == "LONG":
            choices = ["HOLD", "SELL_SMALL", "SELL_MEDIUM"] if can_sell else ["HOLD"]
        elif pos == "FLAT":
            choices = ["HOLD", "BUY_SMALL", "BUY_MEDIUM"] if can_buy else ["HOLD"]
        else:
            choices = ["HOLD"]
            if can_buy:
                choices.extend(["BUY_SMALL", "BUY_MEDIUM"])
            if can_sell:
                choices.extend(["SELL_SMALL", "SELL_MEDIUM"])

    choices = [c for c in choices if c in allowed]
    if not choices:
        choices = ["HOLD"]

    return random.choice(choices)


# ===== Legacy =====

def random_policy(state: dict) -> Action:
    if state.get("pos") == "LONG":
        choices: list = ["HOLD", "HOLD", "SELL_SMALL", "SELL_MEDIUM", "HOLD"]
    else:
        choices = ["HOLD", "HOLD", "BUY_SMALL", "BUY_MEDIUM", "HOLD"]
    return random.choice(choices)


def resonance_policy(state: dict, exp: dict) -> Action:
    """Legacy: reine Erfahrungs-Policy ohne Regel-Vorwissen."""
    scores = experience_scores(state, exp)
    max_score = max(scores.values())
    best = [a for a, s in scores.items() if s == max_score]
    if len(best) == len(ALL_ACTIONS):
        return random_policy(state)
    return random.choice(best)