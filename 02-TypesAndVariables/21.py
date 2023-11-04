height = int(input("Enter height: "))

feetToCm = 30.48
inchToCm = 2.54

feet = int(height/feetToCm)
inch = round((height - feet*feetToCm)/inchToCm)
print(f"I am {height}cm tall, i.e. {feet} feet and {inch} inches")