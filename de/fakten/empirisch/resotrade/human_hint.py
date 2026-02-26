"""
ResoTrade V11.1 - Human Hint System
====================================
Der Mensch gibt Hinweise, keine Befehle.
Hinweise fliessen als zusaetzliches Signal in die Policy ein
und werden in den Erfahrungsspeicher integriert.

Beispiel:
  python human_hint.py bullish "EZB senkt Zinsen, Liquiditaet steigt"
  python human_hint.py bearish "SEC verklagt Binance, Unsicherheit"
  python human_hint.py neutral "Keine relevanten Nachrichten"
  python human_hint.py pause 12 "FOMC-Meeting in 6h, abwarten"
  python human_hint.py status
  python human_hint.py clear
"""

import json
import os
import sys
from datetime import datetime, timezone, timedelta

HINT_PATH = os.path.join("data", "human_hint.json")
HINT_LOG_PATH = os.path.join("data", "human_hint_log.csv")

# Wie stark der Hinweis die Policy beeinflusst (0.0 = ignoriert, 1.0 = dominant)
# Default 0.3 = sanfter Einfluss, System bleibt fuehrend
DEFAULT_WEIGHT = 0.3
HINT_EXPIRY_HOURS = 48  # Hinweis verfaellt nach 48h wenn nicht erneuert


def create_hint(bias: str, reason: str = "", pause_hours: float = 0,
                weight: float = DEFAULT_WEIGHT):
    """Erstellt einen neuen Hinweis."""
    hint = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "bias": bias,           # bullish / bearish / neutral
        "reason": reason,       # Freitext: warum der Mensch das denkt
        "weight": weight,       # 0.0-1.0: wie stark der Hinweis wirkt
        "pause_until": None,
        "active": True,
    }

    if pause_hours > 0:
        pause_end = datetime.now(timezone.utc) + timedelta(hours=pause_hours)
        hint["pause_until"] = pause_end.isoformat()

    os.makedirs("data", exist_ok=True)

    # Hinweis speichern
    with open(HINT_PATH, "w") as f:
        json.dump(hint, f, indent=2)

    # Hinweis-Log (fuer spaetere Auswertung: waren die Hinweise gut?)
    log_line = (f"{hint['timestamp']},{bias},{weight},"
                f"{pause_hours},\"{reason}\"\n")
    write_header = not os.path.exists(HINT_LOG_PATH)
    with open(HINT_LOG_PATH, "a") as f:
        if write_header:
            f.write("timestamp,bias,weight,pause_hours,reason\n")
        f.write(log_line)

    print(f"[Hint] Gespeichert: {bias} (Gewicht {weight})")
    print(f"[Hint] Grund: {reason}")
    if pause_hours > 0:
        print(f"[Hint] Pause: {pause_hours}h bis {hint['pause_until']}")
    print(f"[Hint] Verfaellt automatisch nach {HINT_EXPIRY_HOURS}h")
    return hint


def load_hint():
    """
    Laedt den aktuellen Hinweis.
    Gibt None zurueck wenn kein Hinweis existiert oder er abgelaufen ist.
    """
    if not os.path.exists(HINT_PATH):
        return None

    with open(HINT_PATH) as f:
        hint = json.load(f)

    if not hint.get("active", False):
        return None

    # Ablauf pruefen
    ts = datetime.fromisoformat(hint["timestamp"])
    now = datetime.now(timezone.utc)
    age_hours = (now - ts).total_seconds() / 3600

    if age_hours > HINT_EXPIRY_HOURS:
        print(f"[Hint] Abgelaufen (Alter: {age_hours:.1f}h > {HINT_EXPIRY_HOURS}h)")
        return None

    return hint


def is_paused(hint: dict) -> bool:
    """Prueft ob der Mensch eine Pause angeordnet hat."""
    if hint is None:
        return False
    pause_until = hint.get("pause_until")
    if pause_until is None:
        return False
    pause_end = datetime.fromisoformat(pause_until)
    return datetime.now(timezone.utc) < pause_end


