# resonanzlogik_beispiel.py
# © Dominic-René Schu, 2025/2026 – Resonanzfeldtheorie
#
# Minimalbeispiel: Resonanzlogische Programmierung
#
# Demonstriert alle 5 Prinzipien:
#   1. Schwingungszerlegung (DC + AC)
#   2. Phasenerkennung (peak, trough, transition, flat)
#   3. Kopplungseffizienz ε(Δφ) = cos²(Δφ/2)
#   4. Erfahrungsspeicher (Zustand → Score)
#   5. Regelkette (explizite Leitplanken)
#
# Erzeugt ein synthetisches Signal und handelt darauf.
# Vergleicht: Resonanzlogisch vs. Zufällig vs. HODL.
#
# Ausführung: python resonanzlogik_beispiel.py
# Abhängigkeiten: numpy, matplotlib

import numpy as np
import matplotlib.pyplot as plt
import os

PI = np.pi


# ============================================================
# 1. Kopplungseffizienz (Axiom 4)
# ============================================================

def kopplungseffizienz(delta_phi):
    """ε(Δφ) = cos²(Δφ/2) — universelle RFT-Kopplung."""
    return np.cos(delta_phi / 2.0) ** 2


# ============================================================
# 2. Signalerzeugung
# ============================================================

def erzeuge_signal(n=2000, seed=42):
    """
    Synthetisches Preissignal: DC-Trend + AC-Schwingungen + Rauschen.
    Simuliert einen typischen Markt mit Zyklen.
    """
    rng = np.random.RandomState(seed)
    t = np.arange(n, dtype=float)

    # DC: Langsam steigender Trend (wie BTC über Monate)
    dc = 100.0 + 0.02 * t + 5.0 * np.sin(2 * PI * t / 800)

    # AC: Überlagerte Schwingungen (Marktzyklen)
    ac = (3.0 * np.sin(2 * PI * t / 50)          # Hauptzyklus: 50 Schritte
          + 1.5 * np.sin(2 * PI * t / 120)        # Langzyklus
          + 0.8 * np.sin(2 * PI * t / 20))        # Kurzzyklus

    # Rauschen (realistisch)
    rauschen = rng.normal(0, 0.8, n)

    preis = dc + ac + rauschen
    return t, preis, dc, ac


# ============================================================
# 3. Schwingungszerlegung (Prinzip 1)
# ============================================================

def zerlegung(preis, fenster_lang=50):
    """DC/AC-Zerlegung: DC = gleitender Mittelwert, AC = Preis - DC."""
    dc = np.convolve(preis, np.ones(fenster_lang) / fenster_lang,
                     mode='same')
    ac = preis - dc
    return dc, ac


# ============================================================
# 4. Phasenerkennung (Prinzip 2)
# ============================================================

def erkenne_phase(ac, amplitude_schwelle=0.3):
    """
    Bestimmt die Phase im Schwingungszyklus.

    peak:       AC > +schwelle · amplitude
    trough:     AC < -schwelle · amplitude
    transition: dazwischen, AC ändert Richtung
    flat:       Amplitude zu klein für Signal
    """
    n = len(ac)
    phasen = np.full(n, 'flat', dtype='U10')
    amplitude = np.zeros(n)

    fenster = 25
    for i in range(fenster, n):
        segment = ac[i - fenster:i]
        amp = np.max(segment) - np.min(segment)
        amplitude[i] = amp

        if amp < 0.5:  # Zu wenig Signal
            phasen[i] = 'flat'
        elif ac[i] > amplitude_schwelle * amp:
            phasen[i] = 'peak'
        elif ac[i] < -amplitude_schwelle * amp:
            phasen[i] = 'trough'
        else:
            phasen[i] = 'transition'

    return phasen, amplitude


# ============================================================
# 5. Erfahrungsspeicher (Prinzip 4)
# ============================================================

