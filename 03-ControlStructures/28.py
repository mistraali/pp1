number = input("Enter EAN-13: ")

if len(number) == 13:
    print("Article number is correct!")
    if number[0:4] == "590":
        print("From Poland")
    else:
        print("Not from Poland")
else:
    print("Article number is not correct!")