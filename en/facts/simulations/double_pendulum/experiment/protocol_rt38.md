# RT-38 — Public Experiment Protocol: Tabletop Falsification Test ε(Δφ) = cos²(Δφ/2)

**Status:** ✅ Protocol complete (Aug 2026) — execution external  
**Axiom:** A4 — Coupling efficiency ε(Δφ) = cos²(Δφ/2)  
**Budget:** ~€100–300, a smartphone is sufficient  
**Analysis software:** already available (RT-08), see §5

> **Invitation to replicate:** This protocol is explicitly framed as an open invitation.
> Anyone who performs this test and shares data contributes to the empirical basis of RFT.
> Upload data: Zenodo or GitHub Issues (https://github.com/DominicReneSchu/RFT/issues)

---

## §1 — Scientific Question

### What is being tested?

Axiom A4 of Resonance Field Theory (RFT) postulates that the coupling efficiency
between two pendulums depends on their phase difference Δφ = θ₂ − θ₁:

$$
\varepsilon(\Delta\varphi) = \cos^2\!\left(\frac{\Delta\varphi}{2}\right)
$$

This formula is group-theoretically unique: it follows from the k=1 representation
of U(1) ⊂ G_sync and is not freely chosen. The experiment tests whether this specific
phase dependence is detectable in real measurement data.

### Hypotheses

**H₀ (Null hypothesis — Lagrangian):**
The coupling efficiency in the double pendulum follows no specific phase dependence
beyond classical Lagrangian mechanics. The RFT additional term has amplitude A = 0.
ε_exp(Δθ) is fully described by pure Lagrangian mechanics.

**H₁ (RFT hypothesis):**
ε_exp(Δθ) = cos²(Δθ/2) — the k=1 representation of U(1) ⊂ G_sync describes the
phase dependence of energy transfer measurably better than H₀. The coupling amplitude
A > 0 is statistically significant.

### Falsification criterion (from RT-08)

| χ²_red | Assessment |
|--------|-----------|
| ≤ 1.5 | ✅ H₁ not falsified — ε(Δφ) = cos²(Δφ/2) describes data |
| 1.5 < χ²_red ≤ 2.0 | ⚠️ Borderline — check systematic errors |
| > 2.0 | ❌ H₁ rejected at 5% level |

### Peer-review critical point

**Question:** "Is ε = cos²(Δφ/2) not already contained in Lagrangian mechanics?"

**Answer (clear):** No. The Lagrangian mechanics of the double pendulum contains, as
natural coupling, terms of the form sin(Δφ) and cos(Δφ) from the shared pivot —
but no term with the specific form cos²(Δφ/2). The RFT term

$$
\tau_{\text{RFT}} = A \cdot \cos^2\!\left(\frac{\Delta\varphi}{2}\right) \cdot \sin(\Delta\varphi)
$$

is *additional* to the natural Lagrangian coupling. H₁ tests whether A > 0 is significant
and whether the phase dependence has exactly the form cos²(Δφ/2) — and not e.g.
cos²(Δφ) or a constant coupling.

### Limitation from RT-08

The previous χ² test (χ²_red = 2.42, RT-08, Aug 2026) was performed on **synthetic** data
from a pure Lagrangian simulation (A = 0). This result documents the expected deviation
between the RFT formula and the purely classical null hypothesis — but is not a substitute
for real measurement data. RT-38 provides the protocol to remedy this shortcoming.

---

## §2 — Mechanical Setup

### Bill of materials

| Component | Specification | Example source | Approx. cost |
|---|---|---|---|
| Pendulum arm 1 | Aluminium rod 300 mm × 10 mm × 5 mm | Hardware store / Amazon | €3 |
| Pendulum arm 2 | Aluminium rod 250 mm × 10 mm × 5 mm | Hardware store / Amazon | €3 |
| Joint 1 (axle) | Ball bearing 608ZZ (8 mm inner Ø, 22 mm outer Ø) | Amazon / Conrad | €2 |
| Joint 2 (axle) | Ball bearing 608ZZ (identical) | Amazon / Conrad | €2 |
| Axles | Threaded rod M8 × 30 mm (×2) | Hardware store | €1 |
| Mass m₁ | Steel nut M8 or washer, defined mass ±0.1 g | Hardware store | €1 |
| Mass m₂ | Steel nut M8 or washer, defined mass ±0.1 g | Hardware store | €1 |
| Frame | Steel angle bracket 40×40×3 mm, ca. 200 mm length | Hardware store | €5 |
| Wall mounting | Fischer wall plugs + screws (×4) | Hardware store | €3 |
| Mounting plate | Aluminium plate 100×100×5 mm as pivot platform | Hardware store | €5 |
| Markers (Variant A) | Retroreflective adhesive dots Ø 10 mm (pack of 100) | Office supply / Amazon | €5 |
| Magnet (Variant B) | Neodymium disc magnet Ø 6 mm × 2.5 mm (×2, for AS5600) | Amazon | €3 |
| Encoder (Variant B) | AS5600 magnetic 12-bit I²C encoder (×2 breakout boards) | Amazon / AliExpress | €10 |
| Microcontroller (Var. B) | Arduino Nano or Raspberry Pi Pico | Amazon | €10 |
| Smartphone tripod | Mini tabletop tripod with ball head | Amazon | €10 |
| **Total budget Var. A** | | | **~€50–80** |
| **Total budget Var. B** | | | **~€100–150** |

*All prices approximate, as of 2026. With Variant A and an existing smartphone you can get started under €100.*

### Geometric requirements

- **L₁, L₂:** Length of pendulum arms from pivot to centre of mass, measured to ±1 mm
  and documented in the system parameter template
- **m₁, m₂:** Masses (arm + attached mass) weighed to ±0.5 g and documented
- **Joints:** Clean ball bearings (degreaser), mount without play
  — Test criterion: pendulum arm swings freely > 30 s without measurable damping
- **Mounting:** Wall-mounted on solid masonry or steel beam
  — Test criterion: frame eigenfrequency > 10 × pendulum fundamental frequency
  (pendulum frequency ≈ (1/2π)·√(g/L₁) ≈ 0.9 Hz at L₁ = 300 mm → frame > 9 Hz)

### Assembly sequence

1. Mount frame on wall; verify horizontal with spirit level
2. Mount pendulum arm 1 with ball bearing 608ZZ on frame — verify freedom from play
3. Mount pendulum arm 2 with ball bearing 608ZZ at the end of arm 1
4. Attach masses at respective lower ends (nut + locking nut)
5. Measure L₁ (pivot → joint 2) and L₂ (joint 2 → centre of mass m₂)
6. Weigh m₁ (arm 1 + mass) and m₂ (arm 2 + mass) on a letter scale
7. Attach markers for Variant A: one retroreflective dot each on joint 1 (pivot),
   joint 2 (connection), and mass m₂

---

## §3 — Measurement chain: Two complete variants

### Variant A — Smartphone camera (minimal effort)

**Hardware:**
- Smartphone from 2020 or later with at least 60 fps (120 fps recommended)
  Examples: iPhone 13+, Samsung Galaxy S21+, Google Pixel 6+
- Mini tripod, camera frontal and orthogonal to the plane of oscillation
- Distance camera–pendulum: at least 1 m (reduces perspective distortion)
- Lighting: bright even backlight or ring light in front of camera
  (retroreflective markers + ring light give best contrast)

**Recording:**
- Video format: 1080p or 4K, at least 60 fps
- Export format: MP4 or MOV
- Before measurement: calibration recording with a ruler or known distance in frame

**Software:** `camera_tracking.py` (in this directory)
```bash
pip install opencv-python numpy pandas
python camera_tracking.py \
    --video run_1_20260801.mp4 \
    --output run_1_20260801.csv \
    --cal-length-mm 300 \
    --pivot-auto
```

**Output:** CSV with columns `t,theta1,theta2` (angles in radians), normalised to (−π, π]

**Accuracy:** ±0.01–0.03 rad with good lighting and correct calibration

**Calibration:**
1. Let pendulum arms hang vertically at rest → record a short calibration clip
2. In `camera_tracking.py`: specify known length in frame (e.g. L₁ = 300 mm) as scale
3. Pivot point = suspension point of arm 1 (retroreflective dot or set manually)
4. Sign convention: θ > 0 = deflected to the right (default in tracking script)
5. Check calibration plot `cal_check.png`: θ_measured vs. θ_known must have slope 1.0 ± 0.05

### Variant B — Rotary encoder (higher precision)

**Hardware:**
- 2× AS5600 magnetic 12-bit I²C encoder (breakout board)
- 2× neodymium disc magnet Ø 6 mm × 2.5 mm, glued onto axis of respective ball bearing
- Arduino Nano or Raspberry Pi Pico (I²C, 3.3 V or 5 V depending on board)
- USB cable for serial data transfer to PC/laptop

**Sampling rate:** 100–500 Hz (configurable in Arduino sketch)

**Software:** `encoder_readout.ino` (Arduino) + `encoder_to_csv.py` (Python)
```bash
# Flash Arduino sketch
arduino-cli compile --fqbn arduino:avr:nano encoder_readout.ino
arduino-cli upload  --fqbn arduino:avr:nano -p /dev/ttyUSB0 encoder_readout.ino

# Start serial readout
pip install pyserial pandas
python encoder_to_csv.py --port /dev/ttyUSB0 --duration 120 --output run_1_20260801.csv
```

**Output:** CSV with columns `t,theta1,theta2` (angles in radians, already calibrated)

**Accuracy:** ±0.001 rad (12-bit at 2π → 4096 steps → ≈0.0015 rad resolution)

**Calibration:**
1. Both pendulum arms hanging vertically: AS5600 reads 0° → set `ZERO_OFFSET` in sketch
2. Deflect arm manually to +90° (π/2), check encoder value: must read π/2 ± 0.01 rad
3. Sign convention: clockwise = positive (configurable via `SIGN_THETA1` in sketch)
4. I²C address: AS5600 has fixed address 0x36 — with two encoders use an I²C multiplexer
   (TCA9548A, ~€3) or two separate I²C buses

---

## §4 — Measurement protocol

### Step by step

**Before each measurement series:**
1. Let pendulum come to rest (leave hanging freely for 30 s)
2. Perform calibration (set zero position, verify scaling)
3. Enter system parameters in `system_params.json` (L₁, L₂, m₁, m₂, g_local)

**Per run:**
1. **Set initial condition:** Bring pendulum arms to starting angles θ₁(0), θ₂(0)
   (use a protractor or printed angle template)
2. **Document initial condition:** Note θ₁(0), θ₂(0) to ±0.01 rad
   — release both arms briefly → ω₁(0) = ω₂(0) ≈ 0 (or asymmetric for Run 5)
3. **Start measurement:** Begin recording/encoder, then release pendulum
4. **Minimum duration:** 120 seconds continuously
   (~7200 data points at 60 fps or ~12000 at 100 Hz encoder)
5. **End measurement:** Stop recording, immediately name and save file

### Required runs (5 independent runs)

| Run | θ₁(0) | θ₂(0) | ω₁(0) | ω₂(0) | Description |
|-----|--------|--------|--------|--------|-------------|
| 1 | π/4 (45°) | π/4 (45°) | 0 | 0 | Same phase — maximum RFT coupling expected |
| 2 | π/2 (90°) | 0 (0°) | 0 | 0 | Different phase — medium coupling |
| 3 | π/3 (60°) | 2π/3 (120°) | 0 | 0 | Asymmetric deflection |
| 4 | π/6 (30°) | 5π/6 (150°) | 0 | 0 | Near anti-phase — minimum RFT coupling expected |
| 5 | π/2 (90°) | π/2 (90°) | 0.5 rad/s | 0 | Asymmetric initial velocity |

*Runs 1 and 4 are the informative extreme cases (maximum vs. minimum expected coupling)
and should be performed first.*

### File format and naming

```
experiment/data/
├── run_1_YYYYMMDD.csv      # e.g. run_1_20260801.csv
├── run_2_YYYYMMDD.csv
├── run_3_YYYYMMDD.csv
├── run_4_YYYYMMDD.csv
├── run_5_YYYYMMDD.csv
└── system_params.json
```

CSV header (exact, no deviation):
```
t,theta1,theta2
0.000,0.785,0.785
0.017,0.784,0.786
...
```

- `t`: Time in seconds (float, decimal point)
- `theta1`: Angle of pendulum arm 1 in radians, normalised to (−π, π]
- `theta2`: Angle of pendulum arm 2 in radians, normalised to (−π, π]

`system_params.json` (fill in completely):
```json
{
  "L1_m": 0.300,
  "L2_m": 0.250,
  "m1_kg": 0.150,
  "m2_kg": 0.120,
  "g_ms2": 9.812,
  "measurement_date": "2026-08-01",
  "location": "Berlin, Germany",
  "hardware": "iPhone 14 Pro, 120 fps",
  "fps_or_samplerate_hz": 120,
  "notes": "608ZZ ball bearings, retroreflective markers"
}
```

*g_local: location-specific value (Berlin: 9.8128, Munich: 9.8072, Vienna: 9.8086)*

---

## §5 — Analysis

### Step by step

```bash
# 1. Clone repository
git clone https://github.com/DominicReneSchu/RFT.git
cd RFT

# 2. Install dependencies
pip install numpy matplotlib scipy pandas

# 3. Run analysis script (single run)
python en/facts/simulations/double_pendulum/analyse/rt08_double_pendulum_comparison.py \
    --data en/facts/simulations/double_pendulum/experiment/data/run_1_20260801.csv \
    --params en/facts/simulations/double_pendulum/experiment/data/system_params.json

# 4. Alternatively: via environment variable
export RT08_DATA_FILE=en/facts/simulations/double_pendulum/experiment/data/run_1_20260801.csv
python en/facts/simulations/double_pendulum/analyse/rt08_double_pendulum_comparison.py
```

### Expected output

Terminal table:
```
=== RT-08 χ²-Fit: ε_RFT vs. ε_exp ===
Data points N      : 7200
χ²                 : XXXX.XX
Degrees of freedom : 7199
χ²_red             : X.XX
p-value            : X.XXXX
Residuals µ        : ±X.XXX
Residuals σ        : X.XXX
Verdict            : [confirmed / borderline / rejected]
```

Plots (saved in `analyse/`):
- `rt08_scatter.png` — ε_exp vs. ε_RFT scatter plot
- `rt08_timeseries.png` — θ₁(t), θ₂(t), ε(t) time series
- `rt08_residuals.png` — residuals histogram
- `rt08_chi2dist.png` — χ² distribution with marked measured value

### Interpretation of results

| Result | Meaning | Next step |
|---|---|---|
| χ²_red ≤ 1.5 | H₁ not falsified — ε(Δφ) = cos²(Δφ/2) describes real data | Publish, submit RFT result, share data on Zenodo |
| 1.5 < χ²_red ≤ 2.0 | Borderline — systematic errors possible | Improve measurement chain: encoder instead of camera, reduce friction |
| χ²_red > 2.0 | H₁ rejected — RFT formula not supported by real data | Review Axiom A4, validate measurement system |

### Analyse all 5 runs

```bash
for i in 1 2 3 4 5; do
  python en/facts/simulations/double_pendulum/analyse/rt08_double_pendulum_comparison.py \
      en/facts/simulations/double_pendulum/experiment/data/run_${i}_YYYYMMDD.csv
done
```

---

## §6 — Common sources of error and remedies

| Source of error | Symptom | Remedy |
|---|---|---|
| Frame vibration | Periodic noise on θ₁(t) at frame frequency | Stiffen frame, wall-mount on solid masonry |
| Joint friction | Exponential damping, kinetic energy < 95% after 30 s | Clean (degreaser) or replace ball bearings |
| Camera parallax | Systematic angle offset (θ_measured ≠ θ_actual) | Force calibration with known angle; camera ≥ 1 m distance |
| Tracking loss | NaN values or jumps in CSV | Use retroreflective dots + ring light; increase `--min-area` in tracking script |
| Numerical drift | θ₁/θ₂ exceed ±2π | Angle normalisation to (−π, π] is active by default in tracking script |
| Wrong zero position | θ(t) ≠ 0 at rest | Redo calibration, correct `ZERO_OFFSET` in encoder sketch |
| Camera latency | t column not uniform (irregular gaps) | Use fps override in tracking script: `--fps 60` |
| AS5600 I²C conflict | Encoder values constant or jumping | Use TCA9548A I²C multiplexer (both encoders at address 0x36) |

---

## §7 — Reproducibility requirements

What an independent lab must document and report for the result to be recognised
in the RFT results collection:

**Required:**
- [ ] Complete system parameters: L₁, L₂, m₁, m₂ with measurement protocol and uncertainty
- [ ] Calibration plot: θ_measured vs. θ_known (slope, R², residuals)
- [ ] All 5 CSV raw data files as public data (Zenodo upload recommended)
- [ ] χ² analysis plot and terminal output (screenshot or log file)
- [ ] Date and location of measurement
- [ ] Hardware used (smartphone model + fps or encoder type + sampling rate)
- [ ] g_local with source reference

**Recommended:**
- [ ] Photo of the assembled experiment (methodological transparency)
- [ ] Video clips of individual runs (for tracking validation)
- [ ] Energy time series from the analysis script

**Report results:**
Share data and results as a GitHub Issue:
https://github.com/DominicReneSchu/RFT/issues
(Label: `RT-38-result`)

---

## §8 — References

- **Analysis script (RT-08):** [`analyse/rt08_double_pendulum_comparison.py`](../analyse/rt08_double_pendulum_comparison.py)
- **Simulation:** [`double_pendulum.py`](../double_pendulum.py)
- **Theory A4:** [`en/facts/theory/axiomatic_foundation.md`](../../../theory/axiomatic_foundation.md)
- **Group structure:** [`en/facts/theory/gsync_group_structure.md`](../../../theory/gsync_group_structure.md)
- **Tracking script:** [`camera_tracking.py`](camera_tracking.py)
- **Encoder script:** [`encoder_readout.ino`](encoder_readout.ino) + [`encoder_to_csv.py`](encoder_to_csv.py)
- **System parameter template:** [`system_params_template.json`](system_params_template.json)
- **DE version:** [`de/fakten/simulationen/doppelpendel/experiment/protokoll_rt38.md`](../../../../../de/fakten/simulationen/doppelpendel/experiment/protokoll_rt38.md)

---

*RT-38 — Public Experiment Protocol — Tabletop Falsification Test ε(Δφ) = cos²(Δφ/2)*  
*© Dominic-René Schu, 2026 — Resonance Field Theory*
