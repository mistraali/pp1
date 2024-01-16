"""
Write a program that calculates the total value of products in stock. 
Use the map(), sum() and an anonymous function. 
"""

stock = [(20,5.50),(15,8.30),(37,3.85),(4,11.60)]

total_value = round(sum(map(lambda t: round(t[0]*t[1],2), stock)),2)

print(*stock)
print(total_value)
