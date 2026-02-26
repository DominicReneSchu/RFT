"""
Kraken REST API Client für ResoTrade V9.

Verbesserungen:
  - Monotone Nonce (Thread-safe, keine Kollisionen)
  - Keyring-Support als primäre Key-Quelle
  - Order-Fill-Validierung nach Platzierung
  - Robusteres Error-Handling

Key-Quellen (Priorität):
  1. OS-Keyring (Service: "resotrade", Username: "api_key" / "api_secret")
  2. kraken.key Datei (2 Zeilen: Key + Secret)

Keyring befüllen (einmalig):
  python -c "
  import keyring
  keyring.set_password('resotrade', 'api_key', 'DEIN-API-KEY')
  keyring.set_password('resotrade', 'api_secret', 'DEIN-API-SECRET')
  "
"""
import csv
import hashlib
import hmac
import base64
import time
import threading
import urllib.parse
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import requests

from config import (
    KRAKEN_KEY_FILE,
    KRAKEN_PAIR,
    KRAKEN_ORDER_PAIR,
    KRAKEN_FEE_PCT,
    DRY_RUN,
    MAX_SINGLE_ORDER_USD,
    MAX_SINGLE_ORDER_BTC,
    MIN_BTC_ORDER,
    MIN_USD_ORDER,
    LIVE_LOG_DIR,
    COOLDOWN_SECONDS,
)

KRAKEN_API_URL = "https://api.kraken.com"
KEYRING_SERVICE = "resotrade"

# Maximale Wartezeit für Order-Fill-Validierung
ORDER_VALIDATE_TIMEOUT = 30  # Sekunden
ORDER_VALIDATE_INTERVAL = 3  # Sekunden zwischen Polls


