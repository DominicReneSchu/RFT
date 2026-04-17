# ResoTrade — Resonance Field Theory Multi-Asset AI with AC/DC Decomposition

*Empirical validation of Resonance Field Theory in real financial markets*

*Dominic-René Schu, February 2026 — updated March 2026*

---

## Summary

ResoTrade is a resonance field theory trading system that learns through repeated offline simulation to read price cycles as oscillation fields and accumulate assets beyond pure HODL. It is the first empirical proof that the axioms of Resonance Field Theory produce structurally superior decisions in a real, chaotic system — the financial market.

Since V14.2 ResoTrade is a generic multi-asset system (BTC, Gold, ETH, EURUSD) with a 12-dimensional fine chain, adaptive thresholds (V14 field state), parallel training, and dashboard-controlled operation via Streamlit. The core architecture — experience learning through resonant phase coupling — is invariant across all versions and all asset classes.

**Key result:** +26.1% vs HODL on average across 4 different market phases (24 months), validated through sideways, bull run, correction and crash. No classical indicator on the same dataset achieves a correlation above 0.05.

**Companion document:** The [Altcoin analysis](../../simulations/altcoin_analysis/resotrade_altcoin_analysis.md) shows why altcoins are not independent markets from a resonance theory perspective — and thereby confirms the axioms of Resonance Field Theory from a second, independent direction.

---

## Embedding in Resonance Field Theory

ResoTrade is not an isolated trading application. It is the application of all seven axioms of the [Resonance Field Theory](../../../README.md) to a concrete problem — and the empirical proof that these axioms work in reality:

| Axiom | Principle | Application in ResoTrade V14.2 | Empirical evidence |
|-------|-----------|-------------------------------|-------------------|
| [**Axiom 1**](../../docs/definitions/axiomatic_foundation.md) | Universal oscillation ψ(x,t) | AC/DC decomposition: price = DC + AC | Phase detection beats all indicators |
| [**Axiom 2**](../../docs/definitions/axiomatic_foundation.md) | Superposition of modes | MA_SHORT + MA_LONG as superimposed modes | Multi-timescale analysis improves timing |
| [**Axiom 3**](../../docs/definitions/axiomatic_foundation.md) | Resonance condition (phase difference) | Symmetric BUY/SELL thresholds (V14 fix) | Altcoin analysis confirms: no resonance without own natural frequency |
| [**Axiom 4**](../../docs/definitions/axiomatic_foundation.md) | Coupling energy E = π·ε·h·f | Consolidated decay (0.92), balance controller | System remains actionable over 24 months |
| [**Axiom 5**](../../docs/mathematics/energy_direction.md) | Energy is vectorial | `energy_dir = e_short - e_long`, reduced chain dimensionality | Direction beats prognosis |
| [**Axiom 6**](../../docs/definitions/axiomatic_foundation.md) | Information flow through resonance coupling | Pattern gate, resonance gate: trades only in phase | +26.1% vs HODL across all market regimes |
| [**Axiom 7**](../../docs/definitions/axiomatic_foundation.md) | Invariance of field structure | Asset-agnostic architecture: BTC, Gold, ETH, EURUSD through the same code path | Same system works for all asset classes |

The [Altcoin analysis](../../simulations/altcoin_analysis/resotrade_altcoin_analysis.md) confirms Axiom 3 (Resonance Condition) negatively: Systems without their own natural frequency produce no resonance — empirically demonstrated over 200,000 episodes.

### Further theoretical foundations

- [Energy sphere and AC/DC decomposition](../../docs/mathematics/energy_sphere.md) — Axiom 1 formalised
- [Energy direction in real systems](../../docs/mathematics/energy_direction.md) — Axiom 5 formalised
- [Resonance time coefficient τ*](../../docs/mathematics/tau_resonance_coefficient.md) — Timescales of coupling
- [Resonance analysis in mass data](../cern/documentation.md) — Methodology of empirical validation
- Dual resonance monetary system — Social implication
- ResoMusic — Domain transfer — The same 6 architectural patterns validated in the sound domain

