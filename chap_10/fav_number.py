import json


def getNumber():
    try:
        x = int(input("Enter Your Favorite number:\n"))
    except ValueError or TypeError:
        print("Enter a number")
    else:
        return x


x = getNumber()
fileName = "fav_number.json"

with open(fileName, "w") as fileObject:
    json.dump(x, fileObject)
