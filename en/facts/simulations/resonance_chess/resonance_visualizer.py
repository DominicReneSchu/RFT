import chess
import numpy as np
import matplotlib.pyplot as plt

def king_zone(square):
    rank = chess.square_rank(square)
    file = chess.square_file(square)
    zone = []
    for dr in [-1, 0, 1]:
        for df in [-1, 0, 1]:
            r = rank + dr
            f = file + df
            if 0 <= r < 8 and 0 <= f < 8:
                zone.append(chess.square(f, r))
    return zone

def field_heatmap(board, color, mode="pressure"):
    """
    Erzeuge eine Heatmap für das aktuelle Brett:
    - mode='pressure': Angriffsdruck auf jeden Punkt aus Sicht von 'color'
    - mode='safety': Schutzintensität auf jedem Feld um den König von 'color'
    Gibt ein 8x8-Numpy-Array zurück.
    """
    heatmap = np.zeros((8, 8))
    enemy_color = not color

    if mode == "pressure":
        for sq in chess.SQUARES:
            attackers = board.attackers(color, sq)
            heatmap[7 - chess.square_rank(sq), chess.square_file(sq)] = len(attackers)
    elif mode == "safety":
        king_sq = board.king(color)
        if king_sq is not None:
            local_zone = king_zone(king_sq)
            for sq in local_zone:
                piece_color = board.color_at(sq)
                if piece_color == color and sq != king_sq:
                    heatmap[7 - chess.square_rank(sq), chess.square_file(sq)] = 1
                elif piece_color == enemy_color:
                    heatmap[7 - chess.square_rank(sq), chess.square_file(sq)] = -1
    return heatmap

def visualize_board_resonance(board):
    """
    Zeige das aktuelle Brett als Heatmap:
    - Oben: Angriffsdruck (eigene Figuren auf Felder)
    - Unten: Schutzstruktur (eigene Figuren um den König)
    """
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    color = board.turn

    for ax, mode, title in zip(axs, ["pressure", "safety"], ["Angriffsdruck", "Königsschutz"]):
        data = field_heatmap(board, color, mode=mode)
        im = ax.imshow(data, cmap='coolwarm', vmin=-2, vmax=4)
        ax.set_title(title)
        ax.set_xticks(np.arange(8))
        ax.set_yticks(np.arange(8))
        ax.set_xticklabels("abcdefgh")
        ax.set_yticklabels(list(reversed(range(1,9))))
        for i in range(8):
            for j in range(8):
                val = data[i, j]
                if val != 0:
                    ax.text(j, i, f"{val:+.0f}", ha="center", va="center", color="black", fontsize=8)
    fig.colorbar(im, ax=axs, fraction=0.045)
    plt.tight_layout()
    plt.show()