---

## Core Idea

```
Money is energy. Trade is time. Trading is power.
A chart is not a progression diagram — it is an oscillation image.
```

The classical view treats money as a medium of exchange and charts as trading results. ResoTrade treats the market as a physical oscillation field:

- **DC component** (fundamental) → Long-term trend = HODL core, never traded
- **AC component** (overtones) → Tradable oscillation around the trend, delivers return
- **Resonance coupling** → Trades only when bot and market are in phase
- **Energy direction** → Price flow is a vector, not a scalar

The goal is not USD profit but **more BTC than pure holding** — through resonant extraction of AC oscillation energy with protected DC core.

---

## Why ResoTrade Needs No Prognosis

A chart is a measurement of reality — it shows the present and the past. Classical approaches try to predict the future statistically from this data: probability distributions, correlations, regressions. The future is modelled as random, the prognosis as the best possible estimate within this randomness.

ResoTrade breaks with this paradigm.

Money is energy. In Resonance Field Theory, energy is not a scalar quantity but a **vector in a multidimensional field** — it has magnitude *and* direction. The energy direction vector can be computed from the AC/DC decomposition of the price field:

```
energy_dir = e_short - e_long
```

This is neither a probability nor a correlation coefficient. It is a directed quantity showing where capital energy flows. Energy moves to where resonance occurs — and resonance is computable.

| Classical statistics | Resonance field approach |
|---|---|
| "The price will be at 65,000 tomorrow" | "The energy moves from peak to trough" |
| Point prognosis (almost always wrong) | Phase detection (structurally robust) |
| Probability of a movement | Direction of energy flow |
| Random with distribution | Oscillation with phase |
| Needs prediction to trade | Needs only direction for resonant trading |

The future price is not *predictable*, but it is **navigable**:

- At the **peak**, AC energy is released → SELL is resonant
- At the **trough**, AC energy is absorbed → BUY is resonant
- At the **zero crossing**, coupling efficiency is maximum → timing window
- In **flat** there is no usable signal → HOLD

The future is not random — it is **periodic**. And periodicity is computable. Not the exact moment, not the exact price, but the phase in the oscillation cycle.

ResoTrade is thus the first system that treats market movements not as a stochastic process but as a directed energy field — and through computation of energy direction in the resonance field makes structurally superior trading decisions without having to predict the price.

---

## Vision: Decentralised Market Stabilisation through Resonant Trading

### The Thought Experiment

ResoTrade runs on a Raspberry Pi for €35, needs 5 watts of power and a CSV file as experience store. Any worker can fill a Kraken account with what remains of their salary — €50, €100, €500 per month. The system trades autonomously, 24/7, resonantly.

What happens when hundreds of thousands do this?

### Two Opposing Forces at Mass Adoption

**AC damping (short-term):** Everyone sells at the peak, everyone buys at the trough. Peaks are dampened, troughs are raised. Volatility decreases — and with it the return per oscillation cycle.

**DC elevation (long-term):** More users mean more permanent BTC demand with limited supply (21 million BTC). Each user holds a HODL core of 10%, never sold — permanently withdrawn from the market.

```
100,000 users × avg €500 × 10% HODL core = €5 million permanently bound
1,000,000 users × avg €500 × 10% HODL core = €50 million permanently bound
```

| Effect | Timescale | Component | Impact |
|---|---|---|---|
| Volatility damping | Hours to days | AC decreases | Return per swing decreases |
| Demand pressure | Months to years | DC rises | Base value rises for all |

The AC return becomes smaller, but the DC base on which it sits becomes larger. The user benefits on two levels: moderate excess return through active trading *and* rising value of the HODL core through collective demand.

### Self-Regulating Adoption

```
More users → less volatility → less AC return → some stop
→ volatility rises again → return rises → new users come
→ equilibrium at reduced but stable volatility
```

