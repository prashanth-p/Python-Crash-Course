import sys
print(sys.version)


class Dog():
    """ A simple attempt to model a dog """

    def __init__(self, name, age):
        """Initialize name and age of dog"""
        self.name = name
        self.age = age

    def sit(self):
        """ Command to make the dog sit"""
        print(self.name.title() + " is now sitting")

    def roll(self):
        """ Command to make the dog roll """
        print(self.name.title() + " is now rolling")


if __name__ == '__main__':
    my_dog = Dog("coFFee", 5)
    my_dog.roll()
    my_dog.sit()
    print(my_dog.age)
