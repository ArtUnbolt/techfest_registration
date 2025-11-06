print("Welcome to SMIT TechFest!")
print("Event organized by Leonardo Yangzon of APPDAET BTCS2")

participants = 0
while participants <= 0:
    participants = int(input("How many participants will register? "))
    if participants <= 0:
        print("Invalid number of participants.")
        break

a = []
b = []
c = set()
records = {
"name": a,
"track": b
}

if participants > 0:
    for i in range(participants):
        name = input("Enter participant name: ")
        a.append(name)
        track = input("Enter chosen track: ")
        b.append(track)
        c.add(track)

print()
print("Registered participants:")

for i in range (0, participants):
    print(f"{i + 1}. {list(a)[i]} - {list(b)[i]}")

print()
if len(c) < 2:
    print("Not enough variety in tracks.")
else:
    print(f"Tracks offered in this event: {c}")