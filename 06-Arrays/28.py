def compare(arr1,arr2):
    if len(arr1)!=len(arr2):
        return False
    else:
        for i in range(len(arr1)):
            if arr1[i] != arr2[i]:
                return False
    return True

def compare1(arr1,arr2):
    if arr1 == arr2:
        return True
    else:
        return False

print(compare(["water","book","sky"],["water","book","sky"]))
print(compare([True,False],[True,False,True]))
print(compare([5,3,1],[5,3,1]))
print(compare([3,2,1],[3,2]))

print(compare1([3,2],[3,2]))