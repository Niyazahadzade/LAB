#Sual_1
'''
def ikilik(eded):
    summ=0
    i=0
    while eded>0:
        qaliq=eded%2
        summ+=qaliq*(10**i)
        eded=eded//2
        i+=1
    return summ



def dalga(eded):
    beraber=0
    azalma=0
    coxalma=0
    q_1=eded%10
    eded=eded//10
    while eded>0:
         q_2=eded%10
         if q_1>q_2:
             coxalma+=1
         elif q_1<q_2:
             azalma+=1
         else:
             beraber+=1
         q_1=q_2
         eded=eded//10
    if coxalma>0 and azalma>0 and beraber==0:
         return True
    return False
print(dalga(ikilik(10)))
n=int(input("Enter the number: "))
print(dalga(n))
print(dalga(ikilik(n)))
if dalga(n) and dalga(ikilik(n)):
       print("dalgavaridir")
else:
     print("dalgavari deyil")
'''
import random


#Sual_2

def IP_scanner(dict,ipp):
    for i in dict:
        #print(i)#location
        for j in dict[i]:
            #print(j)#device 2ci locationi Data center 2
            for z in dict[i][j]:
                #print(z)#devicein adi
                for k in dict[i][j][z]:
                   if k=="ip" and dict[i][j][z][k]==ipp:
                        return f" device:{z} , location:{i} -> {j} "

def overloadd(dict):
    ls=[]
    for i in dict:
        #print(i)#location
        for j in dict[i]:
            #print(j)#device 2ci locationi Data center 2
            for z in dict[i][j]:
                #print(z)#devicein adi
                for k in dict[i][j][z]:
                    if k=="load" and dict[i][j][z][k]>80:
                        ls+=[z,i]
    return ls

def statuss(dict):
    ls = []
    for i in dict:
        # print(i)#location
        for j in dict[i]:
            # print(j)#device 2ci locationi Data center 2
            for z in dict[i][j]:
                # print(z)#devicein adi
                for k in dict[i][j][z]:
                    if k=="status" and dict[i][j][z][k]=="down":
                        ls+=[z]
    return ls

def validation_ip(setir):
    soz=""
    status=0
    say=0
    for i in setir:
        if i!=".":
            soz+=i
            status=1

        elif status==1:
           if int(soz)<=255 and int(soz)>=0:
               say+=1

           soz=""
           status=0
    if len(soz)>0:
        if int(soz) <= 255 and int(soz) >= 0:
            say += 1
    if say==4:
        return True
    return False


def validation(dict):
    warning=[]
    for i in dict:
        # print(i)#location
        for j in dict[i]:
            # print(j)#device 2ci locationi Data center 2
            for z in dict[i][j]:
                # print(z)#devicein adi
                for k in dict[i][j][z]:
                    if k=="ip":
                        if not(validation_ip(dict[i][j][z][k])):

                            warning+=[z]
    if len(warning)>0:

        return warning
    return f"Butun ipler duzgundur"
network_infrastructure = {
 "Region_North": {
    "DataCenter_1": {
        "Router_A": {"ip": "192.168.1.1", "status": "active", "load": 45, "connections": 120},
        "Switch_B": {"ip": "192.168.1.10", "status": "active", "load": 20, "connections": 48}
 },
    "DataCenter_2": {
        "Server_X": {"ip": "10.0.0.5", "status": "down", "load": 0, "connections": 0}}},
 "Region_South": {
    "Main_Office": {
        "Router_C": {"ip": "172.16.0.1", "status": "active", "load": 88, "connections": 250},
        "Firewall_D": {"ip": "172.16.0.5", "status": "active", "load": 30, "connections":
1000}}}}

#print(IP_scanner(network_infrastructure,"10.0.0.5"))
#print(overloadd(network_infrastructure))
#print(statuss(network_infrastructure))
#print(validation(network_infrastructure))


#Sual_3
'''

def create_matrix(n,m):
    A=[]
    for i in range(n):
        A+=[[0]*m]
        for j in range(m):
            A[i][j]=random.randint(-10,10)
    return A
def maxx(ls):
    maxx=ls[0]
    for i in ls[1:]:
        if maxx<i:
            maxx=i
    return maxx
def minn(ls):
    minn=ls[0]
    for i in ls[1:]:
        if minn>i:
            minn=i
    return minn
n=int(input("siranin sayini daxil edin: "))
m=int(input("sutunun sayini daxil edin: "))

A=create_matrix(n,m)

for row in A:

    for j in row:
        print(f"{j:4}",end="")
    print()
tapildi=False
for i in range(n):
    for j in range(m):
        if A[i][j]==minn(A[i]):
            sutun=[]
            for k in range(n):
                sutun+=[A[k][j]]
            if A[i][j]==maxx(sutun):
                print(f"tapildi: {A[i][j]}")
                tapildi=True
if not tapildi:
    print("Tapilmadi")

'''

#Sual_4

'''
s=input("setri daxil edin: ")
en_uzun=""
for i in range(len(s)):

    gorulenler={}
    for j in range(i,len(s)):
        simvol=s[j]

        if simvol in gorulenler:
            break
        gorulenler[simvol]=True

        if j-i+1>len(en_uzun):
            en_uzun=s[i:j+1]

print(en_uzun)
'''

#Sual_5

l1=list(map(int,(input("1ci siyahini daxil edin: ").split())))
print(l1)
l2=list(map(int,input("2ci siyahini daxil edin: ").split()))
summ=0
for i in l1:
    summ+=i
k=summ%len(l2)

for t in range(k):
    for j in range(-1,-1*len(l2),-1):
        l2[j],l2[j-1]=l2[j-1],l2[j]
if len(l1)>len(l2):
    for i in range(len(l2))



