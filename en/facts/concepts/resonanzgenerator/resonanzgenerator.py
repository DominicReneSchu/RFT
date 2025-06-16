import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import rfft, rfftfreq
from tqdm import tqdm

# --- Systemparameter ---
m = 0.1
k = 10
d = 0.05
x0 = 0.01
v0 = 0.0

# --- Schu-Resonanzfeldparameter ---
pi = np.pi
e_tilde = 1.0            # Resonanzkopplungskonstante
h = 6.626e-34            # Planck-Konstante
alpha = 5.0              # Lokalisierung des Feldes
phi = 0                  # Phasenverschiebung
v_feld = 1.0             # Ausbreitungsgeschwindigkeit des Feldes (optional)
use_propagation = False  # True: Raum-Zeit-Kopplung, False: statisch

# --- Sweep-Parameter ---
dt = 0.001
t_max = 5
t_array = np.arange(0, t_max, dt)

f_min = 0.5
f_max = 5.0
n_f = 80
frequencies = np.linspace(f_min, f_max, n_f)

max_amplitudes = np.zeros(n_f)
max_amplitudes_ref = np.zeros(n_f)
delta_E = np.zeros(n_f)
E_field_input_end = np.zeros(n_f)

# --- Resonanzfeld-Gleichung für das Resonanzfeld ---
def F_resonanzfeld(x, t, omega_mag):
    # Resonanzfeld-Gleichung: F = π · ℯ̃ · ℎ · ω · cos(phase) · exp(-α x²)
    if use_propagation:
        phase = omega_mag * (t - x / v_feld) - phi  # Raum-Zeit-Kopplung
    else:
        phase = omega_mag * t - phi                 # Nur zeitliche Schwingung
    f_xt = np.cos(phase) * np.exp(-alpha * x**2)
    return pi * e_tilde * h * omega_mag * f_xt

# --- Sweep ---
for idx, f_field in enumerate(tqdm(frequencies, desc="Schu-Resonanzfeld Sweep")):
    omega_mag = 2 * np.pi * f_field

    # --- Mit Resonanzfeld ---
    x = x0
    v = v0
    x_array = np.zeros_like(t_array)
    v_array = np.zeros_like(t_array)
    E_kin = np.zeros_like(t_array)
    E_pot = np.zeros_like(t_array)
    E_power = np.zeros_like(t_array)
    for i, t in enumerate(t_array):
        F_field = F_resonanzfeld(x, t, omega_mag)
        F_feder = -k * x
        F_dämpfung = -d * v
        F_gesamt = F_field + F_feder + F_dämpfung
        a = F_gesamt / m
        v += a * dt
        x += v * dt
        x_array[i] = x
        v_array[i] = v
        E_kin[i] = 0.5 * m * v**2
        E_pot[i] = 0.5 * k * x**2
        E_power[i] = F_field * v

    # --- Ohne Resonanzfeld (Referenz) ---
    x_ref = x0
    v_ref = v0
    xref_array = np.zeros_like(t_array)
    for i, t in enumerate(t_array):
        F_feder = -k * x_ref
        F_dämpfung = -d * v_ref
        F_gesamt = F_feder + F_dämpfung
        a = F_gesamt / m
        v_ref += a * dt
        x_ref += v_ref * dt
        xref_array[i] = x_ref

    # Analyse für diese Frequenz
    start_idx = int(0.5/dt)
    max_amplitudes[idx] = np.max(np.abs(x_array[start_idx:]))
    max_amplitudes_ref[idx] = np.max(np.abs(xref_array[start_idx:]))
    delta_E[idx] = (E_kin[-1] + E_pot[-1]) - (0.5 * m * v_ref**2 + 0.5 * k * x_ref**2)
    E_field_input_end[idx] = np.sum(E_power) * dt

# --- Resonanzmaximum finden ---
resonanz_idx = np.argmax(max_amplitudes)
resonanz_freq = frequencies[resonanz_idx]
halbwert = max_amplitudes[resonanz_idx] / np.sqrt(2)

