setir=input("Faylin unvanini daxil edin: ")
soz=""
status=0
for x in setir:
    if x!=" " and x!="/":
        soz+=x
        status=1
    elif status==1:
        print(soz)
        soz=""
        status=0
print(soz)