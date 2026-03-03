def kempner():
    number=int(input("Enter the number: "))
    fact=1
    i=1
    while True:
        if fact%number==0:
            return f'{number} -> {i}!'
        else:
            i+=1
            fact*=i
print(kempner())