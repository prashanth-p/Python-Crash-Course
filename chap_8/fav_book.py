import sys
print(sys.version)


def favorite_book(favBook):
    print("My favorite book is " + favBook.title())

if __name__ == '__main__':
    book = input("enter your favorite book:\n")
    favorite_book(book)
