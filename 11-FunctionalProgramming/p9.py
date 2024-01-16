"""
Write a program that converts speed in meters per second to speed in kilometers per hour.
"""

speed_convert = lambda x: x*3.6


speed1 = 35
speed2 = 2
print(f"{speed1} m/s = {speed_convert(speed1)} km/h")
print(f"{speed2} m/s = {speed_convert(speed2)} km/h")