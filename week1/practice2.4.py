import math
a=int(input('a= '))
b=int(input('b= '))
c=math.sqrt(a**2 + b**2)
print(c)
p=a + b +c
print(p)

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
    

