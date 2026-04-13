#Bülbül gülə gül dedi gül gülmədi getdi bülbül gülə gülbülbülə yar olmadı getdi
#Axtarılan söz: gül
#gül simvollarının sayı: 6
setir=input("Cumleni daxil edin: ")
word=input("Axtarilan soz: ")
say = 0
i = 0

while i <= len(setir) - len(word):
    if setir[i:i+len(word)] == word:
        say += 1
    i += 1

print(say)