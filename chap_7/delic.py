import sys
print(sys.version)

sandwich_orders = []
print("Enter quit to stop:")
msg = input("Enter the toppings you want:\n")
sandwich_orders.append(msg)
while(msg != "quit"):
    msg = input()
    if (msg != "quit"):
        sandwich_orders.append(msg)

finished_sandwiches = []
print(sandwich_orders)

for each in sandwich_orders:
    print("I just made you a", each, "sandwich")
    finished_sandwiches.append(each)
    # sandwich_orders.remove(each)
    # print(sandwich_orders)
    print()

print(finished_sandwiches)
