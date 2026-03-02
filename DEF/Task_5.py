def length():
    number=int(input("Enter the number: "))
    length=0
    if number!=0:
        if number>0:
            while number>0:
                number=number//10
                length+=1
            return length
        else:
            number=number*(-1)
            while number>0:
                number=number//10
                length+=1
            return length
    return 1
print(length())
