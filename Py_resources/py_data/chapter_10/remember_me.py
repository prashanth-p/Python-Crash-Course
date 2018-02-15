import json

userName = input("\nEnter your name:\n")
fileName = "userName.json"

with open(fileName, "w") as fileObject:
    json.dump(userName, fileObject)
    print("We Will remember you when you visit us again\n")
