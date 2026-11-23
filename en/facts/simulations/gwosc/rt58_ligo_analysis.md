# RT-58: LIGO GW150914 — Γ(f) Analysis (RFT)

**Status:** 🔄 Data available locally, analysis ready  
**Data source:** GWOSC GW150914, GPS 1126257414–1126261510, 4 kHz  
**Analysis script:** `rt58_extract_and_analyze.py`

---

## Objective

Test the RFT prediction that the cross-correlation between LIGO detectors H1 (Hanford) and L1 (Livingston) follows the pattern

$$\Gamma(f) = \varepsilon(\Delta\varphi(f)) = \cos^2\!\left(\frac{\pi f}{2 f_0}\right), \quad f_0 = \frac{c}{2\, d_{HL}} \approx 50\ \mathrm{Hz}$$

where $d_{HL} \approx 3002\ \mathrm{km}$ is the detector separation.

---

## Theoretical Background

### Overlap Reduction Function (ORF)

The standard ORF (Flanagan 1993) describes how well two detectors respond to correlated gravitational wave signals. For H1–L1:

$$\gamma_\mathrm{ORF}(f) = \frac{5}{8\pi} \sum_{A} \int_{S^2} F_H^A(\hat{n}) F_L^A(\hat{n}) \, e^{2\pi i f \hat{n}\cdot\Delta\vec{x}/c} \, d^2\hat{n}$$

### RFT Formulation

In RFT, the coupling efficiency is a field:

$$\varepsilon(\Delta\varphi) = \cos^2\!\left(\frac{\Delta\varphi}{2}\right)$$

For a gravitational-wave-induced phase difference $\Delta\varphi(f) = \pi f / f_0$:

$$\Gamma_\mathrm{RFT}(f) = \cos^2\!\left(\frac{\pi f}{2 f_0}\right)$$

**Predictions:**
- First zero at $f_0 \approx 50\ \mathrm{Hz}$ (geometric, no free parameters)
- Mean $\varepsilon$ in LIGO band (20–200 Hz): $\varepsilon_0 \approx \Omega_\Lambda = 0.6847$

---

## Usage

### Requirements

```bash
pip install h5py numpy scipy matplotlib
```

### Run

```bash
python rt58_extract_and_analyze.py \
  --h1 H-H1_LOSC_4_V2-1126257414-4096.hdf5 \
  --l1 L-L1_LOSC_4_V2-1126257414-4096.hdf5 \
  --outdir rt58_output/
```

The script:
1. Extracts a 32s window around GPS 1126259462.4 (GW150914 event)
2. Saves small HDF5 files (~500 KB) to `rt58_output/`
3. Computes $\Gamma(f)$ via cross-spectral density
4. Compares with RFT prediction and standard ORF
5. Saves plot and result text file

---

## Expected Result

| Quantity | RFT prediction | Source |
|----------|---------------|--------|
| $f_0$ (first zero) | $\approx 50\ \mathrm{Hz}$ | Geometry $c/2d_{HL}$ |
| $\varepsilon_\mathrm{mean}$ (20–200 Hz) | $0.6847 \pm ?$ | $\varepsilon_0 = \Omega_\Lambda$ |
| Structure | $\cos^2$ modulation | A4+A5 (RFT) |

---

## Important Limitations

1. **GW150914 is a single event** — statistically weak
2. **SNR-dominated:** Correlation is primarily determined by the detected signal
3. **Stochastic background** would be better suited (requires months of data)
4. **B_grav status:** $\varepsilon = -g_{tt}$ is an identification, not derived from A1–A9

**Conclusion:** The experiment can show consistency or inconsistency with RFT, but cannot prove it. For a genuine test, the stochastic gravitational wave background (SGWB) with O3 data would be more appropriate.
