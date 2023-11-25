name = input("Enter product name: ")

if name == "jacket":
    time = 40
elif name == "underwear":
    time = 70
elif name == "shoes":
    time = 20
else:
    time = 60


rinse = input("Rinse? (y/n): ").lower().strip() == 'y'
spin = input("Spin? (y/n): ").lower().strip() == 'y'

if rinse:
    time += 15
if spin:
    time += 9

print(f"Total washing time: {time}")

