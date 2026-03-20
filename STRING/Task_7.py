setir=input("Setri daxil edin: ")
old=input("Neyi evezleyirik: ")
new=input("Ne ile evezleyirik: ")
yn_setir=""
status=0
soz=""
for x in setir:
    if x!=" ":
        status=1
        soz+=x
    else:
        if status==1:
            if soz==old:
                yn_setir=yn_setir+new+" "
            else:
                yn_setir=yn_setir+soz+" "
        soz=""
        status=0
yn_setir+=soz
print(yn_setir)