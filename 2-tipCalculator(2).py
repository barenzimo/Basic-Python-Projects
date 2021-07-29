#A simple tip calculator to calculate your tips

print("Welcome to the tip calculator \n")
bill=float(input("What was the total bill paid? $"))
tip_percent=float(input("What percentage of bill would you like to give? 10, 12 or 15? "))
people=int(input("How many people are splitting the bill? "))
total=float(bill+(bill*tip_percent/100))
answer=round(total/people,2)

print(f"Each person should pay ${answer}")