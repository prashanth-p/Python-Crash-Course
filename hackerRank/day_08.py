import sys
# print(sys.version)

n = int(input())
phoneBook = {}


def checkKeyExists(keyVal, dic):
    #print("In Function")
    # print(keyVal)
    # print(dic)
    if (keyVal in dic):
        return dic[keyVal]
    else:
        return 0

if __name__ == "__main__":
    for i in range(0, n):
        buff = [x for x in input().lower().split(" ")]
        phoneBook[buff[0]] = int(buff[1])

    for i in range(0, n):
        keyVal = input().split()
        # print(keyVal)
        Value = checkKeyExists(keyVal[0], phoneBook)
        if (Value == 0):
            print("Not Found")
        else:
            print(str(keyVal[0]) + "=" + str(Value))
