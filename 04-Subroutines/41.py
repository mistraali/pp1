from math import sqrt


def f(amount):
    if amount == 0: return 0
    if amount == 1: return 2
    number = 2
    for i in range (1,amount):
        j = number
        while True:
            check = True
            j += 1
            for n in range(2,int(sqrt(j))+1):
                if j%n == 0:
                    check = False
                    break
            if check == True: 
                number = j
                break
    return number


print(f(2))
print(f(3))
print(f(4))
print(f(5))
print(f(20))