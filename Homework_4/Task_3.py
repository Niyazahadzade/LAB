number=int(input("Enter a number (N>0): "))
def length_num(number: int):
    length=0
    while number>0:
        number=number//10
        length+=1
    return length
length=length_num(number)
if length%2!=0:
    print("invalid")
else:
    def look_and_say(number:int):
        global length

        for i in range(1,length):
            if i%2!=0:
                new_number_1 = number // (10**(length-(i+1)))
                new_number_2 = new_number_1 // 10
                for j in range(1,new_number_2+1):
                    print(new_number_1%10,end="")
                #sum+=(new_number_1%10)*10**
                number=number%(10**(length-(i+1)))
    look_and_say(number)
