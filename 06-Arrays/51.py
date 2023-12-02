import random

arr = [[random.randint(0,20) for _ in range(5)] for _ in range(3)]

print(arr)

arr[0], arr[-1] = arr[-1], arr[0]

print(arr)