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

import random

pc_choice = random.randint(0,2)
player_choice = int(input("What do you choose ? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

options = [rock, paper, scissors]

if player_choice >= 3 or player_choice < 0:
    print("You have chosen a wrong number")
else:
    print(f"You have chosen: \n {options[player_choice]}")
    print(f"PC have chosen: \n {options[pc_choice]}")
    if player_choice == 0 and pc_choice == 0:
        print("\nIt is a draw!")
    elif player_choice == 1 and pc_choice == 0:
        print("\nYou have won!")
    elif player_choice == 2 and pc_choice ==0:
        print("\nComputer has won!")
    elif player_choice == 0 and pc_choice == 1:
        print("\nComputer has won!")
    elif player_choice == 1 and pc_choice == 1:
        print("\nIt is a draw!")
    elif player_choice == 2 and pc_choice == 1:
        print("\nYou have won!")
    elif player_choice == 0 and pc_choice == 2:
        print("\nYou have won!")
    elif player_choice == 1 and pc_choice == 2:
        print("\nComputer has won!")
    else:
        print("\nIt is a draw!")