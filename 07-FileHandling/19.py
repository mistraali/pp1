with open("07-FileHandling/p17.txt") as source:
    with open ("07-FileHandling/p19.txt", "wt") as copy:
        for line in source:
            copy.write(line)