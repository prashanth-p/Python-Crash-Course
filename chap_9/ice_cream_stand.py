import sys
print(sys.version)
print()


class Restaurant():
    """Model Of a restaurant """

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def descirbe_restaurant(self):
        print("The name of the restaurant is " + self.restaurant_name.title())
        print("They serve " + self.cuisine_type.title() + " food.")

    def open_restaurant(self):
        print(self.restaurant_name.title() + " is now Open")

    def set_number_served(self, num):
        self.number_served = num

    def inc_number_served(self, num):
        self.number_served += num


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type, flavours):
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = flavours
        # for each in flavours:
        #   self.flavours.append(each)

    def displayFlavours(self):
        """
            Display Flavours of icecream
        """
        print("The Different flavours of icecream we have are:")
        print(self.flavours)

if __name__ == '__main__':
    icecream = []
    buff = ""
    print("Enter the Different varieties of icecream:")
    print("Enter Done to finalize the menu")
    while True:
        buff = input()
        if buff == "done":
            break
        icecream.append(buff)

    print()
    print()
    myIceCreamShop = IceCreamStand("Corner House", "icecream", icecream)

    myIceCreamShop.open_restaurant()
    myIceCreamShop.descirbe_restaurant()
    print()
    print("Number of customers served:", myIceCreamShop.number_served)
    myIceCreamShop.set_number_served(0)
    print()
    print("Number of customers served:", myIceCreamShop.number_served)
    myIceCreamShop.inc_number_served(255)
    print()
    print("Number of customers served:", myIceCreamShop.number_served)
    print()
    myIceCreamShop.displayFlavours()
    print()
