import math
from itertools import combinations
l=list(input().split(','))
p=int(math.sqrt(len(l)))
b=[]
max=sum(list(map(int,l)))
for i in range(2,len(l)+1):
    a=list(combinations(l,i))
    for j in a:
        c=sum(list(map(int,j)))
        if c==max and len(j)==4:
            b.append(j)
b=set(b)
print(b)
            
            

    
