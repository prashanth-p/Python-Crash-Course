def isnumber(a):
    try:
        int(str(a))
    except:
        bool_a = False
    else:
        bool_a = True
    return bool_a

"""
x = input("\nEnter data:\n")
checkX = isnumber(x)
if checkX:
    print("It is Integer")
else:
    print("Invalid Input")
"""
largest = None
smallest = None

while True:
    num = input("Enter a number: ")

    if num == "done":
        break

    checkX = isnumber(num)
    if not(checkX):
        print("Invalid Input")
        continue
    elif checkX:
        num = int(num)

    if largest is None:
        largest = num
        smallest = num

    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

print("largest:", largest)
print("smallest:", smallest)
