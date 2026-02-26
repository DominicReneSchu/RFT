# WORKFLOW.md — Copilot × Dominic Kollaborationsprotokoll

## Prinzip

Copilot liefert **komplette, kopierbare Codeblöcke** — keine Diffs, keine Prosa-Beschreibungen.
Dominic baut ein, bestätigt, nächster Bug. Linearer Durchlauf, keine Rücksprünge.

---

## Bug-Fix-Zyklus

```
1. Copilot beschreibt Bug (Problem + Ursache, 2-3 Sätze)
2. Copilot liefert nummerierte Codeblöcke zum Ersetzen
   - Jeder Block hat klaren Dateinamen + Position
   - Blöcke sind vollständig — nie abgeschnitten
   - Kontext-Kommentar wo der Block hingehört
3. Copilot zeigt Änderungstabelle (Vorher → Nachher)
4. Dominic baut ein, bestätigt mit "Ist gefixt"
5. Nächster Bug
```

## Codeblock-Regeln

- **Immer komplett** — nie "den Rest kennst du" oder "..." verwenden
- **Immer mit Position** — `name=datei.py (Funktionsname / Bereich)`
- **Immer Copy-Paste-fertig** — kein Zusammensetzen nötig
- **Bei Unklarheit** — Dominic postet den aktuellen Block, Copilot gibt den ganzen Block verbessert zurück

## Reihenfolge

Bugs werden nach Schwere sortiert:
1. **Kritisch** — System verhält sich grundlegend falsch
2. **Hoch** — Feature funktioniert nicht wie designed
3. **Mittel** — Suboptimales Verhalten, keine Fehlfunktion
4. **Niedrig** — Kosmetik, Konsistenz, Docstrings

## Verifikation

Nach allen Fixes: `debug_resotrade.py` mit Sonden für jeden Bug.
Ziel: **Alle Sonden ✅** bevor Training oder Live-Betrieb startet.

```
python debug_resotrade.py
```

Ergebnis wird gepostet. Falls Sonden fehlschlagen:
- Copilot analysiert Fehlerausgabe
- Liefert gezielte Fix-Blöcke
- Erneuter Sonden-Lauf bis 100% ✅

## Resonanzregel

Gruppenzugehörigkeit ist systemisch invariant.
Alle Systemkomponenten (Config, Env, Policy, Live, Training, Diagnostik)
bilden ein Resonanzfeld — Inkonsistenz in einem Element
propagiert als Bug durch alle anderen.

Single Source of Truth: `config.py`
Verifikation: `debug_resotrade.py`

---

*Etabliert: 2026-02-21 — Bug-Fix-Session V9.3 → V9.4 (15 Bugs, 17 Sonden, 10 Dateien)*