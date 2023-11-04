number = input("Enter binary number: ")
print(f"Binary number in decimal notation: ")

decNumber = 0
i = 0
while i<len(number):
    decNumber += int(number[i])*2**(len(number)-i-1)
    i+=1
print(decNumber)