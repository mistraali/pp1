"""
Write a program that converts speed in meters per second to speed in kilometers per hour. 
Define a function ms_to_kmh(ms) that returns the calculated speed in km/h.
"""

def ms_to_kmh(ms):
    return round(ms*3.6,2)

speed1 = 35
speed2 = 2
print(f"{speed1} m/s = {ms_to_kmh(speed1)} km/h")
print(f"{speed2} m/s = {ms_to_kmh(speed2)} km/h")