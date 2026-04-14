# Resonanzlogische Analyse der Finanzmärkte: Altcoins als amplifizierte BTC-Schwingungen

## Empirischer Nachweis durch algorithmisches Trading mit Resonanzfeldtheorie

*Dominic-René Schu, Februar 2026 — korrigiert März 2026*

---

## Zusammenfassung

Diese Analyse dokumentiert ein empirisches Ergebnis, das bei der Entwicklung eines resonanzlogischen Trading-Systems (ResoTrade V11) unerwartet zutage trat: **Der Altcoin-Markt besitzt keine eigenständige AC-Komponente relativ zu BTC.** Altcoins schwingen synchron mit Bitcoin — ihre Preisbewegung ist ein skaliertes Echo, kein unabhängiges Signal.

Die AC/DC-Zerlegung (V11) macht den Grund sichtbar: Altcoins besitzen keine eigenständige AC-Komponente — ihre Schwingung ist ein skaliertes Echo der BTC-Schwingung mit Hebelfaktor α. Ohne eigene Obertöne keine Resonanz, ohne Resonanz kein Diversifikationsgewinn in einem Multi-Asset-Portfolio.

**Korrektur (März 2026):** Die ursprüngliche Analyse schloss daraus, Altcoins seien „nicht handelbar". Das war voreilig. Ein Altcoin mit α = 2.5 schwingt die gleiche Frequenz wie BTC, aber mit 2.5-facher Amplitude. Diese amplifizierten Schwingungen sind mit denselben resonanzlogischen Methoden handelbar — als eigenständiges Asset mit angepassten Schwellen, nicht als Portfolio-Ergänzung neben BTC.

Die korrigierte Kernaussage lautet:

> **Altcoins sind keine Diversifikation zu BTC, aber ihre amplifizierten Schwingungen sind mit denselben Methoden handelbar — als eigenständiges Asset, nicht als Portfolio-Ergänzung.**

---

## 1. Entstehungskontext

Das Ziel war nicht Grundlagenforschung, sondern ein funktionierender Trading-Bot. ResoTrade ist ein resonanzfeldtheoretisches Trading-System, das durch wiederholte Offline-Simulation lernt, Kurszyklen zu handeln. Die Kernmechanismen:

- **AC/DC-Zerlegung** (Axiom 1): Preis = DC (Trend) + AC (handelbare Schwingung)
- **Energierichtungsvektor** (Axiom 5): `energy_dir = e_short - e_long`
- **Resonanzkopplung** (Axiom 6): Trades nur bei Phasengleichheit mit dem Markt
- Erfahrungsbasiertes Lernen (Chain → Score, Decay)
- Dynamische Satellite-Selektion (Top-5 aus 13 Assets)
- Verzögerte Trade-Bewertung (24h kontrafaktisch vs. HOLD)

Die wissenschaftliche Erkenntnis entstand emergent: Als das Multi-Asset-System (V10.2) von Aktien-Satellites auf Altcoin-Satellites umgestellt wurde, brach die Performance zusammen — nicht durch technische Fehler, sondern durch einen fundamentalen Unterschied in der Signalstruktur.

### Performance-Kontext: ResoTrade V11 (BTC-only)

| Metrik | Wert |
|--------|------|
| Performance vs HODL | +42.89% |
| Episoden über HODL | 83.4% (steigend bei weiterem Training) |
| Lernfortschritt | Positiv und konvergierend |
| Theoretische Grundlage | Axiome 1, 2, 5, 6 der Resonanzfeldtheorie |

---

## 2. Theoretischer Rahmen

### 2.1 Universelle Schwingung und AC/DC-Zerlegung (Axiom 1)

Axiom 1 der Resonanzfeldtheorie postuliert: **Jede Entität besitzt eine periodische Schwingung ψ(x,t).** Angewandt auf Finanzmärkte bedeutet das: Jeder Preis lässt sich in zwei Komponenten zerlegen:

```
ψ_Preis(t) = DC(t) + AC(t)
             ╰─────╯   ╰────╯
              Trend     handelbare
           (MA_LONG)    Schwingung
```

Die DC-Komponente ist der Grundton — der langfristige Trend, der nicht prognostizierbar ist. Die AC-Komponente sind die Obertöne — die Schwingung um den Trend, die durch Phasenerkennung handelbar ist.

