age = int(input("Enter the dog's age in human years:"))

if age == 1:
    dogAge = 10.5
elif age == 2:
    dogAge = 21
else:
    dogAge = 21 + 4*(age-2)

print(f"The dog's age in dog's years is {dogAge} years")  