#1.1
N = int(input("Enter N: "))
array=[[int(input()) for i in range(N)] for k in range(N)]
sum = 0
count = 0
for i in range(N):
    for k in range(N):
        if k>=i:
            sum+= array[i][k]
            count+=1
print("Sum: ", sum)
print("Count: ", count)

#1.2
N = int(input("Enter N: "))
M = int(input("Enter M: "))
array=[[int(input()) for i in range(N)] for k in range(M)]
min = float('inf')
max = float('-inf')
tempimin=0
tempkmin=0
tempimax=0
tempkmax=0
for i in range(0,N):
    for k in range(0,N):
        if min>array[i][k]:
            min = array[i][k]
            tempimin = i
            tempkmin = i
        if max<array[i][k]:
            max = array[i][k]
            tempimax =i
            tempimin =i
temp = array[0][0]
array[0][0] = min
array[tempimin][tempkmin] = temp
temp = array[N-1][M-1]
array[N-1][M-1] = max
array[tempimax][tempkmax] = temp
print(array)

#2.1
N = int(input("Enter N: "))
array=[[int(input()) for i in range(N)] for k in range(N)]
arr=[]
arr2 = []
temp = False
for i in range(N):
    arr.append(0)
    arr2.append(0)
for i in range(0,N):
    for k in range(0,N):
        arr[i]+=array[i][k]
for i in range(0,N):
    for k in range(0,N):
        arr2[i]+=array[i][i]
for i in range(0,N):
    for k in range(0,N):
        if arr[i]!=arr[k] or arr2[i]!=arr2[k] or arr[i] !=arr2[k]:
            print("Not magic")
            temp = True
            break
if temp==False:
    print("This is magic")

#2.2
N = int(input("Enter N: "))
array=[[int(input()) for i in range(N)] for k in range(N)]
temp = 0
for i in range(0,N):
    temp = array[0][i]
    array[0][i] = array[N-1][i]
    array[N-1][i] = temp
    for i in range(0,N):
    for k in range(0,N):
        print(array[i][k] , end=" ")
    print("")

#3.1
N = int(input("Enter N: "))
array=[[int(input()) for i in range(N)] for k in range(N)]
def transpose(mat, tr, N):
    for i in range(N):
        for j in range(N):
            tr[i][j] = mat[j][i]

def isSymmetric(mat, N):
    tr = [[0 for j in range(len(mat[0]))] for i in range(len(mat))]
    transpose(mat, tr, N)
    for i in range(N):
        for j in range(N):
            if (mat[i][j] != tr[i][j]):
                return False
    return True

if (isSymmetric(array, 3)):
    print("Yes")
else:
    print("No")

#3.2
N = int(input("Enter N: "))
M = int(input("Enter M: "))
array=[[int(input()) for i in range(N)] for k in range(M)]
max = float('-inf')
tempimax=0
tempkmax=0
for i in range(0,M):
    for k in range(0,N):
        if max<array[i][k]:
            max = array[i][k]
            tempimax =i
            tempimin =i
temp = array[0][0]
array[0][0]=max
array[tempimax][tempkmax] = temp
for i in range(0,M):
    for k in range(0,N):
        print(array[i][k] , end=" ")
    print("")

#4.1
N = int(input("Enter N: "))
M = int(input("Enter M: "))
array=[[int(input()) for i in range(N)] for k in range(M)]
summin = float('inf')
tempsum=0
max=0
min=0
summax = float('-inf')
for i in range(0,M):
    for k in range(0,N):
        tempsum += array[i][k]
   if summin>tempsum:
        summin = tempsum
        min = i
    if summax<tempsum:
        summax = tempsum
        max = i
    tempsum = 0
print("sum of min row: " , summin)
for i in range(0,N):
    print(array[min][i])
print("sum of max row: " , summax)
for i in range(0,N):
    print(array[max][i])
#4.2
N = int(input("Enter N: "))
array=[[int(input()) for i in range(N)] for k in range(N)]
for i in range(0,N-1):
    for k in range(0,N):
        if array[i][k]>0:
            array[i][k]=1
        elif array[i][k]<0:
            array[i][k]=0
