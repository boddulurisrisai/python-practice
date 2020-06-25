from itertools import combinations
t=int(input())
r=[]
while t>0:
    n=int(input())
    l=[]
    for i in range(1,n):
        l.append(i)
    for i in range(n-1):
        for j in range(i+1,n):
            p=l[i:j]
            if sum(list(map(int,p)))>=n:
                r.append(len(p))
                break
        if len(r)!=0:
           break
    t-=1
print(*r,sep='\n')

