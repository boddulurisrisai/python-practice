from itertools import permutations
l=list(map(int,input().split(',')))
r=list(permutations(l,3))
p=[]
r=set(r)
for i in r:
    a=list(i)
    s=''
    for j in range(len(a)):
        s+=str(a[j])
    p.append(int(s))
        
    

print(max(p),len(p),sep=',')
