from typing import Iterable

def transpose(m):
    if isinstance(m[0],Iterable):
        return list(map(list, zip(*m)))
    else:
        return list(map(list, zip(m)))
    
arr=[[5,6,0],[7,8,1]]
arr2=[5,6,7,8]
print(transpose(arr))
print(transpose(arr2))
    
