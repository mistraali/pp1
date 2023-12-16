import json

movie = {
    "title" : "ABC",
    "year" : 2000,
    "actor" : ["A.A.Aaa", "B.B", "Cccc C. Ccc"],
    "oscar" : False
}

with open("08-DictionariesStacksAndQueues/p11.json", "w") as f:
    f.write(json.dumps(movie))

