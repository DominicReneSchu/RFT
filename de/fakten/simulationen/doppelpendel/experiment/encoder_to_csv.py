"""
encoder_to_csv.py — RT-38 Serielle Encoder-Auslese → CSV

Liest t,theta1,theta2 vom Arduino (encoder_auslese.ino) über serielle
Schnittstelle und speichert eine RT-08-kompatible CSV-Datei.

Verwendung:
    pip install pyserial pandas
    python encoder_to_csv.py --port /dev/ttyUSB0 --duration 120 --output run_1_20260801.csv

Unter Windows: --port COM3 (oder COM4, COM5, ...)
Unter macOS:   --port /dev/cu.usbmodem...

© Dominic-René Schu, 2026 — Resonanzfeldtheorie (RT-38)
"""

from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

import pandas as pd
import serial
import serial.tools.list_ports


def list_serial_ports() -> None:
    """Zeigt alle verfügbaren seriellen Ports."""
    ports = list(serial.tools.list_ports.comports())
    if not ports:
        print("Keine seriellen Ports gefunden.")
        return
    print("Verfügbare serielle Ports:")
    for p in ports:
        print(f"  {p.device:20s}  {p.description}")


def read_encoder(
    port: str,
    baud: int,
    duration_s: float,
    output_csv: str,
    skip_comments: bool = True,
) -> pd.DataFrame:
    """Liest Encoder-Daten vom Arduino und speichert sie als CSV.

    Args:
        port: Serieller Port (z.B. '/dev/ttyUSB0' oder 'COM3').
        baud: Baudrate (Standard: 115200).
        duration_s: Messdauer in Sekunden.
        output_csv: Ausgabepfad für die CSV-Datei.
        skip_comments: Zeilen beginnend mit '#' überspringen.

    Returns:
        DataFrame mit Spalten t, theta1, theta2.
    """
    print(f"  Öffne seriellen Port: {port} @ {baud} Baud")
    try:
        ser = serial.Serial(port, baudrate=baud, timeout=2.0)
    except serial.SerialException as e:
        print(f"FEHLER: Seriellen Port konnte nicht geöffnet werden: {e}")
        print("Verfügbare Ports:")
        list_serial_ports()
        sys.exit(1)

    # Arduino startet nach USB-Verbindung neu — kurz warten
    time.sleep(2.0)
    ser.reset_input_buffer()

    records: list[dict] = []
    start_wall = time.monotonic()
    header_seen = False
    line_count = 0
    error_count = 0

    print(f"  Messung läuft für {duration_s:.0f} Sekunden... (Strg+C zum Abbrechen)")

    try:
        while True:
            elapsed = time.monotonic() - start_wall
            if elapsed >= duration_s:
                break

            raw_line = ser.readline()
            if not raw_line:
                continue

            try:
                line = raw_line.decode("ascii", errors="replace").strip()
            except Exception:
                continue

            # Kommentarzeilen überspringen
            if line.startswith("#"):
                print(f"  Arduino: {line}")
                continue

            # CSV-Header überspringen
            if line.startswith("t,"):
                if not header_seen:
                    header_seen = True
                continue

            # Datenwerte parsen
            parts = line.split(",")
            if len(parts) != 3:
                error_count += 1
                continue

            try:
                t      = float(parts[0])
                theta1 = float(parts[1])
                theta2 = float(parts[2])
            except ValueError:
                error_count += 1
                continue

            records.append({"t": t, "theta1": theta1, "theta2": theta2})
            line_count += 1

            if line_count % 500 == 0:
                print(f"  {elapsed:.0f}/{duration_s:.0f}s  —  {line_count} Punkte"
                      f"  ({error_count} Fehler)")

    except KeyboardInterrupt:
        print("\n  Abbruch durch Benutzer.")
    finally:
        ser.close()

    if not records:
        print("FEHLER: Keine Daten empfangen. Port und Baudrate prüfen.")
        sys.exit(1)

    df = pd.DataFrame(records)
    df.to_csv(output_csv, index=False, float_format="%.6f")

    print(f"\n  Messung abgeschlossen:")
    print(f"  Datenpunkte: {len(df)}")
    print(f"  Dauer:       {df['t'].iloc[-1] - df['t'].iloc[0]:.2f} s")
    print(f"  Fehler:      {error_count}")
    print(f"  CSV:         {output_csv}")
    return df


def main() -> None:
    parser = argparse.ArgumentParser(
        description="RT-38 Encoder-Auslese: Arduino → θ₁(t),θ₂(t) CSV"
    )
    parser.add_argument("--port", default=None,
                        help="Serieller Port (z.B. /dev/ttyUSB0 oder COM3)")
    parser.add_argument("--baud", type=int, default=115200,
                        help="Baudrate (Standard: 115200)")
    parser.add_argument("--duration", type=float, default=120.0,
                        help="Messdauer in Sekunden (Standard: 120)")
    parser.add_argument("--output", required=True,
                        help="Ausgabe-CSV-Pfad")
    parser.add_argument("--list-ports", action="store_true",
                        help="Verfügbare serielle Ports anzeigen und beenden")
    args = parser.parse_args()

    if args.list_ports:
        list_serial_ports()
        return

    if args.port is None:
        print("FEHLER: --port erforderlich (z.B. --port /dev/ttyUSB0 oder --port COM3)")
        print("Tipp: --list-ports zeigt verfügbare Ports.")
        sys.exit(1)

    read_encoder(
        port=args.port,
        baud=args.baud,
        duration_s=args.duration,
        output_csv=args.output,
    )


if __name__ == "__main__":
    main()
