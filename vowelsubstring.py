import re
b=input('enter string')
r=[];max=-1;z=-1
for i in range(len(b)):
    for j in range(i+1,len(b)+1):
        c=b[i:j]
        for k in c:
            if k=='a' or k=='e' or k=='i' or k=='o' or k=='u':
                flag=0
            else:
                flag=1
                break
        if flag==0:
            r.append(c)
for i in r:
    if len(i)>max:
        max=len(i)
        z=i
print(z)
            
