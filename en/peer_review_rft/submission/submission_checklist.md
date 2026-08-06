# Submission Checklist — Journal of Physics Communications

*Dominic-René Schu — August 2026*
*Manuscript: "Resonance Field Theory: Axiomatics, Fundamental Formula, and Empirical Validation"*
*Submission portal: https://mc.manuscriptcentral.com/jphyscomm*

---

## Category A — Manuscript Compliance (IOP Standards)

### LaTeX and Document Structure

- [x] **LaTeX class:** `\documentclass[12pt]{iopart}` — present in `rft_manuscript_en_iop.tex` line 1
- [ ] **Abstract word count ≤ 200 words (IOP requirement):** ⚠️ **ACTION REQUIRED**
  - Current word count (LaTeX-stripped estimate): **~244 words** — exceeds the 200-word IOP limit
  - Action: Reduce abstract by approximately 44 words. Suggested cuts: shorten the FLRW result sentence; condense the ResoTrade caveat; reduce the Am-241 SNR detail to a single number. The abstract must retain: main formula, four validation domains, two experimental proposals, falsification criteria, and open-data statement.
- [x] **Title:** Present — "Resonance Field Theory: Axiomatics, Fundamental Formula, and Empirical Validation"
- [x] **Author name and address block:** Present — `\author{Dominic-René Schu}`, `\address{Independent Researcher, ...}`
- [x] **ORCID:** Present in address block (0009-0004-9769-9061)
- [x] **Keywords:** 9 keywords present — within the IOP range of 5–10. Keywords: resonance, field theory, coupling operator, axiomatics, Monte Carlo simulation, FLRW cosmology, Giant Dipole Resonance, transmutation, Schrödinger equation
- [x] **Section structure:** Follows standard IOP article structure (Introduction, Theory, Results, Discussion, Conclusions)
- [x] **Equation numbering:** Sequential, using standard `iopart` equation environment
- [x] **Page numbering:** Handled by `iopart` class

### Figures

- [x] **Figure directory:** `figures/` exists at `en/peer_review_rft/manuscript_en/figures/`
- [x] **All referenced figures present:**
  - `figures/plot.png` ✅
  - `figures/hist_mc_vs_real_hits.png` ✅
  - `figures/pvalue_curves.png` ✅
  - `figures/heatmaps_hits.png` ✅
  - `figures/figure_1.png` ✅
  - `figures/figure_2.png` ✅
  - `figures/h0_scan.png` ✅
  - `figures/hubble_tension.png` ✅
  - `figures/cmb_comparison.png` ✅
  - `figures/cmb_chi2_scan.png` ✅
- [ ] **Figure format — EPS or PDF (IOP production requirement):** ⚠️ **ACTION REQUIRED**
  - All figures are currently `.png` format. IOP production prefers EPS or PDF for line art and vector graphics; PNG is acceptable for photographic/raster content at ≥ 300 dpi.
  - Action: Verify all figures are ≥ 300 dpi. For simulation plots (figure_1, figure_2, h0_scan, cmb_comparison, cmb_chi2_scan, hubble_tension), regenerate as PDF or EPS from the original Python scripts. Raster outputs (hist_mc_vs_real_hits, heatmaps_hits, pvalue_curves) may remain as high-resolution PNG.
- [x] **Figure captions:** All figures have complete captions with panel labels where applicable
- [ ] **Figure resolution ≥ 300 dpi:** ⚠️ **ACTION REQUIRED** — Verify with `identify -verbose figures/*.png | grep Resolution` (ImageMagick). If below 300 dpi, regenerate at higher resolution from source scripts.

### Tables

- [x] **Table style:** Uses `booktabs` package (`\toprule`, `\midrule`, `\bottomrule`) — consistent with IOP recommendation against vertical lines
- [x] **No vertical rules in tables:** Confirmed — `booktabs` style throughout

### References

