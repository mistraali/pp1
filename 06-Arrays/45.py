import matplotlib.pyplot as plt
import math

x = []
y = []

for n in range(0, 360):
    x = x + [n]

for n in x:
    y = y + [math.sin((n/180)*math.pi)]

plt.plot(x,y)
plt.show()