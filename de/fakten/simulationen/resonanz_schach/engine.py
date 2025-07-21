from experience_manager import load_weighted_experience_set
from smart_move_selector import select_learned_move

class ResonanceEngine:
    def __init__(self, conscious_experience=None, max_chain_n=4):
        """
        Systemische Kopplung: Erfahrungsspeicher als Feldgröße.
        - Wird keiner übergeben, erfolgt Initialisierung aus dem gewichteten Speicher.
        """
        if conscious_experience is None:
            self.conscious_experience = load_weighted_experience_set()
        else:
            self.conscious_experience = conscious_experience
        self.max_chain_n = max_chain_n

    def select_best_move(self, board):
        """
        Wählt einen Zug auf Basis des aktuellen Erfahrungsspeichers (Resonanzregel).
        """
        return select_learned_move(board, self.conscious_experience, self.max_chain_n)