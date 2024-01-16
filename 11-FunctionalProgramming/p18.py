"""
Write a program that displays speed values higher than the allowed speed. 
Use anonymous and filter() functions. 
"""

recorded_speeds = [48,47,54,50,42,68,39,46]

print(list(filter(lambda x: x>50, recorded_speeds)))