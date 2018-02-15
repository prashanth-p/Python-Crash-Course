oddNum = []
for val in range(0, 20):
    if ((val + 1) % 2) != 0:
        oddNum.append(val + 1)
print(oddNum)

mulThree = []
tf = []
for val in range(0, 30):
    # if ((val + 1) % 2) == 0:
    mulThree.append(val + 1)
    if (((val + 1) % 3) == 0):
        tf.append(val + 1)

print(mulThree)
print(tf)

cube = [(val + 1)**3 for val in range(0, 10)]
print(cube)
print(cube[0:3])
print("the last three elements are:", cube[-3:])
print(cube[-3:])
