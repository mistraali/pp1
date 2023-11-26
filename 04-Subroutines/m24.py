def check_range(min, max, num):
    if num >= min and num <=max:
        return True
    else:
        return False
    
if __name__ == "__main__":
    print(check_range(1,10,2))
    print(check_range(5,10,2))
    print(check_range(1,10,12))
