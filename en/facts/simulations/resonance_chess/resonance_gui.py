import tkinter as tk
from tkinter import messagebox
import chess
from PIL import Image, ImageTk
from resonance_engine import select_best_move
from experience_manager import save_game_experience, load_user_experience

SQUARE_SIZE = 60
BOARD_COLOR_1 = "#F0D9B5"
BOARD_COLOR_2 = "#B58863"
HIGHLIGHT_COLOR = "#A9A9FF"
MOVE_COLOR = "#DDFFDD"
FONT = ("Arial", 12)

PIECE_IMAGES = {}

PIECE_IMAGE_FILES = {
    "p": "p_s.png",
    "P": "P_w.png",
    "r": "r_s.png",
    "R": "R_w.png",
    "n": "n_s.png",
    "N": "N_w.png",
    "b": "b_s.png",
    "B": "B_w.png",
    "q": "q_s.png",
    "Q": "Q_w.png",
    "k": "k_s.png",
    "K": "K_w.png",
}

def load_piece_images():
    for symbol, filename in PIECE_IMAGE_FILES.items():
        try:
            img = Image.open(f"pieces/{filename}").resize(
                (SQUARE_SIZE, SQUARE_SIZE), Image.Resampling.LANCZOS
            )
            PIECE_IMAGES[symbol] = ImageTk.PhotoImage(img)
        except Exception as e:
            print(f"Warnung: Bild für {symbol} konnte nicht geladen werden: {e}")

def square_to_xy(square):
    file = chess.square_file(square)
    rank = 7 - chess.square_rank(square)
    return file, rank

