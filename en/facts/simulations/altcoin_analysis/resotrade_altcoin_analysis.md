# Resonance-Logical Analysis of Financial Markets: Altcoins as Amplified BTC Oscillations

## Analysis from the ResoTrade Development Context

> **Classification:** This analysis is part of the [ResoTrade](../../../concepts/ResoTrade/resotrade_trading_ki.md) application concept and does not serve as an independent RFT axiom evidence source. Primary axiom evidence comes from RFT-internal simulations (FLRW, Monte Carlo, double pendulum, resonance reactor).

*Dominic-René Schu, February 2026 — corrected March 2026*

---

## Summary

This analysis documents an empirical result that emerged unexpectedly during the development of a resonance-logical trading system (ResoTrade V11): **The altcoin market possesses no independent AC component relative to BTC.** Altcoins oscillate synchronously with Bitcoin — their price movement is a scaled echo, not an independent signal.

The AC/DC decomposition (V11) makes the reason visible: Altcoins have no independent AC component — their oscillation is a scaled echo of the BTC oscillation with leverage factor α. Without their own overtones there is no resonance, and without resonance there is no diversification gain in a multi-asset portfolio.

**Correction (March 2026):** The original analysis concluded from this that altcoins were "not tradeable". That was premature. An altcoin with α = 2.5 oscillates at the same frequency as BTC, but with 2.5 times the amplitude. These amplified oscillations are tradeable with the same resonance-logical methods — as an independent asset with adjusted thresholds, not as a portfolio addition alongside BTC.

The corrected core statement is:

> **Altcoins are not a diversification to BTC, but their amplified oscillations are tradeable with the same methods — as an independent asset, not as a portfolio addition.**

---

## 1. Context of Origin

The goal was not fundamental research, but a functioning trading bot. ResoTrade is a resonance-field-theoretical trading system that learns to trade price cycles through repeated offline simulation. The core mechanisms:

- **AC/DC decomposition** (Axiom 1): Price = DC (trend) + AC (tradeable oscillation)
- **Energy direction vector** (Axiom 5): `energy_dir = e_short - e_long`
- **Resonance coupling** (Axiom 6): Trades only at phase equality with the market
- Experience-based learning (Chain → Score, Decay)
- Dynamic satellite selection (Top-5 from 13 assets)
- Delayed trade evaluation (24h counterfactual vs. HOLD)

The scientific insight emerged emergently: when the multi-asset system (V10.2) was switched from equity satellites to altcoin satellites, performance collapsed — not due to technical errors, but due to a fundamental difference in signal structure.

### Performance Context: ResoTrade V11 (BTC-only)

| Metric | Value |
|--------|-------|
| Performance vs HODL | +42.89% |
| Episodes above HODL | 83.4% (rising with further training) |
| Learning progress | Positive and converging |
| Theoretical basis | Axioms 1, 2, 5, 6 of Resonance Field Theory |

---

## 2. Theoretical Framework

### 2.1 Universal Oscillation and AC/DC Decomposition (Axiom 1)

Axiom 1 of Resonance Field Theory postulates: **Every entity possesses a periodic oscillation ψ(x,t).** Applied to financial markets this means: every price can be decomposed into two components:

```
ψ_Price(t) = DC(t) + AC(t)
              ╰─────╯   ╰────╯
               Trend     tradeable
            (MA_LONG)    oscillation
```

The DC component is the fundamental tone — the long-term trend, which is not predictable. The AC component is the overtones — the oscillation around the trend, which is tradeable through phase detection.

**Decisive for multi-asset portfolios:** Only assets with an **independent AC component** generate diversification gain. If the AC component of an asset is merely a scaled echo of another asset, it contributes no additional information.

**Decisive for single-asset trading:** Even a scaled echo is tradeable if the amplitude is large enough. An altcoin with α = 2.5 reaches trading thresholds faster and more often than BTC itself.

### 2.2 Resonance Condition (Axiom 3)

Two systems enter resonance when their frequencies stand in a rational ratio:

```
f₁ / f₂ = n / m,    n, m ∈ ℤ⁺
```

Resonance generates energy transfer (Axiom 4):

```
E = π · ε · h · f
```

**The prerequisite for productive portfolio resonance is that the participating systems have different natural frequencies.** Two identically tuned strings generate no overtones — they oscillate synchronously. That means: no diversification gain. It does not mean: no signal.

### 2.3 Natural Frequencies in Financial Markets

Every genuine market is driven by an independent value-creation process that generates a characteristic natural frequency:

