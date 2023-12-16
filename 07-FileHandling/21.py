with open("07-FileHandling/p21.txt","w") as f:
    for i in range(1,51):
        f.write(str(i))
        if i != 50: f.write("\n")