# Create a game that plays rock, paper, and scissors with the computer,
# randomly choosing one of the three for 10 turns.

import random

player_wins  = 0
computer_wins = 0
draws = 0

accepted_guesses = ["rock", "paper", "scissor"]

def AI_guess():
    comp_choices = ["rock", "paper", "scissor"]
    random_guess = random.randint(0, len(comp_choices)-1)
    return comp_choices[random_guess]

def winner(player, computer):

    if computer == "scissor" and player == "paper":
        return computer

    elif computer == "paper" and player == "rock":
        return computer

    elif computer == "rock" and player == "scissor":
        return computer

    elif player == "scissor" and computer == "paper":
        return player

    elif player == "paper" and computer == "rock":
        return player

    elif player == "rock" and computer == "scissor":
        return player

    elif player == computer:
        return "draw"

    else:
        raise None

turns = 0

while turns < 10:
    print(f"ROUND {turns+1}")
    player_turn = str(input("Guess!! (rock, paper or scissor)\nMake a guess:"))

    while player_turn not in accepted_guesses:
        player_turn = str(input("\nWRONG GUESS \nMake a guess:"))

    print()
    computer_guess = AI_guess()
    print(f"PLAYER: {player_turn}")
    print(f"COMPUTER: {computer_guess}")

    if winner(player_turn, computer_guess) == computer_guess:
        print("Computer WINS\n")
        computer_wins += 1

    elif  winner(player_turn, computer_guess) == player_turn:
        print("Player WINS\n")
        player_wins += 1

    elif  winner(player_turn, computer_guess) ==  "draw":
        print("It is a DRAW\n")
        draws += 1

    turns += 1

print(f"Computer Total wins: {computer_wins}")
print(f"Player Total wins: {player_wins}")
print(f"Total number of draws:{draws}")


if computer_wins == player_wins:
    print("\nThe overall wins ended up with a DRAW")

elif computer_wins > player_wins:
    print("\nOverall, the Computer WON")

elif computer_wins < player_wins:
    print("\nOverall, the Player WON")



