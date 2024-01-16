"""
Write a program that creates a bar chart showing temperatures recorded in cities. 
Add a title for the chart and descriptions for the x and y axes. 
Tip: use the map() function to create two arrays of data for the chart.
"""
import matplotlib.pyplot as plt

temps = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}

x = list(map(lambda x: x, temps))
y = list(map(lambda x: temps[x], temps))

chart = plt.subplot()
chart.bar(x,y)
chart.set_title("Temperatury w miastach")
chart.set_ylabel("Temperatura")
chart.set_xlabel("Miasta")
plt.show()