f = open("./07-FileHandling/p8.txt")

counter = 0

for x in f:
    counter += 1
    print(f"{counter}. {x}", end="")

f.close()