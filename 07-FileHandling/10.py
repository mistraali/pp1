f = open("./07-FileHandling/p10.txt","r")

for x in f:
    print(x, end="")

f.close()