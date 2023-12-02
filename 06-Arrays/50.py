#findmax = true if searching max, else searching min
def find(arr,findmax):
    x = 0
    y = 0
    value = arr[0][0]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if findmax:
                if arr[i][j]>value:
                    value = arr[i][j]
                    x=i
                    y=j
            else:
                if arr[i][j]<value:
                    value = arr[i][j]
                    x=i
                    y=j
    return (value,x,y)

arr = [[-38, 19], [5,40],[-7,11],[29,16]]

print(find(arr,True))
print(find(arr,False))