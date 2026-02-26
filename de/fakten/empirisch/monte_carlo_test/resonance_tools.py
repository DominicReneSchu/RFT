import numpy as np
from scipy.stats import binomtest
from statsmodels.stats.multitest import multipletests
from typing import Callable, Dict, List, Tuple, Optional, Any


def create_kde_sampler(
    background_data: np.ndarray, bandwidth: float = 0.05
) -> Callable[[int], np.ndarray]:
    """
    Erstelle eine Sampling-Funktion für den Hintergrund basierend auf
    Kernel-Density-Estimate (KDE).
    """
    from sklearn.neighbors import KernelDensity

    background_data = np.asarray(background_data).reshape(-1, 1)
    kde = KernelDensity(kernel="gaussian", bandwidth=bandwidth)
    kde.fit(background_data)

    def sampler(size: int) -> np.ndarray:
        samples = kde.sample(size)
        return samples.flatten()

    return sampler


def correct_pvalues(
    p_values: List[float],
    multitest_methods: Tuple[str, ...] = ("bonferroni", "fdr_bh"),
) -> Dict[str, np.ndarray]:
    """
    Korrigiere eine Liste von p-Werten mit mehreren Multiple-Testing-Methoden.

    Hinweis: Nur sinnvoll bei len(p_values) > 1. Bei Einzelwerten gibt
    Bonferroni den identischen Wert zurück.
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
    expected_hit_rates: Dict[float, float],
    n_total: int,
    multitest_methods: Tuple[str, ...] = ("bonferroni", "fdr_bh"),
    use_permutation: bool = False,
    n_permutations: int = 1000,
) -> Tuple[
    Dict[float, Dict[str, Any]], Dict[float, List[int]], Dict[float, List[float]]
]:
    """
    Führe Resonanzfenster-Analyse durch für gegebene Massenstellen M₀.

    Parameter
    ---------
    data : np.ndarray
        Messdaten (invariante Massen).
    m0_values : List[float]
        Resonanzmassenstellen M₀, an denen gesucht wird.
    deltas : List[float]
        Fensterbreiten (halbe Breite) um jede Massenstelle.
    expected_hit_rates : Dict[float, float]
        Erwartete Trefferrate unter Nullhypothese pro M₀.
    n_total : int
        Gesamtzahl der Ereignisse.
    multitest_methods : Tuple[str, ...]
        Methoden für Multiple-Testing-Korrektur.
    use_permutation : bool
        Ob zusätzlich ein Permutationstest durchgeführt wird.
    n_permutations : int
        Anzahl der Permutationen.

    Rückgabe
    --------
    results : Dict mit Ergebnissen pro M₀
    all_hits : Dict mit Trefferlisten pro M₀
    all_pvals : Dict mit p-Wert-Listen pro M₀
    """
    results: Dict[float, Dict[str, Any]] = {}
    all_hits: Dict[float, List[int]] = {}
    all_pvals: Dict[float, List[float]] = {}

    for m0 in m0_values:
        p_values: List[float] = []
        hits_list: List[int] = []
        permutation_pvals: List[float] = []
        for delta in deltas:
            hits = int(np.sum((data > m0 - delta) & (data < m0 + delta)))
            expected_rate = expected_hit_rates[m0]
            test = binomtest(hits, n_total, expected_rate, alternative="greater")
            p_values.append(test.pvalue)
            hits_list.append(hits)
            if use_permutation:
                perm_p = permutation_test_count(
                    data, m0, delta, hits, n_permutations
                )
                permutation_pvals.append(perm_p)

        pval_corrs = correct_pvalues(p_values, multitest_methods)
        best_idx = int(np.argmin(pval_corrs[multitest_methods[0]]))

        result_entry = {
            "best_delta": deltas[best_idx],
            "hits": hits_list[best_idx],
            "p_raw": p_values[best_idx],
            "p_corr": pval_corrs["bonferroni"][best_idx],
            "hits_list": hits_list,
            "pvals": p_values,
            "pvals_corr": pval_corrs,
        }
        if use_permutation:
            perm_pval_corrs = correct_pvalues(permutation_pvals, multitest_methods)
            result_entry["perm_pvals"] = permutation_pvals
            result_entry["perm_pvals_corr"] = perm_pval_corrs

        results[m0] = result_entry
        all_hits[m0] = hits_list
        all_pvals[m0] = p_values

    return results, all_hits, all_pvals


def permutation_test_count(
    data: np.ndarray,
    m0: float,
    delta: float,
    observed_hits: int,
    n_permutations: int = 1000,
) -> float:
    """
    Permutationstest für Trefferzahl im Fenster [m0-delta, m0+delta].

    Hinweis: Da die Daten keine Gruppenstruktur haben, wird hier
    die Verteilung der Trefferzahl unter zufälliger Permutation
    der Massenwerte geschätzt. Dies testet, ob die räumliche
    Anordnung der Werte (nicht nur ihre Verteilung) zum Überschuss
    beiträgt.
    """
    count = 0
    for _ in range(n_permutations):
        shuffled = np.random.permutation(data)
        perm_hits = int(np.sum((shuffled > m0 - delta) & (shuffled < m0 + delta)))
        if perm_hits >= observed_hits:
            count += 1
    return (count + 1) / (n_permutations + 1)


def bootstrap_hits(
    data: np.ndarray,
    m0: float,
    delta: float,
    n_bootstrap: int = 5000,
) -> Tuple[float, float, float]:
    """
    Bootstrap-Konfidenzintervall für Trefferzahl im Fenster
    [m0-delta, m0+delta].

    Rückgabe: (median, 16%-Perzentil, 84%-Perzentil)
    """
    n = len(data)
    hits = np.empty(n_bootstrap, dtype=int)
    for i in range(n_bootstrap):
        sample = np.random.choice(data, size=n, replace=True)
        hits[i] = int(np.sum((sample > m0 - delta) & (sample < m0 + delta)))
    return float(np.median(hits)), float(np.percentile(hits, 16)), float(np.percentile(hits, 84))


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

    Rückgabe: Dict mit 'median', '16%', '84%' des Bootstrap-p-Werts.

    Hinweis: Multiple-Testing-Korrektur auf Einzel-p-Werte ist nicht
    sinnvoll und wird hier nicht durchgeführt. Die Korrektur erfolgt
    über die Gesamtanalyse in resonance_analysis().
    """
    n = len(data)
    pvals = np.empty(n_bootstrap)
    for i in range(n_bootstrap):
        sample = np.random.choice(data, size=n, replace=True)
        hits = int(np.sum((sample > m0 - delta) & (sample < m0 + delta)))
        pvals[i] = binomtest(hits, n_total, expected_rate, alternative="greater").pvalue

    return {
        "median": float(np.median(pvals)),
        "16%": float(np.percentile(pvals, 16)),
        "84%": float(np.percentile(pvals, 84)),
    }