for i in range(0,N):
    for k in range(0,N):
        print(array[i][k] , end=" ")
    print("")
#5.1
N = int(input("Enter N: "))
M = int(input("Enter M: "))
array=[[int(input()) for i in range(N)] for k in range(M)]
for i in range(0,M):
    array[i].sort()
array.sort()
for i in range(0,M):
    for k in range(0,N):
        print(array[i][k] , end=" ")
    print("") 
#5.2
N = int(input("Enter N: "))
M = int(input("Enter M: "))
array=[[int(input()) for i in range(N)] for k in range(M)]
min = float('inf')
temp = 0
for i in range(0,M):
    for k in range(0,N):
        if min> array[i][k]:
            min = array[i][k]
            temp = k
    if array[i][temp]%2 ==0:
        array[i][temp]=0
    else:
        array[i][temp] =1
for i in range(0,M):
    for k in range(0,N):
        print(array[i][k] , end=" ")
    print("")
#6.1
N = int(input("Enter N: "))
M = int(input("Enter M: "))
array=[[int(input()) for i in range(N)] for k in range(M)]
max = float('-inf')
min = float('inf')
temp = 0
for i in range(0,M):
    for k in range(0,N):
        if max< array[i][k]:
            max = array[i][k]
            temp = k
    print("The biggest number in row:" ,temp," is: " , max)
    max = 0
for i in range(0,M):
    for k in range(0,N):
        if min>array[i][i]:
            min = array[i][i]
    print("The biggest number in column:" ,i," is: " , min)
    min = float('inf')    
#6.2
import random
n = int(input("Enter n: "))
b = [[random.randrange(10) for i in range(n)] for j in range(n)]
for i in b:
    for j in i:
        print(j, end=" ")
    print()
print()
for i in b:
    print(i)
print()

a = sum(b, [])
max1 = max(a[::n + 1])
max2 = max(a[n - 1::n - 1][:n])
if max1 > max2:
    i1 = j1 = a[::n + 1].index(max1)
else:
    i1 = a[n - 1::n - 1][:n].index(max2)
    j1 = n - 1 - i1