This is itself an oscillation system — a meta-resonance. Adoption settles at a level where enough volatility remains for moderate return, but extreme swings are dampened.

### Decentralised Stabilisation Instead of Central Control

A million Raspberry Pis trading resonantly act as a **decentralised stabilisation mechanism** — fewer crashes, fewer bubbles, steadier growth. What central banks attempt for fiat currencies emerges here organically: stability not through central control but through resonant coupling of decentralised actors.

### Why the Monetary System Becomes More Just

Today's fiat system has a structural asymmetry — the Cantillon effect:

```
Fiat system:
  Money creation → central bank → commercial banks → major clients → ... → citizen
  Whoever has access first benefits
  Asymmetry is structurally built in

BTC + ResoTrade:
  21 million BTC → open to everyone → same algorithm for all
  → same physics, same axioms, same performance
  No Cantillon effect, no first-mover advantage
```

ResoTrade neutralises the last remaining advantage of institutions: the information and technology lead. Energy direction beats prognosis — on a Raspberry Pi, for 5 watts.

| Property | Hedge fund on GPU cluster | ResoTrade on Raspberry Pi |
|---|---|---|
| Hardware | Millions in infrastructure | €35 ARM board, 4GB RAM |
| Training | Hours on A100 GPUs | 15 minutes on CPU |
| Experience store | Terabytes of model weights | 2MB CSV file |
| Power consumption | Kilowatts | 5 watts |
| Explainability | Black box | Every decision traceable |
| Physics basis | None — correlations in data | Resonance Field Theory (7 axioms) |
| Access | Accredited investors | Anyone with €50 and WiFi |

### Long-Term Perspective

```
Phase 1: Individual users accumulate BTC              (Years 1-3)
Phase 2: Collective demand raises DC base             (Years 3-7)
Phase 3: BTC becomes store of value alongside fiat    (Years 5-10)
Phase 4: Employers offer BTC salary (demand)          (Years 7-15)
Phase 5: BTC denomination becomes normal              (Years 10-20)

Driver in every phase: Not ideology, but
→ "My Raspberry Pi makes +X% vs savings account"
→ Word of mouth through measurable results
```

The monetary system does not become just because someone *makes* it just. It becomes just because the resonance structure forces justice as an equilibrium state — every participant, whether with €50 or €50,000, operates in the same field, by the same axioms, with the same algorithm.

This is not a utopia. This is physics.

---

## Empirical Results

### Validated Across 4 Market Regimes (2024–2026)

| Section | Market phase | Period | Trades | Performance vs HODL |
|---------|-------------|--------|--------|---------------------|
| Sideways + ETF | 60k–70k range | Mar 2024 – Sep 2024 | 437 | **+33.3%** |
| Bull run 60k–110k | Strong uptrend | Sep 2024 – Mar 2025 | 429 | **+19.8%** |
| Top + correction | Whipsaw, crash + recovery | Mar 2025 – Sep 2025 | 247 | **+4.3%** |
| Current (crash) | 110k → 63k | Sep 2025 – Feb 2026 | 279 | **+46.8%** |
| **Average** | **All regimes** | **24 months** | **1392** | **+26.1%** |

### First Live Validation (Day 1, Dry Run)

| Metric | Value |
|--------|-------|
| Period | 16 hours |
| Cycles | 192 (120 active, 72 skip) |
| Trades | 11 SELLs (0 BUYs) |
| Avg. sell price | 68,941 USD |
| Avg. e_long at SELL | +3.86% (above MA) |
| Price development | -0.62% |
| Performance vs HODL | **+0.41%** |
| Performance vs all-in BTC | **+0.73%** |

The system sold at the peak in sideways, generated no BUYs on falling prices, and outperformed HODL from day one.

### Findings

