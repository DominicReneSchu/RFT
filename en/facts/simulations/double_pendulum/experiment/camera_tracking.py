"""
camera_tracking.py — RT-38 Smartphone video → θ₁(t), θ₂(t) CSV

Extracts angular time series of a double pendulum from a smartphone video
via colour tracking (HSV colour space) or retroreflective markers.

Output: CSV with columns t,theta1,theta2 in the format expected by
load_experimental_data() in double_pendulum.py.

Usage:
    pip install opencv-python numpy pandas
    python camera_tracking.py \\
        --video run_1_20260801.mp4 \\
        --output run_1_20260801.csv \\
        --cal-length-mm 300 \\
        --pivot-auto

© Dominic-René Schu, 2026 — Resonance Field Theory (RT-38)
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
# Default colour masks (HSV) for retroreflective markers
# ---------------------------------------------------------------------------
# Retroreflective dots appear very bright and slightly yellowish under ring
# lighting. The default masks can be overridden via --hsv1/--hsv2.
DEFAULT_HSV_LOWER1 = (15, 60, 200)   # Bright yellow/orange (retroreflective)
DEFAULT_HSV_UPPER1 = (35, 255, 255)
DEFAULT_HSV_LOWER2 = (15, 60, 200)   # Second marker: same type
DEFAULT_HSV_UPPER2 = (35, 255, 255)


def _find_largest_blob(
    mask: np.ndarray,
    min_area: int = 20,
) -> Optional[tuple[float, float]]:
    """Returns the centroid of the largest connected region in mask.

    Returns None if no blob with area >= min_area is found.
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
    """Calculates the angle (radians) of a point relative to the pivot.

    Convention: θ = 0 when pointing straight down, θ > 0 to the right.
    Normalised to (−π, π].
    """
    dx = (px - pivot[0]) / pixels_per_m
    dy = (py - pivot[1]) / pixels_per_m
    # Angle from the vertical (pointing down)
    angle = math.atan2(dx, dy)
    # Normalise to (−π, π]
    angle = (angle + math.pi) % (2 * math.pi) - math.pi
    return angle


