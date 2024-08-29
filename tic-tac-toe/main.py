import tkinter as tk
WIN = 1000
DRAW = 0
LOSS = -1000
AI_MARKER = 'O'
PLAYER_MARKER = 'X'
EMPTY_SPACE = '-'
START_DEPTH = 0
class TicTacToeApp:
    winning_states = [
        # Every row
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],

        # Every column
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],

        # Every diagonal
        [(0, 0), (1, 1), (2, 2)],
        [(2, 0), (1, 1), (0, 2)]
    ]

    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.board = [[EMPTY_SPACE] * 3 for _ in range(3)]
        self.buttons = [[None] * 3 for _ in range(3)]
        self.create_widgets()
    
    def create_widgets(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.root, text=EMPTY_SPACE, font=('Arial', 40), width=5, height=2,
                                   command=lambda row=i, col=j: self.on_button_click(row, col))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button
        
        self.status_label = tk.Label(self.root, text="Player's turn", font=('Arial', 14))
        self.status_label.grid(row=3, column=0, columnspan=3)
    
    def on_button_click(self, row, col):
        if self.board[row][col] == EMPTY_SPACE and not self.game_is_done():
            self.board[row][col] = PLAYER_MARKER
            self.buttons[row][col].config(text=PLAYER_MARKER)
            if not self.game_is_done():
                self.ai_move()
                self.check_game_status()
    
    def ai_move(self):
        _, move = self.minimax_optimization(AI_MARKER, START_DEPTH, LOSS, WIN)
        if move != (-1, -1):
            row, col = move
            self.board[row][col] = AI_MARKER
            self.buttons[row][col].config(text=AI_MARKER)
    
    def check_game_status(self):
        state = self.get_board_state(PLAYER_MARKER)
        if state != DRAW:
            if state == WIN:
                self.status_label.config(text="Player Wins!")
            elif state == LOSS:
                self.status_label.config(text="AI Wins!")
            else:
                self.status_label.config(text="Draw!")
        else:
            self.status_label.config(text="Player's turn" if not self.game_is_done() else "AI's turn")
    
    def get_legal_moves(self):
        return [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == EMPTY_SPACE]
    
    def get_occupied_positions(self, marker):
        return [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == marker]
    
    def board_is_full(self):
        return len(self.get_legal_moves()) == 0
    
    def game_is_won(self, occupied_positions):
        for win_state in self.winning_states:
            if all(pos in occupied_positions for pos in win_state):
                return True
        return False
    
    def get_board_state(self, marker):
        opponent_marker = AI_MARKER if marker == PLAYER_MARKER else PLAYER_MARKER
        if self.game_is_won(self.get_occupied_positions(marker)):
            return WIN
        if self.game_is_won(self.get_occupied_positions(opponent_marker)):
            return LOSS
        if self.board_is_full():
            return DRAW
        return DRAW
    
    def minimax_optimization(self, marker, depth, alpha, beta):
        best_move = (-1, -1)
        best_score = LOSS if marker == AI_MARKER else WIN
        
        if self.board_is_full() or self.get_board_state(AI_MARKER) != DRAW:
            best_score = self.get_board_state(AI_MARKER)
            return best_score, best_move
        
        legal_moves = self.get_legal_moves()
        for move in legal_moves:
            row, col = move
            self.board[row][col] = marker
            
            if marker == AI_MARKER:
                score = self.minimax_optimization(PLAYER_MARKER, depth + 1, alpha, beta)[0]
                if score > best_score:
                    best_score = score - depth * 10
                    best_move = move
                alpha = max(alpha, best_score)
            else:
                score = self.minimax_optimization(AI_MARKER, depth + 1, alpha, beta)[0]
                if score < best_score:
                    best_score = score + depth * 10
                    best_move = move
                beta = min(beta, best_score)
            
            self.board[row][col] = EMPTY_SPACE
            if beta <= alpha:
                break
        
        return best_score, best_move
    
    def game_is_done(self):
        return self.board_is_full() or self.get_board_state(AI_MARKER) != DRAW

def main():
    root = tk.Tk()
    app = TicTacToeApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
