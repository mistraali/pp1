for i in range(1,6):
    for j in range(1,i+1):
        print("* ", end="")
    print("")
    if i == 5:
        for j in reversed(range(1,5)):
            for k in range (1,j+1):
                print("* ", end="")
            print("")