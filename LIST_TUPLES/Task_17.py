import random
def menfi_cut(number):
    while number!=0 and number!=-1:
        number=number+2
    if number==0:
        return True
    return False
list = [random.randint(-10,10) for i in range(10)]
list_2=[]
for i in list:
    if i<0 and menfi_cut(i)==True:
        list_2+=[i]
print(f'A = {list}')
print(f'B = {list_2}')