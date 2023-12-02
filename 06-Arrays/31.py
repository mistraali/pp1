def unique_sorted(arr):
    return (list(set(arr)))

def unique(arr):
    ret_arr = list()
    for i in arr:
        if not(ret_arr.__contains__(i)): ret_arr.append(i) 
    return ret_arr



arr = [2,3,2,5,8,1,9,8]

print(unique_sorted(arr))
print(unique(arr))
