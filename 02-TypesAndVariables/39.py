value = float(input("Enter price: "))
discount = float(input("Enter discout: "))

price = round(value*(1-discount/100),2)

print(f"Price with discout: {price}\nReduction: {round(value-price,2)}")