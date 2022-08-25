import random

player = input('Player name: ')

choices = ["rock", "paper", "scissors"]
computer_points = 0
player_points = 0

while True:
    computer_choice = random.choice(choices)
    player_choice = input("Rock, Paper or Scissors?:").lower()
    print("Computer picks " + computer_choice)

    if player_choice == computer_choice:
        print("Draw!")
    elif player_choice == "rock":
        if computer_choice == "paper":
            computer_points += 1
        else:
            player_points += 1
    elif player_choice == "paper":
        if computer_choice == "scissors":
            computer_points += 1
        else:
            player_points += 1
    elif player_choice == "scissors":
        if computer_choice == "rock":
            computer_points += 1
        else:
            player_points += 1
    elif player_choice == "":
        break
    else:
        print(player + " please pick a valid choice")
    if player_points == 3:
        print('Whole game win ' + player + ' !!!')
        break
    if computer_points == 3:
        print('Whole game win computer !!!')
        break
    print(player + " score:", player_points)
    print("Computer score:", computer_points)