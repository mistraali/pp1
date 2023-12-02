def star(n):
    print(f"{n}: ", end='\t')
    for j in range(n):
        print("*",end='')
    print("")

arr = [12, 6, 4, 9, 10]

for i in arr:
    star(i)


