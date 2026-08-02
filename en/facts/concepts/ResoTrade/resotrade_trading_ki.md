# ResoTrade — Resonance Field Theoretic Multi-Layer Multi-Asset AI

*Application concept of Resonance Field Theory in real financial markets*

*Dominic-René Schu, February 2026 — updated April 2026*

---

## Summary

ResoTrade is a resonance field theoretic trading system that learns through repeated offline simulation to read price cycles as oscillation fields and to accumulate assets beyond pure HODL. It demonstrates the applicability of the axioms of Resonance Field Theory in a real, chaotic system — the financial market. Primary axiom evidence comes from RFT-internal simulations (FLRW, Monte Carlo, double pendulum, resonance reactor); ResoTrade shows as an application concept that these axioms enable structurally superior decisions in a dynamic market environment.

Since V15, ResoTrade is based on a 4-layer architecture (resonance field analysis, experience store, pattern library with proof-of-resonance, neural chart pattern recognition) and operates as a generic multi-asset system across crypto, forex, and commodities. The core architecture — experience learning through resonant phase coupling — is invariant across all versions and all asset classes.

**Key result:** +26.1% vs HODL on average across 4 different market phases (24 months), validated across sideways, bull run, correction, and crash. No classical indicator on the same dataset achieves a correlation above 0.05.

**Accompanying document:** The [altcoin analysis](../../simulations/altcoin_analysis/resotrade_altcoin_analysis.md) shows why altcoins are not independent markets from a resonance-theoretic perspective — documented in the ResoTrade development context (not an independent RFT axiom evidence source).

---

## Classification within Resonance Field Theory

ResoTrade is not an isolated trading software. It is the application of all seven axioms of [Resonance Field Theory](../../../README.md) to a concrete problem — and demonstrates that these axioms work in reality. The axiom mapping table shows how each axiom is implemented in the system; primary, independently verifiable evidence comes from the RFT-internal simulations:

| Axiom | Principle | Application in ResoTrade V15 | Empirical Proof |
|-------|-----------|------------------------------|-----------------|
| [**Axiom 1**](../../docs/definitions/axiomatic_foundation.md) | Universal oscillation ψ(x,t) | Layer 1: Derivative policy via moving averages, cycle phase as dimension | Phase detection beats all indicators |
| [**Axiom 2**](../../docs/definitions/axiomatic_foundation.md) | Superposition of modes | Layer 1: Multiple time scales as superimposed modes in the derivative policy | Multi-time-scale analysis improves timing |
| [**Axiom 3**](../../docs/definitions/axiomatic_foundation.md) | Resonance condition (phase difference) | Layer 3: Proof-of-Resonance — 3-stage signal cascade as resonance criterion | Monte Carlo test: 5 resonances at particle mass, emp. p = 0 |
| [**Axiom 4**](../../docs/definitions/axiomatic_foundation.md) | Coupling energy E = π·ε·h·f | Layer 2: Adaptive decay in experience store, balance controller | System remains operational over 24 months |
| [**Axiom 5**](../../docs/mathematics/energy_direction.md) | Energy is vectorial | Layer 1: Energy direction vector from short- and long-term energy difference | Direction beats prediction |
| [**Axiom 6**](../../docs/definitions/axiomatic_foundation.md) | Information flow through resonance coupling | Layer 3: Pattern library + proof-of-resonance — trades only when signal cascades match | +26.1% vs HODL across all market regimes |
| [**Axiom 7**](../../docs/definitions/axiomatic_foundation.md) | Invariance of field structure | Asset-agnostic architecture: crypto, forex, commodities via the same code path | Same system works for all asset classes |

Primary evidence for Axiom 3 (resonance condition) comes from the [Monte Carlo test](../../empirical/monte_carlo/README.md): 5 resonances at particle masses, emp. p = 0 (1,500,000 simulations, 3 KDE bandwidths, 30 seeds).

### Further Theoretical Foundations

- [Energy sphere and AC/DC decomposition](../../docs/mathematics/energy_sphere.md) — Axiom 1 formalized
- [Energy direction in real systems](../../docs/mathematics/energy_direction.md) — Axiom 5 formalized
- [Resonance time coefficient τ*](../../docs/mathematics/tau_resonance_coefficient.md) — Time scales of coupling
- [Resonance analysis in mass data](../../empirical/cern/documentation.md) — Methodology of empirical validation

---

## Core Idea

```
Money is energy. Trading is time. Trading is power.
A chart is not a progress diagram — it is an oscillation image.
```

The classical view treats money as a medium of exchange and charts as trading results. ResoTrade views the market as a physical oscillation field:

- **DC component** (fundamental tone) → Fundamental growth of the equilibrium price: for stocks through real value creation (invested capital → company growth), for gold/BTC through structural scarcity (limited supply with increasing demand); also artificially producible DC structures via investment + OTC sale. ResoTrade protects this core.
- **AC component** (overtones) → Speculative oscillation around the trend, generated by market participants hoping for rising or falling prices; only this component is traded and generates returns
- **Resonance coupling** → Trades only when bot and market are in phase
- **Energy direction** → Price flow is a vector, not a scalar

