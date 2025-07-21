import chess
import random
from experience_manager import _load_conscious_experience_set

def get_recent_chain(board, n=2, relative=False):
    """
    Gibt die letzten n Züge als Kette zurück.
    Optional: relative Beschreibung der Züge (wie im Trainer).
    """
    stack = board.move_stack[-n:] if len(board.move_stack) >= n else board.move_stack
    if relative:
        # Implementiere hier ggf. die relative Beschreibung, z.B. "Bauer vorwärts"
        # Sonst Standard-SAN
        return [board.san(move) for move in stack]
    else:
        return [board.san(move) for move in stack]

def select_learned_move(board):
    """
    Wählt einen Zug, indem die letzten zwei Züge mit den gespeicherten Erfahrungen abgeglichen werden.
    Bei Resonanz: Zwei Züge vorausberechnen und Erfolg/Misserfolg systemisch prüfen.
    """
    experience_set = _load_conscious_experience_set()
    recent_chain = get_recent_chain(board, n=2)
    recent_key_success = ("|".join(recent_chain), "success")
    recent_key_failure = ("|".join(recent_chain), "failure")

    best_move = None
    avoid_moves = set()
    prefer_moves = set()

    # Prüfe, ob aktuelle Kette resonant ist
    if recent_key_success in experience_set or recent_key_failure in experience_set:
        for move in board.legal_moves:
            board.push(move)
            # Vorausberechnung: alle möglichen Antworten des Gegners
            for reply in board.legal_moves:
                board.push(reply)
                test_chain = get_recent_chain(board, n=2)
                chain_success = ("|".join(test_chain), "success")
                chain_failure = ("|".join(test_chain), "failure")
                if chain_failure in experience_set:
                    avoid_moves.add(move)
                if chain_success in experience_set:
                    prefer_moves.add(move)
                board.pop()
            board.pop()
        # Systemische Auswahl nach Resonanzregel
        if prefer_moves:
            return random.choice(list(prefer_moves))
        # Wenn alle Züge Fehler erzeugen, wähle einen Zug, der nicht in avoid_moves ist
        available_moves = [m for m in board.legal_moves if m not in avoid_moves]
        if available_moves:
            return random.choice(available_moves)
        # Notfall: Keine Vermeidung möglich, wähle beliebigen legalen Zug
        return random.choice(list(board.legal_moves))
    # Keine resonante Erfahrung: Zufall oder Engine
    return random.choice(list(board.legal_moves))