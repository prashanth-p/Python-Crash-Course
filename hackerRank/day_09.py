import sys
print(sys.version)


def fact(n):
    if n != 0:
        return n*fact(n-1)
    if n == 0:
        return 1

if __name__ == "__main__":
    n = int(input())
    res = fact(n)
    print(res)
