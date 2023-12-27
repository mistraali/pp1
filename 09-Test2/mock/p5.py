import re

def f(first_letter,last_letter):
    with open("09-Test2/mock/data.txt", encoding="UTF-8") as f:
        content = f.read()

    results = re.findall(rf"\b{first_letter}[\w]+",content)
    final_results = []
    for x in results:
        if re.findall(rf"{last_letter}\b",x): final_results.append(x)
    
    return final_results

if __name__ == "__main__":
    print(f("w","d"))