import random
def sade(number):
    for i in range(2,number//2+1):
        if number%i==0:
            return  False
    return True
list = [random.randint(100,999) for i in range(int(input("Ededlerin sayi N: ")))]
list2=[]
for i in list:
    if sade(i)==True:
        list2+=[i]
print(list)
print(list2)