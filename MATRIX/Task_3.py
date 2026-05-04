import random


def create_matrix(n):
    A=[]
    for i in range(n):
        A+=[[0]*n]
        for j in range(n):
            A[i][j]=random.randint(10,100)
    return A


n=int(input("Enter the number: "))

A=create_matrix(n)

#Variant_A

'''
maxx=A[0][0]
setir=0
sutun=0
for row in A:
    for j in row:
        print(f"{j:4}",end="")
    print()
for i in range(len(A)):
    for j in range(len(A[i])):
        if A[i][j]>maxx:
            maxx=A[i][j]
            setir=i
            sutun=j
print(f"Maximal eded:{maxx},setirin indexi:{setir}, sutunun indexi:{sutun}")
'''

#Variant_B
'''
for row in A:
    for j in row:
        print(f"{j:4}",end="")
    print()
for i in range(len(A)//2):
    for j in range(len(A[i])):
        A[i][j],A[n-i-1][j]=A[n-i-1][j],A[i][j]
print("Tersine cevrilmis")
for row in A:
    for j in row:
        print(f"{j:4}",end="")
    print()
'''

#Variant_C
'''
def pronic_eded(eded):
    i=1
    while i <= eded // 2:
        hasil = i * (i + 1)
        if hasil == eded:
            return True
        else:
            i = i + 1
    return False
for row in A:
    for j in row:
        print(f"{j:4}",end="")
    print()
ls=[]
for i in range(len(A)):
    if i%2==0:
        for j in range(len(A[i])):
            if pronic_eded(A[i][j]):
                ls+=[A[i][j]]
print(ls)
'''

# Variant_D
'''
def sade(number):
    for i in range(2,number//2+1):
        if number%i==0:
            return False
    return True
for row in A:
    for j in row:
        print(f"{j:4}",end="")
    print()

ls=[]

for i in range(len(A)):
    for j in range(len(A[i])):
        if (i==j or i+j==n-1) and sade(A[i][j]):
            ls+=[A[i][j]]
print(ls)

'''