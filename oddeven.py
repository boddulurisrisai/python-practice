str=input('Enter string')
count=0;even=[];odd=[]
for i in str:
    if i.isalpha():
        continue
    if i.isdigit():
        if int(i)%2==0:
            even.append(i)
        else:
            odd.append(i)
    else:
        count+=1
if count%2!=0:
    odd,even=even,odd
e=0
o=0
m=max(len(even),len(odd))
for i in range(m):
    if e!=len(even):
        print(even[e],end='')
        e+=1
    if o!=len(odd):
        print(odd[o],end='')
        o+=1
