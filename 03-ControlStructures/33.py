dec = input("Enter decimal: ")
bin = ''

revBin = ''
foo = int(dec)
while foo > 0:
    revBin += str(foo % 2)
    foo //= 2
i = len(revBin) - 1
while i >= 0:
    bin += revBin[i]
    i -= 1

print(f"{dec}(10) = {bin}(2)")