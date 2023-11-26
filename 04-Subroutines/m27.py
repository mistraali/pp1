def mask_number(number):
    number = str(number)
    return number[0:2]+'**********'+number[12:16]

if __name__ == "__main__":
    print(mask_number(1234567890123456))