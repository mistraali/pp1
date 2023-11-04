number = int(input("Enter number: "))

if(number > 10 or number < -10):
    comp = False
else:
    comp = True

print(f"Number is in the range <-10,10>: {comp}")