**Entscheidend für Multi-Asset-Portfolios:** Nur Assets mit **eigenständiger AC-Komponente** erzeugen Diversifikationsgewinn. Wenn die AC-Komponente eines Assets lediglich ein skaliertes Echo eines anderen Assets ist, trägt sie keine zusätzliche Information bei.

**Entscheidend für Einzelhandel:** Auch ein skaliertes Echo ist handelbar, wenn die Amplitude groß genug ist. Ein Altcoin mit α = 2.5 erreicht die Handelsschwellen schneller und häufiger als BTC selbst.

### 2.2 Resonanzbedingung (Axiom 3)

Zwei Systeme treten in Resonanz, wenn ihre Frequenzen in einem rationalen Verhältnis stehen:

```
f₁ / f₂ = n / m,    n, m ∈ ℤ⁺
```

Resonanz erzeugt Energietransfer (Axiom 4):

```
E = π · ε · h · f
```

**Voraussetzung für produktive Portfolio-Resonanz ist, dass die beteiligten Systeme unterschiedliche Eigenfrequenzen besitzen.** Zwei identisch gestimmte Saiten erzeugen keine Obertöne — sie schwingen synchron. Das bedeutet: kein Diversifikationsgewinn. Es bedeutet nicht: kein Signal.

### 2.3 Eigenfrequenzen in Finanzmärkten

Jeder echte Markt wird durch einen eigenständigen Wertschöpfungsprozess getrieben, der eine charakteristische Eigenfrequenz erzeugt:

| Asset | Wertschöpfungsbasis | Eigenfrequenz bestimmt durch |
|-------|--------------------|-----------------------------|
| **BTC** | Dezentrale Knappheit, Proof-of-Work | Halving-Zyklus, Netzwerkadoption, Geldpolitik |
| **MRK** (Merck) | Pharma-Pipeline | FDA-Zulassungen, Patentzyklen, Demographie |
| **GLD** (Gold-ETF) | Physische Knappheit | Inflation, Geopolitik, Zentralbankpolitik |
| **AAPL** (Apple) | Produktinnovation | iPhone-Zyklus, Services-Wachstum, China-Risiko |
| **USD** | Produktivität, Institutionen | BIP, Zinspolitik, Fiskaldefizit |

Jedes dieser Systeme schwingt mit einer **eigenen**, durch fundamentale Wertschöpfung bestimmten Frequenz. Die Kopplung zwischen ihnen ist nicht-trivial und erzeugt ein reiches Obertonspektrum.

### 2.4 Altcoins als amplifizierte Schwingungen

Altcoins besitzen keine eigenständige Wertschöpfungsbasis, die von BTC unabhängig wäre. Ihre AC-Komponente ist kein eigenständiger Oberton, sondern ein skaliertes Echo:

```
AC_Altcoin(t) ≈ α · AC_BTC(t) + η(t)
```

wobei α ein Hebelfaktor (typisch 1.5–4.0) und η(t) Rauschen ist. Die Eigenfrequenz des Altcoins ist identisch mit der von BTC — nur die Amplitude und das Rauschen unterscheiden sich.

**Für Portfolio-Diversifikation** ist das äquivalent zu einem linear abhängigen Gleichungssystem:

```
┌         ┐   ┌    ┐     ┌                ┐
│  1    0  │   │ x₁ │     │ b₁             │
│          │ · │    │  =  │                │
│  α    0  │   │ x₂ │     │ α · b₁ + η    │
└         ┘   └    ┘     └                ┘
```

Die Determinante ist Null. Kein Informationsgewinn durch Hinzufügen des Altcoins zum BTC-Portfolio.

**Für Einzelhandel** ist α der entscheidende Vorteil:

| Eigenschaft | BTC (α=1) | ETH (α≈1.8) | SOL (α≈3.0) |
|---|---|---|---|
| AC-Amplitude | ±5% | ±9% | ±15% |
| Sell-Schwelle 4% erreicht | Bei 4% Bewegung | Bei 2.2% BTC-Bewegung | Bei 1.3% BTC-Bewegung |
| Buy-Schwelle -7% erreicht | Bei 7% Drawdown | Bei 3.9% BTC-Drawdown | Bei 2.3% BTC-Drawdown |
| Trades pro Zeitraum | Wenige | Mehr | Deutlich mehr |
| Risiko | Basis | Erhöht | Hoch |

