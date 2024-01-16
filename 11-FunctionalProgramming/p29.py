"""
Write a program that creates a bar chart showing the total number of medals won by each country.
Add a title for the chart and descriptions for the x and y axes. 
Tip: Use the map() function to create arrays of data for your chart.
"""

from matplotlib import pyplot as plt


medals = [{"country":"Denmark","gold":2,"silver":4,"bronze":6},
{"country":"Finland","gold":5,"silver":0,"bronze":4},
{"country":"USA","gold":12,"silver":5,"bronze":11},
{"country":"Peru","gold":0,"silver":1,"bronze":7}]


total_medals = lambda x: x["gold"] + x["silver"] + x["bronze"]

x = list(map(lambda x: x["country"], medals))
y = list(map(total_medals, medals))

chart = plt.subplot()
chart.bar(x,y)
chart.set_title("Liczba medali wg kraju")
chart.set_ylabel("liczba medali")
chart.set_xlabel("Kraje")
plt.show()