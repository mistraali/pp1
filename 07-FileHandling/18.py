with open("07-FileHandling/p17.txt") as source:
    content = source.read()
    with open ("07-FileHandling/p18.txt", "wt") as copy:
            copy.write(content)