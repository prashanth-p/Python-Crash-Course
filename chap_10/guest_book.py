from datetime import datetime

with open("guest_text.csv", 'a+') as fileObject:
    while(True):
        name = input("Enter your name, enter exit to quit:\n")
        if name == "exit":
            break
        else:
            print("Welcome back!")
            date = str(datetime.now().date())
            time = str(datetime.now().time())
            fileObject.write(name)
            fileObject.write(',')
            fileObject.write(date)
            fileObject.write(',')
            fileObject.write(time)
            fileObject.write('\n')
