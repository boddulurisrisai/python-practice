from itertools import combinations
def prime(n,m):
    l=[]
    for i in range(n,m+1):
        flag=0
        q=i//2
        for j in range(2,q):
            if(i%j==0):
                flag=1
                break
        if flag==0:
            l.append(i)
    return l

l=[];e=[]
n,m=map(int,input().split())
l=prime(n,m)
for i in range(1,len(l)-1):
    for j in range(i+1,len(l)):
        w=l[i:j]
        if len(w)<=4 and len(w)>1:
            e.append(w)
for i in e:
    i=tuple(i)
    print(''.join(str(i)))


     
