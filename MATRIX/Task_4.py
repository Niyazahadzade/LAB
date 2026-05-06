import random


def create_matrix(n):
    A=[]
    for i in range(n):
        A+=[[0]*n]
        for j in range(n):
            A[i][j]=random.randint(10,99)
    return A

n=int(input("setiri yazin: "))


A=create_matrix(n)
#Variant_A
'''
summ=0
for row in A:
    for j in row:
        print(f"{j:4}",end="")
    print()
for row in A:
    for j in row:
        summ+=j
ededi_orta=summ/(n*n)

for i in range(n):
    for j in range(n):
        if A[i][j]<ededi_orta:
            A[i][j]=0
        else:
            A[i][j] = 255
print("Sonraki versiya:")
for row in A:
    for j in row:
        print(f"{j:4}",end="")
    print()
'''

#Variant_B
'''
for row in A:
    for j in row:
        print(f"{j:4}",end="")
    print()
for i in range(n):
    for j in range(n):
        if i<=j:
            if A[i][j]>50:
                A[i][j]=255
            else:
                A[i][j] = 0
print("sonraki versiya")
for row in A:
    for j in row:
        print(f"{j:4}",end="")
    print()
'''

#Variant_C
'''
for row in A:
    for j in row:
        print(f"{j:4}",end="")
    print()
for i in range(n):
    for j in range(n):
        if i<=j:
            A[i][j]=0
print("sonraki versiya")
for row in A:
    for j in row:
        print(f"{j:4}",end="")
    print()
'''
#Variant_D
'''
for row in A:
    for j in row:
        print(f"{j:4}",end="")
    print()
for i in range(n):
    for j in range(n//2):
        A[i][j],A[i][n-j-1]=A[i][n-j-1],A[i][j]
print("Result")
for row in A:
    for j in row:
        print(f"{j:4}",end="")
    print()
'''

#Variant_E
'''
for row in A:
    for j in row:
        print(f"{j:4}",end="")
    print()
for i in range(n):
    for j in range(n//2):
         A[j][i],A[n-j-1][i]=A[n-j-1][i],A[j][i]

print("Result")
for row in A:
    for j in row:
        print(f"{j:4}",end="")
    print()
'''
#Variant_F
'''
for row in A:
    for j in row:
        print(f"{j:4}",end="")
    print()
B=create_matrix(n)
for i in range(n):

    for j in range(n):
        B[i][j]=A[n-j-1][i]

print("Result: ")
for row in B:
    for j in row:
        print(f"{j:4}",end="")
    print()
'''