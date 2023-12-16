with open("07-FileHandling/p24.txt") as f:
    for lines in f:
        name, surname, age, gender, email = lines.strip().split(",")
        if int(age) < 30:
            print(f"{name}\t{surname}\t{email}")