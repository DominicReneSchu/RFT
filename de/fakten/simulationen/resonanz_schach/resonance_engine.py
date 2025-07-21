import chess
import time
from resonance_principles import evaluate_all_principles
from resonance_evaluator import evaluate_resonance
from experience_manager import load_user_experience, add_conscious_experience, analyze_causal_chain, blacklist_faulty_chain, _load_conscious_experience_set

FIELD_WEIGHTS = {
    chess.E4: 0.25, chess.D4: 0.25, chess.E5: 0.25, chess.D5: 0.25,
}

class ResonanceEngine:
    def __init__(self, conscious_experience=None):
        self.user_experience = load_user_experience()
        self.SEQUENCE_LENGTH = 10
        self.blacklist = set()
        # Gruppenzugehörigkeit: Erfahrungsfeld aus conscious_experience.csv systemisch einbinden
        if conscious_experience is None:
            self.conscious_experience = _load_conscious_experience_set()
        else:
            self.conscious_experience = conscious_experience

    def get_move_sequence(self, move_list):
        if len(move_list) < self.SEQUENCE_LENGTH:
            return None
        return tuple(move_list[-self.SEQUENCE_LENGTH:])

    def evaluate_position(self, board):
        return evaluate_all_principles(board)

    def after_move(self, game_history, result):
        # Fehler- oder Erfolgsketten systemisch aktualisieren
        if result == "loss":
            idx = len(self.user_experience) - 1
            chain = analyze_causal_chain(self.user_experience, idx)
            self.blacklist.update(blacklist_faulty_chain(chain))
        elif result == "success":
            idx = len(self.user_experience) - 1
            chain = analyze_causal_chain(self.user_experience, idx)
            add_conscious_experience(chain)

    def select_best_move(self, board, depth=2, move_list=None, time_limit=None):
        if time_limit is not None:
            start_time = time.time()
        best_score = -float("inf")
        best_move = None
        if move_list is None:
            move_list = []
        for move in board.legal_moves:
            if time_limit is not None and time.time() - start_time > time_limit:
                break
            # Blacklist-Check: systemisch Fehlerketten vermeiden
            candidate_seq = tuple(move_list + [move.uci()])
            if "|".join(candidate_seq) in self.blacklist:
                continue
            board_push = board.copy(stack=False)
            board_push.push(move)
            base_score = self.evaluate_position(board_push)
            # Resonanz-Erfahrungsfeld: Bewusstseinsbonus systemisch aus conscious_experience.csv
            chain_str = "|".join([m for m in move_list] + [move.uci()])
            key_success = (chain_str, "success")
            key_failure = (chain_str, "failure")
            if key_success in self.conscious_experience:
                base_score += 0.5
            if key_failure in self.conscious_experience:
                base_score -= 0.5
            if base_score > best_score:
                best_score = base_score
                best_move = move
        return best_move, best_score

def select_best_move(board, depth=1, user_experience=None, time_limit=None):
    if time_limit is not None:
        start_time = time.time()
    if depth == 1:
        best_move = None
        best_value = -float('inf')
        best_details = None
        for move in board.legal_moves:
            if time_limit is not None and time.time() - start_time > time_limit:
                break

            value, details = evaluate_resonance(board, move)
            value += aggression_score(board, move)
            value += field_resonance(move)

            if user_experience:
                value += experience_bonus(move, user_experience, board)
                value += avoid_losing_situations(move, user_experience, board)

            board_push = board.copy(stack=False)
            board_push.push(move)

            if board_push.is_checkmate():
                value = float('inf')
                details["matt"] = True
            elif causes_material_loss(board, move):
                value -= 8

            details["field_resonance"] = field_resonance(move)

            if value > best_value:
                best_value = value
                best_move = move
                best_details = details
        return best_move, best_value, best_details
    else:
        move, value, details = minimax_root(
            board, depth, is_maximizing=board.turn,
            user_experience=user_experience, time_limit=time_limit
        )
        return move, value, details

def minimax_root(board, depth, is_maximizing, user_experience=None, time_limit=None):
    best_move = None
    best_value = -float('inf') if is_maximizing else float('inf')
    best_details = None
    if time_limit is not None:
        start_time = time.time()
    for move in board.legal_moves:
        if time_limit is not None and time.time() - start_time > time_limit:
            break
        board_push = board.copy(stack=False)
        board_push.push(move)
        value = minimax(
            board_push, depth-1, not is_maximizing, matthunter=True,
            user_experience=user_experience, time_limit=time_limit, start_time=start_time
        )
        details = {"minimax": value}
        value += aggression_score(board, move)
        value += field_resonance(move)
        if user_experience:
            value += experience_bonus(move, user_experience, board)
            value += avoid_losing_situations(move, user_experience, board)
        if board_push.is_checkmate():
            value = float('inf') - (depth * 100)
            details["matt"] = True
        elif causes_material_loss(board, move):
            value -= 8
        if is_maximizing and value > best_value:
            best_value = value
            best_move = move
            best_details = details
        elif not is_maximizing and value < best_value:
            best_value = value
            best_move = move
            best_details = details
    return best_move, best_value, best_details

