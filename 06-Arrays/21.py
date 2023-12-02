arr = [15, 8, 31, 47, 2, 19]

for i in range(len(arr)):
    print(f"{arr[-i-1]} ",end="")

arr2 = arr
arr2.reverse()
print("\n",arr)
print(arr2)