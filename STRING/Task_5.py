#Soyad, ad və ata adınızı daxil edin: İbrahimov Perviz Senan oglu
#Nəticə: P.S. İbrahimov
setir=input("Soyad, ad ve ata adinizi daxil edin: ")
surname=""
for x in range(len(setir)):
    if setir[x]!=" ":
        surname+=setir[x]
    else:
        if len(surname)>0:
            break
yn_setir=""
for name in setir[x+1:]:
    if name > "A" and name<"Z":
        yn_setir=yn_setir+name+". "

yn_setir+=surname
print(yn_setir)


