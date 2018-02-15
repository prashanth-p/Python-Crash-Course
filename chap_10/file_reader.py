import sys
print(sys.version)

filePath = "../text_files/py_digits.txt"
with open(filePath) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    print(line.rstrip())
    pi_string += line.strip()

print()
print(lines)
print()
print(pi_string)
