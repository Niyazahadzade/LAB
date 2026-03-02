a=int(input("Enter the number a: "))
b=int(input("Enter the number b: "))
def qismet(a,b):
    quotient = a//b
    if quotient % 2 == 0:
        return True
    return False
print(qismet(a,b))