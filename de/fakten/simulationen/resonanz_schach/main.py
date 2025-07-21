import tkinter as tk
from tkinter import simpledialog
import os
import csv
from datetime import datetime
import chess

from gui import ResonanceChessGUI, load_piece_images
from experience_manager import (
    add_conscious_experience,
    decay_experience_weights,
    persist_experience_set_async,
    load_weighted_experience_set,
    apply_user_feedback
)
from smart_move_selector import get_recent_chain
from motif_detection import detect_motifs
from engine import ResonanceEngine

def extend_experience_by_game(move_list, result, experience_set, max_chain_n=4):
    """
    Extrahiert alle n-Zug-Ketten (n=2..max) und erweitert das Erfahrungsspektrum.
    Inkludiert Motiverfahrung und resultiert in vollständiger Gruppenresonanz.
    """
    if result == "1-0":
        res_key = "success"
    elif result == "0-1":
        res_key = "failure"
    else:
        res_key = "draw"
    temp_board = chess.Board()
    for san in move_list:
        move = temp_board.parse_san(san)
        temp_board.push(move)
    for n in range(2, max_chain_n+1):
        for i in range(len(move_list)-n+1):
            partial_board = chess.Board()
            for san in move_list[:i+n]:
                move = partial_board.parse_san(san)
                partial_board.push(move)
            chain = get_recent_chain(partial_board, n=n, relative=True)
            add_conscious_experience(chain, res_key, experience_set)
            motifs = detect_motifs(partial_board)
            if motifs:
                motif_chain = "|".join(sorted(motifs))
                add_conscious_experience(f"motif:{motif_chain}", res_key, experience_set)

def save_game_experience(moves, result, modus="unknown"):
    DATA_DIR = os.path.join(".", "data")
    CSV_PATH = os.path.join(DATA_DIR, "experience.csv")
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    file_exists = os.path.isfile(CSV_PATH)
    with open(CSV_PATH, "a", newline='', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        if not file_exists:
            writer.writerow(["timestamp", "modus", "result", "moves"])
        timestamp = datetime.now().isoformat()
        moves_str = ";".join(moves)
        writer.writerow([timestamp, modus, result, moves_str])

def after_game_update(move_list, result, experience_set, max_chain_n=4, user_feedback=0):
    """
    Nach Partie: Erfahrung erweitern, decay anwenden, Feedback integrieren, persistieren.
    """
    extend_experience_by_game(move_list, result, experience_set, max_chain_n)
    decay_experience_weights(experience_set, decay_factor=0.95, min_threshold=1)
    if user_feedback != 0:
        apply_user_feedback(move_list, result, experience_set, max_chain_n, user_feedback)
    persist_experience_set_async(experience_set)
    return experience_set

def play_selfplay_games(num_games, engine, experience_set, max_chain_n=4):
    stats = {"1-0": 0, "0-1": 0, "1/2-1/2": 0}
    moves_list = []
    for i in range(1, num_games + 1):
        board = chess.Board()
        move_list = []
        while not board.is_game_over():
            move = engine.select_best_move(board)
            if move is None:
                break
            san = board.san(move)
            board.push(move)
            move_list.append(san)
        result = board.result()
        stats[result] = stats.get(result, 0) + 1
        moves_list.append(move_list)
        save_game_experience(move_list, result, modus="KI_vs_KI")
        after_game_update(move_list, result, experience_set, max_chain_n)
        engine.conscious_experience = experience_set
        print(f"Spiel {i}: Ergebnis {result}")
    print("\nStatistik nach", num_games, "Spielen:")
    for res, n in stats.items():
        print(f"{res}: {n}")
    print("Fertig. KI vs. KI abgeschlossen.")
    return moves_list, stats

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    modus = simpledialog.askstring(
        "Modus wählen",
        "Modus wählen:\n1 = Mensch vs. KI\n2 = KI vs. KI",
        parent=root
    )

    if modus is None:
        exit()

    try:
        load_piece_images()
    except Exception as e:
        print("Warnung: Schachfigurenbilder konnten nicht geladen werden.", e)
        print("Bitte platziere die Bilder für p_s, P_w, r_s, R_w, n_s, N_w, b_s, B_w, q_s, Q_w, k_s, K_w im Unterordner 'pieces'.")

    experience_set = load_weighted_experience_set()
    max_chain_n = 4
    engine = ResonanceEngine(conscious_experience=experience_set, max_chain_n=max_chain_n)

    if modus.strip() == "1":
        def patched_on_game_end(self, result):
            save_game_experience(self.move_list, result, modus="Human_vs_KI")
            feedback = getattr(self, "user_feedback", 0)
            updated_experience = after_game_update(self.move_list, result, experience_set, max_chain_n, user_feedback=feedback)
            self.engine.conscious_experience = updated_experience
            self.info_label.config(text="Spielende: " + result)
            from tkinter import messagebox
            messagebox.showinfo("Spielende", f"Ergebnis: {result}")
            self.user_feedback = 0  # Reset Feedback

        root.deiconify()
        app = ResonanceChessGUI(
            root,
            user_experience=None,
            engine=engine
        )
        app.on_game_end = patched_on_game_end.__get__(app, ResonanceChessGUI)
        root.mainloop()

    elif modus.strip() == "2":
        num_games = simpledialog.askinteger(
            "KI vs. KI",
            "Wie viele Spiele sollen gespielt werden?",
            minvalue=1, maxvalue=100000,
            parent=root
        )
        if num_games is not None:
            root.destroy()
            play_selfplay_games(num_games, engine, experience_set, max_chain_n)
        else:
            exit()
    else:
        print("Ungültige Eingabe. Bitte 1 oder 2 wählen.")
        root.destroy()