t=int(input())
a=[]
while(t>0):
    n=int(input())
    l=list(map(int,input().split()))
    p=set(l)
    d={}
    for i in p:
        d[i]=l.count(i)
    max=-1
    for i in d:
        if int(d[i])>max:
            max=int(i)
    if max>(n//2):
        a.append(max)
    else:
        a.append(-1)
    t-=1
print(*a,sep='\n')
