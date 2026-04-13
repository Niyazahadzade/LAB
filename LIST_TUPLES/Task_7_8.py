import random
list = [i**2 for i in range(1,16)]
print('Ilk 5 element = ',end="")
for i in range(5):
    if i!=4:
        print(f'{list[i]}, ',end="")
    else:
        print(f'{list[i]}')

print('Son 5 element = ',end="")
for i in range(len(list)-5,len(list)):
    if i!=len(list)-1:
        print(f'{list[i]}, ',end="")
    else:
        print(f'{list[i]}')
