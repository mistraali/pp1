from typing import Iterable


def transpose(arr):
    new_arr = []
    for x in range(len(arr)):
        if isinstance(arr[x],Iterable):
            for y in range(len(arr[x])):
                new_arr[y][x]=arr[x][y]
        else:
            new_arr[0][x] = arr[x]
    return new_arr


arr=[[5,6],[7,8]]
print(transpose(arr))
    
