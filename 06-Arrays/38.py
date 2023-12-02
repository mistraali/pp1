def check_number(n, arr):
    new_arr = sorted(arr) 
    for i in range(len(new_arr)):
        if n <= new_arr[i]: return i


arr = [7,3,8,5,2]
print(check_number(5, arr))
