plate = input("Enter vehicle reg number: ")

if(plate[0].lower()!='k'):
    comp = False
elif (plate[1].lower() == 'k' or plate[1].lower() == 'r'):
    comp = True
else:
    comp = False

print(f"Car from Kraków: {comp}")