| Asset | Value creation basis | Natural frequency determined by |
|-------|---------------------|----------------------------------|
| **BTC** | Decentralised scarcity, Proof-of-Work | Halving cycle, network adoption, monetary policy |
| **MRK** (Merck) | Pharma pipeline | FDA approvals, patent cycles, demographics |
| **GLD** (Gold ETF) | Physical scarcity | Inflation, geopolitics, central bank policy |
| **AAPL** (Apple) | Product innovation | iPhone cycle, services growth, China risk |
| **USD** | Productivity, institutions | GDP, interest rate policy, fiscal deficit |

Each of these systems oscillates with its **own** frequency determined by fundamental value creation. The coupling between them is non-trivial and generates a rich overtone spectrum.

### 2.4 Altcoins as Amplified Oscillations

Altcoins have no independent value-creation basis that would be independent of BTC. Their AC component is not an independent overtone, but a scaled echo:

```
AC_Altcoin(t) ≈ α · AC_BTC(t) + η(t)
```

where α is a leverage factor (typically 1.5–4.0) and η(t) is noise. The natural frequency of the altcoin is identical to that of BTC — only the amplitude and noise differ.

**For portfolio diversification** this is equivalent to a linearly dependent system of equations:

```
┌          ┐   ┌    ┐      ┌                ┐
│  1    0  │   │ x₁  │      │ b₁             │
│          │ · │     │  =  │                │
│  α    0  │   │ x₂  │     │ α · b₁ + η      │
└          ┘   └     ┘     └                ┘
```

The determinant is zero. No information gain from adding the altcoin to the BTC portfolio.

**For single-asset trading** α is the decisive advantage:

| Property | BTC (α=1) | ETH (α≈1.8) | SOL (α≈3.0) |
|---|---|---|---|
| AC amplitude | ±5% | ±9% | ±15% |
| Sell threshold 4% reached | At 4% movement | At 2.2% BTC movement | At 1.3% BTC movement |
| Buy threshold -7% reached | At 7% drawdown | At 3.9% BTC drawdown | At 2.3% BTC drawdown |
| Trades per period | Few | More | Significantly more |
| Risk | Baseline | Elevated | High |

The amplified thresholds are automatically findable with the `threshold_optimizer` — the same control loop, different parameters.

---

## 3. Methodology

### 3.1 System: ResoTrade

The altcoin analysis was conducted with ResoTrade V10.2 (multi-asset). The BTC-only reference comes from V11 with AC/DC decomposition.

**V11 Core Architecture (BTC-only):**
- AC/DC decomposition: DC = MA_LONG (168h), AC = Price − DC
- Phase detection: peak / trough / transition / flat
- Energy direction vector: `energy_dir = e_short - e_long`
- Resonance gate: trades only at phase equality (K = K₀·cos(θ))
- Experience memory: Chain → Score with AC phase as dimension
- HODL core: 5% of holdings non-sellable

**V10.2 Multi-Asset Extension:**
- State representation: 12 dimensions (position, trend, MA, volatility, cash, allocation, relative strength, cluster)
- Hybrid learning: 30% rule + 70% experience × confidence
- Trade evaluation: delayed (24h), counterfactual against HOLD
- Dynamic satellite selection (Top-5 from 13 assets)

### 3.2 Experimental Setup

Three identical configurations, differing only in satellite assets:

| Configuration | Core | Satellites | Cluster |
|---------------|------|-----------|---------|
| **A: BTC + Equities** | BTC | NVDA, AAPL, TSLA, MSFT, AMZN, META, MCD, MRK, AZN, COIN, SPY, QQQ, GLD | Tech, Value, ETF |
| **B: BTC + Altcoins** | BTC | ETH, XRP, ADA, AVAX, LINK, AAVE, CRV, BONK, LTC, BCH | L1, DeFi, Sentiment, Store |
| **C: BTC only (V11)** | BTC | — | — |

### 3.3 Training Parameters

| Parameter | Value |
|-----------|-------|
| Episodes (Configuration A) | 20,000 |
| Episodes (Configuration B) | 200,000+ |
| Episodes (Configuration C, V11) | 10,000+ (converging) |
| Starting capital | 0.8 BTC + 23,305 USD (≈ 1.0 BTC equivalent) |
| Window length | 90 steps (hourly data) |
| Trade evaluation horizon | 24 steps |
| Max. active satellites | 5 per episode (A, B) |
| Decay factor | 0.80 per pass (V11), 0.9995 (V10.2) |
| Data source | yfinance (180 days, 1h OHLC) |

---

## 4. Results

### 4.1 Comparison Table

