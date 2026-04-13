def say(s):
    sayy=0
    for i in s:
        if i==".":
           sayy+=1
    return sayy


file_name=input("Faylin adini daxil edin: ")
new_extension=input("Faylin genislenmesini daxil edin:")
countt=say(file_name)
k=0
if countt==0:
    new_file_name=file_name+"."+new_extension

else:
    for i in range(0,len(file_name)):
        if file_name[i]==".":
            k=i
    new_file_name=file_name[:k+1]+new_extension
print(new_file_name)