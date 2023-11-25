a = int(input("Enter a: "))
b = int(input("Enter b: "))

for i in range(1,a+1):
    for n in range(1,b+1):
        if i==1 or i==(a):
            print("*",end="")
        else:
            if n==1 or n==(b):
                print("*",end="")
            else:
                print(" ", end="")
    print("")