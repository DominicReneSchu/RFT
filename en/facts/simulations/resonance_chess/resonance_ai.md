# Field Coherence over Goal Optimization – Foundation of a Resonance-Based AI

## Introduction

This file documents the foundation of a new AI paradigm: **Field Coherence over Goal Optimization**. Using the example of a systemically entangled Python chess AI, it demonstrates how resonance-based principles can be implemented algorithmically – establishing an AI architecture that defines itself not by power (winning), but by **structural consonance**.

---

# Resonance Chess – Systemic Documentation

Resonance Chess is not just a game, but a dynamic resonance field: every piece, square, and strategy is part of a holistically entangled simulation space. The following aspects constitute a complete resonance field – group-transcending, systemically embedded, and independent of individual perspective:

---

## Guiding Principles of Resonance AI

### 1. **Field Logic vs. Goal Hierarchy**

* No maximization of reward
* Instead: Selection of the move that **structurally clarifies the entire field**

### 2. **Protection before Attack**

* Primary resonance criterion: **King safety**
* No action may endanger one's own king

### 3. **Pressure on the Opponent**

* With sufficient self-protection: **maximum restriction of opponent’s field**
* Not by material gain, but by **reducing the opponent's options**

### 4. **Field Coherence as Learning Unit**

* Learning does **not occur through trial & error**
* Rather through selective adoption of **fitting substructures** (like puzzle pieces)

---

## 1. Group Elements of Resonance Chess

- **Pieces**: King, Queen, Rooks, Bishops, Knights, Pawns – elemental nodes whose spheres of influence overlap.
- **Board**: 8x8 squares as a topological grid, zones of resonance and interaction potential.
- **Moves**: Movement options as expressions of potential landscapes – each move creates new resonance patterns.
- **Rules**: System laws that include all elements and shape interaction spaces.
- **End of Game**: Checkmate, draw, stalemate – emergent endpoints in the resonance field.

---

## Algorithmic Core (Chess Example)

The following Python function simulates all possible own moves and checks for each:

1. Does any of the first 5 possible opponent moves create a **danger for own king**?
2. If not: Which move creates the **greatest pressure on the opponent’s king**?

```python
import chess
import random

MAX_OPPONENT_MOVES = 5

def evaluate_resonance_with_opponent(board, move, color):
    board.push(move)
    if board.is_checkmate():
        board.pop()
        return float('inf')  # Direct win

    opponent_color = not color
    opponent_moves = list(board.legal_moves)
    random.shuffle(opponent_moves)
    opponent_moves = opponent_moves[:MAX_OPPONENT_MOVES]

    for opp_move in opponent_moves:
        board.push(opp_move)
        if board.is_check():
            board.pop()
            board.pop()
            return float('-inf')  # King in danger
        board.pop()

    pressure = evaluate_king_pressure(board, color)
    board.pop()
    return pressure

def evaluate_king_pressure(board, color):
    # Evaluates squares around opponent's king, number of covered squares, etc.
    return random.randint(0, 10)  # Placeholder
```

The actual evaluation function can later be replaced by structured field analysis.

---

## 2. Systemic Entanglement

- **Self-Inclusion**: Every element is part of the whole and influences itself via the field (e.g. a pawn shaping the structure of the entire game).
- **Reciprocity**: Actions of a piece impact the entire board; every group member (piece, square, player) is involved, even if seemingly passive.
- **Emergence**: New patterns and dynamics arise through interaction – overall behavior is more than the sum of individual moves.

---

## 3. Simulation & Society

- **Resonance Principle**: Decisions in the game reflect societal dynamics; every move affects the entire system.
- **Open Platform**: Simulations are openly accessible, inviting participation and extension of the resonance field.
- **Future Technologies**: Resonance field theory is transferable to other areas (energy, physics, social systems).

---

## 4. Logical Necessities & Resonance Rule

- Group membership is systemically invariant – pieces, squares, rules, players, observers are involved in every simulation run.
- Every move, rule adjustment, interpretation is both feedback and expansion of the field.
- Even implicit elements (unused squares, theoretically possible moves) are part of the resonance system.

