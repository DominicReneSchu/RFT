# Manuscript Review Report

**Manuscript:** `en/peer_review_rft/manuscript_en/rft_manuscript_en_iop.tex`
**Title:** "Resonance Field Theory: Axiomatics, Fundamental Formula, and Empirical Validation"
**Reviewer:** RT-39 automated compliance check, August 2026
**Basis:** IOP author guidelines, PEER_REVIEW_READINESS.md, RT-series results

---

## 1. Abstract Word Count

**IOP Requirement:** ≤ 200 words (iopart class, JPhysComm guidelines)

**Finding:** ⚠️ **EXCEEDS LIMIT**

LaTeX-stripped word count of the abstract (lines 27–66 of manuscript): **approximately 244 words** — approximately 44 words over the IOP limit.

**Specific overruns identified:**
- The FLRW results sentence contains two separate sub-results (scaling coefficient and Δχ² improvement) that could be condensed to one
- The Am-241 description repeats the legacy SNR and the corrected RT-09 SNR in the same sentence — the legacy value (>50,000σ) can be removed as it refers to a pre-correction figure
- The ResoTrade caveat sentence ("primary axiom evidence comes from RFT-internal simulations") is important but the surrounding context is verbose

**Recommended revision for §abstract:**
Remove the legacy Am-241 SNR figure (`$>50{,}000\,\sigma$ legacy, corrected RT-09:`), condense the FLRW results to a single sentence, and reduce the ResoTrade caveat to a clause rather than a full sentence. Target: 195–200 words.

**Action required:** **YES — mandatory before submission**

---

## 2. RT-08 Limitation — χ²_red = 2.42 on Synthetic Data

**IOP / Scientific Standard:** Limitations of simulation comparisons must be explicitly disclosed.

**Finding:** ⚠️ **NOT EXPLICITLY STATED**

The manuscript confirms the double pendulum simulation result (ε(Δφ) = cos²(Δθ/2)) but does not contain an explicit statement that:
- χ²_red = 2.42 is a comparison against the **Lagrange zero-coupling null hypothesis** (A=0), not against real experimental pendulum data
- The comparison data are **synthetic** (N=1500, simulation-generated), not from a physical pendulum measurement

The double pendulum section (§4, around line 1710) notes: "Double pendulum simulation confirms ε(θ₂−θ₁) = cos²(Δθ/2)" without qualification.

**Recommended addition (§4.3 or §4.4, Double Pendulum section):**
> "Note: the reduced chi-squared χ²_red = 2.42 (RT-08) quantifies the goodness of fit against the classical Lagrange null hypothesis (zero RFT coupling, A=0) on synthetic data (N=1500 simulation steps). Comparison against real experimental measurements from a physical double pendulum (RT-38 protocol) remains outstanding and is required for definitive validation."

**Action required:** **YES — add one to two sentences before submission**

---

## 3. RT-10 Limitation — Walk-Forward Backtest 3/5 Folds

**IOP / Scientific Standard:** Partial validation results must be clearly disclosed.

**Finding:** ⚠️ **NOT EXPLICITLY STATED**

The manuscript's ResoTrade section (§4.5) contains the following note (lines ~1127–1133):
> "The 24-month backtest and 5-day live validation results below are not available in the repository (private implementation). This section describes ResoTrade as an application concept..."

This existing note correctly marks the private implementation as not peer-review-ready. However, it does not mention the publicly available RT-10 walk-forward backtest results, specifically:
- Only **3 out of 5 folds** met the falsification criterion (vs_hodl > 0) on synthetic data (Binance Public API fallback, seed=42)
- Ø Sharpe = 0.89, Ø Max-DD = 4.4%
- Live-API verification with real Binance data has not been completed

The public RT-10 backtest is the *reproducible* evidence for ResoTrade's RFT-internal axiom validation. Its mixed result (3/5 folds) should be stated alongside the private 24-month backtest table to give a complete picture.

**Recommended addition (§4.5, after the existing "Application Concept" note):**
> "The publicly reproducible walk-forward backtest (RT-10) on synthetic Binance price data (seed=42, 5-fold cross-validation) yields 3/5 folds positive against the falsification criterion vs\_hodl > 0 (Ø Sharpe = 0.89, Ø Max-DD = 4.4%). Live-API verification with real market data is recommended for conclusive validation."

**Action required:** **YES — add one to two sentences before submission**

---

## 4. RT-38 Experiment Protocol Reference in §6

**Scientific Standard:** Publicly available experiment protocols that enable independent replication should be explicitly cited.

