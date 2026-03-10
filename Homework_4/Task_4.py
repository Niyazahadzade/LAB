def to_Binary(number:int):
    binary_number=0
    sum=1
    while number>0:
        q=number%2
        binary_number+=q*sum
        number=number//2
        sum=sum*10
    return binary_number
number=int(input("Enter a number (N>0): "))
print(to_Binary(number))