The goal is not USD profit, but **more BTC than pure holding** — through resonant extraction of AC oscillation energy while protecting the DC core.

---

## Why ResoTrade Needs No Prediction

A chart is a measurement of reality — it shows the present and the past. Classical approaches try to statistically predict the future from these data: probability distributions, correlations, regressions. The future is modeled as random, the prediction as the best possible estimate within this randomness.

ResoTrade breaks with this paradigm.

Money is energy. Energy in Resonance Field Theory is not a scalar quantity, but a **vector in a multidimensional field** — it has magnitude *and* direction. From the AC/DC decomposition of the price field, the energy direction vector can be calculated:

```
energy_dir = e_short - e_long
```

This is not a probability and not a correlation coefficient. It is a directed quantity that shows where capital energy is flowing. Energy moves to where resonance occurs — and resonance is calculable.

| Classical Statistics | Resonance Field Approach |
|---------------------|--------------------------|
| "The price will be at 65,000 tomorrow" | "Energy is moving from peak to trough" |
| Point prediction (almost always wrong) | Phase detection (structurally robust) |
| Probability of a movement | Direction of energy flow |
| Randomness with distribution | Oscillation with phase |
| Needs prediction to trade | Only needs direction to trade resonantly |

The future of the price is not *predictable*, but it is **navigable**:

- At the **peak**, AC energy is released → SELL is resonant
- At the **trough**, AC energy is absorbed → BUY is resonant
- At the **zero crossing**, coupling efficiency is maximal → timing window
- In **flat** conditions, there is no usable signal → HOLD

The future is not random — it is **periodic**. And periodicity is calculable. Not the exact time, not the exact price, but the phase in the oscillation cycle.

ResoTrade is thus the first system that treats market movements not as a stochastic process, but as a directed energy field — and by calculating the energy direction in the resonance field, makes structurally superior trading decisions without having to predict the price.

---

## Architecture: 4-Layer Model (V15)

### Layer 1 — Resonance Field Analysis

Derivative policy: First and second derivatives of moving averages identify inflection points and accelerations in the price field. The cycle phase (trough, crest, rising, falling) serves as an additional dimension for determining the optimal trading direction.

### Layer 2 — Experience Store (Experience-based RL)

Three-tier store: offline → live → weighted. O(1) dictionary lookup enables real-time decisions without model inference. Adaptive decay ensures that outdated experiences gradually lose weight without being abruptly deleted.

### Layer 3 — Pattern Library + Proof-of-Resonance

Cosine similarity to learned market patterns enables recognition of recurring structures. Cross-asset pattern recognition (transfer learning) transfers experiences between different asset classes. Proof-of-Resonance: 3-stage emergent signal cascade (indicator co-occurrence → signal chains → trade resonance score).

### Layer 4 — Neural Chart Pattern Recognition

Lightweight model recognizes visual chart patterns. Hardware cascade: Edge TPU → GPU → CPU — the system automatically uses the most powerful available hardware.

### Decision Flow

```
Coral-Pattern-Check
       │
       ▼
Proof-of-Resonance
       │
       ▼
Derivative-Policy
       │
       ▼
Experience-Lookup
       │
       ▼
Pattern-Gate → Global-Experience
       │
       ▼
  BUY / SELL / HOLD
```

### MetaTrader 5 — Extension to Forex and Commodities

Since V15, ResoTrade is applied not only to crypto (Kraken API) but also to forex and commodities via MetaTrader 5. This represents an additional empirical domain for the asset-agnostic architecture and confirms Axiom 7 (invariance of field structure): the same 4-layer architecture operates without structural adaptation on different market types.

---

## Empirical Results

### Validated Across 4 Market Regimes (2024–2026)

| Section | Market Phase | Period | Trades | Performance vs HODL |
|---------|-------------|--------|--------|---------------------|
| Sideways + ETF | 60k–70k Range | Mar 2024 – Sep 2024 | 437 | **+33.3%** |
| Bull run 60k–110k | Strong uptrend | Sep 2024 – Mar 2025 | 429 | **+19.8%** |
| Top + Correction | Whipsaw, crash + recovery | Mar 2025 – Sep 2025 | 247 | **+4.3%** |
| Current (Crash) | 110k → 63k | Sep 2025 – Feb 2026 | 279 | **+46.8%** |
| **Average** | **All regimes** | **24 months** | **1392** | **+26.1%** |

### First Live Validation (Day 1, Dry-Run)

| Metric | Value |
|--------|-------|
| Period | 16 hours |
| Cycles | 192 (120 active, 72 skip) |
| Trades | 11 SELLs (0 BUYs) |
| Avg sell price | 68,941 USD |
| Avg e_long at SELL | +3.86% (above MA) |
| Price development | -0.62% |
| Performance vs HODL | **+0.41%** |
| Performance vs All-In-BTC | **+0.73%** |

The system sold at the peak in sideways, generated no BUYs during falling prices, and outperformed HODL from day one.

### Insights

