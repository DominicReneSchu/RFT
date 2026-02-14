# Resonance-Logical Analysis of Financial Markets: Why Altcoins Are Not Real Markets

## Empirical Evidence Through Algorithmic Trading with Resonance Field Theory

*Dominic Schu, February 2026*

---

## Abstract

This analysis documents an empirical result that emerged unexpectedly during the development of a resonance-logical trading system (ResoTrade V10.2): **The altcoin market possesses no independent eigenfrequencies and is therefore, in resonance-theoretical terms, not a real market.** A learning multi-asset trading system trained over 200,000 episodes achieved a mean BTC equivalent of 1.090 with 100% of episodes above HODL using stock satellites (BTC + 13 stocks/ETFs) — but only 1.038 with 86% above HODL using altcoin satellites (BTC + 10 altcoins), with negative learning progress and a draw rate of 98.4%.

The result is the numerical equivalent of two linearly dependent equations with two unknowns: extensive computation, no information gain. Resonance field theory provides the formal framework to explain and generalize this phenomenon.

---

## 1. Context of Origin

The goal was not fundamental research, but a functional trading bot. ResoTrade V10.2 is a multi-asset trading system that optimizes BTC accumulation beyond pure HODL. It employs:

- Resonance analysis (FFT, amplitudes, MA crossover)
- Experience-based learning (chain → score, decay)
- Dynamic satellite selection (top 5 from 13 assets)
- Delayed trade evaluation (24h counterfactual vs. HOLD)
- Cluster system (asset groups with varying BTC correlation)

The scientific insight emerged emergently: When the system was switched from stock satellites to altcoin satellites, performance collapsed — not due to technical errors, but due to the structure of the markets themselves.

---

## 2. Theoretical Framework

### 2.1 Resonance Condition (Axiom 3)

Two systems enter into resonance when their frequencies are in a rational ratio:

$$
\frac{f_1}{f_2} = \frac{n}{m}, \quad n, m \in \mathbb{Z}^+
$$

Resonance generates energy transfer (Axiom 4):

$$
E = \pi \cdot \varepsilon \cdot h \cdot f
$$

**A prerequisite for productive resonance is that the participating systems possess different eigenfrequencies.** Two identically tuned strings produce no overtones — they oscillate in sync. Constructive interference that generates new information arises only from difference.

### 2.2 Eigenfrequencies in Financial Markets

Every real market is driven by an independent value creation process that generates a characteristic eigenfrequency:

| Asset | Value Creation Basis | Eigenfrequency Determined By |
|-------|---------------------|------------------------------|
| **BTC** | Decentralized scarcity, proof-of-work | Halving cycle, network adoption, monetary policy |
| **MRK** (Merck) | Pharma pipeline | FDA approvals, patent cycles, demography |
| **GLD** (Gold ETF) | Physical scarcity | Inflation, geopolitics, central bank policy |
| **AAPL** (Apple) | Product innovation | iPhone cycle, services growth, China risk |
| **USD** | Productivity, institutions | GDP, interest rate policy, fiscal deficit |

Each of these systems oscillates at its **own** frequency, determined by fundamental value creation. The coupling between them is non-trivial and produces a rich overtone spectrum.

### 2.3 Altcoins as Derived Oscillations

Altcoins possess no independent value creation basis that is independent of BTC:

$$
\psi_{\text{Altcoin}}(t) \approx \alpha \cdot \psi_{\text{BTC}}(t) + \eta(t)
$$

where $\alpha$ is a leverage factor and $\eta(t)$ is noise. The eigenfrequency of the altcoin is identical to that of BTC — only amplitude and noise differ.

This is mathematically equivalent to a **linearly dependent system of equations**:

$$
\begin{pmatrix} 1 & 0 \\ \alpha & 0 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} = \begin{pmatrix} b_1 \\ \alpha \cdot b_1 + \eta \end{pmatrix}
$$

The determinant is zero. The system is underdetermined. **No unique solution exists — no tradeable information.**

---

## 3. Methodology

### 3.1 System: ResoTrade V10.2

