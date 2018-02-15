print("Enter two numbers and i will divide them")
print("Enter q to quit")

while True:
    numOne = input("Enter the first Number:\t")
    if numOne == 'q':
        break
    numOne = int(numOne)
    numTwo = input("Enter second number:\t")
    if numTwo == 'q':
        break
    numTwo = int(numTwo)
    try:
        print(numOne / numTwo)
    except ZeroDivisionError:
        print("You cannot divide by zero")
