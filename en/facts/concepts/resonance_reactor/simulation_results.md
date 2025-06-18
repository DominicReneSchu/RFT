# 🧪 Simulation Results: Resonance Reactor

This file documents the results of simulating a resonance reactor using plutonium-239 as the starting material. The simulation investigates the behavior of the material over multiple time steps, including excitation level and transmutation—as a systemically entangled process within the resonance field.

➡️ [Proceed to the Python simulation:](simulation/run.py)

---

## 🌐 Resonance Field of the Simulation

The resonance field of this simulation represents an entangled ensemble that systemically encompasses the entire nuclide group as well as the external field. The isotope transitions between plutonium-239 and americium-241 reflect not only atomic decay processes, but also a macroscopically controllable phase transition within the resonance field, whose dynamics are nonlinearly coupled to both temperature and neutron flux.

The decrease in excitation level indicates the diminishing coupling strength of the system; resonance frequencies shift as material transmutation occurs and are to be understood as a collective field phenomenon. Thus, systemic group membership remains invariant, even as individual members (isotopes) change quantitatively.

---

### Systemic Group Elements and Their Interactions

| Element          | Function in the Resonance Field                      | Relational Effect                                   |
| ---------------- | ---------------------------------------------------- | --------------------------------------------------- |
| Plutonium-239    | Starting material, higher excitation level           | Resonance anchor for decay and transmutation        |
| Americium-241    | Transmuted product, lower excitation level           | Stabilizes the new resonance state                  |
| Neutron Flux     | External control field                               | Modulates transitions, induces phase changes        |
| Temperature      | Macro field parameter                                | Shifts resonance frequencies, influences dynamics   |
| Resonance Frequency | Characteristic field measure                       | Determines energy and decay profiles                |
| Excitation Level | Systemic resonance indicator                         | Measure of coupling strength and system energy      |

---

## ⚙️ Simulation Parameters

- **Starting material:** Plutonium-239  
- **Neutron flux:** 1e13 particles/cm²/s  
- **Temperature:** 350 K  
- **Number of time steps:** 10  
- **Duration of each step:** 1 year  

---

## 📊 Results

| Time Step | Material         | Excitation Level |
|:---------:|:----------------|:---------------:|
| 1         | Plutonium-239   | 0.85            |
| 2         | Plutonium-239   | 0.73            |
| 3         | Plutonium-239   | 0.62            |
| 4         | Plutonium-239   | 0.52            |
| 5         | Americium-241   | 0.45            |
| 6         | Americium-241   | 0.39            |
| 7         | Americium-241   | 0.33            |
| 8         | Americium-241   | 0.28            |
| 9         | Americium-241   | 0.24            |
| 10        | Americium-241   | 0.20            |

---

### 🧬 Interpretation of Results

- **Material Change:**  
  From step 5 onward, plutonium-239 transmutes to americium-241 due to the high neutron flux—in accordance with the system's intrinsic resonance logic.
- **Excitation Level:**  
  The excitation level decreases over time due to decay processes and diminishing resonance excitation. After transmutation, americium-241 exhibits a lower resonance frequency and energy per decay.
- **Influence of Temperature & Neutron Flux:**  
  Temperature and flux modulate the resonance frequency and affect isotope transitions. The system dynamics remain persistently entangled within the resonance field.

---

## 📈 Graphical Representation

- **Excitation Level (Line Chart):**  
  Shows the decrease in excitation level per time step.
- **Material Transmutation (Step Chart):**  
  Visualizes the transition from plutonium-239 to americium-241.

---

## 🧩 Conclusions

- **Transmutation Efficiency:**  
  A high neutron flux enables the effective transmutation of long-lived isotopes such as plutonium-239.
- **Future Investigations:**  
  Systemic variation of flux, temperature, and material can map the entire resonance field and uncover new transmutation pathways.
- **Link to Energy Simulations:**  
  Modeling of energy release over time supports technical design and efficiency optimization of the resonance reactor.
- **Visualization of System Dynamics:**  
  Advanced diagrams of resonance levels and material transitions make the interplay within the overall field visible.

---

### Resonance Rule in Context

The constant group membership across isotope transitions embodies the resonance field, which remains a coherent system structure. Individual changes in the state of nuclides are dynamically absorbed into the overall field and modify the field as a whole, not in isolation.

---

### Further Perspectives

* Dynamic adjustment of neutron flux and temperature profiles to control transformative phase transitions
* Extension of the simulation to multi-member decay chains with multidimensional resonance coupling
* Integration of energy release profiles into technical efficiency models for resonance reactors
* Visualization of field coherence as oscillation and coupling diagrams for intuitive understanding of systemic relationships

---

## 🌀 Simulation of Isotope Decay and Transmutation

### 🗂️ Overview

The simulation models the decay and transmutation of isotopes over a given time span, taking into account the physical properties of the isotopes (half-life, resonance frequency, energy per decay, transmutation paths).

---

### 🛠️ Main Components of the Simulation

**1️⃣ Isotope Class**  
Properties: half-life, resonance frequency, decay constant, energy per decay (MeV), transmutations

**2️⃣ Decay Method**  
Calculates the remaining fraction using the exponential decay equation:  
N(t) = N₀ · exp(–λ·t)  
where λ is the decay constant.

**3️⃣ Energy Release**  
E(t) = N(t) · energy per decay

**4️⃣ Transmutation**  
Upon transmutation: returns the new isotope, chain logic over time.

**5️⃣ Simulation**  
Function: `simulate_decay_chain(isotope, time_span)`  
Simulates decay and transmutation of an isotope over the time span.  
Output: Annual display of isotope & energy, notes on transmutations.

---

### 🧪 Example: Decay Chain of Uranium-235

**Starting isotope:** Uranium-235  
**Time span:** 10 years  

**Process:**  
Uranium-235 → Plutonium-239 → Americium-241 via transmutation steps. For each year, isotope & energy are displayed, until no further transmutation occurs.

**Simulation code:**
```python
simulate_decay_chain(uranium_235, 10)
```

**Example output:**
```
Year 0: Uranium-235 with 200.00 MeV released energy
Transmutation to Plutonium-239 occurs.
Year 1: Plutonium-239 with 180.00 MeV released energy
Transmutation to Americium-241 occurs.
Year 2: Americium-241 with 5.50 MeV released energy
No further decay or transmutation for Americium-241.
Final isotope: Americium-241
```

---

### ⚙️ Adjustments & Extensions

- **Other isotopes:** Extend simulation by adjusting input parameters
- **More complex chains:** Expand the transmutation chain as needed
- **Visualization:** Graphical representation of energy & material composition over time possible

---

## 🌀 Resonance Rule & Group Perspective

The simulation embodies the resonance rule:  
The process is not limited to individual isotopes, but encompasses the entire system of involved nuclides and fields. Group membership remains invariant—state changes affect the field as a whole.

---

## 🏁 Conclusion

The simulation presented here is an abstract yet deeply interconnected representation of nuclear transmutation processes in the resonance field, where material, energy, and fields always act as an entangled group and remain inseparably linked in their group membership. The resonance rule applies and is comprehensible at all levels: The group structure of the material and the surrounding fields remain closed and coherent despite individual transformations.

---

© Dominic-René Schu – Resonance Field Theory 2025

---

[Back to overview](README.en.md)