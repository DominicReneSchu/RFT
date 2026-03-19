"""
train_gold_offline.py — Kompatibilitäts-Wrapper für Gold-Training (ResoTrade V14)

Dieses Modul leitet alle Aufrufe an die asset-invariante train_offline.py-Pipeline
weiter und verwendet GOLD_CONFIG aus asset_config.py.

Re-Exporte stellen sicher, dass bestehende Downstream-Consumer
(z. B. plot_gold_trades.py) weiterhin funktionieren.
"""

from train_offline import train_offline, train_asset_multi_pass, prepare_asset_data
from train_offline import _ensure_columns
from asset_config import GOLD_CONFIG

# ---------------------------------------------------------------------------
# Backward-compatibility alias (train_asset → train_offline)
# ---------------------------------------------------------------------------

#: Legacy alias — prefer calling ``train_offline(GOLD_CONFIG)`` directly.
train_asset = train_offline


# ---------------------------------------------------------------------------
# Convenience helpers
# ---------------------------------------------------------------------------

def train() -> dict:
    """Run a single training pass for Gold using GOLD_CONFIG."""
    return train_offline(GOLD_CONFIG)


def train_multi_pass(passes: int | None = None) -> list:
    """Run multiple training passes for Gold using GOLD_CONFIG."""
    return train_asset_multi_pass(GOLD_CONFIG, passes=passes)


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    results = train_multi_pass()
    for r in results:
        print(
            f"[GOLD] Pass {r['pass']}: episodes={r['episodes']}, "
            f"trades={r['trades']}, score={r['final_score']:.4f}"
        )
