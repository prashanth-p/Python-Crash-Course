from datetime import datetime
date = str(datetime.now())

name = input("Enter your name:\n")

with open("guests.txt", 'w') as fileObject:
    fileObject.write(name)
    fileObject.write(",")
    fileObject.write(date)
    fileObject.write("\n")
