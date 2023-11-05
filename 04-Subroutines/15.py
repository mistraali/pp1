def keypad():

    n = 1
    for i in range (3):
        for j in range (3):
            print(f"{n} ", end="")
            n += 1
        print("")


def keypad2():
    for i in range(1,10):
        print(f"{i} ", end="")
        if not(i%3): 
            print("")


keypad()
print("")
keypad2()