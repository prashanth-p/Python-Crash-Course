import json
# JSON.DUMP(dataVariable, fileObject)
# JSON.LOAD(fileObject)
# numbers = [5, 6, 7, 8, 9, 10]

fileName = "numbers.json"
with open(fileName) as fileObject:
    numbers = json.load(fileObject)

print(numbers)
