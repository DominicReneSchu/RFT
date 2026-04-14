from __future__ import annotations

from typing import Any

import numpy as np
import plotly.graph_objs as go


def interactive_hits_histogram(sim_hits: dict[float, list[int]], real_hits: dict[float, dict[str, Any]], m0_values: list[float]) -> list[go.Figure]:
    """Interaktive Histogramme: MC-Hits vs. echte Hits pro M₀."""
    figs = []
    for m0 in m0_values:
        fig = go.Figure()
        fig.add_trace(
            go.Histogram(
                x=sim_hits[m0],
                nbinsx=30,
                name="Monte-Carlo Hits",
                marker_color="cornflowerblue",
                opacity=0.75,
            )
        )
        fig.add_vline(
            x=real_hits[m0]["hits"],
            line=dict(color="red", dash="dash"),
            annotation_text="Echt",
            annotation_position="top right",
        )
        fig.update_layout(
            title=f"M₀ = {m0:.2f} GeV: Monte-Carlo-Hits vs. echte Hits",
            xaxis_title="Hits (bestes Δ)",
            yaxis_title="Häufigkeit",
            bargap=0.1,
            legend_title="Legende",
            template="plotly_white",
        )
        figs.append(fig)
    return figs


def interactive_pval_curve(
    deltas: list[float], sim_pvals_per_m0_delta: dict[float, np.ndarray], real_pvals_matrix: dict[float, np.ndarray], real_results: dict[float, dict[str, Any]], m0_values: list[float]
) -> list[go.Figure]:
    """Interaktive p-Wert-Verläufe über Δ pro M₀."""
    figs = []
    for m0 in m0_values:
        sim_pvals = sim_pvals_per_m0_delta[m0]
        q_low = np.percentile(sim_pvals, 16, axis=0)
        q_med = np.percentile(sim_pvals, 50, axis=0)
        q_high = np.percentile(sim_pvals, 84, axis=0)
        fig = go.Figure()
        fig.add_traces(
            [
                go.Scatter(
                    x=deltas,
                    y=q_high,
                    mode="lines",
                    line=dict(width=0),
                    showlegend=False,
                ),
                go.Scatter(
                    x=deltas,
                    y=q_low,
                    mode="lines",
                    fill="tonexty",
                    fillcolor="rgba(100,100,255,0.2)",
                    line=dict(width=0),
                    showlegend=True,
                    name="68% MC CI",
                ),
            ]
        )
        fig.add_trace(
            go.Scatter(
                x=deltas,
                y=q_med,
                mode="lines",
                name="Median MC",
                line=dict(color="cornflowerblue"),
            )
        )
        fig.add_trace(
            go.Scatter(
                x=deltas,
                y=real_pvals_matrix[m0],
                mode="lines",
                name="Echt",
                line=dict(color="red"),
            )
        )
        fig.add_trace(
            go.Scatter(
                x=[real_results[m0]["best_delta"]],
                y=[real_results[m0]["p_corr"]],
                mode="markers",
                marker=dict(color="black", size=10, symbol="x"),
                name="Min p_corr",
            )
        )
        fig.update_layout(
            yaxis_type="log",
            title=f"p-Wert-Verlauf für M₀={m0:.2f} GeV",
            xaxis_title="Δ (GeV)",
            yaxis_title="korrigierter p-Wert (log)",
            template="plotly_white",
        )
        figs.append(fig)
    return figs


def interactive_heatmap(
    matrix: np.ndarray,
    xvals: list[str] | list[float],
    yvals: list[str] | list[float],
    xlabel: str,
    ylabel: str,
    title: str,
    colorbar_title: str = "Hits",
    annot: bool = False,
    colorscale: str = "Viridis",
) -> go.Figure:
    """Interaktive Heatmap."""
    fig = go.Figure(
        data=go.Heatmap(
            z=matrix,
            x=xvals,
            y=yvals,
            colorscale=colorscale,
            colorbar=dict(title=colorbar_title),
            hoverongaps=False,
            zmin=np.min(matrix),
            zmax=np.max(matrix),
        )
    )
    fig.update_layout(
        title=title,
        xaxis_title=xlabel,
        yaxis_title=ylabel,
        template="plotly_white",
    )
    return fig


def interactive_heatmap_contrast(
    matrix: np.ndarray,
    xvals: list[str] | list[float],
    yvals: list[str] | list[float],
    xlabel: str,
    ylabel: str,
    title: str,
    colorbar_title: str = "Hits",
    annot: bool = False,
) -> go.Figure:
    """Interaktive Heatmap mit Cividis-Farbskala."""
    return interactive_heatmap(
        matrix,
        xvals,
        yvals,
        xlabel,
        ylabel,
        title,
        colorbar_title,
        annot=annot,
        colorscale="Cividis",
    )