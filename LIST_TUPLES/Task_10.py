List1 = [11, 22, 33, 44, 55]

List2 = [12, 23, 33, 45, 55]
print("Tekrarlanan elementler: ",end="")
say=0
if List1<List2:
    for i in range(len(List1)):
        if List1[i]==List2[i]:
            print(List1[i],end=" ")
            say+=1
else:
    for i in range(len(List2)):
        if List1[i]==List2[i]:
            print(List2[i],end=" ")
            say+=1
print()
print(f'Eyni indeksde yerleshen eyni elementlerin sayi = {say}')