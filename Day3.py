print("Welcome to Python Pizza Deliveries!")
size=input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_chesse=input("Do you want extra cheese? Y or N: ")

#todo: work out how much they need to pay based on their size choice. 
pizzaprice=0
if size == "S":
    pizzaprice=15
elif size=="M":
    pizzaprice=20
else:
    pizzaprice=25

#todo: work out how much to add to their bill based on their pepperoni choice.
if size=="S":
    if pepperoni=="Y":
        pizzaprice=15+2
elif size=="L":
    if pepperoni=="Y":
        pizzaprice=25+3



#todo: work out their final amount based on wheter if they want extra cheese.
if size == "S":
    if extra_chesse=="Y":
        pizzaprice+=1
    
elif size=="M":
    if extra_chesse=="Y":
        pizzaprice+=1
else:
    if extra_chesse=="Y":
        pizzaprice+=1

print(f"Your final bill is {pizzaprice}")
