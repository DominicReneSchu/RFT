import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.signal import spectrogram
import pywt

st.set_page_config(page_title="Nichtlineare Resonanzanalyse", layout="wide")

st.title("Nichtlineare Resonanzanalyse (Resonanzfeldtheorie)")

# --- Parametersteuerung ---
col1, col2, col3 = st.columns(3)
with col1:
    Af = st.slider("Anregungsamplitude (Af)", 0.1, 5.0, 1.0, step=0.1)
    d0 = st.slider("Dämpfungsfaktor (d0)", 0.01, 1.0, 0.1, step=0.01)
with col2:
    omega_f = st.slider("Anregungsfrequenz (omega_f)", 0.1, 5.0, 1.0, step=0.01)
    k = st.slider("Federkonstante (k)", 0.1, 5.0, 1.0, step=0.1)
with col3:
    T = st.slider("Simulationsdauer (T)", 10, 500, 100, step=1)
    v0 = st.slider("Normgeschwindigkeit (v0)", 0.01, 5.0, 1.0, step=0.01)
dt = 0.01

# Weitere Konstanten
m = 1.0
beta = 0.05

# Dämpfungsfunktion
def schu_damping(E):
    return d0 * np.exp(-0.1 * E) / (1 + 0.05 * E**2 + 0.001 * E**4)

# Systemgleichung
def system(t, y, E):
    x, v = y
    epsilon = 1e-8
    theta = np.arctan2(v, x + epsilon)
    delta_t = beta * (v/v0)**2 * np.sin(theta)
    d = schu_damping(E)
    Ff = Af * np.cos(omega_f * t * (1 + delta_t))
    return [v, (Ff - d*v - k*x)/m]

# --- Simulation starten ---
if st.button("Start Simulation"):
    st.info("Simulation läuft...")

    # Simulation
    sol = solve_ivp(system, [0, T], [0.1, 0], args=(0,),
                    method='LSODA', t_eval=np.arange(0, T, dt))
    t_sim, x, v = sol.t, sol.y[0], sol.y[1]

    # Mechanische Energie (kinetisch + potenziell)
    E_kin = 0.5 * m * v**2
    E_pot = 0.5 * k * x**2
    E_mech = E_kin + E_pot

    # Eingebrachte Arbeit durch äußere Kraft (Resonanzfeld)
    theta_arr = np.arctan2(v, x + 1e-8)
    delta_t_arr = beta * (v/v0)**2 * np.sin(theta_arr)
    Ff_arr = Af * np.cos(omega_f * t_sim * (1 + delta_t_arr))
    W_in = np.trapz(Ff_arr * v, t_sim)

    # Mittlere mechanische Energie
    E_mech_mean = np.mean(E_mech)

    # Wirkungsgrad
    eta = E_mech_mean / W_in if W_in != 0 else np.nan

    # Zeitverlauf
    fig, axes = plt.subplots(2, 3, figsize=(18, 8))

    # Zeitreihe
    axes[0, 0].plot(t_sim, x, label="x(t)")
    axes[0, 0].set_title("Zeitverlauf x(t)")
    axes[0, 0].set_xlabel("t")
    axes[0, 0].set_ylabel("x")

    # Phasenraum
    axes[0, 1].plot(x[::10], v[::10], lw=0.3)
    axes[0, 1].set_title("Phasenraum (x vs v)")
    axes[0, 1].set_xlabel("x")
    axes[0, 1].set_ylabel("v")

    # Poincaré-Schnitt bei Anregungsphase = 0 (mod 2π)
    poincare_x, poincare_v = [], []
    for i in range(len(t_sim)):
        phase = omega_f * t_sim[i] % (2 * np.pi)
        if abs(phase) < 0.01:
            poincare_x.append(x[i])
            poincare_v.append(v[i])
    axes[0, 2].plot(poincare_x, poincare_v, 'k.', markersize=1)
    axes[0, 2].set_title("2D Poincaré-Schnitt (x vs v)")
    axes[0, 2].set_xlabel("x")
    axes[0, 2].set_ylabel("v")

    # Frequenzanalyse (FFT)
    n = len(x)
    fft = np.fft.rfft(x * np.hamming(n))
    freq = np.fft.rfftfreq(n, dt)
    axes[1, 0].semilogy(freq, np.abs(fft))
    axes[1, 0].set_xlim(0, 5)
    axes[1, 0].set_title("Frequenzspektrum")
    axes[1, 0].set_xlabel("Frequenz [Hz]")

    # Spektrogramm (STFT)
    f_spec, t_spec, Sxx = spectrogram(x, fs=1/dt, nperseg=1024, noverlap=512)
    pcm = axes[1, 1].pcolormesh(t_spec, f_spec, 10 * np.log10(Sxx + 1e-12), shading='gouraud')
    axes[1, 1].set_title('Spektrogramm')
    axes[1, 1].set_ylabel('Frequenz [Hz]')
    axes[1, 1].set_xlabel('Zeit [s]')
    fig.colorbar(pcm, ax=axes[1, 1], label='dB')

    # Wavelet-Analyse (optional, Morlet)
    try:
        scales = np.logspace(1, 3, 100)
        coeffs, freqs_cwt = pywt.cwt(x, scales, 'cmor1.5-1.0', sampling_period=dt)
        pcm_w = axes[1, 2].pcolormesh(t_sim, freqs_cwt, np.abs(coeffs), shading='gouraud')
        axes[1, 2].set_yscale('log')
        axes[1, 2].set_title('Wavelet-Skalogramm (Morlet)')
        axes[1, 2].set_ylabel('Frequenz [Hz]')
        axes[1, 2].set_xlabel('Zeit [s]')
        fig.colorbar(pcm_w, ax=axes[1, 2], label='Amplitude')
    except Exception as e:
        axes[1, 2].text(0.5, 0.5, 'Wavelet-Analyse nicht möglich:\n'+str(e),
                        ha='center', va='center', fontsize=10)
        axes[1, 2].set_axis_off()

    fig.tight_layout()
    st.pyplot(fig)

    # Wirkungsgrad ausgeben (deutlich, mit Text)
    st.markdown(f"""
    ### Wirkungsgrad der Energieübertragung

    - **Mittlere mechanische Energie:** {E_mech_mean:.4f}
    - **Eingebrachte Arbeit durch das Resonanzfeld:** {W_in:.4f}
    - **Wirkungsgrad** (mechanische Energie / eingebrachte Arbeit):  
      **η = {eta:.4%}**
    """)