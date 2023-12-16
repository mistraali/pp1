import re

with open("07-FileHandling/p10.txt") as file:
    content = file.read()
    words = re.findall("\w{6,}",content)
    for word in words:
        print(word)