timeLong = input("Enter time (24h format): ").strip()

if len(timeLong) == 5:
    hour = int(timeLong[0:2])
    minute = timeLong[3:5]
else:
    hour = int(timeLong[0])
    minute = timeLong[2:4]

if hour >= 12 and hour < 24:
    ap = "pm"
else:
    ap = "am"
    if hour == 24:
        hour = 0

print(f"Time in 12h format: {hour}:{minute} {ap}")


