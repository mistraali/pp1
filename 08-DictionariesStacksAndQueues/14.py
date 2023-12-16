winter_semester = {
    "math":60,
    "programming":30,
    "history":15
}

sum = 0
for x in winter_semester.values():
    sum += int(x)

print("Total number of hours: ", sum)