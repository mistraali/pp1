def keypad():

    n = 1
    for i in range (3):
        for j in range (3):
            print(f"{n}", end="")
            n += 1
            if (j+1)%3:
                print(f" ", end="")
        print("")


def keypad2():
    for i in range(1,10):
        print(f"{i}", end="")
        if not(i%3): 
            print("")
        else:
            print(" ", end="")


keypad()
print("")
keypad2()