def xy_to_square(x, y):
    file = x // SQUARE_SIZE
    rank = 7 - (y // SQUARE_SIZE)
    if 0 <= file < 8 and 0 <= rank < 8:
        return chess.square(file, rank)
    return None

class ResonanceChessGUI:
    def __init__(self, master, user_experience=None):
        self.master = master
        self.master.title("Resonanzschach – Drag & Drop")
        self.board = chess.Board()
        self.move_list = []
        self.selected_square = None
        self.legal_moves = []
        self.drag_data = {"piece": None, "image": None, "start_square": None, "drag_img_id": None}
        self.user_experience = user_experience if user_experience is not None else []
        self.create_widgets()
        self.draw_board()
        self.update_move_list()
        self.info_label.config(text="Du spielst Weiß – KI spielt Schwarz.")
        self.master.after(400, self.ki_move)  # falls Schwarz am Zug ist

    def create_widgets(self):
        self.canvas = tk.Canvas(self.master, width=8*SQUARE_SIZE, height=8*SQUARE_SIZE)
        self.canvas.grid(row=0, column=0, rowspan=10)
        self.canvas.bind("<Button-1>", self.on_press)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)
        self.move_listbox = tk.Listbox(self.master, width=25, font=FONT)
        self.move_listbox.grid(row=0, column=1, sticky="n")
        self.reset_button = tk.Button(self.master, text="Neustart", command=self.reset_board, font=FONT)
        self.reset_button.grid(row=1, column=1, sticky="ew")
        self.info_label = tk.Label(self.master, text="", font=FONT, fg="blue")
        self.info_label.grid(row=2, column=1, sticky="ew")

    def draw_board(self):
        self.canvas.delete("all")
        for rank in range(8):
            for file in range(8):
                color = BOARD_COLOR_1 if (rank + file) % 2 == 0 else BOARD_COLOR_2
                x1 = file * SQUARE_SIZE
                y1 = rank * SQUARE_SIZE
                x2 = x1 + SQUARE_SIZE
                y2 = y1 + SQUARE_SIZE
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")
        if self.selected_square is not None:
            for move in self.legal_moves:
                to_sq = move.to_square
                file, rank = square_to_xy(to_sq)
                x1 = file * SQUARE_SIZE
                y1 = rank * SQUARE_SIZE
                x2 = x1 + SQUARE_SIZE
                y2 = y1 + SQUARE_SIZE
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=MOVE_COLOR, outline="")
            file, rank = square_to_xy(self.selected_square)
            x1 = file * SQUARE_SIZE
            y1 = rank * SQUARE_SIZE
            x2 = x1 + SQUARE_SIZE
            y2 = y1 + SQUARE_SIZE
            self.canvas.create_rectangle(x1, y1, x2, y2, outline=HIGHLIGHT_COLOR, width=4)
        for square in chess.SQUARES:
            piece = self.board.piece_at(square)
            if piece:
                if not (self.drag_data["piece"] and square == self.drag_data["start_square"]):
                    file, rank = square_to_xy(square)
                    x = file * SQUARE_SIZE
                    y = rank * SQUARE_SIZE
                    img = PIECE_IMAGES.get(piece.symbol())
                    if img:
                        self.canvas.create_image(x, y, anchor="nw", image=img)
        if self.drag_data["drag_img_id"] is not None:
            self.canvas.tag_raise(self.drag_data["drag_img_id"])
        self.master.update()

    def on_press(self, event):
        if self.board.is_game_over():
            return
        square = xy_to_square(event.x, event.y)
        piece = self.board.piece_at(square) if square is not None else None
        if piece and piece.color == self.board.turn and self.board.turn == chess.WHITE:
            self.selected_square = square
            self.legal_moves = [m for m in self.board.legal_moves if m.from_square == square]
            self.drag_data["piece"] = piece
            self.drag_data["start_square"] = square
            img = PIECE_IMAGES.get(piece.symbol())
            if img:
                self.drag_data["image"] = img
                self.drag_data["drag_img_id"] = self.canvas.create_image(event.x - SQUARE_SIZE//2, event.y - SQUARE_SIZE//2, anchor="nw", image=img)
        self.draw_board()

    def on_drag(self, event):
        if self.drag_data["drag_img_id"] is not None:
            self.canvas.coords(self.drag_data["drag_img_id"], event.x - SQUARE_SIZE//2, event.y - SQUARE_SIZE//2)
            self.master.update()

    def on_release(self, event):
        if self.selected_square is not None and self.drag_data["drag_img_id"] is not None:
            to_square = xy_to_square(event.x, event.y)
            from_square = self.selected_square
            piece = self.board.piece_at(from_square)
            move = None
            # Promotion: Prüfen, ob ein Bauer auf die letzte Reihe zieht
            if piece and piece.piece_type == chess.PAWN and chess.square_rank(to_square) in [0, 7]:
                # Automatische Umwandlung zur Dame
                move = chess.Move(from_square, to_square, promotion=chess.QUEEN)
            else:
                move = chess.Move(from_square, to_square)
            if move is not None and move in self.board.legal_moves:
                san = self.board.san(move)  # SAN-Notation vor dem Push bestimmen!
                self.board.push(move)
                self.move_list.append(san)
                self.selected_square = None
                self.legal_moves = []
                self.drag_data = {"piece": None, "image": None, "start_square": None, "drag_img_id": None}
                self.draw_board()
                self.update_move_list()
                if self.board.is_game_over():
                    self.on_game_end(self.board.result())
                    return
                if self.board.turn == chess.BLACK:
                    self.info_label.config(text="KI denkt …")
                    self.master.after(400, self.ki_move)
                else:
                    self.info_label.config(text="Dein Zug")
                return
        self.selected_square = None
        self.legal_moves = []
        if self.drag_data["drag_img_id"] is not None:
            self.canvas.delete(self.drag_data["drag_img_id"])
        self.drag_data = {"piece": None, "image": None, "start_square": None, "drag_img_id": None}
        self.draw_board()

    def ki_move(self):
        if self.board.is_game_over():
            self.on_game_end(self.board.result())
            return
        if self.board.turn == chess.BLACK:
            move, score, diag = select_best_move(self.board, depth=2)
            if move is not None:
                san = self.board.san(move)  # SAN VOR push()!
                self.board.push(move)
                self.move_list.append(san)
                self.draw_board()
                self.update_move_list()
                if self.board.is_game_over():
                    self.on_game_end(self.board.result())
                    return
                else:
                    self.info_label.config(text=f"KI zog: {san} (𝓡={score:.2f})")
            else:
                self.info_label.config(text="KI kann nicht ziehen.")
        else:
            self.info_label.config(text="Dein Zug")

    def update_move_list(self):
        self.move_listbox.delete(0, tk.END)
        for i, move in enumerate(self.move_list):
            self.move_listbox.insert(tk.END, f"{i+1}. {move}")

    def reset_board(self):
        self.board = chess.Board()
        self.move_list = []
        self.selected_square = None
        self.legal_moves = []
        self.drag_data = {"piece": None, "image": None, "start_square": None, "drag_img_id": None}
        self.draw_board()
        self.update_move_list()
        self.info_label.config(text="Du spielst Weiß – KI spielt Schwarz.")
        if self.board.turn == chess.BLACK:
            self.master.after(400, self.ki_move)

    def on_game_end(self, result):
        # Spielprotokoll und Ergebnis speichern (nur Nutzerpartien werden gespeichert)
        print(f"Speichere Spielerfahrung: {self.move_list} Ergebnis: {result}")
        save_game_experience(self.move_list, result)
        self.info_label.config(text="Spielende: " + result)
        messagebox.showinfo("Spielende", f"Ergebnis: {result}")

if __name__ == "__main__":
    root = tk.Tk()
    try:
        load_piece_images()
    except Exception as e:
        print("Warnung: Schachfigurenbilder konnten nicht geladen werden.", e)
        print("Bitte platziere die Bilder für p_s, P_w, r_s, R_w, n_s, N_w, b_s, B_w, q_s, Q_w, k_s, K_w im Unterordner 'pieces'.")
    # Nutzererfahrung laden
    user_experience = load_user_experience()
    app = ResonanceChessGUI(root, user_experience=user_experience)
    root.mainloop()