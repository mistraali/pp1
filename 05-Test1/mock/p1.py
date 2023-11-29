def f(amount_to_pay):
    sum = amount_to_pay//5
    amount_to_pay %= 5
    sum += amount_to_pay//2 + amount_to_pay%2
    return sum