**Finding:** ⚠️ **NOT EXPLICITLY REFERENCED**

Section §6.1 (Experiment I) and the double pendulum measurement protocol (§6, Measurement Protocol subsubsection, line 1436) describe the experimental procedure but do not provide a URL to the publicly available RT-38 protocol on GitHub.

The RT-38 protocol is:
- Publicly accessible at: `https://github.com/DominicReneSchu/RFT/blob/main/facts/simulations/double_pendulum/experiment/protocol_rt38.md`
- Complete: step-by-step measurement guide, CSV format specification, χ² evaluation software pointer
- Low-cost: budget ≈ 100–300 EUR, smartphone-compatible
- Reproducible: any group can perform the experiment independently

This protocol directly enables community falsification testing of Axiom A4. Its absence from the manuscript text means readers cannot locate it without searching the repository.

**Recommended addition (§6, end of Double Pendulum / Experiment I section):**
> "A complete, independently reproducible tabletop experiment protocol (RT-38) is publicly available at \url{https://github.com/DominicReneSchu/RFT} (budget: ca.\ 100–300 EUR, smartphone-compatible tracking). Results may be submitted via the repository issue tracker (label: \texttt{RT-38-result})."

**Action required:** **YES — add one to two sentences before submission**

---

## 5. Figure Completeness Check

**Finding:** ✅ **All referenced figures present**

The following 10 figures are referenced in the manuscript via `\includegraphics{}` and all 10 files are present in `en/peer_review_rft/manuscript_en/figures/`:

| Referenced path | File present |
|-----------------|:------------:|
| `figures/plot.png` | ✅ |
| `figures/hist_mc_vs_real_hits.png` | ✅ |
| `figures/pvalue_curves.png` | ✅ |
| `figures/heatmaps_hits.png` | ✅ |
| `figures/figure_1.png` | ✅ |
| `figures/figure_2.png` | ✅ |
| `figures/h0_scan.png` | ✅ |
| `figures/hubble_tension.png` | ✅ |
| `figures/cmb_comparison.png` | ✅ |
| `figures/cmb_chi2_scan.png` | ✅ |

**Additional note — figure format for IOP production:**
All figures are currently `.png`. IOP production guidelines (IOPGraphicsGuidelines.pdf) recommend EPS or PDF for line art; PNG is acceptable at ≥ 300 dpi. **Action recommended:** Verify DPI with `identify -verbose figures/*.png | grep Resolution` and regenerate from source scripts as PDF/EPS where DPI is below 300 or where scalable vector graphics are available.

---

## 6. Reference Completeness Check

**Finding:** ✅ **All citations have matching bibliography entries**

The manuscript uses 17 unique `\bibitem` entries. All 17 correspond to at least one `\cite{}` in the text. No orphaned bibliography entries were found. The citation style is Vancouver (numeric, sequential), consistent with IOP requirements.

Verified entries:
`planck1901`, `einstein1905`, `bohr1913`, `kuramoto1984`, `cms_opendata`, `rftrepo`, `planck2018v`, `planck2018vi`, `riess2022`, `gdr_atlas`, `ishkhanov2021`, `ripl3`, `berman1975`, `dietrich1988`, `elinp2024`, `pdg2022`, `cms_dielectron`

---

## Summary of Actions Required

| # | Finding | Severity | Action |
|---|---------|----------|--------|
| 1 | Abstract word count ≈ 244 words (IOP limit: 200) | 🔴 Mandatory | Reduce by ~44 words |
| 2 | RT-08 limitation not stated (χ²_red synthetic data) | 🟡 Recommended | Add 1–2 sentences to §4.3 |
| 3 | RT-10 limitation not stated (3/5 folds) | 🟡 Recommended | Add 1–2 sentences to §4.5 |
| 4 | RT-38 protocol URL missing from §6 | 🟡 Recommended | Add 1–2 sentences to §6 |
| 5 | Figure resolution not verified | 🟡 Recommended | Run `identify` check; convert if needed |
| 6 | All figures present | ✅ No action | — |
| 7 | All references complete | ✅ No action | — |
| 8 | LaTeX class `iopart` correct | ✅ No action | — |
| 9 | Keywords 5–10 (9 present) | ✅ No action | — |
| 10 | Tables use `booktabs` style | ✅ No action | — |

**One mandatory action before submission:** Abstract word count reduction.
**Four recommended actions:** RT-08, RT-10, RT-38 limitation/reference additions + figure DPI verification. All are minor (one to two sentences each) and strengthen the manuscript's transparency.

---

*Report version: RT-39, August 2026 — Dominic-René Schu*
