def occurs(number,array):
    for i in array:
        if number == i: return True
    
#print(occurs(23,[15, 38, 7, 23, 14]))

number = int(input("Enter a number: "))
arr = [15, 38, 7, 23, 14]
print("Array: ", arr)
print(f"Result: number {number} {"appears" if occurs(number,arr) else "doesn't appear"} in the array")