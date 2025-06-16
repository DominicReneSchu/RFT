import matplotlib.pyplot as plt
import numpy as np
import os
from datetime import datetime

def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def save_figure(fig, path):
    fig.savefig(path, bbox_inches='tight')
    plt.close(fig)

def generate_report(
    output_dir,
    real_results,
    sim_hits,
    empirical_p_values,
    EPSILONS,
    DELTAS,
    sim_pvals_per_epsilon_delta,
    real_pvals_matrix,
    real_hits_matrix,
    sim_hits_heatmap,
    blind_results=None
):
    """
    Automatische Report-Generierung (Markdown mit eingebundenen Grafiken und Kurz-Interpretation).
    """
    ensure_dir(output_dir)
    figures_dir = os.path.join(output_dir, "figures")
    ensure_dir(figures_dir)
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    report_md = [f"# Resonanzanalyse Report\nErstellt am: {now}\n"]
    report_md.append("## Übersicht der wichtigsten Kennzahlen\n")
    report_md.append("| ε | Δ (opt.) | Hits | [16%, 84%] | p_raw | p_corr | empir. p |")
    report_md.append("|---|---------|------|------------|-------|--------|----------|")
    for eps in EPSILONS:
        res = real_results[eps]
        report_md.append(f"| {eps:.2f} | {res['best_delta']:.2f} | {res['hits']} | [{res['hits_16']:.0f}, {res['hits_84']:.0f}] | "
                         f"{res['p_raw']:.2e} | {res['p_corr']:.2e} | {empirical_p_values[eps]:.3g} |")
    report_md.append("\n")

    # Histogramme: Monte-Carlo-Hits vs. echte Hits
    fig, axes = plt.subplots(2, 3, figsize=(16, 8))
    for i, eps in enumerate(EPSILONS):
        ax = axes.flat[i]
        ax.hist(sim_hits[eps], bins=30, alpha=0.7, color='tab:blue', label='MC')
        ax.axvline(real_results[eps]['hits'], color='red', linestyle='--', label='Echte Hits')
        ax.set_title(f'ε={eps}')
        ax.set_xlabel('Hits')
        ax.set_ylabel('Häufigkeit')
        ax.legend()
    plt.tight_layout()
    figpath = os.path.join(figures_dir, "hist_mc_vs_real_hits.png")
    save_figure(fig, figpath)
    report_md.append(f"### Monte-Carlo-Hits vs. echte Hits\n![Histogramm MC vs Echt]({figpath})\n")

    # p-Wert-Verläufe
    fig, axes = plt.subplots(2, 3, figsize=(18, 8))
    for i, eps in enumerate(EPSILONS):
        sim_pvals = sim_pvals_per_epsilon_delta[eps]
        q_low = np.percentile(sim_pvals, 16, axis=0)
        q_med = np.percentile(sim_pvals, 50, axis=0)
        q_high = np.percentile(sim_pvals, 84, axis=0)
        ax = axes.flat[i]
        ax.fill_between(DELTAS, q_low, q_high, color='tab:blue', alpha=0.3, label='68% MC CI')
        ax.plot(DELTAS, q_med, color='tab:blue', label='Median MC')
        ax.plot(DELTAS, real_pvals_matrix[eps], color='red', label='Echt')
        ax.scatter([real_results[eps]['best_delta']], [real_results[eps]['p_corr']], color='black', marker='x', label='Min p_corr')
        ax.set_yscale('log')
        ax.set_xlabel('Δ')
        ax.set_ylabel('korrigierter p-Wert')
        ax.set_title(f'ε={eps}')
        ax.legend()
    plt.tight_layout()
    figpath = os.path.join(figures_dir, "pvalue_curves.png")
    save_figure(fig, figpath)
    report_md.append(f"### p-Wert-Verläufe über Δ\n![p-Wert-Verläufe]({figpath})\n")

    # Heatmaps
    real_hits_heatmap = np.array([real_hits_matrix[eps] for eps in EPSILONS])
    fig, axs = plt.subplots(1, 2, figsize=(17, 6), sharey=True)
    im0 = axs[0].imshow(real_hits_heatmap, aspect='auto', cmap='viridis', extent=[min(DELTAS), max(DELTAS), len(EPSILONS), 0])
    axs[0].set_title("Echte Trefferanzahl")
    axs[0].set_ylabel("ε Index")
    axs[0].set_xlabel("Δ")
    axs[0].set_yticks(np.arange(len(EPSILONS)) + 0.5)
    axs[0].set_yticklabels([f"{e:.2f}" for e in EPSILONS])
    fig.colorbar(im0, ax=axs[0])
    im1 = axs[1].imshow(sim_hits_heatmap, aspect='auto', cmap='viridis', extent=[min(DELTAS), max(DELTAS), len(EPSILONS), 0])
    axs[1].set_title("MC: mittlere Trefferanzahl")
    axs[1].set_xlabel("Δ")
    axs[1].set_yticks(np.arange(len(EPSILONS)) + 0.5)
    axs[1].set_yticklabels([f"{e:.2f}" for e in EPSILONS])
    fig.colorbar(im1, ax=axs[1])
    plt.suptitle("Heatmaps: Trefferanzahl über ε und Δ")
    plt.tight_layout()
    figpath = os.path.join(figures_dir, "heatmaps_hits.png")
    save_figure(fig, figpath)
    report_md.append(f"### Heatmaps Trefferanzahl\n![Heatmaps Trefferanzahl]({figpath})\n")

    # Empirische p-Wert-Interpretation
    report_md.append("## Interpretation\n")
    for eps in EPSILONS:
        res = real_results[eps]
        p_emp = empirical_p_values[eps]
        if p_emp < 0.01:
            signif = "hoch signifikant"
        elif p_emp < 0.05:
            signif = "signifikant"
        else:
            signif = "nicht signifikant"
        report_md.append(
            f"- Für ε={eps:.2f} ist der empirische p-Wert {p_emp:.3g} ({signif}). "
            f"Gefundene Treffer: {res['hits']} (Erwartung im Hintergrund: {res['hits_median']:.1f} [16%: {res['hits_16']:.0f}, 84%: {res['hits_84']:.0f}])."
        )

    # Blind-Analyse (optional)
    if blind_results is not None:
        report_md.append("\n---\n\n## Blind-Analyse\n")
        for item in blind_results["summary"]:
            report_md.append(item)
        for caption, figpath in blind_results["figures"]:
            report_md.append(f"![{caption}]({figpath})\n")

    # Ablage
    md_path = os.path.join(output_dir, "resonanz_report.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(report_md))
    print(f"Report gespeichert unter: {md_path}")