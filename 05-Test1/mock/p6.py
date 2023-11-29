def f(number,even):
    sum = 0
    cipher = lambda a : a%10
    while number > 0:
        if not(even) == cipher(number)%2:
            sum += cipher(number)
        number//=10 
    return sum

if __name__ == "__main__":
    print(3124,f(3124,True))
    print(3124,f(3124,False))
    print(20576,f(20576,True))
    print(20576,f(20576,False))