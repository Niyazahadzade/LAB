def lenn(text: str):
    lenn=0
    for i in text:
        lenn+=1
    return lenn
text=input("Enter the text: ")
yn_txt=str()
for i in text:
    if i == "a":
        yn_txt+="b"

    elif i == "b":
        yn_txt+="a"

    elif i=="A":
        yn_txt+="B"

    elif i=="B":
        yn_txt+="A"

    else:
        yn_txt+=i
print(yn_txt)
