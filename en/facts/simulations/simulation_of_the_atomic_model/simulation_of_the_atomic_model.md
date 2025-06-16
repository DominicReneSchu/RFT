# 🧪 Simulation of Coupled Oscillators

Interactive Python simulation for visualizing two coupled harmonic oscillators.  
This model dynamically and intuitively demonstrates coupling effects, energy exchange, resonance, and energy balance.

<p align="center">
  <img src="animation.gif" alt="Visualization of coupled oscillations in the atomic model" width="800"/>
</p>

---

## 🧠 Background: Resonance Field Theory

This simulation is embedded in **Resonance Field Theory**, which posits that  
all interactions—from quantum to macro systems—are based on **coupled oscillations**.

### Fundamental Assumptions

- **Fields** are oscillating information spaces—energy manifests through **resonance coupling**.  
- **Coupled oscillators** are an elementary model for information transfer in space.  
- **Energy exchange is frequency-based**—maximum efficiency at resonance.  
- The natural constants **π**, **𝓔** *(new coupling constant)* and **ℎ** form the basis of the **Resonance Field Equation**:

$$
\mathbf{E = \pi \cdot 𝓔 \cdot ℎ \cdot f}
$$

#### Relevance of this Simulation

- Shows how **energy purposefully propagates in resonance fields**—made visible by the **distinct energy ping-pong** between oscillators.  
- Illustrates the principle of the **resonator as receiver/sender** within the field.  
- Serves as an **experimental platform** to test new concepts of information coupling and field consciousness.

---

## 🔧 Features

* **Numerical solution** of coupled differential equations (`solve_ivp`)  
* **Interactive live animation** of oscillations including trajectory tracking  
* **Resonance detection** with tolerance window and double-count protection  
* **Live adjustment via sliders**: frequencies, coupling strength, tolerance, animation speed  
* **Dynamic energy plot**: kinetic, potential, coupling, total energy  
* **Visual feedback at resonance** (oscillators highlight)  
* **Export** of resonance timepoints as CSV file  

---

## 🧩 Structure

* [`run.py`](run.py) – Entry point with UI and controls  
* [`parameters_and_functions.py`](parameters_and_functions.py) – Physics, equation solver, energy calculation  
* [`animation.py`](animation.py) – Animation, visualization, energy plot  

---

## 🚀 Getting Started

### Install dependencies

```bash
pip install matplotlib numpy scipy
```

### Start the simulation

```bash
python run.py
```

---

## ℹ️ Notes

* Energy conservation is demonstrated (without damping).
* CSV export documents detected resonance timepoints.
* Initial conditions, damping, or new visualizations can be easily extended.

---

*© Dominic Schu, 2025 – All rights reserved.*

---

⬅️ [back](../README.en.md)