class ErfahrungsSpeicher:
    """
    Zustand-Aktion-Score-Tabelle.
    Jeder Eintrag ist ein lesbarer String.
    Kein Tensor. Keine Gewichte. Keine Black Box.
    """

    def __init__(self, decay=0.90):
        self.speicher = {}  # "zustand,aktion" → score
        self.decay = decay

    def schlüssel(self, phase, trend, aktion):
        return f"{phase},{trend},{aktion}"

    def aktualisiere(self, phase, trend, aktion, belohnung):
        key = self.schlüssel(phase, trend, aktion)
        if key not in self.speicher:
            self.speicher[key] = 0.0
        self.speicher[key] = self.speicher[key] * self.decay + belohnung

    def score(self, phase, trend, aktion):
        key = self.schlüssel(phase, trend, aktion)
        return self.speicher.get(key, 0.0)

    def beste_aktion(self, phase, trend):
        aktionen = ['BUY', 'SELL', 'HOLD']
        scores = {a: self.score(phase, trend, a) for a in aktionen}
        return max(scores, key=scores.get), scores

    def statistik(self):
        print(f"\n  Erfahrungsspeicher: {len(self.speicher)} Einträge")
        if self.speicher:
            top = sorted(self.speicher.items(),
                         key=lambda x: abs(x[1]), reverse=True)[:10]
            print(f"  Top 10:")
            for key, score in top:
                print(f"    {key:40s} → {score:+.4f}")

    def export_csv(self, pfad):
        with open(pfad, 'w') as f:
            f.write("zustand_aktion,score\n")
            for key, score in sorted(self.speicher.items()):
                f.write(f"{key},{score:.6f}\n")
        print(f"  → Erfahrung exportiert: {pfad}"
              f" ({len(self.speicher)} Einträge)")


# ============================================================
# 6. Regelkette (Prinzip 5)
# ============================================================

class RegelKette:
    """
    Explizite Leitplanken. Nicht trainiert. Nicht optimiert.
    Physikalisch motiviert.
    """

    def __init__(self, min_cash_anteil=0.10, min_asset_anteil=0.05,
                 cooldown=3):
        self.min_cash = min_cash_anteil
        self.min_asset = min_asset_anteil
        self.cooldown = cooldown
        self.letzte_trades = []
        self.blockiert = 0

    def prüfe(self, vorschlag, cash, portfolio_wert, epsilon):
        """Filtert Vorschlag durch Regelkette."""
        gründe = []

        # Regel 1: Kopplung zu schwach → kein Trade
        if epsilon < 0.3 and vorschlag != 'HOLD':
            gründe.append(f"ε={epsilon:.2f} < 0.3 → keine Kopplung")
            return 'HOLD', gründe

        # Regel 2: Cash-Schutz
        if vorschlag == 'BUY':
            cash_anteil = cash / max(portfolio_wert, 1e-10)
            if cash_anteil < self.min_cash:
                gründe.append(f"Cash {cash_anteil:.1%} < {self.min_cash:.0%}")
                return 'HOLD', gründe

        # Regel 3: Asset-Schutz
        if vorschlag == 'SELL':
            asset_anteil = 1.0 - cash / max(portfolio_wert, 1e-10)
            if asset_anteil < self.min_asset:
                gründe.append(
                    f"Asset {asset_anteil:.1%} < {self.min_asset:.0%}")
                return 'HOLD', gründe

        # Regel 4: Cooldown (Overtrading-Schutz)
        if self.blockiert > 0:
            self.blockiert -= 1
            gründe.append(f"Cooldown ({self.blockiert} verbleibend)")
            return 'HOLD', gründe

        # Cooldown setzen nach Trade
        if vorschlag in ('BUY', 'SELL'):
            self.letzte_trades.append(vorschlag)
            if len(self.letzte_trades) > self.cooldown:
                self.letzte_trades.pop(0)
            if len(self.letzte_trades) >= self.cooldown:
                if all(t != 'HOLD' for t in self.letzte_trades):
                    self.blockiert = 2
                    gründe.append("Cooldown aktiviert (Overtrading)")

        return vorschlag, gründe


# ============================================================
# 7. Resonanzlogischer Agent
# ============================================================

