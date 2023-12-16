import json

with open("08-DictionariesStacksAndQueues/p20.json") as source:
    data = json.load(source)

print("Date\t\tBuying Rate\tSelling Rate")
for x in range(52):
    print(end='=')
print("")
for i in data["rates"]:
    print(f"{i["effectiveDate"]}\t{i["bid"]}\t\t{i["ask"]}")