- Multi-asset trading with hybrid learning approach (30% rule + 70% experience × confidence)
- State representation: 12 dimensions (position, trend, MA, volatility, cash, allocation, relative strength, cluster)
- Trade evaluation: delayed (24h), counterfactual against HOLD
- HODL core: 60% of BTC holdings unsellable
- Protection rules: ATH, trend, MA, allocation limits

### 3.2 Experimental Setup

Three identical configurations, differing only in satellite assets:

| Configuration | Core | Satellites | Clusters |
|---------------|------|-----------|----------|
| **A: BTC + Stocks** | BTC | NVDA, AAPL, TSLA, MSFT, AMZN, META, MCD, MRK, AZN, COIN, SPY, QQQ, GLD | Tech, Value, ETF |
| **B: BTC + Altcoins** | BTC | ETH, XRP, ADA, AVAX, LINK, AAVE, CRV, BONK, LTC, BCH | L1, DeFi, Sentiment, Store |
| **C: BTC only** | BTC | — | — |

### 3.3 Training Parameters

| Parameter | Value |
|-----------|-------|
| Episodes (Configuration A) | 20,000 |
| Episodes (Configuration B) | 200,000+ |
| Starting capital | 0.8 BTC + 23,305 USD (≈ 1.0 BTC equivalent) |
| Window length | 90 steps (hourly data) |
| Trade evaluation horizon | 24 steps |
| Max active satellites | 5 per episode |
| Decay factor | 0.9995 |
| Data source | yfinance (180 days, 1h OHLC) |

---

## 4. Results

### 4.1 Comparison Table

| Metric | BTC + Stocks | BTC + Altcoins | BTC only (V9) |
|--------|-------------|---------------|---------------|
| **Mean BTC Equivalent** | **1.090** | 1.038 | 1.144 |
| **Median** | **1.077** | 1.033 | — |
| **Min / Max** | **1.020 / 1.282** | 0.927 / 1.173 | — |
| **Episodes above HODL** | **100%** | 86% | 100% |
| **Draw Rate** | 84% | **98.4%** | ~80% |
| **Success Rate** | 14% | **0.9%** | ~18% |
| **Failure Rate** | 2% | 0.7% | ~2% |
| **Learning Progress** | **+0.001 (↑)** | -0.002 (↓) | +0.003 (↑) |
| **BTC_BUY S:F** | **5.2:1** | ∞:1 (7:0) | 4.2:1 |
| **BTC_SELL S:F** | 2.2:1 | **0.0:1** (0:21) | — |

### 4.2 Trade Chain Analysis

**Configuration A (BTC + Stocks):**

```
BTC_BUY_SMALL      S:F = 5.2:1    ← Profitable
TSLA_SELL_SMALL    S:F = ∞:1      ← Informative
MRK_SELL_SMALL     S:F = 2.8:1    ← Diversification gain
AMZN_SELL_SMALL    S:F = 8.0:1    ← Independent signal
```

**Configuration B (BTC + Altcoins):**

```
AVAX_SELL_SMALL    S:F = 0.9:1    ← Neutral (no signal)
BTC_SELL_SMALL     S:F = 0.0:1    ← Catastrophic
BCH_SELL_SMALL     S:F = ∞:1     ← Only because BCH chronically falls
CRV_SELL_SMALL     S:F = ∞:1     ← Draw-dominated, no signal
```

### 4.3 Cluster Balance

**Configuration A:**

| Cluster | S:F | Interpretation |
|---------|-----|----------------|
| crypto (BTC) | 6.0:1 | Strong eigenmode |
| tech | 1.8:1 | Independent information |
| value | 8.0:1 | Highest diversification |
| etf | 0.8:1 | Lowest independence |

**Configuration B:**

| Cluster | S:F | Interpretation |
|---------|-----|----------------|
| core (BTC) | 0.3:1 | **Disrupted by altcoins** |
| l1 | 0.9:1 | No usable information |
| defi | ∞:1 | Draw-dominated |
| store | ∞:1 | Draw-dominated |
| sentiment | 0.0:1 | Pure noise |