1. **No classical indicator has predictive power** (correlation < 0.05)
2. **Profit comes from resonant energy extraction**, not from prognosis
3. **AC/DC decomposition identifies the right moment** in the cycle
4. **Multi-cycle training shows no overfitting** (Δ < 1% after cycle 1 vs 3)
5. **Altcoins disturb the signal** — see [Altcoin analysis](../../simulations/altcoin_analysis/resotrade_altcoin_analysis.md)

### Performance History

| Version | Core change | Performance vs HODL |
|---------|-------------|---------------------|
| V6 | Basis: MA heuristic + experience store | +35.04% (180d) |
| V7 | pc_bin filter | +35.61% (180d) |
| V10 | Energy direction vector (Axiom 5+6) | +37.03% (180d) |
| V11 | AC/DC decomposition (Axiom 1) | +42.89% (180d) |
| **V11.1** | **Downtrend pause gate, multi-cycle, human hint** | **+26.1% avg (4×6M)** |
| V12 | Energy vector engine MA'(t), MA''(t), MA'''(t) | Architecture rebuild |
| V13 | Multi-horizon experience (48h/14d/28d) | ~0.97 HODL equiv (plateau) |
| **V14** | **12 inconsistencies fixed, all 7 axioms, multi-asset** | **Learning curve >1.0 (target)** |
| **V14.2** | **Multi-asset (BTC/Gold/ETH/EURUSD), per-asset isolation, adaptive thresholds** | **Live operation (4 assets)** |

---

## Physics → Economics: The Structural Isomorphism

| Physics | Trading | In code |
|---------|---------|---------|
| Energy | Capital (BTC + cash) | `portfolio.btc_equiv()` |
| Time | Transaction sequence | `step` in training window |
| Power | Return per time unit | `btc_equiv / steps` |
| DC (fundamental oscillation) | Long-term trend | `MA_LONG` (168h) |
| AC (overtone) | Tradable deviation | `price - MA_LONG` |
| Amplitude | Price oscillation around MA | `ac_amplitude` |
| Phase | Position in cycle | `ac_phase` (peak/trough/transition/flat) |
| Resonance | Timing coupling bot ↔ market | `K = K₀·cos(θ)` |
| Damping | Fees, slippage, overtrading | `fee_pct`, cooldown |

The effective power:

```
P_eff = (AC_amplitude / DC_level) · f_trade · η(Δφ) · (1 − γ_fee)
```

### Why Resonance Logic Instead of Conventional ML

| Property | Neural network | Resonance logic |
|----------|----------------|-----------------|
| Data requirements | 100K+ data points | 5,000–10,000 episodes |
| Training time | GPU hours | 15 minutes (CPU) |
| Explainability | None | Fully (readable CSV) |
| Physics basis | None | Resonance Field Theory |
| Market understanding | Correlations | Oscillation structure |

### Biological Precedent: Experience Learning Instead of Weight Optimisation

ResoTrade is architecturally closer to the biological model of the brain than conventional AI. This is not a metaphor — it is an architectural correspondence.

The brain does not store weight matrices. It stores associations — situation patterns linked to outcomes, reinforced by repetition, weakened by time. A neural network compresses experience into opaque weights — the model *is* the experience, but it can no longer be reconstructed. ResoTrade separates both: The experience remains **as experience** — readable, traceable, correctable.

```
Training (offline, compute-intensive)       Live (real-time, lightweight)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━              ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
30h × 100% CPU                              Dict lookup: O(1)
40,000 episodes                             Chain → result → count
720-step window per episode                 No model, no gradient
Experience accumulates                      Experience is present as CSV
```

Computational intensity shifts to training — like the brain, which needs years to build experience, but then decides in milliseconds. Offline training is childhood: intensive experience collection under controlled conditions. Live operation is adulthood: fast decisions based on accumulated experience, with ongoing learning via the live experience channel (`btc_experience_live.csv`).

