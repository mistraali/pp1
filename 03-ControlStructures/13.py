firstNumber = int(input('Enter first number: '))
secondNumber = int(input('Enter second number: '))

if firstNumber >= 0 or secondNumber >= 0:
    print(f"At least one of numbers {firstNumber} and {secondNumber} is not negative")
else:
    print(f"Both {firstNumber} and {secondNumber} are negative")