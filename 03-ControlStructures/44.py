quantity = 0
sum = 0


while True:
    number = int(input("Enter number: "))
    if number == 0:
        break
    else:
        quantity += 1
        sum += number

print(f"Result : quantity = {quantity}, sum = {sum}, mean = {sum/quantity}")