| Property | Brain | ResoTrade | Conventional AI (NN) |
|---|---|---|---|
| Knowledge form | Associations, experiences | Experience CSV (chain → count) | Weight matrices (opaque) |
| Decision | Pattern recognition + instinct | Chain lookup O(1) + asymmetry | Forward pass O(n²) |
| Forgetting | Gradual, controlled | Decay 0.92/pass | Catastrophic forgetting |
| Learning after training | Yes, lifelong | Yes, live experience channel | No (retraining needed) |
| Explainability | Partial ("experience says...") | Full (chain traceable) | Barely |
| Live compute cost | Low (synapse lookup) | Low (dict lookup) | High (GPU/CPU) |
| Training | Years of intensive experience | 30h CPU (parallelisable to ~8h) | GPU hours |

The decay (0.92 per pass) is biologically more honest than catastrophic forgetting: the brain forgets gradually and in a controlled manner. ResoTrade decays with a constant factor — old experience becomes quieter but is never abruptly deleted. A neural network, by contrast, overwrites uncontrollably when retraining.

Since V14.2.4 training is parallelisable: The 4 market phase segments can be trained simultaneously (configurable worker count 1–4). This reduces training time from ~30h to ~8h with 4 workers — without quality loss, since each worker operates in an isolated experience space and the partial experiences are merged after completion.

---

## Architecture

### Resonance Field Theory Policy

```
┌──────────────────────────────────────────────────────────────┐
│          RESONANCE POLICY V14.2 (Axioms 1–7)                │
│                                                              │
│   State ──→ AC/DC decomposition (Axiom 1)                   │
│     │          DC = MA_LONG, AC = price - DC                 │
│     │          Phase: peak / trough / transition / flat      │
│     │              │                                         │
│     │              ▼                                         │
│     ├──→ Energy direction vector (Axiom 5)                   │
│     │          energy_dir = e_short - e_long                 │
│     │              │                                         │
│     │              ▼                                         │
│     │        Resonance gate (Axiom 6)                        │
│     │          allow_buy  = energy_dir > -0.005              │
│     │          allow_sell = energy_dir <  0.005              │
│     │              │                                         │
│     │              ▼                                         │
│     ├──→ Phase-modulated rule policy                         │
│     │       Peak  → SELL more aggressively (MEDIUM at wide amp) │
│     │       Trough → BUY more aggressively (threshold -0.5%) │
│     │              │                                         │
│     │              ▼                                         │
│     ├──→ Balance controller (Axiom 4)                        │
│     │       cash < 8% → no BUY                               │
│     │       sellable < 5% → no SELL                          │
│     │              │                                         │
│     │              ▼                                         │
│     └──→ Experience store (chain → score)                    │
│              Hybrid decision:                                 │
│              20–50% rule + 50–80% experience (×confidence)   │
│                    │                                         │
│                    ▼                                         │
│              BUY / SELL / HOLD                               │
└──────────────────────────────────────────────────────────────┘
```

### AC/DC Decomposition of the Price Field

```
Price ─────────────────────────────────────────────
         ╱╲       ╱╲                ╱╲
        ╱  ╲     ╱  ╲    AC       ╱  ╲
  ─────╱────╲───╱────╲──────────╱────╲────── MA_LONG (DC)
      ╱      ╲ ╱      ╲       ╱      ╲
     ╱        ╳        ╲     ╱        ╲
              ↑              ↑
        zero crossing   zero crossing
       (max. coupling)  (max. coupling)

  Peak:       AC/Amplitude > +0.3 → SELL preferred
  Trough:     AC/Amplitude < -0.3 → BUY preferred
  Transition: between → experience decides
  Flat:       Amplitude < 0.1% → no signal
```

### Rule Chain in Environment

```
Policy decision (phase-modulated)
       │
       ▼
  1. Downtrend pause gate — BEAR_STRONG + e_long < -5% → ALL paused
  2. Regime rule — BULL_STRONG → no SELL, BEAR_STRONG → no BUY
  3. MA-SELL guard — below MA + energy upward → no SELL (peak exception)
  4. ATH rule — no BUY near historical high
  5. Trend rule — downtrend: BUY only deep below MA
  6. MA rule — no BUY >5% above MA short
  7. Cooldown — MEDIUM→SMALL on overtrading
  8. Balance controller — cash < 8%: no BUY, sellable < 5%: no SELL
  9. HODL core protection — never sell more than free BTC
       │
       ▼
  Effective action → Portfolio
```

