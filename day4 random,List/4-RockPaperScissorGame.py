# A simple rock, paper and scissors game
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

options =[rock, paper, scissors]
x=int(input("Chose between Rock-0, Paper-1, Scissors-2  "))
y=random.randint(0,2)
print(f"You chose {options[x]}\n Computer chose {options[y]}")

if (x==0 and y==1) or (x==1 and y==2) or (x==2 and y==0):
    print("Computer wins.. Try again 😉")
elif x==y:
    print("It's a draw 😄")
else: print("You won!! Congratulations 🥳😇")

