firstNumber = int(input('Enter first number: '))
secondNumber = int(input('Enter second number: '))

if firstNumber <= secondNumber:
    print(f"Numbers in ascending order: {firstNumber}, {secondNumber}")
else:
    print(f"Numbers in ascending order: {secondNumber}, {firstNumber}")