### Human Hint System

```
┌─────────────────────────────────────────────────────────────┐
│   HUMAN                         SYSTEM                      │
│                                                             │
│   Read news ──→ python human_hint.py bullish "..."          │
│                              │                              │
│                              ▼                              │
│                         data/human_hint.json                │
│                         (expires after 48h)                 │
│                              │                              │
│                              ▼                              │
│                    Effect (AFTER policy):                    │
│                    bullish w≥0.3 → SELL blocked → HOLD       │
│                    bearish w≥0.3 → BUY blocked → HOLD        │
│                    pause         → ALL → HOLD                │
│                    neutral       → no change                 │
│                              │                              │
│                              ▼                              │
│   hint_evaluator.py ←── Was the hint correct?               │
└─────────────────────────────────────────────────────────────┘
```

### State Representation

| Dimension | Values | Description |
|-----------|--------|-------------|
| `pos` | LONG / PARTIAL / FLAT | BTC share (>70% / 20-70% / <20%) |
| `pc_bin` | up / flat / down | Price change (±0.5%) |
| `trend_bin` | uptrend / sideways / downtrend | MA short vs MA long (±1%) |
| `vol_bin` | low / mid / high | Volatility (<1% / 1-3% / >3%) |
| `e_short` / `e_long` | float | Price relative to MAs |
| `regime` | BULL_STRONG / BEAR_STRONG / NORMAL | Macro regime |
| `ac_phase` | peak / trough / transition / flat | AC oscillation position |
| `ac_amplitude_bin` | narrow / normal / wide | Oscillation magnitude |
| `near_zero` | true / false | Zero crossing zone |
| `energy_dir` | float | Energy direction vector |
| `daytrading_paused` | true / false | Downtrend pause gate |

### Chain Format (Experience Store)

```
pos:X,pc:X,trend:X,step:X,high:X,vol:X,ma_s:X,ma_l:X,
cz:X,sz:X,regime:X,ac:X,action:X
```

12 discretised dimensions ≈ 200,000 possible chains.

---

## Configuration

```python
# Kraken
KRAKEN_FEE_PCT = 0.0026           # 0.26% taker fee

# Portfolio
HODL_SHARE = 0.05                 # 5% HODL core (deprecated, replaced by investment limits)
TRADE_FRACTION_SMALL = 0.10       # 10% per small trade
TRADE_FRACTION_MEDIUM = 0.25      # 25% per medium trade

# MA parameters (hourly basis)
MA_SHORT_WINDOW = 24              # 24h (short-term oscillator, Axiom 2)
MA_LONG_WINDOW = 168              # 7d (DC component, Axiom 1)
VOLATILITY_WINDOW = 72            # 3d

# Training
TRAINING_WINDOW_LENGTH = 720      # 30 days
EXPERIENCE_DECAY_PER_PASS = 0.92  # Forgetting: 8% per pass (consolidated, Axiom 4)

# Symmetric thresholds V14 (Axiom 3)
MIN_EXPECTED_GAIN = 0.025         # 2.5% minimum expectation BUY
MIN_EXPECTED_DROP = 0.020         # 2.0% minimum expectation SELL

# Experience store
FINE_CHAIN_DIMS = 12              # 12 discretised dimensions
PATTERN_MATCH_THRESHOLD = 0.95    # Adaptive pattern match threshold

# Downtrend pause gate (V11.1+)
PAUSE_E_LONG_THRESHOLD = -0.05    # Pause when e_long < -5%
RESUME_E_LONG_THRESHOLD = -0.03   # Resume when e_long > -3%
RESUME_AC_PHASE = "trough"        # OR AC phase = trough
```

---

## Security Architecture

