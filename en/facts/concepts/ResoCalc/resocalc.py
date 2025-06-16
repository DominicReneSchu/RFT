import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, FloatSlider, VBox, HBox, Layout
from IPython.display import display, Markdown

def reso_sim(m=2.0, l=1.0, f_r=5.0, kopplung=0.2, theta_max=0.1):
    frequenzen = np.linspace(1, 20, 300)
    omega = 2 * np.pi * frequenzen

    # Trägheitsmomente
    J_konv = m * l**2
    J_reso = 0.5 * m * l**2

    # Konventionelles Drehmoment
    M_konv = J_konv * omega**2 * theta_max / np.sqrt(2)

    # ResoCalc-Drehmoment
    r = frequenzen / f_r
    delta = np.abs(1 - r**2)
    delta[delta < 0.0001] = 0.0001  # Singularität vermeiden
    V = 1 / delta
    M_reso = J_reso * omega**2 * V * kopplung

    # Plot
    plt.figure(figsize=(10, 6))
    plt.plot(frequenzen, M_konv, label='Konventionell', color='blue', lw=2)
    plt.plot(frequenzen, M_reso, label='ResoCalc', color='red', lw=2)
    plt.axvline(f_r, color='gray', linestyle='--', label='f_r (Resonanz)')
    plt.xlabel('Frequenz (Hz)')
    plt.ylabel('Effektives Drehmoment (Nm)')
    plt.title('Vergleich: Konventionelle Berechnung vs. ResoCalc')
    plt.legend()
    plt.grid(True, which='both', ls=':')
    plt.tight_layout()
    plt.show()

    # Optionale Zusatzinfos (korrekt als Raw-f-String für LaTeX)
    display(Markdown(
        rf"**Konventionelles Trägheitsmoment:** $J_\mathrm{{konv}} = {J_konv:.2f}\ \mathrm{{kg\,m^2}}$<br>"
        rf"**Resonanz-Trägheitsmoment:** $J_\mathrm{{reso}} = {J_reso:.2f}\ \mathrm{{kg\,m^2}}$"
    ))

# Interaktives UI mit kompaktem Layout
style = {'description_width': '90px'}
layout = Layout(width='70%')

m_slider = FloatSlider(value=2.0, min=0.1, max=10.0, step=0.1, description='Masse $m$', style=style, layout=layout)
l_slider = FloatSlider(value=1.0, min=0.1, max=5.0, step=0.1, description='Länge $l$', style=style, layout=layout)
f_r_slider = FloatSlider(value=5.0, min=1.0, max=20.0, step=0.1, description='$f_r$ [Hz]', style=style, layout=layout)
kopplung_slider = FloatSlider(value=0.2, min=0.01, max=1.0, step=0.01, description='Kopplung', style=style, layout=layout)
theta_max_slider = FloatSlider(value=0.1, min=0.01, max=1.0, step=0.01, description='$\\theta_\\mathrm{max}$', style=style, layout=layout)

ui = VBox([
    HBox([m_slider, l_slider, f_r_slider]),
    HBox([kopplung_slider, theta_max_slider])
])

interact(
    reso_sim,
    m=m_slider,
    l=l_slider,
    f_r=f_r_slider,
    kopplung=kopplung_slider,
    theta_max=theta_max_slider,
);