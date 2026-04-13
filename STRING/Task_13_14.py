
ifade = input("İfadəni daxil et: ")

reqem = ""
netice = 0
if ifade=="-":
    ifade="0"+ifade
if ifade[1]=="-":
    isare = -1
else:
    isare = 1
for i in ifade:
    if i in "0123456789":
        reqem += i
    else:
        if len(reqem)!=0:
            netice += isare * int(reqem)
        else:
            netice+=0
        reqem = ""
        if i == '+':
            isare = 1
        else:
            isare = -1


netice += isare * int(reqem)

print("Nəticə:", netice)