def minimax(board, depth, is_maximizing, matthunter=False, user_experience=None, time_limit=None, start_time=None):
    if time_limit is not None and start_time is not None and time.time() - start_time > time_limit:
        return 0
    if depth == 0 or board.is_game_over():
        if board.is_checkmate():
            return -float('inf') if board.turn == chess.WHITE else float('inf')
        elif board.is_stalemate():
            return 0
        move = next(iter(board.legal_moves), None)
        if move:
            value, _ = evaluate_resonance(board, move)
            value += aggression_score(board, move)
            value += field_resonance(move)
            if user_experience:
                value += experience_bonus(move, user_experience, board)
                value += avoid_losing_situations(move, user_experience, board)
            if causes_material_loss(board, move):
                value -= 8
            return value if board.turn == chess.WHITE else -value
        else:
            return 0
    values = []
    for move in board.legal_moves:
        if time_limit is not None and start_time is not None and time.time() - start_time > time_limit:
            break
        board_push = board.copy(stack=False)
        board_push.push(move)
        if matthunter and board_push.is_checkmate():
            val = float('inf') - (depth * 100)
        elif matthunter and board_push.is_stalemate():
            val = 0
        else:
            val = minimax(
                board_push, depth-1, not is_maximizing, matthunter,
                user_experience, time_limit, start_time
            )
            val += aggression_score(board, move)
            val += field_resonance(move)
            if user_experience:
                val += experience_bonus(move, user_experience, board)
                val += avoid_losing_situations(move, user_experience, board)
            if causes_material_loss(board, move):
                val -= 8
        values.append(val)
    return max(values) if is_maximizing else min(values)

def aggression_score(board, move):
    score = 0.0
    piece = board.piece_at(move.from_square)
    if piece:
        if piece.piece_type == chess.PAWN:
            rank_from = chess.square_rank(move.from_square)
            rank_to = chess.square_rank(move.to_square)
            if (piece.color == chess.WHITE and rank_to > rank_from) or (piece.color == chess.BLACK and rank_to < rank_from):
                score += 0.3 * abs(rank_to - rank_from)
        if board.is_capture(move):
            captured = board.piece_at(move.to_square)
            if captured:
                score += 0.5 if captured.piece_type == chess.KING else 0.2
        rank_to = chess.square_rank(move.to_square)
        if (piece.color == chess.WHITE and rank_to >= 4) or (piece.color == chess.BLACK and rank_to <= 3):
            score += 0.2
        if move.to_square in [chess.D4, chess.D5, chess.E4, chess.E5]:
            score += 0.2
    return score

def field_resonance(move):
    return FIELD_WEIGHTS.get(move.to_square, 0.0)

def causes_material_loss(board, move):
    board_push = board.copy(stack=False)
    board_push.push(move)
    moved_piece = board_push.piece_at(move.to_square)
    attackers = board_push.attackers(not moved_piece.color, move.to_square)
    defenders = board_push.attackers(moved_piece.color, move.to_square)
    if attackers and (not defenders or len(attackers) > len(defenders)):
        return True
    return False

def experience_bonus(move, user_experience, board=None):
    bonus = 0.0
    move_san = move.uci()
    for game in user_experience or []:
        history = game.get("history", [])
        for i, m in enumerate(history):
            if m == move_san:
                if game.get("result") == "1-0":
                    bonus += 0.4
                elif game.get("result") == "0-1":
                    bonus -= 0.4
    return bonus

def avoid_losing_situations(move, user_experience, board=None, last_n=3):
    malus = 0.0
    move_san = move.uci()
    my_seq = []
    if board:
        tmp_board = board.copy(stack=False)
        for _ in range(last_n):
            if tmp_board.move_stack:
                my_seq.insert(0, tmp_board.pop().uci())
    seq_to_check = my_seq + [move_san]
    for game in user_experience or []:
        if game.get("result") == "0-1":
            history = game.get("history", [])
            for i in range(len(history) - len(seq_to_check) + 1):
                if history[i:i+len(seq_to_check)] == seq_to_check:
                    malus -= 1.5
    return malus