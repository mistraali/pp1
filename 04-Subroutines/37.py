def f(n):
    if n == 1: return 0
    if n == 2: return 1
    a = 0
    b = 1
    for i in range (0,n-2):
        b = b + a
        a = b - a
    return b

print(f(5))
print(f(9))