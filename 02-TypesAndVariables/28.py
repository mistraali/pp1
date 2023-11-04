height = int(input("Enter your height in cm: "))
weight = int(input("Enter your weight in kg: "))

bmi = weight / ((height/100)**2)
print(f"Your BMI: {bmi}")

if(bmi > 24.99 or bmi < 18.5):
    comp = False
else:
    comp = True

print(f"Correct weight: {comp}")
