import random

def border(arr):
    for _ in range(len(arr)*5 + 1):
        print("-",end="")
    print("")
    for i in arr:
        print("|", end="")
        for _ in range(4-digits(i)):
            print(" ", end="")
        print(i, end="")
    print("|")
    for _ in range(len(arr)*5 + 1):
        print("-",end="")


def digits(n):
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count


arr = [random.randint(0,1000) for _ in range(random.randint(1,20))]

border(arr)