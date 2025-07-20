import chess
import chess.engine
import random
from experience_manager import save_game_experience

# Systemische Parameter
ENGINE_PATH = "C:/Users/info/Desktop/ResoChess/stockfish/stockfish-windows-x86-64-avx2.exe"  # Passe an deinen tatsächlichen Pfad an
NUM_GAMES = 10000
EPSILON = 0.2  # Wahrscheinlichkeit für Exploration (Zufallszug)

def choose_move(board, engine):
    legal_moves = list(board.legal_moves)
    # Exploration: mit Wahrscheinlichkeit EPSILON wird ein Zufallszug gewählt
    if random.random() < EPSILON:
        return random.choice(legal_moves)
    else:
        # Engine wählt den besten Zug
        result = engine.analyse(board, chess.engine.Limit(time=0.1))
        return result["pv"][0]

def play_single_selfplay_game(engine):
    board = chess.Board()
    move_list = []
    while not board.is_game_over():
        move = choose_move(board, engine)
        move_list.append(board.san(move))
        board.push(move)
    result = board.result()  # "1-0", "0-1" oder "1/2-1/2"
    return move_list, result

def main():
    import os
    if not os.path.exists(ENGINE_PATH):
        print(f"[FEHLER] Stockfish-Engine nicht gefunden unter: {ENGINE_PATH}")
        return
    with chess.engine.SimpleEngine.popen_uci(ENGINE_PATH) as engine:
        for game_num in range(1, NUM_GAMES + 1):
            print(f"Starte Selfplay-Spiel {game_num}")
            move_list, result = play_single_selfplay_game(engine)
            save_game_experience(move_list, result)
            print(f"Spiel {game_num} abgeschlossen mit Ergebnis: {result}")
    print("Alle Selfplay-Spiele abgeschlossen. Kollektives Bewusstseinsfeld aktualisiert.")

if __name__ == "__main__":
    main()