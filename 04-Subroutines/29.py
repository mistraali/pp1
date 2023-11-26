def f(amount_to_pay):
    sum = amount_to_pay//5
    amount_to_pay = amount_to_pay % 5
    sum += amount_to_pay//2 + amount_to_pay%2
    return sum

print(23,f(23))
print(8,f(8))
print(2,f(2))
print(0,f(0))