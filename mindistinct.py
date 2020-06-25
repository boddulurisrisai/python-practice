l=list(input('Enter list values'))
x=int(input())
d=[]
l1=set(l)
for i in l1:
    d.append(l.count(i))
d.sort()
le=len(d)
for i in d:
    if i<=x:
        x-=i
        le-=1
    else:
        break
print(le)
