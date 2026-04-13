#yarim qalib
ls=[18,36,23,8,7,45,13,46]

for i in range(len(ls) // 2 // 2):
    ls[i], ls[len(ls) // 2 - i - 1] = ls[len(ls) // 2 - i - 1], ls[i]
k=0
for i in range(len(ls) // 2,len(ls)):
    if (len(ls)-1-len(ls)//2)*2!=i:
        ls[i], ls[len(ls)- k-1] = ls[len(ls)- k-1], ls[i]
        k+=1
print(ls)