Die amplifizierten Schwellen sind mit dem `threshold_optimizer` automatisch findbar — derselbe Regelkreis, andere Parameter.

---

## 3. Methodik

### 3.1 System: ResoTrade

Die Altcoin-Analyse wurde mit ResoTrade V10.2 (Multi-Asset) durchgeführt. Die BTC-only Referenz stammt aus V11 mit AC/DC-Zerlegung.

**V11 Kernarchitektur (BTC-only):**
- AC/DC-Zerlegung: DC = MA_LONG (168h), AC = Preis − DC
- Phasenerkennung: peak / trough / transition / flat
- Energierichtungsvektor: `energy_dir = e_short - e_long`
- Resonanz-Gate: Trades nur bei Phasengleichheit (K = K₀·cos(θ))
- Erfahrungsspeicher: Chain → Score mit AC-Phase als Dimension
- HODL-Kern: 5% des Bestands unverkäuflich

**V10.2 Multi-Asset Erweiterung:**
- State-Repräsentation: 12 Dimensionen (Position, Trend, MA, Volatilität, Cash, Allokation, Relative Strength, Cluster)
- Hybrides Lernen: 30% Regel + 70% Erfahrung × Konfidenz
- Trade-Bewertung: Verzögert (24h), kontrafaktisch gegen HOLD
- Dynamische Satellite-Selektion (Top-5 aus 13 Assets)

### 3.2 Experimentaufbau

Drei identische Konfigurationen, nur die Satellite-Assets unterscheiden sich:

| Konfiguration | Core | Satellites | Cluster |
|---------------|------|-----------|---------|
| **A: BTC + Aktien** | BTC | NVDA, AAPL, TSLA, MSFT, AMZN, META, MCD, MRK, AZN, COIN, SPY, QQQ, GLD | Tech, Value, ETF |
| **B: BTC + Altcoins** | BTC | ETH, XRP, ADA, AVAX, LINK, AAVE, CRV, BONK, LTC, BCH | L1, DeFi, Sentiment, Store |
| **C: BTC only (V11)** | BTC | — | — |

### 3.3 Trainingsparameter

| Parameter | Wert |
|-----------|------|
| Episoden (Konfiguration A) | 20.000 |
| Episoden (Konfiguration B) | 200.000+ |
| Episoden (Konfiguration C, V11) | 10.000+ (konvergierend) |
| Startkapital | 0.8 BTC + 23.305 USD (≈ 1.0 BTC-Äquivalent) |
| Window Length | 90 Schritte (Stundendaten) |
| Trade-Bewertungshorizont | 24 Schritte |
| Max. aktive Satellites | 5 pro Episode (A, B) |
| Decay-Faktor | 0.80 pro Pass (V11), 0.9995 (V10.2) |
| Datenquelle | yfinance (180 Tage, 1h OHLC) |

---

## 4. Ergebnisse

### 4.1 Vergleichstabelle

| Metrik | BTC + Aktien | BTC + Altcoins | BTC only (V11) |
|--------|-------------|---------------|----------------|
| **Ø BTC-Äquivalent** | **1.090** | 1.038 | **1.039** |
| **Median** | **1.077** | 1.033 | **1.041** |
| **Min / Max** | **1.020 / 1.282** | 0.927 / 1.173 | 0.926 / 1.131 |
| **Episoden über HODL** | **100%** | 86% | **83.4%** (steigend) |
| **Draw-Rate** | 84% | **98.4%** | ~49% |
| **Success-Rate** | 14% | **0.9%** | ~29% |
| **Failure-Rate** | 2% | 0.7% | ~22% |
| **Lernfortschritt** | **+0.001 (↑)** | -0.002 (↓) | **+0.010 (↑↑)** |
| **Performance vs HODL** | +9.0% | +3.8% | **+42.89%** |

### 4.2 Schlüsselbeobachtung: Portfolio-Effekt vs. Einzelhandel