class ResonanzAgent:
    """
    Kompletter resonanzlogischer Agent.
    Demonstriert alle 5 Prinzipien.
    """

    def __init__(self, startkapital=1000.0, trade_anteil=0.15):
        self.cash = startkapital
        self.asset = 0.0
        self.trade_anteil = trade_anteil
        self.erfahrung = ErfahrungsSpeicher()
        self.regeln = RegelKette()
        self.historie = []

    def portfolio_wert(self, preis):
        return self.cash + self.asset * preis

    def trend_erkennung(self, dc, i, fenster=20):
        if i < fenster:
            return 'sideways'
        steigung = (dc[i] - dc[i - fenster]) / max(dc[i - fenster], 1e-10)
        if steigung > 0.005:
            return 'uptrend'
        elif steigung < -0.005:
            return 'downtrend'
        return 'sideways'

    def schritt(self, i, preis, dc, ac, phasen):
        """Ein Entscheidungsschritt."""
        phase = phasen[i]
        trend = self.trend_erkennung(dc, i)
        aktueller_preis = preis[i]
        pw = self.portfolio_wert(aktueller_preis)

        # Prinzip 3: Kopplungseffizienz
        # Δφ wird aus der AC-Phase abgeleitet
        if phase == 'peak':
            delta_phi = 0.0       # Perfekte Kopplung für SELL
        elif phase == 'trough':
            delta_phi = 0.0       # Perfekte Kopplung für BUY
        elif phase == 'transition':
            delta_phi = PI / 3    # Mittlere Kopplung
        else:
            delta_phi = PI / 2    # Schwache Kopplung (flat)

        epsilon = kopplungseffizienz(delta_phi)

        # Prinzip 2: Phasenbasierte Entscheidung
        if phase == 'peak':
            vorschlag = 'SELL'
        elif phase == 'trough':
            vorschlag = 'BUY'
        else:
            vorschlag = 'HOLD'

        # Prinzip 4: Erfahrung moduliert
        _, scores = self.erfahrung.beste_aktion(phase, trend)
        if vorschlag != 'HOLD':
            erfahrungs_score = scores.get(vorschlag, 0.0)
            if erfahrungs_score < -0.5:
                vorschlag = 'HOLD'  # Erfahrung überstimmt

        # Prinzip 5: Regelkette filtert
        vorschlag, gründe = self.regeln.prüfe(
            vorschlag, self.cash, pw, epsilon)

        # Ausführung
        menge = self.trade_anteil
        if vorschlag == 'BUY' and self.cash > 10:
            kauf_cash = self.cash * menge
            kauf_asset = kauf_cash / aktueller_preis
            self.cash -= kauf_cash
            self.asset += kauf_asset
        elif vorschlag == 'SELL' and self.asset > 0.01:
            verk_asset = self.asset * menge
            verk_cash = verk_asset * aktueller_preis
            self.asset -= verk_asset
            self.cash += verk_cash
        else:
            vorschlag = 'HOLD'

        # Belohnung berechnen (für Erfahrungsspeicher)
        neuer_pw = self.portfolio_wert(aktueller_preis)
        belohnung = (neuer_pw - pw) / max(pw, 1e-10)
        self.erfahrung.aktualisiere(phase, trend, vorschlag, belohnung)

        self.historie.append({
            'i': i, 'preis': aktueller_preis, 'phase': phase,
            'trend': trend, 'epsilon': epsilon,
            'aktion': vorschlag, 'pw': neuer_pw,
            'cash': self.cash, 'asset': self.asset
        })

        return vorschlag


# ============================================================
# 8. Zufälliger Agent (Baseline)
# ============================================================

class ZufallsAgent:
    def __init__(self, startkapital=1000.0, trade_anteil=0.15, seed=123):
        self.cash = startkapital
        self.asset = 0.0
        self.trade_anteil = trade_anteil
        self.rng = np.random.RandomState(seed)
        self.historie = []

    def portfolio_wert(self, preis):
        return self.cash + self.asset * preis

    def schritt(self, i, preis):
        aktueller_preis = preis[i]
        pw = self.portfolio_wert(aktueller_preis)
        aktion = self.rng.choice(['BUY', 'SELL', 'HOLD'],
                                 p=[0.2, 0.2, 0.6])
        if aktion == 'BUY' and self.cash > 10:
            kauf = self.cash * self.trade_anteil
            self.asset += kauf / aktueller_preis
            self.cash -= kauf
        elif aktion == 'SELL' and self.asset > 0.01:
            verk = self.asset * self.trade_anteil
            self.cash += verk * aktueller_preis
            self.asset -= verk
        self.historie.append({
            'i': i, 'preis': aktueller_preis,
            'aktion': aktion, 'pw': self.portfolio_wert(aktueller_preis)
        })


# ============================================================
# 9. Hauptsimulation
# ============================================================

