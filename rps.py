from random import randint

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
# Pick a random number from 1 to 3
num = randint(1, 3)

# Turn that random number into the computer's RPS move
computer_move = num
if computer_move == 1:
    rock
elif computer_move == 2:
    paper
else:
    scissors
# Ask a user to enter their move
user_move = input("Please choose ROCK,PAPER OR SCISSORS: ")

# Print the rock, paper, or scissors ASCII art that corresponds to the player's move
if user_move == "ROCK":
    print(rock)
elif user_move == "PAPER":
    print(paper)
elif user_move == "SCISSORS":
    print(scissors)

# Print the rock, paper, or scissors ASCII art that corresponds to the computer's move
if computer_move == 1:
    print(rock)
elif computer_move == 2:
    print(paper)
elif computer_move == 3:
    print(scissors)
# Figure out who wins and print the result!


# Rock beats scissors
if user_move == "ROCK" and computer_move == 3:
    print("PLAYER WINS!!!!!")
elif computer_move == 1 and user_move == "SCISSORS":
    print("COMPUTER WINS")
elif user_move == "PAPER" and computer_move == 1:
    print("PLAYER WINS")
elif computer_move == 2 and user_move == "ROCK":
    print("COMPUTER WINS")
elif user_move == "SCISSORS" and computer_move == 2:
    print("PLAYER WINS")
elif computer_move == 3 and user_move == "SCISSORS":
    print("COMPUTER WINS")
elif user_move and computer_move:
    print("ITS A TIE")
