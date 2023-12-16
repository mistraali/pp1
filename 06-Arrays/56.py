def two_to_one(arr):
    new_arr = []
    for rows in arr:
        for columns in rows:
            new_arr.append(columns)
    return new_arr

a = [[2,3],[1,5]]
print(two_to_one(a))