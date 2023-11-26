def f(x,y):
    sum = 0
    for i in range(x,y+1):
        if not(i%2) and not(i%3) and i%4: sum += i
    return sum

print(f(1,20))
print(f(10,30))