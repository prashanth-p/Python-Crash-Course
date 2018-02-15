fileName = '../Py_resources/py_data/chapter_10/pi_million_digits.txt'

with open(fileName) as fileObject:
    lines = fileObject.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()


birthday = input("Enter your birthday in mmddyy: \n")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("fuck off xD")