### 4.4 Core Observation: Draw Rate as Resonance Indicator

The draw rate is the numerical fingerprint of missing eigenfrequencies:

| Configuration | Draw Rate | Meaning |
|---------------|-----------|---------|
| BTC + Stocks | 84% | System finds tradeable differences |
| BTC + Altcoins | **98.4%** | Nearly every action is equivalent to HOLD |
| BTC only | ~80% | BTC alone has more signal than BTC + altcoins |

**98.4% draw means: The system cannot distinguish altcoin movements from noise.** Every buy and sell of an altcoin is nearly identical to doing nothing, because the altcoin moves synchronously with BTC. The 1.6% non-draw is statistical noise, not signal.

---

## 5. Resonance-Theoretical Interpretation

### 5.1 Eigenfrequency Analysis

```
Stock Market:
  BTC  ────── f₁ (crypto adoption, halving)
  MRK  ────── f₂ (pharma pipeline, FDA)
  GLD  ────── f₃ (inflation, geopolitics)
  AAPL ────── f₄ (iPhone cycle, China)
  
  → 4 independent equations, 4 unknowns → solvable
  → Rich overtone spectrum → Tradeable signal

Altcoin Market:
  BTC  ────── f₁
  ETH  ────── α₁·f₁ + η₁
  ADA  ────── α₂·f₁ + η₂
  AVAX ────── α₃·f₁ + η₃
  
  → 1 independent equation, n unknowns → underdetermined
  → No overtone spectrum → No signal, only echo
```

### 5.2 Resonance Condition and Information Content

Axiom 6 of resonance field theory states: **Information is structured resonance.** Information exchange occurs exclusively through coherent resonance paths — through synchronization of phase and frequency.

Between BTC and stocks, such paths exist: When BTC falls and MRK rises, that is a coherent signal (capital flows from risk-on to defensive). The system can learn and trade this phase shift.

Between BTC and altcoins, these paths do not exist: When BTC falls, altcoins fall too. When BTC rises, altcoins rise too. There is no phase shift, no coherent difference, no information content. The system learns nothing because there is nothing to learn.

### 5.3 BTC Dominance Cycle: Apparent Independence

The only moment when altcoins appear to act independently of BTC is the BTC dominance cycle: BTC rises first, then capital rotates into altcoins. But this rotation is:

1. **Temporally limited** (a few weeks per cycle)
2. **Not predictively usable** (the transition is non-stationary)
3. **Amplitude-dependent** (works only in bull markets)

The system attempted to learn this cycle over 200,000 episodes. Result: negative learning progress (-0.002). The cycle is too unstable and too short to function as an independent frequency.

---

## 6. Implications for Monetary Systems

This analysis supplements the [dual resonance money system](../../docs/society/dual_resonance_money_system.md) with an empirical dimension:

### 6.1 Bitcoin as the Only Cryptocurrency with Intrinsic Value

BTC has an independent eigenfrequency because its value arises through a non-replicable process:

- **Proof-of-Work**: Energy binding as physical value basis
- **Algorithmic scarcity**: 21 million, halving as pacemaker
- **Network effect**: Metcalfe's law, self-reinforcing
- **Decentralization**: No single impulse setter

Altcoins do not replicate these properties — they are placed upon the BTC resonance floor and absorb a portion of the price amplitude without delivering independent information.

### 6.2 Stocks and Fiat Currencies as Real Resonance Partners

Stocks represent real value creation: products, patents, employees, cash flows. Every company is an independent resonator with its own frequency. Fiat currencies reflect the productivity and institutional stability of a state — their value is backed by GDP.

These assets can enter into real resonance with BTC because they possess independent eigenfrequencies. The coupling is non-trivial and generates tradeable signal.

### 6.3 Consequence for the Dual Money System

The dual resonance money system (BTC external, national resonance coin internal) receives empirical support through this analysis:

- **BTC as external resonance currency works** because BTC has an independent eigenfrequency
- **Altcoins are unsuitable as reserve currencies** because they carry no independent information
- **National currencies (backed by GDP) complement BTC** because they possess independent eigenfrequencies

