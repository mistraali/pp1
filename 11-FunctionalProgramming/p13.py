"""
In a beverage factory, a machine fills bottles of various capacities. 
A computer checks whether a bottle has been filled correctly. 
The allowable tolerance is 2% for a 500ml bottle, 3% for a 1000ml bottle and 5% for a 1500ml bottle. 
Write a program that checks whether the bottle has been filled correctly or not. 
Define a higher order function. 
"""

def set_volume(capacity):
    tolerance = 0.02 if capacity == 500 else 0.03 if capacity == 1000 else 0.05 if capacity == 1500 else 0
    def check(volume):
        if volume <= capacity:
            return True if volume >= capacity*(1-tolerance) else False
        else:
            return True if volume < capacity*(1+tolerance) else False
    return check

print("-----500 ml")
check_fill = set_volume(500)
print(f"507: {check_fill(507)}")
print(f"489: {check_fill(489)}")
print("-----1000 ml")
check_fill = set_volume(1000)
print(f"984: {check_fill(984)}")
print(f"1032: {check_fill(1032)}")
print("-----1500 ml")
check_fill = set_volume(1500)
print(f"1578: {check_fill(1578)}")
print(f"1430: {check_fill(1430)}")