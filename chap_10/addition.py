def isNumber(x):
    print("In function isNumber: ", x)
    try:
        y = int(x)
    except ValueError or TypeError:
        print("Input should be a number")
        return False
    else:
        return y


while(True):
    x = input("enter a number:\n")
    buff = isNumber(x)
    if buff:
        x = buff
        break

while(True):
    y = input("Enter a number:\n")
    buff = isNumber(y)
    if buff:
        y = buff
        break

print(x + y)