| Layer | Mechanism |
|-------|-----------|
| DRY_RUN | Default `true` — no accidental live trading |
| Order limits | Max 500 USD / 0.01 BTC per order |
| HODL core | 10% BTC never sold |
| Downtrend pause gate | Trading suspension in strong bear market |
| Balance controller | Double (policy + environment) |
| Cooldown | MEDIUM→SMALL with ≥3 consecutive trades |
| Human hint pause | Immediate trade block |
| Hint expiry | Automatically after 48h |

---

## Files

| File | Function |
|------|---------|
| `asset_config.py` | Generic asset registry (BTC, Gold, ETH, EURUSD) |
| `config.py` | Central configuration (cross-asset) |
| `main.py` | Multi-pass training (parallelisable, 1–4 workers) |
| `policy.py` | AC/DC policy with resonance gate (all 7 axioms) |
| `env.py` | Rule chain + downtrend pause gate |
| `experience.py` | Experience store per asset (offline/live/merged) |
| `live_signal.py` | Live generator with human hint + expectation |
| `human_hint.py` | Human hint CLI |
| `hint_evaluator.py` | Hint quality evaluation |
| `data_loader.py` | Multi-source pipeline (yfinance → Binance → CoinGecko) |
| `kraken_client.py` | Kraken REST API |
| `analyze_logs.py` | Live performance analysis |
| `dashboard.py` | Streamlit dashboard (6 tabs, per-asset view) |
| `v14_field_state_{asset}.json` | Adaptive field state per asset |

---

## CLI Reference

```bash
# Training
python main.py 20 500                  # 20×500 episodes
python resonance_analysis.py           # Market data + signals

# Live
python live_signal.py status           # Kraken + portfolio + hint
python live_signal.py expectation      # System expectation
python live_signal.py loop             # Continuous operation (dry run)
python live_signal.py merge            # Merge offline + live
python live_signal.py memory           # Memory status

# Human hint
python human_hint.py bullish "reason"  # Blocks SELL
python human_hint.py bearish "reason"  # Blocks BUY
python human_hint.py pause 12 "reason" # Blocks everything
python human_hint.py status            # Show hint
python human_hint.py clear             # Clear hint

# Analysis
python analyze_logs.py                 # Performance
python hint_evaluator.py               # Hint quality
```

---

## Version History

| Version | Core change | Performance |
|---------|-------------|-------------|
| V6 | MA heuristic + experience store | +35.04% (180d) |
| V7 | pc_bin filter | +35.61% (180d) |
| V10 | Energy direction vector (Axiom 5+6) | +37.03% (180d) |
| V11 | AC/DC decomposition (Axiom 1) | +42.89% (180d) |
| **V11.1** | **Pause gate, multi-cycle, human hint** | **+26.1% avg (4×6M)** |
| V12 | Energy vector engine MA'(t), MA''(t), MA'''(t) | Architecture rebuild |
| V13 | Multi-horizon experience (48h/14d/28d) | ~0.97 HODL equiv (plateau) |
| **V14** | **12 inconsistencies fixed, all 7 axioms, multi-asset** | **Learning curve >1.0 (target)** |
| **V14.2** | **Multi-asset (BTC/Gold/ETH/EURUSD), per-asset isolation, adaptive thresholds** | **Live operation (4 assets)** |

---

## Related Documents

- [Altcoin analysis: Why altcoins are not real markets](../../simulations/altcoin_analysis/resotrade_altcoin_analysis.md)
- [Energy sphere and AC/DC decomposition](../../docs/mathematics/energy_sphere.md)
- [Energy direction in real systems](../../docs/mathematics/energy_direction.md)
- [Resonance time coefficient τ*](../../docs/mathematics/tau_resonance_coefficient.md)
- [Resonance analysis in mass data](../cern/documentation.md)
- Dual resonance monetary system

---

*© Dominic-René Schu — Resonance Field Theory 2025–2026*

---

⬅️ [back to overview](../../../README.md)
