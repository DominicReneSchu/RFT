import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter, FFMpegWriter
from ipywidgets import (
    FloatSlider, Dropdown, Button, Output, HBox, VBox, FloatLogSlider, IntSlider
)
from IPython.display import display, FileLink, clear_output

# Konstanten & Parameter
pi = np.pi
h = 6.626e-34
frames = 100
interval = 50  # ms, default
fps = 1000 // interval  # global FPS, jetzt leicht einstellbar

# Raumgitter
x = np.linspace(-1, 1, 400)
y = np.linspace(-1, 1, 400)
X, Y = np.meshgrid(x, y)

# UI Parameter
slider = FloatSlider(value=0.0, min=-0.7, max=0.7, step=0.01, description='Wand x₀:')
wand_breite_slider = FloatSlider(value=0.15, min=0.05, max=0.4, step=0.01, description='Wandbreite:')
omega1_slider = FloatSlider(value=2.0, min=0.5, max=6.0, step=0.1, description='f₁ [Hz]:')
omega2_slider = FloatSlider(value=3.0, min=0.5, max=6.0, step=0.1, description='f₂ [Hz]:')
intensitaet_slider = FloatLogSlider(value=10.0, base=10, min=0, max=2, step=0.01, description='Intensität:')
cmap_dropdown = Dropdown(
    options=[
        ('Viridis', 'viridis'), 
        ('Plasma', 'plasma'), 
        ('Coolwarm', 'coolwarm'),
        ('Inferno', 'inferno'),
        ('Magma', 'magma'),
        ('Cividis', 'cividis')
    ],
    value='viridis', description='Farbschema:'
)
format_dropdown = Dropdown(options=['gif', 'mp4'], value='gif', description='Format:')
fps_slider = IntSlider(value=fps, min=5, max=60, step=1, description='FPS:')
export_button = Button(description='Exportieren', button_style='success')
preview_button = Button(description='Vorschau', button_style='info')
output = Output()
preview_out = Output()

# Kopplungsfeld mit variabler Breite und Intensität
def make_epsilon(wand_center, wand_breite, intensitaet):
    epsilon = np.exp(-10 * (X**2 + Y**2))
    wand = np.exp(-((X - wand_center) / wand_breite)**2) * (np.abs(Y) < 0.9)
    epsilon += intensitaet * wand
    return epsilon

# Hauptfunktion
def animate_wand(
    wand_center=0.0, 
    wand_breite=0.15, 
    omega1=2.0, 
    omega2=3.0,
    intensitaet=10.0,
    cmap='viridis',
    fps=20,
    show=True
):
    # Umrechnung Frequenz in Kreisfrequenz
    omg1 = 2 * pi * omega1
    omg2 = 2 * pi * omega2

    epsilon = make_epsilon(wand_center, wand_breite, intensitaet)
    fig, ax = plt.subplots(figsize=(6, 5))

    def update(frame):
        t = frame / frames * 2 * pi
        f = (
            np.sin(10 * pi * X) * np.sin(10 * pi * Y) * np.sin(omg1 * t) +
            0.5 * np.sin(20 * pi * X) * np.sin(20 * pi * Y) * np.sin(omg2 * t)
        )
        E = epsilon * pi * h * f
        E_norm = E / np.max(np.abs(E))
        ax.clear()
        im = ax.contourf(X, Y, E_norm, levels=100, cmap=cmap)
        if not hasattr(ax, 'colorbar'):
            cbar = fig.colorbar(im, ax=ax, label='Energiedichte (normiert)')
            ax.colorbar = cbar
        ax.set_title(
            f'Harmonische Wandstruktur\n'
            f'x₀={wand_center:.2f}, σ={wand_breite:.2f}, '
            f'f₁={omega1:.2f}Hz, f₂={omega2:.2f}Hz, I={intensitaet:.2f}, t={t:.2f}'
        )
        ax.axis('equal')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.grid(False)
    ani = FuncAnimation(fig, update, frames=frames, interval=1000//fps, blit=False)
    if show:
        plt.show()
    return ani, fig

# Vorschau nur auf Klick
def preview_callback(_):
    with preview_out:
        clear_output()
        animate_wand(
            slider.value, wand_breite_slider.value,
            omega1_slider.value, omega2_slider.value,
            intensitaet_slider.value, cmap_dropdown.value,
            fps_slider.value, show=True
        )

# Exportfunktion
def export_callback(_):
    export_button.disabled = True
    wand_center = slider.value
    wand_breite = wand_breite_slider.value
    omega1 = omega1_slider.value
    omega2 = omega2_slider.value
    intensitaet = intensitaet_slider.value
    cmap = cmap_dropdown.value
    fmt = format_dropdown.value
    fps_val = fps_slider.value
    fname = (
        f'wand_x{wand_center:.2f}_breite_{wand_breite:.2f}_'
        f'f1_{omega1:.1f}_f2_{omega2:.1f}_I_{intensitaet:.1f}.{fmt}'
    )
    ani, fig = animate_wand(
        wand_center, wand_breite, omega1, omega2, intensitaet, cmap, fps_val, show=False
    )

    with output:
        clear_output()
        print("Export läuft… bitte warten.")

    try:
        if fmt == 'gif':
            writer = PillowWriter(fps=fps_val)
        elif fmt == 'mp4':
            writer = FFMpegWriter(fps=fps_val)
        else:
            raise ValueError("Unbekanntes Format.")

        ani.save(fname, writer=writer)
        plt.close(fig)

        with output:
            clear_output()
            print(f"✅ Export erfolgreich: {fname}")
            display(FileLink(fname))

    except Exception as e:
        with output:
            clear_output()
            print(f"❌ Export FEHLGESCHLAGEN:\n{e}")
    export_button.disabled = False

# UI Setup
export_button.on_click(export_callback)
preview_button.on_click(preview_callback)
ui = VBox([
    HBox([slider, wand_breite_slider, intensitaet_slider]),
    HBox([omega1_slider, omega2_slider, cmap_dropdown, fps_slider]),
    HBox([preview_button, format_dropdown, export_button]),
    output,
    preview_out
])

# Anzeige
display(ui)