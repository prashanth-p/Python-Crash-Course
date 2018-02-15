from name_function import get_formatted_name

print("Enter q to quit any time")

while True:
    first = input("Please enter your full name:\n")
    if first == "q":
        break
    last = input("Please enter your second name:\n")
    if last == "q":
        break

    formatted_name = get_formatted_name(first, last)
    print("Neatly formatted name is: " + formatted_name + ".")
