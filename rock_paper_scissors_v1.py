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
print("Welcome to the exciting game of ROCK PAPER SCISSORS!!")
human_choice = int(input("Write 1 for ROCK, 2 for PAPER OR 3 for SCISSORS.\n"))
computer_choice = random.randint(1,3)

RPS=[]

if human_choice == 1 and computer_choice==1:
    print(f"You Chose:\n{rock}\nComputer Chose:\n{rock}")
    print("It's a Draw")
elif human_choice == 1 and computer_choice==2:
    print(f"You Chose:\n{rock}\nComputer Chose:\n{paper}")
    print("You Lose")
elif human_choice == 1 and computer_choice==3:
    print(f"You Chose:\n{rock}\nComputer Chose:\n{scissors}")
    print("You Won!")
elif human_choice == 2 and computer_choice==2:
    print(f"You Chose:\n{rock}\nComputer Chose:\n{rock}")
    print("It's a Draw")
elif human_choice == 2 and computer_choice==3:
    print(f"You Chose:\n{rock}\nComputer Chose:\n{paper}")
    print("You Lose")
elif human_choice == 2 and computer_choice==1:
    print(f"You Chose:\n{rock}\nComputer Chose:\n{scissors}")
    print("You Won!")
elif human_choice == 3 and computer_choice==3:
    print(f"You Chose:\n{rock}\nComputer Chose:\n{rock}")
    print("It's a Draw")
elif human_choice == 3 and computer_choice==1:
    print(f"You Chose:\n{rock}\nComputer Chose:\n{paper}")
    print("You Lose")
elif human_choice == 3 and computer_choice==2:
    print(f"You Chose:\n{rock}\nComputer Chose:\n{scissors}")
    print("You Won!")
else:
    print("You entered an invalid number. You Lose.")