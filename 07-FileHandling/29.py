import re

with open("07-FileHandling/p29.txt") as file:
    content = file.read()

grades = re.findall(r"\d\.\d",content)
sum = 0
for grade in grades:
    sum += float(grade)
print(sum/len(grades))