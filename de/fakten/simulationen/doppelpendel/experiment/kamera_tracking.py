"""
kamera_tracking.py — RT-38 Smartphone-Video → θ₁(t), θ₂(t) CSV

Extrahiert Winkelzeitreihen eines Doppelpendels aus einem Smartphone-Video
via Farb-Tracking (HSV-Farbraum) oder retroreflektierender Punkte.

Ausgabe: CSV mit Spalten t,theta1,theta2 im Format, das load_experimental_data()
in doppelpendel.py erwartet.

Verwendung:
    pip install opencv-python numpy pandas
    python kamera_tracking.py \\
        --video run_1_20260801.mp4 \\
        --output run_1_20260801.csv \\
        --cal-length-mm 300 \\
        --pivot-auto

© Dominic-René Schu, 2026 — Resonanzfeldtheorie (RT-38)
"""

from __future__ import annotations

import argparse
import math
import sys
from pathlib import Path
from typing import Optional

import cv2
import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------
# Standard-Farbmasken (HSV) für retroreflektierende Punkte
# ---------------------------------------------------------------------------
# Retroreflektierende Punkte erscheinen unter Ringbeleuchtung sehr hell
# und leicht gelblich. Die Standardmasken können über --hsv1/--hsv2 überschrieben
# werden.
DEFAULT_HSV_LOWER1 = (15, 60, 200)   # Helles Gelb/Orange (retroreflektierend)
DEFAULT_HSV_UPPER1 = (35, 255, 255)
DEFAULT_HSV_LOWER2 = (15, 60, 200)   # Zweiter Marker: gleicher Typ
DEFAULT_HSV_UPPER2 = (35, 255, 255)


def _find_largest_blob(
    mask: np.ndarray,
    min_area: int = 20,
) -> Optional[tuple[float, float]]:
    """Gibt den Schwerpunkt des größten zusammenhängenden Bereichs in mask zurück.

    Gibt None zurück wenn kein Blob mit Fläche >= min_area gefunden wird.
    """
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if not contours:
        return None
    largest = max(contours, key=cv2.contourArea)
    area = cv2.contourArea(largest)
    if area < min_area:
        return None
    m = cv2.moments(largest)
    if m["m00"] == 0:
        return None
    cx = m["m10"] / m["m00"]
    cy = m["m01"] / m["m00"]
    return cx, cy


def _pixel_to_angle(
    px: float,
    py: float,
    pivot: tuple[float, float],
    pixels_per_m: float,
) -> float:
    """Berechnet den Winkel (Rad) eines Punktes relativ zum Pivot.

    Konvention: θ = 0 bei senkrecht nach unten, θ > 0 nach rechts.
    Normiert auf (−π, π].
    """
    dx = (px - pivot[0]) / pixels_per_m
    dy = (py - pivot[1]) / pixels_per_m
    # Winkel von der Senkrechten nach unten
    angle = math.atan2(dx, dy)
    # Normierung auf (−π, π]
    angle = (angle + math.pi) % (2 * math.pi) - math.pi
    return angle


def _detect_pivot_auto(cap: cv2.VideoCapture, n_frames: int = 30) -> tuple[float, float]:
    """Schätzt den Pivot-Punkt als den Bereich mit geringstem Bewegungsdurchschnitt.

    Liest die ersten n_frames Bilder und gibt den Pixel zurück, dessen
    Zeitvarianz minimal ist — das ist typischerweise der Aufhängungspunkt.
    """
    frames = []
    for _ in range(n_frames):
        ret, frame = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY).astype(float)
        frames.append(gray)
    cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    if not frames:
        raise RuntimeError("Keine Frames gelesen für automatische Pivot-Erkennung.")

    stack = np.stack(frames, axis=0)
    variance = np.var(stack, axis=0)
    # Minimum der Varianz = geringstes Bewegungspixel
    min_pos = np.unravel_index(np.argmin(variance), variance.shape)
    pivot_y, pivot_x = float(min_pos[0]), float(min_pos[1])
    print(f"  Auto-Pivot erkannt: ({pivot_x:.0f}, {pivot_y:.0f}) Pixel")
    return pivot_x, pivot_y


