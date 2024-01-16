"""
Write a program that calculates and displays student scores that are equal to or greater 
than the following minimum number of points to pass the course:         a. 70        b. 40        c. 30
Use the filter() function and the following higher order function:
    def min_pts(limit):
        return lambda pts: pts>=limit
"""

def min_pts(limit):
        return lambda pts: pts>=limit

grades = [37,51,44,23,78,92,39,84,83,51]

print(f"All aquired grades:    {grades}")
print(f"Grades higher than 70: {list(filter(min_pts(70),grades))}")
print(f"Grades higher than 40: {list(filter(min_pts(40),grades))}")
print(f"Grades higher than 30: {list(filter(min_pts(30),grades))}")