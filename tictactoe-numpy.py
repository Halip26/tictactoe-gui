import numpy as np


def create_board():
    return np.zeros((3, 3), dtype=int)


def print_board(board):
    symbols = {0: " ", 1: "X", 2: "O"}
    for row in board:
        print(" | ".join(symbols[val] for val in row))
        print("---------")


def is_winner(board, player):
    # Check rows, columns, and diagonals for a win
    return (
        np.any(np.all(board == player, axis=1))
        or np.any(np.all(board == player, axis=0))  # rows
        or np.all(np.diag(board) == player)  # columns
        or np.all(np.diag(np.fliplr(board)) == player)  # main diagonal
    )  # anti-diagonal


def is_board_full(board):
    return not any(0 in row for row in board)


def take_turn(board, player):
    while True:
        try:
            row = int(input(f"Player {player}, enter the row (0, 1, 2): "))
            col = int(input(f"Player {player}, enter the column (0, 1, 2): "))
            if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == 0:
                board[row][col] = player
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def play_game():
    board = create_board()
    player = 1

    while True:
        print_board(board)
        take_turn(board, player)

        if is_winner(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        player = 3 - player  # Switch player (1 -> 2 or 2 -> 1)


if __name__ == "__main__":
    play_game()
