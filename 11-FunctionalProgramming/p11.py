"""
Write a program that calculates the average speed of a vehicle. 
Enter from the keyboard: a distance in km, a number of travel hours and a number of travel minutes. 
Use an anonymous function.
"""

distance = int(input("Enter distance: "))
hours = int(input("Enter number of hours: "))
minutes = int(input("Enter number of minutes: "))

avg_speed = lambda distance, hours, minutes: round(distance/(hours+minutes/60),2)

print(avg_speed(distance, hours, minutes))