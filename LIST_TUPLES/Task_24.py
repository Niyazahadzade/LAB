list=[5,5,5,5]
minn_1=float('+inf')
minn_2=float('+inf')
for i in list:
    if i<minn_1:
        minn_2 = minn_1
        minn_1=i
    elif minn_2 > i  and i!=minn_1:
        minn_2=i
if minn_2==float('+inf'):
    print(list[0])
else:
    print(minn_2)