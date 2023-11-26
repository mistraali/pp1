def month_name(n):
    if n == 1:
        return "Jan"
    elif n == 2:
        return "Feb"
    elif n == 3:
        return "Mar"
    elif n == 4:
        return "Apr"
    elif n == 5:
        return "May"
    elif n == 6:
        return "Jun"
    elif n == 7:
        return "Jul"
    elif n == 8:
        return "Aug"
    elif n == 9:
        return "Sep"
    elif n == 10:
        return "Oct"
    elif n == 11:
        return "Nov"
    else:
        return "Dec"
    
if __name__ == "__main__":
    for i in range(1,13):
        print(month_name(i))