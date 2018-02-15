import sys
print(sys.version)
print()
print()


def showMagicians(magicians):
    print(magicians)


def makeGreat(magicians):
    for i, magician in enumerate(magicians):
        magician = "The Great " + magician
        magicians[i] = magician
    return magicians

if __name__ == '__main__':
    magicians = ["Rupert", "ALbert", "Nano", "Coffee"]
    # copyMagicians = magicians[:]
    greatMagicians = makeGreat(magicians[:])

    print("Original List of magicians:")
    showMagicians(magicians)
    print()
    print()
    print("These Magicians are now great")
    showMagicians(greatMagicians)
