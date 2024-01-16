"""
Write a program that displays students whose scores are between 50 and 70 points. 
Use an anonymous function and filter() function.
"""

test_results = [
    {"name":"Peter","result":27},
    {"name":"Anna","result":63},
    {"name":"Robert","result":92},
    {"name":"Paul","result":46},
    {"name":"Barbara","result":52}]

check_score = lambda x: x["result"]>50 and x["result"]<70

print(*list(map(lambda x: x["name"], filter(check_score, test_results))), sep="\t")