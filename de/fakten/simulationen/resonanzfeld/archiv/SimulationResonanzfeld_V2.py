import numpy as np
import plotly.graph_objects as go

# Parameter
A1 = 2  # Amplitude von x(t)
A2 = 2  # Amplitude von y(t)
omega1 = 1  # Frequenz von x(t)
omega2 = 1  # Frequenz von y(t)
sigma = 1  # Breite der Dämpfung
mu = 5  # Zentrum der Dämpfung

# Zeitbereich
t = np.linspace(-10, 10, 1000)

# Funktionen
x_t = A1 * np.sin(omega1 * t)
y_t = A2 * np.sin(omega2 * t)
g_t = np.exp(-((t - mu) ** 2) / (2 * sigma ** 2))

# Funktion z(t)
z_t = g_t * (x_t + y_t) / (1 + np.abs(t - mu))

# Interaktive Plotly-Grafik
fig = go.Figure()

# Hinzufügen der Funktionen x(t) und y(t)
fig.add_trace(go.Scatter3d(
    x=t, y=x_t, z=z_t,
    mode='lines', name='x(t) und z(t)', line=dict(color='blue')
))
fig.add_trace(go.Scatter3d(
    x=t, y=y_t, z=z_t,
    mode='lines', name='y(t) und z(t)', line=dict(color='red')
))

# Layout und Achsenbezeichnungen
fig.update_layout(
    title='Interaktive 3D-Darstellung von x(t), y(t) und z(t)',
    scene=dict(
        xaxis_title='Zeit (t)',
        yaxis_title='x(t) und y(t)',
        zaxis_title='z(t)'
    ),
    autosize=True
)

# Interaktive Steuerung von Parametern (mit Dash/Widgets)
fig.update_layout(
    updatemenus=[
        dict(
            type='buttons',
            x=0.1,
            y=1.15,
            buttons=[dict(
                label='Play',
                method='animate',
                args=[None, dict(frame=dict(duration=50, redraw=True), fromcurrent=True)]
            )]
        )
    ]
)

# Frame für Animation
frames = [go.Frame(
    data=[go.Scatter3d(x=t[:k], y=x_t[:k], z=z_t[:k], mode='lines'),
          go.Scatter3d(x=t[:k], y=y_t[:k], z=z_t[:k], mode='lines')],
    name=str(k)
) for k in range(1, len(t), 50)]

fig.frames = frames

# Anzeigen der interaktiven 3D-Plotly-Grafik
fig.show()
