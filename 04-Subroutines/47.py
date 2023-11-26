def f(text):
    if len(text) == 0: return ''
    if len(text) == 1: return 'text'
    string = text[0]
    for i in range(1,len(text)):
        string = string + '-' + text[i]
    return string

print(f("University"))
print(f("UE"))
print(f("x"))
print(f(""))