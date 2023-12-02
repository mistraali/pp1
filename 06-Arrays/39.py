import random


def checker(arr, odd):
    new_arr = []
    for i in arr:
        if odd:
            if i%2: new_arr.append(i)
        else:
            if not(i%2): new_arr.append(i)
    return new_arr

arr = [random.randint(0,20) for _ in range(10)]
print(arr)
print(checker(arr, False))
print(checker(arr, True))