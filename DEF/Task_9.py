def cem(eded):
    sum=0
    while eded>0:
        q=eded%10
        sum+=q
        eded=eded//10
    return sum
def qismet(q):
    k=0
    for i in range(2,q//2+1):
        if q%i==0:
            k+=1
    if k>=1:
        return False
    return True


number=int(input("Enter the number: "))
q=number//cem(number)
print(qismet(q))
