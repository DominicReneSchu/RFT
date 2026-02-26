from dataclasses import dataclass, field
from typing import List
import time


@dataclass
class Lot:
    """
    Ein einzelner Kauf-Lot mit Tracking-Informationen.
    Jeder BUY erzeugt einen Lot, jeder SELL schließt Lots (FIFO).
    """
    btc_amount: float
    entry_price: float
    entry_step: int = 0
    entry_timestamp: float = 0.0
    peak_price: float = 0.0      # Höchster Preis seit Kauf

    def __post_init__(self):
        if self.peak_price <= 0:
            self.peak_price = self.entry_price
        if self.entry_timestamp <= 0:
            self.entry_timestamp = time.time()

    def unrealized_pnl_pct(self, current_price: float) -> float:
        """Unrealisierter Gewinn/Verlust in Prozent."""
        if self.entry_price <= 0:
            return 0.0
        return (current_price - self.entry_price) / self.entry_price

    def update_peak(self, current_price: float):
        """Aktualisiert den Peak-Preis (für Trailing-Stop)."""
        if current_price > self.peak_price:
            self.peak_price = current_price

    def steps_held(self, current_step: int) -> int:
        """Wie viele Schritte wird dieser Lot schon gehalten."""
        return current_step - self.entry_step


@dataclass
class SellRecord:
    """
    Aufzeichnung eines Verkaufs für Rebuy-Tracking.
    Nach einem SELL wird gewartet, bis der Preis unter
    sell_price * (1 - rebuy_discount) fällt, bevor ein Rückkauf sinnvoll ist.
    """
    usd_amount: float
    sell_price: float
    sell_step: int = 0
    sell_timestamp: float = 0.0
    fulfilled: bool = False       # True wenn Rückkauf erfolgt ist

    def __post_init__(self):
        if self.sell_timestamp <= 0:
            self.sell_timestamp = time.time()

    def rebuy_target_price(self, discount_pct: float) -> float:
        """Zielpreis für Rückkauf (sell_price minus Discount)."""
        return self.sell_price * (1.0 - discount_pct)


