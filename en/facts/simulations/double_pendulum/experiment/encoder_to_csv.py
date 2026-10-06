"""
encoder_to_csv.py — RT-38 Serial encoder readout → CSV

Reads t,theta1,theta2 from the Arduino (encoder_readout.ino) via serial
interface and saves an RT-08-compatible CSV file.

Usage:
    pip install pyserial pandas
    python encoder_to_csv.py --port /dev/ttyUSB0 --duration 120 --output run_1_20260801.csv

Windows:  --port COM3 (or COM4, COM5, ...)
macOS:    --port /dev/cu.usbmodem...

© Dominic-René Schu, 2026 — Resonance Field Theory (RT-38)
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
    """Lists all available serial ports."""
    ports = list(serial.tools.list_ports.comports())
    if not ports:
        print("No serial ports found.")
        return
    print("Available serial ports:")
    for p in ports:
        print(f"  {p.device:20s}  {p.description}")


def read_encoder(
    port: str,
    baud: int,
    duration_s: float,
    output_csv: str,
    skip_comments: bool = True,
) -> pd.DataFrame:
    """Reads encoder data from the Arduino and saves it as a CSV file.

    Args:
        port: Serial port (e.g. '/dev/ttyUSB0' or 'COM3').
        baud: Baud rate (default: 115200).
        duration_s: Measurement duration in seconds.
        output_csv: Output path for the CSV file.
        skip_comments: Skip lines starting with '#'.

    Returns:
        DataFrame with columns t, theta1, theta2.
    """
    print(f"  Opening serial port: {port} @ {baud} baud")
    try:
        ser = serial.Serial(port, baudrate=baud, timeout=2.0)
    except serial.SerialException as e:
        print(f"ERROR: Could not open serial port: {e}")
        print("Available ports:")
        list_serial_ports()
        sys.exit(1)

    # Arduino resets after USB connection — wait briefly
    time.sleep(2.0)
    ser.reset_input_buffer()

    records: list[dict] = []
    start_wall = time.monotonic()
    header_seen = False
    line_count = 0
    error_count = 0

    print(f"  Measurement running for {duration_s:.0f} seconds... (Ctrl+C to abort)")

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

            # Skip comment lines
            if line.startswith("#"):
                print(f"  Arduino: {line}")
                continue

            # Skip CSV header
            if line.startswith("t,"):
                if not header_seen:
                    header_seen = True
                continue

            # Parse data values
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
                print(f"  {elapsed:.0f}/{duration_s:.0f}s  —  {line_count} points"
                      f"  ({error_count} errors)")

    except KeyboardInterrupt:
        print("\n  Aborted by user.")
    finally:
        ser.close()

    if not records:
        print("ERROR: No data received. Check port and baud rate.")
        sys.exit(1)

    df = pd.DataFrame(records)
    df.to_csv(output_csv, index=False, float_format="%.6f")

    print(f"\n  Measurement complete:")
    print(f"  Data points: {len(df)}")
    print(f"  Duration:    {df['t'].iloc[-1] - df['t'].iloc[0]:.2f} s")
    print(f"  Errors:      {error_count}")
    print(f"  CSV:         {output_csv}")
    return df


def main() -> None:
    parser = argparse.ArgumentParser(
        description="RT-38 Encoder readout: Arduino → θ₁(t),θ₂(t) CSV"
    )
    parser.add_argument("--port", default=None,
                        help="Serial port (e.g. /dev/ttyUSB0 or COM3)")
    parser.add_argument("--baud", type=int, default=115200,
                        help="Baud rate (default: 115200)")
    parser.add_argument("--duration", type=float, default=120.0,
                        help="Measurement duration in seconds (default: 120)")
    parser.add_argument("--output", required=True,
                        help="Output CSV path")
    parser.add_argument("--list-ports", action="store_true",
                        help="List available serial ports and exit")
    args = parser.parse_args()

    if args.list_ports:
        list_serial_ports()
        return

    if args.port is None:
        print("ERROR: --port required (e.g. --port /dev/ttyUSB0 or --port COM3)")
        print("Tip: --list-ports shows available ports.")
        sys.exit(1)

    read_encoder(
        port=args.port,
        baud=args.baud,
        duration_s=args.duration,
        output_csv=args.output,
    )


if __name__ == "__main__":
    main()
