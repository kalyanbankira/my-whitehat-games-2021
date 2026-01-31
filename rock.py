import random
count_rock = 0
count_paper = 0
count_scissors = 0

player_score = 0
comp_score = 0

# Update the user's choice counts
def update_counts(user_input):
    global count_rock, count_paper, count_scissors
    if user_input == 0:
        count_rock += 1
    elif user_input == 1:
        count_paper += 1
    elif user_input == 2:
        count_scissors += 1

def predict():
    return random.choice([0, 1, 2])

# Update the scores after each round
def update_scores(user_input):
    global player_score, comp_score
    pred = predict()

    moves = ["ROCK", "PAPER", "SCISSORS"]

    print(f"\nYou played {moves[user_input]}, computer played {moves[pred]}.")

    # 0 = Rock, 1 = Paper, 2 = Scissors
    if user_input == pred:
        print("It's a tie!")
    elif (user_input == 0 and pred == 2) or (user_input == 1 and pred == 0) or (user_input == 2 and pred == 1):
        player_score += 1
        print("You win this round!")
    else:
        comp_score += 1
        print("Computer wins this round!")

    print(f"\nComputer Score: {comp_score} | Your Score: {player_score}")

# Main game loop
valid_entries = ['0', '1', '2']

while True:
    user_input = input("\nEnter 0 for ROCK, 1 for PAPER, and 2 for SCISSORS: ")

    while user_input not in valid_entries:
        print("\nInvalid Input!")
        user_input = input("Enter 0 for ROCK, 1 for PAPER, and 2 for SCISSORS: ")

    user_input = int(user_input)

    update_scores(user_input)
    update_counts(user_input)

    if comp_score == 10:
        print("\n💻 Computer Won the Game!")
        break
    elif player_score == 10:
        print("\n🎉 You Won the Game!")
        break
