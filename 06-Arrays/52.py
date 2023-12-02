import random

arr = [[random.randint(0,20) for _ in range(5)] for _ in range(3)]

print(arr)

for n in arr:
    n[0], n[-1] = n[-1], n[0]

print(arr)