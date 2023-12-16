file_name = input("Enter file name: ")
file_name = "07-FileHandling/" + file_name
try:
    with open(file_name) as f:
        count = 0
        for _ in f:
            count += 1
        print(f"Number of lines: {count}")
except IOError:
    print("Nie ma takiego pliku!")
