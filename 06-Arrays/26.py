arr = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]

print(arr)
longest = ''
for i in arr:
    if len(longest) < len(i): longest = i[:]
print(longest)