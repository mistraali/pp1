current = int(input("Current: "))
previous = int(input("Previous: "))

if (previous-current)/previous >= 0.1:
    print("Buy the product")

print(f"Product price reduced by {((previous-current)/previous)*100}%")