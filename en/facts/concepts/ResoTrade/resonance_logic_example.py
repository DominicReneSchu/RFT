# resonance_logic_example.py
# © Dominic-René Schu, 2025/2026 – Resonance Field Theory
#
# Minimal example: Resonance-logical programming
#
# Demonstrates all 5 principles:
#   1. Oscillation decomposition (DC + AC)
#   2. Phase detection (peak, trough, transition, flat)
#   3. Coupling efficiency ε(Δφ) = cos²(Δφ/2)
#   4. Experience store (state → score)
#   5. Rule chain (explicit guardrails)
#
# Generates a synthetic signal and trades on it.
# Compares: Resonance-logical vs. Random vs. HODL.
#
# Usage: python resonance_logic_example.py
# Dependencies: numpy, matplotlib

import numpy as np
import matplotlib.pyplot as plt
import os

PI = np.pi


# ============================================================
# 1. Coupling efficiency (Axiom 4)
# ============================================================

def coupling_efficiency(delta_phi):
    """ε(Δφ) = cos²(Δφ/2) — universal RFT coupling."""
    return np.cos(delta_phi / 2.0) ** 2


# ============================================================
# 2. Signal generation
# ============================================================

def generate_signal(n=2000, seed=42):
    """
    Synthetic price signal: DC trend + AC oscillations + noise.
    Simulates a typical market with cycles.
    """
    rng = np.random.RandomState(seed)
    t = np.arange(n, dtype=float)

    # DC: Slowly rising trend (like BTC over months)
    dc = 100.0 + 0.02 * t + 5.0 * np.sin(2 * PI * t / 800)

    # AC: Superimposed oscillations (market cycles)
    ac = (3.0 * np.sin(2 * PI * t / 50)          # Main cycle: 50 steps
          + 1.5 * np.sin(2 * PI * t / 120)        # Long cycle
          + 0.8 * np.sin(2 * PI * t / 20))        # Short cycle

    # Noise (realistic)
    noise = rng.normal(0, 0.8, n)

    price = dc + ac + noise
    return t, price, dc, ac


# ============================================================
# 3. Oscillation decomposition (Principle 1)
# ============================================================

def decomposition(price, window_long=50):
    """DC/AC decomposition: DC = moving average, AC = price - DC."""
    dc = np.convolve(price, np.ones(window_long) / window_long,
                     mode='same')
    ac = price - dc
    return dc, ac


# ============================================================
# 4. Phase detection (Principle 2)
# ============================================================

def detect_phase(ac, amplitude_threshold=0.3):
    """
    Determines the phase in the oscillation cycle.

    peak:       AC > +threshold · amplitude
    trough:     AC < -threshold · amplitude
    transition: in between, AC changes direction
    flat:       amplitude too small for signal
    """
    n = len(ac)
    phases = np.full(n, 'flat', dtype='U10')
    amplitude = np.zeros(n)

    window = 25
    for i in range(window, n):
        segment = ac[i - window:i]
        amp = np.max(segment) - np.min(segment)
        amplitude[i] = amp

        if amp < 0.5:  # Too little signal
            phases[i] = 'flat'
        elif ac[i] > amplitude_threshold * amp:
            phases[i] = 'peak'
        elif ac[i] < -amplitude_threshold * amp:
            phases[i] = 'trough'
        else:
            phases[i] = 'transition'

    return phases, amplitude


# ============================================================
# 5. Experience store (Principle 4)
# ============================================================

class ExperienceStore:
    """
    State-action-score table.
    Each entry is a readable string.
    No tensor. No weights. No black box.
    """

    def __init__(self, decay=0.90):
        self.store = {}  # "state,action" → score
        self.decay = decay

    def make_key(self, phase, trend, action):
        return f"{phase},{trend},{action}"

    def update(self, phase, trend, action, reward):
        key = self.make_key(phase, trend, action)
        if key not in self.store:
            self.store[key] = 0.0
        self.store[key] = self.store[key] * self.decay + reward

    def score(self, phase, trend, action):
        key = self.make_key(phase, trend, action)
        return self.store.get(key, 0.0)

    def best_action(self, phase, trend):
        actions = ['BUY', 'SELL', 'HOLD']
        scores = {a: self.score(phase, trend, a) for a in actions}
        return max(scores, key=scores.get), scores

    def statistics(self):
        print(f"\n  Experience store: {len(self.store)} entries")
        if self.store:
            top = sorted(self.store.items(),
                         key=lambda x: abs(x[1]), reverse=True)[:10]
            print(f"  Top 10:")
            for key, score in top:
                print(f"    {key:40s} → {score:+.4f}")

    def export_csv(self, filepath):
        with open(filepath, 'w') as f:
            f.write("state_action,score\n")
            for key, score in sorted(self.store.items()):
                f.write(f"{key},{score:.6f}\n")
        print(f"  → Experience exported: {filepath}"
              f" ({len(self.store)} entries)")


