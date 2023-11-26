def f(detector):
    count = 0
    for i in detector:
        if i == "+":
            count += 1
            if count == 3: break
        else:
            count -= 1
    return True if count == 3 else False

print(f("+-+++-+---"))
print(f("+-+-+-+-"))
print(f("+-++-+--"))
print(f("+-++-++-+---"))