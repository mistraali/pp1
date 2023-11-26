def f(formula):
    sum = 0
    op='+'
    for i in formula:
        if i == '+':
            op = '+'
        elif i == '-':
            op = '-'
        else:
            if op == '+':
                sum += int(i)
            else:
                sum -= int(i)
    return sum

print(f("2+3"))
print(f("2+3-4+5-0"))