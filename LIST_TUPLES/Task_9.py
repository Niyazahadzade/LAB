List1 = [1 ,2 , 3]
List2 = [5 , 4 , 6]
k=0
for i in range(len(List1)):
    for j in range(len(List2)):
        if List1[i]==List2[j]:
            k+=1
            break
    if k!=0:
        print("Cavab: ortaq element var.")
        break
if k==0:
    print("Cavab: ortaq element yoxdur.")
