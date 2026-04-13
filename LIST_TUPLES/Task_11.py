list1=[3,4,6,7,23]
for i in range(len(list1)-1):
    list1[i],list1[i+1]=list1[i+1],list1[i]
print(list1)