| Metric | BTC + Equities | BTC + Altcoins | BTC only (V11) |
|--------|---------------|---------------|----------------|
| **Ø BTC Equivalent** | **1.090** | 1.038 | **1.039** |
| **Median** | **1.077** | 1.033 | **1.041** |
| **Min / Max** | **1.020 / 1.282** | 0.927 / 1.173 | 0.926 / 1.131 |
| **Episodes above HODL** | **100%** | 86% | **83.4%** (rising) |
| **Draw rate** | 84% | **98.4%** | ~49% |
| **Success rate** | 14% | **0.9%** | ~29% |
| **Failure rate** | 2% | 0.7% | ~22% |
| **Learning progress** | **+0.001 (↑)** | -0.002 (↓) | **+0.010 (↑↑)** |
| **Performance vs HODL** | +9.0% | +3.8% | **+42.89%** |

### 4.2 Key Observation: Portfolio Effect vs. Single-Asset Trading

**Portfolio result:** BTC alone (V11, +42.89%) outperforms BTC + Altcoins (+3.8%) by a factor of 11. Altcoins not only generate no diversification gain — they **disturb** the BTC signal. The core cluster S:F ratio drops from 6.0:1 (configuration A) to 0.3:1 (configuration B).

**Implication for single-asset trading:** This result shows that altcoins *alongside BTC* provide no added value. It does not show that a ResoTrade system *on an altcoin chart alone* would not work. The amplified oscillations (α > 1) are potentially more profitable than BTC itself with adjusted thresholds — at correspondingly higher risk.

### 4.3 Trade Chain Analysis

**Configuration A (BTC + Equities):**

```
BTC_BUY_SMALL      S:F = 5.2:1    ← Profitable
TSLA_SELL_SMALL    S:F = ∞:1      ← Informative
MRK_SELL_SMALL     S:F = 2.8:1    ← Diversification gain
AMZN_SELL_SMALL    S:F = 8.0:1    ← Independent signal
```

**Configuration B (BTC + Altcoins):**

```
AVAX_SELL_SMALL    S:F = 0.9:1    ← Neutral (no signal alongside BTC)
BTC_SELL_SMALL     S:F = 0.0:1    ← Disturbed by altcoin noise
BCH_SELL_SMALL     S:F = ∞:1     ← Only because BCH chronically falls
CRV_SELL_SMALL     S:F = ∞:1     ← Draw-dominated, no signal
```

### 4.4 Cluster Balance

**Configuration A:**

| Cluster | S:F | Interpretation |
|---------|-----|----------------|
| crypto (BTC) | 6.0:1 | Strong natural mode |
| tech | 1.8:1 | Independent information |
| value | 8.0:1 | Highest diversification |
| etf | 0.8:1 | Lowest independence |

**Configuration B:**

| Cluster | S:F | Interpretation |
|---------|-----|----------------|
| core (BTC) | 0.3:1 | **Disturbed by altcoins** |
| l1 | 0.9:1 | No additional information |
| defi | ∞:1 | Draw-dominated |
| store | ∞:1 | Draw-dominated |
| sentiment | 0.0:1 | Pure noise |

### 4.5 Draw Rate as Resonance Indicator

The draw rate is the numerical fingerprint of missing natural frequencies in the portfolio context:

| Configuration | Draw rate | AC interpretation | Meaning |
|---------------|-----------|-------------------|---------|
| BTC only (V11) | ~49% | Independent AC, clear phases | System finds signal |
| BTC + Equities | 84% | Different ACs, partially correlated | System finds differences |
| BTC + Altcoins | **98.4%** | Identical AC, no phase difference | Every action ≈ HOLD *relative to BTC* |

**98.4% draw in portfolio context means:** The system cannot distinguish altcoin trades from doing nothing, *because the altcoin does the same as BTC*. On the altcoin chart alone (without BTC comparison) the draw rate would be lower — the oscillations are larger and generate clearer success/failure signals.

---

## 5. Resonance-Theoretical Interpretation

### 5.1 AC/DC Analysis of Asset Classes

```
Equity market — independent AC components:
  BTC  ──── DC₁ + AC₁(f₁)    f₁ = Crypto adoption, halving
  MRK  ──── DC₂ + AC₂(f₂)    f₂ = Pharma pipeline, FDA
  GLD  ──── DC₃ + AC₃(f₃)    f₃ = Inflation, geopolitics
  AAPL ──── DC₄ + AC₄(f₄)    f₄ = iPhone cycle, China

  → 4 independent AC components → rich overtone spectrum
  → Phase shifts between ACs → tradeable portfolio signal

Altcoin market — amplified AC components:
  BTC  ──── DC₁ + AC₁(f₁)              α = 1.0
  ETH  ──── α₁·DC₁ + α₁·AC₁(f₁) + η₁  α₁ ≈ 1.8
  ADA  ──── α₂·DC₁ + α₂·AC₁(f₁) + η₂  α₂ ≈ 2.5
  SOL  ──── α₃·DC₁ + α₃·AC₁(f₁) + η₃  α₃ ≈ 3.0

  → 1 independent AC frequency, different amplitudes
  → No phase shift → no portfolio diversification gain
  → Larger amplitudes → more trading opportunities per asset
```

