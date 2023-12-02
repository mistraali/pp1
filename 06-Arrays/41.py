#if arr1 is a subset of arr2
def check_subset(arr1,arr2):
    for i in arr1:
        check = False
        for j in arr2:
            if i == j:
                check = True
                break
        if not(check): return False
    return True


arr1 = [1,3,5]
arr2 = [i for i in range(1,10)]
arr3 = [1,9,6,5,2,5,7,8]

print(arr1,arr2,check_subset(arr1,arr2))
print(arr1,arr3,check_subset(arr1,arr3))