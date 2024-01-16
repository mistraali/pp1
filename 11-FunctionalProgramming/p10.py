"""
Write a program that calculates the average speed of a vehicle. 
Enter from the keyboard: a distance in km, a number of travel hours and a number of travel minutes. 
Define a function avg_speed(distance,hours,minutes) that returns the calculated average speed. 
"""


distance = int(input("Enter distance: "))
hours = int(input("Enter number of hours: "))
minutes = int(input("Enter number of minutes: "))

def avg_speed(distance, hours, minutes):
    return round(distance/(hours + minutes/60),2)

print(avg_speed(distance, hours, minutes))