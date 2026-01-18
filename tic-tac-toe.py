import numpy as np
import random

n = 3  # board size (5x5) change as needed

def print_board(board):
    print("\n")
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()
    print()

def check_winner(board, player):
    # Check rows
    for row in range(n):
        if np.all(board[row, :] == player):   #np.all() checks if all elements match (for win detection)
            return True
    
    # Check columns
    for col in range(n):
        if np.all(board[:, col] == player):
            return True
    
    # Check diagonals
    if np.all(np.diag(board) == player): #np.diag() gets diagonal elements
        return True
    if np.all(np.diag(np.fliplr(board)) == player): #np.fliplr() flips board for anti-diagonal check
        return True
    
    return False

def check_draw(board):
    return not np.any(board == ' ')

def computer_move(board):
    empty = np.argwhere(board == ' ') #np.argwhere() finds empty positions
    row, col = empty[random.randint(0, len(empty) - 1)]
    return row, col

# Initialize board
board = np.full((n, n), ' ', dtype=str)
current_player = 'X'
move_count = 0

print(f"{n}×{n} Tic-Tac-Toe")
print_board(board)

# Game loop
while True:
    move_count += 1
    row, col = computer_move(board)
    board[row, col] = current_player

    print(f"Move {move_count}: Player {current_player}")
    print_board(board)
    
    if check_winner(board, current_player):
        print(f"Player {current_player} WINS!")
        break
    
    if check_draw(board):
        print("It's a DRAW!")
        break
    
    current_player = 'O' if current_player == 'X' else 'X'