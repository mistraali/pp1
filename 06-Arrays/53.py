def identity_matrix(x):
    arr = [[0 for _ in range(x)] for _ in range(x)]
    for n in range(x):
        arr[n][n] = 1
    return arr

print(identity_matrix(3))
print(identity_matrix(5))