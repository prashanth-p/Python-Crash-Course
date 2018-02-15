fileName = "learning_python.txt"

with open(fileName) as fileObject:
    data = fileObject.read()

with open(fileName) as fileObject:
    dataLines = fileObject.readlines()

print(data)
print()
print()

for line in dataLines:
    line = line.replace("python", "c++")
    print(line)
