import json

fileName = "userName.json"
userName = input("Enter your login ID:\n")

with open(fileName) as fileObject:
    userName = json.load(fileObject)
    print("Welcome back, " + userName + "!")
