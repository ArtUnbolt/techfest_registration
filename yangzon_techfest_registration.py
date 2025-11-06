print("Welcome to SMIT TechFest!")
print("Event organized by Leonardo Yangzon of APPDAET BTCS2")

participants = 0
while participants <= 0:
    participants = int(input("How many participants will register? "))
    if participants <= 0:
        print("Invalid number of participants.")
        break

a = set()
b = set()
records = {
"name": a,
"track": b
}

if participants > 0:
    for i in range(participants):
        name = input("Enter participant name: ")
        a.add(name)
        track = input("Enter chosen track: ")
        b.add(track)

print("Registered participants:")

for i in range (0, participants):
    print(f"{i + 1}. {list(a)[i]} - {list(b)[i]}")