@dataclass
class Portfolio:
    """
    BTC/USD-Portfolio V9.4 mit Lot-Tracking.

    Jeder BUY erzeugt einen Lot (Kaufpreis, Menge, Zeitpunkt).
    Jeder SELL schließt Lots in FIFO-Reihenfolge.
    Lots ermöglichen:
      - Präzises Tracking welche BTC profitabel sind
      - FIFO-basierte Gewinnmitnahme
      - Rückkauf-Tracking nach SELL (Discount-Schwelle)
    """
    btc: float
    cash: float
    price: float
    lots: List[Lot] = field(default_factory=list)
    sell_records: List[SellRecord] = field(default_factory=list)
    _total_realized_pnl: float = 0.0

    def value_usd(self) -> float:
        return self.cash + self.btc * self.price

    def btc_in_lots(self) -> float:
        """BTC-Menge die in aktiven Lots gehalten wird."""
        return sum(lot.btc_amount for lot in self.lots)

    def avg_entry_price(self) -> float:
        """Gewichteter Durchschnittskaufpreis aller offenen Lots."""
        total_btc = sum(lot.btc_amount for lot in self.lots)
        if total_btc <= 1e-10:
            return 0.0
        weighted_sum = sum(lot.btc_amount * lot.entry_price for lot in self.lots)
        return weighted_sum / total_btc

    def unrealized_pnl_pct(self) -> float:
        """Gewichteter unrealisierter PnL über alle Lots."""
        total_btc = sum(lot.btc_amount for lot in self.lots)
        if total_btc <= 1e-10 or self.price <= 0:
            return 0.0
        avg_entry = self.avg_entry_price()
        if avg_entry <= 0:
            return 0.0
        return (self.price - avg_entry) / avg_entry

    def profitable_lots(self, min_profit_pct: float = 0.0) -> List[Lot]:
        """Gibt alle Lots zurück die mindestens min_profit_pct Gewinn haben."""
        if self.price <= 0:
            return []
        return [
            lot for lot in self.lots
            if lot.unrealized_pnl_pct(self.price) >= min_profit_pct
        ]

    def profitable_btc(self, min_profit_pct: float = 0.0) -> float:
        """BTC-Menge in profitablen Lots."""
        return sum(lot.btc_amount for lot in self.profitable_lots(min_profit_pct))

    def stale_lots(self, current_step: int, max_hold_steps: int) -> List[Lot]:
        """Lots die zu lange gehalten werden (Timeout)."""
        return [
            lot for lot in self.lots
            if lot.steps_held(current_step) >= max_hold_steps
        ]

    def unfulfilled_sell_records(self) -> List[SellRecord]:
        """Sell-Records die noch keinen Rückkauf hatten."""
        return [sr for sr in self.sell_records if not sr.fulfilled]

    def pending_rebuy_usd(self) -> float:
        """USD-Menge die auf Rückkauf wartet."""
        return sum(sr.usd_amount for sr in self.unfulfilled_sell_records())

    def update_lot_peaks(self):
        """Aktualisiert Peak-Preise aller Lots."""
        for lot in self.lots:
            lot.update_peak(self.price)

    def apply_trade(self, action: str, fraction: float = 1.0, fee_pct: float = 0.001,
                    current_step: int = 0):
        """
        V9.4: Trade-Aktion mit Lot-Tracking.

        BUY: Erzeugt neuen Lot mit Kaufpreis.
        SELL: Schließt Lots in FIFO-Reihenfolge, erzeugt SellRecord.
        HOLD: Aktualisiert nur Peak-Preise.
        """
        # Peaks immer aktualisieren
        self.update_lot_peaks()

        if action == "HOLD":
            return

        fraction = max(0.0, min(1.0, fraction))
        if self.price <= 0:
            return

        if action == "BUY":
            notional = self.cash * fraction
            if notional <= 0:
                return
            fee = notional * fee_pct
            btc_net = max(0.0, (notional - fee) / self.price)
            self.cash -= notional
            self.btc += btc_net

            # Neuen Lot erzeugen
            self.lots.append(Lot(
                btc_amount=btc_net,
                entry_price=self.price,
                entry_step=current_step,
            ))

            # Prüfe ob ein SellRecord erfüllt wird
            for sr in self.sell_records:
                if not sr.fulfilled and self.price <= sr.rebuy_target_price(0.005):
                    sr.fulfilled = True

        elif action == "SELL":
            btc_to_sell = self.btc * fraction
            if btc_to_sell <= 0:
                return
            gross = btc_to_sell * self.price
            fee = gross * fee_pct
            cash_net = max(0.0, gross - fee)
            self.btc -= btc_to_sell
            self.cash += cash_net

            # Lots in FIFO-Reihenfolge schließen
            remaining_sell = btc_to_sell
            realized_pnl = 0.0
            while remaining_sell > 1e-10 and self.lots:
                lot = self.lots[0]
                consume = min(lot.btc_amount, remaining_sell)
                lot_pnl = consume * (self.price - lot.entry_price) - (consume * self.price * fee_pct)
                realized_pnl += lot_pnl

                lot.btc_amount -= consume
                remaining_sell -= consume

                if lot.btc_amount <= 1e-10:
                    self.lots.pop(0)

            self._total_realized_pnl += realized_pnl

            # SellRecord für Rebuy-Tracking
            self.sell_records.append(SellRecord(
                usd_amount=cash_net,
                sell_price=self.price,
                sell_step=current_step,
            ))

            # SellRecords aufräumen (max 50 behalten)
            fulfilled = [sr for sr in self.sell_records if sr.fulfilled]
            if len(fulfilled) > 50:
                self.sell_records = [sr for sr in self.sell_records if not sr.fulfilled] + fulfilled[-20:]

    @property
    def total_realized_pnl(self) -> float:
        return self._total_realized_pnl