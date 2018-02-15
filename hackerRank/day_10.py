import sys
# print(sys.version)


def maxOnes(num):
    maxCount = 0
    count = 0
    while(num != 0):
        rem = num % 2
        num = num // 2
        # print("count=", count)
        # print("rem=", rem)
        # print("maxCount=", maxCount)
        # print("num=", num)

        if(rem == 1):
            count = count + 1

        elif(rem == 0):
            count = 0

        if(count > maxCount):
            maxCount = count

        # print("countUpdated=", count)
        # print("maxCountUpdated=", maxCount)
        # print()
        # print()
    return maxCount


p = maxOnes(int(input()))
print(p)
