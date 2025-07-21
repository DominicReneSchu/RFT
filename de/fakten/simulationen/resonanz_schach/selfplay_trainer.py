import chess
import random
from experience_manager import save_game_experience, add_conscious_experience, _load_conscious_experience_set

def relative_move_description(board_before, move):
    piece = board_before.piece_at(move.from_square)
    if not piece:
        return "unbekannter Zug"
    piece_type = piece.piece_type
    capture = board_before.is_capture(move)
    if piece_type == chess.PAWN:
        return "Bauer schlägt" if capture else "Bauer vorwärts"
    if piece_type == chess.KNIGHT:
        return "Springer schlägt" if capture else "Springer zieht"
    if piece_type == chess.BISHOP:
        return "Läufer schlägt" if capture else "Läufer diagonal"
    if piece_type == chess.ROOK:
        return "Turm schlägt" if capture else "Turm gerade"
    if piece_type == chess.QUEEN:
        return "Dame schlägt" if capture else "Dame zieht"
    if piece_type == chess.KING:
        return "König schlägt" if capture else "König zieht"
    return "unbekannter Zug"

def get_recent_rel_chain(rel_move_list, n=2):
    """Gibt die letzten n Züge als Kette zurück."""
    return rel_move_list[-n:] if len(rel_move_list) >= n else rel_move_list

def select_learned_move(board, rel_move_list):
    """
    Systemisch: Nutzt conscious_experience, um resonant Erfolg/Fehler zu erkennen und zu vermeiden.
    Vorausberechnung für 2 eigene Züge.
    """
    experience_set = _load_conscious_experience_set()
    recent_chain = get_recent_rel_chain(rel_move_list, n=2)
    recent_key_success = ("|".join(recent_chain), "success")
    recent_key_failure = ("|".join(recent_chain), "failure")

    # Nur wenn Resonanzfeld vorhanden
    if recent_key_success in experience_set or recent_key_failure in experience_set:
        prefer_moves = set()
        avoid_moves = set()
        for move in board.legal_moves:
            board.push(move)
            for reply in board.legal_moves:
                board.push(reply)
                test_chain = get_recent_rel_chain(rel_move_list + [relative_move_description(board, move), relative_move_description(board, reply)], n=2)
                chain_success = ("|".join(test_chain), "success")
                chain_failure = ("|".join(test_chain), "failure")
                if chain_failure in experience_set:
                    avoid_moves.add(move)
                if chain_success in experience_set:
                    prefer_moves.add(move)
                board.pop()
            board.pop()
        # Systemisch: Erfolg bevorzugen, Fehler vermeiden
        if prefer_moves:
            return random.choice(list(prefer_moves))
        available_moves = [m for m in board.legal_moves if m not in avoid_moves]
        if available_moves:
            return random.choice(available_moves)
        return random.choice(list(board.legal_moves))
    # Keine Resonanz: Zufall
    return random.choice(list(board.legal_moves))

def play_single_selfplay_game(engine=None):
    board = chess.Board()
    move_list = []
    rel_move_list = []
    previous_pieces = board.piece_map()
    while not board.is_game_over():
        # Systemisch: Resonanzfeld-orientierte Zugwahl
        move = select_learned_move(board, rel_move_list)
        board_before = board.copy()
        rel_move = relative_move_description(board_before, move)
        rel_move_list.append(rel_move)
        move_list.append(board.san(move))
        board.push(move)
        current_pieces = board.piece_map()
        # Fehlerkennung: Figurenverlust für die ziehende Partei
        last_color = not board.turn
        lost_own = sum(1 for sq, p in previous_pieces.items() if p.color == last_color and
                       (sq not in current_pieces or current_pieces.get(sq) != p)) > \
                   sum(1 for sq, p in current_pieces.items() if p.color == last_color and
                       (sq not in previous_pieces or previous_pieces.get(sq) != p))
        if lost_own:
            color_moves = rel_move_list[-2::-2] if last_color else rel_move_list[-1::-2]
            chain = color_moves[-5:] if len(color_moves) >= 5 else color_moves
            add_conscious_experience(chain, result="failure")
        previous_pieces = current_pieces.copy()
    result = board.result()
    save_game_experience(move_list, result)
    # Paarung von Erfolg und Misserfolg
    white_moves = rel_move_list[::2]
    black_moves = rel_move_list[1::2]
    white_chain = white_moves[-5:] if len(white_moves) >= 5 else white_moves
    black_chain = black_moves[-5:] if len(black_moves) >= 5 else black_moves
    if result == "1-0":
        add_conscious_experience(white_chain, result="success")
        add_conscious_experience(black_chain, result="failure")
    elif result == "0-1":
        add_conscious_experience(black_chain, result="success")
        add_conscious_experience(white_chain, result="failure")
    else:
        add_conscious_experience(white_chain, result="failure")
        add_conscious_experience(black_chain, result="failure")
    return move_list, result

if __name__ == "__main__":
    num_games = 100000
    stats = {"1-0": 0, "0-1": 0, "1/2-1/2": 0}
    for i in range(1, num_games + 1):
        moves, result = play_single_selfplay_game()
        stats[result] = stats.get(result, 0) + 1
        if i % 10 == 0 or i == 1:
            print(f"Spiel {i}: Ergebnis {result}")
    print("\nStatistik nach", num_games, "Spielen:")
    for res, n in stats.items():
        print(f"{res}: {n}")
    print("Fertig. Erfahrungen (success/failure) wurden für beide Seiten gespeichert und beim Zug resonanzbasiert genutzt.")