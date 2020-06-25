from itertools import combinations
n=int(input())
l=list(map(int,input().split()))
r=list(combinations(l,n-1))
max=-1;min=10000
for i in r:
    a=sum(i)
    if a>max:
        max=a
    if a<min:
        min=a
print(max,min)