def resonance_blind_analysis(
    data: np.ndarray,
    m0_grid: np.ndarray,
    delta_grid: List[float],
    n_total: int,
    multitest_methods: Tuple[str, ...] = ("bonferroni", "fdr_bh"),
    use_permutation: bool = False,
    n_permutations: int = 1000,
) -> Tuple[
    np.ndarray, Dict[str, np.ndarray], Optional[np.ndarray], Optional[Dict[str, np.ndarray]]
]:
    """
    Blind-Analyse: Scan über alle Fenster, inkl. Multiple-Testing-Korrekturen.

    Die erwartete Rate wird aus der KDE-Dichte an der jeweiligen
    Massenstelle geschätzt (statt einer uniformen Annahme).
    """
    from sklearn.neighbors import KernelDensity

    # KDE für lokale Dichteabschätzung
    kde = KernelDensity(kernel="gaussian", bandwidth=0.05)
    kde.fit(data.reshape(-1, 1))

    n_m0 = len(m0_grid)
    n_del = len(delta_grid)
    hits_matrix = np.zeros((n_m0, n_del), dtype=int)
    pval_matrix = np.zeros((n_m0, n_del))
    permutation_matrix = np.zeros((n_m0, n_del)) if use_permutation else None

    for i, m0 in enumerate(m0_grid):
        # Lokale erwartete Rate aus KDE
        log_density = kde.score_samples(np.array([[m0]]))
        local_density = np.exp(log_density[0])

        for j, delta in enumerate(delta_grid):
            hits = int(np.sum((data > m0 - delta) & (data < m0 + delta)))
            # Erwartete Rate: lokale Dichte * Fensterbreite
            expected_rate = local_density * 2 * delta
            expected_rate = min(max(expected_rate, 1e-10), 1.0 - 1e-10)

            test = binomtest(hits, n_total, expected_rate, alternative="greater")
            pval_matrix[i, j] = test.pvalue
            hits_matrix[i, j] = hits

            if use_permutation:
                permutation_matrix[i, j] = permutation_test_count(
                    data, m0, delta, hits, n_permutations
                )

    # Multiple Testing über alle Fenster
    pval_corrs = {}
    pvals_flat = pval_matrix.flatten()
    for mt in multitest_methods:
        _, pvals_corr_flat, _, _ = multipletests(pvals_flat, alpha=0.05, method=mt)
        pval_corrs[mt] = pvals_corr_flat.reshape(pval_matrix.shape)

    perm_corrs = None
    if use_permutation:
        perm_corrs = {}
        perms_flat = permutation_matrix.flatten()
        for mt in multitest_methods:
            _, perms_corr_flat, _, _ = multipletests(
                perms_flat, alpha=0.05, method=mt
            )
            perm_corrs[mt] = perms_corr_flat.reshape(permutation_matrix.shape)

    return hits_matrix, pval_corrs, permutation_matrix, perm_corrs