**Portfolio-Ergebnis:** BTC allein (V11, +42.89%) übertrifft BTC + Altcoins (+3.8%) um Faktor 11. Die Altcoins erzeugen nicht nur keinen Diversifikationsgewinn — sie **stören** das BTC-Signal. Die Core-Cluster S:F Ratio fällt von 6.0:1 (Konfiguration A) auf 0.3:1 (Konfiguration B).

**Implikation für Einzelhandel:** Dieses Ergebnis zeigt, dass Altcoins *neben BTC* keinen Mehrwert liefern. Es zeigt nicht, dass ein ResoTrade-System *auf einem Altcoin-Chart allein* nicht funktionieren würde. Die amplifizierten Schwingungen (α > 1) sind mit angepassten Schwellen potenziell profitabler als BTC selbst — bei entsprechend höherem Risiko.

### 4.3 Trade-Chain-Analyse

**Konfiguration A (BTC + Aktien):**

```
BTC_BUY_SMALL      S:F = 5.2:1    ← Profitabel
TSLA_SELL_SMALL    S:F = ∞:1      ← Informativ
MRK_SELL_SMALL     S:F = 2.8:1    ← Diversifikationsgewinn
AMZN_SELL_SMALL    S:F = 8.0:1    ← Unabhängiges Signal
```

**Konfiguration B (BTC + Altcoins):**

```
AVAX_SELL_SMALL    S:F = 0.9:1    ← Neutral (kein Signal neben BTC)
BTC_SELL_SMALL     S:F = 0.0:1    ← Gestört durch Altcoin-Rauschen
BCH_SELL_SMALL     S:F = ∞:1     ← Nur weil BCH chronisch fällt
CRV_SELL_SMALL     S:F = ∞:1     ← Draw-dominiert, kein Signal
```

### 4.4 Cluster-Bilanz

**Konfiguration A:**

| Cluster | S:F | Interpretation |
|---------|-----|----------------|
| crypto (BTC) | 6.0:1 | Starke Eigenmode |
| tech | 1.8:1 | Unabhängige Information |
| value | 8.0:1 | Höchste Diversifikation |
| etf | 0.8:1 | Geringste Eigenständigkeit |

**Konfiguration B:**

| Cluster | S:F | Interpretation |
|---------|-----|----------------|
| core (BTC) | 0.3:1 | **Durch Altcoins gestört** |
| l1 | 0.9:1 | Keine zusätzliche Information |
| defi | ∞:1 | Draw-dominiert |
| store | ∞:1 | Draw-dominiert |
| sentiment | 0.0:1 | Reines Rauschen |

### 4.5 Draw-Rate als Resonanzindikator

Die Draw-Rate ist der numerische Fingerabdruck fehlender Eigenfrequenzen im Portfolio-Kontext:

| Konfiguration | Draw-Rate | AC-Interpretation | Bedeutung |
|---------------|-----------|-------------------|-----------|
| BTC only (V11) | ~49% | Eigenständige AC, klare Phasen | System findet Signal |
| BTC + Aktien | 84% | Verschiedene ACs, teilweise korreliert | System findet Differenzen |
| BTC + Altcoins | **98.4%** | Identische AC, keine Phasendifferenz | Jede Aktion ≈ HOLD *relativ zu BTC* |

**98.4% Draw im Portfolio-Kontext bedeutet:** Das System kann Altcoin-Trades nicht von Nichtstun unterscheiden, *weil der Altcoin dasselbe tut wie BTC*. Auf dem Altcoin-Chart allein (ohne BTC-Vergleich) wäre die Draw-Rate niedriger — die Schwingungen sind größer und erzeugen klarere success/failure-Signale.

---

## 5. Resonanztheoretische Interpretation

### 5.1 AC/DC-Analyse der Asset-Klassen

