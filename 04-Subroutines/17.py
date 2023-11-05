#checks if 3 numbers are different
def check(a,b,c):
    return not(max(a==b, b==c, a==c))


num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
num3 = input("enter third number: ")

print(check(num1,num2,num3))