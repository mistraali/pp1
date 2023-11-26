def f(code):
    code = int(code)
    sum = 0
    control = code % 10
    code //= 10
    while code > 0:
        sum += code % 10
        code //= 10
    
    return True if sum % 7 == control else False

print(f("1082"))
print(f("2035"))
print(f("1114"))