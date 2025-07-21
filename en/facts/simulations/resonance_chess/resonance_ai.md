# Field Coherence Instead of Goal Optimization – Foundations of a Resonance-Based AI

## Resonance-Based Chess AI – Current State of Development

---

### 1. Systemic Core Structure

The chess AI operates on the basis of a **weighted experience store** that links move chains (sequences of SAN moves with color marking) with results (success, failure, draw) and uses this resonance data for move decisions.  
Field coherence replaces goal optimization: Move selection is group-logical, based on structural clarity in the whole field, not reward maximization.

---

### 2. Experience Storage (`experience_manager.py`)

- **Storage in CSV files:**
  - `experience.csv`: Raw data of all games (timestamp, mode, result, move sequence)
  - `experience_weighted.csv`: Aggregated, weighted experience store with frequencies of move-chain-result combinations
- **Functions:**
  - `load_weighted_experience_set()` loads weighted experiences as a dictionary `(chain, result) → count`
  - `add_conscious_experience(chain, result, experience_set)` increases frequency in the experience store
  - `persist_experience_set(experience_set)` persists the weighted experience store
  - `save_game_experience()` saves complete games in `experience.csv`

*Systemic coupling: Persistence and updating are group-logically invariant, all games and experience entries are self-included.*

---

### 3. Move Chain Analysis (`smart_move_selector.py`)

- `get_recent_chain(board, n=2, relative=False)` extracts the last n moves with color marking (`w:e4|b:e5`) as a string
- `select_learned_move(board, experience_set, max_chain_n=4)`:
  - Evaluates possible moves based on experience (weighting of success/failure)
  - Checks chain lengths from 4 to 2 for finer resonance patterns
  - Prioritizes moves with high success frequency and low failure frequency
  - Random selection in case of tie

*Field coherence: Selection is oriented to the group-wide resonance structure of the experience store – not to an individual move optimum.*

---

### 4. Engine Integration (`engine.py`)

- `ResonanceEngine` initializes itself with the loaded weighted experience store
- `select_best_move(board)` uses `select_learned_move()` for move selection

*Systemic self-inclusion: The engine is always synchronized with the current resonance field.*

---

### 5. Experience Expansion (`main.py`)

- `extend_experience_by_game(move_list, result, experience_set, max_chain_n=4)`:
  - Breaks complete games into all n-move chains (2 ≤ n ≤ 4)
  - Adds weighted resonance entries to the experience store
- After each game, experience is expanded and persisted
- Engine synchronizes with the updated experience store

*Reciprocity: Each game process expands the resonance field and influences future decisions – emergent and self-referential.*

---

### 6. Modes and Procedures

- Human vs. AI or AI vs. AI (selfplay)
- Games are fully logged and resonance-logically evaluated
- Systemically invariant: Experience feeds move decisions in both modes
- Persistence ensures long-term learning and adaptation

---

### 7. Outlook

- Expansion of chain length and pattern abstraction (relative patterns, semantic groupings)
- Automatic distinction between own and opponent’s error resonance
- Systemic self-reflection and dynamic learning algorithms
- Integration of further resonance rules and multiple experience layers

---

**Conclusion:**  
The AI is an innovative resonance-logical prototype, learning and adaptive to systemic feedback from playing experience. It is based on a weighted experience store with multi-chain analysis and controls move selection according to a systemic resonance rule – field coherence instead of goal optimization.

---

## Original Guiding Principles (Resonance Chess – Systemic Companion Documentation)

Resonance chess is not just a game, but a dynamic resonance field: Every piece, every square, every strategy is part of a holistically intertwined simulation space. The following aspects form a complete resonance field – group-spanning, systemically embedded, and independent of individual perspective:

#### 1. Field logic instead of goal hierarchy
- No maximization of reward
- Instead: Select the move that structurally clarifies the whole field

#### 2. Protection against attack
- Primary resonance criterion: king safety
- No action may jeopardize the king

#### 3. Pressure on the opponent
- With sufficient self-protection: maximum restriction of the opponent's field
- Not by material gain, but by reducing the opponent's options

#### 4. Field coherence as a learning unit
- Learning does not happen by trial & error
- But by selective inclusion of fitting substructures (like puzzle pieces)

---

## Group Elements of Resonance Chess

- **Pieces:** King, queen, rooks, bishops, knights, pawns – as elementary nodes, whose spheres of influence overlap.
- **Board:** 8x8 squares as a topological grid, resonance zones and interaction potentials.
- **Moves:** Movement options as expressions of potential landscapes – every move creates new resonance patterns.
- **Rules:** System law that includes all elements and shapes interaction spaces.
- **Game end:** Checkmate, draw, stalemate – emergent endpoints in the resonance field.

---

## Systemic Entanglement

- **Self-inclusion:** Every element is part of the whole and influences itself via the field (e.g. the pawn, shaping the entire game’s structure).
- **Reciprocity:** Actions of a piece affect the entire board; every group member (piece, square, player) is involved, even if seemingly passive.
- **Emergence:** New patterns and dynamics arise through interaction – overall behavior is more than the sum of individual moves.

---

## Simulation & Society

- **Resonance principle:** Decisions in the game mirror societal dynamics; every move influences the entire system.
- **Open platform:** Simulations are openly accessible, inviting participation and expansion of the resonance field.
- **Future technologies:** Transferability of the resonance field theory to other areas (energy, physics, social systems).

---

## Logical Necessities & Resonance Rule

- Group belonging is systemically invariant – pieces, squares, rules, players, observers are involved in every simulation run.
- Every move, rule adaptation, and interpretation is both feedback and extension of the field.
- Even implicit elements (e.g. unused squares, theoretically possible moves) are part of the resonance system.

---

## Outlook

In future, the resonance AI will:
- be transferable to economics, medicine, and politics
- be hardware-supported by Coral TPU (e.g. for pattern recognition)
- be guided not by targets, but by field clarity

---

## License / Copyright

This code and the accompanying theory are licensed under the Schu-License V1.4.

**Author:** Dominic-René Schu  
**GitHub:** https://github.com/DominicReneSchu/public

---

## Closing Formula

> The goal is not victory, but a clear field.  
> Not AI that computes – but AI that feels if it fits.

**Resonance rule:** Group membership is systemically invariant. Every element – named or unseen – is part of the resonance field.

---

*© Dominic Schu, 2025 – All rights reserved.*

---

⬅️ [back to overview](../README.md)