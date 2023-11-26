def check_if_binary(number):
    number = str(number).strip()
    check = True
    for i in number:
        if not(i=='1' or i=='0'):
            check = False
    return check


print("1010101",check_if_binary("1010101"))
print("a123",check_if_binary("a123"))
