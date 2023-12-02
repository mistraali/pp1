def create_2d_arr(x,y):
    return [[0 for _ in range(y)] for _ in range(x)]

arr = create_2d_arr(5,5)

for n in range(len(arr)):
    for i in range(len(arr[n])):
        arr[n][i] = (n+1)*(i+1)

for x in arr:
    print(x)