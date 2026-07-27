import numpy as np
from scipy.stats import binomtest
from statsmodels.stats.multitest import multipletests
from sklearn.neighbors import KernelDensity
from typing import Callable, Dict, List, Tuple, Optional, Any


def create_kde_sampler(
    background_data: np.ndarray, bandwidth: float = 0.05
) -> Callable[[int], np.ndarray]:
    """
    Erstelle eine Sampling-Funktion für den Hintergrund basierend auf
    Kernel-Density-Estimate (KDE).
    """
    background_data = np.asarray(background_data).reshape(-1, 1)
    kde = KernelDensity(kernel="gaussian", bandwidth=bandwidth)
    kde.fit(background_data)

    def sampler(size: int) -> np.ndarray:
        return kde.sample(size).flatten()

    return sampler


def create_kde_model(
    background_data: np.ndarray, bandwidth: float = 0.05
) -> KernelDensity:
    """
    Erstelle ein KDE-Modell für die Hintergrunddichte.
    """
    background_data = np.asarray(background_data).reshape(-1, 1)
    kde = KernelDensity(kernel="gaussian", bandwidth=bandwidth)
    kde.fit(background_data)
    return kde


def expected_rate_from_kde(
    kde: KernelDensity, m0: float, delta: float, n_points: int = 50
) -> float:
    """
    Berechne die erwartete Trefferrate im Fenster [m0-delta, m0+delta]
    aus dem KDE-Hintergrundmodell durch numerische Integration (Trapez).
    """
    x_grid = np.linspace(m0 - delta, m0 + delta, n_points).reshape(-1, 1)
    log_density = kde.score_samples(x_grid)
    density = np.exp(log_density)
    rate = float(np.trapz(density, x_grid.flatten()))
    rate = min(max(rate, 1e-10), 1.0 - 1e-10)
    return rate


def precompute_expected_rates(
    kde: KernelDensity,
    m0_values: List[float],
    deltas: List[float],
) -> Dict[float, Dict[float, float]]:
    """
    Vorberechnung aller erwarteten Raten für jede Kombination (M₀, Δ).

    Wird einmal vor der Monte-Carlo-Schleife aufgerufen und eliminiert
    redundante KDE-Integrationen in den Simulationsdurchläufen.

    Rückgabe: {m0: {delta: rate}}
    """
    rates = {}
    for m0 in m0_values:
        rates[m0] = {}
        for delta in deltas:
            rates[m0][delta] = expected_rate_from_kde(kde, m0, delta)
    return rates


def correct_pvalues(
    p_values: List[float],
    multitest_methods: Tuple[str, ...] = ("bonferroni", "fdr_bh"),
) -> Dict[str, np.ndarray]:
    """
    Korrigiere eine Liste von p-Werten mit mehreren Multiple-Testing-Methoden.
    """
    pval_corrs = {}
    for mt in multitest_methods:
        _, pvals_corr, _, _ = multipletests(p_values, alpha=0.05, method=mt)
        pval_corrs[mt] = pvals_corr
    return pval_corrs


def resonance_analysis(
    data: np.ndarray,
    m0_values: List[float],
    deltas: List[float],
    n_total: int,
    expected_rates: Dict[float, Dict[float, float]],
    multitest_methods: Tuple[str, ...] = ("bonferroni", "fdr_bh"),
) -> Tuple[
    Dict[float, Dict[str, Any]], Dict[float, List[int]], Dict[float, List[float]]
]:
    """
    Resonanzfenster-Analyse mit vorberechneten erwarteten Raten.

    Parameter
    ---------
    data : np.ndarray
        Messdaten (invariante Massen).
    m0_values : List[float]
        Resonanzmassenstellen M₀.
    deltas : List[float]
        Fensterbreiten (halbe Breite).
    n_total : int
        Gesamtzahl der Ereignisse.
    expected_rates : Dict[float, Dict[float, float]]
        Vorberechnete erwartete Raten {m0: {delta: rate}}.
    multitest_methods : Tuple[str, ...]
        Methoden für Multiple-Testing-Korrektur.
    """
    results: Dict[float, Dict[str, Any]] = {}
    all_hits: Dict[float, List[int]] = {}
    all_pvals: Dict[float, List[float]] = {}

    for m0 in m0_values:
        p_values: List[float] = []
        hits_list: List[int] = []

        for delta in deltas:
            hits = int(np.sum((data > m0 - delta) & (data < m0 + delta)))
            rate = expected_rates[m0][delta]
            test = binomtest(hits, n_total, rate, alternative="greater")
            p_values.append(test.pvalue)
            hits_list.append(hits)

        pval_corrs = correct_pvalues(p_values, multitest_methods)
        best_idx = int(np.argmin(pval_corrs[multitest_methods[0]]))

        results[m0] = {
            "best_delta": deltas[best_idx],
            "hits": hits_list[best_idx],
            "p_raw": p_values[best_idx],
            "p_corr": pval_corrs["bonferroni"][best_idx],
            "hits_list": hits_list,
            "pvals": p_values,
            "pvals_corr": pval_corrs,
        }
        all_hits[m0] = hits_list
        all_pvals[m0] = p_values

    return results, all_hits, all_pvals


def bootstrap_hits(
    data: np.ndarray,
    m0: float,
    delta: float,
    n_bootstrap: int = 5000,
) -> Tuple[float, float, float]:
    """
    Bootstrap-Konfidenzintervall für Trefferzahl.
    Rückgabe: (median, 16%-Perzentil, 84%-Perzentil)
    """
    n = len(data)
    hits = np.empty(n_bootstrap, dtype=int)
    for i in range(n_bootstrap):
        sample = np.random.choice(data, size=n, replace=True)
        hits[i] = int(np.sum((sample > m0 - delta) & (sample < m0 + delta)))
    return (
        float(np.median(hits)),
        float(np.percentile(hits, 16)),
        float(np.percentile(hits, 84)),
    )


def bootstrap_pvalue(
    data: np.ndarray,
    m0: float,
    delta: float,
    expected_rate: float,
    n_total: int,
    n_bootstrap: int = 5000,
) -> Dict[str, float]:
    """
    Bootstrap-Konfidenzintervall für den rohen p-Wert.
    """
    n = len(data)
    pvals = np.empty(n_bootstrap)
    for i in range(n_bootstrap):
        sample = np.random.choice(data, size=n, replace=True)
        hits = int(np.sum((sample > m0 - delta) & (sample < m0 + delta)))
        pvals[i] = binomtest(
            hits, n_total, expected_rate, alternative="greater"
        ).pvalue
    return {
        "median": float(np.median(pvals)),
        "16%": float(np.percentile(pvals, 16)),
        "84%": float(np.percentile(pvals, 84)),
    }