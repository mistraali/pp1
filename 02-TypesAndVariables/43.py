name = input("Name: ")

i = 0
while i<len(name):
    print(f"{name[i]} ({ord(name[i])}) ")
    i+=1