1. **No classical indicator has predictive power** (correlation < 0.05)
2. **Profit comes from resonant energy extraction**, not from prediction
3. **AC/DC decomposition identifies the right moment** in the cycle
4. **Multi-cycle training shows no overfitting** (Δ < 1% after cycle 1 vs 3)
5. **Altcoins disturb the signal** — see [altcoin analysis](../../simulations/altcoin_analysis/resotrade_altcoin_analysis.md)

### Performance History

| Version | Core Change | Performance vs HODL |
|---------|------------|---------------------|
| V6 | Base: MA heuristic + experience store | +35.04% (180d) |
| V7 | pc_bin filter | +35.61% (180d) |
| V10 | Energy direction vector (Axiom 5+6) | +37.03% (180d) |
| V11 | AC/DC decomposition (Axiom 1) | +42.89% (180d) |
| **V11.1** | **Downtrend pause gate, multi-cycle, human hint** | **+26.1% avg (4×6M)** |
| V12 | Energy vector engine MA'(t), MA''(t), MA'''(t) | Architecture rebuild |
| V13 | Multi-horizon experience (48h/14d/28d) | ~0.97 HODL equiv (plateau) |
| **V14** | **12 inconsistencies fixed, all 7 axioms, multi-asset** | **Learning curve >1.0 (target)** |
| **V14.2** | **Multi-asset (BTC/Gold/ETH/EURUSD), per-asset isolation, adaptive thresholds** | **Live operation (4 assets)** |
| **V15** | **4-layer architecture, proof-of-resonance, Coral integration, MT5** | **Multi-domain (crypto + forex + commodities)** |

---

## Physics → Economics: The Structural Isomorphism

| Physics | Trading | Implementation |
|---------|---------|----------------|
| Energy | Capital (BTC + Cash) | Portfolio equivalent in base currency |
| Time | Transaction sequence | Time step in training window |
| Power | Return per time unit | Portfolio equivalent per time step |
| DC (fundamental oscillation) | Fundamental growth (value creation / scarcity) | Long-term moving average |
| AC (harmonic) | Speculative fluctuation (by market participants with long/short expectations) | Price minus long-term average |
| Amplitude | Price oscillation around average | AC amplitude |
| Phase | Position in cycle | Cycle phase (peak/trough/transition/flat) |
| Resonance | Timing coupling bot ↔ market | Coupling factor K = K₀·cos(θ) |
| Damping | Fees, slippage, overtrading | Fee component, cooldown |

The effective power:

```
P_eff = (AC_amplitude / DC_level) · f_trade · η(Δφ) · (1 − γ_fee)
```

### Why Resonance Logic Instead of Conventional ML

| Property | Neural Network | Resonance Logic |
|----------|---------------|-----------------|
| Data requirement | Very high | Low |
| Training time | GPU-intensive | CPU-efficient |
| Explainability | None | Complete |
| Physics foundation | None | Resonance Field Theory |
| Market understanding | Correlations | Oscillation structure |

### Biological Inspiration

ResoTrade works structurally closer to the biological model of the brain than conventional AI: experiences are stored as associations — readable, traceable, correctable — not compressed into opaque weight matrices. The adaptive decay provides gradual, controlled forgetting, analogous to biological memory.

---

## Version History

| Version | Core Change | Performance |
|---------|------------|-------------|
| V6 | MA heuristic + experience store | +35.04% (180d) |
| V7 | pc_bin filter | +35.61% (180d) |
| V10 | Energy direction vector (Axiom 5+6) | +37.03% (180d) |
| V11 | AC/DC decomposition (Axiom 1) | +42.89% (180d) |
| **V11.1** | **Pause gate, multi-cycle, human hint** | **+26.1% avg (4×6M)** |
| V12 | Energy vector engine MA'(t), MA''(t), MA'''(t) | Architecture rebuild |
| V13 | Multi-horizon experience (48h/14d/28d) | ~0.97 HODL equiv (plateau) |
| **V14** | **12 inconsistencies fixed, all 7 axioms, multi-asset** | **Learning curve >1.0 (target)** |
| **V14.2** | **Multi-asset (BTC/Gold/ETH/EURUSD), per-asset isolation, adaptive thresholds** | **Live operation (4 assets)** |
| **V15** | **4-layer architecture, proof-of-resonance, Coral integration, MT5** | **Multi-domain (crypto + forex + commodities)** |

---

## Related Documents

- [Altcoin Analysis: Why Altcoins Are Not Real Markets](../../simulations/altcoin_analysis/resotrade_altcoin_analysis.md)
- [Energy Sphere and AC/DC Decomposition](../../docs/mathematics/energy_sphere.md)
- [Energy Direction in Real Systems](../../docs/mathematics/energy_direction.md)
- [Resonance Time Coefficient τ*](../../docs/mathematics/tau_resonance_coefficient.md)
- [Resonance Analysis in Mass Data](../../empirical/cern/documentation.md)

---

*© Dominic-René Schu — Resonance Field Theory 2025–2026*

---

⬅️ [back to overview](../../../README.md)
