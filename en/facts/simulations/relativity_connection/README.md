# Resonance Field Theory Framework

This framework provides a modular, modern infrastructure for the simulation and analysis of scalar resonance fields in flat and curved spacetime. It combines numerical methods, visualization, and scientific documentation, with a special focus on energy conservation, stability, and extensibility.

---

## Content and Motivation

**What is Resonance Field Theory?**  
Resonance Field Theory describes a scalar field (epsilon, ε) with a nonlinear potential, coupled to spacetime geometry—specifically to the Ricci scalar (R). Such fields are relevant in modern cosmology (e.g., modified gravity, inflaton models, scalar solitons, topological defects) and in field theory (domain walls, symmetry breaking).

**What can the framework do?**  
- **1D/FLRW Model:** Direct time evolution of the resonance field and the cosmological scale factor (a(t)), coupled through modified Einstein equations. Energy conservation and dynamics are monitored.
- **3D Resonance Field:** Classical lattice simulation (explicit time evolution) for nonlinear wave equations, including visualization of slices and averages. Extendable to parallel or GPU-based computation.
- **Theory, Tests, Docs:** All equations, methods, and scripts are documented and equipped with unit tests. The structure allows rapid adaptation for your own research questions.

---

## Key Insights and Highlights

- **Numerical Energy Monitoring:** The 1D/FLRW implementation checks and visualizes energy conservation as a quality measure for numerical integrity—a crucial aspect of any field simulation.
- **Flexible Modeling:** Potentials (mass, self-coupling, Mexican hat, etc.) and couplings (Ricci scalar, nonlinear) are easily adjustable, enabling a wide variety of physical scenarios.
- **Visualization & Analysis:** Live plots of fields, scale factors, and their means provide rapid insight into dynamics, stability, and pattern formation (e.g., solitons, propagation, relaxation).
- **Extensibility:** Parallel (Numba) and GPU-based (CuPy) 3D algorithms allow for larger simulations with minimal code changes. Clear separation of core logic, visualization, and control makes the framework robust and maintainable.
- **Scientific Reproducibility:** With central configuration, documented test cases, and clear scripts, the framework is ideal for collaborative research and teaching.

---

## Folder Structure

```
relativitaet_verbindung/
│
├── config.py                  # Global parameters & options
├── requirements.txt           # Python dependencies
├── README.md                  # This documentation
│
├── core/                      # Core modules: models & methods
│   ├── flrw_1d.py             # 1D/FLRW integrator
│   ├── field_3d.py            # 3D lattice field (base)
│   ├── field_3d_parallel.py   # 3D (Numba-parallelized)
│   └── field_3d_gpu.py        # 3D (GPU/CuPy)
│
├── viz/                       # Visualization modules
│   ├── plot_1d.py
│   └── plot_3d.py
│
├── run_1d.py                  # Entry script 1D simulation
├── run_3d.py                  # Entry script 3D simulation
│
└── tests/                     # Unit tests
    ├── test_flrw_1d.py
    └── test_field_3d.py
```

---

## Usage: Quickstart

1. **Installation**
   ```bash
   pip install -r requirements.txt
   ```

2. **Start 1D FLRW Simulation**
   ```bash
   python run_1d.py
   ```
   → Plots for ε(t), scale factor a(t), and energy change.

3. **Start 3D Resonance Field Simulation**
   ```bash
   python run_3d.py
   ```
   → Live visualization of slices and averages of the field.

4. **Run Tests**
   ```bash
   pytest tests/
   ```

---

## Example: Physical Scenarios and Insights

- **Cosmic Field Dynamics:**  
  How does a scalar field couple to the expansion of the universe? Which interactions dominate the dynamics?
- **Nonlinear Phenomena:**  
  How do solitons, domain walls, or relaxation phenomena emerge from the potential?
- **Numerical Stability:**  
  How do step size, potential parameters, and coupling choices affect energy conservation?
- **CPU, Parallelization, and GPU Comparison:**  
  How can the simulation be efficiently accelerated for large grids and long time evolutions?

---

## Typical Extensions

- New fields/couplings (e.g., complex fields, tensor fields)
- Extended potentials and initial conditions
- Specialized visualizations (3D volumes, animations, interactivity)
- Integration of experimental or observational data

---

## Further Reading and Background

- Scalar-tensor theories, modified gravity (e.g., Brans-Dicke, f(R) gravity)
- Nonlinear field theory, solitons, topological defects
- Cosmology and the early universe

---

*© Dominic Schu, 2025 – All rights reserved.*

---

⬅️ [back to overview](../README.md)