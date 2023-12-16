def hotel_list(hotel_list):
    hotel_string = ""
    for item in hotel_list:
        hotel_string = hotel_string + item["name"] + ", "
    return hotel_string[:-2]

def avg_price(hotel_list):
    avg = 0
    for item in hotel_list:
        avg = item["price"]
    return avg/len(hotel_list)


hotels_in_Krakow = [
    {"name":"Sky","price":320.00},
    {"name":"Metropol","price":480.00},
    {"name":"New Port","price":420.00},
    {"name":"Aparthotel","price":390.00}
]
hotels_in_Sopot = [
    {"name":"Focus","price":510.00},
    {"name":"Aqua","price":345.00},
    {"name":"La Boutique","price":390.00},
    {"name":"Marina","price":410.00}
]

print(hotel_list(hotels_in_Krakow))
print(avg_price(hotels_in_Krakow))
print(hotel_list(hotels_in_Sopot))
print(avg_price(hotels_in_Sopot))
print("Krakow" if avg_price(hotels_in_Krakow) < avg_price(hotels_in_Sopot) else "Sopot")