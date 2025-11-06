print("Welcome to SMIT TechFest!")
print("Event organized by Leonardo Yangzon of APPDAET BTCS2")

participants = 0
while participants <= 0:
    participants = int(input("How many participants will register? "))
    if participants <= 0:
        print("Invalid number of participants.")
        break

if participants > 0:
    print()