import random


a=random.randint(1,6)

print("Guess!")
b = 0
while b != a:
    b = int(input())
print(f"That's right, it's {b}")