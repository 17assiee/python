#task 1.1
n=int(input("array length\n"))
x=[]
for i in range(n):
    print('enter the elenent ',i)
    x.append(int(input()))
max_number=max(x)
print('max number: ', max_number)
x.reverse()
print('revese array: ', x)

#task 1.2
n=[2,3,5,0,5,0]
x=sum(n)/len(n)
for i in range(len(n)):
    if n[i]==0: n[i]=x
print('new array list: ',n)

#task 2.1
n=int(input('array length\n'))
x=[]
for i in range(n):
    print('enter the number ', i)
    x.append(int(input()))
min_numb=min(x)
print('min number: ', min_numb)

#task 2.2
n=[2,4,5,-4,-5,-6]
a = []
b = []
for i in n:
    if i > 0:
        a.append(i)
    elif i < 0 :
        b.append(i)
print(a)
print(b)

#3.1
n=int(input('enter array length\n'))
D=[]
total = 0
for i in range(n):
    print('enter the number: ', i)
    D.append(int(input()))
for i in range(n):
    if i%2!=0: 
        total += D[i]
print('array: ', D)
print('sum of odd index numbers: ',total)

#3.2
n=8
a=[]
b=[]
for i in range(n):
    print('enter the number: ', i)
    a.append(int(input()))
for i in range(n):
    if a[i]<=7: a[i]*=2
    elif a[i]>15: a[i]=15
    b.append(a[i])
print(b)

#4.1
x=[3,4,6,7,5,4]
max_number=max(x)
print('max number is ' +str(max_number))
print('max number index: ', x.index(max_number))

#4.2
x=[3,4,6,7,5,4]
d=[]
for i in range(len(x)):
    if i%2!=0:
        d.append(x[i])
d.sort(reverse=True)
print(d)

#5.1
n=10
a=[]
for i in range(n):
    print('enter the number: ', i)
    a.append(int(input()))
a.sort()
print(a)

#5.2
n=10
a=[]
b=[]
for i in range(n):
    print('enter the number: ', i)
    a.append(int(input()))
for i in range(n):
    if a[i]==a[i-1]: continue
    else: b.append(a[i])
print(b)

#6.1
n=10
a=[]
more=0
less=0
for i in range(n):
    print('enter the number: ', i)
    a.append(int(input()))
max_number=max(a)
for i in  range(n):
    if i<=max_number: less+=1
    else: more+=1
print('less: ',less)
print('greater: ',more)

#6.2
n=[23,5,7,8,4,3,0,7,8,55]
m=5
summ=0
for i in range(len(n)):
    if n[i]>5: summ+=n[i]
print('sum: ',summ)

#7.1
n=int(input("array length\n"))
x=[]
a=0
b=0
for i in range(n):
    print('enter the elenent ',i)
    x.append(int(input()))
for i in range(n):
    if i%2!=0: a+=x[i]
    elif i%2==0: b+=x[i]
print('sum of even numbers: ', b)
print('sum of odd numbers: ',a)

#7.2
n=int(input("array length\n"))
x=[]
for i in range(n):
    print('enter the elenent ',i)
    x.append(int(input()))
max_numb=max(x)
min_numb=min(x)
for i in range(len(x)):
    if x[i]==max_numb: x[i]=min_numb
    elif x[i]==min_numb: x[i]=max_numb
print('new array: ',x)

#8.1
x=[2,4,5,8,9]
prod=1
summ=0
for i in x:
    prod*=i
    summ+=i
print('sum of elements: ', summ)
print('poduce of elements: ', prod)

#8.2
n=[2,3,5,0,5,0]
x=sum(n)/len(n)
for i in range(len(n)):
    if n[i]==0: n[i]=x
print('new array list: ',n)

#9.1
n=int(input("array length\n"))
x=[]
for i in range(n):
    print('enter the elenent ',i)
    x.append(int(input()))
print('min modulo number:', min(x, key = abs))
x.reverce()
print('newarray: ', x)

#9.2
A=[2,6,5,-6,-4,3,-9,-4,33,24]
B=[5,-27,2,-5,6,7,8,2,12,0]
print('original array A: ', A)
print('original array B: ', B)
A,B=B,A
print('new array A: ',A)
print('new array B: ',B)

#10.1
m = []
n = int(input("Number of elements: "))
for i in range(0,n):
    ele = int(input("Element: "))
    mm.append(ele)
newlist = [] 
replist = []
for i in mylist:
    if i not in newlist:
        newlist.append(i)
    else:
        replist.append(i)
print("List of duplicates", replist)
print("Unique Item List", newlist)

#10.2
n=[3,4,6,12,-78,20,66,54,32,12,15,9,-2,23,1]
m=[]
print('original array: ', n)
for i in range(len(n)):
    if n[i]<10: n[i]=0
    elif n[i]>20: n[i]=1
    m.append(n[i])
print('new array: ', m)

#11.1
n=int(input("array length\n"))
a=[]
for i in range(n):
    print('enter the elenent ',i)
    a.append(int(input()))
x=a[0]
for i in a:
    if i > x and i % 2 == 0:
        x=i
print('max number: ', x)

#11.2
n=int(input("array length\n"))
a=[]
b=[]
for i in range(n):
    print('enter the elenent ',i)
    a.append(int(input()))
for i in range(len(a)):
    if a[i]%2==0 and a[i]<10: b.append(a[i])
b.sort()
print('result: ',b)

#12.1
n=int(input("array length\n"))
a=[]
for i in range(n):
    print('enter the elenent ',i)
    a.append(int(input()))
x=a[0]
for i in a:
    if i < x and i % 2 != 0:
        x=i
print('smalles odd number: ', x)

#12.2
A=[2,6,5,-6,-4,3,-9,-4,33,24]
B=[5,-27,2,-5,6,7,8,2,12,0]
A,B=B,A
print('new array A: ',A)
print('new array B: ',B)

#13.1
n=int(input("array length\n"))
x=[]
for i in range(n):
    print('enter the elenent ',i)
    x.append(int(input()))
m=x[0]
for i in range(len(x)):
    if x[i]==m: print(x[i], i)

#13.2
n=8
x=[]
for i in range(n):
    print('enter the elenent ',i)
    x.append(int(input()))
for i in range(len(x)):
    if x[i]<15: x[i]*=2
print('new array: ', x)

#14.1
n=int(input("array length\n"))
x=[]
k=0
for i in range(n):
    print('enter the elenent ',i)
    x.append(int(input()))
x[-1], x[k]=x[k], x[-1]
print('new array: ', x)

#14.2
n=int(input("array length\n"))
x=[]
for i in range(n):
    print('enter the elenent ',i)
    x.append(int(input()))
m=sum(x)/len(x)
for i in range(len(x)):
    if x[i]>m: x[i]=1
print('new array: ',x)

#15.1
ggg = []
n = int(input("Number of elements: "))
for i in range(0,n):
    ele = int(input("Element: "))
    ggg.append(ele)
newlist = [] 
replist = []
for i in ggg:
    if i not in newlist:
        newlist.append(i)
    else:
        replist.append(i)
print("List of duplicates", replist)

#15.2
n=int(input("array length\n"))
a=[]
b=[]
for i in range(n):
    print('enter the elenent ',i)
    a.append(int(input()))
for i in range(len(a)):
    if a[i]%2!=0: b.append(a[i])
b.sort(reverse=True)
print('new array: ', b)
