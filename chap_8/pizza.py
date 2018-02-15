def make_pizza(size, *toppings):
    """
            Summary of the Pizza we are going to make
    """

    print("\nYou ordered a " + str(size) + '" pizza')
    print("The toppings in your pizza are:")

    for topping in toppings:
        print("	-" + topping)
