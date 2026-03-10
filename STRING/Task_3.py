text=input("Enter the text: ")
string=""
count=0
for i in text:
    if i!=" ":
        string+=i

    else:
        if len(string)>0:
            count+=1
        string=""
print(count)