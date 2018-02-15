N = int(input())
count = 0
while(count < N):
    s = input()
    # print(s)
    for i in range(0, len(s)):
        if ((i % 2) == 0):
            print(s[i], end="")
    print("", end=" ")
    for i in range(0, len(s)):
        if ((i % 2) != 0):
            print(s[i], end="")
    count += 1
