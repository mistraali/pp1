def f(number):
    string = ''
    if number == 0: return ''
    number -= 1
    string += "*"
    while number:
        string +="/*"
        number -= 1
    return string

print(f(4))
print(f(1))