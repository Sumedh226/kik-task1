
import random

# Create a 3x3 grid
board = [" " for i in range(9)]

# Display the grid
def print_board():
    print()
    for i in range(0, 9, 3):
        print(" " + " | ".join(board[i:i+3]))
        if i < 6:
            print("---+---+---")
    print()

# Check for a winner
def check_winner():
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in winning_combinations:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]

    if " " not in board:
        return "Draw"

    return None

# Human player's turn
def player_move():
    while True:
        try:
            move = int(input("Enter position (1-9): ")) - 1

            if 0 <= move < 9 and board[move] == " ":
                board[move] = "X"
                break
            else:
                print("Invalid move! Try again.")
        except ValueError:
            print("Please enter a number.")

# Computer's turn
def computer_move():
    empty_spaces = [
        i for i in range(9) if board[i] == " "
    ]

    if empty_spaces:
        move = random.choice(empty_spaces)
        board[move] = "O"
        print("Computer chose position:", move + 1)

# Main game
print("Welcome to Tic-Tac-Toe!")
print("You are X and Computer is O")

while True:
    print_board()
    player_move()

    result = check_winner()
    if result:
        break

    computer_move()

    result = check_winner()
    if result:
        break

# Display final result
print_board()

if result == "Draw":
    print("It's a Draw!")
elif result == "X":
    print("Congratulations! You Win!")
else:
    print("Computer Wins!")
