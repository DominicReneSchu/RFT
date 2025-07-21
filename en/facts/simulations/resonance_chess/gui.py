import tkinter as tk
from tkinter import messagebox
import chess
from PIL import Image, ImageTk
from engine import ResonanceEngine
from experience_manager import add_conscious_experience  # Nur noch relevante Funktion importieren

SQUARE_SIZE = 60
BOARD_COLOR_1 = "#F0D9B5"
BOARD_COLOR_2 = "#B58863"
HIGHLIGHT_COLOR = "#A9A9FF"
MOVE_COLOR = "#DDFFDD"
LAST_MOVE_COLOR = "#FFE066"
FONT = ("Arial", 12)

PIECE_IMAGES = {}
PIECE_IMAGE_FILES = {
    "p": "p_s.png", "P": "P_w.png",
    "r": "r_s.png", "R": "R_w.png",
    "n": "n_s.png", "N": "N_w.png",
    "b": "b_s.png", "B": "B_w.png",
    "q": "q_s.png", "Q": "Q_w.png",
    "k": "k_s.png", "K": "K_w.png",
}

def load_piece_images():
    for symbol, filename in PIECE_IMAGE_FILES.items():
        try:
            img = Image.open(f"pieces/{filename}").resize((SQUARE_SIZE, SQUARE_SIZE), Image.Resampling.LANCZOS)
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

def relative_move_description(board_before, move):
    return board_before.san(move) if move else "unbekannter Zug"

