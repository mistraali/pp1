"""
An array contains numbers from 1 to 20. 
Write a program that calculates and displays their third power. 
Use the map() and an anonymous function.
"""

numbers = [x+1 for x in range(20)]

cubed = list(map(lambda x: x**3, numbers))

print(*numbers, sep="\t")
print(*cubed, sep="\t")