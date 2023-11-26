def f(number):
    string = ''
    for i in range(1,number+1):
        string += str(i)
    return string

print(f(11))
print(f(4))