from __future__ import annotations

import numpy as np
import plotly.graph_objects as go

# Parameters
A1 = 2  # Amplitude of x(t)
A2 = 2  # Amplitude of y(t)
omega1 = 1  # Frequency of x(t)
omega2 = 1  # Frequency of y(t)
sigma = 1  # Width of damping
mu = 5  # Centre of damping

# Time range
t = np.linspace(-10, 10, 1000)

# Functions
x_t = A1 * np.sin(omega1 * t)
y_t = A2 * np.sin(omega2 * t)
g_t = np.exp(-((t - mu) ** 2) / (2 * sigma ** 2))

# Function z(t)
z_t = g_t * (x_t + y_t) / (1 + np.abs(t - mu))

# Interactive Plotly figure
fig = go.Figure()

# Add functions x(t) and y(t)
fig.add_trace(go.Scatter3d(
    x=t, y=x_t, z=z_t,
    mode='lines', name='x(t) and z(t)', line=dict(color='blue')
))
fig.add_trace(go.Scatter3d(
    x=t, y=y_t, z=z_t,
    mode='lines', name='y(t) and z(t)', line=dict(color='red')
))

# Layout and axis labels
fig.update_layout(
    title='Interactive 3D Representation of x(t), y(t) and z(t)',
    scene=dict(
        xaxis_title='Time (t)',
        yaxis_title='x(t) and y(t)',
        zaxis_title='z(t)'
    ),
    autosize=True
)

# Interactive parameter control (with Dash/Widgets)
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

# Frames for animation
frames = [go.Frame(
    data=[go.Scatter3d(x=t[:k], y=x_t[:k], z=z_t[:k], mode='lines'),
          go.Scatter3d(x=t[:k], y=y_t[:k], z=z_t[:k], mode='lines')],
    name=str(k)
) for k in range(1, len(t), 50)]

fig.frames = frames

# Show the interactive 3D Plotly figure
fig.show()