def hint_bias_adjustment(hint: dict, action: str, trend: str) -> tuple:
    """
    Passt die System-Aktion basierend auf dem menschlichen Hinweis an.

    Abstufung nach Gewicht:
      weight >= 0.3 (Default): SMALL + MEDIUM blockiert
      weight <  0.3:           nur MEDIUM blockiert (minimaler Eingriff)
    """
    if hint is None:
        return action, None

    # Pause: alles blockieren
    if is_paused(hint):
        if action != "HOLD":
            return "HOLD", f"human_pause (bis {hint['pause_until']})"
        return action, None

    bias = hint.get("bias", "neutral")
    weight = hint.get("weight", DEFAULT_WEIGHT)

    # Neutral = kein Eingriff
    if bias == "neutral":
        return action, None

    # Bullish-Hinweis: Verkaeufe abschwaechen
    if bias == "bullish" and action in ("SELL_SMALL", "SELL_MEDIUM"):
        if weight >= 0.3 or action == "SELL_MEDIUM":
            return "HOLD", f"human_hint_bullish (w={weight})"
        return action, None

    # Bearish-Hinweis: Kaeufe abschwaechen
    if bias == "bearish" and action in ("BUY_SMALL", "BUY_MEDIUM"):
        if weight >= 0.3 or action == "BUY_MEDIUM":
            return "HOLD", f"human_hint_bearish (w={weight})"
        return action, None

    return action, None


def clear_hint():
    """Loescht den aktuellen Hinweis."""
    if os.path.exists(HINT_PATH):
        with open(HINT_PATH) as f:
            hint = json.load(f)
        hint["active"] = False
        with open(HINT_PATH, "w") as f:
            json.dump(hint, f, indent=2)
        print("[Hint] Hinweis deaktiviert.")
    else:
        print("[Hint] Kein Hinweis vorhanden.")


def show_status():
    """Zeigt den aktuellen Hinweis-Status."""
    hint = load_hint()
    if hint is None:
        print("============================================================")
        print("Human Hint: KEIN AKTIVER HINWEIS")
        print("System entscheidet autonom.")
        print("============================================================")
        return

    ts = datetime.fromisoformat(hint["timestamp"])
    now = datetime.now(timezone.utc)
    age = now - ts
    remaining = timedelta(hours=HINT_EXPIRY_HOURS) - age

    print("============================================================")
    print("Human Hint: AKTIV")
    print(f"  Bias:       {hint['bias'].upper()}")
    print(f"  Gewicht:    {hint['weight']}")
    print(f"  Grund:      {hint.get('reason', '-')}")
    print(f"  Gesetzt:    {hint['timestamp']}")
    print(f"  Alter:      {age.total_seconds()/3600:.1f}h")
    print(f"  Verbleibt:  {max(0, remaining.total_seconds()/3600):.1f}h")
    if is_paused(hint):
        print(f"  PAUSE:      aktiv bis {hint['pause_until']}")
    print("============================================================")

    # Hint-Log Statistik
    if os.path.exists(HINT_LOG_PATH):
        import pandas as pd
        log = pd.read_csv(HINT_LOG_PATH)
        print(f"\nHint-Historie: {len(log)} Hinweise insgesamt")
        print(f"  bullish: {len(log[log.bias == 'bullish'])}")
        print(f"  bearish: {len(log[log.bias == 'bearish'])}")
        print(f"  neutral: {len(log[log.bias == 'neutral'])}")


# === CLI ===
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(0)

    cmd = sys.argv[1].lower()

    if cmd == "status":
        show_status()

    elif cmd == "clear":
        clear_hint()

    elif cmd == "pause":
        hours = float(sys.argv[2]) if len(sys.argv) > 2 else 24
        reason = sys.argv[3] if len(sys.argv) > 3 else "Manuelle Pause"
        create_hint("neutral", reason, pause_hours=hours)

    elif cmd in ("bullish", "bearish", "neutral"):
        reason = sys.argv[2] if len(sys.argv) > 2 else ""
        weight = float(sys.argv[3]) if len(sys.argv) > 3 else DEFAULT_WEIGHT
        create_hint(cmd, reason, weight=weight)

    else:
        print(f"Unbekannter Befehl: {cmd}")
        print("Verfuegbar: bullish, bearish, neutral, pause, status, clear")