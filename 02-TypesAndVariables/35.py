circumference = int(input("Enter circumference: "))

if circumference/3.14 >= 50:
    comp = True
else:
    comp = False

print(f"Tree can be cut down: {comp}")