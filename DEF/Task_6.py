def disarium():
    number=int(input("Enter the number: "))
    new_number_1=number
    new_number_2=number
    sum=0
    length=0
    while new_number_1>0:
        new_number_1=new_number_1//10
        length+=1
    while new_number_2>0:
        q=new_number_2%10
        sum+=q**length
        new_number_2=new_number_2//10
        length-=1
    if sum==number:
        return True
    return False
print(disarium())
