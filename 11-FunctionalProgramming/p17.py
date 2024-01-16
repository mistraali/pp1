"""
Save the list of employees in a string array. 
Then, write a program that displays people whose surnames start with the letter 'J'. 
Use anonymous and filter() functions. 
"""

employees = ["SMITH Lucy","JONES Janet","LEE Jerry","JACKSON Peter","JOHNSON Rick","LEWIS Terry","CLARKE Robin"]

emp_j = list(filter(lambda s: s[0].lower() == 'j', employees))

print(*emp_j, sep="\t")