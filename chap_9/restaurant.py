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


if __name__ == '__main__':
    my_restaurant = Restaurant("fisherman's warf", "goan")
    # print(my_restaurant.restaurant_name)
    # print(my_restaurant.cuisine_type)
    my_restaurant.open_restaurant()
    my_restaurant.descirbe_restaurant()
    print()
    print("Number of customers served:", my_restaurant.number_served)
    my_restaurant.set_number_served(0)
    print()
    print("Number of customers served:", my_restaurant.number_served)
    my_restaurant.inc_number_served(255)
    print()
    print("Number of customers served:", my_restaurant.number_served)
"""
    annies_kitchen = Restaurant("annies_kitchen", "kerala")
    annies_kitchen.open_restaurant()
    annies_kitchen.descirbe_restaurant()
    print()

    jose_kitchen = Restaurant("jose etans mess", "thalassery")
    jose_kitchen.open_restaurant()
    jose_kitchen.descirbe_restaurant()
    print()
"""
