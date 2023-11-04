import random

sum = 0
for x in range(3):
    a=random.randint(1,6)
    print(f"Result from D6 roll: {a}")
    sum += a

print(f"Sum: {sum}")