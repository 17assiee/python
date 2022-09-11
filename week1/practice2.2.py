import math
y= int(input())
x= int(input())
g= math.sqrt (math.cos(2*y) + math.sin(4*y) + math.sqrt(math.exp(x) + math.exp(-x)))
f= ((math.exp(-x) + math.exp(x))**3) * ((math.sin(4*y) + math.cos(2*y) - 2)**2)
h=g*f
print(h)
