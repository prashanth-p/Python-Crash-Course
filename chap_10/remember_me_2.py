import json


def get_stored_username():
    """ This function will get the stored user name """
    fileName = "userName.json"
    try:
        with open(fileName) as fileObject:
            userName = json.load(fileObject)
    except FileNotFoundError:
        return None
    else:
        return userName


def get_new_userName():
    userName = input("\nEnter your name:\n")
    fileName = "userName.json"
    with open(fileName, "w") as fileObject:
        json.dump(userName, fileObject)
    return userName


def greet_user():
    userName = get_stored_username()
    if userName:
        print("Welcome back, " + userName + "!")
    else:
        userName = get_new_userName()
        print("We Will remember you, " + userName +
              " when you visit us again\n")


greet_user()
