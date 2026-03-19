setir=input("Setri daxil edin: ")
lenn=0
mx=0
status=0
mx_yn=""
yn=""
for x in setir:
    if x != " ":
        lenn+=1
        yn+=x
    else:
        if lenn>=mx:
            mx=lenn
            mx_yn=yn
        lenn=0
        yn=""
print(f'{mx_yn},uzunlugu {mx}')

