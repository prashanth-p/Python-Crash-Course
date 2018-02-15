def mainpList(funLis, cmd, N):
    funCMD = cmd[0]
    if funCMD == "insert":
        i = int(cmd[1])
        e = int(cmd[2])
        funLis.insert(i, e)

    elif funCMD == "print":
        print(funLis)

    elif funCMD == "remove":
        e = int(cmd[1])
        funLis.remove(e)

    elif funCMD == "append":
        e = int(cmd[1])
        funLis.append(e)

    elif funCMD == "sort":
        funLis.sort()

    elif funCMD == "pop":
        funLis.pop()

    elif funCMD == "reverse":
        funLis.sort(reverse=True)


if __name__ == '__main__':
    lis = []
    N = int(input("\nEnter the N:\n"))
    count = 0
    while(count < N):
        cmd = input("\nenter the content:\n").split()
        mainpList(lis, cmd, N)
        count = count + 1

for i in range(0, 5):
    print(i)

