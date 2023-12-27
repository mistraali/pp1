import re

def f(player1, player2):
    return True if read_hand(player1) >= read_hand(player2) else False


def read_hand(hand):
    sum = 0
    lows = re.findall(r"[2-9]",hand)
    for i in lows:
        sum += int(i)
    highs = re.findall(r"[TJQKA]", hand)
    for _ in highs:
        sum += 10
    print(sum)
    return sum

if __name__ == "__main__":
    print(f("AJ972","AQT72"))
    print(f("9532","K8"))