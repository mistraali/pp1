def check_letter(s, l):
    sum = 0
    for i in s:
        if i == l:
            sum += 1
    return sum

if __name__ == "__main__":
    print(f"(Abecadloabecadlo, a): {check_letter("Abecadloabecadlo","a")}")