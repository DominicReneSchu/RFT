import numpy as np
from scipy.stats import binomtest
from statsmodels.stats.multitest import multipletests
from typing import Callable, Dict, List, Tuple, Optional, Any

def create_kde_sampler(background_data: np.ndarray, bandwidth: float = 0.05) -> Callable[[int], np.ndarray]:
    """
    Erstelle eine Sampling-Funktion für den Hintergrund basierend auf Kernel-Density-Estimate (KDE).
    """
    from sklearn.neighbors import KernelDensity
    background_data = np.asarray(background_data).reshape(-1, 1)
    kde = KernelDensity(kernel='gaussian', bandwidth=bandwidth)
    kde.fit(background_data)
    def sampler(size: int) -> np.ndarray:
        samples = kde.sample(size)
        return samples.flatten()
    return sampler

def correct_pvalues(
    p_values: List[float],
    multitest_methods: Tuple[str, ...] = ('bonferroni', 'fdr_bh')
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
    epsilons: List[float],
    deltas: List[float],
    expected_hit_rates: Dict[float, float],
    n_total: int,
    multitest_methods: Tuple[str, ...] = ('bonferroni', 'fdr_bh'),
    use_permutation: bool = False,
    n_permutations: int = 1000
) -> Tuple[
    Dict[float, Dict[str, Any]],
    Dict[float, List[int]],
    Dict[float, List[float]]
]:
    """
    Führe Resonanzfenster-Analyse durch, inkl. Multiple-Testing-Korrekturen und optional Permutationstest.
    """
    results: Dict[float, Dict[str, Any]] = {}
    all_hits: Dict[float, List[int]] = {}
    all_pvals: Dict[float, List[float]] = {}

    for eps in epsilons:
        p_values: List[float] = []
        hits_list: List[int] = []
        permutation_pvals: List[float] = []
        for delta in deltas:
            hits = int(np.sum((data > eps - delta) & (data < eps + delta)))
            expected_rate = expected_hit_rates[eps]
            test = binomtest(hits, n_total, expected_rate, alternative='greater')
            p_values.append(test.pvalue)
            hits_list.append(hits)
            if use_permutation:
                perm_p = permutation_test_count(data, eps, delta, hits, n_permutations)
                permutation_pvals.append(perm_p)
        pval_corrs = correct_pvalues(p_values, multitest_methods)
        best_idx = int(np.argmin(pval_corrs[multitest_methods[0]]))
        result_entry = {
            'best_delta': deltas[best_idx],
            'hits': hits_list[best_idx],
            'p_raw': p_values[best_idx],
            'p_corr': pval_corrs['bonferroni'][best_idx],
            'hits_list': hits_list,
            'pvals': p_values,
            'pvals_corr': pval_corrs,
        }
        if use_permutation:
            perm_pval_corrs = correct_pvalues(permutation_pvals, multitest_methods)
            result_entry['perm_pvals'] = permutation_pvals
            result_entry['perm_pvals_corr'] = perm_pval_corrs
        results[eps] = result_entry
        all_hits[eps] = hits_list
        all_pvals[eps] = p_values
    return results, all_hits, all_pvals

def permutation_test_count(
    data: np.ndarray,
    eps: float,
    delta: float,
    observed_hits: int,
    n_permutations: int = 1000
) -> float:
    """
    Exakter Permutationstest für Trefferzahl im Fenster [eps-delta, eps+delta].
    """
    count = 0
    n = len(data)
    for _ in range(n_permutations):
        shuffled = np.random.permutation(data)
        perm_hits = int(np.sum((shuffled > eps - delta) & (shuffled < eps + delta)))
        if perm_hits >= observed_hits:
            count += 1
    return (count + 1) / (n_permutations + 1)

def bootstrap_hits(
    data: np.ndarray,
    eps: float,
    delta: float,
    n_bootstrap: int = 5000
) -> Tuple[float, float, float]:
    """
    Bootstrap-Konfidenzintervall für Trefferzahl im Fenster [eps-delta, eps+delta].
    """
    hits = np.array([
        int(np.sum((np.random.choice(data, size=len(data), replace=True) > eps - delta) &
                   (np.random.choice(data, size=len(data), replace=True) < eps + delta)))
        for _ in range(n_bootstrap)
    ])
    return np.median(hits), np.percentile(hits, 16), np.percentile(hits, 84)

def bootstrap_pvalue(
    data: np.ndarray,
    eps: float,
    delta: float,
    expected_rate: float,
    n_total: int,
    n_bootstrap: int = 5000,
    multitest_methods: Tuple[str, ...] = ('bonferroni', 'fdr_bh')
) -> Dict[str, Dict[str, Any]]:
    """
    Bootstrap-Konfidenzintervall für p-Wert (bzw. korrigierte p-Werte) auf Basis von Bootstrapsamples.
    """
    pvals_dict: Dict[str, List[float]] = {mt: [] for mt in multitest_methods}
    for _ in range(n_bootstrap):
        bs = np.random.choice(data, size=len(data), replace=True)
        hits = int(np.sum((bs > eps - delta) & (bs < eps + delta)))
        p_raw = binomtest(hits, n_total, expected_rate, alternative='greater').pvalue
        for mt in multitest_methods:
            _, pvals_corr, _, _ = multipletests([p_raw], alpha=0.05, method=mt)
            pvals_dict[mt].append(pvals_corr[0])
    summary = {}
    for mt in multitest_methods:
        arr = np.array(pvals_dict[mt])
        summary[mt] = {
            "median": float(np.median(arr)),
            "16%": float(np.percentile(arr, 16)),
            "84%": float(np.percentile(arr, 84)),
            "all": arr
        }
    return summary

def resonance_blind_analysis(
    data: np.ndarray,
    epsilon_grid: np.ndarray,
    delta_grid: List[float],
    n_total: int,
    multitest_methods: Tuple[str, ...] = ('bonferroni', 'fdr_bh'),
    use_permutation: bool = False,
    n_permutations: int = 1000
) -> Tuple[
    np.ndarray,
    Dict[str, np.ndarray],
    Optional[np.ndarray],
    Optional[Dict[str, np.ndarray]]
]:
    """
    Blind-Analyse: Scan über alle Fenster, inkl. Multiple-Testing-Korrekturen und optional Permutationstest.
    """
    n_eps = len(epsilon_grid)
    n_del = len(delta_grid)
    hits_matrix = np.zeros((n_eps, n_del), dtype=int)
    pval_matrix = np.zeros((n_eps, n_del))
    permutation_matrix = np.zeros((n_eps, n_del)) if use_permutation else None

    for i, eps in enumerate(epsilon_grid):
        for j, delta in enumerate(delta_grid):
            hits = int(np.sum((data > eps - delta) & (data < eps + delta)))
            global_rate = len(data) / (data.max() - data.min()) * (2 * delta) / len(data)
            test = binomtest(hits, n_total, global_rate, alternative='greater')
            pval_matrix[i, j] = test.pvalue
            hits_matrix[i, j] = hits
            if use_permutation:
                permutation_matrix[i, j] = permutation_test_count(data, eps, delta, hits, n_permutations)
    # Multiple Testing
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
            _, perms_corr_flat, _, _ = multipletests(perms_flat, alpha=0.05, method=mt)
            perm_corrs[mt] = perms_corr_flat.reshape(permutation_matrix.shape)
    return hits_matrix, pval_corrs, permutation_matrix, perm_corrs