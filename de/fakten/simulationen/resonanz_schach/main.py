import tkinter as tk
from resonance_gui import ResonanceChessGUI, load_piece_images
from experience_manager import load_user_experience, _load_conscious_experience_set
from resonance_engine import ResonanceEngine  # <--- KI-Engine eingebunden

if __name__ == "__main__":
    root = tk.Tk()
    try:
        load_piece_images()
    except Exception as e:
        print("Warnung: Schachfigurenbilder konnten nicht geladen werden.", e)
        print("Bitte platziere die Bilder für p_s, P_w, r_s, R_w, n_s, N_w, b_s, B_w, q_s, Q_w, k_s, K_w im Unterordner 'pieces'.")
    user_experience = load_user_experience()   # Gruppenzugehörigkeit: Erfahrungssystem (historisch)
    conscious_experience = _load_conscious_experience_set()  # Gruppenzugehörigkeit: Resonanz-Erfahrungsfeld (entscheidungsrelevant)
    engine = ResonanceEngine(conscious_experience=conscious_experience)  # Gruppenzugehörigkeit: Resonanz-Engine mit Erfahrungsfeld
    app = ResonanceChessGUI(
        root,
        user_experience=user_experience,
        engine=engine
    )   # Gruppenzugehörigkeit: Engine und Erfahrung an GUI übergeben, vollständiges Resonanzfeld
    root.mainloop()