import json

with open("08-DictionariesStacksAndQueues/p21.csv") as source:
    data = []
    for x in source:
        data.append(x)

new_list = []
names = data[0].strip().split(",")
data.pop(0)

for i in data:
    new_record = dict(zip(names,i.split(',')))
    new_list.append(new_record)

with open("08-DictionariesStacksAndQueues/p21.json", "w") as output:
    output.write(json.dumps(new_list,indent=4))