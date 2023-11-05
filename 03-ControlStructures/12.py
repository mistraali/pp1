firstName = input("Enter first person name: ")
firstAge = int(input("Enter first person age: "))
secondName = input("Enter second person name: ")
secondAge = int(input("Enter second person age: "))

if firstAge >= 18 and secondAge >= 18:
    print(f"Both {firstName} and {secondName} are adults")
else:
    print(f"At least one person is not an adult")
