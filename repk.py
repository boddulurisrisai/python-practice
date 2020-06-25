n=int(input())
l=list(map(int,input().split()))
k=int(input())
a=list(set(l))
d={};p=[]
for i in range(len(a)):
    d[a[i]]=l.count(a[i])
for i in d:
    if d[i]==k:
        p.append(i)
print(min(p))
    
    
