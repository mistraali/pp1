for i in range(1,8):
    for j in range(i,50,7):
        print(f"{f"  {j}" if j<10 else f" {j}"}", end="")
    print()