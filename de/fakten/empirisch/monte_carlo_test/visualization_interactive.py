import numpy as np
import plotly.graph_objs as go

def interactive_hits_histogram(sim_hits, real_hits, epsilons):
    figs = []
    for eps in epsilons:
        fig = go.Figure()
        fig.add_trace(go.Histogram(
            x=sim_hits[eps], 
            nbinsx=30,
            name='Monte-Carlo Hits',
            marker_color='cornflowerblue',
            opacity=0.75
        ))
        fig.add_vline(
            x=real_hits[eps]['hits'], 
            line=dict(color='red', dash='dash'),
            annotation_text="Echt",
            annotation_position="top right"
        )
        fig.update_layout(
            title=f"ε = {eps}: Monte-Carlo-Hits vs. echte Hits",
            xaxis_title="Hits (bestes Δ)",
            yaxis_title="Häufigkeit",
            bargap=0.1,
            legend_title="Legende",
            template="plotly_white"
        )
        figs.append(fig)
    return figs

def interactive_pval_curve(deltas, sim_pvals_per_epsilon_delta, real_pvals_matrix, real_results, epsilons):
    figs = []
    for eps in epsilons:
        sim_pvals = sim_pvals_per_epsilon_delta[eps]
        q_low = np.percentile(sim_pvals, 16, axis=0)
        q_med = np.percentile(sim_pvals, 50, axis=0)
        q_high = np.percentile(sim_pvals, 84, axis=0)
        fig = go.Figure()
        fig.add_traces([
            go.Scatter(
                x=deltas, y=q_high, mode='lines',
                line=dict(width=0), showlegend=False
            ),
            go.Scatter(
                x=deltas, y=q_low, mode='lines',
                fill='tonexty', fillcolor='rgba(100,100,255,0.2)',
                line=dict(width=0), showlegend=True, name='68% MC CI'
            ),
        ])
        fig.add_trace(go.Scatter(
            x=deltas, y=q_med, mode='lines', name='Median MC', line=dict(color='cornflowerblue')
        ))
        fig.add_trace(go.Scatter(
            x=deltas, y=real_pvals_matrix[eps], mode='lines', name='Echt', line=dict(color='red')
        ))
        fig.add_trace(go.Scatter(
            x=[real_results[eps]['best_delta']], 
            y=[real_results[eps]['p_corr']], 
            mode='markers', marker=dict(color='black', size=10, symbol='x'),
            name='Min p_corr'
        ))
        fig.update_layout(
            yaxis_type="log",
            title=f"p-Wert-Verlauf für ε={eps}",
            xaxis_title="Δ",
            yaxis_title="korrigierter p-Wert (log)",
            template="plotly_white"
        )
        figs.append(fig)
    return figs

def interactive_heatmap(matrix, xvals, yvals, xlabel, ylabel, title, colorbar_title="Hits", annot=True, colorscale="Viridis"):
    fig = go.Figure(
        data=go.Heatmap(
            z=matrix,
            x=xvals, y=yvals,
            colorscale=colorscale,
            colorbar=dict(title=colorbar_title),
            hoverongaps=False,
            zmin=np.min(matrix),
            zmax=np.max(matrix)
        )
    )
    fig.update_layout(
        title=title,
        xaxis_title=xlabel,
        yaxis_title=ylabel,
        template="plotly_white"
    )
    if annot:
        for i, y in enumerate(yvals):
            for j, x in enumerate(xvals):
                fig.add_annotation(
                    x=x, y=y, text=str(int(matrix[i, j])),
                    showarrow=False, font=dict(color="black", size=10),
                    opacity=0.6
                )
    return fig

def interactive_heatmap_contrast(matrix, xvals, yvals, xlabel, ylabel, title, colorbar_title="Hits", annot=True):
    return interactive_heatmap(
        matrix, xvals, yvals, xlabel, ylabel, title, colorbar_title, annot=annot, colorscale="Cividis"
    )