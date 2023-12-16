letters = [chr(ord('a')+x) for x in range(5)]

print(letters)

f = open("07-FileHandling/p13.txt","wt")

for x in letters[:-1]:
    f.write(x+"\n")
f.write(letters[-1])
f.close()