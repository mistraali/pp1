"""
Write a program that calculates and displays transaction amounts in Polish zlotys (1 EUR = 4.5 PLN). 
Use anonymous and map() functions. 
"""

eur = [15.90,38.47,4.07,132.70,9.15]

pln = list(map(lambda x: round(x*4.5,2),eur))

print(*eur, sep="\t")
print(*pln, sep="\t")
