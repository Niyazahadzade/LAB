import random
list = [random.randint(0,100) for i in range(10)]
#list=[int(x) for x in input().split()]
bigger_sum=0
bigger_countt=0
smaller_sum=0
smaller_countt=0
for i in list:
    if i<50:
        smaller_sum+=i
        smaller_countt+=1
    else:
        bigger_sum+=i
        bigger_countt+=1

print(f'[0,50) araliginda ededi orta = {smaller_sum/smaller_countt}')
print(f'[50,100) araliginda ededi orta = {bigger_sum/bigger_countt}')
