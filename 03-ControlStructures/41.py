pin = '0805'
security = 0

while True:
    attempt = input("Enter the PIN code: ")
    if attempt == pin:
        print("Correct! Go ahead!")
        break
    else:
        security += 1
        print("Incorrect...")
        if security >= 3:
            print("Sorry, your entrance has been blocked.")