import random


def create_matrix(row,column):
    A=[]
    for i in range(row):
        A+=[[0]*column]
        for j in range(column):
            A[i][j]= random.randint(-10,10)
    return A
n=int(input("Setir sayini daxil edin: "))
m=int(input("Sutun sayini daxil edin: "))

A=create_matrix(n,m)


for row in A:
    for j in row:
        print(f"{j:3}",end=" ")
    print()

#Variant_A
'''
def abss(eded):
    if eded>0:
        return eded
    return eded*(-1)
summ=0
for row in A:
    for j in row:
        summ+=j
print(f"Mutleq qiymetce elementlerinin cemi:{summ}")
'''
#Variant_B
'''
hasil=1
for row in A:
    for j in row:
        kvadrat=j**2
        hasil*=kvadrat

print(f"Elementlerinin kvadratlarinin hasili: {hasil}")
'''

#Variant_C
'''
k=int(input("istediyiniz setri daxil edin: "))
for i in range(len(A)):
    if i+1==k:
        hasil=1
        for j in A[i]:
            hasil*=j
        print(f"{k} nomreli setrin elementleri hasili:{hasil}")
'''

#Variant_D
'''
min_eded=A[0][0]
sutun=0
for i in A[0][1:]:
    if min_eded>i:
        min_eded=i
for i in range(1,len(A)):
    for j in range(len(A[i])):
        if A[i][j]<min_eded:
            min_eded=A[i][j]
            sutun=j
summ=0
for i in range(len(A)):
    summ+=A[i][sutun]
print(f"Ən kiçik elementinin yerləşdiyi sütun elementlərinin cəmi: {summ}")
'''

#Variant_E
'''
ls=[]
if (n%2==0 and m%2==0) or (n%2==1 and m%2==1):
    for i in range(len(A)):
        for j in range(len(A[i])):
            if i==j or i+j==n-1:
                ls+=[A[i][j]]
    print(ls)

else:
    print("Bu matrisde diaqonal yoxdu!!!")
'''

