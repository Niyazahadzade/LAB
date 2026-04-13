setir=input("Setri daxil edin: ")
first_work=""
status=0
for i in setir:
    if i !=" ":
        first_work+=i
        status=1
    elif status==1:
        print(first_work)
        break