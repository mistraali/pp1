"""
The computer checks whether the bottle has been filled correctly. For a 500ml bottle, the allowable tolerance is 2%.
Write a program that calculates the percentage of incorrectly filled bottles. 
Use the filter() along with a higher order function. 
"""

batch = [508,500,512,499,492,511,503,476,501,509]

def vol500(tolerance):
    def check(volume):
        if volume <= 500:
            return True if volume >= 500*(1-tolerance) else False
        else:
            return True if volume < 500*(1+tolerance) else False
    return check 

print(round((1 - len(list(filter(vol500(0.02), batch)))/len(batch))*100, 2), "%")