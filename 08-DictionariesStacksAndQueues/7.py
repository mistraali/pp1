person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming","excursions"],
    "married": True,
    "phone":{"landline":"123444321","mobile":"777888999"}
}

print("a)\t", person)
print("b)\t", person["name"])
print("c)\t", person["hobby"])
person["surname"] = "Nowak"
print("d)\t", person["surname"])
person["married"] = False
print("e)\t", person["married"])
person["gender"] = "male"
print("f)\t", person["gender"])
person["hobby"].append("bicycle")
print("g)\t", person["hobby"])
person["phone"].update({"workphone":"3131313444"})
print("h)\t", person["phone"])