import random


def create_matrix(n):
    A=[]
    for i in range(n):
        A+=[[0]*n]
        for j in range(n):
            A[i][j]=random.randint(10,20)
    return A

n=int(input("Enter the number of the rows: "))

A=create_matrix(n)

#Type_1
'''
for row in A:
    for j in row:
        print(f"{j:4}",end="")
    print()

for i in range(n):
    for j in range(n):
        if i==j or j==0 or j==n-1:
            A[i][j]="+"
print("Result:")

for row in A:
    for j in row:
         print(f"{j:4}",end=" ")
    print()
'''

#Type_2
'''
for row in A:
    for j in row:
        print(f"{j:4}",end="")
    print()
for i in range(n):
    for j in range(n):
         if i==0 or i==2:
             A[i][j]="+"
         elif j==0 or j==n-1:
             A[i][j]="+"
for row in A:
    for j in row:
        print(f"{j:4}",end="")
    print()
'''

#Type_3
'''
for row in A:
    for j in row:
        print(f"{j:4}",end="")
    print()
for i in range(n):
    for j in range(n):
        if i<=n//2 and (i==j or i+j==n-1):
            A[i][j]="+"
        elif j==n//2 and i>n//2:
            A[i][j]="+"
for row in A:
    for j in row:
        print(f"{j}",end="")
    print()
'''
#Type_4
'''
for row in A:
    for j in row:
        print(f"{j:4}",end="")
    print()
for i in range(n):
    for j in range(n):
        if i==0 or j==n//2:
            A[i][j]=0
print("Result: ")
for row in A:
    for j in row:
        print(f"{j:4}",end="")
    print()
'''

#Type_5
'''
for row in A:
    for j in row:
        print(f"{j:4}",end="")
    print()
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1:
            A[i][j]=0
        elif i+j==n-1:
            A[i][j]=0
print("Result:")
for row in A:
    for j in row:
        print(f"{j:4}",end="")
    print()
'''

#Type_6
'''
for row in A:
    for j in row:
        print(f"{j:4}",end="")
    print()
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1:
            A[i][j]="+"
        elif j==0 or j==n-1:
            A[i][j]="+"
print("Result: ")
for row in A:
    for j in row:
        print(f"{j:4}",end="")
    print()
'''