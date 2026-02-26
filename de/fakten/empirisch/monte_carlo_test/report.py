import matplotlib.pyplot as plt
import numpy as np
import os
from datetime import datetime


def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def save_figure(fig, path):
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)


def generate_report(
    output_dir,
    real_results,
    sim_hits,
    empirical_p_values,
    m0_values,
    deltas,
    sim_pvals_per_m0_delta,
    real_pvals_matrix,
    real_hits_matrix,
    sim_hits_heatmap,
    blind_results=None,
):
    """
    Automatische Report-Generierung (Markdown mit eingebundenen Grafiken
    und Kurz-Interpretation).
    """
    ensure_dir(output_dir)
    figures_dir = os.path.join(output_dir, "figures")
    ensure_dir(figures_dir)
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    report_md = [f"# Resonanzanalyse Report\nErstellt am: {now}\n"]
    report_md.append("## Übersicht der wichtigsten Kennzahlen\n")
    report_md.append(
        "| M₀ (GeV) | Δ (opt.) | Hits | [16%, 84%] | p_raw | p_corr | empir. p |"
    )
    report_md.append(
        "|----------|---------|------|------------|-------|--------|----------|"
    )
    for m0 in m0_values:
        res = real_results[m0]
        report_md.append(
            f"| {m0:.2f} | {res['best_delta']:.3f} | {res['hits']} | "
            f"[{res['hits_16']:.0f}, {res['hits_84']:.0f}] | "
            f"{res['p_raw']:.2e} | {res['p_corr']:.2e} | "
            f"{empirical_p_values[m0]:.3g} |"
        )
    report_md.append("\n")

    # --- Histogramme: Monte-Carlo-Hits vs. echte Hits ---
    n_plots = len(m0_values)
    n_cols = min(3, n_plots)
    n_rows = (n_plots + n_cols - 1) // n_cols
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(6 * n_cols, 5 * n_rows))
    if n_plots == 1:
        axes = np.array([axes])
    axes = axes.flatten()
    for i, m0 in enumerate(m0_values):
        ax = axes[i]
        ax.hist(sim_hits[m0], bins=30, alpha=0.7, color="tab:blue", label="MC")
        ax.axvline(
            real_results[m0]["hits"], color="red", linestyle="--", label="Echte Hits"
        )
        ax.set_title(f"M₀={m0:.2f} GeV")
        ax.set_xlabel("Hits")
        ax.set_ylabel("Häufigkeit")
        ax.legend()
    # Leere Subplots ausblenden
    for j in range(i + 1, len(axes)):
        axes[j].set_visible(False)
    plt.tight_layout()
    figpath = os.path.join(figures_dir, "hist_mc_vs_real_hits.png")
    save_figure(fig, figpath)
    report_md.append(
        f"### Monte-Carlo-Hits vs. echte Hits\n![Histogramm MC vs Echt]"
        f"(figures/hist_mc_vs_real_hits.png)\n"
    )

    # --- p-Wert-Verläufe ---
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(6 * n_cols, 5 * n_rows))
    if n_plots == 1:
        axes = np.array([axes])
    axes = axes.flatten()
    for i, m0 in enumerate(m0_values):
        sim_pvals = sim_pvals_per_m0_delta[m0]
        q_low = np.percentile(sim_pvals, 16, axis=0)
        q_med = np.percentile(sim_pvals, 50, axis=0)
        q_high = np.percentile(sim_pvals, 84, axis=0)
        ax = axes[i]
        ax.fill_between(
            deltas, q_low, q_high, color="tab:blue", alpha=0.3, label="68% MC CI"
        )
        ax.plot(deltas, q_med, color="tab:blue", label="Median MC")
        ax.plot(deltas, real_pvals_matrix[m0], color="red", label="Echt")
        ax.scatter(
            [real_results[m0]["best_delta"]],
            [real_results[m0]["p_corr"]],
            color="black",
            marker="x",
            label="Min p_corr",
        )
        ax.set_yscale("log")
        ax.set_xlabel("Δ (GeV)")
        ax.set_ylabel("korrigierter p-Wert")
        ax.set_title(f"M₀={m0:.2f} GeV")
        ax.legend(fontsize=7)
    for j in range(i + 1, len(axes)):
        axes[j].set_visible(False)
    plt.tight_layout()
    figpath = os.path.join(figures_dir, "pvalue_curves.png")
    save_figure(fig, figpath)
    report_md.append(
        f"### p-Wert-Verläufe über Δ\n![p-Wert-Verläufe]"
        f"(figures/pvalue_curves.png)\n"
    )

    # --- Heatmaps ---
    real_hits_heatmap = np.array([real_hits_matrix[m0] for m0 in m0_values])
    fig, axs = plt.subplots(1, 2, figsize=(17, 4 + len(m0_values) * 0.5), sharey=True)
    y_labels = [f"{m0:.2f}" for m0 in m0_values]
    im0 = axs[0].imshow(
        real_hits_heatmap,
        aspect="auto",
        cmap="viridis",
        extent=[min(deltas), max(deltas), len(m0_values), 0],
    )
    axs[0].set_title("Echte Trefferanzahl")
    axs[0].set_ylabel("M₀ (GeV)")
    axs[0].set_xlabel("Δ (GeV)")
    axs[0].set_yticks(np.arange(len(m0_values)) + 0.5)
    axs[0].set_yticklabels(y_labels)
    fig.colorbar(im0, ax=axs[0])

    im1 = axs[1].imshow(
        sim_hits_heatmap,
        aspect="auto",
        cmap="viridis",
        extent=[min(deltas), max(deltas), len(m0_values), 0],
    )
    axs[1].set_title("MC: mittlere Trefferanzahl")
    axs[1].set_xlabel("Δ (GeV)")
    axs[1].set_yticks(np.arange(len(m0_values)) + 0.5)
    axs[1].set_yticklabels(y_labels)
    fig.colorbar(im1, ax=axs[1])

    plt.suptitle("Heatmaps: Trefferanzahl über M₀ und Δ")
    plt.tight_layout()
    figpath = os.path.join(figures_dir, "heatmaps_hits.png")
    save_figure(fig, figpath)
    report_md.append(
        f"### Heatmaps Trefferanzahl\n![Heatmaps Trefferanzahl]"
        f"(figures/heatmaps_hits.png)\n"
    )

    # --- Empirische p-Wert-Interpretation ---
    report_md.append("## Interpretation\n")
    for m0 in m0_values:
        res = real_results[m0]
        p_emp = empirical_p_values[m0]
        if p_emp < 0.01:
            signif = "hoch signifikant"
        elif p_emp < 0.05:
            signif = "signifikant"
        else:
            signif = "nicht signifikant"
        report_md.append(
            f"- Für M₀={m0:.2f} GeV ist der empirische p-Wert {p_emp:.3g} "
            f"({signif}). Gefundene Treffer: {res['hits']} "
            f"(Erwartung im Hintergrund: {res['hits_median']:.1f} "
            f"[16%: {res['hits_16']:.0f}, 84%: {res['hits_84']:.0f}])."
        )

    # --- Blind-Analyse (optional) ---
    if blind_results is not None:
        report_md.append("\n---\n\n## Blind-Analyse\n")
        for item in blind_results["summary"]:
            report_md.append(item)
        for caption, figpath_blind in blind_results["figures"]:
            report_md.append(f"![{caption}]({figpath_blind})\n")

    # --- Ablage ---
    md_path = os.path.join(output_dir, "resonanz_report.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(report_md))
    print(f"Report gespeichert unter: {md_path}")