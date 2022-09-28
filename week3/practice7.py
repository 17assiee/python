#1.1
def s(a,b,h):
    s=(h*(a+b))/2
    return s
A=[]
for i in range(1):
    a=int(input('a: '))
    b=int(input('b: '))
    h=int(input('h: '))
    A.append(s(a,b,h))
print(A[i])

#1.2
def sum1(a):
  if len(a) == 1:
        return a[0]
  else:
        return a[0] + sum1(a[1:])
def af(a):
    return sum(a)/len(a)
for i in range(3):
    n=int(input('enter thr number of elements: '))
    for i in range(n):
        print('enter the number ', n, ' of array')


#2.1
import math
def s(a):
    s=(3*(math.sqrt(3))*(math.pow(a,2)))/2
    return s
A=[]
for i in range(1):
    a=int(input('a: '))
    A.append=int(input(s(a)))
print('the area is ',A[i])

#2.2
def s(a,b):
    s=a*b
    return s
A=[]
for i in range(3):
    print('enter the data of ', i, 'rectangle')
    a=int(input('a: '))
    b=int(input('b: '))
    A.append(s(a,b))
for i in range(3):
    print('the area of ', i, ' rectangle is ', A[i])

#3.1
import math
def triangl_1(leg1, leg2):
   gip = math.sqrt(leg1 ** 2 + leg2 ** 2)
   return gip

def triangl_2(leg1, leg2):
    gip = math.sqrt(leg1 ** 2 + leg2 ** 2)
    return gip

if triangl_1(34, 25) < triangl_2(6, 56):
   print("first is bigger: ", triangl_1(34,25),' second is less: ', triangl_2(6, 56)) 
else:
   print("second is bigger: ",triangl_2(6, 56), 'first is less: ',triangl_1(34,25))

#3.2
def sortS(a):
    return ''.join(sorted(a))
     
a=input()
print(sortS(a))

#4.1
from fractions import Fraction
a,b = 5,9
c,d = 6,7
ddd= Fraction(Fraction(a,b), Fraction(c,d))

print("The irreducible fraction: ", ddd)
def gcd(a, b):  
    if a > b:
        s = b  
    else:
        s = a  

    for i in range(1, s + 1):  
        if((a%i==0)and(b%i==0)):  
            gcd = i  
    print(gcd)
gcd(ddd.numerator, ddd.denominator)

#4.2
a = 11;
b = 11;
p,pp = 6,8
f,ff = 2,2
n,nn = 6,9
radius = 5
def point_in(pa, pb, radius, a, b):
    if ((a-pa)**2+(b-pb)**2)<=radius**2:
        print("Point is inside if the circle!")
    else:
        print("Point is outside of the circle!")
point_in(p,pp,radius,a,b)
point_in(f,ff,radius,a,b)
point_in(n,nn,radius,a,b)

#5.1
from fractions import Fraction
a,b = 6,7
c,d = 1,2
ddd = Fraction(Fraction(a,b) - Fraction(c,d))
print("The irreducible fraction: ", ddd)
def gcd(a, b):  
    if a > b: s = b  
    else: s = a  
    for i in range(1, s + 1):  
        if((a%i==0)and(b%i==0)):  
            gcd = i  
    print(gcd)
gcd(ddd.numerator, ddd.denominator)
#5.2
def div(a):
    for i in range(1, a+1):
        if a%i==0:
            print(i, end=" ")
        else: continue
n = int(input("Input the number: "))
div(n)

#6.1
 def gcd(x, y):  
    if x > y: s = y  
    else: s = x  
    for i in range(1, s + 1):  
        if((x%i==0)and(y%i==0)):  
            gcd = i  
    return gcd
def lcm(x, y):
    lcm = (x*y)/gcd(x,y)
    print(lcm)
x = int(input("Input the 1st number: "))
y = int(input("Input the 2nd number: "))
print(gcd(x,y))
lcm(x,y)

#6.2
x = float(input("First: "))
y = float(input("Second: "))
z = float(input("Third: "))
s = float(input("Fourth: "))
dia = float(input("Diagonal: "))

def quadl(x,y,z,s,dia):
    def heron_f(x,y,z): p=0.5*(x+y+z)
        return (p*(p-x)*(p-y)*(p-z))**0.5
    return heron_f(z,y,dia) + heron_f(c,z,s,dia)

print("The area of a quadliteral is: ", quadl(x,y,z,s,dia))
   

#7.2
def octal(a):
    print("The octal code: ", oct(a))
a = int(input("Input the number to convert: "))
octal(a)

#8.1
def di(n):
    ans = []
    for i in range(1,n+1):
        s = str(i)
        temp = True
        for j in s:
            if int(j) == 0:
                temp = False
            elif i % int(j) != 0:
                temp = False
        if temp:
            ans.append(i)
    return ans

n = int(input("n: "))
print(di(n))
#8.2
def swap(a):
    a[0],a[len(a)-1] = a[len(a)-1],a[0]
    return a

j = int(input("length of array: "))
A = []
for i in range(j):
    n = int(input("element of array: "))
    A.append(n)

print(A)
print(swap(A))

#9.1
def sum(n):
    s = str(n)
    sum = 0
    for i in s:
        sum += int(i)
    return sum

n = int(input("N: "))
subb = sum(n)
a = 0
while n > 0:
    a += 1
    n -= subb

print(a)

#9.2
def o(n):
    on = [0] * 100
    i = 0
    while (n != 0):
        on[i] = n % 8
        n = int(n / 8)
        i += 1
    for j in range(i - 1, -1, -1):
        print(on[j], end="")
