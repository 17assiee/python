#1
x=int(input('Price per kg of sugar: '))
n=10
s=0
for i in range(n):
    s+=x
    print(s)

#2
s=0
n=int(input('numbers: '))
c=0
while n!=0:
    s+=n
    n=int(input())
    c+=1
print(f'Sum of numbers {s}')
print(f'The number of all numbers {c}')

