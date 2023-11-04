import random

a=random.randint(1,6)
print(f"Result from D6 roll: {a}")

if a == 1 or a == 6: 
    comp = True 
else: 
    comp = False
print(f"Special: {comp}")