# Create Name List
names = ["eric", "chris", "sam", "bumble"]
print(names[0])
print(names[3])

# Greetings
print("Hello, " + names[0].title() + " !")
print("Hello, " + names[1].title() + " !")
print("Hello, " + names[2].title() + " !")
print("Hello, " + names[3].title() + " !")

s = input()
print(s)
countEven = 0
countOdd = 0
evenS = []
oddS = []
for i in range(0, len(s)):
    if ((i % 2) == 0):
        print(s[i], end="")
print("", end=" ")
for i in range(0, len(s)):
    if ((i % 2) != 0):
        print(s[i], end="")

# print(evenS + " " + oddS)