class ResonanceChessGUI:
    def __init__(self, master, user_experience=None, engine=None):
        self.master = master
        self.user_experience = user_experience if user_experience is not None else []
        self.engine = engine if engine is not None else ResonanceEngine()
        self.master.title("Resonanzschach – Minimal")
        self.board = chess.Board()
        self.move_list = []
        self.rel_move_list = []
        self.previous_pieces = self.board.piece_map()
        self.selected_square = None
        self.legal_moves = []
        self.drag_data = {"piece": None, "image": None, "start_square": None, "drag_img_id": None}
        self.human_color = None
        self.last_move_from_square = None
        self.create_start_dialog()

    def create_start_dialog(self):
        dialog = tk.Toplevel(self.master)
        dialog.title("Farbwahl")
        dialog.transient(self.master)
        dialog.grab_set()
        tk.Label(dialog, text="Welche Farbe willst du spielen?", font=FONT).pack(padx=16, pady=16)
        btn_frame = tk.Frame(dialog)
        btn_frame.pack(pady=8)
        tk.Button(btn_frame, text="Weiß", font=FONT, width=12,
                  command=lambda: self.start_game(dialog, chess.WHITE)).pack(side="left", padx=8)
        tk.Button(btn_frame, text="Schwarz", font=FONT, width=12,
                  command=lambda: self.start_game(dialog, chess.BLACK)).pack(side="left", padx=8)
        dialog.wait_window()

    def start_game(self, dialog, color):
        self.human_color = color
        dialog.destroy()
        self.create_widgets()
        self.draw_board()
        self.update_move_list()
        self.previous_pieces = self.board.piece_map()
        self.rel_move_list = []
        self.last_move_from_square = None
        if self.human_color == chess.WHITE:
            self.info_label.config(text="Du spielst Weiß – KI spielt Schwarz.")
        else:
            self.info_label.config(text="Du spielst Schwarz – KI spielt Weiß.")
        if self.board.turn != self.human_color:
            self.master.after(400, self.ki_move)

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
        # 1. Grundfarben
        for rank in range(8):
            for file in range(8):
                color = BOARD_COLOR_1 if (rank + file) % 2 == 0 else BOARD_COLOR_2
                x1 = file * SQUARE_SIZE
                y1 = rank * SQUARE_SIZE
                x2 = x1 + SQUARE_SIZE
                y2 = y1 + SQUARE_SIZE
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")
        # 2. Markiere Ursprungsfeld des letzten Zuges persistent
        if self.last_move_from_square is not None:
            file, rank = square_to_xy(self.last_move_from_square)
            x1 = file * SQUARE_SIZE
            y1 = rank * SQUARE_SIZE
            x2 = x1 + SQUARE_SIZE
            y2 = y1 + SQUARE_SIZE
            self.canvas.create_rectangle(x1, y1, x2, y2, fill=LAST_MOVE_COLOR, outline="")

        # 3. Markiere mögliche Züge bei Auswahl
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
        # 4. Figuren einzeichnen
        for square in chess.SQUARES:
            piece = self.board.piece_at(square)
            if piece:
                file, rank = square_to_xy(square)
                x = file * SQUARE_SIZE
                y = rank * SQUARE_SIZE
                img = PIECE_IMAGES.get(piece.symbol(), None)
                if img:
                    self.canvas.create_image(x, y, anchor="nw", image=img)
        self.master.update()

    def get_status_text(self, prefix=""):
        if self.board.is_check():
            if prefix:
                return f"{prefix} – Schach!"
            return "Schach!"
        return prefix

    def on_press(self, event):
        if self.board.is_game_over():
            return
        square = xy_to_square(event.x, event.y)
        piece = self.board.piece_at(square) if square is not None else None
        if piece and piece.color == self.board.turn and self.board.turn == self.human_color:
            self.selected_square = square
            self.legal_moves = [m for m in self.board.legal_moves if m.from_square == square]
            self.drag_data["piece"] = piece
            self.drag_data["start_square"] = square
        else:
            self.selected_square = None
            self.legal_moves = []
        self.draw_board()

    def on_drag(self, event):
        pass  # Minimalversion: kein Drag-Bild

    def on_release(self, event):
        if self.board.turn != self.human_color:
            return
        if self.selected_square is not None:
            to_square = xy_to_square(event.x, event.y)
            from_square = self.selected_square
            move = chess.Move(from_square, to_square)
            if move in self.board.legal_moves:
                board_before = self.board.copy()
                san = self.board.san(move)
                self.board.push(move)
                self.move_list.append(san)
                self.rel_move_list.append(relative_move_description(board_before, move))
                self.last_move_from_square = from_square
                self.selected_square = None
                self.legal_moves = []
                self.draw_board()
                self.update_move_list()
                if self.board.is_game_over():
                    self.on_game_end(self.board.result())
                    return
                if self.board.turn != self.human_color:
                    self.info_label.config(text=self.get_status_text("KI denkt …"))
                    self.master.after(400, self.ki_move)
                else:
                    self.info_label.config(text=self.get_status_text("Dein Zug"))
                return
        self.selected_square = None
        self.legal_moves = []
        self.draw_board()

    def ki_move(self):
        if self.board.is_game_over() or self.board.turn == self.human_color:
            return
        move = self.engine.select_best_move(self.board)
        if move is not None:
            board_before = self.board.copy()
            san = self.board.san(move)
            from_square = move.from_square
            self.board.push(move)
            self.move_list.append(san)
            self.rel_move_list.append(relative_move_description(board_before, move))
            self.last_move_from_square = from_square
            self.draw_board()
            self.update_move_list()
            if self.board.is_game_over():
                result = self.board.result()
                self.on_game_end(result)
                return
            else:
                self.info_label.config(text=self.get_status_text(f"KI zog: {san}"))
        else:
            self.on_game_end("KI kann nicht ziehen")
        if self.board.turn == self.human_color:
            self.info_label.config(text=self.get_status_text("Dein Zug"))

    def update_move_list(self):
        self.move_listbox.delete(0, tk.END)
        for i, move in enumerate(self.move_list):
            self.move_listbox.insert(tk.END, f"{i+1}. {move}")

    def reset_board(self):
        self.board = chess.Board()
        self.move_list = []
        self.rel_move_list = []
        self.selected_square = None
        self.legal_moves = []
        self.last_move_from_square = None
        self.draw_board()
        self.update_move_list()
        if self.human_color == chess.WHITE:
            self.info_label.config(text="Du spielst Weiß – KI spielt Schwarz.")
        else:
            self.info_label.config(text="Du spielst Schwarz – KI spielt Weiß.")
        if self.board.turn != self.human_color:
            self.master.after(400, self.ki_move)

    def on_game_end(self, result):
        # Persistenz und Lernen ist jetzt systemisch in main.py zentralisiert.
        self.info_label.config(text="Spielende: " + result)
        messagebox.showinfo("Spielende", f"Ergebnis: {result}")