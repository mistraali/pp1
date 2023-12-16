with open("07-FileHandling/p17.txt") as f:
    flag_continue = True
    while flag_continue:
        for _ in range(5):
            print(f.readline(), end="")
        if input() != "":
            flag_continue = False