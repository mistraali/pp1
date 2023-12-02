#A
#Returns seconds largest element of a given array
def second_largest(arr):
    new_arr = sorted(arr)
    return new_arr[-2] if len(new_arr) > 1 else None

#B
#Value amplitude of a given array
def amplitude(arr):
    new_arr = sorted(arr)
    return new_arr[-1]-new_arr[0] if len(new_arr) > 0 else None

#C
#Median of values from a given array
def median(arr):
    new_arr = sorted(arr)
    return new_arr[len(new_arr)//2] if len(new_arr) > 0 else None

#D
#Returns extreme values from a given array as 2 element array
def extremes(arr):
    new_arr = sorted(arr)
    return [new_arr[0],new_arr[-1]] if len(new_arr) > 0 else None

#E
#toString() with '-' as separator
def to_string(arr):
    new_string = ""
    for n in arr:
        new_string += str(n) + '-'
    return new_string[:-1]