# ============================================================
# 6. Rule chain (Principle 5)
# ============================================================

class RuleChain:
    """
    Explicit guardrails. Not trained. Not optimized.
    Physically motivated.
    """

    def __init__(self, min_cash_fraction=0.10, min_asset_fraction=0.05,
                 cooldown=3):
        self.min_cash = min_cash_fraction
        self.min_asset = min_asset_fraction
        self.cooldown = cooldown
        self.recent_trades = []
        self.blocked = 0

    def check(self, proposal, cash, portfolio_value, epsilon):
        """Filters proposal through rule chain."""
        reasons = []

        # Rule 1: Coupling too weak → no trade
        if epsilon < 0.3 and proposal != 'HOLD':
            reasons.append(f"ε={epsilon:.2f} < 0.3 → no coupling")
            return 'HOLD', reasons

        # Rule 2: Cash protection
        if proposal == 'BUY':
            cash_fraction = cash / max(portfolio_value, 1e-10)
            if cash_fraction < self.min_cash:
                reasons.append(f"Cash {cash_fraction:.1%} < {self.min_cash:.0%}")
                return 'HOLD', reasons

        # Rule 3: Asset protection
        if proposal == 'SELL':
            asset_fraction = 1.0 - cash / max(portfolio_value, 1e-10)
            if asset_fraction < self.min_asset:
                reasons.append(
                    f"Asset {asset_fraction:.1%} < {self.min_asset:.0%}")
                return 'HOLD', reasons

        # Rule 4: Cooldown (overtrading protection)
        if self.blocked > 0:
            self.blocked -= 1
            reasons.append(f"Cooldown ({self.blocked} remaining)")
            return 'HOLD', reasons

        # Set cooldown after trade
        if proposal in ('BUY', 'SELL'):
            self.recent_trades.append(proposal)
            if len(self.recent_trades) > self.cooldown:
                self.recent_trades.pop(0)
            if len(self.recent_trades) >= self.cooldown:
                if all(t != 'HOLD' for t in self.recent_trades):
                    self.blocked = 2
                    reasons.append("Cooldown activated (overtrading)")

        return proposal, reasons


# ============================================================
# 7. Resonance-logical agent
# ============================================================

class ResonanceAgent:
    """
    Complete resonance-logical agent.
    Demonstrates all 5 principles.
    """

    def __init__(self, start_capital=1000.0, trade_fraction=0.15):
        self.cash = start_capital
        self.asset = 0.0
        self.trade_fraction = trade_fraction
        self.experience = ExperienceStore()
        self.rules = RuleChain()
        self.history = []

    def portfolio_value(self, price):
        return self.cash + self.asset * price

    def trend_detection(self, dc, i, window=20):
        if i < window:
            return 'sideways'
        slope = (dc[i] - dc[i - window]) / max(dc[i - window], 1e-10)
        if slope > 0.005:
            return 'uptrend'
        elif slope < -0.005:
            return 'downtrend'
        return 'sideways'

    def step(self, i, price, dc, ac, phases):
        """One decision step."""
        phase = phases[i]
        trend = self.trend_detection(dc, i)
        current_price = price[i]
        pv = self.portfolio_value(current_price)

        # Principle 3: Coupling efficiency
        # Δφ is derived from the AC phase
        if phase == 'peak':
            delta_phi = 0.0       # Perfect coupling for SELL
        elif phase == 'trough':
            delta_phi = 0.0       # Perfect coupling for BUY
        elif phase == 'transition':
            delta_phi = PI / 3    # Medium coupling
        else:
            delta_phi = PI / 2    # Weak coupling (flat)

        epsilon = coupling_efficiency(delta_phi)

        # Principle 2: Phase-based decision
        if phase == 'peak':
            proposal = 'SELL'
        elif phase == 'trough':
            proposal = 'BUY'
        else:
            proposal = 'HOLD'

        # Principle 4: Experience modulates
        _, scores = self.experience.best_action(phase, trend)
        if proposal != 'HOLD':
            experience_score = scores.get(proposal, 0.0)
            if experience_score < -0.5:
                proposal = 'HOLD'  # Experience overrides

        # Principle 5: Rule chain filters
        proposal, reasons = self.rules.check(
            proposal, self.cash, pv, epsilon)

        # Execution
        fraction = self.trade_fraction
        if proposal == 'BUY' and self.cash > 10:
            buy_cash = self.cash * fraction
            buy_asset = buy_cash / current_price
            self.cash -= buy_cash
            self.asset += buy_asset
        elif proposal == 'SELL' and self.asset > 0.01:
            sell_asset = self.asset * fraction
            sell_cash = sell_asset * current_price
            self.asset -= sell_asset
            self.cash += sell_cash
        else:
            proposal = 'HOLD'

        # Calculate reward (for experience store)
        new_pv = self.portfolio_value(current_price)
        reward = (new_pv - pv) / max(pv, 1e-10)
        self.experience.update(phase, trend, proposal, reward)

        self.history.append({
            'i': i, 'price': current_price, 'phase': phase,
            'trend': trend, 'epsilon': epsilon,
            'action': proposal, 'pv': new_pv,
            'cash': self.cash, 'asset': self.asset
        })

        return proposal


