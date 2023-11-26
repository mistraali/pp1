def f(rolls):
    max_dice = 0
    max_rolls = 0
    for i in range(1,7):
        max = 0
        for r in rolls:
            if int(r) == i:
                max += 1
        if max > max_rolls:
            max_rolls = max
            max_dice = i
    return max_dice

print(f("5233165554211"))
print(f("2133"))
