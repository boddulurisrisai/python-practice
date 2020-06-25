
str=input('enter a string')
l=[]
flag=0
for i in str:
    if i.isdigit():
        l.append(i)
l=list(set(l))
l.sort(reverse=True)
num=''.join(l)
if int(num)%2==0:
    print(num)
else:
    for i in range(len(l)-1,0,-1):
        if (int(l[i])%2==0):
            flag=0
            temp=l[i]
            l[i]=l[-1]
            l[-1]=temp
            num=''.join(l)
            break
        else:
            flag=1
    if flag==1:
        print(-1)
    else:
        print(num)
            

        