def find_halfwidth(frequencies, amplitudes, peak_idx, halbwert):
    left = peak_idx
    while left > 0 and amplitudes[left] > halbwert:
        left -= 1
    f1 = np.interp(halbwert, [amplitudes[left], amplitudes[left+1]], [frequencies[left], frequencies[left+1]])
    right = peak_idx
    while right < len(amplitudes)-1 and amplitudes[right] > halbwert:
        right += 1
    f2 = np.interp(halbwert, [amplitudes[right-1], amplitudes[right]], [frequencies[right-1], frequencies[right]])
    return f1, f2

f1, f2 = find_halfwidth(frequencies, max_amplitudes, resonanz_idx, halbwert)
Q = resonanz_freq / (f2 - f1) if (f2 - f1) > 0 else np.nan

# --- Plots ---
plt.figure(figsize=(10, 4))
plt.plot(frequencies, max_amplitudes, label='Max. Amplitude (Schu-Resonanzfeld)')
plt.plot(frequencies, max_amplitudes_ref, '--', label='Referenz (ohne Feld)')
plt.axvline(resonanz_freq, color='r', linestyle=':', label=f'Resonanz: {resonanz_freq:.2f} Hz')
plt.xlabel('Feldfrequenz [Hz]')
plt.ylabel('Maximale Auslenkung [m]')
plt.title('Resonanzkurve (Schu-Resonanzfeld)')
plt.grid(True)
plt.legend()
plt.yscale("log")
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 4))
plt.plot(frequencies, delta_E, label='ΔE = E_gesamt - E_ref (Endzeit)')
plt.plot(frequencies, E_field_input_end, '--', label='Integrierte Feldarbeit')
plt.plot(frequencies, delta_E / (E_field_input_end + 1e-30), ':', label='Effizienz ΔE/Feldarbeit')
plt.axvline(resonanz_freq, color='r', linestyle=':', label=f'Resonanz: {resonanz_freq:.2f} Hz')
plt.xlabel('Feldfrequenz [Hz]')
plt.ylabel('Energie [J]')
plt.title('Energieanalyse & Effizienz (Schu-Resonanzfeld)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

print(f"Resonanzfrequenz: {resonanz_freq:.4f} Hz, Q-Faktor: {Q:.1f}")

# --- Detailanalyse am Resonanzpunkt ---
omega_mag = 2 * np.pi * resonanz_freq
x = x0
v = v0
x_array = np.zeros_like(t_array)
v_array = np.zeros_like(t_array)
E_kin = np.zeros_like(t_array)
E_pot = np.zeros_like(t_array)
E_power = np.zeros_like(t_array)
for i, t in enumerate(t_array):
    F_field = F_resonanzfeld(x, t, omega_mag)
    F_feder = -k * x
    F_dämpfung = -d * v
    F_gesamt = F_field + F_feder + F_dämpfung
    a = F_gesamt / m
    v += a * dt
    x += v * dt
    x_array[i] = x
    v_array[i] = v
    E_kin[i] = 0.5 * m * v**2
    E_pot[i] = 0.5 * k * x**2
    E_power[i] = F_field * v
E_field_input = np.cumsum(E_power) * dt

plt.figure(figsize=(10, 4))
plt.plot(t_array, x_array, label='x(t)')
plt.xlabel('Zeit [s]')
plt.ylabel('Auslenkung [m]')
plt.title(f'Auslenkung am Resonanzpunkt ({resonanz_freq:.2f} Hz)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 4))
plt.plot(t_array, E_kin + E_pot, label='Gesamtenergie')
plt.plot(t_array, E_kin, '--', label='Kinetische Energie')
plt.plot(t_array, E_pot, '--', label='Potenzielle Energie')
plt.plot(t_array, E_field_input, ':', label='Energiezufuhr Schu-Feld')
plt.xlabel('Zeit [s]')
plt.ylabel('Energie [J]')
plt.title('Energieverlauf am Resonanzpunkt')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

N = len(t_array)
xf = rfftfreq(N, dt)
Xf = np.abs(rfft(x_array))
plt.figure(figsize=(10, 4))
plt.plot(xf, Xf)
plt.xlabel('Frequenz [Hz]')
plt.ylabel('Amplitude')
plt.title('Frequenzspektrum x(t) am Resonanzpunkt')
plt.xlim(0, 10)
plt.grid(True)
plt.tight_layout()
plt.show()