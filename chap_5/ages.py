age = int(input("\nEnter your age:\n"))

if(age < 2):
    print("You are still a baby")
elif(age >= 2 and age < 4):
    print("You are a toddler")
elif(age >= 4 and age < 13):
    print("You are a kid")
elif(age >= 13 and age < 20):
    print("You are a teenager")
elif(age >= 20 and age < 65):
    print("You are an adult")
elif(age >= 65):
    print("You are now old!")