```
Aktienmarkt — eigenständige AC-Komponenten:
  BTC  ──── DC₁ + AC₁(f₁)    f₁ = Krypto-Adoption, Halving
  MRK  ──── DC₂ + AC₂(f₂)    f₂ = Pharma-Pipeline, FDA
  GLD  ──── DC₃ + AC₃(f₃)    f₃ = Inflation, Geopolitik
  AAPL ──── DC₄ + AC₄(f₄)    f₄ = iPhone-Zyklus, China

  → 4 unabhängige AC-Komponenten → reiches Obertonspektrum
  → Phasenverschiebungen zwischen ACs → handelbares Portfolio-Signal

Altcoin-Markt — amplifizierte AC-Komponenten:
  BTC  ──── DC₁ + AC₁(f₁)              α = 1.0
  ETH  ──── α₁·DC₁ + α₁·AC₁(f₁) + η₁  α₁ ≈ 1.8
  ADA  ──── α₂·DC₁ + α₂·AC₁(f₁) + η₂  α₂ ≈ 2.5
  SOL  ──── α₃·DC₁ + α₃·AC₁(f₁) + η₃  α₃ ≈ 3.0

  → 1 unabhängige AC-Frequenz, verschiedene Amplituden
  → Keine Phasenverschiebung → kein Portfolio-Diversifikationsgewinn
  → Größere Amplituden → mehr Handelsgelegenheiten pro Asset
```

### 5.2 Zwei verschiedene Fragestellungen

Die Resonanzfeldtheorie unterscheidet klar zwischen zwei Fragen:

**Frage 1: Erzeugt Asset B Diversifikationsgewinn neben Asset A?**
Nur wenn `AC_B(t)` unabhängig von `AC_A(t)` ist. Bei Altcoins: Nein.

**Frage 2: Ist Asset B allein handelbar?**
Ja, wenn `|AC_B(t)|` groß genug ist, um die Schwellen zu überschreiten. Bei Altcoins mit α > 1: Ja, mit angepassten Schwellen sogar häufiger als BTC.

Die ursprüngliche Analyse (Februar 2026) beantwortete Frage 1 korrekt und schloss daraus fälschlich auf Frage 2. Die Korrektur macht diese Unterscheidung explizit.

### 5.3 Der Hebelfaktor α als Handelsparameter

Der Hebelfaktor α bestimmt das Risiko-Rendite-Profil:

| α-Bereich | Beispiele | Schwellen | Trades/Monat | Risiko |
|---|---|---|---|---|
| α ≈ 1.0 | BTC | Standard (V11.7) | ~12 | Basis |
| α ≈ 1.5–2.0 | ETH, BNB | ~60% der BTC-Schwellen | ~20 | Moderat erhöht |
| α ≈ 2.5–3.5 | SOL, ADA, AVAX | ~35% der BTC-Schwellen | ~30+ | Hoch |
| α > 4.0 | BONK, Memecoins | Zu volatil, Rauschen dominiert | — | Nicht handelbar |

Der `threshold_optimizer` findet die optimalen Schwellen pro Asset automatisch. Das System passt sich an α an, ohne dass α explizit bekannt sein muss.

### 5.4 BTC-Dominanz-Zyklus

Der einzige Moment, in dem Altcoins scheinbar unabhängig von BTC agieren, ist der BTC-Dominanz-Zyklus: BTC steigt zuerst, dann rotiert Kapital in Altcoins. Diese Rotation ist:

1. **Zeitlich begrenzt** (wenige Wochen pro Zyklus)
2. **Prädiktiv nicht nutzbar** im Portfolio-Kontext (der Übergang ist nicht stationär)
3. **Amplitudenabhängig** (funktioniert nur in Bullenmärkten)

Das V10.2-System hat über 200.000 Episoden versucht, diesen Zyklus als Diversifikation zu nutzen. Ergebnis: negativer Lernfortschritt (−0.002). Der Zyklus ist zu instabil und zu kurz für Portfolio-Resonanz — aber er amplifiziert die AC-Schwingung des einzelnen Altcoins, was den Einzelhandel begünstigt.

---

## 6. Implikation für Geldsysteme

Diese Analyse ergänzt das duale Resonanz-Geldsystem um eine empirische Dimension:

### 6.1 Bitcoin als einzige Kryptowährung mit eigenständiger Schwingung

BTC hat eine eigenständige AC-Komponente, weil sein Wert durch einen nicht-replizierbaren Prozess entsteht:

- **Proof-of-Work**: Energiebindung als physikalische Wertbasis
- **Algorithmische Knappheit**: 21 Millionen, Halving als Taktgeber der DC-Komponente
- **Netzwerkeffekt**: Metcalfesches Gesetz, selbstverstärkend
- **Dezentralität**: Kein einzelner Impulsgeber — echte Emergenz