def _detect_pivot_auto(cap: cv2.VideoCapture, n_frames: int = 30) -> tuple[float, float]:
    """Estimates the pivot point as the region with minimum motion variance.

    Reads the first n_frames and returns the pixel with minimum temporal variance —
    which is typically the suspension point.
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
        raise RuntimeError("No frames read for automatic pivot detection.")

    stack = np.stack(frames, axis=0)
    variance = np.var(stack, axis=0)
    # Minimum of variance = least-moving pixel
    min_pos = np.unravel_index(np.argmin(variance), variance.shape)
    pivot_y, pivot_x = float(min_pos[0]), float(min_pos[1])
    print(f"  Auto-pivot detected: ({pivot_x:.0f}, {pivot_y:.0f}) pixels")
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
    """Extracts θ₁(t), θ₂(t) from a smartphone video via colour tracking.

    Angles are computed relative to pivot_pixel. Joint 2 is the joint between
    arm 1 and arm 2 — its position determines θ₁. The lower end of arm 2
    (mass m₂) together with joint 2 determines θ₂.

    Marker assignment:
        Marker 1 = Joint 2 (connection arm 1 / arm 2)
        Marker 2 = Mass m₂ (lower end of arm 2)

    Args:
        video_path: Path to video file (MP4, MOV, AVI).
        output_csv: Output path for the CSV file.
        calibration_pixels_per_meter: Pixels per metre (from calibration).
        pivot_pixel: (x, y) of suspension point in pixels.
        color_marker1_lower/upper: HSV bounds for marker 1 (joint 2).
        color_marker2_lower/upper: HSV bounds for marker 2 (mass m₂).
        fps_override: Force fps (None = use video metadata).
        show_preview: Show real-time preview (OpenCV window).
        min_blob_area: Minimum area (pixels²) for blob detection.

    Returns:
        DataFrame with columns t, theta1, theta2.
    """
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise FileNotFoundError(f"Could not open video: {video_path}")

    fps = fps_override or cap.get(cv2.CAP_PROP_FPS)
    if fps <= 0:
        fps = 30.0
        print(f"  Warning: FPS not readable from video, using {fps} fps.")

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"  Video: {video_path}")
    print(f"  FPS: {fps:.1f}  |  Total frames: {total_frames}")
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
            cv2.imshow("RT-38 Pendulum Tracking (q = quit)", frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                print("  Aborted by user.")
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
    print(f"  Tracking complete: {len(df)} frames, NaN rate: {nan_rate:.1f}%")
    if nan_rate > 10:
        print("  WARNING: NaN rate > 10% — check lighting and colour masks.")

    df.to_csv(output_csv, index=False, float_format="%.6f")
    print(f"  CSV saved: {output_csv}")
    return df


def calibrate_pixels_per_meter(
    video_path: str,
    known_length_mm: float,
) -> float:
    """Interactive calibration: user clicks two points of known distance.

    Opens the first frame of the video. User clicks two points whose real
    distance is known_length_mm [mm]. Returns pixels per metre.
    """
    cap = cv2.VideoCapture(video_path)
    ret, frame = cap.read()
    cap.release()
    if not ret:
        raise RuntimeError(f"Could not read calibration frame: {video_path}")

    points: list[tuple[int, int]] = []

    def on_click(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN and len(points) < 2:
            points.append((x, y))
            cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)
            cv2.imshow("Calibration: click 2 points (known length)", frame)

    cv2.imshow("Calibration: click 2 points (known length)", frame)
    cv2.setMouseCallback("Calibration: click 2 points (known length)", on_click)

    print(f"  Calibration: click two points with known distance "
          f"{known_length_mm:.0f} mm in the image. Then press Enter.")
    while len(points) < 2:
        cv2.waitKey(50)

    cv2.destroyAllWindows()
    if len(points) < 2:
        raise RuntimeError("Fewer than 2 points selected.")

    dx = points[1][0] - points[0][0]
    dy = points[1][1] - points[0][1]
    pixel_dist = math.sqrt(dx**2 + dy**2)
    px_per_m = pixel_dist / (known_length_mm / 1000.0)
    print(f"  Calibration: {pixel_dist:.1f} pixels = {known_length_mm:.1f} mm "
          f"→ {px_per_m:.1f} px/m")
    return px_per_m


def main() -> None:
    parser = argparse.ArgumentParser(
        description="RT-38 Camera tracking: smartphone video → θ₁(t),θ₂(t) CSV"
    )
    parser.add_argument("--video", required=True, help="Path to video file")
    parser.add_argument("--output", required=True, help="Output CSV path")
    parser.add_argument("--cal-length-mm", type=float, default=None,
                        help="Known length in mm for interactive calibration")
    parser.add_argument("--px-per-m", type=float, default=None,
                        help="Pixels per metre (instead of interactive calibration)")
    parser.add_argument("--pivot-x", type=float, default=None,
                        help="Pivot pixel X (manual)")
    parser.add_argument("--pivot-y", type=float, default=None,
                        help="Pivot pixel Y (manual)")
    parser.add_argument("--pivot-auto", action="store_true",
                        help="Detect pivot automatically from motion minimum")
    parser.add_argument("--fps", type=float, default=None,
                        help="Force fps (overrides video metadata)")
    parser.add_argument("--no-preview", action="store_true",
                        help="No real-time preview")
    parser.add_argument("--min-area", type=int, default=20,
                        help="Minimum area for blob detection (pixels²)")
    args = parser.parse_args()

    # Calibration
    if args.px_per_m is not None:
        px_per_m = args.px_per_m
    elif args.cal_length_mm is not None:
        px_per_m = calibrate_pixels_per_meter(args.video, args.cal_length_mm)
    else:
        print("ERROR: --cal-length-mm or --px-per-m required.")
        sys.exit(1)

    # Pivot
    if args.pivot_auto:
        cap = cv2.VideoCapture(args.video)
        pivot = _detect_pivot_auto(cap)
        cap.release()
    elif args.pivot_x is not None and args.pivot_y is not None:
        pivot = (args.pivot_x, args.pivot_y)
    else:
        print("ERROR: --pivot-auto or --pivot-x + --pivot-y required.")
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
