def pro_or_hete():
    p=int(input("Enter the number p: "))
    for i in range(int(p**(1/2))+1):
        if i*(i+1)==p:
            return "pronic"
    return "heteromecic"
print(pro_or_hete())
