f = open("07-FileHandling/p11.txt","r")

sum = 0
print("Numbers: ", end="")
for x in f:
    n = int(x)
    print(n, end=" ")
    sum += n
print(f"\nSum: {sum}")
f.close()