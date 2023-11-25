a = 0
b = 1
print(f"{a} {b}", end="")
for i in range(1,19):
    b = a + b
    a = b - a
    print(f" {b}", end="")