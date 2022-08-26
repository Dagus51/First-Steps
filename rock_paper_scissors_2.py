import random

player = input('Player name: ')

choices = ["rock", "paper", "scissors"]
computer_points = 0
player_points = 0

while computer_points != 3 and player_points != 3:
    player_choice_is_right = True
    while player_choice_is_right:
        player_choice = input("Rock, Paper or Scissors?:").lower()
        if player_choice in choices:
            player_choice_is_right = False
      
        computer_choice = random.choice(choices)
    
    if player_choice == 'paper' and computer_choice == 'rock' \
    or player_choice == 'rock' and computer_choice == 'scissors' \
    or player_choice == 'scissors' and computer_choice == 'paper':
        player_points += 1   
        
    elif player_choice == computer_choice:
        print("Draw!")
    else:
        computer_points += 1
    
    print(player,':', player_points)
    print('computer:', computer_points)
        
if player_points < computer_points:
    print('Whole game won computer')
else:
    print('Whole game won ',player)