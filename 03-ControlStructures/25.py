number = int(input("Number of products: "))
price = int(input("Price: "))

if number < 2:
    print(f"Amount to pay: {number*price}")
else:
    print(f"Amount to pay: {2*price + (number-2)*price*0.75}")