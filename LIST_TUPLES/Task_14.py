import random
def kvadrat(number):
    i=0
    while i<number//2:
        if i**2==number:
            return True
        else:
            i+=1
    return False
list = [random.randint(10,50) for i in range(int(input("Ededi daxil edin: ")))]
list2=[]
for i in list:
    if kvadrat(i)==True:
       list2+=[i]
print(f'List1 = {list}')
print(f'List2 = {list2}')