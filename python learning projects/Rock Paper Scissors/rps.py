import random

selection = ["rock", "paper", "scissors"]
computer_selection = random.choice(selection)

while True:
  player_input = input("Rock, Paper or Scissors? ").lower()

  #Rock
  if player_input == "rock" and computer_selection == "paper":
    print("Computer picked paper. You lose!")
    break
  elif player_input == "rock" and computer_selection == "scissors":
    print("Computer picked scissors. You win!")
    break
  elif player_input == "rock" and computer_selection == "rock":
    print("Computer picked the same thing. Go again!")
  
  #Paper
  elif player_input == "paper" and computer_selection == "paper":
    print("Computer picked the same thing. Go again!")
  elif player_input == "paper" and computer_selection == "scissors":
    print("Computer picked scissors. You lose!")
    break
  elif player_input == "paper" and computer_selection == "rock":
    print("Computer picked rock. You win!")
    break

  #Scissors
  elif player_input == "scissors" and computer_selection == "paper":
    print("Computer picked paper. You win!")
    break
  elif player_input == "scissors" and computer_selection == "scissors":
    print("Computer picked the same thing. Go again!")
  elif player_input == "scissors" and computer_selection == "rock":
    print("Computer picked rock. You lose!")
    break

  else:
    print("Pick something real!")