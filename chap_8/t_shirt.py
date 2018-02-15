import sys
print(sys.version)


def make_tshirt(size, text="I LOVE PYTHON!! xD"):
    print("The size of the T shirt is: " + size)
    print('The message which will be printed is: "' + text + '" ')
    print()
    print()


if __name__ == '__main__':

    # positional arguments
    make_tshirt("M", "I love you")

    # keyword arguments
    make_tshirt(text="Fuck you", size="L")

    # equivalent function calls
    make_tshirt("S")
    make_tshirt("XL")
    make_tshirt("XL", "Python is kickass")
    make_tshirt(size="XS", text="I love programming")