---

## 7. Why Scam Works — and Why It Exposes Itself

### 7.1 The Business Model

Altcoins create the **illusion** of independent markets. They have their own tickers, their own charts, their own narratives. Price movement suggests independence — especially during the brief phases of altcoin season, when capital rotates from BTC into altcoins.

This illusion is sufficient to:
- Generate trading fees (exchanges profit regardless of direction)
- Fuel speculation (leverage on leverage)
- Sell narratives ("the next Ethereum killer chain")

### 7.2 Why the System Exposes It

A resonance-logical trading system is immune to narratives. It evaluates only: **Did this trade perform better than doing nothing after 24 hours?** When the answer across 200,000 episodes is "identical" in 98.4% of cases, the conclusion is compelling: **There is no signal.**

What people intuitively recognize ("altcoins feel like a scam") but find difficult to formalize, resonance field theory makes mathematically tangible:

> **A system without its own eigenfrequency cannot generate independent resonance. Without resonance, no information exchange. Without information, no market value.**

### 7.3 The Time Dimension

Scam exposes itself over time because noise does not accumulate. Over 100 episodes, a random altcoin rotation may appear profitable. Over 200,000 episodes, the expected value converges to zero (or to fee costs). The draw rate rises asymptotically toward 100%.

Real markets, by contrast, stabilize: The stock configuration showed a stable mean of 1.090 over 20,000 episodes with positive learning progress. The signal does not disappear — it strengthens.

---

## 8. Methodological Transparency

### 8.1 Limitations

- Data scope: 4,159 hourly data points (≈ 173 days) — limited to the available yfinance timeframe
- No consideration of order book depth and slippage
- Simulation environment, no live trades
- Altcoin selection limited to top 10 by Kraken liquidity
- SUI, UNI, PEPE had 0 data points and were excluded (11 instead of 14 assets)

### 8.2 Reproducibility

Results are reproducible with the ResoTrade V10.2 system. Configuration differs only in `asset_registry.py`:

- Configuration A: xStocks registry (13 stocks/ETFs)
- Configuration B: Crypto registry (10 altcoins)

All other parameters (policy, evaluation, protection rules, decay) are identical.

### 8.3 Strength of Evidence

| Criterion | Assessment |
|-----------|------------|
| Sample size | 200,000+ episodes (strong) |
| Control group | Yes (BTC+stocks, BTC-only) |
| Learning progress | Negative for altcoins, positive for stocks (strong) |
| Draw rate difference | 98.4% vs. 84% (14pp, strong) |
| S:F core cluster | 0.3:1 vs. 6.0:1 (strong) |
| Min value | 0.927 vs. 1.020 (strong) |

---

## 9. Conclusion

### 9.1 Core Statement

**The altcoin market is, in resonance-theoretical terms, not an independent market.** Altcoins are linearly dependent derivatives of Bitcoin that possess no independent eigenfrequencies and therefore generate no tradeable information content. A learning trading system cannot extract a stable advantage from BTC-altcoin rotation over 200,000 episodes.

### 9.2 Generalization

This result is not limited to altcoins. It applies to any asset class whose price movement can be entirely explained by another asset:

> **Resonance arises only between systems with different eigenfrequencies. Without eigenfrequency, no resonance; without resonance, no information exchange; without information, no market.**

### 9.3 Resonance Rule

Group membership is systemically invariant. An altcoin belongs to the group "BTC derivative" — regardless of what it calls itself, what narrative it carries, or what technological innovation it promises. Resonance field theory makes this membership visible where classical financial analysis fails.

---

## References

- Schu, D. (2025). *Resonance Field Theory: Axiomatic Foundation, Coupling Operator, and Mathematical Consequences.*
- Schu, D. (2025). *Dual Resonance Money System.*
- Schu, D. (2026). *ResoTrade V10.2 — Multi-Asset Resonance AI with Kraken Live Trading.* (System documentation)

---

*© Dominic Schu, 2026 — All rights reserved.*

---

⬅️ [back to overview](../../README.en.md)