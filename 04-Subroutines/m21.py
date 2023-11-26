import random

def generate_number():
    return random.randint(1,10)

if __name__ == "__main__":
    for i in range (0,10):
        print(generate_number())
