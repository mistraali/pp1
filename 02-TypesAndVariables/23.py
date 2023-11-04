from math import sqrt


a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

p = (a+b+c)/2
area = sqrt(p*(p-a)*(p-b)*(p-c))

print(f"Triangle area: {area}\nCircumference: {a+b+c}")