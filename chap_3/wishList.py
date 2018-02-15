wishList = []
wishList.append("d")
wishList.append("g")
wishList.append("a")
wishList.append("p")
wishList.append("c")
print(wishList)
print(sorted(wishList))
print()
# order not changed. same order
print(wishList)
print(list(reversed(wishList)))
print(wishList)
print()

wishList.sort()
print(wishList)
wishList.sort(reverse=True)
print(wishList)
print()
print(len(wishList))

# print(wishList[5])
