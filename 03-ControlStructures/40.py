university = "Krakow University of Economics"

for i in range(len(university)):
    print(f"{university[i]}", end="")
    if not(i == len(university)):
        print(" ", end="")