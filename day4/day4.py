#!/opt/anaconda3/bin/python

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

playerChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if playerChoice == 0:
    print(rock)
elif playerChoice == 1:
    print(paper)
elif playerChoice == 2:
    print(scissors)
else:
    print("invalid choice")
computerChoice = random.randint(0,2)
print("Computer chose:")
if computerChoice == 0:
    print(rock)
elif computerChoice == 1:
    print(paper)
elif computerChoice == 2:
    print(scissors)
if playerChoice == computerChoice:
    print("Tie")
elif playerChoice == 0 and computerChoice == 1:
    print("You lose")
elif playerChoice == 0 and computerChoice == 2:
    print("You win")
elif playerChoice == 1 and computerChoice == 0:
    print("You win")
elif playerChoice == 1 and computerChoice == 2:
    print("You lose")
elif playerChoice == 2 and computerChoice == 0:
    print("You lose")
elif playerChoice == 2 and computerChoice == 1:
    print("You win")

