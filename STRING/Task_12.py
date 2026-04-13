setir=input("Setir: ")
sait="AOUE"; samit="bcmf"; reqem="3579"; durgu="!?,;"
sait_setir=""
samit_setir=""
reqem_setir=""
durgu_setir=""
for x in setir:
    if x in sait and x not in sait_setir:
        sait_setir+='"'+x+'"'+" "
    elif x in samit and x not in samit_setir:
        samit_setir+='"'+x+'"'+" "
    elif x in reqem and x not in reqem_setir:
        reqem_setir+='"'+x+'"'+" "
    elif x in durgu and x not in durgu_setir:
        durgu_setir+='"'+x+'"'+" "

yn_setir=sait_setir+samit_setir+reqem_setir+durgu_setir
print(f'{yn_setir}simvollari var')