speed = int(input("Enter speed: "))

comp = False

if speed >= 40 and speed <= 140:
    comp = True

print(f"Speed is valid: {comp}")