x = int(input("Enter X: "))
y = int(input("Enter Y: "))

if x == 0 and y == 0:
    print("P(0,0) is the center")
elif x == 0:
    print(f"P(0,{y}) is on X axis")
elif y == 0:
    print(f"P({x},0) is on Y axis")
elif x > 0 and y > 0:
    print(f"P({x},{y}) is in the first quadrant")
elif x < 0 and y > 0:
    print(f"P({x},{y}) is in the second quadrant")
elif x < 0 and y < 0:
    print(f"P({x},{y}) is in the third quadrant")
else:
    print(f"P({x},{y}) is in the forth quadrant")