ResoTrade V11 bestätigt: BTC allein erzeugt +42.89% über HODL durch AC-Schwingungsextraktion. Die Schwingung ist real, eigenständig und handelbar.

Altcoins replizieren diese Eigenfrequenz nicht — sie amplifizieren sie. Das macht sie als Portfolio-Ergänzung wertlos, als Einzelinstrument aber potenziell profitabel.

### 6.2 Aktien und Fiat-Währungen als echte Resonanzpartner

Aktien repräsentieren reale Wertschöpfung: Produkte, Patente, Mitarbeiter, Cashflows. Jedes Unternehmen ist ein eigenständiger Resonator mit eigener Frequenz und eigener AC-Komponente. Fiat-Währungen werden durch die Produktivität ganzer Volkswirtschaften getrieben.

Diese Assets können mit BTC in echte Portfolio-Resonanz treten, weil sie unabhängige Eigenfrequenzen besitzen. Die Kopplung ist nicht-trivial und erzeugt handelbares Signal — bestätigt durch die Aktien-Konfiguration (+9.0% vs HODL).

### 6.3 Konsequenz für das duale Geldsystem

Das duale Resonanz-Geldsystem (BTC extern, nationale Resonanzmünze intern) erhält durch diese Analyse eine empirische Stütze:

- **BTC als externe Resonanzwährung funktioniert**, weil BTC eine eigenständige Eigenfrequenz und AC-Komponente hat
- **Altcoins sind als Reservewährung ungeeignet**, weil sie keine eigenständige Information tragen (korrekter Befund)
- **Altcoins sind als Handelsinstrument nutzbar**, weil ihre amplifizierten Schwingungen mit angepassten Schwellen handelbar sind (korrigierter Befund)
- **Nationale Währungen (gedeckt durch BIP) ergänzen BTC**, weil sie unabhängige Eigenfrequenzen besitzen

---

## 7. Warum die Unterscheidung wichtig ist

### 7.1 Das Narrativ-Problem

Die ursprüngliche Analyse formulierte: *"Altcoins sind kein eigenständiger Markt."* Das ist resonanztheoretisch korrekt im Sinne der Eigenfrequenz — aber es wurde als *"Altcoins sind Scam"* gelesen, was über die Daten hinausgeht.

Die korrigierte Formulierung unterscheidet präziser:

| Aussage | Status |
|---------|--------|
| Altcoins haben keine eigene Eigenfrequenz relativ zu BTC | ✓ Empirisch bestätigt |
| Altcoins liefern keine Diversifikation neben BTC | ✓ Empirisch bestätigt |
| Altcoins sind nicht handelbar | ✗ Voreilig — Amplitude ≠ Information |
| Altcoins als Einzelinstrument mit α-angepassten Schwellen | ○ Hypothese, noch zu validieren |

### 7.2 Was noch validiert werden muss

Die Hypothese, dass ein ResoTrade-System auf einem Altcoin-Chart (ohne BTC) profitabel arbeitet, ist theoretisch fundiert aber empirisch noch offen. Der Test wäre:

1. `AssetConfig` für ETH anlegen (engere Schwellen, höhere Volatilität)
2. `threshold_optimizer` auf ETH-Daten laufen lassen
3. Training ausschließlich auf ETH-Chart
4. Performance vergleichen mit BTC-System (normiert auf Volatilität)

Die Architektur (V11.7) unterstützt das bereits — es ist eine Konfigurationsänderung, kein Systemumbau.

### 7.3 Die Zeitdimension

Scam entlarvt sich über die Zeit, weil Rauschen nicht akkumuliert. In 100 Episoden kann eine zufällige Altcoin-Rotation profitabel erscheinen. In 200.000 Episoden konvergiert der Portfolio-Mehrwert gegen Null.

Echte Märkte dagegen stabilisieren sich: Die BTC-only Konfiguration (V11) zeigt über 10.000+ Episoden ein Einschwingverhalten — gedämpfte Oszillation mit steigendem Trend, konvergierend gegen +42.89% über HODL. Das ist das Verhalten eines resonanten Systems.

Die Amplituden-Hypothese für Altcoin-Einzelhandel müsste dasselbe Einschwingverhalten zeigen — mit höherer Volatilität der Konvergenz, aber positivem Trend.

---

