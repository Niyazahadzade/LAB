#Task_1
'''
def bubble_sort():
    global cem_list
    n=len(cem_list)
    global ls
    for i in range(n):
        for j in range(n-1):
            if cem_list[j]<cem_list[j+1]:
                ls[j],ls[j+1]=ls[j+1],ls[j]
    return ls

setir="ali12 vali31 pirali111"
soz=""
ls=[]
status=0
for i in setir:
    if i!=" ":
        soz+=i
        status=1
    elif status==1:
        ls+=[soz]
        status=0
        soz=""
if len(soz)!=0:
    ls+=[soz]
cem_list=[]
for i in ls:
    cem=0
    for j in i:
        if j>="0" and j<="9":
            cem+=int(j)
    cem_list+=[cem]
print(ls)
print(cem_list)
print(bubble_sort())
'''

#Task_2
'''
def bubble_sort(listt):

    global ls
    n=len(listt)
    print(listt)

    for i in range(n):
         for j in range(n-1):
             if listt[j]<listt[j+1]:
                 ls[j],ls[j+1]=ls[j+1],ls[j]
                 listt[j],listt[j+1]=listt[j+1],listt[j]
    return ls
setir="Salam"
ls=[]

tekrarlanan=[]
n=len(setir)
yeni=""

for i in range(n):
    say=0
    tekrarlanma=False
    if setir[i] not in yeni:
        yeni+=setir[i]
        tekrarlanma=True
        for j in range(i,n):

            if setir[i]==setir[j]:
                say+=1
    if tekrarlanma==True:
        tekrarlanan+=[say]

for i in yeni:
    ls+=[i]
print(tekrarlanan)
print(ls)
print(bubble_sort(tekrarlanan))
'''

#Task_3
'''
def bubble_sort(ls,sait_say):

    n=len(ls)
    for i in range(n):
        for j in range(n-1):
            if sait_say[j]>sait_say[j+1]:
                sait_say[j],sait_say[j+1]=sait_say[j+1],sait_say[j]
                ls[j],ls[j+1]=ls[j+1],ls[j]
    return ls
cumle=input("Enter the sentence: ")
sait="aeiouöüıə"
sait_say=[]
ls=[]
soz=""
status=0
for i in cumle:
    if i!=" ":
        soz+=i
        status=1
    elif status==1:
        ls+=[soz]
        status=0
        soz=""
if len(soz)!=0:
    ls+=[soz]
print(ls)

for i in ls:
    say=0
    for j in i:
        if j in sait:
            say+=1
    sait_say+=[say]

print(bubble_sort(ls,sait_say))
'''
#Task_4
'''
def summ_ascii_codes(soz):
    summ=0
    for i in soz:
        summ+=ord(i)
    return summ
def bubble_sort(ls):
    global sozler
    for i in range(len(ls)):
        for j in range(len(ls)-i-1):
            if len(sozler[j])==len(sozler[j+1]):
                if summ_ascii_codes(sozler[j])<summ_ascii_codes(sozler[j+1]):
                    ls[j], ls[j + 1] = ls[j + 1], ls[j]
                    sozler[j], sozler[j + 1] = sozler[j + 1], sozler[j]
            else:
                if ls[j]>ls[j+1]:
                    ls[j], ls[j + 1] = ls[j + 1], ls[j]
                    sozler[j], sozler[j + 1] = sozler[j + 1], sozler[j]

    return sozler

def lenn(soz):
    uzun=0
    for i in soz:
        uzun+=i
    return uzun

sozler=input("Enter the words: ").split()
uzunluq=[]

for i in sozler:
    uzunluq+=[len(i)]
sorted_list=bubble_sort(uzunluq)
for i in sorted_list:
    print(i)
'''

#Task_5
'''
def bubble_sort_eded_min(eded):
    eded_1=eded
    ededler_list=[]
    while eded_1:
        q=eded_1%10
        ededler_list+=[q]
        eded_1//=10

    for i in range(len(ededler_list)):
        for j in range(len(ededler_list)-i-1):
            if ededler_list[j]>ededler_list[j+1]:
                ededler_list[j],ededler_list[j+1]=ededler_list[j+1],ededler_list[j]

    if 0 in ededler_list:
        ededler_list[0],ededler_list[1]=ededler_list[1],ededler_list[0]
    n=len(ededler_list)
    summ=0
    for i in range(n):
         summ+=ededler_list[i]*(10**(n-i-1))
    return summ
def quick_sort(ls):
     if len(ls) <= 1:
         return ls
     p = ls[len(ls)//2]
     l = [x for x in ls if x < p]
     m = [x for x in ls if x == p]
     r = [x for x in ls if x > p]
     return quick_sort(l) + m + quick_sort(r)
ededler=map(int,input("Enter the numbers: ").split())
yn_list=[]
for i in ededler:
    yn_list+=[bubble_sort_eded_min(i)]
print(quick_sort(yn_list))
'''

#Task_6
'''
def bubble_sort_eded_min(eded):
    eded_1=eded
    ededler_list=[]
    while eded_1:
        q=eded_1%10
        ededler_list+=[q]
        eded_1//=10

    for i in range(len(ededler_list)):
        for j in range(len(ededler_list)-i-1):
            if ededler_list[j]>ededler_list[j+1]:
                ededler_list[j],ededler_list[j+1]=ededler_list[j+1],ededler_list[j]

    if 0 in ededler_list:
        ededler_list[0],ededler_list[1]=ededler_list[1],ededler_list[0]
    n=len(ededler_list)
    summ=0
    for i in range(n):
         summ+=ededler_list[i]*(10**(n-i-1))
    return summ
def bubble_sort_eded_max(eded):
    eded_1 = eded
    ededler_list = []
    while eded_1:
        q = eded_1 % 10
        ededler_list += [q]
        eded_1 //= 10

    for i in range(len(ededler_list)):
        for j in range(len(ededler_list) - i - 1):
            if ededler_list[j] < ededler_list[j + 1]:
                ededler_list[j], ededler_list[j + 1] = ededler_list[j + 1], ededler_list[j]
    n = len(ededler_list)
    summ = 0
    for i in range(n):
        summ += ededler_list[i] * (10 ** (n - i - 1))
    return summ
def quick_sort(ls):
    if len(ls)<=1:
        return ls
    p=ls[len(ls)//2]
    l=[x for x in ls if x>p]
    m=[x for x in ls if x==p]
    r=[x for x in ls if x<p]
    return quick_sort(l)+m+quick_sort(r)
ededler=map(int,input("Enter the numbers: ").split())
eded_yekun=[]
for i in ededler:
    ferq=bubble_sort_eded_max(i)-bubble_sort_eded_min(i)
    eded_yekun+=[ferq]
print(quick_sort(eded_yekun))
'''

#Task_7
