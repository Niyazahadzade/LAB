import random
list = [random.randint(100,999) for i in range(int(input("Ededlerin sayi N: ")))]
list2=[]
for i in list:
    if abs(i % 100-(i // 10) % 10) % 2 != 0 and (i % 100-(i // 10) % 10) % 2 != 0:
        list2+=[i]
print(f'list1 = {list}')
print(f'list2 = {list2}')