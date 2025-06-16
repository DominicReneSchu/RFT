import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, FloatSlider, Dropdown
from fractions import Fraction
from IPython.display import display, Math

def simulate_resonance(
    f1=2.0, f2=3.0, epsilon=0.5, t_max=10,
    use_eta=False, eta=1e-33,
    coupling_type='linear'
):
    """Simuliert die Resonanzfeldkopplung mit wählbarer Nichtlinearität und Formelanzeige."""
    
    # Konstante: Planck oder η
    h = 6.626e-34 if not use_eta else eta
    
    # Verhältnis und Resonanzprüfung
    if f2 == 0:
        n, m = 0, 1
    else:
        ratio = Fraction(f1 / f2).limit_denominator(10)
        n, m = ratio.numerator, ratio.denominator
    is_resonant = np.isclose(f1 / f2, n / m, rtol=1e-2)
    
    # Resonanzfeld-Gleichung
    E = np.pi * epsilon * h * (f1 + f2)
    
    # Zeit und Schwingungen
    t = np.linspace(0, t_max, 1000)
    psi1 = np.cos(2 * np.pi * f1 * t)
    psi2 = np.cos(2 * np.pi * f2 * t)
    psi_total = psi1 + psi2

    # Energieübertragung je nach Kopplungsart
    if coupling_type == 'linear':
        energy_transfer = epsilon * (psi1 * psi2)
    elif coupling_type == 'quadratisch':
        energy_transfer = epsilon * (psi1**2 * psi2)
    elif coupling_type == 'trigonometrisch':
        energy_transfer = epsilon * np.sin(psi1) * np.sin(psi2)
    else:
        energy_transfer = np.zeros_like(t)
    
    # Gedämpft (optional)
    energy_transfer *= np.exp(-0.1 * t)

    # Plot
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
    ax1.plot(t, psi1, label=f'Oszillator 1: $f_1$ = {f1:.1f} Hz')
    ax1.plot(t, psi2, label=f'Oszillator 2: $f_2$ = {f2:.1f} Hz')
    ax1.plot(t, psi_total, 'k--', alpha=0.5, label='Superposition')
    ax1.text(0.02, 0.9, f'Resonanz: {is_resonant}', transform=ax1.transAxes,
             bbox=dict(facecolor='yellow' if is_resonant else 'lightgray', alpha=0.5))
    ax1.set_xlabel('Zeit [s]')
    ax1.set_ylabel('Amplitude')
    ax1.legend()

    ax2.plot(t, energy_transfer, 'r-', label='Energieübertragung')
    ax2.axhline(E, color='g' if is_resonant else 'gray', linestyle='--',
                label=f'Schu-Energie: $E = {E:.2e}$ J')
    ax2.set_xlabel('Zeit [s]')
    ax2.set_ylabel('Energie [J]')
    ax2.legend()
    plt.tight_layout()
    plt.show()

    # Formelanzeige
    kopplungsformeln = {
        'linear': r"E_\mathrm{trans} = \varepsilon \cdot \psi_1 \cdot \psi_2",
        'quadratisch': r"E_\mathrm{trans} = \varepsilon \cdot \psi_1^2 \cdot \psi_2",
        'trigonometrisch': r"E_\mathrm{trans} = \varepsilon \cdot \sin(\psi_1) \cdot \sin(\psi_2)"
    }
    formel = kopplungsformeln.get(coupling_type, r"E_\mathrm{trans} = 0")
    display(Math(r"\text{Kopplungsform: } " + formel))

# Interaktive Steuerung
interact(
    simulate_resonance,
    f1=FloatSlider(min=0.1, max=5.0, step=0.1, value=2.0),
    f2=FloatSlider(min=0.1, max=5.0, step=0.1, value=3.0),
    epsilon=FloatSlider(min=0.0, max=1.0, step=0.05, value=0.5),
    t_max=FloatSlider(min=1.0, max=20.0, step=1.0, value=10),
    use_eta=False,
    eta=FloatSlider(min=1e-35, max=1e-30, step=1e-34, value=1e-33, readout_format='.1e'),
    coupling_type=Dropdown(options=['linear', 'quadratisch', 'trigonometrisch'], value='linear')
);
