#1
class Second:
    color = "red"
    form = "circle"
    def changecolor(self,newcolor):
        self.color = newcolor
    def changeform(self,newform):
        self.form = newform
obj1 = Second()
obj2 = Second()
print (obj1.color, obj1.form) 
print (obj2.color, obj2.form) 
obj1.changecolor("green") 
obj2.changecolor("blue") 
obj2.changeform("oval") 
print (obj1.color, obj1.form) 
print (obj2.color, obj2.form) 

class Rectangle():
   def __init__(self, color='green', width=100, height=100):
       self.color = color
       self.width = width
       self.height = height

   def square(self):
       return self.width * self.height

   def plus(self):
       return self.width+self.height


rect1 = Rectangle()
print(rect1.color)
print(rect1.square())

rect2 = Rectangle('yellow', 23, 34)
print(rect2.color)
print(rect2.square())

rect3 = Rectangle("blue", 44, 55)
print(rect3.color)
print(rect3.square())

rect4 = Rectangle("orange", 67, 78)
print(rect4.color)
print(rect4.plus())

#2
class Name:
    def __init__(self,fname,sname):
        self.fname = fname
        self.sname = sname
    def fullname(self):
        return self.fname, self.sname
    def initials(self):
        return self.fname[0], self.sname[0]
a1=Name('john','SMITH')
print(a1.fname)
print(a1.sname)
print(a1.fullname())
print(a1.initials())


#3
import math
class Calculator:
    def __init__(self, first=88, second=99):
        self.first=first
        self.second=second

    def add(self):
        return self.first+self.second

    def subtract(self):
        return abs(self.first-self.second)

    def multiply(self):
        return self.first*self.second

    def division(self):
        return self.first/self.second

calculator = Calculator(10,5)
print(calculator.add())
print(calculator.subtract())
print(calculator.multiply())
print(calculator.division())



