list = [5, 7, 5, 9, 2, 6, 4, 3, 2, 5, 6]
sum=0
for i in list:
    if i%2!=0:
        sum+=i
    else:
        break
print(f'Listin ilk cüt ədədinə qədər olan cəm: {sum}')