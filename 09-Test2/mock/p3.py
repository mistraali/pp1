def f(array2d):
    l = len(array2d)
    for i in range(l):
        sum_r = 0
        for j in array2d[i]:
            sum_r += j
        sum_c = 0
        for j in range(l):
            sum_c += array2d[j][i]
        if sum_r != sum_c:
            return False
    return True

if __name__ == "__main__":
    print(f([[3,7,2],[4,2,5],[5,2,1]]))
    print(f([[3,7,2],[4,2,5],[9,2,1]]))