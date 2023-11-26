def f(number):
    sum = 0
    number = str(number)
    for i in range(1,10):
        count = 0
        for j in number:
            if int(j) == i: count += 1
        if count >= 2: sum += i*count
    return sum

print(f(1027))
print(f(230335))
print(f(513553007))