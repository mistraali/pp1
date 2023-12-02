arr1 = [4,36,12,28,9,44,5] 
arr2 = [5,1,36]

for i in arr1:
    display = True
    for j in arr2:
        if i == j: display = False
    if display: print(i,end=" ") 