def track_pendulum(
    video_path: str,
    output_csv: str,
    calibration_pixels_per_meter: float,
    pivot_pixel: tuple[float, float],
    color_marker1_lower: tuple = DEFAULT_HSV_LOWER1,
    color_marker1_upper: tuple = DEFAULT_HSV_UPPER1,
    color_marker2_lower: tuple = DEFAULT_HSV_LOWER2,
    color_marker2_upper: tuple = DEFAULT_HSV_UPPER2,
    fps_override: Optional[float] = None,
    show_preview: bool = True,
    min_blob_area: int = 20,
) -> pd.DataFrame:
    """Extrahiert θ₁(t), θ₂(t) aus einem Smartphone-Video via Farb-Tracking.

    Die Winkel werden relativ zu pivot_pixel berechnet. Gelenk 2 ist das
    Gelenk zwischen Arm 1 und Arm 2 — dessen Position bestimmt θ₁.
    Das untere Ende von Arm 2 (Masse m₂) bestimmt zusammen mit Gelenk 2 den θ₂.

    Marker-Zuordnung:
        Marker 1 = Gelenk 2 (Verbindung Arm 1 / Arm 2)
        Marker 2 = Masse m₂ (unteres Ende von Arm 2)

    Args:
        video_path: Pfad zur Videodatei (MP4, MOV, AVI).
        output_csv: Ausgabepfad für die CSV-Datei.
        calibration_pixels_per_meter: Pixel pro Meter (aus Kalibrierung).
        pivot_pixel: (x, y) des Aufhängungspunkts in Pixeln.
        color_marker1_lower/upper: HSV-Grenzen für Marker 1 (Gelenk 2).
        color_marker2_lower/upper: HSV-Grenzen für Marker 2 (Masse m₂).
        fps_override: FPS erzwingen (None = aus Video-Metadaten).
        show_preview: Echtzeit-Vorschau anzeigen (OpenCV-Fenster).
        min_blob_area: Mindestfläche (Pixel²) für Blob-Erkennung.

    Returns:
        DataFrame mit Spalten t, theta1, theta2.
    """
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise FileNotFoundError(f"Video konnte nicht geöffnet werden: {video_path}")

    fps = fps_override or cap.get(cv2.CAP_PROP_FPS)
    if fps <= 0:
        fps = 30.0
        print(f"  Warnung: FPS nicht aus Video lesbar, verwende {fps} fps.")

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"  Video: {video_path}")
    print(f"  FPS: {fps:.1f}  |  Frames total: {total_frames}")
    print(f"  Pivot: {pivot_pixel}  |  px/m: {calibration_pixels_per_meter:.1f}")

    lower1 = np.array(color_marker1_lower, dtype=np.uint8)
    upper1 = np.array(color_marker1_upper, dtype=np.uint8)
    lower2 = np.array(color_marker2_lower, dtype=np.uint8)
    upper2 = np.array(color_marker2_upper, dtype=np.uint8)

    records: list[dict] = []
    frame_idx = 0
    nan_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        t = frame_idx / fps
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        mask1 = cv2.inRange(hsv, lower1, upper1)
        mask2 = cv2.inRange(hsv, lower2, upper2)

        pos1 = _find_largest_blob(mask1, min_blob_area)
        pos2 = _find_largest_blob(mask2, min_blob_area)

        if pos1 is not None and pos2 is not None:
            theta1 = _pixel_to_angle(pos1[0], pos1[1], pivot_pixel,
                                     calibration_pixels_per_meter)
            theta2 = _pixel_to_angle(pos2[0], pos2[1],
                                     (pos1[0], pos1[1]),
                                     calibration_pixels_per_meter)
            records.append({"t": t, "theta1": theta1, "theta2": theta2})

            if show_preview:
                cv2.circle(frame, (int(pos1[0]), int(pos1[1])), 8, (0, 255, 0), 2)
                cv2.circle(frame, (int(pos2[0]), int(pos2[1])), 8, (0, 0, 255), 2)
                cv2.circle(frame, (int(pivot_pixel[0]), int(pivot_pixel[1])), 6,
                           (255, 255, 0), 2)
                cv2.line(frame,
                         (int(pivot_pixel[0]), int(pivot_pixel[1])),
                         (int(pos1[0]), int(pos1[1])), (0, 255, 0), 1)
                cv2.line(frame,
                         (int(pos1[0]), int(pos1[1])),
                         (int(pos2[0]), int(pos2[1])), (0, 0, 255), 1)
                info = (f"t={t:.2f}s  th1={math.degrees(theta1):.1f}deg"
                        f"  th2={math.degrees(theta2):.1f}deg")
                cv2.putText(frame, info, (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                            0.6, (255, 255, 255), 2)
        else:
            nan_count += 1
            records.append({"t": t, "theta1": float("nan"), "theta2": float("nan")})

        if show_preview:
            cv2.imshow("RT-38 Pendel-Tracking (q = beenden)", frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                print("  Abbruch durch Benutzer.")
                break

        frame_idx += 1
        if frame_idx % 300 == 0:
            print(f"  Frame {frame_idx}/{total_frames} ({100*frame_idx/max(total_frames,1):.0f}%)"
                  f"  NaN: {nan_count}")

    cap.release()
    if show_preview:
        cv2.destroyAllWindows()

    df = pd.DataFrame(records)
    nan_rate = nan_count / max(len(records), 1) * 100
    print(f"  Tracking abgeschlossen: {len(df)} Frames, NaN-Rate: {nan_rate:.1f}%")
    if nan_rate > 10:
        print("  WARNUNG: NaN-Rate > 10% — Beleuchtung und Farb-Masken prüfen.")

    df.to_csv(output_csv, index=False, float_format="%.6f")
    print(f"  CSV gespeichert: {output_csv}")
    return df


def calibrate_pixels_per_meter(
    video_path: str,
    known_length_mm: float,
) -> float:
    """Interaktive Kalibrierung: Benutzer klickt zwei Punkte bekannter Länge.

    Öffnet das erste Frame des Videos. Benutzer klickt zwei Punkte,
    deren realer Abstand known_length_mm [mm] beträgt.
    Gibt Pixel pro Meter zurück.
    """
    cap = cv2.VideoCapture(video_path)
    ret, frame = cap.read()
    cap.release()
    if not ret:
        raise RuntimeError(f"Kalibrierungsbild konnte nicht gelesen werden: {video_path}")

    points: list[tuple[int, int]] = []

    def on_click(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN and len(points) < 2:
            points.append((x, y))
            cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)
            cv2.imshow("Kalibrierung: 2 Punkte anklicken (bekannte Laenge)", frame)

    cv2.imshow("Kalibrierung: 2 Punkte anklicken (bekannte Laenge)", frame)
    cv2.setMouseCallback("Kalibrierung: 2 Punkte anklicken (bekannte Laenge)", on_click)

    print(f"  Kalibrierung: Klicke zwei Punkte mit bekanntem Abstand "
          f"{known_length_mm:.0f} mm im Bild. Dann Enter drücken.")
    while len(points) < 2:
        cv2.waitKey(50)

    cv2.destroyAllWindows()
    if len(points) < 2:
        raise RuntimeError("Weniger als 2 Punkte ausgewählt.")

    dx = points[1][0] - points[0][0]
    dy = points[1][1] - points[0][1]
    pixel_dist = math.sqrt(dx**2 + dy**2)
    px_per_m = pixel_dist / (known_length_mm / 1000.0)
    print(f"  Kalibrierung: {pixel_dist:.1f} Pixel = {known_length_mm:.1f} mm "
          f"→ {px_per_m:.1f} px/m")
    return px_per_m


def main() -> None:
    parser = argparse.ArgumentParser(
        description="RT-38 Kamera-Tracking: Smartphone-Video → θ₁(t),θ₂(t) CSV"
    )
    parser.add_argument("--video", required=True, help="Pfad zur Videodatei")
    parser.add_argument("--output", required=True, help="Ausgabe-CSV-Pfad")
    parser.add_argument("--cal-length-mm", type=float, default=None,
                        help="Bekannte Länge in mm für interaktive Kalibrierung")
    parser.add_argument("--px-per-m", type=float, default=None,
                        help="Pixel pro Meter (statt interaktiver Kalibrierung)")
    parser.add_argument("--pivot-x", type=float, default=None,
                        help="Pivot-Pixel X (manuell)")
    parser.add_argument("--pivot-y", type=float, default=None,
                        help="Pivot-Pixel Y (manuell)")
    parser.add_argument("--pivot-auto", action="store_true",
                        help="Pivot automatisch aus Bewegungsminimum bestimmen")
    parser.add_argument("--fps", type=float, default=None,
                        help="FPS erzwingen (überschreibt Video-Metadaten)")
    parser.add_argument("--no-preview", action="store_true",
                        help="Keine Echtzeit-Vorschau")
    parser.add_argument("--min-area", type=int, default=20,
                        help="Mindestfläche für Blob-Erkennung (Pixel²)")
    args = parser.parse_args()

    # Kalibrierung
    if args.px_per_m is not None:
        px_per_m = args.px_per_m
    elif args.cal_length_mm is not None:
        px_per_m = calibrate_pixels_per_meter(args.video, args.cal_length_mm)
    else:
        print("FEHLER: --cal-length-mm oder --px-per-m erforderlich.")
        sys.exit(1)

    # Pivot
    if args.pivot_auto:
        cap = cv2.VideoCapture(args.video)
        pivot = _detect_pivot_auto(cap)
        cap.release()
    elif args.pivot_x is not None and args.pivot_y is not None:
        pivot = (args.pivot_x, args.pivot_y)
    else:
        print("FEHLER: --pivot-auto oder --pivot-x + --pivot-y erforderlich.")
        sys.exit(1)

    track_pendulum(
        video_path=args.video,
        output_csv=args.output,
        calibration_pixels_per_meter=px_per_m,
        pivot_pixel=pivot,
        fps_override=args.fps,
        show_preview=not args.no_preview,
        min_blob_area=args.min_area,
    )


if __name__ == "__main__":
    main()
