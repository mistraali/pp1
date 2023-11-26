def f(sentence):
    if len(sentence) != 0: 
        string = sentence[0]
    else:
        return None

    for i in range(1,len(sentence.strip())):
        if sentence[i-1] == ' ' and sentence[i] != ' ': string += sentence[i]
    return string

print(f("Internet of Things"))
print(f("iee  iee  iee"))
print(f(""))
print(f("a"))
