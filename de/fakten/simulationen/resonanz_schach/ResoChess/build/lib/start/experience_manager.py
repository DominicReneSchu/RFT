import csv
import os
import threading

DATA_DIR = os.path.join(".", "data")
CSV_PATH = os.path.join(DATA_DIR, "experience_weighted.csv")

_experience_cache = None
_experience_dirty = set()
_lock = threading.Lock()

def add_conscious_experience(chain, result, experience_set):
    """
    Fügt einen neuen Erfahrungseintrag oder erhöht dessen Gewichtung.
    - chain: Zugkette mit Farbmarkierung, z.B. "w:e4|b:e5"
    - result: "success", "failure" oder "draw"
    - experience_set: dict, wird als Frequenzspeicher aktualisiert
    """
    key = (chain, result)
    with _lock:
        if key in experience_set:
            experience_set[key] += 1
        else:
            experience_set[key] = 1
        _experience_dirty.add(key)

def decay_experience_weights(experience_set, decay_factor=0.95, min_threshold=1):
    """
    Schwächt systemisch alle Einträge ab (Decay).
    Entfernt Einträge unterhalb Schwellwert.
    """
    to_delete = []
    with _lock:
        for key in list(experience_set.keys()):
            new_count = int(experience_set[key] * decay_factor)
            if new_count < min_threshold:
                to_delete.append(key)
            else:
                experience_set[key] = new_count
                _experience_dirty.add(key)
        for key in to_delete:
            del experience_set[key]
            _experience_dirty.add(key)

def persist_experience_set(experience_set):
    """
    Persistiert den Erfahrungsspeicher in experience_weighted.csv (vollständig, synchron).
    """
    with _lock:
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)
        with open(CSV_PATH, "w", newline='', encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["chain", "result", "count"])
            for (chain, result), count in experience_set.items():
                writer.writerow([chain, result, count])
        _experience_dirty.clear()

def persist_experience_set_async(experience_set):
    """
    Persistiert den Erfahrungsspeicher asynchron im Hintergrund.
    """
    def _persist():
        persist_experience_set(experience_set)
    t = threading.Thread(target=_persist)
    t.daemon = True
    t.start()

def load_weighted_experience_set():
    """
    Lädt den gewichteten Erfahrungsspeicher (wenn vorhanden).
    """
    experience_set = {}
    if os.path.isfile(CSV_PATH):
        with open(CSV_PATH, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                key = (row["chain"], row["result"])
                experience_set[key] = int(row["count"])
    return experience_set

def get_experience_set_lazy():
    """
    Lädt und cached den Erfahrungsspeicher nur bei Bedarf (Lazy Loading).
    """
    global _experience_cache
    with _lock:
        if _experience_cache is None:
            _experience_cache = load_weighted_experience_set()
        return _experience_cache

def apply_user_feedback(move_list, result, experience_set, max_chain_n=4, feedback=1):
    """
    Verstärkt oder schwächt Zug- und Motiv-Erfahrungen nach Nutzerfeedback.
    feedback: +N (positiv), -N (negativ), 0 (neutral)
    """
    import chess
    from .smart_move_selector import get_recent_chain
    from .motif_detection import detect_motifs

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
            if chain is not None:
                key = (chain, result)
                with _lock:
                    experience_set[key] = experience_set.get(key, 0) + feedback
                    _experience_dirty.add(key)
            motifs = detect_motifs(partial_board)
            if motifs:
                motif_chain = "|".join(sorted(motifs))
                key = (f"motif:{motif_chain}", result)
                with _lock:
                    experience_set[key] = experience_set.get(key, 0) + feedback
                    _experience_dirty.add(key)