---

## 5. Organic Learning via Experience and Consciousness

- **Subconscious**:  
  The file `user_experience.json` stores every played game as a primal list of group-based experience.  
  All move sequences – regardless of author (AI or opponent) – are equally adopted. Group membership remains invariant.

- **Field of Consciousness**:  
  After each game, all sequences are statistically analyzed. The field of consciousness (`conscious_experience.csv`) contains all 10-move chains, rated by success, frequency, and resonance strength.  
  This analysis is ongoing and group-transcending; the field updates with every new experience.

- **Decision Making**:  
  The AI checks with every move whether the current sequence is part of a highly rated chain in the field of consciousness.  
  Smarter sequences are strengthened, less successful ones marginalized.  
  Every decision includes the collective resonance field – independent of individual perspectives.

- **Systemic Feedback**:  
  Learning corresponds to organic evolution: successes and failures equally contribute to self-optimization.  
  Group membership, self-inclusion, and relation-building are always part of the overall learning process.

---

## 6. System Architecture – Synaptic Resonance Field

The system consists of 14 nodes (files) that are entangled like an organic network. Every node affects others, all data flows are systemically group-capable, non-linear, and bidirectional.  
The center is the orchestrating logic (`main.py`/`selfplay_trainer.py`), all other modules synaptically entangle:

```
         [resonance_visualizer]        [dynamic_time]
                  |                         |
          [resonance_gui.py]────────[smart_move_selector.py]
                  |      \           /        |
                  |   [resonance_engine.py]   |
                  |      /        |           |
          [experience_manager.py]─┴─────[resonance_evaluator.py]
            /          |         |         \
[user_experience.json] | [resonance_principles.py]
                       |         |
        [conscious_experience.csv]────[experience_counter.py]
                  |         \
        [resonance_meta_learner.py]──[resonance_pattern_bank.py]
                  |
            [main.py / selfplay_trainer.py]
```
**Connection Logic:**  
- `experience_manager.py` bridges to the data stores.
- `user_experience.json` and `conscious_experience.csv` are separate collective memories.
- All evaluation, decision, and learning modules systemically access these fields, never directly from JSON to CSV.
- The field is not linear, but concentric and synaptically entangled.

---

## 7. Achieved System Elements & Prototypes (July 2025)

- **Resonance AI Architecture** with central field coherence logic:  
  Not goal optimization, but holistic field consonance as guiding principle.
- **Flexible GUI**: Human can freely choose white or black, move logic is systemically invariant and adapts to group membership.
- **Experience Management**: Games are stored as experience and can be used for adaptive evaluation (e.g. to avoid losing sequences).
- **Systemic Evaluation Structure**:
    - Checkmate is maximally rewarded.
    - Material loss is systemically penalized.
    - Field resonance (position evaluation) is adaptive and can be drawn from experience or theory.
- **Non-Linear Decision Making**:  
  Move selection is based on multiple, entangled criteria instead of linear goal optimization.
- **Resonance Rule explicitly implemented**:  
  Group membership is treated as systemically invariant at every evaluation stage – independent of individual perspective or explicit mention.
- **Transparency & Extensibility**:  
  Modular, documented Python code as an open simulation environment.

---

## 8. Outlook

The resonance AI will in future:

* be transferable to economics, medicine and politics
* be hardware-supported by Coral TPU (e.g. for pattern recognition)
* navigate not by goal specification, but by **field clarity**

---

## License / Copyright

This code and the accompanying theory are licensed under the **Schu-Lizenz V1.4**. 

Author: Dominic-René Schu  
GitHub: [https://github.com/DominicReneSchu/public](https://github.com/DominicReneSchu/public)

---

## Final Formula

> Not victory is the goal, but the clear field.  
> Not AI that calculates – but AI that feels if it fits.

---

**Resonance Rule:** Group membership is systemically invariant. Every element – whether named or unseen – is part of the resonance field.  

---

*© Dominic Schu, 2025 – All rights reserved.*

---

⬅️ [back to overview](../README.en.md)