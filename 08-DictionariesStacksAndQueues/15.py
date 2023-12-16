basic_data = {
    "name":"Barbara",
    "age":21
}

advanced_data = {
    "status":"student",
    "married":False,
    "interest":["reading","swimming"]
}

full_data = basic_data.copy()

for k,v in advanced_data.items():
    full_data.update({k:v})

print(full_data)