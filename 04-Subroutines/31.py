def f(min,max):
    if min == -1 or min > 0: return 0
    if min%2: min+=1
    count = 0
    while min < max and min < 0:
        count+=1
        min+=2
    return count

print(-7,8,f(-7,8))
print(-1,11,f(-1,11))