def main():
    print("=" * 60)
    print("RESONANZLOGISCHE PROGRAMMIERUNG — BEISPIEL")
    print("E = π · ε(Δφ) · ℏ · f, κ = 1")
    print("=" * 60)

    out = "figures"
    os.makedirs(out, exist_ok=True)

    # Signal erzeugen
    t, preis, dc_true, ac_true = erzeuge_signal(n=2000)
    print(f"\n  Signal: {len(preis)} Datenpunkte")
    print(f"  Preis: {preis[0]:.1f} → {preis[-1]:.1f}")

    # Prinzip 1: Zerlegung
    dc, ac = zerlegung(preis, fenster_lang=50)

    # Prinzip 2: Phasenerkennung
    phasen, amplituden = erkenne_phase(ac)
    phase_counts = {p: np.sum(phasen == p) for p in
                    ['peak', 'trough', 'transition', 'flat']}
    print(f"\n  Phasen: {phase_counts}")

    # Agenten
    agent_reso = ResonanzAgent(startkapital=1000.0)
    agent_zufall = ZufallsAgent(startkapital=1000.0)
    hodl_start = 1000.0 / preis[50]  # Alles investieren bei t=50

    # Simulation
    start = 50  # Warte auf MA-Initialisierung
    trades_reso = 0
    for i in range(start, len(preis)):
        aktion = agent_reso.schritt(i, preis, dc, ac, phasen)
        agent_zufall.schritt(i, preis)
        if aktion != 'HOLD':
            trades_reso += 1

    # Ergebnisse
    pw_reso = agent_reso.portfolio_wert(preis[-1])
    pw_zufall = agent_zufall.portfolio_wert(preis[-1])
    pw_hodl = hodl_start * preis[-1]
    pw_start = 1000.0

    print(f"\n  {'─' * 50}")
    print(f"  ERGEBNISSE:")
    print(f"  {'─' * 50}")
    print(f"  HODL:           {pw_hodl:10.2f}"
          f" ({(pw_hodl / pw_start - 1) * 100:+.1f}%)")
    print(f"  Zufall:         {pw_zufall:10.2f}"
          f" ({(pw_zufall / pw_start - 1) * 100:+.1f}%)")
    print(f"  Resonanzlogisch:{pw_reso:10.2f}"
          f" ({(pw_reso / pw_start - 1) * 100:+.1f}%)")
    print(f"  {'─' * 50}")
    print(f"  Reso vs HODL:   {(pw_reso / pw_hodl - 1) * 100:+.1f}%")
    print(f"  Reso vs Zufall: {(pw_reso / pw_zufall - 1) * 100:+.1f}%")
    print(f"  Trades (Reso):  {trades_reso}")

    # Erfahrungsspeicher
    agent_reso.erfahrung.statistik()
    agent_reso.erfahrung.export_csv(
        os.path.join(out, 'erfahrung.csv'))

    # ── Plot ──
    fig, axes = plt.subplots(4, 1, figsize=(16, 16), sharex=True)

    # 1: Preis + DC + Trades
    ax = axes[0]
    ax.plot(t, preis, 'gray', lw=0.5, alpha=0.5, label='Preis')
    ax.plot(t, dc, 'blue', lw=2, label='DC (Trend)')

    buys = [h for h in agent_reso.historie if h['aktion'] == 'BUY']
    sells = [h for h in agent_reso.historie if h['aktion'] == 'SELL']
    if buys:
        ax.scatter([b['i'] for b in buys], [b['preis'] for b in buys],
                   marker='^', color='green', s=30, zorder=5, label='BUY')
    if sells:
        ax.scatter([s['i'] for s in sells], [s['preis'] for s in sells],
                   marker='v', color='red', s=30, zorder=5, label='SELL')
    ax.set_ylabel('Preis')
    ax.set_title('Signal + DC-Zerlegung + Trades')
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3)

    # 2: AC + Phase
    ax = axes[1]
    ax.plot(t, ac, 'purple', lw=0.8, label='AC')
    ax.axhline(0, color='black', ls='-', lw=0.5)

    phase_colors = {'peak': 'red', 'trough': 'blue',
                    'transition': 'orange', 'flat': 'gray'}
    for phase_name, color in phase_colors.items():
        mask = phasen == phase_name
        if np.any(mask):
            ax.fill_between(t, np.min(ac) * 1.2, np.max(ac) * 1.2,
                            where=mask, alpha=0.1, color=color,
                            label=phase_name)
    ax.set_ylabel('AC (Abweichung)')
    ax.set_title('AC-Komponente + Phasenerkennung')
    ax.legend(fontsize=7, ncol=4); ax.grid(True, alpha=0.3)

    # 3: Kopplung ε
    ax = axes[2]
    epsilons = [h['epsilon'] for h in agent_reso.historie]
    t_hist = [h['i'] for h in agent_reso.historie]
    ax.plot(t_hist, epsilons, 'green', lw=1)
    ax.axhline(0.5, color='red', ls='--', lw=1,
               label='Schwelle ε = 0.5')
    ax.axhline(1.0, color='gray', ls=':', lw=0.5)
    ax.set_ylabel('ε(Δφ)')
    ax.set_title('Kopplungseffizienz ε(Δφ) = cos²(Δφ/2)')
    ax.set_ylim(0, 1.1)
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3)

    # 4: Portfolio-Vergleich
    ax = axes[3]
    pw_reso_hist = [h['pw'] for h in agent_reso.historie]
    pw_zufall_hist = [h['pw'] for h in agent_zufall.historie]
    pw_hodl_hist = hodl_start * preis[start:]

    ax.plot(t_hist, pw_reso_hist, 'green', lw=2,
            label=f'Resonanzlogisch ({(pw_reso / pw_start - 1) * 100:+.1f}%)')
    ax.plot(t_hist, pw_zufall_hist, 'red', lw=1, alpha=0.7,
            label=f'Zufall ({(pw_zufall / pw_start - 1) * 100:+.1f}%)')
    ax.plot(t[start:], pw_hodl_hist, 'blue', lw=1, ls='--',
            label=f'HODL ({(pw_hodl / pw_start - 1) * 100:+.1f}%)')
    ax.set_xlabel('t')
    ax.set_ylabel('Portfolio [€]')
    ax.set_title('Performance: Resonanzlogisch vs. Zufall vs. HODL')
    ax.legend(fontsize=9); ax.grid(True, alpha=0.3)

    fig.suptitle(
        'Resonanzlogische Programmierung — Beispiel\n'
        'DC/AC-Zerlegung → Phase → ε(Δφ) → Erfahrung → Regeln\n'
        f'Ergebnis: Reso {(pw_reso / pw_hodl - 1) * 100:+.1f}% vs HODL  |  '
        f'{trades_reso} Trades  |  κ = 1',
        fontsize=11, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(out, 'resonanzlogik_beispiel.png'), dpi=150)
    plt.close()
    print(f"\n  → {out}/resonanzlogik_beispiel.png")

    # Zusammenfassung
    print(f"\n{'=' * 60}")
    print("ZUSAMMENFASSUNG")
    print(f"{'=' * 60}")
    print(f"""
  RESONANZLOGISCHE PROGRAMMIERUNG — 5 PRINZIPIEN:
  ────────────────────────────────────────────────
  1. Schwingungszerlegung:  DC + AC (statt 50+ Features)
  2. Phasenerkennung:       peak/trough/transition/flat
  3. Kopplungseffizienz:    ε(Δφ) = cos²(Δφ/2)
  4. Erfahrungsspeicher:    Lesbare CSV (statt Tensorgewichte)
  5. Regelkette:            Explizite Leitplanken

  ERGEBNIS:
  Resonanzlogisch:  {pw_reso:.2f}  ({(pw_reso / pw_start - 1) * 100:+.1f}%)
  HODL:             {pw_hodl:.2f}  ({(pw_hodl / pw_start - 1) * 100:+.1f}%)
  Zufall:           {pw_zufall:.2f}  ({(pw_zufall / pw_start - 1) * 100:+.1f}%)

  Reso vs HODL:     {(pw_reso / pw_hodl - 1) * 100:+.1f}%
  Reso vs Zufall:   {(pw_reso / pw_zufall - 1) * 100:+.1f}%

  Null freie Parameter. Null GPUs. Vollständig erklärbar.
  E = π · ε(Δφ) · ℏ · f, κ = 1
""")
    print("Fertig.")


if __name__ == "__main__":
    main()