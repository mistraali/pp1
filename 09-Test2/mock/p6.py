import json


def f(years,course):
    with open("09-Test2/mock/data.json") as f:
        content = json.load(f)

    sum = 0
    for i in content:
        if age_check(years,i) and grade_check(course, i): sum += 1
    return sum
    

def age_check(n, p):
    if p["age"] == n:
        return True
    else:
        return False
    
def grade_check(name, p):
    sum = 0
    foo = p["studies"]["courses"]["name"]
    for i in foo:
        if foo["name"] == name:
            for j in foo["grades"]:
                sum += int(j)
                print (j)
    return True if sum/len(p["studies"]["courses"][name]) >=4 else False

if __name__ == "__main__":
    print(f(21,"statistics"))