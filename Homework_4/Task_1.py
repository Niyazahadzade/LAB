def max_collatz(number: int):
    global n
    mx =n
    while n!=1:
        print(n, end=" ")
        if n%2==0:
            n=n//2
        else:
            n=n*3+1
            if n>mx:
                mx=n
    print(n)
    print(mx)
n=int(input("Enter a number (N>0): "))
max_collatz(n)