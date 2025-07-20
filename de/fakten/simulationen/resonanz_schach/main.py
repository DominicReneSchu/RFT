import tkinter as tk
from resonance_gui import ResonanceChessGUI, load_piece_images
from experience_manager import load_user_experience
from resonance_engine import ResonanceEngine  # <--- KI-Engine eingebunden

if __name__ == "__main__":
    root = tk.Tk()
    try:
        load_piece_images()
    except Exception as e:
        print("Warnung: Schachfigurenbilder konnten nicht geladen werden.", e)
        print("Bitte platziere die Bilder für p_s, P_w, r_s, N_w, b_s, B_w, q_s, Q_w, k_s, K_w im Unterordner 'pieces'.")
    user_experience = load_user_experience()
    engine = ResonanceEngine()  # <--- KI-Instanz erzeugen
    app = ResonanceChessGUI(root, user_experience=user_experience, engine=engine)  # <--- Engine an GUI übergeben
    root.mainloop()