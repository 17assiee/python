#1.1
n=input('Your last name, first name? ')
m=int(input("How old are you? "))
d=int(input("Your phone number? "))
print('Your first name, last name: ',n)
print('Your age: ', m)
print('Your phone number: ',d)

#1.2
n=int(input('Please choose the srea of which shape you want find: trapezoid, parallellogram, triangle(1,2,3): '))
if n==1:
    a=int(input('a: '))
    b=int(input('b: '))
    h=int(input('h: '))
    s=((a+b)*h)/2
    print('Area of trapezoid: ', s)
elif n==2:
    a=int(input('a: '))
    h=int(input('b: '))
    s=a*h
    print('Area of parallellogram: ', s)
elif n==3:
    b=int(input('b: '))
    h=int(input('h: '))
    s=(b*h)/2
    print('Area of triangle: ', s)

#1.4
a=3
y=a**2/3 + (a**2+4)/6 + ((a**2+4)**0.5)/4 + (((a**2+4)**3)**0.5)/4
print(y)

#1.5
n=int(input('Guess a number, multiply by 5, add 8 and multiply by 2: '))
m=((n/2)-8)/5
print(f'You have made a number... {m}?')

#2.1-2.2
def math():
  while True:
    num1 = int(input('First number: '))
    operation=input('Operation: ')
    num2 = int(input('Second number: '))
    
 
    if operation == '+':
      print(num1, '+', num2, '=', num1 + num2)
    elif operation == '-':
      print(num1, '-', num2, '=', num1 - num2)
    elif operation == '*':
      print(num1, '*', num2, '=', num1 * num2)
    elif operation == '/':
      if num2!=0:
          print(num1, '/', num2, '=', num1 / num2)
      else:
          print("Division by zero")
    else:
      print('Error. The operation does not exist')
      
    if num1>10 and num1!=12 and num1>=15:
        return True
    elif num1==18:
        return True
    math()
  
math()

#2.3
def numb(n):
    if n>10 and n!=12 and n>=15 and n==18:
        return True
    else:
        return False
print(numb(14))

#2.4
i = 34
while i < 67:
    if i % 2 != 1:
        print(i)
        i += 2 

#2.5
while True:
     number = int(input("Enter a positive number: "))
     print(number)
     if not number > 0:
         break

#2.6
i = 0
while (i<100):
    i += 1
    if i==50: continue
    if i==99: continue
    print(i)

    
        



    
    
            
