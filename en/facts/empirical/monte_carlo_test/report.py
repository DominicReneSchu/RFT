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
    Automatic report generation (Markdown with embedded graphics and brief interpretation).
    """
    ensure_dir(output_dir)
    figures_dir = os.path.join(output_dir, "figures")
    ensure_dir(figures_dir)
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    report_md = [f"# Resonance Analysis Report\nGenerated on: {now}\n"]
    report_md.append("## Overview of Key Metrics\n")
    report_md.append("| ε | Δ (opt.) | Hits | [16%, 84%] | p_raw | p_corr | empir. p |")
    report_md.append("|---|---------|------|------------|-------|--------|----------|")
    for eps in EPSILONS:
        res = real_results[eps]
        report_md.append(f"| {eps:.2f} | {res['best_delta']:.2f} | {res['hits']} | [{res['hits_16']:.0f}, {res['hits_84']:.0f}] | "
                         f"{res['p_raw']:.2e} | {res['p_corr']:.2e} | {empirical_p_values[eps]:.3g} |")
    report_md.append("\n")

    # Histograms: Monte-Carlo hits vs. real hits
    fig, axes = plt.subplots(2, 3, figsize=(16, 8))
    for i, eps in enumerate(EPSILONS):
        ax = axes.flat[i]
        ax.hist(sim_hits[eps], bins=30, alpha=0.7, color='tab:blue', label='MC')
        ax.axvline(real_results[eps]['hits'], color='red', linestyle='--', label='Real Hits')
        ax.set_title(f'ε={eps}')
        ax.set_xlabel('Hits')
        ax.set_ylabel('Frequency')
        ax.legend()
    plt.tight_layout()
    figpath = os.path.join(figures_dir, "hist_mc_vs_real_hits.png")
    save_figure(fig, figpath)
    report_md.append(f"### Monte-Carlo Hits vs. Real Hits\n![Histogram MC vs Real]({figpath})\n")

    # p-value curves
    fig, axes = plt.subplots(2, 3, figsize=(18, 8))
    for i, eps in enumerate(EPSILONS):
        sim_pvals = sim_pvals_per_epsilon_delta[eps]
        q_low = np.percentile(sim_pvals, 16, axis=0)
        q_med = np.percentile(sim_pvals, 50, axis=0)
        q_high = np.percentile(sim_pvals, 84, axis=0)
        ax = axes.flat[i]
        ax.fill_between(DELTAS, q_low, q_high, color='tab:blue', alpha=0.3, label='68% MC CI')
        ax.plot(DELTAS, q_med, color='tab:blue', label='Median MC')
        ax.plot(DELTAS, real_pvals_matrix[eps], color='red', label='Real')
        ax.scatter([real_results[eps]['best_delta']], [real_results[eps]['p_corr']], color='black', marker='x', label='Min p_corr')
        ax.set_yscale('log')
        ax.set_xlabel('Δ')
        ax.set_ylabel('corrected p-value')
        ax.set_title(f'ε={eps}')
        ax.legend()
    plt.tight_layout()
    figpath = os.path.join(figures_dir, "pvalue_curves.png")
    save_figure(fig, figpath)
    report_md.append(f"### p-value Curves over Δ\n![p-value Curves]({figpath})\n")

    # Heatmaps
    real_hits_heatmap = np.array([real_hits_matrix[eps] for eps in EPSILONS])
    fig, axs = plt.subplots(1, 2, figsize=(17, 6), sharey=True)
    im0 = axs[0].imshow(real_hits_heatmap, aspect='auto', cmap='viridis', extent=[min(DELTAS), max(DELTAS), len(EPSILONS), 0])
    axs[0].set_title("Real Hit Count")
    axs[0].set_ylabel("ε Index")
    axs[0].set_xlabel("Δ")
    axs[0].set_yticks(np.arange(len(EPSILONS)) + 0.5)
    axs[0].set_yticklabels([f"{e:.2f}" for e in EPSILONS])
    fig.colorbar(im0, ax=axs[0])
    im1 = axs[1].imshow(sim_hits_heatmap, aspect='auto', cmap='viridis', extent=[min(DELTAS), max(DELTAS), len(EPSILONS), 0])
    axs[1].set_title("MC: Mean Hit Count")
    axs[1].set_xlabel("Δ")
    axs[1].set_yticks(np.arange(len(EPSILONS)) + 0.5)
    axs[1].set_yticklabels([f"{e:.2f}" for e in EPSILONS])
    fig.colorbar(im1, ax=axs[1])
    plt.suptitle("Heatmaps: Hit Count over ε and Δ")
    plt.tight_layout()
    figpath = os.path.join(figures_dir, "heatmaps_hits.png")
    save_figure(fig, figpath)
    report_md.append(f"### Heatmaps Hit Count\n![Heatmaps Hit Count]({figpath})\n")

    # Empirical p-value interpretation
    report_md.append("## Interpretation\n")
    for eps in EPSILONS:
        res = real_results[eps]
        p_emp = empirical_p_values[eps]
        if p_emp < 0.01:
            signif = "highly significant"
        elif p_emp < 0.05:
            signif = "significant"
        else:
            signif = "not significant"
        report_md.append(
            f"- For ε={eps:.2f}, the empirical p-value is {p_emp:.3g} ({signif}). "
            f"Found hits: {res['hits']} (Background expectation: {res['hits_median']:.1f} [16%: {res['hits_16']:.0f}, 84%: {res['hits_84']:.0f}])."
        )

    # Blind analysis (optional)
    if blind_results is not None:
        report_md.append("\n---\n\n## Blind Analysis\n")
        for item in blind_results["summary"]:
            report_md.append(item)
        for caption, figpath in blind_results["figures"]:
            report_md.append(f"![{caption}]({figpath})\n")

    # Save report
    md_path = os.path.join(output_dir, "resonance_report.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(report_md))
    print(f"Report saved to: {md_path}")