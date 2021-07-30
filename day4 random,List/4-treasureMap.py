## Let's fill out all the areas in the treasure map

print("Welcome to the treasure map🏴🗺 \n")
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map =[row1,row2,row3]
print(f"Here is your map\n\n{row1}\n{row2}\n{row3}")
position=(input("\nWhere do you want to put the treasure eg. 31 corresponds to 3rd rpw 1st column\n"))
a=int(position[0])
b=int(position[1])
map[a-1][b-1]="X"
# print(map[a][b])
print(f"Here is your map and the x represents treasure\n\n{row1}\n{row2}\n{row3}")






