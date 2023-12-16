with open("07-FileHandling/p20.txt","w") as final_file:
    with open("07-FileHandling/p8.txt") as file_1:
        content = file_1.read()
        final_file.write(content)
    final_file.write("\n")
    with open("07-FileHandling/p10.txt") as file_2:
        content = file_2.read()
        final_file.write(content)