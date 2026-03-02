def checking_curzon():
    number=int(input("Enter the number n: "))
    if (2**number+1)%(2*number+1)==0:
        return True
    return False
print(checking_curzon())