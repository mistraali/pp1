import re

f = open("07-FileHandling/p14.txt","a+")

f.seek(0)
read_product = True
counter = 0
for row in f:
    if len(row) > 1:    counter = int(re.findall(r"\d", str(row))[0])

while read_product:
    product = input("Enter product name: ")
    if product != "":
        if counter > 0: f.write("\n")
        counter +=1
        f.write(f"{counter}. {product}")
    else:
        read_product = False
f.close()