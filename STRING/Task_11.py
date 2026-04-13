#Input: This text is used to check the program.
#Output: Tis txt i ued t ceck te pogram.

string=input("Enter the text: ")

say=0
soz=""
status=0
yn_setir=""
for i in string:
    if i != " " :
        status=1
        say += 1
        if say != 2:
            soz += i

    elif status==1:
        yn_setir+=soz+" "
        soz=""
        say=0
yn_setir+=soz
print(yn_setir)