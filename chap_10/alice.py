def count_words(fileName):
    """ Count the approximate number of words in a file. """
    try:
        with open(fileName) as fileObject:
            contents = fileObject.read()

    except FileNotFoundError:
        # fail silently
        pass
        # msg = "Sorry, the file " + fileName + " is not found!"
        # print(msg)

    else:
        words = contents.split()
        print(len(words))

filenames = ['../Py_resources/py_data/chapter_10/alice.txt',
             '../Py_resources/py_data/chapter_10/sidartha.txt',
             '../Py_resources/py_data/chapter_10/moby_dick.txt',
             '../Py_resources/py_data/chapter_10/little_women.txt']

for filename in filenames:
    count_words(filename)
fileName = "../Py_resources/py_data/chapter_10/alice.txt"
count_words(fileName)