## 8. Methodik-Transparenz

### 8.1 Einschränkungen

- Datenumfang: ~4.300 Stundendaten (≈ 180 Tage) — begrenzt auf den verfügbaren yfinance-Zeitraum
- Keine Berücksichtigung von Orderbuch-Tiefe und Slippage
- Simulationsumgebung, keine Live-Trades (Live-Validierung ausstehend)
- Altcoin-Auswahl auf Top-10 nach Kraken-Liquidität beschränkt
- SUI, UNI, PEPE hatten 0 Datenpunkte und wurden ausgeschlossen (11 statt 14 Assets)
- **Altcoin-Einzelhandel (ohne BTC) wurde nicht getestet** — die Portfolioanalyse ist nicht auf Einzelhandel übertragbar

### 8.2 Reproduzierbarkeit

Die Ergebnisse sind reproduzierbar:

- **Multi-Asset (V10.2):** Konfiguration unterscheidet sich nur in `asset_registry.py` (Aktien-Registry vs. Crypto-Registry). Alle anderen Parameter identisch.
- **BTC-only (V11):** `env.py` + `policy.py` mit AC/DC-Zerlegung. Training mit `python main.py 20 500`.

### 8.3 Stärke der Evidenz

| Kriterium | Bewertung |
|-----------|-----------|
| Stichprobengröße | 200.000+ Episoden (Multi-Asset), 10.000+ (BTC-only) |
| Kontrollgruppe | Ja (BTC+Aktien, BTC-only, BTC+Altcoins) |
| Lernfortschritt | Negativ bei Altcoins im Portfolio, positiv bei Aktien und BTC-only |
| Draw-Rate-Differenz | 98.4% vs. 84% vs. 49% (stark) |
| S:F Core-Cluster | 0.3:1 vs. 6.0:1 (stark) |
| Min-Wert | 0.927 vs. 1.020 (stark) |
| AC/DC-Konsistenz | V11 bestätigt eigenständige BTC-Schwingung empirisch |
| Altcoin-Einzelhandel | **Nicht getestet** — offene Hypothese |

---

## 9. Fazit

### 9.1 Bestätigter Befund

**Der Altcoin-Markt liefert keine Diversifikation zu BTC.** Altcoins sind linear abhängige Ableitungen von Bitcoin mit identischer Eigenfrequenz. In einem Multi-Asset-Portfolio neben BTC stören sie das Signal und reduzieren die Performance (von +42.89% auf +3.8%).

### 9.2 Korrigierter Befund

**Altcoins sind potenziell als Einzelinstrument handelbar.** Ihre amplifizierten Schwingungen (α > 1) erzeugen größere AC-Ausschläge, die mit angepassten Schwellen häufiger und deutlicher die Handelsschwellen überschreiten. Der `threshold_optimizer` (V11.7) kann diese Schwellen pro Asset automatisch finden.

### 9.3 Verallgemeinerung

Dieses Ergebnis betrifft zwei verschiedene Fragen:

> **Portfolio-Diversifikation erfordert verschiedene Eigenfrequenzen.** Ohne eigenständige AC-Komponente keine Phasenverschiebung, ohne Phasenverschiebung kein Informationsgewinn durch das zweite Asset.

> **Einzelhandel erfordert ausreichende Amplitude.** Ein skaliertes Echo mit α > 1 ist handelbar — es schwingt stärker, nicht anders. Die Methoden sind identisch, die Parameter ändern sich.

---

## Referenzen

- Schu, D.-R. (2025). *Resonanzfeldtheorie: Axiomatische Grundlage, Kopplungsoperator und mathematische Konsequenzen.*
- Schu, D.-R. (2025). *Duales Resonanz-Geldsystem.*
- Schu, D.-R. (2026). *Energiekugel und AC/DC-Zerlegung.* [GitHub](https://github.com/DominicReneSchu/public/blob/main/de/fakten/docs/mathematik/energiekugel.md)
- Schu, D.-R. (2026). *ResoTrade V11 — Resonanzfeldtheoretische BTC-KI mit AC/DC-Zerlegung.* (Systemdokumentation)

---

*© Dominic-René Schu, 2026 — Alle Rechte vorbehalten.*

---

⬅️ [zurück zur Übersicht](../../README.md)