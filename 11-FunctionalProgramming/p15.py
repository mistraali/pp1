"""
Write a program that calculates and displays the number of letters in each word. 
Use the map() and an anonymous functions to calculate the number of letters. 
Tip: to split text into words, use the split() function. 
"""

text = "I completely agree with you"

letters_count = list(map(lambda s: len(s),text.split()))


print(letters_count)