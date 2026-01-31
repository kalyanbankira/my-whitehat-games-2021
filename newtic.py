import random

# ------------------------------------
# Function: Return all empty positions
# ------------------------------------
def empty_positions(board):
    positions = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                positions.append((i, j))
    return positions


# ------------------------------------
# Function: Evaluate board result
# ------------------------------------
def evaluate(board):
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != 0:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != 0:
            return board[0][i]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != 0:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != 0:
        return board[0][2]
    # No winner yet
    return 0


# ------------------------------------
# Function: Smart move for Player 1
# ------------------------------------
def best_move(board):
    # 1️⃣ Take center if available
    if board[1][1] == 0:
        return (1, 1)
    # 2️⃣ Take corners if available
    for (i, j) in [(0,0), (0,2), (2,0), (2,2)]:
        if board[i][j] == 0:
            return (i, j)
    # 3️⃣ Otherwise, random move
    return random.choice(empty_positions(board))


# ------------------------------------
# Simulate 100 Games
# ------------------------------------
print("🎮 LET'S PLAY 100 ROUNDS OF TIC-TAC-TOE!\n")

player1_wins = 0
player2_wins = 0
draws = 0

# Start with Player 1
starting_player = 1

for game in range(1, 101):
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    player = starting_player
    emp_positions = empty_positions(board)

    while emp_positions:
        # Player 1 (smart)
        if player == 1:
            playi, playj = best_move(board)
            board[playi][playj] = 1
            player = 2
        # Player 2 (random)
        else:
            playi, playj = random.choice(emp_positions)
            board[playi][playj] = 2
            player = 1

        result = evaluate(board)
        if result != 0:
            if result == 1:
                player1_wins += 1
            else:
                player2_wins += 1
            break

        emp_positions = empty_positions(board)

        # Draw condition
        if not emp_positions:
            draws += 1
            break

    # Alternate first player next game
    starting_player = 1 if starting_player == 2 else 2


# ------------------------------------
# Final Results
# ------------------------------------
print("🏁 RESULTS AFTER 100 GAMES:")
print("-----------------------------")
print(f"Player 1 (Smart AI) Wins : {player1_wins}")
print(f"Player 2 (Random) Wins   : {player2_wins}")
print(f"Draws                    : {draws}")
print("-----------------------------")

if player1_wins > player2_wins:
    print("✅ Player 1 dominates with smart strategy!")
elif player2_wins > player1_wins:
    print("🤖 Random Player 2 wins surprisingly!")
else:
    print("😐 It's a balanced match overall!")