### 5.2 Two Different Questions

Resonance Field Theory clearly distinguishes between two questions:

**Question 1: Does asset B generate diversification gain alongside asset A?**
Only if `AC_B(t)` is independent of `AC_A(t)`. For altcoins: No.

**Question 2: Is asset B tradeable on its own?**
Yes, if `|AC_B(t)|` is large enough to cross the thresholds. For altcoins with α > 1: Yes, with adjusted thresholds even more frequently than BTC.

The original analysis (February 2026) answered Question 1 correctly and incorrectly concluded from it to Question 2. The correction makes this distinction explicit.

### 5.3 The Leverage Factor α as a Trading Parameter

The leverage factor α determines the risk-return profile:

| α range | Examples | Thresholds | Trades/month | Risk |
|---|---|---|---|---|
| α ≈ 1.0 | BTC | Standard (V11.7) | ~12 | Baseline |
| α ≈ 1.5–2.0 | ETH, BNB | ~60% of BTC thresholds | ~20 | Moderately elevated |
| α ≈ 2.5–3.5 | SOL, ADA, AVAX | ~35% of BTC thresholds | ~30+ | High |
| α > 4.0 | BONK, Memecoins | Too volatile, noise dominates | — | Not tradeable |

The `threshold_optimizer` finds the optimal thresholds per asset automatically. The system adapts to α without α needing to be explicitly known.

### 5.4 BTC Dominance Cycle

The only moment at which altcoins appear to act independently of BTC is the BTC dominance cycle: BTC rises first, then capital rotates into altcoins. This rotation is:

1. **Temporally limited** (a few weeks per cycle)
2. **Not predictively usable** in the portfolio context (the transition is not stationary)
3. **Amplitude-dependent** (works only in bull markets)

The V10.2 system attempted to use this cycle as diversification over 200,000+ episodes. Result: negative learning progress (−0.002). The cycle is too unstable and too short for portfolio resonance — but it amplifies the AC oscillation of the individual altcoin, which favours single-asset trading.

---

## 6. Implication for Monetary Systems

This analysis supplements the dual resonance monetary system with an empirical dimension:

### 6.1 Bitcoin as the Only Cryptocurrency with an Independent Oscillation

BTC has an independent AC component because its value arises from a non-replicable process:

- **Proof-of-Work**: Energy binding as a physical value basis
- **Algorithmic scarcity**: 21 million, halving as the clock of the DC component
- **Network effect**: Metcalfe's law, self-reinforcing
- **Decentralisation**: No single impulse generator — genuine emergence

ResoTrade V11 confirms: BTC alone generates +42.89% above HODL through AC oscillation extraction. The oscillation is real, independent, and tradeable.

Altcoins do not replicate this natural frequency — they amplify it. That makes them worthless as a portfolio addition, but potentially profitable as a single instrument.

### 6.2 Equities and Fiat Currencies as Genuine Resonance Partners

Equities represent real value creation: products, patents, employees, cash flows. Every company is an independent resonator with its own frequency and its own AC component. Fiat currencies are driven by the productivity of entire economies.

These assets can enter genuine portfolio resonance with BTC because they have independent natural frequencies. The coupling is non-trivial and generates tradeable signal — confirmed by the equity configuration (+9.0% vs HODL).

### 6.3 Consequence for the Dual Monetary System

The dual resonance monetary system (BTC external, national resonance coin internal) receives an empirical support through this analysis:

- **BTC as external resonance currency works**, because BTC has an independent natural frequency and AC component
- **Altcoins are unsuitable as reserve currency**, because they carry no independent information (correct finding)
- **Altcoins are usable as trading instruments**, because their amplified oscillations are tradeable with adjusted thresholds (corrected finding)
- **National currencies (backed by GDP) complement BTC**, because they have independent natural frequencies

---

## 7. Why the Distinction Matters

### 7.1 The Narrative Problem

The original analysis stated: *"Altcoins are not an independent market."* That is resonance-theoretically correct in the sense of natural frequency — but it was read as *"Altcoins are a scam"*, which goes beyond the data.

The corrected formulation distinguishes more precisely:

