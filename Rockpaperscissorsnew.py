import random
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
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
options = [rock, paper, scissors]
play_game = int(input("What do you choose? 0 for rock,  1 for paper, 2 for scissors. \n"))
cpu_choice = random.randint(0, 2)
if play_game >= 3:
    print("Invalid Input")
elif play_game >= 0:
    print(options[play_game])
    print("Computer chose: \n" + options[cpu_choice])
else:
    print("Invalid Input")

if play_game > 2:
    print("Invalid Input")
elif play_game == 0 and cpu_choice == 2:
    print("You win!")
elif cpu_choice == 0 and play_game == 2:
    print("You lose.")
elif play_game > cpu_choice:
    print("You win!")
elif play_game == cpu_choice:
    print("You draw.")
elif cpu_choice > play_game:
    print("You lose.")