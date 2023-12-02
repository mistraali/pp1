def reverse(tuple):
    new_tuple = tuple[::-1]
    return new_tuple

my_tuple = (10,20,30,40,50)

#new object
print(reverse(my_tuple))

#same object
print(tuple(reversed(my_tuple)))