n = int(input('Enter the int: '))
o(n)
#10.1
def digitsofn(n):
    anss = []
    s = str(n)

    for i in s:
        anss.append(int(i))
    return anss

N = int(input("N: "))
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

anss = []
for i in range(100,N):
    dgts = digitsofn(i)
    if x in dgts:
        dgts.remove(x)
    if y in dgts:
        dgts.remove(y)
    if z in dgts:
        dgts.remove(z)
    if len(dgts) == 0:
        anss.append(i)
print(anss)

#10.2
def reverceseq(x):
    x = x.split()[::-1]
    anss = []
    for i in x:
        anss.append(i)
    return ' '.join(anss)

x = input("Enter str to reverse: ")
print(reverceseq(x))

#11.1
def twins(n):
    print([[i, i+2] for i in range(n, 2*n - 1)])
    
twins(int(input())) 

#11.2
import random
a = int(input())
b= int(input())
c = [[random.randrange(10) for i in range(a)] for j in range(b)] 
for i, row in enumerate(c):
    max = min = 0
    for j, elem in enumerate(row):
        if elem > row[max]:
            max = j
        if elem < row[min]:
            min = j
    row[max], row[0] = row[0], row[max]
    row[min], row[-1] = row[-1], row[min]
print(c)
#12.1
def getsum(value):
    res = 1

    for i in range(2, int(value**0.5) + 1):
        if value % i == 0:
            res += i + value // i
    return res
for i in range(10, 10000):
    sum1 = getsum(i)
    sum2 = getsum(sum1)
    if sum2 == i and sum1 != sum2:
        print(i, sum1)

#12.2
def m(a, b, c):
    return 1/2(sqrt(2*b**2+2*c**2-a**2))
#13.1
num=int(input("enter number: "))
for n in range(num, 1000):
    s1=0
    numcp=n
    if(n>=10 and n<100):
        while(n>0):
            digit=int(n%10)
            d2=digit*digit
            s1=s1+d2
            n=int(n/10)

    if(n>=100 and n<1000):
        while(n>0):
            digit=int(n%10)
            d2=digit*digit*digit
            s1=s1+d2
            n=int(n/10)
    if(numcp==s1):
        print("angstrong number: ", s1)

#13.2
def cosa(x, y) :
    return x  / ((x * x + y * y) ** 0.5)
x1, x2 = map(float,input("enter the coordinaties x1.x2" ).split())
y1, y2 = map(float,input("enter the coordinaties y1, y2").split())
z1, z2 = map(float,input("enter the coordinaties z1, z2" ).split())
res = [x1, x2]
cosax = cosa(x1, x2)
cosay = cosa(y1, y2)
if cosay > cosax :
    cosax = cosay
    res = [y1, y2]
cosaz = cosa(z1, z2)
if cosaz > cosax :
    cosaz = cosaz
    res = [z1, z2]
print(*res)
n = 3
res = [tuple(map (float,input().split())) for i in range(n)]
rcos = [cosa(*res[i]) for i in range(n)]
k = rcos.index(max(rcos))
print(res[k])

#14.1
import math
def countdividers(n):
    if n <= 0: return 0 
    if n == 1: return 1

    k = 2 
    for i in range(2, round(math.sqrt(n)) + 1): 
        if n % i == 0:
            k += 1 if i == n // i else 2
    return k
def maxdividerscount(m , n):
    if m > n : m, n = n, m 
    maxDivs = 0 
    numberWithMaxDivs = [] 
    for i in range(m, n): 
        d = countdividers(i)
        if d > maxDivs: 
            maxDivs = d
            numberWithMaxDivs = [] 
        if d == maxDivs:
            numberWithMaxDivs.append(i) 
    return maxDivs, numberWithMaxDivs
print(maxdividerscount(20,80))

#14.2
import math
def distance(a, b):
    d = 0
    for i in range(3):
        d += pow((a[i]-b[i]),2)
    return d
coordinates=['x','y','z','t']
arr=[]
print("enter the coordinates of the points:")
for i in range(4):
    b=[]
    print("the coordinates of the points:",coordinates[i])
    for j in range(3):
        b.append(int(input()))
    arr.append(b)
flag = True
for i in range(3):
    for j in range(i+1, 4):
        dist = distance(arr[i],arr[j])
        if flag or max_dist < dist:
            m1=i
            m2=j
            max_dist = dist 
            flag = False
print(f'Maximum distance between points {coordinates[m1]} и {coordinates[m2]}')
print(f' distance = {max_dist**0.5:.3f}')

#15.1
def palindrome(n: int) -> bool:
	rev = 0
	i = n
	while i > 0:
		rev = rev * 10 + i % 10
		i //= 10
	return (n == rev)
def count(minn: int, maxx: int) -> None:
	for i in range(minn, maxx + 1):
		if palindrome(i):
			print(i, end = " ")
if __name__ == "__main__":
	count(100, 4000)

#15.2
import math
def distance(a, b):
    d = 0
    for i in range(3):
        d += pow((a[i]-b[i]),2)
    return d
 
coordinates=['x','y','z','t']
arr=[]
print("enter the coordinates of the points:")
for i in range(4):
    b=[]
    print("the coordinates of the points:",coordinates[i])
    for j in range(3):
        b.append(int(input()))
    arr.append(b)
 
flag = True
for i in range(3):
    for j in range(i+1, 4):
        dist = distance(arr[i],arr[j])
        if flag or min_dist > dist:
            m1=i
            m2=j
            min_dist = dist 
            flag = False
 
print(f'Minimum distance between points {coordinates[m1]} и {coordinates[m2]}')
print(f' distance = {min_dist**0.5:.3f}')


