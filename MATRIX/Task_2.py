#Variant_A
import random


def create_matrix(row,column):
    A=[]
    for i in range(row):
        A+=[[0]*column]
        for j in range(column):
            A[i][j]=random.randint(-10,10)
    return A
n=int(input("Enter the number of rows: "))


A=create_matrix(n,n)
B=create_matrix(n,n)
print("A matrisi")
for row in A:
    for j in row:
        print(f"{j:4}",end="")
    print()
print("B matrisi")
for row in B:
    for j in row:
        print(f"{j:4}",end="")
    print()
#Variant_A
'''
C=create_matrix(n,m)
for i in range(len(C)):
    for j in range(len(C[i])):
        C[i][j]=A[i][j]-B[i][j]
print("C nin ferq matrisi")
for row in C:
    for j in row:
        print(f"{j:4}",end="")
    print()

for i in range(len(C)):
    for j in range(len(C[i])):
        C[i][j]=A[i][j]+B[i][j]
print("C nin cem matrisi")
for row in C:
    for j in row:
        print(f"{j:4}",end="")
    print()
'''

#Variant_B
'''
k=int(input("A matrisinin istediginiz setrini daxil edin: "))
m=int(input("B matrisinin istediginiz sutunu daxil edin: "))
C=[]

for i in range(n):
    C+=[A[k-1][i]*B[i][m-1]]
for row in C:
    print(row,end=" ")
'''

#Variant_C
'''
k=int(input("A matrisinin istediginiz setri daxil edin: "))
diaq=[]
for i in range(len(A)):
    for j in range(len(A[i])):
        if  i==j:
            diaq+=[A[i][j]]

B=[]
if 0 in diaq:
    print("Bas diaqonalda sifir var!")
else:    
    for i in range(len(A[k])):
        B+=[A[k-1][i]/diaq[i]]
print(B)
'''

#Variant_D
'''
diaq=0
for i in range(len(A)):
    for j in range(len(A[i])):
        if  i==j:
            diaq+=A[i][j]
for i in range(len(A)):
    if i>0 and i%2==0:
        for j in range(len(A[i])):
            A[i][j]=A[i][j]/diaq
print("yeni A matrisi")
for row in A:
    for j in row:
        print(f"{j:4}",end=" ")
    print()
'''

#Variant_E
'''
ls=[]
for row in A:
    summ=0
    for j in row:
        summ+=j
    ls+=[summ]
print(ls)
'''

#Variant_F
'''
ls=[]
for i in range(len(A)):
    hasil=1
    for j in range(len(A[i])):
        hasil*=A[j][i]
    ls+=[hasil]
print(ls)
'''