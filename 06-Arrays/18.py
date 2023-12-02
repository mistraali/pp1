arr = [[True,False],[True,True],[False,False]]
print(arr)
for i in arr:
    for j in range(0,len(i)):
        i[j] = not(i[j])
        

print(arr)