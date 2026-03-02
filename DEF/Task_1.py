def odd_or_even():
    sum=0
    while True:
        number=int(input("Enter the number: "))
        if number!=-1:
            sum+=number
        else:
            if sum%2==0:
                return "Even"
            return "Odd"
print(odd_or_even())



