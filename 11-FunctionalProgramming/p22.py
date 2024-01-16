"""
Write a program that determines and displays a list of employees whose last names are given in capital letters followed by first names, 
separated by commas.
"""

emp = [("Smith","Lucy"),("Jones","Janet"),("Lee","Jerry"),("Jackson","Peter"),("Johnson","Rick"),("Lewis","Terry"),("Clarke","Robin")]

print(*list(map(lambda e: f"{e[0].upper()}, {e[1]}",emp)), sep="\n")