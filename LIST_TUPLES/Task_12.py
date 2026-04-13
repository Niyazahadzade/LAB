list1 = ['A','B','C']
list2 = [5,2 ,3]
yeni_list=[]
for i in range(len(list1)):
    yeni_list+=[[list1[i],list2[i]]]
print(yeni_list)