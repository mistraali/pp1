from math import sqrt


number = int(input("Enter number to check: "))
check = True
i = 2
if number == 1 or number == 0 or number < 0:
    check = False
else:
    while check == True and i <= sqrt(number):
        if not(number % i):
            check = False
        i += 1

print(check)