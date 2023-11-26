def f(sentence):
    string = ''
    for i in sentence:
        if i != ' ': string += i
    return string

print(f("any seq more asd"))