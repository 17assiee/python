#1.1
import math
a= int(input())
b= int(input())
h= int(input())
g= (a**2 + b)*h
f= 2*(a-b) + 4
s=g/f
print(s)

#1.2

import math
y= int(input())
x= int(input())
g= math.sqrt (math.cos(2*y) + math.sin(4*y) + math.sqrt(math.exp(x) + math.exp(-x)))
f= ((math.exp(-x) + math.exp(x))**3) * ((math.sin(4*y) + math.cos(2*y) - 2)**2)
h=g*f
print(h)

#1.3
import math
x=2
y=1
z=math.pow(math.pow(x, y), x) + math.pow(math.pow(x, x), y) - math.pow(x,4)
print(z)

x=1
y=4
z=3
d=math.pow((math.fabs(1/math.tan(y) + 6)), 1/3) + math.sqrt(math.pow(x+1, 3))/(4*y-2*z)
print(d)

x=3
y=0.2
z=(5*x*y)/(math.pow(x, 3) - 4) + math.exp(math.pow(x, 2)) + math.sqrt((math.pow(math.cos(y), 2) - math.pow(y, 2)))
print(z)

x=3
y=5
z=math.sqrt(math.fabs(y)) + ((math.pow((math.atan(math.log(x))),3)) / (math.pow(x,y)-y+1))
print(z)

x=3
y=1
z=2
d=math.pow(4, x*y) + math.pow(x, y*z) + math.pow(x*y, z)
print(d)

x=2
y=2
z=1
d=(4*math.fabs(x) - x*y*math.pow(z,2)) / (x + math.exp(y*x) - 2*y*z)
print(d)

x=0.8
y=0.1
z=4
d=math.pow((((1-x+math.atan(x-7*y)))) / (4*x*z - math.pow(math.log(y), 2)), 1/5)
print(d)

x=3
y=1
z=3
d= (2*3*4) / (math.pow(math.sin(x), 3) + math.pow(math.tan(y),3)) - math.sqrt(math.pow(z, x-y))
print(d)

x=4
d= (math.log(math.pow(x-3, 4)) + math.pow(2,x)*(math.pow(math.sin(3*x),2))) / 4*x - 5.2
print(d)

x=2
y=2
z=1
d=math.sqrt(0.6*x*y*z) + math.pow(math.pow(y,x), 2) - math.exp(math.sin(2*math.pow(x,2)))
print(d)

x=0.5
y=2
d=(math.asin(math.pow(x,3) - 6)) / (8*(math.cos(4*y) - math.sin(4*x)))
print(d)

x=2
y=1
z=3
d=((math.fabs(math.log(math.pow(x,3))) + math.exp(2*x)) / x+3.4) - (math.pow(1/(math.tan(3/x*y*z))), 3)
print(d)

#2.1
import math
a=int(input('a= '))
b=int(input('b= '))
c=math.sqrt(a**2 + b**2)
print(c)
p=a + b +c
print(p)

#2.2
print("Equation: a*x**2 + b*x + c")
a=int(input('a= '))
b=int(input('b= '))
c=int(input('c= '))
d=b**2 - 4*a*c
d1=d**0.5
if(d<0):
    print("no roots")
else:
    x1=(-b+d1) / (2*a)
    x2=(-b-d1) / (2*a)
    print("root 1:",round(x1,2))
    print("root 2:",round(x1,2))

#2.3
 x=int(input("Choose want to find areo of rectangle, triangle or circle(1,2,3):"))
if(x==1):
    a=int(input("a= "))
    b=int(input("b= "))
    s=a*b
    print("The area of the rectangle: ",s)
elif(x==2):
    a=int(input("a= "))
    b=int(input("b= "))
    c=int(input("c= "))
    p=(a+b+c)/2
    s=math.sqrt(p*(p-a)*(p-b)*(p-c))
    print("The are of the triangle: ", round(s,2))
elif(x==3):
    r=int(input("r= "))
    s=math.pi*math.pow(r,2)
    print("The area is the circle: ", round(s,2))
    

