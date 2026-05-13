list_1=[-1,2,'aasf','1','123',123]
list_2=[]
for i in list_1:
     eded=i*10
     if len(str(eded))==len(str(i))+1 and str(i)[0]!="-":
         list_2+=[i]
print(list_2)