class KrakenClient:
    """
    Minimaler Kraken-Client mit Signature-Auth.
    Thread-safe Nonce, Keyring-Support, Order-Validierung.
    """

    _nonce_lock = threading.Lock()
    _last_nonce: int = 0

    def __init__(self, key_file: Optional[Path] = None):
        self._api_key, self._api_secret = self._load_keys_with_fallback(key_file)
        self._session = requests.Session()
        self._session.headers.update({
            "User-Agent": "ResoTrade/9.1",
        })
        LIVE_LOG_DIR.mkdir(parents=True, exist_ok=True)
        self._last_order_time: float = 0.0
        self._last_ticker: Optional[dict] = None
        self._last_ticker_time: float = 0.0
        self._ticker_cache_seconds: float = 10.0

    # === Key-Loading ===

    @staticmethod
    def _load_keys_with_fallback(key_file: Optional[Path] = None) -> tuple:
        """
        Lädt API-Keys. Priorität:
          1. OS-Keyring
          2. kraken.key Datei
        """
        # 1. Keyring versuchen
        try:
            import keyring
            api_key = keyring.get_password(KEYRING_SERVICE, "api_key")
            api_secret = keyring.get_password(KEYRING_SERVICE, "api_secret")
            if api_key and api_secret:
                print("[Kraken] API-Keys aus OS-Keyring geladen.")
                return api_key.strip(), api_secret.strip()
        except ImportError:
            pass  # keyring nicht installiert
        except Exception as e:
            print(f"[Kraken] Keyring-Zugriff fehlgeschlagen: {e}")

        # 2. Datei-Fallback
        key_path = key_file or KRAKEN_KEY_FILE
        return KrakenClient._load_keys_from_file(key_path)

    @staticmethod
    def _strip_prefix(line: str) -> str:
        stripped = line.strip()
        if "=" in stripped:
            _, _, value = stripped.partition("=")
            return value.strip()
        return stripped

    @staticmethod
    def _load_keys_from_file(path: Path) -> tuple:
        if not path.exists():
            raise FileNotFoundError(
                f"Kraken-Key-Datei nicht gefunden: {path}\n"
                f"Option 1: Datei erstellen (Zeile 1 = API-Key, Zeile 2 = API-Secret)\n"
                f"Option 2: Keys im OS-Keyring speichern:\n"
                f"  python -c \"\n"
                f"  import keyring\n"
                f"  keyring.set_password('resotrade', 'api_key', 'DEIN-KEY')\n"
                f"  keyring.set_password('resotrade', 'api_secret', 'DEIN-SECRET')\n"
                f"  \""
            )
        raw = path.read_text(encoding="utf-8-sig").strip()
        lines = [l for l in raw.splitlines() if l.strip()]

        if len(lines) < 2:
            raise ValueError(
                f"kraken.key muss mindestens 2 nicht-leere Zeilen enthalten, "
                f"gefunden: {len(lines)}"
            )

        api_key = KrakenClient._strip_prefix(lines[0])
        api_secret = KrakenClient._strip_prefix(lines[1])

        if not api_key or not api_secret:
            raise ValueError(
                "API-Key oder API-Secret in kraken.key ist leer "
                "(nach Entfernung von Präfixen)"
            )

        try:
            api_key.encode("ascii")
            api_secret.encode("ascii")
        except UnicodeEncodeError as e:
            raise ValueError(
                f"kraken.key enthält ungültige Zeichen. "
                f"Bitte als 'UTF-8 ohne BOM' speichern. Detail: {e}"
            )

        print("[Kraken] API-Keys aus Datei geladen.")
        return api_key, api_secret

    # === Nonce (Thread-safe, monoton steigend) ===

    def _nonce(self) -> str:
        """
        Streng monoton steigende Nonce.
        Thread-safe: Lock verhindert Kollisionen bei parallelen Aufrufen.
        """
        with KrakenClient._nonce_lock:
            candidate = int(time.time() * 1000)
            n = max(candidate, KrakenClient._last_nonce + 1)
            KrakenClient._last_nonce = n
            return str(n)

    # === Signatur ===

    def _sign(self, uri_path: str, data: dict) -> dict:
        postdata = urllib.parse.urlencode(data)
        encoded = (str(data["nonce"]) + postdata).encode("utf-8")
        message = uri_path.encode("utf-8") + hashlib.sha256(encoded).digest()
        signature = hmac.new(
            base64.b64decode(self._api_secret),
            message,
            hashlib.sha512,
        )
        return {
            "API-Key": self._api_key,
            "API-Sign": base64.b64encode(signature.digest()).decode("utf-8"),
        }

    # === API-Aufrufe ===

    def _public(self, endpoint: str, params: Optional[dict] = None) -> dict:
        url = f"{KRAKEN_API_URL}/0/public/{endpoint}"
        resp = self._session.get(url, params=params or {}, timeout=30)
        resp.raise_for_status()
        data = resp.json()
        errors = data.get("error", [])
        if errors:
            raise RuntimeError(f"Kraken API Error: {errors}")
        return data.get("result", {})

    def _private(self, endpoint: str, params: Optional[dict] = None) -> dict:
        uri_path = f"/0/private/{endpoint}"
        url = f"{KRAKEN_API_URL}{uri_path}"
        data = params or {}
        data["nonce"] = self._nonce()
        headers = self._sign(uri_path, data)
        resp = self._session.post(url, data=data, headers=headers, timeout=30)
        resp.raise_for_status()
        result = resp.json()
        errors = result.get("error", [])
        if errors:
            raise RuntimeError(f"Kraken API Error: {errors}")
        return result.get("result", {})

    # === Public Endpoints ===

    def get_ticker(self, pair: str = KRAKEN_PAIR, use_cache: bool = True) -> dict:
        now = time.time()
        if (use_cache
                and self._last_ticker is not None
                and (now - self._last_ticker_time) < self._ticker_cache_seconds):
            return self._last_ticker

        result = self._public("Ticker", {"pair": pair})
        if pair not in result:
            key = list(result.keys())[0] if result else pair
            ticker_data = result.get(key, {})
        else:
            ticker_data = result[pair]

        parsed = {
            "bid": float(ticker_data["b"][0]),
            "ask": float(ticker_data["a"][0]),
            "last": float(ticker_data["c"][0]),
            "volume_24h": float(ticker_data["v"][1]),
        }
        self._last_ticker = parsed
        self._last_ticker_time = now
        return parsed

    def get_ohlc(self, pair: str = KRAKEN_PAIR, interval: int = 60,
                 since: Optional[int] = None) -> list:
        params = {"pair": pair, "interval": interval}
        if since is not None:
            params["since"] = since
        result = self._public("OHLC", params)
        for key, val in result.items():
            if isinstance(val, list):
                return val
        return []

    # === Private Endpoints ===

    def get_balance(self) -> dict:
        raw = self._private("Balance")
        balances = {}
        for asset, amount in raw.items():
            val = float(amount)
            if val > 1e-10:
                balances[asset] = val
        return balances

    def get_btc_usd_balance(self) -> tuple:
        bal = self.get_balance()
        btc = bal.get("XXBT", bal.get("XBT", 0.0))
        usd = bal.get("ZUSD", bal.get("USD", 0.0))
        return btc, usd

    def get_open_orders(self) -> dict:
        return self._private("OpenOrders")

    def query_orders(self, txids: list) -> dict:
        """
        Fragt den Status spezifischer Orders ab.
        txids: Liste von Kraken Transaction-IDs.
        """
        if not txids:
            return {}
        txid_str = ",".join(txids)
        return self._private("QueryOrders", {"txid": txid_str})

    # === Order-Platzierung mit Fill-Validierung ===

    def place_order(
        self,
        side: str,
        volume_btc: float,
        order_type: str = "market",
        price: Optional[float] = None,
        validate_fill: bool = True,
    ) -> dict:
        """
        Platziert eine Order auf Kraken.

        Args:
            side: "buy" oder "sell"
            volume_btc: BTC-Menge
            order_type: "market" oder "limit"
            price: Nur für Limit-Orders
            validate_fill: True → prüft ob Order gefüllt wurde

        Returns:
            Order-Info dict mit Status und ggf. Fill-Info
        """
        volume_btc = abs(volume_btc)

        if volume_btc < MIN_BTC_ORDER:
            return {"status": "skipped", "reason": f"volume {volume_btc:.8f} < min {MIN_BTC_ORDER}"}

        # Cooldown-Check
        now = time.time()
        elapsed = now - self._last_order_time
        if elapsed < COOLDOWN_SECONDS and self._last_order_time > 0:
            return {
                "status": "skipped",
                "reason": f"cooldown: {elapsed:.0f}s < {COOLDOWN_SECONDS}s",
            }

        if volume_btc > MAX_SINGLE_ORDER_BTC:
            print(f"[Kraken] ⚠ Volume {volume_btc:.6f} BTC > Max {MAX_SINGLE_ORDER_BTC}, "
                  f"begrenzt auf {MAX_SINGLE_ORDER_BTC}")
            volume_btc = MAX_SINGLE_ORDER_BTC

        # USD-Wert prüfen
        try:
            ticker = self.get_ticker(use_cache=True)
            current_price = ticker["last"]
            usd_value = volume_btc * current_price

            if side == "buy" and usd_value < MIN_USD_ORDER:
                return {"status": "skipped", "reason": f"USD value {usd_value:.2f} < min {MIN_USD_ORDER}"}

            if usd_value > MAX_SINGLE_ORDER_USD:
                volume_btc = MAX_SINGLE_ORDER_USD / current_price
                print(f"[Kraken] ⚠ USD-Wert begrenzt auf {MAX_SINGLE_ORDER_USD}, "
                      f"volume angepasst auf {volume_btc:.8f} BTC")
        except Exception as e:
            print(f"[Kraken] ⚠ Ticker-Check fehlgeschlagen: {e}")
            return {"status": "error", "error": f"ticker_check_failed: {e}"}

        order_info = {
            "side": side,
            "volume_btc": round(volume_btc, 8),
            "order_type": order_type,
            "price": price,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }

        if DRY_RUN:
            order_info["status"] = "dry_run"
            print(f"[Kraken] 🔸 DRY RUN: {side.upper()} {volume_btc:.8f} BTC "
                  f"({order_type})")
            self._log_order(order_info)
            self._last_order_time = now
            return order_info

        # Echte Order
        params = {
            "pair": KRAKEN_ORDER_PAIR,
            "type": side,
            "ordertype": order_type,
            "volume": f"{volume_btc:.8f}",
        }
        if order_type == "limit" and price is not None:
            params["price"] = f"{price:.1f}"

        try:
            result = self._private("AddOrder", params)
            txids = result.get("txid", [])
            order_info["status"] = "submitted"
            order_info["kraken_txid"] = txids
            order_info["kraken_descr"] = result.get("descr", {})
            self._last_order_time = now
            print(f"[Kraken] 📤 ORDER SUBMITTED: {side.upper()} {volume_btc:.8f} BTC — "
                  f"txid: {txids}")

            # Fill-Validierung
            if validate_fill and txids and order_type == "market":
                fill_info = self._validate_order_fill(txids)
                order_info["fill_info"] = fill_info
                if fill_info.get("fully_filled"):
                    order_info["status"] = "filled"
                    print(f"[Kraken] ✅ ORDER FILLED: {fill_info.get('vol_exec', '?')} BTC "
                          f"@ avg {fill_info.get('avg_price', '?')}")
                elif fill_info.get("partially_filled"):
                    order_info["status"] = "partial_fill"
                    print(f"[Kraken] ⚠ PARTIAL FILL: {fill_info.get('vol_exec', '?')} "
                          f"von {volume_btc:.8f} BTC")
                else:
                    order_info["status"] = "submitted_unvalidated"
                    print(f"[Kraken] ⚠ Fill-Status unklar nach {ORDER_VALIDATE_TIMEOUT}s")
            elif not validate_fill:
                order_info["status"] = "executed"

        except Exception as e:
            order_info["status"] = "error"
            order_info["error"] = str(e)
            print(f"[Kraken] ❌ ORDER FEHLER: {e}")

        self._log_order(order_info)
        return order_info

    def _validate_order_fill(self, txids: list) -> dict:
        """
        Prüft ob eine Market-Order gefüllt wurde.
        Pollt bis Timeout oder bis Order geschlossen ist.
        """
        if not txids:
            return {"error": "no_txids"}

        start = time.time()
        last_status = {}

        while (time.time() - start) < ORDER_VALIDATE_TIMEOUT:
            try:
                orders = self.query_orders(txids)
                for txid in txids:
                    if txid in orders:
                        order = orders[txid]
                        status = order.get("status", "unknown")
                        vol_exec = float(order.get("vol_exec", 0))
                        vol_total = float(order.get("vol", 0))
                        cost = float(order.get("cost", 0))
                        avg_price = cost / vol_exec if vol_exec > 0 else 0

                        last_status = {
                            "txid": txid,
                            "status": status,
                            "vol_exec": vol_exec,
                            "vol_total": vol_total,
                            "avg_price": round(avg_price, 2),
                            "cost": cost,
                            "fully_filled": status == "closed" and vol_exec >= vol_total * 0.999,
                            "partially_filled": vol_exec > 0 and vol_exec < vol_total * 0.999,
                        }

                        if status in ("closed", "canceled", "expired"):
                            return last_status

            except Exception as e:
                print(f"[Kraken] ⚠ Fill-Check Fehler: {e}")

            time.sleep(ORDER_VALIDATE_INTERVAL)

        # Timeout — letzten bekannten Status zurückgeben
        if last_status:
            last_status["timeout"] = True
            return last_status
        return {"error": "timeout", "timeout": True}

    def _log_order(self, order_info: dict):
        log_file = LIVE_LOG_DIR / "order_log.csv"
        file_exists = log_file.exists()
        with log_file.open("a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow([
                    "timestamp", "status", "side", "volume_btc",
                    "order_type", "price", "kraken_txid", "error",
                    "fill_vol_exec", "fill_avg_price",
                ])
            fill_info = order_info.get("fill_info", {})
            writer.writerow([
                order_info.get("timestamp", ""),
                order_info.get("status", ""),
                order_info.get("side", ""),
                order_info.get("volume_btc", ""),
                order_info.get("order_type", ""),
                order_info.get("price", ""),
                order_info.get("kraken_txid", ""),
                order_info.get("error", ""),
                fill_info.get("vol_exec", ""),
                fill_info.get("avg_price", ""),
            ])