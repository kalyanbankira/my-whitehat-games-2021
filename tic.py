# Look out for all empty positions and return empty positions

def empty_positions(tic_tac_toe):
  # declare the position list.
    positions = []
   # use for loop to iterate over all the positions and return rows and columns of empty cells.
    for i in range(3):
        for j in range(3):
              if tic_tac_toe[i][j] == 0:
                positions.append((i, j))
    return(positions)


#Evaluate weather we have reached any conclusion or not

def evaluate(tic_tac_toe):
# check any conclusion wrt columns for player 1

# First condition is provided as a hint.
    if tic_tac_toe[0][0]==1 and tic_tac_toe[1][0]==1 and tic_tac_toe[2][0]==1:
        return 1
    elif tic_tac_toe[0][1]==1 and tic_tac_toe[1][1]==1 and tic_tac_toe[2][1]==1:
        return 1
    elif tic_tac_toe[0][2]==1 and tic_tac_toe[1][2]==1 and tic_tac_toe[2][2]==1:
        return 1

# check any conclusion wrt rows for player 1
    elif tic_tac_toe[0][0]==1 and tic_tac_toe[0][1]==1 and tic_tac_toe[0][2]==1:
        return 1
    elif tic_tac_toe[1][0]==1 and tic_tac_toe[1][1]==1 and tic_tac_toe[1][2]==1:
        return 1
    elif tic_tac_toe[2][0]==1 and tic_tac_toe[2][1]==1 and tic_tac_toe[2][2]==1:
        return 1

# check any conclusion wrt diagonals for player 1
    elif tic_tac_toe[0][0]==1 and tic_tac_toe[1][1]==1 and tic_tac_toe[2][2]==1:
        return 1
    elif tic_tac_toe[0][2]==1 and tic_tac_toe[1][1]==1 and tic_tac_toe[2][0]==1:
        return 1


# check any conclusion wrt columns for player 2

    elif tic_tac_toe[0][0]==2 and tic_tac_toe[1][0]==2 and tic_tac_toe[2][0]==2:
        return 2
    elif tic_tac_toe[0][1]==2 and tic_tac_toe[1][1]==2 and tic_tac_toe[2][1]==2:
        return 2
    elif tic_tac_toe[0][2]==2 and tic_tac_toe[1][2]==2 and tic_tac_toe[2][2]==2:
        return 2

# check any conclusion wrt rows for player 2
    elif tic_tac_toe[0][0]==2 and tic_tac_toe[0][1]==2 and tic_tac_toe[0][2]==2:
        return 2
    elif tic_tac_toe[1][0]==2 and tic_tac_toe[1][1]==2 and tic_tac_toe[1][2]==2:
        return 2
    elif tic_tac_toe[2][0]==2 and tic_tac_toe[2][1]==2 and tic_tac_toe[2][2]==2:
        return 2

# check any conclusion wrt diagonals for player 2
    elif tic_tac_toe[0][0]==2 and tic_tac_toe[1][1]==2 and tic_tac_toe[2][2]==2:
        return 2
    elif tic_tac_toe[0][2]==2 and tic_tac_toe[1][1]==2 and tic_tac_toe[2][0]==2:
        return 2


# Return 0 if no conclusions are made
    else:
        return 0


#Import random Module

import random

# Play tic-tac-toe for each player with Random algorithm

# No.of wins for players
player1_wins=0
player2_wins=0
draw=0

# First player one will have the first move in the first game. Each time player wins the game another player will have the first attempt in the next game.

player=1


# We will play 100 games.

print("LET'S PLAY TIC-TAC-TOE!!")

for i in range(100):
  # tic-tac-toe Board 3*3 list
    tic_tac_toe=[[0,0,0],[0,0,0],[0,0,0]]
    print(" Start Game : ",i+1) # i starts from index 0

  # Checking for all the empty positions
    emp_positions=empty_positions(tic_tac_toe)
    print(" Start Game : ",i+1) # i starts from index 0

