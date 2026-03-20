#Bülbül gülə gül dedi gül gülmədi getdi bülbül gülə gülbülbülə yar olmadı getdi
#Axtarılan söz: gül
#gül simvollarının sayı: 6
setir=input("Cumleni daxil edin: ")
word=input("Axtarilan soz: ")
lenn_word=0
lenn_setir=0
for i in word:
    lenn_word+=1
for j in setir:
    lenn_setir+=1
i=0
soz=""
status=0
say=0
while i<lenn_setir:
    if setir[i]!=" " and len(soz)!=lenn_word:
        soz+=setir[i]
        status=1
        i+=1
    elif status==1 and soz==word:
        say+=1
        status=0
        soz=""
        i+=lenn_word
print(say)