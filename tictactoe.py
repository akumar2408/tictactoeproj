import random

class TicTacToe:
    def __init__(self, size=3):
        self.size = size
        self.board = [[' ' for _ in range(size)] for _ in range(size)]
        self.current_turn = 'X'
        self.game_over = False
        self.winner = None

    def print_board(self):
        # Print the board
        print('\n' + '-' * (self.size * 2 + 1))
        for row in self.board:
            print('|' + '|'.join(row) + '|')
        print('-' * (self.size * 2 + 1))

    def check_winner(self):
        # Check horizontal, vertical, and diagonal lines for a win
        lines = []
        for i in range(self.size):
            lines.append(self.board[i])  # Horizontal
            lines.append([self.board[j][i] for j in range(self.size)])  # Vertical
        lines.append([self.board[i][i] for i in range(self.size)])  # Diagonal \
        lines.append([self.board[i][self.size - 1 - i] for i in range(self.size)])  # Diagonal /

        for line in lines:
            if line.count(line[0]) == self.size and line[0] != ' ':
                self.game_over = True
                self.winner = line[0]
                return

        if all(cell != ' ' for row in self.board for cell in row):
            self.game_over = True

    def player_move(self, row, col):
        if 0 <= row < self.size and 0 <= col < self.size and self.board[row][col] == ' ':
            self.board[row][col] = self.current_turn
            self.check_winner()
            self.current_turn = 'O' if self.current_turn == 'X' else 'X'
            return True
        return False

    def ai_move(self):
        while not self.game_over:
            row, col = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
            if self.player_move(row, col):
                break

    def play_game(self):
        print("Welcome to Tic Tac Toe!")
        self.print_board()
        while not self.game_over:
            if self.current_turn == 'X':
                try:
                    row, col = map(int, input("Enter row and column numbers (0 indexed) separated by space: ").split())
                    if not self.player_move(row, col):
                        print("Invalid move, try again.")
                except ValueError:
                    print("Please enter valid integers.")
            else:
                self.ai_move()
            self.print_board()

        if self.winner:
            print(f"{self.winner} wins!")
        else:
            print("It's a tie!")

# Example usage
if __name__ == "__main__":
    size = input("Enter the size of the Tic Tac Toe board (default is 3): ")
    try:
        size = int(size)
    except ValueError:
        size = 3
    game = TicTacToe(size)
    game.play_game()
