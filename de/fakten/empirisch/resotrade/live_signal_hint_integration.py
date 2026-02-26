"""
Integration des Human-Hint-Systems in live_signal.py
=====================================================
Diese Funktionen werden in live_signal.py eingebunden.
"""

from human_hint import load_hint, is_paused, hint_bias_adjustment


def get_live_expectation(df, experience, current_state):
    """
    Zeigt dem Menschen, was das System aktuell erwartet.
    Aufruf: python live_signal.py expectation
    """
    hint = load_hint()

    # Aktuelle Marktdaten
    price = df['price'].iloc[-1]
    trend = current_state.get('trend', 'unknown')
    regime = current_state.get('regime', 'unknown')
    e_long = current_state.get('e_long', 0.0)
    resonance = current_state.get('resonance_score', 0.0)

    # Posterior-Winrates aus Erfahrung
    buy_wr = current_state.get('posterior_buy_7d', 0.5)
    sell_wr = current_state.get('posterior_sell_7d', 0.5)

    # Erwartung ableiten
    if sell_wr > buy_wr + 0.05 and trend == "downtrend":
        expectation = "FALLEND"
        confidence = min(95, int((sell_wr - buy_wr) * 200 + 50))
    elif buy_wr > sell_wr + 0.05 and trend == "uptrend":
        expectation = "STEIGEND"
        confidence = min(95, int((buy_wr - sell_wr) * 200 + 50))
    else:
        expectation = "SEITWAERTS"
        confidence = max(30, int(50 - abs(buy_wr - sell_wr) * 100))

    # Geplante Aktion
    planned_action = current_state.get('planned_action', 'HOLD')
    blocked_by = current_state.get('blocked_by', None)

    print("")
    print("============================================================")
    print("ResoTrade Live-Erwartung")
    print("============================================================")
    print(f"  Preis:          {price:.2f} USD")
    print(f"  Trend:          {trend}")
    print(f"  Regime:         {regime}")
    print(f"  e_long:         {e_long*100:+.1f}%")
    print(f"  Resonance:      {resonance:.2f}")
    print(f"")
    print(f"  ERWARTUNG:      {expectation} (Konfidenz: {confidence}%)")
    print(f"  Buy-Winrate:    {buy_wr:.3f}")
    print(f"  Sell-Winrate:   {sell_wr:.3f}")
    print(f"")
    print(f"  Geplante Aktion: {planned_action}")
    if blocked_by:
        print(f"  Blockiert durch: {blocked_by}")
    print("")

    # Human Hint Status
    if hint:
        bias = hint.get('bias', 'neutral').upper()
        reason = hint.get('reason', '-')
        weight = hint.get('weight', 0.3)
        print(f"  Human Hint:     {bias} (w={weight})")
        print(f"  Grund:          {reason}")
        if is_paused(hint):
            print(f"  PAUSE aktiv bis {hint['pause_until']}")

        # Zeige was der Hint bewirken wuerde
        adj_action, adj_reason = hint_bias_adjustment(
            hint, planned_action, trend
        )
        if adj_action != planned_action:
            print(f"  Hint-Wirkung:   {planned_action} -> {adj_action}")
            print(f"                  ({adj_reason})")
        else:
            print(f"  Hint-Wirkung:   keine (Aktion passt zum Hint)")
    else:
        print("  Human Hint:     KEINER (System autonom)")

    print("============================================================")
    print("")
    print("Hinweis setzen:")
    print("  python human_hint.py bullish \"EZB senkt Zinsen\"")
    print("  python human_hint.py bearish \"SEC verklagt Boerse\"")
    print("  python human_hint.py pause 12 \"FOMC in 6h\"")
    print("  python human_hint.py clear")
    print("")


def apply_human_hint_to_action(action: str, trend: str) -> tuple:
    """
    Wird in der Live-Schleife nach der Policy-Entscheidung aufgerufen.
    Gibt (angepasste_aktion, hint_info) zurueck.

    Einbindung in live_signal.py:
        action = policy.decide(state)
        action, hint_info = apply_human_hint_to_action(action, trend)
        if hint_info:
            log(f"[Hint] {hint_info}")
    """
    hint = load_hint()
    if hint is None:
        return action, None

    adjusted, reason = hint_bias_adjustment(hint, action, trend)

    if adjusted != action:
        print(f"[Hint] {action} -> {adjusted} ({reason})")

    return adjusted, reason