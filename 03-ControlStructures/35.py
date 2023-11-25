i = 1
while i <= 30:
        print(f"{"BINGO" if not(i % 3 or i % 5) else "FIVE" if not(i % 5) else "THREE" if not(i % 3) else {i}}")
        i += 1