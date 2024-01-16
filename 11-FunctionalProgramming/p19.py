"""
Write a program that calculates the arithmetic mean of the grades, excluding negative grades (2.0). 
Use the filter() along with an anonymous function.
"""

grades = [3.0,5.0,2.0,3.5,4.0,4.0,3.5,2.0,4.0,2,0]

pos_grades = list(filter(lambda x: x>=3.0, grades))

pos_mean = round(sum(pos_grades)/len(pos_grades),2)

print(grades)
print(pos_mean)