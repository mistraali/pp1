def f(subjects):
    max = 0
    name = ""
    for k,v in subjects.items():
        sum = 0
        for j in v:
            sum += j
        if max < (sum/len(v)):
            max = sum/len(v)
            name = k
    return name



if __name__ == "__main__":
    print(f({"math":[3,4,4],"geo":[5,4,4,4],"comp":[5,4]}))