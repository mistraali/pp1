import json

with open("08-DictionariesStacksAndQueues/p19.json","r",encoding="utf8") as source:
    content = json.load(source)

with open("08-DictionariesStacksAndQueues/p19_1.json", "w") as output:
    new_list = []
    for i in content:
        new_record = {"first_name" : i["first_name"], "last_name" : i["last_name"], "student_id" : i["index"]}
        new_list.append(new_record)   
    output.write(json.dumps(new_list, indent=4))
