def f(number):
    number = str(number).strip()
    check = True
    for i in number:
        if not(i=='1' or i=='0'):
            check = False
    return check

if __name__ == "__main__":
    print("1010101",f("1010101"))
    print("a123",f("a123"))
