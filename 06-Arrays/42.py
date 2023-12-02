import random


def rand_elem(arr):
    return arr[random.randint(0,len(arr)-1)]


arr = [random.randint(0,20) for _ in range(random.randint(1,20))]

print(arr,rand_elem(arr))