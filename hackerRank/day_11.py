import sys
print(sys.version)


def hourGlassSum(arr):
    sumBuff = 0
    for i in range(4):
        for j in range(4):
            # print(i, j)
            sumBuff = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + \
                arr[i + 1][j + 1] + arr[i + 2][j] + \
                arr[i + 2][j + 1] + arr[i + 2][j + 2]
            if (i == 0 and j == 0):
                maxSum = sumBuff
            if(sumBuff > maxSum):
                maxSum = sumBuff
        # print("sumBuff=", sumBuff)
        # print("maxSum=", maxSum)
        # print("i,j:", i, j)
        # print()
        # print()
    return maxSum


if __name__ == '__main__':
    arr = []
    for arr_i in range(6):
        arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
        arr.append(arr_t)

    # print(arr)
    maxVal = hourGlassSum(arr)
    print(maxVal)
