def get_dynamic_depth(board):
    # Kritische Stellungen: Schach, wenige Züge, Endspiel, Materialschwankung
    # Gruppenzugehörigkeit: Die Tiefe gilt invariant für alle Mitglieder
    if board.is_check():
        return 3
    if len(list(board.legal_moves)) < 8:
        return 3
    # Optional: mehr Heuristik, z.B. droht eine Figur zu fallen (systemisch erweiterbar)
    return 2  # Standardtiefe für unkritische Züge