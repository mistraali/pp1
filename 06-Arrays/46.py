from typing import Iterable

def show(arr):
    for i in arr:
        for j in i:
            print(j,end=" ")
        print("")

def show_rec(arr):
    if not(isinstance(arr,Iterable)): 
        print(arr,end=" ")
    else:
        for i in range(len(arr)):
            show_rec(arr[i])
        print("")


arr = [[1,2],[3,4],[5,6],[7,8]]
show(arr)
show_rec(arr)


