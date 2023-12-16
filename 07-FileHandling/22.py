import random


with open("07-FileHandling/p22.txt","w") as f:
    i = 0
    while True:
        f.write(str(random.randint(100,999)))
        i += 1
        if i < 50:
            f.write("\n")
        else:
            break