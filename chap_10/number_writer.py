import json

numbers = [5, 6, 7, 8, 9, 10]

fileName = "numbers.json"
with open(fileName, 'w') as fileObject:
    json.dump(numbers, fileObject)
