amount = int(input("Enter the amount: "))

division = amount
fives = division // 5
division -= 5*fives
twos = division // 2
division -= 2*twos

print(f"The amount of PLN {amount} in coins: {fives} fives, {twos} twos, {division} ones")