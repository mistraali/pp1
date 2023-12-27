def f(arr):
    if arr[0] == arr [1]:
        return compare(arr, arr[0])
    elif arr[0] == arr[2]:
        return arr[1]
    else:
        return arr[0]

def compare(arr, n):
    for i in arr:
        if i != n:
            return i
    return None

if __name__ == "__main__":
    print(f([7,7,7,7,7,5,7,7]))
    print(f([7,5,7,7,7,7,7,7]))
    print(f([5,7,7,7,7,7,7,7]))
    print(f([7,7,5,7,7,7,7,7]))