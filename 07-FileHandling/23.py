with open("07-FileHandling/p23.txt","w") as f:
    for i in range(1,11):
        f.write(f"{i} {i**2} {i**3}")
        if i != 10: f.write("\n")