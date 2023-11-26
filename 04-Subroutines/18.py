def writeCon(n):
    string = ""
    for i in range (1,n+1):
        string += str(i)
        string += ' '
    return string.strip()


print(writeCon(15))
print(writeCon(7))