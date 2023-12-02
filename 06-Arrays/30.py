def bubblesort(array):
    for j in range(len(array)-1):
        for i in range(len(array) - 1 - j):
            if array[i] > array[i+1]: 
                array[i], array[i+1] = array[i+1], array[i]
    return array

print(bubblesort([4,36,12,28,9,44,5]))

print(bubblesort([x for x in range(10,0,-1)]))