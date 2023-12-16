import json

with open("08-DictionariesStacksAndQueues/p10.json") as file:
    data = json.load(file)

for x in data:
    for key,value in x.items():
        print(f"{key} : {value}")