- [x] **Reference style:** Vancouver (numeric, sequential) — consistent with IOP standard
- [x] **Bibliography entries present for all cited works:**
  - `\cite{planck1901}` → `\bibitem{planck1901}` ✅
  - `\cite{einstein1905}` → `\bibitem{einstein1905}` ✅
  - `\cite{bohr1913}` → `\bibitem{bohr1913}` ✅
  - `\cite{kuramoto1984}` → `\bibitem{kuramoto1984}` ✅
  - `\cite{cms_opendata}` → `\bibitem{cms_opendata}` ✅
  - `\cite{rftrepo}` → `\bibitem{rftrepo}` ✅
  - `\cite{planck2018v}` → `\bibitem{planck2018v}` ✅
  - `\cite{planck2018vi}` → `\bibitem{planck2018vi}` ✅
  - `\cite{riess2022}` → `\bibitem{riess2022}` ✅
  - `\cite{gdr_atlas}` → `\bibitem{gdr_atlas}` ✅
  - `\cite{ishkhanov2021}` → `\bibitem{ishkhanov2021}` ✅
  - `\cite{ripl3}` → `\bibitem{ripl3}` ✅
  - `\cite{berman1975}` → `\bibitem{berman1975}` ✅
  - `\cite{dietrich1988}` → `\bibitem{dietrich1988}` ✅
  - `\cite{elinp2024}` → `\bibitem{elinp2024}` ✅
  - `\cite{pdg2022}` → `\bibitem{pdg2022}` ✅
  - `\cite{cms_dielectron}` → `\bibitem{cms_dielectron}` ✅
- [x] **No orphaned `\bibitem` entries** (all entries are cited)

### Declarations

- [x] **Author Declaration:** Single author — no co-author conflicts. State in submission portal: "This is a single-author manuscript."
- [x] **Data Availability Statement:** Present in manuscript — GitHub URL https://github.com/DominicReneSchu/RFT referenced
- [x] **Conflicts of Interest:** None — declare explicitly in submission portal
- [x] **Funding Statement:** No external funding — declare explicitly: "This research received no external funding."
- [x] **Supplementary Material:** Source code and simulation scripts referenced via GitHub repository

---

## Category B — Scientific Completeness

### Core Theoretical Claims

- [x] **Falsification criteria — explicit and numerical (§6):** Present — Am-241 SNR ≥ 3σ at 100 h (realistic scenario); ⁸⁷Rb |Δ⟨x⟩| ≈ 2.0·λ μm at Δφ = π
- [x] **Axiom Status Table (August 2026 version):** Present in §2.8 — all seven axioms with derivation status
- [x] **κ convention (κ_RFT = 1):** Explicitly declared as normalization convention in §3.4 — not claimed as derivation
- [x] **A7 domain transfer (ResoTrade) declared as analogy:** Present — ResoTrade classified as "application concept" with caveat "primary axiom evidence comes from RFT-internal simulations" (abstract and §4.4)

### Limitation Disclosures

- [ ] **RT-08 Limitation — χ²_red = 2.42 on synthetic data, not real experimental data:** ⚠️ **ACTION REQUIRED**
  - Current status: The manuscript mentions the double pendulum simulation confirms ε(Δφ) = cos²(Δφ/2) but does not explicitly state that the χ²_red = 2.42 result is a comparison against the Lagrange null hypothesis (A=0, N=1500) using synthetic data — not against real physical measurements.
  - Action: Add one sentence to §4.3 (Double Pendulum) or §4.4: "Note: the reduced chi-squared χ²_red = 2.42 (RT-08) is computed against the Lagrange zero-coupling null hypothesis on synthetic data; comparison against real experimental measurements (e.g., from RT-38 protocol) remains outstanding."

- [ ] **RT-10 Limitation — Walk-Forward Backtest: 3/5 folds positive, not all folds:** ⚠️ **ACTION REQUIRED**
  - Current status: The manuscript references the ResoTrade backtest results but does not explicitly state that only 3 out of 5 walk-forward folds met the falsification criterion (vs_hodl > 0) on synthetic data.
  - Action: Add one sentence to §4.5 (ResoTrade): "The walk-forward backtest (RT-10) on synthetic price data (seed=42) yields 3/5 folds positive (falsification criterion vs_hodl > 0, Ø Sharpe = 0.89, Ø Max-DD = 4.4%); live-API verification with real Binance data is recommended for conclusive validation."

- [x] **RT-09 Limitation — Conservative Am-241 scenario:** Present in manuscript abstract — "corrected RT-09: SNR ≈ 10σ at 100 h" with implicit reference to the conservative scenario requiring longer exposure. Can be strengthened. See §6.1.

