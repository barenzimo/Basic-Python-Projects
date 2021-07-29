# Let's count the love percentage of you and your beloved

print("Welome to the love calculator..💖")

name1=input("What is your full name  😉\n").lower()
name2=input("What is their full name 😁\n").lower()

a=name1.count("t")+name1.count("r")+name1.count("u")+name1.count("e")+name2.count("t")+name2.count("r")+name2.count("u")+name2.count("e")
b=name1.count("l")+name1.count("o")+name1.count("v")+name1.count("e")+name2.count("l")+name2.count("o")+name2.count("u")+name2.count("e")
score=str(a)+str(b)
print(f"Your love percentage is {score} \n")
score=int(score)
if score<10 or score>90:
    print("You guys are like coke and mentos 😘🤞")
elif score>40 and score<50:
    print("You guys are alright together 😍\n")
