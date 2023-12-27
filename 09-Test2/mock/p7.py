import re


def f(arr):
    sum = 0
    for password in arr:
        if check(password): sum +=1

    return sum

def check(password):
    if len(password) < 4: return False
    if len(re.findall(r"[a-z_0-9]",password)) == len(password): 
        return True
    else: 
        return False

if __name__ == "__main__":
    print(f(["uek","water_7_x","anna.may","a_b_c_d_e_f"]))