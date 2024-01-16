"""
Write a program that displays the data of countries that have won at least 10 medals. 
Use anonymous and filter() functions.
"""


medals = [{"country":"Denmark","gold":2,"silver":4,"bronze":6},
{"country":"Finland","gold":5,"silver":0,"bronze":4},
{"country":"USA","gold":12,"silver":5,"bronze":11},
{"country":"Peru","gold":0,"silver":1,"bronze":7}]

medal_count = lambda x: x["gold"] + x["silver"] + x["bronze"] >= 10

print(*list(map(lambda x: x["country"], filter(medal_count, medals))), sep="\t")