| Statement | Status |
|-----------|--------|
| Altcoins have no own natural frequency relative to BTC | ✓ Empirically confirmed |
| Altcoins provide no diversification alongside BTC | ✓ Empirically confirmed |
| Altcoins are not tradeable | ✗ Premature — amplitude ≠ information |
| Altcoins as single instrument with α-adjusted thresholds | ○ Hypothesis, yet to be validated |

### 7.2 What Still Needs to be Validated

The hypothesis that a ResoTrade system works profitably on an altcoin chart (without BTC) is theoretically sound but empirically still open. The test would be:

1. Create `AssetConfig` for ETH (narrower thresholds, higher volatility)
2. Run `threshold_optimizer` on ETH data
3. Train exclusively on ETH chart
4. Compare performance with BTC system (normalised for volatility)

The architecture (V11.7) already supports this — it is a configuration change, not a system rebuild.

### 7.3 The Time Dimension

Scams expose themselves over time because noise does not accumulate. In 100 episodes a random altcoin rotation can appear profitable. In 200,000 episodes the portfolio added value converges to zero.

Genuine markets, on the other hand, stabilise: the BTC-only configuration (V11) shows a settling behaviour over 10,000+ episodes — damped oscillation with rising trend, converging towards +42.89% above HODL. That is the behaviour of a resonant system.

The amplitude hypothesis for altcoin single-asset trading would need to show the same settling behaviour — with higher volatility of convergence, but a positive trend.

---

## 8. Methodology Transparency

### 8.1 Limitations

- Data scope: ~4,300 hourly data points (≈ 180 days) — limited to the available yfinance period
- No consideration of order book depth and slippage
- Simulation environment, no live trades (live validation pending)
- Altcoin selection limited to Top-10 by Kraken liquidity
- SUI, UNI, PEPE had 0 data points and were excluded (11 instead of 14 assets)
- **Altcoin single-asset trading (without BTC) was not tested** — the portfolio analysis is not transferable to single-asset trading

### 8.2 Reproducibility

The results are reproducible:

- **Multi-asset (V10.2):** Configuration differs only in `asset_registry.py` (equity registry vs. crypto registry). All other parameters identical.
- **BTC-only (V11):** `env.py` + `policy.py` with AC/DC decomposition. Training with `python main.py 20 500`.

### 8.3 Strength of Evidence

| Criterion | Assessment |
|-----------|------------|
| Sample size | 200,000+ episodes (multi-asset), 10,000+ (BTC-only) |
| Control group | Yes (BTC+equities, BTC-only, BTC+altcoins) |
| Learning progress | Negative for altcoins in portfolio, positive for equities and BTC-only |
| Draw rate difference | 98.4% vs. 84% vs. 49% (strong) |
| S:F core cluster | 0.3:1 vs. 6.0:1 (strong) |
| Min value | 0.927 vs. 1.020 (strong) |
| AC/DC consistency | V11 confirms independent BTC oscillation empirically |
| Altcoin single-asset trading | **Not tested** — open hypothesis |

---

## 9. Conclusion

### 9.1 Confirmed Finding

**The altcoin market provides no diversification to BTC.** Altcoins are linearly dependent derivatives of Bitcoin with identical natural frequency. In a multi-asset portfolio alongside BTC they disturb the signal and reduce performance (from +42.89% to +3.8%).

### 9.2 Corrected Finding

**Altcoins are potentially tradeable as a single instrument.** Their amplified oscillations (α > 1) generate larger AC excursions that cross trading thresholds more frequently and more clearly with adjusted thresholds. The `threshold_optimizer` (V11.7) can find these thresholds per asset automatically.

### 9.3 Generalisation

This result concerns two different questions:

> **Portfolio diversification requires different natural frequencies.** Without an independent AC component no phase shift, without a phase shift no information gain from the second asset.

> **Single-asset trading requires sufficient amplitude.** A scaled echo with α > 1 is tradeable — it oscillates more strongly, not differently. The methods are identical, the parameters change.

---

## References

- Schu, D.-R. (2025). *Resonance Field Theory: Axiomatic Foundation, Coupling Operator, and Mathematical Consequences.*
- Schu, D.-R. (2026). *Energy Sphere and AC/DC Decomposition.* [GitHub](https://github.com/DominicReneSchu/public/blob/main/de/fakten/docs/mathematik/energiekugel.md)
- Schu, D.-R. (2026). *ResoTrade V15 — Resonance Field Theoretical BTC-AI with AC/DC Decomposition.* (System documentation)

---

*© Dominic-René Schu, 2026 — All rights reserved.*

---

⬅️ [Back to Overview](../../../README.md#simulations)