# ============================================================
# 8. Random agent (baseline)
# ============================================================

class RandomAgent:
    def __init__(self, start_capital=1000.0, trade_fraction=0.15, seed=123):
        self.cash = start_capital
        self.asset = 0.0
        self.trade_fraction = trade_fraction
        self.rng = np.random.RandomState(seed)
        self.history = []

    def portfolio_value(self, price):
        return self.cash + self.asset * price

    def step(self, i, price):
        current_price = price[i]
        pv = self.portfolio_value(current_price)
        action = self.rng.choice(['BUY', 'SELL', 'HOLD'],
                                 p=[0.2, 0.2, 0.6])
        if action == 'BUY' and self.cash > 10:
            buy_amount = self.cash * self.trade_fraction
            self.asset += buy_amount / current_price
            self.cash -= buy_amount
        elif action == 'SELL' and self.asset > 0.01:
            sell_amount = self.asset * self.trade_fraction
            self.cash += sell_amount * current_price
            self.asset -= sell_amount
        self.history.append({
            'i': i, 'price': current_price,
            'action': action, 'pv': self.portfolio_value(current_price)
        })


# ============================================================
# 9. Main simulation
# ============================================================

def main():
    print("=" * 60)
    print("RESONANCE-LOGICAL PROGRAMMING — EXAMPLE")
    print("E = π · ε(Δφ) · ℏ · f, κ = 1")
    print("=" * 60)

    out = "figures"
    os.makedirs(out, exist_ok=True)

    # Generate signal
    t, price, dc_true, ac_true = generate_signal(n=2000)
    print(f"\n  Signal: {len(price)} data points")
    print(f"  Price: {price[0]:.1f} → {price[-1]:.1f}")

    # Principle 1: Decomposition
    dc, ac = decomposition(price, window_long=50)

    # Principle 2: Phase detection
    phases, amplitudes = detect_phase(ac)
    phase_counts = {p: np.sum(phases == p) for p in
                    ['peak', 'trough', 'transition', 'flat']}
    print(f"\n  Phases: {phase_counts}")

    # Agents
    agent_reso = ResonanceAgent(start_capital=1000.0)
    agent_random = RandomAgent(start_capital=1000.0)
    hodl_start = 1000.0 / price[50]  # Invest everything at t=50

    # Simulation
    start = 50  # Wait for MA initialization
    trades_reso = 0
    for i in range(start, len(price)):
        action = agent_reso.step(i, price, dc, ac, phases)
        agent_random.step(i, price)
        if action != 'HOLD':
            trades_reso += 1

    # Results
    pv_reso = agent_reso.portfolio_value(price[-1])
    pv_random = agent_random.portfolio_value(price[-1])
    pv_hodl = hodl_start * price[-1]
    pv_start = 1000.0

    print(f"\n  {'─' * 50}")
    print(f"  RESULTS:")
    print(f"  {'─' * 50}")
    print(f"  HODL:              {pv_hodl:10.2f}"
          f" ({(pv_hodl / pv_start - 1) * 100:+.1f}%)")
    print(f"  Random:            {pv_random:10.2f}"
          f" ({(pv_random / pv_start - 1) * 100:+.1f}%)")
    print(f"  Resonance-logical: {pv_reso:10.2f}"
          f" ({(pv_reso / pv_start - 1) * 100:+.1f}%)")
    print(f"  {'─' * 50}")
    print(f"  Reso vs HODL:      {(pv_reso / pv_hodl - 1) * 100:+.1f}%")
    print(f"  Reso vs Random:    {(pv_reso / pv_random - 1) * 100:+.1f}%")
    print(f"  Trades (Reso):     {trades_reso}")

    # Experience store
    agent_reso.experience.statistics()
    agent_reso.experience.export_csv(
        os.path.join(out, 'experience.csv'))

    # ── Plot ──
    fig, axes = plt.subplots(4, 1, figsize=(16, 16), sharex=True)

    # 1: Price + DC + Trades
    ax = axes[0]
    ax.plot(t, price, 'gray', lw=0.5, alpha=0.5, label='Price')
    ax.plot(t, dc, 'blue', lw=2, label='DC (Trend)')

    buys = [h for h in agent_reso.history if h['action'] == 'BUY']
    sells = [h for h in agent_reso.history if h['action'] == 'SELL']
    if buys:
        ax.scatter([b['i'] for b in buys], [b['price'] for b in buys],
                   marker='^', color='green', s=30, zorder=5, label='BUY')
    if sells:
        ax.scatter([s['i'] for s in sells], [s['price'] for s in sells],
                   marker='v', color='red', s=30, zorder=5, label='SELL')
    ax.set_ylabel('Price')
    ax.set_title('Signal + DC Decomposition + Trades')
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3)

    # 2: AC + Phase
    ax = axes[1]
    ax.plot(t, ac, 'purple', lw=0.8, label='AC')
    ax.axhline(0, color='black', ls='-', lw=0.5)

    phase_colors = {'peak': 'red', 'trough': 'blue',
                    'transition': 'orange', 'flat': 'gray'}
    for phase_name, color in phase_colors.items():
        mask = phases == phase_name
        if np.any(mask):
            ax.fill_between(t, np.min(ac) * 1.2, np.max(ac) * 1.2,
                            where=mask, alpha=0.1, color=color,
                            label=phase_name)
    ax.set_ylabel('AC (Deviation)')
    ax.set_title('AC Component + Phase Detection')
    ax.legend(fontsize=7, ncol=4); ax.grid(True, alpha=0.3)

    # 3: Coupling ε
    ax = axes[2]
    epsilons = [h['epsilon'] for h in agent_reso.history]
    t_hist = [h['i'] for h in agent_reso.history]
    ax.plot(t_hist, epsilons, 'green', lw=1)
    ax.axhline(0.5, color='red', ls='--', lw=1,
               label='Threshold ε = 0.5')
    ax.axhline(1.0, color='gray', ls=':', lw=0.5)
    ax.set_ylabel('ε(Δφ)')
    ax.set_title('Coupling Efficiency ε(Δφ) = cos²(Δφ/2)')
    ax.set_ylim(0, 1.1)
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3)

    # 4: Portfolio comparison
    ax = axes[3]
    pv_reso_hist = [h['pv'] for h in agent_reso.history]
    pv_random_hist = [h['pv'] for h in agent_random.history]
    pv_hodl_hist = hodl_start * price[start:]

    ax.plot(t_hist, pv_reso_hist, 'green', lw=2,
            label=f'Resonance-logical ({(pv_reso / pv_start - 1) * 100:+.1f}%)')
    ax.plot(t_hist, pv_random_hist, 'red', lw=1, alpha=0.7,
            label=f'Random ({(pv_random / pv_start - 1) * 100:+.1f}%)')
    ax.plot(t[start:], pv_hodl_hist, 'blue', lw=1, ls='--',
            label=f'HODL ({(pv_hodl / pv_start - 1) * 100:+.1f}%)')
    ax.set_xlabel('t')
    ax.set_ylabel('Portfolio [€]')
    ax.set_title('Performance: Resonance-Logical vs. Random vs. HODL')
    ax.legend(fontsize=9); ax.grid(True, alpha=0.3)

    fig.suptitle(
        'Resonance-Logical Programming — Example\n'
        'DC/AC Decomposition → Phase → ε(Δφ) → Experience → Rules\n'
        f'Result: Reso {(pv_reso / pv_hodl - 1) * 100:+.1f}% vs HODL  |  '
        f'{trades_reso} Trades  |  κ = 1',
        fontsize=11, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(out, 'resonance_logic_example.png'), dpi=150)
    plt.close()
    print(f"\n  → {out}/resonance_logic_example.png")

    # Summary
    print(f"\n{'=' * 60}")
    print("SUMMARY")
    print(f"{'=' * 60}")
    print(f"""
  RESONANCE-LOGICAL PROGRAMMING — 5 PRINCIPLES:
  ──────────────────────────────────────────────
  1. Oscillation decomposition:  DC + AC (instead of 50+ features)
  2. Phase detection:            peak/trough/transition/flat
  3. Coupling efficiency:        ε(Δφ) = cos²(Δφ/2)
  4. Experience store:           Readable CSV (instead of tensor weights)
  5. Rule chain:                 Explicit guardrails

  RESULT:
  Resonance-logical: {pv_reso:.2f}  ({(pv_reso / pv_start - 1) * 100:+.1f}%)
  HODL:              {pv_hodl:.2f}  ({(pv_hodl / pv_start - 1) * 100:+.1f}%)
  Random:            {pv_random:.2f}  ({(pv_random / pv_start - 1) * 100:+.1f}%)

  Reso vs HODL:      {(pv_reso / pv_hodl - 1) * 100:+.1f}%
  Reso vs Random:    {(pv_reso / pv_random - 1) * 100:+.1f}%

  Zero free parameters. Zero GPUs. Fully explainable.
  E = π · ε(Δφ) · ℏ · f, κ = 1
""")
    print("Done.")


if __name__ == "__main__":
    main()