- [ ] **RT-38 — Public experiment protocol referenced in §6:** ⚠️ **ACTION REQUIRED**
  - Current status: §6 describes the experimental setup and measurement protocol but does not explicitly reference the publicly available RT-38 experiment protocol at the GitHub repository.
  - Action: Add one sentence at the end of §6.1 (Experiment I / Double Pendulum section, if present) or §6.2: "A complete, independently reproducible experiment protocol (RT-38) is available at https://github.com/DominicReneSchu/RFT/blob/main/facts/simulations/double_pendulum/experiment/protocol_rt38.md (budget: ≈200 EUR, smartphone-compatible)."

### Structural Checks

- [x] **Section 2 (Axioms) is internally consistent:** Axioms A1–A7 each have statement, formula, and status
- [x] **Section 3 (Mathematical Formulation) cites RT-01 and RT-02 for derived results**
- [x] **Section 4 (Empirical Validation) covers all four primary domains**
- [x] **Section 5 (Comparison with Established Theories) addresses QFT, GR, and QM**
- [x] **Section 6 (Experimental Predictions) gives two proposals with numerical criteria**

---

## Category C — Submission Logistics

### Portal and Format

- [ ] **Submission portal:** https://mc.manuscriptcentral.com/jphyscomm — register or log in before submitting
- [ ] **Article Type:** Select "Original Research Article" in the submission portal
- [ ] **Subject Category:** Select "Mathematical Physics" primary, "Quantum Physics" secondary

### File Package

- [ ] **Main manuscript file:** `rft_manuscript_en_iop.tex` — upload as primary LaTeX file
- [ ] **IOP class files (required):** `iopart.cls`, `iopart12.clo`, `iopart10.clo`, `iopams.sty`, `setstack.sty` — include in ZIP
- [ ] **Figure files:** all 10 PNG files from `figures/` — include in ZIP (or upload separately per portal instructions)
- [ ] **ZIP archive:** Create: `zip rft_submission.zip rft_manuscript_en_iop.tex iopart.cls iopart12.clo iopart10.clo iopams.sty setstack.sty figures/`
- [ ] **Compiled PDF:** `rft_manuscript_en_iop.pdf` — upload separately as a standalone PDF
- [ ] **Cover Letter:** `cover_letter_jphyscomm.pdf` (compile `cover_letter_jphyscomm.tex` with `pdflatex`) — upload as cover letter

### Reviewer Information (for portal)

Each suggested reviewer requires: Full name + Email + Institution + One-sentence justification

- [ ] Dr. Günter Dissertori — ETH Zürich — dissertori@phys.ethz.ch — *CMS collaboration, expertise in resonance searches in dielectron channels, directly relevant to the Monte Carlo analysis in §4.1*
- [ ] Dr. Markus Klute — MIT — mklute@mit.edu — *CMS/Higgs physics, expertise in resonance structure and precision SM measurements*
- [ ] Prof. Gerd Rudolph — Universität Leipzig — rudolph@itp.uni-leipzig.de — *Group-theoretic structures in gauge theories, directly relevant to the G_sync proof in §3.4*
- [ ] Dr. Licia Verde — Universitat de Barcelona / ICREA — liciaverde@icc.ub.edu — *CMB power spectrum analysis and Hubble tension, directly relevant to the FLRW validation in §4.2*
- [ ] Prof. Markus Oberthaler — Universität Heidelberg — markus.oberthaler@kip.uni-heidelberg.de — *BEC physics and ⁸⁷Rb interferometry, directly relevant to Experiment II in §6.2*

### Pre-Submission Quality Check

- [ ] **Compile manuscript locally** with `pdflatex rft_manuscript_en_iop.tex` — no errors, no missing figure warnings
- [ ] **Verify abstract word count** after any edits — must be ≤ 200 words
- [ ] **Spell-check** the final PDF (pdftotext + aspell or equivalent)
- [ ] **Confirm all URLs** in the manuscript are live and accessible

### Parallel arXiv Submission (Recommended)

- [ ] **arXiv pre-print:** Submit to arXiv simultaneously with or before journal submission
  - **Category:** `quant-ph` (primary) or `physics.gen-ph` (if quant-ph scope decision is uncertain)
  - **Justification:** Establishes priority date; increases visibility before review; IOP allows simultaneous arXiv posting
  - Use the same `.tex` file; arXiv will auto-compile with standard packages
  - arXiv identifier to be added to manuscript as a footnote after acceptance is confirmed

---

*Checklist version: RT-39, August 2026*
