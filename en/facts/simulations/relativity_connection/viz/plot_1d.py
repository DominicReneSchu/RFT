import matplotlib.pyplot as plt

def plot_1d_results(sol, V):
    eps, epsdot, a = sol.y[0], sol.y[1], sol.y[2]
    rho_eps = 0.5*epsdot**2 + V(eps)
    energie_gesamt = rho_eps * a**3
    plt.figure(figsize=(14,4))
    plt.subplot(131)
    plt.plot(sol.t, eps)
    plt.xlabel("t"); plt.ylabel("ε")
    plt.title("Resonanzfeld ε(t)")
    plt.subplot(132)
    plt.plot(sol.t, a)
    plt.xlabel("t"); plt.ylabel("a")
    plt.title("Skalenfaktor a(t)")
    plt.subplot(133)
    plt.plot(sol.t, (energie_gesamt-energie_gesamt[0])/energie_gesamt[0])
    plt.xlabel("t"); plt.ylabel("ΔE/E₀")
    plt.title("Relative Energieänderung")
    plt.tight_layout()
    plt.show()