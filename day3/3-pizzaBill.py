# A simple pizza bill app
print("Welcome to baren Pizzas --🍕")
size=input("What size of pizza do you want? 'S', 'M' or 'L' ")
pepproni=input("Do you want pepproni? 'Y' or 'N' ")
extra_cheese=input("Do you want to have extra cheese? 'Y' or 'N ")
bill=0
if size=='S':
    bill=15
elif size=='M' :
    bill=20
else:
    bill=25
if pepproni=='Y':
    if size=='S':
        bill+=2
    else:
        bill+=3
if extra_cheese=='Y':
    bill+=1
print(f"Your final bill is ${bill}. Thank's for coming ")