b[n // 2][n // 2], b[i1][j1] = b[i1][j1], b[n // 2][n // 2]
for i in b:
    print(i)

#7.1
matrix = [
       [1, 2, 3],
       [0, 6, 4],
       [0, 0, 6]
    ]
correct = []
for i in range(0,3):
    for k in range(i,3):
        correct.append(matrix[i][k])
for i in range(0,len(correct)):
    print(correct[i],end=" ")
#7.2
N = int(input("Enter N: "))
M = int(input("Enter M: "))
array=[[int(input()) for i in range(N)] for k in range(M)]
arr = []
count = 0
for i in range(0,M):
    for k in range(0,N):
        if i==k:
            arr.append(array[i][k])
for i in range(0,len(arr)):
    count+=arr[i]
for i in range(0,len(arr)):
    if arr[i]%2 == 1:
        arr[i] = arr[i]/count
    print(arr[i],end="-")
#8.1
N = int(input("Enter N: "))
M = int(input("Enter M: "))
array=[[int(input()) for i in range(N)] for k in range(M)]
K = int(input("Enter k: "))
for i in range(0,M):
    for k in range(0,N):
        if i==k:
            array[K][i] = array[i][i]
for i in range(0,M):
    for k in range(0,N):
        print(array[i][k],end=" ")
    print(" ")
#9.1
N = int(input("Enter N: "))
M = int(input("Enter M: "))
array=[[int(input()) for i in range(N)] for k in range(M)]
K = int(input("Enter k: "))
for i in range(0,M):
    for k in range(0,N):
        if i==k:
            array[K][i] = array[i][i]
for i in range(0,M):
    for k in range(0,N):
        print(array[i][k],end=" ")
    print(" ")

#10.1
import numpy
def maxelement(arr):
    no_of_rows = len(arr)
    no_of_column = len(arr[0])
     
    for i in range(no_of_rows):
        max1 = 0
        for j in range(no_of_column):
            if arr[i][j] > max1 :
                max1 = arr[i][j]
arr = [[7, 4, 4, 8],
       [9, 41, 93, 11],
       [76, 34, 231, 1],
       [23, 13, 4, 5]]      
maxelement(arr)

#10.2
MAX_SIZE=10
def sortByRow(mat, n, ascending):
 
    for i in range(n):
        if (ascending):   
            mat[i].sort()
        else:
            mat[i].sort(reverse=True)
def transpose(mat, n):
 
    for i in range(n):
        for j in range(i + 1, n):
            temp = mat[i][j]
            mat[i][j] = mat[j][i]
            mat[j][i] = temp
def sortMatRowAndColWise(mat, n):
    sortByRow(mat, n, True)
    transpose(mat, n)
    sortByRow(mat, n, False)
    transpose(mat, n)
def printMat(mat, n):
 
    for i in range(n):
        for j in range(n):
            print(mat[i][j] , " ", end="")
        print()
n = 3
      
mat = [[32, 22, 1],
    [9, 58, 7],
    [6, 57, 34]]
  
print("Original Matrix:")
printMat(mat, n)
  
sortMatRowAndColWise(mat, n)
  
print("Matrix After Sorting:")
printMat(mat, n)

#11.2
import random
array = []
n = 5
for i in range(n):
    array.append([random.randint(-10, 10) for x in range(n)])

num = 0
ind = 0

array = [list(i) for i in zip(*array)]

for index, x in enumerate(array):
    if not(num):
        num = sum(x)
        ind = index
    if num > sum(x):
        num = sum(x)
        ind = index
print(array[ind])
#12.1
arr = [[-6, -1, -1, 2], [-1, -8, -1, -5], [-1, -8, -8, -8], [2, -8, -4, 0]]
for i in arr :
    print(*map('{:2d}'.format, i))
print()
n = 4
arr_rev = list(map(list,zip(*arr)))
for i in range(n) :
    for j in range(n) :
        if arr[i] == arr_rev[j] :
            print(i+1, 'строка и ', j+1, 'столбец равны')

#12.2
srand(time(NULL));;
    for (i = 0; i < str; i++)
    {
        for (j = 0; j < stolb; j++)
        {
            matr[i][j] = rand() % 10;
#13.1
import random
 
N = int(input())
M = int(input())
B = [[random.randrange(10) for i in range(M)] for j in range(N)]
 
for i in B:
    print(*map('{:3}'.format, i))
 
for i in range(0, N, 2): # четность строк тут задается
    k = min(B[i])
    print('Минимум строки %d равен %d' % (i, k))
#13.2
n = int(input())
m = int(input())
a = []
 
for i in range(n):
    a.append(list(map(int, input().split())))
 
max1 = max(max(a))
ind_max1 = a.index(max(a))
ind_max2 = a[ind_max1].index(max1)
 
min1 = min(min(a))
ind_min1 = a.index(min(a))
ind_min2 = a[ind_min1].index(min1)
 
a[ind_min1][ind_min2], a[ind_max1][ind_max2] = max1, min1
 
for i in a:
    print(*i)
#15.1
from random import randint
from operator import mul
from functools import reduce
 
 
def mprint(matrix):
    for row in matrix:
        for item in row:
            print(f'{item:>3}', end=' ')
        print()
 
 
n = int(input('Size: '))
 
matrix = [[randint(-10, 10) for _ in range(n)] for _ in range(n)]
mprint(matrix)
print()
 
tmatrix = list(zip(*matrix))
ps = [reduce(mul, row) for row in tmatrix]
min_p = min(ps)
idx = ps.index(min_p)
 
if idx < n - 1:
    tmatrix[idx], tmatrix[idx + 1] = tmatrix[idx + 1], tmatrix[idx]
else:
    tmatrix[idx], tmatrix[idx - 1] = tmatrix[idx - 1], tmatrix[idx]
 
matrix = list(zip(*tmatrix))
mprint(matrix)