# while loop will run till there are no empty positions
    while(emp_positions):
         # Get move for player1
        if player==1:
        # Change in strategy than random
            if tic_tac_toe[1][1]==0 :
                playi=1
                playj=1
                print("Player 1 move:",playi,playj)


            else:
                playi,playj=random.choice(emp_positions)
                print("Player 1 move:",playi,playj)
            tic_tac_toe[playi][playj]=1
            player=2

  # Get move for player2
        elif player==2:
            playi,playj=random.choice(emp_positions)
            print("Player 2 move:",playi,playj)
            tic_tac_toe[playi][playj]=2
            player=1
# Evaluate results
        eval = evaluate(tic_tac_toe)

        if eval==1:
            print("Game Over")
            for i in range(3):
                print(tic_tac_toe[i][0],tic_tac_toe[i][1],tic_tac_toe[i][2])
            print('Player 1 wins')
            print("-----------------------------")
            player1_wins=player1_wins+1
            break

        elif eval==2:
            print("Game Over")
            for i in range(3):
                print(tic_tac_toe[i][0],tic_tac_toe[i][1],tic_tac_toe[i][2])
            print('Player 2 wins')
            print("-----------------------------")
            player2_wins=player2_wins+1
            break

# Check for empty position and return draw if no empty space is found.
        emp_positions=empty_positions(tic_tac_toe)

        if not emp_positions:
            print("Game Over")
            for i in range(3):
                print(tic_tac_toe[i][0],tic_tac_toe[i][1],tic_tac_toe[i][2])
            print('Game draw')
            print("-----------------------------")

            draw=draw+1
            break

# Print the number of wins and loses by respective players
print("Number of wins for player 1 are: ",player1_wins)
print("Number of wins for player 2 are: ",player2_wins)
print("Number of draws are:             ",draw)



# Here we change strategy by putting first mark at the center.
# This is implemented only for player1

player1_wins=0
player2_wins=0
draw=0
player=1

print("LET'S PLAY TIC-TAC-TOE!!")

# Play tic-tac-toe player1 with AI bot algorithm and  player2 with Random algorithm

# No.of wins for players

for i in range(100):
  # tic-tac-toe Board 3*3 list
    tic_tac_toe=[[0,0,0],[0,0,0],[0,0,0]]

  # Checking for all the empty positions
    emp_positions=empty_positions(tic_tac_toe)
    print(" Start Game : ",i+1) # i starts from index 0


  # while loop will run till there are no empty positions
    while(emp_positions):

  # Get move for player1
        if player==1:

      # Change in strategy than random
            if tic_tac_toe[1][1]==0 :
                playi=1
                playj=1
                print("Player 1 move:",playi,playj)


            else:
                playi,playj=random.choice(emp_positions)
                print("Player 1 move:",playi,playj)
            tic_tac_toe[playi][playj]=1
            player=2


    # Get move for player2
        elif player==2:
            playi,playj=random.choice(emp_positions)
            print("Player 2 move:",playi,playj)
            tic_tac_toe[playi][playj]=2
            player=1


# Evaluate results
        eval=evaluate(tic_tac_toe)

        if eval==1:
            print("Game Over")
            for i in range(3):
                print(tic_tac_toe[i][0],tic_tac_toe[i][1],tic_tac_toe[i][2])
            print('Player 1 wins')
            print("-----------------------------")
            player1_wins=player1_wins+1
            break

        elif eval==2:
            print("Game Over")
            for i in range(3):
                print(tic_tac_toe[i][0],tic_tac_toe[i][1],tic_tac_toe[i][2])
            print('Player 2 wins')
            print("-----------------------------")

            player2_wins=player2_wins+1
            break

    # Check for empty position and return draw if no empty space is found.
        emp_positions=empty_positions(tic_tac_toe)

        if not emp_positions:
            print("Game Over")
            for i in range(3):
                print(tic_tac_toe[i][0],tic_tac_toe[i][1],tic_tac_toe[i][2])
            print('Game draw')
            print("-----------------------------")

            draw=draw+1
            break

# Print the number of wins and loses by respective players
# Driver Code
print("Number of wins for player 1 are: ",player1_wins)
print("Number of wins for player 2 are: ",player2_wins)
print("Number of draws are            : ",draw)

