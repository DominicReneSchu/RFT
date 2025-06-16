import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Parameter
m = 1.0
omega1 = 1.0
omega2 = 1.02
k = 0.15  # Kopplungsstärke

def coupled_oscillators(t, y):
    x1, v1, x2, v2 = y
    dx1dt = v1
    dv1dt = -omega1**2 * x1 + (k/m)*(x2 - x1)
    dx2dt = v2
    dv2dt = -omega2**2 * x2 + (k/m)*(x1 - x2)
    return [dx1dt, dv1dt, dx2dt, dv2dt]

# Anfangswerte
y0 = [1.0, 0.0, 0.0, 0.0]  # z.B. x1(0)=1, x2(0)=0

# Zeitintervall
t_span = (0, 50)
t_eval = np.linspace(*t_span, 3000)

# Numerische Lösung
sol = solve_ivp(coupled_oscillators, t_span, y0, t_eval=t_eval)

# Plot
plt.plot(sol.t, sol.y[0], label='x1 (gekoppelt)')
plt.plot(sol.t, sol.y[2], label='x2 (gekoppelt)')
plt.xlabel('Zeit')
plt.ylabel('Amplitude')
plt.legend()
plt.title('Gekoppelte Oszillatoren')
plt.show()