import tkinter as tk
import time
from tkinter import messagebox
import chess
from PIL import Image, ImageTk
from resonance_engine import ResonanceEngine
from experience_manager import save_game_experience, load_user_experience

SQUARE_SIZE = 60
BOARD_COLOR_1 = "#F0D9B5"
BOARD_COLOR_2 = "#B58863"
HIGHLIGHT_COLOR = "#A9A9FF"
MOVE_COLOR = "#DDFFDD"
LAST_MOVE_COLOR = "#FFE066"
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

def get_time_limit(board, last_move=None):
    if last_move:
        piece = board.piece_at(last_move.to_square)
        if piece and piece.piece_type == chess.KING:
            return 300
    if board.is_check():
        return 300
    if len(list(board.legal_moves)) < 8:
        return 240
    if sum(1 for p in board.piece_map().values() if p.color == board.turn) < 5:
        return 180
    return 120

class ResonanceChessGUI:
    def __init__(self, master, user_experience=None, engine=None):
        self.master = master
        self.user_experience = user_experience if user_experience is not None else []
        self.engine = engine if engine is not None else ResonanceEngine()
        self.master.title("Resonanzschach – Drag & Drop")
        self.board = chess.Board()
        self.move_list = []
        self.selected_square = None
        self.legal_moves = []
        self.drag_data = {"piece": None, "image": None, "start_square": None, "drag_img_id": None}
        self.human_color = None
        self.last_move_squares = None
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

    def get_board_status_text(self):
        if self.board.is_checkmate():
            return "Schachmatt!"
        elif self.board.is_stalemate():
            return "Patt – Unentschieden"
        elif self.board.is_insufficient_material():
            return "Unentschieden – unzureichendes Material"
        elif self.board.is_seventyfive_moves():
            return "Unentschieden – 75-Züge-Regel"
        elif self.board.is_fivefold_repetition():
            return "Unentschieden – 5-fache Wiederholung"
        elif self.board.is_check():
            return "Schach!"
        return ""

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
        if self.last_move_squares:
            for square in self.last_move_squares:
                file, rank = square_to_xy(square)
                x1 = file * SQUARE_SIZE
                y1 = rank * SQUARE_SIZE
                x2 = x1 + SQUARE_SIZE
                y2 = y1 + SQUARE_SIZE
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=LAST_MOVE_COLOR, outline="")
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
        if piece and piece.color == self.board.turn and self.board.turn == self.human_color:
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
        if self.board.turn != self.human_color:
            return
        if self.selected_square is not None and self.drag_data["drag_img_id"] is not None:
            to_square = xy_to_square(event.x, event.y)
            from_square = self.selected_square
            piece = self.board.piece_at(from_square)
            move = None
            if piece and piece.piece_type == chess.PAWN and chess.square_rank(to_square) in [0, 7]:
                move = chess.Move(from_square, to_square, promotion=chess.QUEEN)
            else:
                move = chess.Move(from_square, to_square)
            if move is not None and move in self.board.legal_moves:
                san = self.board.san(move)
                self.last_move_squares = (from_square, to_square)
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
                if self.board.turn != self.human_color:
                    self.info_label.config(text="KI denkt …")
                    self.master.after(400, self.ki_move)
                else:
                    status = self.get_board_status_text()
                    if status:
                        self.info_label.config(text=f"Dein Zug ({status})")
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
        if self.board.is_game_over() or self.board.turn == self.human_color:
            return
        last_move = self.board.move_stack[-1] if self.board.move_stack else None
        time_limit = get_time_limit(self.board, last_move)
        start_time = time.time()
        move, score = self.engine.select_best_move(self.board, depth=2)
        elapsed = time.time() - start_time
        if move is not None:
            san = self.board.san(move)
            self.last_move_squares = (move.from_square, move.to_square)
            self.board.push(move)
            self.move_list.append(san)
            self.draw_board()
            self.update_move_list()
            if self.board.is_game_over() or len(list(self.board.legal_moves)) == 0:
                result = self.board.result() if self.board.is_game_over() else "KI kann nicht ziehen"
                self.on_game_end(result)
                return
            else:
                self.info_label.config(
                    text=f"KI zog: {san} (𝓡={score:.2f}, {elapsed:.1f}s gerechnet)"
                )
        else:
            self.on_game_end("KI kann nicht ziehen")
        if self.board.turn == self.human_color:
            status = self.get_board_status_text()
            if status:
                self.info_label.config(text=f"Dein Zug ({status})")
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
        self.last_move_squares = None
        self.draw_board()
        self.update_move_list()
        if self.human_color == chess.WHITE:
            self.info_label.config(text="Du spielst Weiß – KI spielt Schwarz.")
        else:
            self.info_label.config(text="Du spielst Schwarz – KI spielt Weiß.")
        if self.board.turn != self.human_color:
            self.master.after(400, self.ki_move)

    def on_game_end(self, result):
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
    user_experience = load_user_experience()
    app = ResonanceChessGUI(root, user_experience=user_experience)
    root.mainloop()