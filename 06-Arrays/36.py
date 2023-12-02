def occurs(my_tuple,number):
    count = 0
    for i in my_tuple: 
        if i == number: count += 1
    return count


my_tuple = (50,20,40,50,30,50)
print(f"50 occurs {occurs(my_tuple,50)} times")