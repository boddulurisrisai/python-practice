n=int(input())
l=list(map(int,input().split(',')))
l=list(set(l))
print(len(l)-n)
