import random
list = [random.randint(-100,100) for i in range(8)]
musbet_list=[]
menfi_list=[]
sifir_list=[]
for i in list:
    if i>0:
        musbet_list+=[i]
    elif i==0:
        sifir_list+=[i]
    else:
        menfi_list+=[i]
print(f' A = {list}')
print(f' B = {musbet_list+sifir_list+menfi_list}')