countries = [
    {"name" : "Poland", "population" : "12345"},
    {"name" : "Finland", "population" : "6789"},
    {"name" : "England", "population" : "25869"},
    {"name" : "Smaland", "population" : "124"},
    {"name" : "Thailand", "population" : "4568"}
]
i = 0
while i < len(countries):
    print(countries[i].get("name"),"\t" if len(countries[i].get("name")) > 6 else "\t\t",countries[i].get("population"))
    i += 1