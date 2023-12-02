arr = [[3,9,2],[2,4,5],[7,1,6],[0,4,8]]

sum = 0

for i in range(0,len(arr)):
    for j in range(0,len(arr[0])):
        if arr[i][j]%2: sum += arr[i][j]

print(sum)