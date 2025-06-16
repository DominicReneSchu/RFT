import numpy as np
import matplotlib.pyplot as plt

# --- Parameterbereich definieren ---
def init_parameter():
    return {
        "f_akteur1": 1.0,           # Frequenz Akteur 1
        "f_akteur2": 1.3,           # Frequenz Akteur 2
        "epsilon": 0.6,             # Kopplungskonstante
        "h": 1,                     # Plancksche Konstante (normiert)
        "t": np.linspace(0, 20, 2000),
        "phi1": 0.0,                # Phasenverschiebung Akteur 1
        "phi2": 0.0                 # Phasenverschiebung Akteur 2
    }

# --- Schwingung berechnen (mit Phase) ---
def berechne_schwingung(f, t, phi=0.0):
    return np.cos(2 * np.pi * f * t + phi)

# --- Resonanzfeld berechnen ---
def berechne_resonanzfeld(psi1, psi2, epsilon):
    return psi1 + epsilon * psi2

# --- Resonanzenergie nach Resonanzfeld-Gleichung ---
def schu_resonanzenergie(f1, f2, epsilon, h=1):
    return np.pi * epsilon * h * ((f1 + f2) / 2)

# --- Fourier-Analyse des Resonanzfeldes ---
def fourier_analyse(signal, t):
    n = len(t)
    dt = t[1] - t[0]
    f = np.fft.rfftfreq(n, dt)
    fft_abs = np.abs(np.fft.rfft(signal))
    return f, fft_abs

# --- Visualisierung ---
def plot_resonanzmodell(t, psi1, psi2, resonanzfeld, E_res, epsilon, f, fft_abs):
    fig, axs = plt.subplots(2, 1, figsize=(10, 8))
    axs[0].plot(t, psi1, label="Akteur 1")
    axs[0].plot(t, psi2, label="Akteur 2", alpha=0.7)
    axs[0].plot(t, resonanzfeld, label=f"Resonanzfeld (ε={epsilon})", linewidth=2, color="k")
    axs[0].set_title(f"Resonanz-KI-Modell (E_res ≈ {E_res:.2f})")
    axs[0].set_xlabel("Zeit")
    axs[0].set_ylabel("Amplitude")
    axs[0].legend()
    axs[0].grid(True)

    axs[1].plot(f, fft_abs, color="purple")
    axs[1].set_title("Fourier-Analyse des Resonanzfeldes")
    axs[1].set_xlabel("Frequenz")
    axs[1].set_ylabel("Amplitude")
    axs[1].set_xlim(0, max(f))
    axs[1].grid(True)

    plt.tight_layout()
    plt.show()

# --- Hauptfunktion ---
def main():
    p = init_parameter()
    psi1 = berechne_schwingung(p["f_akteur1"], p["t"], p["phi1"])
    psi2 = berechne_schwingung(p["f_akteur2"], p["t"], p["phi2"])
    resonanzfeld = berechne_resonanzfeld(psi1, psi2, p["epsilon"])
    E_res = schu_resonanzenergie(p["f_akteur1"], p["f_akteur2"], p["epsilon"], p["h"])
    f, fft_abs = fourier_analyse(resonanzfeld, p["t"])
    plot_resonanzmodell(p["t"], psi1, psi2, resonanzfeld, E_res, p["epsilon"], f, fft_abs)

if __name__ == "__main__":
    main()