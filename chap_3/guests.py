guestNames = ["ashish", "afsal", "ranjith"]
for i in range(0, len(guestNames)):
    print("I invite You, " + guestNames[i] + ", for a dinner party on ddmmyy")
print()

# adding more names
cantMakeIt = guestNames[1]
guestNames.remove(cantMakeIt)
newFriend = "Haley"
guestNames.insert(1, newFriend)
for i in range(0, len(guestNames)):
    print("I invite You, " + guestNames[i] + ", for a dinner party on ddmmyy")
print()
guestNames.insert(0, "khan")
guestNames.append("Pauly")
guestNames.insert(round(len(guestNames) / 2), "Nivin")
for i in range(0, len(guestNames)):
    print("I invite You, " + guestNames[i] + ", for a dinner party on ddmmyy")
print()

# removing the contents only 2 should remain
while(len(guestNames) > 2):
    temp = guestNames.pop()
    print("sorry, " + temp + " the table is full. Maybe next time. ")

print()
del guestNames[1]
del guestNames[0]
print(guestNames)
