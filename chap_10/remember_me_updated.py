import json


def greetUser():
    """ Greet the user by their name """
    fileName = "Name.json"
    try:
        with open(fileName) as fileObject:
            userName = json.load(fileObject)

    except FileNotFoundError:
        userName = input("\nEnter your name:\n")

        with open(fileName, "w") as fileObject:
            json.dump(userName, fileObject)
            print("We Will remember you when you visit us again\n")

    else:
        print("Welcome back, " + userName + "!")


greetUser()
