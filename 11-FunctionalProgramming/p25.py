"""
Write a program that displays the names of towns where positive temperatures were recorded. 
Use anonymous and filter() functions.
"""

temps = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}

print(*list(map(lambda x: x[0], filter(lambda x: x[1]>0, temps.items()))), sep="\t")

print(*list(filter(lambda x: temps[x]>0,temps)), sep="\t")