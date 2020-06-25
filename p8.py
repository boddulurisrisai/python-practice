from itertools import permutations
n=int(input())
l=input().split(' ')
for i in range(1,n+1):
    r=list(permutations(l,i))
print(r)
