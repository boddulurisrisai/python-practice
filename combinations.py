from itertools import combinations
l=list(map(int,input().split()))
s=int(input())
count=0
r=list(combinations(l,4))
for i in r:
    p=list(i)
    if sum(p)==s:
        count+=1
print(count)
