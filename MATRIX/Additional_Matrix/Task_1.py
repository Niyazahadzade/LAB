

import random


def create_matrix(n,m):
    A=[]
    for i in range(n):
        A+=[[0]*m]
        for j in range(m):
            A[i][j]=random.randint(-10 ,30)
    return A



n=int(input("Enter the number of the rows: "))
m=int(input("Enter the number of the columns: "))

A=create_matrix(n,m)


#Task_1
'''
def maxx(ls):
    maxx=ls[0]
    for i in ls[1:]:
        if i>maxx:
            maxx=i
    return maxx
def minn(ls):
    minn=ls[0]
    for i in ls[1:]:
        if minn>i:
            minn=i
    return minn
for row in A:
    for j in row:
        print(f"{j:4}",end="")
    print()

for i in range(len(A)):

    maxi=maxx(A[i])
    for j in range(len(A[i])):
        if A[i][j]==maxi:
            ls=[]
            for _ in range(len(A)):
                ls+=[A[_][j]]
            if A[i][j]==minn(ls):
                print(A[i][j])
'''

#Task_2
'''
def summ(ls):
    summ=0
    for i in ls:
        summ+=i
    return summ
for row in A:
    for j in row:
        print(f"{j:4}",end="")
    print()

for i in range(m):
    ls=[]
    say=0
    for j in range(n):
        ls+=[A[i][j]]
    for _ in ls:
        if _ < 0:
            say+=1
    if say!=0:
        print(f"{i} sutunundaki menfilerin sayi:{say}")
    else:
        print(f"{i} sutunundaki ededlerin cemi:{summ(ls)}")
'''

#Task_3
# Matrisdə bütün elementləri dəyiş:
# o Əgər element təkdirsə → kvadratını al
# o Əgər element cütdürsə → 2-yə böl
'''
for row in A:
    for j in row:
        print(f"{j:4}",end="")
    print()

for i in range(n):
    for j in range(m):
        if A[i][j]%2==1:
            A[i][j]=A[i][j]**2
        else:
            A[i][j]=A[i][j]/2
print("Result: ")
for row in A:
    for j in row:
        print(f"{j:5}",end="")
    print()

'''

#Task_4


for row in A:
    for j in row:
        print(f"{j:4}",end="")
    print()
ls_cem=[]
for i in range(n-1):
    for j in range(m-1):
        ls_cem+=[A[i][j]+A[i][j+1]+A[i+1][j]+A[i+1][j+1]]
print(maxx(ls_cem))