import random

## Python program to check who's going to pay the bill
print("Welcome to bill picker ")
str= input("Enter the names separated by comma\n ex: Rahul, Raj etc --")
nameList= str.split(", ")
randomName=nameList[random.randint(0, len(nameList)-1)]
print(f"{randomName} is going to pay the bill ")