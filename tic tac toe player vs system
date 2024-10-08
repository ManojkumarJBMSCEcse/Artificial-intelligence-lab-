import random

class TicTacToe:
    def _init_(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        for row in range(3):
            print('|'.join(self.board[row*3:(row+1)*3]))
            if row < 2:
                print('-' * 5)

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def player_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = 'X'
            if self.winner('X'):
                self.current_winner = 'X'
            return True
        return False

    def ai_move(self):
        position = random.choice(self.available_moves())
        self.board[position] = 'O'
        if self.winner('O'):
            self.current_winner = 'O'

    def winner(self, letter):
        win_conditions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8), 
            (0, 3, 6), (1, 4, 7), (2, 5, 8), 
            (0, 4, 8), (2, 4, 6)
        ]
        for condition in win_conditions:
            if all(self.board[i] == letter for i in condition):
                return True
        return False

    def play_game(self):
        while self.empty_squares():
            self.print_board()
            valid_move = False
            while not valid_move:
                try:
                    position = int(input("Enter your move (1-9): ")) - 1
                    valid_move = self.player_move(position)
                    if not valid_move:
                        print("Invalid move. Try again.")
                except (ValueError, IndexError):
                    print("Invalid input. Enter a number between 1 and 9.")

            if self.current_winner:
                print("You win!")
                break

            if not self.empty_squares():
                print("It's a tie!")
                break

            self.ai_move()

            if self.current_winner:
                self.print_board()
                print("AI wins!")
                break

        if not self.current_winner:
            self.print_board()
            print("It's a tie!")

if _name_ == "_main_":
    game = TicTacToe()
    game.play_game()
