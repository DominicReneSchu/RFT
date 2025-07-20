def ki_move(self):
    if self.board.is_game_over() or not any(self.board.legal_moves):
        result = self.board.result() if self.board.is_game_over() else "KI kann nicht ziehen"
        self.on_game_end(result)
        return
    if self.board.turn == chess.BLACK:
        depth = get_dynamic_depth(self.board)
        move, score = self.engine.select_best_move(
            self.board, depth=depth, move_list=self.move_list
        )
        if move is not None:
            san = self.board.san(move)
            self.board.push(move)
            self.move_list.append(san)
            self.draw_board()
            self.update_move_list()
            if self.board.is_game_over() or len(list(self.board.legal_moves)) == 0:
                result = self.board.result() if self.board.is_game_over() else "KI kann nicht ziehen"
                self.on_game_end(result)
                return
            else:
                self.info_label.config(text=f"KI zog: {san} (𝓡={score:.2f})")
        else:
            self.on_game_end("KI kann nicht ziehen")
    else:
        self.info_label.config(text="Dein Zug")