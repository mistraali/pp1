"""
An array contains numbers from 1 to 20. 
Write a program that displays only numbers divisible by 2 and 3 without remainder. 
Use the filter() and an anonymous function.
"""

numbers = [x+1 for x in range(20)]

reduced = list(filter(lambda x: not(x % 2 and x % 3), numbers))

print(*reduced, sep="\t")