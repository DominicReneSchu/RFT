from resonance_engine import select_best_move
from resonance_visualizer import visualize_board_resonance
import chess

def get_human_move(board):
    while True:
        try:
            uci = input("Dein Zug (im UCI-Format, z.B. e2e4): ").strip()
            move = chess.Move.from_uci(uci)
            if move in board.legal_moves:
                return move
            else:
                print("Ungültiger Zug. Bitte erneut eingeben.")
        except Exception:
            print("Fehlerhafte Eingabe. Beispiel: e2e4")

def play_human_vs_resonance(max_moves=100, ki_depth=2):
    board = chess.Board()
    print("Du spielst Weiß. Resonanz-KI spielt Schwarz. (KI-Suchtiefe: %d)" % ki_depth)
    for turn in range(max_moves):
        print("\nAktuelles Brett:")
        print(board)
        visualize_board_resonance(board)
        if board.turn == chess.WHITE:
            move = get_human_move(board)
        else:
            move, score, diag = select_best_move(board, depth=ki_depth)
            print(f"\nResonanz-KI zieht: {board.san(move)} (𝓡 = {score:.2f}) | Details: {diag}\n")
        board.push(move)
        if board.is_game_over():
            print("Spielende:", board.result())
            print(board)
            break

if __name__ == "__main__":
    play_human_vs_resonance()