f = open("07-FileHandling/p12.txt", "wt")

name = "BK"
university = "UEK"
field = "IS"

f.write(f"{name}\n{university}\n{field}")
f.close()