def f(a,b,op):
    return a+b if op=='+' else a-b if op=='-' else a*b if op=='*' else a%b if op=='%' else a**b if op=='**' else False

print(f(2,3,"+"))
print(f(2,3,"%"))
print(f(2,3,"**"))
print(f(2,3,"*"))
print(f(2,3,"-"))